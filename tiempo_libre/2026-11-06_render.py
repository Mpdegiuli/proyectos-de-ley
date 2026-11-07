"""Pasa SVG a PNG con el Chromium de Playwright. Uso: python3 render.py archivo.svg [más.svg] [--ancho 800]
Escribe <nombre>.png al lado de cada SVG. Si un nombre no existe, prueba con la fecha adelante (AAAA-MM-DD_)."""
import sys, pathlib, glob
from playwright.sync_api import sync_playwright

def hallar(nombre):
    p = pathlib.Path(nombre)
    if p.exists():
        return p
    c = sorted(glob.glob(str(p.parent / f"????-??-??_{p.name}")))
    if c:
        return pathlib.Path(c[0])
    raise FileNotFoundError(nombre)

def main():
    args = sys.argv[1:]
    ancho = 800
    if "--ancho" in args:
        i = args.index("--ancho"); ancho = int(args[i + 1]); del args[i:i + 2]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": ancho, "height": ancho}, device_scale_factor=1)
        for a in args:
            svg = hallar(a)
            texto = svg.read_text(encoding="utf-8")
            pg.set_content(f"<html><body style='margin:0;background:white'><div id=d style='width:{ancho}px'>{texto}</div></body></html>")
            pg.add_style_tag(content="svg{width:100%;height:auto;display:block}")
            alto = pg.evaluate("document.getElementById('d').getBoundingClientRect().height")
            pg.set_viewport_size({"width": ancho, "height": int(alto)})
            pg.locator("#d").screenshot(path=str(svg.with_suffix(".png")))
            print("escrito", svg.with_suffix(".png"))
        b.close()

if __name__ == "__main__":
    main()
