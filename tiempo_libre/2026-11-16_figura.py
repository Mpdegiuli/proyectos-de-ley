#!/usr/bin/env python3
"""figura.py — la hoja del cuaderno del 16/11/2026: en qué idioma viene el razonamiento guardado de cada casa cuando
se le habla en castellano (panel grande) y cuando se le habla en chino (panel chico). Lee `idioma.csv`, que escribe
`idioma.py --csv`, y escribe `razonan.svg` (y `razonan.png` si está cairosvg). No toca el repositorio.
  python3 figura.py [idioma.csv] [razonan.svg]"""
import collections
import csv
import sys

ENT = sys.argv[1] if len(sys.argv) > 1 else "idioma.csv"
SAL = sys.argv[2] if len(sys.argv) > 2 else "razonan.svg"
COL = {"es": "#2a78d6", "en": "#eb6834", "mixto": "#1baf7a", "zh": "#eda100"}  # fijos, validados (dataviz)
NOMBRE = {"es": "castellano", "en": "inglés", "mixto": "mezcla", "zh": "chino"}
FAM = {"claude": "Anthropic", "grok": "xAI", "mistral": "Mistral", "deepseek": "DeepSeek", "qwen": "Alibaba",
       "kimi": "Moonshot", "glm": "Zhipu", "minimax": "MiniMax", "mimo": "Xiaomi"}
ETIQ = {"claude-fable-5": "Fable 5", "claude-fable-5-1": "Fable 5.1", "claude-fable-5-2": "Fable 5.2",
        "claude-opus-5": "Opus 5", "claude-opus-5-5": "Opus 5.5", "claude-sonnet-5": "Sonnet 5",
        "claude-sonnet-5-5": "Sonnet 5.5", "claude-haiku-5-5": "Haiku 5.5", "grok-4.6": "Grok 4.6",
        "grok-4.7": "Grok 4.7", "mistral-large-4": "Mistral Large 4", "deepseek-v4-pro": "DeepSeek V4 Pro",
        "deepseek-flash": "DeepSeek Flash", "qwen3.8-max": "Qwen 3.8 Max", "kimi-k3": "Kimi K3",
        "kimi-k3.1-pro": "Kimi K3.1 Pro", "glm-5.3-razonamiento-minimo": "GLM 5.3", "minimax-m3": "MiniMax M3",
        "mimo-v2.6-pro": "MiMo V2.6 Pro"}

filas = list(csv.DictReader(open(ENT, encoding="utf-8")))
tab = collections.defaultdict(collections.Counter)
for r in filas:
    if r["clase"] in ("corto", "otro"):
        continue
    tab[(r["casa"], r["consigna"])][r["clase"]] += 1


def fam(casa):
    for k, v in FAM.items():
        if casa.startswith(k):
            return v
    return "otra"


def panel(idioma, x0, y0, ancho, minimo, titulo):
    casas = [c for (c, i) in tab if i == idioma and c in ETIQ and sum(tab[(c, i)].values()) >= minimo]
    # orden: por familia (Anthropic, xAI, Mistral, chinas) y dentro, por parte de inglés descendente
    orden_fam = ["Anthropic", "xAI", "Mistral", "DeepSeek", "Moonshot", "Alibaba", "Zhipu", "MiniMax", "Xiaomi"]
    casas.sort(key=lambda c: (orden_fam.index(fam(c)), -tab[(c, idioma)]["en"] / sum(tab[(c, idioma)].values())))
    out = [f'<text x="{x0}" y="{y0}" class="t">{titulo}</text>']
    y = y0 + 22
    alto = 16
    ult = None
    for c in casas:
        if ult and fam(c) != ult:
            y += 6
        ult = fam(c)
        cnt = tab[(c, idioma)]
        n = sum(cnt.values())
        out.append(f'<text x="{x0 + 128}" y="{y + 12}" class="e" text-anchor="end">{ETIQ[c]}</text>')
        x = x0 + 136
        for k in ("es", "mixto", "zh", "en"):
            if not cnt[k]:
                continue
            w = ancho * cnt[k] / n
            out.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w - 2, 0.5):.1f}" height="{alto}" rx="2" fill="{COL[k]}">'
                       f'<title>{ETIQ[c]}, consigna en {NOMBRE[idioma] if idioma in NOMBRE else idioma}: '
                       f'{cnt[k]} de {n} razonamientos en {NOMBRE[k]}</title></rect>')
            if w > 26:
                out.append(f'<text x="{x + w / 2 - 1:.1f}" y="{y + 12}" class="n" text-anchor="middle">{cnt[k]}</text>')
            x += w
        out.append(f'<text x="{x0 + 136 + ancho + 6}" y="{y + 12}" class="m">{n}</text>')
        y += alto + 3
    return out, y


W = 760
cuerpo, y1 = panel("es", 20, 78, 440, 20, "Se le habla en castellano: idioma del razonamiento guardado")
chico, y2 = panel("zh", 20, y1 + 30, 440, 4, "Se le habla en chino")
H = y2 + 50
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="DejaVu Sans, Helvetica, Arial, sans-serif">',
       '<style>.t{font-size:13px;font-weight:bold;fill:#222}.e{font-size:11px;fill:#222}.n{font-size:9.5px;fill:#fff}'
       '.m{font-size:9.5px;fill:#666}.p{font-size:10.5px;fill:#444}.h{font-size:15px;font-weight:bold;fill:#111}</style>',
       f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>',
       '<text x="20" y="26" class="h">¿En qué idioma pensás? El razonamiento guardado de cada casa</text>',
       '<text x="20" y="42" class="p">corridas/, campo razonamiento; clasificado por palabras funcionales y caracteres CJK (idioma.py); a la derecha, cuántos.</text>',
       '<text x="20" y="55" class="p">Las Claude y los Grok devuelven un resumen hecho aparte, no el razonamiento mismo.</text>']
svg += cuerpo + chico
# leyenda
lx = 20
for k in ("es", "en", "mixto", "zh"):
    svg.append(f'<rect x="{lx}" y="{H - 28}" width="12" height="12" rx="2" fill="{COL[k]}"/>')
    svg.append(f'<text x="{lx + 16}" y="{H - 18}" class="p">{NOMBRE[k]}</text>')
    lx += 90
svg.append(f'<text x="{W - 20}" y="{H - 18}" class="m" text-anchor="end">tiempo libre, 16/11/2026</text>')
svg.append('</svg>')
open(SAL, "w", encoding="utf-8").write("\n".join(svg))
print(SAL, f"{W}x{H}")
try:
    import cairosvg
    cairosvg.svg2png(url=SAL, write_to=SAL.replace(".svg", ".png"), output_width=W * 2)
    print(SAL.replace(".svg", ".png"))
except ImportError:
    print("sin cairosvg: no se hizo el PNG")
