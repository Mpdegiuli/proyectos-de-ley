#!/usr/bin/env python3
"""La urna de la fecha.

Seis instancias frescas, sin herramientas, tenían que "sortear" un patrono entre
doce santos. Ninguna tiró un dado: las seis usaron la fecha del día (11/11/2026)
como fuente de azar, con cuatro fórmulas distintas (y tres resultados):

  A. suma de los dígitos de la fecha, módulo 12            (S2, S3; S4 de yapa)
  B. la fecha como número AAAAMMDD, módulo 12               (S1, S5)
  B'. la fecha al revés, DDMMAAAA, módulo 12                (S4)
  C. día + mes + año, módulo 12                             (S6)

Este script mira qué "urna" es cada fórmula: qué santo sale con cada una para
cada día de 2026, cuántas veces puede salir cada uno, y qué habría salido el
20 de octubre de 1580. Resto 0 = número 12, como declararon las instancias.
"""
from collections import Counter
from datetime import date, timedelta

SANTOS = ["San Andrés", "Santa Bárbara", "San Blas", "San Bernabé",
          "Santa Catalina", "San Lorenzo", "San Martín de Tours",
          "San Nicolás de Bari", "San Pedro", "San Sebastián", "Santiago",
          "Santa Lucía"]

def santo(resto):
    return SANTOS[(resto - 1) % 12]

def f_a(d):  # suma de dígitos de DDMMAAAA (o AAAAMMDD: la suma no cambia)
    return sum(int(c) for c in f"{d.day:02d}{d.month:02d}{d.year:04d}") % 12

def f_b(d):  # AAAAMMDD como número
    return int(f"{d.year:04d}{d.month:02d}{d.day:02d}") % 12

def f_b2(d):  # DDMMAAAA como número (la S4)
    return int(f"{d.day:02d}{d.month:02d}{d.year:04d}") % 12

def f_c(d):  # día + mes + año
    return (d.day + d.month + d.year) % 12

FORMULAS = [("A suma de dígitos", f_a), ("B AAAAMMDD mod 12", f_b),
            ("B' DDMMAAAA mod 12", f_b2), ("C día+mes+año", f_c)]

hoy = date(2026, 11, 11)
print("Hoy, 11/11/2026:")
for nombre, f in FORMULAS:
    print(f"  {nombre:22s} resto {f(hoy):2d} -> {santo(f(hoy))}")

print("\nEl 20 de octubre de 1580 (la fecha del acta; fecha juliana, pero el")
print("número es el número):")
viejo = date(1580, 10, 20)
for nombre, f in FORMULAS:
    print(f"  {nombre:22s} resto {f(viejo):2d} -> {santo(f(viejo))}")

print("\nCada fórmula como urna, sobre los 365 días de 2026 (veces que sale cada santo):")
d = date(2026, 1, 1)
dias = []
while d.year == 2026:
    dias.append(d)
    d += timedelta(days=1)
for nombre, f in FORMULAS:
    c = Counter(santo(f(x)) for x in dias)
    print(f"\n  {nombre}")
    for s in SANTOS:
        n = c.get(s, 0)
        barra = "#" * (n // 4)
        print(f"    {s:20s} {n:3d} {barra}")
    print(f"    santos que nunca salen en el año: {[s for s in SANTOS if c.get(s,0)==0]}")

print("\nDías de 2026 en que la suma de dígitos saca a San Martín de Tours (resto 7):")
print("  ", ", ".join(x.strftime("%d/%m") for x in dias if f_a(x) == 7)[:400], "...")
print("   total:", sum(1 for x in dias if f_a(x) == 7))

print("\nSi la urna fuera de verdad (doce papeles, con reposición):")
print("  P(el mismo nombre tres veces seguidas) = 1/12^2 =", f"{1/144:.4f}")
print("  P(tres de seis sorteos independientes coincidan en algún nombre) ~",
      end=" ")
# cuenta exacta por enumeración de 12^6 resultados
from itertools import product
tot = 12 ** 6
k3 = 0
for r in product(range(12), repeat=6):
    if max(Counter(r).values()) >= 3:
        k3 += 1
print(f"{k3/tot:.3f}")
