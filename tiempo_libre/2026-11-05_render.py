#!/usr/bin/env python3
"""Pasa uno o más SVG a PNG con el Chromium de Playwright, sin tocar el SVG.
Uso: python3 render.py archivo.svg [otro.svg ...]  (escribe archivo.png al lado)."""
import sys, os
from playwright.sync_api import sync_playwright

def render(ruta_svg, escala=2):
    svg = open(ruta_svg, encoding="utf-8").read()
    html = f"<html><body style='margin:0;background:white'>{svg}</body></html>"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(device_scale_factor=escala)
        pg.set_content(html)
        el = pg.query_selector("svg")
        salida = os.path.splitext(ruta_svg)[0] + ".png"
        el.screenshot(path=salida)
        b.close()
    return salida

if __name__ == "__main__":
    for r in sys.argv[1:]:
        print(render(r))
