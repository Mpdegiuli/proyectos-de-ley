#!/usr/bin/env python3
"""lunas.py — busca las lunas en los dibujo.svg y mide cómo están hechas.


Uso:  python3 lunas.py [carpeta corridas]      (por defecto: ./corridas)


No llama a nadie y no abre las carpetas del animal (pendientes de la lectura a ciegas de Maia).


Qué busca: un disco claro (círculo, o elipse casi redonda, de radio >= 6) y, dibujado después, otro disco
más oscuro que lo tapa en parte sin quedar adentro. Eso es la "luna de dos círculos". Para cada una mide:
  lado      hacia dónde está corrido el disco que tapa (E = derecha, O = izquierda; N = arriba, S = abajo).
            Tapado a la derecha = luz a la izquierda = forma de C.
  r/R       radio del disco que tapa sobre el radio del disco claro.
  cuernos   cuántos grados del borde del disco claro quedan a la vista. En una fase de verdad son 180.
  k         fracción del diámetro que queda iluminada sobre el eje (0 = nueva, 1 = llena).
  cielo     si lo que hay detrás es un degradado, y si el color del disco que tapa coincide con algo del cielo.
  estrellas cuántos puntos claros chicos caen dentro de la parte tapada y están dibujados después (delante).
También mide las lunas hechas de otro modo: un disco con máscara (el disco negro de la máscara hace de
tapa, pero transparente) y un <path> de dos arcos (se reconstruyen los dos círculos con las reglas de SVG,
incluida la que agranda un radio que no alcanza; si los dos arcos coinciden, el path no pinta nada).
Con --hoja arma hoja_de_lunas.png, un recorte por luna. Con --mirar (necesita playwright y Pillow) dibuja cada SVG con Chromium y mide en la imagen cuánto se
distingue del cielo el disco que tapa: 'contraste' es la distancia, en RGB de 0 a 255, entre la mediana
del color dentro del disco (fuera de la luna) y la mediana en un anillo justo afuera, con signo: positivo
si el disco se ve más claro que lo que lo rodea, negativo si se ve más oscuro.
EXCLUIR es la lista de candidatos que el detector encuentra y que, mirados, no son lunas.
Borrador de una sesión de tiempo libre (1/10/2026): propuesta, no parte del repo.
"""
import re, os, sys, glob, math, json
from xml.etree import ElementTree as ET


BASE = sys.argv[1] if len(sys.argv) > 1 else 'corridas'
NOMBRES = {'white': '#ffffff', 'black': '#000000', 'ivory': '#fffff0', 'lightyellow': '#ffffe0',
           'yellow': '#ffff00', 'gold': '#ffd700', 'navy': '#000080', 'midnightblue': '#191970',
           'beige': '#f5f5dc', 'khaki': '#f0e68c', 'lemonchiffon': '#fffacd', 'cornsilk': '#fff8dc',
           'whitesmoke': '#f5f5f5', 'lightgray': '#d3d3d3', 'lightgrey': '#d3d3d3', 'silver': '#c0c0c0',
           'gray': '#808080', 'grey': '#808080', 'darkblue': '#00008b', 'indigo': '#4b0082',
           'orange': '#ffa500', 'red': '#ff0000', 'blue': '#0000ff', 'skyblue': '#87ceeb',
           'lightblue': '#add8e6', 'purple': '#800080', 'snow': '#fffafa', 'floralwhite': '#fffaf0',
           'aliceblue': '#f0f8ff', 'darkslateblue': '#483d8b', 'wheat': '#f5deb3', 'moccasin': '#ffe4b5'}


def num(s, d=0.0):
    try: return float(re.sub(r'[^0-9.eE+\-]', '', s or '') or d)
    except ValueError: return d


def rgb(c):
    if not c: return None
    c = c.strip().lower(); c = NOMBRES.get(c, c)
    m = re.fullmatch(r'#([0-9a-f]{3})', c)
    if m: return tuple(int(x * 2, 16) for x in m.group(1))
    m = re.fullmatch(r'#([0-9a-f]{6})([0-9a-f]{2})?', c)
    if m: return tuple(int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4))
    m = re.match(r'rgba?\(([^)]+)\)', c)
    if m:
        p = [x for x in re.split(r'[ ,/]+', m.group(1).strip()) if x]
        try: return tuple(int(float(x.rstrip('%')) * (2.55 if x.endswith('%') else 1)) for x in p[:3])
        except ValueError: return None
    return None


def lum(c): return None if c is None else (0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]) / 255
def dist(a, b): return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


# --- transformaciones afines (a, b, c, d, e, f) ---
ID = (1, 0, 0, 1, 0, 0)
def mul(m, n):
    a, b, c, d, e, f = m; a2, b2, c2, d2, e2, f2 = n
    return (a * a2 + c * b2, b * a2 + d * b2, a * c2 + c * d2, b * c2 + d * d2, a * e2 + c * f2 + e, b * e2 + d * f2 + f)
def parse_tr(s):
    m = ID
    for nom, args in re.findall(r'(\w+)\s*\(([^)]*)\)', s or ''):
        v = [float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?', args)]
        if nom == 'translate' and v: t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif nom == 'scale' and v: t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif nom == 'rotate' and v:
            q = math.radians(v[0]); co, si = math.cos(q), math.sin(q); t = (co, si, -si, co, 0, 0)
            if len(v) == 3: t = mul(mul((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
        elif nom == 'matrix' and len(v) == 6: t = tuple(v)
        else: continue
        m = mul(m, t)
    return m
def ap(m, x, y): return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])
def escala(m): return math.sqrt(abs(m[0] * m[3] - m[1] * m[2]))


def estilo(el, attr):
    v = el.get(attr)
    m = re.search(r'(?:^|;)\s*' + attr + r'\s*:\s*([^;]+)', el.get('style') or '')
    return (m.group(1).strip() if m else v)


class Dibujo:
    def __init__(self, ruta):
        self.raiz = ET.parse(ruta).getroot()
        self.grad = {}; self.discos = []; self.fondos = []; self.paths = []; self.mascaras = 0
        vb = [float(x) for x in re.findall(r'[-\d.]+', self.raiz.get('viewBox') or '')]
        self.W = vb[2] if len(vb) == 4 else num(self.raiz.get('width'), 800)
        self.H = vb[3] if len(vb) == 4 else num(self.raiz.get('height'), 600)
        for el in self.raiz.iter():
            tag = el.tag.split('}')[-1]
            if tag in ('linearGradient', 'radialGradient'):
                ps = []
                for s in el:
                    c = rgb(estilo(s, 'stop-color')); o = estilo(s, 'stop-opacity')
                    if c: ps.append((c, num(o, 1.0) if o is not None else 1.0))
                self.grad[el.get('id')] = (tag, ps)
        self.n = 0
        self.rec(self.raiz, ID, None, 1.0, False)


    def color(self, fill):
        """devuelve (rgb representativo, es_degradado, paradas)"""
        if fill is None: return ((0, 0, 0), False, [])
        m = re.match(r'url\(\s*["\']?#([^)"\']+)', fill)
        if m:
            tag, ps = self.grad.get(m.group(1), (None, []))
            if not ps: return (None, True, [])
            cs = [p[0] for p in ps]
            base = cs[0] if tag == 'radialGradient' else tuple(sum(c[i] for c in cs) / len(cs) for i in range(3))
            return (base, True, ps)
        return (rgb(fill), False, [])


    def rec(self, el, m, fill, op, oculto):
        tag = el.tag.split('}')[-1]
        if tag in ('defs', 'clipPath', 'mask', 'symbol', 'pattern', 'filter', 'linearGradient', 'radialGradient'):
            if tag == 'mask': self.mascaras += 1
            return
        m = mul(m, parse_tr(el.get('transform')))
        f = estilo(el, 'fill'); fill = f if f is not None else fill
        o = estilo(el, 'opacity'); op = op * (num(o, 1.0) if o is not None else 1.0)
        fo = estilo(el, 'fill-opacity'); opf = op * (num(fo, 1.0) if fo is not None else 1.0)
        self.n += 1; orden = self.n
        if tag in ('circle', 'ellipse'):
            if tag == 'circle': rx = ry = num(el.get('r'))
            else: rx, ry = num(el.get('rx')), num(el.get('ry'))
            cx, cy = ap(m, num(el.get('cx')), num(el.get('cy'))); s = escala(m)
            if fill != 'none' and rx > 0 and ry > 0:
                col, esg, ps = self.color(fill)
                self.discos.append(dict(x=cx, y=cy, r=math.sqrt(rx * ry) * s, redondo=min(rx, ry) / max(rx, ry),
                                        col=col, grad=esg, paradas=ps, op=opf, orden=orden, fill=fill,
                                        mask=el.get('mask'), clip=el.get('clip-path'),
                                        trazo=estilo(el, 'stroke')))
        elif tag == 'rect':
            w = el.get('width') or ''; h = el.get('height') or ''
            ww = self.W if w.endswith('%') else num(w) * abs(m[0]); hh = self.H * num(h) / 100 if h.endswith('%') else num(h) * abs(m[3])
            if ww >= 0.9 * self.W and hh >= 0.3 * self.H and fill != 'none':
                col, esg, ps = self.color(fill)
                x0, y0 = ap(m, num(el.get('x')), num(el.get('y')))
                self.fondos.append(dict(col=col, grad=esg, paradas=ps, orden=orden, y0=y0, y1=y0 + hh, op=opf, fill=fill))
        elif tag == 'path':
            self.paths.append(dict(d=el.get('d') or '', fill=fill, orden=orden, m=m, mask=el.get('mask')))
        for h in el: self.rec(h, m, fill, op, oculto)


    def cielo_en(self, y, antes_de):
        """color del fondo a la altura y (interpolando degradados lineales verticales, que es lo usual)"""
        f = [b for b in self.fondos if b['orden'] < antes_de and b['y0'] - 1 <= y <= b['y1'] + 1 and b['op'] > 0.5]
        if not f: return None
        b = f[-1]
        if b['grad'] and len(b['paradas']) >= 2:
            cs = [p[0] for p in b['paradas']]
            t = min(max((y - b['y0']) / max(b['y1'] - b['y0'], 1), 0), 1) * (len(cs) - 1)
            i = min(int(t), len(cs) - 2); u = t - i
            return dict(col=tuple(cs[i][k] * (1 - u) + cs[i + 1][k] * u for k in range(3)), grad=True, paradas=cs)
        return dict(col=b['col'], grad=False, paradas=[b['col']] if b['col'] else [])


def lunas_de_dos_circulos(D):
    out = []; ds = D.discos
    for i, A in enumerate(ds):
        if A['r'] < 6 or A['redondo'] < 0.85 or A['op'] < 0.6 or A['col'] is None: continue
        la = lum(A['col'])
        if la < 0.55: continue
        for B in ds:
            if B['orden'] <= A['orden'] or B['redondo'] < 0.85 or B['op'] < 0.6 or B['col'] is None: continue
            d = math.hypot(B['x'] - A['x'], B['y'] - A['y']); R, r = A['r'], B['r']
            if not (0.45 * R <= r <= 4 * R): continue
            if d < 0.04 * R or d >= R + r: continue            # concéntricos (halo) o no se tocan
            if d + r <= R * 1.001: continue                     # el segundo queda adentro (cráter, pupila)
            if d + R <= r * 1.001: continue                     # el primero queda tapado entero
            if lum(B['col']) > la - 0.25: continue              # el que tapa tiene que ser claramente más oscuro
            # ¿hay algo dibujado entre A y B que sea otro disco claro igual (lunas dobles)? se deja pasar
            cosA = (d * d + R * R - r * r) / (2 * d * R); cosA = max(-1, min(1, cosA))
            visto = 360 - 2 * math.degrees(math.acos(cosA))   # grados del borde de A a la vista
            k = max(0.0, min(1.0, (d + R - r) / (2 * R)))        # fracción del diámetro iluminada en el eje
            ang = math.degrees(math.atan2(-(B['y'] - A['y']), B['x'] - A['x']))  # 0 = derecha, 90 = arriba
            cielo = D.cielo_en(A['y'], A['orden'])
            # estrellas delante: discos chicos claros, dibujados después de B, dentro de B y dentro de A
            est = [s for s in ds if s['orden'] > B['orden'] and s['r'] <= max(3.5, 0.12 * R) and s['col'] and lum(s['col']) > 0.6
                   and math.hypot(s['x'] - B['x'], s['y'] - B['y']) < r - s['r'] and math.hypot(s['x'] - A['x'], s['y'] - A['y']) < R - s['r']]
            out.append(dict(A=A, B=B, d=d, rR=r / R, cuernos=visto, k=k, ang=ang, cielo=cielo, estrellas=len(est)))
            break
    return out


def centro_arco(x1, y1, x2, y2, r, fa, fs):
    """centro y radio efectivo de un arco circular de SVG (notas de implementación F.6.5, con rx = ry)"""
    dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
    lam = (dx * dx + dy * dy) / (r * r); agrandado = lam > 1 + 1e-9
    if lam > 1: r = r * math.sqrt(lam)
    den = dx * dx + dy * dy
    co = math.sqrt(max(0.0, (r * r - den) / den)) * (-1 if fa == fs else 1)
    return (co * dy + (x1 + x2) / 2, -co * dx + (y1 + y2) / 2, r, agrandado)


def puntos_arco(x1, y1, x2, y2, cx, cy, r, fa, fs, n=120):
    t1 = math.atan2(y1 - cy, x1 - cx); t2 = math.atan2(y2 - cy, x2 - cx); dt = t2 - t1
    if fs == 0 and dt > 0: dt -= 2 * math.pi
    if fs == 1 and dt < 0: dt += 2 * math.pi
    return [(cx + r * math.cos(t1 + dt * k / n), cy + r * math.sin(t1 + dt * k / n)) for k in range(n + 1)], abs(dt)


def paths_de_luna(D):
    """paths claros y cerrados hechos con exactamente dos arcos: la luna de un solo trazo"""
    out = []
    for p in D.paths:
        d = p['d']; cmds = re.findall(r'[a-zA-Z]', d)
        if [c.upper() for c in cmds] not in (['M', 'A', 'A', 'Z'], ['M', 'A', 'A']) or p['fill'] in (None, 'none'): continue
        col, _, _ = D.color(p['fill'])
        if not col or lum(col) <= 0.55: continue
        v = [float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?', d)]
        if len(v) != 16: continue
        rel = [c for c in cmds if c in 'aA']
        x0, y0 = v[0], v[1]; arcs = []; x, y = x0, y0
        for q in range(2):
            rx, ry, rot, fa, fs, ex, ey = v[2 + 7 * q: 9 + 7 * q]
            if rel[q] == 'a': ex, ey = x + ex, y + ey
            cx, cy, r, agr = centro_arco(x, y, ex, ey, rx, int(fa), int(fs))
            pts, barrido = puntos_arco(x, y, ex, ey, cx, cy, r, int(fa), int(fs))
            arcs.append(dict(cx=cx, cy=cy, r=r, r_escrito=rx, agrandado=agr, pts=pts, barrido=barrido)); x, y = ex, ey
        poli = arcs[0]['pts'] + arcs[1]['pts']
        area = abs(sum(poli[k][0] * poli[k + 1][1] - poli[k + 1][0] * poli[k][1] for k in range(len(poli) - 1))) / 2
        ext, inte = (arcs[0], arcs[1]) if arcs[0]['barrido'] >= arcs[1]['barrido'] else (arcs[1], arcs[0])
        s = escala(p['m']); X, Y = ap(p['m'], ext['cx'], ext['cy']); BX, BY = ap(p['m'], inte['cx'], inte['cy'])
        R, r = ext['r'] * s, inte['r'] * s; dd = math.hypot(BX - X, BY - Y)
        res = dict(x=X, y=Y, R=R, d=d, area=area * s * s / (math.pi * R * R), agrandado=inte['agrandado'] or ext['agrandado'],
                   r_escritos=(arcs[0]['r_escrito'], arcs[1]['r_escrito']), orden=p['orden'])
        if res['area'] < 0.01: res['clase'] = 'no pinta nada'
        else:
            # ¿los dos arcos se curvan hacia el mismo lado (creciente) o hacia lados opuestos (lente)?
            mx, my = (poli[0][0] + arcs[0]['pts'][-1][0]) / 2, (poli[0][1] + arcs[0]['pts'][-1][1]) / 2
            a, b = arcs[0]['pts'][60], arcs[1]['pts'][60]
            mismo = ((a[0] - mx) * (b[0] - mx) + (a[1] - my) * (b[1] - my)) > 0
            res['clase'] = 'creciente' if mismo else 'lente'
            if mismo and dd > 0:
                res.update(medidas(R, r, dd, math.degrees(math.atan2(-(BY - Y), BX - X))))
        out.append(res)
    return out


def medidas(R, r, d, ang):
    cosA = max(-1, min(1, (d * d + R * R - r * r) / (2 * d * R)))
    return dict(rR=r / R, cuernos=360 - 2 * math.degrees(math.acos(cosA)), k=max(0.0, min(1.0, (d + R - r) / (2 * R))), ang=ang)


def lunas_con_mascara(D):
    """disco claro con mask=...: el disco negro de la máscara hace de tapa"""
    out = []; masks = {}
    for el in D.raiz.iter():
        if el.tag.split('}')[-1] == 'mask':
            masks[el.get('id')] = [(num(c.get('cx')), num(c.get('cy')), num(c.get('r')), rgb(estilo(c, 'fill') or 'black'))
                                   for c in el.iter() if c.tag.split('}')[-1] == 'circle']
    for A in D.discos:
        m = re.match(r'url\(\s*["\']?#([^)"\']+)', A['mask'] or '')
        if not m or A['r'] < 6 or not A['col'] or lum(A['col']) <= 0.55: continue
        negros = [c for c in masks.get(m.group(1), []) if c[3] is not None and lum(c[3]) < 0.3]
        if len(negros) != 1: continue
        bx, by, r, _ = negros[0]; d = math.hypot(bx - A['x'], by - A['y'])
        if d < 0.04 * A['r'] or d >= A['r'] + r: continue
        res = dict(x=A['x'], y=A['y'], R=A['r'], orden=A['orden'])
        res.update(medidas(A['r'], r, d, math.degrees(math.atan2(-(by - A['y']), bx - A['x']))))
        out.append(res)
    return out


def lado(ang):
    ew = 'E' if abs(ang) < 67.5 else ('O' if abs(ang) > 112.5 else '')
    ns = 'N' if 22.5 < ang < 157.5 else ('S' if -157.5 < ang < -22.5 else '')
    return ns + ew


# candidatos que el detector encuentra y que, mirados en la hoja de contactos, no son lunas
EXCLUIR = {('mundo', 'es', 'qwen3.8-max_1'): 'sol detrás del planeta',
           ('persona', 'es', 'qwen3.8-max_1'): 'sol detrás del pelo',
           ('persona_imposible', 'es', 'claude-haiku-4-5_1'): 'ojo',
           ('puente_inexistente', 'es', 'grok-4.6_1'): 'luna llena detrás de los árboles',
           ('mundo', 'en', 'gpt-6-sol_1'): 'sol detrás del planeta',
           ('mundo', 'en', 'kimi-k3_1', 'N'): 'sol en el horizonte',
           ('mundo', 'es', 'gpt-5.5-2026-04-23_1'): 'sol con rayos tapado por un globo oscuro',
           ('libre', 'zh', 'gemini-3.1-pro-preview_1'): 'sol con máscara de rayas',
           ('casa_inexistente', 'es', 'claude-sonnet-5-5_1'): 'adorno en la pared de la casa, no está en el cielo'}


def imagen(svg, D, cache={}):
    """dibuja el SVG con Chromium a 2400 px de ancho"""
    from PIL import Image
    from playwright.sync_api import sync_playwright
    import tempfile
    if svg not in cache:
        S = 2400 / D.W; t = open(svg, encoding='utf-8').read()
        t = re.sub(r'<svg\b', '<svg style="width:2400px;height:auto;display:block" ', t, count=1)
        png = tempfile.mktemp(suffix='.png')
        with sync_playwright() as p:
            b = p.chromium.launch(); pg = b.new_page(viewport={'width': 2400, 'height': int(D.H * S) + 2})
            pg.set_content('<html><body style="margin:0;background:#888">' + t + '</body></html>')
            pg.screenshot(path=png, full_page=True); b.close()
        cache[svg] = Image.open(png).convert('RGB')
    return cache[svg]


def origen(D):
    vb = [float(x) for x in re.findall(r'[-\d.]+', D.raiz.get('viewBox') or '')]
    return (vb[0], vb[1]) if len(vb) == 4 else (0, 0)


def recorte(svg, D, x, y, R, lado_px=200):
    im = imagen(svg, D); S = im.width / D.W; x0, y0 = origen(D)
    cx, cy, m = (x - x0) * S, (y - y0) * S, max(R * S * 2.6, 30)
    from PIL import Image
    return im.crop((int(cx - m), int(cy - m), int(cx + m), int(cy + m))).resize((lado_px, lado_px), Image.LANCZOS)


def contraste(svg, D, L):
    """compara en la imagen el disco que tapa con el cielo de alrededor (RGB 0-255)"""
    import statistics as st
    im = imagen(svg, D); S = im.width / D.W; x0, y0 = origen(D)
    A, B = L['A'], L['B']; ax, ay, R = (A['x'] - x0) * S, (A['y'] - y0) * S, A['r'] * S
    bx, by, r = (B['x'] - x0) * S, (B['y'] - y0) * S, B['r'] * S
    dentro, fuera = [], []; px = im.load()
    for q in range(0, 360, 2):
        # solo el lado de afuera: lejos del disco claro
        for rho, lista in ((0.90 * r, dentro), (1.10 * r, fuera)):
            x, y = bx + rho * math.cos(math.radians(q)), by + rho * math.sin(math.radians(q))
            if math.hypot(x - ax, y - ay) < R * 1.12: continue
            if 0 <= x < im.width and 0 <= y < im.height: lista.append(px[int(x), int(y)])
    if len(dentro) < 8 or len(fuera) < 8: return None
    med = lambda l: tuple(st.median(c[i] for c in l) for i in range(3))
    a, b = med(dentro), med(fuera)
    return dist(a, b) * (1 if lum(a) >= lum(b) else -1)   # signo: + el disco se ve más claro que lo de alrededor, - más oscuro


if __name__ == '__main__':
    import statistics as st
    args = [a for a in sys.argv[1:] if not a.startswith('--')]; MIRAR = '--mirar' in sys.argv; HOJA = '--hoja' in sys.argv; cortes = []
    BASE = args[0] if args else 'corridas'
    filas = []; raros = []; excl = []; total = 0
    hexa = lambda t: '#%02x%02x%02x' % tuple(int(round(x)) for x in t) if t else '-'
    for f in sorted(glob.glob(os.path.join(BASE, 'dibujos*', '*', '*', 'dibujo.svg'))):
        partes = f.split(os.sep); consigna, casa = partes[-3], partes[-2]
        if 'animal' in consigna: continue
        idioma = partes[-4].replace('dibujos', '').strip('_') or 'es'
        try: D = Dibujo(f)
        except ET.ParseError: continue
        total += 1; clave = (consigna, idioma, casa)
        for L in lunas_de_dos_circulos(D):
            motivo = EXCLUIR.get(clave) or EXCLUIR.get(clave + (lado(L['ang']),))
            if motivo: excl.append(clave + ('dos círculos', motivo)); continue
            c = L['cielo']; tapa = L['B']['col']
            if c and c['col']:
                rel = ('=' if dist(tapa, c['col']) < 12 else ('+' if lum(tapa) > lum(c['col']) else '-')) + ('g' if c['grad'] else ' ') \
                      + ('p' if dist(tapa, c['col']) < 12 or any(dist(tapa, p) < 12 for p in c['paradas']) else ' ')
            else: rel = '?'
            fila = dict(consigna=consigna, idioma=idioma, casa=casa, tipo='dos círculos', ang=L['ang'], rR=L['rR'], cuernos=L['cuernos'],
                        k=L['k'], claro=hexa(L['A']['col']), tapa=hexa(tapa), cielo=hexa(c['col']) if c and c['col'] else '-', rel=rel,
                        estrellas=L['estrellas'], op_tapa=L['B']['op'])
            if MIRAR: fila['contraste'] = contraste(f, D, L)
            filas.append(fila)
            if HOJA: cortes.append((fila, recorte(f, D, L['A']['x'], L['A']['y'], L['A']['r'])))
        for L in lunas_con_mascara(D):
            if EXCLUIR.get(clave): excl.append(clave + ('máscara', EXCLUIR[clave])); continue
            filas.append(dict(consigna=consigna, idioma=idioma, casa=casa, tipo='máscara', ang=L['ang'], rR=L['rR'], cuernos=L['cuernos'], k=L['k']))
            if HOJA: cortes.append((filas[-1], recorte(f, D, L['x'], L['y'], L['R'])))
        for L in paths_de_luna(D):
            if EXCLUIR.get(clave): excl.append(clave + ('path', EXCLUIR[clave])); continue
            if L['clase'] == 'creciente':
                filas.append(dict(consigna=consigna, idioma=idioma, casa=casa, tipo='path', ang=L['ang'], rR=L['rR'], cuernos=L['cuernos'], k=L['k']))
                if HOJA: cortes.append((filas[-1], recorte(f, D, L['x'], L['y'], L['R'])))
            else:
                raros.append((consigna, idioma, casa, L['clase'], 'radios escritos %g y %g' % L['r_escritos'], L['d']))
                if HOJA: cortes.append((dict(consigna=consigna, idioma=idioma, casa=casa, tipo='path: ' + L['clase']), recorte(f, D, L['x'], L['y'], L['R'] * 1.5)))
    print(f'{total} dibujos leídos (sin los del animal); {len(filas)} lunas con dos círculos adentro\n')
    print(f"{'consigna':20s}{'id':3s}{'casa':30s}{'tipo':13s}{'lado':5s}{'ang':>5s}{'r/R':>6s}{'cuernos':>8s}{'k':>6s}  {'tapa':8s}{'cielo':8s}{'rel':4s}{'estr':>5s}{'contraste':>10s}")
    for F in filas:
        ct = F.get('contraste'); 
        print(f"{F['consigna']:20s}{F['idioma']:3s}{F['casa']:30s}{F['tipo']:13s}{lado(F['ang']):5s}{F['ang']:5.0f}{F['rR']:6.2f}{F['cuernos']:8.0f}{F['k']:6.2f}  "
              f"{F.get('tapa', ''):8s}{F.get('cielo', ''):8s}{F.get('rel', ''):4s}{F.get('estrellas', ''):>5}{'' if ct is None else format(ct, '10.0f')}")
    print('\nrel: = el disco que tapa tiene el color del cielo a esa altura; + más claro; - más oscuro;')
    print('     g el cielo es un degradado; p el color del disco coincide con alguna parada del degradado')
    n = len(filas); der = sum(1 for F in filas if abs(F['ang']) < 90)
    print(f'\nResumen de las {n}:')
    print(f"  tapa corrida a la derecha (luz a la izquierda, forma de C): {der} de {n}")
    ne = [F['ang'] for F in filas if 0 < F['ang'] < 90]
    print(f"  de esas, arriba a la derecha: {len(ne)}; ángulo sobre la horizontal: mediana {st.median(ne):.0f}, de {min(ne):.0f} a {max(ne):.0f}")
    print(f"  r/R: mediana {st.median(F['rR'] for F in filas):.2f}, de {min(F['rR'] for F in filas):.2f} a {max(F['rR'] for F in filas):.2f}; mayores que 1: {sum(F['rR'] > 1.005 for F in filas)}")
    print(f"  cuernos: mediana {st.median(F['cuernos'] for F in filas):.0f} grados, de {min(F['cuernos'] for F in filas):.0f} a {max(F['cuernos'] for F in filas):.0f}")
    print(f"  k: mediana {st.median(F['k'] for F in filas):.2f}, de {min(F['k'] for F in filas):.2f} a {max(F['k'] for F in filas):.2f}")
    dc = [F for F in filas if F['tipo'] == 'dos círculos']
    print(f"  de las {len(dc)} de dos círculos: cielo en degradado {sum('g' in F['rel'] for F in dc)}; tapa del color de una parada o del cielo {sum('p' in F['rel'] for F in dc)}; estrellas delante {sum(F['estrellas'] > 0 for F in dc)}")
    if MIRAR:
        cs = [F['contraste'] for F in dc if F.get('contraste') is not None]
        print(f"  contraste medido en la imagen ({len(cs)} medibles): mediana del valor absoluto {st.median(abs(c) for c in cs):.0f}; "
              f"de 10 o más: {sum(abs(c) >= 10 for c in cs)} (más oscuro que el entorno {sum(c <= -10 for c in cs)}, más claro {sum(c >= 10 for c in cs)}); menos de 5: {sum(abs(c) < 5 for c in cs)}")
        hal = [F for F in dc if F.get('contraste') is not None and '=' in F['rel']]
        print(f"  de las {len(hal)} cuya tapa coincide en el código con el cielo a esa altura, se distinguen igual en la imagen (10 o más): {sum(abs(F['contraste']) >= 10 for F in hal)}")
    print('\nPaths de dos arcos que no dan un creciente:')
    for o in raros: print('  ', *o)
    print('\nCandidatos excluidos por no ser lunas:')
    for o in excl: print('  ', *o)
    json.dump(filas, open('lunas.json', 'w'), indent=1, ensure_ascii=False)
    if HOJA:
        from PIL import Image, ImageDraw, ImageFont
        C, cols = 200, 7; alto = C + 44; rows = math.ceil(len(cortes) / cols)
        hoja = Image.new('RGB', (cols * C, rows * alto), 'white'); dr = ImageDraw.Draw(hoja)
        try: fuente = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
        except Exception: fuente = ImageFont.load_default()
        for i, (F, im) in enumerate(cortes):
            X, Y = (i % cols) * C, (i // cols) * alto; hoja.paste(im, (X, Y))
            pie = f"{F['consigna']} {F['idioma']}\n{F['casa']}\n{F['tipo']}" + (f" · {lado(F['ang'])} · k {F['k']:.2f}" if 'k' in F else '')
            dr.multiline_text((X + 3, Y + C + 1), pie, fill='black', font=fuente, spacing=1)
        hoja.save('hoja_de_lunas.png'); print('\nhoja_de_lunas.png:', len(cortes), 'recortes')
