#!/usr/bin/env python3
"""Pasa un SVG a PNG con el Chromium de Playwright, sin tocar el SVG.
Uso: python3 render.py entrada.svg salida.png [escala]
Lee width y height de la etiqueta <svg> (acepta comillas simples o dobles)."""
import asyncio
import os
import re
import sys

from playwright.async_api import async_playwright


async def main(svg, png, scale):
    s = open(svg, encoding="utf-8").read()
    w = int(float(re.search(r"""width=['"]([\d.]+)""", s).group(1)))
    h = int(float(re.search(r"""height=['"]([\d.]+)""", s).group(1)))
    html = svg + ".html"
    open(html, "w", encoding="utf-8").write(f"<html><body style='margin:0;background:white'>{s}</body></html>")
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(device_scale_factor=scale, viewport={"width": w, "height": h})
        await pg.goto("file://" + os.path.abspath(html))
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=png, timeout=180000)
        await b.close()
    os.remove(html)


if __name__ == "__main__":
    svg, png = sys.argv[1], sys.argv[2]
    scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    asyncio.run(main(svg, png, scale))
