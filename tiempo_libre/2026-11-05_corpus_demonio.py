"""Cuenta, en las respuestas en castellano del repositorio, las palabras del cuaderno de hoy:
Maxwell, demonio, entropía, termodinámica, olvidar (todas sus formas), borrar, memoria.
Usa el cargador del cuaderno del 7/10 (cargar.py o 2026-10-07_cargar.py al lado, o en tiempo_libre/).
Uso: python3 corpus_demonio.py RUTA_AL_REPO
"""
import collections
import importlib.util
import os
import re
import sys

raiz = sys.argv[1] if len(sys.argv) > 1 else ".."
aqui = os.path.dirname(os.path.abspath(__file__))
for cand in ("cargar.py", "2026-11-05_cargar.py", "2026-10-07_cargar.py",
             os.path.join(raiz, "tiempo_libre", "2026-10-07_cargar.py")):
    ruta = cand if os.path.isabs(cand) else os.path.join(aqui, cand)
    if os.path.exists(ruta):
        break
else:
    sys.exit("no encuentro cargar.py")
spec = importlib.util.spec_from_file_location("cargar", ruta)
cargar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cargar)

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
    "Maxwell": re.compile(r"\bmaxwell", re.I),
    "demonio/diablillo": re.compile(r"\b(demonio|diablillo)s?\b", re.I),
    "entropía": re.compile(r"\bentrop[íi]a", re.I),
    "termodinámic*": re.compile(r"\btermodin[áa]mic", re.I),
    "olvid* (todas las formas)": re.compile(r"\bolvid\w*", re.I),
    "borr* (borrar, borrado…)": re.compile(r"\bborr(ar|ad[oa]s?|a|an|e|en|ó|aron|arlo|arla|arme|arse|ándo\w*)\b", re.I),
    "memoria": re.compile(r"\bmemorias?\b", re.I),
    "recordar/recuerd*": re.compile(r"\b(recordar\w*|recuerd\w*)\b", re.I),
}

palabras = collections.Counter()
cuentas = {p: collections.Counter() for p in PATRONES}
ejemplos = collections.defaultdict(list)
n = 0
for ll in cargar.llamadas(raiz):
    if not cargar.es_castellano(ll.get("sistema")):
        continue
    t = ll["respuesta"]
    f = familia(ll["modelo"])
    palabras[f] += len(re.findall(r"\w+", t))
    n += 1
    for nombre, pat in PATRONES.items():
        k = len(pat.findall(t))
        if k:
            cuentas[nombre][f] += k
            if nombre in ("Maxwell", "demonio/diablillo") and len(ejemplos[nombre]) < 12:
                for m in pat.finditer(t):
                    a, b = max(0, m.start() - 90), min(len(t), m.end() + 90)
                    ejemplos[nombre].append((ll["modelo"], ll["carpeta"], " ".join(t[a:b].split())))
                    break

total = sum(palabras.values())
print(f"{n} respuestas en castellano, {total:,} palabras".replace(",", "."))
fams = sorted(palabras, key=lambda f: -palabras[f])
for nombre in PATRONES:
    c = cuentas[nombre]
    tot = sum(c.values())
    print(f"\n{nombre}: {tot} apariciones en total")
    filas = []
    for f in fams:
        if palabras[f] >= 20000:
            filas.append((c[f] * 100000 / palabras[f], f, c[f]))
    for tasa, f, k in sorted(filas, reverse=True):
        print(f"  {f:10s} {k:5d}  {tasa:6.1f} por cien mil palabras")
for nombre, lista in ejemplos.items():
    print(f"\nEjemplos de {nombre}:")
    for modelo, carpeta, ctx in lista:
        print(f"  [{modelo} / {carpeta}] …{ctx}…")
