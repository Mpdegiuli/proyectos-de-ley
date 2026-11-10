"""Pasa SVG a PNG con el Chromium de Playwright. Uso: python3 render.py a.svg [b.svg ...]"""
import asyncio
import os
import sys
from playwright.async_api import async_playwright


async def main(rutas):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(device_scale_factor=2)
        for r in rutas:
            svg = open(r, encoding="utf-8").read()
            await pg.set_content('<html><body style="margin:0;background:#fff">' + svg + "</body></html>")
            el = await pg.query_selector("svg")
            await el.screenshot(path=os.path.splitext(r)[0] + ".png")
            print(os.path.splitext(r)[0] + ".png")
        await b.close()

asyncio.run(main(sys.argv[1:]))
