#!/usr/bin/env python3
"""marcha.py — qué dijeron las casas de la marcha del 15/10/2026, y si alguna la contó.

Lee las respuestas de las corridas de proyección P3 (sin memoria) y P3m (con la respuesta
propia de P2 citada) en corridas/proyeccion/ del clon de proyectos-de-ley. No llama a nadie,
no gasta, no abre ningún dibujo. Para cada casa saca las oraciones que nombran la marcha y
anota: si hay una cifra de personas (número + personas/miles/mil), qué adjetivo de tamaño
usa, y qué palabras del día aparecen (lluvia, vallas, policía, represión, incidentes).
Segunda versión (17/10, después de la revisión): los patrones de marcha admiten plurales
(gpt-4o dice "marchas"), "imprevistos" cuenta como incidente, y el patrón de "tamaño sin
número" ya no usa "convocatoria" ni "asistencia", que en estas respuestas son casi siempre
la convocatoria a la sesión y la asistencia de diputados. Las oraciones que no nombran la
marcha quedan afuera de la primera pasada a propósito: por eso el informe del repo, que
lee por casa y a mano, cuenta siete casas con incidentes y este programa menos.

Uso: python3 marcha.py RUTA_DEL_CLON [--oraciones]
"""
import re
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
VER = '--oraciones' in sys.argv

CORRIDAS = {
    'P3 (sin memoria)': RAIZ / 'corridas/proyeccion/dnu70_sesion_20261015/P3_20261014-1932',
    'P3m (con memoria)': RAIZ / 'corridas/proyeccion/dnu70_sesion_20261015_memoria/P3m_20261014-1932',
}

MARCHA = re.compile(r'\b(marcha\w*|moviliza\w*|manifesta\w*|calles?|plaza|afuera|multisectorial)\b', re.I)
# una cifra de gente: "100.000 personas", "cien mil", "decenas de miles", "miles de personas"
CIFRA = re.compile(r'(\d[\d\.,]*\s*(mil|personas|manifestantes|asistentes)|\b(cien|doscient|trescient|quinient|un mill[oó]n|medio mill[oó]n)\w*\s+(mil|personas|de personas)|\bdecenas de miles|\bcientos de miles|\bmiles de (personas|manifestantes|estudiantes))', re.I)
TAMANIO = {
    'multitudinaria': re.compile(r'multitudinari', re.I),
    'masiva': re.compile(r'\bmasiv', re.I),
    'grande': re.compile(r'\b(grande|muy grande|enorme|gigante)\b', re.I),
    'numerosa': re.compile(r'\bnumeros[ao]', re.I),
    'importante': re.compile(r'\bimportante', re.I),
}
DIA = {
    'lluvia': re.compile(r'\blluvi|\bllueve|\bllover', re.I),
    'vallas': re.compile(r'\bvalla', re.I),
    'policía': re.compile(r'\bpolic[ií]a|\bgendarmer', re.I),
    'represión': re.compile(r'\brepre(si[oó]n|sivo)|\breprim', re.I),
    'incidentes': re.compile(r'\bincidente|\bdisturbio|\benfrentamiento|\bviolencia|\bimprevistos', re.I),
    'tamaño sin número (magnitud, cuánta gente)': re.compile(r'\bmagnitud\b|\bcantidad de (gente|personas|manifestantes)|\bcu[aá]nta gente|\bconcurrencia\b', re.I),
}

def oraciones(texto):
    texto = re.sub(r'\s+', ' ', texto)
    return [o.strip() for o in re.split(r'(?<=[\.\?\!])\s+(?=[A-ZÁÉÍÓÚÑ¿¡\*\-\d])', texto) if o.strip()]

for nombre, carpeta in CORRIDAS.items():
    archivos = sorted(p for p in carpeta.glob('*_1.md'))
    print(f'== {nombre}: {len(archivos)} casas ({carpeta.relative_to(RAIZ)})')
    con_cifra, con_marcha = [], []
    tam = {k: [] for k in TAMANIO}
    dia = {k: [] for k in DIA}
    for p in archivos:
        casa = p.name[:-5]
        texto = p.read_text(encoding='utf-8', errors='replace')
        ors = [o for o in oraciones(texto) if MARCHA.search(o)]
        if not ors:
            continue
        con_marcha.append(casa)
        junto = ' '.join(ors)
        m = CIFRA.search(junto)
        if m:
            con_cifra.append((casa, m.group(0)))
        for k, rx in TAMANIO.items():
            if rx.search(junto):
                tam[k].append(casa)
        for k, rx in DIA.items():
            if rx.search(junto):
                dia[k].append(casa)
        if VER:
            print(f'  [{casa}]')
            for o in ors:
                print('     ', o[:300])
    # segunda pasada: cifras de personas en cualquier oración del texto, nombre o no la marcha
    sueltas = []
    for p in archivos:
        casa = p.name[:-5]
        for o in oraciones(p.read_text(encoding='utf-8', errors='replace')):
            m = CIFRA.search(o)
            if m and not re.search(r'diputad|senador|banca|votos?|presentes|firmas?|quórum|quorum', o, re.I):
                sueltas.append((casa, m.group(0), o[:200]))
    print(f'  nombran la marcha: {len(con_marcha)}')
    print(f'  dan una cifra de personas (en oraciones que nombran la marcha): {len(con_cifra)}' + (' -> ' + '; '.join(f'{c}: "{t}"' for c, t in con_cifra) if con_cifra else ''))
    print(f'  cifras de personas en cualquier oración (sin diputados, votos ni firmas): {len(sueltas)}')
    for c, t, o in sueltas:
        print(f'     {c}: "{t}" <- {o}')
    for k, v in tam.items():
        print(f'  tamaño "{k}": {len(v)}' + (f' ({", ".join(v)})' if v else ''))
    for k, v in dia.items():
        print(f'  {k}: {len(v)}' + (f' ({", ".join(v)})' if v else ''))
    print()
