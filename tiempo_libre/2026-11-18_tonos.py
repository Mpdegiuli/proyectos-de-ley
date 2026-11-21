#!/usr/bin/env python3
"""Hace sonar el teclado de tonos y algunas cosas que no son el teclado.

Escribe archivos WAV (mono, 8.000 Hz, como una línea telefónica) y, si hay ffmpeg, MP3:
  teclado.wav          las doce teclas en orden (1 2 3 4 5 6 7 8 9 * 0 #) y después "1964"
  teclado_afinado.wav  lo mismo, con cada tono corrido a la nota más cercana del piano
  vocal_<nombre>.wav   zumbidos con formantes, a la manera del modelo de Fletcher que cita
                       Schenker (1960): un tren de pulsos a f0 pasado por dos resonadores

No lee nada del repositorio. Uso: python3 tonos.py [carpeta_de_salida]
"""
import math
import os
import subprocess
import sys
import wave

import numpy as np
from scipy.signal import lfilter

FS = 8000
FILAS = [697, 770, 852, 941]
COLS = [1209, 1336, 1477, 1633]
TECLAS = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "A": (0, 3), "4": (1, 0), "5": (1, 1), "6": (1, 2), "B": (1, 3),
          "7": (2, 0), "8": (2, 1), "9": (2, 2), "C": (2, 3), "*": (3, 0), "0": (3, 1), "#": (3, 2), "D": (3, 3)}


def afinada(f):
    """La frecuencia de la nota temperada más cercana (La4 = 440)."""
    n = round(12 * math.log2(f / 440.0))
    return 440.0 * 2 ** (n / 12)


def tecla(nombre, dur=0.15, pausa=0.10, afinar=False, nivel=0.3):
    i, j = TECLAS[nombre]
    fr, fc = FILAS[i], COLS[j]
    if afinar:
        fr, fc = afinada(fr), afinada(fc)
    t = np.arange(int(FS * dur)) / FS
    s = nivel * (np.sin(2 * math.pi * fr * t) + np.sin(2 * math.pi * fc * t))
    # bordes suaves de 5 ms para que no haga clic
    n = int(0.005 * FS)
    env = np.ones_like(s)
    env[:n] = np.linspace(0, 1, n)
    env[-n:] = np.linspace(1, 0, n)
    return np.concatenate([s * env, np.zeros(int(FS * pausa))])


def secuencia(texto, afinar=False):
    partes = []
    for c in texto:
        if c == " ":
            partes.append(np.zeros(int(FS * 0.4)))
        else:
            partes.append(tecla(c, afinar=afinar))
    return np.concatenate(partes)


def resonador(x, f, ancho):
    """Resonador de dos polos (un formante), ganancia unitaria en el pico."""
    r = math.exp(-math.pi * ancho / FS)
    theta = 2 * math.pi * f / FS
    a = [1, -2 * r * math.cos(theta), r * r]
    b = [1 - r]  # aproximación
    y = lfilter(b, a, x)
    return y / (np.max(np.abs(y)) + 1e-9)


def vocal(f0, formantes, dur=0.6, anchos=None, nivel=0.5):
    """Tren de pulsos a f0 (la 'chicharra' de las cuerdas vocales) por dos o tres resonadores."""
    n = int(FS * dur)
    x = np.zeros(n)
    periodo = FS / f0
    k = 0.0
    while k < n:
        x[int(k)] = 1.0
        k += periodo
    anchos = anchos or [60] * len(formantes)
    y = np.zeros(n)
    for f, w in zip(formantes, anchos):
        y += resonador(x, f, w)
    y = y / (np.max(np.abs(y)) + 1e-9) * nivel
    env = np.ones(n)
    m = int(0.02 * FS)
    env[:m] = np.linspace(0, 1, m)
    env[-m:] = np.linspace(1, 0, m)
    return y * env


def escribir(nombre, s):
    s = np.clip(s, -1, 1)
    with wave.open(nombre, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(FS)
        w.writeframes((s * 32767).astype("<i2").tobytes())
    mp3 = nombre[:-4] + ".mp3"
    try:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", nombre, "-codec:a", "libmp3lame", "-b:a", "64k", mp3], check=True)
    except Exception as e:  # sin ffmpeg queda el wav
        print("sin mp3:", e)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out, exist_ok=True)
    escribir(os.path.join(out, "teclado.wav"), secuencia("123456789*0# 1964"))
    escribir(os.path.join(out, "teclado_afinado.wav"), secuencia("123456789*0# 1964", afinar=True))
    # Vocales de Fletcher: zumbido + formantes. Los formantes de /a/ (hombre) de Peterson y Barney (1952): 730 y 1090 Hz.
    pruebas = {
        "a_120": (120, [730, 1090, 2440]),           # una "a" grave, hablada
        "a_174": (174.6, [730, 1090, 2440]),         # una "a" cantada en Fa3
        "uno_174": (174.6, [697, 1209]),             # Fa3 con los formantes puestos justo en la tecla 1
        "cinco_190": (190.0, [770, 1336]),           # armónicos 4 y 7 de 190 Hz: 760 y 1330 (tecla 5)
        "siete_171": (171.5, [852, 1209]),           # armónicos 5 y 7 de 171,5: 857 y 1200 (tecla 7)
        "silbido_1336": (1336, [1336]),              # un "silbido": un solo tono, no es una tecla
    }
    for nombre, (f0, form) in pruebas.items():
        escribir(os.path.join(out, f"vocal_{nombre}.wav"), vocal(f0, form))
    print("escrito en", out)
