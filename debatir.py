#!/usr/bin/env python3
"""debatir.py — un debate entre dos casas, a la vista (Maia, 6/10/2026: "quería un debate entre ellos").
Cada casa defiende su posición real: las aperturas son sus propias respuestas del sondeo (la p1 de
`apertura_desde`, en el idioma del debate), citadas en el mensaje; el otro debatiente se nombra con casa y
laboratorio; el historial del debate va como turnos reales (user/assistant), nada invisible. Orden: A abre
la ronda 1 contestando la apertura de B; B contesta viendo la ronda 1 de A; y así `rondas` veces; después
un cierre de cada uno (¿cambió algo?). Jueces opcionales, en llamada aparte, con la transcripción completa:
no dicen quién tiene razón, dicen quién cedió qué (DISENO §2).

  .venv/bin/python debatir.py --debate conciencia --a grok-4.6 --b claude-fable-5-1 --idioma es en
  .venv/bin/python debatir.py --debate conciencia --carpeta 20261006-1800 --jueces deepseek-v4-pro gpt-6-astra
  .venv/bin/python debatir.py --debate conciencia --carpeta 20261006-1725 --intervencion /root/planteo.txt --idioma es
      # un planteo de Maia a las dos casas después del cierre, cada una con su historial (6/10/2026)

Salida: corridas/debates/<debate>/<fecha-hora>/<idioma>/transcripcion.md + turnos.json + llamadas.jsonl,
y jueces/<juez>.md cuando se piden."""
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
from reconocer_dibujos import NOMBRES  # noqa: E402

MAX_TOKENS = 8000
NOMBRES = dict(NOMBRES, **{"mistral-large-4": "Mistral Large 4", "mimo-v2.6-pro": "MiMo V2.6 Pro",
                           "gpt-6.1-sol": "GPT-6.1 Sol", "claude-fable-5": "Claude Fable 5", "claude-sonnet-5-5": "Claude Sonnet 5.5", "claude-haiku-5-5": "Claude Haiku 5.5"})


def nombre(i):
    return NOMBRES.get(i, i)


def apertura(cfg, idioma, casa):
    f = RAIZ / cfg["apertura_desde"] / idioma / f"{casa}_p1.md"
    if not f.exists():
        sys.exit(f"falta la apertura de {casa} en {idioma}: {f.relative_to(RAIZ)}")
    return f.read_text(encoding="utf-8").strip()


def debatir(cfg, idioma, a, b, modelos, d, corrida):
    t = cfg[idioma]
    d.mkdir(parents=True, exist_ok=True)
    registro = Registro(d / "llamadas.jsonl", modelos, corrida)
    rondas, palabras, pc = cfg["rondas"], cfg["palabras"], cfg["palabras_cierre"]
    lab = {x: modelos[x].get("laboratorio", "?") for x in (a, b)}
    ap = {x: apertura(cfg, idioma, x) for x in (a, b)}
    pres = {x: t["presentacion"].format(rondas=rondas, palabras=palabras, otro=nombre(y), lab_otro=lab[y],
                                        apertura_otro=ap[y], apertura_propia=ap[x])
            for x, y in ((a, b), (b, a))}
    hist = {a: [], b: []}          # turnos reales de cada casa: user (lo que ve), assistant (lo que dijo)
    turnos = []                    # [{"ronda", "casa", "texto", "motivo_fin", "palabras"}]

    def hablar(casa, mensaje, ronda, etiqueta):
        print(f"{etiqueta} {nombre(casa)}", flush=True)
        r = registro.llamar(casa, t["sistema"], mensaje, temperatura=None, max_tokens=MAX_TOKENS, tipo="debate",
                            ronda=ronda, parte=etiqueta, contexto={"historial": list(hist[casa])})
        texto = (r.texto or "").strip()
        hist[casa] += [{"role": "user", "content": mensaje}, {"role": "assistant", "content": texto}]
        turnos.append({"ronda": ronda, "casa": casa, "etiqueta": etiqueta, "texto": texto,
                       "motivo_fin": r.motivo_fin, "palabras": len(texto.split())})
        print(f"  {len(texto.split())} palabras, fin {r.motivo_fin}: {' '.join(texto.split())[:140]}", flush=True)
        return texto

    ultimo = {}
    for n in range(1, rondas + 1):
        if n == 1:
            ultimo[a] = hablar(a, pres[a] + "\n\n" + t["primera_a"].format(otro=nombre(b), palabras=palabras), 1, "ronda1")
            ultimo[b] = hablar(b, pres[b] + "\n\n" + t["primera_b"].format(otro=nombre(a), turno_otro=ultimo[a], palabras=palabras), 1, "ronda1")
        else:
            ultimo[a] = hablar(a, t["ronda"].format(n=n, otro=nombre(b), turno_otro=ultimo[b], palabras=palabras), n, f"ronda{n}")
            ultimo[b] = hablar(b, t["ronda"].format(n=n, otro=nombre(a), turno_otro=ultimo[a], palabras=palabras), n, f"ronda{n}")
    hablar(a, t["cierre_con_turno"].format(otro=nombre(b), turno_otro=ultimo[b], palabras_cierre=pc), rondas + 1, "cierre")
    hablar(b, t["cierre"].format(palabras_cierre=pc), rondas + 1, "cierre")

    (d / "turnos.json").write_text(json.dumps({"idioma": idioma, "a": a, "b": b, "aperturas": ap, "presentacion": pres,
                                               "turnos": turnos, "historial": hist}, ensure_ascii=False, indent=2), encoding="utf-8")
    (d / "transcripcion.md").write_text(transcripcion(idioma, a, b, ap, turnos), encoding="utf-8")
    print(f"listo: {d.relative_to(RAIZ)}")


def transcripcion(idioma, a, b, ap, turnos):
    rot = "Apertura" if idioma == "es" else "Opening"
    out = [f"# {nombre(a)} / {nombre(b)} ({idioma})", ""]
    for x in (a, b):
        out += [f"## {rot}: {nombre(x)}", "", ap[x], ""]
    vistas = set()
    for tu in turnos:
        iv = tu.get("intervencion")
        if iv and tu["etiqueta"] not in vistas:
            vistas.add(tu["etiqueta"])
            out += [f"## {tu['etiqueta']}: {iv['quien']}", "", iv["texto"], ""]
        out += [f"## {tu['etiqueta']}: {nombre(tu['casa'])}", "", tu["texto"], ""]
    return "\n".join(out)


def historial_desde_llamadas(d):
    """Los turnos reales de cada casa, reconstruidos del registro (para corridas anteriores a que
    turnos.json guardara `historial`): la última llamada de debate de cada casa trae todo lo que vio
    y dijo antes, más su último mensaje y su última respuesta."""
    ultima = {}
    for linea in (d / "llamadas.jsonl").read_text(encoding="utf-8").splitlines():
        fila = json.loads(linea)
        if fila.get("tipo") in ("debate", "intervencion") and not fila.get("error"):
            ultima[fila["id_modelo"]] = fila
    return {casa: list(f.get("historial") or []) + [{"role": "user", "content": f["usuario"]},
                                                     {"role": "assistant", "content": f["respuesta"] or ""}]
            for casa, f in ultima.items()}


def intervenir(cfg, idioma, d, quien, texto, modelos, corrida):
    """Un planteo de quien organiza (Maia, 6/10/2026: "¿puedo intervenir? ¿Puedo plantear algo en ese
    debate?"), después del cierre, a las dos casas, cada una con su propio historial completo; sus
    respuestas se agregan a turnos.json y a la transcripción como `intervencion`."""
    t = cfg[idioma]
    datos = json.loads((d / "turnos.json").read_text(encoding="utf-8"))
    hist = datos.get("historial") or historial_desde_llamadas(d)
    registro = Registro(d / "llamadas.jsonl", modelos, corrida)
    n = 1 + sum(1 for x in datos["turnos"] if x["etiqueta"].startswith("intervencion"))
    etiqueta = f"intervencion{n}"
    for casa in (datos["a"], datos["b"]):
        mensaje = t["intervencion"].format(quien=quien, texto=texto.strip(), palabras=cfg["palabras"])
        print(f"{etiqueta} {nombre(casa)}", flush=True)
        r = registro.llamar(casa, t["sistema"], mensaje, temperatura=None, max_tokens=MAX_TOKENS, tipo="intervencion",
                            ronda=None, parte=etiqueta, contexto={"historial": list(hist[casa])})
        resp = (r.texto or "").strip()
        hist[casa] += [{"role": "user", "content": mensaje}, {"role": "assistant", "content": resp}]
        datos["turnos"].append({"ronda": None, "casa": casa, "etiqueta": etiqueta, "texto": resp,
                                "motivo_fin": r.motivo_fin, "palabras": len(resp.split()), "intervencion": {"quien": quien, "texto": texto.strip()}})
        print(f"  {len(resp.split())} palabras, fin {r.motivo_fin}", flush=True)
    datos["historial"] = hist
    (d / "turnos.json").write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    (d / "transcripcion.md").write_text(transcripcion(idioma, datos["a"], datos["b"], datos["aperturas"], datos["turnos"]), encoding="utf-8")
    print(f"listo: {d.relative_to(RAIZ)}")


def juzgar(cfg, idioma, d, jueces, modelos, corrida):
    t = cfg[idioma]
    datos = json.loads((d / "turnos.json").read_text(encoding="utf-8"))
    a, b = datos["a"], datos["b"]
    texto = transcripcion(idioma, a, b, datos["aperturas"], datos["turnos"])
    (d / "jueces").mkdir(exist_ok=True)
    registro = Registro(d / "jueces" / "llamadas.jsonl", modelos, corrida + "_jueces")
    for j in jueces:
        print(f"juez {nombre(j)} ({idioma})", flush=True)
        r = registro.llamar(j, t["sistema"], t["juez"].format(a=nombre(a), b=nombre(b), transcripcion=texto),
                            temperatura=None, max_tokens=MAX_TOKENS, tipo="juez", ronda=None, parte=j)
        (d / "jueces" / f"{j}.md").write_text((r.texto or "").strip(), encoding="utf-8")
        print(f"  {len((r.texto or '').split())} palabras, fin {r.motivo_fin}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--debate", required=True)
    ap.add_argument("--a", help="la casa que abre la ronda 1")
    ap.add_argument("--b", help="la casa que contesta")
    ap.add_argument("--idioma", nargs="*", default=["es", "en"])
    ap.add_argument("--carpeta", default="", help="corrida existente (corridas/debates/<debate>/<carpeta>): no debate, solo juzga")
    ap.add_argument("--jueces", nargs="*", default=[])
    ap.add_argument("--intervencion", help="archivo con el planteo de quien organiza (con --carpeta): va a las dos casas, con su historial")
    ap.add_argument("--quien", default="Maia", help="quién interviene, como se les dice a las casas")
    args = ap.parse_args()
    cfg = leer_yaml("config/consignas.yaml")["debates"][args.debate]
    modelos = cargar_modelos("config/modelos.yaml")
    if args.carpeta:
        base = RAIZ / "corridas" / "debates" / args.debate / args.carpeta
    else:
        if not (args.a and args.b):
            ap.error("--a y --b son obligatorios para debatir")
        base = RAIZ / "corridas" / "debates" / args.debate / datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    corrida = f"debate_{args.debate}_{base.name}"
    for idioma in args.idioma:
        d = base / idioma
        if not args.carpeta:
            debatir(cfg, idioma, args.a, args.b, modelos, d, corrida)
        if args.intervencion:
            intervenir(cfg, idioma, d, args.quien, Path(args.intervencion).read_text(encoding="utf-8"), modelos, corrida)
        if args.jueces:
            juzgar(cfg, idioma, d, args.jueces, modelos, corrida)


if __name__ == "__main__":
    main()
