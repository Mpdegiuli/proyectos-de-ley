#!/usr/bin/env python3
"""render.py — pasa los SVG del día a PNG con el Chromium de Playwright, sin tocar el SVG."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

AQUI = Path(__file__).parent
archivos = [Path(a) for a in sys.argv[1:]] or sorted(AQUI.glob("*.svg"))
with sync_playwright() as p:
    b = p.chromium.launch()
    for svg in archivos:
        pg = b.new_page(device_scale_factor=2)
        pg.goto(svg.resolve().as_uri())
        el = pg.query_selector("svg")
        el.screenshot(path=str(svg.with_suffix(".png")))
        print("escrito", svg.with_suffix(".png").name)
        pg.close()
    b.close()
