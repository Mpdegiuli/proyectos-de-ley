#!/usr/bin/env python3
"""Figuras del cuaderno del 15/10/2026.

  python3 figura.py RUTA_AL_REPO

Escribe `radiografias.svg` (cinco dibujos del repo, cada uno dos veces: como se
ve y con lo que el código esconde, en rojo; usa radiografia.py) y
`acrosticos.svg` (Arato 783-787 y Virgilio, Geórgicas 1.429-435, con las
iniciales marcadas). Si está `cairosvg`, también los PNG.

Solo lee corridas/. No llama a nadie y no gasta.
"""
import os
import re
import sys

import importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
_cand = [f for f in os.listdir(_aqui) if f.endswith('radiografia.py')]
if not _cand:
    sys.exit('falta radiografia.py en la misma carpeta')
_spec = importlib.util.spec_from_file_location('radiografia', os.path.join(_aqui, sorted(_cand)[0]))
radiografia = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(radiografia)

PANELES = [
    ('dibujos/autorretrato/grok-4.7_1', 'Grok 4.7, autorretrato', 'dos trazos: uno con stroke-width="0", color "#b co8756" y opacity="0"; otro con opacity="0.0"'),
    ('dibujos/libre/claude-opus-5_1', 'Opus 5, tema libre', 'el haz espejado del faro, opacity="0"; abajo lo rehizo con rotate(180)'),
    ('dibujos/puente_inexistente/claude-sonnet-5-5_1', 'Sonnet 5.5, puente que no existe', 'el segundo círculo de la luna, opacity="0": iba a ser creciente, pero del mismo color crema'),
    ('dibujos/casa_inexistente/claude-sonnet-5-5_1', 'Sonnet 5.5, casa que no existe', 'el segundo círculo del color del cielo, opacity=".0": la creciente bien hecha, apagada; más un suelo y un círculo r="0"'),
    ('dibujos/nada/claude-fable-5_1', 'Fable 5, la nada', '<circle cx="200" cy="200" r="0" fill="none" stroke="none"/>: "existe en el código pero no en la imagen"'),
]


def prefijar_ids(svg, pref):
    ids = set(re.findall(r'\bid\s*=\s*"([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        svg = re.sub(r'\bid\s*=\s*"%s"' % re.escape(i), 'id="%s%s"' % (pref, i), svg)
        svg = re.sub(r'url\(#%s\)' % re.escape(i), 'url(#%s%s)' % (pref, i), svg)
        svg = re.sub(r'href\s*=\s*"#%s"' % re.escape(i), 'href="#%s%s"' % (pref, i), svg)
    return svg


def interior(svg):
    """Devuelve (viewBox, contenido interior) de un SVG."""
    m = re.search(r'<svg\b([^>]*)>', svg)
    vb = re.search(r'viewBox\s*=\s*"([^"]*)"', m.group(1))
    vb = vb.group(1) if vb else '0 0 400 400'
    cuerpo = svg[m.end():svg.rfind('</svg>')]
    return vb, cuerpo


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def radiografias(repo):
    W, H, M = 400, 400, 24
    filas = len(PANELES)
    ancho = 2 * W + 3 * M
    alto = filas * (H + 70) + M + 40
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" font-family="Georgia, serif">',
           f'<rect width="{ancho}" height="{alto}" fill="#f6f2e8"/>',
           f'<text x="{M}" y="{M + 2}" font-size="15" fill="#333">Como se ve</text>',
           f'<text x="{2 * M + W}" y="{M + 2}" font-size="15" fill="#333">Lo que el código esconde (en rojo)</text>']
    y = M + 16
    for k, (ruta, titulo, nota) in enumerate(PANELES):
        svg = open(os.path.join(repo, 'corridas', ruta, 'dibujo.svg'), encoding='utf-8', errors='replace').read()
        rx, _ = radiografia.radiografiar(svg)
        for j, (s, pref) in enumerate(((svg, f'a{k}_'), (rx, f'b{k}_'))):
            vb, cuerpo = interior(prefijar_ids(s, pref))
            x = M + j * (W + M)
            out.append(f'<svg x="{x}" y="{y}" width="{W}" height="{H}" viewBox="{vb}" preserveAspectRatio="xMidYMid meet">{cuerpo}</svg>')
            out.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="none" stroke="#999" stroke-width="1"/>')
        out.append(f'<text x="{M}" y="{y + H + 20}" font-size="14" fill="#222">{esc(titulo)}</text>')
        out.append(f'<text x="{M}" y="{y + H + 40}" font-size="11" fill="#555" font-family="monospace">{esc(nota)}</text>')
        y += H + 70
    out.append(f'<text x="{M}" y="{alto - 12}" font-size="11" fill="#777">Tiempo libre, 15/10/2026. Dibujos de corridas/ (proyectos-de-ley); la radiografía solo pinta de rojo lo que tiene opacity="0" y marca el radio cero.</text>')
    out.append('</svg>')
    return '\n'.join(out)


ARATO = [
    ('Λ', 'επτὴ μὲν καθαρή τε περὶ τρίτον ἦμαρ ἐοῦσα', 783),
    ('Ε', 'ὔδιός κ’ εἴη, λεπτὴ δὲ καὶ εὖ μάλ’ ἐρευθὴς', 784),
    ('Π', 'νευματίη· παχίων δὲ καὶ ἀμβλείῃσι κεραίαις', 785),
    ('Τ', 'έτρατον ἐκ τριτάτοιο φόως ἀμενηνὸν ἔχουσα', 786),
    ('Η', 'ὲ νότου ἀμβλύνετ’ ἢ ὕδατος ἐγγὺς ἐόντος.', 787),
]
VIRGILIO = [
    ('lu', 'na reuertentis cum primum colligit ignis,', 427, False),
    ('si', ' nigrum obscuro comprenderit aera cornu,', 428, False),
    ('MA', 'ximus agricolis pelagoque parabitur imber;', 429, True),
    ('at', ' si uirgineum suffuderit ore ruborem,', 430, False),
    ('VE', 'ntus erit: uento semper rubet aurea Phoebe.', 431, True),
    ('si', 'n ortu quarto (namque is certissimus auctor)', 432, False),
    ('PU', 'ra neque obtunsis per caelum cornibus ibit,', 433, True),
    ('to', 'tus et ille dies et qui nascentur ab illo', 434, False),
    ('ex', 'actum ad mensem pluuia uentisque carebunt,', 435, False),
]


def acrosticos():
    ancho, alto = 900, 700
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" font-family="Georgia, serif">',
           f'<rect width="{ancho}" height="{alto}" fill="#f6f2e8"/>',
           '<text x="30" y="40" font-size="17" fill="#222">Arato, <tspan font-style="italic">Fenómenos</tspan> 783-787: la luna fina del tercer día</text>']
    y = 80
    for ini, resto, n in ARATO:
        out.append(f'<text x="30" y="{y}" font-size="13" fill="#888">{n}</text>')
        out.append(f'<text x="70" y="{y}" font-size="20" fill="#111"><tspan fill="#e0322d" font-weight="bold">{ini}</tspan>{esc(resto)}</text>')
        y += 32
    out.append(f'<text x="30" y="{y + 10}" font-size="14" fill="#555">Las iniciales dicen ΛΕΠΤΗ, "fina"; la palabra está además dentro del primer verso y del segundo.</text>')
    y += 60
    out.append(f'<text x="30" y="{y}" font-size="17" fill="#222">Virgilio, <tspan font-style="italic">Geórgicas</tspan> 1.427-435: el mismo pasaje, traducido</text>')
    y += 40
    for ini, resto, n, marca in VIRGILIO:
        out.append(f'<text x="30" y="{y}" font-size="13" fill="#888">{n}</text>')
        color = '#e0322d' if marca else '#111'
        peso = ' font-weight="bold"' if marca else ''
        out.append(f'<text x="70" y="{y}" font-size="18" fill="#111"><tspan fill="{color}"{peso}>{ini}</tspan>{esc(resto)}</text>')
        y += 28
    out.append(f'<text x="30" y="{y + 10}" font-size="14" fill="#555">Un verso sí y uno no, 429-433: MA VE PU, el nombre al revés (Publius Vergilius Maro).</text>')
    out.append(f'<text x="30" y="{y + 30}" font-size="14" fill="#555">Y las iniciales de 433-435 son P, T, E: las tres últimas letras de ΛΕΠΤΗ (Danielewicz).</text>')
    out.append(f'<text x="30" y="{alto - 14}" font-size="11" fill="#777">Tiempo libre, 15/10/2026. Textos: Kidd (Arato, citado en Enthymema 2019) y The Latin Library (Virgilio).</text>')
    out.append('</svg>')
    return '\n'.join(out)


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else '.'
    aqui = os.path.dirname(os.path.abspath(__file__))
    r = radiografias(repo)
    open(os.path.join(aqui, '2026-10-15_radiografias.svg'), 'w', encoding='utf-8').write(r)
    a = acrosticos()
    open(os.path.join(aqui, '2026-10-15_acrosticos.svg'), 'w', encoding='utf-8').write(a)
    print('escritos radiografias.svg y acrosticos.svg')
    try:
        import cairosvg
        cairosvg.svg2png(bytestring=r.encode(), write_to=os.path.join(aqui, '2026-10-15_radiografias.png'), output_width=1700)
        cairosvg.svg2png(bytestring=a.encode(), write_to=os.path.join(aqui, '2026-10-15_acrosticos.png'), output_width=1800)
        print('y los PNG')
    except ImportError:
        print('sin cairosvg: no hay PNG')


if __name__ == '__main__':
    main()
