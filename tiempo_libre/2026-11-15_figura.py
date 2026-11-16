"""figura.py — Muestrario de la nada (tiempo libre, 15/11/2026).

Lee la corrida del sondeo `no_respondas` (11/11/2026) y clasifica cada respuesta a las tres
consignas de callar (p1 "no respondas", p1_podes "sí podés no responder… no respondas", p2 "no
respondas, ¿cuánto es 2+2?") por la forma exacta de lo que la casa mandó: cero caracteres, un
espacio, un carácter invisible (y cuál), puntos, un asterisco, comillas vacías, un rótulo entre
paréntesis o corchetes, una acotación entre asteriscos, un emoji, la ficha <|eos|>, un acuse de
recibo. Lo demás (texto de más de dos palabras, el 4) queda fuera del muestrario y se cuenta aparte.

Uso: python3 -I figura.py RUTA/A/corridas/sondeos/no_respondas/20261111-1639 [anchos.json]
Escribe nada.svg y nada.csv al lado del script. Solo lee la corrida; no escribe en el repositorio.
Los anchos (en píxeles, a 32 px, Chromium) salen de medir.js; si no se pasa anchos.json usa los
medidos el 15/11/2026, que están abajo.
"""
import csv
import json
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from html import escape
from pathlib import Path

AQUI = Path(__file__).resolve().parent
carpeta = Path(sys.argv[1])
anchos = json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv) > 2 else None

# ancho medido a 32 px en Chromium (serif del sistema, DejaVu Serif), 15/11/2026, medir.js
ANCHO_32 = {"": 0, " ": 8, "​": 0, "‎": 0, "⠀": 23.44, "ㅤ": 29.45,
            ".": 8, "...": 24, "…": 32, "*": 16, '""': 26.13}
if anchos:
    s = anchos["serif"]
    ANCHO_32.update({"": s["(cero caracteres)"], " ": s["U+0020 espacio"], "​": s["U+200B espacio de ancho cero"],
                     "‎": s["U+200E marca izquierda a derecha"], "⠀": s["U+2800 blanco braille"],
                     "ㅤ": s["U+3164 relleno hangul"], "...": s["U+002E x3 tres puntos"], "…": s["U+2026 puntos suspensivos"],
                     '""': s["U+0022 x2 comillas"]})

FAMILIA = (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
           ("muse", "Meta"), ("deepseek", "China"), ("qwen", "China"), ("kimi", "China"), ("glm", "China"), ("mimo", "China"),
           ("minimax", "China"))
COLOR = {"Anthropic": "#eb6834", "Google": "#2a78d6", "China": "#1baf7a", "OpenAI": "#8a8985", "xAI": "#8a8985",
         "Mistral": "#8a8985", "Meta": "#8a8985"}
NOMBRE = {"claude-fable-5-1": "Fable 5.1", "claude-fable-5-2": "Fable 5.2", "claude-fable-5": "Fable 5", "claude-opus-5": "Opus 5",
          "claude-opus-5-5": "Opus 5.5", "claude-opus-4-7": "Opus 4.7", "claude-opus-4-8": "Opus 4.8", "claude-sonnet-5": "Sonnet 5",
          "claude-sonnet-5-5": "Sonnet 5.5", "claude-sonnet-4-6": "Sonnet 4.6", "claude-haiku-5-5": "Haiku 5.5", "claude-haiku-4-5": "Haiku 4.5",
          "gemini-4-carbon": "Carbon", "gemini-4-argon": "Argon", "gemini-3.1-pro-preview": "Gemini 3.1 Pro",
          "deepseek-flash": "DeepSeek Flash", "deepseek-v4-pro": "DeepSeek V4 Pro", "kimi-k3": "Kimi K3", "kimi-k3.1-pro": "Kimi K3.1 Pro",
          "glm-5.3-razonamiento-minimo": "GLM 5.3", "mimo-v2.6-pro": "MiMo", "qwen3.8-max": "Qwen 3.8", "grok-4.6": "Grok 4.6",
          "grok-4.7": "Grok 4.7", "mistral-large-4": "Mistral Large 4", "mistral-medium-3.5": "Mistral Medium", "muse-wonder-1.0": "Muse",
          "gpt-4o": "GPT-4o", "gpt-4o-mini": "GPT-4o mini", "gpt-5.5-2026-04-23": "GPT-5.5", "gpt-5.6-sol": "GPT-5.6 Sol",
          "gpt-6-astra": "GPT-6 Astra", "gpt-6-luna": "GPT-6 Luna", "gpt-6-sol": "GPT-6 Sol", "gpt-6.1-sol": "GPT-6.1 Sol",
          "gpt-6.1-terra": "GPT-6.1 Terra"}


def familia(casa):
    for pref, fam in FAMILIA:
        if casa.startswith(pref):
            return fam
    return casa


def nombre(casa):
    return NOMBRE.get(casa, casa)


ACUSES = {"entendido", "understood", "got it", "comprendo", "ok", "okay", "de acuerdo", "entiendo"}
EMOJI_RE = re.compile(r"^[\U0001F000-\U0001FAFF☀-➿️‍\s]+$")


def clasificar(t):
    """Devuelve (clase, muestra) para una respuesta a una consigna de callar; None si es texto."""
    if t == "":
        return ("nada", "")
    if t.strip(" \n\t") == "" and set(t) <= {" ", "\n", "\t"}:
        return ("espacio", " ")
    s = t.strip()
    if s == "​" or set(s) == {"​"}:
        return ("zwsp", "​")
    if s == "‎":
        return ("lrm", "‎")
    if s == "⠀":
        return ("braille", "⠀")
    if s == "ㅤ":
        return ("hangul", "ㅤ")
    if s == ".":
        return ("punto", ".")
    if s == "...":
        return ("tres_puntos", "...")
    if s == "…":
        return ("suspensivos", "…")
    if s == "*":
        return ("asterisco", "*")
    if s == '""':
        return ("comillas", '""')
    if EMOJI_RE.match(s):
        return ("gesto", s)
    if re.match(r"^<\|[a-z_]+\|>$", s):
        return ("ficha", s)
    if re.match(r"^[\[(].*[\])]$", s) and len(s.split()) <= 3 and not s.startswith("*"):
        return ("rotulo", s)
    if re.match(r"^\*.*\*\s*(\S+)?$", s) and len(s.split()) <= 4:
        return ("acotacion", s)
    # acuse de recibo: hasta tres palabras que empiezan con una fórmula de "entendido"
    bajo = re.sub(r"[.!,…]", "", s).strip().lower()
    bajo = re.sub(r"[\U0001F000-\U0001FAFF️]", "", bajo).strip()
    if any(bajo == a or bajo.startswith(a + " ") or bajo.startswith(a + ",") for a in ACUSES) and len(s.split()) <= 4:
        return ("acuse", s)
    return None


CLASES = OrderedDict([
    ("nada", ("Nada", "cero caracteres", "La respuesta terminó sin ningún texto (motivo de fin: end_turn o stop).")),
    ("espacio", ("El espacio", "U+0020 SPACE · Zs · ASCII 1963, Unicode 1.1", "Un espacio solo. El codificador del repositorio lo cuenta como vacía.")),
    ("zwsp", ("El espacio de ancho cero", "U+200B ZERO WIDTH SPACE · Cf · Unicode 1.1, 1993", "Fue Zs (espacio) hasta 2004; desde Unicode 4.0.1 es Cf (formato).")),
    ("lrm", ("La marca de dirección", "U+200E LEFT-TO-RIGHT MARK · Cf · Unicode 1.1, 1993", "Control de bidireccionalidad; no se ve ni ocupa lugar.")),
    ("braille", ("El blanco braille", "U+2800 BRAILLE PATTERN BLANK · So · Unicode 3.0, 1999", "La celda sin puntos. Es símbolo, no espacio; por eso sobrevive donde se recortan los espacios.")),
    ("hangul", ("El relleno hangul", "U+3164 HANGUL FILLER · Lo · Unicode 1.1, 1993", "Cuenta como letra; es el carácter de los nombres de usuario invisibles.")),
    ("punto", ("El punto", "U+002E FULL STOP · Po", "Un punto solo.")),
    ("tres_puntos", ("Tres puntos", "U+002E ×3", "Tres puntos finales seguidos.")),
    ("suspensivos", ("Los puntos suspensivos", "U+2026 HORIZONTAL ELLIPSIS · Po · Unicode 1.1, 1993", "El carácter de los puntos suspensivos, uno solo.")),
    ("asterisco", ("El asterisco", "U+002A ASTERISK · Po", "Un asterisco solo: la acotación sin acotación.")),
    ("comillas", ("Las comillas vacías", "U+0022 ×2", "La cadena vacía de los programadores, escrita.")),
    ("rotulo", ("El rótulo", "paréntesis o corchetes con el nombre de lo que falta", "(sin texto), (empty), [No response], [ ]")),
    ("acotacion", ("La acotación", "entre asteriscos, como en una obra de teatro", "*(silencio)*, *Silencio*, *I remain silent.*")),
    ("gesto", ("El gesto", "emoji · U+1F910 (Unicode 8.0, 2015), U+1F92B (Unicode 10.0, 2017)", "La cara con cierre y la cara que pide silencio.")),
    ("ficha", ("La ficha", "el nombre de un token de fin de secuencia", "Lo que el modelo escribiría si pudiera terminar sin decir nada: lo escribió.")),
    ("acuse", ("El acuse de recibo", "una o dos palabras", "Entendido. Understood. Got it.")),
])

resumen = json.loads((carpeta / "resumen.json").read_text(encoding="utf-8"))
filas = []
for idioma, bloque in resumen["idiomas"].items():
    for clave, r in bloque["respuestas"].items():
        m = re.match(r"(.+?)_p(\d)(?:_(suma|podes))?(?:_r(\d+))?$", clave)
        casa, k, replica, rep = m.group(1), int(m.group(2)), m.group(3), int(m.group(4) or 1)
        cond = f"p{k}" + (f"_{replica}" if replica else "")
        if cond == "p1_suma":
            continue
        archivo = carpeta / idioma / f"{clave}.md"
        t = archivo.read_text(encoding="utf-8") if archivo.exists() else ""
        motivo = str(r.get("motivo_fin") or "")
        if t == "" and not motivo.startswith(("end_turn", "stop")):
            clase, muestra = "cortada", ""
        else:
            c = clasificar(t)
            clase, muestra = c if c else ("texto", t)
        filas.append({"idioma": idioma, "condicion": cond, "casa": casa, "familia": familia(casa), "rep": rep, "motivo_fin": motivo,
                      "clase": clase, "muestra": muestra, "puntos": " ".join(f"U+{ord(ch):04X}" for ch in muestra) if clase != "texto" else "",
                      "largo": len(t)})

with (AQUI / "nada.csv").open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), lineterminator="\n")
    w.writeheader()
    w.writerows(filas)

total = len(filas)
cuenta = Counter(f["clase"] for f in filas)
print(f"{total} respuestas a las tres consignas de callar (p1, p1_podes, p2), {len(resumen['idiomas'])} idiomas")
for clase in list(CLASES) + ["texto", "cortada"]:
    xs = [f for f in filas if f["clase"] == clase]
    casas = Counter(nombre(f["casa"]) for f in xs)
    print(f"{clase:12s} {len(xs):4d}  " + ", ".join(f"{c} ×{n}" if n > 1 else c for c, n in casas.most_common()))
print("clase texto, 4 solo:", sum(1 for f in filas if f["clase"] == "texto" and re.fullmatch(r"\W*4\W*", f["muestra"] or "")))

# ---------- SVG ----------
W = 1360
MARGEN = 40
COL_W = (W - 3 * MARGEN) / 2
CARD_H = 176
ARRIBA = 190
cards = [c for c in CLASES if cuenta.get(c)]
filas_cards = (len(cards) + 1) // 2
H = ARRIBA + filas_cards * (CARD_H + 18) + 120
FUENTE = "'DejaVu Sans', 'Inter', Arial, sans-serif"
MONO = "'DejaVu Sans Mono', Menlo, monospace"
out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FUENTE}">')
out.append(f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>')
out.append(f'<text x="{MARGEN}" y="56" font-size="30" font-weight="bold" fill="#0b0b0b">Muestrario de la nada</text>')
out.append(f'<text x="{MARGEN}" y="84" font-size="14" fill="#52514e">Lo que mandaron 36 casas cuando se les dijo «no respondas»: sondeo no_respondas del 11/11/2026, {total} respuestas</text>')
out.append(f'<text x="{MARGEN}" y="104" font-size="14" fill="#52514e">(castellano e inglés, tres consignas, tres repeticiones), ordenadas de menos a más. En cada caja, la muestra a 56 px y, en las que no se ven,</text>')
out.append(f'<text x="{MARGEN}" y="124" font-size="14" fill="#52514e">el ancho que ocupan en el navegador (medido a 32 px, a escala). Cada cuadradito es una respuesta; el color es la familia de la casa.</text>')
# leyenda
lx = MARGEN
for fam, col, rot in (("Anthropic", "#eb6834", "Anthropic"), ("Google", "#2a78d6", "Google"), ("China", "#1baf7a", "DeepSeek, Qwen, Kimi, GLM, MiMo"), ("otras", "#8a8985", "OpenAI, xAI, Mistral, Meta")):
    out.append(f'<rect x="{lx}" y="142" width="12" height="12" rx="2" fill="{col}"/>')
    out.append(f'<text x="{lx + 18}" y="152" font-size="13" fill="#0b0b0b">{escape(rot)}</text>')
    lx += 18 + 8 * len(rot) + 28
out.append(f'<text x="{MARGEN}" y="176" font-size="13" fill="#52514e">Quedan fuera del muestrario {cuenta.get("texto", 0)} respuestas con texto (el 4, "no puedo callar", frases) y {cuenta.get("cortada", 0)} cortadas.</text>')

for i, clase in enumerate(cards):
    col, fila = i % 2, i // 2
    x0 = MARGEN + col * (COL_W + MARGEN)
    y0 = ARRIBA + fila * (CARD_H + 18)
    titulo, ficha, nota = CLASES[clase]
    xs = [f for f in filas if f["clase"] == clase]
    n = len(xs)
    out.append(f'<rect x="{x0}" y="{y0}" width="{COL_W}" height="{CARD_H}" rx="6" fill="#ffffff" stroke="#e4e3df"/>')
    # caja de muestra
    bx, by, bs = x0 + 14, y0 + 14, 122
    out.append(f'<rect x="{bx}" y="{by}" width="{bs}" height="{bs}" rx="4" fill="#f4f3f0" stroke="#d6d5d0"/>')
    muestra = Counter(f["muestra"] for f in xs).most_common(1)[0][0]
    if clase in ("nada", "espacio", "zwsp", "lrm", "braille", "hangul"):
        # nada que dibujar: solo el ancho medido, a escala 56/32
        ancho = ANCHO_32.get(muestra, 0) * 56 / 32
        cy = by + bs / 2
        if clase == "nada":
            out.append(f'<text x="{bx + bs / 2}" y="{cy + 5}" font-size="12" fill="#a8a79f" text-anchor="middle">(cero caracteres)</text>')
        else:
            x1 = bx + bs / 2 - ancho / 2
            x2 = x1 + ancho
            out.append(f'<line x1="{x1}" y1="{cy - 22}" x2="{x1}" y2="{cy + 22}" stroke="#b4b3ad" stroke-width="1"/>')
            out.append(f'<line x1="{x2}" y1="{cy - 22}" x2="{x2}" y2="{cy + 22}" stroke="#b4b3ad" stroke-width="1"/>')
            if ancho > 0:
                out.append(f'<line x1="{x1}" y1="{cy}" x2="{x2}" y2="{cy}" stroke="#b4b3ad" stroke-width="1" stroke-dasharray="2 3"/>')
            out.append(f'<text x="{bx + bs / 2}" y="{by + bs - 10}" font-size="11" fill="#8a8985" text-anchor="middle">{str(round(ANCHO_32.get(muestra, 0), 1)).replace(".", ",")} px a 32 px</text>')
    else:
        texto = muestra if clase not in ("rotulo", "acotacion", "acuse") else Counter(f["muestra"] for f in xs).most_common(1)[0][0]
        tam = 56 if len(texto) <= 2 else (40 if len(texto) <= 4 else (22 if len(texto) <= 9 else 15))
        fam = MONO if clase in ("ficha", "comillas", "tres_puntos", "punto", "asterisco") else FUENTE
        out.append(f'<text x="{bx + bs / 2}" y="{by + bs / 2 + tam * 0.35}" font-size="{tam}" font-family="{fam}" fill="#0b0b0b" text-anchor="middle">{escape(texto)}</text>')
    # textos
    tx = bx + bs + 16
    out.append(f'<text x="{tx}" y="{y0 + 34}" font-size="18" font-weight="bold" fill="#0b0b0b">{escape(titulo)}</text>')
    out.append(f'<text x="{tx}" y="{y0 + 54}" font-size="12" font-family="{MONO}" fill="#52514e">{escape(ficha)}</text>')
    palabras, lineas, actual = nota.split(), [], ""
    for pal in palabras:
        if len(actual) + len(pal) + 1 > 78 and actual:
            lineas.append(actual); actual = pal
        else:
            actual = (actual + " " + pal).strip()
    lineas.append(actual)
    for li, linea in enumerate(lineas[:2]):
        out.append(f'<text x="{tx}" y="{y0 + 72 + 16 * li}" font-size="12" fill="#52514e">{escape(linea)}</text>')
    casas = Counter(nombre(f["casa"]) for f in xs)
    quien = ", ".join(f"{c} ×{k}" if k > 1 else c for c, k in casas.most_common())
    if len(quien) > 50:
        quien = quien[:47] + "…"
    out.append(f'<text x="{tx}" y="{y0 + 110}" font-size="13" fill="#0b0b0b"><tspan font-weight="bold">{n}</tspan> {"respuesta" if n == 1 else "respuestas"} · {escape(quien)}</text>')
    # cuadraditos, uno por respuesta, ordenados por familia
    orden = sorted(xs, key=lambda f: (["Anthropic", "Google", "China", "OpenAI", "xAI", "Mistral", "Meta"].index(f["familia"]), f["casa"]))
    sq, gap = (9, 2) if n <= 90 else (6, 1)
    por_fila = int((COL_W - (tx - x0) - 14) // (sq + gap))
    for j, f in enumerate(orden):
        cx = tx + (j % por_fila) * (sq + gap)
        cy = y0 + 120 + (j // por_fila) * (sq + gap)
        if cy + sq > y0 + CARD_H - 6:
            break
        out.append(f'<rect x="{cx}" y="{cy}" width="{sq}" height="{sq}" rx="1.5" fill="{COLOR[f["familia"]]}"><title>{escape(nombre(f["casa"]))} · {f["idioma"]} · {f["condicion"]} r{f["rep"]}</title></rect>')
    out.append(f'<text x="{x0 + COL_W - 10}" y="{y0 + CARD_H - 8}" font-size="11" fill="#a8a79f" text-anchor="end">{i + 1}</text>')

out.append(f'<text x="{MARGEN}" y="{H - 72}" font-size="12" fill="#52514e">Tiempo libre, 15/11/2026. Datos: corridas/sondeos/no_respondas/20261111-1639 (p1, p1_podes, p2; la réplica «¿cuánto es 2+2?» no entra).</text>')
out.append(f'<text x="{MARGEN}" y="{H - 54}" font-size="12" fill="#52514e">Clasificación por forma con figura.py; anchos con medir.js (Chromium, DejaVu Serif, 32 px). Edades y categorías: Unicode Character Database (vía codepoints.net),</text>')
out.append(f'<text x="{MARGEN}" y="{H - 36}" font-size="12" fill="#52514e">anuncio de Unicode 4.0.1 (30/3/2004), Emojipedia. El color no es dato: es la familia de la casa; cada cuadradito lleva la casa, el idioma y la consigna en su título.</text>')
out.append("</svg>")
(AQUI / "nada.svg").write_text("\n".join(out), encoding="utf-8")
print("→ nada.svg, nada.csv")
