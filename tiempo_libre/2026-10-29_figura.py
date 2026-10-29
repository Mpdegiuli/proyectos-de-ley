#!/usr/bin/env python3
"""Dos figuras del cuaderno del 29/10/2026.

cinco_trazos.svg: los cuatro recorridos de un solo trazo que dibujaron las instancias frescas
  (numerados en el orden en que se recorren las ocho aristas) y, en el quinto panel, la casa con el
  grado de cada vértice y la cuenta de los 44 recorridos.
biromes.svg: por casa, metros de línea y metros de pintura por dibujo (de tinta.csv), en dos
  paneles con un eje cada uno; solo las casas con cinco dibujos o más.

Solo biblioteca estándar. Uso: python3 figura.py [tinta.csv]
Colores: azul #2a78d6 y naranja #eb6834 (validados para visión del color) y grises; nada depende
solo del color: cada barra lleva su número y cada recorrido sus numeritos.
"""
import csv
import sys
from collections import defaultdict

AZUL, NARANJA, GRIS, TINTA, SUAVE = "#2a78d6", "#eb6834", "#8a8a8a", "#222", "#d8d8d8"
FUENTE = "font-family='Helvetica, Arial, sans-serif'"

# Las cuatro instancias frescas (ver instancias_frescas.md y salida_nikolaus.txt)
RECORRIDOS = [
    ("A-B-C-D-A-C-E-D-B", "1. castellano, con coordenadas"),
    ("A-D-E-C-D-B-C-A-B", "2. inglés, con coordenadas"),
    ("A-B-C-E-D-C-A-D-B", "3. castellano, con coordenadas"),
    ("A-B-C-A-D-E-C-D-B", "4. castellano, sin coordenadas"),
]
V = {"A": (40, 190), "B": (200, 190), "C": (200, 30), "D": (40, 30), "E": (120, -40)}
GRADO = {"A": 3, "B": 3, "C": 4, "D": 4, "E": 2}


def panel_trazo(recorrido, titulo, ox, oy):
    letras = recorrido.split("-")
    s = [f"<g transform='translate({ox},{oy})'>"]
    s.append(f"<text x='120' y='-70' text-anchor='middle' font-size='11' fill='{TINTA}' {FUENTE}>{titulo}</text>")
    # las ocho aristas, finas y grises, debajo
    for a, b in ("AB", "BC", "CD", "DA", "AC", "BD", "CE", "DE"):
        (x1, y1), (x2, y2) = V[a], V[b]
        s.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{SUAVE}' stroke-width='6' stroke-linecap='round'/>")
    pts = " ".join(f"{V[l][0]},{V[l][1]}" for l in letras)
    s.append(f"<polyline points='{pts}' fill='none' stroke='{AZUL}' stroke-width='2.5' stroke-linejoin='round' stroke-linecap='round'/>")
    # numeritos en el orden del recorrido, corridos hacia un lado para que no se pisen en las diagonales
    for i, (a, b) in enumerate(zip(letras, letras[1:]), 1):
        (x1, y1), (x2, y2) = V[a], V[b]
        # en las diagonales el numerito va a un tercio del camino, para que no caiga en el cruce
        t = 0.3 if {a, b} in ({"A", "C"}, {"B", "D"}) else 0.5
        mx, my = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        # desplazamiento perpendicular, distinto según el sentido para que las dos diagonales no coincidan
        dx, dy = x2 - x1, y2 - y1
        n = (dx * dx + dy * dy) ** 0.5
        px, py = -dy / n * 11, dx / n * 11
        s.append(f"<circle cx='{mx+px:.1f}' cy='{my+py:.1f}' r='7.5' fill='white' stroke='{GRIS}' stroke-width='0.8'/>")
        s.append(f"<text x='{mx+px:.1f}' y='{my+py+3.5:.1f}' text-anchor='middle' font-size='10' fill='{TINTA}' {FUENTE}>{i}</text>")
    x0, y0 = V[letras[0]]
    xf, yf = V[letras[-1]]
    s.append(f"<circle cx='{x0}' cy='{y0}' r='5' fill='{AZUL}'/>")
    s.append(f"<circle cx='{xf}' cy='{yf}' r='5' fill='white' stroke='{AZUL}' stroke-width='2.5'/>")
    for l, (x, y) in V.items():
        dx = -14 if l in "AD" else (14 if l in "BC" else 0)
        dy = 16 if l in "AB" else (-10 if l in "CD" else -12)
        s.append(f"<text x='{x+dx}' y='{y+dy}' text-anchor='middle' font-size='11' fill='{GRIS}' {FUENTE}>{l}</text>")
    s.append("</g>")
    return "\n".join(s)


def panel_grados(ox, oy):
    s = [f"<g transform='translate({ox},{oy})'>"]
    s.append(f"<text x='120' y='-70' text-anchor='middle' font-size='11' fill='{TINTA}' {FUENTE}>5. el grado de cada vértice</text>")
    for a, b in ("AB", "BC", "CD", "DA", "AC", "BD", "CE", "DE"):
        (x1, y1), (x2, y2) = V[a], V[b]
        s.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{GRIS}' stroke-width='2'/>")
    for l, (x, y) in V.items():
        impar = GRADO[l] % 2 == 1
        s.append(f"<circle cx='{x}' cy='{y}' r='13' fill='{NARANJA if impar else 'white'}' stroke='{NARANJA if impar else GRIS}' stroke-width='2'/>")
        s.append(f"<text x='{x}' y='{y+4}' text-anchor='middle' font-size='12' font-weight='bold' fill='{'white' if impar else TINTA}' {FUENTE}>{GRADO[l]}</text>")
    s.append(f"<text x='120' y='225' text-anchor='middle' font-size='10.5' fill='{TINTA}' {FUENTE}>dos vértices impares (naranja): el trazo</text>")
    s.append(f"<text x='120' y='239' text-anchor='middle' font-size='10.5' fill='{TINTA}' {FUENTE}>empieza en uno y termina en el otro</text>")
    s.append(f"<text x='120' y='256' text-anchor='middle' font-size='10.5' fill='{TINTA}' {FUENTE}>44 recorridos desde A, 44 desde B, 0 desde C, D o E</text>")
    s.append("</g>")
    return "\n".join(s)


def cinco_trazos():
    W, H = 1300, 400
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>",
         f"<rect width='{W}' height='{H}' fill='white'/>",
         f"<text x='20' y='24' font-size='13' fill='{TINTA}' {FUENTE}>La casa de un solo trazo: cuatro instancias frescas (29/10/2026) y el porqué</text>"]
    for i, (rec, tit) in enumerate(RECORRIDOS):
        s.append(panel_trazo(rec, tit, 30 + i * 255, 110))
    s.append(panel_grados(30 + 4 * 255, 110))
    s.append(f"<text x='20' y='{H-12}' font-size='10' fill='{GRIS}' {FUENTE}>Punto lleno: empieza; punto vacío: termina. Los números dicen en qué orden se recorre cada arista. Las cuatro cumplen y son cuatro de los 44 recorridos posibles desde A.</text>")
    s.append("</svg>")
    return "\n".join(s)


def biromes(ruta_csv):
    filas = list(csv.DictReader(open(ruta_csv, encoding="utf-8")))
    por_casa = defaultdict(list)
    for r in filas:
        por_casa[r["casa"]].append(r)
    casas = [(c, rs) for c, rs in por_casa.items() if len(rs) >= 5]
    datos = []
    for c, rs in casas:
        t = sum(float(r["trazo_birome_m"]) for r in rs) / len(rs)
        p = sum(float(r["relleno_birome_m"]) for r in rs) / len(rs)
        datos.append((c, len(rs), t, p))
    datos.sort(key=lambda d: -d[2])
    fila_h = 15
    top = 70
    W = 900
    H = top + fila_h * len(datos) + 40
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>",
         f"<rect width='{W}' height='{H}' fill='white'/>",
         f"<text x='20' y='24' font-size='13' fill='{TINTA}' {FUENTE}>Cuánta birome gasta cada casa, por dibujo (885 dibujos; casas con cinco o más; ordenadas por la línea)</text>",
         f"<text x='20' y='42' font-size='10.5' fill='{GRIS}' {FUENTE}>Línea: largo de todo lo que tiene stroke, en pasadas de 0,4 mm. Pintura: área de todo lo que tiene fill, rayada a 0,4 mm. Lienzo de 10,6 cm; una birome son 3 km.</text>"]
    x_nom = 20
    x1, w1 = 210, 230     # panel de línea
    x2, w2 = 560, 300     # panel de pintura
    max_t = max(d[2] for d in datos)
    max_p = max(d[3] for d in datos)
    esc_t = w1 / 4.5
    esc_p = w2 / 70
    s.append(f"<text x='{x1}' y='{top-8}' font-size='11' fill='{AZUL}' font-weight='bold' {FUENTE}>metros de línea por dibujo</text>")
    s.append(f"<text x='{x2}' y='{top-8}' font-size='11' fill='{NARANJA}' font-weight='bold' {FUENTE}>metros de pintura por dibujo</text>")
    for v in (1, 2, 3, 4):
        x = x1 + v * esc_t
        s.append(f"<line x1='{x:.1f}' y1='{top}' x2='{x:.1f}' y2='{top + fila_h*len(datos)}' stroke='{SUAVE}' stroke-width='0.6'/>")
        s.append(f"<text x='{x:.1f}' y='{top + fila_h*len(datos) + 14}' text-anchor='middle' font-size='9.5' fill='{GRIS}' {FUENTE}>{v} m</text>")
    for v in (20, 40, 60):
        x = x2 + v * esc_p
        s.append(f"<line x1='{x:.1f}' y1='{top}' x2='{x:.1f}' y2='{top + fila_h*len(datos)}' stroke='{SUAVE}' stroke-width='0.6'/>")
        s.append(f"<text x='{x:.1f}' y='{top + fila_h*len(datos) + 14}' text-anchor='middle' font-size='9.5' fill='{GRIS}' {FUENTE}>{v} m</text>")
    for i, (c, n, t, p) in enumerate(datos):
        y = top + i * fila_h + fila_h / 2
        s.append(f"<text x='{x_nom}' y='{y+3.5:.1f}' font-size='10' fill='{TINTA}' {FUENTE}>{c}</text>")
        s.append(f"<text x='{x1-6}' y='{y+3.5:.1f}' text-anchor='end' font-size='9' fill='{GRIS}' {FUENTE}>{n}</text>")
        bt = t * esc_t
        s.append(f"<rect x='{x1}' y='{y-4:.1f}' width='{bt:.1f}' height='8' rx='2' fill='{AZUL}'/>")
        s.append(f"<text x='{x1+bt+5:.1f}' y='{y+3.5:.1f}' font-size='9.5' fill='{TINTA}' {FUENTE}>{t:.2f}</text>")
        bp = p * esc_p
        s.append(f"<rect x='{x2}' y='{y-4:.1f}' width='{bp:.1f}' height='8' rx='2' fill='{NARANJA}'/>")
        s.append(f"<text x='{x2+bp+5:.1f}' y='{y+3.5:.1f}' font-size='9.5' fill='{TINTA}' {FUENTE}>{p:.0f}</text>")
    s.append(f"<text x='{x1-6}' y='{top-8}' text-anchor='end' font-size='9' fill='{GRIS}' {FUENTE}>n</text>")
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    open("cinco_trazos.svg", "w", encoding="utf-8").write(cinco_trazos())
    print("cinco_trazos.svg")
    ruta = sys.argv[1] if len(sys.argv) > 1 else "tinta.csv"
    for candidato in (ruta, "2026-10-29_" + ruta):   # suelto al lado, con el prefijo de fecha de tiempo_libre/
        try:
            open("biromes.svg", "w", encoding="utf-8").write(biromes(candidato))
            print("biromes.svg")
            break
        except FileNotFoundError:
            continue
    else:
        print(f"(no encontré {ruta}; biromes.svg no se escribió)")
