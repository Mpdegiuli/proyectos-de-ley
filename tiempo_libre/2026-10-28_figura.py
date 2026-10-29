#!/usr/bin/env python3
"""Escribe marte.svg (las lunas de Swift y las de Hall, a la misma escala) y
lagado.svg (tres marcos del motor, con las ternas que están en el libro marcadas).

Cuaderno de tiempo libre del 28/10/2026. Solo biblioteca estándar.
Uso: python3 figura.py [RUTA_AL_829-0.txt]   (por defecto busca 829-0.txt al lado)
"""
import math
import os
import re
import random
import sys
from collections import Counter, defaultdict

AZUL = "#2563eb"     # las lunas de Swift / lo del libro
NARANJA = "#d97706"  # las lunas reales / la referencia
GRIS = "#6b7280"
TINTA = "#1f2937"
FONDO = "#ffffff"

# ------------------------------------------------------------------ marte.svg
D = 6779.0
D_PX = 30.0                 # un diámetro de Marte en píxeles
R = D_PX / 2
W, H = 980, 450
cx1, cx2 = 245, 735
cy = 240
T_ROT = 24.6229
GM = 4.2828e13
a_sync = (GM * (T_ROT * 3600) ** 2 / (4 * math.pi ** 2)) ** (1 / 3) / 1000 / D   # en diámetros

swift = [("interior", 3.0, "10 h", "sale por el oeste"), ("exterior", 5.0, "21 h 30", "sale por el oeste")]
hall = [("Fobos", 9377.0 / D, "7 h 39", "sale por el oeste"), ("Deimos", 23457.5 / D, "30 h 18", "sale por el este")]

def panel(cx, titulo, sub, lunas, color, estacionaria=False):
    s = []
    s.append(f'<text x="{cx}" y="36" text-anchor="middle" font-size="17" font-weight="600" fill="{TINTA}">{titulo}</text>')
    s.append(f'<text x="{cx}" y="56" text-anchor="middle" font-size="12" fill="{GRIS}">{sub}</text>')
    # órbitas
    for nombre, a, per, lado in lunas:
        r = a * D_PX
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="{color}" stroke-width="1.2"/>')
    if estacionaria:
        r = a_sync * D_PX
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="{AZUL}" stroke-width="1.2" stroke-dasharray="5 4"/>')
        s.append(f'<text x="{cx}" y="{cy + r + 16:.1f}" text-anchor="middle" font-size="11" fill="{AZUL}">órbita estacionaria del Marte real, {a_sync:.2f} diámetros</text>')
    # Marte
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{NARANJA}" fill-opacity="0.25" stroke="{NARANJA}" stroke-width="1.5"/>')
    s.append(f'<text x="{cx}" y="{cy + 4}" text-anchor="middle" font-size="10" fill="{TINTA}">Marte</text>')
    # lunas y etiquetas, en ángulos distintos para que no se pisen
    angulos = [math.radians(-35), math.radians(200)]
    for (nombre, a, per, lado), ang in zip(lunas, angulos):
        r = a * D_PX
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>')
        anchor = "start"
        dx = 8
        s.append(f'<text x="{x+dx:.1f}" y="{y-6:.1f}" text-anchor="{anchor}" font-size="12" font-weight="600" fill="{TINTA}">{nombre}</text>')
        s.append(f'<text x="{x+dx:.1f}" y="{y+8:.1f}" text-anchor="{anchor}" font-size="11" fill="{TINTA}">{a:.2f} diámetros · {per}</text>')
        s.append(f'<text x="{x+dx:.1f}" y="{y+21:.1f}" text-anchor="{anchor}" font-size="11" fill="{GRIS}">{lado}</text>')
    return "\n".join(s)

def marte_svg():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="{FONDO}"/>']
    s.append(panel(cx1, "Marte según los astrónomos de Laputa (Swift, 1726)",
                   "dos satélites a tres y cinco diámetros; diez horas y veintiuna y media", swift, AZUL))
    s.append(panel(cx2, "Marte según Asaph Hall (1877)",
                   "Fobos y Deimos; la misma escala", hall, NARANJA, estacionaria=True))
    s.append(f'<line x1="{W/2}" y1="70" x2="{W/2}" y2="{H-40}" stroke="{GRIS}" stroke-width="0.6" stroke-dasharray="2 4"/>')
    # escala
    s.append(f'<line x1="40" y1="{H-28}" x2="{40 + D_PX:.0f}" y2="{H-28}" stroke="{TINTA}" stroke-width="1.5"/>')
    s.append(f'<text x="{40 + D_PX + 6:.0f}" y="{H-24}" font-size="11" fill="{TINTA}">un diámetro de Marte (6.779 km)</text>')
    s.append(f'<text x="{W-20}" y="{H-24}" text-anchor="end" font-size="11" fill="{GRIS}">La luna interior de Swift, a 3 diámetros, cae a 0,4 % de la órbita en que una luna del Marte real no saldría ni se pondría.</text>')
    s.append("</svg>")
    return "\n".join(s)

# ------------------------------------------------------------------ lagado.svg
def cargar(ruta):
    texto = open(ruta, encoding="utf-8-sig").read()
    ini = texto.find("***START OF THE PROJECT GUTENBERG EBOOK")
    fin = texto.find("***END OF THE PROJECT GUTENBERG EBOOK")
    if ini >= 0 and fin > ini:
        texto = texto[texto.find("\n", ini) + 1:fin]
    texto = re.sub(r"\[Picture:[^\]]*\]", " ", texto).replace("’", "'")
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", texto.lower())

def lagado_svg(ruta, semilla=20261028, filas=6, cols=10):
    random.seed(semilla)
    palabras = cargar(ruta)
    mitad = len(palabras) // 2
    p1, p2 = palabras[:mitad], palabras[mitad:]
    vocab = sorted(set(p1))
    uni = Counter(p1)
    big = defaultdict(Counter)
    for a, b in zip(p1, p1[1:]):
        big[a][b] += 1
    tri = set(zip(p2, p2[1:], p2[2:]))
    uni_pal, uni_pesos = list(uni.keys()), [uni[w] for w in uni]
    big_l = {a: (list(c.keys()), list(c.values())) for a, c in big.items()}

    def fila_cero():
        return [random.choice(vocab) for _ in range(cols)]
    def fila_uno():
        return random.choices(uni_pal, uni_pesos, k=cols)
    def fila_dos():
        out = [random.choices(uni_pal, uni_pesos, k=1)[0]]
        while len(out) < cols:
            a = out[-1]
            if a in big_l:
                ks, vs = big_l[a]
                out.append(random.choices(ks, vs, k=1)[0])
            else:
                out.append(random.choices(uni_pal, uni_pesos, k=1)[0])
        return out

    marcos = [("Orden cero: cada cara, una palabra cualquiera del vocabulario", fila_cero),
              ("Primer orden: cada cara, una palabra con su frecuencia en el libro (el profesor; Shannon, muestra 5)", fila_uno),
              ("Segundo orden: cada palabra según la anterior (Shannon, muestra 6, hecha abriendo un libro al azar)", fila_dos)]
    ancho_celda, alto_celda = 92, 24
    x0, y0 = 30, 30
    W2 = x0 * 2 + cols * ancho_celda
    alto_marco = filas * alto_celda
    H2 = y0 + len(marcos) * (alto_marco + 62) + 10
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" viewBox="0 0 {W2} {H2}" font-family="Helvetica, Arial, sans-serif">',
         f'<rect width="{W2}" height="{H2}" fill="{FONDO}"/>']
    y = y0
    total_marcadas = []
    for titulo, f in marcos:
        s.append(f'<text x="{x0}" y="{y}" font-size="13" font-weight="600" fill="{TINTA}">{titulo}</text>')
        y += 10
        s.append(f'<rect x="{x0}" y="{y}" width="{cols*ancho_celda}" height="{alto_marco}" fill="none" stroke="{GRIS}" stroke-width="1"/>')
        marcadas = 0
        for i in range(filas):
            fila = f()
            # ventanas de tres que están en la segunda mitad del libro
            marca = [False] * cols
            for j in range(cols - 2):
                if (fila[j], fila[j+1], fila[j+2]) in tri:
                    marca[j] = marca[j+1] = marca[j+2] = True
                    marcadas += 1
            for j, w in enumerate(fila):
                cx = x0 + j * ancho_celda
                cy_ = y + i * alto_celda
                if marca[j]:
                    s.append(f'<rect x="{cx+1}" y="{cy_+1}" width="{ancho_celda-2}" height="{alto_celda-2}" fill="{AZUL}" fill-opacity="0.18"/>')
                s.append(f'<line x1="{cx}" y1="{cy_}" x2="{cx}" y2="{cy_+alto_celda}" stroke="{GRIS}" stroke-width="0.4"/>')
                s.append(f'<text x="{cx + ancho_celda/2}" y="{cy_ + 16}" text-anchor="middle" font-size="11" fill="{TINTA}">{w}</text>')
            s.append(f'<line x1="{x0}" y1="{y + i*alto_celda}" x2="{x0 + cols*ancho_celda}" y2="{y + i*alto_celda}" stroke="{GRIS}" stroke-width="0.4"/>')
        total_marcadas.append(marcadas)
        y += alto_marco + 18
        s.append(f'<text x="{x0}" y="{y}" font-size="11" fill="{GRIS}">{marcadas} terna{"s" if marcadas != 1 else ""} de tres palabras seguidas que aparecen tal cual en la segunda mitad del libro (sombreadas)</text>')
        y += 34
    s.append("</svg>")
    return "\n".join(s), total_marcadas

if __name__ == "__main__":
    aqui = os.path.dirname(os.path.abspath(__file__))
    candidatas = [os.path.join(aqui, "829-0.txt"), os.path.join(aqui, "2026-10-28_829-0.txt")]
    ruta = sys.argv[1] if len(sys.argv) > 1 else next((c for c in candidatas if os.path.exists(c)), candidatas[0])
    open(os.path.join(aqui, "marte.svg"), "w", encoding="utf-8").write(marte_svg())
    print("marte.svg escrito")
    if os.path.exists(ruta):
        svg, marcadas = lagado_svg(ruta)
        open(os.path.join(aqui, "lagado.svg"), "w", encoding="utf-8").write(svg)
        print("lagado.svg escrito; ternas marcadas por marco:", marcadas)
    else:
        print("no encontré", ruta, "; lagado.svg no se escribió")
