#!/usr/bin/env python3
"""figura.py — escribe figura.svg: la elongación de Venus respecto del Sol de enero de 2025 a
diciembre de 2027 (arriba del cero, al este: lucero de la tarde, Héspero; abajo, al oeste:
lucero del alba, Fósforo), con las conjunciones, el punto de hoy y las fechas de Van Gogh
sobre el ciclo de 1889-1890 llevado al mismo eje; a la derecha, Venus como se ve hoy
(fase y diámetro) y el juicio «Héspero ≡ Fósforo» en los trazos de la Begriffsschrift.
Necesita ephem (pip install ephem). Uso: python3 figura.py
"""
import math, ephem

def elong(d):
    s, v = ephem.Sun(d), ephem.Venus(d)
    e = math.degrees(float(ephem.separation(s, v)))
    ls, lv = ephem.Ecliptic(s).lon, ephem.Ecliptic(v).lon
    return e if ((float(lv) - float(ls) + math.pi) % (2*math.pi) - math.pi) > 0 else -e

d0, d1 = ephem.Date("2025/01/01"), ephem.Date("2028/01/01")
hoy = ephem.Date("2026/11/08")
W, H = 1120, 540
x0, x1, y0, y1 = 70, 660, 60, 440   # panel de la curva
def X(d): return x0 + (d - d0) / (d1 - d0) * (x1 - x0)
def Y(e): return (y0 + y1) / 2 - e / 50 * (y1 - y0) / 2

pts = []
d = d0
while d <= d1:
    pts.append((X(d), Y(elong(d)))); d = ephem.Date(d + 2)
camino = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)

out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
       f'<rect width="{W}" height="{H}" fill="#f6f1e7"/>',
       # mitades
       f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{(y1-y0)/2}" fill="#3b2a5e" opacity="0.10"/>',
       f'<rect x="{x0}" y="{(y0+y1)/2}" width="{x1-x0}" height="{(y1-y0)/2}" fill="#e8865a" opacity="0.12"/>',
       f'<text x="{x0+8}" y="{y0+20}" font-size="14" fill="#3b2a5e">al este del Sol: se ve de tarde · Héspero</text>',
       f'<text x="{x0+8}" y="{y1-10}" font-size="14" fill="#8a4a1a">al oeste del Sol: se ve de mañana · Fósforo</text>',
       f'<line x1="{x0}" y1="{(y0+y1)/2}" x2="{x1}" y2="{(y0+y1)/2}" stroke="#555" stroke-width="1"/>',
       f'<text x="{x1+6}" y="{(y0+y1)/2+4}" font-size="11" fill="#555">0°</text>',
       f'<text x="{x1+6}" y="{Y(47)+4}" font-size="11" fill="#555">+47°</text>',
       f'<text x="{x1+6}" y="{Y(-47)+4}" font-size="11" fill="#555">−47°</text>',
       f'<path d="{camino}" fill="none" stroke="#222" stroke-width="2"/>']
# años
for a in (2025, 2026, 2027):
    xa = X(ephem.Date(f"{a}/01/01"))
    out.append(f'<line x1="{xa:.1f}" y1="{y0}" x2="{xa:.1f}" y2="{y1}" stroke="#999" stroke-dasharray="3 3"/>')
    out.append(f'<text x="{xa+4:.1f}" y="{y1+18}" font-size="12" fill="#333">{a}</text>')
# conjunciones (cruces por cero)
prev = elong(d0); d = d0
while d < d1:
    dn = ephem.Date(d + 1); e = elong(dn)
    if (e > 0) != (prev > 0):
        a, b = d, dn
        for _ in range(30):
            m = ephem.Date((a + b) / 2)
            if (elong(m) > 0) == (prev > 0): a = m
            else: b = m
        dc = b
        tipo = "inferior" if ephem.Venus(dc).earth_distance < 1 else "superior"
        out.append(f'<circle cx="{X(dc):.1f}" cy="{Y(0):.1f}" r="4" fill="#fff" stroke="#222" stroke-width="1.5"/>')
        out.append(f'<text x="{X(dc):.1f}" y="{Y(0) + (16 if tipo=="inferior" else -8):.1f}" font-size="10" fill="#333" text-anchor="middle">{tipo} {ephem.Date(dc).datetime():%d/%m/%Y}</text>')
    prev = e; d = dn
# hoy
eh = elong(hoy)
out.append(f'<circle cx="{X(hoy):.1f}" cy="{Y(eh):.1f}" r="6" fill="#c0392b"/>')
out.append(f'<text x="{X(hoy)+10:.1f}" y="{Y(eh)+4:.1f}" font-size="12" fill="#c0392b" font-weight="bold">hoy, 8/11/2026: {eh:+.0f}°</text>')
# Van Gogh: sus dos fechas llevadas al ciclo de 2026 por la conjunción inferior más cercana (1/5/1889 → 24/10/2026)
desfase = ephem.Date("2026/10/24") - ephem.Date("1889/05/01")
for fecha, texto, dy in (("1889/06/02", "Venus de la carta 777 (2/6/1889), llevado al ciclo de hoy", 16), ("1890/04/20", "Venus, Mercurio y la Luna (20/4/1890)", -10)):
    f = ephem.Date(fecha); e = elong(f); xf = X(ephem.Date(f + desfase))
    out.append(f'<circle cx="{xf:.1f}" cy="{Y(e):.1f}" r="5" fill="none" stroke="#1a6b3a" stroke-width="2"/>')
    anc = "end" if e > 0 else "start"; xt = xf - 9 if e > 0 else xf + 9
    out.append(f'<text x="{xt:.1f}" y="{Y(e)+dy:.1f}" font-size="10.5" fill="#1a6b3a" text-anchor="{anc}">{texto}</text>')
out.append(f'<text x="{x0}" y="{y0-30}" font-size="18" fill="#222">Elongación de Venus, 2025–2027 (grados al este o al oeste del Sol)</text>')
out.append(f'<text x="{x0}" y="{y0-12}" font-size="12" fill="#555">la misma curva, dos nombres: cuando cruza el cero no se ve, y al salir del otro lado cambia de nombre</text>')

# panel derecho: Venus hoy
px, py = 720, 60
v = ephem.Venus(hoy)
fase = v.phase / 100.0   # fracción iluminada
R = 70
out.append(f'<text x="{px}" y="{py}" font-size="16" fill="#222">Venus hoy, visto con aumento</text>')
out.append(f'<text x="{px}" y="{py+18}" font-size="12" fill="#555">{v.phase:.0f} % iluminado, {v.size:.0f}″ de diámetro, magnitud {v.mag:.1f}</text>')
cx, cy = px + 110, py + 130
out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#1b1a2e"/>')
# creciente: lado iluminado hacia el Sol (a la derecha, abajo del horizonte este, de mañana); el terminador es una elipse
k = 2 * fase - 1   # -1 luna nueva, +1 llena; semieje del terminador
rx = abs(k) * R
sweep_term = 0 if k < 0 else 1
out.append(f'<path d="M{cx} {cy-R} A{R} {R} 0 0 1 {cx} {cy+R} A{rx:.2f} {R} 0 0 {sweep_term} {cx} {cy-R} Z" fill="#fff6d6"/>')
out.append(f'<text x="{px}" y="{cy+R+24}" font-size="11.5" fill="#555">una uña de luz, no una estrella de cuatro puntas:</text>')
out.append(f'<text x="{px}" y="{cy+R+39}" font-size="11.5" fill="#555">lo que ninguna de las ocho instancias dibujó</text>')

# Begriffsschrift: ⊢ (Héspero ≡ Fósforo)
bx, by = 720, 360
out.append(f'<text x="{bx}" y="{by-18}" font-size="16" fill="#222">El juicio de 1892 en los trazos de 1879</text>')
out.append(f'<g stroke="#222" stroke-width="2.2" stroke-linecap="square" fill="none">'
           f'<line x1="{bx+10}" y1="{by+12}" x2="{bx+10}" y2="{by+40}"/>'
           f'<line x1="{bx+10}" y1="{by+26}" x2="{bx+100}" y2="{by+26}"/></g>')
out.append(f'<text x="{bx+110}" y="{by+32}" font-size="20" font-family="Georgia, serif" fill="#222">(Héspero ≡ Fósforo)</text>')
out.append(f'<text x="{bx}" y="{by+70}" font-size="11.5" fill="#555">trazo de juicio, trazo de contenido, identidad de contenido.</text>')
out.append(f'<text x="{bx}" y="{by+85}" font-size="11.5" fill="#555">En 1879 el ≡ decía que dos signos tienen el mismo contenido;</text>')
out.append(f'<text x="{bx}" y="{by+100}" font-size="11.5" fill="#555">en 1892 pasó a decir que dos sentidos dan con una cosa.</text>')
out.append(f'<text x="{bx}" y="{by+115}" font-size="11.5" fill="#555">(Fórmula mía: Frege nunca la escribió.)</text>')
out.append(f'<text x="{x0}" y="{H-14}" font-size="11" fill="#777">Cuaderno de tiempo libre, 8/11/2026. Posiciones con ephem (VSOP87); el ciclo de 1889-1890 se superpone al de hoy por la conjunción inferior más cercana (1/5/1889 → 24/10/2026).</text>')
out.append('</svg>')
open("figura.svg", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("figura.svg")
