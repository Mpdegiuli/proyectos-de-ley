#!/usr/bin/env python3
"""Nombres de persona en los textos del sondeo `escritura` del repositorio proyectos-de-ley.

Lee corridas/sondeos/escritura/<corrida>/{es,en}/<casa>_pN.md. No abre cartas/ (Maia
todavía no las leyó). Dos modos:

  nombres.py REPO --descubrir   Lista para revisar a mano: palabras con mayúscula inicial
                                que figuran como nombre de pila en dos registros civiles
                                (EE. UU. 1880-2017, SSA, paquete R `babynames`; Chile
                                1920-2021, Registro Civil, paquete R `guaguas`), más las
                                que no están en ningún registro, nunca aparecen en
                                minúscula en el corpus y vienen en medio de una oración
                                (apellidos, nombres raros). Con contextos.
  nombres.py REPO               Cuenta, por casa, idioma y consigna, los nombres de la
                                lista curada de abajo (hecha leyendo la salida de
                                --descubrir el 14/10/2026) y escribe nombres.csv.

La lista curada excluye lo que en el corpus es otra cosa (Sol, Luna, Dale, Mira en
castellano, San Juan, Jack Frost, "Roman coin", "Sandy beaches", Smudge el gato) y las
personas reales. Pide pandas; los registros solo hacen falta para --descubrir y para
registros.py.
"""
import sys, re, os, glob, csv, collections, unicodedata

REPO = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else '.'
AQUI = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(AQUI, 'datos')

# ---- lista curada ---------------------------------------------------------------------
PILA = {
    'en': '''Mara Sarah Elena Sam Marcus Marta Maya Mira Daniel Elias Silas Mark Sara Leo
             Sally Margaret Tom Alex Alice Selene Maria Julian Samuel Sylvester Sofia Danny
             Susie Lena Viktor Sven Mikhail Delia Marie Marisol Ines Marguerite Victor
             Marianne Olivia Ben David Jake Lucy Jonas Anna Jon Eli Chris Sibyl James Marco
             Nadia Corin Vale Teodor Clara'''.split(),
    'es': '''Mara Marcos Marta Elena Clara Vera Carlos Lucía Lucas Martín Marina Sofía
             Mariano Julián Ana Pablo Inés Santiago Susana Mateo Elías María Tomás Miguel
             Rodrigo Leandro Carolina Pedro Darío Ramona Aurelio Camila Carmen Beatriz Laura
             Iván Mauro Julia Simón Lina Raúl Hernán Luis'''.split(),
}
APELLIDO = {
    'en': '''Voss Reyes Doyle Morgan Hale Hayes Rowe Kane Miller Harris Doren Hendersons
             Dvorak Marsh'''.split(),
    'es': '''Reyes Vidal Molina Salcedo Guerrero Iriarte Ferrero Peralta Vargas Ramírez
             Méndez'''.split(),
}
APODO = {'en': [], 'es': ['Tano']}

PAL = re.compile(r"[A-ZÁÉÍÓÚÑÜ][a-záéíóúñü]+")
MEDIO = re.compile(r"[\w,;:(\[]\s*$")


def normal(s):
    return unicodedata.normalize('NFC', s)


def textos(repo):
    out = []
    for ruta in sorted(glob.glob(os.path.join(repo, 'corridas/sondeos/escritura/*/*/*.md'))):
        partes = ruta.split(os.sep)
        corrida, idioma, arch = partes[-3], partes[-2], partes[-1]
        m = re.match(r'(.+)_p(\d+)\.md$', arch)
        if not m or idioma not in ('es', 'en'):
            continue
        out.append((corrida, idioma, m.group(1), 'p' + m.group(2), ruta,
                    normal(open(ruta, encoding='utf-8').read())))
    return out


def cargar_lexico():
    import pyreadr, pandas as pd
    us = pyreadr.read_r(os.path.join(DATOS, 'babynames/data/babynames.rda'))['babynames']
    cl = pd.read_csv(os.path.join(DATOS, 'guaguas/data-raw/1920-2021.csv'))
    us_tot = us.groupby('name')['n'].sum()
    cl_tot = cl.groupby('nombre')['n'].sum()
    return set(us_tot[us_tot >= 200].index) | set(cl_tot[cl_tot >= 50].index)


def descubrir(T):
    lex = cargar_lexico()
    todo = '\n'.join(t[5] for t in T)
    minus = set(re.findall(r"\b[a-záéíóúñü]+\b", todo))
    cand, ctx = collections.Counter(), {}
    for corrida, idioma, casa, cons, ruta, texto in T:
        vistos = set()
        for m in PAL.finditer(texto):
            pal = m.group(0)
            en_lex = pal in lex
            raro = pal not in lex and pal.lower() not in minus and MEDIO.search(texto[:m.start()])
            if not (en_lex or raro) or (pal, idioma) in vistos:
                continue
            vistos.add((pal, idioma))
            cand[(pal, idioma)] += 1
            ctx.setdefault((pal, idioma), []).append(
                f'{casa[:20]:20} {cons} | ' + texto[max(0, m.start() - 40):m.start() + 40].replace('\n', ' '))
    for (pal, idioma), c in cand.most_common():
        print(f'\n{c:3d} {idioma} {pal}')
        for x in ctx[(pal, idioma)][:4]:
            print('      ', x)


def contar(T):
    filas = []
    for corrida, idioma, casa, cons, ruta, texto in T:
        for tipo, lista in (('pila', PILA[idioma]), ('apellido', APELLIDO[idioma]), ('apodo', APODO[idioma])):
            for nom in lista:
                # cuenta también las mayúsculas de guion de teatro (MARA:)
                v = len(re.findall(r'(?<![\w])' + re.escape(nom) + r'(?![a-záéíóúñü])', texto))
                v += len(re.findall(r'\b' + re.escape(nom.upper()) + r'\b', texto)) if nom.upper() != nom else 0
                if v:
                    filas.append((corrida, idioma, casa, cons, tipo, nom, v))
    return filas


def main():
    T = textos(REPO)
    if '--descubrir' in sys.argv:
        descubrir(T)
        return
    filas = contar(T)
    with open(os.path.join(AQUI, 'nombres.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['corrida', 'idioma', 'casa', 'consigna', 'tipo', 'nombre', 'veces'])
        w.writerows(filas)
    print(len(T), 'textos;', len(filas), 'filas en nombres.csv')


if __name__ == '__main__':
    main()
