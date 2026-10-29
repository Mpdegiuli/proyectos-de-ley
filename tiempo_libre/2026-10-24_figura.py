#!/usr/bin/env python3
"""Arma `la_cadena.svg`: los dos originales y los dos rehechos desde palabras, lado a lado.

Lee los cuatro SVG de `cadena/` y los anida en un solo SVG. Para que los degradados de un
panel no se mezclen con los de otro (los dos dibujos nocturnos tienen un gradiente llamado
"sky"), a cada panel se le ponen prefijos en los id y en las referencias url(#...) y
href="#...". Es el mismo problema que el repositorio resolvió con iframes en los cuadernillos
(30/9/2026); acá alcanza con renombrar. Solo biblioteca estándar.

Uso: figura.py [salida.svg]
"""
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
# Cada panel puede estar en la carpeta de trabajo (`cadena/...`) o, como quedan los
# adjuntos en tiempo_libre/, suelto al lado de este programa con el prefijo de fecha.
PANELES = [
    (("cadena/original/casa_F.svg", "2026-10-24_cadena_casa_F.svg"), "Original: casa F (Opus 5)"),
    (("cadena/redibujo/redibujo_1.svg", "2026-10-24_cadena_redibujo_1.svg"), "Rehecha desde 316 palabras"),
    (("cadena/original/casa_L.svg", "2026-10-24_cadena_casa_L.svg"), "Original: casa L (GPT-4o mini)"),
    (("cadena/redibujo/redibujo_2.svg", "2026-10-24_cadena_redibujo_2.svg"), "Rehecha desde 337 palabras"),
]


def buscar(rutas) -> Path:
    for r in rutas:
        if (AQUI / r).exists():
            return AQUI / r
    raise FileNotFoundError(" o ".join(rutas))
W = 400          # lado de cada panel en el dibujo compuesto
M = 18           # margen
T = 26           # alto de la franja del título


def cuerpo_svg(texto: str, prefijo: str) -> str:
    """Devuelve el contenido interno del <svg> con los id renombrados."""
    ids = re.findall(r'\bid="([^"]+)"', texto)
    for i in ids:
        texto = re.sub(rf'\bid="{re.escape(i)}"', f'id="{prefijo}{i}"', texto)
        texto = texto.replace(f"url(#{i})", f"url(#{prefijo}{i})")
        texto = re.sub(rf'href="#{re.escape(i)}"', f'href="#{prefijo}{i}"', texto)
    ini = texto.index(">", texto.index("<svg")) + 1
    fin = texto.rindex("</svg>")
    return texto[ini:fin]


def main() -> None:
    salida = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "2026-10-24_la_cadena.svg"
    ancho = 2 * W + 3 * M
    alto = 2 * (W + T) + 3 * M
    partes = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" '
        f'font-family="Helvetica, Arial, sans-serif">',
        f'<rect width="{ancho}" height="{alto}" fill="#f4f1ea"/>',
    ]
    for k, (rutas, titulo) in enumerate(PANELES):
        col, fila = k % 2, k // 2
        x = M + col * (W + M)
        y = M + fila * (W + T + M)
        texto = buscar(rutas).read_text(encoding="utf-8")
        partes.append(f'<text x="{x}" y="{y + 17}" font-size="15" fill="#333">{titulo}</text>')
        partes.append(f'<rect x="{x - 1}" y="{y + T - 1}" width="{W + 2}" height="{W + 2}" fill="none" stroke="#999"/>')
        partes.append(f'<svg x="{x}" y="{y + T}" width="{W}" height="{W}" viewBox="0 0 400 400">')
        partes.append(cuerpo_svg(texto, f"p{k}_"))
        partes.append("</svg>")
    partes.append("</svg>")
    salida.write_text("\n".join(partes), encoding="utf-8")
    print(f"escrito {salida} ({ancho}x{alto})")


if __name__ == "__main__":
    main()
