#!/usr/bin/env python3
"""Saca los dibujos de instancias_frescas.md y arma hoja.svg (los 57 en una grilla).

Uso: python3 hoja.py [instancias_frescas.md]
Escribe dibujos/NN.svg (uno por instancia) y hoja.svg. Solo biblioteca estándar.
Los ids internos de cada dibujo (degradados, símbolos) se prefijan con dNN_ para
que no choquen entre sí dentro de la hoja; los dibujos sueltos quedan tal cual.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def buscar(nombre):
    """Busca un archivo por su nombre y, si no está, por el nombre con la fecha adelante."""
    for carpeta in (AQUI, os.getcwd()):
        ruta = os.path.join(carpeta, nombre)
        if os.path.exists(ruta):
            return ruta
        for f in sorted(os.listdir(carpeta)):
            if f.endswith("_" + nombre) and re.match(r"\d{4}-\d{2}-\d{2}", f):
                return os.path.join(carpeta, f)
    raise FileNotFoundError(nombre)


CABECERA = re.compile(r'^### (\d+) — (C\d+), (.+?)\s*$', re.M)


def leer_dibujos(ruta):
    texto = open(ruta, encoding="utf-8").read()
    dibujos = []
    for m in CABECERA.finditer(texto):
        n = int(m.group(1))
        consigna = m.group(2)
        rotulo = m.group(3).strip('"')
        resto = texto[m.end():]
        b = re.search(r"```svg\n(.*?)\n```", resto, re.S)
        if not b:
            continue
        dibujos.append((n, consigna, rotulo, b.group(1).strip()))
    return dibujos


def viewbox(svg):
    m = re.search(r'viewBox="([^"]+)"', svg)
    if not m:
        return 0, 0, 400, 300
    x, y, w, h = [float(v) for v in m.group(1).replace(",", " ").split()]
    return x, y, w, h


def interior(svg):
    """Lo que hay entre <svg ...> y </svg>."""
    m = re.match(r"\s*<svg\b[^>]*>(.*)</svg>\s*$", svg, re.S)
    return m.group(1) if m else svg


def prefijar(cuerpo, pref):
    ids = set(re.findall(r'\bid="([^"]+)"', cuerpo))
    for i in sorted(ids, key=len, reverse=True):
        cuerpo = cuerpo.replace('id="%s"' % i, 'id="%s%s"' % (pref, i))
        cuerpo = cuerpo.replace("url(#%s)" % i, "url(#%s%s)" % (pref, i))
        cuerpo = cuerpo.replace('href="#%s"' % i, 'href="#%s%s"' % (pref, i))
    return cuerpo


ESC = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}


def esc(s):
    return "".join(ESC.get(c, c) for c in s)


def hoja(dibujos, columnas=6, ancho=250, alto=230, margen=12):
    filas = (len(dibujos) + columnas - 1) // columnas
    W = columnas * ancho + 2 * margen
    H = filas * alto + 2 * margen + 30
    partes = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
              'viewBox="0 0 %d %d" width="%d" height="%d">' % (W, H, W, H),
              '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H),
              '<text x="%d" y="22" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#333">'
              'Instancias frescas, 2/11/2026: 57 dibujos, sin contexto, sin herramientas. Número y consigna debajo de cada uno.</text>' % margen]
    for k, (n, consigna, rotulo, svg) in enumerate(dibujos):
        c, f = k % columnas, k // columnas
        x = margen + c * ancho
        y = margen + 30 + f * alto
        vx, vy, vw, vh = viewbox(svg)
        cuerpo = prefijar(interior(svg), "d%02d_" % n)
        partes.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="#dddddd"/>' % (x, y, ancho, alto))
        partes.append('<svg x="%d" y="%d" width="%d" height="%d" viewBox="%g %g %g %g" preserveAspectRatio="xMidYMid meet">%s</svg>'
                      % (x + 8, y + 6, ancho - 16, alto - 34, vx, vy, vw, vh, cuerpo))
        partes.append('<text x="%d" y="%d" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#333">%d · %s</text>'
                      % (x + 8, y + alto - 9, n, esc(rotulo)))
    partes.append("</svg>")
    return "\n".join(partes)


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else buscar("instancias_frescas.md")
    dibujos = leer_dibujos(ruta)
    carpeta = os.path.join(AQUI, "dibujos")
    os.makedirs(carpeta, exist_ok=True)
    for n, consigna, rotulo, svg in dibujos:
        with open(os.path.join(carpeta, "%02d.svg" % n), "w", encoding="utf-8") as f:
            f.write(svg + "\n")
    with open(os.path.join(AQUI, "hoja.svg"), "w", encoding="utf-8") as f:
        f.write(hoja(dibujos))
    print("%d dibujos; dibujos/NN.svg y hoja.svg escritos" % len(dibujos))


if __name__ == "__main__":
    main()
