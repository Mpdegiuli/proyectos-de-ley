#!/usr/bin/env python3
"""dias.py — días de la semana en los dos calendarios, y Pascua en los dos.
Solo biblioteca estándar. Uso: python3 dias.py
"""
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

def jdn_greg(y, m, d):
    a = (14 - m) // 12; yy = y + 4800 - a; mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045

def jdn_jul(y, m, d):
    a = (14 - m) // 12; yy = y + 4800 - a; mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - 32083

def dia(jdn):
    return DIAS[jdn % 7]

def de_jdn_greg(j):
    a = j + 32044; b = (4 * a + 3) // 146097; c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461; e = c - 1461 * d // 4; m = (5 * e + 2) // 153
    return (100 * b + d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1)

def de_jdn_jul(j):
    c = j + 32082; d = (4 * c + 3) // 1461; e = c - 1461 * d // 4; m = (5 * e + 2) // 153
    return (d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1)

def pascua_jul(y):
    a = y % 4; b = y % 7; c = y % 19
    d = (19 * c + 15) % 30; e = (2 * a + 4 * b - d + 34) % 7
    m = (d + e + 114) // 31; dd = (d + e + 114) % 31 + 1
    return (y, m, dd)          # fecha juliana

def pascua_greg(y):
    a = y % 19; b = y // 100; c = y % 100; d = b // 4; e = b % 4
    f = (b + 8) // 25; g = (b - f + 1) // 3; h = (19 * a + b - d - g + 15) % 30
    i = c // 4; k = c % 4; l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes = (h + l - 7 * m + 114) // 31; dd = (h + l - 7 * m + 114) % 31 + 1
    return (y, mes, dd)        # fecha gregoriana

def f(t): return "%d/%d/%d" % (t[2], t[1], t[0])

if __name__ == "__main__":
    print("== anclas ==")
    print("4/10/1582 juliano:", dia(jdn_jul(1582, 10, 4)), "| 15/10/1582 gregoriano:", dia(jdn_greg(1582, 10, 15)),
          "| consecutivos:", jdn_greg(1582, 10, 15) - jdn_jul(1582, 10, 4) == 1)
    print("\n== el salto según el año ==")
    for y in (1582, 1583, 1584, 1585):
        print(y, ": 4 de octubre (jul.)", dia(jdn_jul(y, 10, 4)), "-> 15 de octubre (greg.)", dia(jdn_greg(y, 10, 15)))
    print("\n== fechas del cuaderno: la misma cifra leída en cada calendario ==")
    casos = [("fundación de Buenos Aires", 1580, 6, 11), ("domingo de la Trinidad de Garay", 1580, 5, 29),
             ("desembarco de Colón", 1492, 10, 12),
             ("Córdoba, año nuevo", 1583, 1, 1), ("Córdoba, año nuevo", 1584, 1, 1),
             ("Córdoba, cabildo", 1584, 10, 8), ("Córdoba, cabildo", 1584, 11, 20),
             ("Córdoba, año nuevo", 1585, 1, 1), ("Córdoba, cabildo", 1585, 1, 14), ("Córdoba, cabildo", 1585, 3, 6),
             ("Córdoba, cabildo", 1585, 3, 10), ("Córdoba, registro de hierro", 1585, 3, 22), ("Córdoba, cabildo", 1585, 4, 11),
             ("Córdoba, entierro", 1585, 6, 6), ("Córdoba, cabildo", 1585, 6, 9), ("Córdoba, 'hayer Domingo'", 1585, 6, 16), ("Córdoba, cabildo", 1585, 6, 17),
             ("Córdoba, año nuevo", 1587, 1, 1), ("Santiago, cabildo", 1586, 8, 1),
             ("Lima, obedecimiento", 1584, 4, 19), ("Lima, auto de impresión", 1584, 7, 14),
             ("La Plata, recepción", 1584, 7, 29), ("Huarochirí", 1584, 8, 17), ("Cañete, pregón", 1584, 9, 27),
             ("Manila, carta de Dávalos", 1584, 7, 3), ("carta de Montalvo", 1585, 10, 12)]
    for nombre, y, m, d in casos:
        print("%-32s %2d/%2d/%d  juliano: %-10s gregoriano: %s" % (nombre, d, m, y, dia(jdn_jul(y, m, d)), dia(jdn_greg(y, m, d))))
    print("\n== Pascua de 1585 en las dos cuentas ==")
    pj = pascua_jul(1585); pg = pascua_greg(1585)
    print("juliana: %s (jul.) = %s (greg.)" % (f(pj), f(de_jdn_greg(jdn_jul(*pj)))))
    print("gregoriana: %s (greg.) = %s (jul.)" % (f(pg), f(de_jdn_jul(jdn_greg(*pg)))))
    print("Pentecostés gregoriano 1585:", f(de_jdn_greg(jdn_greg(*pg) + 49)), "| juliano:", f(de_jdn_jul(jdn_jul(*pj) + 49)), "(jul.) =",
          f(de_jdn_greg(jdn_jul(*pj) + 49)), "(greg.)")
    print("Corpus gregoriano 1585:", f(de_jdn_greg(jdn_greg(*pg) + 60)))
    for y in (1583, 1584, 1586):
        pj = pascua_jul(y); pg = pascua_greg(y)
        print(y, "Pascua juliana", f(pj), "=", f(de_jdn_greg(jdn_jul(*pj))), "greg. | Pascua gregoriana", f(pg))
    print("\n== hoy ==")
    hoy = jdn_greg(2026, 10, 8)
    print("8/10/2026:", dia(hoy), "| en juliano hoy es", f(de_jdn_jul(hoy)))
    print("del 8/10/1584 (jul., Córdoba) a hoy:", hoy - jdn_jul(1584, 10, 8), "días")
    print("8/10/1584 juliano =", f(de_jdn_greg(jdn_jul(1584, 10, 8))), "gregoriano")
