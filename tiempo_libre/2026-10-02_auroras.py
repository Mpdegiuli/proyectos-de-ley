#!/usr/bin/env python3
"""Cuentas sobre las islas Aurora: dónde las puso la Atrevida (1794), dónde
están las rocas Cormorán, y qué pasa con el meridiano de Cádiz.
Posiciones: Poe (Pym, cap. 15) y Gould (1928) para las tres islas; leyenda de
la estampa de Brambila (1798) para la noche del 28/1/1794; Wikipedia para las
rocas; Guía Digital de la UAM para los meridianos.
"""
import math
R = 6371.0088
MN = 1.852

def dms(g, m=0, s=0): return g + m / 60 + s / 3600
def fmt(x):
    g = int(abs(x)); m = (abs(x) - g) * 60
    return f"{g}°{m:04.1f}'"

def dist(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2); dl = math.radians(lon2 - lon1)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))

def rumbo(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2); dl = math.radians(lon2 - lon1)
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return math.degrees(math.atan2(y, x)) % 360

CADIZ = dms(6, 17, 14.025)        # observatorio viejo de Cádiz, al oeste de Greenwich
SANFERNANDO = dms(6, 12, 20)

# las tres islas según la memoria de 1809, en la versión inglesa (oeste de Greenwich)
ATREVIDA = [("norte", -dms(52, 37, 24), -dms(47, 43, 15)),
            ("centro", -dms(53, 2, 40), -dms(47, 55, 15)),
            ("sur", -dms(53, 15, 22), -dms(47, 57, 15))]
CORMORAN = (-dms(53, 33, 0), -dms(42, 2, 22))
NEGRA = (-dms(53, 39, 7), -dms(41, 48, 1))
ESTAMPA = (-dms(52, 13), dms(42, 7))      # 28/1/1794: lat, longitud al oeste de CÁDIZ
SOLEDAD = (-51.53, -58.12)                 # Puerto Soledad / Port Louis (aprox.)
GEORGIAS_O = (-54.0, -38.05)               # extremo oeste de las Georgias (isla Bird)
GEORGIAS_C = (-54.4, -36.6)                # centro aproximado de la isla San Pedro

def main():
    print("== La estampa de Brambila")
    eg = ESTAMPA[1] + CADIZ
    print(f"  42°07' al oeste de Cádiz = {fmt(eg)} al oeste de Greenwich (con San Fernando: {fmt(ESTAMPA[1] + SANFERNANDO)})")
    for n, la, lo in ATREVIDA:
        print(f"  de la estampa a la isla del {n}: {dist(ESTAMPA[0], -eg, la, lo):.0f} km")
    print(f"  si la estampa se leyera como Greenwich (42°07'O): a {dist(ESTAMPA[0], -ESTAMPA[1], *CORMORAN):.0f} km de las rocas Cormorán")

    print("== Las tres islas de la Atrevida contra las rocas")
    for n, la, lo in ATREVIDA:
        d = dist(la, lo, *CORMORAN)
        print(f"  {n}: {fmt(la)}S {fmt(lo)}O = {fmt(-lo - CADIZ)} al oeste de Cádiz; a {d:.0f} km ({d / MN:.0f} millas) de las Cormorán; "
              f"dif. de latitud {abs(la - CORMORAN[0]) * 60:.0f}', de longitud {abs(lo - CORMORAN[1]) * 60:.0f}'")
    print(f"  de la isla del norte a la del sur: {dist(ATREVIDA[0][1], ATREVIDA[0][2], ATREVIDA[2][1], ATREVIDA[2][2]):.0f} km; "
          f"de las Cormorán a la Negra: {dist(*CORMORAN, *NEGRA):.1f} km")
    dl = abs(ATREVIDA[2][2] - CORMORAN[1])
    print(f"  diferencia de longitud isla del sur - Cormorán: {fmt(dl)} = {dl * 4:.1f} minutos de reloj; "
          f"Cádiz - Greenwich: {fmt(CADIZ)} = {CADIZ * 4:.1f} min")
    print(f"  Cormorán: {fmt(-CORMORAN[1])} O de Greenwich = {fmt(-CORMORAN[1] - CADIZ)} O de Cádiz")

    print("== Las tres lecturas posibles del número de la Atrevida (isla del sur)")
    cad = -ATREVIDA[2][2] - CADIZ
    for txt, lonG in (("tal como se publicó en inglés (Greenwich)", -ATREVIDA[2][2]),
                      ("si 47°57' fuera de Cádiz y hubiera que sumarle", -ATREVIDA[2][2] + CADIZ),
                      ("si el número de Cádiz (41°40') se leyera como de Greenwich", cad)):
        d = dist(ATREVIDA[2][1], -lonG, *CORMORAN)
        print(f"  {txt}: {fmt(lonG)} O -> a {d:.0f} km de las Cormorán")

    print("== Weddell, 1820: corrió el paralelo 53°15' hasta los 46°O")
    print(f"  de (53°15'S, 46°O) a las Cormorán: {dist(-53.25, -46, *CORMORAN):.0f} km; "
          f"si seguía por el paralelo habría pasado a {abs(-53.25 - CORMORAN[0]) * 60 * MN:.0f} km al norte de ellas")
    h = 75
    print(f"  una roca de {h} m se asoma al horizonte a {3.57 * math.sqrt(h):.0f} km para un ojo al nivel del mar, "
          f"y a {3.57 * (math.sqrt(h) + math.sqrt(25)):.0f} km desde un tope de 25 m (sin refracción)")

    print("== El proyecto 5370-D-2011: '135 millas (250 km) al S de las Georgias'")
    for n, g in (("extremo oeste", GEORGIAS_O), ("centro", GEORGIAS_C)):
        print(f"  desde el {n} de las Georgias: {dist(*g, *CORMORAN):.0f} km ({dist(*g, *CORMORAN) / MN:.0f} millas), rumbo {rumbo(*g, *CORMORAN):.0f}°")
    print(f"  de Puerto Soledad a las Cormorán: {dist(*SOLEDAD, *CORMORAN):.0f} km; a la isla del sur de la Atrevida: {dist(*SOLEDAD, ATREVIDA[2][1], ATREVIDA[2][2]):.0f} km")

if __name__ == "__main__":
    main()
