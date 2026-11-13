#!/usr/bin/env python3
"""Figura del cuaderno del 14/10/2026: los nombres que eligen las casas, puestos en el año
en que cada uno fue más dado en un registro civil (Chile para los textos en castellano,
EE. UU. para los de inglés), y la parte de nombres que empiezan con "Mar" en los
registros y en los textos. Lee nombres.csv (de nombres.py) y los registros en ./datos/.
Escribe 2026-10-14_nombres.svg y, si está cairosvg, el PNG.
"""
import os, unicodedata, collections
import pandas as pd, pyreadr

AQUI = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(AQUI, 'datos')
AZUL, NARANJA, TINTA, GRIS, FONDO = '#2a78d6', '#eb6834', '#0b0b0b', '#52514e', '#fcfcfb'

us = pyreadr.read_r(os.path.join(DATOS, 'babynames/data/babynames.rda'))['babynames']
us['year'] = us.year.astype(int)
cl = pd.read_csv(os.path.join(DATOS, 'guaguas/data-raw/1920-2021.csv')).rename(
    columns={'anio': 'year', 'nombre': 'name', 'sexo': 'sex'})
for df in (us, cl):
    tot = df.groupby('year')['n'].sum()
    df['p'] = df['n'] / df['year'].map(tot)

nom = pd.read_csv(os.path.join(AQUI, 'nombres.csv'))
nom = nom[(nom.corrida == '20261012-2259') & (nom.tipo == 'pila')]


def ficha(df, nombre):
    d = df[df.name == nombre]
    if d.empty:
        return None
    por = d.groupby('year')['p'].sum()
    return int(por.idxmax()), d.groupby('sex')['n'].sum().idxmax()


def puntos(idioma, reg):
    cuenta = nom[nom.idioma == idioma].groupby('nombre').size()
    out = []
    for n, c in cuenta.items():
        f = ficha(reg, n)
        if f:
            out.append((n, int(c), f[0], f[1]))
    return out


def mar(df):
    m = df[df.name.str.startswith('Mar')]
    return 100 * m.n.sum() / df.n.sum()


def mar_casas(idioma):
    d = nom[(nom.idioma == idioma) & (nom.consigna != 'p5')]  # sin el tautograma
    return 100 * d.nombre.str.startswith('Mar').mean()


W, H = 900, 800
X0, X1 = 70, 830
A0, A1 = 1880, 2022


def x(a):
    return X0 + (a - A0) / (A1 - A0) * (X1 - X0)


svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Georgia, serif" font-size="13" fill="{TINTA}">',
       f'<rect width="{W}" height="{H}" fill="{FONDO}"/>']


def panel(y0, idioma, reg, titulo, nota):
    alto = 250
    pts = puntos(idioma, reg)
    maxc = max(c for _, c, _, _ in pts)
    def y(c):
        return y0 + alto - (c ** 0.5) / (maxc ** 0.5) * (alto - 30)
    svg.append(f'<text x="{X0}" y="{y0 - 14}" font-size="15" font-weight="bold">{titulo}</text>')
    svg.append(f'<text x="{X0}" y="{y0 + 2}" font-size="12" fill="{GRIS}">{nota}</text>')
    # ejes
    svg.append(f'<line x1="{X0}" y1="{y0 + alto}" x2="{X1}" y2="{y0 + alto}" stroke="{GRIS}" stroke-width="1"/>')
    for a in range(1880, 2021, 20):
        svg.append(f'<line x1="{x(a):.1f}" y1="{y0 + alto}" x2="{x(a):.1f}" y2="{y0 + alto + 5}" stroke="{GRIS}"/>')
        svg.append(f'<text x="{x(a):.1f}" y="{y0 + alto + 18}" text-anchor="middle" font-size="11" fill="{GRIS}">{a}</text>')
    for c in (1, 5, 10, 20):
        if c <= maxc:
            svg.append(f'<line x1="{X0}" y1="{y(c):.1f}" x2="{X1}" y2="{y(c):.1f}" stroke="#e4e3df" stroke-width="1"/>')
            svg.append(f'<text x="{X0 - 6}" y="{y(c) + 4:.1f}" text-anchor="end" font-size="11" fill="{GRIS}">{c}</text>')
    svg.append(f'<text x="{X0 - 40}" y="{y0 + 8}" font-size="11" fill="{GRIS}">textos</text>')
    # puntos, con corrimiento horizontal cuando coinciden año y cuenta; primero se dibujan
    # todos los puntos, después las etiquetas, probando corrimientos verticales para que no
    # se pisen entre sí ni con los puntos (las cajas ocupadas se van anotando)
    vistos = collections.Counter()
    cajas, pos = [], []
    def libre(x1, y1, x2, y2):
        return all(x2 < a or x1 > c or y2 < b or y1 > d for a, b, c, d in cajas)
    for n, c, a, s in sorted(pts, key=lambda t: (-t[1], t[0])):
        k = (a, c)
        dx = vistos[k] * 7
        vistos[k] += 1
        cx, cy = x(a) + dx, y(c)
        pos.append((n, c, a, s, cx, cy))
        cajas.append((cx - 5, cy - 5, cx + 5, cy + 5))
        svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="{AZUL if s == "F" else NARANJA}" stroke="{FONDO}" stroke-width="1.5"/>')
    cajas.append((X0 - 60, y0 + alto + 2, X1 + 60, y0 + alto + 30))  # el eje y sus años
    for n, c, a, s, cx, cy in pos:
        if not (c >= 3 or n in ('Mara', 'Mira', 'Vera', 'Clara', 'Vale', 'Selene', 'Elías', 'Elias', 'Silas', 'Marta', 'Sara')):
            continue
        et = f'{n} {c}'
        ancho = 7.4 * len(et)
        puesto = False
        for dy in (0, -15, 15, -30, 30, -45, 45, -60, 60):
            for lado in (('start', 8), ('end', -8)) if a <= 1995 else (('end', -8), ('start', 8)):
                tx = cx + lado[1]
                x1 = tx if lado[0] == 'start' else tx - ancho
                if x1 < X0 - 60 or x1 + ancho > W - 8:
                    continue
                if libre(x1, cy + dy - 7, x1 + ancho, cy + dy + 7):
                    svg.append(f'<text x="{tx:.1f}" y="{cy + dy + 4:.1f}" text-anchor="{lado[0]}" font-size="12">{et}</text>')
                    if dy:
                        svg.append(f'<line x1="{cx:.1f}" y1="{cy + (4 if dy > 0 else -4):.1f}" x2="{(x1 if lado[0]=="start" else x1 + ancho):.1f}" y2="{cy + dy:.1f}" stroke="{GRIS}" stroke-width="0.6"/>')
                    cajas.append((x1, cy + dy - 7, x1 + ancho, cy + dy + 7))
                    puesto = True
                    break
            if puesto:
                break


panel(46, 'es', cl, 'Textos en castellano, nombres puestos en su año de pico en el registro de Chile (1920-2021)',
      'cada punto es un nombre; altura: en cuántos textos aparece')
panel(361, 'en', us, 'Textos en inglés, nombres puestos en su año de pico en el registro de EE. UU. (1880-2017)',
      'los nombres de 2017 y 2021 siguen subiendo al final del registro')
# leyenda
ly = 660
svg.append(f'<circle cx="{X0 + 6}" cy="{ly}" r="4.5" fill="{AZUL}"/><text x="{X0 + 16}" y="{ly + 4}">nombre de mujer en el registro</text>')
svg.append(f'<circle cx="{X0 + 236}" cy="{ly}" r="4.5" fill="{NARANJA}"/><text x="{X0 + 246}" y="{ly + 4}">nombre de varón en el registro</text>')

# barras de "Mar"
by = 705
svg.append(f'<text x="{X0}" y="{by - 10}" font-size="15" font-weight="bold">Nombres que empiezan con «Mar», cada cien</text>')
filas = [('nacidos en Chile, 1920-2021', mar(cl)), ('textos en castellano (sin el tautograma)', mar_casas('es')),
         ('nacidos en EE. UU., 1880-2017', mar(us)), ('textos en inglés (sin el tautograma)', mar_casas('en'))]
for i, (et, v) in enumerate(filas):
    yy = by + i * 20
    svg.append(f'<text x="{X0 + 300}" y="{yy + 11}" text-anchor="end" font-size="12">{et}</text>')
    svg.append(f'<rect x="{X0 + 310}" y="{yy}" width="{v * 10:.1f}" height="14" rx="2" fill="{TINTA if "textos" in et else GRIS}"/>')
    svg.append(f'<text x="{X0 + 316 + v * 10:.1f}" y="{yy + 11}" font-size="12">{v:.0f}</text>')

svg.append('</svg>')
salida = os.path.join(AQUI, '2026-10-14_nombres.svg')
open(salida, 'w', encoding='utf-8').write('\n'.join(svg))
print('escrito', salida)
try:
    import cairosvg
    cairosvg.svg2png(url=salida, write_to=salida[:-4] + '.png', output_width=1800)
    print('y el PNG')
except ImportError:
    print('sin cairosvg, no hay PNG')
