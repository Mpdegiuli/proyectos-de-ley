#!/usr/bin/env python3
"""El motor de Lagado, con el vocabulario de Gulliver.

Cuaderno de tiempo libre del 28/10/2026. Solo biblioteca estándar.

Lee el texto de Gulliver's Travels (Project Gutenberg n.º 829, archivo 829-0.txt,
tomado del clon de github.com/GITenberg/Gulliver-s-Travels_829 porque gutenberg.org
no se deja abrir desde este entorno), arma tres motores y mide, para cada uno, qué
fracción de las ventanas de tres y de cuatro palabras seguidas "podrían formar parte
de una oración", con el criterio más tacaño posible: que esa secuencia exacta aparezca
en algún lugar del libro.

  orden cero   : cada cara del dado trae una palabra del vocabulario, todas igual de
                 probables ("sin ningún orden"; Shannon 1948 no la da por palabras).
  primer orden : cada cara trae una palabra con la frecuencia que tiene en el libro
                 ("la proporción general que hay en los libros entre las partículas,
                 los sustantivos y los verbos"; la muestra 5 de Shannon).
  segundo orden: cada palabra se elige según la anterior (bigramas; la muestra 6 de
                 Shannon, la que él hizo abriendo un libro al azar).
  el libro     : control: la segunda mitad del libro medida contra la primera.

Uso: python3 lagado.py RUTA_AL_829-0.txt [--semilla N] [--palabras N]
"""
import re
import sys
import random
from collections import Counter, defaultdict

import os
_aqui = os.path.dirname(os.path.abspath(__file__))
_candidatas = [os.path.join(_aqui, "829-0.txt"), os.path.join(_aqui, "2026-10-28_829-0.txt"), "829-0.txt"]
ruta = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else next((c for c in _candidatas if os.path.exists(c)), "829-0.txt")
semilla = 20261028
n_palabras = 200_000
for i, a in enumerate(sys.argv):
    if a == "--semilla":
        semilla = int(sys.argv[i + 1])
    if a == "--palabras":
        n_palabras = int(sys.argv[i + 1])
random.seed(semilla)

texto = open(ruta, encoding="utf-8-sig").read()
ini = texto.find("***START OF THE PROJECT GUTENBERG EBOOK")
fin = texto.find("***END OF THE PROJECT GUTENBERG EBOOK")
if ini >= 0 and fin > ini:
    texto = texto[texto.find("\n", ini) + 1:fin]
texto = re.sub(r"\[Picture:[^\]]*\]", " ", texto)
texto = texto.replace("’", "'")
palabras = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", texto.lower())

N = len(palabras)
# Los motores se cargan con la PRIMERA mitad del libro y se miden contra la SEGUNDA,
# que ninguno vio; el control es la primera mitad medida contra la segunda, que es
# lo que hace un texto de verdad bajo el mismo criterio.
mitad = N // 2
p1, p2 = palabras[:mitad], palabras[mitad:]
vocab = sorted(set(p1))
uni = Counter(p1)
big = defaultdict(Counter)
for a, b in zip(p1, p1[1:]):
    big[a][b] += 1
tri = set(zip(p2, p2[1:], p2[2:]))
cua = set(zip(p2, p2[1:], p2[2:], p2[3:]))
tri_todo = set(zip(palabras, palabras[1:], palabras[2:]))
vocab_todo = len(set(palabras))

print(f"Gulliver's Travels (Gutenberg 829): {N:,} palabras, {vocab_todo:,} distintas, {len(tri_todo):,} trigramas distintos")
print(f"Primera mitad (carga los motores): {mitad:,} palabras, {len(vocab):,} distintas, "
      f"{sum(len(c) for c in big.values()):,} bigramas distintos. Segunda mitad (mide): {len(tri):,} trigramas, {len(cua):,} cuatrigramas")

# --- los motores -----------------------------------------------------------
def orden_cero(n):
    return [random.choice(vocab) for _ in range(n)]

uni_pal = list(uni.keys())
uni_pesos = [uni[w] for w in uni_pal]
def primer_orden(n):
    return random.choices(uni_pal, uni_pesos, k=n)

big_listas = {a: (list(c.keys()), list(c.values())) for a, c in big.items()}
def segundo_orden(n):
    out = [random.choices(uni_pal, uni_pesos, k=1)[0]]
    while len(out) < n:
        a = out[-1]
        if a in big_listas:
            ks, vs = big_listas[a]
            out.append(random.choices(ks, vs, k=1)[0])
        else:
            out.append(random.choices(uni_pal, uni_pesos, k=1)[0])
    return out

def medir(seq, tri_ref, cua_ref):
    t = sum(1 for g in zip(seq, seq[1:], seq[2:]) if g in tri_ref)
    c = sum(1 for g in zip(seq, seq[1:], seq[2:], seq[3:]) if g in cua_ref)
    return t / (len(seq) - 2), c / (len(seq) - 3)

print()
print(f"Ventanas que aparecen tal cual en la segunda mitad del libro (semilla {semilla}, {n_palabras:,} palabras por motor):")
print(f"{'motor':28s} {'3 seguidas':>12s} {'4 seguidas':>12s}")
resultados = {}
for nombre, f in (("orden cero", orden_cero), ("primer orden", primer_orden), ("segundo orden", segundo_orden)):
    seq = f(n_palabras)
    t, c = medir(seq, tri, cua)
    resultados[nombre] = (t, c, seq[:60])
    print(f"{nombre:28s} {100*t:11.3f} % {100*c:11.4f} %")

# control: la primera mitad del libro contra los n-gramas de la segunda
t, c = medir(p1, tri, cua)
print(f"{'el libro (1.ª mitad vs 2.ª)':28s} {100*t:11.3f} % {100*c:11.4f} %")
resultados["el libro"] = (t, c, p1[:60])
# orden cero, de manera exacta: una terna al azar es uno de los trigramas de la segunda mitad con probabilidad |tri|/V³
p0 = len(tri) / len(vocab) ** 3
print(f"{'orden cero (cuenta exacta)':28s} {100*p0:11.6f} %   (una ventana de cada {1/p0:,.0f})")

print()
print("Una línea de cada motor (las primeras 40 palabras):")
for nombre in ("orden cero", "primer orden", "segundo orden"):
    print(f"  {nombre}: " + " ".join(resultados[nombre][2][:40]))

# --- el marco ----------------------------------------------------------------
print()
print("El marco de veinte pies:")
lado_m = 20 * 0.3048
dado_cm = 1.3   # "del tamaño de un dado": supuesto, un dado de 13 mm
por_lado = int(lado_m * 100 / dado_cm)
dados = por_lado ** 2
print(f"  {lado_m:.2f} m de lado; con dados de {dado_cm} cm, {por_lado} por lado, {dados:,} dados, {6*dados:,} caras")
print(f"  el vocabulario de Gulliver ({len(vocab):,} palabras) entra {6*dados/len(vocab):.0f} veces")
ventanas = por_lado * (por_lado - 2)
print(f"  por vuelta de manija, {ventanas:,} ventanas de tres palabras en las {por_lado} líneas")
for nombre, t in (("orden cero", p0), ("primer orden", resultados["primer orden"][0]),
                  ("segundo orden", resultados["segundo orden"][0]), ("el libro", resultados["el libro"][0])):
    print(f"  {nombre:14s}: {t*ventanas:10.2f} fragmentos de tres palabras por vuelta; "
          f"con 4 vueltas por día, {4*t*ventanas:10.1f} por día")
print(f"  orden cero: una vuelta de cada {1/(p0*ventanas):.1f} da un fragmento; a cuatro vueltas por día, uno cada {1/(p0*ventanas)/4:.1f} días")
