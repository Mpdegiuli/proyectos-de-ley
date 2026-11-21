#!/usr/bin/env python3
"""Convierte un SVG en PNG con el Chromium de Playwright. Uso: python3 render.py entrada.svg salida.png"""
import sys
from playwright.sync_api import sync_playwright

svg, png = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(device_scale_factor=2)
    pg.goto("file://" + __import__("os").path.abspath(svg))
    el = pg.query_selector("svg")
    el.screenshot(path=png)
    b.close()
print("escrito", png)
