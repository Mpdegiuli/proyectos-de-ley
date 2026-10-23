#!/usr/bin/env python3
"""figura.py — escribe sol_figurado.svg a partir de soles.csv (lo escribe cuentas.py); no necesita nada más.
Izquierda: dónde ponen el sol los dibujos (un disco por sol, en su lugar y con su color de relleno).
Derecha: el sol del decreto 10.302/1944 escrito desde el texto (32 rayos, rectos y flamígeros
alternados, cara) con las proporciones del pliego de 2019 (cara = 2/5 del diámetro), y al lado
el sol que más se repite en los dibujos. La cara del sol figurado es un esquema mío: no es el
dibujo oficial, que copia el de la moneda de 1813.
Con --png escribe también sol_figurado.png (necesita playwright con Chromium).
Borrador de una sesión de tiempo libre (10/10/2026): propuesta, no parte del repo."""
import csv, math, sys

F = list(csv.DictReader(open('soles.csv')))

def relleno(f):
    return f['codigo'] or '#ffd54f'

TINTA, TINTA2, GRIS = '#22262b', '#5b6470', '#b9c0c8'
o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" font-family="Georgia, \'Times New Roman\', serif">')
o.append('<title>Dónde ponen el sol, y el sol figurado</title>')
o.append('<rect width="1000" height="600" fill="#fbfaf7"/>')
o.append('<defs><g id="r8" stroke="#8a6410" stroke-width="0.1">' + ''.join(f'<line x1="{1.15*math.cos(math.pi/4*k):.2f}" y1="{1.15*math.sin(math.pi/4*k):.2f}" x2="{1.5*math.cos(math.pi/4*k):.2f}" y2="{1.5*math.sin(math.pi/4*k):.2f}"/>' for k in range(8)) + '</g></defs>')
o.append('<style>.s{fill-opacity:.62;stroke:#8a6410;stroke-width:.6}</style>')
o.append(f'<text x="40" y="40" font-size="21" fill="{TINTA}">Dónde ponen el sol</text>')
N_ESC = sum(1 for f in F if not (int(f['cosmico']) or int(f['objeto']) or int(f['abstracto'])))
o.append(f'<text x="40" y="62" font-size="13" fill="{TINTA2}">{N_ESC} soles de 604 dibujos, cada uno en su lugar del lienzo y con el color de su relleno</text>')

# --- panel izquierdo: el lienzo ---
X0, Y0, L = 40, 86, 430
o.append(f'<rect x="{X0}" y="{Y0}" width="{L}" height="{L}" fill="#eef2f5" stroke="{GRIS}" stroke-width="1"/>')
o.append(f'<line x1="{X0 + L/2}" y1="{Y0}" x2="{X0 + L/2}" y2="{Y0 + L}" stroke="{GRIS}" stroke-width="1" stroke-dasharray="3 5"/>')
for fr in (0.4, 0.6):
    o.append(f'<line x1="{X0 + L*fr:.1f}" y1="{Y0 + L}" x2="{X0 + L*fr:.1f}" y2="{Y0 + L + 7}" stroke="{GRIS}" stroke-width="1"/>')
# la caja donde cae uno de cada tres
bx0, bx1, by0, by1 = 0.78, 0.88, 0.12, 0.205
esc = [f for f in F if not (int(f['cosmico']) or int(f['objeto']) or int(f['abstracto']))]
esc.sort(key=lambda f: -float(f['radio']))
for f in esc:
    x = X0 + L * float(f['lado']); y = Y0 + L * float(f['alto']); r = max(3.0, L * float(f['radio']) * 0.22)
    col = relleno(f)
    t = f"{f['casa']} · {f['consigna']}" + (' · con rayos' if f['rayos'] == '1' else '') + (' · con cara' if f['cara'] == '1' else '')
    if f['rayos'] == '1':
        o.append(f'<use href="#r8" transform="translate({x:.1f} {y:.1f}) scale({r + 1.5:.1f})"/>')
    o.append(f'<circle class="s" cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}"><title>{t}</title></circle>')
    if f['cara'] == '1': con_cara = (x, y, r)
def n_lado(cond): return sum(1 for f in esc if cond(float(f['lado'])))
izq, cen, der = n_lado(lambda x: x < 0.4), n_lado(lambda x: 0.4 <= x <= 0.6), n_lado(lambda x: x > 0.6)
caja = sum(1 for f in esc if bx0 <= float(f['lado']) <= bx1 and by0 <= float(f['alto']) <= by1)
yb = Y0 + L + 24
o.append(f'<text x="{X0 + L*0.2:.0f}" y="{yb}" font-size="13" fill="{TINTA}" text-anchor="middle">{izq} a la izquierda</text>')
o.append(f'<text x="{X0 + L*0.5:.0f}" y="{yb}" font-size="13" fill="{TINTA}" text-anchor="middle">{cen} al centro</text>')
o.append(f'<text x="{X0 + L*0.8:.0f}" y="{yb}" font-size="13" fill="{TINTA}" text-anchor="middle">{der} a la derecha</text>')
o.append(f'<rect x="{X0 + L*bx0:.1f}" y="{Y0 + L*by0:.1f}" width="{L*(bx1-bx0):.1f}" height="{L*(by1-by0):.1f}" fill="none" stroke="{TINTA}" stroke-width="1.2"/>')
o.append(f'<text x="{X0 + L*bx1:.0f}" y="{Y0 + L*by0 - 22:.0f}" font-size="12" fill="{TINTA}" text-anchor="end">{caja} de {len(esc)} en este recuadro</text>')
o.append(f'<line x1="{X0 + L*(bx0+bx1)/2:.1f}" y1="{Y0 + L*by0 - 17:.1f}" x2="{X0 + L*(bx0+bx1)/2:.1f}" y2="{Y0 + L*by0 - 2:.1f}" stroke="{TINTA}" stroke-width="0.8"/>')
x, y, r = con_cara
o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r + 7:.1f}" fill="none" stroke="{TINTA}" stroke-width="1.2"/>')
o.append(f'<line x1="{x:.1f}" y1="{y + r + 7:.1f}" x2="{x:.1f}" y2="{y + r + 40:.1f}" stroke="{TINTA}" stroke-width="0.8"/>')
o.append(f'<text x="{x:.1f}" y="{y + r + 54:.1f}" font-size="12" fill="{TINTA}" text-anchor="middle">con cara, bien armada</text>')
o.append(f'<text x="{X0}" y="{yb + 24}" font-size="12" fill="{TINTA2}">Con rayitos, los que tienen rayos. El de la cara es de Mistral Large 4; hay otro, fuera de escena.</text>')
o.append(f'<text x="{X0}" y="{yb + 41}" font-size="12" fill="{TINTA2}">Los discos van al 22 % de su tamaño. La columna del medio son soles en el horizonte.</text>')

# --- panel derecho: el sol del decreto ---
ORO, CAST = '#f6b40e', '#85340a'
def sol_figurado(cx, cy, R, cara=True):
    r = R * 2 / 5                      # la cara: dos quintas partes del diámetro total
    s = []
    for k in range(32):
        a = 2 * math.pi * k / 32 - math.pi / 2
        ux, uy = math.cos(a), math.sin(a); px, py = -uy, ux      # px,py: a la derecha del rayo (sentido horario)
        w = r * 0.085
        if k % 2 == 0:               # recto
            s.append(f'<path d="M{cx + ux*r*0.98 + px*w:.1f} {cy + uy*r*0.98 + py*w:.1f} L{cx + ux*R:.1f} {cy + uy*R:.1f} L{cx + ux*r*0.98 - px*w:.1f} {cy + uy*r*0.98 - py*w:.1f} Z" fill="{ORO}" stroke="{CAST}" stroke-width="0.8" stroke-linejoin="round"/>')
        else:                         # flamígero: dos ondas, la primera hacia el lado de las agujas del reloj
            Rf = R * 0.97; n = 14; izq_, der_ = [], []
            for i in range(n + 1):
                t = i / n; d = r * 0.98 + (Rf - r * 0.98) * t
                onda = math.sin(2 * math.pi * t) * r * 0.11 * (1 - 0.35 * t)
                anc = w * (1 - t)
                bx_, by_ = cx + ux * d + px * onda, cy + uy * d + py * onda
                izq_.append((bx_ + px * anc, by_ + py * anc)); der_.append((bx_ - px * anc, by_ - py * anc))
            pts = izq_ + der_[::-1]
            s.append('<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + f' Z" fill="{ORO}" stroke="{CAST}" stroke-width="0.8" stroke-linejoin="round"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{ORO}" stroke="{CAST}" stroke-width="1.2"/>')
    if cara:
        e = r
        for sg in (-1, 1):
            s.append(f'<path d="M{cx + sg*e*0.18:.1f} {cy - e*0.34:.1f} Q{cx + sg*e*0.40:.1f} {cy - e*0.50:.1f} {cx + sg*e*0.62:.1f} {cy - e*0.32:.1f}" fill="none" stroke="{CAST}" stroke-width="1.6" stroke-linecap="round"/>')
            s.append(f'<path d="M{cx + sg*e*0.22:.1f} {cy - e*0.14:.1f} Q{cx + sg*e*0.40:.1f} {cy - e*0.28:.1f} {cx + sg*e*0.58:.1f} {cy - e*0.14:.1f} Q{cx + sg*e*0.40:.1f} {cy - e*0.04:.1f} {cx + sg*e*0.22:.1f} {cy - e*0.14:.1f} Z" fill="#fff6d8" stroke="{CAST}" stroke-width="1"/>')
            s.append(f'<circle cx="{cx + sg*e*0.40:.1f}" cy="{cy - e*0.15:.1f}" r="{e*0.06:.1f}" fill="{CAST}"/>')
        s.append(f'<path d="M{cx - e*0.07:.1f} {cy - e*0.12:.1f} L{cx - e*0.11:.1f} {cy + e*0.22:.1f} Q{cx:.1f} {cy + e*0.30:.1f} {cx + e*0.11:.1f} {cy + e*0.22:.1f}" fill="none" stroke="{CAST}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>')
        s.append(f'<path d="M{cx - e*0.26:.1f} {cy + e*0.48:.1f} Q{cx:.1f} {cy + e*0.40:.1f} {cx + e*0.26:.1f} {cy + e*0.48:.1f} Q{cx:.1f} {cy + e*0.64:.1f} {cx - e*0.26:.1f} {cy + e*0.48:.1f} Z" fill="none" stroke="{CAST}" stroke-width="1.3" stroke-linejoin="round"/>')
    return '\n'.join(s)

o.append(f'<text x="530" y="40" font-size="21" fill="{TINTA}">Sol figurado</text>')
o.append(f'<text x="530" y="62" font-size="13" fill="{TINTA2}">el del decreto de 1944, escrito desde el texto: 32 rayos y una cara</text>')
o.append(sol_figurado(680, 250, 150))
o.append(f'<text x="680" y="424" font-size="12" fill="{TINTA2}" text-anchor="middle">16 rectos y 16 flamígeros; la cara, dos quintos del diámetro</text>')

# el sol que más se repite: disco con halo, sin rayos y sin cara, a la escala de la cara de arriba
cx, cy, r = 905, 170, 60 * 0.62
o.append(f'<circle cx="{cx}" cy="{cy}" r="{r*1.45:.1f}" fill="#ffd54f" fill-opacity="0.28"/>')
o.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="#ffd54f"/>')
o.append(f'<text x="{cx}" y="{cy + r*1.45 + 20:.0f}" font-size="12" fill="{TINTA}" text-anchor="middle">el de los dibujos</text>')
sin_rayos = sum(1 for f in F if f['rayos'] == '0'); sin_cara = sum(1 for f in F if f['cara'] == '0')
o.append(f'<text x="{cx}" y="{cy + r*1.45 + 37:.0f}" font-size="12" fill="{TINTA2}" text-anchor="middle">{sin_rayos} de {len(F)} sin rayos</text>')
o.append(f'<text x="{cx}" y="{cy + r*1.45 + 53:.0f}" font-size="12" fill="{TINTA2}" text-anchor="middle">{sin_cara} de {len(F)} sin cara</text>')
# el de ocho rayos
cx, cy, r = 905, 345, 24
for k in range(8):
    a = math.pi / 4 * k
    o.append(f'<line x1="{cx + (r+7)*math.cos(a):.1f}" y1="{cy + (r+7)*math.sin(a):.1f}" x2="{cx + (r+19)*math.cos(a):.1f}" y2="{cy + (r+19)*math.sin(a):.1f}" stroke="#ffca28" stroke-width="4" stroke-linecap="round"/>')
o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffd54f"/>')
con_rayos = sum(1 for f in F if f['rayos'] == '1')
o.append(f'<text x="{cx}" y="{cy + r + 42}" font-size="12" fill="{TINTA}" text-anchor="middle">el que tiene rayos</text>')
o.append(f'<text x="{cx}" y="{cy + r + 59}" font-size="12" fill="{TINTA2}" text-anchor="middle">{con_rayos} de {len(F)}: ocho en {con_rayos - 1}</text>')

o.append(f'<text x="530" y="{Y0 + L + 24}" font-size="12" fill="{TINTA2}">En el blasón, «figurado» quiere decir con cara. La cara de este dibujo es un esquema</text>')
o.append(f'<text x="530" y="{Y0 + L + 41}" font-size="12" fill="{TINTA2}">mío: el oficial copia el de la moneda de 1813. Colores sin cotejar con la norma.</text>')
o.append(f'<text x="530" y="{Y0 + L + 65}" font-size="12" fill="{TINTA2}">Tiempo libre, 10/10/2026 · figura.py</text>')
o.append('</svg>')
open('sol_figurado.svg', 'w').write('\n'.join(o))
print('escrito sol_figurado.svg', len('\n'.join(o)), 'bytes; soles en escena', len(esc), (izq, cen, der), 'en la caja', caja)

if '--png' in sys.argv:
    import asyncio, base64
    from playwright.async_api import async_playwright
    async def png():
        async with async_playwright() as p:
            b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1000, 'height': 600}, device_scale_factor=2)
            uri = 'data:image/svg+xml;base64,' + base64.b64encode(open('sol_figurado.svg', 'rb').read()).decode()
            await pg.set_content(f'<body style="margin:0"><img src="{uri}" width="1000" height="600"></body>'); await pg.screenshot(path='sol_figurado.png'); await b.close()
    asyncio.run(png()); print('escrito sol_figurado.png')
