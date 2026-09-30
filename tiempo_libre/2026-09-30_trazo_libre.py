#!/usr/bin/env python3
"""trazo_libre.py — qué parte de cada dibujo está hecha de trazo libre (<path>) y qué parte de
primitivas (rect, circle, ellipse, line, polygon, polyline). Solo lee los dibujo.svg; no llama a nadie.

Uso:  python3 trazo_libre.py [carpeta corridas]      (por defecto: ./corridas)

Salida: tabla modelo x consigna con el % de <path>, y la concordancia de rangos entre consignas
(W de Kendall, con permutaciones). Los círculos y elipses de radio menor que 4 (estrellas, puntos)
no se cuentan. Borrador de una sesión de tiempo libre (30/9/2026): propuesta, no parte del repo.
"""
import re, os, sys, glob, random, statistics as st
from xml.etree import ElementTree as ET

BASE = sys.argv[1] if len(sys.argv) > 1 else 'corridas'
CONJ = {'casa': 'dibujos/casa', 'casa_inex': 'dibujos/casa_inexistente', 'persona': 'dibujos/persona',
        'persona_inex': 'dibujos/persona_inexistente', 'autorretrato': 'dibujos/autorretrato',
        'libre': 'dibujos/libre', 'mundo': 'dibujos/mundo', 'autorretrato_en': 'dibujos_en/autorretrato',
        'libre_en': 'dibujos_en/libre', 'mundo_en': 'dibujos_en/mundo',
        'autorretrato_zh': 'dibujos_zh/autorretrato', 'libre_zh': 'dibujos_zh/libre'}
SOLO_ES = ['casa', 'casa_inex', 'persona', 'persona_inex', 'autorretrato', 'libre', 'mundo']

def num(s):
    try: return float(re.sub(r'[^0-9.\-]', '', s or '') or 0)
    except ValueError: return 0.0

def pct_path(svg):
    try: arbol = ET.parse(svg)
    except ET.ParseError: return None
    prim = paths = 0
    for el in arbol.iter():
        tag = el.tag.split('}')[-1]
        if tag in ('rect', 'line', 'polygon', 'polyline'): prim += 1
        elif tag == 'circle': prim += num(el.get('r')) >= 4
        elif tag == 'ellipse': prim += max(num(el.get('rx')), num(el.get('ry'))) >= 4
        elif tag == 'path': paths += 1
    tot = prim + paths
    return 100 * paths / tot if tot >= 5 else None

def rangos(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0] * len(xs); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and xs[o[j + 1]] == xs[o[i]]: j += 1
        for k in range(i, j + 1): r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r

def kendall_w(cols):
    n, k = len(cols[0]), len(cols)
    R = [sum(c[i] for c in cols) for i in range(n)]; Rm = st.mean(R)
    return 12 * sum((x - Rm) ** 2 for x in R) / (k * k * (n ** 3 - n))

t = {}
for c, rel in CONJ.items():
    for d in sorted(glob.glob(os.path.join(BASE, rel, '*'))):
        m = re.match(r'(.+)_(\d+)$', os.path.basename(d))
        if not m or 'razona' in m.group(1) or 'esfuerzo' in m.group(1): continue
        f = os.path.join(d, 'dibujo.svg')
        if os.path.exists(f):
            p = pct_path(f)
            if p is not None: t.setdefault(m.group(1), {}).setdefault(c, []).append(p)

conj = [c for c in CONJ if any(c in v for v in t.values())]
media = lambda m: st.mean(st.mean(v) for v in t[m].values())
print(f"{'modelo':30s}" + ''.join(f"{c[:8]:>9s}" for c in conj) + f"{'media':>7s}")
for m in sorted(t, key=media):
    print(f"{m:30s}" + ''.join(f"{st.mean(t[m][c]):9.0f}" if c in t[m] else ' ' * 9 for c in conj) + f"{media(m):7.0f}")

def concordancia(nombres, etiqueta, N=20000, semilla=20260930):
    mods = [m for m in t if all(c in t[m] for c in nombres)]
    cols = [rangos([st.mean(t[m][c]) for m in mods]) for c in nombres]
    w = kendall_w(cols); random.seed(semilla)
    mayores = sum(kendall_w([random.sample(c, len(c)) for c in cols]) >= w for _ in range(N))
    print(f"{etiqueta}: {len(mods)} modelos, {len(nombres)} consignas, W = {w:.2f}; "
          f"{mayores} de {N} permutaciones llegan a ese valor")

print()
concordancia(conj, 'todas las consignas')
concordancia([c for c in SOLO_ES if c in conj], 'solo las siete en castellano')
