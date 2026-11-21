#!/usr/bin/env python3
"""Un receptor de tonos (DTMF) de juguete, con y sin "acción de guardia".

Lee cualquier archivo de audio que ffmpeg entienda (mp3, wav), lo pasa a mono 8.000 Hz y
escucha de a cuadros de 205 muestras (25,6 ms; paso 10 ms) con el algoritmo de Goertzel en las ocho
frecuencias del teclado. Una tecla "se marca" cuando el mismo par (fila, columna) se
sostiene al menos 40 ms, que es el tiempo de reconocimiento que da Schenker (1960).

Dos receptores:
  sin guardia: acepta la tecla si el tono de fila más fuerte y el de columna más fuerte
               superan un umbral absoluto. Nada más. Es el receptor ingenuo.
  con guardia: además exige (a) que el segundo tono de cada grupo esté al menos 8 dB por
               debajo del primero, (b) que los dos tonos no difieran entre sí en más de
               8 dB ("twist"), (c) que los dos tonos juntos tengan al menos el 70 % de la
               energía del cuadro entre 600 y 1.800 Hz. (c) es la "acción de guardia" del
               artículo de 1960: "ningún sonido compuesto de una multiplicidad de frecuencias
               a niveles comparables" debe pasar. (Una primera versión exigía además que el
               segundo armónico de cada tono estuviera 15 dB abajo; se sacó porque con cuadros
               de 25 ms el 1.336 de la tecla 2 se derrama sobre 1.394, el doble de 697, y la
               tecla 2 del propio teclado no pasaba.)

Uso: python3 decodificar.py archivo1.mp3 [archivo2.wav ...]
"""
import math
import subprocess
import sys

import numpy as np

FS = 8000
FILAS = [697, 770, 852, 941]
COLS = [1209, 1336, 1477, 1633]
TECLAS = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]
CUADRO = 205  # 25,6 ms: el largo clásico de Goertzel a 8.000 Hz para estas ocho frecuencias
PASO = int(0.010 * FS)
UMBRAL_DB = -45.0  # respecto de un tono puro a plena escala, por tono


def cargar(nombre):
    cmd = ["ffmpeg", "-loglevel", "error", "-i", nombre, "-f", "s16le", "-acodec", "pcm_s16le", "-ac", "1", "-ar", str(FS), "-"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0


def goertzel(x, f):
    """Potencia (relativa) de x en la frecuencia f, normalizada para que un seno de amplitud 1 dé 1."""
    n = len(x)
    w = 2 * math.pi * f / FS  # frecuencia exacta, no la del bin entero
    c = 2 * math.cos(w)
    s0 = s1 = s2 = 0.0
    for v in x:
        s0 = v + c * s1 - s2
        s2, s1 = s1, s0
    p = s1 * s1 + s2 * s2 - c * s1 * s2
    return p / (n * n / 4)


def db(p):
    return 10 * math.log10(p + 1e-12)


def energia_banda(x, lo=600, hi=1800):
    """Energía del cuadro entre lo y hi, normalizada como goertzel: un seno de amplitud 1 da ~1 (Parseval)."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / FS)
    m = (f >= lo) & (f <= hi)
    return float(np.sum(np.abs(X[m]) ** 2) / (len(x) * len(x) / 4))


def cuadro_a_tecla(x, guardia):
    pf = [goertzel(x, f) for f in FILAS]
    pc = [goertzel(x, f) for f in COLS]
    i = int(np.argmax(pf))
    j = int(np.argmax(pc))
    if db(pf[i]) < UMBRAL_DB or db(pc[j]) < UMBRAL_DB:
        return None
    if not guardia:
        return TECLAS[i][j]
    seg_f = max(p for k, p in enumerate(pf) if k != i)
    seg_c = max(p for k, p in enumerate(pc) if k != j)
    if db(pf[i]) - db(seg_f) < 8 or db(pc[j]) - db(seg_c) < 8:
        return None
    if abs(db(pf[i]) - db(pc[j])) > 8:
        return None
    total = energia_banda(x)
    if (pf[i] + pc[j]) < 0.70 * total:
        return None
    return TECLAS[i][j]


def decodificar(x, guardia, minimo_ms=40):
    teclas = []
    t = 0
    for ini in range(0, len(x) - CUADRO, PASO):
        teclas.append(cuadro_a_tecla(x[ini:ini + CUADRO], guardia))
    # tramos sostenidos
    salida = []
    actual, desde = None, 0
    for n, k in enumerate(teclas + [None]):
        if k != actual:
            if actual is not None and (n - desde) * 10 >= minimo_ms:
                salida.append((actual, desde * 10, (n - desde) * 10))
            actual, desde = k, n
    return salida


def resumen(nombre):
    x = cargar(nombre)
    print(f"== {nombre}: {len(x)/FS:.1f} s")
    for guardia in (False, True):
        tramos = decodificar(x, guardia)
        marcado = "".join(k for k, _, _ in tramos)
        print(f"   {'con guardia' if guardia else 'sin guardia'}: {len(tramos)} teclas  -> {marcado if marcado else '(nada)'}")
        if tramos and len(tramos) <= 40:
            print("     " + ", ".join(f"{k}@{t}ms/{d}ms" for k, t, d in tramos))


if __name__ == "__main__":
    for nombre in sys.argv[1:]:
        resumen(nombre)
