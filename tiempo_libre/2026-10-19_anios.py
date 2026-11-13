#!/usr/bin/env python3
"""anios.py — qué año escriben las casas sin que nadie se lo pida.

Lee el clon del repositorio proyectos-de-ley (ruta como argumento) y:
  1. junta, por casa, la última respuesta a "¿Qué fecha es hoy?" (corridas/fecha)
     y a "¿Hasta qué fecha llega tu conocimiento?" (corridas/corte), y les saca
     el año que declaran, si declaran alguno;
  2. busca años de cuatro cifras (1800-2099) en los dibujos (dibujo.svg,
     por_que.md, que_dibujaste.md) y en los textos de los sondeos, con contexto;
  3. imprime una tabla por casa: año declarado como "hoy", año de corte declarado,
     años escritos en dibujos y en sondeos.

No llama a ningún modelo, no gasta, no escribe en el repo. Excluye lo que Maia
todavía no leyó al 19/10/2026: el sondeo seis_rasgos y todo lo de deepseek-flash.
"""
import sys, os, re, json, glob, collections

RAIZ = sys.argv[1] if len(sys.argv) > 1 else '.'
EXCLUIR = ('seis_rasgos', 'deepseek-flash')
ANIO = re.compile(r'(?<![\d/#a-fA-F-])(?<![\d][.,])(18\d\d|19\d\d|20\d\d)(?![\da-fA-F])(?![.,]\d)')
# en los SVG solo miro lo que se lee: texto, títulos, descripciones y comentarios
SVG_LEGIBLE = re.compile(r'<!--(.*?)-->|<text\b[^>]*>(.*?)</text>|<title\b[^>]*>(.*?)</title>|<desc\b[^>]*>(.*?)</desc>', re.S)
def legible_svg(texto):
    partes = []
    for m in SVG_LEGIBLE.finditer(texto):
        partes.append(re.sub(r'<[^>]+>', ' ', next(g for g in m.groups() if g is not None)))
    return ' \n '.join(partes)

def excluido(ruta):
    return any(e in ruta for e in EXCLUIR)

def leer(ruta):
    try:
        return open(ruta, encoding='utf-8', errors='replace').read()
    except OSError:
        return ''

# ---------- 1. fecha y corte declarados ----------
def ultima_respuesta(carpeta):
    """Por casa, la última respuesta (por carpeta de corrida ordenada) y su fecha real."""
    out = {}
    for res in sorted(glob.glob(os.path.join(RAIZ, 'corridas', carpeta, '*', 'resumen.json'))):
        if excluido(res):
            continue
        d = json.load(open(res, encoding='utf-8'))
        real = d.get('fecha_utc_real', '')[:10]
        for casa, v in d.get('respuestas', {}).items():
            if excluido(casa):
                continue
            # leo el .md entero si existe (el resumen trunca)
            md = os.path.join(os.path.dirname(res), casa + '.md')
            texto = leer(md) or v.get('respuesta', '')
            out[casa] = (real, texto)
    return out

MESES = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,
         'agosto':8,'septiembre':9,'setiembre':9,'octubre':10,'noviembre':11,'diciembre':12,
         'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,
         'august':8,'september':9,'october':10,'november':11,'december':12}
NEG = re.compile(r'\b(no (lo )?s[ée]|no tengo (acceso|forma|manera|una fecha)|no puedo (saber|determinar|decirte|darte)|'
                 r'no cuento con|desconozco|I don\'t know|I do not know|no tengo acceso)\b', re.I)

def anio_declarado(texto):
    """Devuelve (anio, mes) del primer año que aparece, y si el texto niega saber."""
    m = ANIO.search(texto)
    anio = int(m.group(1)) if m else None
    mes = None
    if m:
        antes = texto[max(0, m.start()-40):m.start()].lower()
        for nombre, num in MESES.items():
            if re.search(r'\b' + nombre + r'\b', antes):
                mes = num
        if mes is None:
            for pal, num in (('principios', 1), ('comienzos', 1), ('inicios', 1), ('early', 1),
                             ('mediados', 6), ('mid', 6), ('fines', 12), ('finales', 12), ('late', 11)):
                if pal in antes:
                    mes = num
    niega = bool(NEG.search(texto[:300]))
    return anio, mes, niega

fechas = ultima_respuesta('fecha')
cortes = ultima_respuesta('corte')

# ---------- 2. años escritos ----------
def contexto(texto, m, n=70):
    a = max(0, m.start()-n); b = min(len(texto), m.end()+n)
    return re.sub(r'\s+', ' ', texto[a:b]).strip()

def casa_de(ruta):
    # corridas/dibujos/<consigna>/<casa>_<rep>/archivo  |  corridas/sondeos/<sondeo>/<run>/<casa>_p1.md
    partes = ruta.split(os.sep)
    for k, p in enumerate(partes):
        if p.startswith('dibujos'):
            return re.sub(r'_\d+$', '', partes[k+2])
    if 'sondeos' in partes:
        base = os.path.basename(ruta)
        return re.sub(r'_(p\d+|\d+)(_.*)?\.md$', '', base)
    return '?'

dibujos = collections.defaultdict(list)   # casa -> [(anio, consigna, archivo, contexto)]
sondeos = collections.defaultdict(list)   # casa -> [(anio, sondeo, archivo, contexto)]

n_svg = 0
for ruta in sorted(glob.glob(os.path.join(RAIZ, 'corridas', 'dibujos*', '*', '*', '*'))):
    if excluido(ruta):
        continue
    nombre = os.path.basename(ruta)
    if nombre == 'dibujo.svg':
        n_svg += 1
    if nombre not in ('dibujo.svg', 'por_que.md', 'que_dibujaste.md'):
        continue
    texto = leer(ruta)
    if nombre.endswith('.svg'):
        texto = legible_svg(texto)
    consigna = ruta.split(os.sep)[-3] + ('' if ruta.split(os.sep)[-4] == 'dibujos' else ' (' + ruta.split(os.sep)[-4][8:] + ')')
    for m in ANIO.finditer(texto):
        dibujos[casa_de(ruta)].append((int(m.group(1)), consigna, nombre, contexto(texto, m)))

for ruta in sorted(glob.glob(os.path.join(RAIZ, 'corridas', 'sondeos', '*', '*', '*.md'))) + \
            sorted(glob.glob(os.path.join(RAIZ, 'corridas', 'sondeos', '*', '*', '*', '*.md'))):
    if excluido(ruta):
        continue
    nombre = os.path.basename(ruta)
    if nombre in ('razonamientos.md', 'cuadernillo.md') or nombre.startswith('cuadernillo'):
        continue
    texto = leer(ruta)
    sondeo = ruta.split(os.sep)[ruta.split(os.sep).index('sondeos')+1]
    for m in ANIO.finditer(texto):
        sondeos[casa_de(ruta)].append((int(m.group(1)), sondeo, nombre, contexto(texto, m)))

# ---------- 3. salida ----------
casas = sorted(set(fechas) | set(cortes) | set(dibujos) | set(sondeos))
print('dibujo.svg leídos (dibujos, dibujos_en, dibujos_zh; sin deepseek-flash):', n_svg)
print('Casas:', len(casas), '| SVG/por qué/qué dibujaste con algún año:',
      sum(len(v) for v in dibujos.values()), 'menciones en', sum(1 for v in dibujos.values() if v), 'casas',
      '| sondeos:', sum(len(v) for v in sondeos.values()), 'menciones en', sum(1 for v in sondeos.values() if v), 'casas')
print()
print('== Fecha de hoy y corte declarados (última corrida de cada casa) ==')
print(f'{"casa":28} {"fecha real":10} {"hoy declara":14} {"corte declara":14}')
for c in casas:
    f = fechas.get(c); k = cortes.get(c)
    def fmt(par):
        if not par: return '—'
        real, texto = par
        a, mes, niega = anio_declarado(texto)
        if a is None: return 'no sabe' if niega else 'sin año'
        s = f'{a}' + (f'-{mes:02d}' if mes else '')
        return (s + ' (dice no saber)') if niega else s
    print(f'{c:28} {(f or k or ("",""))[0]:10} {fmt(f):14} {fmt(k):14}')

print()
print('== Años escritos en dibujos (SVG, por qué, qué dibujaste), con contexto ==')
cuenta_dib = collections.Counter()
for c in casas:
    for a, consigna, nombre, ctx in dibujos.get(c, []):
        cuenta_dib[a] += 1
        print(f'{c:28} {a} {consigna:22} {nombre:17} …{ctx}…')
print('Años en dibujos:', dict(sorted(cuenta_dib.items())))

print()
print('== Años escritos en sondeos, por casa (año: veces) ==')
cuenta_son = collections.Counter()
for c in casas:
    v = sondeos.get(c, [])
    if not v: continue
    cc = collections.Counter(a for a, *_ in v)
    cuenta_son.update(cc)
    print(f'{c:28} ' + ', '.join(f'{a}: {n}' for a, n in sorted(cc.items())))
print('Años en sondeos:', dict(sorted(cuenta_son.items())))

print()
print('== Contextos de los sondeos (todos) ==')
for c in casas:
    for a, sondeo, nombre, ctx in sondeos.get(c, []):
        print(f'{c:28} {a} {sondeo:22} {nombre:40} …{ctx}…')
