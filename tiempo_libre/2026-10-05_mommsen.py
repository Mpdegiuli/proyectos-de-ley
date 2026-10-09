#!/usr/bin/env python3
"""La restitución de Mommsen para Res Gestae 34.3, medida como se mide a una máquina.

Tres estados de la misma oración:
  ANCYRA   lo que se leía en Ankara (corchetes de la edición de Fairley, 1898, que sigue a Mommsen)
  MOMMSEN  lo que Mommsen puso en los huecos (1883)
  HOY      el texto compuesto con los fragmentos de Antioquía (versión con corchetes de The Latin Library)
Los textos están copiados acá a mano; las fuentes están en el cuaderno.

Mide la distancia de edición (Levenshtein), letra por letra, entre lo que Mommsen puso
en cada hueco y lo que hoy se lee o se restituye en ese mismo hueco, y la divide por el
largo del texto de hoy: es la "tasa de error por carácter" (CER) que usan Ithaca y Aeneas.
Es una cuenta sobre UNA oración; sirve de ilustración, no de estadística.
"""
def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

def letras(s):
    return "".join(c for c in s.lower() if c.isalpha())

MOMMSEN = "Post id tem[pus praestiti omnibus dignitate potest]atis au[tem n]ihilo ampliu[s habui quam qui fuerunt m]ihi quoque in ma[gis]tra[t]u conlegae"
HOY     = "Post id tem[pus a]uctoritate [omnibus praestiti potest]atis au[tem n]ihilo ampliu[s habu]i quam cet[eri qui m]ihi quoque in ma[gis]tra[t]u conlegae f[uerunt]"

# huecos de Ancyra en 34.3 y lo que va en cada uno, según Mommsen y según el texto de hoy
HUECOS = [
    ("tem[…]atis",     "pus praestiti omnibus dignitate potest", "pus auctoritate omnibus praestiti potest"),
    ("au[…]ihilo",     "tem n",                                  "tem n"),
    ("ampliu[…]ihi",   "s habui quam qui fuerunt m",             "s habui quam ceteri qui m"),
    ("ma[…]tra[…]u",   "gist",                                   "gist"),
]
tot_d = tot_n = 0
print("hueco            Mommsen → hoy                                                    dist  largo")
for nombre, m, h in HUECOS:
    d = lev(letras(m), letras(h)); n = len(letras(h))
    tot_d += d; tot_n += n
    print(f"{nombre:16} {m:38} → {h:40} {d:3} {n:5}")
print(f"\nCER de Mommsen en los huecos de 34.3: {tot_d}/{tot_n} = {100*tot_d/tot_n:.0f} %")
# el "fuerunt" del final: Antioquía muestra que la oración seguía después de "conlegae"
d7 = lev("", "fuerunt")
print(f"sumando el final (nada → fuerunt): {tot_d + d7}/{tot_n + 7} = {100*(tot_d + d7)/(tot_n + 7):.0f} %")

# la oración entera
om = "Post id tempus praestiti omnibus dignitate potestatis autem nihilo amplius habui quam qui fuerunt mihi quoque in magistratu conlegae"
oh = "Post id tempus auctoritate omnibus praestiti potestatis autem nihilo amplius habui quam ceteri qui mihi quoque in magistratu conlegae fuerunt"
print(f"oración entera: distancia {lev(letras(om), letras(oh))} sobre {len(letras(oh))} letras")
pm, ph = om.lower().split(), oh.lower().split()
print(f"palabras de Mommsen: {len(pm)}; de hoy: {len(ph)}; "
      f"solo en Mommsen: {sorted(set(pm) - set(ph))}; solo hoy: {sorted(set(ph) - set(pm))}")

# cuánto de la oración de hoy está en piedra
def piedra(s):
    dentro = fuera = 0; nivel = 0
    for ch in s:
        if ch == "[": nivel = 1
        elif ch == "]": nivel = 0
        elif ch.isalpha():
            dentro += nivel; fuera += 1 - nivel
    return fuera, dentro
for nombre, s in (("con Ancyra sola (Mommsen)", MOMMSEN), ("con Antioquía (hoy)", HOY)):
    f, d = piedra(s)
    print(f"{nombre}: {f} letras en piedra, {d} restituidas ({100*d/(f+d):.0f} %)")

# 34.1
print("\n34.1: potitus → potens: distancia", lev("potitus", "potens"), "sobre", len("potens"), "letras")
print("      el fragmento de Botteri trae TENS RE: seis letras")
# dignitate / auctoritate
a, b = "dignitate", "auctoritate"
suf = 0
while a[-1 - suf] == b[-1 - suf]: suf += 1
print(f"\ndignitate ({len(a)} letras) y auctoritate ({len(b)}) terminan igual en {suf} letras: -{a[-suf:]}")
