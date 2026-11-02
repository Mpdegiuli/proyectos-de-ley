#!/usr/bin/env python3
"""Pasa los SVG de este cuaderno a PNG con el Chromium de Playwright, sin tocar el SVG;
si hay Pillow, deja el PNG en 64 colores para que pese menos.
Uso: python3 render.py [archivo.svg ...]   (sin argumentos: contrarios.svg)
"""
import os
import sys
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))


def main():
    archivos = sys.argv[1:] or ["contrarios.svg"]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for a in archivos:
            ruta = a if os.path.isabs(a) else os.path.join(AQUI, a)
            if not os.path.isfile(ruta):
                base = os.path.basename(ruta)
                # con la fecha adelante, como queda en tiempo_libre/
                cands = [os.path.join(AQUI, f) for f in os.listdir(AQUI) if f.endswith("_" + base)]
                if cands:
                    ruta = cands[0]
            with open(ruta, encoding="utf-8") as f:
                svg = f.read()
            pg.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
            el = pg.query_selector("svg")
            png = os.path.splitext(ruta)[0] + ".png"
            el.screenshot(path=png, scale="device")
            try:  # achica el archivo a 64 colores (la figura tiene seis); si no hay PIL, queda como salió
                from PIL import Image
                im = Image.open(png).convert("RGB").quantize(colors=64, method=Image.Quantize.MEDIANCUT)
                im.save(png, optimize=True)
            except ImportError:
                pass
            print("escrito", png)
        b.close()


if __name__ == "__main__":
    main()
