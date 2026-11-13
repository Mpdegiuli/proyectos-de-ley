#!/usr/bin/env python3
"""Cuántas veces habrían hecho falta las tres letras de Claudio.

Cuenta, en textos latinos de la copia de The Latin Library que mantiene el proyecto
CLTK (github.com/cltk/lat_text_latin_library):
  - la u consonante (la 'v' de las ediciones que la distinguen): F invertida
  - los grupos ps y bs: antisigma
  - la y (palabras griegas con ípsilon): media H, según el uso de las piedras
  - la x, para comparar con ps+bs

Uso: python3 letras.py RUTA_AL_CLON
No llama a nadie. Los textos son copias de la web con erratas; los números son
aproximados y sirven para comparar proporciones, no para citar un total.
"""
import glob
import os
import re
import sys

VOCALES = "aeiouy"


def limpiar(t, lyon=False):
    if lyon:
        # la copia trae encabezados en inglés, barras de fin de renglón y cortes
        t = t.split("Column I", 1)[1]
        t = t.split("The Miscellany")[0]
        t = t.replace("Column II", " ")
        # palabras partidas por el fin de renglón del bronce: "succ es |soribus"
        t = re.sub(r"(\w) (\w{1,2}) ?\|", r"\1\2|", t)   # "qua m |" -> "quam|"
        t = re.sub(r"\s*\|\s*", "", t)
    else:
        # corta el pie de página de la copia
        t = re.split(r"The Latin Library|Tacitus\s+The Latin", t)[0] if len(t) > 2000 else t
    return t


def contar(t):
    letras = re.findall(r"[A-Za-z]", t)
    n = len(letras)
    bajo = t.lower()
    # u consonante: toda 'v' minúscula; 'V' mayúscula solo si le sigue vocal
    v = len(re.findall(r"v", t))
    v += len(re.findall(r"V(?=[aeiouAEIOU])", t))
    ps = len(re.findall(r"ps", bajo))
    bs = len(re.findall(r"bs", bajo))
    x = len(re.findall(r"x", bajo))
    y = len(re.findall(r"y", bajo))
    return dict(letras=n, v=v, ps=ps, bs=bs, x=x, y=y)


def fila(nombre, c):
    n = c["letras"]
    pm = lambda k: 1000.0 * c[k] / n
    print(f"{nombre:28s} {n:8d}  v {c['v']:6d} ({pm('v'):5.1f}‰)  ps {c['ps']:5d}  bs {c['bs']:5d}"
          f"  ps+bs {c['ps']+c['bs']:5d} ({1000.0*(c['ps']+c['bs'])/n:4.1f}‰)"
          f"  x {c['x']:5d} ({pm('x'):4.1f}‰)  y {c['y']:4d} ({pm('y'):4.2f}‰)")


def leer(ruta):
    return open(ruta, encoding="utf-8", errors="replace").read()


def main():
    base = sys.argv[1]
    lyon = limpiar(leer(os.path.join(base, "claud.inscr.txt")), lyon=True)
    c = contar(lyon)
    fila("Tabla de Lyon", c)
    palabras = re.findall(r"[A-Za-z]+", lyon)
    print("  palabras:", len(palabras))
    print("  con ps/bs:", sorted(set(w for w in palabras if re.search(r"ps|bs", w.lower()))))
    print("  con y:", sorted(set(w for w in palabras if "y" in w.lower())))
    print("  superlativos y afines (-imus/-ima/-ime…):",
          sorted(set(w for w in palabras if re.search(r"(issim|xim|tim|rrim|llim)[aeiou]", w.lower()))))
    print()
    grupos = {
        "Tácito, Anales 11-12": ["tacitus/tac.ann11.txt", "tacitus/tac.ann12.txt"],
        "Tácito, Anales (todos)": sorted(glob.glob(os.path.join(base, "tacitus/tac.ann*.txt"))),
        "César, Guerra de las Galias": sorted(glob.glob(os.path.join(base, "caesar/gall*.txt"))),
        "Virgilio, Eneida": sorted(glob.glob(os.path.join(base, "vergil/aen*.txt"))),
        "Livio 1-5": [f"livy/liv.{i}.txt" for i in range(1, 6)],
        "Séneca, Apocolocyntosis": ["sen/sen.apoc.txt"],
    }
    for nombre, archivos in grupos.items():
        tot = dict(letras=0, v=0, ps=0, bs=0, x=0, y=0)
        for a in archivos:
            ruta = a if os.path.exists(a) else os.path.join(base, a)
            if not os.path.exists(ruta):
                print("  (falta", a, ")")
                continue
            c = contar(limpiar(leer(ruta)))
            for k in tot:
                tot[k] += c[k]
        if tot["letras"]:
            fila(nombre, tot)
    # qué palabras llevan ps/bs en los Anales
    from collections import Counter
    cnt = Counter()
    for a in sorted(glob.glob(os.path.join(base, "tacitus/tac.ann*.txt"))):
        # se quitan los corchetes de editor para no partir palabras ("Vips[t]ano")
        for w in re.findall(r"[A-Za-z]+", re.sub(r"[\[\]<>+]", "", limpiar(leer(a))).lower()):
            if "ps" in w or "bs" in w:
                cnt[w] += 1
    print("\nAnales, las 25 palabras con ps/bs más frecuentes:")
    print("  " + ", ".join(f"{w} {n}" for w, n in cnt.most_common(25)))
    lemas = Counter()
    for w, n in cnt.items():
        if w.startswith("ips"):
            lemas["ipse"] += n
        elif w.startswith("abs") or w.startswith("obs") or w.startswith("subs"):
            lemas["empiezan con ab-, ob- o sub- seguido de s (incluye abs-)"] += n
        elif w.endswith("bs") or w.endswith("ps"):
            lemas["final -bs/-ps (urbs, plebs, princeps…)"] += n
        else:
            lemas["otras"] += n
    print("  por tipo:", dict(lemas))


if __name__ == "__main__":
    main()
