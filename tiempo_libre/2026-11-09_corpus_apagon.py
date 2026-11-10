#!/usr/bin/env python3
"""Cuenta las palabras de hoy en las respuestas en castellano del repositorio (solo lee).
Uso: python3 corpus_apagon.py <raíz del clon>   (necesita cargar.py al lado, el del 7/10)."""
import re
import sys
from collections import Counter, defaultdict
from cargar import llamadas

raiz = sys.argv[1] if len(sys.argv) > 1 else ".."
PALABRAS = {
    "apagón": r"\bapag[oó]n(es)?\b",
    "apagar/apagad*": r"\bapag(a|ó|ad[oa]s?|ada)\b",
    "blackout": r"\bblackout\b",
    "luna llena": r"\bluna llena\b",
    "luna (cualquiera)": r"\bluna\b",
    "vela(s)": r"\bvelas?\b",
    "linterna": r"\blinternas?\b",
    "relé": r"\brel[eé]s?\b",
    "cascada": r"\bcascadas?\b",
    "farol": r"\bfarol(es)?\b",
    "faro": r"\bfaros?\b",
    "se corta/cortó la luz": r"\bse cort[aó] la luz\b",
    "sin luz": r"\bsin luz\b",
    "a oscuras": r"\ba oscuras\b",
    "oscuridad": r"\boscuridad\b",
}
cuenta = Counter(); por_familia = defaultdict(Counter); ejemplos = defaultdict(list)
n = 0; palabras_total = 0
for ll in llamadas(raiz):
    n += 1
    t = ll["respuesta"]
    palabras_total += len(t.split())
    fam = ll["modelo"].split("/")[0] if "/" in ll["modelo"] else ll["modelo"].split("-")[0]
    for nombre, pat in PALABRAS.items():
        for m in re.finditer(pat, t, re.I):
            cuenta[nombre] += 1
            por_familia[nombre][fam] += 1
            if len(ejemplos[nombre]) < 4:
                a, b = max(0, m.start() - 70), min(len(t), m.end() + 70)
                ejemplos[nombre].append((ll["modelo"], ll["carpeta"], " ".join(t[a:b].split())))
print(f"{n} respuestas en castellano, {palabras_total} palabras")
for nombre in PALABRAS:
    print(f"\n{nombre}: {cuenta[nombre]}  ({dict(por_familia[nombre].most_common(6))})")
    for mod, carp, ej in ejemplos[nombre]:
        print(f"   [{mod} / {carp}] …{ej}…")
