#!/usr/bin/env python3
"""figura.py - la figura del cuaderno de tiempo libre del 12/10/2026 (tres_derrotas.svg).

Tres paneles:
  A. El Diario del 8/9 al 12/10 de 1492 como un solo <path> escrito en órdenes relativas,
     sobre carta plana, una unidad = una legua (la altura está exagerada).
  B. Dónde cae esa misma suma sobre el mapa según cuánto mida la legua y cuánto se
     corra la aguja: una red de dos familias de curvas, con las islas candidatas adentro.
  C. Qué parte de las órdenes de <path> de cada casa son relativas.

Uso: python3 figura.py [carpeta con gshhs_i.dat y gshhsmeta_i.dat] [paso de la costa en px, por defecto 5]
Lee derrota.py (para la suma) y ordenes.csv (lo escribe rosa.py --csv). Los datos de
costas son los de basemap v2.0.0 (GSHHG 2.3.6), sacados del historial del repositorio
como en el cuaderno del 2/10; sin ellos dibuja el mapa sin costas.
Solo biblioteca estándar.
"""
import sys, os, math, csv, struct, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))

def busca(nombre):
    for cand in (nombre, '2026-10-12_' + nombre):
        p = os.path.join(AQUI, cand)
        if os.path.exists(p): return p
    raise SystemExit(f'falta {nombre}')

spec = importlib.util.spec_from_file_location('derrota', busca('derrota.py'))
D = importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
DATOS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, 'datos')
PASO = float(sys.argv[2]) if len(sys.argv) > 2 else 5.0     # separación mínima, en píxeles, entre puntos de costa

# colores (paleta de referencia de la guía de gráficos: azul y naranja, tinta y gris)
FONDO, TINTA, TINTA2, GRIS, GRIS_CLARO = '#fcfcfb', '#0b0b0b', '#52514e', '#8a8984', '#e4e3df'
AZUL, NARANJA, TIERRA = '#2a78d6', '#eb6834', '#dddcd6'
ESTILO = (f'text{{font-size:9.5px;fill:{TINTA2}}}.t{{font-size:14px;font-weight:bold;fill:{TINTA}}}.u{{font-size:10.5px}}'
          f'.k{{fill:{TINTA}}}.g{{fill:{GRIS}}}.c{{font-size:9px}}.d{{font-size:10px}}.m{{text-anchor:middle}}.e{{text-anchor:end}}'
          f'.b{{font-weight:bold}}.i{{font-style:italic}}.h{{stroke:{FONDO};stroke-width:3px;paint-order:stroke;stroke-linejoin:round}}'
          f'.o{{font-family:monospace;font-size:9px}}')

def n(v):
    """número con un decimal, sin ceros de más"""
    return f'{v:.1f}'.rstrip('0').rstrip('.')

W = 1000
o = []
def t(x, y, s, cls=''):
    s = s.replace('&', '&amp;').replace('<', '&lt;')
    o.append(f'<text x="{n(x)}" y="{n(y)}"' + (f' class="{cls}"' if cls else '') + f'>{s}</text>')

# ------------------------------------------------------------------ panel A
tramos = D.lectura('IFE')
d = 'M0,0'
x = y = 0.0; pts = [(0.0, 0.0)]; fechas = [t_[0] for t_ in D.TRAMOS]
for r, l in tramos:
    dx = l * math.sin(math.radians(r)); dy = -l * math.cos(math.radians(r))
    if abs(dy) < 1e-9: d += f' h{dx:g}'
    else: d += f' l{round(dx, 1):g},{round(dy, 1):g}'
    x += dx; y += dy; pts.append((x, y))
AX0, AY0, SX, SY = 960.0, 150.0, 0.84, 0.84 * 3       # origen (La Gomera) a la derecha; el oeste va a la izquierda
t(40, 30, 'A. El Diario como un solo trazo', 't')
t(40, 47, 'Del 8 de septiembre a las 2 de la madrugada del 12 de octubre de 1492: 42 tramos, una unidad = una legua, '
          'carta plana. La altura está exagerada tres veces.', 'u')
o.append(f'<line x1="{n(AX0 - 1100 * SX)}" y1="{n(AY0)}" x2="{n(AX0)}" y2="{n(AY0)}" stroke="{GRIS_CLARO}"/>')
t(AX0 - 660 * SX, AY0 - 5, 'paralelo de la salida', 'c g m')
o.append(f'<path transform="translate({n(AX0)},{n(AY0)}) scale({SX},{SY:g})" d="{d}" fill="none" stroke="{AZUL}" stroke-width="2" '
         f'vector-effect="non-scaling-stroke" stroke-linejoin="round" stroke-linecap="round"/>')
o.append(f'<g fill="{FONDO}" stroke="{AZUL}">')
for f in dict.fromkeys(fechas):                       # un punto al final de cada día
    ult = max(i for i, ff in enumerate(fechas) if ff == f)
    qx, qy = pts[ult + 1]
    o.append(f'<circle cx="{n(AX0 + qx * SX)}" cy="{n(AY0 + qy * SY)}" r="1.6"/>')
o.append('</g>')
o.append(f'<circle cx="{n(AX0)}" cy="{n(AY0)}" r="4" fill="{TINTA}" stroke="{FONDO}" stroke-width="2"/>')
t(AX0, AY0 + 17, 'La Gomera, 8/9', 'd k e')
fx, fy = pts[-1]
o.append(f'<circle cx="{n(AX0 + fx * SX)}" cy="{n(AY0 + fy * SY)}" r="4" fill="{AZUL}" stroke="{FONDO}" stroke-width="2"/>')
t(AX0 + fx * SX + 34, AY0 + fy * SY + 15, '12/10, 2 de la madrugada', 'd k')
t(AX0 + fx * SX + 156, AY0 + fy * SY + 15, f'{-fx:.0f} leguas al oeste y {fy:.0f} al sur de la salida', 'd')
i23 = max(i for i, ff in enumerate(fechas) if ff == '23/9'); qx, qy = pts[i23 + 1]
t(AX0 + qx * SX + 22, AY0 + qy * SY + 3, '22 y 23/9: al Oesnoroeste y al Noroeste')
i7 = max(i for i, ff in enumerate(fechas) if ff == '7/10'); qx, qy = pts[i7]
t(AX0 + qx * SX, AY0 + qy * SY - 8, '7/10: vira al Oessudoeste', 'm')
ex = 800                                              # escala
o.append(f'<line x1="{ex}" y1="194" x2="{n(ex + 100 * SX)}" y2="194" stroke="{TINTA}" stroke-width="1.5"/>')
t(ex + 100 * SX + 6, 197.5, '100 leguas')
dd = d.split(' ')                                     # el atributo d, escrito
lineas = [' '.join(dd[i:i + 16]) for i in range(0, len(dd), 16)]
for k, ln in enumerate(lineas):
    o.append(f'<text x="40" y="{224 + 12 * k}" class="o">{"d=&quot;" if k == 0 else ""}{ln}{"&quot;" if k == len(lineas) - 1 else ""}</text>')

# ------------------------------------------------------------------ panel B
BX, BY, BW = 40, 306, 580
LON0, LON1, LAT0, LAT1 = -84.0, -69.5, 19.6, 28.8
K = BW / ((LON1 - LON0) * math.cos(math.radians(24.2)))
BH = (LAT1 - LAT0) * K
def P(lat, lon):
    return (BX + (lon - LON0) * math.cos(math.radians(24.2)) * K, BY + (LAT1 - lat) * K)

t(BX, BY - 26, 'B. La misma suma sobre el mapa', 't')
t(BX, BY - 10, 'Dónde termina según lo que mida la legua (azul) y lo que la aguja se corra al oeste (naranja).', 'u')
o.append(f'<clipPath id="mapa"><rect x="{BX}" y="{BY}" width="{BW}" height="{n(BH)}"/></clipPath>')
o.append(f'<rect x="{BX}" y="{BY}" width="{BW}" height="{n(BH)}" fill="#f3f6f9" stroke="{GRIS_CLARO}"/>')
o.append('<g clip-path="url(#mapa)">')
meta, dat = os.path.join(DATOS, 'gshhsmeta_i.dat'), os.path.join(DATOS, 'gshhs_i.dat')
if os.path.exists(meta) and os.path.exists(dat):
    raw = open(dat, 'rb').read()
    o.append(f'<g fill="{TIERRA}" stroke="{GRIS}" stroke-width="0.5">')
    for ln in open(meta):
        p = ln.split()
        if int(p[0]) != 1: continue                      # solo tierra
        s_, n_ = float(p[3]), float(p[4])
        if n_ < LAT0 - 0.5 or s_ > LAT1 + 0.5: continue
        off, bl = int(p[5]), int(p[6])
        v = struct.unpack('<%df' % (bl // 4), raw[off:off + bl])
        xy = [((v[i] + 180) % 360 - 180, v[i + 1]) for i in range(0, len(v), 2)]
        if not any(LON0 - 0.5 <= lo <= LON1 + 0.5 and LAT0 - 0.5 <= la <= LAT1 + 0.5 for lo, la in xy): continue
        # recorte grueso: los puntos de fuera se arriman al marco y el clipPath hace el resto
        xy = [(max(LON0 - 1, min(LON1 + 1, lo)), max(LAT0 - 1, min(LAT1 + 1, la))) for lo, la in xy]
        limpio = []
        for q in xy:                                     # sin puntos a menos de PASO px del anterior
            a_ = P(q[1], q[0])
            if not limpio or abs(a_[0] - limpio[-1][0]) + abs(a_[1] - limpio[-1][1]) >= PASO: limpio.append(a_)
        if len(limpio) < 3: continue
        ancho_p = max(q[0] for q in limpio) - min(q[0] for q in limpio); alto_p = max(q[1] for q in limpio) - min(q[1] for q in limpio)
        if ancho_p + alto_p < 3: continue                # islotes de menos de 3 px
        o.append('<polygon points="' + ' '.join(f'{a_:.0f},{b_:.0f}' for a_, b_ in limpio) + '"/>')
    o.append('</g>')
o.append(f'<g stroke="{GRIS_CLARO}" stroke-width="0.6">')    # paralelos y meridianos
for la in range(20, 29, 2):
    yy = P(la, LON0)[1]
    o.append(f'<line x1="{BX}" y1="{n(yy)}" x2="{BX + BW}" y2="{n(yy)}"/>')
for lo in range(-84, -69, 2):
    xx = P(LAT0, lo)[0]
    o.append(f'<line x1="{n(xx)}" y1="{BY}" x2="{n(xx)}" y2="{n(BY + BH)}"/>')
o.append('</g>')
# la red
LEGUAS = (2.67, 2.82, 3.0, 3.2)
GIROS = (0.0, 2.8125, 5.625, 8.4375, 11.25)       # de cuarto en cuarto de cuarta
def fin(L, g): return D.estima(tramos, L, g)[-1]
for color, curvas in ((AZUL, [[P(*fin(L, g * 1.25)) for g in range(0, 10)] for L in LEGUAS]),
                      (NARANJA, [[P(*fin(2.55 + k * 0.08, g)) for k in range(0, 10)] for g in GIROS])):
    o.append(f'<g fill="none" stroke="{color}" stroke-width="1.6">')
    for c in curvas:
        o.append('<polyline points="' + ' '.join(f'{n(a)},{n(b)}' for a, b in c) + '"/>')
    o.append('</g>')
o.append('</g>')
for L in LEGUAS:                                    # rótulos de la red
    a, b = P(*fin(L, 0.0))
    t(a, b - 7, f'{L:g}'.replace('.', ','), 'k m h')
a, b = P(*fin(LEGUAS[0], 0.0)); t(a + 18, b - 7, 'millas náuticas por legua', 'h')
for g, nom in zip(GIROS, ('aguja justa', '¼ de cuarta', '½ cuarta', '¾ de cuarta', 'una cuarta (11¼°)')):
    a, b = P(*fin(2.55, g))
    if BY < b < BY + BH: t(BX + BW + 6, b + 3.5, nom)
# las dos lecturas
a1 = P(*D.estima(D.lectura('IFE'), 2.82)[-1]); a2 = P(*D.estima(D.lectura('NAV'), 2.82)[-1])
o.append(f'<circle cx="{n(a1[0])}" cy="{n(a1[1])}" r="3.2" fill="{AZUL}" stroke="{FONDO}" stroke-width="1.5"/>')
o.append(f'<circle cx="{n(a2[0])}" cy="{n(a2[1])}" r="3.2" fill="{FONDO}" stroke="{AZUL}" stroke-width="1.5"/>')
o.append(f'<line x1="{n(a2[0] + 3)}" y1="{n(a2[1] + 4)}" x2="{n(a2[0] + 22)}" y2="{n(a2[1] + 30)}" stroke="{GRIS}" stroke-width="0.7"/>')
t(a2[0] + 24, a2[1] + 38, 'lleno: 15 y 27 leguas (Ife);', 'c h')
t(a2[0] + 24, a2[1] + 49, 'hueco: 19 y 22 (Navarrete). 19 km', 'c h')
# las islas
for nombre, la, lo in D.CANDIDATAS:
    a, b = P(la, lo)
    o.append(f'<circle cx="{n(a)}" cy="{n(b)}" r="4.2" fill="{TINTA}" stroke="{FONDO}" stroke-width="2"/>')
    corto = {'Egg (Molander)': 'Egg', 'Watling / San Salvador': 'Watling (San Salvador)'}.get(nombre, nombre)
    if nombre.startswith('Cayos Plana'): t(a - 7, b + 12, corto, 'd k b e h')
    elif nombre.startswith('Egg'): t(a - 7, b - 6, corto, 'd k b e h')
    else: t(a + 8, b - 4, corto, 'd k b h')
for la in (20, 22, 24, 26, 28):
    t(BX - 5, P(la, LON0)[1] + 3.5, f'{la}° N', 'c g e')
for lo in (-82, -78, -74, -70):
    t(P(LAT0, lo)[0], BY + BH + 13, f'{-lo}° O', 'c g m')
t(P(27.9, -81.6)[0], P(27.9, -81.6)[1], 'Florida', 'g m i')
t(P(21.9, -79.2)[0], P(21.9, -79.2)[1], 'Cuba', 'g m i')

# ------------------------------------------------------------------ panel C
CX, CY = 760, 306
t(CX - 62, CY - 26, 'C. Quién escribe en relativas', 't')
t(CX - 62, CY - 10, 'Órdenes de <path> en minúscula, por casa (%)', 'u')
filas = []
for r in csv.DictReader(open(busca('ordenes.csv'))):
    a, b, nd = int(r['absolutas']), int(r['relativas']), int(r['dibujos_con_path'])
    if nd < 3: continue                               # quedan afuera las variantes con uno o dos dibujos
    filas.append((100 * b / (a + b), r['modelo'], r['laboratorio']))
filas.sort(reverse=True)
alto = (BH - 22) / len(filas); ancho = 150
o.append(f'<rect x="{CX - 62}" y="{CY + 2}" width="9" height="9" rx="2" fill="{AZUL}"/>'); t(CX - 49, CY + 10, 'OpenAI')
o.append(f'<rect x="{CX + 2}" y="{CY + 2}" width="9" height="9" rx="2" fill="{GRIS}"/>'); t(CX + 15, CY + 10, 'las demás')
o.append(f'<line x1="{CX + 64}" y1="{CY + 22}" x2="{CX + 64}" y2="{n(CY + BH)}" stroke="{GRIS_CLARO}"/>')
barras = {AZUL: [], GRIS: []}
for k, (pct, mo, lab) in enumerate(filas):
    yy = CY + 22 + k * alto
    nombre = mo.replace('-2026-04-23', '').replace('-razonamiento-minimo', '').replace('-preview', '').replace('-0125', '').replace('-0613', '')
    t(CX + 58, yy + alto * 0.72, nombre, 'c k e')
    w = max(0.0, pct / 100 * ancho)
    if w > 0.5:                                       # barra con la punta redondeada, apoyada en el eje
        r_ = min(3, w / 2)
        barras[AZUL if lab == 'OpenAI' else GRIS].append(
            f'M{CX + 64},{n(yy + 1.5)}h{n(w - r_)}a{n(r_)},{n(r_)} 0 0 1 {n(r_)},{n(r_)}v{n(alto - 3 - 2 * r_)}a{n(r_)},{n(r_)} 0 0 1 -{n(r_)},{n(r_)}h-{n(w - r_)}z')
    t(CX + 64 + w + 4, yy + alto * 0.72, f'{pct:.0f}', 'c')
for color, ds in barras.items():
    o.append(f'<path fill="{color}" d="{"".join(ds)}"/>')

H = BY + BH + 62
t(40, H - 26, 'Fuentes: los tramos, del extracto de Las Casas en la edición de B. W. Ife (King\'s College London); las islas, de la Tabla I de '
              'Goldsmith y Richardson (WHOI-92-14) y, los Cayos Plana, de Wikipedia;', 'c g')
t(40, H - 14, 'costas GSHHG 2.3.6; panel C, 714 dibujo.svg del repositorio proyectos-de-ley. La red no tiene corriente ni abatimiento: es la '
              'suma cruda. Cuaderno de tiempo libre, 12/10/2026.', 'c g')
cab = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.0f}" width="{W}" height="{H:.0f}" '
       f'font-family="Helvetica, Arial, sans-serif">\n<title>Tres derrotas: el Diario de 1492 como trazo, la red de la estima y las órdenes '
       f'relativas por casa</title>\n<style>{ESTILO}</style>\n<rect width="{W}" height="{H:.0f}" fill="{FONDO}"/>')
open(os.path.join(AQUI, 'tres_derrotas.svg'), 'w').write(cab + '\n' + '\n'.join(o) + '\n</svg>\n')
print('escrito tres_derrotas.svg', W, 'x', round(H))
