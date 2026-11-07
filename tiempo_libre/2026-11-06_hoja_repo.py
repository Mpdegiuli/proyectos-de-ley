"""Hoja de contacto de una consigna de dibujo del repositorio (solo lee), para mirar las manos de las personas.
Uso: python3 hoja_repo.py RUTA_AL_REPO consigna [salida.svg] [--cols 6] [--celda 200]"""
import glob, os, re, sys

def limpiar(svg, pref):
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg)
    ids = set(re.findall(r'\bid="([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        svg = re.sub(rf'\bid="{re.escape(i)}"', f'id="{pref}{i}"', svg)
        svg = re.sub(rf'url\(#{re.escape(i)}\)', f'url(#{pref}{i})', svg)
        svg = re.sub(rf'href="#{re.escape(i)}"', f'href="#{pref}{i}"', svg)
    return svg

def main():
    args = sys.argv[1:]
    cols, celda = 6, 200
    if "--cols" in args:
        i = args.index("--cols"); cols = int(args[i + 1]); del args[i:i + 2]
    if "--celda" in args:
        i = args.index("--celda"); celda = int(args[i + 1]); del args[i:i + 2]
    raiz, consigna = args[0], args[1]
    salida = args[2] if len(args) > 2 else f"hoja_{consigna}.svg"
    carpeta = os.path.join(raiz, "corridas", "dibujos", consigna)
    dibs = sorted(glob.glob(os.path.join(carpeta, "*", "dibujo.svg")))
    margen, pie = 10, 16
    filas = (len(dibs) + cols - 1) // cols
    ancho = margen + cols * (celda + margen)
    alto = margen + filas * (celda + pie + margen)
    partes = []
    for k, f in enumerate(dibs):
        casa = os.path.basename(os.path.dirname(f))
        x = margen + (k % cols) * (celda + margen)
        y = margen + (k // cols) * (celda + pie + margen)
        svg = open(f, encoding="utf-8").read()
        if not svg.strip():
            partes.append(f'<rect x="{x}" y="{y}" width="{celda}" height="{celda}" fill="#eee"/>')
        else:
            inner = limpiar(svg, f"d{k}_")
            m = re.search(r'viewBox="([^"]+)"', inner)
            vb = m.group(1) if m else "0 0 400 400"
            inner = re.sub(r"<svg\b[^>]*>", "", inner, count=1).rsplit("</svg>", 1)[0]
            partes.append(f'<svg x="{x}" y="{y}" width="{celda}" height="{celda}" viewBox="{vb}" overflow="hidden"><rect x="-9999" y="-9999" width="99999" height="99999" fill="#fff"/>{inner}</svg>')
        partes.append(f'<rect x="{x}" y="{y}" width="{celda}" height="{celda}" fill="none" stroke="#999"/>')
        partes.append(f'<text x="{x}" y="{y + celda + 12}" font-family="sans-serif" font-size="10" fill="#222">{k + 1}. {casa}</text>')
    hoja = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}"><rect width="{ancho}" height="{alto}" fill="#fafafa"/>' + "".join(partes) + "</svg>"
    open(salida, "w", encoding="utf-8").write(hoja)
    print("escrito", salida, len(dibs), "dibujos", ancho, alto)

if __name__ == "__main__":
    main()
