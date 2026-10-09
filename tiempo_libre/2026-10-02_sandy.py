#!/usr/bin/env python3
"""La isla Sandy en los datos de costas de basemap (GSHHS), antes y después.

Uso: python3 sandy.py DIR
DIR tiene los archivos de datos de dos versiones de basemap, sacados del
historial de github.com/matplotlib/basemap:
  old_{l,i,f}.dat y oldmeta_{l,i,f}.dat  -> etiqueta v1.0.7rel (GSHHS 2.2.0, commit 8442448, 7/3/2012)
  new_{i,f}.dat  y newmeta_{i,f}.dat     -> v2.0.0 (GSHHG 2.3.6, commit 006cf93, 23/9/2016)
Formato de basemap: el meta trae, por polígono, tipo, área (km2), puntos,
lat mínima, lat máxima, desplazamiento en bytes, largo en bytes e id; el .dat,
pares (lon, lat) en float32.
"""
import sys, math
import numpy as np

R = 6371.0088

def leer(d, tag, res):
    raw = open(f'{d}/{tag}_{res}.dat', 'rb').read()
    for ln in open(f'{d}/{tag}meta_{res}.dat'):
        p = ln.split()
        off, bl = int(p[5]), int(p[6])
        yield dict(tipo=int(p[0]), area=float(p[1]), n=int(p[2]), s=float(p[3]),
                   nn=float(p[4]), off=off, bl=bl, id=p[7], raw=raw)

def puntos(q):
    return np.frombuffer(q['raw'][q['off']:q['off'] + q['bl']], dtype='<f4').reshape(-1, 2).astype(float)

def cerca(d, tag, res, lat, lon, radio_km):
    """polígonos con algún punto a menos de radio_km de (lat, lon)"""
    dlat = math.degrees(radio_km / R)
    out = []
    for q in leer(d, tag, res):
        if q['nn'] < lat - dlat or q['s'] > lat + dlat:
            continue
        a = puntos(q)
        lo = (a[:, 0] + 180) % 360 - 180
        dl = np.radians(lo - lon); la = np.radians(a[:, 1]); l0 = math.radians(lat)
        h = np.sin((la - l0) / 2) ** 2 + np.cos(la) * math.cos(l0) * np.sin(dl / 2) ** 2
        dist = 2 * R * np.arcsin(np.sqrt(h))
        if dist.min() < radio_km:
            out.append((q, a, float(dist.min())))
    return out

def area_km2(a):
    """área sobre la esfera (fórmula de la línea de latitud; alcanza para una isla chica)"""
    lon = np.radians(a[:, 0]); lat = np.radians(a[:, 1])
    s = 0.0
    for i in range(len(a) - 1):
        s += (lon[i + 1] - lon[i]) * (2 + math.sin(lat[i]) + math.sin(lat[i + 1]))
    return abs(s) * R * R / 2

def perimetro_km(a):
    la = np.radians(a[:, 1]); lo = np.radians(a[:, 0])
    h = np.sin(np.diff(la) / 2) ** 2 + np.cos(la[:-1]) * np.cos(la[1:]) * np.sin(np.diff(lo) / 2) ** 2
    return float((2 * R * np.arcsin(np.sqrt(h))).sum())

SANDY = (-19.22, 159.93)

FANTASMAS = [  # nombre, lat, lon (posiciones de las fuentes citadas en el cuaderno)
    ("Sandy", -19.22, 159.93),
    ("Pepys", -47.0, -59.0),
    ("Auroras (Atrevida, isla del sur)", -53.256, -47.954),
    ("Saxemberg", -30.75, -19.667),
    ("Thompson", -53.933, 5.5),
    ("Dougherty", -59.333, -120.333),
    ("Bermeja", -0 + 22.646, -90.855),
    ("Sarah Ann", 4.0, -154.367),
    ("Podestá", -32.233, -89.133),
    ("Emerald", -57.5, 162.2),
    ("Nimrod", -56.0, -158.0),
    ("Ernest Legouvé (arrecife)", -35.2, -150.667),
    ("Maria Theresa (arrecife)", -36.833, -136.65),
]
REALES = [
    ("Rockall", 57.596, -13.687),
    ("rocas Clerke", -55.02, -34.68),
    ("rocas Cormorán / Shag", -53.5475, -42.02),
    ("roca Negra / Black Rock", -53.652, -41.800),
    ("Malden", -4.017, -154.933),
    ("Bouvet", -54.42, 3.36),
]

def tabla(d, tag, amin):
    out = []
    for q in leer(d, tag, 'f'):
        if q['tipo'] != 1 or q['area'] < amin or q['nn'] < -60:
            continue
        a = puntos(q)
        out.append((q['area'], q['s'], q['nn'], float(a[:, 0].min()), float(a[:, 0].max()), q['id']))
    return out

def diferencias(d):
    """islas de 1 km2 o más, al norte de 60°S, que estaban en 2012 y hoy no tienen
    ninguna con la caja a menos de 0,05°; y cuántas de esas tienen una de área
    parecida (±50 %) a menos de medio grado (o sea, corridas y no borradas)"""
    old = tabla(d, 'old', 1.0); new = tabla(d, 'new', 0.3)
    cajas = np.array([x[1:5] for x in new]); areas = np.array([x[0] for x in new])
    sin = []
    for x in old:
        dd = np.abs(cajas - np.array(x[1:5])).max(axis=1)
        if dd.min() > 0.05:
            corrida = bool(((dd < 0.5) & (np.abs(areas - x[0]) / x[0] < 0.5)).any())
            sin.append((x, corrida))
    print(f"  islas de 1 km2 o más al norte de 60°S en 2012: {len(old)}; sin par en la versión actual: {len(sin)}; "
          f"de esas, con una parecida a menos de medio grado: {sum(c for _, c in sin)}")
    for x, c in sorted(sin, key=lambda t: -t[0][0])[:6]:
        print(f"     {x[0]:7.1f} km2 en {x[1]:.2f}, {x[3]:.2f} (id {x[5]}) {'corrida' if c else 'sin candidata cerca'}")
    chicas = sum(1 for q in leer(d, 'new', 'f') if q['tipo'] == 1 and q['area'] < 0.2)
    todas = sum(1 for q in leer(d, 'new', 'f') if q['tipo'] == 1)
    print(f"  polígonos de tierra en la versión actual: {todas}; de menos de 0,2 km2: {chicas}")

if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else 'gshhs'
    print("== La isla Sandy, por resolución y versión")
    for tag, nombre in (('old', 'basemap 1.0.7 (GSHHS 2.2.0)'), ('new', 'basemap 2.0.0 (GSHHG 2.3.6)')):
        for res in ('l', 'i', 'f'):
            try:
                hall = cerca(d, tag, res, *SANDY, 20)
            except FileNotFoundError:
                continue
            if not hall:
                print(f"  {nombre} [{res}]: nada a menos de 20 km")
            for q, a, dist in hall:
                print(f"  {nombre} [{res}]: id {q['id']}, {q['n']} puntos, {q['bl']} bytes desde el byte {q['off']}, "
                      f"área declarada {q['area']:.2f} km2")
                if tag == 'old':
                    np.savetxt({'f': 'sandy_contorno.txt', 'i': 'sandy_10_puntos.txt', 'l': 'sandy_5_puntos.txt'}[res], a, fmt='%.5f',
                               header='lon lat (isla Sandy en GSHHS 2.2.0, resolución ' + res + ')')
                if res == 'f':
                    ns = (a[:, 1].max() - a[:, 1].min()) * math.pi / 180 * R
                    eo = (a[:, 0].max() - a[:, 0].min()) * math.pi / 180 * R * math.cos(math.radians(SANDY[0]))
                    print(f"     de {a[:,1].min():.4f} a {a[:,1].max():.4f} de latitud y de {a[:,0].min():.4f} a {a[:,0].max():.4f} de longitud")
                    print(f"     {ns:.1f} km de norte a sur, {eo:.1f} km de este a oeste; área calculada {area_km2(a):.1f} km2; perímetro {perimetro_km(a):.1f} km")
                    dx = np.abs(np.diff(a[:, 0])); dy = np.abs(np.diff(a[:, 1]))
                    paso = 1 / 1200
                    kx = dx / paso; ky = dy / paso
                    ok = (np.abs(kx - np.round(kx)) < 0.12) & (np.abs(ky - np.round(ky)) < 0.12)
                    print(f"     tramos: {len(dx)}; con los dos lados múltiplos de 3 segundos de arco (±0,12): {int(ok.sum())}")
                    diag = (np.round(kx) >= 1) & (np.round(ky) >= 1)
                    print(f"     tramos en diagonal: {int(diag.sum())}; solo norte-sur: {int(((np.round(kx)==0)&(np.round(ky)>=1)).sum())}; solo este-oeste: {int(((np.round(ky)==0)&(np.round(kx)>=1)).sum())}")
    print()
    print("== Otras islas de la lista, en resolución completa (algo de costa a menos de 30 km)")
    for grupo, lista in (("no existen", FANTASMAS), ("existen", REALES)):
        for nombre, lat, lon in lista:
            fila = []
            for tag in ('old', 'new'):
                hall = cerca(d, tag, 'f', lat, lon, 30)
                if not hall and grupo == "existen":
                    lejos = cerca(d, tag, 'f', lat, lon, 200)
                    if not lejos:
                        fila.append("nada, ni a 200 km"); continue
                if hall:
                    q, a, dist = min(hall, key=lambda h: h[2])
                    fila.append(f"{len(hall)} polígono(s), el más cercano a {dist:.1f} km ({q['area']:.2f} km2)")
                else:
                    fila.append("nada")
            print(f"  [{grupo}] {nombre}: 2012 -> {fila[0]} | actual -> {fila[1]}")
    print()
    print("== Qué más cambió entre las dos versiones")
    diferencias(d)
