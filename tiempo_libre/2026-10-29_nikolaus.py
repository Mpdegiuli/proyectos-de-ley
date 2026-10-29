#!/usr/bin/env python3
"""La casa de Nikolaus (el sobre abierto): cuenta los recorridos de un solo trazo y
comprueba los que dibujaron las instancias frescas del 29/10/2026.

Cinco vértices: A y B abajo, D y C arriba, E la punta del techo. Ocho aristas:
el cuadrado (AB, BC, CD, DA), las dos diagonales (AC, BD) y el techo (CE, DE).
Solo biblioteca estándar. Uso: python3 nikolaus.py [instancias_frescas.md]
"""
import re
import sys
from collections import Counter
from itertools import permutations

ARISTAS = ["AB", "BC", "CD", "DA", "AC", "BD", "CE", "DE"]
VERTICES = "ABCDE"


def grado(v):
    return sum(v in a for a in ARISTAS)


def vecinos(v):
    return [a.replace(v, "") for a in ARISTAS if v in a]


def recorridos_desde(v0):
    """Todos los recorridos que usan cada arista exactamente una vez, empezando en v0."""
    hallados = []

    def paso(v, usadas, camino):
        if len(usadas) == len(ARISTAS):
            hallados.append(camino)
            return
        for w in vecinos(v):
            a = "".join(sorted(v + w))
            a = a if a in ARISTAS else a[::-1]
            if a in usadas:
                continue
            paso(w, usadas | {a}, camino + w)

    paso(v0, frozenset(), v0)
    return hallados


def arista_canonica(p, q):
    a = p + q
    return a if a in ARISTAS else q + p


def comprobar(camino):
    """Devuelve (ok, motivo) para un recorrido dado como cadena de vértices."""
    if len(camino) != 9:
        return False, f"{len(camino)} vértices en vez de 9"
    usadas = []
    for p, q in zip(camino, camino[1:]):
        if p == q:
            return False, f"se queda en {p}"
        a = arista_canonica(p, q)
        if a not in ARISTAS:
            return False, f"salta por {p}{q}, que no es una arista"
        if a in usadas:
            return False, f"repite {a}"
        usadas.append(a)
    return True, "las ocho aristas, una vez cada una"


def vertices_de_path(d, coords):
    """Convierte el atributo d de un <path> (solo M y L absolutas) en letras de vértices."""
    nums = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", d)]
    ordenes = re.findall(r"[A-Za-z]", d)
    if ordenes[0] != "M" or any(o != "L" for o in ordenes[1:]):
        return None, f"órdenes {''.join(ordenes)}"
    puntos = list(zip(nums[0::2], nums[1::2]))
    letras = ""
    for p in puntos:
        v = next((k for k, c in coords.items() if c == p), None)
        if v is None:
            return None, f"el punto {p} no es un vértice"
        letras += v
    return letras, None


def main():
    print("Grados:", {v: grado(v) for v in VERTICES})
    impares = [v for v in VERTICES if grado(v) % 2]
    print("Vértices de grado impar:", impares, "-> el trazo empieza en uno y termina en el otro")
    for v0 in VERTICES:
        r = recorridos_desde(v0)
        finales = Counter(c[-1] for c in r)
        print(f"Empezando en {v0}: {len(r)} recorridos", dict(finales) if r else "")
    desde_a = recorridos_desde("A")
    print("\nLos 44 desde A, por primera arista:", dict(Counter(c[:2] for c in desde_a)))
    print("Los 44 desde A, por el momento del techo (índice de la E en el camino):",
          dict(sorted(Counter(c.index("E") for c in desde_a).items())))
    print("Los 44 desde A:")
    for i in range(0, 44, 4):
        print("   ", "  ".join("-".join(c) for c in desde_a[i:i + 4]))

    # Las instancias frescas: coordenadas de la consigna (A(100,300) B(300,300) C(300,100) D(100,100) E(200,20))
    # y las que eligió la instancia 8 (A(100,350) B(300,350) C(300,150) D(100,150) E(200,50)).
    archivo = sys.argv[1] if len(sys.argv) > 1 else "instancias_frescas.md"
    texto = None
    for candidato in (archivo, "2026-10-29_" + archivo):   # suelto al lado, con el prefijo de fecha de tiempo_libre/
        try:
            texto = open(candidato, encoding="utf-8").read()
            break
        except FileNotFoundError:
            continue
    if texto is None:
        print(f"\n(no encontré {archivo}; salto la comprobación de las instancias)")
        return
    paths = re.findall(r'<path d="([^"]+)"', texto)
    print(f"\nInstancias frescas: {len(paths)} elementos <path> en {archivo}")
    c1 = {"A": (100.0, 300.0), "B": (300.0, 300.0), "C": (300.0, 100.0), "D": (100.0, 100.0), "E": (200.0, 20.0)}
    c2 = {"A": (100.0, 350.0), "B": (300.0, 350.0), "C": (300.0, 150.0), "D": (100.0, 150.0), "E": (200.0, 50.0)}
    for i, d in enumerate(paths, 1):
        letras, err = vertices_de_path(d, c1)
        if letras is None:
            letras, err = vertices_de_path(d, c2)
        if letras is None:
            print(f"  path {i}: no se pudo leer ({err})")
            continue
        ok, motivo = comprobar(letras)
        es_de_los_44 = letras in desde_a or letras[::-1] in desde_a
        print(f"  path {i}: {'-'.join(letras)}  ->  {'cumple' if ok else 'NO cumple'}: {motivo}"
              f"{'; es uno de los 44' if es_de_los_44 else ''}")


if __name__ == "__main__":
    main()
