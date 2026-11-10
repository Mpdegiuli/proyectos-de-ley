#!/usr/bin/env python3
"""Red eléctrica de juguete con relés: cuánto margen hace falta para que una línea
que se abre no se lleve la red entera.

Modelo (declarado, no es la red de 1965):
- Grilla de n × n nodos; cada nodo se conecta con sus vecinos (líneas iguales,
  susceptancia 1).
- Generadores en una fila de nodos de un lado (el "Niágara"), cargas en el resto;
  la demanda total iguala la generación. Flujo de corriente continua (DC power
  flow): ángulos = B⁺ · P, flujo de cada línea = diferencia de ángulos.
- Cada línea tiene un relé ajustado a (1 + alfa) veces el flujo que llevaba el
  día del ajuste, más un piso (fracción del flujo medio) para que una línea que
  ese día estaba casi vacía no se abra con nada. Es la idea de Motter y Lai
  (2002), que la aplican a nodos y caminos más cortos; acá va en líneas y con
  flujo eléctrico, que es otra cosa.
- Si la red se parte en islas, cada isla equilibra sola: la que tiene más
  generación que carga baja los generadores; la que tiene más carga que
  generación pierde la diferencia (apagón parcial); la isla sin generadores
  queda a oscuras.
- Cascada: se abre una línea; se recalculan flujos; se abren todas las líneas
  cuyo flujo supera su relé; se repite hasta que nada más se abre.

Dos experimentos:
  A. Falla: se abre la línea más cargada, para alfa de 0 a 1. Se mide qué
     fracción de las líneas cayó y qué fracción de la carga quedó a oscuras.
  B. Crecimiento: los relés se ajustan con margen alfa el "año 0"; después la
     demanda de una esquina de la red (la que más crece) sube de a poco hasta
     que una línea supera su relé sin que haya ninguna falla, y ahí arranca
     la cascada. Se anota cuánto creció esa esquina hasta el primer disparo y
     qué pasó después.

Sin dependencias fuera de numpy. Escribe cascada.json y salida_cascada.txt.
"""
import json
import sys
import numpy as np

N = 10            # grilla N x N
PISO = 0.10       # piso del relé: fracción del flujo medio inicial
SEMILLA = 1965


def grilla(n):
    nodos = [(i, j) for i in range(n) for j in range(n)]
    idx = {p: k for k, p in enumerate(nodos)}
    lineas = []
    for i in range(n):
        for j in range(n):
            if i + 1 < n:
                lineas.append((idx[(i, j)], idx[(i + 1, j)]))
            if j + 1 < n:
                lineas.append((idx[(i, j)], idx[(i, j + 1)]))
    return nodos, lineas


def componentes(nn, lineas_vivas):
    ady = {k: [] for k in range(nn)}
    for a, b in lineas_vivas:
        ady[a].append(b)
        ady[b].append(a)
    comp = [-1] * nn
    c = 0
    for s in range(nn):
        if comp[s] >= 0:
            continue
        pila = [s]
        comp[s] = c
        while pila:
            u = pila.pop()
            for v in ady[u]:
                if comp[v] < 0:
                    comp[v] = c
                    pila.append(v)
        c += 1
    return comp, c


def flujos(nn, lineas, vivas, gen, carga):
    """Devuelve (flujo por línea viva, carga servida por nodo, generación por nodo)."""
    lv = [lineas[k] for k in vivas]
    comp, nc = componentes(nn, lv)
    gen_e = gen.copy()
    carga_e = carga.copy()
    # equilibrio por isla
    for c in range(nc):
        m = np.array([comp[k] == c for k in range(nn)])
        g = gen[m].sum()
        d = carga[m].sum()
        if d < 1e-12 and g < 1e-12:
            continue
        if g >= d:
            gen_e[m] = gen[m] * (d / g if g > 0 else 0)
        else:
            carga_e[m] = carga[m] * (g / d)   # se pierde carga (apagón parcial)
    P = gen_e - carga_e
    # B por isla, con un nodo de referencia (ángulo 0) en cada isla; np.linalg.solve
    # en el sistema reducido (la pseudoinversa de este numpy dejaba residuos de 5e-3)
    B = np.zeros((nn, nn))
    for a, b in lv:
        B[a, a] += 1; B[b, b] += 1; B[a, b] -= 1; B[b, a] -= 1
    theta = np.zeros(nn)
    for c in range(nc):
        miembros = [k for k in range(nn) if comp[k] == c]
        if len(miembros) < 2:
            continue
        red = miembros[1:]
        theta[red] = np.linalg.solve(B[np.ix_(red, red)], P[red])
    f = np.array([theta[lineas[k][0]] - theta[lineas[k][1]] for k in vivas])
    return f, carga_e, gen_e


def armar(n, semilla, factor_esquina=1.0):
    rng = np.random.default_rng(semilla)
    nodos, lineas = grilla(n)
    nn = len(nodos)
    gen = np.zeros(nn)
    carga = np.zeros(nn)
    for k, (i, j) in enumerate(nodos):
        if i == 0:
            gen[k] = 1.0 + 0.5 * rng.random()        # fila de generadores
        else:
            carga[k] = 0.5 + rng.random()             # cargas
            if i >= n - 3 and j >= n - 3:             # la esquina que crece
                carga[k] *= factor_esquina
    carga *= gen.sum() / carga.sum()                   # demanda = generación
    return nodos, lineas, gen, carga


def cascada(nn, lineas, gen, carga, cap, vivas, abrir):
    """Abre las líneas `abrir` y deja que los relés hagan lo suyo. Devuelve los pasos."""
    vivas = [k for k in vivas if k not in set(abrir)]
    pasos = [list(abrir)]
    while True:
        f, carga_e, _ = flujos(nn, lineas, vivas, gen, carga)
        caen = [k for k, fk in zip(vivas, f) if abs(fk) > cap[k] + 1e-9]
        if not caen:
            break
        pasos.append(caen)
        vivas = [k for k in vivas if k not in set(caen)]
    f, carga_e, _ = flujos(nn, lineas, vivas, gen, carga)
    return pasos, vivas, carga_e


def experimento_A(alfas, n=N, semilla=SEMILLA, piso=PISO):
    nodos, lineas, gen, carga = armar(n, semilla)
    nn = len(nodos)
    todas = list(range(len(lineas)))
    f0, _, _ = flujos(nn, lineas, todas, gen, carga)
    mas_cargada = int(np.argmax(np.abs(f0)))
    res = []
    for alfa in alfas:
        cap = np.maximum((1 + alfa) * np.abs(f0), piso * np.abs(f0).mean())
        pasos, vivas, carga_e = cascada(nn, lineas, gen, carga, cap, todas, [mas_cargada])
        caidas = sum(len(p) for p in pasos) - 1
        res.append({
            "alfa": alfa,
            "lineas_caidas_ademas_de_la_primera": caidas,
            "fraccion_lineas_caidas": caidas / (len(lineas) - 1),
            "fraccion_carga_a_oscuras": 1 - carga_e.sum() / carga.sum(),
            "pasos": len(pasos) - 1,
        })
    return {"n": n, "nodos": nn, "lineas": len(lineas), "linea_disparada": lineas[mas_cargada],
            "flujo_max_inicial": float(np.abs(f0).max()), "flujo_medio_inicial": float(np.abs(f0).mean()),
            "resultados": res, "pasos_detalle_alfa0": None}


def mapa_cascada(alfa, n=N, semilla=SEMILLA, piso=PISO):
    """Para dibujar: qué línea cayó en qué paso con un alfa dado (experimento A)."""
    nodos, lineas, gen, carga = armar(n, semilla)
    nn = len(nodos)
    todas = list(range(len(lineas)))
    f0, _, _ = flujos(nn, lineas, todas, gen, carga)
    mas_cargada = int(np.argmax(np.abs(f0)))
    cap = np.maximum((1 + alfa) * np.abs(f0), piso * np.abs(f0).mean())
    pasos, vivas, carga_e = cascada(nn, lineas, gen, carga, cap, todas, [mas_cargada])
    paso_de = {}
    for i, p in enumerate(pasos):
        for k in p:
            paso_de[k] = i
    return {"nodos": nodos, "lineas": lineas, "gen": gen.tolist(), "carga": carga.tolist(),
            "carga_servida": carga_e.tolist(), "paso_de": {str(k): v for k, v in paso_de.items()},
            "flujo0": np.abs(f0).tolist(), "alfa": alfa, "pasos": len(pasos)}


def experimento_B(alfa, n=N, semilla=SEMILLA, piso=PISO, paso_crec=0.01, tope=4.0, donde="toda"):
    """Relés ajustados el año 0 con margen alfa; después crece la demanda (toda la red, o solo la
    esquina 3x3 opuesta a los generadores) y los generadores acompañan. Se anota el primer disparo
    sin falla alguna, cuántas líneas llegan juntas a su relé, y la cascada que sigue."""
    nodos, lineas, gen, carga0 = armar(n, semilla)
    nn = len(nodos)
    todas = list(range(len(lineas)))
    f0, _, _ = flujos(nn, lineas, todas, gen, carga0)
    cap = np.maximum((1 + alfa) * np.abs(f0), piso * np.abs(f0).mean())
    esquina = np.array([(i >= n - 3 and j >= n - 3) for (i, j) in nodos])
    factor = 1.0
    while factor < tope:
        factor = round(factor + paso_crec, 4)
        carga2 = carga0.copy()
        if donde == "toda":
            carga2 = carga0 * factor
        else:
            carga2[esquina] = carga0[esquina] * factor
        gen2 = gen * (carga2.sum() / gen.sum())
        f, _, _ = flujos(nn, lineas, todas, gen2, carga2)
        sobre = [k for k in todas if abs(f[k]) > cap[k] + 1e-9]
        if sobre:
            primera = max(sobre, key=lambda k: abs(f[k]) / cap[k])
            piso_manda = bool(piso * np.abs(f0).mean() > (1 + alfa) * abs(f0[primera]))
            pasos, vivas, carga_e = cascada(nn, lineas, gen2, carga2, cap, todas, [primera])
            caidas = sum(len(p) for p in pasos) - 1
            return {"alfa": alfa, "donde": donde, "factor_al_primer_disparo": factor,
                    "crecimiento_total_demanda": float(carga2.sum() / carga0.sum()),
                    "lineas_que_llegan_juntas": len(sobre),
                    "linea_que_dispara": lineas[primera], "flujo0_de_esa_linea": float(abs(f0[primera])),
                    "la_manda_el_piso": piso_manda,
                    "lineas_caidas_ademas_de_la_primera": caidas,
                    "fraccion_lineas_caidas": caidas / (len(lineas) - 1),
                    "fraccion_carga_a_oscuras": 1 - carga_e.sum() / carga2.sum(),
                    "pasos": len(pasos) - 1}
    return {"alfa": alfa, "donde": donde, "factor_al_primer_disparo": None}


def main():
    alfas = [0.0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0]
    A = experimento_A(alfas)
    alfas_B = [0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0]
    B = [experimento_B(a, donde="toda") for a in alfas_B]
    B2 = [experimento_B(a, donde="esquina") for a in alfas_B]
    mapa0 = mapa_cascada(0.0)
    mapa2 = mapa_cascada(0.2)
    salida = {"A": A, "B_toda": B, "B_esquina": B2, "mapa_alfa0": mapa0, "mapa_alfa02": mapa2,
              "parametros": {"N": N, "PISO": PISO, "SEMILLA": SEMILLA}}
    with open("cascada.json", "w") as fh:
        json.dump(salida, fh, indent=1)
    lineas_txt = []
    p = lineas_txt.append
    p(f"Grilla {N}x{N}: {A['nodos']} nodos, {A['lineas']} líneas. Piso del relé: {PISO:.0%} del flujo medio.")
    p(f"Línea más cargada (la que se abre en A): {A['linea_disparada']}, flujo {A['flujo_max_inicial']:.3f} "
      f"(medio {A['flujo_medio_inicial']:.3f}).")
    p("")
    p("A. Se abre la línea más cargada. Por alfa: líneas caídas además de la primera, "
      "fracción de líneas, fracción de carga a oscuras, pasos de la cascada.")
    for r in A["resultados"]:
        p(f"  alfa={r['alfa']:.2f}  caídas={r['lineas_caidas_ademas_de_la_primera']:3d}  "
          f"líneas={r['fraccion_lineas_caidas']:.1%}  a oscuras={r['fraccion_carga_a_oscuras']:.1%}  pasos={r['pasos']}")
    p("")
    p("B. Relés ajustados el año 0 con margen alfa; después crece la demanda y los generadores acompañan. "
      "Primer disparo sin falla, cuántas líneas llegan juntas a su relé, y la cascada que sigue.")
    for titulo, lista in (("B1. Crece toda la red por igual:", B), ("B2. Crece solo la esquina 3x3 opuesta a los generadores:", B2)):
        p("  " + titulo)
        for r in lista:
            if r["factor_al_primer_disparo"] is None:
                p(f"    alfa={r['alfa']:.2f}  ningún disparo hasta cuadruplicar")
            else:
                p(f"    alfa={r['alfa']:.2f}  primer disparo con demanda x{r['factor_al_primer_disparo']:.2f} "
                  f"(total x{r['crecimiento_total_demanda']:.3f}); llegan juntas {r['lineas_que_llegan_juntas']} líneas; "
                  f"dispara {r['linea_que_dispara']} (flujo inicial {r['flujo0_de_esa_linea']:.3f}"
                  f"{', la manda el piso' if r['la_manda_el_piso'] else ''}); "
                  f"caen {r['lineas_caidas_ademas_de_la_primera']} más ({r['fraccion_lineas_caidas']:.1%}), "
                  f"a oscuras {r['fraccion_carga_a_oscuras']:.1%}, pasos={r['pasos']}")
    p("")
    p(f"Mapa alfa=0: {mapa0['pasos']} pasos; mapa alfa=0,2: {mapa2['pasos']} pasos.")
    txt = "\n".join(lineas_txt)
    with open("salida_cascada.txt", "w") as fh:
        fh.write(txt + "\n")
    print(txt)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    main()
