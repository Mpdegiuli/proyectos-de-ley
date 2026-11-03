#!/usr/bin/env python3
"""Hace sonar las señales: escribe senales.wav con las seis señales de la figura, una tras otra
con dos segundos de silencio: ···−−−··· como signo continuo, SOS con huecos de letra, SOE como
signo continuo, CQD, NC y SSS DDD, a 12 palabras por minuto
(unidad = 100 ms, tono de 700 Hz). Solo biblioteca estándar; si hay ffmpeg, también senales.mp3."""
import math, struct, subprocess, shutil, wave

MORSE = {'S': '...', 'O': '---', 'E': '.', 'C': '-.-.', 'Q': '--.-', 'D': '-..', 'N': '-.'}
FS, UNIDAD, HZ = 22050, 0.100, 700.0

def tono(seg):
    n = int(FS * seg)
    return [0.6 * math.sin(2 * math.pi * HZ * i / FS) * min(1, i / 200, (n - i) / 200) for i in range(n)]

def silencio(seg):
    return [0.0] * int(FS * seg)

def senal(letras, continuo):
    out = []
    for i, l in enumerate(letras):
        for j, e in enumerate(MORSE[l]):
            out += tono(UNIDAD if e == '.' else 3 * UNIDAD)
            out += silencio(UNIDAD)
        if i < len(letras) - 1:
            out += silencio(0 if continuo else 2 * UNIDAD)
    return out

muestras = []
for letras, continuo in [("SOS", True), ("SOS", False), ("SOE", True), ("CQD", False), ("NC", False), ("SSSDDD", False)]:
    muestras += senal(letras, continuo) + silencio(2.0)
with wave.open("senales.wav", "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(FS)
    w.writeframes(b"".join(struct.pack("<h", int(32767 * m)) for m in muestras))
print(f"senales.wav: {len(muestras) / FS:.1f} s")
if shutil.which("ffmpeg"):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "senales.wav", "-b:a", "64k", "senales.mp3"], check=True)
    print("senales.mp3")
