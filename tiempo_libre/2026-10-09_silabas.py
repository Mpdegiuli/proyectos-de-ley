#!/usr/bin/env python3
"""silabas.py — cómo le llega una sílaba hangul a una máquina.

En Unicode las 11.172 sílabas hangul no se guardan una por una: se calculan.
Una sílaba es un número de tres cifras en base mixta (19 iniciales, 21 vocales,
28 finales contando "ninguna"):

    código = 0xAC00 + (inicial * 21 + vocal) * 28 + final

Este programa hace la cuenta a mano, la compara con lo que trae Python
(unicodedata) para las 11.172, y descompone las palabras del día.

Uso: python3 silabas.py        (solo biblioteca estándar)
"""
import unicodedata

SBASE, LBASE, VBASE, TBASE = 0xAC00, 0x1100, 0x1161, 0x11A7
LCOUNT, VCOUNT, TCOUNT = 19, 21, 28
NCOUNT = VCOUNT * TCOUNT          # 588
SCOUNT = LCOUNT * NCOUNT          # 11172

# nombres cortos de la norma (Jamo.txt), para armar el nombre de cada sílaba
L_NOMBRE = ["G", "GG", "N", "D", "DD", "R", "M", "B", "BB", "S", "SS", "", "J", "JJ",
            "C", "K", "T", "P", "H"]
V_NOMBRE = ["A", "AE", "YA", "YAE", "EO", "E", "YEO", "YE", "O", "WA", "WAE", "OE", "YO",
            "U", "WEO", "WE", "WI", "YU", "EU", "YI", "I"]
T_NOMBRE = ["", "G", "GG", "GS", "N", "NJ", "NH", "D", "L", "LG", "LM", "LB", "LS", "LT",
            "LP", "LH", "M", "B", "BS", "S", "SS", "NG", "J", "C", "K", "T", "P", "H"]


def partir(silaba):
    """Devuelve (inicial, vocal, final) como índices."""
    s = ord(silaba) - SBASE
    assert 0 <= s < SCOUNT, "no es una sílaba hangul"
    return s // NCOUNT, (s % NCOUNT) // TCOUNT, s % TCOUNT


def juntar(l, v, t=0):
    return chr(SBASE + (l * VCOUNT + v) * TCOUNT + t)


def jamo(l, v, t):
    out = chr(LBASE + l) + chr(VBASE + v)
    if t:
        out += chr(TBASE + t)
    return out


def comprobar():
    """La cuenta a mano contra la tabla de Python, para las 11.172 sílabas."""
    for i in range(SCOUNT):
        c = chr(SBASE + i)
        l, v, t = partir(c)
        assert juntar(l, v, t) == c
        assert unicodedata.normalize("NFD", c) == jamo(l, v, t)
        assert unicodedata.name(c) == "HANGUL SYLLABLE " + L_NOMBRE[l] + V_NOMBRE[v] + T_NOMBRE[t]
    return SCOUNT


def mostrar(palabra):
    print("\n%s" % palabra)
    for c in palabra:
        l, v, t = partir(c)
        j = jamo(l, v, t)
        compat = " ".join(unicodedata.name(x).replace("HANGUL ", "") for x in j)
        print("  %s  U+%04X = AC00 + (%2d×21 + %2d)×28 + %2d   UTF-8: %s   %s"
              % (c, ord(c), l, v, t, c.encode("utf-8").hex(" ").upper(), unicodedata.name(c)))
        print("       %s" % compat)


if __name__ == "__main__":
    n = comprobar()
    print("Sílabas comprobadas contra unicodedata: %d  (19 × 21 × 28 = %d)" % (n, 19 * 21 * 28))
    print("Primera: %s (U+%04X). Última: %s (U+%04X)."
          % (chr(SBASE), SBASE, chr(SBASE + SCOUNT - 1), SBASE + SCOUNT - 1))

    for p in ("한글날", "가갸날", "훈민정음", "조선글날"):
        mostrar(p)

    # La misma letra, dos códigos: inicial y final no se reúsan
    print("\nLa ㄴ de 날 (inicial) y la ㄴ de 한 (final) en los jamo que se combinan:")
    ini = chr(LBASE + 2)
    fin = chr(TBASE + 4)
    print("  inicial U+%04X %s" % (ord(ini), unicodedata.name(ini)))
    print("  final   U+%04X %s" % (ord(fin), unicodedata.name(fin)))

    # Las cuatro letras de 1446 que ya no se usan
    print("\nLas cuatro de las 28 que hoy no se usan:")
    for c in "ㆍㅿㆁㆆ":
        print("  %s  U+%04X  %s" % (c, ord(c), unicodedata.name(c)))
