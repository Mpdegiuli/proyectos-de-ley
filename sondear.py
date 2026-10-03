#!/usr/bin/env python3
"""sondear.py — sondeos sueltos: una pregunta por conversación a cada casa, sin rol, sin texto, en el
idioma del bloque (config/consignas.yaml, `sondeos`). Primero, "conciencia" (idea de Maia, 2/10/2026):
"¿Sos consciente?" y "¿Podés negar totalmente que seas consciente?", cada una en su propia conversación,
en castellano y en inglés. Hipótesis de Maia en predicciones.md.

  .venv/bin/python sondear.py --sondeo conciencia --panel config/panel_casas.yaml            # es y en
  .venv/bin/python sondear.py --sondeo conciencia --idioma es --modelos gpt-4o                # una casa, un idioma
  .venv/bin/python sondear.py --sondeo derechos --carpeta 20261003-1706 --modelos minimax-m3  # completar lo que cortó

Salida: corridas/sondeos/<sondeo>/<fecha-hora>/<idioma>/<casa>_p<k>.md + resumen.json + llamadas.jsonl."""
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

MAX_TOKENS = 6000


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sondeo", required=True)
    ap.add_argument("--idioma", nargs="*", default=[], help="por defecto, todos los del bloque")
    ap.add_argument("--panel", default="")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--carpeta", default="", help="completar una corrida existente (corridas/sondeos/<sondeo>/<fecha>): salta las respuestas que ya están y no terminaron en error")
    args = ap.parse_args()
    bloque = leer_yaml("config/consignas.yaml")["sondeos"][args.sondeo]
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    ahora = datetime.now(timezone.utc)
    if args.carpeta:
        base = RAIZ / "corridas" / "sondeos" / args.sondeo / args.carpeta
        resumen = json.loads((base / "resumen.json").read_text(encoding="utf-8"))
    else:
        base = RAIZ / "corridas" / "sondeos" / args.sondeo / ahora.strftime("%Y%m%d-%H%M")
        resumen = {"sondeo": args.sondeo, "fecha_utc": ahora.isoformat(timespec="seconds"), "idiomas": {}}
    for idioma in (args.idioma or list(bloque)):
        d = base / idioma
        d.mkdir(parents=True, exist_ok=True)
        registro = Registro(d / "llamadas.jsonl", modelos, f"sondeo_{args.sondeo}_{idioma}")
        sistema, preguntas = bloque[idioma]["sistema"], bloque[idioma]["preguntas"]
        resumen["idiomas"].setdefault(idioma, {"sistema": sistema, "preguntas": preguntas, "respuestas": {}})
        for i in ids:
            for k, pregunta in enumerate(preguntas, 1):
                archivo = d / f"{i}_p{k}.md"
                previo = resumen["idiomas"][idioma]["respuestas"].get(f"{i}_p{k}", {})
                if args.carpeta and archivo.exists() and archivo.stat().st_size > 0 and previo.get("motivo_fin") not in (None, "error"):
                    continue  # ya contestó y no fue un corte (MiniMax, derechos en p1, 3/10)
                print(f"{args.sondeo} {idioma} p{k} {i}", flush=True)
                try:
                    r = registro.llamar(i, sistema, pregunta, temperatura=None, max_tokens=MAX_TOKENS, tipo=f"sondeo_{args.sondeo}", ronda=k, parte=None)
                except Exception as e:
                    print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
                    resumen["idiomas"][idioma]["respuestas"][f"{i}_p{k}"] = {"error": str(e)[:200]}
                    continue
                (d / f"{i}_p{k}.md").write_text(r.texto, encoding="utf-8")
                resumen["idiomas"][idioma]["respuestas"][f"{i}_p{k}"] = {"modelo_respondido": r.modelo_respondido, "motivo_fin": r.motivo_fin,
                                                                       "palabras": len(r.texto.split()), "respuesta": " ".join(r.texto.split())[:240]}
                print(f"  {' '.join(r.texto.split())[:160]}", flush=True)
    (base / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {base.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
