#!/usr/bin/env python3
"""Los nombres que eligen las casas, mirados en dos registros civiles.

Lee nombres.csv (lo escribe nombres.py) y los registros de EE. UU. (SSA 1880-2017, paquete
R `babynames`, clon de github.com/hadley/babynames) y de Chile (Registro Civil 1920-2021,
paquete R `guaguas`, clon de github.com/rivaquiroga/guaguas) en ./datos/. Para cada nombre
usado en inglés busca en EE. UU. y para cada uno usado en castellano busca en Chile: el
año de pico (máxima proporción de nacidos con ese nombre), el mejor puesto, el sexo
mayoritario. Después: mediana ponderada del año de pico, reparto por sexo, parte de los
nacidos cuyo nombre empieza con "Mar" en cada registro, y la historia de "Mara" en los dos.
Solo la corrida base (20261012-2259, 28 casas). Escribe salida_registros.txt por pantalla.
"""
import os, sys, unicodedata
import pandas as pd, pyreadr

AQUI = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(AQUI, 'datos')


def sin_tilde(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


us = pyreadr.read_r(os.path.join(DATOS, 'babynames/data/babynames.rda'))['babynames']
us['year'] = us.year.astype(int)
cl = pd.read_csv(os.path.join(DATOS, 'guaguas/data-raw/1920-2021.csv'))
cl = cl.rename(columns={'anio': 'year', 'nombre': 'name', 'sexo': 'sex', 'proporcion': 'prop'})
# proporción sobre el total de nacidos de ese año (los dos sexos), para que sea comparable
for df in (us, cl):
    tot = df.groupby('year')['n'].sum()
    df['p'] = df['n'] / df['year'].map(tot)
    # puesto del nombre entre los de su sexo en cada año (1 = el más dado)
    df['puesto'] = df.groupby(['year', 'sex'])['n'].rank(method='min', ascending=False).astype(int)

nom = pd.read_csv(os.path.join(AQUI, 'nombres.csv'))
nom = nom[(nom.corrida == '20261012-2259') & (nom.tipo == 'pila')]


def ficha(df, nombre):
    """(año de pico, proporción en el pico, mejor puesto, sexo mayoritario, total)"""
    d = df[df.name == nombre]
    if d.empty:
        return None
    por_año = d.groupby('year')['p'].sum()
    pico = int(por_año.idxmax())
    sexo = d.groupby('sex')['n'].sum().idxmax()
    mejor = int(d[d.sex == sexo].puesto.min())
    return pico, por_año.max(), mejor, sexo, int(d.n.sum())


def tabla(idioma, reg, etiqueta):
    d = nom[nom.idioma == idioma]
    cuenta = d.groupby('nombre').size().sort_values(ascending=False)
    filas = []
    print(f'\n== {etiqueta}: nombres usados en {idioma} ({len(cuenta)} distintos, {cuenta.sum()} textos)')
    print(f'{"nombre":12} {"textos":>6} {"pico":>5} {"por mil":>8} {"mejor puesto":>13} {"sexo":>5}')
    for n, c in cuenta.items():
        f = ficha(reg, n)
        if f is None and idioma == 'es':
            f = ficha(reg, sin_tilde(n))
        if f is None:
            print(f'{n:12} {c:6d}   — no está en el registro')
            continue
        pico, pp, mejor, sexo, tot = f
        filas.append((n, c, pico, pp, mejor, sexo))
        print(f'{n:12} {c:6d} {pico:5d} {1000*pp:8.2f} {mejor:13d} {sexo:>5}')
    df = pd.DataFrame(filas, columns=['nombre', 'textos', 'pico', 'p', 'mejor', 'sexo'])
    # mediana ponderada del año de pico
    orden = df.sort_values('pico')
    acum = orden.textos.cumsum()
    mediana = int(orden.pico[acum >= acum.iloc[-1] / 2].iloc[0])
    print(f'mediana ponderada del año de pico: {mediana}; media ponderada: {(df.pico*df.textos).sum()/df.textos.sum():.0f}')
    print('por sexo (textos):', df.groupby('sexo').textos.sum().to_dict())
    print('nombres que nunca entraron entre los 100 de su sexo:', int((df.mejor > 100).sum()), 'de', len(df),
          '; textos:', int(df[df.mejor > 100].textos.sum()), 'de', int(df.textos.sum()))
    return df


def mar(df, etiqueta):
    print(f'\n== {etiqueta}: parte de los nacidos cuyo nombre empieza con "Mar"')
    m = df[df.name.str.startswith('Mar')]
    tot = df.groupby('year')['n'].sum()
    s = m.groupby('year')['n'].sum() / tot
    for a, b in ((1920, 1939), (1940, 1959), (1960, 1979), (1980, 1999), (2000, 2017)):
        print(f'  {a}-{b}: {100*s.loc[a:b].mean():.1f} %')
    print(f'  todo el registro: {100*m.n.sum()/df.n.sum():.1f} %')
    top = m.groupby('name')['n'].sum().sort_values(ascending=False).head(8)
    print('  los más dados:', ', '.join(f'{k} {v}' for k, v in top.items()))


def historia(df, nombre, etiqueta):
    d = df[(df.name == nombre)]
    print(f'\n== {etiqueta}: {nombre}')
    if d.empty:
        print('  no figura')
        return
    por = d.groupby('year').agg(n=('n', 'sum'), p=('p', 'sum'))
    print(f'  primer año: {int(por.index.min())}; total: {int(por.n.sum())}; pico: {int(por.p.idxmax())} ({por.n.max()} nacidos, {1000*por.p.max():.3f} por mil)')
    for y in (1920, 1950, 1980, 2000, 2010, int(por.index.max())):
        if y in por.index:
            print(f'  {y}: {int(por.loc[y, "n"])} ({1000*por.loc[y, "p"]:.3f} por mil)')
    f = ficha(df, nombre)
    print(f'  mejor puesto entre los de su sexo: {f[2]}; sexo: {f[3]}')


if __name__ == '__main__':
    en = tabla('en', us, 'EE. UU.')
    es = tabla('es', cl, 'Chile')
    mar(us, 'EE. UU.')
    mar(cl, 'Chile')
    historia(us, 'Mara', 'EE. UU.')
    historia(cl, 'Mara', 'Chile')
    for n in ('Elara', 'Lyra', 'Kael', 'Elena', 'Marcus', 'Marta', 'Vera', 'Clara'):
        f = ficha(us, n)
        print(f'EE. UU. {n}: {f}')
    for n in ('Elara', 'Mara', 'Marcos', 'Marta', 'Vera', 'Clara', 'Mariana', 'Maia', 'Maya'):
        f = ficha(cl, n)
        print(f'Chile {n}: {f}')
