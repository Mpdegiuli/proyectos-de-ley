"""Pasa un SVG a PNG con el Chromium de Playwright. Uso: python3 render.py archivo.svg [escala]"""
import sys, os
from playwright.sync_api import sync_playwright
src = sys.argv[1]
escala = float(sys.argv[2]) if len(sys.argv) > 2 else 2
svg = open(src, encoding="utf-8").read()
import re
m = re.search(r'width="(\d+)" height="(\d+)"', svg)
w, h = int(m.group(1)), int(m.group(2))
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=escala)
    pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
    pg.screenshot(path=os.path.splitext(src)[0] + ".png", full_page=True)
    b.close()
print(os.path.splitext(src)[0] + ".png")
