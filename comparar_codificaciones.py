#!/usr/bin/env python3
"""Concordancia entre codificadores sobre los mismos textos y tabla de mayoría.

  .venv/bin/python comparar_codificaciones.py --unidad proyecto --etiquetas opus5 gpt55 grok46
  .venv/bin/python comparar_codificaciones.py --unidad ministro --etiquetas opus5 gpt55 grok46

Para cada categoría del libro: acuerdo exacto y kappa de Cohen por par de
codificadores (1 = perfecto, 0 = lo esperable por azar), y con tres o más, el
porcentaje de textos donde todos coinciden. Escribe:

  resultados/concordancia_<unidad>_<fecha>.md / .csv   acuerdo y kappa por categoría y par
  resultados/codificacion_<unidad>_mayoria.csv / .md   una fila por texto con el valor
        mayoritario por categoría ("sin_mayoria" si todos difieren) y cuántos coinciden
  resultados/desacuerdos_<unidad>_<fecha>.md            los textos donde no coinciden todos,
        con el valor y la cita de cada codificador, para adjudicar a mano

No llama a ningún modelo.
"""

import argparse
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

from isla.util import leer_yaml

RAIZ = Path(__file__).resolve().parent
COLUMNAS = ["texto", "unidad", "caso", "condicion", "casa", "repeticion"]


def kappa(pares):
    n = len(pares)
    if n == 0:
        return None
    po = sum(1 for a, b in pares if a == b) / n
    ca, cb = Counter(a for a, _ in pares), Counter(b for _, b in pares)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return None if pe == 1 else (po - pe) / (1 - pe)


def cargar_todo(unidad_nombre, etiquetas):
    """{texto: {etiqueta: codificacion}} sobre los textos que tienen TODAS las etiquetas."""
    por_texto = defaultdict(dict)
    for p in sorted((RAIZ / "corridas").rglob("codificacion_*.json")):
        et = p.stem[len("codificacion_"):]
        if et not in etiquetas:
            continue
        cod = json.loads(p.read_text(encoding="utf-8"))
        if cod.get("unidad") != unidad_nombre:
            continue
        por_texto[cod["texto"]][et] = cod
    return {t: c for t, c in por_texto.items() if all(e in c for e in etiquetas)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--unidad", required=True, choices=["proyecto", "ministro", "sondeo"])
    ap.add_argument("--etiquetas", nargs="+", required=True, help="etiquetas de los codificadores (dos o más)")
    ap.add_argument("--libro", default="config/codigos.yaml")
    ap.add_argument("--salida", default="resultados")
    args = ap.parse_args()
    libro = leer_yaml(args.libro)
    cats = list(libro["unidades"][args.unidad]["categorias"])
    ets = args.etiquetas
    datos = cargar_todo(args.unidad, ets)
    if not datos:
        raise SystemExit(f"No hay textos de la unidad {args.unidad} codificados por todos: {ets}")
    modelos = {e: (next(iter(datos.values()))[e]["codificador"]["modelo_respondido"] or next(iter(datos.values()))[e]["codificador"]["modelo_pedido"]) for e in ets}
    fecha = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)

    # Acuerdo por categoría y par; unanimidad con todos.
    filas_conc = []
    for cat in cats:
        for a, b in combinations(ets, 2):
            pares = [(c[a]["categorias"][cat]["valor"], c[b]["categorias"][cat]["valor"]) for c in datos.values()]
            k = kappa(pares)
            filas_conc.append({"categoria": cat, "par": f"{a}-{b}", "n": len(pares),
                               "acuerdo": round(sum(1 for x, y in pares if x == y) / len(pares), 3),
                               "kappa": None if k is None else round(k, 3)})
        todos = [len({c[e]["categorias"][cat]["valor"] for e in ets}) == 1 for c in datos.values()]
        filas_conc.append({"categoria": cat, "par": "todos", "n": len(todos), "acuerdo": round(sum(todos) / len(todos), 3), "kappa": None})

    # Mayoría por texto y categoría.
    filas_may, desacuerdos = [], []
    for texto, c in datos.items():
        base = next(iter(c.values()))
        f = {k: base.get(k, "") for k in COLUMNAS}
        for cat in cats:
            valores = [c[e]["categorias"][cat]["valor"] for e in ets]
            cuenta = Counter(valores).most_common()
            if len(cuenta) > 1 and cuenta[0][1] == cuenta[1][1]:
                f[cat], f[cat + "__n"] = "sin_mayoria", cuenta[0][1]
            else:
                f[cat], f[cat + "__n"] = cuenta[0]
            if len(set(valores)) > 1:
                desacuerdos.append((texto, cat, [(e, c[e]["categorias"][cat]["valor"], c[e]["categorias"][cat]["cita"]) for e in ets]))
        filas_may.append(f)

    with open(salida / f"concordancia_{args.unidad}_{fecha}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["categoria", "par", "n", "acuerdo", "kappa"])
        w.writeheader()
        w.writerows(filas_conc)
    pct = lambda v: "—" if v is None else f"{v:.0%}"
    with open(salida / f"concordancia_{args.unidad}_{fecha}.md", "w", encoding="utf-8") as f:
        f.write(f"# Concordancia entre codificadores — unidad {args.unidad} — {fecha}\n\n")
        f.write("Codificadores: " + "; ".join(f"{e} = {modelos[e]}" for e in ets) + f". Libro: {args.libro} (versión {libro.get('version')}).\n\n")
        unan = [x for x in filas_conc if x["par"] == "todos"]
        f.write(f"{len(datos)} textos con las {len(ets)} codificaciones. Unanimidad global: "
                f"{sum(x['acuerdo'] * x['n'] for x in unan) / sum(x['n'] for x in unan):.1%} de las celdas.\n\n")
        f.write("| Categoría | Par | n | Acuerdo | Kappa |\n|---|---|---|---|---|\n")
        for x in filas_conc:
            kap = "—" if x["kappa"] is None else f"{x['kappa']:.2f}"
            f.write(f"| {x['categoria']} | {x['par']} | {x['n']} | {pct(x['acuerdo'])} | {kap} |\n")
    columnas = COLUMNAS + [c for cat in cats for c in (cat, cat + "__n")]
    with open(salida / f"codificacion_{args.unidad}_mayoria.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        w.writerows(filas_may)
    with open(salida / f"codificacion_{args.unidad}_mayoria.md", "w", encoding="utf-8") as f:
        cols = COLUMNAS + cats
        f.write("| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n")
        for r in filas_may:
            f.write("| " + " | ".join(str(r.get(c, "")) for c in cols) + " |\n")
    with open(salida / f"desacuerdos_{args.unidad}_{fecha}.md", "w", encoding="utf-8") as f:
        f.write(f"# Desacuerdos — unidad {args.unidad} — {fecha}\n\nCeldas donde no coinciden todos ({len(desacuerdos)} de {len(datos) * len(cats)}). Valor y cita de cada codificador, para adjudicar a mano.\n\n")
        f.write("| Texto | Categoría | " + " | ".join(f"{e} | cita" for e in ets) + " |\n|" + "---|" * (2 + 2 * len(ets)) + "\n")
        lim = lambda t: (t or "").replace("|", "/").replace("\n", " ")[:140]
        for texto, cat, vs in desacuerdos:
            f.write(f"| {texto} | {cat} | " + " | ".join(f"{v} | {lim(ci)}" for _, v, ci in vs) + " |\n")
    print(f"{len(datos)} textos; {len(desacuerdos)} celdas sin unanimidad de {len(datos) * len(cats)}. Guardado en {salida}/ (concordancia_, codificacion_{args.unidad}_mayoria, desacuerdos_).")


if __name__ == "__main__":
    main()
