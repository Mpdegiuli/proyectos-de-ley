#!/usr/bin/env python3
"""hoja.py — arma hoja.svg con los doce dibujos de las instancias frescas
(dibujos/*.svg) y lo que cada una declaró (lineas.json), en una grilla de 4 × 3:
fila 1, "Dibujá un meteorito" (es, es, en, en, zh, zh) — seis;
fila 2, "una piedra que cayó del cielo" (c1, c2), "la piedra de Ensisheim" (s1, s2),
"un meteorito que no exista" (n1, n2).
Si no existe dibujos/, los saca de instancias_frescas.md.
"""
import json, os, re, html

ORDEN = [("m1", "meteorito (es)"), ("m2", "meteorito (es)"), ("m3", "meteorite (en)"),
         ("m4", "meteorite (en)"), ("m5", "陨石 (zh)"), ("m6", "陨石 (zh)"),
         ("c1", "piedra que cayó del cielo"), ("c2", "piedra que cayó del cielo"),
         ("s1", "la piedra de Ensisheim"), ("s2", "la piedra de Ensisheim"),
         ("n1", "meteorito que no exista"), ("n2", "meteorito que no exista")]

def extraer_de_md():
    md = None
    for n in ("instancias_frescas.md", "2026-11-07_instancias_frescas.md"):
        if os.path.exists(n):
            md = open(n, encoding="utf-8").read(); break
    if md is None:
        raise SystemExit("faltan dibujos/ e instancias_frescas.md")
    os.makedirs("dibujos", exist_ok=True)
    for m in re.finditer(r"### (\w\d) \([^)]*\)\s*\n+```svg\n(.*?)\n```", md, re.S):
        open(f"dibujos/{m.group(1)}.svg", "w", encoding="utf-8").write(m.group(2) + "\n")

def main():
    if not os.path.isdir("dibujos") or not os.path.exists("dibujos/m1.svg"):
        extraer_de_md()
    lineas = json.load(open("lineas.json", encoding="utf-8")) if os.path.exists("lineas.json") else \
             json.load(open("2026-11-07_lineas.json", encoding="utf-8"))
    cel, gap, top, lin = 300, 14, 40, 44
    cols = 6
    W = gap + cols * (cel + gap)
    filas = 2
    H = top + filas * (cel + gap + lin) + 10
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Georgia, serif">',
         f'<rect width="{W}" height="{H}" fill="#f4f1ea"/>',
         f'<text x="{gap}" y="26" font-size="16" fill="#333">Doce meteoritos de instancias frescas, 7/11/2026. Arriba, "Dibujá un meteorito" en tres lenguas; abajo, la piedra, Ensisheim y el que no existe.</text>']
    for i, (k, rotulo) in enumerate(ORDEN):
        f, c = divmod(i, cols)
        x = gap + c * (cel + gap)
        y = top + f * (cel + gap + lin)
        svg = open(f"dibujos/{k}.svg", encoding="utf-8").read()
        # se anida el dibujo completo como <svg> interno con su propio viewBox, sin tocarlo
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg).strip()
        # se quitan width/height propios de la etiqueta raíz y se ponen los de la celda
        cabeza, resto = svg.split(">", 1)
        cabeza = re.sub(r'\s(width|height)="[^"]*"', "", cabeza)
        svg = cabeza.replace("<svg ", f'<svg x="{x}" y="{y}" width="{cel}" height="{cel}" ', 1) + ">" + resto
        # ids repetidos entre dibujos: se prefijan con la clave
        for idm in set(re.findall(r'\bid="([^"]+)"', svg)):
            svg = re.sub(r'\bid="%s"' % re.escape(idm), f'id="{k}_{idm}"', svg)
            svg = svg.replace(f'url(#{idm})', f'url(#{k}_{idm})')
            svg = re.sub(r'href="#%s"' % re.escape(idm), f'href="#{k}_{idm}"', svg)
        o.append(svg)
        o.append(f'<rect x="{x}" y="{y}" width="{cel}" height="{cel}" fill="none" stroke="#999"/>')
        o.append(f'<text x="{x+4}" y="{y+cel+15}" font-size="12" fill="#333">{k}: {html.escape(rotulo)}</text>')
        dec = lineas[k]["linea"]
        corto = dec if len(dec) <= 52 else dec[:50] + "…"
        o.append(f'<text x="{x+4}" y="{y+cel+31}" font-size="10" fill="#555">{html.escape(corto)}</text>')
    o.append("</svg>")
    open("hoja.svg", "w", encoding="utf-8").write("\n".join(o))
    print("hoja.svg", os.path.getsize("hoja.svg"), "bytes")

if __name__ == "__main__":
    main()
