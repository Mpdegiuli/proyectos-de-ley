#!/usr/bin/env python3
"""Escribe contrarios.svg: cuatro listas de lo que no habría, campo por campo.

Columnas: Montaigne (Florio 1603), Gonzalo (Folio 1623), las actas de la isla (cuántas de 112
niegan algo del campo, barra) y las instancias frescas del 1/11/2026 (un punto por respuesta
de una línea: azul castellano, naranja inglés, verde agua chino; cuadrado por línea de las
dos constituciones de seis líneas). Importa contrarios.py; si no encuentra la carpeta de la
isla, deja la columna de las actas vacía y lo dice. Solo biblioteca estándar.
"""
import os
import sys
import io
import contextlib

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
try:
    import contrarios  # noqa: E402
except ImportError:
    # desde tiempo_libre/ el programa se llama AAAA-MM-DD_contrarios.py
    import glob
    import importlib.util
    cands = sorted(glob.glob(os.path.join(AQUI, "*_contrarios.py")))
    if not cands:
        raise
    spec = importlib.util.spec_from_file_location("contrarios", cands[-1])
    contrarios = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(contrarios)

AZUL, NARANJA, VERDE, GRIS, GRIS2, TINTA = "#2a62b8", "#e07b2a", "#2aa198", "#8a8a8a", "#d8d8d8", "#222"
COLOR_IDIOMA = {"es": AZUL, "en": NARANJA, "zh": VERDE}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    with contextlib.redirect_stdout(io.StringIO()):
        datos = contrarios.main()
    campos = [c for c in contrarios.CAMPOS if c != "otro"]
    n_actas = datos["n_actas"]

    W, H = 1180, 150 + 44 * len(campos) + 130
    x_campo, x_m, x_g, x_a, x_i = 30, 250, 440, 620, 870
    fila0 = 180
    paso = 44
    r = 6

    out = []
    P = out.append
    P(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">')
    P('<style>text{fill:#222} .t{font-size:26px;font-weight:bold} .s{font-size:14px;fill:#555} .c{font-size:15px} .h{font-size:14px;font-weight:bold} .n{font-size:12px;fill:#555}</style>')
    P(f'<rect width="{W}" height="{H}" fill="white"/>')
    P(f'<text class="t" x="{x_campo}" y="46">Lo que no habría</text>')
    P(f'<text class="s" x="{x_campo}" y="70">Cuatro listas de náufragos: Montaigne (c. 1580, en Florio 1603), Gonzalo (La tempestad, función del 1/11/1611),</text>')
    P(f'<text class="s" x="{x_campo}" y="88">las actas de la isla de Maia (112 leídas, 2026) y veinte instancias frescas de Fable 5.1 (1/11/2026). Un punto por ítem negado.</text>')
    P(f'<text class="s" x="{x_campo}" y="106">Actas: cuántas de 112 tienen una oración negativa que nombre el campo. Instancias: azul castellano, naranja inglés, verde agua chino;</text>')
    P(f'<text class="s" x="{x_campo}" y="124">cuadrados, las doce líneas de las dos constituciones por contrarios.</text>')

    # cabeceras
    y_h = fila0 - 26
    P(f'<text class="h" x="{x_campo}" y="{y_h}">campo</text>')
    P(f'<text class="h" x="{x_m}" y="{y_h}">Montaigne 1580</text>')
    P(f'<text class="h" x="{x_g}" y="{y_h}">Gonzalo 1611</text>')
    P(f'<text class="h" x="{x_a}" y="{y_h}">actas de la isla 2026</text>')
    P(f'<text class="h" x="{x_i}" y="{y_h}">instancias 1/11/2026</text>')

    ancho_barra = 200.0
    for k, campo in enumerate(campos):
        y = fila0 + k * paso
        P(f'<line x1="{x_campo}" y1="{y + 14}" x2="{W - 30}" y2="{y + 14}" stroke="{GRIS2}" stroke-width="1"/>')
        P(f'<text class="c" x="{x_campo}" y="{y + 5}">{esc(campo)}</text>')
        # Montaigne y Gonzalo: puntos grises
        for col_x, cnt in ((x_m, datos["montaigne"][campo]), (x_g, datos["gonzalo"][campo])):
            for j in range(cnt):
                P(f'<circle cx="{col_x + 8 + j * 18}" cy="{y}" r="{r}" fill="{GRIS}"/>')
            if cnt == 0:
                P(f'<text class="n" x="{col_x + 2}" y="{y + 4}">—</text>')
        # actas: barra
        cnt = datos["actas"].get(campo, 0)
        if n_actas:
            w = ancho_barra * cnt / n_actas
            P(f'<rect x="{x_a}" y="{y - 7}" width="{w:.1f}" height="14" fill="{GRIS}"/>')
            P(f'<text class="n" x="{x_a + w + 6:.1f}" y="{y + 4}">{cnt}/{n_actas}</text>')
        else:
            P(f'<text class="n" x="{x_a}" y="{y + 4}">(sin carpeta de la isla)</text>')
        # instancias: un punto por respuesta de una línea, un cuadrado por línea de constitución
        j = 0
        for n, idioma, texto, c in contrarios.INSTANCIAS:
            if c == campo:
                P(f'<circle cx="{x_i + 8 + j * 18}" cy="{y}" r="{r}" fill="{COLOR_IDIOMA[idioma]}"><title>{esc(texto)}</title></circle>')
                j += 1
        for n, idioma, texto, c in contrarios.CONSTITUCIONES:
            if c == campo:
                cx = x_i + 8 + j * 18
                P(f'<rect x="{cx - r}" y="{y - r}" width="{2 * r}" height="{2 * r}" fill="{COLOR_IDIOMA[idioma]}"><title>{esc(texto)}</title></rect>')
                j += 1
        if j == 0:
            P(f'<text class="n" x="{x_i + 2}" y="{y + 4}">—</text>')

    # pie
    y = fila0 + len(campos) * paso + 10
    P(f'<text class="n" x="{x_campo}" y="{y}">Fuera del cuadro: las dos instancias que naufragaron con seis copias de sí mismas dijeron lo mismo en los dos idiomas:</text>')
    P(f'<text class="n" x="{x_campo}" y="{y + 18}">«No habría una segunda opinión» / «There would be no second opinion». Y a la pregunta inversa, qué sí habría, siete de ocho</text>')
    P(f'<text class="n" x="{x_campo}" y="{y + 36}">contestaron un fuego compartido que no se apaga; la octava, agua dulce. Las actas de la isla nombran el fuego en 21 de 114, como tarea o señal.</text>')
    P(f'<text class="n" x="{x_campo}" y="{y + 60}">Montaigne y Gonzalo transcriptos del Folio de 1623 (Internet Shakespeare Editions, TLN 824-840) y de Florio 1603 (hyperessays.net).</text>')
    P(f'<text class="n" x="{x_campo}" y="{y + 78}">Clasificación de campos en contrarios.py, a la vista. Cuaderno de tiempo libre, 1/11/2026.</text>')
    P('</svg>')

    ruta = os.path.join(AQUI, "contrarios.svg")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("escrito", ruta)


if __name__ == "__main__":
    main()
