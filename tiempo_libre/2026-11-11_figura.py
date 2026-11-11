#!/usr/bin/env python3
"""Dibuja `2026-11-11_urnas.svg`: las cuatro fórmulas con que seis instancias
frescas "sortearon" un patrono a partir de la fecha, vistas como urnas. Para
cada fórmula, los doce nombres con la cantidad de días de 2026 en que esa
fórmula los saca (un papel por cada 10 días, redondeando), y marcado el que
salió hoy, 11/11/2026. Reusa las fórmulas de `2026-11-11_sorteo.py`.
Con `--png` escribe también el PNG (pide rsvg-convert).
"""
import subprocess
import sys
from collections import Counter
from datetime import date, timedelta
from html import escape

SANTOS = ["San Andrés", "Santa Bárbara", "San Blas", "San Bernabé",
          "Santa Catalina", "San Lorenzo", "San Martín de Tours",
          "San Nicolás de Bari", "San Pedro", "San Sebastián", "Santiago",
          "Santa Lucía"]

def f_a(d): return sum(int(c) for c in f"{d.day:02d}{d.month:02d}{d.year:04d}") % 12
def f_b(d): return int(f"{d.year:04d}{d.month:02d}{d.day:02d}") % 12
def f_b2(d): return int(f"{d.day:02d}{d.month:02d}{d.year:04d}") % 12
def f_c(d): return (d.day + d.month + d.year) % 12

FORMULAS = [("A. suma de dígitos (S2, S3; S4 de yapa)", f_a),
            ("B. AAAAMMDD mod 12 (S1, S5)", f_b),
            ("B'. DDMMAAAA mod 12 (S4)", f_b2),
            ("C. día + mes + año (S6)", f_c)]

hoy = date(2026, 11, 11)
dias = []
d = date(2026, 1, 1)
while d.year == 2026:
    dias.append(d); d += timedelta(days=1)

W, H = 1000, 720
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">',
       f'<rect width="{W}" height="{H}" fill="#fbf7ef"/>',
       '<text x="500" y="34" text-anchor="middle" font-size="20" fill="#222">La urna de la fecha: qué puede salir de cada fórmula a lo largo de 2026</text>',
       '<text x="500" y="56" text-anchor="middle" font-size="12" fill="#555">un papel por cada diez días del año en que la fórmula saca ese nombre; en naranja, lo que salió el 11/11/2026</text>']

col_w = 240
for k, (nombre, f) in enumerate(FORMULAS):
    x0 = 20 + k * col_w
    c = Counter(f(x) for x in dias)
    r_hoy = f(hoy)
    out.append(f'<text x="{x0 + col_w/2 - 10}" y="90" text-anchor="middle" font-size="12.5" fill="#222">{escape(nombre)}</text>')
    # sombrero
    cx = x0 + col_w / 2 - 10
    out.append(f'<path d="M{cx-70} 660 Q{cx} 690 {cx+70} 660" fill="none" stroke="#333" stroke-width="2"/>')
    out.append(f'<rect x="{cx-45}" y="610" width="90" height="52" rx="8" fill="#e8dcc3" stroke="#333" stroke-width="2"/>')
    for i, s in enumerate(SANTOS):
        resto = (i + 1) % 12
        n = c.get(resto, 0)
        y = 115 + i * 40
        es_hoy = (resto == r_hoy)
        fill = "#e07b2a" if es_hoy else "#222"
        peso = ' font-weight="bold"' if es_hoy else ''
        out.append(f'<text x="{x0}" y="{y+12}" font-size="11.5" fill="{fill}"{peso}>{escape(s)}</text>')
        out.append(f'<text x="{x0 + 205}" y="{y+12}" font-size="11" text-anchor="end" fill="#777">{n}</text>')
        papeles = round(n / 10)
        for p in range(papeles):
            px = x0 + 2 + p * 13
            out.append(f'<rect x="{px}" y="{y+17}" width="10" height="13" fill="{"#f3c9a0" if es_hoy else "#fff"}" stroke="#555" stroke-width="0.8" transform="rotate({(-6 + (p*7)%13)} {px+5} {y+23})"/>')
out.append('<text x="500" y="705" text-anchor="middle" font-size="11" fill="#555">Seis instancias, una fecha, cuatro fórmulas: Santa Bárbara tres veces, Santiago dos, San Nicolás una. La urna B\' tiene tres papeles en todo 2026.</text>')
out.append('</svg>')

svg = "\n".join(out)
with open("2026-11-11_urnas.svg", "w", encoding="utf-8") as fh:
    fh.write(svg)
print("escrito 2026-11-11_urnas.svg")
if "--png" in sys.argv:
    subprocess.run(["rsvg-convert", "-w", "2000", "2026-11-11_urnas.svg", "-o", "2026-11-11_urnas.png"], check=True)
    print("escrito 2026-11-11_urnas.png")
