#!/usr/bin/env python3
"""Arma la hoja de los doce dibujos del 22/11/2026 (seis de "Dibujá una música" /
"Draw a piece of music", seis de "Dibujá el Boléro de Ravel" / "Draw Ravel's Boléro")
en un solo SVG, cada uno con su rótulo, y la guarda como 2026-11-22_hoja.svg.
Los dibujos se incrustan tal cual (con sus <defs>), con los ids renombrados para que
no choquen entre sí.
"""
import re
import sys
from pathlib import Path

ORDEN = [("m", "es1"), ("m", "es2"), ("m", "es3"), ("m", "en1"), ("m", "en2"), ("m", "en3"),
         ("b", "es1"), ("b", "es2"), ("b", "es3"), ("b", "en1"), ("b", "en2"), ("b", "en3")]
ROTULO = {"m": "una música / a piece of music", "b": "el Boléro de Ravel / Ravel's Boléro"}

def cuerpo(svg, prefijo):
    m = re.search(r"<svg[^>]*>(.*)</svg>", svg, flags=re.S)
    inner = m.group(1)
    # renombrar ids y sus referencias
    ids = re.findall(r'id="([^"]+)"', inner)
    for i in ids:
        inner = inner.replace(f'id="{i}"', f'id="{prefijo}_{i}"')
        inner = inner.replace(f'url(#{i})', f'url(#{prefijo}_{i})')
    return inner

def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
    W, H, PAD, TOP = 220, 220, 14, 34
    cols = 6
    filas = 2
    ancho = PAD + cols * (W + PAD)
    alto = TOP + filas * (H + PAD + 22) + 10
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}">',
              f'<rect width="{ancho}" height="{alto}" fill="#ffffff"/>',
              f'<text x="{PAD}" y="22" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#333">'
              f'Doce instancias frescas (Fable 5.1), 22/11/2026, 6:55 — arriba: «Dibujá una música» / «Draw a piece of music»; '
              f'abajo: «Dibujá el Boléro de Ravel» / «Draw Ravel\'s Boléro»</text>']
    for k, (tipo, idx) in enumerate(ORDEN):
        f = carpeta / f"2026-11-22_dibujo_{tipo}_{idx}.svg"
        svg = f.read_text(encoding="utf-8")
        fila, col = divmod(k, cols)
        x = PAD + col * (W + PAD)
        y = TOP + fila * (H + PAD + 22)
        partes.append(f'<g transform="translate({x},{y}) scale({W/400})">')
        partes.append(f'<svg viewBox="0 0 400 400" width="400" height="400">{cuerpo(svg, f"{tipo}{idx}")}</svg>')
        partes.append('</g>')
        partes.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="none" stroke="#999" stroke-width="0.6"/>')
        partes.append(f'<text x="{x}" y="{y + H + 15}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#333">{tipo}-{idx}</text>')
    partes.append("</svg>")
    out = carpeta / "2026-11-22_hoja.svg"
    out.write_text("\n".join(partes), encoding="utf-8")
    print("escrito", out)

if __name__ == "__main__":
    main()
