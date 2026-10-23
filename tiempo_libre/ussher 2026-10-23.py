#!/usr/bin/env python3
"""Comprobación al margen: el 23 de octubre de 4004 a. C. (juliano proléptico) según Ussher.
Día juliano de una fecha del calendario juliano (algoritmo de Meeus, válido para años negativos)
y día de la semana; año del Período Juliano (año 1 = 4713 a. C.)."""
import math
def jdn_juliano(Y, M, D):
    # Y astronómico (4004 a. C. = -4003). Fliegel–Van Flandern para el calendario juliano:
    a = (14 - M) // 12
    y = Y + 4800 - a
    m = M + 12 * a - 3
    return D + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
for (Y, M, D, et) in [(-4003, 10, 23, "23 de octubre de 4004 a. C. (Ussher)"),
                      (-4712, 1, 1, "1 de enero de 4713 a. C. (origen del Período Juliano)"),
                      (2026, 10, 10, "10 de octubre de 2026 juliano = 23 de octubre de 2026 gregoriano")]:
    j = jdn_juliano(Y, M, D)
    print(f"{et}: JDN {j}, {dias[j % 7]}")
j0 = jdn_juliano(-4712, 1, 1); j = jdn_juliano(-4003, 10, 23)
print("Período Juliano, año", (j - j0) // 365.25 + 1, "→ Ussher dice 710")
print("Días desde entonces hasta hoy (JDN de hoy, gregoriano 23/10/2026):", end=" ")
# JDN gregoriano de hoy
Y, M, D = 2026, 10, 23
a = (14 - M) // 12; y = Y + 4800 - a; m = M + 12 * a - 3
jhoy = D + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
print(jhoy, "−", j, "=", jhoy - j, "días =", round((jhoy - j) / 365.2425, 2), "años")
