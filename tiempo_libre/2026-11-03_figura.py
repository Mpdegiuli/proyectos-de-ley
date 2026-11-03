#!/usr/bin/env python3
"""Figura del cuaderno: seis señales de socorro dibujadas en el tiempo (punto = 1 unidad, raya = 3),
a la misma escala, y abajo el SOS de la instancia h1 tal cual, girado 180 grados y en espejo.
Escribe senales.svg. Solo biblioteca estándar. Busca dibujos/h1_es.svg y, si no está, lo omite."""
import os, re

MORSE = {'S': '...', 'O': '---', 'E': '.', 'C': '-.-.', 'Q': '--.-', 'D': '-..', 'N': '-.'}
SENALES = [
    ("···−−−···", "SOS como signo continuo, art. XVI del reglamento de 1906", list("SOS"), True),
    ("SOS", "SOS con huecos de letra", list("SOS"), False),
    ("SOE", "Suchzeichen (llamada general) alemán de 1905", list("SOE"), True),
    ("CQD", "CQD de la Marconi, circular 57 de 1904", list("CQD"), False),
    ("NC", "NC del Código Internacional de Señales, propuesta de la marina de EE.UU. 1906", list("NC"), False),
    ("SSS DDD", "SSS DDD de Quintino Bonomo, conferencia preliminar de 1903", list("SSSDDD"), False),
]
U = 9          # píxeles por unidad
X0, Y0 = 200, 50
ALTO_BARRA = 14
W = 1060
partes = []
y = Y0
for nombre, leyenda, letras, continuo in SENALES:
    x = X0
    partes.append(f'<text x="{X0 - 12}" y="{y + 12}" text-anchor="end" font-family="Courier New, monospace" font-size="15" font-weight="bold" fill="#222">{nombre}</text>')
    for i, l in enumerate(letras):
        for j, e in enumerate(MORSE[l]):
            w = U if e == '.' else 3 * U
            partes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{ALTO_BARRA}" rx="2" fill="{"#c1272d" if continuo else "#222"}"/>')
            x += w + U
        if i < len(letras) - 1:
            x += 0 if continuo else 2 * U
    total = (x - U - X0) // U
    partes.append(f'<text x="{x + 6}" y="{y + 12}" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#555">{total} unidades</text>')
    partes.append(f'<text x="{X0}" y="{y + 30}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#777">{leyenda}</text>')
    y += 52

# regla de unidades
partes.append(f'<text x="{X0}" y="{y + 4}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#777">punto = 1 unidad, raya = 3, hueco entre elementos = 1, entre letras = 3; el signo continuo no tiene huecos de letra</text>')
y += 40

# el SOS de h1, tal cual, girado y en espejo
ruta = next((c for c in ("dibujos/h1_es.svg", "2026-11-03_h1_es.svg") if os.path.exists(c)), None)
if ruta:
    svg = open(ruta, encoding="utf-8").read()
    cuerpo = re.sub(r"^\s*<svg[^>]*>", "", svg, count=1, flags=re.S)
    cuerpo = re.sub(r"</svg>\s*$", "", cuerpo, flags=re.S)
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    vx, vy, vw, vh = map(float, vb.split())
    ancho_celda = 240
    esc = ancho_celda / vw
    for k, (titulo, transf) in enumerate([("tal cual", ""),
                                           ("girado 180°", f"rotate(180 {vw/2:g} {vh/2:g})"),
                                           ("en espejo", f"translate({vw:g} 0) scale(-1 1)")]):
        x = X0 + k * (ancho_celda + 30)
        partes.append(f'<text x="{x}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#555">{titulo}</text>')
        partes.append(f'<svg x="{x}" y="{y + 8}" width="{ancho_celda}" height="{vh*esc:.1f}" viewBox="{vb}"><g transform="{transf}">{cuerpo}</g></svg>')
    y += int(vh * esc) + 40
    partes.append(f'<text x="{X0}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#777">el SOS de la instancia h1 (dos arcos por S), tal cual, girado y en espejo:</text>')
    partes.append(f'<text x="{X0}" y="{y + 16}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#777">girado coincide consigo mismo en el 99,8 % de los píxeles pintados; en espejo, en el 79 % (giro.py)</text>')
    y += 40

alto = y + 10
svg_final = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {alto}" width="{W}" height="{alto}">'
             f'<rect width="{W}" height="{alto}" fill="#f4f1ea"/>'
             f'<text x="{X0}" y="28" font-family="Helvetica, Arial, sans-serif" font-size="16" fill="#222">Seis señales en el tiempo, a la misma escala</text>'
             + "\n".join(partes) + "</svg>\n")
open("senales.svg", "w", encoding="utf-8").write(svg_final)
print("senales.svg escrita")
