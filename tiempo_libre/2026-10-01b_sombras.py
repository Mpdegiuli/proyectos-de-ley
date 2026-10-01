#!/usr/bin/env python3
"""La sombra de un clavo en Buenos Aires, hoy: sobre el piso y sobre una pared que mira al norte.
Comprueba con el Sol calculado (PyEphem) el sentido en que gira cada sombra y escribe la figura.
Uso: python3 sombras.py   -> imprime la cuenta y escribe dos_relojes.svg
Necesita: pip install ephem
Tiempo libre, 1/10/2026 (segunda sesion). No lee nada del repositorio."""
import ephem, math


LAT, LON = "-34.6037", "-58.3816"
DIA = "2026/10/1 15:00"                      # mediodia aproximado en UTC, para ubicar el dia
MARCAS = [("6:48", ephem.Date("2026/10/1 09:48:00"), "#eb6834"),
          ("14:31", ephem.Date("2026/10/1 17:31:43"), "#2a78d6")]
ROMANOS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]


obs = ephem.Observer(); obs.lat, obs.lon, obs.elevation = LAT, LON, 0
sol = ephem.Sun()
obs.date = DIA
SAL, PUE = obs.previous_rising(sol), obs.next_setting(sol)


def vector(instante):
    """Direccion del Sol (este, norte, arriba)."""
    obs.date = instante; sol.compute(obs)
    al, az = float(sol.alt), float(sol.az)
    return (math.cos(al) * math.sin(az), math.cos(al) * math.cos(az), math.sin(al))


def piso(instante):
    """Punta de la sombra de un clavo vertical de largo 1, vista desde arriba: x = este, y = norte."""
    e, n, u = vector(instante)
    return None if u <= 0 else (-e / u, -n / u)


def pared(instante):
    """Punta de la sombra de un clavo horizontal de largo 1 clavado en una pared que mira al norte,
    vista de frente (quien mira tiene el oeste a la derecha): x = derecha, y = arriba."""
    e, n, u = vector(instante)
    return None if n <= 0 or u <= 0 else (e / n, -u / n)


def giro(puntos):
    """Suma de productos cruz entre sombras sucesivas: positivo = antihorario, negativo = horario."""
    s = 0.0
    for (x1, y1), (x2, y2) in zip(puntos, puntos[1:]):
        s += x1 * y2 - x2 * y1
    return s


def hora_local(d):
    t = ephem.Date(d - 3 / 24.0 + 30 / 86400.0).datetime()
    return f"{t.hour}:{t.minute:02d}"


horas = [ephem.Date(SAL + (PUE - SAL) * h / 12.0) for h in range(1, 12)]   # fin de cada hora temporal
P = [piso(t) for t in horas]
W = [pared(t) for t in horas]
print("sale", hora_local(SAL), "se pone", hora_local(PUE))
print("piso :", "antihorario" if giro(P) > 0 else "horario", f"({giro(P):+.2f})")
print("pared:", "antihorario" if giro([w for w in W if w]) > 0 else "horario", f"({giro([w for w in W if w]):+.2f})")
for r, t, p, w in zip(ROMANOS, horas, P, W):
    print(f"  fin de la hora {r:4s} {hora_local(t):>5s}  piso {p[0]:+6.2f} {p[1]:+6.2f}   pared " +
          (f"{w[0]:+6.2f} {w[1]:+6.2f}" if w else "sin sol"))
# cuando el Sol cruza el plano de la pared (acimut 90 y 270)
def cruce(t0, t1):
    f = lambda t: vector(t)[1]
    for _ in range(50):
        m = (t0 + t1) / 2
        if (f(t0) > 0) == (f(m) > 0): t0 = m
        else: t1 = m
    return ephem.Date(t0)
c1, c2 = cruce(SAL, SAL + 3 / 24.0), cruce(PUE - 3 / 24.0, PUE)
print("la pared tiene sol de", hora_local(c1), "a", hora_local(c2))
for nombre, t, _ in MARCAS:
    print(nombre, "piso", piso(t), "pared", pared(t))


# ---------- figura ----------
ANCHO, ALTO, R = 920, 520, 150
TINTA, GRIS, FONDO, LINEA = "#0b0b0b", "#52514e", "#fcfcfb", "#c9c8c2"
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" height="{ALTO}" '
       f'font-family="Helvetica, Arial, sans-serif">',
       f'<rect width="{ANCHO}" height="{ALTO}" fill="{FONDO}"/>',
       f'<text x="40" y="38" font-size="19" fill="{TINTA}" font-weight="bold">La sombra de un clavo en Buenos Aires, 1 de octubre de 2026</text>',
       f'<text x="40" y="60" font-size="13" fill="{GRIS}">Cada raya gris es el final de una hora de las de Benito (el día de sol a sol partido en doce); el punto, hasta dónde llega la sombra.</text>']


def recorta(x, y, escala):
    """Pasa a pixeles y corta en el borde del cuadrante."""
    px, py = x * escala, -y * escala
    d = math.hypot(px, py)
    if d > R:
        return px * R / d, py * R / d, True
    return px, py, False


def cuadrante(cx, cy, puntos, escala, titulo, sub, sentido, marcas, nota, rumbos):
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{LINEA}" stroke-width="1"/>')
    for r, p in zip(ROMANOS, puntos):
        if not p: continue
        d = math.hypot(p[0], p[1])
        ux, uy = p[0] / d, -p[1] / d
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + ux * R:.1f}" y2="{cy + uy * R:.1f}" stroke="{LINEA}" stroke-width="1"/>')
        px, py, cortada = recorta(p[0], p[1], escala)
        if not cortada:
            out.append(f'<circle cx="{cx + px:.1f}" cy="{cy + py:.1f}" r="2.5" fill="{GRIS}"/>')
        out.append(f'<text x="{cx + ux * (R + 16):.1f}" y="{cy + uy * (R + 16) + 4:.1f}" font-size="12" fill="{GRIS}" text-anchor="middle">{r}</text>')
    for nombre, p, color, dx, dy, ancla in marcas:
        if not p: continue
        px, py, cortada = recorta(p[0], p[1], escala)
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + px:.1f}" y2="{cy + py:.1f}" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>')
        if not cortada:
            out.append(f'<circle cx="{cx + px:.1f}" cy="{cy + py:.1f}" r="4" fill="{color}" stroke="{FONDO}" stroke-width="2"/>')
        out.append(f'<text x="{cx + px + dx:.1f}" y="{cy + py + dy:.1f}" font-size="13" fill="{TINTA}" text-anchor="{ancla}">{nombre}</text>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{TINTA}"/>')
    # flecha del sentido de giro, un arco en la mitad de abajo, por dentro del borde
    ra = R - 26
    a1, a2 = (205, 245) if sentido == "antihorario" else (335, 295)   # grados, medidos como en un reloj de pared (0 = derecha, antihorario)
    x1, y1 = cx + ra * math.cos(math.radians(a1)), cy - ra * math.sin(math.radians(a1))
    x2, y2 = cx + ra * math.cos(math.radians(a2)), cy - ra * math.sin(math.radians(a2))
    barrido = 0 if sentido == "antihorario" else 1
    out.append(f'<path d="M {x1:.1f} {y1:.1f} A {ra} {ra} 0 0 {barrido} {x2:.1f} {y2:.1f}" fill="none" stroke="{TINTA}" stroke-width="1.5"/>')
    # punta de flecha: triangulo orientado por la tangente
    tang = math.radians(a2 + (90 if sentido == "antihorario" else -90))
    tx, ty = math.cos(tang), -math.sin(tang)
    nx, ny = -ty, tx
    out.append(f'<path d="M {x2 + tx * 9:.1f} {y2 + ty * 9:.1f} L {x2 + nx * 4.5:.1f} {y2 + ny * 4.5:.1f} L {x2 - nx * 4.5:.1f} {y2 - ny * 4.5:.1f} Z" fill="{TINTA}"/>')
    for txt, lx, ly in rumbos:
        out.append(f'<text x="{cx + lx}" y="{cy + ly}" font-size="12" fill="{GRIS}" text-anchor="middle">{txt}</text>')
    out.append(f'<text x="{cx}" y="{cy - R - 46}" font-size="15" fill="{TINTA}" text-anchor="middle" font-weight="bold">{titulo}</text>')
    out.append(f'<text x="{cx}" y="{cy - R - 28}" font-size="12.5" fill="{GRIS}" text-anchor="middle">{sub}</text>')
    out.append(f'<text x="{cx}" y="{cy + R + 44}" font-size="13" fill="{TINTA}" text-anchor="middle">{nota}</text>')


m_piso = [("6:48", piso(MARCAS[0][1]), MARCAS[0][2], 8, -10, "start"),
          ("14:31", piso(MARCAS[1][1]), MARCAS[1][2], 2, 22, "middle")]
m_pared = [("14:31", pared(MARCAS[1][1]), MARCAS[1][2], -10, -6, "end")]
cuadrante(240, 290, P, 60, "En el piso", "clavo vertical, visto desde arriba, con el norte arriba",
          "antihorario" if giro(P) > 0 else "horario", m_piso, "gira al revés que las agujas",
          [("norte", 0, -R + 20), ("oeste", -R + 34, -48), ("este", R - 30, -48)])
cuadrante(680, 290, W, 60, "En una pared que mira al norte", "clavo horizontal, visto de frente (el oeste queda a la derecha)",
          "antihorario" if giro([w for w in W if w]) > 0 else "horario", m_pared, "gira como las agujas; a las 6:48 todavía no le da el sol",
          [("arriba", 0, -R + 20), ("este", -R + 30, -48), ("oeste", R - 34, -48)])
out.append('</svg>')
open("dos_relojes.svg", "w").write("\n".join(out) + "\n")
print("escrito dos_relojes.svg")
