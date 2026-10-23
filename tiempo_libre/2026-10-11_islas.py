#!/usr/bin/env python3
"""islas.py - ¿Dónde estaban las naves a las diez de la noche del 11 de octubre de 1492,
según cuál sea la isla del desembarco, y qué tierra tenían cerca?

Es una reconstrucción gruesa, no una derrota. Toma del Diario (extracto de Las Casas,
asiento del jueves 11) solo cuatro datos: que después de la puesta del sol navegaron
"al Oueste", que andaban "12 millas cada hora", que a las dos de la madrugada la tierra
estaba a "2 leguas", y que la lumbre se vio "a las diez de la noche". Para cada isla
candidata y para cada derrota recta hacia el oeste que termina a dos leguas de ella,
retrocede cuatro horas y mide la distancia a la tierra más cercana. Descarta las
derrotas que entre las diez y las dos pisan tierra, y cuenta aparte las que la pisan
antes, entre la puesta del sol y las diez (lo señaló el agente revisor).

Uso: python3 islas.py DIR [--csv salida.csv]
DIR tiene gshhs_f.dat y gshhsmeta_f.dat (costas GSHHG de resolución completa, del
paquete basemap-data-hires 2.0.0 de PyPI). Formato: el meta trae, por polígono, tipo,
área (km2), puntos, lat mínima, lat máxima, desplazamiento, largo en bytes e id;
el .dat, pares (lon, lat) en float32.
Necesita: numpy, scipy y matplotlib (este último solo para la prueba de punto en polígono).
"""
import sys, math, csv
import numpy as np
from scipy.spatial import cKDTree
from matplotlib.path import Path as MplPath
from collections import Counter

KM_LAT = 110.75            # km por grado de latitud hacia los 23°N
OJO = 6.5                  # altura del ojo sobre el agua, en metros (ver el cuaderno)
K_HOR = 3.86               # km de horizonte por raíz de metro, con refracción normal

NOMBRES = {
    '1121': 'San Salvador (Watling)', '650': 'Cat', '6085': 'Conception', '1718': 'Rum Cay',
    '527': 'Long Island', '2840': 'Samana Cay', '6175': 'Plana Cays (oeste)',
    '6644': 'Plana Cays (este)', '763': 'Mayaguana', '536': 'Acklins', '871': 'Crooked',
    '3435': 'Long Cay', '3827': 'Gran Turca', '6508': 'Salt Cay', '927': 'East Caicos',
    '736': 'Middle Caicos', '914': 'North Caicos', '1307': 'Providenciales',
    '3421': 'South Caicos', '245': 'Gran Inagua', '1249': 'Pequeña Inagua', '542': 'Eleuthera',
    '5714': 'Little San Salvador', '23213': 'Egg', '8994': 'Royal Island', '11041': 'Russell Island',
    '3346': 'Great Harbour Cay', '1029': 'Gran Exuma', '290': 'Gran Abaco', '898': 'New Providence',
    '22': 'Cuba',
}
# isla candidata -> ids de sus polígonos
CANDIDATAS = [
    ('San Salvador (Watling)', ['1121']),
    ('Cat', ['650']),
    ('Conception', ['6085']),
    ('Samana Cay', ['2840']),
    ('Plana Cays', ['6175', '6644']),
    ('Mayaguana', ['763']),
    ('Gran Turca', ['3827']),
    ('East Caicos', ['927']),
    ('Egg', ['23213']),
]

def cargar(d):
    raw = open(f'{d}/gshhs_f.dat', 'rb').read()
    pol = []
    for ln in open(f'{d}/gshhsmeta_f.dat'):
        p = ln.split()
        if int(p[0]) != 1 or float(p[1]) > 1e6:      # solo tierra; sin continentes
            continue
        if float(p[4]) < 19.0 or float(p[3]) > 28.0:
            continue
        off, bl = int(p[5]), int(p[6])
        a = np.frombuffer(raw[off:off + bl], dtype='<f4').reshape(-1, 2).astype(float)
        lon = (a[:, 0] + 180) % 360 - 180
        if lon.max() < -80.0 or lon.min() > -68.0:
            continue
        pol.append(dict(id=p[7], area=float(p[1]), lon=lon, lat=a[:, 1]))
    return pol

class Plano:
    """proyección plana local (km) alrededor de un punto: alcanza para 200 km"""
    def __init__(self, lat0, lon0):
        self.lat0, self.lon0 = lat0, lon0
        self.kx = 111.32 * math.cos(math.radians(lat0))
    def xy(self, lon, lat):
        return (np.asarray(lon) - self.lon0) * self.kx, (np.asarray(lat) - self.lat0) * KM_LAT
    def ll(self, x, y):
        return self.lon0 + x / self.kx, self.lat0 + y / KM_LAT

def nube(pol, pl, radio, paso=0.1):
    """puntos de costa cada 'paso' km (vértices más puntos intermedios) a menos de 'radio' km
    del centro, con el índice del polígono de cada uno; y el árbol para buscar el más cercano"""
    X, I = [], []
    for i, q in enumerate(pol):
        x, y = pl.xy(q['lon'], q['lat'])
        if np.hypot(x, y).min() > radio:
            continue
        P = np.column_stack([x, y])
        d = np.hypot(*np.diff(P, axis=0).T)
        trozos = [P]
        for k in np.where(d > paso)[0]:
            n = int(d[k] // paso) + 1
            t = np.arange(1, n) / n
            trozos.append(P[k] + t[:, None] * (P[k + 1] - P[k]))
        P = np.vstack(trozos)
        X.append(P); I.append(np.full(len(P), i))
    X = np.vstack(X); I = np.concatenate(I)
    return cKDTree(X), I

def dentro(P, x, y):
    """puntos (n,2) dentro del polígono (x, y)"""
    return MplPath(np.column_stack([x, y])).contains_points(P)

def altura_necesaria(d_km):
    """altura (m) a la que tiene que estar una luz para asomar sobre el horizonte a d_km, con el ojo a OJO"""
    r = d_km / K_HOR - math.sqrt(OJO)
    return 0.0 if r <= 0 else r * r

def hacer_nombres(pol):
    """a los cayos que no están en la tabla les pone el nombre de la isla con nombre más cercana"""
    con = [q for q in pol if q['id'] in NOMBRES]
    cen = np.array([[q['lon'].mean(), q['lat'].mean()] for q in con])
    out = {}
    for q in pol:
        if q['id'] in NOMBRES:
            out[q['id']] = NOMBRES[q['id']]; continue
        # distancia del centro del cayo a los vértices de cada isla con nombre
        best = (1e9, None)
        lo, la = q['lon'].mean(), q['lat'].mean()
        kx = 111.32 * math.cos(math.radians(la))
        for c in con:
            if abs(c['lat'].mean() - la) > 1.5 or abs(c['lon'].mean() - lo) > 1.5:
                continue
            d = np.hypot((c['lon'] - lo) * kx, (c['lat'] - la) * KM_LAT).min()
            if d < best[0]:
                best = (d, NOMBRES[c['id']])
        out[q['id']] = (f"cayo junto a {best[1]}" if best[0] <= 12
                        else f"cayo sin nombre en la tabla ({la:.2f}N {-lo:.2f}O)")
    return out

def derrotas(pol, nom, ids, milla_km, millas_4h, rumbo=270.0, paso=0.5, nombres=None):
    """todas las derrotas rectas con ese rumbo que terminan a dos leguas de la isla"""
    L2 = 8 * milla_km                 # dos leguas de cuatro millas
    D = millas_4h * milla_km          # lo andado de las diez a las dos
    th = math.radians(rumbo)
    u = np.array([math.sin(th), math.cos(th)])       # dirección de avance (x este, y norte)
    nrm = np.array([-u[1], u[0]])                     # perpendicular
    isla = [q for q in pol if q['id'] in ids]
    lat0 = np.mean([q['lat'].mean() for q in isla]); lon0 = np.mean([q['lon'].mean() for q in isla])
    pl = Plano(lat0, lon0)
    arbol, I = nube(pol, pl, 330)
    arbol_isla, _ = nube(isla, pl, 330)
    c = arbol_isla.data @ nrm
    s = np.arange(-260.0, 60.0, 0.1)
    res = []
    for off in np.arange(c.min() - L2, c.max() + L2 + 1e-9, paso):
        P = off * nrm + s[:, None] * u
        dd, _ = arbol_isla.query(P)
        kk = np.where(dd <= L2)[0]
        if len(kk) == 0:
            continue
        p2 = P[kk[0]]
        p10 = p2 - D * u
        tr = p10 + np.linspace(0, 1, 400)[:, None] * (p2 - p10)
        dtr, itr = arbol.query(tr)
        pisa = False
        for qi in set(I[itr[dtr < 2.0]]):
            x, y = pl.xy(pol[qi]['lon'], pol[qi]['lat'])
            if dentro(tr, x, y).any():
                pisa = True
        # lo mismo para el tramo anterior: de la puesta del sol (90 millas antes de las dos) a las diez
        p0 = p2 - 90 * milla_km * u
        tr0 = p0 + np.linspace(0, 1, 400)[:, None] * (p10 - p0)
        d0, i0 = arbol.query(tr0)
        antes = False
        for qi in set(I[i0[d0 < 2.0]]):
            x, y = pl.xy(pol[qi]['lon'], pol[qi]['lat'])
            if dentro(tr0, x, y).any():
                antes = True
        d10, i10 = arbol.query(p10)
        lon2, lat2 = pl.ll(*p2); lon10, lat10 = pl.ll(*p10)
        res.append(dict(off=float(off), lat2=lat2, lon2=lon2, lat10=lat10, lon10=lon10, d10=float(d10),
                        tierra=nombres[pol[I[i10]]['id']], pisa=pisa, antes=antes))
    return res

def correr(pol, nombres, milla_km, millas_4h, rumbo=270.0, filas=None):
    L2 = 8 * milla_km; D = millas_4h * milla_km
    print(f"\n### milla de {milla_km*1000:.0f} m; de las diez a las dos, {millas_4h:g} millas = {D:.1f} km; "
          f"dos leguas = {L2:.1f} km; rumbo verdadero {rumbo:g}°")
    print(f"{'isla del desembarco':24s} {'derrotas':>8s}  {'km a la tierra más cercana, a las diez':38s} {'≤22':>4s} {'≤35':>4s}  {'luz a (m)':>9s}  tierra más cercana (derrotas)")
    for nom, ids in CANDIDATAS:
        res = derrotas(pol, nom, ids, milla_km, millas_4h, rumbo, nombres=nombres)
        ok = [r for r in res if not r['pisa']]
        if not ok:
            print(f"{nom:24s} {0:>4d}/{len(res):<3d}  toda derrota con ese rumbo pisa otra tierra antes")
            continue
        d = np.array([r['d10'] for r in ok])
        cnt = Counter(r['tierra'] for r in ok).most_common(3)
        print(f"{nom:24s} {len(ok):>4d}/{len(res):<3d}  mín {d.min():5.1f}  mediana {np.median(d):5.1f}  máx {d.max():5.1f}      "
              f"{(d <= 22).sum():>4d} {(d <= 35).sum():>4d}  {altura_necesaria(d.min()):4.0f}–{altura_necesaria(d.max()):<4.0f}  "
              + "; ".join(f"{t} ({n})" for t, n in cnt))
        na = sum(1 for r in ok if r['antes'])
        if na:
            ok2 = [r for r in ok if not r['antes']]
            d2 = np.array([r['d10'] for r in ok2])
            print(f"{'':24s} de esas, {na} pisan tierra antes de las diez (entre la puesta del sol y las diez); "
                  f"sin ellas quedan {len(ok2)}, con tierra a 35 km o menos en {(d2 <= 35).sum()}")
        if filas is not None:
            for r in ok:
                filas.append([nom, milla_km, millas_4h, rumbo, f"{r['lat2']:.4f}", f"{r['lon2']:.4f}", f"{r['lat10']:.4f}",
                              f"{r['lon10']:.4f}", f"{r['d10']:.2f}", r['tierra'], f"{altura_necesaria(r['d10']):.0f}", int(r['antes'])])

if __name__ == '__main__':
    d = sys.argv[1]
    pol = cargar(d)
    nombres = hacer_nombres(pol)
    print(f"{len(pol)} polígonos de tierra en la caja 19–28°N, 68–80°O")
    print(f"ojo a {OJO} m: horizonte a {K_HOR*math.sqrt(OJO):.1f} km")
    for h in (0, 2, 10, 35, 43, 63):
        print(f"  una luz a {h:2d} m asoma hasta {K_HOR*(math.sqrt(OJO)+math.sqrt(h)):.1f} km")
    for txt, dkm in (("48 millas de 1.480 m", 48 * 1.480), ("56 millas de 1.480 m", 56 * 1.480),
                     ("48 millas de 1.238 m", 48 * 1.238), ("35 millas náuticas", 35 * 1.852),
                     ("29 millas náuticas", 29 * 1.852)):
        print(f"  para asomar a {dkm:5.1f} km ({txt}) tiene que estar a {altura_necesaria(dkm):.0f} m")
    for ojo in (4.3 + 1.5, 6.5, 9.1):
        r = 71.0 / K_HOR - math.sqrt(ojo)
        print(f"  con el ojo a {ojo:.1f} m, a 71 km: {r*r:.0f} m")
    filas = []
    correr(pol, nombres, 1.480, 48, filas=filas)          # milla romana, 4 h a 12 millas
    correr(pol, nombres, 1.238, 48, filas=filas)          # milla corta ("geométrica")
    correr(pol, nombres, 1.480, 43.5)                     # 90 millas de la puesta a las dos: 10,9 por hora
    correr(pol, nombres, 1.480, 48, rumbo=270 - 11.25)    # una cuarta al sur del oeste
    correr(pol, nombres, 1.480, 48, rumbo=270 + 11.25)    # una cuarta al norte del oeste
    if '--csv' in sys.argv:
        with open(sys.argv[sys.argv.index('--csv') + 1], 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['isla', 'milla_km', 'millas_4h', 'rumbo', 'lat_2h', 'lon_2h', 'lat_22h', 'lon_22h',
                        'km_a_tierra_22h', 'tierra', 'altura_luz_m', 'pisa_tierra_antes_de_las_22h'])
            w.writerows(filas)
