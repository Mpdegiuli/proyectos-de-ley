"""Pasa un SVG a PNG con el Chromium de Playwright, sin tocar el SVG.  Uso: python3 render.py entrada.svg salida.png"""
import sys, re, asyncio
from playwright.async_api import async_playwright

async def main(ent, sal):
    svg = open(ent, encoding="utf-8").read()
    m = re.search(r"<svg[^>]*\swidth='(\d+)'[^>]*\sheight='(\d+)'", svg)
    w, h = (int(m.group(1)), int(m.group(2))) if m else (900, 900)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        await pg.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
        await pg.screenshot(path=sal, clip={"x": 0, "y": 0, "width": w, "height": h})
        await b.close()
    print("escrito", sal)

asyncio.run(main(sys.argv[1], sys.argv[2]))
