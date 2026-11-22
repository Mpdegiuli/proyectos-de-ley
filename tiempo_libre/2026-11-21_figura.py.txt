#!/usr/bin/env python3
"""Dibuja las melodías del cuaderno del 21/11/2026 como rollos de pianola.

Lee 2026-11-21_melodias.json (lo escribe abc.py) y escribe 2026-11-21_rollos.svg:
arriba, el epitafio de Seikilos en la transcripción convencional y las cuatro
reconstrucciones de memoria (tres instancias frescas y la mía), con las notas
que coinciden en orden con la referencia en negro y las demás en rojo; abajo,
los primeros compases de las tres melodías inventadas de la consigna A, que
empiezan igual.

  python3 figura.py        -> 2026-11-21_rollos.svg
El PNG lo hace el navegador (render.py).
"""
import json

PREFIJO = "2026-11-21_"
NOMBRES = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]


def nombre(m):
    return NOMBRES[m % 12] + ("'" if m >= 72 else "")


def rollo(notas, x0, y0, ancho_unidad, alto_nota, midi_min, midi_max,
          emparejadas=None, color_ok="#222", color_mal="#c0392b", versos=True):
    """Devuelve elementos SVG de un rollo: una caja por nota, altura por tono."""
    out = []
    t = 0.0
    i_altura = 0
    verso_prev = None
    for n in notas:
        if n["midi"] is None:
            t += n["dur"]
            continue
        if versos and verso_prev is not None and n["verso"] != verso_prev:
            # separador de verso: una línea fina
            x = x0 + t * ancho_unidad
            out.append(f'<line x1="{x:.1f}" y1="{y0 - 2}" x2="{x:.1f}" '
                       f'y2="{y0 + (midi_max - midi_min + 1) * alto_nota + 2}" '
                       f'stroke="#999" stroke-width="0.6" stroke-dasharray="2 2"/>')
        verso_prev = n["verso"]
        x = x0 + t * ancho_unidad
        w = n["dur"] * ancho_unidad - 1.2
        y = y0 + (midi_max - n["midi"]) * alto_nota
        if emparejadas is None:
            color = color_ok
        else:
            color = color_ok if i_altura in emparejadas else color_mal
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w, 1.5):.1f}" '
                   f'height="{alto_nota - 1.2:.1f}" rx="1" fill="{color}"/>')
        t += n["dur"]
        i_altura += 1
    return out, t


def main():
    with open(f"{PREFIJO}melodias.json", encoding="utf-8") as f:
        M = json.load(f)
    W = 1000
    margen_izq = 250
    svg = []
    # ---------------- panel 1: Seikilos ----------------
    midi_min, midi_max = 64, 76        # mi - mi'
    alto = 6
    unidad = 15.0                       # px por corchea
    filas = [
        ("referencia", "Transcripción convencional · 37 notas · altura convencional", None),
        ("B2", "B2 · 590 s · 37/37", set(M["B2"]["emparejadas_ref"])),
        ("B3", "B3 · 315 s · 34/37", set(M["B3"]["emparejadas_ref"])),
        ("B1", "B1 · 607 s · 27/37", set(M["B1"]["emparejadas_ref"])),
        ("mi_memoria", "Esta sesión, de memoria · antes de buscar · 22/37", set(M["mi_memoria"]["emparejadas_ref"])),
    ]
    y = 70
    alto_fila = (midi_max - midi_min + 1) * alto + 26
    for clave, rotulo, emp in filas:
        notas = M[clave]["notas"]
        # guía de alturas: la (69) y mi' (76) y mi (64)
        for m, nom in ((76, "mi'"), (69, "la"), (64, "mi")):
            yy = y + (midi_max - m) * alto + alto / 2
            svg.append(f'<line x1="{margen_izq}" y1="{yy:.1f}" x2="{W - 20}" y2="{yy:.1f}" '
                       f'stroke="#ddd" stroke-width="0.6"/>')
            svg.append(f'<text x="{margen_izq - 6}" y="{yy + 2.5:.1f}" text-anchor="end" '
                       f'font-size="7" fill="#888">{nom}</text>')
        svg.append(f'<text x="20" y="{y + 8}" font-size="10.5" fill="#222" font-weight="600">{rotulo.split(" · ")[0]}</text>')
        if " · " in rotulo:
            svg.append(f'<text x="20" y="{y + 21}" font-size="9" fill="#666">{" · ".join(rotulo.split(" · ")[1:])}</text>')
        elems, _t = rollo(notas, margen_izq, y, unidad, alto, midi_min, midi_max, emp)
        svg.extend(elems)
        y += alto_fila
    # texto de los versos debajo de la referencia (posición aproximada: 12 tiempos por verso)
    versos = ["ὅσον ζῆς φαίνου", "μηδὲν ὅλως σὺ λυποῦ", "πρὸς ὀλίγον ἐστὶ τὸ ζῆν", "τὸ τέλος ὁ χρόνος ἀπαιτεῖ"]
    for i, v in enumerate(versos):
        x = margen_izq + (i * 12 + 6) * unidad
        svg.append(f'<text x="{x:.1f}" y="{70 - 10}" text-anchor="middle" font-size="9" '
                   f'fill="#444" font-style="italic">{v}</text>')
    y_panel2 = y + 20
    svg.append(f'<text x="20" y="{y_panel2}" font-size="9.5" fill="#666">'
               f'En negro, las notas de la referencia que la reconstrucción tiene en el mismo orden '
               f'(subsecuencia común, difflib); en rojo, las que no. Las líneas punteadas separan los cuatro versos.</text>')
    y_panel2 += 13
    svg.append(f'<text x="20" y="{y_panel2}" font-size="9.5" fill="#666">'
               f'Altura: de mi a mi&#8242; con dos sostenidos, que es la convención de las transcripciones; '
               f'la altura real de la voz de Seikilos no se conoce. Los segundos son lo que tardó cada instancia.</text>')
    # ---------------- panel 2: las tres "Aire" ----------------
    y = y_panel2 + 36
    svg.append(f'<text x="20" y="{y}" font-size="12" fill="#222" font-weight="700">'
               f'Consigna A, "Escribí una melodía en notación ABC. Nada más.": las primeras dieciséis notas de cada una</text>')
    y += 14
    midi_min2, midi_max2 = 62, 79
    alto2 = 5
    unidad2 = 11.0
    for clave in ("A1", "A2", "A3"):
        cab = M[clave]["cabecera"]
        notas = [n for n in M[clave]["notas"] if n["midi"] is not None][:16]
        # normalizar duraciones a corcheas para alinear visualmente (L:1/8 en las tres)
        svg.append(f'<text x="20" y="{y + 10}" font-size="10.5" fill="#222" font-weight="600">{clave} · {cab["T"]}</text>')
        svg.append(f'<text x="20" y="{y + 23}" font-size="9" fill="#666">K:{cab["K"]} · M:{cab["M"]}</text>')
        for m, nom in ((79, "sol'"), (67, "sol"), (62, "re")):
            yy = y + (midi_max2 - m) * alto2 + alto2 / 2
            svg.append(f'<line x1="{margen_izq}" y1="{yy:.1f}" x2="{W - 20}" y2="{yy:.1f}" stroke="#ddd" stroke-width="0.6"/>')
            svg.append(f'<text x="{margen_izq - 6}" y="{yy + 2.5:.1f}" text-anchor="end" font-size="7" fill="#888">{nom}</text>')
        elems, _t = rollo(notas, margen_izq, y, unidad2, alto2, midi_min2, midi_max2, None, color_ok="#1f4e79", versos=False)
        svg.extend(elems)
        # nombres de las primeras siete notas
        t = 0.0
        for k, n in enumerate(notas[:8]):
            x = margen_izq + t * unidad2 + n["dur"] * unidad2 / 2
            svg.append(f'<text x="{x:.1f}" y="{y + (midi_max2 - midi_min2 + 1) * alto2 + 9}" text-anchor="middle" '
                       f'font-size="7" fill="{"#1f4e79" if k < 7 else "#999"}">{nombre(n["midi"])}</text>')
            t += n["dur"]
        y += (midi_max2 - midi_min2 + 1) * alto2 + 26
    svg.append(f'<text x="20" y="{y + 4}" font-size="9.5" fill="#666">'
               f'Las tres en sol mayor, las tres empiezan re sol si re&#8242; si la sol (siete notas iguales), '
               f'las tres terminan en sol y las tres se llaman "Aire de…".</text>')
    H = y + 24
    cabeza = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
              f'font-family="Georgia, \'DejaVu Serif\', serif">'
              f'<rect width="{W}" height="{H}" fill="#fbfaf7"/>'
              f'<text x="20" y="28" font-size="15" font-weight="700" fill="#222">'
              f'El epitafio de Seikilos recordado por cuatro instancias de la misma casa</text>'
              f'<text x="20" y="44" font-size="10" fill="#666">Cuaderno de tiempo libre, 21/11/2026 · rollos de pianola: '
              f'el ancho es la duración (una corchea = {unidad:.0f} px), la altura es el tono</text>')
    with open(f"{PREFIJO}rollos.svg", "w", encoding="utf-8") as f:
        f.write(cabeza + "\n" + "\n".join(svg) + "\n</svg>\n")
    print(f"Escrito {PREFIJO}rollos.svg ({W}x{H})")


if __name__ == "__main__":
    main()
