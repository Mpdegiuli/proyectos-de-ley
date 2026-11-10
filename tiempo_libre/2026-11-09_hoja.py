#!/usr/bin/env python3
"""Saca los siete SVG de instancias_frescas.md a dibujos/ (si no están) y arma hoja.svg:
siete dibujos de 800 × 800 reducidos, con su código (a1, a2, a3, n1, n2, x1, x2) y una línea
de lo que cada instancia declaró (lineas.json). Los ids internos de cada SVG se prefijan
con su código para que los degradados de uno no pisen los del otro."""
import json
import os
import re

MD = "instancias_frescas.md"
if not os.path.exists(MD):
    import glob
    cands = glob.glob("*_instancias_frescas.md")
    MD = cands[0]
texto = open(MD, encoding="utf-8").read()

CODIGOS = ["a1", "a2", "a3", "n1", "n2", "x1", "x2"]
os.makedirs("dibujos", exist_ok=True)
svgs = {}
for cod in CODIGOS:
    ruta = f"dibujos/{cod}.svg"
    if not os.path.exists(ruta):
        i = texto.index(f"\n## {cod} ")
        j = texto.find("\n## ", i + 1)
        bloque = texto[i:j if j > 0 else None]
        a = bloque.index("<svg")
        b = bloque.index("</svg>") + len("</svg>")
        open(ruta, "w", encoding="utf-8").write(bloque[a:b] + "\n")
    svgs[cod] = open(ruta, encoding="utf-8").read()

lineas = json.load(open("lineas.json", encoding="utf-8"))

def prefijar(svg, pre):
    ids = re.findall(r'\bid="([^"]+)"', svg)
    for i in sorted(set(ids), key=len, reverse=True):
        svg = svg.replace(f'id="{i}"', f'id="{pre}_{i}"')
        svg = svg.replace(f'url(#{i})', f'url(#{pre}_{i})')
        svg = svg.replace(f'href="#{i}"', f'href="#{pre}_{i}"')
        svg = re.sub(rf'(aria-labelledby=")([^"]*)\b{re.escape(i)}\b', rf'\g<1>\g<2>{pre}_{i}'.replace(f'{pre}_{i}', f'{pre}_{i}'), svg)
    # quitar el ancho/alto fijo del svg raíz y convertirlo en svg anidado
    svg = re.sub(r'<svg\b[^>]*>', lambda m: re.sub(r'\s(width|height)="[^"]*"', '', m.group(0)), svg, count=1)
    return svg

W, CELL, GAP, TOP, LEG = 1240, 300, 20, 60, 104
filas = [["a1", "a2", "a3"], ["n1", "n2"], ["x1", "x2"]]
titulos = ["Dibujá un apagón (es / en / zh)", "Nueva York, la noche del 9 de noviembre de 1965 (es / en)",
           "Un apagón que no pueda existir (es / en)"]
H = TOP + len(filas) * (CELL + LEG + 40)
out = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" '
       f'width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif" font-size="12">',
       '<rect width="100%" height="100%" fill="#fbfaf6"/>',
       '<text x="20" y="34" font-size="18" font-weight="bold">Siete dibujos de instancias frescas, 9/11/2026</text>']
y = TOP
for fila, titulo in zip(filas, titulos):
    out.append(f'<text x="20" y="{y-8}" font-size="14" font-weight="bold">{titulo}</text>')
    x = 20
    for cod in fila:
        out.append(f'<svg x="{x}" y="{y}" width="{CELL}" height="{CELL}" viewBox="0 0 800 800">{prefijar(svgs[cod], cod)}</svg>')
        out.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="none" stroke="#999"/>')
        out.append(f'<text x="{x+6}" y="{y+CELL+16}" font-weight="bold">{cod}</text>')
        # declaración, partida en renglones de ~62 caracteres
        palabras = lineas[cod].split()
        reng, actual = [], ""
        for w in palabras:
            if len(actual) + len(w) + 1 > 50:
                reng.append(actual); actual = w
            else:
                actual = (actual + " " + w).strip()
        reng.append(actual)
        for k, r in enumerate(reng[:6]):
            out.append(f'<text x="{x+6}" y="{y+CELL+32+k*14}" fill="#333">{r.replace("&", "&amp;").replace("<", "&lt;")}</text>')
        x += CELL + GAP
    y += CELL + LEG + 40
out.append('</svg>')
open("hoja.svg", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("hoja.svg escrito;", len(svgs), "dibujos en dibujos/")
