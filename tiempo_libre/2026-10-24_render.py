#!/usr/bin/env python3
"""Pasa un SVG a PNG con el Chromium de Playwright, sin tocar el SVG.

Uso: render.py entrada.svg salida.png [ancho_px]

El SVG se mete tal cual en una página en blanco y se le saca una captura del
elemento. Si el SVG no trae width/height, se usa el viewBox a escala.
"""
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> None:
    entrada, salida = Path(sys.argv[1]), Path(sys.argv[2])
    ancho = int(sys.argv[3]) if len(sys.argv) > 3 else 800
    svg = entrada.read_text(encoding="utf-8")
    m = re.search(r'viewBox="\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)', svg)
    if m:
        vw, vh = float(m.group(3)), float(m.group(4))
    else:
        vw = vh = 400.0
    alto = round(ancho * vh / vw)
    # Forzar el tamaño de salida sin cambiar la geometría interna: solo se
    # tocan los atributos width/height de la etiqueta <svg> de apertura (no
    # los de un <rect> de fondo, que fue el error de la primera versión).
    fin = svg.index(">", svg.index("<svg")) + 1
    apertura, resto = svg[:fin], svg[fin:]
    apertura = re.sub(r'\s(width|height)="[^"]*"', "", apertura)
    apertura = apertura.replace("<svg", f'<svg width="{ancho}" height="{alto}"', 1)
    svg_mostrado = apertura + resto
    html = (
        "<!doctype html><html><body style='margin:0;background:#fff'>"
        f"<div id='d' style='width:{ancho}px;height:{alto}px'>{svg_mostrado}</div></body></html>"
    )
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": ancho, "height": alto}, device_scale_factor=1)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        pg.locator("#d").screenshot(path=str(salida))
        b.close()
    print(f"{entrada.name} -> {salida} ({ancho}x{alto})")


if __name__ == "__main__":
    main()
