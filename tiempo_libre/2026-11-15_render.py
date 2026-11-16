"""render.py — hace nada.png a partir de nada.svg con Chromium (Playwright), a escala 2.
Uso: python3 render.py [nada.svg] [nada.png]. Sirve para mirar la figura; el SVG es el original."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

svg = Path(sys.argv[1] if len(sys.argv) > 1 else "nada.svg").resolve()
png = Path(sys.argv[2] if len(sys.argv) > 2 else svg.with_suffix(".png"))
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(device_scale_factor=2)
    pg.goto(svg.as_uri())
    el = pg.query_selector("svg")
    el.screenshot(path=str(png))
    b.close()
print("→", png)
