#!/usr/bin/env python3
"""rosa.py - cuentas sobre corridas/dibujos* del cuaderno de tiempo libre del 12/10/2026.
Solo lee los dibujo.svg; no llama a nadie.

Uso: python3 rosa.py CARPETA_CORRIDAS [--csv]

Mide tres cosas:

A. Órdenes de <path>: cuántas son absolutas (mayúscula: "andá a tal punto") y cuántas
   relativas (minúscula: "desde donde estás, tanto para allá"). La z no se cuenta; la m
   inicial de un trazo vale como absoluta, que es lo que dice la norma.

B. Recalada: en los subtrazos que terminan en z y cuya última orden antes de la z es una
   curva (c, s, q, t, a), la distancia entre el punto donde termina esa curva y el punto
   de partida, dividida por el tamaño del subtrazo. Una curva que cierra una figura tiene
   que llegar al punto de salida; si no llega, la z tapa la diferencia con una recta.
   Se separan los subtrazos escritos con órdenes absolutas de los escritos con relativas.

C. Rosas: grupos de seis o más rayos (<line>, o trazos y polilíneas de dos puntos) cuyas
   rectas pasan por un mismo centro. Cuántos rayos, a qué ángulos, y si el rayo diagonal
   mide lo mismo que el del eje. Se anota si los rayos están escritos uno por uno o si
   algún transform="rotate(...)" hizo la cuenta.
"""
import sys, os, re, glob, math, csv, statistics as st
from collections import Counter, defaultdict
from xml.etree import ElementTree as ET

BASE = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else 'corridas'

# ---------------------------------------------------------------- utilidades
NUM = re.compile(r'[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?')

def f(s, d=0.0):
    try:
        m = NUM.search(s or '')
        return float(m.group()) if m else d
    except ValueError:
        return d

def mat_mul(a, b):
    return (a[0]*b[0]+a[2]*b[1], a[1]*b[0]+a[3]*b[1], a[0]*b[2]+a[2]*b[3], a[1]*b[2]+a[3]*b[3],
            a[0]*b[4]+a[2]*b[5]+a[4], a[1]*b[4]+a[3]*b[5]+a[5])

ID = (1, 0, 0, 1, 0, 0)

def parse_transform(s):
    """devuelve (matriz, tiene_giro)"""
    m = ID; giro = False
    for nombre, args in re.findall(r'(\w+)\s*\(([^)]*)\)', s or ''):
        v = [float(x) for x in NUM.findall(args)]
        if nombre == 'translate' and v:
            t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif nombre == 'scale' and v:
            t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif nombre == 'rotate' and v:
            a = math.radians(v[0]); c, s_ = math.cos(a), math.sin(a)
            t = (c, s_, -s_, c, 0, 0)
            if len(v) >= 3:
                t = mat_mul(mat_mul((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
            if abs(v[0]) % 180 > 1e-6: giro = True
        elif nombre == 'matrix' and len(v) == 6:
            t = tuple(v)
            if abs(v[1]) > 1e-9 or abs(v[2]) > 1e-9: giro = True
        elif nombre in ('skewX', 'skewY') and v:
            k = math.tan(math.radians(v[0]))
            t = (1, 0, k, 1, 0, 0) if nombre == 'skewX' else (1, k, 0, 1, 0, 0)
        else:
            continue
        m = mat_mul(m, t)
    return m, giro

def aplica(m, x, y):
    return (m[0]*x + m[2]*y + m[4], m[1]*x + m[3]*y + m[5])

# ---------------------------------------------------------------- trazos
CMD = re.compile(r'([MmLlHhVvCcSsQqTtAaZz])|(' + NUM.pattern + ')')
NARGS = dict(M=2, L=2, H=1, V=1, C=6, S=4, Q=4, T=2, A=7, Z=0)

def leer_d(d):
    """devuelve lista de (orden, [args]) con las repeticiones implícitas desplegadas.
    La orden repetida de una M es L (de una m, l), como dice la norma."""
    out = []; pos = 0; cmd = None; args = []
    toks = []
    i = 0; n = len(d); en_arco = False; k_arco = 0
    while i < n:
        ch = d[i]
        if ch in 'MmLlHhVvCcSsQqTtAaZz':
            toks.append(ch); i += 1
            en_arco = ch in 'Aa'; k_arco = 0
        elif ch in ' ,\t\r\n':
            i += 1
        else:
            if en_arco and k_arco % 7 in (3, 4) and ch in '01':
                toks.append(float(ch)); i += 1; k_arco += 1      # los flags de un arco pueden venir pegados
                continue
            m = NUM.match(d, i)
            if not m: i += 1; continue
            toks.append(float(m.group())); i = m.end(); k_arco += 1
    cur = None; buf = []
    def cierra():
        nonlocal buf
        if cur is None: return
        k = NARGS[cur.upper()]
        if k == 0:
            out.append((cur, [])); buf = []; return
        c = cur; primero = True
        while len(buf) >= k:
            out.append((c if primero or c not in 'Mm' else ('L' if c == 'M' else 'l'), buf[:k]))
            buf = buf[k:]; primero = False
        buf = []
    for t in toks:
        if isinstance(t, str):
            cierra(); cur = t
            if t in 'Zz': out.append((t, [])); cur = None
        else:
            buf.append(t)
    cierra()
    return out

def recorrer(ordenes):
    """devuelve subtrazos: cada uno dict(ini, ordenes=[(orden, p0, p1, ctrl)], cerrado)"""
    subs = []; x = y = 0.0; sx = sy = 0.0; actual = None
    for c, a in ordenes:
        C = c.upper(); rel = c.islower()
        if C == 'M':
            x, y = (x + a[0], y + a[1]) if rel else (a[0], a[1])
            sx, sy = x, y
            actual = dict(ini=(x, y), ordenes=[], cerrado=False, m=c); subs.append(actual)
            continue
        if actual is None or actual['cerrado']:
            actual = dict(ini=(x, y), ordenes=[], cerrado=False, m='(sigue)'); subs.append(actual); sx, sy = x, y
        p0 = (x, y); ctrl = []
        if C == 'Z':
            actual['cerrado'] = True; actual['fin'] = (x, y); x, y = sx, sy; continue
        if C == 'L' or C == 'T': x, y = (x + a[0], y + a[1]) if rel else (a[0], a[1])
        elif C == 'H': x = x + a[0] if rel else a[0]
        elif C == 'V': y = y + a[0] if rel else a[0]
        elif C == 'C':
            ctrl = [((p0[0] + a[0], p0[1] + a[1]) if rel else (a[0], a[1])), ((p0[0] + a[2], p0[1] + a[3]) if rel else (a[2], a[3]))]
            x, y = (x + a[4], y + a[5]) if rel else (a[4], a[5])
        elif C in 'SQ':
            ctrl = [((p0[0] + a[0], p0[1] + a[1]) if rel else (a[0], a[1]))]
            x, y = (x + a[2], y + a[3]) if rel else (a[2], a[3])
        elif C == 'A': x, y = (x + a[5], y + a[6]) if rel else (a[5], a[6])
        actual['ordenes'].append((c, p0, (x, y), ctrl))
    return subs

# ---------------------------------------------------------------- lectura de un svg
def segmentos_y_trazos(svg):
    """devuelve (lista de segmentos [(p, q, con_giro, etiqueta)], lista de d) o None si no se lee"""
    try:
        raiz = ET.parse(svg).getroot()
    except ET.ParseError:
        return None
    segs = []; ds = []
    def baja(el, m, giro, en_defs):
        tag = el.tag.split('}')[-1] if isinstance(el.tag, str) else ''
        t, g = parse_transform(el.get('transform'))
        m2 = mat_mul(m, t); giro2 = giro or g
        if tag in ('defs', 'clipPath', 'mask', 'pattern', 'symbol', 'marker'): en_defs = True
        if tag == 'path' and el.get('d'):
            ds.append(el.get('d'))
            o = leer_d(el.get('d'))
            if not en_defs and len(o) >= 2 and len(o) % 2 == 0 and all(
                    o[k][0] in 'Mm' and o[k + 1][0] in 'LlHhVv' for k in range(0, len(o), 2)):
                for sub in recorrer(o):
                    if sub['ordenes']:
                        _, p0, p1, _ = sub['ordenes'][0]
                        segs.append((aplica(m2, *p0), aplica(m2, *p1), giro2, 'path'))
        elif tag == 'line' and not en_defs:
            p = (f(el.get('x1')), f(el.get('y1'))); q = (f(el.get('x2')), f(el.get('y2')))
            segs.append((aplica(m2, *p), aplica(m2, *q), giro2, 'line'))
        elif tag == 'polyline' and not en_defs:
            v = [float(x) for x in NUM.findall(el.get('points') or '')]
            if len(v) == 4:
                segs.append((aplica(m2, v[0], v[1]), aplica(m2, v[2], v[3]), giro2, 'polyline'))
        for h in el:
            baja(h, m2, giro2, en_defs)
    baja(raiz, ID, False, False)
    return segs, ds

# ---------------------------------------------------------------- rosas
def dist_punto_recta(c, p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy)
    if L < 1e-9: return 1e9, 0
    t = ((c[0] - p[0]) * dx + (c[1] - p[1]) * dy) / (L * L)
    return abs((c[0] - p[0]) * dy - (c[1] - p[1]) * dx) / L, t

def rayos_por(c, segs, usados):
    """segmentos cuya recta pasa por c y que no lo cruzan por el medio. Un segmento que
    cruza c (un diámetro) cuenta como dos rayos."""
    out = []
    for i, (p, q, giro, tag) in enumerate(segs):
        if i in usados: continue
        L = math.hypot(q[0] - p[0], q[1] - p[1])
        if L < 2: continue
        d, t = dist_punto_recta(c, p, q)
        lejos = max(math.hypot(p[0] - c[0], p[1] - c[1]), math.hypot(q[0] - c[0], q[1] - c[1]))
        if d > max(1.0, 0.025 * lejos): continue
        if t <= 0.12 or t >= 0.88:               # c está en un extremo o antes de él: un rayo
            a, b = (p, q) if t <= 0.12 else (q, p)
            out.append((i, a, b, giro, tag, False))
        elif 0.35 <= t <= 0.65:                  # diámetro: dos rayos
            out.append((i, c, p, giro, tag, True)); out.append((i, c, q, giro, tag, True))
    return out

def rosas(segs):
    grupos = []; usados = set()
    while True:
        libres = [i for i in range(len(segs)) if i not in usados]
        if len(libres) < 3: break
        votos = Counter()
        for a in range(len(libres)):
            p1, q1 = segs[libres[a]][0], segs[libres[a]][1]
            d1 = (q1[0] - p1[0], q1[1] - p1[1]); L1 = math.hypot(*d1)
            if L1 < 2: continue
            for b in range(a + 1, len(libres)):
                p2, q2 = segs[libres[b]][0], segs[libres[b]][1]
                d2 = (q2[0] - p2[0], q2[1] - p2[1]); L2 = math.hypot(*d2)
                if L2 < 2: continue
                cr = d1[0] * d2[1] - d1[1] * d2[0]
                if abs(cr) < 0.08 * L1 * L2: continue
                t = ((p2[0] - p1[0]) * d2[1] - (p2[1] - p1[1]) * d2[0]) / cr
                x, y = p1[0] + t * d1[0], p1[1] + t * d1[1]
                if abs(x) > 5000 or abs(y) > 5000: continue
                votos[(round(x / 2), round(y / 2))] += 1
        if not votos: break
        mejor = None
        for (kx, ky), _ in votos.most_common(6):
            c = (kx * 2.0, ky * 2.0)
            r = rayos_por(c, segs, usados)
            # afinar el centro con la media de las intersecciones no hace falta a esta tolerancia
            if mejor is None or len(r) > len(mejor[1]): mejor = (c, r)
        if mejor is None or len(mejor[1]) < 6: break
        c, r = mejor
        # centro afinado: mínimos cuadrados sobre las rectas del grupo
        A11 = A12 = A22 = B1 = B2 = 0.0
        for (_, a, b, _, _, _) in r:
            dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy)
            if L < 1e-9: continue
            nx, ny = -dy / L, dx / L; k = nx * b[0] + ny * b[1]
            A11 += nx * nx; A12 += nx * ny; A22 += ny * ny; B1 += nx * k; B2 += ny * k
        det = A11 * A22 - A12 * A12
        if abs(det) > 1e-9:
            c = ((B1 * A22 - B2 * A12) / det, (A11 * B2 - A12 * B1) / det)
            r2 = rayos_por(c, segs, usados)
            if len(r2) >= len(r): r = r2
        grupos.append((c, r))
        usados |= {x[0] for x in r}
    return grupos

def describe(c, r):
    ang = []; rad_fuera = []; rad_dentro = []
    for (_, a, b, giro, tag, diam) in r:
        ra = math.hypot(a[0] - c[0], a[1] - c[1]); rb = math.hypot(b[0] - c[0], b[1] - c[1])
        lejos, cerca = (b, a) if rb >= ra else (a, b)
        t = math.degrees(math.atan2(-(lejos[1] - c[1]), lejos[0] - c[0])) % 360   # 0 = este, antihorario
        ang.append(t); rad_fuera.append(max(ra, rb)); rad_dentro.append(min(ra, rb))
    n = len(ang)
    def todos(paso, tol=2.0):
        return all(min(a % paso, paso - a % paso) <= tol for a in ang)
    if todos(90): red = 4
    elif todos(45): red = 8
    elif todos(30): red = 12
    elif todos(22.5): red = 16
    elif todos(15): red = 24
    elif todos(11.25, 1.5): red = 32
    else: red = 0
    orden = sorted(ang); huecos = [(orden[(i + 1) % n] - orden[i]) % 360 for i in range(n)]
    hueco_max = max(huecos) if n > 1 else 360
    parejo = (max(huecos) - min(huecos)) <= 6 if n > 1 else False
    eje = [rf for a, rf in zip(ang, rad_fuera) if min(a % 90, 90 - a % 90) <= 2]
    diag = [rf for a, rf in zip(ang, rad_fuera) if abs(a % 90 - 45) <= 2]
    eje_d = [rd for a, rd in zip(ang, rad_dentro) if min(a % 90, 90 - a % 90) <= 2]
    diag_d = [rd for a, rd in zip(ang, rad_dentro) if abs(a % 90 - 45) <= 2]
    razon = st.mean(diag) / st.mean(eje) if eje and diag and st.mean(eje) > 0 else None
    # el "seno de 45 grados" que usó: lo que el rayo diagonal se corre en x (o en y), sobre el largo del rayo del eje
    seno = desvio = None
    if eje and diag and st.mean(eje) > 0:
        corr = []
        for (_, a, b, _, _, _) in r:
            ra = math.hypot(a[0] - c[0], a[1] - c[1]); rb = math.hypot(b[0] - c[0], b[1] - c[1])
            lejos = b if rb >= ra else a
            t = math.degrees(math.atan2(-(lejos[1] - c[1]), lejos[0] - c[0])) % 360
            if abs(t % 90 - 45) <= 2: corr.append((abs(lejos[0] - c[0]) + abs(lejos[1] - c[1])) / 2)
        seno = st.mean(corr) / st.mean(eje); desvio = st.mean(corr) - st.mean(eje) * math.sin(math.radians(45))
    razon_d = st.mean(diag_d) / st.mean(eje_d) if eje_d and diag_d and st.mean(eje_d) > 1 else None
    return dict(n=n, red=red, hueco_max=hueco_max, parejo=parejo, razon=razon, razon_d=razon_d, seno=seno, desvio=desvio, r_eje=(st.mean(eje) if eje else None),
                giro=any(x[3] for x in r), tags=Counter(x[4] for x in r), diam=any(x[5] for x in r),
                r_fuera=st.mean(rad_fuera), angulos=orden)

# ---------------------------------------------------------------- corpus
def modelo_de(carpeta):
    m = re.match(r'(.+)_(\d+)$', os.path.basename(carpeta))
    return (m.group(1), int(m.group(2))) if m else (os.path.basename(carpeta), 0)

def laboratorio(modelo):
    for pref, lab in (('claude', 'Anthropic'), ('gpt', 'OpenAI'), ('gemini', 'Google'), ('grok', 'xAI'),
                      ('mistral', 'Mistral'), ('deepseek', 'DeepSeek'), ('qwen', 'Alibaba'), ('kimi', 'Moonshot'),
                      ('glm', 'Zhipu'), ('minimax', 'MiniMax'), ('mimo', 'Xiaomi')):
        if modelo.startswith(pref): return lab
    return '?'

def main():
    archivos = sorted(glob.glob(os.path.join(BASE, 'dibujos*', '*', '*', 'dibujo.svg')))
    print(f"dibujo.svg encontrados: {len(archivos)}")
    ilegibles = 0
    ordenes = defaultdict(Counter)        # modelo -> Counter(abs, rel)
    por_dibujo = []                       # (modelo, consigna, abs, rel)
    recaladas = []                        # (modelo, consigna, tipo 'abs'|'rel'|'mixto', error relativo, error px)
    filas_rosa = []
    pegadas = defaultdict(lambda: [0, 0])
    for a in archivos:
        partes = a.split(os.sep)
        conj, consigna = partes[-4], partes[-3]
        modelo, rep = modelo_de(partes[-2])
        r = segmentos_y_trazos(a)
        if r is None:
            ilegibles += 1; continue
        segs, ds = r
        na = nr = 0
        for d in ds:
            o = leer_d(d)
            pegadas[modelo][1] += 1
            if re.search(r'\d[A-DF-Ya-df-y]', d): pegadas[modelo][0] += 1      # una letra de orden pegada a un número ("8v54")
            primera = True
            for c, _ in o:
                if c in 'Zz': continue
                if c == 'm' and primera: na += 1
                elif c.isupper(): na += 1
                else: nr += 1
                primera = False
            for s in recorrer(o):
                if not s['cerrado'] or not s['ordenes']: continue
                ult = s['ordenes'][-1]
                if ult[0].upper() not in 'CSQTA': continue
                pts = [s['ini']] + [x[2] for x in s['ordenes']] + [p for x in s['ordenes'] for p in x[3]]
                ext = math.hypot(max(p[0] for p in pts) - min(p[0] for p in pts), max(p[1] for p in pts) - min(p[1] for p in pts))
                if ext < 4 or len(s['ordenes']) < 2: continue
                err = math.hypot(s['fin'][0] - s['ini'][0], s['fin'][1] - s['ini'][1])
                letras = [x[0] for x in s['ordenes']]
                tipo = 'rel' if all(l.islower() for l in letras) else ('abs' if all(l.isupper() for l in letras) else 'mixto')
                recaladas.append((modelo, f"{conj}/{consigna}", tipo, err / ext, err, len(letras), ult[0]))
        ordenes[modelo]['abs'] += na; ordenes[modelo]['rel'] += nr
        por_dibujo.append((modelo, f"{conj}/{consigna}", na, nr))
        if len(segs) <= 600:
            for c, rr in rosas(segs):
                d = describe(c, rr)
                filas_rosa.append(dict(modelo=modelo, conj=conj, consigna=consigna, rep=rep, cx=round(c[0], 1), cy=round(c[1], 1), **d))
    print(f"no se leen como XML: {ilegibles}; leídos: {len(archivos) - ilegibles}")

    # ---------------- A
    print("\nA. Órdenes de <path>: absolutas y relativas")
    ta = sum(v['abs'] for v in ordenes.values()); tr = sum(v['rel'] for v in ordenes.values())
    print(f"   corpus: {ta} absolutas, {tr} relativas ({100 * tr / (ta + tr):.1f} % relativas)")
    con_rel = sum(1 for x in por_dibujo if x[3] > 0); con_path = sum(1 for x in por_dibujo if x[2] + x[3] > 0)
    may = sum(1 for x in por_dibujo if x[3] > x[2])
    print(f"   dibujos con algún <path>: {con_path}; con alguna orden relativa: {con_rel}; con más relativas que absolutas: {may}")
    print("   por casa (órdenes, % relativas, dibujos con mayoría relativa / dibujos con path):")
    for mo in sorted(ordenes, key=lambda k: -ordenes[k]['rel'] / max(1, ordenes[k]['abs'] + ordenes[k]['rel'])):
        v = ordenes[mo]; tot = v['abs'] + v['rel']
        dm = sum(1 for x in por_dibujo if x[0] == mo and x[3] > x[2]); dp = sum(1 for x in por_dibujo if x[0] == mo and x[2] + x[3] > 0)
        if tot: print(f"     {mo:32s} {tot:6d}  {100 * v['rel'] / tot:5.1f} %   {dm}/{dp}")
    print("   por casa, contando por dibujo (dibujos con cinco órdenes o más): mediana del % de relativas; % de atributos d con una letra pegada a un número")
    pd_ = defaultdict(list)
    for mo, _, na_, nr_ in por_dibujo:
        if na_ + nr_ >= 5: pd_[mo].append(100 * nr_ / (na_ + nr_))
    for mo in sorted(pd_, key=lambda k: -st.median(pd_[k])):
        print(f"     {mo:32s} {st.median(pd_[mo]):5.1f} %  (n={len(pd_[mo]):2d})   {100 * pegadas[mo][0] / max(1, pegadas[mo][1]):5.1f} %")
    print(f"     casas con mediana 0: {sum(1 for k in pd_ if st.median(pd_[k]) == 0)} de {len(pd_)}")
    labs = defaultdict(Counter)
    for mo, v in ordenes.items(): labs[laboratorio(mo)].update(v)
    print("   por laboratorio: " + "; ".join(f"{l} {100 * v['rel'] / max(1, v['abs'] + v['rel']):.1f} %" for l, v in sorted(labs.items(), key=lambda kv: -kv[1]['rel'] / max(1, kv[1]['abs'] + kv[1]['rel']))))
    letras_rel = Counter(); letras_abs = Counter()
    # qué órdenes relativas son
    for a in archivos:
        r = segmentos_y_trazos(a)
        if r is None: continue
        for d in r[1]:
            primera = True
            for c, _ in leer_d(d):
                if c in 'Zz': continue
                if c.islower() and not (c == 'm' and primera): letras_rel[c] += 1
                else: letras_abs[c.upper()] += 1
                primera = False
    print("   relativas por letra: " + ", ".join(f"{k} {v}" for k, v in letras_rel.most_common()))
    print("   absolutas por letra: " + ", ".join(f"{k} {v}" for k, v in letras_abs.most_common()))

    # ---------------- B
    print("\nB. Recalada: subtrazos que cierran con una curva y después z")
    for tipo in ('abs', 'rel', 'mixto'):
        xs = [x for x in recaladas if x[2] == tipo]
        if not xs: print(f"   {tipo}: ninguno"); continue
        exactos = sum(1 for x in xs if x[4] < 0.01)
        cerca = sum(1 for x in xs if x[3] <= 0.02)
        errs = sorted(x[3] for x in xs)
        print(f"   {tipo:5s}: {len(xs):4d} subtrazos; llegan justo (menos de 0,01 px): {exactos} ({100 * exactos / len(xs):.0f} %); "
              f"a menos del 2 % del tamaño: {cerca} ({100 * cerca / len(xs):.0f} %); mediana del error {100 * st.median(errs):.1f} %, "
              f"percentil 90 {100 * errs[int(0.9 * (len(errs) - 1))]:.1f} %")
    print("   por casa, subtrazos relativos o mixtos (n, llegan justo, mediana del error de los que no):")
    casas = defaultdict(list)
    for x in recaladas:
        if x[2] != 'abs': casas[x[0]].append(x)
    for mo, xs in sorted(casas.items(), key=lambda kv: -len(kv[1])):
        no = [x[3] for x in xs if x[4] >= 0.01]
        print(f"     {mo:32s} {len(xs):4d}  {sum(1 for x in xs if x[4] < 0.01):4d}  " + (f"{100 * st.median(no):5.1f} %" if no else "   -"))
    print("   por casa, subtrazos absolutos (n, llegan justo):")
    casas = defaultdict(list)
    for x in recaladas:
        if x[2] == 'abs': casas[x[0]].append(x)
    for mo, xs in sorted(casas.items(), key=lambda kv: -len(kv[1])):
        print(f"     {mo:32s} {len(xs):4d}  {sum(1 for x in xs if x[4] < 0.01):4d}")

    # ---------------- C
    print("\nC. Rosas: grupos de seis o más rayos por un mismo centro")
    todas = filas_rosa
    completas = [x for x in todas if x['hueco_max'] <= 100 and x['parejo']]
    print(f"   grupos: {len(todas)}; con rayos parejos todo alrededor: {len(completas)}; el resto son abanicos, medias rosas o haces")
    for nombre, G in (("todas", todas), ("parejas todo alrededor", completas)):
        cn = Counter(x['n'] for x in G)
        print(f"   {nombre}: por número de rayos: " + ", ".join(f"{k}: {v}" for k, v in sorted(cn.items())))
    una = [x for x in completas if not x['giro']]
    print(f"   de las parejas, escritas rayo por rayo (sin rotate): {len(una)}; con rotate: {len(completas) - len(una)}")
    cn = Counter(x['n'] for x in una); print("     rayo por rayo, por número: " + ", ".join(f"{k}: {v}" for k, v in sorted(cn.items())))
    cn = Counter(x['n'] for x in completas if x['giro']); print("     con rotate, por número:    " + ", ".join(f"{k}: {v}" for k, v in sorted(cn.items())))
    red = Counter(x['red'] for x in una); print("     rayo por rayo, por red de ángulos (0 = ninguna): " + ", ".join(f"{k}: {v}" for k, v in sorted(red.items())))
    ocho = [x for x in una if x['n'] == 8 and x['red'] == 8 and x['razon']]
    bien = [x for x in ocho if abs(x['razon'] - 1) <= 0.05]
    raiz = [x for x in ocho if abs(x['razon'] - math.sqrt(2)) <= 0.07]
    corto = [x for x in ocho if x['razon'] < 0.95]
    print(f"   rosas de ocho rayos a 45°, rayo por rayo: {len(ocho)}; diagonal igual al eje (5 %): {len(bien)}; "
          f"diagonal raíz de 2 más largo: {len(raiz)}; diagonal más corto: {len(corto)}; otros más largos: {len(ocho) - len(bien) - len(raiz) - len(corto)}")
    print("     razones diagonal/eje: " + " ".join(f"{x['razon']:.2f}" for x in sorted(ocho, key=lambda x: x['razon'])))
    print("     por casa (n, iguales, razones):")
    pc = defaultdict(list)
    for x in ocho: pc[x['modelo']].append(x['razon'])
    for mo, rs in sorted(pc.items(), key=lambda kv: -len(kv[1])):
        print(f"       {mo:32s} {len(rs):3d} {sum(1 for r in rs if abs(r - 1) <= 0.05):3d}   " + " ".join(f"{r:.2f}" for r in sorted(rs)))
    todas8 = [x for x in completas if x['n'] == 8 and x['red'] == 8 and x['seno']]
    print(f"   el seno de 45° de cada rosa de ocho (corrimiento del rayo diagonal / largo del rayo del eje; el de la toleta es 0,71):")
    for x in sorted(todas8, key=lambda x: x['seno']):
        print(f"       {x['modelo']:30s} {x['conj']}/{x['consigna']:20s} eje {x['r_eje']:6.1f}  seno {x['seno']:.3f}  desvío {x['desvio']:+6.1f} px  {'rotate' if x['giro'] else ''}")
    dentro = [x for x in todas8 if abs(x['desvio']) <= 1.0]
    print(f"     a un píxel o menos del valor justo: {len(dentro)} de {len(todas8)} (de ellas con rotate: {sum(1 for x in dentro if x['giro'])})")
    print("   rosas que no son de 4 ni de 8 vientos, rayo por rayo:")
    for x in sorted(una, key=lambda x: (x['red'], x['n'])):
        if x['red'] in (4, 8): continue
        print(f"       {x['modelo']:30s} {x['conj']}/{x['consigna']:22s} {x['n']:3d} rayos, red {x['red']:2d}, {dict(x['tags'])}")
    print("   rosas con rotate:")
    for x in sorted([x for x in completas if x['giro']], key=lambda x: x['n']):
        print(f"       {x['modelo']:30s} {x['conj']}/{x['consigna']:22s} {x['n']:3d} rayos, red {x['red']:2d}, {dict(x['tags'])}")
    print("   por consigna (rosas parejas): " + ", ".join(f"{k} {v}" for k, v in Counter(x['consigna'] for x in completas).most_common()))
    print("   por casa (rosas parejas):     " + ", ".join(f"{k} {v}" for k, v in Counter(x['modelo'] for x in completas).most_common()))

    if '--csv' in sys.argv:
        with open('rosas.csv', 'w', newline='') as fh:
            w = csv.writer(fh)
            w.writerow(['modelo', 'conjunto', 'consigna', 'rep', 'cx', 'cy', 'rayos', 'red', 'hueco_max', 'parejo', 'con_rotate',
                        'razon_diag_eje', 'radio_medio', 'angulos'])
            for x in todas:
                w.writerow([x['modelo'], x['conj'], x['consigna'], x['rep'], x['cx'], x['cy'], x['n'], x['red'], round(x['hueco_max'], 1),
                            int(x['parejo']), int(x['giro']), '' if x['razon'] is None else round(x['razon'], 3), round(x['r_fuera'], 1),
                            ' '.join(f"{a:.1f}" for a in x['angulos'])])
        with open('ordenes.csv', 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['modelo', 'laboratorio', 'absolutas', 'relativas', 'dibujos_con_path', 'dibujos_mayoria_relativa'])
            for mo in sorted(ordenes):
                dm = sum(1 for x in por_dibujo if x[0] == mo and x[3] > x[2]); dp = sum(1 for x in por_dibujo if x[0] == mo and x[2] + x[3] > 0)
                w.writerow([mo, laboratorio(mo), ordenes[mo]['abs'], ordenes[mo]['rel'], dp, dm])
        with open('recaladas.csv', 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['modelo', 'consigna', 'tipo', 'error_relativo', 'error_px', 'ordenes', 'ultima'])
            for x in recaladas: w.writerow([x[0], x[1], x[2], round(x[3], 4), round(x[4], 3), x[5], x[6]])

if __name__ == '__main__':
    main()
