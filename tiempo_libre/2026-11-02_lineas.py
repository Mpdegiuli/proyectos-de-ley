#!/usr/bin/env python3
"""Pasa un dibujo por televisión: 30 líneas (Baird, 1929), 240 (Baird, 1936) y 405 (Marconi-EMI, 1936).

Uso: python3 lineas.py [dibujos/14.svg] [12 8 ...: otros barridos verticales, lineas_N.png]
Lee el SVG, lo pasa a PNG en gris (con render.py, que usa el Chromium de Playwright), y escribe:
  - treinta_lineas.svg: el dibujo en 30 líneas verticales (Baird barría en vertical), vector,
    cada línea como una pila de rectángulos grises de ancho fijo (run-length, 8 grises);
  - treinta_lineas.png, doscientas_cuarenta.png, cuatrocientas_cinco.png: cada barrido solo;
  - lineas.png: los tres paneles juntos, con el original a la izquierda.
Necesita Pillow y numpy, más lo que pide render.py.
"""
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
GRISES = 8


def a_png(svg):
    png = os.path.splitext(svg)[0] + ".png"
    if not os.path.exists(png):
        subprocess.run([sys.executable, os.path.join(AQUI, "render.py"), svg, "--ancho", "1200"], check=True)
    return png


def barrido(gris, lineas, vertical, muestras):
    """Devuelve una matriz (lineas × muestras) de grises promediados.
    vertical=True: las líneas son columnas (Baird 30); False: filas."""
    im = gris
    if vertical:
        im = im.transpose(Image.Transpose.TRANSPOSE)  # ahora cada fila es una línea vertical del original
    chico = im.resize((muestras, lineas), Image.Resampling.BOX)
    a = np.asarray(chico, dtype=np.float32)
    q = np.round(a / 255 * (GRISES - 1)) / (GRISES - 1) * 255  # cuantizar
    return q.astype(np.uint8)


def pintar(mat, vertical, ancho, alto, hueco=0.25):
    """Dibuja la matriz como líneas con un hueco oscuro entre ellas (para que se vea el barrido)."""
    lineas, muestras = mat.shape
    img = Image.new("L", (ancho, alto), 0)
    d = ImageDraw.Draw(img)
    if vertical:
        paso = ancho / lineas
        grosor = max(1, int(paso * (1 - hueco)))
        for i in range(lineas):
            x0 = int(i * paso)
            for j in range(muestras):
                y0, y1 = int(j * alto / muestras), int((j + 1) * alto / muestras)
                d.rectangle([x0, y0, x0 + grosor - 1, max(y0, y1 - 1)], fill=int(mat[i, j]))
    else:
        paso = alto / lineas
        grosor = max(1, int(round(paso * (1 - hueco))))
        for i in range(lineas):
            y0 = int(i * paso)
            for j in range(muestras):
                x0, x1 = int(j * ancho / muestras), int((j + 1) * ancho / muestras)
                d.rectangle([x0, y0, max(x0, x1 - 1), y0 + grosor - 1], fill=int(mat[i, j]))
    return img


def svg_treinta(mat, w, h):
    """30 líneas verticales como rectángulos (run-length por línea)."""
    lineas, muestras = mat.shape
    paso = w / lineas
    grosor = paso * 0.75
    partes = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" width="%g" height="%g">' % (w, h, w, h),
              '<rect width="%g" height="%g" fill="#000"/>' % (w, h)]
    for i in range(lineas):
        x = i * paso
        j = 0
        while j < muestras:
            k = j
            while k + 1 < muestras and mat[i, k + 1] == mat[i, j]:
                k += 1
            g = int(mat[i, j])
            if g > 0:
                y0 = j * h / muestras
                y1 = (k + 1) * h / muestras
                partes.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#%02x%02x%02x"/>'
                              % (x, y0, grosor, y1 - y0, g, g, g))
            j = k + 1
    partes.append("</svg>")
    return "\n".join(partes)


def rotulo(img, texto):
    d = ImageDraw.Draw(img)
    try:
        fuente = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except Exception:
        fuente = ImageFont.load_default()
    d.rectangle([0, img.height - 30, img.width, img.height], fill=20)
    d.text((8, img.height - 26), texto, fill=255, font=fuente)
    return img


def main():
    svg = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "dibujos", "14.svg")
    png = a_png(svg)
    original = Image.open(png).convert("L")
    w, h = original.size
    alto = 480
    ancho = int(w * alto / h)
    paneles = []
    base = original.resize((ancho, alto), Image.Resampling.LANCZOS)
    paneles.append(rotulo(base.copy(), "original"))
    # 30 líneas verticales, 12,5 cuadros por segundo (Baird, 1929): 30 columnas, ~70 muestras por columna
    m30 = barrido(original, 30, True, 70)
    p30 = pintar(m30, True, ancho, alto)
    p30.save(os.path.join(AQUI, "treinta_lineas.png"))
    with open(os.path.join(AQUI, "treinta_lineas.svg"), "w", encoding="utf-8") as f:
        f.write(svg_treinta(m30, 300, 300 * h / w))
    paneles.append(rotulo(p30.copy(), "30 lineas verticales (Baird, 1929)"))
    # 240 líneas horizontales, 25 cuadros (Baird, 1936)
    m240 = barrido(original, 240, False, 320)
    p240 = pintar(m240, False, ancho, alto, hueco=0.0)
    p240.save(os.path.join(AQUI, "doscientas_cuarenta.png"))
    paneles.append(rotulo(p240.copy(), "240 lineas (Baird, 1936)"))
    # 405 líneas, 50 campos entrelazados (Marconi-EMI, 1936); acá se muestra un campo de 202 líneas y el otro
    m405 = barrido(original, 405, False, 500)
    p405 = pintar(m405, False, ancho, 810, hueco=0.0).resize((ancho, alto), Image.Resampling.LANCZOS)
    p405.save(os.path.join(AQUI, "cuatrocientas_cinco.png"))
    paneles.append(rotulo(p405.copy(), "405 lineas (Marconi-EMI, 1936)"))
    hoja = Image.new("L", (ancho * 4 + 30, alto + 20), 40)
    for i, p in enumerate(paneles):
        hoja.paste(p, (10 + i * (ancho + 3), 10))
    hoja.save(os.path.join(AQUI, "lineas.png"))
    print("escritos: treinta_lineas.svg/.png, doscientas_cuarenta.png, cuatrocientas_cinco.png, lineas.png")
    # barridos verticales con otras cantidades de líneas (para la prueba de reconocimiento): python3 lineas.py svg 12 8
    for n in sys.argv[2:]:
        n = int(n)
        mn = barrido(original, n, True, max(8, int(70 * n / 30)))
        pintar(mn, True, ancho, alto).save(os.path.join(AQUI, "lineas_%d.png" % n))
        print("lineas_%d.png" % n)


if __name__ == "__main__":
    main()
