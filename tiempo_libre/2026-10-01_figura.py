#!/usr/bin/env python3
"""figura.py — escribe 2026-10-01_tres_lunas.svg con los números medidos: la luna mediana de los dibujos
(dos círculos), el esquema de los cuernos, la Luna de Buenos Aires del 14/12/2026 a las 22 y la de hoy a las 6:48.
Borrador de una sesión de tiempo libre (1/10/2026)."""
import math
R = 58
def fase(k, rumbo, cx, cy, R, fill, extra=''):
    """fase de verdad: semicírculo del limbo + media elipse del terminador. rumbo: hacia dónde mira la luz,
    en grados desde arriba y en sentido horario."""
    b = R * abs(1 - 2 * k)
    barrido = 0 if k < 0.5 else 1          # creciente: la elipse vuelve por el lado de la luz; gibosa: por el otro
    d = f'M0 {-R} A{R} {R} 0 0 1 0 {R} A{b:.2f} {R} 0 0 {barrido} 0 {-R} Z'
    return f'<path d="{d}" transform="translate({cx} {cy}) rotate({rumbo - 90:.1f})" fill="{fill}" {extra}/>'


def lunula_area(R, r, d):
    a = R * R * math.acos((d * d + R * R - r * r) / (2 * d * R)) + r * r * math.acos((d * d + r * r - R * R) / (2 * d * r))
    a -= 0.5 * math.sqrt((-d + R + r) * (d + R - r) * (d - R + r) * (d + R + r))
    return (math.pi * R * R - a) / (math.pi * R * R)


# medianas medidas por lunas.py sobre 31 lunas
K, RR, ANG = 0.30, 0.91, 36
r = RR * R; d = R * (2 * K - 1 + RR)
bx, by = d * math.cos(math.radians(ANG)), -d * math.sin(math.radians(ANG))
W, H, PW = 1240, 430, 290
def panel(i): return 20 + i * (PW + 13.3)
o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Georgia, serif">',
     '<defs>',
     '<linearGradient id="noche" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#141a3f"/><stop offset="1" stop-color="#3a2f6b"/></linearGradient>',
     '<linearGradient id="manana" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fa9d6"/><stop offset="0.75" stop-color="#b9cfe4"/><stop offset="1" stop-color="#f1d9c0"/></linearGradient>',
     '<radialGradient id="halo"><stop offset="0" stop-color="#fff3c4" stop-opacity="0.45"/><stop offset="1" stop-color="#fff3c4" stop-opacity="0"/></radialGradient>',
     '</defs>', f'<rect width="{W}" height="{H}" fill="#f6f3ec"/>']
titulos = ['La luna de las máquinas', 'Los cuernos', 'Buenos Aires, 14/12/2026, 22:00', 'Buenos Aires, hoy, 6:48']
subs = ['mediana de 31: dos círculos, tapa a 36° arriba a la derecha', 'dos círculos: 232° de borde · fase: 180°',
        'k = 0,29 · la luz mira a 234° · una sola forma', 'k = 0,74 · la luz mira a 74° · Sol recién salido']
for i in range(4):
    x = panel(i); cx, cy = x + PW / 2, 160
    fondo = 'url(#manana)' if i == 3 else ('#fbfaf6' if i == 1 else 'url(#noche)')
    o.append(f'<rect x="{x:.1f}" y="20" width="{PW}" height="300" rx="6" fill="{fondo}"' + (' stroke="#c9c2b2"' if i == 1 else '') + '/>')
    if i == 0:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{2.3 * R}" fill="url(#halo)"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff3c4"/>')
        o.append(f'<circle cx="{cx + bx:.1f}" cy="{cy + by:.1f}" r="{r:.1f}" fill="#141a3f"/>')   # la tapa, del color de una parada del cielo
    if i == 1:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#2b2b2b" stroke-width="1.6"/>')
        o.append(f'<circle cx="{cx + bx:.1f}" cy="{cy + by:.1f}" r="{r:.1f}" fill="none" stroke="#b5482f" stroke-width="1.6"/>')
        # terminador de verdad con la misma luz (media elipse) y el diámetro de los cuernos
        b = R * (1 - 2 * K)
        o.append(f'<g transform="translate({cx} {cy}) rotate({234 - 90})"><path d="M0 {-R} A{b:.2f} {R} 0 0 1 0 {R}" fill="none" stroke="#2a6f97" stroke-width="1.8"/>'
                 f'<line x1="0" y1="{-R - 14}" x2="0" y2="{R + 14}" stroke="#2a6f97" stroke-width="1" stroke-dasharray="4 4"/>'
                 f'<circle cx="0" cy="{-R}" r="3.2" fill="#2a6f97"/><circle cx="0" cy="{R}" r="3.2" fill="#2a6f97"/></g>')
        # cuernos de la luna de dos círculos: intersección de los dos círculos
        a = (d * d + R * R - r * r) / (2 * d); h = math.sqrt(R * R - a * a); ux, uy = bx / d, by / d
        for sg in (1, -1):
            px, py = cx + a * ux - sg * h * uy, cy + a * uy + sg * h * ux
            o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="#b5482f"/>')
        o.append(f'<text x="{cx}" y="296" font-size="12.5" text-anchor="middle" fill="#b5482f">rojo: el disco que tapa y sus cuernos</text>')
        o.append(f'<text x="{cx}" y="312" font-size="12.5" text-anchor="middle" fill="#2a6f97">azul: el terminador y sus cuernos</text>')
    if i == 2:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{2.3 * R}" fill="url(#halo)" opacity="0.6"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff3c4" opacity="0.04"/>')              # luz cenicienta: más clara que el cielo, nunca más oscura
        o.append(fase(0.29, 234, cx, cy, R, '#fff3c4'))
    if i == 3:
        o.append(fase(0.74, 74.5, cx, cy, R, '#fbfcfd', 'opacity="0.82"'))
    o.append(f'<text x="{cx}" y="350" font-size="17" text-anchor="middle" fill="#2b2b2b">{titulos[i]}</text>')
    o.append(f'<text x="{cx}" y="372" font-size="12" text-anchor="middle" fill="#6b6558">{subs[i]}</text>')
o.append(f'<text x="{W / 2}" y="410" font-size="12" text-anchor="middle" fill="#6b6558">Tiempo libre, 1/10/2026 · escrito sin ver, mirado después · las medidas salen de lunas.py y cielo.py</text>')
o.append('</svg>')
open('2026-10-01_tres_lunas.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('área iluminada de la luna mediana de dos círculos: %.3f del disco (una fase con k = 0,30 tiene 0,300)' % lunula_area(R, r, d))
a = (d * d + R * R - r * r) / (2 * d * R); print('cuernos de la mediana: %.0f grados' % (360 - 2 * math.degrees(math.acos(a))))
