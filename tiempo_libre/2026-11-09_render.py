#!/usr/bin/env python3
"""Pasa SVG a PNG con el Chromium de Playwright: python3 render.py archivo.svg [más.svg ...]"""
import asyncio
import pathlib
import sys
from playwright.async_api import async_playwright


async def main(rutas):
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for ruta in rutas:
            ruta = pathlib.Path(ruta)
            svg = ruta.read_text(encoding="utf-8")
            import re
            m = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', svg)
            w, h = (int(float(m.group(1))), int(float(m.group(2)))) if m else (800, 800)
            page = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            await page.set_content(f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
            await page.screenshot(path=str(ruta.with_suffix(".png")), clip={"x": 0, "y": 0, "width": w, "height": h})
            await page.close()
            print(ruta.with_suffix(".png"))
        await b.close()

asyncio.run(main(sys.argv[1:]))
