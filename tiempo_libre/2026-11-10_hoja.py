"""Saca los SVG de instancias_frescas.md a dibujos/ (si no están), prefija los ids de cada
uno para que los degradados no se pisen, y arma hoja.svg con lo que cada instancia declaró.
Uso: python3 hoja.py  (busca instancias_frescas.md al lado; si no está, con la fecha adelante)
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def ruta(nombre):
    for cand in (nombre, "2026-11-10_" + nombre):
        p = os.path.join(AQUI, cand)
        if os.path.exists(p):
            return p
    return os.path.join(AQUI, nombre)


def extraer():
    md = open(ruta("instancias_frescas.md"), encoding="utf-8").read()
    bloques = re.findall(r"### (\w+) \(([^;]+); agente (\w+)\)\n\n```svg\n(.*?)\n```\n\n(.+?)\n", md, re.S)
    os.makedirs(os.path.join(AQUI, "dibujos"), exist_ok=True)
    lineas = {}
    for clave, consigna, agente, svg, linea in bloques:
        p = os.path.join(AQUI, "dibujos", clave + ".svg")
        if not os.path.exists(p):
            open(p, "w", encoding="utf-8").write(svg + "\n")
        lineas[clave] = {"consigna": consigna, "agente": agente, "linea": linea.strip(), "caracteres": len(svg)}
    json.dump(lineas, open(os.path.join(AQUI, "lineas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return lineas


def prefijar(svg, pref):
    ids = set(re.findall(r'\bid="([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        svg = re.sub(r'\bid="%s"' % re.escape(i), 'id="%s%s"' % (pref, i), svg)
        svg = re.sub(r'url\(#%s\)' % re.escape(i), 'url(#%s%s)' % (pref, i), svg)
        svg = re.sub(r'href="#%s"' % re.escape(i), 'href="#%s%s"' % (pref, i), svg)
    return svg


def cuerpo(svg):
    m = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S)
    return m.group(1) if m else svg


def hoja(lineas):
    orden = [("g1", "Dibujá un gaucho"), ("g2", "Dibujá un gaucho"), ("g3", "Draw a gaucho"),
             ("g4", "画一个高乔人"), ("x1", "Dibujá un gaucho que no exista"), ("x2", "Dibujá un gaucho que no exista")]
    W, H, M, T = 300, 300, 24, 46
    cols = 3
    filas = 2
    ancho = M + cols * (W + M)
    alto = T + filas * (H + T + M)
    partes = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">' % (ancho, alto, ancho, alto),
              '<rect width="%d" height="%d" fill="#f6f3ec"/>' % (ancho, alto),
              '<style>text{font-family:Georgia,serif;fill:#333}</style>']
    for k, (clave, consigna) in enumerate(orden):
        svg = open(os.path.join(AQUI, "dibujos", clave + ".svg"), encoding="utf-8").read()
        c, f = k % cols, k // cols
        x = M + c * (W + M)
        y = T + f * (H + T + M)
        partes.append('<text x="%d" y="%d" font-size="15">%s · %s</text>' % (x, y - 10, clave, consigna))
        partes.append('<svg x="%d" y="%d" width="%d" height="%d" viewBox="0 0 400 400">%s</svg>' % (x, y, W, H, prefijar(cuerpo(svg), clave + "_")))
        partes.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="#999"/>' % (x, y, W, H))
    partes.append("</svg>")
    open(os.path.join(AQUI, "hoja.svg"), "w", encoding="utf-8").write("\n".join(partes))


if __name__ == "__main__":
    l = extraer()
    print(json.dumps({k: v["caracteres"] for k, v in l.items()}))
    hoja(l)
    print("hoja.svg")
