#!/usr/bin/env python3
"""Pasa SVG a PNG con el Chromium de Playwright, sin tocar el SVG.

Uso: python3 render.py archivo.svg [otro.svg ...] [--ancho 1600]
Escribe archivo.png al lado de cada SVG. Necesita `pip install playwright` y un Chromium
(`playwright install chromium`); acá ya estaban.
"""
import os
import re
import sys


def medidas(svg):
    m = re.search(r'viewBox="([^"]+)"', svg)
    if m:
        x, y, w, h = [float(v) for v in m.group(1).replace(",", " ").split()]
        return w, h
    return 800.0, 600.0


def main():
    from playwright.sync_api import sync_playwright
    ancho = 1600
    args = []
    resto = sys.argv[1:]
    while resto:
        a = resto.pop(0)
        if a == "--ancho":
            ancho = int(resto.pop(0))
        elif not a.startswith("--"):
            args.append(a)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for ruta in args:
            svg = open(ruta, encoding="utf-8").read()
            w, h = medidas(svg)
            escala = ancho / w
            pag = nav.new_page(viewport={"width": int(w * escala), "height": int(h * escala)})
            html = ('<!doctype html><html><body style="margin:0;background:#fff">'
                    '<div style="width:%dpx;height:%dpx">%s</div></body></html>'
                    % (int(w * escala), int(h * escala),
                       re.sub(r'<svg\b', '<svg style="width:100%;height:100%" ', svg, count=1)))
            pag.set_content(html)
            salida = os.path.splitext(ruta)[0] + ".png"
            pag.screenshot(path=salida, full_page=True)
            pag.close()
            print(salida)
        nav.close()


if __name__ == "__main__":
    main()
