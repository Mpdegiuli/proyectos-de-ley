#!/usr/bin/env python3
"""derrota.py - cuentas del cuaderno de tiempo libre del 12/10/2026.

La travesía de 1492 como una suma de tramos (rumbo y leguas), tal como los da el
extracto de Las Casas, del 8 de septiembre a las 2 de la madrugada del 12 de octubre.

No es una reconstrucción de la derrota: no hay corriente, ni abatimiento, ni un
campo de declinación magnética. Es la estima cruda, para ver cuánto mueve el
resultado (a) qué número se lee en el manuscrito, (b) cuánto mide la legua y
(c) un error constante de la aguja.

Dos lecturas de los números:
  IFE   el texto castellano de la edición de B. W. Ife (King's College London,
        Early Modern Spain), que coincide con la tabla de Keith Pickering
  NAV   Fernández de Navarrete (1825; reimpresión Calpe, 1922), que es la que
        circula en castellano en la web
Difieren en dos tramos: 9 de septiembre (15 / 19) y 23 de septiembre (27 / 22).

Uso: python3 derrota.py            (imprime todo)
     python3 derrota.py --json     (además escribe derrota.json para la figura)
No necesita nada fuera de la biblioteca estándar.
"""
import math, json, sys

# rumbos de la aguja, en grados desde el norte
W, WbN, WNW, NW, SW, WSW = 270.0, 281.25, 292.5, 315.0, 225.0, 247.5

# (fecha, rumbo, leguas IFE, leguas NAV, lo que contó a la gente o None, nota)
TRAMOS = [
    ("8/9",  W,   9,    9,    None, "desde las 3 de la madrugada"),
    ("9/9",  W,   15,   19,   None, "de día; 'acordó contar menos'"),
    ("9/9",  W,   30,   30,   None, "de noche, 120 millas"),
    ("10/9", W,   60,   60,   48,   "rumbo no dicho"),
    ("11/9", W,   20,   20,   None, "de día, 'y más'"),
    ("11/9", W,   20,   20,   16,   "de noche, 'cerca de'"),
    ("12/9", W,   33,   33,   None, "'contando menos'"),
    ("13/9", W,   33,   33,   29.5, "'tres o cuatro menos'"),
    ("14/9", W,   20,   20,   None, "'alguna menos'"),
    ("15/9", W,   27,   27,   None, "'y algunas más'"),
    ("16/9", W,   39,   39,   36,   ""),
    ("17/9", W,   50,   50,   47,   "'y más'"),
    ("18/9", W,   55,   55,   48,   "'más de'"),
    ("19/9", W,   25,   25,   22,   ""),
    ("20/9", (WbN + WNW) / 2, 7.5, 7.5, None, "'cuarta del Norueste y a la media partida', 7 u 8"),
    ("21/9", W,   13,   13,   None, "'a ratos a la vía y a ratos no'"),
    ("22/9", WNW, 30,   30,   None, "'más o menos'"),
    ("23/9", NW,  27,   22,   None, "'y a las veces a la cuarta del Norte y a las veces a su camino'"),
    ("24/9", W,   14.5, 14.5, 12,   ""),
    ("25/9", W,   4.5,  4.5,  None, "de día"),
    ("25/9", SW,  17,   17,   13,   "de noche; el 13 es por los dos tramos"),
    ("26/9", W,   31,   31,   24,   "al Oeste hasta pasado el mediodía y después al Sudoeste, sin reparto: va todo al Oeste"),
    ("27/9", W,   24,   24,   20,   ""),
    ("28/9", W,   14,   14,   13,   ""),
    ("29/9", W,   24,   24,   21,   ""),
    ("30/9", W,   14,   14,   11,   ""),
    ("1/10", W,   25,   25,   20,   ""),
    ("2/10", W,   39,   39,   30,   ""),
    ("3/10", W,   47,   47,   40,   ""),
    ("4/10", W,   63,   63,   46,   ""),
    ("5/10", W,   57,   57,   45,   ""),
    ("6/10", W,   40,   40,   33,   ""),
    ("7/10", W,   23,   23,   18,   "hasta una hora de sol"),
    ("7/10", WSW, 5,    5,    None, "de noche"),
    ("8/10", WSW, 11.75, 11.75, None, "'11 leguas y media o 12'"),
    ("9/10", SW,  5,    5,    None, ""),
    ("9/10", WbN, 4,    4,    None, ""),
    ("9/10", WbN, 2,    2,    None, "lo que falta para las 11 del día; rumbo supuesto"),
    ("9/10", WbN, 20.5, 20.5, 17,   "de noche; rumbo supuesto (el último dicho)"),
    ("10/10", WSW, 59,  59,   44,   ""),
    ("11/10", WSW, 27,  27,   None, "hasta puesto el sol"),
    ("11/10", W,  22.5, 22.5, None, "90 millas, hasta las 2 de la madrugada del 12"),
]

# La cuenta menor no siempre se refiere al día entero: el 11/9 es la de la noche (20 leguas),
# el 7/10 la del día (23) y el 9/10, por cómo está escrita, parece la de la noche (20,5).
BASE_MENOR = {"11/9": 20.0, "7/10": 23.0, "9/10": 20.5}

SALIDA = (28.09, -17.11)          # San Sebastián de La Gomera
HIERRO = (27.75, -18.00)

# Puntos de llegada de la Tabla I de Goldsmith y Richardson (WHOI-92-14, 1992), más
# los Cayos Plana (posición de Wikipedia). Son puntos frente a cada isla, no su centro.
CANDIDATAS = [
    ("Egg (Molander)",            25.635, -76.575),
    ("Watling / San Salvador",    24.019, -74.342),
    ("Cayo Samaná",               23.065, -73.546),
    ("Cayos Plana",               22.60,  -73.55),
    ("Gran Turco",                21.429, -71.139),
]

def estima(tramos, legua_mn, giro=0.0, inicio=SALIDA):
    """Suma los tramos sobre la esfera (latitud media). giro: grados que se le restan a
    cada rumbo (declinación al oeste: la aguja marca Oeste y el barco va al sur del Oeste)."""
    lat, lon = inicio
    puntos = [(lat, lon)]
    for rumbo, leguas in tramos:
        d = leguas * legua_mn
        t = math.radians(rumbo - giro)
        dlat = d * math.cos(t) / 60.0
        latm = math.radians(lat + dlat / 2)
        lon += d * math.sin(t) / (60.0 * math.cos(latm))
        lat += dlat
        puntos.append((lat, lon))
    return puntos

def km(p, q):
    a1, o1, a2, o2 = map(math.radians, (p[0], p[1], q[0], q[1]))
    h = math.sin((a2 - a1) / 2) ** 2 + math.cos(a1) * math.cos(a2) * math.sin((o2 - o1) / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))

def lectura(cual):
    i = 2 if cual == "IFE" else 3
    return [(t[1], t[i]) for t in TRAMOS]

def resolver(tramos, destino):
    """legua y giro constantes con los que la estima cae justo en destino (Newton en 2D)."""
    L, g = 2.8, 0.0
    for _ in range(60):
        f = estima(tramos, L, g)[-1]
        e = (f[0] - destino[0], f[1] - destino[1])
        if abs(e[0]) < 1e-9 and abs(e[1]) < 1e-9:
            break
        h = 1e-5
        fL = estima(tramos, L + h, g)[-1]; fg = estima(tramos, L, g + h)[-1]
        a, b = (fL[0] - f[0]) / h, (fg[0] - f[0]) / h
        c, d = (fL[1] - f[1]) / h, (fg[1] - f[1]) / h
        det = a * d - b * c
        L -= (d * e[0] - b * e[1]) / det
        g -= (-c * e[0] + a * e[1]) / det
    return L, g

def main():
    out = {}
    print("1. Sumas de leguas (8/9 a las 2 de la madrugada del 12/10)")
    for cual in ("IFE", "NAV"):
        i = 2 if cual == "IFE" else 3
        tot = sum(t[i] for t in TRAMOS)
        desde9 = sum(t[i] for t in TRAMOS if t[0] != "8/9")
        print(f"   {cual}: {tot:7.2f} leguas desde el 8/9; {desde9:7.2f} desde el 9/9")
        out[f"suma_{cual}"] = tot
    # cuentas corridas que da el propio texto
    def hasta(fecha, i):
        s = 0
        for t in TRAMOS:
            s += t[i]
            if t[0] == fecha and (TRAMOS.index(t) + 1 == len(TRAMOS) or TRAMOS[TRAMOS.index(t) + 1][0] != fecha):
                return s
    for fecha, dicho in (("19/9", "pilotos: 440 (Niña), 420 (Pinta), 400 (nao)"),
                         ("1/10", "piloto 578; Almirante 707 'la verdadera', 584 'la menor'")):
        print(f"   al {fecha}: suma IFE {hasta(fecha, 2):.1f}, suma NAV {hasta(fecha, 3):.1f}   (el texto: {dicho})")
        print(f"            sin el 8/9: IFE {hasta(fecha, 2) - 9:.1f}, NAV {hasta(fecha, 3) - 9:.1f}")

    print("\n2. La cuenta menor")
    dias = []
    for t in TRAMOS:
        if t[0] not in dias: dias.append(t[0])
    con = sorted({t[0] for t in TRAMOS if t[4] is not None}, key=dias.index)
    print(f"   días del 8/9 al 11/10: {len(dias)}; con cifra menor: {len(con)}")
    # suma comparada solo en los días que tienen las dos cifras
    def cierta_de(d):
        return BASE_MENOR.get(d, sum(t[2] for t in TRAMOS if t[0] == d))
    cierta = sum(cierta_de(d) for d in con)
    menor = sum(t[4] for t in TRAMOS if t[4] is not None)
    print(f"   en esos días: cierta {cierta:.1f}, menor {menor:.1f}, razón {menor / cierta:.3f}")
    hasta1 = [d for d in con if dias.index(d) <= dias.index("1/10")]
    c1 = sum(cierta_de(d) for d in hasta1); m1 = sum(t[4] for t in TRAMOS if t[0] in hasta1 and t[4] is not None)
    print(f"   hasta el 1/10: {len(hasta1)} días con las dos cifras; cierta {c1:.1f}, menor {m1:.1f}, razón {m1 / c1:.3f}")
    print(f"   584 / 707 = {584 / 707:.3f}")
    razones = [(t[0], t[4] / cierta_de(t[0])) for t in TRAMOS if t[4] is not None]
    print(f"   la más baja: {min(razones, key=lambda x: x[1])}; la más alta: {max(razones, key=lambda x: x[1])}")
    cerca = [(f, r) for f, r in razones if abs(r * cierta_de(f) - cierta_de(f) * 5 / 6) <= 1.0]
    print(f"   días en que la menor está a una legua o menos de cinco sextos de la cierta: {len(cerca)} de {len(razones)}")
    print("   razón día por día: " + ", ".join(f"{f} {r:.2f}" for f, r in razones))

    print("\n3. Rumbos")
    solo_w = [d for d in dias if all(t[1] == W for t in TRAMOS if t[0] == d)]
    print(f"   días con todo el camino al Oeste: {len(solo_w)} de {len(dias)}")
    lw = sum(t[2] for t in TRAMOS if t[1] == W); tot = sum(t[2] for t in TRAMOS)
    print(f"   leguas al Oeste a secas: {lw:.1f} de {tot:.2f} ({100 * lw / tot:.0f} %)")

    print("\n4. Carta plana, en leguas (x al oeste, y al sur)")
    for cual in ("IFE", "NAV"):
        x = sum(-l * math.sin(math.radians(r)) for r, l in lectura(cual))
        y = sum(-l * math.cos(math.radians(r)) for r, l in lectura(cual))
        print(f"   {cual}: {x:7.1f} al oeste, {y:6.1f} al sur")
        out[f"plana_{cual}"] = (x, y)

    print("\n5. Dónde cae la estima cruda, sin giro (latitud, longitud)")
    for L in (2.67, 2.82, 2.88, 3.2):
        for cual in ("IFE", "NAV"):
            f = estima(lectura(cual), L)[-1]
            print(f"   legua {L:.2f} mn, {cual}: {f[0]:6.2f} N {-f[1]:6.2f} O")
    a = estima(lectura("IFE"), 2.82)[-1]; b = estima(lectura("NAV"), 2.82)[-1]
    print(f"   distancia entre las dos lecturas (legua 2,82): {km(a, b):.0f} km")
    a = estima(lectura("IFE"), 2.67)[-1]; b = estima(lectura("IFE"), 3.2)[-1]
    print(f"   distancia entre legua 2,67 y 3,2 (IFE): {km(a, b):.0f} km")
    a = estima(lectura("IFE"), 2.82, 0)[-1]; b = estima(lectura("IFE"), 2.82, 11.25)[-1]
    print(f"   distancia entre giro 0 y una cuarta al oeste (legua 2,82, IFE): {km(a, b):.0f} km; latitud {a[0]:.2f} -> {b[0]:.2f}")
    a = estima(lectura("IFE"), 2.82, 0)[-1]; b = estima(lectura("IFE"), 2.82, 1)[-1]
    print(f"   un grado de giro: {km(a, b):.0f} km")

    print("\n6. Qué legua y qué giro constante de la aguja hacen falta para llegar a cada isla (IFE)")
    out["soluciones"] = []
    for nombre, la, lo in CANDIDATAS:
        L, g = resolver(lectura("IFE"), (la, lo))
        Ln, gn = resolver(lectura("NAV"), (la, lo))
        print(f"   {nombre:24s} {la:6.2f} N {-lo:6.2f} O: legua {L:.3f} mn, giro {g:5.2f}° al oeste "
              f"({g / 11.25:.2f} cuartas)   [NAV: {Ln:.3f}, {gn:5.2f}°]")
        out["soluciones"].append((nombre, la, lo, L, g))
    print("   legua que deja la estima sin giro en la longitud de Watling:")
    for cual in ("IFE", "NAV"):
        lo_, hi = 2.0, 4.0
        for _ in range(60):
            mid = (lo_ + hi) / 2
            if estima(lectura(cual), mid)[-1][1] > -74.342: lo_ = mid
            else: hi = mid
        f = estima(lectura(cual), mid)[-1]
        print(f"     {cual}: {mid:.3f} mn; latitud ahí {f[0]:.2f} N ({(f[0] - 24.019) * 60:.0f} millas al norte de Watling)")
    for L in (3.18, 3.2):
        f = estima(lectura("IFE"), L)[-1]
        print(f"   con {L} la estima pasa la longitud de Watling por {-f[1] - 74.342:.2f}°")
    print(f"   de Watling al Gran Turco (puntos de la tabla): {km((24.019, -74.342), (21.429, -71.139)):.0f} km")
    print(f"   entre los finales de Goldsmith y Richardson de 1987 (23,766 N 74,359 O) y de 1992, caso 3d (21,704 N 71,282 O): "
          f"{km((23.766, -74.359), (21.704, -71.282)):.0f} km")

    print("\n8. La cuenta cierta, la cuenta menor y la distancia que hay")
    tot = sum(t[2] for t in TRAMOS)
    for nombre, la, lo in CANDIDATAS:
        d_mn = km(SALIDA, (la, lo)) / 1.852
        print(f"   La Gomera - {nombre:24s}: {d_mn:5.0f} mn por círculo máximo = {d_mn / tot:.2f} mn por legua de la cuenta cierta")
    d_w = km(SALIDA, (24.019, -74.342)) / 1.852
    menor_tot = tot * 584 / 707
    print(f"   cuenta cierta: {tot:.0f} leguas; cuenta menor, si guardó la proporción del 1/10 (584/707): {menor_tot:.0f} leguas")
    for L in (2.67, 2.82, 3.20):
        print(f"   legua {L:.2f} mn: cierta {tot * L:5.0f} mn ({100 * (tot * L / d_w - 1):+4.0f} % respecto de Watling), "
              f"menor {menor_tot * L:5.0f} mn ({100 * (menor_tot * L / d_w - 1):+4.0f} %)")
    print(f"   cuatro millas romanas de 1.480 m = {4 * 1480 / 1852:.2f} mn; 5/6 = {5 / 6:.3f}")

    if "--json" in sys.argv:
        out["tramos"] = [(t[0], t[1], t[2], t[3], t[4]) for t in TRAMOS]
        out["tracks"] = {f"{L}_{g}": estima(lectura("IFE"), L, g) for L in (2.67, 2.82, 3.2) for g in (0.0, 11.25)}
        out["candidatas"] = CANDIDATAS
        json.dump(out, open("derrota.json", "w"), indent=1)

    print("\n7. El Diario como atributo d (carta plana, una unidad = una legua, mirando al norte)")
    d = "M0,0"
    for r, l in lectura("IFE"):
        dx = l * math.sin(math.radians(r)); dy = -l * math.cos(math.radians(r))
        if abs(dy) < 1e-9: d += f" h{dx:g}"
        else: d += f" l{round(dx, 1):g},{round(dy, 1):g}"
    print("   " + d)
    n_h = d.count(" h"); n_l = d.count(" l")
    print(f"   {n_h} órdenes h y {n_l} órdenes l")

if __name__ == "__main__":
    main()
