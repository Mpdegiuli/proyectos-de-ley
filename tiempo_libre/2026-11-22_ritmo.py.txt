#!/usr/bin/env python3
"""Lee los seis dibujos del Boléro hechos por instancias frescas (22/11/2026) y
busca, en los puntos y en los guiones (stroke-dasharray), la célula rítmica del
tambor: dos compases de 3/4, 24 golpes, largo-corto-corto-corto en cada tiempo
salvo el tercer tiempo del primer compás (dos largos) y el tercero del segundo
(dos grupos de tres cortos). En letras: L=largo (corchea), c=corto (tresillo de
semicorcheas):

    compás 1: L ccc L ccc L L          (10 golpes)
    compás 2: L ccc L ccc ccc ccc      (14 golpes)

El script no sabe nada de música: compara secuencias de "grande/chico".
Uso: python3 2026-11-22_ritmo.py [carpeta con los SVG]
"""
import re
import sys
import math
from pathlib import Path

CELULA = "LcccLcccLL" + "LcccLccccccccc"  # 24 golpes
assert len(CELULA) == 24

def puntos_en_circulo(svg):
    """Secuencias de círculos consecutivos (en un mismo <g>) con dos radios distintos,
    ordenados por ángulo alrededor del centro del dibujo si están en anillo, o por x
    si están en fila. Devuelve lista de cadenas L/c."""
    salidas = []
    for g in re.findall(r"<g[^>]*>(.*?)</g>", svg, flags=re.S):
        circs = re.findall(r'<circle cx="([-\d.]+)" cy="([-\d.]+)" r="([-\d.]+)"', g)
        if len(circs) < 8:
            continue
        pts = [(float(x), float(y), float(r)) for x, y, r in circs]
        radios = sorted(set(r for _, _, r in pts))
        if len(radios) != 2:
            continue
        chico, grande = radios
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        # ¿anillo o fila/arco? Si el rango en y es grande, ordenar por ángulo desde el centro.
        cx, cy = 200.0, 200.0
        if max(ys) - min(ys) > 150:
            # ángulo desde arriba (12 en punto), sentido horario
            def ang(p):
                a = math.atan2(p[0] - cx, -(p[1] - cy))
                return a % (2 * math.pi)
            pts = sorted(pts, key=ang)
        else:
            pts = sorted(pts, key=lambda p: p[0])
        salidas.append("".join("L" if r == grande else "c" for _, _, r in pts))
    return salidas

def guiones(svg):
    """stroke-dasharray con más de 8 valores: los guiones (posiciones pares) se leen
    como golpes, largo si es el valor máximo, corto si no."""
    salidas = []
    for da in re.findall(r'stroke-dasharray="([^"]+)"', svg):
        vals = [float(v) for v in da.split()]
        if len(vals) < 8:
            continue
        dashes = vals[0::2]
        mx = max(dashes)
        salidas.append("".join("L" if d == mx else "c" for d in dashes))
    return salidas

def mejor_coincidencia(seq):
    """Compara la secuencia con la célula en todas sus rotaciones y devuelve
    (golpes iguales, largo comparado, rotación)."""
    mejor = (0, 0, 0)
    n = len(seq)
    for rot in range(24):
        cel = (CELULA[rot:] + CELULA[:rot]) * 3
        iguales = sum(1 for a, b in zip(seq, cel) if a == b)
        if iguales > mejor[0]:
            mejor = (iguales, min(n, 24), rot)
    return mejor

def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
    archivos = sorted(carpeta.glob("*dibujo_b_*.svg"))
    print(f"célula del tambor (24 golpes): {CELULA}")
    print()
    for f in archivos:
        svg = f.read_text(encoding="utf-8")
        print(f.name)
        hallado = False
        for seq in puntos_en_circulo(svg):
            ig, n, rot = mejor_coincidencia(seq)
            print(f"  puntos  ({len(seq):2d}): {seq}   coinciden {ig}/{min(len(seq),24)} (rotación {rot})")
            hallado = True
        for seq in guiones(svg):
            ig, n, rot = mejor_coincidencia(seq)
            print(f"  guiones ({len(seq):2d}): {seq}   coinciden {ig}/{min(len(seq),24)} (rotación {rot})")
            hallado = True
        if not hallado:
            print("  sin puntos de dos tamaños ni guiones largos")
        print()

if __name__ == "__main__":
    main()
