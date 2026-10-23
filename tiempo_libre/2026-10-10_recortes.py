#!/usr/bin/env python3
"""recortes.py — una hoja con un recorte ampliado de cada sol anotado, para mirar cara y rayos."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '.')
from veredicto import S, A
clave = json.load(open('hojas.json')); cands = json.load(open('candidatos.json'))
por = {}
for c in cands: por.setdefault(c['ruta'], {})[c['i']] = c
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
def recorte(k, L, lado=300, k_r=3.4):
    r = clave[k]; c = por[r['ruta']][r['letras'][L]]
    im = Image.open(r['png']).convert('RGB'); W, H = im.size; vb = c['vb']
    px = (c['x'] - vb[0]) / vb[2] * W; py = (c['y'] - vb[1]) / vb[3] * H; pr = max(8, c['r'] / vb[2] * W)
    m = pr * k_r / 2 * 1.0
    m = max(m, 40)
    caja = (int(px - m), int(py - m), int(px + m), int(py + m))
    lienzo = Image.new('RGB', (int(2 * m), int(2 * m)), '#555')
    src = im.crop((max(0, caja[0]), max(0, caja[1]), min(W, caja[2]), min(H, caja[3])))
    lienzo.paste(src, (max(0, -caja[0]), max(0, -caja[1])))
    return lienzo.resize((lado, lado), Image.LANCZOS)
def hoja(dic, pref, cols=6, filas=4):
    ks = list(dic.items())
    for h in range(0, len(ks), cols * filas):
        tr = ks[h:h + cols * filas]
        im = Image.new('RGB', (cols * 306 + 6, filas * 306 + 6), '#222'); dr = ImageDraw.Draw(im)
        for j, (k, L) in enumerate(tr):
            x = 6 + (j % cols) * 306; y = 6 + (j // cols) * 306
            im.paste(recorte(k, L), (x, y))
            dr.rectangle([x, y, x + 62, y + 22], fill='#000'); dr.text((x + 3, y + 1), k, fill='#fff', font=F)
        n = f'recorte_{pref}_{h // (cols * filas):02d}.png'; im.save(n); print(n, len(tr))
hoja(S, 's'); hoja(A, 'a')
