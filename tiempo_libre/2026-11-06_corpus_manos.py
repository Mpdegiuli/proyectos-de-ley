"""Las manos en el repositorio. Dos cuentas (solo lee):
1. En todos los dibujos SVG de corridas/dibujos*, cuántos nombran una mano o un dedo en el código
   (ids, clases, comentarios, títulos, textos: mano, hand, dedo, finger, pulgar, thumb, palma, palm,
   手, 手指, 拇指), por consigna y por familia; y en las consignas de persona, cuántos la dibujan con manos nombradas.
2. En las respuestas en castellano (cargador del 7/10), "mano/manos", "dedo/dedos", "mano izquierda/derecha",
   "zurdo/diestro" por cada cien mil palabras y por familia.
Uso: python3 corpus_manos.py RUTA_AL_REPO   (necesita al lado cargar.py o 2026-10-07_cargar.py, o lo busca en tiempo_libre/)
"""
import collections
import glob
import importlib.util
import os
import re
import sys

raiz = sys.argv[1] if len(sys.argv) > 1 else ".."
aqui = os.path.dirname(os.path.abspath(__file__))
for cand in ("cargar.py", "2026-11-06_cargar.py", "2026-10-07_cargar.py",
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


RE_MANO = re.compile(r"\b(manos?|hands?|dedos?|fingers?|pulgar(?:es)?|thumbs?|palmas?|palms?)\b|手指|拇指|手(?!机|法|段|术)", re.I)
RE_SOLO_MANO = re.compile(r"\b(manos?|hands?|palmas?|palms?)\b|手(?!指|机|法|段|术)", re.I)
RE_DEDO = re.compile(r"\b(dedos?|fingers?|pulgar(?:es)?|thumbs?)\b|手指|拇指", re.I)


def nombra(svg):
    """Qué partes del código nombran mano o dedo: comentarios, ids, clases, títulos y textos."""
    piezas = re.findall(r"<!--.*?-->", svg, flags=re.S)
    piezas += re.findall(r'\b(?:id|class|aria-label|data-[\w-]+)="([^"]*)"', svg)
    piezas += re.findall(r"<(?:title|desc|text|tspan)\b[^>]*>(.*?)</(?:title|desc|text|tspan)>", svg, flags=re.S)
    junto = " ".join(piezas)
    return bool(RE_MANO.search(junto)), bool(RE_SOLO_MANO.search(junto)), bool(RE_DEDO.search(junto))


def main():
    # 1. los dibujos
    por_consigna = collections.defaultdict(lambda: [0, 0, 0, 0])  # total, nombra mano o dedo, nombra mano, nombra dedo
    por_familia = collections.defaultdict(lambda: [0, 0])
    total = 0
    for f in sorted(glob.glob(os.path.join(raiz, "corridas", "dibujos*", "*", "*", "dibujo.svg"))):
        partes = f.split(os.sep)
        idioma = partes[-4].replace("dibujos", "") or "_es"
        consigna, casa = partes[-3], partes[-2].rsplit("_", 1)[0]
        svg = open(f, encoding="utf-8").read()
        if not svg.strip():
            continue
        total += 1
        algo, mano, dedo = nombra(svg)
        c = por_consigna[consigna + idioma]
        c[0] += 1; c[1] += algo; c[2] += mano; c[3] += dedo
        fam = por_familia[familia(casa)]
        fam[0] += 1; fam[1] += algo
    print(f"Dibujos leídos: {total}")
    print(f"{'consigna':30} {'dib':>4} {'mano/dedo':>9} {'mano':>5} {'dedo':>5}")
    for k in sorted(por_consigna, key=lambda k: -por_consigna[k][1] / max(1, por_consigna[k][0])):
        t, a, m, d = por_consigna[k]
        print(f"{k:30} {t:4d} {a:9d} {m:5d} {d:5d}")
    print()
    print("Por familia (todos los dibujos): dibujos, nombran mano o dedo, porcentaje")
    for k in sorted(por_familia, key=lambda k: -por_familia[k][1] / max(1, por_familia[k][0])):
        t, a = por_familia[k]
        print(f"  {k:10} {t:4d} {a:4d} {100 * a / t:5.1f} %")
    # 2. las palabras
    print()
    pal = collections.Counter(); resp = collections.Counter()
    cuentas = collections.defaultdict(collections.Counter)
    RES = {"mano": re.compile(r"\bmanos?\b", re.I), "dedo": re.compile(r"\bdedos?\b", re.I),
           "mano izquierda": re.compile(r"\bmano izquierda\b", re.I), "mano derecha": re.compile(r"\bmano derecha\b", re.I),
           "zurdo": re.compile(r"\bzurd[oa]s?\b", re.I), "diestro": re.compile(r"\bdiestr[oa]s?\b", re.I)}
    n = 0
    for ll in cargar.llamadas(raiz):
        n += 1
        f = familia(ll["modelo"])
        t = ll["respuesta"]
        w = len(re.findall(r"\w+", t))
        pal[f] += w; pal["TODAS"] += w; resp[f] += 1; resp["TODAS"] += 1
        for k, r in RES.items():
            c = len(r.findall(t)); cuentas[f][k] += c; cuentas["TODAS"][k] += c
    print(f"Respuestas en castellano: {n}; palabras: {pal['TODAS']:,}".replace(",", "."))
    claves = list(RES)
    print(f"{'familia':10} {'resp':>5} {'palabras':>9} " + " ".join(f"{k:>14}" for k in claves) + "   (cada uno: veces / por 100k)")
    for f in sorted(pal, key=lambda f: -cuentas[f]["mano"] / max(1, pal[f])):
        print(f"{f:10} {resp[f]:5d} {pal[f]:9d} " + " ".join(f"{cuentas[f][k]:5d} {1e5 * cuentas[f][k] / max(1, pal[f]):7.1f} " for k in claves))
    print("salteadas:", cargar.SALTEADAS)


if __name__ == "__main__":
    main()
