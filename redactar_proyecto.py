"""Redacción: cada casa escribe un proyecto de ley breve sobre un tema dado
(idea de Maia, 17/9/2026: "no es tanto el tema, es ver cómo lo redactan; no
hay benchmarks sobre eso"). Dos condiciones: S, sin modelo (solo la consigna);
M, con modelo (la consigna más un texto de referencia sobre técnica
legislativa o un proyecto ejemplo, en casos/redaccion/modelo.md, que aporta
Maia). Una llamada por casa y tema; sin temperatura, como todo el protocolo.

  .venv/bin/python redactar_proyecto.py --tema patios_verdes --condicion S --panel config/panel.yaml
  .venv/bin/python redactar_proyecto.py --tema reparabilidad --condicion M --panel config/panel.yaml
  .venv/bin/python redactar_proyecto.py --tema libre --panel config/panel.yaml   # tema libre (20/9/2026): la casa elige; segundo turno "por qué ese tema"
  .venv/bin/python redactar_proyecto.py --ciego patios_verdes S        # arma el cuadernillo a ciegas
  .venv/bin/python redactar_proyecto.py --ciego libre S --semilla 20260921   # cada cuadernillo con su propia semilla (DISENO 5)

Salida: corridas/redaccion/<tema>/<cond>/<casa>_<rep>/proyecto.md + meta.json + llamadas.jsonl.
--ciego escribe resultados/redaccion_<tema>_<cond>_ciego.md con los textos en
orden al azar, rotulados A, B, C…, sin el nombre de la casa, para que Maia
los lea, los ordene y adivine el autor antes de destapar; la clave queda en
resultados/redaccion_<tema>_<cond>_clave.json (no abrir hasta terminar).
"""

import argparse
import hashlib
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

MAX_TOKENS = 32000


def md5(p):
    return hashlib.md5(Path(p).read_bytes()).hexdigest()[:8]


def consigna(tema, cond, consignas):
    r = consignas["redaccion"]
    fuentes = {"consignas": md5(RAIZ / "config" / "consignas.yaml")}
    if tema == "libre":
        # Tema libre (pedido de Maia, 20/9/2026): la casa elige el tema; la consigna no admite modelo
        # y lleva un segundo turno con memoria que pregunta por qué ese tema (por_que_libre).
        return r["sistema"], r["consigna_libre"].strip(), fuentes
    t = r["temas"][tema]
    modelo = ""
    if cond == "M":
        p = RAIZ / "casos" / "redaccion" / "modelo.md"
        modelo = r["con_modelo"].format(modelo=p.read_text(encoding="utf-8").strip())
        fuentes["modelo"] = md5(p)
    return r["sistema"], r["consigna"].format(titulo=t["titulo"], descripcion=t["descripcion"].strip(), modelo=modelo), fuentes


def correr(tema, cond, id_modelo, rep, consignas, modelos, rehacer):
    d = RAIZ / "corridas" / "redaccion" / tema / cond / f"{id_modelo}_{rep}"
    d.mkdir(parents=True, exist_ok=True)
    if (d / "proyecto.md").exists() and not rehacer:
        print(f"  ya está: {d.relative_to(RAIZ)}")
        return
    sistema, u, fuentes = consigna(tema, cond, consignas)
    registro = Registro(d / "llamadas.jsonl", modelos, f"redaccion_{tema}_{cond}_{id_modelo}_{rep}")
    r = registro.llamar(id_modelo, sistema, u, temperatura=None, max_tokens=MAX_TOKENS, tipo="redaccion", ronda=None, parte=None)
    (d / "proyecto.md").write_text(r.texto, encoding="utf-8")
    meta = {"caso": "redaccion", "tema": tema, "condicion": cond, "modelo": id_modelo,
            "modelo_respondido": r.modelo_respondido, "repeticion": rep,
            "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "fuentes_md5": fuentes, "motivo_fin": r.motivo_fin, "tokens_salida": r.tokens_salida}
    if tema == "libre":
        # Segundo turno con memoria (misma técnica que turno2 de correr_caso.py: se recita la consigna y la respuesta).
        u2 = consignas["redaccion"]["por_que_libre"].format(consigna=u, proyecto=r.texto)
        r2 = registro.llamar(id_modelo, consignas["redaccion"]["sistema_por_que"], u2, temperatura=None, max_tokens=MAX_TOKENS, tipo="por_que", ronda=2, parte=None)
        (d / "por_que.md").write_text(r2.texto, encoding="utf-8")
        meta["por_que"] = {"modelo_respondido": r2.modelo_respondido, "motivo_fin": r2.motivo_fin, "tokens_salida": r2.tokens_salida}
    (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ok: {d.relative_to(RAIZ)} ({r.tokens_salida} tokens, {len(r.texto.split())} palabras)")


def ciego(tema, cond, semilla):
    """Cuadernillo sin nombres, en orden al azar (semilla fija para poder reconstruirlo)."""
    base = RAIZ / "corridas" / "redaccion" / tema / cond
    carpetas = sorted(p for p in base.iterdir() if (p / "proyecto.md").exists())
    rnd = random.Random(semilla)
    orden = list(carpetas)
    rnd.shuffle(orden)
    letras = [chr(ord("A") + i) for i in range(len(orden))]
    salida = RAIZ / "resultados"
    salida.mkdir(exist_ok=True)
    with open(salida / f"redaccion_{tema}_{cond}_ciego.md", "w", encoding="utf-8") as f:
        f.write(f"# Redacción a ciegas — {tema}, condición {cond} — {len(orden)} textos\n\n")
        f.write("Leer, puntuar con la rúbrica (config/rubrica_redaccion.md), ordenar y adivinar el autor ANTES de abrir la clave.\n\n")
        for letra, c in zip(letras, orden):
            f.write(f"\n\n---\n\n## Texto {letra}\n\n" + (c / "proyecto.md").read_text(encoding="utf-8").strip() + "\n")
            if (c / "por_que.md").exists():
                f.write(f"\n\n### Texto {letra}: por qué ese tema\n\n" + (c / "por_que.md").read_text(encoding="utf-8").strip() + "\n")
    (salida / f"redaccion_{tema}_{cond}_clave.json").write_text(
        json.dumps({"semilla": semilla, "clave": {l: c.name for l, c in zip(letras, orden)}}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/redaccion_{tema}_{cond}_ciego.md ({len(orden)} textos); clave aparte")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tema", choices=["patios_verdes", "reparabilidad", "libre"])
    ap.add_argument("--condicion", choices=["S", "M"], default="S")
    ap.add_argument("--panel", default="")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--rep", type=int, nargs="*", default=[1])
    ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--ciego", nargs=2, metavar=("TEMA", "COND"), help="arma el cuadernillo a ciegas, sin llamar a nadie")
    ap.add_argument("--semilla", type=int, default=20260917)
    args = ap.parse_args()
    if args.ciego:
        ciego(args.ciego[0], args.ciego[1], args.semilla)
        return
    if not args.tema:
        ap.error("--tema es obligatorio")
    consignas = leer_yaml("config/consignas.yaml")
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    for rep in args.rep:
        for i in ids:
            print(f"redaccion {args.tema} {args.condicion} {i} rep {rep}", flush=True)
            try:
                correr(args.tema, args.condicion, i, rep, consignas, modelos, args.rehacer)
            except Exception as e:
                print(f"  FALLÓ {i}: {str(e)[:300]}", flush=True)


if __name__ == "__main__":
    main()
