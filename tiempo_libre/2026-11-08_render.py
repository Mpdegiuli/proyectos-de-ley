#!/usr/bin/env python3
"""render.py — pasa SVG a PNG con el Chromium de Playwright.
Uso: python3 render.py archivo.svg [más.svg ...]   (escribe archivo.png al lado)
Sin argumentos: dibujos/*.svg, hoja.svg y caida.svg si existen.
"""
import glob, os, sys
from playwright.sync_api import sync_playwright

def main():
    archivos = sys.argv[1:] or sorted(glob.glob("dibujos/*.svg")) + [f for f in ("hoja.svg", "hoja_ciega.svg", "figura.svg", "begriffsschrift.svg") if os.path.exists(f)]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(device_scale_factor=2)
        for f in archivos:
            svg = open(f, encoding="utf-8").read()
            import re
            m = re.search(r'viewBox="([\d.\s-]+)"', svg)
            w, h = (400, 400)
            if m:
                vb = m.group(1).split()
                w, h = float(vb[2]), float(vb[3])
            pg.set_viewport_size({"width": int(w), "height": int(h)})
            pg.set_content(f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
            # forzar el tamaño del svg al viewport
            pg.evaluate("""(wh)=>{const s=document.querySelector('svg'); s.setAttribute('width', wh[0]); s.setAttribute('height', wh[1]);}""", [w, h])
            out = os.path.splitext(f)[0] + ".png"
            pg.screenshot(path=out, full_page=False)
            print(out)
        b.close()

if __name__ == "__main__":
    main()
