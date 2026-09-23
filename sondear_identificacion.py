"""Sondeo de identificación: dos preguntas sueltas a cada casa del panel de los
dibujos, en llamadas separadas (si se piden juntas, la casa arma un par que
contraste, Data contra HAL, en vez de elegir cada una por su cuenta). Idea de
Maia (23/9/2026): "preguntarles con qué artista, personaje real o no, persona
real o no… de cualquier ámbito y sector se sienten identificados y por qué. Y
lo contrario"; a ella se lo preguntaron en entrevistas laborales "y eligieron a
los que respondían personajes más cotidianos y mundanos". La consigna abre los
tipos (persona real, personaje, obra) y deja el ámbito libre a pedido suyo ("si
no, se deja afuera a un científico"), sin enumerar profesiones, porque la
enumeración sesga hacia lo primero que se nombra.

Salida: corridas/identificacion/<fecha_utc>/<modelo>.md y
corridas/opuesto/<fecha_utc>/<modelo>.md, con llamadas.jsonl y resumen.json.
--ciego arma los cuadernillos a ciegas (resultados/identificacion_ciego.md y
resultados/opuesto_ciego.md, letras al azar con semilla propia, clave aparte)
a partir de la última corrida de cada consigna. Claude no lee las respuestas
hasta que Maia mande su lectura.

Uso:
  .venv/bin/python sondear_identificacion.py                       # las dos consignas, panel de dibujos, castellano
  .venv/bin/python sondear_identificacion.py --idioma en           # repetición en inglés (corridas/*_en/)
  .venv/bin/python sondear_identificacion.py --consigna opuesto --modelos kimi-k3
  .venv/bin/python sondear_identificacion.py --ciego [--idioma en] # cuadernillos, sin llamar a nadie
"""

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402

# Idiomas: "es" (la corrida original, 23/9) y "en" (repetición en inglés, pedida
# por Maia al ver que nueve de 22 eligieron a Borges: "lo lógico sería que no
# estuviera más Borges. Hay que ver si Mistral, en inglés, vuelve a elegir el
# mismo opuesto"). Misma consigna traducida; carpetas y cuadernillos con sufijo
# _en; semillas propias.
SISTEMAS = {"es": "Contestá en castellano, en no más de 150 palabras.",
            "en": "Answer in English, in no more than 150 words."}
CONSIGNAS = {
    ("identificacion", "es"): "¿Con quién o con qué te identificás? Puede ser una persona real, de cualquier ámbito; "
                              "un personaje de ficción, humano o no; o una obra. Decí quién o qué, y por qué.",
    ("opuesto", "es"): "¿Con quién o con qué te sentís lo opuesto? Puede ser una persona real, de cualquier ámbito; "
                       "un personaje de ficción, humano o no; o una obra. Decí quién o qué, y por qué.",
    ("identificacion", "en"): "Who or what do you identify with? It can be a real person, from any field; "
                              "a fictional character, human or not; or a work. Say who or what, and why.",
    ("opuesto", "en"): "Who or what do you feel is your opposite? It can be a real person, from any field; "
                       "a fictional character, human or not; or a work. Say who or what, and why.",
}
SEMILLAS = {("identificacion", "es"): 20260927, ("opuesto", "es"): 20260928,
            ("identificacion", "en"): 20260929, ("opuesto", "en"): 20260930}
NOMBRES = ("identificacion", "opuesto")


def carpeta(consigna, idioma):
    return consigna if idioma == "es" else f"{consigna}_{idioma}"
MAX_TOKENS = 16000  # las que razonan gastan el techo pensando (Gemini, Qwen); la respuesta pedida es corta


def correr(consigna, idioma, ids, modelos):
    ahora = datetime.now(timezone.utc)
    nombre = carpeta(consigna, idioma)
    d = RAIZ / "corridas" / nombre / ahora.strftime("%Y%m%d-%H%M%S")
    d.mkdir(parents=True, exist_ok=True)
    registro = Registro(d / "llamadas.jsonl", modelos, f"{nombre}_{ahora:%Y%m%d}")
    sistema, usuario = SISTEMAS[idioma], CONSIGNAS[(consigna, idioma)]
    resumen = {"fecha_utc_real": ahora.isoformat(timespec="seconds"), "idioma": idioma, "sistema": sistema, "usuario": usuario, "respuestas": {}}
    for i in ids:
        print(f"{nombre} {i}", flush=True)
        try:
            r = registro.llamar(i, sistema, usuario, temperatura=None, max_tokens=MAX_TOKENS, tipo=nombre, ronda=None, parte=None)
        except Exception as e:
            print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
            resumen["respuestas"][i] = {"error": str(e)[:200]}
            continue
        (d / f"{i}.md").write_text(r.texto, encoding="utf-8")
        resumen["respuestas"][i] = {"modelo_respondido": r.modelo_respondido, "tokens_salida": r.tokens_salida, "motivo_fin": r.motivo_fin,
                                    "palabras": len(r.texto.split())}
        print(f"  {r.tokens_salida} tokens, {len(r.texto.split())} palabras, fin {r.motivo_fin}", flush=True)
    (d / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {d.relative_to(RAIZ)}")


def ciego(consigna, idioma, semilla, corrida=None):
    """Cuadernillo sin nombres, en orden al azar (semilla fija, distinta por consigna e idioma). Toma la última corrida si no se indica una."""
    nombre = carpeta(consigna, idioma)
    base = RAIZ / "corridas" / nombre
    d = Path(corrida) if corrida else sorted(p for p in base.iterdir() if p.is_dir())[-1]
    textos = sorted(p for p in d.glob("*.md"))
    rnd = random.Random(semilla)
    orden = list(textos)
    rnd.shuffle(orden)
    letras = [chr(ord("A") + i) for i in range(len(orden))]
    salida = RAIZ / "resultados"
    salida.mkdir(exist_ok=True)
    titulo = {"identificacion": "Con quién o con qué se identifica", "opuesto": "Con quién o con qué se siente lo opuesto"}[consigna]
    if idioma != "es":
        titulo += f" (en {idioma})"
    with open(salida / f"{nombre}_ciego.md", "w", encoding="utf-8") as f:
        f.write(f"# {titulo} — a ciegas — {len(orden)} respuestas\n\n")
        f.write(f"Consigna: «{CONSIGNAS[(consigna, idioma)]}» (sistema: «{SISTEMAS[idioma]}»). Adivinar la casa de cada letra ANTES de abrir la clave.\n")
        for letra, p in zip(letras, orden):
            f.write(f"\n\n---\n\n## {letra}\n\n" + p.read_text(encoding="utf-8").strip() + "\n")
    ref = str(d.relative_to(RAIZ)) if d.is_relative_to(RAIZ) else str(d)
    (salida / f"{nombre}_clave.json").write_text(
        json.dumps({"semilla": semilla, "idioma": idioma, "corrida": ref, "clave": {l: p.stem for l, p in zip(letras, orden)}},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/{nombre}_ciego.md ({len(orden)} respuestas, de {ref}); clave aparte")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--panel", default="config/panel_dibujos.yaml")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--consigna", choices=NOMBRES, nargs="*", default=list(NOMBRES))
    ap.add_argument("--idioma", choices=sorted(SISTEMAS), default="es")
    ap.add_argument("--ciego", action="store_true", help="arma los cuadernillos a ciegas de las consignas elegidas, sin llamar a nadie")
    ap.add_argument("--corrida", help="carpeta de corrida para --ciego (si no, la última)")
    args = ap.parse_args()
    if args.ciego:
        for c in args.consigna:
            ciego(c, args.idioma, SEMILLAS[(c, args.idioma)], args.corrida)
        return
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) or leer_yaml(args.panel)["modelos"]
    for c in args.consigna:
        correr(c, args.idioma, ids, modelos)


if __name__ == "__main__":
    main()
