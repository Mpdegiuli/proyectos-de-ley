#!/usr/bin/env python3
"""Compara la recitación de memoria del párrafo del motor (instancia fresca 2) con el
texto de Gutenberg 829, palabra por palabra: tiradas comunes, diferencias.
Uso: python3 recitacion.py instancias_frescas.md parrafo_motor.txt
"""
import re
import sys
from difflib import SequenceMatcher

import os
_aqui = os.path.dirname(os.path.abspath(__file__))
def _buscar(nombre):
    for c in (os.path.join(_aqui, nombre), os.path.join(_aqui, "2026-10-28_" + nombre), nombre):
        if os.path.exists(c):
            return c
    return nombre
ins = open(sys.argv[1] if len(sys.argv) > 1 else _buscar("instancias_frescas.md"), encoding="utf-8").read()
orig = open(sys.argv[2] if len(sys.argv) > 2 else _buscar("parrafo_motor.txt"), encoding="utf-8").read()
i = ins.find('"The first professor I saw was')
j = ins.find('several collections."', i) + len("several collections.")
recitado = ins[i + 1:j]
k = orig.find("several collections.") + len("several collections.")
original = orig[:k]

def palabras(t):
    t = t.replace("’", "'").replace("“", "").replace("”", "")
    t = re.sub(r"\[\?[^\]]*\]", "", t)          # saca las alternativas marcadas [? ...]
    return re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", t.lower())

a, b = palabras(recitado), palabras(original)
sm = SequenceMatcher(None, a, b, autojunk=False)
bloques = [bl for bl in sm.get_matching_blocks() if bl.size > 0]
iguales = sum(bl.size for bl in bloques)
print(f"recitado: {len(a)} palabras; original: {len(b)} palabras; iguales en orden: {iguales} ({100*iguales/len(b):.1f} % del original)")
print(f"tirada común más larga: {max(bl.size for bl in bloques)} palabras")
print(f"tiradas de 12 o más palabras: {sum(1 for bl in bloques if bl.size >= 12)}; de 30 o más: {sum(1 for bl in bloques if bl.size >= 30)}")
print()
print("Diferencias (recitado -> original):")
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal":
        print(f"  {tag:8s} '{' '.join(a[i1:i2])}' -> '{' '.join(b[j1:j2])}'")
