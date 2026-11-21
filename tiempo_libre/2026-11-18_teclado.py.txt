#!/usr/bin/env python3
"""Cuentas sobre las frecuencias del teclado de tonos (DTMF).

No lee nada del repositorio. Escribe en la salida estándar:
  1. la razón entre frecuencias vecinas de cada grupo (Schenker, BSTJ, enero de 1960,
     dice 21:19 dentro de cada grupo y un intervalo y medio entre los grupos);
  2. la distancia de cada tono a la nota más cercana de la escala temperada (La4 = 440 Hz);
  3. el intervalo que suena en cada tecla (agudo/grave) y a qué distancia queda de las
     "diagonales" que el artículo quiso esquivar: 1:2, 2:3, 3:4, 3:5, 4:5, 5:6;
  4. qué tecla "marcaría" una voz con armónicos puros según su fundamental.

Uso: python3 teclado.py > salida_teclado.txt
"""
import math
from fractions import Fraction

FILAS = [697, 770, 852, 941]
COLS = [1209, 1336, 1477, 1633]
TECLAS = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]
GRUPO_B_1960 = [1094, 1209, 1336, 1477]  # lo que imprime el artículo de 1960

NOMBRES = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]


def cents(a, b):
    return 1200 * math.log2(a / b)


def nota_cercana(f):
    n = round(12 * math.log2(f / 440.0))  # semitonos desde La4
    f_nota = 440.0 * 2 ** (n / 12)
    idx = (n + 9) % 12
    octava = 4 + (n + 9) // 12
    return f"{NOMBRES[idx]}{octava}", f_nota, cents(f, f_nota)


def parte1():
    r = Fraction(21, 19)
    print("1. La razón 21:19")
    print(f"   21/19 = {float(r):.5f}; un semitono temperado es 2^(1/12) = {2**(1/12):.5f}; un tono, {2**(2/12):.5f}.")
    print(f"   En cents, 21:19 son {cents(21, 19):.1f} (un semitono son 100, un tono 200).")
    for nombre, grupo in (("filas", FILAS), ("columnas", COLS), ("grupo B de 1960", GRUPO_B_1960)):
        razones = [b / a for a, b in zip(grupo, grupo[1:])]
        print(f"   {nombre}: " + ", ".join(f"{b}/{a} = {b/a:.4f}" for a, b in zip(grupo, grupo[1:])))
    # un intervalo y medio entre grupos (941 -> 1094) y, en el estándar, dos y medio (941 -> 1209)
    print(f"   941 * (21/19)^1.5 = {941 * float(r) ** 1.5:.1f} (el 1.094 del artículo de 1960)")
    print(f"   941 * (21/19)^2.5 = {941 * float(r) ** 2.5:.1f} (el 1.209 del estándar)")
    serie = [941 * float(r) ** (1.5 + k) for k in range(5)]
    print("   la serie entera desde 941 con medio paso de corrimiento: " + ", ".join(f"{x:.1f}" for x in serie))
    print("   es decir, 1.094, 1.209, 1.336, 1.477 y 1.633 son cinco términos seguidos de la misma serie;")
    print("   el estándar de 1963 dejó los cuatro de arriba y el artículo de 1960 tenía los cuatro de abajo.")
    serie_a = [697 * float(r) ** k for k in range(4)]
    print("   desde 697: " + ", ".join(f"{x:.1f}" for x in serie_a) + " (697, 770, 852, 941)")
    print()


def parte2():
    print("2. Cada tono contra la escala temperada (La4 = 440 Hz)")
    print("   tono     nota    frecuencia de la nota   desvío (cents)   desvío (%)")
    for f in FILAS + COLS:
        nombre, fn, c = nota_cercana(f)
        print(f"   {f:5d}   {nombre:6s}  {fn:9.2f} Hz           {c:+7.1f}         {100*(f/fn-1):+.2f} %")
    print("   (un cuarto de tono son 50 cents; el oído distingue unos 5 o 6 cents en tonos puros sostenidos)")
    print()


DIAGONALES = {"1:2 (octava)": Fraction(2, 1), "2:3 (quinta)": Fraction(3, 2), "3:4 (cuarta)": Fraction(4, 3),
              "3:5 (sexta mayor)": Fraction(5, 3), "4:5 (tercera mayor)": Fraction(5, 4), "5:6 (tercera menor)": Fraction(6, 5)}
JUSTOS = {"octava": 2, "séptima mayor": 15 / 8, "séptima menor": 9 / 5, "sexta mayor": 5 / 3, "sexta menor": 8 / 5,
          "quinta": 3 / 2, "tritono": 45 / 32, "cuarta": 4 / 3, "tercera mayor": 5 / 4, "tercera menor": 6 / 5,
          "segunda mayor": 9 / 8, "segunda menor": 16 / 15, "unísono": 1}


def parte3():
    print("3. El intervalo de cada tecla (tono agudo / tono grave) y la diagonal más cercana")
    print("   tecla  grave  agudo   razón    cents   intervalo justo más cercano    diagonal más cercana (desvío en %)")
    peor = (None, 1e9)
    for i, fila in enumerate(FILAS):
        for j, col in enumerate(COLS):
            r = col / fila
            c = cents(col, fila)
            justo = min(JUSTOS.items(), key=lambda kv: abs(cents(r, kv[1])))
            diag = min(DIAGONALES.items(), key=lambda kv: abs(cents(r, float(kv[1]))))
            desvio = 100 * (r / float(diag[1]) - 1)
            if abs(desvio) < abs(peor[1]):
                peor = (TECLAS[i][j], desvio, diag[0])
            print(f"   {TECLAS[i][j]:^5s}  {fila:4d}  {col:5d}   {r:.4f}  {c:6.0f}   {justo[0]:14s} ({cents(r, justo[1]):+5.0f} cents)   {diag[0]:22s} {desvio:+.1f} %")
    print(f"   la tecla más cerca de una diagonal prohibida es {peor[0]}: {peor[2]}, a {peor[1]:+.1f} %"
          " (la ventana de reconocimiento del artículo es ±2 %).")
    print("   Con 1.094 en vez de 1.633 (el código de 1960), las cuatro teclas de la columna baja daban:")
    for fila in FILAS:
        r = 1094 / fila
        diag = min(DIAGONALES.items(), key=lambda kv: abs(cents(r, float(kv[1]))))
        print(f"     {fila}-1094: razón {r:.4f}, {diag[0]} a {100*(r/float(diag[1])-1):+.1f} %")
    print()


def parte4():
    print("4. Qué tecla marcaría un zumbido con armónicos puros (fundamental f0, armónicos m·f0 y n·f0)")
    print("   Una tecla se 'marca' si algún armónico cae a ±2 % de su tono grave y otro a ±2 % de su agudo.")
    print("   f0 de 80 a 400 Hz, de a 1 Hz; se listan los tramos de f0 que marcan cada tecla.")
    tol = 0.02
    marcados = {}
    for f0x10 in range(800, 4001):
        f0 = f0x10 / 10
        for i, fila in enumerate(FILAS):
            for j, col in enumerate(COLS):
                m = round(fila / f0)
                n = round(col / f0)
                if m < 1 or n < 1:
                    continue
                if abs(m * f0 / fila - 1) <= tol and abs(n * f0 / col - 1) <= tol:
                    marcados.setdefault(TECLAS[i][j], []).append((f0, m, n))
    orden = [t for fila in TECLAS for t in fila]
    for t in orden:
        if t not in marcados:
            print(f"   {t}: ninguna fundamental entre 80 y 400 Hz la marca con armónicos puros")
            continue
        # agrupar en tramos contiguos con el mismo (m, n)
        tramos = []
        for f0, m, n in marcados[t]:
            if tramos and tramos[-1][2] == (m, n) and abs(f0 - tramos[-1][1]) < 0.15:
                tramos[-1][1] = f0
            else:
                tramos.append([f0, f0, (m, n)])
        desc = "; ".join(f"{a:.1f}-{b:.1f} Hz (armónicos {mn[0]} y {mn[1]})" for a, b, mn in tramos)
        print(f"   {t}: {desc}")
    print("   Ejemplo: cantar un Fa3 (174,6 Hz) pone el 4º armónico en 698 y el 7º en 1.222: la tecla 1.")
    print("   Lo que lo impide en un receptor de verdad es la 'acción de guardia': los demás armónicos")
    print("   (el 5º, el 6º...) suenan con niveles comparables y el receptor no acepta la pareja.")
    print()


if __name__ == "__main__":
    parte1()
    parte2()
    parte3()
    parte4()
