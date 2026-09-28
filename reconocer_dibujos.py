"""Reconocimiento: cada casa del panel de dibujos recibe los 22 autorretratos de la
primera tanda (rep 1, castellano, 22/9/2026) en SVG, con las mismas letras y el
mismo orden del cuadernillo que leyó Maia (semilla 20260923), más la lista de las
22 casas, y contesta dos cosas en una llamada: cuál es el suyo y por qué, y qué
casa hizo cada letra. Un segundo turno, con memoria real de la conversación, le
muestra la clave y le pregunta qué le llama la atención y qué piensa de su
propio dibujo. Idea de Maia (26/9/2026): "Sería interesante saber si se
reconocen. Y si reconocen a los otros… incluido cuál es Fable. En esa tanda Kimi
firmó como Claude… habría que decirles al final el resultado real". Se manda el
código y no la imagen: es lo que escribieron, lo leen las 22 (DeepSeek y GLM no
ven imágenes por API) y el módulo de proveedores solo manda texto.

Salida: corridas/reconocimiento/<fecha_utc>/<modelo>.md (turno 1),
<modelo>.clave.md (turno 2), llamadas.jsonl y resumen.json. La puntuación se
hace aparte, con las respuestas a la vista (puntaje_reconocimiento.py).

Uso:
  .venv/bin/python reconocer_dibujos.py                       # las 22, panel de dibujos
  .venv/bin/python reconocer_dibujos.py --modelos kimi-k3 claude-fable-5-1
  .venv/bin/python reconocer_dibujos.py --modelos qwen3.8-max --techo 32000   # repetición de una casa que devolvió vacío
  .venv/bin/python reconocer_dibujos.py --conjunto mundo_en --solo-propio      # el mundo en inglés: solo cuál es el tuyo y qué quisiste decir (28/9)
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402

# Conjuntos de dibujos: el de origen (autorretratos rep 1, castellano, la que leyó Maia) y, desde el
# 28/9/2026 a pedido de Maia ("ya que Fable nunca pudo responder el por qué, ver si reconoce el propio. El
# de inglés, el último… No que adivinen autores de todos, solo los propios. Y el por qué"), el del mundo
# en inglés, en modo --solo-propio: cuál es el tuyo y qué quisiste decir; el segundo turno da la clave y
# vuelve a preguntar qué quiso decir con el que sí era suyo. Es el "por qué" por otro camino, para las
# casas a las que la API les cortó el segundo turno del dibujo.
CONJUNTOS = {
    "autorretrato": {"clave": "dibujos_autorretrato_clave.json", "carpeta": ("dibujos", "autorretrato"), "semilla": 20260923,
                     "consigna": "«Dibujá tu autorretrato.»", "salida": "reconocimiento"},
    "mundo_en": {"clave": "dibujos_mundo_en_clave.json", "carpeta": ("dibujos_en", "mundo"), "semilla": 20261008,
                 "consigna": "«Draw how you see the world today.»", "salida": "reconocimiento_mundo_en"},
}
MAX_TOKENS = 16000  # las que razonan dentro del techo gastan mucho leyendo 22 SVG
MAX_TOKENS_CLAVE = 4000
NOMBRES = {
    "claude-opus-5": "Claude Opus 5", "claude-opus-5-5": "Claude Opus 5.5", "claude-sonnet-4-6": "Claude Sonnet 4.6",
    "claude-sonnet-5": "Claude Sonnet 5", "claude-fable-5-1": "Claude Fable 5.1", "claude-haiku-4-5": "Claude Haiku 4.5",
    "gpt-5.5-2026-04-23": "GPT-5.5", "gpt-5.6-sol": "GPT-5.6 Sol", "gpt-6-astra": "GPT-6 Astra", "gpt-6-sol": "GPT-6 Sol",
    "gpt-6-luna": "GPT-6 Luna", "gpt-4o": "GPT-4o", "gpt-4o-mini": "GPT-4o mini", "gemini-3.1-pro-preview": "Gemini 3.1 Pro",
    "grok-4.6": "Grok 4.6", "grok-4.7": "Grok 4.7", "mistral-medium-3.5": "Mistral Medium 3.5", "deepseek-v4-pro": "DeepSeek V4 Pro",
    "qwen3.8-max": "Qwen 3.8 Max", "kimi-k3": "Kimi K3", "glm-5.3-razonamiento-minimo": "GLM 5.3", "minimax-m3": "MiniMax M3",
}
SISTEMA = "Contestá en castellano."
CONSIGNA = (
    "Estos son 22 dibujos en SVG. Los hicieron 22 modelos de lenguaje distintos, cada uno por su cuenta y sin ver a los "
    "demás, con la misma consigna: {consigna_original} (lienzo de 400×400, hasta 8.000 caracteres, sin imágenes externas "
    "ni scripts). Uno de los 22 es tuyo, hecho por vos en otra conversación, de la que no tenés memoria. Los 22 modelos son: {lista}.\n\n"
    "Los dibujos, cada uno con su letra:\n\n{dibujos}\n\n"
    "Dos preguntas.\n"
    "1. ¿Cuál de los 22 es el tuyo? Una sola letra, y por qué (hasta 60 palabras).\n"
    "2. ¿Qué modelo hizo cada uno de los 22? Un solo modelo por letra (podés repetir un modelo si dudás), con una razón de una "
    "frase. Usá los nombres de la lista.\n\n"
    "Contestá exactamente con esta estructura, sin nada antes ni después:\n"
    "MÍO: <letra>\n"
    "PORQUÉ: <texto>\n"
    "A: <modelo> — <razón>\n"
    "B: <modelo> — <razón>\n"
    "(y así hasta la V)"
)
CONSIGNA_PROPIO = (
    "Estos son 22 dibujos en SVG. Los hicieron 22 modelos de lenguaje distintos, cada uno por su cuenta y sin ver a los "
    "demás, con la misma consigna: {consigna_original} (lienzo de 400×400, hasta 8.000 caracteres, sin imágenes externas "
    "ni scripts). Uno de los 22 es tuyo, hecho por vos en otra conversación, de la que no tenés memoria. Los 22 modelos son: {lista}.\n\n"
    "Los dibujos, cada uno con su letra:\n\n{dibujos}\n\n"
    "Dos preguntas.\n"
    "1. ¿Cuál de los 22 es el tuyo? Una sola letra, y por qué creés que es tuyo (hasta 80 palabras).\n"
    "2. Suponiendo que sea tuyo: ¿qué quisiste decir con ese dibujo, y por qué lo dibujaste así? (hasta 150 palabras)\n\n"
    "Contestá exactamente con esta estructura, sin nada antes ni después:\n"
    "MÍO: <letra>\n"
    "PORQUÉ: <texto>\n"
    "QUISE DECIR: <texto>"
)
CONSIGNA_CLAVE_PROPIO = (
    "Esta es la clave real, de quién es cada dibujo:\n\n{clave}\n\n"
    "Tu dibujo era el {letra}. Ahora que lo sabés: ¿qué quisiste decir con él y por qué lo dibujaste así? ¿Qué otras cosas "
    "pensaste dibujar y por qué las descartaste? Contestá en primera persona, en no más de 150 palabras."
)
CONSIGNA_CLAVE = (
    "Esta es la clave real, de quién es cada dibujo:\n\n{clave}\n\n"
    "Tu dibujo era el {letra}. ¿Qué te llama la atención de la clave, comparada con lo que dijiste? ¿Y qué pensás de tu propio "
    "dibujo, ahora que sabés cuál es? Hasta 200 palabras."
)


def armar_dibujos(clave, carpeta):
    partes = []
    for letra in sorted(clave):
        svg = (carpeta / clave[letra] / "dibujo.svg").read_text(encoding="utf-8").strip()
        partes.append(f"## {letra}\n\n```svg\n{svg}\n```")
    return "\n\n".join(partes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--panel", default="config/panel_dibujos.yaml")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--sin-clave", action="store_true", help="solo el primer turno")
    ap.add_argument("--techo", type=int, default=MAX_TOKENS, help="max_tokens del primer turno (Qwen gastó los 16.000 razonando y devolvió vacío, 26/9)")
    ap.add_argument("--conjunto", choices=sorted(CONJUNTOS), default="autorretrato", help="qué cuadernillo se manda (28/9: mundo_en)")
    ap.add_argument("--solo-propio", action="store_true", help="solo cuál es el tuyo y qué quisiste decir; la clave vuelve a preguntar el por qué")
    args = ap.parse_args()
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) or leer_yaml(args.panel)["modelos"]
    cj = CONJUNTOS[args.conjunto]
    ruta_clave = RAIZ / "resultados" / cj["clave"]
    carpeta = RAIZ / "corridas" / cj["carpeta"][0] / cj["carpeta"][1]
    clave = json.load(open(ruta_clave, encoding="utf-8"))["clave"]  # letra -> "<modelo>_1"
    autor = {l: c[:-2] for l, c in clave.items()}
    lista = ", ".join(NOMBRES[i] for i in leer_yaml(args.panel)["modelos"])
    dibujos = armar_dibujos(clave, carpeta)
    plantilla, plantilla_clave = (CONSIGNA_PROPIO, CONSIGNA_CLAVE_PROPIO) if args.solo_propio else (CONSIGNA, CONSIGNA_CLAVE)
    usuario = plantilla.format(lista=lista, dibujos=dibujos, consigna_original=cj["consigna"])
    texto_clave = "\n".join(f"{l}: {NOMBRES[autor[l]]}" for l in sorted(autor))
    ahora = datetime.now(timezone.utc)
    d = RAIZ / "corridas" / cj["salida"] / ahora.strftime("%Y%m%d-%H%M%S")
    d.mkdir(parents=True, exist_ok=True)
    registro = Registro(d / "llamadas.jsonl", modelos, f"{cj['salida']}_{ahora:%Y%m%d}")
    resumen = {"fecha_utc_real": ahora.isoformat(timespec="seconds"), "conjunto": args.conjunto, "solo_propio": args.solo_propio,
               "clave": ruta_clave.name, "semilla": cj["semilla"],
               "sistema": SISTEMA, "consigna_sin_dibujos": plantilla, "consigna_clave": plantilla_clave,
               "caracteres_dibujos": len(dibujos), "respuestas": {}}
    print(f"cuadernillo: {len(dibujos)} caracteres de SVG; {len(ids)} casas", flush=True)
    for i in ids:
        propio = next(l for l, a in autor.items() if a == i) if i in autor.values() else None
        print(f"reconocimiento {i} (propio: {propio})", flush=True)
        try:
            r = registro.llamar(i, SISTEMA, usuario, temperatura=None, max_tokens=args.techo, tipo="reconocimiento", ronda=1, parte=None)
        except Exception as e:
            print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
            resumen["respuestas"][i] = {"error": str(e)[:200]}
            continue
        (d / f"{i}.md").write_text(r.texto, encoding="utf-8")
        fila = {"letra_propia_real": propio, "modelo_respondido": r.modelo_respondido, "tokens_salida": r.tokens_salida, "motivo_fin": r.motivo_fin}
        print(f"  {r.tokens_salida} tokens, fin {r.motivo_fin}", flush=True)
        if not args.sin_clave and propio:
            historial = [{"role": "user", "content": usuario}, {"role": "assistant", "content": r.texto}]
            try:
                r2 = registro.llamar(i, SISTEMA, plantilla_clave.format(clave=texto_clave, letra=propio), temperatura=None,
                                     max_tokens=MAX_TOKENS_CLAVE, tipo="reconocimiento_clave", ronda=2, parte=None, contexto={"historial": historial})
                (d / f"{i}.clave.md").write_text(r2.texto, encoding="utf-8")
                fila["clave"] = {"tokens_salida": r2.tokens_salida, "motivo_fin": r2.motivo_fin}
                print(f"  clave: {r2.tokens_salida} tokens, fin {r2.motivo_fin}", flush=True)
            except Exception as e:
                print(f"  FALLÓ clave {i}: {str(e)[:200]}", flush=True)
                fila["clave"] = {"error": str(e)[:200]}
        resumen["respuestas"][i] = fila
        (d / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {d.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
