#!/usr/bin/env python3
"""¿Cuál era la palabra más probable para el hueco de Res Gestae 34.3?

Cuenta, en un corpus de prosa latina, cuántas veces aparecen los ablativos
"dignitate" y "auctoritate" en la misma oración que un verbo de aventajar
(praestare, antecellere, excellere, antecedere, anteire, antestare/antistare,
superare), y cuántas veces en total.

Corpus: la copia en texto plano de The Latin Library que mantiene el proyecto CLTK
    git clone --depth 1 https://github.com/cltk/lat_text_latin_library.git
Uso: python3 corpus.py RUTA_AL_CLON

Es una cuenta de superficie: no lematiza, no distingue ablativo de comparación de
ablativo de causa, y "praest-" incluye praesto en el sentido de "cumplir". Por eso
el script imprime también todas las oraciones con "praest-", para leerlas.
"""
import re, sys, os, glob, collections

RAIZ = sys.argv[1] if len(sys.argv) > 1 else "../lat_text_latin_library"

# autores de prosa, de Cicerón a Suetonio (más o menos el latín que Mommsen tenía de modelo)
AUTORES = {
    "Cicerón": ["cicero/*.txt"],
    "César": ["caesar/*.txt"],
    "Salustio": ["sall*.txt", "sallust/*.txt"],
    "Nepote": ["nepos/*.txt"],
    "Livio": ["livy/*.txt"],
    "Veleyo": ["vell*.txt"],
    "Valerio Máximo": ["valmax*.txt"],
    "Séneca": ["sen/*.txt", "seneca*.txt"],
    "Quintiliano": ["quintilian/*.txt"],
    "Plinio el Joven": ["pliny.ep*.txt", "pliny.panegyricus.txt"],
    "Tácito": ["tacitus/*.txt"],
    "Suetonio": ["suetonius/*.txt"],
}
VERBOS = {
    "praestare":   r"\bpraest(o|as|at|amus|atis|ant|a[bv]|et|es|em|ent|are|ar[ei]|it|iti|iterunt|itit|iteri|itiss|ans|ant[ei])\w*",
    "antecellere": r"\bantecell\w*",
    "excellere":   r"\bexcell\w*",
    "antecedere":  r"\bantece(d|ss)\w*",
    "anteire":     r"\bante(i[brst]|e[ou]|ib|iss|ier)\w*",
    "antestare":   r"\bant[ei]st(a|e|i)\w*",
    "superare":    r"\bsuper(o|a[bsntv]|a$|e[mnst]|av|ar[ei])\w*",
}
PAL = ["dignitate", "auctoritate"]

def oraciones(texto):
    texto = re.sub(r"\s+", " ", texto)
    return re.split(r"(?<=[.;:?!])\s+", texto)

def norm(s):
    return s.lower().replace("j", "i").replace("v", "u")

tot = collections.Counter(); con = collections.Counter(); porverbo = collections.Counter()
porautor = collections.defaultdict(collections.Counter)
palabras = 0; ejemplos = []
# el texto se normaliza (v → u, j → i), así que los patrones también
VERBOSN = {k: re.compile(v.replace("v", "u")) for k, v in VERBOS.items()}
for autor, patrones in AUTORES.items():
    archivos = sorted({f for p in patrones for f in glob.glob(os.path.join(RAIZ, p))})
    for f in archivos:
        t = open(f, encoding="utf-8", errors="replace").read()
        for o in oraciones(t):
            on = norm(o)
            palabras += len(on.split())
            for p in PAL:
                k = len(re.findall(r"\b" + p + r"\b", on))
                if not k: continue
                tot[p] += k; porautor[autor][p + "_tot"] += k
                hits = [v for v, rx in VERBOSN.items() if rx.search(on)]
                if hits:
                    con[p] += 1; porautor[autor][p + "_con"] += 1
                    for v in hits: porverbo[(p, v)] += 1
                    if "praestare" in hits:
                        ejemplos.append((p, autor, os.path.basename(f), o.strip()))

print(f"palabras en el corpus: {palabras:,}")
print(f"{'':16}{'total':>8}{'con verbo de aventajar':>26}")
for p in PAL:
    print(f"{p:16}{tot[p]:8}{con[p]:26}")
print("\npor verbo:")
for v in VERBOS:
    print(f"  {v:12} dignitate {porverbo[('dignitate', v)]:3}   auctoritate {porverbo[('auctoritate', v)]:3}")
print("\npor autor (total / con verbo):")
for a in AUTORES:
    c = porautor[a]
    print(f"  {a:16} dignitate {c['dignitate_tot']:4} / {c['dignitate_con']:2}    auctoritate {c['auctoritate_tot']:4} / {c['auctoritate_con']:2}")
print("\noraciones con praest- (para leer):")
for p, a, f, o in ejemplos:
    i = norm(o).find(p)
    print(f"  [{p}] {a}, {f}: …{o[max(0, i-170): i+170]}…")
