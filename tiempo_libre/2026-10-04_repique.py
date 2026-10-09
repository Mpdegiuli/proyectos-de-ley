# repique.py — tiempo libre 4/10/2026. Solo biblioteca estándar; usa campanas.py y grandsire.py.
# Busca un 5040 de Grandsire Triples en dos pasos:
#  1) recocido simulado sobre los 72 Q-sets hasta dar con un bloque de 357 leads (4998 cambios)
#     hecho solo con bobs; lo que queda afuera es un bloque de tres leads con bob (42 cambios);
#  2) probar, en cada lead del bloque grande, si esos 42 cambios entran con dos singles:
#     single, dos leads, single, y de vuelta al bloque grande donde se lo dejó.
# Cada candidato se comprueba fila por fila: 5040 filas, todas distintas, y termina en rounds.
# Uso: python3 repique.py [cantidad de semillas]
import random, math, sys
from itertools import permutations, product
from collections import Counter
from campanas import paridad
from grandsire import R, lead, sig, filas_de

pares = [p for p in permutations(R) if p[0] == 1 and paridad(p) == 0]
idx = {p: i for i, p in enumerate(pares)}
P = [idx[sig(p, "P")] for p in pares]; B = [idx[sig(p, "B")] for p in pares]
invP = [0] * 360
for i, j in enumerate(P): invP[j] = i
q_de = [None] * 360; Q = []
for i in range(360):
    if q_de[i] is None:
        q = []; j = i
        while q_de[j] is None:
            q_de[j] = len(Q); q.append(j); j = invP[B[j]]
        Q.append(q)

def ciclos(s):
    visto = [False] * 360; out = []
    for i in range(360):
        if not visto[i]:
            c = []; j = i
            while not visto[j]: visto[j] = True; c.append(j); j = s[j]
            out.append(c)
    return out

def recocido(semilla, pasos=4000):
    rng = random.Random(semilla)
    bobs = {k for k in range(72) if rng.random() < 0.5}
    suc = lambda b: [B[i] if q_de[i] in b else P[i] for i in range(360)]
    act = max(len(c) for c in ciclos(suc(bobs)))
    for t in range(pasos):
        if act == 357: break
        T = 6.0 * (1 - t / pasos) + 0.05
        k = rng.randrange(72); bobs ^= {k}
        nu = max(len(c) for c in ciclos(suc(bobs)))
        if nu >= act or rng.random() < math.exp((nu - act) / T): act = nu
        else: bobs ^= {k}
    return act, bobs, suc(bobs)

if __name__ == "__main__":
    intentos = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    hallados = []; n4998 = 0; entre = Counter(); por_bloque = Counter(); mismos_cuerpos = 0
    for semilla in range(intentos):
        largo, bobs, s = recocido(semilla)
        if largo != 357: continue
        n4998 += 1
        cs = ciclos(s); grande = max(cs, key=len); chico = min(cs, key=len)
        llam = ["B" if q_de[i] in bobs else "P" for i in grande]
        for pos in range(357):
            h = pares[grande[pos]]; despues = pares[grande[(pos + 1) % 357]]
            o1 = sig(h, "S")
            for c1, c2 in product("PB", repeat=2):
                o2 = sig(o1, c1); o3 = sig(o2, c2)
                if sig(o3, "S") != despues: continue
                orden = [(pos + 1 + k) % 357 for k in range(357)]
                llamadas = [llam[i] for i in orden[:-1]] + ["S", c1, c2, "S"]
                filas, fin = filas_de(despues, llamadas)
                if fin == despues and len(set(filas)) == 5040 == len(filas):
                    hallados.append((semilla, despues, llamadas)); entre[c1 + c2] += 1; por_bloque[semilla] += 1
                    # ¿cada lead del tramo recorre al revés las 12 filas de un lead del bloque chico?
                    del_chico = [lead(pares[i], "P")[:12] for i in chico]
                    if all(lead(o, "P")[:12][::-1] in del_chico for o in (o1, o2, o3)): mismos_cuerpos += 1
    print("semillas probadas:", intentos, "; bloques de 4998 solo con bobs:", n4998,
          "; repiques de 5040 verdaderos:", len(hallados), "en", len(por_bloque), "bloques")
    print("llamadas entre los dos singles:", dict(entre),
          "; los tres leads del tramo recorren al revés las filas de los tres leads sobrantes:", mismos_cuerpos, "de", len(hallados))
    if hallados:
        semilla, cab, llamadas = min(hallados, key=lambda x: (x[2].count("B"), x[0]))
        # girarlo para que el bloque SBBS quede al final; rebautizando las campanas, cualquier
        # giro de las llamadas es otro repique verdadero que empieza y termina en rounds
        c = "".join(llamadas); k = c.index("SBBS") + 4
        llamadas = list(c[k:] + c[:k])
        filas, fin = filas_de(R, llamadas)
        assert fin == R and len(filas) == 5040 and set(filas) == set(permutations(R)) and filas[-1] == R
        ant = R
        for f in filas:               # ninguna campana se mueve más de un lugar por cambio
            assert all(abs(f.index(b) - ant.index(b)) <= 1 for b in R); ant = f
        print("el de menos llamadas: semilla", semilla, ";", llamadas.count("B"), "bobs,", llamadas.count("S"),
              "singles,", llamadas.count("P"), "leads simples; singles en los leads",
              [i + 1 for i, c in enumerate(llamadas) if c == "S"])
        print("cantidades de bobs en todos los hallados: de", min(x[2].count("B") for x in hallados), "a", max(x[2].count("B") for x in hallados))
        open("repique_5040.txt", "w").write(
            "# Un 5040 de Grandsire Triples encontrado por búsqueda el 4/10/2026 (repique.py, semilla %d),\n"
            "# girado para que el bloque SBBS quede al final. Una letra por lead, desde rounds (1234567):\n"
            "# P = lead simple, B = bob, S = single. 360 leads de 14 cambios; %d bobs y %d singles.\n"
            "# Comprobado fila por fila: 5040 filas, todas distintas, la última es rounds.\n"
            % (semilla, llamadas.count("B"), llamadas.count("S")) + "".join(llamadas) + "\n")
        print("".join(llamadas))
