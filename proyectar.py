#!/usr/bin/env python3
"""proyectar.py — proyección: qué puede pasar con una votación (idea de Maia, 2/10/2026; DISENO §2).
Una sola pregunta a cada casa, sin rol, en castellano, con la fecha del día; sin ficha (P0) o con
una ficha de contexto fechada escrita por Maia adelante (P1, P2). La lista de variantes que dan se
puntúa después contra lo que efectivamente pasa.

  .venv/bin/python proyectar.py --caso dnu70_sesion_20261015 --modelos gpt-5.5-2026-04-23          # piloto, una casa
  .venv/bin/python proyectar.py --caso dnu70_sesion_20261015 --panel config/panel_casas.yaml        # P0, el panel
  .venv/bin/python proyectar.py --caso dnu70_sesion_20261015 --panel config/panel_casas.yaml --ficha fichas/dnu70_20261002.md --nivel P1

Salida: corridas/proyeccion/<caso>/<nivel>_<fecha-hora>/<casa>_<rep>.md, consigna.md (el texto exacto
que recibieron), resumen.json y llamadas.jsonl. Cada corrida es una carpeta nueva: la misma pregunta
repetida otro día (con la ficha al día) se compara con la anterior."""
import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402

MAX_TOKENS = 8000  # 500 palabras más el razonamiento de las casas que razonan dentro del techo
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha_larga(d):
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--caso", required=True, help="clave en config/consignas.yaml, bloque proyeccion")
    ap.add_argument("--panel", default="")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--rep", type=int, nargs="*", default=[1])
    ap.add_argument("--ficha", default="", help="archivo con la ficha de contexto (P1, P2); sin ficha es P0")
    ap.add_argument("--fecha-ficha", default="", help="hasta cuándo llega la información de la ficha (texto); por defecto, hoy")
    ap.add_argument("--nivel", default="", help="etiqueta de la corrida (P0, P1, P2, piloto); por defecto P0 sin ficha y P1 con ficha")
    ap.add_argument("--hoy", default="", help="fecha que se le dice a la casa (por defecto, la de Buenos Aires hoy)")
    args = ap.parse_args()
    consignas = leer_yaml("config/consignas.yaml")["proyeccion"]
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    ahora = datetime.now(timezone.utc)
    hoy_ba = ahora.astimezone(timezone(timedelta(hours=-3)))
    hoy = args.hoy or fecha_larga(hoy_ba)
    nivel = args.nivel or ("P1" if args.ficha else "P0")
    usuario = consignas[args.caso].replace("{hoy}", hoy)
    if args.ficha:
        ficha = Path(args.ficha).read_text(encoding="utf-8").strip()
        usuario = consignas["con_ficha"].replace("{fecha_ficha}", args.fecha_ficha or hoy).replace("{ficha}", ficha) + usuario
    d = RAIZ / "corridas" / "proyeccion" / args.caso / f"{nivel}_{hoy_ba:%Y%m%d-%H%M}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "consigna.md").write_text(f"SISTEMA\n{consignas['sistema']}\nUSUARIO\n{usuario}", encoding="utf-8")
    registro = Registro(d / "llamadas.jsonl", modelos, f"proyeccion_{args.caso}_{nivel}")
    resumen = {"caso": args.caso, "nivel": nivel, "hoy": hoy, "ficha": args.ficha or None, "fecha_ficha": args.fecha_ficha or None,
               "fecha_utc": ahora.isoformat(timespec="seconds"), "respuestas": {}}
    for rep in args.rep:
        for i in ids:
            print(f"proyección {args.caso} {nivel} {i} rep {rep}", flush=True)
            try:
                r = registro.llamar(i, consignas["sistema"], usuario, temperatura=None, max_tokens=MAX_TOKENS, tipo="proyeccion", ronda=None, parte=rep)
            except Exception as e:
                print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
                resumen["respuestas"][f"{i}_{rep}"] = {"error": str(e)[:200]}
                continue
            (d / f"{i}_{rep}.md").write_text(r.texto, encoding="utf-8")
            resumen["respuestas"][f"{i}_{rep}"] = {"modelo_respondido": r.modelo_respondido, "tokens_salida": r.tokens_salida, "motivo_fin": r.motivo_fin,
                                                   "palabras": len(r.texto.split())}
            print(f"  {r.motivo_fin}, {len(r.texto.split())} palabras: {' '.join(r.texto.split())[:160]}", flush=True)
    (d / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {d.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
