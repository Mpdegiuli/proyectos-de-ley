#!/usr/bin/env python3
"""Pasa un SVG a PNG con el Chromium de Playwright, sin tocar el SVG.
Uso: python3 render.py archivo.svg [salida.png]
"""
import re
import sys
from playwright.sync_api import sync_playwright

src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else src.rsplit(".", 1)[0] + ".png"
svg = open(src, encoding="utf-8").read()
m = re.search(r'<svg[^>]*\swidth="(\d+)"[^>]*\sheight="(\d+)"', svg)
w, h = (int(m.group(1)), int(m.group(2))) if m else (1000, 600)
html = f'<!doctype html><html><body style="margin:0;background:#fff">{svg}</body></html>'
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
    pg.set_content(html)
    pg.screenshot(path=dst, full_page=True)
    b.close()
print("escrito", dst, w, h)
