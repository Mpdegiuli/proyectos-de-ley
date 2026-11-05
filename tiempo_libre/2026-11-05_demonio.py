"""Un demonio de Maxwell con la memoria a la vista.

Gas ideal en dos dimensiones (las partículas no chocan entre sí, rebotan en las paredes), caja
de 2 × 1 partida al medio por un tabique con una puerta de 0,1 de alto. Cada vez que una
partícula llega a la puerta, el demonio decide: abrir o cerrar. Cada decisión es un bit que el
demonio tiene que anotar en su memoria (Bennett, 1982: lo que cuesta no es ver ni decidir, es
borrar ese registro para poder seguir). El programa cuenta los bits y, al mismo tiempo, la
entropía del gas (Sackur-Tetrode en dos dimensiones, por cámara), para cotejar la cuenta de
Bennett: bits · ln 2 ≥ −ΔS/k.

Cuatro demonios:
  temperatura  deja pasar las rápidas hacia la derecha y las lentas hacia la izquierda
  valvula      deja pasar todo lo que va hacia la derecha y nada de lo que vuelve (el "demonio
               menos inteligente" de la carta de Maxwell a Tait: "This reduces the demon to a valve")
  abierta      puerta siempre abierta (control: no pasa nada)
  cerrada      puerta siempre cerrada (control)

Unidades: k = m = 1; la temperatura inicial es 1 (velocidades gaussianas de desvío 1 por eje),
así que en 2D la energía cinética media por partícula es kT = 1 y T = <v²>/2.

Uso:  python3 demonio.py [semilla]      escribe demonio.json y salida_demonio.txt
"""
import json
import math
import os
import sys

import numpy as np

SEMILLA = int(sys.argv[1]) if len(sys.argv) > 1 else 1879   # el año
N = 600
ANCHO, ALTO = 2.0, 1.0
PUERTA = (0.45, 0.55)
DT = 0.002
T_FIN = 60.0
CADA = 50                      # pasos entre dos registros de la serie
UMBRAL_V2 = 2 * math.log(2)    # mediana de v² en 2D con <v²> = 2: separa "rápidas" de "lentas"


def entropia(x, v2):
    """S/k del gas ideal 2D en las dos cámaras, sin la constante: Σ N_i [ln(A_i/N_i) + ln T_i]."""
    s = 0.0
    for lado in (x < 1.0, x >= 1.0):
        n = int(lado.sum())
        if n == 0:
            continue
        T = v2[lado].mean() / 2
        s += n * (math.log(1.0 / n) + math.log(T))
    return s


def correr(demonio, semilla=SEMILLA):
    rng = np.random.default_rng(semilla)
    x = rng.uniform(0, ANCHO, N)
    y = rng.uniform(0, ALTO, N)
    vx = rng.normal(0, 1, N)
    vy = rng.normal(0, 1, N)
    v2 = vx * vx + vy * vy
    s0 = entropia(x, v2)
    bits = 0
    pasaron = 0
    llegadas = 0
    serie = []
    pasos = int(round(T_FIN / DT))
    for paso in range(pasos + 1):
        if paso % CADA == 0:
            izq = x < 1.0
            nl = int(izq.sum())
            tl = float(v2[izq].mean() / 2) if nl else float("nan")
            tr = float(v2[~izq].mean() / 2) if nl < N else float("nan")
            serie.append({"t": round(paso * DT, 3), "NL": nl, "NR": N - nl,
                          "TL": tl, "TR": tr, "bits": bits, "pasaron": pasaron,
                          "menosDS": -(entropia(x, v2) - s0)})
        if paso == pasos:
            break
        xn = x + vx * DT
        yn = y + vy * DT
        # paredes de arriba y de abajo
        arriba = yn > ALTO
        yn[arriba] = 2 * ALTO - yn[arriba]
        vy[arriba] *= -1
        abajo = yn < 0
        yn[abajo] = -yn[abajo]
        vy[abajo] *= -1
        # paredes de los costados
        der = xn > ANCHO
        xn[der] = 2 * ANCHO - xn[der]
        vx[der] *= -1
        izq = xn < 0
        xn[izq] = -xn[izq]
        vx[izq] *= -1
        # el tabique
        cruza = (x < 1.0) != (xn < 1.0)
        if cruza.any():
            idx = np.nonzero(cruza)[0]
            frac = (1.0 - x[idx]) / (xn[idx] - x[idx])
            yc = y[idx] + frac * (yn[idx] - y[idx])
            en_puerta = (yc >= PUERTA[0]) & (yc <= PUERTA[1])
            hacia_der = vx[idx] > 0
            if demonio == "temperatura":
                abre = (hacia_der & (v2[idx] > UMBRAL_V2)) | (~hacia_der & (v2[idx] <= UMBRAL_V2))
            elif demonio == "valvula":
                abre = hacia_der
            elif demonio == "abierta":
                abre = np.ones(len(idx), bool)
            elif demonio == "cerrada":
                abre = np.zeros(len(idx), bool)
            else:
                raise ValueError(demonio)
            llegadas += int(en_puerta.sum())
            if demonio in ("temperatura", "valvula"):
                bits += int(en_puerta.sum())          # una decisión por llegada a la puerta
            pasaron += int((en_puerta & abre).sum())
            rebota = ~(en_puerta & abre)
            r = idx[rebota]
            xn[r] = 2.0 - xn[r]
            vx[r] *= -1
        x, y = xn, yn
    return {"demonio": demonio, "N": N, "semilla": semilla, "serie": serie,
            "bits": bits, "pasaron": pasaron, "llegadas": llegadas, "menosDS": serie[-1]["menosDS"],
            "NL": serie[-1]["NL"], "NR": serie[-1]["NR"], "TL": serie[-1]["TL"], "TR": serie[-1]["TR"]}


def main():
    res = {d: correr(d) for d in ("temperatura", "valvula", "abierta", "cerrada")}
    aqui = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(aqui, "demonio.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, separators=(",", ":"))
    lineas = []
    p = lineas.append
    p(f"N = {N} partículas, caja {ANCHO} × {ALTO}, puerta de {PUERTA[1]-PUERTA[0]:.2f} de alto, "
      f"dt = {DT}, t final = {T_FIN}, semilla {SEMILLA}")
    p(f"umbral de velocidad (mediana de v²): {UMBRAL_V2:.4f}")
    p("")
    for d, r in res.items():
        p(f"[{d}]")
        p(f"  al final: N izquierda {r['NL']}, N derecha {r['NR']}; T izquierda {r['TL']:.3f}, T derecha {r['TR']:.3f}")
        p(f"  llegadas a la puerta (bits anotados): {r['bits']}; pasaron: {r['pasaron']}")
        p(f"  bits · ln 2 = {r['bits']*math.log(2):.1f}   −ΔS/k = {r['menosDS']:.1f}")
        if r["bits"]:
            p(f"  cociente (bits · ln 2) / (−ΔS/k) = {r['bits']*math.log(2)/r['menosDS']:.2f}"
              if r["menosDS"] > 0 else "  (la entropía no bajó)")
        # cuándo la memoria ya llevaba diez veces lo que había bajado la entropía
        for fila in r["serie"]:
            if fila["menosDS"] > 5 and fila["bits"] * math.log(2) > 10 * fila["menosDS"]:
                p(f"  a t = {fila['t']} la memoria (bits · ln 2 = {fila['bits']*math.log(2):.0f}) ya era "
                  f"diez veces −ΔS/k ({fila['menosDS']:.1f})")
                break
        # cuándo se alcanzó la mitad de la caída final de entropía
        if r["menosDS"] > 0:
            for fila in r["serie"]:
                if fila["menosDS"] >= r["menosDS"] / 2:
                    p(f"  la mitad de la caída de entropía se alcanzó a t = {fila['t']}, con {fila['bits']} bits")
                    break
        p("")
    # la cuenta de Landauer a 300 K
    k = 1.380649e-23
    kTln2 = k * 300 * math.log(2)
    p(f"k·T·ln 2 a 300 K = {kTln2:.3e} J = {kTln2/1.602176634e-19*1000:.2f} meV")
    r = res["temperatura"]
    p(f"borrar la memoria del demonio de temperatura ({r['bits']} bits) costaría, como mínimo, "
      f"{r['bits']*kTln2:.2e} J a 300 K")
    palabras = 1_478_093
    bits_corpus = palabras * 5.5 * 8   # 5,5 caracteres por palabra en castellano, un byte cada uno: estimación gruesa
    p(f"borrar las {str(palabras).replace(',', '.')} palabras en castellano del repositorio "
      f"(unos {bits_corpus/8/1e6:.0f} MB, {bits_corpus:.2e} bits) costaría, como mínimo, "
      f"{bits_corpus*kTln2:.2e} J a 300 K")
    llegadas = {d: r["llegadas"] for d, r in res.items()}
    p(f"llegadas a la puerta por demonio: {llegadas} (con la misma semilla son iguales: en un gas ideal "
      f"y una caja simétrica, rebotar o pasar dan trayectorias espejo, y la próxima llegada al plano del "
      f"tabique ocurre en el mismo instante; el demonio no cambia cuántas decisiones tiene que tomar)")
    texto = "\n".join(lineas)
    with open(os.path.join(aqui, "salida_demonio.txt"), "w", encoding="utf-8") as f:
        f.write(texto + "\n")
    print(texto)


if __name__ == "__main__":
    main()
