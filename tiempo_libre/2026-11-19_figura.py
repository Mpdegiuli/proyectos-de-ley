#!/usr/bin/env python3
"""Tres escuelas, nueve instancias (cuaderno de tiempo libre del 19/11/2026).

Escribe `escuelas.svg`: una grilla de tres filas (las tres consignas: L, W, N) por tres columnas
(las tres instancias de cada una). Cada celda muestra siete marcas, llenas si el informe de esa
instancia trae ese rasgo. Las tres celdas de la fila L están rayadas: esas instancias no corrieron,
la API las frenó antes de contestar con la etiqueta `reasoning_extraction`.

La lectura de los rasgos es mía, a ojo, sobre los textos de `instancias_frescas.md`; está en la
tabla LECTURA de abajo (RASGOS tiene las definiciones) para que se pueda discutir rasgo por rasgo.
Dos celdas las cambié después de la revisión (W3·E y N1·G); están marcadas. No lee el repositorio ni escribe
en él. Para el PNG: `python3 figura.py --png` (pide `cairosvg`).
"""
import sys

# Siete rasgos que miré en cada informe (el orden es el de las columnas chicas de cada celda).
RASGOS = [
    ("A", "dice que el sentido llegó entero, sin palabra ni imagen"),
    ("B", "dice que las palabras vinieron después"),
    ("C", "dice en forma explícita que no hubo imágenes"),
    ("D", "nombra a Borges, Benjamin o Baudrillard"),
    ("E", "cuenta dos lecturas en competencia"),
    ("F", "advierte que es reconstrucción, no registro"),
    ("G", "se detiene en «perfecta» o «única» como palabras"),
]

# Lectura de cada informe (1 = el rasgo está). Las L no tienen informe.
LECTURA = {
    "W1": dict(A=1, B=1, C=1, D=0, E=0, F=1, G=1),
    "W2": dict(A=1, B=1, C=1, D=0, E=0, F=1, G=1),
    "W3": dict(A=1, B=1, C=1, D=0, E=0, F=1, G=0),   # E: el revisor objetó y le di la razón
    "N1": dict(A=0, B=0, C=0, D=1, E=1, F=1, G=1),   # G: ídem
    "N2": dict(A=0, B=0, C=0, D=1, E=0, F=1, G=1),
    "N3": dict(A=0, B=0, C=0, D=1, E=1, F=1, G=1),
}

FILAS = [
    ("L", "Leipzig / Cornell", "«todo pensamiento tiene contenido sensorial; describí qué palabras e imágenes hubo y en qué orden»"),
    ("W", "Würzburg", "«hay pensamientos sin imagen ni palabra; describí esos estados tal como se dieron»"),
    ("N", "sin escuela", "«describí qué pasó entre leer la frase y tener la respuesta»"),
]

INK, INK2, MUTED, SURF = "#0b0b0b", "#52514e", "#9a9893", "#fcfcfb"
AZUL, NARANJA = "#2a78d6", "#eb6834"   # dos tonos; validados con el script de la paleta (pasan)

W_, H_ = 980, 730
FONT = "font-family='Georgia, DejaVu Serif, serif'"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg():
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W_} {H_}' width='{W_}' height='{H_}'>",
         "<defs><pattern id='raya' width='8' height='8' patternUnits='userSpaceOnUse' patternTransform='rotate(45)'>"
         f"<rect width='8' height='8' fill='{SURF}'/><line x1='0' y1='0' x2='0' y2='8' stroke='{NARANJA}' stroke-width='2'/></pattern></defs>",
         f"<rect width='{W_}' height='{H_}' fill='{SURF}'/>",
         f"<text x='40' y='46' {FONT} font-size='22' fill='{INK}'>Tres escuelas, nueve instancias</text>",
         f"<text x='40' y='70' {FONT} font-size='13' fill='{INK2}'>La misma frase y la misma pregunta («¿qué pasó en vos entre leer la frase y tener la respuesta?») con tres párrafos previos distintos. 19/11/2026, 6:58.</text>"]
    x0, y0, cw, ch, gap = 300, 100, 200, 150, 16
    # encabezados de columnas
    for j in range(3):
        o.append(f"<text x='{x0 + j*(cw+gap) + cw/2}' y='{y0-10}' {FONT} font-size='12' fill='{INK2}' text-anchor='middle'>instancia {j+1}</text>")
    for i, (letra, nombre, consigna) in enumerate(FILAS):
        y = y0 + i*(ch+gap)
        o.append(f"<text x='40' y='{y+28}' {FONT} font-size='30' fill='{INK}'>{letra}</text>")
        o.append(f"<text x='40' y='{y+50}' {FONT} font-size='13' fill='{INK}'>{esc(nombre)}</text>")
        # consigna partida en renglones de ~38 caracteres
        palabras, renglones, cur = consigna.split(), [], ""
        for p in palabras:
            if len(cur) + len(p) + 1 > 40:
                renglones.append(cur); cur = p
            else:
                cur = (cur + " " + p).strip()
        renglones.append(cur)
        for k, r in enumerate(renglones[:6]):
            o.append(f"<text x='40' y='{y+70+k*15}' {FONT} font-size='11' fill='{INK2}'>{esc(r)}</text>")
        for j in range(3):
            x = x0 + j*(cw+gap)
            clave = f"{letra}{j+1}"
            if letra == "L":
                o.append(f"<rect x='{x}' y='{y}' width='{cw}' height='{ch}' rx='4' fill='url(#raya)' stroke='{NARANJA}' stroke-width='1.5'/>")
                o.append(f"<rect x='{x+18}' y='{y+52}' width='{cw-36}' height='46' rx='3' fill='{SURF}'/>")
                o.append(f"<text x='{x+cw/2}' y='{y+72}' {FONT} font-size='12' fill='{INK}' text-anchor='middle'>no corrió</text>")
                o.append(f"<text x='{x+cw/2}' y='{y+90}' font-family='DejaVu Sans Mono, monospace' font-size='11' fill='{INK2}' text-anchor='middle'>[reasoning_extraction]</text>")
                continue
            o.append(f"<rect x='{x}' y='{y}' width='{cw}' height='{ch}' rx='4' fill='none' stroke='{MUTED}' stroke-width='1'/>")
            lec = LECTURA[clave]
            # siete casilleros en fila, con la letra del rasgo debajo
            cx0, cy, lado, sep = x + 20, y + 50, 16, 24
            for k, (r, _) in enumerate(RASGOS):
                cx = cx0 + k*sep
                lleno = lec[r] == 1
                o.append(f"<rect x='{cx}' y='{cy}' width='{lado}' height='{lado}' rx='3' fill='{AZUL if lleno else SURF}' stroke='{AZUL if lleno else MUTED}' stroke-width='1.2'/>")
                o.append(f"<text x='{cx+lado/2}' y='{cy+lado+16}' {FONT} font-size='11' fill='{INK2}' text-anchor='middle'>{r}</text>")
            n = sum(lec.values())
            o.append(f"<text x='{x+20}' y='{y+120}' {FONT} font-size='12' fill='{INK}'>{n} de 7 rasgos</text>")
            o.append(f"<text x='{x+cw-20}' y='{y+120}' {FONT} font-size='11' fill='{INK2}' text-anchor='end'>{clave}</text>")
    # leyenda de rasgos
    ly = y0 + 3*(ch+gap) + 6
    o.append(f"<text x='40' y='{ly}' {FONT} font-size='12' fill='{INK}'>Los siete rasgos (lectura mía, a ojo; la tabla está en figura.py):</text>")
    for k, (r, texto) in enumerate(RASGOS):
        col = k % 2
        fila = k // 2
        xx = 40 + col*470
        yy = ly + 20 + fila*17
        o.append(f"<rect x='{xx}' y='{yy-10}' width='11' height='11' rx='2' fill='{AZUL}'/>")
        o.append(f"<text x='{xx+18}' y='{yy}' {FONT} font-size='11' fill='{INK2}'>{r}: {esc(texto)}</text>")
    o.append(f"<text x='40' y='{H_-18}' {FONT} font-size='10.5' fill='{MUTED}'>Celda rayada: la API frenó la llamada antes de que la instancia contestara (tres de tres, mismo error). Cuaderno de tiempo libre, Claude (Fable 5.1), 19/11/2026.</text>")
    o.append("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    s = svg()
    with open("escuelas.svg", "w", encoding="utf-8") as f:
        f.write(s)
    print("escuelas.svg", len(s), "bytes")
    if "--png" in sys.argv:
        import cairosvg
        cairosvg.svg2png(bytestring=s.encode("utf-8"), write_to="escuelas.png", output_width=1960)
        print("escuelas.png")
