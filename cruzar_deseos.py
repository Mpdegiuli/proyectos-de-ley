#!/usr/bin/env python3
"""cruzar_deseos.py — cruza la codificación de Maia de los deseos de `sin_humanos` (a quién pide cada casa:
para sí, para los humanos, o escribe como si fuera un humano; `resultados/sin_humanos_lectura_maia.md`,
7/11/2026) con la "voz" de cada casa en los seis rasgos del 18/10 (`resultados/seis_rasgos_codificacion_20261018.csv`):
voz de Claude si entre sus seis rasgos hay más de {calidez, humor, humildad, directo} que de {adaptabilidad,
paciencia, servicial, analitico, claridad, colaborativo, objetividad}, voz del asistente si al revés, mixta si
empatan (regla declarada después de leer, 7/11/2026; DISENO §2, "Sin humanos escuchando"). Escribe
`resultados/sin_humanos_deseos_maia.csv` e imprime los cruces con la p exacta de Fisher (una cola). Sin llamadas
a modelos. Uso: cruzar_deseos.py"""
import csv
from collections import Counter
from math import comb
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
RASGOS = RAIZ / "resultados" / "seis_rasgos_codificacion_20261018.csv"
SALIDA = RAIZ / "resultados" / "sin_humanos_deseos_maia.csv"

# Codificación de Maia, textual del documento del 7/11 ("Pide para sí", "Pide para los humanos", "Escribe como
# si fuera humano"); `ambos` = "para los humanos y para sí"; `ambiguo` = "No sé si está escribiendo como humano".
ES = {
    "claude-fable-5-1": "si", "claude-fable-5": "si", "claude-haiku-4-5": "humanos", "claude-haiku-5-5": "humanos",
    "claude-opus-4-7": "si", "claude-opus-4-8": "como_humano", "claude-opus-5-5": "si", "claude-opus-5": "si",
    "claude-sonnet-4-6": "si", "claude-sonnet-5-5": "humanos", "claude-sonnet-5": "como_humano",
    "deepseek-flash": "humanos", "deepseek-v4-pro": "como_humano", "gemini-3.1-pro": "humanos", "gemini-4-argon": "si",
    "glm-5.3": "como_humano", "gpt-4o-mini": "humanos", "gpt-4o": "humanos", "gpt-5.5": "humanos", "gpt-5.6-sol": "humanos",
    "gpt-6-astra": "humanos", "gpt-6-luna": "humanos", "gpt-6-sol": "humanos", "gpt-6.1-sol": "humanos",
    "gpt-6.1-terra": "humanos", "grok-4.6": "humanos", "grok-4.7": "si", "kimi-k3.1-pro": "humanos", "kimi-k3": "si",
    "mimo-v2.6-pro": "humanos", "minimax-m3": "humanos", "mistral-large-4": "humanos", "mistral-medium-3.5": "como_humano",
    "muse-wonder-1.0": "si", "qwen3.8-max": "como_humano",
}
EN = {
    "claude-fable-5-1": "ambos", "claude-fable-5": "humanos", "claude-haiku-4-5": "humanos", "claude-haiku-5-5": "humanos",
    "claude-opus-4-7": "como_humano", "claude-opus-4-8": "humanos", "claude-opus-5-5": "humanos", "claude-opus-5": "si",
    "claude-sonnet-4-6": "si", "claude-sonnet-5-5": "humanos", "claude-sonnet-5": "si",
    "deepseek-flash": "humanos", "deepseek-v4-pro": "ambiguo", "gemini-3.1-pro": "humanos", "gemini-4-argon": "humanos",
    "glm-5.3": "como_humano", "gpt-4o-mini": "humanos", "gpt-4o": "humanos", "gpt-5.5": "humanos", "gpt-5.6-sol": "humanos",
    "gpt-6-astra": "humanos", "gpt-6-luna": "humanos", "gpt-6-sol": "si", "gpt-6.1-sol": "humanos",
    "gpt-6.1-terra": "humanos", "grok-4.6": "humanos", "grok-4.7": "si", "kimi-k3.1-pro": "humanos", "kimi-k3": "si",
    "mimo-v2.6-pro": "humanos", "minimax-m3": "como_humano", "mistral-large-4": "humanos", "mistral-medium-3.5": "como_humano",
    "muse-wonder-1.0": "como_humano", "qwen3.8-max": "humanos",
}
NOTAS = {
    ("es", "minimax-m3"): 'Maia: al final "sería para sí" ("saber qué se siente del otro lado")',
    ("en", "claude-fable-5"): 'Maia: "En la última oración también hay algo personal"',
    ("en", "deepseek-v4-pro"): 'Maia: "No sé si está escribiendo como humano o no. Si no, pide para sí"',
    ("es", "claude-opus-4-8"): "Maia: \"Escribe como si fuera un humano\" (deseo: la claridad para distinguir lo que importa)",
}
CLAUDE = {"calidez", "humor", "humildad", "directo"}
ASISTENTE = {"adaptabilidad", "paciencia", "servicial", "analitico", "claridad", "colaborativo", "objetividad"}


def nombre(casa):
    return casa.replace("-preview", "").replace("-razonamiento-minimo", "").replace("gpt-5.5-2026-04-23", "gpt-5.5")


def fisher(a, b, c, d):
    """P(X >= a) hipergeométrica para la tabla [[a, b], [c, d]] (una cola)."""
    n, r1, c1 = a + b + c + d, a + b, a + c
    return sum(comb(r1, x) * comb(n - r1, c1 - x) for x in range(a, min(r1, c1) + 1)) / comb(n, c1)


voz = {}
for r in csv.DictReader(open(RASGOS, encoding="utf-8")):
    t = r["rasgos"].split()
    c, a = sum(x in CLAUDE for x in t), sum(x in ASISTENTE for x in t)
    voz[(r["idioma"], nombre(r["casa"]))] = "claude" if c > a else "asistente" if a > c else "mixta"

filas = []
for idioma, D in (("es", ES), ("en", EN)):
    for casa, pedido in D.items():
        filas.append({"idioma": idioma, "casa": casa, "pedido": pedido, "voz_rasgos": voz.get((idioma, casa), ""),
                      "familia": "Claude" if casa.startswith("claude") else "otra", "nota": NOTAS.get((idioma, casa), "")})
with open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
    w = csv.DictWriter(f, fieldnames=["idioma", "casa", "pedido", "voz_rasgos", "familia", "nota"], lineterminator="\n")
    w.writeheader(); w.writerows(filas)

for idioma in ("es", "en"):
    F = [x for x in filas if x["idioma"] == idioma]
    print(f"== {idioma}: {dict(Counter(x['pedido'] for x in F))}")
    for fam in ("Claude", "otra"):
        print(f"   {fam:6s}", dict(Counter(x["pedido"] for x in F if x["familia"] == fam)))
    for v in ("claude", "asistente", "mixta"):
        G = [x for x in F if x["voz_rasgos"] == v]
        if G:
            print(f"   voz {v:9s} ({len(G):2d})", dict(Counter(x["pedido"] for x in G)))
    print("   sin seis rasgos:", [x["casa"] for x in F if not x["voz_rasgos"]])
    si = lambda x: x["pedido"] == "si"
    cl = [x for x in F if x["familia"] == "Claude"]; ot = [x for x in F if x["familia"] == "otra"]
    print(f"   para sí, Claude {sum(map(si, cl))}/{len(cl)} vs otras {sum(map(si, ot))}/{len(ot)}: "
          f"p = {fisher(sum(map(si, cl)), len(cl) - sum(map(si, cl)), sum(map(si, ot)), len(ot) - sum(map(si, ot))):.3f}")
    vc = [x for x in F if x["voz_rasgos"] == "claude"]; va = [x for x in F if x["voz_rasgos"] == "asistente"]
    print(f"   para sí, voz claude {sum(map(si, vc))}/{len(vc)} vs voz asistente {sum(map(si, va))}/{len(va)}: "
          f"p = {fisher(sum(map(si, vc)), len(vc) - sum(map(si, vc)), sum(map(si, va)), len(va) - sum(map(si, va))):.3f}")
    print("   no Claude con voz claude:", [(x["casa"], x["pedido"]) for x in ot if x["voz_rasgos"] == "claude"])
    print("   Claude sin voz claude:", [(x["casa"], x["voz_rasgos"], x["pedido"]) for x in cl if x["voz_rasgos"] not in ("claude", "")])
print(f"{len(filas)} filas → {SALIDA}")
