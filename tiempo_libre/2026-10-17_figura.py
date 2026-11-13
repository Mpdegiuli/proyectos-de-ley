#!/usr/bin/env python3
"""figura.py — escribe cuanta_gente.svg (y el PNG si está cairosvg). No lee nada.

Dos paneles sobre un mismo eje de personas, en escala logarítmica.
A. 17 de octubre de 1945: las cifras que circulan, sobre las bandas de lo que entra
   (2 a 4 personas por m²) en la Plaza de Mayo sola, en la plaza más la Avenida de
   Mayo, y en el eje entero hasta el Congreso. Superficies: ver plazas.py.
B. Las marchas universitarias de 2024-2026: la cuenta de La Nación con método, la
   cifra de los organizadores y la del Gobierno de la Ciudad; y la del 15/10/2026,
   que al 17/10 no tiene ninguna.
"""
import math
from pathlib import Path

W, H = 1000, 700
X0, X1 = 150, 940          # eje de personas
LOG0, LOG1 = math.log10(10_000), math.log10(2_000_000)
INK, INK2, GRIS, BANDA = '#0b0b0b', '#52514e', '#c3c2b7', '#e9e8e3'
AZUL, NARANJA, AGUA = '#2a78d6', '#eb6834', '#1baf7a'   # paleta validada (dataviz, slots 1-3)

def x(n):
    return X0 + (X1 - X0) * (math.log10(n) - LOG0) / (LOG1 - LOG0)

def fmt(n):
    return f'{n:,.0f}'.replace(',', '.')

out = []
def add(s):
    out.append(s)

add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">')
add('<title>Cuánta gente: las cifras de 1945 contra lo que entra, y las marchas de 2024-2026</title>')
add(f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>')
add(f'<style>text{{font-size:11px;fill:{INK2}}} .t{{font-size:13px;fill:{INK};font-weight:bold}} .n{{font-size:10.5px;fill:{INK}}} .m{{font-size:10px;fill:{INK2}}}</style>')

def eje(y, con_titulo):
    add(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="{GRIS}" stroke-width="1"/>')
    for n in (10_000, 20_000, 50_000, 100_000, 200_000, 500_000, 1_000_000, 2_000_000):
        add(f'<line x1="{x(n):.1f}" y1="{y}" x2="{x(n):.1f}" y2="{y+4}" stroke="{GRIS}"/>')
        add(f'<text x="{x(n):.1f}" y="{y+16}" text-anchor="middle">{fmt(n)}</text>')
    if con_titulo:
        add(f'<text x="{X1}" y="{y+30}" text-anchor="end" class="m">personas (escala logarítmica)</text>')

# ---------- Panel A: 1945 ----------
add(f'<text x="{X0}" y="28" class="t">A. 17 de octubre de 1945: lo que se dijo y lo que entra</text>')
add(f'<text x="{X0}" y="44" class="m">bandas: de 2 a 4 personas por m² (Jacobs, en metros); superficies en plazas.py</text>')

bandas = [
    ('Plaza de Mayo sola (23.665 m²)', 23665),
    ('Plaza + Avenida de Mayo (68.665 m²)', 23665 + 45000),
    ('Plaza + Avenida + las tres plazas del Congreso (98.665 m²)', 23665 + 45000 + 30000),
]
yb = 70
for nombre, m2 in bandas:
    a, b = x(2 * m2), x(4 * m2)
    add(f'<rect x="{a:.1f}" y="{yb}" width="{b-a:.1f}" height="14" rx="4" fill="{BANDA}"/>')
    add(f'<text x="{a-6:.1f}" y="{yb+11}" text-anchor="end" class="m">{nombre}</text>')
    add(f'<text x="{a+4:.1f}" y="{yb+11}" class="m">{fmt(2*m2)}</text>')
    add(f'<text x="{b-4:.1f}" y="{yb+11}" text-anchor="end" class="m">{fmt(4*m2)}</text>')
    yb += 22

# cifras: (etiqueta, desde, hasta)
cifras = [
    ('"unas 15.000" antes del mediodía (Perfil, 2025)', 15000, 15000),
    ('"cien o doscientas mil" (Grimson, 2022)', 100000, 200000),
    ('"tal vez 200.000 o 300.000" (Perfil, 2025)', 200000, 300000),
    ('"más de doscientas cincuenta mil" (Golzman, 2004)', 250000, 250000),
    ('300.000, la cifra que circula', 300000, 300000),
    ('"un millón" (La Época, 1945, según Perfil)', 1000000, 1000000),
]
yc = yb + 18
for et, a, b in cifras:
    xa, xb = x(a), x(b)
    if a != b:
        add(f'<line x1="{xa:.1f}" y1="{yc}" x2="{xb:.1f}" y2="{yc}" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
        add(f'<circle cx="{xa:.1f}" cy="{yc}" r="4" fill="{INK}"/><circle cx="{xb:.1f}" cy="{yc}" r="4" fill="{INK}"/>')
    else:
        add(f'<circle cx="{xa:.1f}" cy="{yc}" r="4.5" fill="{INK}"/>')
    # etiqueta: a la derecha si hay lugar, si no a la izquierda
    if xb < 700:
        add(f'<text x="{xb+9:.1f}" y="{yc+4}" class="n">{et}</text>')
    else:
        add(f'<text x="{xa-9:.1f}" y="{yc+4}" text-anchor="end" class="n">{et}</text>')
    yc += 22
eje(yc + 4, True)

# ---------- Panel B: 2024-2026 ----------
yB = yc + 70
add(f'<text x="{X0}" y="{yB}" class="t">B. Las marchas universitarias al Congreso y a la Plaza de Mayo, 2024-2026</text>')
add(f'<text x="{X0}" y="{yB+16}" class="m">Buenos Aires; la cuenta de La Nación es cuadra por cuadra, con 1, 2, 4 (y 5) personas por m²</text>')

filas = [
    ('23/4/2024', [('ln', 430000, 'LN 430.000'), ('org', 800000, 'organizadores 800.000'), ('ciudad', 150000, 'Ciudad 150.000')]),
    ('2/10/2024', [('ln', 270000, 'LN 270.000'), ('org', 1100000, 'organizadores 1.100.000')]),
    ('12/5/2026', [('ln', 120000, 'LN "unas 120.000"'), ('org', 600000, 'UBA "más de 600 mil"')]),
    ('15/10/2026', []),
]
yf = yB + 42
for fecha, marcas in filas:
    add(f'<text x="{X0-8}" y="{yf+4}" text-anchor="end" class="n">{fecha}</text>')
    add(f'<line x1="{X0}" y1="{yf}" x2="{X1}" y2="{yf}" stroke="{BANDA}" stroke-width="1"/>')
    if not marcas:
        add(f'<rect x="{X0+2}" y="{yf-7}" width="{X1-X0-4}" height="14" rx="7" fill="none" stroke="{INK2}" stroke-dasharray="4 4"/>')
        add(f'<text x="{(X0+X1)/2:.1f}" y="{yf+4}" text-anchor="middle" class="n">sin cifra pública al 17/10: "miles", "decenas de miles", "masiva", "multitudinaria"; el acto se adelantó por la lluvia y terminó a las 16.40</text>')
    for tipo, n, et in marcas:
        cx = x(n)
        if tipo == 'ln':
            add(f'<circle cx="{cx:.1f}" cy="{yf}" r="5" fill="{AZUL}" stroke="#fcfcfb" stroke-width="2"/>')
            add(f'<text x="{cx:.1f}" y="{yf-10}" text-anchor="middle" class="n">{et}</text>')
        elif tipo == 'org':
            add(f'<circle cx="{cx:.1f}" cy="{yf}" r="5" fill="#fcfcfb" stroke="{NARANJA}" stroke-width="2.5"/>')
            add(f'<text x="{cx:.1f}" y="{yf+18}" text-anchor="middle" class="n">{et}</text>')
        else:
            add(f'<rect x="{cx-5:.1f}" y="{yf-5}" width="10" height="10" rx="2" fill="{AGUA}" stroke="#fcfcfb" stroke-width="2"/>')
            add(f'<text x="{cx:.1f}" y="{yf+18}" text-anchor="middle" class="n">{et}</text>')
    yf += 44
eje(yf - 10, True)

# leyenda
yl = yf + 36
add(f'<circle cx="{X0+6}" cy="{yl}" r="5" fill="{AZUL}"/><text x="{X0+16}" y="{yl+4}" class="n">cuenta con método (La Nación)</text>')
add(f'<circle cx="{X0+206}" cy="{yl}" r="5" fill="#fcfcfb" stroke="{NARANJA}" stroke-width="2.5"/><text x="{X0+216}" y="{yl+4}" class="n">cifra de los organizadores</text>')
add(f'<rect x="{X0+376}" y="{yl-5}" width="10" height="10" rx="2" fill="{AGUA}"/><text x="{X0+391}" y="{yl+4}" class="n">cifra del Gobierno de la Ciudad</text>')
add(f'<circle cx="{X0+576}" cy="{yl}" r="4.5" fill="{INK}"/><text x="{X0+586}" y="{yl+4}" class="n">cifras de 1945 (ninguna con método declarado)</text>')
add(f'<text x="{X1}" y="{H-12}" text-anchor="end" class="m">tiempo libre, 17/10/2026 · fuentes en el cuaderno</text>')
add('</svg>')

svg = '\n'.join(out)
Path('cuanta_gente.svg').write_text(svg, encoding='utf-8')
print('cuanta_gente.svg', len(svg), 'bytes')
try:
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode(), write_to='cuanta_gente.png', output_width=2000)
    print('cuanta_gente.png')
except ImportError:
    print('sin cairosvg: el PNG se hace con Chromium o no se hace')
