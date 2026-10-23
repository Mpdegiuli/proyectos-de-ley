#!/usr/bin/env python3
"""
leer.py — mide lo que se oye en cada lectura de la hoja (sin oírlo).

Para cada WAV estima la altura (f0) cada 50 ms por autocorrelación y la compara
con la partitura con que se cantó. Imprime: duración, f0 mediana por sílaba y
el desvío respecto de lo cantado. Uso: python3 leer.py carpeta
"""
import os
import sys
import wave

import numpy as np

carpeta = sys.argv[1] if len(sys.argv) > 1 else "salida"

def cargar(nombre):
    with wave.open(os.path.join(carpeta, nombre)) as w:
        sr = w.getframerate()
        s = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16) / 32768
    return sr, s

def f0_por_autocorrelacion(sr, s, paso=0.05, vent=0.06, fmin=60, fmax=700):
    out = []
    n = int(vent * sr)
    for i in range(0, len(s) - n, int(paso * sr)):
        v = s[i:i + n]
        if np.abs(v).max() < 0.05:
            out.append((i / sr, np.nan))
            continue
        v = v - v.mean()
        ac = np.correlate(v, v, "full")[n - 1:]
        lo, hi = int(sr / fmax), int(sr / fmin)
        k = lo + np.argmax(ac[lo:hi])
        out.append((i / sr, sr / k))
    return out

partitura = []
with open(os.path.join(carpeta, "partitura.txt")) as f:
    next(f)
    for linea in f:
        sil, hz, d, desde = linea.split("\t")
        partitura.append((sil, float(hz), float(d), float(desde)))

for nombre in ("voz_sin_reloj.wav", "voz_500.wav", "voz_250.wav"):
    sr, s = cargar(nombre)
    dur = len(s) / sr
    f0 = f0_por_autocorrelacion(sr, s)
    print(f"\n== {nombre}: {dur:.2f} s")
    # escala temporal: la lectura a 500 corre al doble; la de 250 va a tiempo;
    # la sin reloj no tiene escala fija, se compara por posición proporcional
    factor = dur / (partitura[-1][3] + partitura[-1][2])
    print("silaba   cantado   leido   razon")
    for sil, hz, d, desde in partitura:
        a, b = (desde + 0.1) * factor, (desde + d - 0.1) * factor
        vals = [f for t, f in f0 if a <= t < b and not np.isnan(f)]
        if not vals:
            print(f"{sil:6s}  {hz:7.1f}      —")
            continue
        med = float(np.median(vals))
        print(f"{sil:6s}  {hz:7.1f}  {med:6.1f}  {med / hz:5.2f}   "
              f"(min {min(vals):.0f}, max {max(vals):.0f})")
