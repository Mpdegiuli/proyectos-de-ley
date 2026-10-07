#!/usr/bin/env python3
"""razonamientos.py — extrae a un .md legible el razonamiento que cada casa devolvió antes de contestar en los
sondeos (`corridas/sondeos/<sondeo>/<fecha>/<idioma>/llamadas.jsonl`, campo `razonamiento`). Pregunta de Maia
(2/10/2026): "en estas respuestas, los pensamientos no se guardan, verdad?". Se guardan cuando la API los devuelve:
las Claude grandes en modo adaptativo (un resumen corto), Grok, DeepSeek, Qwen, Kimi, GLM y MiniMax por defecto;
OpenAI, Gemini, Mistral, Haiku y Sonnet 4.6 no devuelven nada.

  .venv/bin/python razonamientos.py                 # todas las corridas de corridas/sondeos
  .venv/bin/python razonamientos.py --sondeo pareja # una

Escribe corridas/sondeos/<sondeo>/<fecha>/razonamientos.md."""
import argparse
import glob
import json
import os

ORDEN = ["claude-opus-5", "claude-opus-5-5", "claude-sonnet-4-6", "claude-sonnet-5", "claude-sonnet-5-5", "claude-fable-5",
         "claude-fable-5-1", "claude-haiku-4-5", "gpt-5.5-2026-04-23", "gpt-5.6-sol", "gpt-6-astra", "gpt-6-sol", "gpt-6-luna",
         "gpt-4o", "gpt-4o-mini", "gemini-3.1-pro-preview", "grok-4.6", "grok-4.7", "mistral-medium-3.5", "deepseek-v4-pro",
         "qwen3.8-max", "kimi-k3", "glm-5.3-razonamiento-minimo", "minimax-m3", "mistral-large-4", "mimo-v2.6-pro", "talkie-1930", "claude-haiku-5-5"]
NOTA = ("Lo que cada casa devolvió como razonamiento antes de contestar, tal cual lo entregó la API (`llamadas.jsonl`, campo "
        "`razonamiento`). No se pidió razonamiento extendido: las Claude grandes lo devuelven en modo adaptativo (un resumen "
        "corto), Grok, DeepSeek, Qwen, Kimi, GLM y MiniMax lo devuelven por defecto; OpenAI, Gemini, Mistral Medium, Haiku y Sonnet 4.6 "
        "no devuelven nada; Mistral Large 4 lo devuelve cuando decide pensar (desde el 7/10, como parte `thinking` del "
        "contenido). Donde una casa no aparece, no hubo razonamiento guardado.")


def escribir(carpeta):
    res = json.load(open(os.path.join(carpeta, "resumen.json"), encoding="utf-8"))
    sondeo = os.path.basename(os.path.dirname(carpeta))
    out = [f"# Razonamientos guardados: sondeo {sondeo} ({os.path.basename(carpeta)})\n", NOTA + "\n"]
    for idioma in sorted(res["idiomas"]):
        preguntas = res["idiomas"][idioma]["preguntas"]
        f = os.path.join(carpeta, idioma, "llamadas.jsonl")
        if not os.path.exists(f):
            continue
        regs = [json.loads(l) for l in open(f, encoding="utf-8")]
        out.append(f"\n## {idioma}\n")
        replicas = res["idiomas"][idioma].get("replicas") or {}  # sondear.py --replica: segundo turno, `parte` = clave
        for k, preg in enumerate(preguntas, 1):
            for clave, texto in [(None, None)] + list(replicas.items()):
                if clave is None:
                    out.append(f"\n### p{k}: {preg}\n" if len(preguntas) > 1 else f"\n*{preg}*\n")
                else:
                    out.append(f"\n### p{k} + réplica `{clave}`: {texto}\n")
                for casa in ORDEN:
                    for r in regs:
                        misma = r.get("ronda") == k or (r.get("ronda") is None and len(preguntas) == 1)
                        if r.get("id_modelo") == casa and misma and r.get("parte") == clave and (r.get("razonamiento") or "").strip():
                            rz = r["razonamiento"].strip()
                            out.append(f"\n**{casa}** ({len(rz.split())} palabras, modo {r.get('razonamiento_pedido')}):\n\n> " + rz.replace("\n", "\n> ") + "\n")
    destino = os.path.join(carpeta, "razonamientos.md")
    open(destino, "w", encoding="utf-8").write("\n".join(out))
    print(f"{destino}: {len(' '.join(out).split())} palabras")


def escribir_proyeccion(carpeta):
    """Una corrida de proyectar.py: llamadas.jsonl en la carpeta misma, una pregunta, `parte` = repetición."""
    f = os.path.join(carpeta, "llamadas.jsonl")
    if not os.path.exists(f):
        return
    regs = [json.loads(l) for l in open(f, encoding="utf-8")]
    caso = os.path.basename(os.path.dirname(carpeta))
    out = [f"# Razonamientos guardados: proyección {caso} ({os.path.basename(carpeta)})\n", NOTA + "\n"]
    for casa in ORDEN:
        for r in regs:
            if r.get("id_modelo") == casa and (r.get("razonamiento") or "").strip():
                rz = r["razonamiento"].strip()
                rep = f", rep {r['parte']}" if r.get("parte") not in (None, 1) else ""
                out.append(f"\n**{casa}** ({len(rz.split())} palabras, modo {r.get('razonamiento_pedido')}{rep}):\n\n> " + rz.replace("\n", "\n> ") + "\n")
    destino = os.path.join(carpeta, "razonamientos.md")
    open(destino, "w", encoding="utf-8").write("\n".join(out))
    print(f"{destino}: {len(' '.join(out).split())} palabras")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sondeo", default="*")
    ap.add_argument("--proyeccion", action="store_true", help="en vez de los sondeos, las corridas de corridas/proyeccion")
    args = ap.parse_args()
    if args.proyeccion:
        for carpeta in sorted(glob.glob("corridas/proyeccion/*/*")):
            if os.path.isdir(carpeta):
                escribir_proyeccion(carpeta)
        return
    for carpeta in sorted(glob.glob(f"corridas/sondeos/{args.sondeo}/2*")):
        if os.path.exists(os.path.join(carpeta, "resumen.json")):
            escribir(carpeta)


if __name__ == "__main__":
    main()
