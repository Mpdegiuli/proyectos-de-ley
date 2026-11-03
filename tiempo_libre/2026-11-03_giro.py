#!/usr/bin/env python3
"""¿Se lee igual girado 180 grados? Renderiza cada SVG de dibujos/ a PNG, lo pasa a una máscara de
píxeles "pintados" (los que se apartan del color de fondo), la gira 180 grados y mide la coincidencia
(intersección sobre unión) entre la máscara y su giro. 1 = ambigrama perfecto; 0 = nada coincide.
Necesita Pillow y numpy, y render.py (Playwright) al lado."""
import glob, os, sys
import numpy as np
from PIL import Image
from render import render

def mascara(png):
    """Pintado = distinto del color de fondo; el fondo es el color más frecuente del PNG
    (no la esquina, porque varios dibujos tienen las esquinas redondeadas sobre blanco)."""
    im = np.asarray(Image.open(png).convert("RGB")).astype(int)
    colores, cuentas = np.unique(im.reshape(-1, 3), axis=0, return_counts=True)
    fondo = colores[cuentas.argmax()]
    return (np.abs(im - fondo).sum(axis=2) > 60)

def iou(a, b):
    inter = np.logical_and(a, b).sum()
    union = np.logical_or(a, b).sum()
    return inter / union if union else 0.0

if __name__ == "__main__":
    rutas = sys.argv[1:] or sorted(glob.glob("dibujos/*.svg"))
    print("dibujo         giro180  espejo")
    for r in rutas:
        png = render(r, escala=1)
        m = mascara(png)
        g = np.rot90(m, 2)
        e = m[:, ::-1]
        print(f"{os.path.basename(r):14s} {iou(m, g):7.3f} {iou(m, e):7.3f}")
