#!/usr/bin/env python3
"""Convierte SVG a PNG con el Chromium de Playwright (no hay cairosvg en este entorno).
Uso: python3 2026-11-22_render.py archivo.svg [más.svg ...]   → archivo.png al lado.
"""
import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

async def main(paths):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for s in paths:
            s = Path(s)
            svg = s.read_text(encoding="utf-8")
            page = await browser.new_page(device_scale_factor=2)
            await page.set_content(f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
            el = await page.query_selector("svg")
            await el.screenshot(path=str(s.with_suffix(".png")))
            await page.close()
            print("→", s.with_suffix(".png").name)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
