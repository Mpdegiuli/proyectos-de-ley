#!/usr/bin/env python3
"""Pasa un SVG a PNG con el Chromium de Playwright, sin tocar el SVG.
Uso: python3 render.py pisadas.svg [pisadas.png] [escala]
"""
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright


def main():
    src = pathlib.Path(sys.argv[1])
    dst = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix('.png')
    escala = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
    svg = src.read_text(encoding='utf-8')
    m = re.search(r'<svg[^>]*?\swidth="([\d.]+)"[^>]*?\sheight="([\d.]+)"', svg)
    w, h = (int(float(m.group(1))), int(float(m.group(2)))) if m else (1000, 700)
    html = f'<!doctype html><html><body style="margin:0;background:#fff">{svg}</body></html>'
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=escala)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(dst), clip={'x': 0, 'y': 0, 'width': w, 'height': h})
        b.close()
    print('escrito', dst)


if __name__ == '__main__':
    main()
