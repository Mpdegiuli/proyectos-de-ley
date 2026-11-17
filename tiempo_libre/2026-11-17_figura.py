"""figura.py — Veinte segundos (tiempo libre, 17/11/2026).

Dibuja veinte_segundos.svg: setenta y cinco segundos de una sesión de manejo del Lunojod 1 tal como
la describen RAND R-802 (1971) y Dovgán: un cuadro de televisión cada 20 s, 1,28 s de luz por
sentido, unos 2,4 s de gente entre ver y ordenar, órdenes de marcha de 27 s como máximo a 0,93 km/h
(7 m). Arriba, la Luna y la Tierra como dos carriles unidos por las señales (diagonales); abajo,
dónde está el vehículo de verdad (línea llena) y dónde está en la foto que el conductor tiene
delante (escalones), con el hueco entre las dos sombreado: eso es lo que el conductor no ve.
Uso: python3 -I figura.py. No lee nada; escribe veinte_segundos.svg al lado del script."""
from pathlib import Path

LUZ = 384_400 / 299_792.458          # 1,28 s
GENTE = 5 - 2 * LUZ                  # 2,44 s (RAND: 5 s de suceso a respuesta)
CUADRO = 20.0                        # s
TOPE = 27.0                          # s
V = 0.93 / 3.6                       # m/s
T_FIN = 75.0

W, H = 980, 560
x0, x1 = 90, 940
def X(t): return x0 + (x1 - x0) * t / T_FIN
yL, yT = 125, 240                    # carriles Luna y Tierra
yP0, yP1 = 510, 320                  # eje de posición (0 m abajo, 16 m arriba)
def Y(m): return yP0 - (yP0 - yP1) * m / 16.0

# cronología
cuadros = [0, 20, 40, 60]
llegadas = [c + LUZ for c in cuadros]
# primera orden: tras el cuadro 0; segunda: tras el primer cuadro que muestra el vehículo parado (40)
ordenes_tierra = [llegadas[0] + GENTE, llegadas[2] + GENTE]
ordenes_luna = [o + LUZ for o in ordenes_tierra]
marchas = [(o, min(o + TOPE, T_FIN)) for o in ordenes_luna]

def pos(t):
    m = 0.0
    for a, b in marchas:
        if t >= a:
            m += V * (min(t, b) - a)
    return m

# posición que muestra el último cuadro recibido en la Tierra en el instante t
def pos_vista(t):
    ultimo = None
    for c, l in zip(cuadros, llegadas):
        if l <= t:
            ultimo = c
    return None if ultimo is None else pos(ultimo)

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Georgia, serif">')
s.append(f'<rect width="{W}" height="{H}" fill="#f6f3ec"/>')
s.append(f'<text x="{x0}" y="36" font-size="22" fill="#222">Veinte segundos</text>')
s.append(f'<text x="{x0}" y="58" font-size="12.5" fill="#555">Setenta y cinco segundos de una sesión de manejo del Lunojod 1, según RAND R-802 (1971) y Dovgán:</text>')
s.append(f'<text x="{x0}" y="75" font-size="12.5" fill="#555">un cuadro de televisión cada 20 s, 1,28 s de luz por sentido, 2,4 s de gente, marchas de 27 s como máximo a 0,93 km/h.</text>')

# carriles
for y, nombre in ((yL, "Luna"), (yT, "Tierra")):
    s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#888" stroke-width="1"/>')
    s.append(f'<text x="{x0-10}" y="{y+4}" font-size="13" fill="#333" text-anchor="end">{nombre}</text>')
# segundos
for t in range(0, 76, 5):
    s.append(f'<line x1="{X(t)}" y1="{yT}" x2="{X(t)}" y2="{yT+5}" stroke="#888"/>')
    if t % 10 == 0:
        s.append(f'<text x="{X(t)}" y="{yT+19}" font-size="11" fill="#666" text-anchor="middle">{t} s</text>')
# cuadros: de la Luna a la Tierra
for c, l in zip(cuadros, llegadas):
    s.append(f'<line x1="{X(c)}" y1="{yL}" x2="{X(l)}" y2="{yT}" stroke="#2a6f97" stroke-width="1.6"/>')
    s.append(f'<rect x="{X(c)-5}" y="{yL-13}" width="10" height="8" rx="1" fill="#2a6f97"/>')
    s.append(f'<circle cx="{X(c)}" cy="{yL-15}" r="1.6" fill="#2a6f97"/>')
    s.append(f'<text x="{X(c)}" y="{yL-22}" font-size="11" fill="#2a6f97" text-anchor="middle">foto {cuadros.index(c)+1}</text>')
# órdenes: de la Tierra a la Luna
for ot, ol in zip(ordenes_tierra, ordenes_luna):
    s.append(f'<line x1="{X(ot)}" y1="{yT}" x2="{X(ol)}" y2="{yL}" stroke="#b5452b" stroke-width="1.6"/>')
    s.append(f'<text x="{X(ot)+4}" y="{yT+34}" font-size="11" fill="#b5452b">«Primera, adelante»</text>')
# marchas sobre el carril Luna
for a, b in marchas:
    s.append(f'<rect x="{X(a)}" y="{yL-5}" width="{X(b)-X(a)}" height="10" fill="#b5452b" opacity="0.25"/>')
    s.append(f'<text x="{(X(a)+X(b))/2}" y="{yL+24}" font-size="11" fill="#b5452b" text-anchor="middle">marcha, {b-a:.0f} s → {V*(b-a):.0f} m</text>')
# gente
s.append(f'<rect x="{X(llegadas[0])}" y="{yT-5}" width="{X(ordenes_tierra[0])-X(llegadas[0])}" height="10" fill="#555" opacity="0.25"/>')
s.append(f'<text x="{X(llegadas[0])}" y="{yT-10}" font-size="10.5" fill="#555">mirar, decidir: {GENTE:.1f} s</text>')
s.append(f'<text x="{X(0)+2}" y="{yL+45}" font-size="10.5" fill="#2a6f97">luz: {LUZ:.2f} s por sentido</text>')

# posición
s.append(f'<line x1="{x0}" y1="{yP0}" x2="{x1}" y2="{yP0}" stroke="#888"/>')
s.append(f'<line x1="{x0}" y1="{yP0}" x2="{x0}" y2="{yP1}" stroke="#888"/>')
for m in range(0, 17, 4):
    s.append(f'<line x1="{x0-4}" y1="{Y(m)}" x2="{x0}" y2="{Y(m)}" stroke="#888"/>')
    s.append(f'<text x="{x0-8}" y="{Y(m)+4}" font-size="11" fill="#666" text-anchor="end">{m} m</text>')
for t in range(0, 76, 10):
    s.append(f'<line x1="{X(t)}" y1="{yP0}" x2="{X(t)}" y2="{yP0+5}" stroke="#888"/>')
    s.append(f'<text x="{X(t)}" y="{yP0+19}" font-size="11" fill="#666" text-anchor="middle">{t} s</text>')
# hueco sombreado entre lo real y lo visto
paso = 0.25
t = llegadas[0]
pts_arriba, pts_abajo = [], []
while t <= T_FIN:
    pv = pos_vista(t)
    pr = pos(t)
    pts_arriba.append((X(t), Y(pr)))
    pts_abajo.append((X(t), Y(pv if pv is not None else 0)))
    t += paso
poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts_arriba) + " " + " ".join(f"{x:.1f},{y:.1f}" for x, y in reversed(pts_abajo))
s.append(f'<polygon points="{poly}" fill="#b5452b" opacity="0.18"/>')
# línea real
pts = [(X(t/4), Y(pos(t/4))) for t in range(0, int(T_FIN*4)+1)]
s.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" fill="none" stroke="#222" stroke-width="2"/>')
# línea vista (escalones)
pts = []
for t4 in range(0, int(T_FIN*4)+1):
    t = t4/4
    pv = pos_vista(t)
    if pv is None: continue
    pts.append((X(t), Y(pv)))
s.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" fill="none" stroke="#2a6f97" stroke-width="2" stroke-dasharray="5 3"/>')
# cuadros sobre el eje de posición
for c, l in zip(cuadros, llegadas):
    s.append(f'<line x1="{X(c)}" y1="{yP1-10}" x2="{X(c)}" y2="{yP0}" stroke="#2a6f97" stroke-width="0.8" stroke-dasharray="2 3"/>')
# leyenda
s.append(f'<line x1="{X(1)}" y1="{yP1+6}" x2="{X(5)}" y2="{yP1+6}" stroke="#222" stroke-width="2"/>')
s.append(f'<text x="{X(6)}" y="{yP1+10}" font-size="11.5" fill="#222">dónde está el vehículo</text>')
s.append(f'<line x1="{X(1)}" y1="{yP1+24}" x2="{X(5)}" y2="{yP1+24}" stroke="#2a6f97" stroke-width="2" stroke-dasharray="5 3"/>')
s.append(f'<text x="{X(6)}" y="{yP1+28}" font-size="11.5" fill="#2a6f97">dónde está en la foto que mira el conductor</text>')
s.append(f'<rect x="{X(1)}" y="{yP1+36}" width="{X(5)-X(1)}" height="10" fill="#b5452b" opacity="0.18"/>')
s.append(f'<text x="{X(6)}" y="{yP1+45}" font-size="11.5" fill="#b5452b">lo que el conductor no ve</text>')
# máximo hueco
hueco = max(pos(t/4) - (pos_vista(t/4) or 0) for t in range(int(llegadas[0]*4), int(T_FIN*4)))
s.append(f'<text x="{x0}" y="{H-14}" font-size="11" fill="#555">El hueco llega a {hueco:.1f} m justo antes de que llegue la foto siguiente. Dovgán: «mientras recibimos la imagen, el Lunojod recorre 6 metros».</text>')
s.append("</svg>")
Path(__file__).resolve().with_name("veinte_segundos.svg").write_text("\n".join(s), encoding="utf-8")
print("→ veinte_segundos.svg; hueco máximo", round(hueco, 2), "m")
