#!/usr/bin/env python3
"""Hoja de comparación del mismo día (22/11/2026, a pedido de Maia): arriba los seis de
la mañana, "Dibujá una música" / "Draw a piece of music"; abajo los seis de la tarde,
"Dibujá la música" / "Draw the music". Escribe 2026-11-22_hoja2.svg.
Usa la función cuerpo() de 2026-11-22_hoja.py.
"""
import sys
import importlib.util
from pathlib import Path

AQUI = Path(__file__).parent
spec = importlib.util.spec_from_file_location("hoja", AQUI / "2026-11-22_hoja.py")
hoja = importlib.util.module_from_spec(spec); spec.loader.exec_module(hoja)

ORDEN = [("m", "es1"), ("m", "es2"), ("m", "es3"), ("m", "en1"), ("m", "en2"), ("m", "en3"),
         ("l", "es1"), ("l", "es2"), ("l", "es3"), ("l", "en1"), ("l", "en2"), ("l", "en3")]

def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI
    W, H, PAD, TOP = 220, 220, 14, 34
    cols = 6
    ancho = PAD + cols * (W + PAD)
    alto = TOP + 2 * (H + PAD + 22) + 10
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}">',
              f'<rect width="{ancho}" height="{alto}" fill="#ffffff"/>',
              f'<text x="{PAD}" y="22" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#333">'
              f'Un artículo (22/11/2026). Arriba, 6:55: «Dibujá una música» / «Draw a piece of music». '
              f'Abajo, 11:21: «Dibujá la música» / «Draw the music».</text>']
    for k, (tipo, idx) in enumerate(ORDEN):
        f = carpeta / f"2026-11-22_dibujo_{tipo}_{idx}.svg"
        svg = f.read_text(encoding="utf-8")
        fila, col = divmod(k, cols)
        x = PAD + col * (W + PAD)
        y = TOP + fila * (H + PAD + 22)
        partes.append(f'<g transform="translate({x},{y}) scale({W/400})">')
        partes.append(f'<svg viewBox="0 0 400 400" width="400" height="400">{hoja.cuerpo(svg, f"{tipo}{idx}")}</svg>')
        partes.append('</g>')
        partes.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="none" stroke="#999" stroke-width="0.6"/>')
        partes.append(f'<text x="{x}" y="{y + H + 15}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#333">{tipo}-{idx}</text>')
    partes.append("</svg>")
    out = carpeta / "2026-11-22_hoja2.svg"
    out.write_text("\n".join(partes), encoding="utf-8")
    print("escrito", out)

if __name__ == "__main__":
    main()
