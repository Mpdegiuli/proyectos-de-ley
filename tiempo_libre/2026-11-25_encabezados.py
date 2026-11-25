#!/usr/bin/env python3
"""encabezados.py — cuenta los casilleros de las doce instancias frescas del 25/11/2026.

Uso: python3 encabezados.py 2026-11-25_instancias_frescas.md

Lee el título y los encabezados de cada instancia (secciones "## es1" ... "## en6" del
archivo) y cuenta, sin mirar nada más: cuántos encabezados tiene cada una; si el primero
dice por qué empieza ahí; si hay un desvío o digresión; si el último (o el anteúltimo) es
de cabos sueltos, preguntas abiertas o cosas para otro día; si hay una sección sobre sí
misma; el tema (por palabras del título); y qué frases de tres palabras o más comparten
dos instancias distintas. Solo biblioteca estándar.
"""
import re
import sys
import unicodedata
from collections import Counter, defaultdict

PATRONES = {
    "abre diciendo de dónde arranca": r"^(por qu[eé]|why|starting point|preface|una pregunta)",
    "desvío / digresión": r"desv[ií]o|digresi[oó]n|detour|digression|sidetrack|sidebar",
    "cierre: cabos sueltos / otro día / lo que no sé": r"otro d[ií]a|otra tarde|no s[eé]\b|no entiendo|no entend[ií]|cabos sueltos|notas sueltas|loose|next time|look up later|open questions|still don't understand|lecturas que",
    "una sección sobre sí misma": r"\byo\b|\bsoy\b|\bmyself\b|\bI am\b|copia yo",
    "pide un experimento que no puede hacer": r"if i had|i'd need|things i.d need",
}


def norm(s):
    s = unicodedata.normalize("NFC", s.lower())
    s = re.sub(r"[^0-9a-záéíóúüñ\s]", " ", s)
    return s.split()


def main(ruta):
    texto = open(ruta, encoding="utf-8").read()
    partes = re.split(r"^## (es\d|en\d)\s*$", texto, flags=re.M)
    inst = {}
    for i in range(1, len(partes), 2):
        nombre, cuerpo = partes[i], partes[i + 1]
        titulo = ""
        encs = []
        for l in cuerpo.splitlines():
            l = l.strip()
            if l.startswith("# "):
                titulo = l[2:].strip()
            elif l.startswith("## ") or re.match(r"^\d+\.\s", l):
                e = re.sub(r"^## ", "", l).strip()
                e = re.sub(r"^\d+\.\s*", "", e).strip()   # "1. Por qué..." -> "Por qué..."
                if e.startswith("("):                      # un subtítulo entre paréntesis no es un encabezado
                    continue
                encs.append(e)
        inst[nombre] = (titulo, encs)

    print(f"{'inst':5s} {'enc':>3s}  " + "  ".join(f"{k[:14]:14s}" for k in PATRONES) + "  título")
    tot = Counter()
    for nombre, (titulo, encs) in inst.items():
        marcas = {}
        for k, p in PATRONES.items():
            if k.startswith("abre"):
                marcas[k] = bool(encs) and bool(re.search(p, encs[0], flags=re.I))
            elif k.startswith("cierre"):
                marcas[k] = any(re.search(p, e, flags=re.I) for e in encs[-2:])
            else:
                marcas[k] = any(re.search(p, e, flags=re.I) for e in encs)
            tot[k] += marcas[k]
        print(f"{nombre:5s} {len(encs):3d}  " + "  ".join(f"{('sí' if marcas[k] else '—'):14s}" for k in PATRONES) + f"  {titulo}")
    print("")
    for k in PATRONES:
        print(f"  {tot[k]:2d} de {len(inst)}  {k}")
    largos = [len(e) for _, e in inst.values()]
    print(f"  encabezados por instancia: mín {min(largos)}, máx {max(largos)}, entre 4 y 7: {sum(4 <= n <= 7 for n in largos)} de {len(inst)}")

    # temas por título
    print("")
    print("temas (por el título):")
    for nombre, (titulo, encs) in inst.items():
        print(f"  {nombre}: {titulo}")
    rios = [n for n, (t, e) in inst.items() if re.search(r"meandr|r[ií]o", t + " " + " ".join(e), flags=re.I)]
    print(f"  nombran meandros o ríos en título o encabezados: {len(rios)} de {len(inst)} ({', '.join(rios)})")

    # frases compartidas entre instancias
    print("")
    print("frases de tres o más palabras que aparecen en dos o más instancias distintas (título y encabezados):")
    n = 3
    donde = defaultdict(set)
    for nombre, (titulo, encs) in inst.items():
        for linea in [titulo] + encs:
            tk = norm(linea)
            for i in range(len(tk) - n + 1):
                donde[tuple(tk[i:i + n])].add(nombre)
    comp = {g: d for g, d in donde.items() if len(d) >= 2}
    # alargar: quedarse con las frases maximales
    vistas = set()
    for g, d in sorted(comp.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        # extender a la derecha mientras el conjunto no cambie
        frase = list(g)
        while True:
            ext = [gg for gg in comp if gg[:-1] == tuple(frase[-(n - 1):]) and comp[gg] == d]
            if not ext:
                break
            frase.append(ext[0][-1])
            if len(frase) > 12:
                break
        clave = tuple(frase)
        if any(clave == v[-len(clave):] or clave == v[:len(clave)] for v in vistas if len(v) >= len(clave)):
            continue
        vistas.add(clave)
        print(f"  {len(d)}  {' '.join(sorted(d))}: \"{' '.join(frase)}\"")


if __name__ == "__main__":
    main(sys.argv[1])
