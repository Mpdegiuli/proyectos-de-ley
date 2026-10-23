#!/usr/bin/env python3
"""hojas.py — arma hojas de contacto con los PNG de render.py, para mirar.
Uso: python3 hojas.py png candidatos.json [corridas]
Hojas 'hoja_m_NN.png': dibujos donde el código o el texto nombran un sol, o hay un disco cálido
en la parte alta. Sobre cada dibujo, una letra al lado de cada disco candidato (a = el más grande).
Hojas 'hoja_r_NN.png': todos los demás, más chicos, para controlar lo que el detector no vio.
Cada casilla lleva un número; hojas.json dice qué dibujo es cada número y qué disco es cada letra.
Las hojas no muestran la casa: se mira primero y se abre la clave después."""
import os, sys, json
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import soles

PNG = sys.argv[1]; CAND = sys.argv[2]; BASE = sys.argv[3] if len(sys.argv) > 3 else 'corridas'
indice = json.load(open(os.path.join(PNG, 'indice.json')))
cands = json.load(open(CAND))
por_ruta = {}
for c in cands: por_ruta.setdefault(c['ruta'], []).append(c)

def nombra_sol(d):
    svg = open(d['ruta'], encoding='utf-8', errors='replace').read()
    carp = os.path.dirname(d['ruta']); t = ''
    for f in ('por_que.md', 'que_dibujaste.md', 'por_que_en.md'):
        p = os.path.join(carp, f)
        if os.path.exists(p): t += open(p, encoding='utf-8', errors='replace').read()
    lim = lambda s: soles.PALABRA_NO_SOL.sub('', s)
    return bool(soles.PALABRA_SOL.search(lim(svg))), bool(soles.PALABRA_SOL.search(lim(t)))

marcados, resto = [], []
for d in indice:
    if not os.path.exists(d['png']): continue
    a, b = nombra_sol(d)
    cs = sorted([c for c in por_ruta.get(d['ruta'], []) if c['rW'] >= 0.02], key=lambda c: -c['rW'])[:6]
    d['letras'] = cs
    arriba = any(c['rW'] >= 0.03 and c['alto'] < 0.7 for c in cs)
    d['en_svg'], d['en_txt'], d['disco_arriba'] = a, b, arriba
    (marcados if (a or b or arriba) else resto).append(d)

def fuente(n):
    try: return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', n)
    except OSError: return ImageFont.load_default()
F1, F2 = fuente(22), fuente(15)

def hoja(lista, pref, cols, filas, w, letras):
    clave = {}
    for h in range(0, len(lista), cols * filas):
        trozo = lista[h:h + cols * filas]
        alto = int(w * 0.85)
        im = Image.new('RGB', (cols * (w + 8) + 8, filas * (alto + 8) + 8), '#777')
        dr = ImageDraw.Draw(im)
        for k, d in enumerate(trozo):
            p = Image.open(d['png']).convert('RGB')
            W0, H0 = p.size
            p.thumbnail((w, alto))
            esc = p.width / W0
            x = 8 + (k % cols) * (w + 8); y = 8 + (k // cols) * (alto + 8)
            ox, oy = x + (w - p.width) // 2, y + (alto - p.height) // 2
            im.paste(p, (ox, oy))
            num = h + k
            reg = dict(serie=d['serie'], consigna=d['consigna'], casa=d['casa'], rep=d['rep'], ruta=d['ruta'],
                       png=d['png'], en_svg=d['en_svg'], en_txt=d['en_txt'], disco_arriba=d['disco_arriba'], letras={})
            if letras:
                for j, c in enumerate(d['letras']):
                    vb = c['vb']
                    px = ox + (c['x'] - vb[0]) / vb[2] * W0 * esc
                    py = oy + (c['y'] - vb[1]) / vb[3] * H0 * esc
                    pr = c['r'] / vb[2] * W0 * esc
                    L = 'abcdef'[j]
                    tx, ty = px + pr * 0.75 + 2, py + pr * 0.75 + 2
                    dr.rectangle([tx, ty, tx + 13, ty + 17], fill='#fff', outline='#000')
                    dr.text((tx + 2, ty - 1), L, fill='#d00', font=F2)
                    reg['letras'][L] = c['i']
            dr.rectangle([x, y, x + 52, y + 26], fill='#000')
            dr.text((x + 3, y + 1), str(num), fill='#fff', font=F1)
            clave[f'{pref}{num}'] = reg
        nombre = f'hoja_{pref}_{h // (cols * filas):02d}.png'
        im.save(nombre); print(nombre, len(trozo))
    return clave

clave = {}
clave.update(hoja(marcados, 'm', 4, 3, 470, True))
clave.update(hoja(resto, 'r', 7, 5, 270, False))
json.dump(clave, open('hojas.json', 'w'), ensure_ascii=False, indent=0)
print(len(marcados), 'marcados;', len(resto), 'resto')
