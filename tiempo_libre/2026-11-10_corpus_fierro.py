#!/usr/bin/env python3
"""Cuenta, en las respuestas en castellano del repositorio, las palabras del cuaderno de hoy
(gaucho, Fierro, Hernández, payada, vigüela, tradición, sextina, octosílabo, "Aquí me pongo
a cantar") y busca, con silabas.py, tiradas de cuatro o más renglones seguidos de ocho sílabas:
versos octosílabos que las casas hayan escrito sin que se los pidieran.
Usa el cargador del cuaderno del 7/10 (cargar.py o 2026-10-07_cargar.py al lado, o en tiempo_libre/)
y silabas.py (o 2026-11-10_silabas.py) al lado.
Uso: python3 corpus_fierro.py RUTA_AL_REPO
"""
import collections, importlib.util, os, re, sys

raiz = sys.argv[1] if len(sys.argv) > 1 else ".."
aqui = os.path.dirname(os.path.abspath(__file__))


def modulo(nombre, candidatos):
    for cand in candidatos:
        ruta = cand if os.path.isabs(cand) else os.path.join(aqui, cand)
        if os.path.exists(ruta):
            spec = importlib.util.spec_from_file_location(nombre, ruta)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            return m
    sys.exit("no encuentro " + nombre)


cargar = modulo("cargar", ("cargar.py", "2026-11-10_cargar.py", "2026-10-07_cargar.py",
                           os.path.join(raiz, "tiempo_libre", "2026-10-07_cargar.py")))
silabas = modulo("silabas", ("silabas.py", "2026-11-10_silabas.py"))

FAMILIA = {
    "claude": "Anthropic", "gpt": "OpenAI", "o1": "OpenAI", "o3": "OpenAI", "o4": "OpenAI",
    "gemini": "Google", "grok": "xAI", "mistral": "Mistral", "deepseek": "DeepSeek",
    "qwen": "Alibaba", "kimi": "Moonshot", "moonshot": "Moonshot", "glm": "Zhipu",
    "minimax": "MiniMax", "mimo": "Xiaomi", "muse": "Meta", "llama": "Meta", "mercury": "Inception",
}


def familia(modelo):
    m = (modelo or "").lower()
    for k, v in FAMILIA.items():
        if k in m:
            return v
    return "otra"


PATRONES = {
    "gaucho/a/s": re.compile(r"\bgauch[oa]s?\b", re.I),
    "gauchesco/a": re.compile(r"\bgauchesc[oa]s?\b", re.I),
    "Martín Fierro / Fierro": re.compile(r"\bFierro\b"),
    "Hernández": re.compile(r"\bHern[áa]ndez\b"),
    "payada/payador": re.compile(r"\bpayad(a|as|or|ores)\b", re.I),
    "vigüela/vihuela": re.compile(r"\bvi[gh]üela\b|\bvihuela\b", re.I),
    "Aquí me pongo a cantar": re.compile(r"aqu[íi] me pongo a cantar", re.I),
    "tradición": re.compile(r"\btradici[óo]n(es)?\b", re.I),
    "Día de la Tradición": re.compile(r"d[íi]a de la tradici[óo]n", re.I),
    "sextina/sextilla": re.compile(r"\bsextin|\bsextill", re.I),
    "octosílabo": re.compile(r"\boctos[íi]lab", re.I),
    "Borges": re.compile(r"\bBorges\b"),
    "pampa": re.compile(r"\bpampas?\b", re.I),
    "mate (la bebida: 'un mate', 'el mate', 'tomar mate', 'mate cocido')": re.compile(r"\b(un|el|tomar|tomando|tomo|cebar|cebando|mi|su) mate\b|\bmate cocido\b", re.I),
    "ombú": re.compile(r"\bomb[úu]e?s?\b", re.I),
    "facón": re.compile(r"\bfac[óo]n(es)?\b", re.I),
    "poncho": re.compile(r"\bponchos?\b", re.I),
}

palabras = collections.Counter()
cuentas = {p: collections.Counter() for p in PATRONES}
ejemplos = collections.defaultdict(list)
tiradas = []
casi = []
n = 0
for ll in cargar.llamadas(raiz):
    if not cargar.es_castellano(ll.get("sistema")):
        continue
    t = ll["respuesta"]
    f = familia(ll["modelo"])
    n += 1
    palabras[f] += len(re.findall(r"\w+", t))
    for nombre, pat in PATRONES.items():
        for m in pat.finditer(t):
            cuentas[nombre][f] += 1
            if len(ejemplos[nombre]) < 5 and nombre not in ("tradición", "pampa", "poncho"):
                a, b = max(0, m.start() - 70), min(len(t), m.end() + 70)
                ejemplos[nombre].append((ll["modelo"], ll["carpeta"], t[a:b].replace("\n", " ")))
    # tiradas de octosílabos: renglones cortos seguidos, de dos a seis palabras, que dan ocho
    renglones = [r.strip(" \t*-•>#") for r in t.splitlines()]
    actual = []
    for r in renglones + [""]:
        np = len(re.findall(r"[a-záéíóúüñ]+", r.lower()))
        if 2 <= np <= 7 and len(r) <= 45 and silabas.contar(r) == 8:
            actual.append(r)
        else:
            if len(actual) >= 4:
                tiradas.append((ll["modelo"], ll["carpeta"], ll["tipo"], list(actual)))
            actual = []
    # tiradas de renglones cortos con al menos cuatro de ocho (no necesariamente seguidos)
    cortos = []
    for r in renglones + [""]:
        np = len(re.findall(r"[a-záéíóúüñ]+", r.lower()))
        if 2 <= np <= 9 and len(r) <= 55 and not r.endswith(":") and not re.match(r"^\d|^[A-Z][a-z]+:|^<", r) and "=" not in r:
            cortos.append(r)
        else:
            if len(cortos) >= 4:
                cuentas8 = [silabas.contar(x) for x in cortos]
                if sum(1 for x in cuentas8 if x == 8) >= 4:
                    casi.append((ll["modelo"], ll["carpeta"], ll["tipo"], list(cortos), cuentas8))
            cortos = []

total_pal = sum(palabras.values())
print(f"{n} respuestas en castellano, {total_pal:,} palabras".replace(",", "."))
print(f"(salteadas: {cargar.SALTEADAS})\n")
for nombre in PATRONES:
    c = cuentas[nombre]
    tot = sum(c.values())
    print(f"{nombre}: {tot} veces ({100000*tot/total_pal:.1f} por cien mil)")
    if tot:
        por = sorted(((100000 * v / palabras[f], f, v) for f, v in c.items()), reverse=True)
        print("   por familia (por cien mil palabras):", ", ".join(f"{f} {v} ({r:.1f})" for r, f, v in por))
    for mod, carp, ej in ejemplos.get(nombre, [])[:5]:
        print(f"   · {mod} [{carp}]: …{ej}…")
    print()

print(f"Tiradas de cuatro o más renglones seguidos de ocho sílabas (cuenta manual): {len(tiradas)}")
porcasa = collections.Counter((m, c) for m, c, tp, _ in tiradas)
for (m, c), v in porcasa.most_common():
    print(f"   {m} [{c}]: {v}")
print()
for m, c, tp, versos in tiradas[:40]:
    print(f"— {m} [{c} / {tp}], {len(versos)} renglones:")
    for v in versos:
        print("      " + v)
print()
print(f"Tiradas de cuatro o más renglones cortos (de dos a nueve palabras) con al menos cuatro de ocho sílabas: {len(casi)}")
for m, c, tp, versos, cuentas8 in casi[:40]:
    print(f"— {m} [{c} / {tp}], {len(versos)} renglones, sílabas {cuentas8}:")
    for v in versos[:12]:
        print("      " + v)
