#!/usr/bin/env python3
"""luna.py - El sol y la luna de la noche del jueves 11 al viernes 12 de octubre de 1492
(calendario juliano) en el lugar de las naves. Necesita: pip install ephem

Las fechas se arman con el número de día juliano, para no depender de cómo cada
biblioteca trate el calendario antes de 1582. La hora que se imprime es la hora
solar media del lugar (TU + longitud/15); al lado va la hora solar verdadera,
que es la que marcaría un reloj de sol y la más parecida a la de las ampolletas
corregidas al mediodía.
"""
import math, ephem

def jdn_juliano(a, m, d):
    x = (14 - m) // 12; y = a + 4800 - x; mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083

def djd(jdn, frac=0.0):
    """jdn = día juliano entero (empieza al mediodía TU); frac = fracción desde ese mediodía"""
    return ephem.Date(jdn - 2415020 + frac)

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
J11 = jdn_juliano(1492, 10, 11)
J12 = jdn_juliano(1492, 10, 12)
print(f"11/10/1492 juliano: JDN {J11}, {DIAS[J11 % 7]};  12/10/1492: JDN {J12}, {DIAS[J12 % 7]}")
# el mismo día en el calendario gregoriano llevado hacia atrás
def gregoriano(jdn):
    a = jdn + 32044; b = (4 * a + 3) // 146097; c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461; e = c - 1461 * d // 4; m = (5 * e + 2) // 153
    return (100 * b + d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1)
print("12/10/1492 juliano = %d-%02d-%02d gregoriano proléptico" % gregoriano(J12))
hoy = 2461326  # 12/10/2026 gregoriano
print(f"del viernes 12/10/1492 al lunes 12/10/2026: {hoy - J12} días = {(hoy - J12) // 7} semanas y {(hoy - J12) % 7} días")

def hora(t, lon):
    """(hora media local, hora verdadera local) en horas decimales a partir de una fecha TU"""
    tu = (float(t) + 0.5) % 1 * 24            # ephem cuenta desde el mediodía
    media = (tu + lon / 15) % 24
    s = ephem.Sun(); o = ephem.Observer(); o.lon = str(lon); o.lat = "0"; o.date = t
    s.compute(o)
    ah = (float(o.sidereal_time()) - float(s.ra)) * 12 / math.pi   # ángulo horario del sol
    verd = (ah + 12) % 24
    return media, verd

def hm(h):
    h = h % 24; m = int(round(h * 60)); return f"{m // 60:02d}:{m % 60:02d}"

def noche(nombre, lat, lon, alt_ojo=6.5):
    print(f"\n== {nombre}: {lat:.2f}°N, {-lon:.2f}°O ==")
    o = ephem.Observer(); o.lat, o.lon, o.elevation = str(lat), str(lon), alt_ojo
    o.pressure = 1010; o.temp = 26
    # mediodía local del 11: TU = 12 - lon/15
    t_med = djd(J11, (-lon / 15) / 24)
    o.date = t_med
    puesta = o.next_setting(ephem.Sun())
    m, v = hora(puesta, lon)
    print(f"puesta del sol del 11: {hm(m)} media, {hm(v)} verdadera")
    o.date = puesta; o.horizon = "-18"
    fin = o.next_setting(ephem.Sun(), use_center=True)
    o.horizon = "0"
    m, v = hora(fin, lon); print(f"fin del crepúsculo astronómico: {hm(m)} media, {hm(v)} verdadera")
    o.date = puesta
    sale = o.next_rising(ephem.Moon())
    m, v = hora(sale, lon); print(f"salida de la luna: {hm(m)} media, {hm(v)} verdadera")
    o.date = sale
    amanece = o.next_rising(ephem.Sun())
    m, v = hora(amanece, lon); print(f"salida del sol del 12: {hm(m)} media, {hm(v)} verdadera")
    # la ecuación del tiempo de esa noche
    m, v = hora(djd(J12, 0.5 - lon / 360 - 0.5), lon)
    print(f"hora verdadera - hora media a la medianoche: {(v - m + 12) % 24 - 12:+.2f} h = {((v - m + 12) % 24 - 12) * 60:+.0f} min")
    # la luna a las horas verdaderas del relato
    for etiqueta, hv in (("22:00 (la lumbre)", 22.0), ("23:00", 23.0), ("00:00", 24.0), ("02:00 (la tierra)", 26.0)):
        # buscar el instante TU en que la hora verdadera local vale hv
        t = djd(J11, (hv - 12 - lon / 15) / 24)
        for _ in range(4):
            _, v = hora(t, lon)
            dif = ((hv - v + 12) % 24) - 12
            t = ephem.Date(t + dif / 24)
        o.date = t
        l = ephem.Moon(o); s = ephem.Sun(o)
        print(f"  {etiqueta:20s} luna: altura {math.degrees(l.alt):6.1f}°, acimut {math.degrees(l.az):5.1f}°, "
              f"{l.phase:4.1f} % iluminada, en {ephem.constellation(l)[1]};  sol {math.degrees(s.alt):6.1f}°")
    return o

noche("frente a San Salvador (Watling), a las dos", 24.0, -74.4)
noche("56 millas romanas al este (posición de las diez)", 24.0, -73.6)
noche("frente a Samana Cay", 23.1, -73.6)
noche("frente a la Gran Turca", 21.5, -71.0)

# fases
t0 = djd(J11, 0)
llena = ephem.previous_full_moon(t0); menguante = ephem.next_last_quarter_moon(t0); nueva = ephem.next_new_moon(t0)
def fecha_jul(t):
    jd = float(t) + 2415020.0
    z = int(jd + 0.5); f = jd + 0.5 - z
    # de JDN a fecha juliana
    c = z + 32082; d = (4 * c + 3) // 1461; e = c - 1461 * d // 4; m = (5 * e + 2) // 153
    return f"{e - (153 * m + 2) // 5 + 1}/{m + 3 - 12 * (m // 10)}/{d - 4800 + m // 10} {hm(f * 24)} TU"
print("\nluna llena anterior :", fecha_jul(llena))
print("cuarto menguante    :", fecha_jul(menguante))
print("luna nueva siguiente:", fecha_jul(nueva))
lon = -74.4
t2 = djd(J11, (26 - 12 - lon / 15) / 24)   # ~02:00 media local del 12
print(f"de la llena a las dos de la madrugada del 12 (hora local): {float(t2) - float(llena):.2f} días")
print(f"de las dos de la madrugada del 12 al cuarto menguante: {(float(menguante) - float(t2)) * 24:.1f} horas")
t22 = djd(J11, (22 - 12 - lon / 15) / 24)
print(f"de las diez de la noche del 11 al cuarto menguante: {(float(menguante) - float(t22)) * 24:.1f} horas")
