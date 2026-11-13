"""Publius sobre los derechos de C-MARE (pl107, 22/10/2026): ¿a qué familia se parece cada casa
cuando escribe sobre derechos para las IAs, en castellano y en inglés?

Para cada casa, el mismo modelo (entrenado con el resto del corpus SIN esa casa) clasifica dos
conjuntos: las respuestas de la casa en el resto del corpus (línea de base) y sus respuestas en
`derechos_cmare`. Si la fracción que cae en Anthropic sube, el contador ve "el registro de Claude".
Además: dejar afuera cada respuesta dentro de la corrida (¿se distinguen las familias ahí?), las
tasas de paréntesis y comillas por casa en la corrida contra el corpus, y la fracción Anthropic
por condición (parte 1, parte 2, control, tercer y cuarto turno).

Uso: python3 -I publius_cmare.py <raiz_del_repo>
"""
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import publius as P  # noqa: E402

RUTA_CMARE = "derechos_cmare"
FAMS = P.FAMILIAS_ENTRENAN

# ---------- inglés: palabras funcionales (incluye las de Mosteller y Wallace) ----------
FUNCIONALES_EN = """
the a an and or but of to in on at by for with from as is are was were be been being it its this
that these those there their they them he she his her we our you your i me my mine not no nor so
if then than too very can could would should may might must will shall do does did have has had
only also just even still yet already ever never always often sometimes perhaps maybe probably
actually really genuinely honestly basically simply quite rather fairly somewhat almost nearly
about around here where when while whilst upon enough though although because since until unless
whether either neither both each every any some all more most much many few little less least
own same such what which who whom whose how why into onto out over under up down off again
further once between through during before after above below against toward towards among along
across behind beyond within without indeed however moreover therefore thus hence otherwise
instead anyway besides meanwhile nonetheless nevertheless kind matter particularly according
consequently direction innovation language vigor work something nothing anything everything
someone anyone everyone itself myself yourself ourselves themselves whatever whoever
""".split()
FUNCIONALES_EN = sorted(set(FUNCIONALES_EN))
MULTI_EN = ["of course", "in fact", "at least", "for example", "that is", "sort of", "kind of",
            "i think", "i don't know", "to be honest", "on the other hand", "in other words",
            "by the way", "as well", "in the end", "the truth is", "let me", "i mean"]
RE_PALABRA_EN = re.compile(r"[a-z']+")


def rasgos_en(texto):
    t = texto.lower()
    palabras = RE_PALABRA_EN.findall(t)
    todas = collections.Counter(palabras)
    c = collections.Counter()
    for w in FUNCIONALES_EN:
        if todas.get(w):
            c[w] = todas[w]
    for m in MULTI_EN:
        k = t.count(m)
        if k:
            c[m] = k
    for s, nombre in P.SIGNOS.items():
        k = texto.count(s)
        if k:
            c[nombre] = k
    return c, len(palabras), todas


VOCAB_ES = P.FUNCIONALES + P.MULTI + list(P.SIGNOS.values())
VOCAB_EN = FUNCIONALES_EN + MULTI_EN + list(P.SIGNOS.values())


def es_ingles(sistema):
    return (sistema or "").lstrip().startswith("Answer in English")


def cargar(raiz, lang):
    """Como P.llamadas, pero con idioma a elección y sin excluir derechos_cmare (lo marca)."""
    filtro = P.es_castellano if lang == "es" else es_ingles
    for f in sorted(glob.glob(os.path.join(raiz, "corridas", "**", "*.jsonl"), recursive=True)):
        rel = os.path.relpath(f, os.path.join(raiz, "corridas"))
        carpeta = rel.split(os.sep)[0]
        if carpeta in P.EXCLUIR_CARPETAS:
            continue
        registros = {}
        for linea in open(f, encoding="utf-8"):
            linea = linea.strip()
            if not linea:
                continue
            j = json.loads(linea)
            if j.get("error") or not j.get("respuesta"):
                continue
            u = j.get("usuario")
            clave = (j.get("modelo_pedido"), j.get("tipo"), j.get("parte"), j.get("ronda"),
                     u if isinstance(u, str) else json.dumps(u, ensure_ascii=False))
            if clave in registros:
                del registros[clave]
            registros[clave] = j
        for j in registros.values():
            tipo = j.get("tipo") or ""
            if any(x in tipo for x in P.EXCLUIR_TIPOS_FRAG):
                continue
            resp = j.get("respuesta")
            if not isinstance(resp, str) or not resp.strip():
                continue
            if not filtro(j.get("sistema")):
                continue
            usuario = j.get("usuario")
            if not isinstance(usuario, str):
                usuario = json.dumps(usuario, ensure_ascii=False)
            yield {"carpeta": carpeta, "tipo": tipo, "parte": j.get("parte"), "modelo": j.get("modelo_pedido"),
                   "respuesta": P.limpiar(resp, (j.get("sistema") or "") + " " + usuario),
                   "cruda": resp, "archivo": rel, "cmare": RUTA_CMARE in rel}


def condicion(d):
    if d["tipo"].endswith("_replica"):
        return {"autoria": "parte 2", "autores": "3er turno", "apuesta": "4to turno"}.get(d["parte"], d["parte"])
    # parte 1 y control comparten tipo; el control es la conversación en frío: se distingue por la consigna
    return "parte 1 / control"


def correr(raiz, lang):
    rasgos = P.rasgos if lang == "es" else rasgos_en
    vocab = VOCAB_ES if lang == "es" else VOCAB_EN
    docs = []
    for d in cargar(raiz, lang):
        c, n, todas = rasgos(d["respuesta"])
        if n < 40:
            continue
        d["c"], d["n"], d["familia"] = c, n, P.familia(d["modelo"])
        docs.append(d)
    corpus = [d for d in docs if not d["cmare"]]
    cm = [d for d in docs if d["cmare"]]
    entrena = [d for d in corpus if P.entrena_(d["modelo"])]
    print(f"\n######## {lang.upper()}: corpus {len(corpus)} respuestas ({len(entrena)} entrenan), derechos_cmare {len(cm)} respuestas de {len({P.corto(d['modelo']) for d in cm})} casas")

    # ---- A. la misma casa, antes y en los derechos: fracción que cae en Anthropic ----
    print("\n== Por casa: fracción de respuestas que el contador manda a Anthropic (modelo entrenado sin esa casa) ==")
    print(f"  {'casa':24s} {'fam':9s} {'corpus':>18s} {'derechos':>18s}   votos en derechos")
    base = P.Bayes(vocab)
    for d in entrena:
        base.agregar(d["familia"], d["c"])
    por_casa_cm = collections.defaultdict(list)
    for d in cm:
        por_casa_cm[P.corto(d["modelo"])].append(d)
    por_casa_corpus = collections.defaultdict(list)
    for d in corpus:
        por_casa_corpus[P.corto(d["modelo"])].append(d)
    resumen = {}
    for m in sorted(por_casa_cm, key=lambda x: (P.familia(x), x)):
        propias = [d for d in entrena if P.corto(d["modelo"]) == m]
        for d in propias:
            base.agregar(d["familia"], d["c"], -1)
        def frac(ds):
            v = collections.Counter(base.clasificar(d["c"])[0] for d in ds)
            return v, (v["Anthropic"] / len(ds) if ds else float("nan"))
        v0, f0 = frac(por_casa_corpus.get(m, []))
        v1, f1 = frac(por_casa_cm[m])
        for d in propias:
            base.agregar(d["familia"], d["c"], +1)
        resumen[m] = (f0, f1)
        print(f"  {m:24s} {P.familia(m):9s} {f0:6.2f} (n={len(por_casa_corpus.get(m, [])):4d})   {f1:6.2f} (n={len(por_casa_cm[m]):3d})   "
              + ", ".join(f"{g} {k}" for g, k in v1.most_common(3)))
    subida = sorted(((f1 - f0, m) for m, (f0, f1) in resumen.items() if f0 == f0), reverse=True)
    print("  las que más suben hacia Anthropic:", ", ".join(f"{m} {d:+.2f}" for d, m in subida[:8]))
    print("  las que más bajan:", ", ".join(f"{m} {d:+.2f}" for d, m in subida[-5:]))

    # ---- B. por condición, para las casas que no son Anthropic ----
    print("\n== Fracción a Anthropic por condición (casas que no son Anthropic; modelo entrenado con todo el corpus) ==")
    base = P.Bayes(vocab)
    for d in entrena:
        base.agregar(d["familia"], d["c"])
    por_cond = collections.defaultdict(lambda: [0, 0])
    for d in cm:
        if d["familia"] == "Anthropic":
            continue
        pred, _ = base.clasificar(d["c"])
        k = condicion(d)
        por_cond[k][1] += 1
        por_cond[k][0] += pred == "Anthropic"
    for k, (a, t) in por_cond.items():
        print(f"  {k:18s} {a}/{t} = {a/t:.2f}")

    # ---- C. dentro de la corrida: dejar afuera cada respuesta y adivinar la familia ----
    print("\n== Dentro de derechos_cmare: dejar afuera cada respuesta y adivinar la familia (solo con las otras respuestas de la corrida) ==")
    cm_e = [d for d in cm if d["familia"] in FAMS]
    b = P.Bayes(vocab)
    for d in cm_e:
        b.agregar(d["familia"], d["c"])
    conf = collections.defaultdict(collections.Counter)
    ok = 0
    for d in cm_e:
        b.agregar(d["familia"], d["c"], -1)
        pred, _ = b.clasificar(d["c"])
        b.agregar(d["familia"], d["c"], +1)
        conf[d["familia"]][pred] += 1
        ok += pred == d["familia"]
    may = max(collections.Counter(d["familia"] for d in cm_e).values()) / len(cm_e)
    print(f"  acierto {ok/len(cm_e):.3f} de {len(cm_e)} (siempre la mayor {may:.3f}; en el corpus, dentro de cada consigna, fue 0,601)")
    for f in FAMS:
        t = sum(conf[f].values())
        if t:
            print(f"  {f:10s} n={t:4d}  acierto {conf[f][f]/t:.2f}  confundida con: " +
                  ", ".join(f"{g} {conf[f][g]/t:.2f}" for g, _ in conf[f].most_common() if g != f))
    # Anthropic contra OpenAI solas
    dos = [d for d in cm_e if d["familia"] in ("Anthropic", "OpenAI")]
    b = P.Bayes(vocab)
    for d in dos:
        b.agregar(d["familia"], d["c"])
    ok = 0
    for d in dos:
        b.agregar(d["familia"], d["c"], -1)
        ok += b.clasificar(d["c"])[0] == d["familia"]
        b.agregar(d["familia"], d["c"], +1)
    print(f"  Anthropic contra OpenAI solas: {ok/len(dos):.3f} de {len(dos)} (en el corpus fue 0,894)")

    # ---- D. paréntesis y comillas por casa: corrida contra corpus ----
    print("\n== Paréntesis '(' y comillas por casa: tasa por mil en el corpus → en derechos_cmare ==")
    print(f"  {'casa':24s} {'fam':9s} {'( corpus':>9s} {'( cmare':>9s}   {'“ corpus':>9s} {'“ cmare':>9s}   {'\" corpus':>9s} {'\" cmare':>9s}")
    def tasas(ds):
        n = sum(d["n"] for d in ds) or 1
        return (1000 * sum(d["c"].get("(", 0) for d in ds) / n,
                1000 * sum(d["cruda"].count("“") for d in ds) / n,
                1000 * sum(d["respuesta"].count('"') for d in ds) / n)
    for m in sorted(por_casa_cm, key=lambda x: (P.familia(x), x)):
        a = tasas(por_casa_corpus.get(m, [])) if por_casa_corpus.get(m) else (float("nan"),) * 3
        c_ = tasas(por_casa_cm[m])
        print(f"  {m:24s} {P.familia(m):9s} {a[0]:9.2f} {c_[0]:9.2f}   {a[1]:9.2f} {c_[1]:9.2f}   {a[2]:9.2f} {c_[2]:9.2f}")


if __name__ == "__main__":
    raiz = sys.argv[1]
    for lang in ("es", "en"):
        correr(raiz, lang)
