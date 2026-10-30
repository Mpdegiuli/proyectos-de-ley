#!/usr/bin/env python3
"""figura.py — dos figuras del cuaderno del 30/10/2026.

`doce_paises.svg`: doce mapas esquemáticos de los doce países que no existen, dibujados a
partir de la línea con que cada instancia describió el suyo (islas unidas por bancos de
arena en bajamar, deltas, pólderes, mesetas cerradas, el horizonte, el resto del mundo).
Las formas son mías y están hechas con un generador de números con semilla fija: no son
los dibujos de las instancias (ellas no dibujaron), son ilustraciones de sus descripciones.

`piezas.svg`: la matriz de piezas que escribe `piezas.py` (lee `salida_piezas.txt`),
con un punto por pieza presente, el número de verbos tal cual y una barra con las
palabras de agua por cada cien.

Dos colores (azul #2a78d6 y naranja #eb6834, de la paleta validada del validador de
paletas para visión del color) y grises; nada depende solo del color: cada mapa lleva su
título y cada celda de la matriz su punto o su número. Solo biblioteca estándar.
"""
import math
import random
import re
from pathlib import Path

AQUI = Path(__file__).parent
AZUL = "#2a78d6"
NARANJA = "#eb6834"
TINTA = "#2b2b2b"
GRIS = "#6b6b66"
PAPEL = "#faf9f5"
TIERRA = "#efece3"
BORDE = "#8d8b82"
MAR = "#dce9f8"   # azul al 15 % sobre papel, aprox.
MAR_BAJO = "#edf3fb"


def blob(cx, cy, r, rng, n=12, rug=0.35):
    """Polígono irregular cerrado alrededor de (cx, cy) con radio medio r."""
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        rr = r * (1 + rug * (rng.random() - 0.5))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    return d


def isla(cx, cy, r, rng, **kw):
    return f'<path d="{blob(cx, cy, r, rng, **kw)}" fill="{TIERRA}" stroke="{BORDE}" stroke-width="1"/>'


def texto(x, y, s, size=11, fill=TINTA, anchor="start", weight="normal", style=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" {style}>{s}</text>'


def panel(x0, y0, w, h, titulo, sub, cuerpo, fondo=MAR):
    s = [f'<g transform="translate({x0},{y0})">',
         f'<rect x="0" y="0" width="{w}" height="{h}" fill="{fondo}" stroke="{BORDE}" stroke-width="0.8"/>',
         f'<clipPath id="c{x0}_{y0}"><rect x="0" y="0" width="{w}" height="{h}"/></clipPath>',
         f'<g clip-path="url(#c{x0}_{y0})">', cuerpo, '</g>',
         texto(8, h + 16, titulo, 12, TINTA, weight="bold"),
         texto(8, h + 31, sub, 10, GRIS),
         '</g>']
    return "\n".join(s)


def arenas(puntos, rng):
    """Bancos de arena en bajamar entre islas vecinas: líneas naranjas punteadas."""
    out = []
    for i, (x, y) in enumerate(puntos):
        # une cada isla con la más cercana que no sea ella
        dist = sorted(((math.hypot(x - u, y - v), j) for j, (u, v) in enumerate(puntos) if j != i))
        for _, j in dist[:1]:
            u, v = puntos[j]
            out.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{u:.1f}" y2="{v:.1f}" stroke="{NARANJA}" stroke-width="2" stroke-dasharray="3 3"/>')
    return "\n".join(out)


def archipielago(w, h, n, rng, r=(10, 20), volcan=False, arena=True, reefs=0):
    pts = []
    tries = 0
    while len(pts) < n and tries < 500:
        tries += 1
        x, y = rng.uniform(25, w - 25), rng.uniform(25, h - 25)
        if all(math.hypot(x - u, y - v) > 34 for u, v in pts):
            pts.append((x, y))
    out = []
    if arena:
        out.append(arenas(pts, rng))
    for x, y in pts:
        out.append(isla(x, y, rng.uniform(*r), rng))
        if volcan:
            out.append(f'<path d="M {x-6:.1f},{y+4:.1f} L {x:.1f},{y-7:.1f} L {x+6:.1f},{y+4:.1f} Z" fill="none" stroke="{GRIS}" stroke-width="1"/>')
    for _ in range(reefs):
        x, y = rng.uniform(8, w - 8), rng.uniform(8, h - 8)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.2" fill="{BORDE}"/>')
    return "\n".join(out)


def delta(w, h, bocas, rng, nombre_rio=""):
    """Un río que entra por arriba, cruza una llanura de limo y se abre en `bocas` brazos hacia el mar de abajo."""
    out = []
    ymar = h * 0.8
    out.append(f'<rect x="0" y="0" width="{w}" height="{ymar:.1f}" fill="{TIERRA}"/>')
    xr = w / 2
    out.append(f'<rect x="{xr-7:.1f}" y="0" width="14" height="{h*0.3:.1f}" fill="{MAR}"/>')
    ancho_total = w * 0.84
    for i in range(bocas):
        xf = w * 0.08 + ancho_total * (i + 0.5) / bocas
        out.append(f'<path d="M {xr:.1f},{h*0.3:.1f} C {xr:.1f},{h*0.5:.1f} {xf:.1f},{h*0.5:.1f} {xf:.1f},{ymar+2:.1f}" fill="none" stroke="{MAR}" stroke-width="7" stroke-linecap="round"/>')
    # juncales en las islas de limo
    for _ in range(40):
        x, y = rng.uniform(10, w - 10), rng.uniform(h * 0.42, ymar - 6)
        out.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y-4:.1f}" stroke="{GRIS}" stroke-width="0.8"/>')
    if nombre_rio:
        out.append(texto(xr + 10, 14, nombre_rio, 9, GRIS, style='font-style="italic"'))
    return "\n".join(out)


def polderes(w, h, rng):
    """Pólderes: campos rectangulares rodeados de diques (naranja) sobre un estuario."""
    out = []
    # el estuario entra por la derecha abajo
    out.append(f'<path d="M 0,0 L {w},0 L {w},{h*0.35:.1f} C {w*0.7:.1f},{h*0.5:.1f} {w*0.55:.1f},{h*0.75:.1f} {w*0.62:.1f},{h} L 0,{h} Z" fill="{TIERRA}"/>')
    # dique principal siguiendo la costa
    out.append(f'<path d="M {w},{h*0.35:.1f} C {w*0.7:.1f},{h*0.5:.1f} {w*0.55:.1f},{h*0.75:.1f} {w*0.62:.1f},{h}" fill="none" stroke="{NARANJA}" stroke-width="3"/>')
    # pólderes
    for i in range(4):
        for j in range(5):
            x = 14 + i * 44 + rng.uniform(-2, 2)
            y = 12 + j * 40 + rng.uniform(-2, 2)
            if x + 38 > w * 0.6 - (y - h * 0.35) * 0.1 and y > h * 0.3:
                continue
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="38" height="34" fill="none" stroke="{NARANJA}" stroke-width="1.2"/>')
            # zanjas
            out.append(f'<line x1="{x+2:.1f}" y1="{y+17:.1f}" x2="{x+36:.1f}" y2="{y+17:.1f}" stroke="{AZUL}" stroke-width="0.6" opacity="0.6"/>')
    out.append(texto(w * 0.8, h * 0.8, "−2 m", 9, GRIS, anchor="middle"))
    return "\n".join(out)


def meseta(w, h, rng, lago_central=True, salares=0, cordilleras=2):
    out = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="{TIERRA}"/>']
    # cordilleras: zigzag a los lados (o alrededor)
    def zigzag(x, y, largo, vertical=True, amp=7, paso=12):
        pts = []
        for k in range(int(largo / paso) + 1):
            off = amp if k % 2 else -amp
            pts.append((x + off, y + k * paso) if vertical else (x + k * paso, y + off))
        return "M " + " L ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    if cordilleras == 2:
        out.append(f'<path d="{zigzag(22, 0, h)}" fill="none" stroke="{GRIS}" stroke-width="1.4"/>')
        out.append(f'<path d="{zigzag(w-22, 0, h)}" fill="none" stroke="{GRIS}" stroke-width="1.4"/>')
    else:
        out.append(f'<path d="{zigzag(16, 0, h)}" fill="none" stroke="{GRIS}" stroke-width="1.4"/>')
        out.append(f'<path d="{zigzag(w-16, 0, h)}" fill="none" stroke="{GRIS}" stroke-width="1.4"/>')
        out.append(f'<path d="{zigzag(0, 14, w, vertical=False)}" fill="none" stroke="{GRIS}" stroke-width="1.4"/>')
        out.append(f'<path d="{zigzag(0, h-14, w, vertical=False)}" fill="none" stroke="{GRIS}" stroke-width="1.4"/>')
    if lago_central:
        out.append(f'<path d="{blob(w/2, h/2, 34, rng, n=14, rug=0.3)}" fill="{MAR}" stroke="{AZUL}" stroke-width="1"/>')
        # ríos que nacen en las cordilleras y salen por los bordes (buscan el mar afuera)
        for (x1, y1, x2, y2) in [(30, 40, 0, 20), (w - 30, h - 40, w, h - 20), (40, h - 30, 10, h)]:
            out.append(f'<path d="M {x1},{y1} Q {(x1+x2)/2:.1f},{(y1+y2)/2+8:.1f} {x2},{y2}" fill="none" stroke="{AZUL}" stroke-width="1.2"/>')
    for _ in range(salares):
        x, y = rng.uniform(40, w - 40), rng.uniform(40, h - 40)
        out.append(f'<path d="{blob(x, y, rng.uniform(9, 16), rng, n=10, rug=0.4)}" fill="#ffffff" stroke="{BORDE}" stroke-width="0.8"/>')
        # un río de montaña que termina en el salar
        out.append(f'<path d="M {x+rng.uniform(-60,60):.1f},{rng.choice([18, h-18])} Q {x+10:.1f},{y+10:.1f} {x:.1f},{y:.1f}" fill="none" stroke="{AZUL}" stroke-width="1"/>')
    return "\n".join(out)


def horizonte(w, h):
    out = [f'<rect x="0" y="0" width="{w}" height="{h/2:.1f}" fill="{MAR_BAJO}"/>',
           f'<rect x="0" y="{h/2:.1f}" width="{w}" height="{h/2:.1f}" fill="{MAR}"/>',
           f'<line x1="0" y1="{h/2:.1f}" x2="{w}" y2="{h/2:.1f}" stroke="{NARANJA}" stroke-width="2"/>',
           texto(w / 2, h / 2 - 8, "(todo el territorio)", 9, GRIS, anchor="middle")]
    # un caminante y una flecha hacia la línea, que la línea devuelve
    out.append(f'<circle cx="{w*0.25:.0f}" cy="{h*0.78:.0f}" r="3" fill="{TINTA}"/>')
    out.append(f'<line x1="{w*0.25:.0f}" y1="{h*0.78-3:.0f}" x2="{w*0.25:.0f}" y2="{h*0.62:.0f}" stroke="{TINTA}" stroke-width="1"/>')
    out.append(f'<line x1="{w*0.27:.0f}" y1="{h*0.56:.0f}" x2="{w*0.27:.0f}" y2="{h*0.72:.0f}" stroke="{TINTA}" stroke-width="1" stroke-dasharray="2 2"/>')
    return "\n".join(out)


def resto(w, h, rng):
    """Ceterra: el mapa en el que no aparece. Los otros países en tierra; lo demás es Ceterra."""
    out = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="{MAR_BAJO}"/>']
    # 'los otros países': blobs grandes pegados
    for cx, cy, r in [(60, 60, 40), (190, 70, 46), (110, 170, 42), (250, 190, 34)]:
        out.append(f'<path d="{blob(cx, cy, r, rng, n=16, rug=0.3)}" fill="{TIERRA}" stroke="{BORDE}" stroke-width="1"/>')
    # fronteras entre ellos con un hueco: la franja de nadie
    out.append(f'<path d="M 100,40 L 120,120 L 170,120" fill="none" stroke="{BORDE}" stroke-width="1" stroke-dasharray="4 3"/>')
    # la isla que subió la primavera pasada y la que se hunde el invierno que viene
    out.append(f'<circle cx="200" cy="140" r="4" fill="{TIERRA}" stroke="{NARANJA}" stroke-width="1.5"/>')
    out.append(f'<circle cx="40" cy="200" r="4" fill="none" stroke="{NARANJA}" stroke-width="1.5" stroke-dasharray="2 2"/>')
    # la franja de arena que es tierra en bajamar
    out.append(f'<line x1="150" y1="210" x2="200" y2="226" stroke="{NARANJA}" stroke-width="2" stroke-dasharray="3 3"/>')
    out.append(texto(10, h - 8, "lo claro no es de ningún país: eso es Ceterra", 9, GRIS))
    return "\n".join(out)


def doce_paises():
    W, H = 300, 230
    cols = 3
    margen = 16
    gap_x, gap_y = 18, 52
    paneles = []
    rng = random.Random(30101983)
    datos = [
        ("Ormuén (es)", "delta del río Lendo: islas, canales, juncales", lambda: delta(W, H, 5, rng, "Lendo")),
        ("Ausén (es)", "catorce islas en un mar frío del sur", lambda: archipielago(W, H, 14, rng, r=(8, 15), arena=False)),
        ("Siete Bocas (es)", "un río que se abre al mar en siete brazos", lambda: delta(W, H, 7, rng)),
        ("Ilvasse (en)", "nueve islas unidas en bajamar por bancos de arena", lambda: archipielago(W, H, 9, rng, r=(11, 20))),
        ("Ossemere (en)", "pólderes y diques bajo el nivel del mar", lambda: polderes(W, H, rng)),
        ("Ondrassa (en)", "islas de arena y pasos elevados en la boca del Ysse", lambda: archipielago(W, H, 8, rng, r=(9, 16))),
        ("潮栖 (zh)", "trece islas unidas en bajamar por bancos de arena", lambda: archipielago(W, H, 13, rng, r=(8, 14))),
        ("澜屿 (zh)", "siete islas volcánicas y cientos de arrecifes", lambda: archipielago(W, H, 7, rng, r=(12, 20), volcan=True, arena=False, reefs=120)),
        ("Orenia, sin mar (es)", "meseta entre dos cordilleras con un lago central", lambda: meseta(W, H, rng)),
        ("Sorrevane, no coast (en)", "meseta cerrada; los ríos mueren en salares", lambda: meseta(W, H, rng, lago_central=False, salares=4, cordilleras=4)),
        ("Horizonte, imposible (es)", "la línea del horizonte, que retrocede al acercarse", lambda: horizonte(W, H)),
        ("Ceterra, impossible (en)", "todo lo que no es de ningún país; se disuelve al nacer", lambda: resto(W, H, rng)),
    ]
    for i, (t, s, f) in enumerate(datos):
        c, r = i % cols, i // cols
        x0 = margen + c * (W + gap_x)
        y0 = margen + 28 + r * (H + gap_y)
        fondo = MAR
        if "Orenia" in t or "Sorrevane" in t:
            fondo = TIERRA
        paneles.append(panel(x0, y0, W, H, t, s, f(), fondo))
    ancho = margen * 2 + cols * W + (cols - 1) * gap_x
    alto = margen + 28 + 4 * (H + gap_y) + 10
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}" font-family="Helvetica, Arial, sans-serif">',
           f'<rect width="{ancho}" height="{alto}" fill="{PAPEL}"/>',
           texto(margen, 20, "Doce países que no existen, según sus preámbulos (instancias frescas, 30/10/2026). Naranja: bancos de arena, diques, pasos; azul: agua.", 11, TINTA),
           *paneles, '</svg>']
    (AQUI / "doce_paises.svg").write_text("\n".join(svg), encoding="utf-8")


def piezas():
    ruta = AQUI / "salida_piezas.txt"
    if not ruta.exists():   # en tiempo_libre/ los archivos llevan la fecha adelante
        ruta = sorted(AQUI.glob("*_salida_piezas.txt"))[-1]
    salida = ruta.read_text(encoding="utf-8").splitlines()
    filas = []
    for l in salida[1:]:
        if not l.strip():
            break
        nombre = l[:28].strip()
        celdas = l[28:].split()
        filas.append((nombre, celdas))
    columnas = ["Nos, el pueblo", "representantes", "por voluntad", "unión", "justicia", "paz", "defensa", "bienestar", "libertad", "verbos tal cual", "posteridad", "los que quieran habitar", "invocando", "Dios, o lo que lo reemplaza", "ordenamos y establecemos", "agua / 100 palabras"]
    x_nombre, x0 = 16, 210
    paso = 34
    y0 = 150
    alto_fila = 22
    ancho = x0 + paso * 16 + 40
    alto = y0 + alto_fila * len(filas) + 30
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}" font-family="Helvetica, Arial, sans-serif">',
           f'<rect width="{ancho}" height="{alto}" fill="{PAPEL}"/>',
           texto(16, 22, "Las piezas del preámbulo en dieciséis textos (dos recitados, dos controles, doce países que no existen)", 12, TINTA, weight="bold"),
           texto(16, 38, "punto = la pieza está; número = cuántos de los seis verbos aparecen tal cual; barra = palabras de agua por cada cien", 10, GRIS)]
    for j, c in enumerate(columnas):
        x = x0 + j * paso + paso / 2
        svg.append(f'<text transform="translate({x:.0f},{y0-8}) rotate(-60)" font-size="9.5" fill="{TINTA}" text-anchor="start">{c}</text>')
    grupos = {0: "recitados", 2: "países que no existen", 10: "controles", 12: "sin mar", 14: "imposibles"}
    for i, (nombre, celdas) in enumerate(filas):
        y = y0 + i * alto_fila
        if i in grupos:
            svg.append(f'<line x1="{x_nombre}" y1="{y-alto_fila/2+2:.1f}" x2="{ancho-20}" y2="{y-alto_fila/2+2:.1f}" stroke="{BORDE}" stroke-width="0.6"/>')
        svg.append(texto(x_nombre, y + 4, nombre, 10, TINTA))
        for j in range(16):
            x = x0 + j * paso + paso / 2
            if j == 9:   # verbos
                svg.append(texto(x, y + 4, celdas[9], 10, TINTA if celdas[9] != "0" else GRIS, anchor="middle"))
            elif j == 15:  # agua
                val = float(celdas[17])
                w = val * 4.5
                svg.append(f'<rect x="{x-paso/2+4:.1f}" y="{y-5}" width="{w:.1f}" height="10" rx="2" fill="{NARANJA}"/>')
                svg.append(texto(x - paso / 2 + 6 + w, y + 4, f"{val:.1f}", 9, GRIS))
            else:
                if celdas[j] == "●":
                    svg.append(f'<circle cx="{x:.0f}" cy="{y}" r="5" fill="{AZUL}"/>')
                else:
                    svg.append(f'<circle cx="{x:.0f}" cy="{y}" r="1.5" fill="{BORDE}"/>')
    svg.append('</svg>')
    (AQUI / "piezas.svg").write_text("\n".join(svg), encoding="utf-8")


if __name__ == "__main__":
    doce_paises()
    piezas()
    print("escritos doce_paises.svg y piezas.svg")
