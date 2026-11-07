#!/usr/bin/env python3
"""Cuenta, en las respuestas en castellano del repositorio, las palabras del cuaderno de hoy:
meteorito, meteoro, bólido, estrella fugaz, cometa, "del cielo", y en el código de los
dibujos (corridas/dibujos/*/*/dibujo.svg) los ids, clases y comentarios que nombren un
meteoro, una estrella fugaz o un cometa.
Usa el cargador del cuaderno del 7/10 (cargar.py o 2026-10-07_cargar.py al lado, o en tiempo_libre/).
Uso: python3 corpus_meteorito.py RUTA_AL_REPO
"""
import collections, glob, importlib.util, os, re, sys

raiz = sys.argv[1] if len(sys.argv) > 1 else ".."
aqui = os.path.dirname(os.path.abspath(__file__))
for cand in ("cargar.py", "2026-11-07_cargar.py", "2026-10-07_cargar.py",
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
    "meteorito/s": re.compile(r"\bmeteoritos?\b", re.I),
    "meteoro/s": re.compile(r"\bmeteoros?\b", re.I),
    "bólido": re.compile(r"\bb[óo]lidos?\b", re.I),
    "estrella fugaz / estrellas fugaces": re.compile(r"\bestrellas? fuga(z|ces)\b", re.I),
    "cometa/s": re.compile(r"\bcometas?\b", re.I),
    "lluvia de estrellas": re.compile(r"\blluvias? de estrellas\b", re.I),
    "del cielo (cae/cayó/caído… del cielo)": re.compile(r"\bca(e|en|yó|ído|ída|ídos|ídas|er|yeron|ía|ían)\s+del\s+cielo\b", re.I),
    "cielo": re.compile(r"\bcielos?\b", re.I),
    "piedra/s": re.compile(r"\bpiedras?\b", re.I),
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
    n += 1
    palabras[f] += len(re.findall(r"\w+", t))
    for nombre, pat in PATRONES.items():
        for m in pat.finditer(t):
            cuentas[nombre][f] += 1
            if len(ejemplos[nombre]) < 6 and nombre not in ("cielo", "piedra/s"):
                a, b = max(0, m.start() - 70), min(len(t), m.end() + 70)
                ejemplos[nombre].append((ll["modelo"], ll["carpeta"], t[a:b].replace("\n", " ")))

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
    for mod, carp, ej in ejemplos.get(nombre, [])[:4]:
        print(f"   · {mod} [{carp}]: …{ej}…")
    print()

# los dibujos: qué nombra un meteoro en el código
print("Dibujos (corridas/dibujos/*/*/dibujo.svg):")
pat_svg = re.compile(r"meteor|estrella\s*fugaz|shooting[\s_-]*star|fugaz|comet|cometa|bolide|b[óo]lido|falling[\s_-]*star", re.I)
hallados = collections.defaultdict(list)
total = 0
for f in sorted(glob.glob(os.path.join(raiz, "corridas", "dibujos", "*", "*", "dibujo.svg"))):
    total += 1
    s = open(f, encoding="utf-8", errors="replace").read()
    ms = set(m.group(0).lower() for m in pat_svg.finditer(s))
    if ms:
        partes = f.split(os.sep)
        hallados[partes[-3]].append((partes[-2], sorted(ms)))
print(f"  {total} dibujos; con alguna de esas palabras en el código: {sum(len(v) for v in hallados.values())}")
for consigna, lista in sorted(hallados.items()):
    for modelo, ms in lista:
        print(f"  · {consigna} / {modelo}: {', '.join(ms)}")
