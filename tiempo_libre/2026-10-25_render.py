#!/usr/bin/env python3
"""Pasa un SVG a PNG con el Chromium de Playwright, sin tocar el SVG.

Uso: python3 2026-10-25_render.py entrada.svg salida.png [escala]

Abre el SVG en una página en blanco, lo mide con getBoundingClientRect y
saca la captura del tamaño del dibujo (por defecto a escala 2).
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def render(svg_path: Path, png_path: Path, escala: float = 2.0) -> None:
    svg = svg_path.read_text(encoding="utf-8")
    html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<style>html,body{margin:0;padding:0;background:white}"
        "svg{display:block}</style></head><body>" + svg + "</body></html>"
    )
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page(device_scale_factor=escala)
        pagina.set_content(html)
        caja = pagina.evaluate(
            "() => { const s = document.querySelector('svg');"
            " const r = s.getBoundingClientRect();"
            " return {w: Math.ceil(r.width), h: Math.ceil(r.height)}; }"
        )
        pagina.set_viewport_size({"width": caja["w"], "height": caja["h"]})
        pagina.screenshot(path=str(png_path), full_page=False)
        navegador.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    escala = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
    render(Path(sys.argv[1]), Path(sys.argv[2]), escala)
    print("escrito", sys.argv[2])
