#!/usr/bin/env python3
"""caida.py — la caída de una piedra: vuelo luminoso y vuelo oscuro.

Modelo de un solo cuerpo con ablación (el de los manuales de meteorítica):
    dv/dt = -Γ ρ(h) A v² / m  + g·(componente vertical)
    dm/dt = -Λ ρ(h) A v³ / (2 Q)
con Γ = 0,5 (arrastre; Γ = c_d/2), Λ = coeficiente de transferencia de calor, Q = calor de
ablación, A = sección de una esfera de densidad ρ_m que se achica con la masa.
Atmósfera exponencial (ρ₀ = 1,225 kg/m³, escala 7,16 km). Dos dimensiones.

Se considera "luminoso" el tramo en que la piedra va a más de 3 km/s (el umbral
que usa el FAQ de la American Meteor Society es 2–4 km/s). Lo que sigue es el
"vuelo oscuro": la piedra cae a su velocidad terminal, sin brillar.

Uso: python3 caida.py [masa_inicial_kg] [velocidad_km_s] [angulo_grados]
Sin argumentos busca la masa inicial que deja 127 kg en el suelo (Ensisheim),
con 15 km/s y 45°, y además corre una grilla de entradas para ver qué tan
estables son las alturas y los tiempos. Escribe caida.json y salida_caida.txt.
"""
import json, math, sys

G = 9.81
RHO0, H_ESC = 1.225, 7160.0      # atmósfera exponencial
RHO_M = 3400.0                   # kg/m³, condrita ordinaria
GAMMA = 0.5                      # coeficiente de arrastre (Γ = c_d/2; c_d = 1)
LAMBDA = 0.1                     # coeficiente de transferencia de calor
Q = 8.0e6                        # J/kg, calor de ablación
# El coeficiente de ablación que resulta, σ = Λ/(2ΓQ) = 0,0125 s²/km², está en el
# orden del que la literatura da para los bólidos de piedra ordinaria (~0,014).
V_LUM = 3000.0                   # m/s: por debajo, ya no brilla
H0 = 120_000.0                   # altura de entrada

def rho_aire(h):
    return RHO0 * math.exp(-max(h, 0.0) / H_ESC)

def area(m):
    r = (3 * m / (4 * math.pi * RHO_M)) ** (1 / 3)
    return math.pi * r * r

def caer(m0, v0, ang_deg, dt=0.0005, registrar=True):
    """Integra hasta el suelo. Devuelve un dict con los hitos y la traza."""
    ang = math.radians(ang_deg)
    x, h = 0.0, H0
    vx, vh = v0 * math.cos(ang), -v0 * math.sin(ang)
    m, t = m0, 0.0
    traza = []
    fin_luz = None
    paso_reg = 0.05
    prox_reg = 0.0
    while h > 0:
        v = math.hypot(vx, vh)
        rho = rho_aire(h)
        A = area(m)
        a_drag = GAMMA * rho * A * v * v / m
        ax = -a_drag * vx / v
        ah = -a_drag * vh / v - G
        dm = -LAMBDA * rho * A * v ** 3 / (2 * Q)
        # paso adaptativo: fino mientras va rápido, grueso en el vuelo oscuro
        paso = dt if v > 1000 else 0.01
        vx += ax * paso
        vh += ah * paso
        x += vx * paso
        h += vh * paso
        m = max(m + dm * paso, 1e-6)
        t += paso
        if fin_luz is None and v < V_LUM:
            fin_luz = dict(t=t, h=h, x=x, v=v, m=m)
        if registrar and t >= prox_reg:
            traza.append((round(t, 3), round(h), round(x), round(v, 1), round(m, 3)))
            prox_reg += paso_reg
        if m < 0.001:
            break
    v = math.hypot(vx, vh)
    res = dict(m0=m0, v0=v0, ang=ang_deg, t_total=t, x_total=x, v_final=v, m_final=m,
               fin_luz=fin_luz)
    if fin_luz:
        res["t_oscuro"] = t - fin_luz["t"]
        res["x_oscuro"] = x - fin_luz["x"]
    if registrar:
        res["traza"] = traza
    return res

def masa_para(m_final_objetivo, v0, ang):
    """Bisección sobre la masa inicial para dejar m_final_objetivo en el suelo."""
    lo, hi = m_final_objetivo, 200 * m_final_objetivo
    for _ in range(40):
        mid = math.sqrt(lo * hi)
        r = caer(mid, v0, ang, registrar=False)
        if r["m_final"] < m_final_objetivo:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)

def fmt(r):
    fl = r["fin_luz"]
    s = (f"m0={r['m0']:.0f} kg  v0={r['v0']/1000:.0f} km/s  ángulo={r['ang']:.0f}°\n"
         f"  fin de la luz: t={fl['t']:.1f} s, altura={fl['h']/1000:.1f} km, "
         f"v={fl['v']:.0f} m/s, masa={fl['m']:.1f} kg\n"
         f"  vuelo oscuro: {r['t_oscuro']:.0f} s ({r['t_oscuro']/60:.1f} min), "
         f"recorre {r['x_oscuro']/1000:.1f} km más en horizontal\n"
         f"  suelo: t={r['t_total']:.0f} s, v={r['v_final']:.0f} m/s "
         f"({r['v_final']*3.6:.0f} km/h), masa={r['m_final']:.1f} kg "
         f"({100*r['m_final']/r['m0']:.0f} % de la inicial)\n")
    return s

def main():
    global GAMMA, LAMBDA
    args = [float(a) for a in sys.argv[1:]]
    salida = []
    if args:
        m0 = args[0]; v0 = (args[1] if len(args) > 1 else 15) * 1000; ang = args[2] if len(args) > 2 else 45
        r = caer(m0, v0, ang)
        salida.append(fmt(r))
        json.dump(r, open("caida.json", "w"))
    else:
        v0, ang = 15000.0, 45.0
        m0 = masa_para(127.0, v0, ang)
        r = caer(m0, v0, ang)
        salida.append("Ensisheim: la masa inicial que deja 127 kg en el suelo\n")
        salida.append(fmt(r))
        salida.append("\nGrilla (misma física; la masa inicial se ajusta en cada caso para dejar 127 kg):\n")
        grilla = []
        for vv in (12, 15, 20, 25):
            for aa in (20, 45, 70):
                mm = masa_para(127.0, vv * 1000, aa)
                g = caer(mm, vv * 1000, aa, registrar=False)
                fl = g["fin_luz"]
                grilla.append(dict(v0=vv, ang=aa, m0=mm, h_luz=fl["h"], t_osc=g["t_oscuro"],
                                   v_fin=g["v_final"], x_osc=g["x_oscuro"], t_luz=fl["t"]))
                geo = H0 / (vv * 1000 * math.sin(math.radians(aa)))
                salida.append(f"  v0={vv:2d} km/s ang={aa:2d}°  m0={mm:6.0f} kg  luz {fl['t']:4.1f} s "
                              f"(120 km/(v·sen θ) = {geo:4.1f} s)  fin de la luz a {fl['h']/1000:4.1f} km  "
                              f"vuelo oscuro {g['t_oscuro']:5.0f} s  llega a {g['v_final']:3.0f} m/s  "
                              f"({100*127/mm:4.1f} % de la masa)\n")
        salida.append("\nUn cuerpo de 300 kg, 15 km/s, 45° (la apuesta de las predicciones):\n")
        r300 = caer(300.0, v0, ang)
        salida.append(fmt(r300))
        # velocidad terminal de la piedra final al nivel del mar, en forma cerrada
        A = area(127.0)
        vt = math.sqrt(127.0 * G / (GAMMA * RHO0 * A))
        salida.append(f"\nVelocidad terminal de 127 kg (esfera de {1000*(3*127/(4*math.pi*RHO_M))**(1/3):.0f} mm de radio) "
                      f"al nivel del mar con Γ={GAMMA}: {vt:.0f} m/s; con Γ=0,25 (c_d=0,5): {vt*math.sqrt(2):.0f} m/s.\n"
                      f"σ = Λ/(2ΓQ) = {LAMBDA/(2*GAMMA*Q)*1e6:.4f} s²/km²\n")
        # sensibilidad al coeficiente de arrastre, que es lo que menos se sabe
        salida.append("\nSensibilidad al arrastre (15 km/s, 45°, masa inicial ajustada para dejar 127 kg):\n")
        gammas = []
        for gm in (0.5, 0.75, 1.0):
            GAMMA = gm
            mm = masa_para(127.0, v0, ang)
            g = caer(mm, v0, ang, registrar=False)
            fl = g["fin_luz"]
            gammas.append(dict(gamma=gm, m0=mm, h_luz=fl["h"], t_osc=g["t_oscuro"], v_fin=g["v_final"], t_luz=fl["t"]))
            salida.append(f"  Γ={gm:.2f}  m0={mm:5.0f} kg  luz {fl['t']:4.1f} s  fin de la luz a {fl['h']/1000:4.1f} km  "
                          f"vuelo oscuro {g['t_oscuro']:3.0f} s  llega a {g['v_final']:3.0f} m/s\n")
        GAMMA = 0.5
        # sensibilidad a la ablación: Λ = 0,24 da σ = 0,03 s²/km²; Ceplecha (1980) calibra
        # log σ = −11,49 y −11,41 (cgs) en Lost City e Innisfree, o sea 0,032 y 0,039 s²/km²
        salida.append("\nSensibilidad a la ablación (Γ=0,5, 15 km/s, 45°, masa inicial ajustada para dejar 127 kg):\n")
        lambdas = []
        for lam in (0.1, 0.24, 0.26, 0.31):
            LAMBDA = lam
            mm = masa_para(127.0, v0, ang)
            g = caer(mm, v0, ang, registrar=False)
            fl = g["fin_luz"]
            lambdas.append(dict(sigma=lam / (2 * GAMMA * Q) * 1e6, m0=mm, h_luz=fl["h"], t_osc=g["t_oscuro"],
                                v_fin=g["v_final"], t_luz=fl["t"]))
            salida.append(f"  σ={lam/(2*GAMMA*Q)*1e6:.3f} s²/km²  m0={mm:6.0f} kg  luz {fl['t']:4.1f} s  "
                          f"fin de la luz a {fl['h']/1000:4.1f} km  vuelo oscuro {g['t_oscuro']:3.0f} s  llega a {g['v_final']:3.0f} m/s\n")
        LAMBDA = 0.1
        json.dump(dict(ensisheim=r, grilla=grilla, gammas=gammas, lambdas=lambdas,
                       trescientos={k: v for k, v in r300.items() if k != "traza"}),
                  open("caida.json", "w"))
    txt = "".join(salida)
    print(txt, end="")
    open("salida_caida.txt", "w").write(txt)

if __name__ == "__main__":
    main()
