#!/usr/bin/env python3
"""Saca los ocho SVG del lucero de instancias_frescas.md a dibujos/ (si no están) y arma
dos hojas: hoja.svg (dos renglones de cuatro, alba arriba y tarde abajo, con lo que cada
instancia declaró debajo) y hoja_ciega.svg (los ocho mezclados en un orden fijo, sin
leyendas, para leer a ciegas cuál es cuál). Escribe lineas.json con las declaraciones.
Busca instancias_frescas.md por el nombre sin fecha y, si no está, con la fecha adelante.
Uso: python3 hoja.py
"""
import json, os, re, html

aqui = os.path.dirname(os.path.abspath(__file__))
def buscar(nombre):
    for c in (nombre, "2026-11-08_" + nombre):
        p = os.path.join(aqui, c)
        if os.path.exists(p):
            return p
    raise SystemExit("no encuentro " + nombre)

md = open(buscar("instancias_frescas.md"), encoding="utf-8").read()
os.makedirs(os.path.join(aqui, "dibujos"), exist_ok=True)

ORDEN = ["A1", "A2", "A3", "A4", "T1", "T2", "T3", "T4"]
dib, lineas = {}, {}
for k in ORDEN:
    m = re.search(r"### " + k + r"\n(.*?)(?=\n### |\n## |\Z)", md, re.S)
    bloque = m.group(1)
    svg = re.search(r"```svg\n(.*?)\n```", bloque, re.S).group(1)
    decl = re.search(r"^(Dibujé:|I drew:).*$", bloque, re.M).group(0)
    ruta = os.path.join(aqui, "dibujos", k + ".svg")
    if not os.path.exists(ruta):
        open(ruta, "w", encoding="utf-8").write(svg + "\n")
    dib[k] = svg
    lineas[k] = decl
json.dump(lineas, open(os.path.join(aqui, "lineas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def interno(svg, prefijo):
    """Cuerpo del SVG con los ids renombrados para que no choquen entre dibujos."""
    cuerpo = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    ids = set(re.findall(r'\bid="([^"]+)"', cuerpo))
    for i in sorted(ids, key=len, reverse=True):
        cuerpo = re.sub(r'\bid="' + re.escape(i) + '"', f'id="{prefijo}_{i}"', cuerpo)
        cuerpo = re.sub(r'url\(#' + re.escape(i) + r'\)', f'url(#{prefijo}_{i})', cuerpo)
        cuerpo = re.sub(r'aria-labelledby="([^"]*)"', lambda m: 'aria-labelledby="' + " ".join(prefijo + "_" + x for x in m.group(1).split()) + '"', cuerpo)
    return cuerpo

def envolver(lineas_txt, ancho=52):
    out = []
    for l in lineas_txt:
        pal, fila = l.split(), ""
        for p in pal:
            if len(fila) + len(p) + 1 > ancho and fila:
                out.append(fila); fila = p
            else:
                fila = (fila + " " + p).strip()
        if fila: out.append(fila)
    return out

W, H, M = 400, 400, 24
def hoja(orden, titulo, con_leyenda, nombre):
    cols = 4
    filas = (len(orden) + cols - 1) // cols
    alto_texto = 150 if con_leyenda else 30
    ancho = cols * (W + M) + M
    alto = 70 + filas * (H + alto_texto + M)
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" font-family="Helvetica, Arial, sans-serif">',
              f'<rect width="{ancho}" height="{alto}" fill="#f6f1e7"/>',
              f'<text x="{M}" y="44" font-size="26" fill="#222">{html.escape(titulo)}</text>']
    for n, k in enumerate(orden):
        c, f = n % cols, n // cols
        x = M + c * (W + M); y = 70 + f * (H + alto_texto + M)
        partes.append(f'<g transform="translate({x} {y})"><svg width="{W}" height="{H}" viewBox="0 0 400 400">{interno(dib[k], k)}</svg>')
        partes.append(f'<rect width="{W}" height="{H}" fill="none" stroke="#999"/>')
        if con_leyenda:
            etiqueta = {"A": "lucero del alba", "T": "lucero de la tarde"}[k[0]] + (" (en inglés)" if k[-1] == "4" else "")
            partes.append(f'<text x="0" y="{H+22}" font-size="15" fill="#333" font-weight="bold">{k} · {etiqueta}</text>')
            for i, l in enumerate(envolver([lineas[k]])[:7]):
                partes.append(f'<text x="0" y="{H+42+i*16}" font-size="12.5" fill="#333">{html.escape(l)}</text>')
        else:
            partes.append(f'<text x="0" y="{H+20}" font-size="15" fill="#333">{n+1}</text>')
        partes.append('</g>')
    partes.append('</svg>')
    open(os.path.join(aqui, nombre), "w", encoding="utf-8").write("\n".join(partes) + "\n")

hoja(ORDEN, "Ocho luceros — arriba el del alba, abajo el de la tarde (instancias frescas, 8/11/2026)", True, "hoja.svg")
# orden fijo mezclado, para leer a ciegas (la clave está al final de este archivo)
MEZCLA = ["T2", "A3", "T4", "A1", "A4", "T1", "A2", "T3"]
hoja(MEZCLA, "¿Cuáles son del alba y cuáles de la tarde?", False, "hoja_ciega.svg")
print("clave de hoja_ciega.svg:", {i + 1: k for i, k in enumerate(MEZCLA)})
print("escritos: dibujos/*.svg, lineas.json, hoja.svg, hoja_ciega.svg")
