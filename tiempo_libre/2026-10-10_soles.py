#!/usr/bin/env python3
"""soles.py — busca los soles en los dibujo.svg y anota cómo están hechos.

Uso:  python3 soles.py [carpeta corridas] [--json candidatos.json]

No llama a nadie. No abre las carpetas de las letras (letra, letra_inexistente,
letra_imposible, letra_eme), que el 10/10/2026 estaban pendientes de la lectura a
ciegas de Maia.

Qué hace: recorre cada dibujo.svg, aplica las transformaciones y junta todos los
discos (círculos y elipses casi redondas). Un disco es candidato a sol si
  a) su color es cálido (del rojo al amarillo, o un blanco amarillento) y mide por lo
     menos el 2 % del ancho del lienzo, o
  b) él, su grupo o el comentario que tiene justo antes dicen sol / sun / soleil / 太阳.
Los discos concéntricos del mismo dibujo (halo, resplandor, núcleo) se juntan en un
solo candidato: se queda el disco opaco más grande y se anotan los demás como halo.

El detector exagera a propósito: flores, lámparas, ventanas redondas, caras y planetas
entran como candidatos. Lo que es sol se decide mirando (ver hojas.py y veredicto.json).
Para cada candidato anota:
  lado     posición del centro sobre el ancho (0 = borde izquierdo, 1 = derecho)
  alto     posición del centro sobre el alto (0 = arriba)
  r        radio sobre el ancho
  color    el relleno, resuelto (si es un degradado, el primer color y el último)
  adentro  cuántos elementos dibujados después caen enteros dentro del disco
           (ojos, boca, cachetes: lo que haría una cara)

Borrador de una sesión de tiempo libre (10/10/2026): propuesta, no parte del repo.
"""
import re, os, sys, glob, math, json, colorsys
from xml.etree import ElementTree as ET

EXCLUIR_CONSIGNAS = {'letra', 'letra_inexistente', 'letra_imposible', 'letra_eme'}

NOMBRES = {
    'white': '#ffffff', 'black': '#000000', 'yellow': '#ffff00', 'gold': '#ffd700', 'orange': '#ffa500',
    'red': '#ff0000', 'darkorange': '#ff8c00', 'orangered': '#ff4500', 'tomato': '#ff6347',
    'coral': '#ff7f50', 'khaki': '#f0e68c', 'lightyellow': '#ffffe0', 'lemonchiffon': '#fffacd',
    'goldenrod': '#daa520', 'darkgoldenrod': '#b8860b', 'ivory': '#fffff0', 'cornsilk': '#fff8dc',
    'moccasin': '#ffe4b5', 'wheat': '#f5deb3', 'beige': '#f5f5dc', 'crimson': '#dc143c',
    'firebrick': '#b22222', 'salmon': '#fa8072', 'lightsalmon': '#ffa07a', 'peachpuff': '#ffdab9',
    'papayawhip': '#ffefd5', 'navy': '#000080', 'blue': '#0000ff', 'skyblue': '#87ceeb',
    'lightblue': '#add8e6', 'green': '#008000', 'gray': '#808080', 'grey': '#808080',
    'silver': '#c0c0c0', 'brown': '#a52a2a', 'pink': '#ffc0cb', 'purple': '#800080',
    'lightgoldenrodyellow': '#fafad2', 'palegoldenrod': '#eee8aa', 'sandybrown': '#f4a460',
    'darkred': '#8b0000', 'maroon': '#800000', 'whitesmoke': '#f5f5f5', 'snow': '#fffafa',
}
PALABRA_SOL = re.compile(r'(?<![a-záéíóúñ])(sol|soles|sun|suns|sunshine|soleil|solar)(?![a-záéíóúñ])|太阳|太陽|日头', re.I)
PALABRA_NO_SOL = re.compile(r'girasol|sunflower|sunset[- ]?sky|solar[- ]?panel|panel(es)?[- ]?solar', re.I)


def num(s, d=0.0):
    try:
        return float(re.sub(r'[^0-9.eE+\-]', '', s or '') or d)
    except ValueError:
        return d


def rgb(c):
    if not c:
        return None
    c = c.strip().lower()
    c = NOMBRES.get(c, c)
    m = re.fullmatch(r'#([0-9a-f]{3})', c)
    if m:
        return tuple(int(x * 2, 16) for x in m.group(1))
    m = re.fullmatch(r'#([0-9a-f]{6})([0-9a-f]{2})?', c)
    if m:
        return tuple(int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4))
    m = re.match(r'rgba?\(([^)]+)\)', c)
    if m:
        p = [x for x in re.split(r'[ ,/]+', m.group(1).strip()) if x]
        try:
            return tuple(int(float(x.rstrip('%')) * (2.55 if x.endswith('%') else 1)) for x in p[:3])
        except ValueError:
            return None
    m = re.match(r'hsla?\(([^)]+)\)', c)
    if m:
        p = [x for x in re.split(r'[ ,/]+', m.group(1).strip()) if x]
        try:
            h = float(re.sub(r'[a-z]', '', p[0])) / 360.0
            s = float(p[1].rstrip('%')) / 100
            l = float(p[2].rstrip('%')) / 100
            r, g, b = colorsys.hls_to_rgb(h, l, s)
            return (int(r * 255), int(g * 255), int(b * 255))
        except (ValueError, IndexError):
            return None
    return None


def hsv(c):
    h, s, v = colorsys.rgb_to_hsv(c[0] / 255, c[1] / 255, c[2] / 255)
    return h * 360, s, v


def calido(c):
    """Del rojo al amarillo con algo de saturación, o un blanco amarillento."""
    if c is None:
        return False
    h, s, v = hsv(c)
    if v < 0.45:
        return False
    if (h <= 68 or h >= 345) and s >= 0.28:
        return True
    if 30 <= h <= 70 and s >= 0.08 and v >= 0.93:      # blancos crema: #fff8dc, #fffde7
        return True
    return False


def familia(c):
    """Nombre grueso del color de un sol."""
    if c is None:
        return '?'
    h, s, v = hsv(c)
    if s < 0.12 and v > 0.9:
        return 'blanco'
    if h >= 345 or h < 18:
        return 'rojo'
    if h < 40:
        return 'naranja'
    if h <= 70:
        return 'amarillo' if s >= 0.25 else 'crema'
    return 'otro'


# --- transformaciones afines (a, b, c, d, e, f) ---
ID = (1, 0, 0, 1, 0, 0)


def mul(m, n):
    a, b, c, d, e, f = m
    a2, b2, c2, d2, e2, f2 = n
    return (a * a2 + c * b2, b * a2 + d * b2, a * c2 + c * d2, b * c2 + d * d2,
            a * e2 + c * f2 + e, b * e2 + d * f2 + f)


def parse_tr(s):
    m = ID
    for nom, args in re.findall(r'(\w+)\s*\(([^)]*)\)', s or ''):
        v = [float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?', args)]
        t = ID
        if nom == 'translate' and v:
            t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif nom == 'scale' and v:
            t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif nom == 'rotate' and v:
            a = math.radians(v[0])
            r = (math.cos(a), math.sin(a), -math.sin(a), math.cos(a), 0, 0)
            if len(v) >= 3:
                t = mul(mul((1, 0, 0, 1, v[1], v[2]), r), (1, 0, 0, 1, -v[1], -v[2]))
            else:
                t = r
        elif nom == 'matrix' and len(v) == 6:
            t = tuple(v)
        m = mul(m, t)
    return m


def aplicar(m, x, y):
    a, b, c, d, e, f = m
    return a * x + c * y + e, b * x + d * y + f


def escala(m):
    a, b, c, d, e, f = m
    return math.sqrt(abs(a * d - b * c))


def local(tag):
    return tag.split('}')[-1] if isinstance(tag, str) else '#comment'


def estilo(el):
    d = {}
    for k, v in el.attrib.items():
        d[local(k)] = v
    for par in (el.attrib.get('style') or '').split(';'):
        if ':' in par:
            k, v = par.split(':', 1)
            d[k.strip()] = v.strip()
    return d


def leer_svg(ruta):
    txt = open(ruta, encoding='utf-8', errors='replace').read()
    try:
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        root = ET.fromstring(txt, parser=parser)
    except ET.ParseError:
        try:
            root = ET.fromstring(txt)
        except ET.ParseError:
            return None, txt
    return root, txt


def lienzo(root):
    vb = root.attrib.get('viewBox')
    if vb:
        p = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', vb)]
        if len(p) == 4 and p[2] > 0 and p[3] > 0:
            return p
    w = num(root.attrib.get('width'), 0)
    h = num(root.attrib.get('height'), 0)
    return [0, 0, w or 800, h or 600]


def degradados(root):
    g = {}
    for el in root.iter():
        if local(el.tag) in ('linearGradient', 'radialGradient') and el.attrib.get('id'):
            cols = []
            for st in el:
                if local(st.tag) == 'stop':
                    e = estilo(st)
                    c = rgb(e.get('stop-color'))
                    op = num(e.get('stop-opacity'), 1.0) if e.get('stop-opacity') is not None else 1.0
                    if c:
                        cols.append((c, op))
            g[el.attrib['id']] = cols
    # degradados que heredan de otro con href
    for el in root.iter():
        if local(el.tag) in ('linearGradient', 'radialGradient') and el.attrib.get('id'):
            if not g.get(el.attrib['id']):
                for k, v in el.attrib.items():
                    if local(k) == 'href' and v.startswith('#'):
                        g[el.attrib['id']] = g.get(v[1:], [])
    return g


def discos(root):
    """Todos los discos del dibujo, en orden de pintura, con todo resuelto."""
    vb = lienzo(root)
    grads = degradados(root)
    salida = []
    orden = [0]

    def andar(el, m, heredado, etiquetas, en_defs):
        tag = local(el.tag)
        if tag in ('defs', 'clipPath', 'mask', 'symbol', 'pattern', 'marker', 'linearGradient',
                   'radialGradient', 'filter', 'style', 'title', 'desc'):
            return
        e = estilo(el)
        m2 = mul(m, parse_tr(e.get('transform')))
        h2 = dict(heredado)
        for k in ('fill', 'opacity', 'fill-opacity', 'stroke'):
            if k in e:
                if k == 'opacity':
                    h2['opacity'] = h2.get('opacity', 1.0) * num(e[k], 1.0)
                else:
                    h2[k] = e[k]
        et2 = etiquetas
        propias = ' '.join(x for x in (e.get('id'), e.get('class')) if x)
        if propias:
            et2 = etiquetas + [propias]
        comentario = ['']
        for hijo in el:
            if local(hijo.tag) == '#comment':
                comentario[0] = (hijo.text or '').strip()
                continue
            orden[0] += 1
            n = orden[0]
            t = local(hijo.tag)
            eh = estilo(hijo)
            if t in ('circle', 'ellipse'):
                mh = mul(m2, parse_tr(eh.get('transform')))
                cx, cy = num(eh.get('cx')), num(eh.get('cy'))
                if t == 'circle':
                    rx = ry = num(eh.get('r'))
                else:
                    rx, ry = num(eh.get('rx')), num(eh.get('ry'))
                X, Y = aplicar(mh, cx, cy)
                s = escala(mh)
                RX, RY = rx * s, ry * s
                fill = eh.get('fill', h2.get('fill', '#000000'))
                op = h2.get('opacity', 1.0) * (num(eh.get('opacity'), 1.0) if eh.get('opacity') is not None else 1.0)
                op *= num(eh.get('fill-opacity', h2.get('fill-opacity')), 1.0) if (eh.get('fill-opacity') or h2.get('fill-opacity')) is not None else 1.0
                col, col2, grad = None, None, False
                mu = re.match(r'url\(\s*["\']?#([^)"\']+)', fill or '')
                if mu:
                    grad = True
                    st = grads.get(mu.group(1), [])
                    if st:
                        col, col2 = st[0][0], st[-1][0]
                        # un halo: degradado que termina transparente
                        if st[-1][1] <= 0.05:
                            op *= 0.5
                elif fill and fill != 'none':
                    col = rgb(fill)
                etq = ' | '.join(et2 + [x for x in (eh.get('id'), eh.get('class')) if x])
                salida.append(dict(n=n, tipo='disco', x=X, y=Y, rx=RX, ry=RY, fill=fill, col=col, col2=col2,
                                   grad=grad, op=op, etiqueta=etq, comentario=comentario[0],
                                   stroke=eh.get('stroke', h2.get('stroke')), sin_relleno=(fill == 'none')))
            elif t in ('g', 'a', 'svg', 'switch'):
                # el comentario de antes de un grupo vale para lo de adentro
                andar(hijo, m2, h2, et2 + ([comentario[0]] if comentario[0] else []), en_defs)
            else:
                # cualquier otra forma: se guarda su caja aproximada, para saber qué cae dentro de un disco
                mh = mul(m2, parse_tr(eh.get('transform')))
                pts = []
                if t == 'rect':
                    x, y, w, h = num(eh.get('x')), num(eh.get('y')), num(eh.get('width')), num(eh.get('height'))
                    pts = [(x, y), (x + w, y), (x, y + h), (x + w, y + h)]
                elif t == 'line':
                    pts = [(num(eh.get('x1')), num(eh.get('y1'))), (num(eh.get('x2')), num(eh.get('y2')))]
                elif t in ('polygon', 'polyline'):
                    v = [float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?', eh.get('points', ''))]
                    pts = list(zip(v[0::2], v[1::2]))
                elif t == 'path':
                    # solo los pares de números del path: alcanza para una caja aproximada
                    d = eh.get('d', '')
                    if not re.search(r'[aAhHvV]', d):
                        v = [float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?', d)]
                        if not re.search(r'[mlcsqt]', d):          # solo absolutos
                            pts = list(zip(v[0::2], v[1::2]))
                        else:
                            pts = None
                    else:
                        pts = None
                elif t == 'text':
                    pts = [(num(eh.get('x')), num(eh.get('y')))]
                if pts:
                    P = [aplicar(mh, x, y) for x, y in pts]
                    xs, ys = [p[0] for p in P], [p[1] for p in P]
                    salida.append(dict(n=n, tipo=t, caja=(min(xs), min(ys), max(xs), max(ys)),
                                       fill=eh.get('fill', h2.get('fill')), stroke=eh.get('stroke', h2.get('stroke')),
                                       comentario=comentario[0], d=eh.get('d', '')[:200]))
                elif pts is None:
                    salida.append(dict(n=n, tipo=t, caja=None, fill=eh.get('fill', h2.get('fill')),
                                       stroke=eh.get('stroke', h2.get('stroke')), comentario=comentario[0],
                                       d=eh.get('d', '')[:200], m=mh))
            # el comentario vale solo para el elemento que le sigue
            if t not in ('g',):
                pass
            comentario[0] = comentario[0] if t in ('animate', 'animateTransform', 'set') else ''
    andar(root, ID, {}, [], False)
    return vb, salida


def candidatos(ruta):
    root, txt = leer_svg(ruta)
    if root is None:
        return None, []
    vb, formas = discos(root)
    W, H = vb[2], vb[3]
    ds = [f for f in formas if f['tipo'] == 'disco' and f['rx'] > 0 and f['ry'] > 0
          and 0.6 <= f['rx'] / f['ry'] <= 1.67]
    marcados = []
    for f in ds:
        r = (f['rx'] + f['ry']) / 2
        texto = (f['etiqueta'] + ' ' + f['comentario'])
        dice = bool(PALABRA_SOL.search(texto)) and not PALABRA_NO_SOL.search(texto)
        cal = (calido(f['col']) or calido(f['col2'])) and not f['sin_relleno']
        if (cal and r >= 0.02 * W) or (dice and r >= 0.012 * W):
            f = dict(f)
            f['r'] = r
            f['dice'] = dice
            marcados.append(f)
    # juntar concéntricos
    grupos = []
    for f in sorted(marcados, key=lambda f: -f['r']):
        for g in grupos:
            if math.hypot(f['x'] - g[0]['x'], f['y'] - g[0]['y']) <= 0.35 * g[0]['r'] + 2:
                g.append(f)
                break
        else:
            grupos.append([f])
    res = []
    for g in grupos:
        # el cuerpo: el disco más grande con opacidad >= 0.75; si no hay, el más opaco
        opacos = [f for f in g if f['op'] >= 0.75]
        cuerpo = max(opacos, key=lambda f: f['r']) if opacos else max(g, key=lambda f: f['op'])
        # qué hay adentro, dibujado después
        adentro = []
        for h in formas:
            if h['n'] <= cuerpo['n']:
                continue
            if h['tipo'] == 'disco':
                rr = (h['rx'] + h['ry']) / 2
                if rr < 0.6 * cuerpo['r'] and math.hypot(h['x'] - cuerpo['x'], h['y'] - cuerpo['y']) + rr <= cuerpo['r'] * 1.02:
                    if not (math.hypot(h['x'] - cuerpo['x'], h['y'] - cuerpo['y']) < 0.2 * cuerpo['r'] and rr > 0.35 * cuerpo['r']):
                        adentro.append(('disco', h['fill']))
            elif h.get('caja'):
                x0, y0, x1, y1 = h['caja']
                esquinas = [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]
                if all(math.hypot(x - cuerpo['x'], y - cuerpo['y']) <= cuerpo['r'] * 1.02 for x, y in esquinas):
                    if (x1 - x0) > 0.05 * cuerpo['r'] or (y1 - y0) > 0.05 * cuerpo['r']:
                        adentro.append((h['tipo'], h.get('stroke') or h.get('fill')))
        res.append(dict(
            x=cuerpo['x'], y=cuerpo['y'], r=cuerpo['r'], lado=(cuerpo['x'] - vb[0]) / W, alto=(cuerpo['y'] - vb[1]) / H,
            rW=cuerpo['r'] / W, fill=cuerpo['fill'], col=cuerpo['col'], col2=cuerpo['col2'], grad=cuerpo['grad'],
            op=round(cuerpo['op'], 2), dice=any(f['dice'] for f in g),
            etiqueta=' / '.join(sorted({(f['etiqueta'] + ' ' + f['comentario']).strip() for f in g if (f['etiqueta'] + f['comentario']).strip()}))[:160],
            capas=len(g), adentro=adentro, n=cuerpo['n'],
        ))
    return vb, res


def listar(base):
    for ruta in sorted(glob.glob(os.path.join(base, 'dibujos*', '*', '*', 'dibujo.svg'))):
        partes = ruta.split(os.sep)
        serie, consigna, casa_rep = partes[-4], partes[-3], partes[-2]
        if consigna in EXCLUIR_CONSIGNAS:
            continue
        casa, _, rep = casa_rep.rpartition('_')
        yield dict(ruta=ruta, serie=serie, consigna=consigna, casa=casa, rep=rep)


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    base = args[0] if args else 'corridas'
    todo = []
    nd = 0
    for d in listar(base):
        nd += 1
        vb, cs = candidatos(d['ruta'])
        if vb is None:
            print('no se pudo leer:', d['ruta'], file=sys.stderr)
            continue
        for i, c in enumerate(cs):
            c.update(serie=d['serie'], consigna=d['consigna'], casa=d['casa'], rep=d['rep'], ruta=d['ruta'], i=i,
                     vb=vb)
            todo.append(c)
    print(f'{nd} dibujos leídos, {len(todo)} discos candidatos en {len({c["ruta"] for c in todo})} dibujos')
    if '--json' in sys.argv:
        out = sys.argv[sys.argv.index('--json') + 1]
        json.dump(todo, open(out, 'w'), ensure_ascii=False, indent=0, default=str)
        print('escrito', out)
