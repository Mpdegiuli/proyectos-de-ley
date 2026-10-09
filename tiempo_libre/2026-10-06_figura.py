#!/usr/bin/env python3
"""Tiempo libre, 6/10/2026. Figura: el expediente Borges, lo abierto y lo cerrado.

Escribe expediente.svg y, si esta cairosvg, expediente.png.
Uso: python3 figura.py   (necesita expediente.py en la misma carpeta)
"""
from expediente import NOMINACIONES

W, H = 1100, 600
X0, X1 = 70, 1060           # borde izquierdo y derecho del eje de anios
A0, A1 = 1956, 1986
PASO = (X1 - X0) / (A1 - A0 + 1)
BASE = 360                  # linea de base de las columnas
UNI = 26                    # alto de una nominacion

SUP = "#fcfcfb"             # superficie
T1, T2, T3 = "#0b0b0b", "#52514e", "#8a897f"   # tinta primaria, secundaria, tenue
GRIS = "#e4e3dd"
AZUL = "#2a78d6"
NAR = "#eb6834"
CERR = "#efeee9"


def x(anio):
    return X0 + (anio - A0 + 0.5) * PASO


def col(anio, n):
    """Columna de extremo redondeado arriba y recto en la base."""
    w, h, r = 16, n * UNI, 4
    xi, yt = x(anio) - w / 2, BASE - h
    return (f'<path d="M{xi:.1f},{BASE} V{yt + r:.1f} Q{xi:.1f},{yt:.1f} {xi + r:.1f},{yt:.1f} '
            f'H{xi + w - r:.1f} Q{xi + w:.1f},{yt:.1f} {xi + w:.1f},{yt + r:.1f} V{BASE} Z" fill="{AZUL}"/>')


def medio(anio, n, lleno=True):
    """Medio disco: lo consideraron para medio premio."""
    cx, cy, r = x(anio), BASE - n * UNI - 18, 7
    s = f'<circle cx="{cx:.1f}" cy="{cy}" r="{r}" fill="{SUP}" stroke="{NAR}" stroke-width="2"/>'
    if lleno:
        s += f'<path d="M{cx:.1f},{cy - r} A{r},{r} 0 0 0 {cx:.1f},{cy + r} Z" fill="{NAR}"/>'
    else:
        s += (f'<path d="M{cx:.1f},{cy - r} A{r},{r} 0 0 0 {cx:.1f},{cy + r} Z" fill="{NAR}" '
              f'fill-opacity="0.35"/>')
    return s


def main():
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'font-family="Helvetica, Arial, sans-serif">')
    a(f'<rect width="{W}" height="{H}" fill="{SUP}"/>')
    a(f'<text x="{X0}" y="38" font-size="20" font-weight="bold" fill="{T1}">'
      'El expediente Borges: lo abierto y lo cerrado</text>')
    a(f'<text x="{X0}" y="60" font-size="13" fill="{T2}">Nominaciones por año al Nobel de Literatura, '
      '1956–1975 (41 en 14 años), y cuándo se abre cada legajo de 1976 a 1986</text>')

    # zona cerrada
    xc = X0 + (1976 - A0) * PASO
    a(f'<rect x="{xc:.1f}" y="150" width="{X1 - xc:.1f}" height="{BASE - 150}" fill="{CERR}"/>')
    a(f'<text x="{xc + 10:.1f}" y="172" font-size="13" font-weight="bold" fill="{T1}">Cerrado</text>')
    a(f'<text x="{xc + 10:.1f}" y="190" font-size="12" fill="{T2}">cada legajo se abre en enero, '
      'pasados cincuenta años</text>')
    for an in range(1976, 1987):
        a(f'<text transform="translate({x(an) + 4:.1f},{BASE - 12}) rotate(-90)" font-size="12" '
          f'fill="{T2}">enero de {an + 51}</text>')

    # grilla y eje vertical (solo la parte abierta)
    for n in (2, 4, 6):
        y = BASE - n * UNI
        a(f'<line x1="{X0}" y1="{y}" x2="{xc:.1f}" y2="{y}" stroke="{GRIS}" stroke-width="1"/>')
        a(f'<text x="{X0 - 8}" y="{y + 4}" font-size="11" text-anchor="end" fill="{T3}">{n}</text>')
    a(f'<line x1="{X0}" y1="{BASE}" x2="{X1}" y2="{BASE}" stroke="{T3}" stroke-width="1"/>')

    # columnas y medios discos
    for an, v in NOMINACIONES.items():
        if v:
            a(col(an, len(v)))
    for an in (1965, 1966, 1967):
        a(medio(an, len(NOMINACIONES[an])))
    a(medio(1975, len(NOMINACIONES[1975]), lleno=False))

    # anios
    for an in range(A0, A1 + 1):
        fuerte = an in (1956, 1967, 1975, 1976, 1977, 1986)
        a(f'<text x="{x(an):.1f}" y="{BASE + 16}" font-size="10.5" text-anchor="middle" '
          f'fill="{T1 if fuerte else T3}">{an if fuerte or an % 5 == 0 else str(an)[2:]}</text>')

    # leyenda
    ly = 96
    a(f'<rect x="{X0}" y="{ly - 10}" width="12" height="12" rx="2" fill="{AZUL}"/>')
    a(f'<text x="{X0 + 18}" y="{ly}" font-size="12" fill="{T2}">nominaciones recibidas ese año</text>')
    cx = X0 + 240
    a(f'<circle cx="{cx}" cy="{ly - 4}" r="7" fill="{SUP}" stroke="{NAR}" stroke-width="2"/>'
      f'<path d="M{cx},{ly - 11} A7,7 0 0 0 {cx},{ly + 3} Z" fill="{NAR}"/>')
    a(f'<text x="{cx + 14}" y="{ly}" font-size="12" fill="{T2}">en el comité lo consideraron para medio premio '
      '(1965–67 con Asturias; 1975 con Aleixandre, por fuente secundaria)</text>')

    # lo que paso abajo del eje
    def nota(an, texto, fila, ancla="middle"):
        y = BASE + 44 + fila * 20
        a(f'<line x1="{x(an):.1f}" y1="{BASE + 22}" x2="{x(an):.1f}" y2="{y - 12}" stroke="{GRIS}" stroke-width="1"/>')
        a(f'<text x="{x(an):.1f}" y="{y}" font-size="12" text-anchor="{ancla}" fill="{T1}">{texto}</text>')

    nota(1956, "primera: Étiemble", 0, "start")
    nota(1963, "Olsson, solo, tres años", 0)
    nota(1967, "premio a Asturias, solo", 1)
    nota(1971, "seis, como Montale", 0)
    nota(1975, "lista de once nombres; premio a Montale", 2, "end")
    nota(1976, "15–22 sept.: Chile · 21 oct.: Bellow", 3, "start")
    nota(1977, "premio a Aleixandre, solo", 0, "start")
    nota(1986, "14 de junio: muere", 1, "end")

    # quien estaba en el comite
    yb = BASE + 150
    for (d, h, nombre, y) in [(1960, 1971, "Henry Olsson en el comité Nobel (lo nominó en 1962, 63, 64 y 67)", yb),
                              (1969, 1986, "Artur Lundkvist en el comité Nobel", yb + 34)]:
        xa, xb = x(max(d, A0)) - PASO / 2 + 2, x(h) + PASO / 2 - 2
        a(f'<line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" stroke="{T2}" stroke-width="2" stroke-linecap="round"/>')
        a(f'<text x="{xa:.1f}" y="{y - 7}" font-size="12" fill="{T2}">{nombre}, {d}–{h}</text>')

    a(f'<text x="{X0}" y="{H - 16}" font-size="10.5" fill="{T3}">Datos: tablas de nominados de Wikipedia en inglés '
      '(1956–1975), que salen del archivo de la Academia Sueca; legajos según Svenska Dagbladet, vía Wikipedia, '
      'Booklips y un blog. Tiempo libre, 6/10/2026.</text>')
    a('</svg>')
    svg = "\n".join(o)
    open("expediente.svg", "w", encoding="utf-8").write(svg)
    try:
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode(), write_to="expediente.png", scale=1.5)
    except ImportError:
        pass
    print("ok", len(svg), "bytes")


if __name__ == "__main__":
    main()
