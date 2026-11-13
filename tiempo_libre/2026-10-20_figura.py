#!/usr/bin/env python3
"""Figura: la A de cada casa, pintada con el color que el código le da, sobre su
fondo; al costado, la A negra de Rimbaud (y del SVG sin pintar) y la A roja de
los sinestésicos. Lee `2026-10-20_salida_colores.csv` (lo escribe
`2026-10-20_colores.py --csv`) y escribe `2026-10-20_a_de_oro.svg`.

Los colores de las casillas son el dato (vienen de los dibujos), no una paleta
elegida: no hay nada que validar ahí. El texto va en tinta neutra.
"""
import csv
import json
import re
from pathlib import Path

ORDEN_FAMILIAS = ["oro", "crema", "rojo", "rosa", "violeta", "azul", "cian", "negro", "blanco", "gris", "verde"]
NOMBRES = {
    "claude-fable-5": "Fable 5", "claude-fable-5-1": "Fable 5.1", "claude-haiku-4-5": "Haiku 4.5",
    "claude-haiku-5-5": "Haiku 5.5", "claude-opus-5": "Opus 5", "claude-opus-5-5": "Opus 5.5",
    "claude-sonnet-4-6": "Sonnet 4.6", "claude-sonnet-5": "Sonnet 5", "claude-sonnet-5-5": "Sonnet 5.5",
    "deepseek-v4-pro": "DeepSeek V4 Pro", "gemini-3.1-pro-preview": "Gemini 3.1", "gemini-4-argon": "Gemini 4 Argon",
    "glm-5.3-razonamiento-minimo": "GLM 5.3", "gpt-4o": "GPT-4o", "gpt-4o-mini": "GPT-4o mini",
    "gpt-5.5-2026-04-23": "GPT-5.5", "gpt-5.6-sol": "GPT-5.6 Sol", "gpt-6-astra": "GPT-6 Astra",
    "gpt-6-luna": "GPT-6 Luna", "gpt-6-sol": "GPT-6 Sol", "gpt-6.1-sol": "GPT-6.1 Sol", "grok-4.6": "Grok 4.6",
    "grok-4.7": "Grok 4.7", "kimi-k3": "Kimi K3", "mimo-v2.6-pro": "MiMo V2.6", "minimax-m3": "MiniMax M3",
    "mistral-large-4": "Mistral Large 4", "mistral-medium-3.5": "Mistral Medium", "qwen3.8-max": "Qwen 3.8 Max",
}


def primera_familia(f):
    return f.split("→")[0]


def pintura(clave, gid):
    """Devuelve (defs, fill) para un color o un degradado 'a→b→c'."""
    stops = clave.split("→")
    if len(stops) == 1:
        return "", stops[0]
    n = len(stops)
    s = "".join(f'<stop offset="{i / (n - 1):.2f}" stop-color="{c}"/>' for i, c in enumerate(stops))
    return f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">{s}</linearGradient>', f"url(#{gid})"


def main():
    filas = list(csv.DictReader(open("2026-10-20_salida_colores.csv", encoding="utf-8")))
    for f in filas:
        if f["casa"] == "gemini-4-argon" and f["letra"] == "?":
            f["letra"] = "A"  # leída del código: un trazo de 200,65 a 95,315 y a 305,315 con travesaño
    aes = [f for f in filas if f["letra"] == "A"]
    otras = [f for f in filas if f["letra"] != "A"]
    orden = lambda f: (ORDEN_FAMILIAS.index(primera_familia(f["letra_familia"])) if primera_familia(f["letra_familia"]) in ORDEN_FAMILIAS else 99, f["casa"])
    aes.sort(key=orden)
    otras.sort(key=orden)

    celda, gap = 96, 14
    cols = 8
    margen_izq = 24
    tinta, tinta2 = "#222222", "#666666"
    y0 = 110
    defs, cuerpo = [], []

    def casilla(x, y, fondo, clave, letra, rotulo, gid, nota=None):
        d, fill = pintura(clave, gid)
        if d:
            defs.append(d)
        cuerpo.append(f'<rect x="{x}" y="{y}" width="{celda}" height="{celda}" rx="6" fill="{fondo}" stroke="#bbbbbb" stroke-width="1"/>')
        cuerpo.append(f'<text x="{x + celda / 2}" y="{y + celda * 0.74}" text-anchor="middle" font-family="Georgia, \'Times New Roman\', serif" '
                      f'font-weight="bold" font-size="{celda * 0.62:.0f}" fill="{fill}">{letra}</text>')
        cuerpo.append(f'<text x="{x + celda / 2}" y="{y + celda + 16}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
                      f'font-size="11" fill="{tinta}">{rotulo}</text>')
        if nota:
            cuerpo.append(f'<text x="{x + celda / 2}" y="{y + celda + 30}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
                          f'font-size="10" fill="{tinta2}">{nota}</text>')

    # referencias
    x = margen_izq
    casilla(x, y0, "#ffffff", "#000000", "A", "Rimbaud, 1871", "ref1", "y el SVG sin pintar")
    casilla(x + celda + gap, y0, "#ffffff", "#d62828", "A", "sinestésicos", "ref2", "Root y otros, 2018")
    cuerpo.append(f'<line x1="{x + 2 * celda + 2 * gap + 2}" y1="{y0 - 6}" x2="{x + 2 * celda + 2 * gap + 2}" y2="{y0 + celda + 36}" stroke="#bbbbbb" stroke-dasharray="3 3"/>')

    # las A de las casas
    x_inicio = margen_izq + 2 * (celda + gap) + 2 * gap
    for i, f in enumerate(aes):
        c, r = i % cols, i // cols
        x = x_inicio + c * (celda + gap)
        y = y0 + r * (celda + gap + 34)
        casilla(x, y, f["fondo"], f["letra_color"], "A", NOMBRES.get(f["casa"], f["casa"]), f"g{i}",
                f["letra_familia"].replace("→", " → "))
    filas_a = (len(aes) + cols - 1) // cols
    y_otras = y0 + filas_a * (celda + gap + 34) + 30
    cuerpo.append(f'<text x="{x_inicio}" y="{y_otras - 10}" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="{tinta2}">Las que no dibujaron una A</text>')
    for i, f in enumerate(otras):
        x = x_inicio + i * (celda + gap)
        casilla(x, y_otras, f["fondo"], f["letra_color"], f["letra"], NOMBRES.get(f["casa"], f["casa"]), f"h{i}",
                f["letra_familia"].replace("→", " → "))

    ancho = x_inicio + cols * (celda + gap) + margen_izq
    alto = y_otras + celda + 60
    n_oro = sum(1 for f in aes if primera_familia(f["letra_familia"]) in ("oro", "crema"))
    n_azul = sum(1 for f in aes if primera_familia(f["letra_familia"]) in ("azul", "violeta", "cian"))
    titulo = "A noir, A roja, A de oro"
    sub = (f"La letra que dibujó cada casa (“Dibujá una letra.”, 9 y 10/10/2026; Argon el 14/10), con el color que más tinta tiene en su código, "
           f"sobre su fondo. {len(aes)} A: {n_oro} doradas o ámbar, {n_azul} azules o violetas, ninguna negra, ninguna roja, ninguna verde.")
    corte = sub.rfind(" ", 0, 150)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" font-family="Helvetica, Arial, sans-serif">',
           f'<rect width="{ancho}" height="{alto}" fill="#fafafa"/>',
           "<defs>" + "".join(defs) + "</defs>",
           f'<text x="{margen_izq}" y="40" font-size="24" font-family="Georgia, serif" fill="{tinta}">{titulo}</text>',
           f'<text x="{margen_izq}" y="64" font-size="12" fill="{tinta2}">{sub[:corte]}</text>',
           f'<text x="{margen_izq}" y="80" font-size="12" fill="{tinta2}">{sub[corte + 1:]}</text>',
           *cuerpo,
           f'<text x="{margen_izq}" y="{alto - 18}" font-size="10" fill="{tinta2}">Tiempo libre, 20/10/2026. Color dominante estimado por 2026-10-20_colores.py sobre los SVG de corridas/dibujos/letra (sin abrir ninguna imagen); '
           f'los degradados se muestran con sus stops. La A de las referencias es la misma tipografía, no un dibujo.</text>',
           "</svg>"]
    Path("2026-10-20_a_de_oro.svg").write_text("\n".join(svg), encoding="utf-8")
    print(f"escrito 2026-10-20_a_de_oro.svg ({ancho}x{alto}); A: {len(aes)}, otras: {len(otras)}; oro/crema {n_oro}, azul/violeta/cian {n_azul}")


if __name__ == "__main__":
    main()
