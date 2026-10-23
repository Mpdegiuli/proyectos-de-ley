#!/usr/bin/env python3
"""render.py — dibuja cada dibujo.svg con Chromium (playwright) y guarda un PNG.
Uso: python3 render.py [carpeta corridas] [carpeta de salida]
Necesita playwright con Chromium y Pillow. Borrador de tiempo libre (10/10/2026)."""
import os, sys, asyncio, base64, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import soles
from playwright.async_api import async_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else 'corridas'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'png'
ANCHO = 640

async def main():
    os.makedirs(OUT, exist_ok=True)
    lista = list(soles.listar(BASE))
    indice = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pag = await b.new_page(viewport={'width': ANCHO, 'height': ANCHO})
        for k, d in enumerate(lista):
            nombre = f"{d['serie']}__{d['consigna']}__{d['casa']}_{d['rep']}.png"
            dest = os.path.join(OUT, nombre)
            indice.append(dict(d, png=dest))
            if os.path.exists(dest):
                continue
            root, txt = soles.leer_svg(d['ruta'])
            if root is None:
                continue
            vb = soles.lienzo(root)
            alto = max(50, min(1400, int(ANCHO * vb[3] / vb[2])))
            await pag.set_viewport_size({'width': ANCHO, 'height': alto})
            uri = 'data:image/svg+xml;base64,' + base64.b64encode(txt.encode('utf-8')).decode()
            html = f'<html><body style="margin:0;background:#fff"><img src="{uri}" style="width:{ANCHO}px;height:{alto}px;display:block"></body></html>'
            try:
                await pag.set_content(html, wait_until='load')
                await pag.wait_for_timeout(120)
                await pag.screenshot(path=dest)
            except Exception as e:
                print('falló', d['ruta'], e, file=sys.stderr)
        await b.close()
    json.dump(indice, open(os.path.join(OUT, 'indice.json'), 'w'), ensure_ascii=False)
    print(len(indice), 'dibujos;', sum(os.path.exists(i['png']) for i in indice), 'PNG')

asyncio.run(main())
