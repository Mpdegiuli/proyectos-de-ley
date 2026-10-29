#!/usr/bin/env python3
"""Figura del cuaderno del 25/10/2026: tres casas de los rumores.

1. Dibuja la mía (`casa_rumores_propia.svg`), escrita a ciegas: una jaula de
   mimbre de sesenta millas que no entra en el cuadro, girando sobre su eje,
   con el castillo de la Fama en su roca de hielo para dar la escala, las
   noticias que crecen de boca en boca como los círculos del águila, y una
   mentira y una verdad trabadas en una ventana.
2. Arma `tres_casas.svg` con los tres dibujos (de memoria, con el texto,
   propio) lado a lado. Los `id` de cada panel llevan un prefijo para que
   los degradados de un dibujo no pisen los de otro (el problema de los
   cuadernillos del 30/9).

Busca los SVG de las instancias en la carpeta de trabajo o al lado, con el
prefijo de fecha. Solo biblioteca estándar.
"""
import math
import random
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FECHA = "2026-10-25"


def casa_propia() -> str:
    rng = random.Random(1400)
    p = []
    w, h = 400, 400
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">')
    p.append('<defs>'
             '<linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0" stop-color="#1b1f3a"/><stop offset="1" stop-color="#4a4f7a"/>'
             '</linearGradient>'
             '<linearGradient id="hielo" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0" stop-color="#dff3ff"/><stop offset="1" stop-color="#8fbfe0"/>'
             '</linearGradient>'
             '</defs>')
    p.append('<rect width="400" height="400" fill="url(#cielo)"/>')
    # valle
    p.append('<path d="M0 300 Q 100 270 200 300 T 400 300 L 400 400 L 0 400 Z" fill="#2f4a2f"/>')
    # la roca de hielo con el castillo, chiquitos, a la izquierda: la escala
    p.append('<path d="M20 300 L 45 215 L 75 300 Z" fill="url(#hielo)" stroke="#9cc" stroke-width="1"/>')
    # nombres grabados: del lado del sol (derecha) borrosos, del lado de la sombra nítidos
    for i in range(5):
        y = 240 + i * 11
        p.append(f'<line x1="{36 + i}" y1="{y}" x2="{46 + i}" y2="{y}" stroke="#235" stroke-width="1.2"/>')
        p.append(f'<line x1="{50 + i}" y1="{y}" x2="{58 + i}" y2="{y}" stroke="#235" stroke-width="1.2" opacity="{0.15 + 0.1 * i}" stroke-dasharray="1 2"/>')
    p.append('<rect x="37" y="200" width="16" height="16" fill="#cfc8b8" stroke="#555" stroke-width="0.8"/>')
    for x in (37, 43, 49):
        p.append(f'<rect x="{x}" y="196" width="4" height="4" fill="#cfc8b8" stroke="#555" stroke-width="0.6"/>')
    p.append('<text x="45" y="190" font-family="serif" font-size="8" fill="#eee" text-anchor="middle">Fama</text>')
    # la jaula: un cilindro de mimbre acostado que sale del cuadro por los dos lados
    cx, cy, ry = 200, 230, 70
    p.append('<g id="jaula">')
    p.append(f'<rect x="-10" y="{cy - ry}" width="420" height="{2 * ry}" fill="#8a6a3a" opacity="0.35"/>')
    # varillas longitudinales (curvas por la perspectiva del cilindro)
    colores = ["#d9b35a", "#b9413a", "#4f8a3f", "#eee8d5"]
    n = 14
    for i in range(n):
        t = (i + 0.5) / n
        y = cy - ry * math.cos(math.pi * t)
        grosor = 1.5 + 2.5 * math.sin(math.pi * t)
        c = colores[i % 4]
        p.append(f'<line x1="-10" y1="{y:.1f}" x2="410" y2="{y:.1f}" stroke="{c}" stroke-width="{grosor:.1f}" opacity="0.9"/>')
    # aros transversales
    for k in range(-1, 11):
        x = 40 * k + 20
        p.append(f'<ellipse cx="{x}" cy="{cy}" rx="7" ry="{ry}" fill="none" stroke="#5b3f1e" stroke-width="1.2" opacity="0.8"/>')
    # mil agujeros (bueno, ciento veinte) por donde sale el ruido
    for _ in range(120):
        x = rng.uniform(-5, 405)
        t = rng.uniform(0.08, 0.92)
        y = cy - ry * math.cos(math.pi * t)
        r = rng.uniform(1.2, 3.2) * (0.6 + math.sin(math.pi * t))
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#120f1a"/>')
    # puertas abiertas día y noche, sin portero
    for k in range(5):
        x = 60 + 70 * k
        p.append(f'<rect x="{x}" y="{cy + 25}" width="16" height="42" fill="#120f1a"/>')
        p.append(f'<path d="M{x} {cy + 25} L {x - 11} {cy + 20} L {x - 11} {cy + 62} L {x} {cy + 67} Z" fill="#7a5a30" stroke="#3a2a10" stroke-width="0.8"/>')
    p.append('</g>')
    # flechas de giro sobre el eje largo (gira como un tronco rodando)
    p.append(f'<path d="M 120 {cy - ry - 14} A 90 20 0 0 1 280 {cy - ry - 14}" fill="none" stroke="#ddd" stroke-width="1.2" stroke-dasharray="4 3"/>')
    p.append(f'<path d="M 280 {cy - ry - 14} l -8 -5 l 2 8 z" fill="#ddd"/>')
    p.append(f'<path d="M 280 {cy + ry + 14} A 90 20 0 0 1 120 {cy + ry + 14}" fill="none" stroke="#ddd" stroke-width="1.2" stroke-dasharray="4 3"/>')
    p.append(f'<path d="M 120 {cy + ry + 14} l 8 5 l -2 -8 z" fill="#ddd"/>')
    # noticias que crecen de boca en boca: círculos cada vez más anchos, como los del agua
    for i, (x, r) in enumerate(((150, 3), (190, 6), (240, 11), (300, 18), (370, 28))):
        p.append(f'<circle cx="{x}" cy="{cy}" r="{r}" fill="none" stroke="#ffd166" stroke-width="1.3" opacity="{0.95 - 0.12 * i}"/>')
        if i:
            p.append(f'<line x1="{x - r - 4}" y1="{cy}" x2="{x - r - 14}" y2="{cy}" stroke="#ffd166" stroke-width="1" stroke-dasharray="2 2"/>')
    # una chispa
    p.append(f'<circle cx="150" cy="{cy}" r="1.2" fill="#fff"/>')
    # una mentira (negra) y una verdad (blanca) trabadas en una ventana
    vx, vy = 330, cy - 48
    p.append(f'<rect x="{vx - 10}" y="{vy - 9}" width="20" height="18" fill="#120f1a" stroke="#d9b35a" stroke-width="1.2"/>')
    p.append(f'<ellipse cx="{vx - 4}" cy="{vy}" rx="5" ry="7" fill="#eee"/>')
    p.append(f'<ellipse cx="{vx + 4}" cy="{vy}" rx="5" ry="7" fill="#222" stroke="#eee" stroke-width="0.8"/>')
    # el águila, posada en una piedra, y el soñador abajo
    p.append(f'<path d="M 352 {cy + ry + 40} l 10 -6 l 10 6 l -6 2 l -4 10 l -4 -10 z" fill="#d9b35a"/>')
    p.append(f'<rect x="350" y="{cy + ry + 50}" width="24" height="8" fill="#555"/>')
    p.append(f'<circle cx="318" cy="{cy + ry + 48}" r="4" fill="#eee"/>')
    p.append(f'<line x1="318" y1="{cy + ry + 52}" x2="318" y2="{cy + ry + 66}" stroke="#eee" stroke-width="2"/>')
    p.append(f'<line x1="310" y1="{cy + ry + 58}" x2="326" y2="{cy + ry + 58}" stroke="#eee" stroke-width="2"/>')
    p.append('<text x="200" y="388" font-family="serif" font-size="9" fill="#ddd" text-anchor="middle">'
             'sixty myle of lengthe: no entra en el cuadro</text>')
    p.append('</svg>')
    return "\n".join(p)


def buscar(nombre: str) -> Path:
    for carpeta in (AQUI, AQUI.parent, Path.cwd()):
        for cand in (carpeta / f"{FECHA}_{nombre}", carpeta / nombre):
            if cand.exists():
                return cand
    sys.exit(f"no encuentro {nombre}")


def prefijar_ids(svg: str, prefijo: str) -> str:
    ids = set(re.findall(r'\bid="([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        svg = svg.replace(f'id="{i}"', f'id="{prefijo}{i}"')
        svg = svg.replace(f'url(#{i})', f'url(#{prefijo}{i})')
        svg = svg.replace(f'href="#{i}"', f'href="#{prefijo}{i}"')
    return svg


def panel(svg: str, x: int, prefijo: str) -> str:
    svg = prefijar_ids(svg, prefijo)
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg)
    # fija tamaño y posición en el panel
    svg = re.sub(r"<svg\b([^>]*)>", lambda m: "<svg" + re.sub(r'\s(width|height|x|y)="[^"]*"', "", m.group(1))
                 + f' x="{x}" y="30" width="400" height="400">', svg, count=1)
    return svg


def main() -> None:
    propia = casa_propia()
    (AQUI / f"{FECHA}_casa_rumores_propia.svg").write_text(propia, encoding="utf-8")
    memoria = buscar("casa_rumores_memoria.svg").read_text(encoding="utf-8")
    texto = buscar("casa_rumores_texto.svg").read_text(encoding="utf-8")
    partes = ['<svg xmlns="http://www.w3.org/2000/svg" width="1260" height="470" viewBox="0 0 1260 470">',
              '<rect width="1260" height="470" fill="#fafaf7"/>']
    titulos = ["De memoria, sin el texto (instancia fresca)",
               "Con el texto de Skeat, vv. 1918-2093 (instancia fresca)",
               "La mía, escrita a ciegas (figura.py)"]
    for i, (svg, t) in enumerate(zip((memoria, texto, propia), titulos)):
        x = 20 + i * 410
        partes.append(f'<text x="{x + 200}" y="20" font-family="sans-serif" font-size="13" fill="#333" text-anchor="middle">{t}</text>')
        partes.append(panel(svg, x, f"p{i}_"))
        partes.append(f'<rect x="{x}" y="30" width="400" height="400" fill="none" stroke="#999" stroke-width="1"/>')
    partes.append('<text x="630" y="455" font-family="sans-serif" font-size="12" fill="#555" text-anchor="middle">'
                  'Tres casas de los rumores (Chaucer, The House of Fame, III, 1918-2158), 25/10/2026</text>')
    partes.append("</svg>")
    (AQUI / f"{FECHA}_tres_casas.svg").write_text("\n".join(partes), encoding="utf-8")
    print("escritos", f"{FECHA}_casa_rumores_propia.svg", f"{FECHA}_tres_casas.svg")


if __name__ == "__main__":
    main()
