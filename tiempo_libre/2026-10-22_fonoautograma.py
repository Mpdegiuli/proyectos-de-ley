#!/usr/bin/env python3
"""
fonoautograma.py — una hoja ahumada escrita con código.

Canta despacio el principio de "Au clair de la lune" (aire popular francés del
siglo XVIII), la "escribe" como lo hacía el fonoautógrafo de Scott de Martinville
en 1860 —una cerda que raya una hoja ahumada enrollada en un cilindro que se gira
a mano— y escribe al lado la traza de un diapasón de 250 Hz, que es el reloj que
Scott ponía en sus hojas de 1860 ("500 v.s.": quinientas vibraciones simples).

Después lee la hoja de tres maneras, que son las tres lecturas que tuvo la hoja
real entre 2008 y 2009:
  - sin reloj: suponiendo que el cilindro giró parejo (no giró parejo);
  - con el diapasón leído como 500 Hz: el error de 2008 (sale una octava arriba,
    el doble de rápido: "una mujer");
  - con el diapasón leído como 250 Hz: la lectura de 2009 (un hombre, despacio).

Escribe:
  hoja.svg            la hoja ahumada entera (la traza de la voz y la del diapasón,
                      en renglones, como queda la hélice del cilindro desenrollada)
  detalle.svg         una lupa sobre 0,25 s, donde se ven los dos trazos
  voz_sin_reloj.wav, voz_500.wav, voz_250.wav   las tres lecturas
  partitura.txt       la lista de notas (frecuencia y duración) con que se cantó

No llama a nadie ni usa nada que no sea numpy y la biblioteca estándar.
Uso: python3 fonoautograma.py [carpeta_de_salida]
"""
import math
import os
import sys
import wave

import numpy as np

SALIDA = sys.argv[1] if len(sys.argv) > 1 else "."
os.makedirs(SALIDA, exist_ok=True)

SR = 8000          # muestras por segundo del "aire" (lo que vibra la membrana)
FORK = 250.0       # Hz del diapasón: 500 vibraciones simples por segundo
V0 = 250.0         # mm/s: velocidad nominal del papel bajo la cerda (una vibración
                   # entera del diapasón = 1 mm de hoja, para tener una regla fácil)

# --- la melodía ------------------------------------------------------------
# Primera frase y el arranque de la segunda. Negra = 0,62 s: muy lento, como
# cantaba Scott ("sluggish", dice First Sounds). La hoja se termina en "prê-".
NEGRA = 0.62
C3, D3, E3 = 130.81, 146.83, 164.81
melodia = [  # (sílaba, Hz, negras)
    ("Au", C3, 1), ("clair", C3, 1), ("de", C3, 1), ("la", D3, 1),
    ("lu", E3, 2), ("ne", D3, 2),
    ("mon", C3, 1), ("a", E3, 1), ("mi", D3, 1), ("Pier", D3, 1),
    ("rot", C3, 4),
    ("prê", C3, 1), ("te", C3, 1),
]
T_TOTAL = sum(n for _, _, n in melodia) * NEGRA
# Entre "Pierrot" y "prête" el cilindro casi se para (First Sounds lo vio en la hoja
# del 9 de abril de 1860: "possibly to a complete stop"). Acá se para casi del todo
# durante medio segundo, al terminar "rot".
T_PARADA = sum(n for _, _, n in melodia[:11]) * NEGRA - 0.3

t = np.arange(0, T_TOTAL, 1 / SR)

# --- la voz: una f0 por sílaba, con vibrato, armónicos y una envolvente -------
f0 = np.zeros_like(t)
env = np.zeros_like(t)
t0 = 0.0
with open(os.path.join(SALIDA, "partitura.txt"), "w") as f:
    f.write("silaba\thz\tsegundos\tdesde\n")
    for sil, hz, n in melodia:
        d = n * NEGRA
        m = (t >= t0) & (t < t0 + d)
        f0[m] = hz
        tt = t[m] - t0
        # ataque de 60 ms, caída en los últimos 80 ms (para que se oigan las sílabas)
        e = np.minimum(1, tt / 0.06) * np.minimum(1, (d - tt) / 0.08)
        env[m] = np.clip(e, 0, 1)
        f.write(f"{sil}\t{hz:.2f}\t{d:.2f}\t{t0:.2f}\n")
        t0 += d
vibrato = 1 + 0.004 * np.sin(2 * np.pi * 5.5 * t)
fase = 2 * np.pi * np.cumsum(f0 * vibrato) / SR
voz = np.zeros_like(t)
for n in range(1, 12):
    if n * E3 > SR / 2 - 200:
        break
    voz += np.sin(n * fase) / n ** 1.3
voz *= env
voz /= np.abs(voz).max()

diapason = np.sin(2 * np.pi * FORK * t)

# --- el cilindro: la velocidad del papel no es constante -------------------
# un vaivén de la mano (6 %, a 0,8 vueltas por segundo) y la casi-parada.
v = V0 * (1 + 0.06 * np.sin(2 * np.pi * 0.8 * t + 1.0))
v *= 1 - 0.92 * np.exp(-((t - T_PARADA) / 0.22) ** 2)
x = np.cumsum(v) / SR            # posición de la cerda sobre la hoja, en mm
L = float(x[-1])                 # largo de la traza

# --- la hoja, "escaneada": y en función de x, a paso uniforme en x ----------
def escanear(dx):
    xs = np.arange(0, L, dx)
    return xs, np.interp(xs, x, voz), np.interp(xs, x, diapason)

# --- las tres lecturas ------------------------------------------------------
def guardar_wav(nombre, senal, sr=SR):
    s = np.int16(np.clip(senal, -1, 1) * 32000)
    with wave.open(os.path.join(SALIDA, nombre), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(s.tobytes())

# escaneo fino para el sonido: 0,02 mm (50 puntos por vibración del diapasón)
xs, yv, yf = escanear(0.02)

# 1) sin reloj: x / V0 es el tiempo, como si el cilindro hubiera girado parejo
t_sin = xs / V0
t_uni = np.arange(0, t_sin[-1], 1 / SR)
guardar_wav("voz_sin_reloj.wav", np.interp(t_uni, t_sin, yv))

# 2) y 3) con reloj: cada cruce por cero del diapasón vale medio período
cruces = np.where(np.diff(np.signbit(yf)))[0]
x_cruces = xs[cruces]
for nombre, hz in (("voz_500.wav", 500.0), ("voz_250.wav", 250.0)):
    t_cruces = np.arange(len(x_cruces)) / (2 * hz)
    t_leido = np.interp(xs, x_cruces, t_cruces)
    t_uni = np.arange(0, t_leido[-1], 1 / SR)
    guardar_wav(nombre, np.interp(t_uni, t_leido, yv))

# --- la hoja en SVG ---------------------------------------------------------
PX = 4.0                       # píxeles por mm: una vibración del diapasón = 4 px
ANCHO_MM = 150.0               # cada renglón: 150 mm de traza (0,6 s a velocidad nominal)
ALTO_RENGLON = 44              # px
AMP_VOZ, AMP_FORK = 13.0, 4.0  # px
MARGEN = 24

def camino(xs_mm, ys, y0, amp, x_ini):
    """Un <path> con coordenadas relativas enteras (para que la hoja pese poco)."""
    px = np.round((xs_mm - x_ini) * PX + MARGEN).astype(int)
    py = np.round(y0 - ys * amp).astype(int)
    partes = [f"M{px[0]} {py[0]}"]
    dx = np.diff(px)
    dy = np.diff(py)
    partes.extend(f"l{a} {b}" for a, b in zip(dx, dy))
    return "".join(partes)

xs, yv, yf = escanear(1 / FORK * V0 / 6)   # 6 puntos por vibración del diapasón
n_reng = int(math.ceil(L / ANCHO_MM))
alto = MARGEN * 2 + n_reng * ALTO_RENGLON
ancho = int(ANCHO_MM * PX + 2 * MARGEN)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" '
       f'viewBox="0 0 {ancho} {alto}">',
       f'<rect width="{ancho}" height="{alto}" fill="#111"/>',
       '<g fill="none" stroke="#e8e2d0" stroke-width="0.8" stroke-linejoin="round">']
for r in range(n_reng):
    a, b = r * ANCHO_MM, (r + 1) * ANCHO_MM
    m = (xs >= a) & (xs < b)
    if m.sum() < 2:
        continue
    y0 = MARGEN + r * ALTO_RENGLON + 16
    svg.append(f'<path d="{camino(xs[m], yv[m], y0, AMP_VOZ, a)}"/>')
    svg.append(f'<path d="{camino(xs[m], yf[m], y0 + 22, AMP_FORK, a)}" stroke-width="0.6"/>')
svg.append("</g></svg>")
with open(os.path.join(SALIDA, "hoja.svg"), "w") as f:
    f.write("\n".join(svg))

# --- la lupa: 0,25 s alrededor del paso de "la" a "lu" (D3 → E3) ------------
t_lupa = sum(n for _, _, n in melodia[:4]) * NEGRA - 0.12
x_lupa = float(np.interp(t_lupa, t, x))
xs2, yv2, yf2 = escanear(0.02)
m = (xs2 >= x_lupa) & (xs2 < x_lupa + 0.25 * V0)
PX2 = 16.0
ancho2 = int(0.25 * V0 * PX2 + 2 * MARGEN)
alto2 = 170
def camino2(xs_mm, ys, y0, amp):
    px = (xs_mm - x_lupa) * PX2 + MARGEN
    py = y0 - ys * amp
    return "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in zip(px[::3], py[::3]))
svg2 = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho2}" height="{alto2}" '
        f'viewBox="0 0 {ancho2} {alto2}">',
        f'<rect width="{ancho2}" height="{alto2}" fill="#111"/>',
        '<g fill="none" stroke="#e8e2d0" stroke-width="1.2">',
        f'<path d="{camino2(xs2[m], yv2[m], 60, 40)}"/>',
        f'<path d="{camino2(xs2[m], yf2[m], 135, 14)}" stroke-width="0.9"/>',
        "</g>",
        f'<text x="{MARGEN}" y="{alto2 - 6}" fill="#e8e2d0" font-family="serif" font-size="11">'
        f'0,25 s de hoja: la voz pasa de re ({D3:.0f} Hz) a mi ({E3:.0f} Hz); abajo, el diapasón de 250 Hz</text>',
        "</svg>"]
with open(os.path.join(SALIDA, "detalle.svg"), "w") as f:
    f.write("\n".join(svg2))

print(f"traza: {L:.0f} mm en {T_TOTAL:.2f} s; {n_reng} renglones; "
      f"cruces del diapasón: {len(x_cruces)} (esperados {int(2 * FORK * T_TOTAL)})")
for nombre in ("voz_sin_reloj.wav", "voz_500.wav", "voz_250.wav"):
    with wave.open(os.path.join(SALIDA, nombre)) as w:
        print(f"{nombre}: {w.getnframes() / w.getframerate():.2f} s")
print("hoja.svg:", os.path.getsize(os.path.join(SALIDA, "hoja.svg")), "bytes")
