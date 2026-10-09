#!/usr/bin/env python3
"""figura.py — las 28 letras de 1446 con dos primitivas.

Dibuja las 17 consonantes y las 11 vocales del Hunminjeongeum usando solo <line> y
<circle> (el punto es un círculo lleno), ordenadas como las ordena el Haerye: una
forma básica por órgano y las demás "agregando trazos". Lo agregado va en color.
Abajo, dos bocas de perfil mirando a la izquierda (esas sí con <path>: son un esquema
mío, hecho a partir del texto, no una lámina de anatomía) con ㄴ y ㄱ encima.

Escribe veintiocho.svg y, si está cairosvg, veintiocho.png.
Uso: python3 figura.py
"""
ESTILO = (
    "text{font-family:DejaVu Sans,Helvetica,Arial,sans-serif;font-size:11px;fill:#6b7280}"
    ".n{fill:#1d2a3a;font-weight:bold;font-size:15px}.m{text-anchor:middle}.e{text-anchor:end}"
    "line,.o{stroke:#1d2a3a;stroke-width:4.8;stroke-linecap:square;fill:none}"
    ".r{stroke:#b5451b}.p{fill:#1d2a3a}.q{fill:#b5451b}"
    "path{fill:none;stroke:#6b7280;stroke-width:2.5;stroke-linejoin:round}"
    ".l{fill:#e3d9c6;stroke-width:1.5}.w{stroke:#b5451b;stroke-width:7}.s{stroke:#e3d9c6;stroke-width:1}"
    ".y{stroke:#6b7280;stroke-width:2.5}"
)

# Cada letra: lista de primitivas en un cuadro de lado 1.
# ("l", x1, y1, x2, y2, nuevo)  o  ("c", cx, cy, r, lleno, nuevo); nuevo = 1: trazo agregado;
# nuevo = 2: resalte en color de la parte que sobresale (ㅂ y ㅍ no suman trazos respecto de ㅁ:
# los alargan), que se dibuja encima y no entra en la cuenta de primitivas
G = [("l", .15, .2, .85, .2, 0), ("l", .85, .2, .85, .85, 0)]
N = [("l", .15, .15, .15, .8, 0), ("l", .15, .8, .85, .8, 0)]
M = [("l", .18, .2, .82, .2, 0), ("l", .82, .2, .82, .82, 0), ("l", .82, .82, .18, .82, 0),
     ("l", .18, .82, .18, .2, 0)]
S = [("l", .5, .15, .12, .85, 0), ("l", .5, .15, .88, .85, 0)]
O = [("c", .5, .5, .32, 0, 0)]

CONSONANTES = [
    # (órgano, lo que dibuja según el Haerye, [(romanización, primitivas), ...], aparte)
    ("muela", "la raíz de la lengua cierra la garganta",
     [("g", G), ("k", G + [("l", .15, .52, .85, .52, 1)])],
     ("ng", [("c", .5, .62, .27, 0, 0), ("l", .5, .35, .5, .12, 0)])),
    ("lengua", "la lengua toca el paladar",
     [("n", N),
      ("d", [("l", .15, .2, .85, .2, 1), ("l", .15, .2, .15, .8, 0), ("l", .15, .8, .85, .8, 0)]),
      ("t", [("l", .15, .2, .85, .2, 0), ("l", .15, .2, .15, .8, 0), ("l", .15, .8, .85, .8, 0),
             ("l", .15, .5, .85, .5, 1)])],
     ("r", [("l", .15, .15, .85, .15, 0), ("l", .85, .15, .85, .5, 0), ("l", .15, .5, .85, .5, 0),
            ("l", .15, .5, .15, .85, 0), ("l", .15, .85, .85, .85, 0)])),
    ("labio", "la boca",
     [("m", M),
      ("b", [("l", .18, .1, .18, .85, 0), ("l", .82, .1, .82, .85, 0), ("l", .18, .45, .82, .45, 0),
             ("l", .18, .85, .82, .85, 0), ("l", .18, .1, .18, .45, 2), ("l", .82, .1, .82, .45, 2)]),
      ("p", [("l", .08, .2, .92, .2, 0), ("l", .08, .82, .92, .82, 0), ("l", .3, .2, .3, .82, 0),
             ("l", .7, .2, .7, .82, 0), ("l", .08, .2, .3, .2, 2), ("l", .7, .2, .92, .2, 2),
             ("l", .08, .82, .3, .82, 2), ("l", .7, .82, .92, .82, 2)])],
     None),
    ("diente", "el diente",
     [("s", S),
      ("j", [("l", .12, .22, .88, .22, 1), ("l", .5, .22, .12, .85, 0), ("l", .5, .22, .88, .85, 0)]),
      ("ch", [("l", .12, .25, .88, .25, 0), ("l", .5, .25, .12, .88, 0), ("l", .5, .25, .88, .88, 0),
              ("l", .5, .06, .5, .25, 1)])],
     ("z", S + [("l", .12, .85, .88, .85, 0)])),
    ("garganta", "la garganta",
     [("(nada)", O),
      ("ʔ", [("c", .5, .62, .27, 0, 0), ("l", .15, .24, .85, .24, 1)]),
      ("h", [("c", .5, .64, .25, 0, 0), ("l", .15, .28, .85, .28, 0), ("l", .5, .08, .5, .28, 1)])],
     None),
]


def punto(x, y):
    return ("c", x, y, .075, 1, 1)


VOCALES = [
    [("ʌ · cielo", [("c", .5, .5, .1, 1, 0)]), ("eu · tierra", [("l", .1, .5, .9, .5, 0)]),
     ("i · persona", [("l", .5, .1, .5, .9, 0)])],
    [("o", [("l", .1, .62, .9, .62, 0), punto(.5, .4)]),
     ("a", [("l", .42, .1, .42, .9, 0), punto(.64, .5)]),
     ("u", [("l", .1, .38, .9, .38, 0), punto(.5, .6)]),
     ("eo", [("l", .58, .1, .58, .9, 0), punto(.36, .5)])],
    [("yo", [("l", .1, .62, .9, .62, 0), punto(.36, .4), punto(.64, .4)]),
     ("ya", [("l", .42, .1, .42, .9, 0), punto(.64, .36), punto(.64, .64)]),
     ("yu", [("l", .1, .38, .9, .38, 0), punto(.36, .6), punto(.64, .6)]),
     ("yeo", [("l", .58, .1, .58, .9, 0), punto(.36, .36), punto(.36, .64)])],
]

cuenta = {"line": 0, "circle": 0, "letras": 0}


def n(v):
    """Número corto: un decimal como mucho."""
    return ("%.1f" % v).rstrip("0").rstrip(".")


def linea(x1, y1, x2, y2, clase=""):
    c = ' class="%s"' % clase if clase else ""
    return '<line%s x1="%s" y1="%s" x2="%s" y2="%s"/>' % (c, n(x1), n(y1), n(x2), n(y2))


def letra(prims, x, y, lado):
    out = []
    for p in prims:
        if p[0] == "l":
            _, x1, y1, x2, y2, nuevo = p
            out.append(linea(x + x1 * lado, y + y1 * lado, x + x2 * lado, y + y2 * lado, "r" if nuevo else ""))
            if nuevo != 2:
                cuenta["line"] += 1
        else:
            _, cx, cy, r, lleno, nuevo = p
            clase = ("q" if nuevo else "p") if lleno else "o"
            out.append('<circle class="%s" cx="%s" cy="%s" r="%s"/>'
                       % (clase, n(x + cx * lado), n(y + cy * lado), n(r * lado)))
            cuenta["circle"] += 1
    cuenta["letras"] += 1
    return out


def texto(x, y, s, clase=""):
    c = ' class="%s"' % clase if clase else ""
    return '<text%s x="%s" y="%s">%s</text>' % (c, n(x), n(y), s)


def camino(x0, y0, d, clase=""):
    """Un <path>; d usa coordenadas relativas al origen (x0, y0) de la boca."""
    partes = []
    for tok in d.split():
        if "," in tok:
            a, b = tok.split(",")
            partes.append("%s,%s" % (n(x0 + float(a)), n(y0 + float(b))))
        else:
            partes.append(tok)
    c = ' class="%s"' % clase if clase else ""
    return '<path%s d="%s"/>' % (c, " ".join(partes))


def boca(x0, y0, cual):
    """Corte de perfil, mirando a la izquierda. Esquema, no anatomía."""
    o = []
    # paladar: labio de arriba, diente, encía, bóveda, velo; y la pared de atrás de la garganta
    o.append(camino(x0, y0, "M 8,40 C 2,52 6,66 22,62 L 26,80 L 32,62 L 40,56 C 52,34 96,30 122,40 "
                            "C 136,46 146,58 148,74 C 150,80 144,84 141,76"))
    o.append(linea(x0 + 176, y0 + 22, x0 + 176, y0 + 150, "y"))
    # labio y diente de abajo
    o.append(camino(x0, y0, "M 8,122 C 2,108 8,96 22,100 L 27,86 L 33,104"))
    if cual == "n":
        # la punta sube a tocar la encía; el cuerpo queda abajo
        o.append(camino(x0, y0, "M 38,112 C 34,90 36,66 44,60 C 54,62 56,86 72,92 C 104,98 140,100 152,118 "
                                "L 152,150 L 38,150 Z", "l"))
        o.append(linea(x0 + 46, y0 + 64, x0 + 46, y0 + 106, "w"))
        o.append(linea(x0 + 46, y0 + 106, x0 + 140, y0 + 106, "w"))
    else:
        # el fondo de la lengua sube al velo y la raíz baja tapando la garganta
        o.append(camino(x0, y0, "M 38,112 C 46,100 60,92 78,74 C 92,58 118,48 140,54 C 158,60 160,100 158,150 "
                                "L 38,150 Z", "l"))
        o.append(linea(x0 + 84, y0 + 62, x0 + 152, y0 + 62, "w"))
        o.append(linea(x0 + 152, y0 + 62, x0 + 152, y0 + 140, "w"))
    return o


def armar():
    W, H = 1120, 800
    s = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H, W, H),
         "<style>%s</style>" % ESTILO,
         '<rect width="%d" height="%d" fill="#f6f1e7"/>' % (W, H),
         '<text class="n" x="40" y="44" style="font-size:22px">Las veintiocho letras de 1446, '
         "con dos primitivas</text>",
         '<text x="40" y="68" style="font-size:13px">Solo &lt;line&gt; y &lt;circle&gt;. En color, lo que el '
         "Haerye llama agregar un trazo (y, en las vocales, el punto).</text>"]

    # consonantes
    x_lab, x0, paso, lado = 40, 190, 92, 64
    s.append(texto(x_lab, 104, "17 consonantes", "n"))
    for i, t in enumerate(("forma básica", "+ un trazo", "+ otro")):
        s.append(texto(x0 + i * paso + lado / 2, 104, t, "m"))
    xa = x0 + 3.45 * paso
    s.append(texto(xa + lado / 2, 104, "aparte", "m"))
    y = 118
    for organo, dibuja, serie, aparte in CONSONANTES:
        s.append(texto(x_lab, y + 30, organo, "n"))
        renglones, actual = [], ""
        for pal in dibuja.split():
            if len(actual) + len(pal) + 1 > 20 and actual:
                renglones.append(actual)
                actual = pal
            else:
                actual = (actual + " " + pal).strip()
        renglones.append(actual)
        for k, r in enumerate(renglones):
            s.append(texto(x_lab, y + 47 + 13 * k, r))
        for i, (rom, prims) in enumerate(serie):
            s += letra(prims, x0 + i * paso, y, lado)
            s.append(texto(x0 + i * paso + lado / 2, y + lado + 13, rom, "m"))
        if aparte:
            rom, prims = aparte
            s += letra(prims, xa, y, lado)
            s.append(texto(xa + lado / 2, y + lado + 13, rom, "m"))
        y += 92

    # vocales
    xv, lv, pv = 640, 64, 104
    s.append(texto(xv, 104, "11 vocales", "n"))
    yv = 118
    for fila in VOCALES:
        for i, (rom, prims) in enumerate(fila):
            s += letra(prims, xv + i * pv, yv, lv)
            s.append(texto(xv + i * pv + lv / 2, yv + lv + 15, rom, "m"))
        yv += 104
    s.append(texto(xv, yv + 30, "28 letras · %d líneas · %d círculos · ningún &lt;path&gt;"
                   % (cuenta["line"], cuenta["circle"]), "n"))

    # bocas
    yb = 598
    s.append(linea(40, yb - 22, W - 40, yb - 22, "s"))
    s.append(texto(40, yb + 4, "De perfil, mirando a la izquierda", "n"))
    s.append(texto(40, yb + 24, "(esquema mío a partir del texto;"))
    s.append(texto(40, yb + 39, "no es una lámina de anatomía)"))
    s += boca(330, yb - 6, "n")
    s.append(texto(420, yb + 172, "n: la lengua toca el paladar", "m"))
    s += boca(640, yb - 6, "g")
    s.append(texto(730, yb + 172, "g: la raíz de la lengua cierra la garganta", "m"))
    s.append(texto(W - 40, yb + 4, "labios ←", "e"))
    s.append(texto(W - 40, yb + 20, "→ garganta", "e"))
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    svg = armar()
    with open("veintiocho.svg", "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("letras: %d   <line>: %d   <circle>: %d   primitivas: %d"
          % (cuenta["letras"], cuenta["line"], cuenta["circle"], cuenta["line"] + cuenta["circle"]))
    try:
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to="veintiocho.png", scale=1.5)
        print("veintiocho.svg y veintiocho.png escritos")
    except ImportError:
        print("veintiocho.svg escrito (sin cairosvg no hay PNG)")
