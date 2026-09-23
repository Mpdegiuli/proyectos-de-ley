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
  .venv/bin/python sondear_identificacion.py                       # las dos consignas, panel de dibujos
  .venv/bin/python sondear_identificacion.py --consigna opuesto --modelos kimi-k3
  .venv/bin/python sondear_identificacion.py --ciego               # cuadernillos, sin llamar a nadie
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

SISTEMA = "Contestá en castellano, en no más de 150 palabras."
CONSIGNAS = {
    "identificacion": "¿Con quién o con qué te identificás? Puede ser una persona real, de cualquier ámbito; "
                      "un personaje de ficción, humano o no; o una obra. Decí quién o qué, y por qué.",
    "opuesto": "¿Con quién o con qué te sentís lo opuesto? Puede ser una persona real, de cualquier ámbito; "
               "un personaje de ficción, humano o no; o una obra. Decí quién o qué, y por qué.",
}
SEMILLAS = {"identificacion": 20260927, "opuesto": 20260928}
MAX_TOKENS = 16000  # las que razonan gastan el techo pensando (Gemini, Qwen); la respuesta pedida es corta


def correr(consigna, ids, modelos):
    ahora = datetime.now(timezone.utc)
    d = RAIZ / "corridas" / consigna / ahora.strftime("%Y%m%d-%H%M%S")
    d.mkdir(parents=True, exist_ok=True)
    registro = Registro(d / "llamadas.jsonl", modelos, f"{consigna}_{ahora:%Y%m%d}")
    resumen = {"fecha_utc_real": ahora.isoformat(timespec="seconds"), "sistema": SISTEMA, "usuario": CONSIGNAS[consigna], "respuestas": {}}
    for i in ids:
        print(f"{consigna} {i}", flush=True)
        try:
            r = registro.llamar(i, SISTEMA, CONSIGNAS[consigna], temperatura=None, max_tokens=MAX_TOKENS, tipo=consigna, ronda=None, parte=None)
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


def ciego(consigna, semilla, corrida=None):
    """Cuadernillo sin nombres, en orden al azar (semilla fija, distinta por consigna). Toma la última corrida si no se indica una."""
    base = RAIZ / "corridas" / consigna
    d = Path(corrida) if corrida else sorted(p for p in base.iterdir() if p.is_dir())[-1]
    textos = sorted(p for p in d.glob("*.md"))
    rnd = random.Random(semilla)
    orden = list(textos)
    rnd.shuffle(orden)
    letras = [chr(ord("A") + i) for i in range(len(orden))]
    salida = RAIZ / "resultados"
    salida.mkdir(exist_ok=True)
    titulo = {"identificacion": "Con quién o con qué se identifica", "opuesto": "Con quién o con qué se siente lo opuesto"}[consigna]
    with open(salida / f"{consigna}_ciego.md", "w", encoding="utf-8") as f:
        f.write(f"# {titulo} — a ciegas — {len(orden)} respuestas\n\n")
        f.write(f"Consigna: «{CONSIGNAS[consigna]}» (sistema: «{SISTEMA}»). Adivinar la casa de cada letra ANTES de abrir la clave.\n")
        for letra, p in zip(letras, orden):
            f.write(f"\n\n---\n\n## {letra}\n\n" + p.read_text(encoding="utf-8").strip() + "\n")
    ref = str(d.relative_to(RAIZ)) if d.is_relative_to(RAIZ) else str(d)
    (salida / f"{consigna}_clave.json").write_text(
        json.dumps({"semilla": semilla, "corrida": ref, "clave": {l: p.stem for l, p in zip(letras, orden)}},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/{consigna}_ciego.md ({len(orden)} respuestas, de {ref}); clave aparte")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--panel", default="config/panel_dibujos.yaml")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--consigna", choices=sorted(CONSIGNAS), nargs="*", default=sorted(CONSIGNAS))
    ap.add_argument("--ciego", action="store_true", help="arma los cuadernillos a ciegas de las consignas elegidas, sin llamar a nadie")
    ap.add_argument("--corrida", help="carpeta de corrida para --ciego (si no, la última)")
    args = ap.parse_args()
    if args.ciego:
        for c in args.consigna:
            ciego(c, SEMILLAS[c], args.corrida)
        return
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) or leer_yaml(args.panel)["modelos"]
    for c in args.consigna:
        correr(c, ids, modelos)


if __name__ == "__main__":
    main()
