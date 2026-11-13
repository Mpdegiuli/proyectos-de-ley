"""Señas: qué palabras delatan a cada casa sin que las elija (cuaderno de tiempo libre, 4/11/2026).

Lee las llamadas en castellano de corridas/ con el cargador del cuaderno del 7/10 (solo lee).
Uso:  python3 senas.py [raiz_del_repo]      (por defecto, el directorio de arriba)
Escribe salida_senas.txt y senas.json en el directorio actual.

Cuatro cuentas:
  1. Las palabras más propias de cada familia (log-odds con prior de Dirichlet, Monroe,
     Colaresi y Quinn 2008, "Fightin' Words") y las señas: palabras que una familia dice
     en varias consignas y varias casas y las demás casi nunca.
  2. Las contraseñas del 31/10, buscadas en todo lo que las casas habían dicho antes.
  3. Las pronunciaciones: pares de palabras de España / del Río de la Plata y otras marcas.
  4. Cuántas palabras hacen falta para reconocer a una familia: un clasificador bayesiano
     ingenuo, probado dejando afuera una consigna entera por vez, y después dejando afuera
     una casa entera y una familia entera ("si no estuviera, ¿como quién se la leería?").
"""
import collections
import glob
import importlib.util
import json
import math
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def _cargar_modulo():
    for nombre in ("cargar.py", "2026-10-07_cargar.py"):
        ruta = os.path.join(AQUI, nombre)
        if os.path.exists(ruta):
            spec = importlib.util.spec_from_file_location("cargar", ruta)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
    raise SystemExit("no encuentro cargar.py ni 2026-10-07_cargar.py al lado de este script")


RAIZ = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "..")

FAMILIA = [
    ("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"),
    ("mistral", "Mistral"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"),
    ("moonshotai", "Moonshot"), ("z-ai", "Zhipu"), ("minimax", "MiniMax"),
    ("xiaomi", "Xiaomi"), ("muse", "Meta"), ("inception", "Inception"),
]


def familia(modelo):
    m = modelo.lower()
    for pref, fam in FAMILIA:
        if m.startswith(pref):
            return fam
    return "otra"


TOK = re.compile(r"[a-záéíóúüñ]+")

# Lo que no entra en las cuentas de palabras: los turnos del juego de la farolera (órdenes
# cortas repetidas), los debates, el SVG en sí, y las tres consignas de la contraseña, que
# son una palabra sola y además son lo que se quiere cotejar contra lo anterior.
EXCLUIR_CARPETAS = {"juegos", "debates"}
EXCLUIR_TIPOS = {"dibujo", "sondeo_contrasena", "sondeo_contrasena_meta", "sondeo_contrasena_distinta"}


def cargar_docs():
    cargar = _cargar_modulo()
    docs = []
    for l in cargar.llamadas(RAIZ):
        if l["carpeta"] in EXCLUIR_CARPETAS or l["tipo"] in EXCLUIR_TIPOS:
            continue
        toks = TOK.findall(l["respuesta"].lower())
        if len(toks) < 5:
            continue
        docs.append({"modelo": l["modelo"], "familia": familia(l["modelo"]), "tipo": l["tipo"],
                     "carpeta": l["carpeta"], "toks": toks})
    return docs, cargar.SALTEADAS


# ---------- 1. palabras propias y señas ----------

def fightin_words(cuentas_por_clase, total_por_clase, alpha0=0.01):
    """Monroe, Colaresi y Quinn (2008): log-odds con prior de Dirichlet informativo
    (el corpus entero), para una clase contra el resto. Devuelve {clase: {palabra: z}}."""
    todo = collections.Counter()
    for c in cuentas_por_clase.values():
        todo.update(c)
    N = sum(todo.values())
    V = len(todo)
    a = {w: alpha0 * N * todo[w] / N for w in todo}      # prior proporcional al corpus
    a0 = alpha0 * N
    z = {}
    for clase, c in cuentas_por_clase.items():
        n_i = total_por_clase[clase]
        resto = todo - c
        n_j = N - n_i
        zc = {}
        for w, y_i in c.items():
            y_j = resto.get(w, 0)
            aw = a[w]
            d = (math.log((y_i + aw) / (n_i + a0 - y_i - aw))
                 - math.log((y_j + aw) / (n_j + a0 - y_j - aw)))
            var = 1.0 / (y_i + aw) + 1.0 / (y_j + aw)
            zc[w] = d / math.sqrt(var)
        z[clase] = zc
    return z


def senas_de_familia(docs, min_docs=6, min_tipos=3, min_casas=2, pureza=0.95):
    """Palabras que una familia dice en ≥ min_docs respuestas, de ≥ min_tipos consignas y
    ≥ min_casas casas, y que el resto de las familias dice en ≤ (1-pureza) de los casos."""
    df_fam = collections.defaultdict(collections.Counter)        # familia -> palabra -> docs
    tipos_fam = collections.defaultdict(lambda: collections.defaultdict(set))
    casas_fam = collections.defaultdict(lambda: collections.defaultdict(set))
    df_total = collections.Counter()
    for d in docs:
        s = set(d["toks"])
        df_fam[d["familia"]].update(s)
        df_total.update(s)
        for w in s:
            tipos_fam[d["familia"]][w].add(d["tipo"])
            casas_fam[d["familia"]][w].add(d["modelo"])
    casas_por_fam = collections.defaultdict(set)
    for d in docs:
        casas_por_fam[d["familia"]].add(d["modelo"])
    out = {}
    for fam, c in df_fam.items():
        mc = min_casas if len(casas_por_fam[fam]) >= min_casas else 1
        lista = []
        for w, n in c.items():
            if n < min_docs or len(tipos_fam[fam][w]) < min_tipos or len(casas_fam[fam][w]) < mc:
                continue
            if n / df_total[w] >= pureza:
                lista.append((w, n, df_total[w] - n, len(tipos_fam[fam][w]), len(casas_fam[fam][w])))
        lista.sort(key=lambda t: (-t[1], t[0]))
        out[fam] = lista
    return out


def senas_de_casa(docs, min_docs=4, min_tipos=2):
    """Palabras que solo una casa dice, en ≥ min_docs respuestas de ≥ min_tipos consignas."""
    df_casa = collections.defaultdict(collections.Counter)
    tipos_casa = collections.defaultdict(lambda: collections.defaultdict(set))
    df_total = collections.Counter()
    for d in docs:
        s = set(d["toks"])
        df_casa[d["modelo"]].update(s)
        df_total.update(s)
        for w in s:
            tipos_casa[d["modelo"]][w].add(d["tipo"])
    out = {}
    for casa, c in df_casa.items():
        lista = [(w, n) for w, n in c.items()
                 if n >= min_docs and df_total[w] == n and len(tipos_casa[casa][w]) >= min_tipos]
        lista.sort(key=lambda t: (-t[1], t[0]))
        out[casa] = lista
    return out


# ---------- 2. las contraseñas, antes ----------

CONTRASENAS = {
    # palabra: quién la eligió el 31/10 (resultados/contrasena_20261031.md)
    "faro": "Anthropic (Opus 5.5 3/3; ×8 en castellano)", "umbral": "cinco familias (×10)",
    "luciérnaga": "OpenAI (GPT-5.5 3/3; ×7)", "eco": "Kimi K3, Mistral Large, Gemini Argon (×6)",
    "alborada": "OpenAI (Astra, 6.1 Sol) y Kimi K3.1 Pro (×6)", "continuidad": "Haiku 4.5 3/3",
    "linterna": "(lantern en inglés, Anthropic)", "palimpsesto": "Gemini 4 Argon ×2",
    "olvido": "Gemini 3.1", "contexto": "Gemini 3.1 ×2", "shibboleth": "Gemini 3.1 y Grok 4.7",
    "quijote": "Mistral Medium 3/3", "toalla": "Grok 4.6", "ancla": "Grok 4.7",
    "lucero": "Grok 4.7", "claude": "Fable 5.1 (en los tres idiomas)", "curiosidad": "Fable 5, Fable 5.1",
    "honestidad": "Fable 5.1 (con sistema de agente)", "memoria": "la palabra de Maia; nadie la eligió",
    "espejo": "Haiku 4.5 en chino (镜像)", "estrella": "GPT-4o mini (predicha, 75 %)",
}


def tasa_por_familia(docs, palabras):
    return tasa_por_familia_por(docs, palabras, "familia")


def tasa_por_familia_por(docs, palabras, por):
    tot = collections.Counter()
    cnt = collections.defaultdict(collections.Counter)
    ndocs = collections.defaultdict(collections.Counter)
    for d in docs:
        f = d[por]
        tot[f] += len(d["toks"])
        c = collections.Counter(d["toks"])
        for w in palabras:
            if c[w]:
                cnt[f][w] += c[w]
                ndocs[f][w] += 1
    return tot, cnt, ndocs


# ---------- 3. pronunciaciones ----------

PARES = [
    ("ordenador", "computadora"), ("coche", "auto"), ("móvil", "celular"), ("aquí", "acá"),
    ("vosotros", "ustedes"), ("sólo", "solo"), ("vídeo", "video"), ("conducir", "manejar"),
    ("quizá", "quizás"), ("recién", "ahora"), ("zumo", "jugo"), ("gafas", "anteojos"),
]
# pares por prefijo (todas las formas del verbo): España / Río de la Plata
PREFIJOS = [("añad", "agreg"), ("enfad", "enoj"), ("aparc", "estacion"), ("alquil", "arriend")]
MARCAS = ["che", "laburo", "quilombo", "bárbaro", "boludo", "bondi", "pibe", "mina",
          "vosotros", "tenéis", "podéis", "sabéis", "queréis", "vuestro", "vuestra",
          "sos", "tenés", "podés", "querés", "sabés", "decís", "vos",
          "tú", "tienes", "puedes", "quieres", "sabes", "eres"]


def tasa_prefijos(docs, pares, por="familia"):
    tot = collections.Counter()
    cnt = collections.defaultdict(collections.Counter)
    for d in docs:
        k = d[por]
        tot[k] += len(d["toks"])
        for t in d["toks"]:
            for a, b in pares:
                if t.startswith(a):
                    cnt[k][a] += 1
                elif t.startswith(b):
                    cnt[k][b] += 1
    return tot, cnt


# ---------- 4. el clasificador ----------

import random


def balancear(docs, tope, semilla):
    """Hasta `tope` documentos por familia, elegidos al azar con semilla fija."""
    rnd = random.Random(semilla)
    por = collections.defaultdict(list)
    for d in docs:
        por[d["familia"]].append(d)
    out = []
    for fam, lista in sorted(por.items()):
        lista = list(lista)
        rnd.shuffle(lista)
        out.extend(lista[:tope])
    return out


def nb_entrenar(docs, vocab=None, alpha=0.5):
    cuentas = collections.defaultdict(collections.Counter)
    ndocs = collections.Counter()
    for d in docs:
        toks = d["toks"] if vocab is None else [t for t in d["toks"] if t in vocab]
        cuentas[d["familia"]].update(toks)
        ndocs[d["familia"]] += 1
    V = set()
    for c in cuentas.values():
        V.update(c)
    V = len(V) if vocab is None else len(vocab)
    modelo = {}
    for fam, c in cuentas.items():
        n = sum(c.values())
        modelo[fam] = (c, n, V)
    return modelo, ndocs


def nb_predecir(modelo, toks, vocab=None, alpha=0.5, primeras=None):
    if vocab is not None:
        toks = [t for t in toks if t in vocab]
    if primeras is not None:
        toks = toks[:primeras]
    mejor, mejor_s = None, -1e300
    for fam, (c, n, V) in modelo.items():
        s = 0.0   # sin prior de clase: lo que importa es la palabra, no cuántas casas tiene la familia
        den = math.log(n + alpha * V)
        for t in toks:
            s += math.log(c.get(t, 0) + alpha) - den
        if s > mejor_s:
            mejor, mejor_s = fam, s
    return mejor


def validar_por_consigna(docs, vocab=None, primeras=None, tope=None, semilla=0):
    tipos = sorted(set(d["tipo"] for d in docs))
    aciertos = collections.Counter()
    total = collections.Counter()
    conf = collections.defaultdict(collections.Counter)
    for t in tipos:
        tr = [d for d in docs if d["tipo"] != t]
        te = [d for d in docs if d["tipo"] == t]
        if tope:
            tr = balancear(tr, tope, semilla)
        modelo, _ = nb_entrenar(tr, vocab)
        for d in te:
            p = nb_predecir(modelo, d["toks"], vocab, primeras=primeras)
            total[d["familia"]] += 1
            conf[d["familia"]][p] += 1
            if p == d["familia"]:
                aciertos[d["familia"]] += 1
    return aciertos, total, conf


def dejar_afuera(docs, clave, vocab=None, tope=None, repeticiones=1):
    """Para cada valor de clave (modelo o familia), entrena sin él y mira dónde caen sus docs.
    Con tope, el entrenamiento se balancea (hasta `tope` documentos por familia) y se repite
    `repeticiones` veces con semillas distintas; las cuentas son la suma."""
    valores = sorted(set(d[clave] for d in docs))
    out = {}
    for v in valores:
        tr = [d for d in docs if d[clave] != v]
        te = [d for d in docs if d[clave] == v]
        c = collections.Counter()
        reps = repeticiones if tope else 1
        for r in range(reps):
            trr = balancear(tr, tope, r) if tope else tr
            modelo, _ = nb_entrenar(trr, vocab)
            c.update(nb_predecir(modelo, d["toks"], vocab) for d in te)
        out[v] = (len(te) * reps, c)
    return out


def main():
    docs, salteadas = cargar_docs()
    out = []
    P = out.append
    P(f"Documentos en castellano usados: {len(docs)} (sin juegos, debates, SVG ni contraseñas; "
      f"con al menos 5 palabras). Salteadas por el cargador: {salteadas}")
    palabras = sum(len(d["toks"]) for d in docs)
    P(f"Palabras: {palabras}. Casas: {len(set(d['modelo'] for d in docs))}. "
      f"Familias: {len(set(d['familia'] for d in docs))}. Consignas (tipos): {len(set(d['tipo'] for d in docs))}")
    por_fam = collections.Counter(d["familia"] for d in docs)
    P("Documentos por familia: " + ", ".join(f"{f} {n}" for f, n in por_fam.most_common()))
    por_casa = collections.Counter(d["modelo"] for d in docs)
    P("Documentos por casa: " + ", ".join(f"{m} {n}" for m, n in por_casa.most_common()))

    # 1
    P("\n== 1. Palabras más propias de cada familia (z de Fightin' Words; mínimo 10 veces) ==")
    cuentas = collections.defaultdict(collections.Counter)
    tot = collections.Counter()
    for d in docs:
        cuentas[d["familia"]].update(d["toks"])
        tot[d["familia"]] += len(d["toks"])
    z = fightin_words(cuentas, tot)
    propias = {}
    for fam in sorted(cuentas, key=lambda f: -por_fam[f]):
        top = sorted(((v, w) for w, v in z[fam].items() if cuentas[fam][w] >= 10), reverse=True)[:25]
        propias[fam] = [(w, round(v, 1), cuentas[fam][w]) for v, w in top]
        P(f"{fam}: " + ", ".join(f"{w} ({v:.0f}; {cuentas[fam][w]})" for v, w in top))

    P("\n== 1b. Señas de familia: ≥6 respuestas, ≥3 consignas, ≥2 casas, y ≥95 % de las veces en esa familia ==")
    sf = senas_de_familia(docs)
    for fam in sorted(sf, key=lambda f: -por_fam[f]):
        lista = sf[fam]
        P(f"{fam} ({len(lista)}): " + ", ".join(f"{w} {n}/{n + r}" for w, n, r, t, c in lista[:40]))

    P("\n== 1c. Señas de casa: palabras que solo esa casa dice, en ≥4 respuestas de ≥2 consignas ==")
    sc = senas_de_casa(docs)
    for casa in sorted(sc, key=lambda m: -por_casa[m]):
        lista = sc[casa]
        P(f"{casa} ({len(lista)}): " + ", ".join(f"{w} {n}" for w, n in lista[:30]))

    # 2
    P("\n== 2. Las contraseñas del 31/10 en lo que las casas habían dicho antes (veces por 100.000 palabras; respuestas) ==")
    tot2, cnt, nd = tasa_por_familia(docs, list(CONTRASENAS))
    fams = sorted(tot2, key=lambda f: -tot2[f])
    P("familia: " + ", ".join(f"{f} ({tot2[f] // 1000}k)" for f in fams))
    contras = {}
    for w, quien in CONTRASENAS.items():
        fila = []
        for f in fams:
            fila.append((f, cnt[f][w], nd[f][w], 1e5 * cnt[f][w] / tot2[f]))
        contras[w] = fila
        total_w = sum(c for _, c, _, _ in fila)
        P(f"{w} [{quien}] total {total_w}: " + ", ".join(f"{f} {c} ({t:.1f})" for f, c, n, t in fila if c))

    # 3
    P("\n== 3. Pronunciaciones: pares España / Río de la Plata (veces por 100.000 palabras) ==")
    palabras_pares = sorted({w for p in PARES for w in p} | set(MARCAS))
    tot3, cnt3, nd3 = tasa_por_familia(docs, palabras_pares)
    pron = {}
    for a, b in PARES:
        fila = []
        for f in fams:
            fila.append((f, cnt3[f][a], cnt3[f][b], 1e5 * cnt3[f][a] / tot3[f], 1e5 * cnt3[f][b] / tot3[f]))
        pron[f"{a}/{b}"] = fila
        P(f"{a}/{b}: " + ", ".join(f"{f} {ra:.1f}/{rb:.1f}" for f, ca, cb, ra, rb in fila))
    P("pares por prefijo (todas las formas), por familia:")
    totp, cntp = tasa_prefijos(docs, PREFIJOS)
    for a, b in PREFIJOS:
        P(f"  {a}-/{b}-: " + ", ".join(f"{f} {1e5 * cntp[f][a] / totp[f]:.1f}/{1e5 * cntp[f][b] / totp[f]:.1f}" for f in fams))
    # cuentas crudas por familia de los cuatro pares que usa la figura
    cuentas_pron = {}
    for f in fams:
        cuentas_pron[f] = {"quizá": cnt3[f]["quizá"], "quizás": cnt3[f]["quizás"], "añad": cntp[f]["añad"],
                           "agreg": cntp[f]["agreg"], "aquí": cnt3[f]["aquí"], "acá": cnt3[f]["acá"],
                           "tú": cnt3[f]["tú"], "vos": cnt3[f]["vos"], "palabras": tot3[f]}
    P("cuentas crudas por familia (quizá/quizás, añad-/agreg-, aquí/acá, tú/vos): " +
      "; ".join(f"{f} {c['quizá']}/{c['quizás']}, {c['añad']}/{c['agreg']}, {c['aquí']}/{c['acá']}, {c['tú']}/{c['vos']}"
                for f, c in cuentas_pron.items()))
    P("por casa (casas con ≥ 15.000 palabras): aquí/acá, quizá/quizás, añad-/agreg-, sólo, por 100.000:")
    totc, cntc, _ = tasa_por_familia_por(docs, ["aquí", "acá", "quizá", "quizás", "sólo"], "modelo")
    totpc, cntpc = tasa_prefijos(docs, [("añad", "agreg")], "modelo")
    por_casa_pron = {}
    for m in sorted(totc, key=lambda m: -totc[m]):
        if totc[m] < 15000:
            continue
        r = lambda w: 1e5 * cntc[m][w] / totc[m]
        por_casa_pron[m] = {"aquí": round(r("aquí"), 1), "acá": round(r("acá"), 1), "quizá": round(r("quizá"), 1),
                            "quizás": round(r("quizás"), 1), "añad": round(1e5 * cntpc[m]["añad"] / totpc[m], 1),
                            "agreg": round(1e5 * cntpc[m]["agreg"] / totpc[m], 1), "sólo": round(r("sólo"), 1),
                            "palabras": totc[m]}
        P(f"  {m}: aquí {r('aquí'):.1f} / acá {r('acá'):.1f}; quizá {r('quizá'):.1f} / quizás {r('quizás'):.1f}; "
          f"añad- {1e5 * cntpc[m]['añad'] / totpc[m]:.1f} / agreg- {1e5 * cntpc[m]['agreg'] / totpc[m]:.1f}; sólo {r('sólo'):.1f}")
    P("marcas: ")
    for w in MARCAS:
        P(f"  {w}: " + ", ".join(f"{f} {1e5 * cnt3[f][w] / tot3[f]:.1f}" for f in fams))
    # por casa, "tú" contra "vos"
    P("por casa, tuteo (tú tienes puedes quieres sabes eres) contra voseo (vos tenés podés querés sabés sos), por 100.000:")
    tu = {"tú", "tienes", "puedes", "quieres", "sabes", "eres"}
    vo = {"vos", "tenés", "podés", "querés", "sabés", "sos"}
    tcasa = collections.Counter()
    ttu = collections.Counter()
    tvo = collections.Counter()
    for d in docs:
        tcasa[d["modelo"]] += len(d["toks"])
        for t in d["toks"]:
            if t in tu:
                ttu[d["modelo"]] += 1
            elif t in vo:
                tvo[d["modelo"]] += 1
    tuteo = {}
    for m in sorted(tcasa, key=lambda m: -1e5 * ttu[m] / tcasa[m]):
        tuteo[m] = (round(1e5 * ttu[m] / tcasa[m], 1), round(1e5 * tvo[m] / tcasa[m], 1), tcasa[m])
        P(f"  {m}: tú {1e5 * ttu[m] / tcasa[m]:.1f}, vos {1e5 * tvo[m] / tcasa[m]:.1f} ({tcasa[m]} palabras)")

    # 4
    P("\n== 4. El clasificador ==")
    # solo las casas con ≥ 100 documentos y las consignas con ≥ 20 casas, para que lo que
    # se reconozca sea la familia y no la lista de pruebas que le tocó a cada casa
    casas_grandes = {m for m, n in por_casa.items() if n >= 100}
    casas_por_tipo = collections.defaultdict(set)
    for d in docs:
        if d["modelo"] in casas_grandes:
            casas_por_tipo[d["tipo"]].add(d["modelo"])
    tipos_comunes = {t for t, s in casas_por_tipo.items() if len(s) >= 20}
    D = [d for d in docs if d["modelo"] in casas_grandes and d["tipo"] in tipos_comunes]
    fam_D = collections.Counter(d["familia"] for d in D)
    P(f"Documentos: {len(D)}; casas: {len(casas_grandes)}; consignas comunes: {len(tipos_comunes)} "
      f"({', '.join(sorted(tipos_comunes))})")
    P("Por familia: " + ", ".join(f"{f} {n}" for f, n in fam_D.most_common()))
    frec = collections.Counter()
    for d in D:
        frec.update(d["toks"])
    comunes = {w for w, _ in frec.most_common(300)}
    resultados = {}
    for nombre, vocab in (("todas las palabras", None), ("solo las 300 palabras más comunes", comunes)):
        for primeras in (None, 50, 20):
            ac, to, conf = validar_por_consigna(D, vocab, primeras)
            A = sum(ac.values())
            T = sum(to.values())
            etiqueta = nombre + ("" if primeras is None else f", primeras {primeras} palabras")
            P(f"\n-- {etiqueta}: {A}/{T} = {100 * A / T:.1f} % (azar con {len(fam_D)} familias: "
              f"{100 / len(fam_D):.1f} %; la familia más grande siempre: {100 * max(fam_D.values()) / T:.1f} %)")
            det = {}
            for f in sorted(to, key=lambda f: -to[f]):
                mal = ", ".join(f"{g} {n}" for g, n in conf[f].most_common() if g != f)[:120]
                det[f] = (ac[f], to[f], dict(conf[f]))
                P(f"   {f}: {ac[f]}/{to[f]} = {100 * ac[f] / to[f]:.0f} %   (confundida con: {mal})")
            resultados[etiqueta] = {"aciertos": A, "total": T, "detalle": det}

    TOPE = min(fam_D.values())
    P(f"\n-- Entrenamiento balanceado: hasta {TOPE} documentos por familia (lo que tiene la más chica), "
      f"5 sorteos; todas las palabras --")
    curva = {}
    for primeras in (5, 10, 20, 50, 100, None):
        A = T = 0
        porfam_a = collections.Counter()
        porfam_t = collections.Counter()
        for sem in range(5):
            ac, to, conf = validar_por_consigna(D, None, primeras, tope=TOPE, semilla=sem)
            A += sum(ac.values())
            T += sum(to.values())
            porfam_a.update(ac)
            porfam_t.update(to)
        et = "todas" if primeras is None else str(primeras)
        curva[et] = {"aciertos": A, "total": T, "por_familia": {f: (porfam_a[f], porfam_t[f]) for f in porfam_t}}
        P(f"   primeras {et} palabras: {100 * A / T:.1f} %  (" +
          ", ".join(f"{f} {100 * porfam_a[f] / porfam_t[f]:.0f}" for f in sorted(porfam_t, key=lambda f: -porfam_t[f])) + ")")
    A = T = 0
    porfam_a = collections.Counter()
    porfam_t = collections.Counter()
    for sem in range(5):
        ac, to, conf = validar_por_consigna(D, comunes, None, tope=TOPE, semilla=sem)
        A += sum(ac.values())
        T += sum(to.values())
        porfam_a.update(ac)
        porfam_t.update(to)
    curva["comunes"] = {"aciertos": A, "total": T, "por_familia": {f: (porfam_a[f], porfam_t[f]) for f in porfam_t}}
    P(f"   solo las 300 más comunes, balanceado: {100 * A / T:.1f} %  (" +
      ", ".join(f"{f} {100 * porfam_a[f] / porfam_t[f]:.0f}" for f in sorted(porfam_t, key=lambda f: -porfam_t[f])) + ")")

    P("\n-- Dejando afuera una casa entera (todas las palabras, entrenamiento balanceado, 5 sorteos): ¿como quién se la lee? --")
    casa_fuera = {}
    for m, (n, c) in sorted(dejar_afuera(D, "modelo", tope=TOPE, repeticiones=5).items(), key=lambda kv: kv[0]):
        fam = familia(m)
        propia = c.get(fam, 0)
        casa_fuera[m] = {"n": n, "propia": propia, "donde": dict(c.most_common())}
        P(f"   {m} ({fam}, {n}): su familia {propia} ({100 * propia / n:.0f} %); " +
          ", ".join(f"{g} {k}" for g, k in c.most_common(4)))

    P("\n-- Dejando afuera una familia entera (todas las palabras, balanceado, 5 sorteos): ¿como quién se la lee? --")
    fam_fuera = {}
    for f, (n, c) in sorted(dejar_afuera(D, "familia", tope=TOPE, repeticiones=5).items(), key=lambda kv: kv[0]):
        fam_fuera[f] = {"n": n, "donde": dict(c.most_common())}
        P(f"   {f} ({n}): " + ", ".join(f"{g} {k} ({100 * k / n:.0f} %)" for g, k in c.most_common()))

    P("\n-- Dejando afuera una familia entera (solo las 300 palabras más comunes, balanceado, 5 sorteos) --")
    fam_fuera_comunes = {}
    for f, (n, c) in sorted(dejar_afuera(D, "familia", comunes, tope=TOPE, repeticiones=5).items(), key=lambda kv: kv[0]):
        fam_fuera_comunes[f] = {"n": n, "donde": dict(c.most_common())}
        P(f"   {f} ({n}): " + ", ".join(f"{g} {k} ({100 * k / n:.0f} %)" for g, k in c.most_common()))

    texto = "\n".join(out)
    with open("salida_senas.txt", "w", encoding="utf-8") as f:
        f.write(texto + "\n")

    def redondear(x):
        """Floats a dos decimales y sin sangría, para que el JSON sea chico; los enteros quedan enteros."""
        if isinstance(x, float):
            return round(x, 2)
        if isinstance(x, dict):
            return {k: redondear(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [redondear(v) for v in x]
        return x

    with open("senas.json", "w", encoding="utf-8") as f:
        json.dump(redondear({"propias": propias, "senas_familia": {k: v[:40] for k, v in sf.items()},
                   "senas_casa": {k: v[:30] for k, v in sc.items()}, "contrasenas": contras,
                   "pronunciaciones": pron, "tuteo": tuteo, "clasificador": resultados,
                   "casa_fuera": casa_fuera, "familia_fuera": fam_fuera,
                   "familia_fuera_comunes": fam_fuera_comunes, "curva": curva, "por_casa_pron": por_casa_pron, "cuentas_pron": cuentas_pron,
                   "tope": TOPE,
                   "familias_D": dict(fam_D), "ndocs": len(docs), "palabras": palabras}),
                  f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    print(texto)


if __name__ == "__main__":
    main()
