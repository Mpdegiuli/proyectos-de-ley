# campanas.py — tiempo libre 4/10/2026. Solo biblioteca estándar.
# Filas = tuplas de campanas (1..n) en el orden en que suenan. Un "cambio" se escribe con la
# notación de lugares de los campaneros: los lugares que se quedan quietos; el resto de las
# campanas se cruzan de a pares vecinos.
import random
from itertools import permutations
from collections import Counter

def cambio(fila, lugares):
    n = len(fila); f = list(fila); i = 0
    while i < n:
        if (i + 1) in lugares:
            i += 1
        else:
            f[i], f[i + 1] = f[i + 1], f[i]; i += 2
    return tuple(f)

def paridad(fila):
    f = list(fila); p = 0
    for i in range(len(f)):
        while f[i] != i + 1:
            j = f[i] - 1; f[i], f[j] = f[j], f[i]; p ^= 1
    return p

# ---------------------------------------------------------------- caza simple en siete
def caza(n):
    fila = tuple(range(1, n + 1)); filas = [fila]
    a, b = ({n}, {1}) if n % 2 else (set(), {1, n})
    for k in range(2 * n):
        fila = cambio(fila, a if k % 2 == 0 else b); filas.append(fila)
    return filas          # 2n+1 filas: la última repite la primera

def williams(filas):
    n = len(filas[0])
    lugar = Counter((c, i) for f in filas for i, c in enumerate(f))
    sigue = Counter((f[i], f[i + 1]) for f in filas for i in range(n - 1))
    return set(lugar.values()), set(sigue.values()), len(sigue)

if __name__ == "__main__":
    print("== Caza simple ==")
    for n in (4, 5, 6, 7, 8):
        F = caza(n)
        assert F[-1] == F[0] and len(set(F[:-1])) == 2 * n
        l, s, k = williams(F[:-1])
        print(f"n={n}: {2*n} filas; veces que cada campana ocupa cada lugar: {l}; "
              f"veces que cada campana suena justo después de cada otra: {s} ({k} de {n*(n-1)} pares)")
    print("las 14 filas en siete campanas:")
    for f in caza(7)[:-1]:
        print("  ", "".join(map(str, f)))
    # rotación cíclica (la de isla/bucle.py) como comparación
    rot = [tuple((i + r) % 7 + 1 for i in range(7)) for r in range(7)]
    l, s, k = williams(rot)
    print("rotación cíclica en 7 rondas: lugares", l, "; pares 'b justo después de a' que aparecen:", k, "de 42, veces:", s)
