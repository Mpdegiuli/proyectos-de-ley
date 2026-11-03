#!/usr/bin/env python3
"""Cuentas del cuaderno del 3/11/2026: fechas, duraciones en morse, lecturas de ···−−−···,
señales de tres letras que son palíndromos en el tiempo y ambigramas en el papel.
Solo biblioteca estándar."""
from datetime import date
from itertools import product

# --- fechas -----------------------------------------------------------------
HOY = date(2026, 11, 3)
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
for d, que in [(date(1906, 11, 3), "convención de Berlín"), (date(1957, 11, 3), "Sputnik 2"),
               (date(1905, 4, 1), "reglamento alemán"), (date(1908, 7, 1), "entrada en vigor"),
               (date(1909, 6, 10), "Slavonia"), (date(1909, 8, 11), "Arapahoe"),
               (date(1912, 4, 15), "Titanic"), (date(1999, 2, 1), "GMDSS")]:
    print(f"{d.isoformat()} fue {DIAS[d.weekday()]}: {que}; hasta hoy {(HOY - d).days} días")
print()

# --- morse ------------------------------------------------------------------
MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}
LETRAS = [c for c in MORSE if c.isalpha()]

def unidades(simbolos, continuo=False):
    """Duración en unidades (punto = 1, raya = 3, hueco entre elementos = 1, entre letras = 3)."""
    total = 0
    for i, letra in enumerate(simbolos):
        s = MORSE[letra]
        total += sum(1 if e == '.' else 3 for e in s) + (len(s) - 1)
        if i < len(simbolos) - 1:
            total += 1 if continuo else 3
    return total

print("Duración en unidades (punto = 1):")
for s, nota in [("SOS", "con huecos de letra"), ("CQD", ""), ("NC", ""), ("SSSDDD", ""), ("SOE", "")]:
    print(f"  {s:7s} {unidades(s):3d} {nota}")
print(f"  {'SOS':7s} {unidades('SOS', continuo=True):3d} como signo continuo (···−−−···), que es como manda el artículo XVI")
print()

# --- lecturas de ···−−−··· en letras y cifras ---------------------------------
SENAL = "...---..."
def lecturas(resto, pref=""):
    if not resto:
        yield pref
        return
    for c, code in MORSE.items():
        if resto.startswith(code):
            yield from lecturas(resto[len(code):], pref + c)
todas = sorted(set(lecturas(SENAL)))
solo_letras = [t for t in todas if t.isalpha()]
print(f"···−−−··· se puede leer de {len(todas)} maneras con letras y cifras, {len(solo_letras)} solo con letras:")
print("  " + " ".join(solo_letras))
print("  con cifras: " + " ".join(t for t in todas if not t.isalpha()))
print(f"  la más corta: {min(todas, key=len)}; las de tres letras: {[t for t in solo_letras if len(t) == 3]}")
print()

# --- palíndromos en el tiempo y ambigramas en el papel --------------------------
def reverso(code):
    return code[::-1]
pal_tiempo = [c for c in LETRAS if MORSE[c] == reverso(MORSE[c])]
print(f"Letras cuyo morse se lee igual al revés ({len(pal_tiempo)}): {' '.join(pal_tiempo)}")
# Letras mayúsculas de palo seco que dan la misma letra giradas 180 grados.
AMBI = set("HINOSXZ")
pares_giro = {('M', 'W'), ('W', 'M')}  # M y W se intercambian al girar; no las uso
ambas = [c for c in pal_tiempo if c in AMBI]
print(f"De esas, las que además se leen igual giradas 180° en el papel ({len(ambas)}): {' '.join(ambas)}")

# Señal de tres letras XYZ: palíndromo temporal si morse(Z) = reverso(morse(X)) y morse(Y) palíndromo.
inv = {}
for c in LETRAS:
    inv.setdefault(MORSE[c], c)
tres_tiempo = []
for x, y in product(LETRAS, pal_tiempo):
    z = inv.get(reverso(MORSE[x]))
    if z:
        tres_tiempo.append(x + y + z)
tres_ambos = [s for s in tres_tiempo if all(c in AMBI for c in s)]
print(f"Señales de tres letras que son palíndromos en el tiempo: {len(tres_tiempo)}")
print(f"  y además ambigramas giradas 180° en el papel: {len(tres_ambos)}")
print("  " + " ".join(sorted(tres_ambos)))
# De esas, duración como signo continuo y contraste (solo puntos / solo rayas)
print("  duración continua de cada una (unidades):")
for s in sorted(tres_ambos, key=lambda s: unidades(s, True)):
    print(f"    {s} {unidades(s, True):3d}")
