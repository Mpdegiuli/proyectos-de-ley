#!/usr/bin/env python3
"""borrador.py — cuánto del razonamiento guardado es borrador de la respuesta: parte de los 5-gramas de palabras del
razonamiento que aparecen tal cual en la respuesta. Lee corridas/**/llamadas.jsonl; no escribe en el repositorio.
  python3 borrador.py /ruta/al/clon [--csv salida.csv]"""
import argparse, collections, csv, glob, json, os, re, statistics, sys
import importlib.util, glob as _g
def _vecino(nombre):
    """Importa un script vecino aunque lleve la fecha adelante del nombre (2026-11-16_idioma.py)."""
    aqui = os.path.dirname(os.path.abspath(__file__))
    for cand in [os.path.join(aqui, nombre + ".py")] + sorted(_g.glob(os.path.join(aqui, "*_" + nombre + ".py"))):
        if os.path.exists(cand):
            spec = importlib.util.spec_from_file_location(nombre, cand); mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod); return mod
    raise ImportError(nombre + ".py no está al lado de este script")
_idioma = _vecino("idioma"); clasificar, idioma_consigna = _idioma.clasificar, _idioma.idioma_consigna
PAL = re.compile(r"\w+", re.U)

def ngr(t, n=5):
    w = [x.lower() for x in PAL.findall(t)]
    return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}

ap = argparse.ArgumentParser(); ap.add_argument("repo"); ap.add_argument("--csv"); a = ap.parse_args()
filas = []
for f in sorted(glob.glob(os.path.join(a.repo, "corridas", "**", "llamadas.jsonl"), recursive=True)):
    for l in open(f, encoding="utf-8"):
        try: r = json.loads(l)
        except json.JSONDecodeError: continue
        rz = r.get("razonamiento"); resp = r.get("respuesta")
        if not isinstance(rz, str) or not rz.strip() or not isinstance(resp, str): continue
        g = ngr(rz)
        if len(g) < 5: continue
        h = ngr(resp)
        sol = len(g & h) / len(g)
        c, n, es, en, zh = clasificar(rz)
        filas.append({"casa": r["id_modelo"], "consigna": idioma_consigna(r, os.path.dirname(f)), "clase": c,
                      "solapamiento": round(sol, 3), "palabras": n})
if a.csv:
    w = csv.DictWriter(open(a.csv, "w", newline="", encoding="utf-8"), fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
print(f"{len(filas)} razonamientos con respuesta\n")
print(f"{'casa':30} {'n':>5} {'mediana':>8} {'media':>6} {'>=0,5':>6} | en consigna es: clase es {'n':>4} {'med':>5}  clase en {'n':>4} {'med':>5}")
por = collections.defaultdict(list)
for x in filas: por[x["casa"]].append(x)
for casa, xs in sorted(por.items()):
    s = [x["solapamiento"] for x in xs]
    es_ = [x["solapamiento"] for x in xs if x["consigna"]=="es" and x["clase"]=="es"]
    en_ = [x["solapamiento"] for x in xs if x["consigna"]=="es" and x["clase"]=="en"]
    med = lambda v: f"{statistics.median(v):5.2f}" if v else "    -"
    print(f"{casa:30} {len(s):5d} {statistics.median(s):8.2f} {statistics.mean(s):6.2f} {sum(v>=0.5 for v in s)/len(s):6.2f} | {'':20} {len(es_):4d} {med(es_)}  {'':8} {len(en_):4d} {med(en_)}")
