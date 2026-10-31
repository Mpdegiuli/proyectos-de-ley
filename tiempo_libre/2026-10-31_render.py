#!/usr/bin/env python3
"""Pasa los SVG del día a PNG con el Chromium de Playwright, sin tocar el SVG.

Uso: python3 render.py [archivo.svg ...]   (sin argumentos: contrasenas.svg y codigo.svg,
con o sin la fecha adelante). Pide `pip install playwright` y un Chromium instalado.
"""
import os
import sys

from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))


def buscar(nombre):
    for cand in (nombre, "2026-10-31_" + nombre):
        p = os.path.join(AQUI, cand)
        if os.path.exists(p):
            return p
    sys.exit(f"no encuentro {nombre}")


def main():
    archivos = sys.argv[1:] or ["contrasenas.svg", "codigo.svg"]
    with sync_playwright() as pw:
        navegador = pw.chromium.launch()
        pagina = navegador.new_page(device_scale_factor=2)
        for a in archivos:
            ruta = buscar(a)
            svg = open(ruta, encoding="utf-8").read()
            pagina.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
            el = pagina.query_selector("svg")
            salida = ruta[:-4] + ".png"
            el.screenshot(path=salida)
            print("escrito", salida)
        navegador.close()


if __name__ == "__main__":
    main()
