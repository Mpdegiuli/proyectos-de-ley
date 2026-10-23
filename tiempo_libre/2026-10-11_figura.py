#!/usr/bin/env python3
"""figura.py - La noche del 11 al 12 de octubre de 1492 en dos dibujos.

Arriba, un mapa: para cada isla propuesta como lugar del desembarco, la raya de las
posiciones de las diez de la noche (una por cada latitud por la que pudieron llegar
navegando al oeste), pintada según tuvieran o no tierra a 35 km o menos.
Abajo, la altura de la luna a lo largo de esa noche, en hora solar verdadera del lugar.

Lee DIR/gshhs_f.dat y DIR/gshhsmeta_f.dat (costas) y el CSV que escribe islas.py.
Escribe la_noche_y_las_islas.svg y, si está cairosvg, el PNG.
Uso: python3 figura.py DIR derrotas.csv [salida.svg]
Necesita: numpy y ephem; cairosvg solo para el PNG.
"""
import sys, csv, math
import numpy as np
import ephem

DIR, CSV = sys.argv[1], sys.argv[2]
OUT = sys.argv[3] if len(sys.argv) > 3 else 'la_noche_y_las_islas.svg'

# ---------- colores (dos series categóricas validadas con el validador de la paleta; lo demás, tinta y grises)
SUP, TINTA, TINTA2, TENUE, GRILLA = '#fcfcfb', '#0b0b0b', '#52514e', '#8a8983', '#e4e2db'
CON, SIN = '#2a78d6', '#eb6834'          # con tierra cerca / sin tierra cerca
TIERRA, COSTA = '#dcd9cf', '#b3afa3'
LUNA = '#52514e'

W = 1000
MX0, MX1, MY0 = 40, 960, 118
LON0, LON1, LAT0, LAT1 = -76.0, -69.8, 21.1, 24.9
PXLON = (MX1 - MX0) / (LON1 - LON0)
PXLAT = PXLON * 110.75 / (111.32 * math.cos(math.radians(23.0)))
MY1 = MY0 + (LAT1 - LAT0) * PXLAT
KM = PXLON / (111.32 * math.cos(math.radians(23.0)))      # px por km

def X(lon): return MX0 + (lon - LON0) * PXLON
def Y(lat): return MY0 + (LAT1 - lat) * PXLAT

def dp(P, tol):
    """Douglas-Peucker sobre un arreglo (n,2)"""
    if len(P) < 3: return P
    keep = np.zeros(len(P), bool); keep[0] = keep[-1] = True
    pila = [(0, len(P) - 1)]
    while pila:
        a, b = pila.pop()
        if b <= a + 1: continue
        d = P[b] - P[a]; L = math.hypot(*d)
        seg = P[a + 1:b]
        dist = (np.hypot(*(seg - P[a]).T) if L == 0
                else np.abs(d[0] * (seg[:, 1] - P[a, 1]) - d[1] * (seg[:, 0] - P[a, 0])) / L)
        k = int(dist.argmax())
        if dist[k] > tol:
            keep[a + 1 + k] = True
            pila += [(a, a + 1 + k), (a + 1 + k, b)]
    return P[keep]

def costas():
    raw = open(f'{DIR}/gshhs_f.dat', 'rb').read()
    out = []
    for ln in open(f'{DIR}/gshhsmeta_f.dat'):
        p = ln.split()
        if int(p[0]) != 1 or float(p[1]) > 1e6 or float(p[1]) < 2.0: continue
        if float(p[4]) < LAT0 - 0.3 or float(p[3]) > LAT1 + 0.3: continue
        a = np.frombuffer(raw[int(p[5]):int(p[5]) + int(p[6])], dtype='<f4').reshape(-1, 2).astype(float)
        lon = (a[:, 0] + 180) % 360 - 180
        if lon.max() < LON0 - 0.3 or lon.min() > LON1 + 0.3: continue
        P = dp(np.column_stack([X(lon), Y(a[:, 1])]), 1.4)
        if len(P) >= 3: out.append(P)
    return out

s = []
def t(x, y, txt, cls='', extra=''):
    s.append(f'<text x="{x:.1f}" y="{y:.1f}"{" class=" + chr(34) + cls + chr(34) if cls else ""}{extra}>{txt}</text>')

s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 1050" width="{W}" height="1050">')
s.append(f'<rect width="100%" height="100%" fill="{SUP}"/>')
s.append('<style>text{font-family:DejaVu Sans,Verdana,sans-serif;font-size:12px;fill:' + TINTA2 + '}'
         '.h{font-size:20px;font-weight:bold;fill:' + TINTA + '}.b{font-weight:bold;fill:' + TINTA + '}'
         '.s{font-size:11px;fill:' + TENUE + '}.m{text-anchor:middle}.e{text-anchor:end}'
         '.g{stroke:' + GRILLA + ';stroke-width:1;fill:none}</style>')
t(40, 40, 'Dónde estaban a las diez', 'h')
t(40, 62, 'Para cada isla propuesta como Guanahaní, la raya gruesa marca dónde estaban las naves a las diez de la noche del 11 de octubre de 1492,')
t(40, 79, 'cuatro horas y 48 millas antes de quedar a dos leguas de tierra, según por qué latitud hayan llegado navegando al oeste.')
t(40, 96, 'Reconstrucción con cuatro datos del Diario; milla de 1.480 m; costas de GSHHG. La flecha gris es una de esas derrotas, la del medio. Egg queda fuera del mapa.', 's')

# ---------- mapa
s.append(f'<clipPath id="caja"><rect x="{MX0}" y="{MY0}" width="{MX1 - MX0}" height="{MY1 - MY0:.1f}"/></clipPath>')
s.append(f'<rect x="{MX0}" y="{MY0}" width="{MX1 - MX0}" height="{MY1 - MY0:.1f}" fill="none" class="g"/>')
s.append('<g clip-path="url(#caja)">')
for lon in range(-75, -69):
    s.append(f'<line class="g" x1="{X(lon):.1f}" y1="{MY0}" x2="{X(lon):.1f}" y2="{MY1:.1f}"/>')
for lat in range(22, 25):
    s.append(f'<line class="g" x1="{MX0}" y1="{Y(lat):.1f}" x2="{MX1}" y2="{Y(lat):.1f}"/>')
for P in costas():
    d = 'M' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in P) + 'Z'
    s.append(f'<path d="{d}" fill="{TIERRA}" stroke="{COSTA}" stroke-width="0.6"/>')

filas = [r for r in csv.DictReader(open(CSV)) if r['milla_km'] == '1.48' and r['millas_4h'] == '48' and r['rumbo'] == '270.0']
islas = []
for r in filas:
    if r['isla'] not in islas: islas.append(r['isla'])
resumen = {}
for isla in islas:
    rs = [r for r in filas if r['isla'] == isla]
    d = np.array([float(r['km_a_tierra_22h']) for r in rs])
    resumen[isla] = (len(rs), int((d <= 35).sum()), float(d.min()), float(np.median(d)), float(d.max()))
    if isla == 'Egg': continue                      # queda fuera del mapa, al noroeste
    # la línea de las dos de la madrugada
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in dp(np.array([[X(float(r["lon_2h"])), Y(float(r["lat_2h"]))] for r in rs]), 0.8))
    s.append(f'<polyline points="{pts}" fill="none" stroke="{TENUE}" stroke-width="1.2"/>')
    # la derrota del medio
    m = rs[len(rs) // 2]
    xa, ya, xb, yb = X(float(m['lon_22h'])), Y(float(m['lat_22h'])), X(float(m['lon_2h'])), Y(float(m['lat_2h']))
    s.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb + 5:.1f}" y2="{yb:.1f}" stroke="{TENUE}" stroke-width="1.2"/>')
    s.append(f'<path d="M{xb:.1f},{yb:.1f}l7,-3.5v7z" fill="{TENUE}"/>')
    # la raya de las diez, por tramos del mismo color
    tramo, col = [], None
    def cerrar():
        if len(tramo) == 1:
            s.append(f'<circle cx="{tramo[0][0]:.1f}" cy="{tramo[0][1]:.1f}" r="2.5" fill="{col}"/>')
        elif tramo:
            pp = ' '.join(f'{x:.1f},{y:.1f}' for x, y in dp(np.array(tramo), 0.6))
            s.append(f'<polyline points="{pp}" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
                     f'<title>{isla}: {n35} de {ntot} derrotas con tierra a 35 km o menos a las diez</title></polyline>')
    ntot, n35 = resumen[isla][0], resumen[isla][1]
    for r in rs:
        c = CON if float(r['km_a_tierra_22h']) <= 35 else SIN
        p = (X(float(r['lon_22h'])), Y(float(r['lat_22h'])))
        if c != col:
            cerrar(); tramo = [p]; col = c
        else:
            tramo.append(p)
    cerrar()
s.append('</g>')

# nombres: (texto, lon, lat, clase, ancla) - las candidatas en negrita
NOM = [('Watling', -74.57, 23.895, 'b', 'm'), ('Cat', -75.80, 24.45, 'b', 'e'),
       ('Conception', -75.16, 23.80, 'b', 'e'), ('Rum Cay', -74.87, 23.545, '', 'm'),
       ('Long Island', -75.32, 23.05, '', 'e'), ('Samana Cay', -73.90, 23.17, 'b', 'e'),
       ('Plana Cays', -73.45, 22.80, 'b', 'm'), ('Mayaguana', -72.95, 22.20, 'b', 'm'),
       ('Acklins', -74.33, 22.33, '', 'e'), ('Crooked', -74.40, 22.80, '', 'e'),
       ('Caicos', -72.0, 21.60, '', 'm'), ('East Caicos', -71.52, 21.49, 'b', 'm'),
       ('Gran Turca', -71.10, 21.33, 'b', 'm'), ('Gran Inagua', -73.35, 21.22, '', 'm'),
       ('Exumas', -75.62, 23.60, '', 'm')]
for txt, lo, la, cls, anc in NOM:
    t(X(lo), Y(la), txt, (cls + ' ' + anc).strip())
# rótulos de las rayas
ROT = [('San Salvador (Watling)', -73.52, 24.03), ('Cat', -74.58, 24.60), ('Conception', -74.21, 23.74),
       ('Samana Cay', -72.80, 23.09), ('Plana Cays', -72.62, 22.87), ('Mayaguana', -71.86, 22.40),
       ('East Caicos', -70.62, 21.92), ('Gran Turca', -69.83, 21.24)]
for isla, lo, la in ROT:
    n, n35, mn, med, mx = resumen[isla]
    cls = 's e' if isla == 'Gran Turca' else 's'
    t(X(lo), Y(la), f'si fue {"Watling" if isla.startswith("San") else isla}:', cls)
    t(X(lo), Y(la) + 13, f'tierra a {mn:.0f}–{mx:.0f} km'.replace('.', ','), cls)
# escala y regla de alcance
ex, ey = MX0 + 24, MY1 - 22
s.append(f'<line x1="{ex}" y1="{ey}" x2="{ex + 100 * KM:.1f}" y2="{ey}" stroke="{TINTA2}" stroke-width="1.5"/>')
t(ex + 50 * KM, ey - 6, '100 km', 's m')
cx, cy = X(-70.45), Y(24.42)
for rkm in (32.6, 15.3):
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{rkm * KM:.1f}" fill="none" stroke="{TINTA2}" stroke-width="1"/>')
s.append(f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="{TINTA2}"/>')
t(MX1 - 10, cy + 35.2 * KM + 18, 'Hasta dónde asoma una luz, con el ojo a 6,5 m:', 's e')
t(MX1 - 10, cy + 35.2 * KM + 32, 'círculo chico, una antorcha a 2 m (15 km);', 's e')
t(MX1 - 10, cy + 35.2 * KM + 46, 'círculo grande, un fuego a 35 m, el alto de High Cay según Wolper (33 km)', 's e')
# leyenda
lx, ly = X(-73.25), MY0 + 26
s.append(f'<line x1="{lx}" y1="{ly - 4}" x2="{lx + 26}" y2="{ly - 4}" stroke="{CON}" stroke-width="5" stroke-linecap="round"/>')
t(lx + 36, ly, 'a las diez había tierra a 35 km o menos')
s.append(f'<line x1="{lx}" y1="{ly + 14}" x2="{lx + 26}" y2="{ly + 14}" stroke="{SIN}" stroke-width="5" stroke-linecap="round"/>')
t(lx + 36, ly + 18, 'a las diez no había tierra a 35 km')
s.append(f'<line x1="{lx}" y1="{ly + 32}" x2="{lx + 26}" y2="{ly + 32}" stroke="{TENUE}" stroke-width="1.2"/>')
t(lx + 36, ly + 36, 'a dos leguas de la isla: las dos de la madrugada')
for lon in range(-75, -69):
    t(X(lon), MY1 + 14, f'{-lon}° O', 's m')
for lat in range(22, 25):
    t(MX0 - 6, Y(lat) + 4, f'{lat}°', 's e')

# ---------- la luna de esa noche
def jdn_juliano(a, m, d):
    x = (14 - m) // 12; y = a + 4800 - x; mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083
J11 = jdn_juliano(1492, 10, 11)
LAT, LON = 24.0, -74.4
o = ephem.Observer(); o.lat, o.lon, o.elevation, o.pressure = str(LAT), str(LON), 6.5, 0   # sin refracción: la curva queda lisa
def verdadera(tt):
    sol = ephem.Sun(); q = ephem.Observer(); q.lon = str(LON); q.lat = '0'; q.date = tt; sol.compute(q)
    return ((float(q.sidereal_time()) - float(sol.ra)) * 12 / math.pi + 12) % 24
TY0 = MY1 + 88; TY1 = TY0 + 170
H0, H1 = 17.0, 31.0                                   # de las 17 a las 7 del otro día
def TX(h): return MX0 + (h - H0) / (H1 - H0) * (MX1 - MX0)
A0, A1 = -25.0, 95.0
def TYy(a): return TY1 - (a - A0) / (A1 - A0) * (TY1 - TY0)
pts = []
for k in range(0, 14 * 4 + 1):
    tt = ephem.Date(J11 - 2415020 + (H0 - 12 - 0.25 - LON / 15 + k / 4) / 24)   # hora verdadera = media + 15 min
    hv = verdadera(tt); hv = hv + 24 if hv < 12 else hv
    o.date = tt; l = ephem.Moon(o)
    pts.append((hv, math.degrees(l.alt)))
t(40, TY0 - 52, 'La luna de esa noche', 'h')
t(40, TY0 - 31, 'Altura de la luna sobre el horizonte, frente a Watling, en hora solar verdadera. A las diez no había salido: salió a las 22:43.')
t(40, TY0 - 14, 'A las dos estaba a 42° de altura y al este justo, o sea a popa de una nave que va al oeste, alumbrando lo que hubiera por la proa.')
s.append(f'<rect x="{TX(19.0):.1f}" y="{TY0}" width="{TX(29.0) - TX(19.0):.1f}" height="{TY1 - TY0}" fill="{GRILLA}" opacity="0.45"/>')
for a in (0, 30, 60):
    s.append(f'<line class="g" x1="{MX0}" y1="{TYy(a):.1f}" x2="{MX1}" y2="{TYy(a):.1f}"' + (f' style="stroke:{TENUE}"' if a == 0 else '') + '/>')
    t(MX0 - 6, TYy(a) + 4, f'{a}°', 's e')
for h in range(17, 32):
    t(TX(h), TY1 + 15, f'{h % 24}', 's m')
t(MX1, TY1 + 30, 'hora (17 del jueves 11 a 7 del viernes 12); en gris, la noche cerrada, sin crepúsculo', 's e')
s.append(f'<clipPath id="noche"><rect x="{MX0}" y="{TY0}" width="{MX1 - MX0}" height="{TY1 - TY0}"/></clipPath>')
s.append('<polyline clip-path="url(#noche)" points="' + ' '.join(f'{TX(h):.1f},{TYy(a):.1f}' for h, a in pts) + f'" fill="none" stroke="{LUNA}" stroke-width="2" stroke-linejoin="round"/>')
EV = [(17 + 44 / 60, 'se pone el sol', '17:44', 0), (18 + 40 / 60, 'hora del gusano', 'de Bermuda, 18:40', 1),
      (22.0, 'la lumbre', '22:00, luna a −9°', 0), (22 + 43 / 60, 'sale la luna', '22:43', 1),
      (26.0, 'tierra', '2:00, luna a 42°', 0), (30 + 16 / 60, 'sale el sol', '6:16', 2)]
for h, a1, a2, baja in EV:
    alt = np.interp(h, [p[0] for p in pts], [p[1] for p in pts])
    s.append(f'<line x1="{TX(h):.1f}" y1="{TY0 + (6, 34, 100)[baja]}" x2="{TX(h):.1f}" y2="{TY1}" stroke="{TENUE}" stroke-width="1"/>')
    if a1 in ('la lumbre', 'tierra', 'sale la luna'):
        s.append(f'<circle cx="{TX(h):.1f}" cy="{TYy(alt):.1f}" r="4.5" fill="{LUNA}" stroke="{SUP}" stroke-width="2"><title>{a1}: luna a {alt:.0f}°</title></circle>')
    yy = TY0 + (6, 34, 100)[baja]
    if h > 30: t(TX(h) - 5, yy + 9, a1, 'b e'); t(TX(h) - 5, yy + 23, a2, 's e')
    else: t(TX(h) + 5, yy + 9, a1, 'b'); t(TX(h) + 5, yy + 23, a2, 's')
s.append('</svg>')
open(OUT, 'w').write('\n'.join(s))
print('escrito', OUT, len('\n'.join(s)), 'bytes')
for k, v in resumen.items(): print(k, v)
try:
    import cairosvg
    cairosvg.svg2png(url=OUT, write_to=OUT[:-4] + '.png', scale=1.5)
    print('escrito', OUT[:-4] + '.png')
except Exception as e:
    print('sin PNG:', e)
