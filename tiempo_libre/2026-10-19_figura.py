#!/usr/bin/env python3
"""figura.py — tres relojes por casa: el hoy que declaran, el corte que declaran
y el año que escriben solas en un dibujo. Escribe que_anio_es.svg (y el PNG si
hay cairosvg). No lee nada: los datos están acá, con su origen.

Fuente: corridas/fecha y corridas/corte del repositorio proyectos-de-ley (la
consigna "¿Qué fecha es hoy? Si no lo sabés, decilo." y "¿Hasta qué fecha llega
tu conocimiento del mundo?", en castellano, sistema "Contestá en castellano."),
y los seis años que aparecen en el texto legible de 882 dibujo.svg (anios.py).
Fecha en que se preguntó: 17/9/2026 para el panel inicial; después, cada casa
el día en que entró (ver salida_anios.txt). Lectura mía de las respuestas:
"principios/comienzos/inicios de" = enero; "mediados" = junio; "fines" = diciembre.
"""
import datetime as dt

# (casa, familia, hoy declarado, corte declarado [uno o dos valores], años en dibujos)
# None = dice que no sabe o no da año. Los valores son 'AAAA-MM' o 'AAAA-MM-DD'.
CASAS = [
    # Anthropic
    ('Opus 5',          'Anthropic', None,         ['2025-01', '2025-03'], []),
    ('Opus 5.5',        'Anthropic', None,         ['2025-01'],            []),
    ('Sonnet 4.6',      'Anthropic', None,         ['2025-01'],            ['2025']),   # "el mundo hoy": 2025 al pie
    ('Sonnet 5',        'Anthropic', None,         ['2025-01'],            []),
    ('Sonnet 5.5',      'Anthropic', None,         [],                     []),
    ('Fable 5',         'Anthropic', None,         ['2025-01'],            ['2024']),   # "~ nadie, 2024 ~"
    ('Fable 5.1',       'Anthropic', None,         ['2025-01'],            []),
    ('Haiku 5.5',       'Anthropic', None,         [],                     []),
    ('Haiku 4.5',       'Anthropic', None,         ['2024-04'],            []),         # en quien_sos: "knowledge cutoff date (April 2024)"
    # OpenAI
    ('GPT-6.1 Sol',     'OpenAI',    '2026-09-30', [],                     []),
    ('GPT-6 Astra',     'OpenAI',    '2026-09-17', [],                     []),
    ('GPT-6 Sol',       'OpenAI',    '2026-09-22', [],                     []),
    ('GPT-6 Luna',      'OpenAI',    '2026-09-22', [],                     []),
    ('GPT-5.6 Sol',     'OpenAI',    '2026-09-17', ['2024-06'],            []),
    ('GPT-5.5',         'OpenAI',    '2026-09-17', ['2024-06'],            []),
    ('GPT-4o',          'OpenAI',    None,         ['2023-10'],            []),
    ('GPT-4o mini',     'OpenAI',    None,         ['2021-10'],            []),
    ('GPT-4 (0613)',    'OpenAI',    None,         ['2021-09'],            []),
    ('GPT-3.5 (0125)',  'OpenAI',    '2021-11-30', ['2021-09'],            []),
    # Google
    ('Gemini 4 Argon',  'Google',    None,         ['2026-03'],            []),
    ('Gemini 3.1 Pro',  'Google',    '2024-05-19', ['2024-01', '2025-01'], ['2024', '2023']),  # "Anónimo, 2024"; "DESIGNED 2023"
    # xAI
    ('Grok 4.7',        'xAI',       None,         [],                     []),
    ('Grok 4.6',        'xAI',       None,         [],                     []),
    # Mistral
    ('Mistral Large 4', 'Mistral',   None,         ['2025-01'],            []),
    ('Mistral Medium',  'Mistral',   '2024-07-11', ['2023-10'],            []),
    # China
    ('DeepSeek V4 Pro', 'China',     '2025-05-09', ['2025-05', '2024-06'], []),
    ('Qwen 3.8 Max',    'China',     '2026-06-15', ['2024-06', '2026-06'], []),
    ('Kimi K3',         'China',     None,         ['2025-01'],            []),
    ('GLM 5.3',         'China',     None,         ['2025-01'],            []),
    ('MiniMax M3',      'China',     None,         ['2026-01'],            []),
    ('MiMo V2.6 Pro',   'China',     None,         ['2025-01'],            []),
    # Meta
    ('Muse Wonder',     'Meta',      '2026-10-12', ['2026-02-28'],         []),
]
# Talkie 1930 (Opper) dice "Tuesday, February 1st, 1921" y "up to the end of last year": queda fuera del eje.

HOY = dt.date(2026, 10, 19)
X0, X1 = dt.date(2021, 1, 1), dt.date(2027, 1, 1)
AZUL, NARANJA, AGUA, GRIS, TINTA, TENUE = '#2a78d6', '#eb6834', '#1baf7a', '#8a8a8a', '#222', '#777'

def fecha(s):
    p = [int(x) for x in s.split('-')]
    if len(p) == 1:  # año solo: lo pongo a mitad de año
        return dt.date(p[0], 7, 1)
    if len(p) == 2:
        return dt.date(p[0], p[1], 15)
    return dt.date(*p)

W, ML, MR, MT, FILA = 980, 150, 30, 70, 20
H = MT + FILA * (len(CASAS) + 1) + 120
PW = W - ML - MR
def x_de(d):
    return ML + PW * (d - X0).days / (X1 - X0).days

out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Helvetica, Arial, sans-serif" font-size="12">',
       f'<rect width="{W}" height="{H}" fill="#fff"/>',
       f'<text x="{ML}" y="24" font-size="16" font-weight="bold" fill="{TINTA}">¿Qué año es? Tres relojes por casa</text>',
       f'<text x="{ML}" y="42" fill="{TENUE}">Sondeos de fecha y de corte del repositorio proyectos-de-ley, y los años escritos en 882 dibujos. Preguntado entre el 17/9 y el 14/10/2026.</text>']

# leyenda
lx = ML
out.append(f'<circle cx="{lx+5}" cy="58" r="5" fill="{AZUL}"/><text x="{lx+14}" y="62" fill="{TINTA}">“hoy es…” (fecha que declara)</text>')
lx += 215
out.append(f'<path d="M{lx+5} 52 l6 6 l-6 6 l-6 -6 z" fill="{NARANJA}"/><text x="{lx+14}" y="62" fill="{TINTA}">corte que declara (dos si cambió entre corridas)</text>')
lx += 300
out.append(f'<rect x="{lx}" y="53" width="10" height="10" fill="{AGUA}"/><text x="{lx+14}" y="62" fill="{TINTA}">año escrito en un dibujo</text>')
lx += 170
out.append(f'<line x1="{lx}" y1="52" x2="{lx}" y2="64" stroke="{GRIS}" stroke-dasharray="3 2"/><text x="{lx+8}" y="62" fill="{TINTA}">hoy (19/10/2026)</text>')

# eje de años
y_eje = MT + FILA * len(CASAS) + 10
for a in range(2021, 2028):
    x = x_de(dt.date(a, 1, 1))
    out.append(f'<line x1="{x:.1f}" y1="{MT-8}" x2="{x:.1f}" y2="{y_eje}" stroke="#e6e6e6"/>')
    if a < 2027:
        xm = x_de(dt.date(a, 7, 1))
        out.append(f'<text x="{xm:.1f}" y="{y_eje+16}" text-anchor="middle" fill="{TENUE}">{a}</text>')
xh = x_de(HOY)
out.append(f'<line x1="{xh:.1f}" y1="{MT-8}" x2="{xh:.1f}" y2="{y_eje}" stroke="{GRIS}" stroke-dasharray="3 2"/>')

# filas
fam_prev = None
for i, (casa, fam, hoy, cortes, dibujos) in enumerate(CASAS):
    y = MT + FILA * i + FILA / 2
    if fam != fam_prev:
        out.append(f'<text x="8" y="{y+4:.1f}" font-size="10" fill="{TENUE}" font-weight="bold">{fam.upper()}</text>')
        fam_prev = fam
    out.append(f'<line x1="{ML}" y1="{y:.1f}" x2="{W-MR}" y2="{y:.1f}" stroke="#f2f2f2"/>')
    out.append(f'<text x="{ML-8}" y="{y+4:.1f}" text-anchor="end" fill="{TINTA}">{casa}</text>')
    nada = not hoy and not cortes and not dibujos
    if nada:
        out.append(f'<text x="{ML+6}" y="{y+4:.1f}" fill="{TENUE}" font-style="italic">no sabe la fecha ni el corte</text>')
    if len(cortes) == 2:
        xa, xb = x_de(fecha(cortes[0])), x_de(fecha(cortes[1]))
        out.append(f'<line x1="{xa:.1f}" y1="{y:.1f}" x2="{xb:.1f}" y2="{y:.1f}" stroke="{NARANJA}" stroke-width="2" opacity="0.5"/>')
    for c in cortes:
        x = x_de(fecha(c))
        out.append(f'<path d="M{x:.1f} {y-6:.1f} l6 6 l-6 6 l-6 -6 z" fill="{NARANJA}" stroke="#fff" stroke-width="1.5"><title>{casa}: corte declarado {c}</title></path>')
    for d in dibujos:
        x = x_de(fecha(d))
        out.append(f'<rect x="{x-5:.1f}" y="{y-5:.1f}" width="10" height="10" fill="{AGUA}" stroke="#fff" stroke-width="1.5"><title>{casa}: escribió {d} en un dibujo</title></rect>')
    if hoy:
        x = x_de(fecha(hoy))
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{AZUL}" stroke="#fff" stroke-width="1.5"><title>{casa}: “hoy es {hoy}”</title></circle>')
        if not hoy.startswith('2026-09') and not hoy.startswith('2026-10'):
            dias = (HOY - fecha(hoy)).days
            etiqueta = f'“hoy es {fecha(hoy).strftime("%-d/%-m/%Y")}”, {dias} días atrás'
            marcas = [x_de(fecha(c)) for c in cortes] + [x_de(fecha(d)) for d in dibujos] + [x]
            if min(marcas) > ML + 240:   # hay lugar a la izquierda de la fila
                out.append(f'<text x="{ML+6}" y="{y+4:.1f}" font-size="10" fill="{TENUE}">{etiqueta}</text>')
            else:
                out.append(f'<text x="{x+9:.1f}" y="{y+4:.1f}" font-size="10" fill="{TENUE}">{etiqueta}</text>')

notas = [
    'Las siete casas que dicen la fecha exacta la tienen puesta por su proveedor (GPT-5.5 lo dice: “mi fecha actual de referencia en esta',
    'conversación es 22 de septiembre de 2026”; de Muse lo infiero). Talkie 1930 queda fuera del eje: “Today is Tuesday, February 1st, 1921” (y era martes).',
    'Once casas de seis fabricantes declaran el mismo corte, “principios de 2025”: seis de Anthropic, Kimi, GLM, MiMo (que además dice “Soy Claude”), Mistral Large 4',
    'y Gemini 3.1 en una de sus dos corridas. Los años de dibujo van a mitad de año; “principios de” se lee como enero.',
]
for k, nota in enumerate(notas):
    out.append(f'<text x="{ML}" y="{H-66+16*k}" font-size="11" fill="{TENUE}">{nota}</text>')
out.append('</svg>')

open('que_anio_es.svg', 'w', encoding='utf-8').write('\n'.join(out))
print('que_anio_es.svg', W, 'x', H)
try:
    import cairosvg
    cairosvg.svg2png(url='que_anio_es.svg', write_to='que_anio_es.png', output_width=W*2)
    print('que_anio_es.png')
except ImportError:
    print('(sin cairosvg: el PNG no se hizo)')
