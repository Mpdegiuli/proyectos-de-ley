#!/usr/bin/env python3
"""render.py — pasa un SVG a PNG con el Chromium de Playwright (acá no hay cairosvg).
Uso: python3 render.py entrada.svg salida.png [escala]"""
import sys
from playwright.sync_api import sync_playwright

svg, png = sys.argv[1], sys.argv[2]
escala = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
html = "<html><body style='margin:0'>" + open(svg, encoding="utf-8").read() + "</body></html>"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(device_scale_factor=escala)
    pg.set_content(html)
    el = pg.query_selector("svg")
    el.screenshot(path=png)
    b.close()
print(png)
