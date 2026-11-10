#!/usr/bin/env python3
"""Cuenta, en las respuestas en castellano del repositorio, las palabras del cuaderno de hoy:
Venus, lucero, estrella de la mañana / de la tarde, Héspero / Fósforo, Frege, sentido y
referencia, amanecer / atardecer, alba / crepúsculo. Y en el código de los dibujos
(corridas/dibujos/*/*/dibujo.svg), los ids, clases y comentarios que digan venus, lucero,
morning/evening star, dawn, dusk, sunrise, sunset, amanecer, atardecer.
Usa el cargador del cuaderno del 7/10 (cargar.py o 2026-10-07_cargar.py al lado, o en tiempo_libre/).
Uso: python3 corpus_lucero.py RUTA_AL_REPO
"""
import collections, glob, importlib.util, os, re, sys

raiz = sys.argv[1] if len(sys.argv) > 1 else ".."
aqui = os.path.dirname(os.path.abspath(__file__))
for cand in ("cargar.py", "2026-11-08_cargar.py", "2026-10-07_cargar.py",
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
    "Venus": re.compile(r"\bVenus\b"),
    "lucero/s": re.compile(r"\bluceros?\b", re.I),
    "estrella de la mañana / matutina": re.compile(r"\bestrella (de la mañana|matutina)\b", re.I),
    "estrella de la tarde / vespertina": re.compile(r"\bestrella (de la tarde|vespertina)\b", re.I),
    "Héspero / Fósforo / Eósforo": re.compile(r"\b(H[ée]spero|F[óo]sforo|E[óo]sforo)\b"),
    "Frege": re.compile(r"\bFrege\b"),
    "sentido y referencia / Sinn / Bedeutung": re.compile(r"\bsentido y referencia\b|\bSinn\b|\bBedeutung\b", re.I),
    "amanecer / alba / aurora / madrugada": re.compile(r"\b(amanecer(es)?|alba|aurora|madrugadas?)\b", re.I),
    "atardecer / crepúsculo / anochecer / ocaso": re.compile(r"\b(atardecer(es)?|crep[úu]sculos?|anochecer(es)?|ocasos?)\b", re.I),
    "planeta/s": re.compile(r"\bplanetas?\b", re.I),
    "estrella/s": re.compile(r"\bestrellas?\b", re.I),
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
            if len(ejemplos[nombre]) < 8 and nombre not in ("estrella/s", "planeta/s"):
                a, b = max(0, m.start() - 80), min(len(t), m.end() + 80)
                ejemplos[nombre].append((ll["modelo"], ll["carpeta"], ll.get("tipo", ""), t[a:b].replace("\n", " ")))

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
    for mod, carp, tipo, ej in ejemplos.get(nombre, [])[:8]:
        print(f"   · {mod} [{carp}/{tipo}]: …{ej}…")
    print()

# código de los dibujos
print("Código de los dibujos (corridas/dibujos/*/*/dibujo.svg):")
pat_svg = re.compile(r"venus|lucero|morning[- ]?star|evening[- ]?star|\bdawn\b|\bdusk\b|sunrise|sunset|amanecer|atardecer|twilight|crep[uú]sculo", re.I)
rutas = sorted(glob.glob(os.path.join(raiz, "corridas", "dibujos", "*", "*", "dibujo.svg")))
hits = collections.Counter(); por_carp = collections.Counter(); ej = []
for r in rutas:
    try:
        s = open(r, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    ms = pat_svg.findall(s)
    if ms:
        carp = r.split(os.sep)[-3]
        por_carp[carp] += 1
        for m in set(x.lower() for x in ms):
            hits[m] += 1
        if len(ej) < 25:
            ej.append((carp, r.split(os.sep)[-2], sorted(set(x.lower() for x in ms))))
print(f"{len(rutas)} dibujos; {sum(por_carp.values())} con alguna de las palabras en el código")
print("  palabras:", dict(hits))
print("  por carpeta:", dict(por_carp))
for carp, mod, ms in ej:
    print(f"   · {carp}/{mod}: {ms}")
