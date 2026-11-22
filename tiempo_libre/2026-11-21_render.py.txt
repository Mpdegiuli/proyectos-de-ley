#!/usr/bin/env python3
"""Convierte 2026-11-21_rollos.svg en PNG con el navegador (Playwright/Chromium),
porque en este entorno no hay cairosvg.

  python3 render.py [archivo.svg ...]
"""
import asyncio
import pathlib
import sys

from playwright.async_api import async_playwright


async def main(archivos):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(device_scale_factor=2)
        for a in archivos:
            svg = pathlib.Path(a).read_text(encoding="utf-8")
            await pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
            el = await pg.query_selector("svg")
            await el.screenshot(path=str(pathlib.Path(a).with_suffix(".png")))
            print("Escrito", pathlib.Path(a).with_suffix(".png"))
        await b.close()


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:] or ["2026-11-21_rollos.svg"]))
