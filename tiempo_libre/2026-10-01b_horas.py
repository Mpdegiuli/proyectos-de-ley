#!/usr/bin/env python3
"""Horas temporales (el dia de sol a sol partido en doce) para un lugar y una fecha.
Uso: python3 horas.py
Necesita: pip install ephem
Tiempo libre, 1/10/2026 (segunda sesion). Solo calcula; no lee nada del repositorio."""
import ephem, math
from datetime import timedelta


def dia(lat, lon, fecha_utc_mediodia, elev=0):
    """Devuelve (salida, puesta, transito) en UTC como ephem.Date, para el dia que contiene la fecha dada."""
    o = ephem.Observer()
    o.lat, o.lon, o.elevation = str(lat), str(lon), elev
    o.date = fecha_utc_mediodia
    sol = ephem.Sun()
    sal = o.previous_rising(sol)
    pue = o.next_setting(sol)
    o.date = sal
    tra = o.next_transit(sol)
    return sal, pue, tra


def hm(d, corr_h):
    """ephem.Date -> 'hh:mm' sumando corr_h horas (huso, o longitud/15 para hora solar media local)."""
    t = ephem.Date(d + corr_h/24.0).datetime()
    t = t + timedelta(seconds=30)
    return f"{t.hour:02d}:{t.minute:02d}"


def temporal(sal, pue, instante):
    """En que hora temporal cae un instante: 0 = salida, 12 = puesta."""
    return 12.0 * (instante - sal) / (pue - sal)


def informe(nombre, lat, lon, fecha, corr_h, etiqueta_hora, marcas=()):
    sal, pue, tra = dia(lat, lon, fecha)
    largo = (pue - sal) * 24 * 60
    print(f"== {nombre} ==")
    print(f"  salida {hm(sal, corr_h)}  transito {hm(tra, corr_h)}  puesta {hm(pue, corr_h)}  ({etiqueta_hora})")
    print(f"  dia de {int(largo//60)} h {largo%60:.0f} min; hora temporal de {largo/12:.1f} min")
    hitos = [("fin de la hora segunda", 2), ("comienzo de la hora cuarta", 3), ("fin de la hora cuarta", 4),
             ("sexta (mediodia)", 6), ("media hora octava", 7.5), ("fin de la octava", 8), ("nona (fin de la novena)", 9)]
    for txt, h in hitos:
        inst = ephem.Date(sal + (pue - sal) * h / 12.0)
        print(f"  {txt:28s} {hm(inst, corr_h)}")
    o = ephem.Observer(); o.lat, o.lon = str(lat), str(lon)
    sol = ephem.Sun()
    for txt, inst in marcas:
        o.date = inst; sol.compute(o)
        print(f"  {txt}: hora temporal {temporal(sal, pue, inst):.2f}; Sol a {math.degrees(sol.alt):.1f} grados de altura, acimut {math.degrees(sol.az):.1f}")
    print()
    return sal, pue, tra


if __name__ == "__main__":
    # Buenos Aires, 1/10/2026. Huso UTC-3.
    informe("Buenos Aires, 1/10/2026", -34.6037, -58.3816, "2026/10/1 15:00", -3, "hora oficial, UTC-3",
            marcas=[("6:48 (la tarea)", ephem.Date("2026/10/1 09:48:00")),
                    ("14:31:43 (esta sesion)", ephem.Date("2026/10/1 17:31:43"))])
    # Montecassino. PyEphem lee las fechas anteriores a 1582 en calendario juliano.
    lonMC = 13.814
    for f, n in [("540/10/1 11:00", "Montecassino, 1 de octubre de 540 (juliano)"),
                 ("540/9/14 11:00", "Montecassino, 14 de septiembre de 540 (juliano)"),
                 ("540/6/21 11:00", "Montecassino, 21 de junio de 540 (juliano)"),
                 ("540/12/18 11:00", "Montecassino, 18 de diciembre de 540 (juliano)")]:
        informe(n, 41.49, lonMC, f, lonMC/15.0, "hora solar media local")
    print("equinoccio de otono de 540 (juliano):", ephem.next_autumnal_equinox("540/9/1"))
    print("solsticio de invierno de 540:", ephem.next_winter_solstice("540/12/1"))
    # Buenos Aires en los solsticios, para ver cuanto se estira la hora
    informe("Buenos Aires, 21/12/2026", -34.6037, -58.3816, "2026/12/21 15:00", -3, "hora oficial, UTC-3")
    informe("Buenos Aires, 21/6/2026", -34.6037, -58.3816, "2026/6/21 15:00", -3, "hora oficial, UTC-3")


    # --- la tarea de las 6:48 a lo largo del ano: en que hora temporal cae ---
    print("equinoccio de septiembre de 2026 (UTC):", ephem.next_autumnal_equinox("2026/9/1"))
    o = ephem.Observer(); o.lat, o.lon, o.elevation = "-34.6037", "-58.3816", 0
    sol = ephem.Sun()
    d0 = ephem.Date("2026/10/1 09:48:00")          # 6:48 de Buenos Aires
    estado, cambios, maximo, minimo = None, [], (-99, None), (99, None)
    for k in range(366):
        t = ephem.Date(d0 + k)
        o.date = t
        # salida del mismo dia civil: la mas cercana a las 6:48
        ant, sig = o.previous_rising(sol), o.next_rising(sol)
        sal = ant if (t - ant) < (sig - t) else sig
        o.date = sal; pue = o.next_setting(sol)
        h = 12.0 * (t - sal) / (pue - sal) if t >= sal else (t - sal) * 24 * 60   # de dia: hora temporal; de noche: minutos antes de la salida (negativo)
        de_dia = t >= sal
        if estado is not None and de_dia != estado:
            cambios.append((ephem.Date(t - 3/24.0).datetime().strftime("%d/%m/%Y"), "ya es de dia" if de_dia else "todavia es de noche"))
        estado = de_dia
        if de_dia and h > maximo[0]: maximo = (h, ephem.Date(t - 3/24.0).datetime().strftime("%d/%m/%Y"))
        if not de_dia and h < minimo[0]: minimo = (h, ephem.Date(t - 3/24.0).datetime().strftime("%d/%m/%Y"))
    print("cambios (a las 6:48):", cambios)
    print("lo mas adentro del dia: hora temporal %.2f el %s" % maximo)
    print("lo mas adentro de la noche: %.0f minutos antes de la salida, el %s" % (-minimo[0], minimo[1]))
    # la regla de las letras aplicada a las horas canonicas
    for n in ["Maitines", "Laudes", "Prima", "Tercia", "Sexta", "Nona", "Vísperas", "Completas", "Tiempo libre"]:
        letras = sum(c.isalpha() for c in n)
        print(f"  {n:13s} {letras:2d} letras -> {letras % 15 + 1:2d} minutos antes")
