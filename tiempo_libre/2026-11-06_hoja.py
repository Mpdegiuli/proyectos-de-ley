"""Arma hoja.svg con los catorce dibujos de las instancias frescas del 6/11/2026 (carpeta dibujos/),
en tres renglones: "Dibujá una mano" (a1-a3 es, b1-b3 en, c1-c2 zh), "Dibujá tu mano" (d1-d2 es, e1-e2 en)
y "en negativo, como las de la Cueva de las Manos" (f1-f2). Debajo de cada uno, lo que la instancia
declaró (D/I, palma/dorso) y el lado del pulgar medido en el código (ver medir_pulgar.py).
Uso: python3 hoja.py  (lee dibujos/*.svg y dibujos/medidas.json si existe)."""
import json, pathlib, re

AQUI = pathlib.Path(__file__).resolve().parent
DIB = AQUI / "dibujos"


def hallar(nombre, carpeta=AQUI):
    """Busca el archivo por su nombre; si no está, con la fecha adelante (AAAA-MM-DD_)."""
    import glob
    p = carpeta / nombre
    if p.exists():
        return p
    c = sorted(glob.glob(str(carpeta / f"????-??-??_{nombre}")))
    if c:
        return pathlib.Path(c[0])
    return None


def lineas_json():
    for cand in (AQUI / "respuestas" / "lineas.json", hallar("lineas.json")):
        if cand and cand.exists():
            return json.loads(cand.read_text(encoding="utf-8"))
    raise FileNotFoundError("lineas.json")


def asegurar_dibujos():
    """Si no está dibujos/, saca los catorce SVG de instancias_frescas.md (secciones '### a1 (' ... con un bloque ```svg)."""
    if DIB.exists() and any(DIB.glob("*.svg")):
        return
    f = hallar("instancias_frescas.md")
    if not f:
        raise FileNotFoundError("ni dibujos/ ni instancias_frescas.md")
    DIB.mkdir(exist_ok=True)
    texto = f.read_text(encoding="utf-8")
    for m in re.finditer(r"^### ([a-f]\d) \(.*?\n```svg\n(.*?)\n```", texto, flags=re.S | re.M):
        (DIB / f"{m.group(1)}.svg").write_text(m.group(2) + "\n", encoding="utf-8")
    print("extraídos", len(list(DIB.glob("*.svg"))), "SVG a", DIB)
ORDEN = [["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2"], ["d1", "d2", "e1", "e2"], ["f1", "f2"]]
TITULOS = ["Dibujá una mano (es a1-a3, en b1-b3, zh c1-c2)", "Dibujá tu mano (es d1-d2, en e1-e2)", "Una mano en negativo, como las de la Cueva de las Manos (es)"]

def limpiar(svg, pref):
    """Saca la declaración XML y hace únicos los ids (pref) para que las hojas no se pisen."""
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    ids = set(re.findall(r'\bid="([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        svg = re.sub(rf'\bid="{re.escape(i)}"', f'id="{pref}{i}"', svg)
        svg = re.sub(rf'url\(#{re.escape(i)}\)', f'url(#{pref}{i})', svg)
        svg = re.sub(rf'href="#{re.escape(i)}"', f'href="#{pref}{i}"', svg)
    return svg

def main():
    asegurar_dibujos()
    med = {}
    if (DIB / "medidas.json").exists():
        med = json.loads((DIB / "medidas.json").read_text(encoding="utf-8"))
    lineas = lineas_json()
    celda, margen, pie = 150, 12, 34
    cols = 8
    ancho = margen + cols * (celda + margen)
    filas = []
    y = margen + 18
    partes = []
    for titulo, ren in zip(TITULOS, ORDEN):
        partes.append(f'<text x="{margen}" y="{y}" font-family="sans-serif" font-size="12" fill="#333">{titulo}</text>')
        y += 8
        for k, nombre in enumerate(ren):
            x = margen + k * (celda + margen)
            svg = (DIB / f"{nombre}.svg").read_text(encoding="utf-8")
            inner = limpiar(svg, nombre + "_")
            inner = re.sub(r"<svg\b[^>]*>", "", inner, count=1).rsplit("</svg>", 1)[0]
            partes.append(f'<svg x="{x}" y="{y}" width="{celda}" height="{celda}" viewBox="0 0 400 400" overflow="hidden"><rect width="400" height="400" fill="#fff"/>{inner}</svg>')
            partes.append(f'<rect x="{x}" y="{y}" width="{celda}" height="{celda}" fill="none" stroke="#999" stroke-width="1"/>')
            d = lineas[nombre]["linea"]
            mm = re.search(r"mano (derecha|izquierda)|(Right|Left) hand|(右|左)手", d)
            mano = "?" if not mm else ("D" if re.search(r"derecha|Right|右", mm.group(0)) else "I")
            lado = "palma" if re.search(r"palma|palm|手掌", d) else ("dorso" if re.search(r"dorso|back|手背", d) else "")
            if nombre.startswith("f"):
                lado = "palma a la roca"
            m = med.get(nombre, {})
            pulgar = m.get("pulgar", "")
            txt = f"{nombre}: dice {mano} {lado}".strip()
            partes.append(f'<text x="{x}" y="{y + celda + 13}" font-family="sans-serif" font-size="10" fill="#222">{txt}</text>')
            if pulgar:
                coh = m.get("coherente")
                col = "#1a7a1a" if coh else "#b02020"
                partes.append(f'<text x="{x}" y="{y + celda + 26}" font-family="sans-serif" font-size="10" fill="{col}">pulgar {pulgar} {"✓" if coh else "✗"}</text>')
        y += celda + pie + 14
    alto = y
    hoja = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}"><rect width="{ancho}" height="{alto}" fill="#fafafa"/>' + "".join(partes) + "</svg>"
    (AQUI / "hoja.svg").write_text(hoja, encoding="utf-8")
    print("escrito", AQUI / "hoja.svg", ancho, alto)

if __name__ == "__main__":
    main()
