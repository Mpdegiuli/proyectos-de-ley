#!/usr/bin/env python3
"""El paso del gato sobre las teclas.

Mide, en semitonos y en centímetros de teclado, los pasos entre notas sucesivas
de unas cuantas secuencias: el tema de la "fuga del gato" de Scarlatti (K.30),
un tema de Bach, un paseo de gato simulado y una secuencia al azar. Con
--secuencias imprime las cuatro para la prueba a ciegas; con --simular N genera
N paseos de gato y resume la distribución de sus pasos.

Supuestos (son supuestos, no datos):
- Teclado moderno: tecla blanca de 23,5 mm de ancho (octava de 164,5 mm);
  las negras se toman centradas en el límite entre dos blancas (en un piano
  real están corridas unos milímetros; no cambia nada de lo que se mide).
- El gato camina a lo largo del teclado, siempre hacia el mismo lado, y cada
  pata delantera cae a una distancia de la anterior que se sortea de una
  normal de media ZANCADA cm y desvío DESVIO cm (parámetros a la vista).
- Una pata pisa la tecla más cercana a donde cae y, con probabilidad VECINA,
  también la tecla blanca de al lado (la pata es más ancha que la tecla).

Solo biblioteca estándar.
"""
import argparse
import random
import statistics

ANCHO_BLANCA = 2.35  # cm
NOMBRES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ES_BLANCA = [True, False, True, False, True, True, False, True, False, True, False, True]
# posición (en blancas) del semitono dentro de la octava: las blancas en su
# centro, las negras en el límite entre las dos blancas que separan
POS_EN_OCTAVA = [0.5, 1.0, 1.5, 2.0, 2.5, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]


def nombre(midi):
    return f"{NOMBRES[midi % 12]}{midi // 12 - 1}"


def midi_de(nombre_nota):
    """'Bb3' o 'A#3' -> 58. Acepta b y # (y ♭ ♯)."""
    s = nombre_nota.replace('♭', 'b').replace('♯', '#')
    letra = s[0].upper()
    resto = s[1:]
    alt = 0
    while resto and resto[0] in 'b#':
        alt += -1 if resto[0] == 'b' else 1
        resto = resto[1:]
    base = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}[letra]
    octava = int(resto)
    return (octava + 1) * 12 + base + alt


def x_cm(midi):
    """Posición del centro de la tecla, en cm desde el borde izquierdo de C0."""
    octava = midi // 12
    return (octava * 7 + POS_EN_OCTAVA[midi % 12]) * ANCHO_BLANCA


def pasos(midis):
    semis = [b - a for a, b in zip(midis, midis[1:])]
    cms = [x_cm(b) - x_cm(a) for a, b in zip(midis, midis[1:])]
    return semis, cms


def describir(titulo, midis):
    semis, cms = pasos(midis)
    print(f"== {titulo}")
    print("   notas:    ", ' '.join(nombre(m) for m in midis))
    print("   MIDI:     ", ' '.join(str(m) for m in midis))
    print("   semitonos:", ' '.join(f"{s:+d}" for s in semis))
    print("   cm:       ", ' '.join(f"{c:+.1f}" for c in cms))
    abs_cm = [abs(c) for c in cms]
    print(f"   paso medio {statistics.mean(abs_cm):.1f} cm (mediana {statistics.median(abs_cm):.1f}); "
          f"ámbito {x_cm(max(midis)) - x_cm(min(midis)):.1f} cm = {max(midis) - min(midis)} semitonos; "
          f"cambios de dirección: {sum(1 for a, b in zip(cms, cms[1:]) if a * b < 0)}")


def paseo_de_gato(rng, n_pisadas=4, zancada=12.0, desvio=3.0, vecina=0.5, x0=None):
    """Devuelve la lista de teclas (MIDI) que pisa un gato que camina hacia la derecha.

    Cada pisada es un racimo de 1 o 2 teclas blancas vecinas; las notas se
    listan en orden de posición, como las oiría alguien, de izquierda a derecha.
    """
    blancas = [m for m in range(21, 109) if ES_BLANCA[m % 12]]  # A0..C8
    if x0 is None:
        x0 = x_cm(rng.choice([m for m in blancas if 48 <= m <= 60]))
    x = x0
    notas = []
    for _ in range(n_pisadas):
        # tecla blanca más cercana al punto donde cae la pata
        idx = min(range(len(blancas)), key=lambda i: abs(x_cm(blancas[i]) - x))
        racimo = [blancas[idx]]
        if rng.random() < vecina and idx + 1 < len(blancas):
            racimo.append(blancas[idx + 1])
        notas.extend(racimo)
        x += max(2.0, rng.gauss(zancada, desvio))
        if x > x_cm(blancas[-1]):
            break
    return notas


def gato_que_registra(rng, n_pasos=4, paso=10.0, desvio=2.5, vecina=0.5, x0=None):
    """Gato que camina a lo largo del teclado y 'registra': la pata trasera cae
    donde cayó la delantera del mismo lado (lo que las guías de rastreo llaman
    registro directo). Cada pisada delantera abre una tecla nueva (o un racimo
    de dos vecinas); una pisada después, la trasera vuelve a pisar las mismas.
    Devuelve las notas en el orden en que suenan: delantera, delantera,
    trasera (sobre la primera), delantera, trasera (sobre la segunda)...
    Un paso = la distancia entre pisadas delanteras sucesivas (PASO cm).
    """
    blancas = [m for m in range(21, 109) if ES_BLANCA[m % 12]]
    if x0 is None:
        x0 = x_cm(rng.choice([m for m in blancas if 48 <= m <= 60]))
    x = x0
    delanteras = []
    for _ in range(n_pasos):
        idx = min(range(len(blancas)), key=lambda i: abs(x_cm(blancas[i]) - x))
        racimo = [blancas[idx]]
        if rng.random() < vecina and idx + 1 < len(blancas):
            racimo.append(blancas[idx + 1])
        delanteras.append(racimo)
        x += max(2.0, rng.gauss(paso, desvio))
    # orden de los sonidos: D1, D2, T1, D3, T2, D4, T3, T4
    sonidos = []
    for i, racimo in enumerate(delanteras):
        sonidos.extend(racimo)
        if i >= 1:
            sonidos.extend(delanteras[i - 1])
    sonidos.extend(delanteras[-1])
    return sonidos


SCARLATTI = [midi_de(n) for n in 'G3 Bb3 Eb4 F#4 Bb4 C#5 D5'.split()]
BACH_ARTE = [midi_de(n) for n in 'D4 A4 F4 D4 C#4 D4 E4 F4'.split()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--semilla', type=int, default=20261026)
    ap.add_argument('--secuencias', action='store_true', help='imprime las cuatro secuencias de la prueba')
    ap.add_argument('--simular', type=int, default=0, help='simula N paseos y resume los pasos')
    ap.add_argument('--zancada', type=float, default=12.0)
    ap.add_argument('--desvio', type=float, default=3.0)
    ap.add_argument('--vecina', type=float, default=0.5)
    a = ap.parse_args()
    rng = random.Random(a.semilla)

    gato = paseo_de_gato(rng, n_pisadas=5, zancada=a.zancada, desvio=a.desvio, vecina=a.vecina)[:8]
    azar = [rng.randint(48, 84) for _ in range(7)]
    rng2 = random.Random(a.semilla + 1)
    registra = gato_que_registra(rng2, n_pasos=4, paso=10.0, desvio=2.5, vecina=0.5)

    describir("Scarlatti, K.30, tema (como lo recuerdo antes de verificar)", SCARLATTI)
    describir("Bach, Arte de la fuga, tema", BACH_ARTE)
    describir(f"Paseo de gato simulado (semilla {a.semilla}, zancada {a.zancada}±{a.desvio} cm, vecina {a.vecina})", gato)
    describir("Siete notas al azar, uniformes entre C3 y C6", azar)
    describir(f"Gato que registra (semilla {a.semilla + 1}, paso 10±2,5 cm, vecina 0,5): las traseras repiten", registra)

    if a.secuencias:
        print("\n== Para la prueba a ciegas (nombres y MIDI)")
        for k, v in dict(scarlatti=SCARLATTI, bach=BACH_ARTE, gato=gato, azar=azar, registra=registra).items():
            print(f"   {k:9s} {' '.join(nombre(m) for m in v):44s} {v}")

    if a.simular:
        todos = []
        for _ in range(a.simular):
            r = paseo_de_gato(rng, n_pisadas=5, zancada=a.zancada, desvio=a.desvio, vecina=a.vecina)
            s, _c = pasos(r)
            todos.extend(abs(x) for x in s)
        print(f"\n== {a.simular} paseos simulados: {len(todos)} pasos")
        for lim in (2, 4, 7, 12):
            print(f"   pasos de hasta {lim:2d} semitonos: {100 * sum(1 for t in todos if t <= lim) / len(todos):5.1f} %")
        print(f"   paso medio {statistics.mean(todos):.1f} semitonos; máximo {max(todos)}")


if __name__ == '__main__':
    main()
