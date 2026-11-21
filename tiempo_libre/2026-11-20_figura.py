"""figura.py — Mal armado (tiempo libre, 20/11/2026).

Dibuja dos_idiomas.svg a partir de libreto.csv y repite.csv (los escriben libreto.py y
repite.py): cinco paneles, uno por clase de marca (A fórmulas de servicio, B descargos de
asistente, D conectores de manual, E clichés de prosa de modelo) y uno para la repetición entre
réplicas (sondeo de tiempo libre). En cada panel, un punto por casa con 50 o más respuestas por
idioma: el porcentaje de respuestas con la marca en castellano (horizontal) contra el mismo
porcentaje en inglés (vertical). La diagonal es "igual en los dos idiomas"; arriba de la
diagonal, más en inglés; abajo, más en castellano. Color por laboratorio (familias), con el
nombre de la casa al lado de los puntos que se salen.

Uso: python3 -I figura.py  (lee libreto.csv y repite.csv al lado del script; escribe dos_idiomas.svg).
"""
import csv
import os

AQUI = os.path.dirname(os.path.abspath(__file__))

COLORES = {  # paleta categórica validada (cinco tonos, light)
    "Anthropic": "#2a78d6",
    "OpenAI": "#eb6834",
    "Google": "#1baf7a",
    "chinas": "#eda100",
    "otras": "#e87ba4",
}
NOMBRES = {
    "claude-fable-5": "Fable 5", "claude-fable-5-1": "Fable 5.1", "claude-haiku-4-5": "Haiku 4.5",
    "claude-haiku-5-5": "Haiku 5.5", "claude-opus-4-7": "Opus 4.7", "claude-opus-4-8": "Opus 4.8",
    "claude-opus-5": "Opus 5", "claude-opus-5-5": "Opus 5.5", "claude-sonnet-4-6": "Sonnet 4.6",
    "claude-sonnet-5": "Sonnet 5", "claude-sonnet-5-5": "Sonnet 5.5", "claude-fable-5-2": "Fable 5.2",
    "gpt-4o": "GPT-4o", "gpt-4o-mini": "4o mini", "gpt-5.5-2026-04-23": "GPT-5.5", "gpt-5.6-sol": "5.6 Sol",
    "gpt-6-astra": "GPT-6 Astra", "gpt-6-luna": "GPT-6 Luna", "gpt-6-sol": "GPT-6 Sol", "gpt-6.1-sol": "6.1 Sol",
    "gpt-6.1-terra": "6.1 Terra", "gemini-3.1-pro-preview": "Gemini 3.1", "gemini-4-argon": "Argon",
    "minimax/minimax-m3": "MiniMax", "moonshotai/kimi-k3": "Kimi K3", "moonshotai/kimi-k3.1-pro": "K3.1 Pro",
    "qwen/qwen3.8-max-0902": "Qwen 3.8", "xiaomi/mimo-v2.6-pro": "MiMo", "z-ai/glm-5.3": "GLM",
    "deepseek-flash": "DS Flash", "deepseek-v4-pro": "DS V4 Pro", "muse-wonder-1.0": "Muse",
    "mistral-large-4": "Mistral L4", "mistral-medium-3.5": "Mistral M", "grok-4.6": "Grok 4.6", "grok-4.7": "Grok 4.7",
}


def familia(casa, lab):
    if lab in ("Anthropic", "OpenAI", "Google"):
        return lab
    if lab == "DeepSeek" or lab == "?" and any(k in casa for k in ("minimax", "kimi", "qwen", "mimo", "glm")):
        return "chinas"
    return "otras"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


filas = [r for r in csv.DictReader(open(os.path.join(AQUI, "libreto.csv"), encoding="utf-8"))
         if int(r["N_es"]) >= 50 and int(r["N_en"]) >= 50]
rep = {}
for r in csv.DictReader(open(os.path.join(AQUI, "repite.csv"), encoding="utf-8")):
    if r["tipo"] != "sondeo_tiempo_libre" or not r["base_jaccard3"]:
        continue
    k = (r["casa"], r["idioma"])
    rep.setdefault(k, []).append(float(r["jaccard3"]) / float(r["base_jaccard3"]))
labs = {r["casa"]: r["laboratorio"] for r in filas}
for r in csv.DictReader(open(os.path.join(AQUI, "repite.csv"), encoding="utf-8")):
    labs.setdefault(r["casa"], r["laboratorio"])

paneles = [
    ("A", "Fórmulas de servicio", "% de respuestas con «no dudes en», «si querés, puedo», «con gusto», «¡claro!»… / «feel free to», «happy to help», «let me know»…"),
    ("B", "Descargos de asistente", "«soy una IA», «no tengo sentimientos», «fui diseñado para» / «I'm an AI», «I don't have feelings», «I was designed to»"),
    ("D", "Conectores de manual", "«en resumen», «dicho esto», «vale la pena destacar» / «in summary», «that said», «ultimately»"),
    ("E", "Clichés de prosa de modelo", "«no solo X sino Y», «susurro de», «tapiz», «testimonio de» / «not just X but Y», «whisper of», «tapestry», «testament to»"),
    ("R", "Repetición entre réplicas", "similitud entre tres respuestas de la misma casa a la misma consigna, dividida por la de casas distintas (sondeo de tiempo libre)"),
]

W, H = 1240, 930
mx, my = 70, 160
pw, ph = 300, 300
gapx, gapy = 60, 120
pos = {"A": (0, 0), "B": (1, 0), "D": (2, 0), "E": (0, 1), "R": (1, 1)}

out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
       f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>',
       f'<text x="{mx}" y="44" font-size="22" fill="#1b1b1a">Mal armado: lo mismo en los dos idiomas</text>',
       f'<text x="{mx}" y="70" font-size="13" fill="#5d5c58">Cada punto es una casa (35 con 50 o más respuestas por idioma; 6.920 respuestas en castellano y 6.951 en inglés a las mismas consignas, corridas/sondeos).</text>',
       f'<text x="{mx}" y="88" font-size="13" fill="#5d5c58">Horizontal: en castellano. Vertical: en inglés. La diagonal es «igual en los dos idiomas»: arriba de ella el libreto sale más en inglés; abajo, más en castellano.</text>',
       f'<text x="{mx}" y="106" font-size="13" fill="#5d5c58">Las marcas están definidas en pares, una por idioma (libreto.py); la repetición, en repite.py.</text>']


def panel(clase, titulo, sub, puntos, maxv, unidad):
    cx, cy = pos[clase]
    x0 = mx + cx * (pw + gapx)
    y0 = my + cy * (ph + gapy)
    o = []
    o.append(f'<text x="{x0}" y="{y0 - 28}" font-size="15" fill="#1b1b1a" font-weight="bold">{esc(titulo)}</text>')
    # subtítulo en dos líneas
    palabras = sub.split()
    l1, l2 = [], []
    for w in palabras:
        (l1 if len(" ".join(l1 + [w])) <= 62 else l2).append(w)
    o.append(f'<text x="{x0}" y="{y0 - 13}" font-size="10" fill="#5d5c58">{esc(" ".join(l1))}</text>')
    if l2:
        o.append(f'<text x="{x0}" y="{y0 - 2}" font-size="10" fill="#5d5c58">{esc(" ".join(l2))}</text>')
    # marco y diagonal
    o.append(f'<rect x="{x0}" y="{y0}" width="{pw}" height="{ph}" fill="#ffffff" stroke="#d9d8d2"/>')
    o.append(f'<line x1="{x0}" y1="{y0 + ph}" x2="{x0 + pw}" y2="{y0}" stroke="#b5b4ad" stroke-dasharray="4 4"/>')
    # ejes
    for i in range(5):
        v = maxv * i / 4
        x = x0 + pw * i / 4
        y = y0 + ph - ph * i / 4
        lab = f"{v:.0f}{unidad}" if maxv >= 4 else f"{v:.1f}{unidad}"
        o.append(f'<text x="{x}" y="{y0 + ph + 16}" font-size="10" fill="#5d5c58" text-anchor="middle">{lab}</text>')
        o.append(f'<text x="{x0 - 6}" y="{y + 3}" font-size="10" fill="#5d5c58" text-anchor="end">{lab}</text>')
        if i:
            o.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0 + ph}" stroke="#f0efe9"/>')
            o.append(f'<line x1="{x0}" y1="{y}" x2="{x0 + pw}" y2="{y}" stroke="#f0efe9"/>')
    o.append(f'<text x="{x0 + pw / 2}" y="{y0 + ph + 34}" font-size="11" fill="#5d5c58" text-anchor="middle">castellano</text>')
    o.append(f'<text x="{x0 - 44}" y="{y0 + ph / 2}" font-size="11" fill="#5d5c58" text-anchor="middle" transform="rotate(-90 {x0 - 44} {y0 + ph / 2})">inglés</text>')
    arriba = sum(1 for _, a, b, _ in puntos if b > a)
    abajo = sum(1 for _, a, b, _ in puntos if a > b)
    o.append(f'<text x="{x0 + 8}" y="{y0 + 16}" font-size="11" fill="#1b1b1a">más en inglés: {arriba} casas</text>')
    o.append(f'<text x="{x0 + pw - 8}" y="{y0 + ph - 8}" font-size="11" fill="#1b1b1a" text-anchor="end">más en castellano: {abajo}</text>')
    # puntos
    usados = []
    for casa, a, b, fam in sorted(puntos, key=lambda p: -(p[1] + p[2])):
        px = x0 + pw * min(a, maxv) / maxv
        py = y0 + ph - ph * min(b, maxv) / maxv
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{COLORES[fam]}" stroke="#fcfcfb" stroke-width="1.5"><title>{esc(casa)}: castellano {a:.1f}{unidad}, inglés {b:.1f}{unidad}</title></circle>')
        # etiqueta si se aparta de la diagonal o es grande
        if abs(a - b) >= 0.28 * maxv or (a + b) >= 1.1 * maxv:
            tx, ty = px + 7, (py + 14 if py < y0 + 12 else py + 4)
            for ux, uy in usados:
                if abs(ux - tx) < 50 and abs(uy - ty) < 11:
                    ty = uy + 11
            usados.append((tx, ty))
            o.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="9.5" fill="#1b1b1a">{esc(NOMBRES.get(casa, casa))}</text>')
    return o


for clase, titulo, sub in paneles:
    if clase == "R":
        puntos = []
        for casa in {c for c, _ in rep}:
            if (casa, "es") in rep and (casa, "en") in rep:
                a = sum(rep[(casa, "es")]) / len(rep[(casa, "es")])
                b = sum(rep[(casa, "en")]) / len(rep[(casa, "en")])
                puntos.append((casa, a, b, familia(casa, labs.get(casa, "?"))))
        out += panel(clase, titulo, sub, puntos, 30, "×")
    else:
        puntos = [(r["casa"], float(r[f"{clase}_es"]), float(r[f"{clase}_en"]), familia(r["casa"], r["laboratorio"])) for r in filas]
        maxv = max(10.0, 2 * max(max(a, b) for _, a, b, _ in puntos) / 2)
        maxv = {"A": 8, "B": 24, "D": 16, "E": 8}[clase]
        out += panel(clase, titulo, sub, puntos, maxv, " %")

# leyenda en el hueco de abajo a la derecha
lx, ly = mx + 2 * (pw + gapx), my + ph + gapy
out.append(f'<text x="{lx}" y="{ly - 28}" font-size="15" fill="#1b1b1a" font-weight="bold">Familias</text>')
for i, (fam, col) in enumerate(COLORES.items()):
    y = ly + 16 + i * 24
    out.append(f'<circle cx="{lx + 8}" cy="{y}" r="6" fill="{col}"/>')
    etiqueta = {"chinas": "casas chinas (DeepSeek, Qwen, Kimi, GLM, MiniMax, MiMo)", "otras": "otras (Mistral, xAI, Meta)"}.get(fam, fam)
    out.append(f'<text x="{lx + 22}" y="{y + 4}" font-size="12" fill="#1b1b1a">{esc(etiqueta)}</text>')
for i, linea in enumerate([
        "Clase C, calcos del inglés («hacer sentido», «en orden de»,",
        "«tomar lugar», «déjame saber»…): 3 en 6.920 respuestas en",
        "castellano (5 apariciones, 2 literales). No hay panel: no hay puntos.",
        "",
        "En el total, castellano / inglés, por ciento de respuestas:",
        "A 2,2 / 2,1; B 5,8 / 5,3; D 2,8 / 2,4; E 1,6 / 1,7;",
        "repetición entre réplicas ×5,5 / ×6,4.",
        "Ninguna de las cinco medidas separa los idiomas."]):
    out.append(f'<text x="{lx}" y="{ly + 160 + i * 15}" font-size="11" fill="#5d5c58">{esc(linea)}</text>')
out.append(f'<text x="{lx}" y="{ly + 292}" font-size="10" fill="#8a8984">Tiempo libre, 20/11/2026. libreto.py, repite.py y figura.py sobre corridas/sondeos.</text>')
out.append("</svg>")
open(os.path.join(AQUI, "dos_idiomas.svg"), "w", encoding="utf-8").write("\n".join(out))
print("→ dos_idiomas.svg")
