import sys, asyncio, re, os
from playwright.async_api import async_playwright
async def main(svg, png, scale):
    s = open(svg).read()
    w = int(re.search(r'width="(\d+)"', s).group(1)); h = int(re.search(r'height="(\d+)"', s).group(1))
    html = svg + ".html"
    open(html, "w").write(f"<html><body style='margin:0;background:#111'>{s}</body></html>")
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(device_scale_factor=scale, viewport={"width": w, "height": h})
        await pg.goto("file://" + html)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=png, timeout=180000)
        await b.close()
    os.remove(html)
svg, png, scale = sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
asyncio.run(main(svg, png, scale))
