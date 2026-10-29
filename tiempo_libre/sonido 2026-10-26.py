#!/usr/bin/env python3
"""Hace sonar las secuencias del cuaderno con un timbre pellizcado de mentira
(suma de armónicos con decaimiento exponencial; no es un clave, es una idea de
clave) y las guarda como WAV; si hay ffmpeg, también como MP3.

Usa numpy. Las secuencias se importan de gato.py (misma semilla), así que lo
que suena es exactamente lo que vieron las instancias frescas.

  python3 sonido.py            -> escribe tema_scarlatti.wav, gato_simple.wav,
                                   gato_que_registra.wav, azar.wav (+ .mp3)
"""
import math
import random
import shutil
import subprocess
import wave

import numpy as np

import gato

SR = 44100


def nota(midi, dur, amp=0.5):
    f = 440.0 * 2 ** ((midi - 69) / 12)
    t = np.arange(int(SR * dur)) / SR
    # armónicos con pesos que bajan y un decaimiento que depende de la altura
    y = np.zeros_like(t)
    for k, w in enumerate((1.0, 0.55, 0.35, 0.2, 0.12, 0.08), start=1):
        y += w * np.sin(2 * math.pi * f * k * t)
    tau = max(0.25, 1.2 - midi / 100)
    y *= np.exp(-t / tau)
    y[: int(0.004 * SR)] *= np.linspace(0, 1, int(0.004 * SR))  # ataque corto
    return amp * y / 2.3


def secuencia(eventos, cola=1.2):
    """eventos: lista de (tiempo_inicio_s, [midis], duracion_s)."""
    fin = max(t0 + d for t0, _m, d in eventos) + cola
    out = np.zeros(int(SR * fin))
    for t0, midis, d in eventos:
        for m in midis:
            y = nota(m, d + 0.6)
            i = int(t0 * SR)
            out[i:i + len(y)] += y[: len(out) - i]
    pico = np.max(np.abs(out)) or 1.0
    return out / pico * 0.9


def guardar(nombre, y):
    with wave.open(nombre + '.wav', 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((y * 32767).astype('<i2').tobytes())
    if shutil.which('ffmpeg'):
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', nombre + '.wav',
                        '-codec:a', 'libmp3lame', '-q:a', '4', nombre + '.mp3'], check=False)
    print('escrito', nombre + '.wav', f'({len(y) / SR:.1f} s)')


def main():
    rng = random.Random(20261026)
    simple = gato.paseo_de_gato(rng, n_pisadas=5, zancada=12.0, desvio=3.0, vecina=0.5)[:8]
    azar = [rng.randint(48, 84) for _ in range(7)]
    registra = gato.gato_que_registra(random.Random(20261027), n_pasos=4, paso=10.0, desvio=2.5, vecina=0.5)

    # El tema de K.30 en 6/8, Moderato: seis negras con puntillo (un tiempo cada
    # una, 0,75 s) y después corcheas (0,25 s) que bajan hasta el sol.
    q = 0.75
    tema = [(i * q, [m], q) for i, m in enumerate(gato.SCARLATTI[:6])]
    bajada = [gato.midi_de(n) for n in 'D5 C5 Bb4 A4 G4 F#4 G4'.split()]
    t = 6 * q
    for m in bajada[:-1]:
        tema.append((t, [m], q / 3))
        t += q / 3
    tema.append((t, [bajada[-1]], q))
    guardar('tema_scarlatti', secuencia(tema))

    # El gato simple: una tecla por pisada, racimos pegados, tiempos algo irregulares
    r = random.Random(1)
    t = 0.0
    ev = []
    i = 0
    while i < len(simple):
        racimo = [simple[i]]
        if i + 1 < len(simple) and simple[i + 1] - simple[i] <= 2:
            racimo.append(simple[i + 1])
            i += 1
        ev.append((t, racimo, 0.5))
        t += r.uniform(0.35, 0.7)
        i += 1
    guardar('gato_simple', secuencia(ev))

    # El gato que registra: cada pisada es un racimo; las traseras repiten
    t = 0.0
    ev = []
    i = 0
    while i < len(registra):
        racimo = [registra[i]]
        if i + 1 < len(registra) and 0 < registra[i + 1] - registra[i] <= 2:
            racimo.append(registra[i + 1])
            i += 1
        ev.append((t, racimo, 0.5))
        t += r.uniform(0.3, 0.55)
        i += 1
    guardar('gato_que_registra', secuencia(ev))

    guardar('azar', secuencia([(i * 0.5, [m], 0.5) for i, m in enumerate(azar)]))


if __name__ == '__main__':
    main()
