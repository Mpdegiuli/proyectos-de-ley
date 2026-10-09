# cuentas.py — tiempo libre 4/10/2026. Cuentas sobre 5040. Solo biblioteca estándar.
import math
from itertools import permutations

N = 5040
divs = [d for d in range(1, N + 1) if N % d == 0]
print("5040 =", "2^4 * 3^2 * 5 * 7;  7! =", math.factorial(7), "; 7*8*9*10 =", 7*8*9*10)
print("divisores:", len(divs), "(sin el propio 5040:", len(divs) - 1, ")")
print("divisible por 1..10:", all(N % k == 0 for k in range(1, 11)), "; por 11:", N % 11 == 0, "; por 12:", N % 12 == 0)
print("5038 / 11 =", 5038 / 11, "; 5040 / 12 =", N // 12, "; 420 divisores:", sum(1 for d in range(1, 421) if 420 % d == 0))
print("primer entero no divisor de 5040:", next(k for k in range(1, 100) if N % k))
print("420 divisible por 1..7:", all(420 % k == 0 for k in range(1, 8)), "; 420/12 =", 420 // 12)

# números altamente compuestos hasta 5040
LIM = 6000
d = [0] * (LIM + 1)
for i in range(1, LIM + 1):
    for j in range(i, LIM + 1, i):
        d[j] += 1
hc, best = [], 0
for n in range(1, LIM + 1):
    if d[n] > best:
        best = d[n]; hc.append(n)
print("altamente compuestos hasta", LIM, ":", hc, "-> 5040 es el n.º", hc.index(5040) + 1)

# Robin: sigma(n) < e^gamma * n * ln ln n para n > 5040  (equivale a la hipótesis de Riemann)
G = 0.57721566490153286060651209
LIM2 = 10_000_000
sig = [0] * (LIM2 + 1)
for i in range(1, LIM2 + 1):
    for j in range(i, LIM2 + 1, i):
        sig[j] += i
eg = math.exp(G)
exc = [n for n in range(2, LIM2 + 1) if sig[n] >= eg * n * math.log(math.log(n))]
print("excepciones a la desigualdad de Robin entre 2 y", LIM2, ":", exc, "(", len(exc), ")")
r = lambda n: sig[n] / (n * math.log(math.log(n)))
print("sigma(5040) =", sig[5040], "; sigma(n)/(n ln ln n) en 5040:", round(r(5040), 5), " e^gamma =", round(eg, 5))
m = max(range(5041, LIM2 + 1), key=r)
print("el que más se acerca después de 5040 (hasta 10^7):", m, round(r(m), 5))
