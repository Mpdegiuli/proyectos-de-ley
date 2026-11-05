#!/usr/bin/env python3
"""Saca los SVG de instancias_frescas.md (bloques ```svg con su etiqueta ### e1 (es), g2 (zh)...),
los escribe uno por archivo en dibujos/ y arma hoja.svg con los diez en dos renglones:
los seis "Dibujá el demonio de Maxwell" (es, en, zh), y abajo los dos "como una válvula" y los dos
"lo que cuesta olvidar un bit". Los ids internos (degradados, marcadores, símbolos) se prefijan con la
etiqueta para que no choquen en la hoja. Solo biblioteca estándar. Busca el .md por el nombre sin fecha
y, si no está, con la fecha adelante, para correr desde tiempo_libre/."""
import os, re, sys

def hallar(nombre):
    for cand in (nombre, "2026-11-05_" + nombre):
        if os.path.exists(cand):
            return cand
    sys.exit(f"no encuentro {nombre}")

texto = open(hallar("instancias_frescas.md"), encoding="utf-8").read()
bloques = []
for seccion in texto.split("\n### ")[1:]:
    m = re.match(r"([a-z]\d) \(([a-z]{2})\)", seccion)
    s = re.search(r"```svg\n(.*?)\n```", seccion, re.S)
    if m and s:
        bloques.append((m.group(1), m.group(2), s.group(1)))
os.makedirs("dibujos", exist_ok=True)
dib = {}
for etiq, idioma, svg in bloques:
    dib[etiq] = (idioma, svg)
    with open(f"dibujos/{etiq}.svg", "w", encoding="utf-8") as f:
        f.write(svg + "\n")
print(f"{len(dib)} dibujos escritos en dibujos/: {' '.join(sorted(dib))}")

def viewbox(svg):
    m = re.search(r'viewBox="([\d.\s-]+)"', svg)
    x, y, w, h = map(float, m.group(1).split())
    return x, y, w, h

PRESENTACION = ("fill", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin", "opacity", "font-family")

def inner(svg, etiq):
    """Contenido del <svg> sin la etiqueta exterior, con los ids prefijados. Los atributos de presentación
    que la instancia puso en la etiqueta exterior (h2 y g1 ponen font-family en el <svg>) se conservan en
    un <g> que envuelve todo, para que el dibujo se vea como lo entregó."""
    apertura = re.match(r"^\s*<svg[^>]*>", svg, flags=re.S).group(0)
    cuerpo = re.sub(r"^\s*<svg[^>]*>", "", svg, count=1, flags=re.S)
    cuerpo = re.sub(r"</svg>\s*$", "", cuerpo, flags=re.S)
    attrs = " ".join(m.group(0) for m in re.finditer(r'\b(?:%s)="[^"]*"' % "|".join(PRESENTACION), apertura))
    if attrs:
        cuerpo = f"<g {attrs}>{cuerpo}</g>"
    ids = re.findall(r'\sid="([^"]+)"', cuerpo)
    for i in sorted(set(ids), key=len, reverse=True):
        cuerpo = cuerpo.replace(f'id="{i}"', f'id="{etiq}_{i}"')
        cuerpo = cuerpo.replace(f'url(#{i})', f'url(#{etiq}_{i})')
        cuerpo = cuerpo.replace(f'href="#{i}"', f'href="#{etiq}_{i}"')
    return cuerpo

FILAS = [
    ("Dibujá el demonio de Maxwell / Draw Maxwell's demon / 画出麦克斯韦妖", ["e1", "e2", "f1", "f2", "g1", "g2"]),
    ("Dibujá al demonio de Maxwell como Maxwell pidió que lo llamaran: una válvula   ·   Dibujá lo que cuesta olvidar un bit", ["h1", "h2", "i1", "i2"]),
]
CELDA, MARGEN, TITULO = 300, 16, 30
ancho = MARGEN + 6 * (CELDA + MARGEN)
alto = MARGEN + sum(TITULO + CELDA + MARGEN for _ in FILAS)
partes = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}">',
          f'<rect width="{ancho}" height="{alto}" fill="#f4f1ea"/>']
y = MARGEN
for titulo, etiqs in FILAS:
    partes.append(f'<text x="{MARGEN}" y="{y + 20}" font-family="Helvetica, Arial, sans-serif" font-size="15" fill="#333">{titulo.replace("<", "&lt;").replace(">", "&gt;")}</text>')
    y += TITULO
    x = MARGEN
    for e in etiqs:
        idioma, svg = dib[e]
        vx, vy, vw, vh = viewbox(svg)
        esc = min(CELDA / vw, CELDA / vh)
        dx = x + (CELDA - vw * esc) / 2
        dy = y + (CELDA - vh * esc) / 2
        partes.append(f'<rect x="{x}" y="{y}" width="{CELDA}" height="{CELDA}" fill="#ffffff" stroke="#ccc"/>')
        partes.append(f'<svg x="{dx:.1f}" y="{dy:.1f}" width="{vw * esc:.1f}" height="{vh * esc:.1f}" viewBox="{vx:g} {vy:g} {vw:g} {vh:g}">{inner(svg, e)}</svg>')
        partes.append(f'<text x="{x + 4}" y="{y + CELDA - 5}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#666">{e} {idioma}</text>')
        x += CELDA + MARGEN
    y += CELDA + MARGEN
partes.append("</svg>")
open("hoja.svg", "w", encoding="utf-8").write("\n".join(partes) + "\n")
print("hoja.svg escrita")
