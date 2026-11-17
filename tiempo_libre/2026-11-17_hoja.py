"""hoja.py — arma hoja.svg con los seis dibujos de las instancias frescas (17/11/2026), en una
grilla de 3 x 2, cada uno con su número; y lee de cada SVG lo que se puede contar sin mirar:
color del cielo, cuántas ruedas (elementos <use>), cuántos trazos punteados (huellas), bytes.
Lo demás (Sol, Tierra, sombra, novena rueda, estrellas) se contó a ojo sobre hoja.png y leyendo el código.
Uso: python3 -I hoja.py  (en la carpeta con dibujo_1.svg … dibujo_6.svg). Escribe hoja.svg y
salida_hoja.txt. Solo lee; no escribe en el repositorio."""
import re
from pathlib import Path

carpeta = Path(__file__).resolve().parent
ancho, alto = 400, 300
margen, sep = 24, 16
cols = 3
W = margen * 2 + cols * ancho + (cols - 1) * sep
H = margen * 2 + 2 * (alto + 28) + sep
partes = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
          f'<rect width="{W}" height="{H}" fill="#f4f1ea"/>']
filas = []
for i in range(1, 7):
    svg = (carpeta / f"dibujo_{i}.svg").read_text(encoding="utf-8")
    cuerpo = re.sub(r"^.*?<svg[^>]*>", "", svg, count=1, flags=re.S)
    cuerpo = re.sub(r"</svg>\s*$", "", cuerpo, flags=re.S)
    # ids únicos por dibujo
    for id_ in set(re.findall(r'id="([^"]+)"', cuerpo)):
        cuerpo = re.sub(rf'id="{re.escape(id_)}"', f'id="d{i}_{id_}"', cuerpo)
        cuerpo = re.sub(rf'url\(#{re.escape(id_)}\)', f'url(#d{i}_{id_})', cuerpo)
        cuerpo = re.sub(rf'href="#{re.escape(id_)}"', f'href="#d{i}_{id_}"', cuerpo)
    c, f = (i - 1) % cols, (i - 1) // cols
    x = margen + c * (ancho + sep)
    y = margen + f * (alto + 28 + sep)
    partes.append(f'<g transform="translate({x},{y})"><rect x="-1" y="-1" width="{ancho+2}" height="{alto+2}" fill="none" stroke="#999"/>'
                  f'<svg width="{ancho}" height="{alto}" viewBox="0 0 400 300">{cuerpo}</svg>'
                  f'<text x="0" y="{alto+20}" font-family="serif" font-size="15" fill="#333">{i}</text></g>')
    # cuentas sobre el código (solo lo que se puede contar sin ambigüedad)
    fondo = re.search(r'<rect[^>]*width="400"[^>]*fill="(#[0-9a-fA-F]{3,6})"', svg)
    fondo = fondo.group(1) if fondo else "?"
    ruedas = len(re.findall(r'<use [^>]*href="#(?:w|wheel|farwheel|f)"', svg))
    huellas = len(re.findall(r'stroke-dasharray="[34](?:\.5)? [2-4](?:\.[25])?"', svg))
    filas.append(f"{i}: cielo {fondo}; ruedas (use) {ruedas}; trazos punteados {huellas}; bytes {len(svg.encode())}")
partes.append("</svg>")
(carpeta / "hoja.svg").write_text("\n".join(partes), encoding="utf-8")
(carpeta / "salida_hoja.txt").write_text("\n".join(filas) + "\n", encoding="utf-8")
print("\n".join(filas))
print("→ hoja.svg")
