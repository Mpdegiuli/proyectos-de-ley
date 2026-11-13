#!/usr/bin/env python3
"""Figura del cuaderno del 13/10/2026: las tres letras de Claudio hechas con tres
operaciones de SVG (rotate, scale, clip-path) sobre un alfabeto de palo seco dibujado
a mano con líneas y arcos (no usa ninguna fuente para las letras romanas).
Cada letra se define una vez en <defs> y se llama con <use>; las de Claudio son
<use href="#F" transform="rotate(180 ...)">, <use href="#C" transform="... scale(-1 1)">
y <use href="#H" clip-path="url(#mitad)">.

Uso: python3 figura.py  -> escribe tres_letras.svg (y tres_letras.png si hay cairosvg)
"""

# Cada letra: (ancho, lista de trazos) en una caja de alto 100, y hacia abajo.
G = {
    "A": (60, ["M0,100 L30,0 L60,100", "M11,64 H49"]),
    "C": (74, ["M76,20 A42,50 0 1 0 76,80"]),
    "D": (58, ["M0,0 V100", "M0,0 H12 A46,50 0 0 1 12,100 H0"]),
    "E": (48, ["M48,0 H0 V100 H48", "M0,50 H38"]),
    "F": (48, ["M48,0 H0 V100", "M0,50 H38"]),
    "G": (76, ["M76,20 A42,50 0 1 0 76,80", "M76,80 V56 H56"]),
    "H": (56, ["M0,0 V100", "M56,0 V100", "M0,50 H56"]),
    "I": (8, ["M4,0 V100"]),
    "L": (44, ["M0,0 V100 H44"]),
    "M": (72, ["M0,100 V0 L36,72 L72,0 V100"]),
    "N": (56, ["M0,100 V0 L56,100 V0"]),
    "O": (68, ["M34,0 A34,50 0 1 0 34,100 A34,50 0 1 0 34,0"]),
    "P": (50, ["M0,100 V0 H24 A25,25 0 0 1 24,50 H0"]),
    "Q": (68, ["M34,0 A34,50 0 1 0 34,100 A34,50 0 1 0 34,0", "M44,78 L70,106"]),
    "R": (54, ["M0,100 V0 H24 A25,25 0 0 1 24,50 H0", "M24,50 L54,100"]),
    "S": (52, ["M48,16 C38,-5 2,-3 2,26 C2,50 50,48 50,76 C50,105 10,103 2,84"]),
    "T": (58, ["M0,0 H58", "M29,0 V100"]),
    "V": (60, ["M0,0 L30,100 L60,0"]),
}
ESP = 17          # separación entre letras
TINTA = "#2b2a28"
ROJO = "#b23a2a"
GRIS = "#8a8478"
FONDO = "#f6f2e9"


def defs():
    """Cada letra se define una sola vez; después se la llama con <use>."""
    out = ['<defs>']
    for letra, (w, ps) in G.items():
        out.append(f'<path id="{letra}" d="{" ".join(ps)}"/>')
    hw = G["H"][0] / 2
    out.append(f'<clipPath id="mitad"><rect x="-10" y="-10" width="{hw + 10:g}" height="120"/></clipPath>')
    out.append('</defs>')
    return "".join(out)


def claudiana(cual):
    """Las tres letras se hacen con las de siempre y una operación."""
    if cual == "Ⅎ":      # F con media vuelta
        w = G["F"][0]
        return w, f'transform="rotate(180 {w / 2:g} 50)"', "F"
    if cual == "Ↄ":      # C en el espejo
        w = G["C"][0]
        return w, f'transform="translate({w} 0) scale(-1 1)"', "C"
    if cual == "Ⱶ":      # la mitad izquierda de la H
        return G["H"][0] / 2, 'clip-path="url(#mitad)"', "H"
    raise ValueError(cual)


_n = [0]


def linea(texto, x, y, alto, color=TINTA, grosor=7.0, rojo=ROJO):
    """Escribe `texto` con la esquina superior izquierda en (x, y)."""
    k = alto / 100.0
    out, cx = [], 0.0
    for ch in texto:
        if ch == " ":
            cx += 34
            continue
        if ch in "ℲↃⱵ":
            w, op, base = claudiana(ch)
            out.append(f'<g transform="translate({cx:g} 0)" stroke="{rojo}"><use href="#{base}" {op}/></g>')
        else:
            w = G[ch][0]
            out.append(f'<use href="#{ch}" x="{cx:g}"/>')
        cx += w + ESP
    ancho = (cx - ESP) * k
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({k:g})" fill="none" stroke="{color}" '
            f'stroke-width="{grosor:g}" stroke-linecap="round" stroke-linejoin="round">{"".join(out)}</g>'), ancho


def t(x, y, s, size=15, color=TINTA, anchor="start", mono=False, bold=False, italic=False):
    fam = "ui-monospace, Menlo, Consolas, monospace" if mono else "Georgia, 'Times New Roman', serif"
    extra = (' font-weight="bold"' if bold else "") + (' font-style="italic"' if italic else "")
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" fill="{color}" '
            f'text-anchor="{anchor}"{extra}>{s}</text>')


def main():
    W, H = 1040, 1120
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         f'aria-label="Las tres letras de Claudio hechas con tres operaciones de SVG">',
         f'<rect width="{W}" height="{H}" fill="{FONDO}"/>', defs()]
    o.append(t(40, 46, "Tres letras, tres operaciones", 26, bold=True))
    o.append(t(40, 70, "Las letras que Claudio agregó al alfabeto (47/48–54), hechas con las de siempre y una operación de SVG cada una.", 14, GRIS))

    # --- Panel A
    col = [70, 400, 730]
    datos = [
        ("F", "Ⅎ", 'transform="rotate(180)"', "digamma inversum", "para la u consonante (VIR, ARVALES)",
         "en las piedras: 55 veces en 18 inscripciones"),
        ("C", "Ↄ", 'transform="scale(-1,1)"', "antisigma", "para bs y ps, como la psi griega",
         "en las piedras: ninguna vez"),
        ("H", "Ⱶ", 'clip-path (la mitad izquierda)', "media H", "para la ípsilon griega (y)",
         "en las piedras: 12 ejemplos seguros"),
    ]
    y0 = 105
    for x, (a, b, attr, nombre, uso, piedra) in zip(col, datos):
        s, wa = linea(a, x, y0, 100, TINTA, 8)
        o.append(s)
        s, wb = linea(b, x + 150, y0, 100, ROJO, 8)
        o.append(s)
        o.append(f'<path d="M{x + 78},{y0 + 50} H{x + 128}" stroke="{GRIS}" stroke-width="2" fill="none"/>'
                 f'<path d="M{x + 128},{y0 + 50} l-9,-5 v10 z" fill="{GRIS}"/>')
        o.append(t(x, y0 + 132, attr, 14, TINTA, mono=True))
        o.append(t(x, y0 + 156, nombre, 16, ROJO, bold=True))
        o.append(t(x, y0 + 176, uso, 13.5, TINTA))
        o.append(t(x, y0 + 196, piedra, 13.5, GRIS, italic=True))
    o.append(f'<line x1="40" y1="325" x2="{W - 40}" y2="325" stroke="{GRIS}" stroke-width="0.8"/>')

    # --- Panel B
    o.append(t(40, 356, "Lo que está grabado", 19, bold=True))
    yb = 380
    s, w = linea("AMPLIAℲIT TERMINAℲITQ", 40, yb, 44, grosor=8)
    o.append(s)
    o.append(t(40 + w + 22, yb + 20, "cipos del pomerio de Roma, año 49", 13.5))
    o.append(t(40 + w + 22, yb + 38, "(CIL VI 1231)", 13.5, GRIS))
    yb += 84
    s, w = linea("ℲOℲEMVS  VOℲIMVS  VOVIMVS", 40, yb, 40, grosor=8.5)
    o.append(s)
    o.append(t(40 + w + 22, yb + 20, "actas de los hermanos Arvales:", 13.5))
    o.append(t(40 + w + 22, yb + 38, "tres grafías en una piedra (CIL VI 2034)", 13.5, GRIS))
    yb += 84
    s, w = linea("AEGⱵPTI", 40, yb, 44, grosor=8)
    o.append(s)
    o.append(t(40 + w + 22, yb + 20, "dedicatoria del prefecto de Egipto, 47-48 (CIL VI 918)", 13.5))
    o.append(t(40 + w + 22, yb + 38, "la media H solo aparece en palabras griegas con ípsilon", 13.5, GRIS))
    o.append(f'<line x1="40" y1="{yb + 78}" x2="{W - 40}" y2="{yb + 78}" stroke="{GRIS}" stroke-width="0.8"/>')

    # --- Panel C
    yc = yb + 110
    o.append(t(40, yc, "Lo que no está grabado", 19, bold=True))
    o.append(t(40, yc + 22, "El discurso de Claudio del año 48 en el bronce de Lyon, y el mismo renglón con sus letras (reconstrucción mía).", 14, GRIS))
    y1 = yc + 46
    s, w = linea("QVASI NOVAM ISTAM REM INTRODVCI", 40, y1, 36, grosor=9)
    o.append(s)
    o.append(t(40 + w + 22, y1 + 23, "así está en el bronce", 13.5))
    y2 = y1 + 70
    s, w2 = linea("QVASI NOℲAM ISTAM REM INTRODVCI", 40, y2, 36, grosor=9)
    o.append(f'<rect x="28" y="{y2 - 12}" width="{w2 + 24}" height="60" fill="none" stroke="{GRIS}" stroke-width="1" stroke-dasharray="5 4"/>')
    o.append(s)
    o.append(t(40 + w2 + 22, y2 + 23, "así no está en ningún lado", 13.5, ROJO))
    y3 = y2 + 84
    s, wa = linea("IPSIVS", 40, y3, 40, grosor=8.5)
    o.append(s)
    o.append(f'<path d="M{40 + wa + 18},{y3 + 20} h40" stroke="{GRIS}" stroke-width="2"/>'
             f'<path d="M{40 + wa + 58},{y3 + 20} l-9,-5 v10 z" fill="{GRIS}"/>')
    xb = 40 + wa + 78
    s, wb = linea("IↃIVS", xb, y3, 40, grosor=8.5)
    o.append(f'<rect x="{xb - 12}" y="{y3 - 12}" width="{wb + 24}" height="64" fill="none" stroke="{GRIS}" stroke-width="1" stroke-dasharray="5 4"/>')
    o.append(s)
    o.append(t(xb + wb + 30, y3 + 16, "conjetura: si el antisigma era una C al revés y valía dentro de palabra.", 13.5))
    s, wl = linea("Ↄ L", xb + wb + 30, y3 + 25, 13, GRIS, 12, GRIS)
    o.append(s)
    o.append(t(xb + wb + 30 + wl + 8, y3 + 37, "ya estaba en las piedras con otro oficio: «liberto de una mujer».", 13.5, GRIS))

    # --- pie con las cuentas
    yp = y3 + 100
    o.append(f'<line x1="40" y1="{yp - 24}" x2="{W - 40}" y2="{yp - 24}" stroke="{GRIS}" stroke-width="0.8"/>')
    o.append(t(40, yp, "Cuánta falta hacían (por cada mil letras de latín corrido)", 19, bold=True))
    barras = [("u consonante", 12.9, "12,9", ROJO), ("x, que ya tenía letra", 4.9, "4,9", TINTA),
              ("ps + bs", 1.4, "1,4", ROJO), ("y griega", 0.36, "0,4", ROJO)]
    for i, (nom, v, vs, c) in enumerate(barras):
        yy = yp + 22 + i * 26
        o.append(t(230, yy + 13, nom, 14, TINTA, anchor="end"))
        o.append(f'<rect x="244" y="{yy}" width="{v * 46:.1f}" height="16" fill="{c}"/>')
        o.append(t(244 + v * 46 + 8, yy + 13, vs + " ‰", 14, TINTA))
    o.append(t(40, yp + 22 + 4 * 26 + 18,
               "Anales de Tácito, unas 559.000 letras, copia de The Latin Library (letras.py). En el discurso de Lyon, 3.858 letras: 50, 4 y ninguna.",
               12.5, GRIS))
    o.append("</svg>")
    svg = "\n".join(o)
    open("tres_letras.svg", "w", encoding="utf-8").write(svg)
    print("tres_letras.svg", len(svg), "bytes")
    try:
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to="tres_letras.png", output_width=2 * W)
        print("tres_letras.png")
    except Exception as e:  # la figura no depende del PNG
        print("sin PNG:", e)


if __name__ == "__main__":
    main()
