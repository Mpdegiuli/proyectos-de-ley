#!/usr/bin/env python3
"""Una música escrita sin oírla (22/11/2026).

Una melodía propia de ocho compases en 3/4, repetida seis veces sin cambiar una
nota: lo único que cambia es cuántas voces la dicen y a qué volumen, sobre un
tambor de dos compases que tampoco cambia. Es la forma del Boléro con otra
melodía y otro tambor; no hay una sola nota de Ravel.

Escribe:
  2026-11-22_musica.wav        el sonido (44.100 Hz, mono, ~2 min)
  2026-11-22_musica.abc        la melodía y el tambor en notación ABC, para leerla
  2026-11-22_compases.csv      un renglón por compás: volumen, altura media, voces
  2026-11-22_cuadro.svg        el dibujo compás por compás (un rectángulo por compás:
                               el largo es el volumen, el color la altura, la forma
                               cuántas voces), en zigzag, a la manera de Anne Adams

Solo numpy. Después: ffmpeg -i 2026-11-22_musica.wav 2026-11-22_musica.mp3
"""
import csv
import math
import wave
from pathlib import Path

import numpy as np

AQUI = Path(__file__).parent
SR = 44100
BPM = 72                # el número de las ediciones tardías del Boléro, según la Wikipedia
NEGRA = 60.0 / BPM      # 0,8333 s
COMPAS = 3 * NEGRA      # 2,5 s
REPETICIONES = 6

# --- la melodía: (nota MIDI, duración en negras). Re dórico. Ocho compases.
MELODIA = [
    (62, 1), (62, 1), (65, 1),            # re re fa
    (69, 2), (67, 1),                     # la ... sol
    (65, 1.5), (64, 0.5), (62, 1),        # fa  mi re
    (60, 2), (64, 1),                     # do ... mi
    (65, 1), (65, 1), (69, 1),            # fa fa la
    (72, 2), (71, 1),                     # do' ... si
    (69, 1), (67, 0.5), (65, 0.5), (64, 1),  # la sol fa mi
    (62, 3),                              # re ---
]
assert abs(sum(d for _, d in MELODIA) - 24) < 1e-9

# --- el tambor: dos compases, golpes en negras desde el principio del compás 1.
# compás A: negra, corchea corchea, negra        → 0, 1, 1.5, 2
# compás B: corchea corchea, negra, corchea corchea → 3, 3.5, 4, 5, 5.5
TAMBOR = [0, 1, 1.5, 2, 3, 3.5, 4, 5, 5.5]   # 9 golpes por dos compases
ACENTO = {0: 1.0, 1: 0.6, 1.5: 0.5, 2: 0.8, 3: 0.7, 3.5: 0.5, 4: 1.0, 5: 0.6, 5.5: 0.5}

def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)

def envolvente(n, ataque=0.01, caida=0.08):
    a = int(SR * ataque); c = int(SR * caida)
    env = np.ones(n)
    if a > 0:
        env[:a] = np.linspace(0, 1, a)
    if c > 0 and c < n:
        env[-c:] = np.linspace(1, 0, c)
    return env

def voz(midi, dur, timbre, amp):
    """Un sonido de 'dur' segundos. timbre: 'seno', 'triangulo' (armónicos impares),
    'sierra' (todos los armónicos, cayendo)."""
    n = int(SR * dur)
    t = np.arange(n) / SR
    f = hz(midi)
    if timbre == "seno":
        y = np.sin(2 * np.pi * f * t)
    elif timbre == "triangulo":
        y = sum(((-1) ** k) * np.sin(2 * np.pi * (2 * k + 1) * f * t) / (2 * k + 1) ** 2 for k in range(6))
    else:  # sierra
        y = sum(np.sin(2 * np.pi * k * f * t) / k for k in range(1, 10) if k * f < 12000)
    y = y / np.max(np.abs(y))
    return amp * y * envolvente(n)

def golpe(amp, rng):
    """Un golpe de tambor: ruido con caída rápida."""
    n = int(SR * 0.09)
    t = np.arange(n) / SR
    ruido = rng.standard_normal(n)
    # filtro pasabajos muy simple (promedio móvil) para que no sea tan áspero
    k = 6
    ruido = np.convolve(ruido, np.ones(k) / k, mode="same")
    env = np.exp(-t * 55)
    y = ruido * env
    return amp * y / np.max(np.abs(y))

def capas(rep):
    """Qué voces entran en cada repetición (0..5)."""
    c = {"melodia_seno": True}
    c["tambor"] = True
    c["octava_abajo"] = rep >= 1
    c["pedal"] = rep >= 2
    c["sierra"] = rep >= 2
    c["octava_arriba"] = rep >= 3
    c["quinta"] = rep >= 4
    c["tambor_doble"] = rep >= 5
    return c

def main():
    rng = np.random.default_rng(1928)
    total = REPETICIONES * 8 * COMPAS + 2.0
    out = np.zeros(int(SR * total))
    compases = []  # para el cuadro

    for rep in range(REPETICIONES):
        c = capas(rep)
        nvoces = sum(1 for k, v in c.items() if v and k.startswith(("melodia", "octava", "quinta", "sierra", "pedal")))
        vol = 0.12 * (1.0 / 0.12) ** (rep / (REPETICIONES - 1))   # 0,12 → 1,0, geométrico
        t0 = rep * 8 * COMPAS
        # pedal: re grave sostenido ocho compases
        if c["pedal"]:
            n = int(SR * 8 * COMPAS)
            t = np.arange(n) / SR
            ped = 0.25 * vol * np.sin(2 * np.pi * hz(38) * t) * envolvente(n, 0.5, 0.5)
            i = int(SR * t0); out[i:i + n] += ped
        # melodía y sus dobles
        pos = 0.0
        for midi, dur in MELODIA:
            d = dur * NEGRA
            i = int(SR * (t0 + pos))
            y = voz(midi, d, "seno", 0.5 * vol)
            if c["sierra"]:
                y = 0.6 * y + voz(midi, d, "sierra", 0.25 * vol)
            if c["octava_abajo"]:
                y += voz(midi - 12, d, "triangulo", 0.35 * vol)
            if c["octava_arriba"]:
                y += voz(midi + 12, d, "seno", 0.3 * vol)
            if c["quinta"]:
                y += voz(midi + 7, d, "seno", 0.2 * vol)
            out[i:i + len(y)] += y
            pos += dur * NEGRA / NEGRA * NEGRA  # = d
        # tambor: la célula de dos compases, cuatro veces por repetición
        for par in range(4):
            for g in TAMBOR:
                tt = t0 + par * 2 * COMPAS + g * NEGRA
                i = int(SR * tt)
                a = 0.35 * vol * ACENTO[g] * (1.6 if c["tambor_doble"] else 1.0)
                y = golpe(a, rng)
                out[i:i + len(y)] += y
        # medidas por compás, para el cuadro (el rms se calcula después de normalizar,
        # así los números del CSV son los del WAV)
        for k in range(8):
            # altura media de la melodía en ese compás (ponderada por duración)
            pos2 = 0.0; suma = 0.0; peso = 0.0
            for midi, dur in MELODIA:
                ini, fin = pos2, pos2 + dur
                solap = max(0.0, min(fin, 3 * (k + 1)) - max(ini, 3 * k))
                if solap > 0:
                    suma += midi * solap; peso += solap
                pos2 += dur
            compases.append({"compas": rep * 8 + k + 1, "repeticion": rep + 1, "rms": None,
                             "altura_media": round(suma / peso, 2), "voces": nvoces,
                             "_a": int(SR * (t0 + k * COMPAS)), "_b": int(SR * (t0 + (k + 1) * COMPAS))})

    # acorde final: re-la-re-fa, dos segundos, y corte seco
    tf = REPETICIONES * 8 * COMPAS
    i = int(SR * tf)
    acorde = np.zeros(int(SR * 2.0))
    for m, a in [(38, 0.3), (50, 0.3), (57, 0.25), (62, 0.3), (65, 0.25), (74, 0.2)]:
        acorde += voz(m, 2.0, "sierra" if m < 60 else "seno", a)
    acorde *= envolvente(len(acorde), 0.02, 0.02)
    out[i:i + len(acorde)] += acorde

    out = out / np.max(np.abs(out)) * 0.95
    for c in compases:
        seg = out[c.pop("_a"):c.pop("_b")]
        c["rms"] = round(float(np.sqrt(np.mean(seg ** 2))), 4)
    with wave.open(str(AQUI / "2026-11-22_musica.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((out * 32767).astype(np.int16).tobytes())

    # ABC
    nombres = {60: "C", 62: "D", 64: "E", 65: "F", 67: "G", 69: "A", 71: "B", 72: "c"}
    def abc_dur(d):
        return {1: "", 2: "2", 3: "3", 1.5: "3/2", 0.5: "/2"}[d]
    notas = []
    pos = 0
    for midi, dur in MELODIA:
        notas.append(nombres[midi] + abc_dur(dur))
        pos += dur
        if pos % 3 == 0:
            notas.append("|")
    abc = ["X:1", "T:Una música sin oírla (22/11/2026)", "M:3/4", "L:1/4", "Q:1/4=72", "K:Ddor",
           "% la melodía, ocho compases; se repite seis veces sin cambiar",
           " ".join(notas), "",
           "% el tambor, dos compases: negra corchea corchea negra | corchea corchea negra corchea corchea",
           "V:2 clef=perc", "B B/2 B/2 B | B/2 B/2 B B/2 B/2 |"]
    (AQUI / "2026-11-22_musica.abc").write_text("\n".join(abc) + "\n", encoding="utf-8")

    with open(AQUI / "2026-11-22_compases.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(compases[0].keys()))
        w.writeheader(); w.writerows(compases)

    cuadro(compases)
    print("escrito wav, abc, csv, svg;", len(compases), "compases;", f"{tf + 2:.1f} s")

def color_altura(m):
    """Altura media → color. Grave = azul oscuro, agudo = amarillo, pasando por rojo."""
    x = (m - 60) / 12.0  # 0 en do4, 1 en do5
    x = min(1, max(0, x))
    # interpolación en tres puntos
    puntos = [(0.0, (40, 60, 140)), (0.5, (190, 50, 60)), (1.0, (250, 200, 60))]
    for (xa, ca), (xb, cb) in zip(puntos, puntos[1:]):
        if xa <= x <= xb:
            u = (x - xa) / (xb - xa)
            return tuple(int(ca[i] + u * (cb[i] - ca[i])) for i in range(3))
    return puntos[-1][1]

def cuadro(compases):
    """Un rectángulo por compás, en zigzag de ocho por fila (una fila por repetición):
    el largo es el volumen (rms), el color la altura media, la forma cuántas voces
    (1 voz: rectángulo liso; más voces: más esquinas cortadas)."""
    W, H = 820, 620
    mx = max(c["rms"] for c in compases)
    filas = REPETICIONES
    alto_fila = (H - 80) / filas
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
              f'<rect width="{W}" height="{H}" fill="#f4efe4"/>',
              '<text x="20" y="22" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#333">'
              'Una música sin oírla, compás por compás: el largo es el volumen, el color la altura media '
              '(azul grave, amarillo agudo),</text>',
              '<text x="20" y="38" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#333">'
              'las esquinas cortadas cuántas voces. Se lee en zigzag, una fila por repetición, como el cuadro de Adams.</text>']
    for c in compases:
        rep = c["repeticion"] - 1
        k = (c["compas"] - 1) % 8
        col = k if rep % 2 == 0 else 7 - k      # zigzag
        x0 = 20 + col * ((W - 40) / 8)
        ancho = (W - 40) / 8 - 10
        largo = 12 + (alto_fila - 34) * (c["rms"] / mx)
        ybase = 50 + rep * alto_fila + alto_fila - 6
        y0 = ybase - largo
        r, g, b = color_altura(c["altura_media"])
        corte = min(ancho / 3, 2.5 * (c["voces"] - 1))
        if corte <= 0:
            forma = f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{ancho:.1f}" height="{largo:.1f}" fill="rgb({r},{g},{b})"/>'
        else:
            pts = [(x0 + corte, y0), (x0 + ancho - corte, y0), (x0 + ancho, y0 + corte),
                   (x0 + ancho, ybase - corte), (x0 + ancho - corte, ybase), (x0 + corte, ybase),
                   (x0, ybase - corte), (x0, y0 + corte)]
            forma = '<polygon points="' + " ".join(f"{px:.1f},{py:.1f}" for px, py in pts) + f'" fill="rgb({r},{g},{b})"/>'
        partes.append(forma)
        partes.append(f'<text x="{x0 + ancho/2:.1f}" y="{ybase + 12:.1f}" font-family="Helvetica, Arial, sans-serif" '
                      f'font-size="8" fill="#666" text-anchor="middle">{c["compas"]}</text>')
    # la flecha del zigzag
    for rep in range(REPETICIONES):
        y = 50 + rep * alto_fila + alto_fila / 2
        if rep % 2 == 0:
            partes.append(f'<text x="{W - 14}" y="{y:.0f}" font-size="10" fill="#999">→</text>')
        else:
            partes.append(f'<text x="4" y="{y:.0f}" font-size="10" fill="#999">←</text>')
    partes.append("</svg>")
    (AQUI / "2026-11-22_cuadro.svg").write_text("\n".join(partes), encoding="utf-8")

if __name__ == "__main__":
    main()
