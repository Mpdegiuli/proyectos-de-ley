#!/usr/bin/env python3
"""Dibuja demonio.svg a partir de demonio.json (lo escribe demonio.py). Tres paneles:
izquierda, las dos temperaturas con el demonio de temperatura; centro, las dos poblaciones con la
válvula; derecha, la memoria del demonio (bits · ln 2) contra lo que bajó la entropía del gas (−ΔS/k),
para los dos demonios. Solo biblioteca estándar. Busca el .json por el nombre sin fecha y, si no está,
con la fecha adelante."""
import json
import math
import os
import sys


def hallar(nombre):
    for cand in (nombre, "2026-11-05_" + nombre):
        if os.path.exists(cand):
            return cand
    sys.exit(f"no encuentro {nombre}")


res = json.load(open(hallar("demonio.json"), encoding="utf-8"))
LN2 = math.log(2)


def c(x, nd=2):
    """Número con coma decimal."""
    return f"{x:.{nd}f}".replace(".", ",")

W, H = 1500, 520
PANEL_W, PANEL_H = 420, 330
X0 = [60, 560, 1060]
Y0 = 100
FONDO = "#f4f1ea"
ROJO, AZUL, GRIS, NEGRO, VERDE = "#b5452f", "#2f5f9e", "#8a8a8a", "#222", "#4f7a3a"

partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
          f'<rect width="{W}" height="{H}" fill="{FONDO}"/>',
          f'<text x="{W/2}" y="40" text-anchor="middle" font-size="22" fill="{NEGRO}">Un demonio con la memoria a la vista: 600 partículas, una puerta, 60 unidades de tiempo</text>']


def ejes(x0, titulo, ymax, ylabel, yticks, xmax=60.0):
    p = []
    p.append(f'<text x="{x0 + PANEL_W/2}" y="{Y0 - 16}" text-anchor="middle" font-size="15" fill="{NEGRO}">{titulo}</text>')
    p.append(f'<rect x="{x0}" y="{Y0}" width="{PANEL_W}" height="{PANEL_H}" fill="#fff" stroke="#bbb"/>')
    for t in range(0, 61, 10):
        xx = x0 + t / xmax * PANEL_W
        p.append(f'<line x1="{xx:.1f}" y1="{Y0 + PANEL_H}" x2="{xx:.1f}" y2="{Y0 + PANEL_H + 5}" stroke="#555"/>')
        p.append(f'<text x="{xx:.1f}" y="{Y0 + PANEL_H + 20}" text-anchor="middle" font-size="12" fill="#555">{t}</text>')
    p.append(f'<text x="{x0 + PANEL_W/2}" y="{Y0 + PANEL_H + 42}" text-anchor="middle" font-size="13" fill="#555">tiempo</text>')
    for v, lab in yticks:
        yy = Y0 + PANEL_H - v / ymax * PANEL_H
        p.append(f'<line x1="{x0 - 5}" y1="{yy:.1f}" x2="{x0}" y2="{yy:.1f}" stroke="#555"/>')
        p.append(f'<text x="{x0 - 9}" y="{yy + 4:.1f}" text-anchor="end" font-size="12" fill="#555">{lab}</text>')
    p.append(f'<text transform="translate({x0 - 44},{Y0 + PANEL_H/2}) rotate(-90)" text-anchor="middle" font-size="13" fill="#555">{ylabel}</text>')
    return p


def linea(x0, puntos, ymax, color, dash="", ancho=2, xmax=60.0):
    pts = " ".join(f"{x0 + t / xmax * PANEL_W:.1f},{Y0 + PANEL_H - min(max(v, 0), ymax) / ymax * PANEL_H:.1f}"
                   for t, v in puntos if v == v)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{ancho}"{d}/>'


# Panel 1: temperaturas con el demonio de temperatura
s = res["temperatura"]["serie"]
ymax1 = 1.6
partes += ejes(X0[0], "Demonio de temperatura: las dos cámaras", ymax1, "temperatura (kT inicial = 1)",
               [(0, "0"), (0.5, "0,5"), (1.0, "1"), (1.5, "1,5")])
t0 = (s[0]["TL"] * s[0]["NL"] + s[0]["TR"] * s[0]["NR"]) / 600
yy = Y0 + PANEL_H - t0 / ymax1 * PANEL_H
partes.append(f'<line x1="{X0[0]}" y1="{yy:.1f}" x2="{X0[0] + PANEL_W}" y2="{yy:.1f}" stroke="{GRIS}" stroke-dasharray="4 4"/>')
partes.append(linea(X0[0], [(f["t"], f["TR"]) for f in s], ymax1, ROJO))
partes.append(linea(X0[0], [(f["t"], f["TL"]) for f in s], ymax1, AZUL))
partes.append(f'<text x="{X0[0] + PANEL_W - 8}" y="{Y0 + PANEL_H - s[-1]["TR"] / ymax1 * PANEL_H - 8:.1f}" text-anchor="end" font-size="12" fill="{ROJO}">derecha, {c(s[-1]["TR"])}</text>')
partes.append(f'<text x="{X0[0] + PANEL_W - 8}" y="{Y0 + PANEL_H - s[-1]["TL"] / ymax1 * PANEL_H + 16:.1f}" text-anchor="end" font-size="12" fill="{AZUL}">izquierda, {c(s[-1]["TL"])}</text>')
partes.append(f'<text x="{X0[0] + 8}" y="{yy - 6:.1f}" font-size="11" fill="{GRIS}">temperatura inicial de las dos, {c(t0)}</text>')

# Panel 2: poblaciones con la válvula
s = res["valvula"]["serie"]
ymax2 = 600
partes += ejes(X0[1], "La válvula (todo lo que va a la derecha pasa): cuántas hay en cada cámara", ymax2, "partículas",
               [(0, "0"), (150, "150"), (300, "300"), (450, "450"), (600, "600")])
partes.append(linea(X0[1], [(f["t"], f["NR"]) for f in s], ymax2, ROJO))
partes.append(linea(X0[1], [(f["t"], f["NL"]) for f in s], ymax2, AZUL))
partes.append(f'<text x="{X0[1] + PANEL_W - 8}" y="{Y0 + PANEL_H - s[-1]["NR"] / ymax2 * PANEL_H + 18:.1f}" text-anchor="end" font-size="12" fill="{ROJO}">derecha, {s[-1]["NR"]}</text>')
partes.append(f'<text x="{X0[1] + PANEL_W - 8}" y="{Y0 + PANEL_H - s[-1]["NL"] / ymax2 * PANEL_H - 8:.1f}" text-anchor="end" font-size="12" fill="{AZUL}">izquierda, {s[-1]["NL"]}</text>')
tv = res["valvula"]
partes.append(f'<text x="{X0[1] + 10}" y="{Y0 + 24}" font-size="12" fill="{NEGRO}">al final la izquierda quedó más fría ({c(tv["TL"])}) que la derecha ({c(tv["TR"])}):</text>')
partes.append(f'<text x="{X0[1] + 10}" y="{Y0 + 42}" font-size="12" fill="{NEGRO}">las rápidas llegan antes a la puerta y se van primero</text>')

# Panel 3: memoria contra entropía
ymax3 = 1000
partes += ejes(X0[2], "La memoria del demonio (bits · ln 2) y lo que bajó la entropía (−ΔS/k)", ymax3, "nats",
               [(0, "0"), (250, "250"), (500, "500"), (750, "750"), (1000, "1000")])
for nombre, color in (("temperatura", VERDE), ("valvula", "#9b6b1f")):
    s = res[nombre]["serie"]
    partes.append(linea(X0[2], [(f["t"], f["bits"] * LN2) for f in s], ymax3, color))
    partes.append(linea(X0[2], [(f["t"], f["menosDS"]) for f in s], ymax3, color, dash="6 4"))
    ult = s[-1]
    coc = ult["bits"] * LN2 / ult["menosDS"]
    partes.append(f'<text x="{X0[2] + PANEL_W - 8}" y="{Y0 + PANEL_H - ult["menosDS"] / ymax3 * PANEL_H - 6:.1f}" text-anchor="end" font-size="12" fill="{color}">−ΔS/k, {nombre}: {ult["menosDS"]:.0f}</text>')
s = res["temperatura"]["serie"]
partes.append(f'<text x="{X0[2] + 10}" y="{Y0 + 24}" font-size="12" fill="{NEGRO}">línea llena: bits · ln 2 (igual para los dos demonios: {s[-1]["bits"]} llegadas a la puerta)</text>')
partes.append(f'<text x="{X0[2] + 10}" y="{Y0 + 42}" font-size="12" fill="{NEGRO}">línea de trazos: −ΔS/k. Cociente al final: {c(res["temperatura"]["bits"] * LN2 / res["temperatura"]["menosDS"], 1)} (temperatura), {c(res["valvula"]["bits"] * LN2 / res["valvula"]["menosDS"], 1)} (válvula)</text>')
partes.append(f'<text x="{X0[2] + 10}" y="{Y0 + 60}" font-size="12" fill="{NEGRO}">Bennett: la llena nunca puede quedar debajo de la de trazos</text>')

partes.append(f'<text x="{W/2}" y="{H - 14}" text-anchor="middle" font-size="12" fill="#666">demonio.py, semilla {res["temperatura"]["semilla"]}: gas ideal en 2D, k = m = 1, entropía de Sackur-Tetrode por cámara; un bit por cada partícula que llega a la puerta, abra o no</text>')
partes.append("</svg>")
open("demonio.svg", "w", encoding="utf-8").write("\n".join(partes) + "\n")
print("demonio.svg escrita")
