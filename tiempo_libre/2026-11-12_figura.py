#!/usr/bin/env python3
"""Saldo cero: el día del peluquero Fusi según el hombre gris de *Momo*.

Dibuja un SVG con 96 celdas, una por cuarto de hora del día, repartidas como las
reparte el hombre gris en el capítulo de la Caja de Ahorros de Tiempo: cada rubro
del libro es un múltiplo exacto de 13.797.000 segundos, que es 1.324.512.000 / 96,
o sea un cuarto de hora por día durante 42 años de 365 días. Las cifras son las del
libro (traducción inglesa de J. Maxwell Brownjohn, donde Fusi se llama Figaro);
el reparto en cuartos de hora es una lectura mía de esas cifras.

Uso: python3 2026-11-12_figura.py  -> escribe 2026-11-12_saldo_cero.svg
     (y un PNG si está rsvg-convert o cairosvg)
"""
import shutil
import subprocess
import sys
from pathlib import Path

TOTAL = 1_324_512_000           # 42 × 365 × 24 × 60 × 60
CUARTO = TOTAL // 96            # 13.797.000

# (rubro, segundos del libro, etiqueta)
RUBROS = [
    ("dormir",       441_504_000, "dormir, 8 h"),
    ("trabajar",     441_504_000, "trabajar, 8 h"),
    ("comer",        110_376_000, "comer, 2 h"),
    ("la madre",      55_188_000, "la madre, 1 h"),
    ("el periquito",  13_797_000, "el periquito, ¼ h"),
    ("compras",       55_188_000, "compras y trámites, 1 h"),
    ("amigos",       165_564_000, "amigos, club, etc., 3 h"),
    ("Daria",         27_594_000, "la señorita Daria, ½ h"),
    ("la ventana",    13_797_000, "soñar despierto, ¼ h"),
]

assert sum(s for _, s, _ in RUBROS) == TOTAL
for _, s, _ in RUBROS:
    assert s % CUARTO == 0, s
assert sum(s // CUARTO for _, s, _ in RUBROS) == 96

W, H = 1000, 330
X0, Y0 = 20, 150
CELL, GAP = 9, 1          # 96 × 10 = 960
ALTO = 44
AZUL = ("#2a78d6", "#8fb8ea")   # un solo tono, dos pasos, para separar rubros vecinos
TINTA, TINTA2 = "#0b0b0b", "#52514e"

# dónde va cada etiqueta: (lado, nivel, anclaje); nivel 0 pegado a la barra, 1 y 2 más lejos con guía
POS = {
    "dormir":       ("arriba", 0, "middle"),
    "trabajar":     ("abajo",  0, "middle"),
    "comer":        ("arriba", 0, "middle"),
    "la madre":     ("abajo",  1, "middle"),
    "el periquito": ("arriba", 2, "middle"),
    "compras":      ("abajo",  2, "middle"),
    "amigos":       ("arriba", 0, "middle"),
    "Daria":        ("abajo",  1, "end"),
    "la ventana":   ("arriba", 1, "end"),
}

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">')
out.append(f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>')
out.append(f'<text x="{X0}" y="34" font-size="17" fill="{TINTA}" font-weight="bold">'
           'Saldo cero: el día del peluquero según el hombre gris</text>')
out.append(f'<text x="{X0}" y="56" font-size="12.5" fill="{TINTA2}">'
           'Cada celda es un cuarto de hora por día durante 42 años de 365 días: 13.797.000 segundos.</text>')
out.append(f'<text x="{X0}" y="74" font-size="12.5" fill="{TINTA2}">'
           'Las nueve cifras del libro suman exactamente 1.324.512.000, que es el total: no sobra nada.</text>')
out.append(f'<text x="{X0}" y="92" font-size="12.5" fill="{TINTA2}">'
           'Sin años bisiestos: con los diez que hay en 42 años serían 864.000 segundos más, diez días que el hombre gris no cobra.</text>')

x = X0
for i, (nombre, seg, etiqueta) in enumerate(RUBROS):
    n = seg // CUARTO
    color = AZUL[i % 2]
    ancho = n * (CELL + GAP) - GAP
    out.append(f'<rect x="{x}" y="{Y0}" width="{ancho}" height="{ALTO}" fill="{color}" rx="3"/>')
    for k in range(1, n):
        cx = x + k * (CELL + GAP) - GAP
        out.append(f'<rect x="{cx}" y="{Y0}" width="{GAP}" height="{ALTO}" fill="#fcfcfb"/>')
    xm = x + ancho / 2
    lado, nivel, ancla = POS[nombre]
    texto = f"{etiqueta} ({n})"
    if lado == "arriba":
        ty = Y0 - 10 - nivel * 22
        if nivel:
            out.append(f'<line x1="{xm:.1f}" y1="{Y0 - 3}" x2="{xm:.1f}" y2="{ty + 4}" stroke="{TINTA2}" stroke-width="1"/>')
    else:
        ty = Y0 + ALTO + 18 + nivel * 22
        if nivel:
            out.append(f'<line x1="{xm:.1f}" y1="{Y0 + ALTO + 3}" x2="{xm:.1f}" y2="{ty - 12}" stroke="{TINTA2}" stroke-width="1"/>')
    tx = xm if ancla == "middle" else xm + 4
    out.append(f'<text x="{tx:.1f}" y="{ty}" font-size="12" fill="{TINTA}" text-anchor="{ancla}">{texto}</text>')
    x += ancho + GAP

out.append(f'<text x="{X0}" y="{H - 44}" font-size="11.5" fill="{TINTA2}">'
           '96 cuartos de hora = 24 horas. El reparto es el del hombre gris para el señor Fusi, aplicado a los 42 años enteros:</text>')
out.append(f'<text x="{X0}" y="{H - 28}" font-size="11.5" fill="{TINTA2}">'
           'según la cuenta, el peluquero trabajó ocho horas por día desde el día en que nació.</text>')
out.append(f'<text x="{X0}" y="{H - 10}" font-size="11.5" fill="{TINTA2}">'
           'Cifras del libro (Momo, 1973, cap. 6, trad. inglesa de Brownjohn). Cuaderno de tiempo libre del 12/11/2026; el reparto en cuartos de hora es una lectura, no una cita.</text>')
out.append('</svg>')

aqui = Path(__file__).resolve().parent
svg = aqui / "2026-11-12_saldo_cero.svg"
svg.write_text("\n".join(out), encoding="utf-8")
print("escrito", svg)

png = svg.with_suffix(".png")
if shutil.which("rsvg-convert"):
    subprocess.run(["rsvg-convert", "-w", "2000", "-o", str(png), str(svg)], check=True)
    print("escrito", png)
else:
    try:
        import cairosvg
        cairosvg.svg2png(url=str(svg), write_to=str(png), output_width=2000)
        print("escrito", png)
    except ImportError:
        print("sin rsvg-convert ni cairosvg: queda solo el SVG", file=sys.stderr)
