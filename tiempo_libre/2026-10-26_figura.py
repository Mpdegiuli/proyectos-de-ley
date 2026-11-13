#!/usr/bin/env python3
"""Dibuja `pisadas.svg`: cuatro teclados de C3 a C6 con las pisadas de cada
secuencia del cuaderno, en el orden en que suenan. Importa las secuencias de
gato.py (misma semilla). Solo biblioteca estándar; el PNG lo hace render.py.
"""
import random

import gato

BAJA, ALTA = 48, 84  # C3 .. C6
W_BLANCA = 30.0      # px por tecla blanca (la escala real es 23,5 mm)
H_BLANCA = 110.0
H_NEGRA = 68.0
W_NEGRA = 17.0
MARGEN_X = 40.0
ANCHO = MARGEN_X * 2 + 22 * W_BLANCA


def blancas_hasta(m):
    """cuántas teclas blancas hay desde BAJA hasta m (sin contar m)."""
    return sum(1 for k in range(BAJA, m) if gato.ES_BLANCA[k % 12])


def centro_x(m):
    if gato.ES_BLANCA[m % 12]:
        return MARGEN_X + (blancas_hasta(m) + 0.5) * W_BLANCA
    return MARGEN_X + blancas_hasta(m + 1) * W_BLANCA  # límite entre las dos blancas


def teclado(y0, titulo, nota_titulo):
    s = [f'<text x="{MARGEN_X}" y="{y0 - 28}" class="t">{titulo}</text>',
         f'<text x="{MARGEN_X}" y="{y0 - 10}" class="n">{nota_titulo}</text>']
    # blancas
    i = 0
    for m in range(BAJA, ALTA + 1):
        if gato.ES_BLANCA[m % 12]:
            x = MARGEN_X + i * W_BLANCA
            s.append(f'<rect x="{x:.1f}" y="{y0}" width="{W_BLANCA:.1f}" height="{H_BLANCA}" class="b"/>')
            if m % 12 == 0:
                s.append(f'<text x="{x + W_BLANCA / 2:.1f}" y="{y0 + H_BLANCA - 8}" class="c">C{m // 12 - 1}</text>')
            i += 1
    # negras
    for m in range(BAJA, ALTA + 1):
        if not gato.ES_BLANCA[m % 12]:
            x = centro_x(m) - W_NEGRA / 2
            s.append(f'<rect x="{x:.1f}" y="{y0}" width="{W_NEGRA}" height="{H_NEGRA}" class="k"/>')
    return s


def pisadas(y0, midis, color, etiquetas=None, racimos=True):
    """Marca cada nota con un círculo numerado por orden de aparición; las notas
    de teclas vecinas consecutivas (racimo de una pata) van unidas por un trazo."""
    s = []
    pos = []
    for j, m in enumerate(midis):
        x = centro_x(m)
        y = y0 + (H_NEGRA - 14 if not gato.ES_BLANCA[m % 12] else H_BLANCA - 36)
        # si la misma tecla ya sonó, el círculo baja un poco para que se vea
        repes = sum(1 for k in midis[:j] if k == m)
        y -= 20 * repes
        pos.append((x, y))
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{color}" stroke="#222" stroke-width="0.8"/>')
        et = (etiquetas[j] if etiquetas else str(j + 1))
        s.append(f'<text x="{x:.1f}" y="{y + 3.5:.1f}" class="p">{et}</text>')
    if racimos:
        for j in range(1, len(midis)):
            if 0 < midis[j] - midis[j - 1] <= 2:
                (x1, y1), (x2, y2) = pos[j - 1], pos[j]
                s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="5" opacity="0.5"/>')
    return s


def main():
    rng = random.Random(20261026)
    simple = gato.paseo_de_gato(rng, n_pisadas=5, zancada=12.0, desvio=3.0, vecina=0.5)[:8]
    azar = [rng.randint(48, 84) for _ in range(7)]
    registra = gato.gato_que_registra(random.Random(20261027), n_pasos=4, paso=10.0, desvio=2.5, vecina=0.5)

    paneles = [
        ("Scarlatti, K.30, el tema (G B♭ E♭ F♯ B♭ C♯ D): cada paso, 1 a 7 cm hacia la derecha; nada se repite",
         "Lo que la leyenda atribuye al gato. Siete notas, una sola dirección, ninguna tecla vecina.", gato.SCARLATTI, "#e4b04a", None),
        ("Gato simple (el de la primera prueba): una pisada cada 12 ± 3 cm, a veces dos teclas vecinas",
         "Elegido como gato por 1 de 4 instancias frescas; las otras tres eligieron el azar.", simple, "#6aa0d8", None),
        ("Gato que registra: la trasera vuelve a pisar donde pisó la delantera (D = delantera, T = trasera)",
         "Elegido como gato por 2 de 2 instancias frescas. Cada estación suena dos veces: el gato camina en canon.", registra, "#7cc07a",
         ['D1', 'D1', 'D2', 'D2', 'T1', 'T1', 'D3', 'D3', 'T2', 'T2', 'D4', 'T3', 'T3', 'T4']),
        ("Siete notas al azar entre C3 y C6",
         "Elegido como gato por 3 de 4 instancias en la primera prueba; \"lo contrario de un gato\" en la segunda.", azar, "#d98a8a", None),
    ]
    alto_panel = H_BLANCA + 64
    alto = 40 + alto_panel * len(paneles) + 30
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO:.0f}" height="{alto:.0f}" viewBox="0 0 {ANCHO:.0f} {alto:.0f}">',
           '<style>text{font-family:Georgia,serif} .t{font-size:14px;fill:#222} .n{font-size:12px;fill:#555;font-style:italic} '
           '.c{font-size:10px;fill:#888;text-anchor:middle} .p{font-size:9px;fill:#111;text-anchor:middle;font-family:Helvetica,Arial,sans-serif} '
           '.b{fill:#fbfaf6;stroke:#777;stroke-width:0.8} .k{fill:#2a2a2a}</style>',
           f'<rect width="{ANCHO:.0f}" height="{alto:.0f}" fill="#ffffff"/>',
           f'<text x="{MARGEN_X}" y="26" style="font-size:17px;fill:#111">Pisadas sobre el teclado, de C3 a C6 (una tecla blanca = 23,5 mm en el piano; acá, {W_BLANCA:.0f} px)</text>']
    for i, (titulo, nota, midis, color, et) in enumerate(paneles):
        y0 = 40 + 44 + i * alto_panel
        out += teclado(y0, titulo, nota)
        out += pisadas(y0, midis, color, et, racimos=(i in (1, 2)))
    out.append(f'<text x="{MARGEN_X}" y="{alto - 10}" class="n">Los números dan el orden en que suena cada nota; en los dos gatos, el trazo une las dos teclas vecinas de una misma pisada. figura.py, 26/10/2026.</text>')
    out.append('</svg>')
    open('pisadas.svg', 'w', encoding='utf-8').write('\n'.join(out))
    print('escrito pisadas.svg')


if __name__ == '__main__':
    main()
