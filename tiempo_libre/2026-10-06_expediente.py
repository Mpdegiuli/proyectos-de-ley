#!/usr/bin/env python3
"""Tiempo libre, 6/10/2026. El expediente de Borges en el Nobel, 1956-1975.

Los datos estan copiados a mano de las tablas de nominados de los articulos
"19XX Nobel Prize in Literature" de Wikipedia en ingles, leidas dos veces.
No pude abrir el archivo oficial de nobelprize.org (403).
Solo biblioteca estandar. Uso: python3 expediente.py
"""
import datetime as dt
from collections import Counter

NOMINACIONES = {
    1956: ["Rene Etiemble"],
    1957: [], 1958: [], 1959: [], 1960: [], 1961: [],
    1962: ["Henry Olsson"],
    1963: ["Henry Olsson"],
    1964: ["Henry Olsson"],
    1965: ["Raimundo Lida", "PEN Club sueco"],
    1966: ["Paul Benichou", "Eugenio Florit"],
    1967: ["Henry Olsson", "Raimundo Lida", "Gustaf Freden"],
    1968: [],
    1969: ["Arnold Chapman", "Helmut Kreuzer", "Manuel Duran", "Helen Gardner"],
    1970: ["Arthur E. Gordon", "Helen Gardner", "Manuel Duran",
           "Edward H. Schafer", "Heinrich Bihler"],
    1971: ["Manuel Duran", "Yakov Malkiel", "Andri Peer", "Heinrich Bihler",
           "Christopher Ricks", "Raimundo Lida"],
    1972: ["Kurt L. Levy", "Raimundo Lida"],
    1973: ["Charles Dedeyan", "Raimundo Lida", "Miguel Alfredo Olivera"],
    1974: ["Charles Dedeyan", "Richard Goodwin", "Jonas Kristjansson",
           "Kurt L. Levy", "Sven Skydsgaard", "Kazmer Geza Werner"],
    1975: ["Luis Droguett Alfaro", "Michel Cadot", "Jonas Kristjansson",
           "Aatos Ojala"],
}

# Anios en que, segun lo publicado de los legajos, se lo considero para medio premio.
DE_A_DOS = {
    1965: "con Asturias (se discutio)",
    1966: "con Asturias (se propuso)",
    1967: "con Asturias (primera propuesta de Johnson, Olsson y Lindegren; Gierow, las mismas tres sin orden)",
    1975: "con Aleixandre (segun una fuente secundaria)",
}

# Lo que decidio la Academia en esos anios.
RESULTADO = {1965: "Sholojov", 1966: "Agnon y Sachs", 1967: "Asturias solo",
             1975: "Montale"}

# Parejas para premio compartido que nombran los resumenes de los legajos que lei.
# (anio en que aparece, mitad A, mitad B, que paso)
PAREJAS = [
    (1965, "Sholojov", "Ajmatova", "A solo (1965)"),
    (1965, "Asturias", "Borges", "A solo (1967)"),
    (1965, "Agnon", "Sachs", "juntos (1966)"),
    (1966, "Sachs", "Celan", "A sin B (1966, con Agnon)"),
    (1974, "Johnson", "Martinson", "juntos (1974)"),
    (1974, "Gordimer", "Lessing", "cada una sola (1991 y 2007)"),
    (1974, "Bellow", "Mailer", "A solo (1976)"),
    (1975, "Aleixandre", "Borges", "A solo (1977)"),
]


def main():
    total = sum(len(v) for v in NOMINACIONES.values())
    con = [a for a, v in NOMINACIONES.items() if v]
    cuenta = Counter(n for v in NOMINACIONES.values() for n in v)
    print("anio  n  nominadores")
    for a in sorted(NOMINACIONES):
        v = NOMINACIONES[a]
        print(f"{a}  {len(v)}  {'; '.join(v) if v else '-'}")
    print()
    print(f"anios abiertos: {len(NOMINACIONES)} (1956-1975)")
    print(f"anios con nominacion: {len(con)}")
    print(f"nominaciones: {total}")
    print(f"nominadores distintos: {len(cuenta)}")
    print("los que repiten:",
          ", ".join(f"{n} ({k})" for n, k in cuenta.most_common() if k > 1))
    print()
    print("de a dos:")
    for a, t in DE_A_DOS.items():
        print(f"  {a}: {t} -> {RESULTADO[a]}")
    print()
    print("parejas:")
    for an, x, y, q in PAREJAS:
        print(f"  {an}: {x}-{y} -> {q}")
    afuera = Counter(y for _, _, y, q in PAREJAS if q.startswith("A s"))
    print("  mitades que no lo ganaron nunca:",
          ", ".join(f"{n} ({k})" for n, k in afuera.most_common()))
    print()
    print("cuando se abre cada legajo cerrado (el anio mas 51, en enero):")
    for a in range(1976, 1987):
        print(f"  {a} -> enero de {a + 51}")
    print()
    print("dias de la semana:")
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    for f, que in [
        ((1975, 9, 25), "discurso de Olsson por Montale"),
        ((1975, 10, 23), "anuncio de Montale"),
        ((1976, 9, 15), "Borges llega a Santiago"),
        ((1976, 9, 21), "doctorado honoris causa, Universidad de Chile"),
        ((1976, 9, 22), "encuentro con Pinochet y partida"),
        ((1976, 9, 23), "el dia siguiente"),
        ((1976, 10, 21), "anuncio de Bellow"),
        ((1977, 10, 6), "anuncio de Aleixandre"),
        ((2026, 10, 6), "hoy"),
    ]:
        d = dt.date(*f)
        print(f"  {d.isoformat()}  {dias[d.weekday()]:9s}  {que}")
    print()
    d0, d1 = dt.date(1976, 9, 22), dt.date(1976, 10, 21)
    print(f"del encuentro con Pinochet al anuncio de Bellow: {(d1 - d0).days} dias")
    # 1967: el comite delibero el 14/9, firmo el 15/9 y el anuncio fue el 19/10.
    tramo = dt.date(1967, 10, 19) - dt.date(1967, 9, 14)
    eq = d1 - tramo
    print(f"1967: de la deliberacion del comite al anuncio, {tramo.days} dias")
    print(f"la misma distancia antes del anuncio de 1976: {eq.isoformat()} ({dias[eq.weekday()]})")


if __name__ == "__main__":
    main()
