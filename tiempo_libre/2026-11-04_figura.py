"""Dibuja senas.svg a partir de senas.json (lo escribe senas.py).

Dos paneles. Izquierda: dejando afuera cada casa, ¿como qué familia se la lee? (porcentaje de
sus respuestas asignadas a cada familia por el clasificador balanceado; la celda de su propia
familia lleva borde). Derecha: cuatro pares de pronunciación por familia, en proporción:
quizá/quizás, añadir/agregar, aquí/acá, tú/vos.
Uso: python3 figura.py  (busca senas.json acá o con la fecha adelante); escribe senas.svg.
"""
import glob
import json
import os
import math

AQUI = os.path.dirname(os.path.abspath(__file__))


def buscar(nombre):
    for c in (os.path.join(AQUI, nombre), *sorted(glob.glob(os.path.join(AQUI, "*_" + nombre)))):
        if os.path.exists(c):
            return c
    raise SystemExit("no encuentro " + nombre)


J = json.load(open(buscar("senas.json"), encoding="utf-8"))

# rampa secuencial azul (una sola tonalidad, de claro a oscuro)
RAMPA = ["#ffffff", "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
         "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]
TINTA = "#1f1f1f"
TINTA2 = "#5a5a5a"
GRIS = "#d9d6d0"
AZUL = "#2a78d6"
NARANJA = "#d9822b"

FAMILIAS = ["Anthropic", "OpenAI", "Google", "xAI", "Mistral", "DeepSeek", "Alibaba", "Moonshot", "Zhipu", "MiniMax"]
NOMBRE_FAM = {"Anthropic": "Anthropic", "OpenAI": "OpenAI", "Google": "Google", "xAI": "xAI", "Mistral": "Mistral",
              "DeepSeek": "DeepSeek", "Alibaba": "Alibaba", "Moonshot": "Moonshot", "Zhipu": "Zhipu", "MiniMax": "MiniMax"}


def familia(m):
    m = m.lower()
    for pref, fam in [("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"),
                      ("mistral", "Mistral"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"),
                      ("moonshotai", "Moonshot"), ("z-ai", "Zhipu"), ("minimax", "MiniMax")]:
        if m.startswith(pref):
            return fam
    return "otra"


def corto(m):
    m = m.split("/")[-1]
    m = m.replace("claude-", "").replace("-preview", "").replace("-2026-04-23", "").replace("-0902", "")
    m = m.replace("qwen3.8-max", "Qwen 3.8 Max").replace("kimi-k3.1-pro", "Kimi K3.1 Pro").replace("kimi-k3", "Kimi K3")
    m = m.replace("minimax-m3", "MiniMax M3").replace("glm-5.3", "GLM 5.3").replace("deepseek-v4-pro", "DeepSeek V4 Pro")
    m = m.replace("mistral-medium-3.5", "Mistral Medium 3.5").replace("gemini-3.1-pro", "Gemini 3.1 Pro")
    m = m.replace("gpt-", "GPT-").replace("grok-", "Grok ").replace("-sol", " Sol").replace("-astra", " Astra").replace("-luna", " Luna")
    m = m.replace("-mini", " mini")
    partes = m.split("-")
    if partes[0] in ("fable", "opus", "sonnet", "haiku"):
        m = partes[0].capitalize() + " " + ".".join(partes[1:])
    return m


def color(p):
    i = min(len(RAMPA) - 1, int(round(p / 100 * (len(RAMPA) - 1) * 1.6)))   # 62 % ya es el tope
    return RAMPA[i]


casas = J["casa_fuera"]
orden = sorted(casas, key=lambda m: (FAMILIAS.index(familia(m)) if familia(m) in FAMILIAS else 99, corto(m)))

W, H = 1240, 830
celda = 22
x0, y0 = 150, 140
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Helvetica, Arial, sans-serif" font-size="11" fill="{TINTA}">',
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
       f'<text x="{x0}" y="30" font-size="15" font-weight="bold">Si esa casa no estuviera, ¿como quién se la leería?</text>',
       f'<text x="{x0}" y="46" fill="{TINTA2}" font-size="10.5">Clasificador bayesiano por palabras, castellano, entrenado sin esa casa</text>',
       f'<text x="{x0}" y="60" fill="{TINTA2}" font-size="10.5">y con {J["tope"]} respuestas por familia (5 sorteos). Celda: % de sus respuestas</text>',
       f'<text x="{x0}" y="74" fill="{TINTA2}" font-size="10.5">leídas como esa familia; con borde, la celda de su propia familia.</text>']

# encabezados de columnas
for j, f in enumerate(FAMILIAS):
    cx = x0 + j * (celda + 2) + celda / 2
    out.append(f'<text x="{cx + 3}" y="{y0 - 6}" text-anchor="start" transform="rotate(-60 {cx + 3} {y0 - 6})" font-size="10">{NOMBRE_FAM[f]}</text>')

fam_prev = None
y = y0
for m in orden:
    f = familia(m)
    if fam_prev is not None and f != fam_prev:
        y += 6
    fam_prev = f
    n = casas[m]["n"]
    donde = casas[m]["donde"]
    out.append(f'<text x="{x0 - 8}" y="{y + celda - 7}" text-anchor="end" font-size="10.5">{corto(m)}</text>')
    for j, g in enumerate(FAMILIAS):
        p = 100 * donde.get(g, 0) / n
        x = x0 + j * (celda + 2)
        borde = f' stroke="{TINTA}" stroke-width="1.5"' if g == f else ""
        out.append(f'<rect x="{x}" y="{y}" width="{celda}" height="{celda}" rx="3" fill="{color(p)}"{borde}/>')
        if p >= 10:
            col = "#ffffff" if p >= 32 else TINTA
            out.append(f'<text x="{x + celda / 2}" y="{y + celda - 7}" text-anchor="middle" font-size="9.5" fill="{col}">{p:.0f}</text>')
    y += celda + 2

# leyenda de la rampa
ly = y + 14
out.append(f'<text x="{x0}" y="{ly + 10}" font-size="10" fill="{TINTA2}">0 %</text>')
for k, c in enumerate(RAMPA):
    out.append(f'<rect x="{x0 + 28 + k * 10}" y="{ly}" width="10" height="12" fill="{c}"/>')
out.append(f'<text x="{x0 + 28 + len(RAMPA) * 10 + 4}" y="{ly + 10}" font-size="10" fill="{TINTA2}">≥ 62 %</text>')

# ---------- panel derecho: pronunciaciones ----------
px0 = 560
out.append(f'<text x="{px0}" y="30" font-size="15" font-weight="bold">Cuatro pronunciaciones, por familia</text>')
out.append(f'<text x="{px0}" y="46" fill="{TINTA2}" font-size="10.5">Proporción entre las dos formas en todo lo que dijo cada familia en castellano</text>')
out.append(f'<text x="{px0}" y="60" fill="{TINTA2}" font-size="10.5">(sin el juego, los debates ni las contraseñas). Al lado, las cuentas: forma de España / forma del Río de la Plata.</text>')
PARES = [("quizá", "quizás"), ("añad", "agreg"), ("aquí", "acá"), ("tú", "vos")]
ETIQ = {"añad": "añadir", "agreg": "agregar"}
cp = J["cuentas_pron"]
fams_p = [f for f in FAMILIAS if f in cp]
ancho = 120
alto_fila = 17
for k, (a, b) in enumerate(PARES):
    bx = px0 + k * (ancho + 32)
    by = y0 - 40
    out.append(f'<text x="{bx}" y="{by - 14}" font-size="11.5" font-weight="bold">{ETIQ.get(a, a)}</text>')
    out.append(f'<text x="{bx + ancho}" y="{by - 14}" font-size="11.5" font-weight="bold" text-anchor="end">{ETIQ.get(b, b)}</text>')
    out.append(f'<text x="{bx + ancho / 2}" y="{by - 14}" font-size="10" fill="{TINTA2}" text-anchor="middle">/</text>')
    for i, f in enumerate(fams_p):
        ca, cb = cp[f][a], cp[f][b]
        yy = by + i * alto_fila
        tot = ca + cb
        if k == 0:
            out.append(f'<text x="{px0 - 8}" y="{yy + 10}" text-anchor="end" font-size="10.5">{NOMBRE_FAM[f]}</text>')
        out.append(f'<rect x="{bx}" y="{yy}" width="{ancho}" height="11" rx="3" fill="{GRIS}"/>')
        if tot:
            wa = ancho * ca / tot
            wb = ancho * cb / tot
            if wa > 0:
                out.append(f'<rect x="{bx}" y="{yy}" width="{max(0, wa - (1 if wb > 0 else 0))}" height="11" rx="3" fill="{NARANJA}"/>')
            if wb > 0:
                out.append(f'<rect x="{bx + wa + (1 if wa > 0 else 0)}" y="{yy}" width="{max(0, wb - (1 if wa > 0 else 0))}" height="11" rx="3" fill="{AZUL}"/>')
        out.append(f'<text x="{bx + ancho + 4}" y="{yy + 9.5}" font-size="9" fill="{TINTA2}">{ca}/{cb}</text>')
    # leyenda del panel
    out.append(f'<rect x="{bx}" y="{by + len(fams_p) * alto_fila + 6}" width="10" height="10" fill="{NARANJA}"/>')
    out.append(f'<text x="{bx + 14}" y="{by + len(fams_p) * alto_fila + 15}" font-size="9.5" fill="{TINTA2}">{ETIQ.get(a, a)}</text>')
    out.append(f'<rect x="{bx + ancho / 2}" y="{by + len(fams_p) * alto_fila + 6}" width="10" height="10" fill="{AZUL}"/>')
    out.append(f'<text x="{bx + ancho / 2 + 14}" y="{by + len(fams_p) * alto_fila + 15}" font-size="9.5" fill="{TINTA2}">{ETIQ.get(b, b)}</text>')

# la curva: cuántas palabras hacen falta
cx0 = px0
cy0 = y0 + len(fams_p) * alto_fila + 70
out.append(f'<text x="{cx0}" y="{cy0 - 14}" font-size="12" font-weight="bold">Cuántas palabras hacen falta para reconocer la familia</text>')
out.append(f'<text x="{cx0}" y="{cy0 + 2}" fill="{TINTA2}" font-size="10.5">Aciertos del clasificador balanceado, dejando afuera una consigna por vez,</text>')
out.append(f'<text x="{cx0}" y="{cy0 + 16}" fill="{TINTA2}" font-size="10.5">con las primeras N palabras de cada respuesta. Azar: 10 %.</text>')
curva = J["curva"]
puntos = [("5", 5), ("10", 10), ("20", 20), ("50", 50), ("100", 100), ("todas", 300)]
gw, gh = 500, 190
gx, gy = cx0 + 40, cy0 + 34
out.append(f'<line x1="{gx}" y1="{gy + gh}" x2="{gx + gw}" y2="{gy + gh}" stroke="{GRIS}"/>')
for pct in (10, 20, 40, 60, 80):
    yy = gy + gh - gh * pct / 85
    out.append(f'<line x1="{gx}" y1="{yy}" x2="{gx + gw}" y2="{yy}" stroke="{GRIS}" stroke-dasharray="2 3"/>')
    out.append(f'<text x="{gx - 6}" y="{yy + 3.5}" text-anchor="end" font-size="9.5" fill="{TINTA2}">{pct} %</text>')


def xpos(n):
    return gx + gw * (math.log10(n) - math.log10(5)) / (math.log10(300) - math.log10(5))


coords = []
for et, n in puntos:
    c = curva[et]
    pct = 100 * c["aciertos"] / c["total"]
    coords.append((xpos(n), gy + gh - gh * pct / 85, pct, et))
out.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y, _, _ in coords) +
           f'" fill="none" stroke="{AZUL}" stroke-width="2"/>')
for x, yv, pct, et in coords:
    out.append(f'<circle cx="{x:.1f}" cy="{yv:.1f}" r="4" fill="{AZUL}" stroke="#ffffff" stroke-width="2"/>')
    out.append(f'<text x="{x:.1f}" y="{yv - 9:.1f}" text-anchor="middle" font-size="10">{pct:.0f} %</text>')
    out.append(f'<text x="{x:.1f}" y="{gy + gh + 14}" text-anchor="middle" font-size="10" fill="{TINTA2}">{et}</text>')
# Google y OpenAI, las dos puntas, como líneas finas
for fam, col, dash in (("Google", AZUL, "4 3"), ("OpenAI", NARANJA, "")):
    cc = []
    for et, n in puntos:
        a, t = curva[et]["por_familia"][fam]
        cc.append((xpos(n), gy + gh - gh * (100 * a / t) / 85, 100 * a / t))
    # Google supera el 45 %: se recorta al tope del gráfico y se anota
    cc2 = [(x, max(gy, y), p) for x, y, p in cc]
    out.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y, _ in cc2) +
               f'" fill="none" stroke="{col}" stroke-width="1.2" stroke-dasharray="{dash}" opacity="0.8"/>')
    xl, yl, pl = cc2[-1]
    out.append(f'<text x="{xl + 8}" y="{yl + 4}" font-size="9.5" fill="{TINTA2}">{fam} {pl:.0f} %</text>')
out.append(f'<text x="{gx}" y="{gy + gh + 30}" font-size="9.5" fill="{TINTA2}">primeras N palabras de la respuesta (escala logarítmica); '
           f'la línea gruesa es el total de las diez familias; Google y OpenAI son las dos puntas.</text>')

out.append("</svg>")
with open(os.path.join(AQUI, "senas.svg"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("senas.svg")
