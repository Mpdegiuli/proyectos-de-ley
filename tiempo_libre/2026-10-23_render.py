#!/usr/bin/env python3
"""Convierte veintitres.svg en veintitres.png con el Chromium de Playwright
(el SVG va incrustado en una página HTML mínima; la captura es del tamaño del SVG)."""
import asyncio, pathlib, re
from playwright.async_api import async_playwright

async def main():
    svg = pathlib.Path("veintitres.svg").read_text(encoding="utf-8")
    w = int(re.search(r"width='(\d+)'", svg).group(1))
    h = int(re.search(r"height='(\d+)'", svg).group(1))
    html = f"<!doctype html><html><body style='margin:0;background:#fcfcfb'>{svg}</body></html>"
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        await pg.set_content(html)
        await pg.screenshot(path="veintitres.png", clip={"x": 0, "y": 0, "width": w, "height": h}, timeout=60000)
        await b.close()
asyncio.run(main())
print("veintitres.png escrito")
