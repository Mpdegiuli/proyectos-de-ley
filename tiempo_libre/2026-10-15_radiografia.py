#!/usr/bin/env python3
"""Radiografía de un dibujo.svg: vuelve visibles, en rojo, los elementos que el
autor dejó con opacity="0", "0.0" o ".0" (y no animó), y marca con un punto rojo los
círculos de radio cero. Lo demás queda como está.

Uso: python3 radiografia.py entrada.svg salida.svg

Solo lee el archivo que se le pasa. Cuaderno de tiempo libre del 15/10/2026.
"""
import re
import sys

ROJO = '#e0322d'


def radiografiar(svg):
    salida = []
    pos = 0
    n = 0
    # elementos (no <stop>) con opacity="0" o "0.0"
    patron = re.compile(r'<(?P<tag>circle|path|g|polygon|line|rect|text|ellipse|polyline)\b(?P<attrs>[^>]*?)\bopacity\s*=\s*"(?:0|0\.0+|\.0+)"(?P<resto>[^>]*)>')
    for m in patron.finditer(svg):
        # si el elemento está animado (tiene <animate> adentro o enseguida), no es un secreto: se deja
        if '<animate' in svg[m.end():m.end() + 300] and m.group('tag') != 'g':
            continue
        if m.group('tag') == 'g' and '<animate' in svg[m.end():svg.find('</g>', m.end())]:
            continue
        attrs = m.group('attrs') + m.group('resto')
        cierre = ''
        if attrs.rstrip().endswith('/'):
            attrs = attrs.rstrip()[:-1]
            cierre = '/'
        # saco stroke-width="0" para que se vea el trazo
        attrs = re.sub(r'\bstroke-width\s*=\s*"0(?:\.0+)?"', 'stroke-width="2.5"', attrs)
        # relleno/trazo en rojo: si tenía fill distinto de none, lo pinto; si tenía stroke, lo pinto
        tiene_fill_none = re.search(r'\bfill\s*=\s*"none"', attrs)
        attrs = re.sub(r'\bfill\s*=\s*"[^"]*"', '', attrs)
        attrs = re.sub(r'\bstroke\s*=\s*"[^"]*"', '', attrs)
        if m.group('tag') in ('line', 'polyline') or tiene_fill_none:
            attrs += f' fill="none" stroke="{ROJO}"'
            if 'stroke-width' not in attrs:
                attrs += ' stroke-width="2.5"'
        else:
            attrs += f' fill="{ROJO}" fill-opacity="0.75" stroke="{ROJO}" stroke-width="1.5"'
        nuevo = f'<{m.group("tag")}{attrs} opacity="1"{cierre}>'
        salida.append(svg[pos:m.start()])
        salida.append(nuevo)
        pos = m.end()
        n += 1
    salida.append(svg[pos:])
    svg = ''.join(salida)
    # círculos de radio cero: un punto rojo chico, con un anillo
    def punto(m):
        nonlocal n
        n += 1
        cx, cy = m.group('cx'), m.group('cy')
        return (f'<circle cx="{cx}" cy="{cy}" r="4" fill="{ROJO}"/>'
                f'<circle cx="{cx}" cy="{cy}" r="14" fill="none" stroke="{ROJO}" stroke-width="1.5" stroke-dasharray="3 3"/>')
    svg = re.sub(r'<circle\b[^>]*\bcx\s*=\s*"(?P<cx>[^"]*)"[^>]*\bcy\s*=\s*"(?P<cy>[^"]*)"[^>]*\br\s*=\s*"0(?:\.0+)?"[^>]*/>', punto, svg)
    return svg, n


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    svg = open(sys.argv[1], encoding='utf-8', errors='replace').read()
    nuevo, n = radiografiar(svg)
    open(sys.argv[2], 'w', encoding='utf-8').write(nuevo)
    print(f'{n} elementos revelados -> {sys.argv[2]}')


if __name__ == '__main__':
    main()
