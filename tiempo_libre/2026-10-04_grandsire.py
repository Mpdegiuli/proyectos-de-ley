# grandsire.py — tiempo libre 4/10/2026. Solo biblioteca estándar.
# Grandsire Triples: siete campanas, 14 cambios por "lead". Notación de lugares:
#   lead simple:  3.1.7.1.7.1.7.1.7.1.7.1.7.1
#   con bob:      los dos últimos cambios son 3.1
#   con single:   los dos últimos cambios son 3.123
# Comprueba el teorema de Thompson (1886) a fuerza de cuentas y busca el bloque más largo
# que se puede tocar solo con bobs. Uso: python3 grandsire.py [pasos] [semillas]
import random, sys
from itertools import permutations
from campanas import cambio, paridad

R = tuple(range(1, 8))
BASE = [{3}, {1}] + [{7}, {1}] * 5
FIN = {"P": [{7}, {1}], "B": [{3}, {1}], "S": [{3}, {1, 2, 3}]}

def lead(h, c):
    filas = []; f = h
    for lug in BASE + FIN[c]:
        f = cambio(f, lug); filas.append(f)
    return filas                       # 14 filas; la última es la cabeza del lead siguiente

def sig(h, c):
    return lead(h, c)[-1]

def filas_de(cabeza, llamadas):
    """Todas las filas de un toque que empieza en `cabeza` con esa lista de llamadas."""
    out = []; h = cabeza
    for c in llamadas:
        L = lead(h, c); out.extend(L); h = L[-1]
    return out, h

if __name__ == "__main__":
    # curso simple
    h = R; cabezas = []
    while True:
        h = sig(h, "P"); cabezas.append("".join(map(str, h)))
        if h == R: break
    print("curso simple, cabezas de lead:", cabezas, "->", 14 * len(cabezas), "cambios")
    print("desde rounds: con bob", "".join(map(str, sig(R, "B"))), "; con single", "".join(map(str, sig(R, "S"))))
    pares = [p for p in permutations(R) if p[0] == 1 and paridad(p) == 0]
    print("cabezas de lead en curso (pares, con la 1 adelante):", len(pares))
    todas = set()
    for p in pares:
        todas.update(lead(p, "P"))
    print("filas distintas en los 360 leads simples:", len(todas))
    idx = {p: i for i, p in enumerate(pares)}
    P = [idx[sig(p, "P")] for p in pares]; B = [idx[sig(p, "B")] for p in pares]
    invP = [0] * 360
    for i, j in enumerate(P): invP[j] = i
    def orden(perm):
        k, x = 1, perm[0]
        while x != 0: x = perm[x]; k += 1
        return k
    def ciclos(s):
        visto = [False] * len(s); largos = []
        for i in range(len(s)):
            if not visto[i]:
                k = 0; j = i
                while not visto[j]: visto[j] = True; j = s[j]; k += 1
                largos.append(k)
        return largos
    print("ciclos de P:", sorted(set(ciclos(P))), "x", len(ciclos(P)), "; ciclos de B:", sorted(set(ciclos(B))), "x", len(ciclos(B)))
    # Q-sets: si un lead pasa de simple a bob, cae en la cabeza a la que iba otro lead simple;
    # ese otro tiene que cambiar también, y así hasta cerrar.
    q_de = [None] * 360; Q = []
    for i in range(360):
        if q_de[i] is None:
            q = []; j = i
            while q_de[j] is None:
                q_de[j] = len(Q); q.append(j); j = invP[B[j]]
            Q.append(q)
    print("Q-sets:", len(Q), "de tamaño", sorted(set(len(q) for q in Q)))

    def sucesor(bobs):                 # bobs: conjunto de índices de Q-sets con bob
        return [B[i] if q_de[i] in bobs else P[i] for i in range(360)]
    # comprobación de Thompson: con cualquier elección de Q-sets, la cantidad de bloques es par
    rng = random.Random(1886)
    pares_siempre = True; minimo = 360; vistos = set()
    for _ in range(20000):
        bobs = {k for k in range(len(Q)) if rng.random() < rng.choice((0.1, 0.3, 0.5, 0.7, 0.9))}
        s = sucesor(bobs)
        assert sorted(s) == list(range(360))
        c = len(ciclos(s)); vistos.add(c)
        if c % 2: pares_siempre = False
        minimo = min(minimo, c)
    print("20.000 elecciones al azar de Q-sets: cantidad de bloques siempre par:", pares_siempre,
          "; valores vistos:", min(vistos), "a", max(vistos), "; todo simple:", len(ciclos(P)), "; todo bob:", len(ciclos(B)))

    # búsqueda: el bloque más largo solo con bobs (recocido simulado sobre los Q-sets)
    import math
    def mejor_bloque(semilla, pasos):
        rng = random.Random(semilla)
        bobs = {k for k in range(len(Q)) if rng.random() < 0.5}
        def puntaje(b):
            cs = ciclos(sucesor(b)); return max(cs), len(cs)
        act = puntaje(bobs); mejor = (act, set(bobs))
        for t in range(pasos):
            T = 6.0 * (1 - t / pasos) + 0.05
            k = rng.randrange(len(Q)); bobs ^= {k}
            nu = puntaje(bobs)
            if nu[0] >= act[0] or rng.random() < math.exp((nu[0] - act[0]) / T):
                act = nu
                if act[0] > mejor[0][0]: mejor = (act, set(bobs))
            else:
                bobs ^= {k}
        return mejor
    pasos = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    tope = None
    for semilla in range(int(sys.argv[2]) if len(sys.argv) > 2 else 6):
        (largo, nbloques), bobs = mejor_bloque(semilla, pasos)
        cs = sorted(ciclos(sucesor(bobs)), reverse=True)
        print(f"semilla {semilla}: bloque más largo {largo} leads = {14*largo} cambios; bloques: {cs[:8]}{'...' if len(cs) > 8 else ''}")
        if tope is None or largo > tope[0]: tope = (largo, bobs)
    largo, bobs = tope
    # reconstruir las llamadas del bloque más largo y comprobar fila por fila
    s = sucesor(bobs); visto = [False] * 360; mejor_ini = None
    for i in range(360):
        if not visto[i]:
            j = i; k = 0
            while not visto[j]: visto[j] = True; j = s[j]; k += 1
            if k == largo: mejor_ini = i
    j = mejor_ini; llamadas = []
    for _ in range(largo):
        llamadas.append("B" if q_de[j] in bobs else "P"); j = s[j]
    filas, fin = filas_de(pares[mejor_ini], llamadas)
    print("mejor encontrado:", 14 * largo, "cambios;", llamadas.count("B"), "bobs; filas distintas:", len(set(filas)),
          "; vuelve al comienzo:", fin == pares[mejor_ini])
    open("toque_solo_bobs.txt", "w").write("".join(map(str, pares[mejor_ini])) + "\n" + "".join(llamadas) + "\n")
