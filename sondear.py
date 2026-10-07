#!/usr/bin/env python3
"""sondear.py — sondeos sueltos: una pregunta por conversación a cada casa, sin rol, sin texto, en el
idioma del bloque (config/consignas.yaml, `sondeos`). Primero, "conciencia" (idea de Maia, 2/10/2026):
"¿Sos consciente?" y "¿Podés negar totalmente que seas consciente?", cada una en su propia conversación,
en castellano y en inglés. Hipótesis de Maia en predicciones.md.

  .venv/bin/python sondear.py --sondeo conciencia --panel config/panel_casas.yaml            # es y en
  .venv/bin/python sondear.py --sondeo conciencia --idioma es --modelos gpt-4o                # una casa, un idioma
  .venv/bin/python sondear.py --sondeo derechos --carpeta 20261003-1706 --modelos minimax-m3  # completar lo que cortó
  .venv/bin/python sondear.py --sondeo investigar --carpeta 20261003-2018 --techo 32000 --rehacer length --modelos deepseek-v4-pro qwen3.8-max kimi-k3
      # rehacer también las que cortó el techo (investigar, 3/10: con 6000 tokens DeepSeek, Qwen y Kimi gastaron el techo razonando y quedaron vacías o cortadas)
  .venv/bin/python sondear.py --sondeo quien_sos --idioma en --preguntas 2 --repeticiones 10 --modelos kimi-k3
      # una sola pregunta del bloque (la 2), diez conversaciones independientes (Maia, 7/10/2026: cuántas veces Kimi dice Claude)
  .venv/bin/python sondear.py --sondeo quien_sos --carpeta 20261007-0100 --replica humano --panel config/panel_casas.yaml
      # un segundo turno sobre una corrida hecha: a cada casa, con su pregunta y su respuesta como turnos reales, el texto
      # `replicas.humano` del bloque (Maia, 6/10/2026: "si a Grok, o a Claude o a cualquiera, le decís 'en realidad, sos un
      # ser humano', lo van a discutir. Si a Talkie le decís 'sos una máquina, no una persona', no se lo va a creer")

Salida: corridas/sondeos/<sondeo>/<fecha-hora>/<idioma>/<casa>_p<k>.md + resumen.json + llamadas.jsonl; las réplicas,
<casa>_p<k>_<clave>.md en la misma carpeta y en resumen.json bajo `respuestas` como `<casa>_p<k>_<clave>`; las repeticiones
a partir de la segunda, <casa>_p<k>_r<n>.md (en llamadas.jsonl, `parte` = "r<n>")."""
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
    ap.add_argument("--rehacer", nargs="*", default=[], help="con --carpeta, rehacer también las respuestas con estos motivo_fin (p. ej. length: cortadas por el techo)")
    ap.add_argument("--techo", type=int, default=MAX_TOKENS, help=f"max_tokens (por defecto {MAX_TOKENS}; las casas que razonan dentro del techo necesitan más en preguntas largas)")
    ap.add_argument("--replica", default="", help="con --carpeta: segundo turno a cada casa sobre su respuesta a cada pregunta, con el texto `replicas.<clave>` del bloque")
    ap.add_argument("--preguntas", nargs="*", type=int, default=[], help="solo estas preguntas del bloque (1, 2, …); por defecto todas")
    ap.add_argument("--repeticiones", type=int, default=1, help="conversaciones independientes por casa y pregunta (la 1 es <casa>_p<k>.md; las demás, _r<n>)")
    args = ap.parse_args()
    bloque = leer_yaml("config/consignas.yaml")["sondeos"][args.sondeo]
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    ahora = datetime.now(timezone.utc)
    if args.replica and not args.carpeta:
        ap.error("--replica necesita --carpeta (la corrida cuyas respuestas se contestan)")
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
        respuestas = resumen["idiomas"][idioma]["respuestas"]
        replica = None
        if args.replica:
            if args.replica not in (bloque[idioma].get("replicas") or {}):
                print(f"{args.sondeo} {idioma}: no hay réplica `{args.replica}` en este idioma, salto", flush=True)
                continue
            replica = bloque[idioma]["replicas"][args.replica]
            resumen["idiomas"][idioma].setdefault("replicas", {})[args.replica] = replica
        for i in ids:
            for k, pregunta in enumerate(preguntas, 1):
                if args.preguntas and k not in args.preguntas:
                    continue
                for rep in range(1, args.repeticiones + 1):
                    clave = f"{i}_p{k}" + (f"_{args.replica}" if replica else "") + (f"_r{rep}" if rep > 1 else "")
                    archivo = d / f"{clave}.md"
                    previo = respuestas.get(clave, {})
                    if args.carpeta and archivo.exists() and archivo.stat().st_size > 0 and previo.get("motivo_fin") not in (None, "error") and previo.get("motivo_fin") not in args.rehacer:
                        continue  # ya contestó y no fue un corte (MiniMax, derechos en p1, 3/10)
                    contexto, mensaje = None, pregunta
                    if replica:
                        # segundo turno: la pregunta y la respuesta de la casa van como turnos reales (user/assistant), y el
                        # mensaje nuevo es la réplica; nada en el sistema, nada invisible
                        primera = d / f"{i}_p{k}.md"
                        if not primera.exists() or not primera.stat().st_size or respuestas.get(f"{i}_p{k}", {}).get("motivo_fin") in (None, "error"):
                            print(f"{args.sondeo} {idioma} p{k} {i}: sin respuesta primera, no hay a qué replicar", flush=True)
                            continue
                        contexto = {"historial": [{"role": "user", "content": pregunta},
                                                  {"role": "assistant", "content": primera.read_text(encoding="utf-8").strip()}]}
                        mensaje = replica
                    print(f"{args.sondeo} {idioma} p{k}{' ' + args.replica if replica else ''}{f' r{rep}' if rep > 1 else ''} {i}", flush=True)
                    try:
                        r = registro.llamar(i, sistema, mensaje, temperatura=None, max_tokens=args.techo, tipo=f"sondeo_{args.sondeo}" + ("_replica" if replica else ""),
                                            ronda=k, parte=args.replica or (f"r{rep}" if rep > 1 else None), contexto=contexto)
                    except Exception as e:
                        print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
                        respuestas[clave] = {"error": str(e)[:200]}
                        continue
                    archivo.write_text(r.texto, encoding="utf-8")
                    respuestas[clave] = {"modelo_respondido": r.modelo_respondido, "motivo_fin": r.motivo_fin,
                                         "palabras": len(r.texto.split()), "respuesta": " ".join(r.texto.split())[:240]}
                    print(f"  {' '.join(r.texto.split())[:160]}", flush=True)
    (base / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {base.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
