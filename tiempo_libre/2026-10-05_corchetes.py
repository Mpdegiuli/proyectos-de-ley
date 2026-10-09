#!/usr/bin/env python3
"""Cuánto de las Res Gestae en latín está entre corchetes, y dónde cae "auctoritate".

Lee la versión con corchetes que trae The Latin Library ("Res Gestae II", archivo
resgestae1.txt de la copia de CLTK) y cuenta letras dentro y fuera de [ ].
Compara además, capítulo por capítulo, con la versión corrida (resgestae.txt).

    git clone --depth 1 https://github.com/cltk/lat_text_latin_library.git
    python3 corchetes.py RUTA_AL_CLON

Salvedad: la página no dice de qué edición sale el texto con corchetes, y tiene
erratas ("oxstinxeram", "pea potestate"). Es un texto compuesto (Ancyra más
Antioquía), anterior a 2003: todavía dice [potitus reru]m.
"""
import re, sys, os
RAIZ = sys.argv[1] if len(sys.argv) > 1 else "../lat_text_latin_library"
b = open(os.path.join(RAIZ, "resgestae1.txt"), encoding="utf-8", errors="replace").read()
p = open(os.path.join(RAIZ, "resgestae.txt"), encoding="utf-8", errors="replace").read()

# capítulos de la versión con corchetes: líneas que empiezan con "N. "
b = b[b.find("1. Annos"):]
cap_b = {}
partes = re.split(r"(?m)^\s*(\d{1,2})\. ", b)
for i in range(1, len(partes), 2):
    n = int(partes[i])
    if n not in cap_b and 1 <= n <= 35:
        cap_b[n] = partes[i + 1]
# cortar el apéndice después del 35
cap_b[35] = cap_b[35].split("APPENDIX")[0].split("Appendix")[0]

def cuenta(t):
    dentro = fuera = 0; nivel = 0
    for ch in t:
        if ch == "[": nivel += 1
        elif ch == "]": nivel = max(0, nivel - 1)
        elif ch.isalpha():
            if nivel: dentro += 1
            else: fuera += 1
    return dentro, fuera

D = F = 0
filas = []
for n in sorted(cap_b):
    d, f = cuenta(cap_b[n]); D += d; F += f
    filas.append((n, d, f))
print(f"capítulos leídos: {len(cap_b)}")
print(f"letras fuera de corchetes: {F}   dentro: {D}   restituido: {100*D/(D+F):.1f} %")
print("capítulos con más restitución:")
for n, d, f in sorted(filas, key=lambda x: -x[1] / (x[1] + x[2]))[:6]:
    print(f"  cap. {n:2}: {100*d/(d+f):.0f} % ({d} de {d+f} letras)")
n, d, f = filas[33]
print(f"cap. 34: {100*d/(d+f):.0f} % ({d} de {d+f} letras)")

print('\n"auctor-" en la versión con corchetes:')
for n in sorted(cap_b):
    t = re.sub(r"\s+", " ", cap_b[n])
    liso = re.sub(r"[\[\]]", "", t)
    for m in re.finditer(r"auctor\w*", liso):
        # reubicar en el texto con corchetes
        k = 0; ini = None; fin = None
        for j, ch in enumerate(t):
            if ch in "[]": continue
            if k == m.start(): ini = j
            k += 1
            if k == m.end(): fin = j + 1; break
        a = t[max(0, ini - 28): fin + 22]
        print(f"  cap. {n:2}: …{a}…")

print('\n"auctor-", "consulto", "decret-", "auspic-" en la versión corrida, caps. 12, 20, 28, 34:')
pp = re.sub(r"\s+", " ", p)
caps_p = re.split(r"\[ ?(\d+) ?\]", pp)
cap_p = {int(caps_p[i]): caps_p[i + 1] for i in range(1, len(caps_p), 2)}
for n in (12, 20, 28, 34):
    for m in re.finditer(r"[^.,;]*\b(auctor|auspic)\w*[^.,;]*", cap_p[n]):
        print(f"  cap. {n:2}: {m.group(0).strip()[:110]}")
