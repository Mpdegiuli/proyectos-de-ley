"""Escribe `parentesis.svg`: el paréntesis de apertura como el "upon" del Federalista.

Arriba, al estilo de la tabla 2.3 de Mosteller y Wallace (1963): qué fracción de las respuestas de
cada familia cae en cada franja de tasa de "(" por mil palabras. Abajo, las 36 casas, una por fila,
agrupadas por familia, con su tasa. Lee `tasas_respuesta.json`, que escribe `publius.py`.

Uso:  python3 figura.py [tasas_respuesta.json] [parentesis.svg]
"""
import collections
import json
import sys

ENT = sys.argv[1] if len(sys.argv) > 1 else "tasas_respuesta.json"
SAL = sys.argv[2] if len(sys.argv) > 2 else "parentesis.svg"

SUPERFICIE, TINTA, TINTA2, TINTA3, GRILLA = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8986", "#e6e5e1"
AZUL, NARANJA = "#2a78d6", "#eb6834"          # paleta validada (dataviz/references/palette.md)
COLOR = {"Anthropic": AZUL, "OpenAI": NARANJA}
FUENTE = "font-family='Helvetica, Arial, sans-serif'"

docs = json.load(open(ENT, encoding="utf-8"))
FAMS = ["Anthropic", "OpenAI", "chinas", "Google", "xAI", "Mistral", "Meta", "otras"]


def familia(m):
    m = m.split("/")[-1]
    for p, f in [("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"),
                 ("mistral", "Mistral"), ("muse", "Meta")]:
        if m.startswith(p):
            return f
    if m.split("-")[0] in ("deepseek", "qwen3.8", "glm", "minimax", "mimo", "kimi"):
        return "chinas"
    return "otras"


# ---- panel 1: franjas ----
FRANJAS = [(0, 0, "0"), (0, 2, "0–2"), (2, 4, "2–4"), (4, 6, "4–6"), (6, 8, "6–8"), (8, 12, "8–12"), (12, 1e9, "más de 12")]


def franja(t):
    if t == 0:
        return 0
    for i, (a, b, _) in enumerate(FRANJAS[1:], 1):
        if a < t <= b:
            return i
    return len(FRANJAS) - 1


hist = {f: collections.Counter() for f in ("Anthropic", "OpenAI")}
tot = collections.Counter()
for d in docs:
    f = familia(d["modelo"])
    if f in hist:
        hist[f][franja(d["("])] += 1
        tot[f] += 1

W, H = 920, 1180
out = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>",
       f"<rect width='{W}' height='{H}' fill='{SUPERFICIE}'/>",
       f"<text x='40' y='44' {FUENTE} font-size='20' font-weight='600' fill='{TINTA}'>El paréntesis es el «upon» del repositorio</text>",
       f"<text x='40' y='68' {FUENTE} font-size='13' fill='{TINTA2}'>Tasa del signo «(» por mil palabras en {str(len(docs)).replace(',', '.') if len(docs) < 1000 else str(len(docs))[:-3] + '.' + str(len(docs))[-3:]} respuestas en castellano de 36 casas del repositorio proyectos-de-ley</text>",
       f"<text x='40' y='84' {FUENTE} font-size='13' fill='{TINTA2}'>(corridas leídas por Maia hasta el 23/10/2026; sin el código, sin el SVG y sin las citas de la consigna).</text>",
       f"<text x='40' y='116' {FUENTE} font-size='14' font-weight='600' fill='{TINTA}'>Fracción de las respuestas de cada familia en cada franja de tasa (como la tabla 2.3 de Mosteller y Wallace para «upon»)</text>"]

x0, y0, ancho, alto = 90, 140, 780, 220
out.append(f"<line x1='{x0}' y1='{y0+alto}' x2='{x0+ancho}' y2='{y0+alto}' stroke='{GRILLA}' stroke-width='1'/>")
for p in (25, 50, 75, 100):
    y = y0 + alto - alto * p / 100
    out.append(f"<line x1='{x0}' y1='{y:.1f}' x2='{x0+ancho}' y2='{y:.1f}' stroke='{GRILLA}' stroke-width='1'/>")
    out.append(f"<text x='{x0-8}' y='{y+4:.1f}' {FUENTE} font-size='11' fill='{TINTA3}' text-anchor='end'>{p} %</text>")
paso = ancho / len(FRANJAS)
bw = 24
for i, (_, _, et) in enumerate(FRANJAS):
    cx = x0 + paso * (i + 0.5)
    out.append(f"<text x='{cx:.1f}' y='{y0+alto+18}' {FUENTE} font-size='12' fill='{TINTA2}' text-anchor='middle'>{et}</text>")
    for j, f in enumerate(("Anthropic", "OpenAI")):
        frac = hist[f][i] / tot[f]
        h = alto * frac
        x = cx - bw - 1 if j == 0 else cx + 1          # 2 px de superficie entre las dos barras
        y = y0 + alto - h
        if h > 0:
            r = min(4, h)
            out.append(f"<path d='M{x:.1f},{y0+alto} V{y+r:.1f} Q{x:.1f},{y:.1f} {x+r:.1f},{y:.1f} H{x+bw-r:.1f} Q{x+bw:.1f},{y:.1f} {x+bw:.1f},{y+r:.1f} V{y0+alto} Z' fill='{COLOR[f]}'/>")
        # etiqueta directa solo en los extremos del relato: la franja 0 y la de más de 12
        if i in (0, len(FRANJAS) - 1) or (i == 1 and f == "Anthropic"):
            out.append(f"<text x='{x+bw/2:.1f}' y='{y-5:.1f}' {FUENTE} font-size='11' fill='{TINTA2}' text-anchor='middle'>{100*frac:.0f} %</text>")
out.append(f"<text x='{x0+ancho/2:.1f}' y='{y0+alto+40}' {FUENTE} font-size='12' fill='{TINTA3}' text-anchor='middle'>paréntesis de apertura por mil palabras, en cada respuesta</text>")
# leyenda
lx, ly = x0 + ancho - 250, y0 + 6
for j, f in enumerate(("Anthropic", "OpenAI")):
    out.append(f"<rect x='{lx}' y='{ly + 18*j - 9}' width='12' height='12' rx='2' fill='{COLOR[f]}'/>")
    out.append(f"<text x='{lx+18}' y='{ly + 18*j + 1}' {FUENTE} font-size='12' fill='{TINTA2}'>{f} ({tot[f]} respuestas)</text>")

# ---- panel 2: las casas ----
casas = collections.defaultdict(lambda: [0, 0, 0, 0])   # k, n, docs, docs con
for d in docs:
    c = casas[d["modelo"].split("/")[-1]]
    c[0] += d["k("]
    c[1] += d["n"]
    c[2] += 1
    c[3] += d["k("] > 0
filas = sorted(casas.items(), key=lambda kv: (FAMS.index(familia(kv[0])), -1000 * kv[1][0] / kv[1][1]))
y2 = y0 + alto + 80
out.append(f"<text x='40' y='{y2}' {FUENTE} font-size='14' font-weight='600' fill='{TINTA}'>Las 36 casas, por familia: tasa de «(» por mil palabras</text>")
out.append(f"<text x='40' y='{y2+17}' {FUENTE} font-size='12' fill='{TINTA2}'>(a la derecha, la tasa y cuántas respuestas tienen al menos un paréntesis)</text>")
xa, xb = 300, 800
maxt = 30
top = y2 + 44
fila_h = 15.5
grupos = len({familia(m) for m, _ in filas})
fondo = top + fila_h * len(filas) + 6 * (grupos - 1) + 2
out.append(f"<line x1='{xa}' y1='{top-6}' x2='{xa}' y2='{fondo:.1f}' stroke='{GRILLA}' stroke-width='1'/>")
for t in (0, 5, 10, 15, 20, 25, 30):
    x = xa + (xb - xa) * t / maxt
    out.append(f"<line x1='{x:.1f}' y1='{top-6}' x2='{x:.1f}' y2='{fondo:.1f}' stroke='{GRILLA}' stroke-width='1'/>")
    out.append(f"<text x='{x:.1f}' y='{fondo + 14:.1f}' {FUENTE} font-size='11' fill='{TINTA3}' text-anchor='middle'>{t}</text>")
out.append(f"<text x='{(xa+xb)/2:.1f}' y='{fondo + 30:.1f}' {FUENTE} font-size='12' fill='{TINTA3}' text-anchor='middle'>paréntesis de apertura por mil palabras</text>")
fam_ant = None
y = top
for m, (k, n, nd, ncon) in filas:
    f = familia(m)
    if f != fam_ant:
        if fam_ant is not None:
            y += 6
        out.append(f"<text x='40' y='{y+4:.1f}' {FUENTE} font-size='12' font-weight='600' fill='{TINTA}'>{f if f != 'chinas' else 'chinas'}</text>")
        fam_ant = f
    tasa = 1000 * k / n
    x = xa + (xb - xa) * min(tasa, maxt) / maxt
    out.append(f"<text x='{xa-10}' y='{y+4:.1f}' {FUENTE} font-size='11' fill='{TINTA2}' text-anchor='end'>{m}</text>")
    out.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='6' fill='{SUPERFICIE}'/>")
    out.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='4.5' fill='{COLOR.get(f, TINTA3)}'/>")
    out.append(f"<text x='{xb+12}' y='{y+4:.1f}' {FUENTE} font-size='11' fill='{TINTA2}'>{tasa:.1f} · {ncon}/{nd}</text>")
    y += fila_h
out.append(f"<text x='40' y='{H-30}' {FUENTE} font-size='11' fill='{TINTA3}'>Hamilton usaba «upon» unas 3 veces por mil palabras y Madison 1/6 (Mosteller y Wallace, 1963, p. 278): cociente 18.</text>")
out.append(f"<text x='40' y='{H-14}' {FUENTE} font-size='11' fill='{TINTA3}'>Acá, Anthropic abre 7,2 paréntesis por mil palabras y OpenAI 0,4: cociente 19. Es una coincidencia; lo que no es coincidencia es la forma.</text>")
out.append("</svg>")
open(SAL, "w", encoding="utf-8").write("\n".join(out))
print("escrito", SAL, "filas", len(filas), "H necesaria", y + 60)
