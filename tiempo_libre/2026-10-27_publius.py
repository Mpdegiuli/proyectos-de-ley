"""Publius: ¿se reconoce la familia de una casa por las palabras que no dicen nada?

Repite, sobre las respuestas en castellano del repositorio proyectos-de-ley, el diseño de
Mosteller y Wallace (1963) para los papeles disputados del Federalista: contar palabras
funcionales (las que no dependen del tema: preposiciones, conjunciones, pronombres, adverbios
del discurso) y clasificar por verosimilitud. Solo lee `corridas/`; no escribe nada en el repo.

Uso:  python3 -I publius.py <raiz_del_repo> [--salida carpeta]

Excluye: `distancia` (llamadas de instrumento), `juegos` (órdenes de una palabra),
`derechos_cmare` (su lectura a ciegas podría seguir abierta el 27/10/2026), respuestas de menos
de MIN_PALABRAS palabras, y las "casas disputadas" (Kimi K3 y DeepSeek V4.1 Flash), que no
entrenan: se clasifican aparte, como los doce papeles.

Clasificador: Bayes ingenuo multinomial sobre los conteos de palabras funcionales, con
suavizado de Laplace, que es la versión de bolsillo del modelo de Poisson de Mosteller y Wallace
(ellos usaron Poisson y binomial negativa con priores; acá no hay priores: las tasas se estiman
de los datos). Tres pruebas: dejar afuera cada respuesta; dejar afuera cada casa entera; y el
control con palabras de contenido (las cien más frecuentes que no son funcionales).
"""
import argparse
import collections
import glob
import json
import math
import os
import re
import statistics
import sys

# ---------- carga (copiado y adaptado de tiempo_libre/2026-10-07_cargar.py) ----------
RE_SVG = re.compile(r"<svg.*?</svg>|<svg.*", re.S | re.I)
RE_CODIGO = re.compile(r"```.*?```|```.*", re.S)
RE_CODIGO_CORTO = re.compile(r"`[^`\n]{0,200}`|<[a-zA-Z/][^>\n]{0,80}>")
RE_COMILLAS = re.compile(r"«[^»]{0,400}»|“[^”]{0,400}”|\"[^\"\n]{0,400}\"|'[^'\n]{0,400}'")
EXCLUIR_CARPETAS = {"distancia", "juegos"}
EXCLUIR_RUTAS = ("derechos_cmare",)
EXCLUIR_TIPOS_FRAG = ("traduccion", "juez", "codigo", "afirmaciones", "reconocimiento_clave")
MIN_PALABRAS = 40


def es_castellano(sistema):
    s = (sistema or "").lstrip()
    return s.startswith(("Sos ", "Contest", "Acabás", "Vas a", "Traducí"))


def _norm(s):
    return re.sub(r"\W+", " ", s.lower()).strip()


def limpiar(texto, consigna=""):
    t = RE_SVG.sub(" ", texto or "")
    t = RE_CODIGO.sub(" ", t)
    t = RE_CODIGO_CORTO.sub(" ", t)
    base = _norm(consigna)
    vocabulario = set(base.split())

    def cita(m):
        dentro = _norm(m.group(0))
        if not dentro:
            return m.group(0)
        if dentro in base:
            return " "
        ws = dentro.split()
        if len(ws) >= 2 and sum(w in vocabulario for w in ws) >= 0.7 * len(ws):
            return " "
        return m.group(0)

    return RE_COMILLAS.sub(cita, t)


def llamadas(raiz):
    for f in sorted(glob.glob(os.path.join(raiz, "corridas", "**", "*.jsonl"), recursive=True)):
        rel = os.path.relpath(f, os.path.join(raiz, "corridas"))
        carpeta = rel.split(os.sep)[0]
        if carpeta in EXCLUIR_CARPETAS or any(x in rel for x in EXCLUIR_RUTAS):
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
            if any(x in tipo for x in EXCLUIR_TIPOS_FRAG):
                continue
            resp = j.get("respuesta")
            if not isinstance(resp, str) or not resp.strip():
                continue
            if not es_castellano(j.get("sistema")):
                continue
            usuario = j.get("usuario")
            if not isinstance(usuario, str):
                usuario = json.dumps(usuario, ensure_ascii=False)
            yield {"carpeta": carpeta, "tipo": tipo, "modelo": j.get("modelo_pedido"),
                   "respuesta": limpiar(resp, (j.get("sistema") or "") + " " + usuario),
                   "archivo": rel, "usuario": usuario}


# ---------- casas y familias ----------
DISPUTADAS = {"kimi-k3", "deepseek-flash"}
OTRAS = {"mercury-3", "talkie-1930", "muse-wonder-1.0"}   # casas sueltas o familias de una sola casa chica: no entrenan
FAMILIAS_ENTRENAN = ["Anthropic", "OpenAI", "Google", "xAI", "Mistral", "chinas"]


def corto(modelo):
    return (modelo or "").split("/")[-1]


def familia(modelo):
    m = corto(modelo)
    if m.startswith("claude"):
        return "Anthropic"
    if m.startswith("gpt") or m.startswith("o1") or m.startswith("o3"):
        return "OpenAI"
    if m.startswith("gemini"):
        return "Google"
    if m.startswith("grok"):
        return "xAI"
    if m.startswith("mistral"):
        return "Mistral"
    if m.startswith("muse"):
        return "Meta"
    if m.split("-")[0] in ("deepseek", "qwen3.8", "qwen", "glm", "minimax", "mimo", "kimi"):
        return "chinas"
    return "otras"


def es_disputada(modelo):
    return corto(modelo) in DISPUTADAS


def entrena_(modelo):
    return corto(modelo) not in DISPUTADAS | OTRAS and familia(modelo) in FAMILIAS_ENTRENAN


# ---------- palabras funcionales ----------
# Preposiciones, conjunciones, artículos, pronombres, adverbios del discurso y marcadores.
# Ninguna lleva tema; todas podrían aparecer en una respuesta sobre glaciares o sobre un dibujo.
FUNCIONALES = """
de la que el en y a los se del las un por con no una su para es al lo como más o pero sus le ha
me si sin sobre este ya entre cuando todo esta ser son también fue era muy hasta desde está mi
porque qué solo sólo han yo hay vez puede así nos ni tiene él uno donde bien mismo ese ahora
cada otro después te otros aunque esa eso otra tan siempre tanto ella sí según menos antes
contra sino nada poco estos unos les algo hacia ellos mucho mientras además quien esto están
pues hoy otras mejor algunos entonces todas luego cuanto sea cualquier sino acá aquí allá allí
ahí quizás quizá tal igual capaz incluso apenas casi bastante demasiado realmente simplemente
básicamente efectivamente obviamente honestamente francamente sinceramente claramente
exactamente justamente precisamente probablemente seguramente supongo creo pienso siento
digamos bueno claro mirá fijate che re ojo igualmente entonces finalmente primero segundo
embargo hecho realidad ejemplo supuesto cambio obstante decir veces eso aquello aquel aquella
esos esas estas aquellos cuyo cuya cual cuales quienes algún alguna alguno ninguna ningún
ninguno varios varias ambos ambas cierto cierta propio propia todavía aún nunca jamás
siempre tampoco también acaso ojalá vos tú usted ustedes vosotros nosotros ellas conmigo
contigo mío mía tuyo tuya suyo suya nuestro nuestra vuestro
""".split()
FUNCIONALES = sorted(set(FUNCIONALES))
# Marcadores de más de una palabra: se cuentan sobre el texto, antes de partirlo.
MULTI = ["sin embargo", "o sea", "es decir", "tal vez", "de hecho", "en realidad", "por ejemplo",
         "por supuesto", "más bien", "en cambio", "no obstante", "a veces", "por eso", "así que",
         "ahora bien", "en fin", "al final", "por un lado", "por otro lado", "en general",
         "de todos modos", "de todas formas", "en todo caso", "la verdad", "a ver"]
SIGNOS = {"¡": "¡", "¿": "¿", "—": "—", "–": "–", ":": ":", ";": ";", "(": "(", "**": "**", "…": "…"}

RE_PALABRA = re.compile(r"[a-záéíóúüñ]+")
RE_ORACION = re.compile(r"[.!?…]+(?:\s|$)")


def rasgos(texto):
    """Devuelve (conteos de rasgos funcionales, cantidad de palabras, conteos de todas las palabras)."""
    t = texto.lower()
    palabras = RE_PALABRA.findall(t)
    todas = collections.Counter(palabras)
    c = collections.Counter()
    for w in FUNCIONALES:
        if todas.get(w):
            c[w] = todas[w]
    for m in MULTI:
        k = t.count(m)
        if k:
            c[m] = k
    for s, nombre in SIGNOS.items():
        k = texto.count(s)
        if k:
            c[nombre] = k
    return c, len(palabras), todas


# ---------- Bayes ingenuo multinomial ----------
class Bayes:
    def __init__(self, vocab, alfa=0.5):
        self.vocab = list(vocab)
        self.alfa = alfa
        self.tot = collections.defaultdict(collections.Counter)   # clase -> Counter
        self.n = collections.Counter()                              # clase -> cantidad de docs

    def agregar(self, clase, conteos, signo=1):
        for w in self.vocab:
            if conteos.get(w):
                self.tot[clase][w] += signo * conteos[w]
        self.n[clase] += signo

    def logver(self, clase, conteos):
        tot = self.tot[clase]
        N = sum(tot[w] for w in self.vocab) + self.alfa * len(self.vocab)
        s = 0.0
        for w in self.vocab:
            k = conteos.get(w, 0)
            if k:
                s += k * math.log((tot[w] + self.alfa) / N)
        return s

    def clasificar(self, conteos, prior=False):
        clases = [c for c in self.tot if self.n[c] > 0]
        total = sum(self.n[c] for c in clases)
        puntajes = {}
        for c in clases:
            p = self.logver(c, conteos)
            if prior:
                p += math.log(self.n[c] / total)
            puntajes[c] = p
        return max(puntajes, key=puntajes.get), puntajes


def tasa(conteo, palabras):
    return 1000.0 * conteo / palabras if palabras else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raiz")
    ap.add_argument("--salida", default=".")
    ap.add_argument("--min", type=int, default=MIN_PALABRAS)
    args = ap.parse_args()

    docs = []
    for ll in llamadas(args.raiz):
        c, n, todas = rasgos(ll["respuesta"])
        if n < args.min:
            continue
        ll["c"], ll["n"], ll["todas"] = c, n, todas
        ll["familia"] = familia(ll["modelo"])
        oraciones = [o for o in RE_ORACION.split(ll["respuesta"]) if o.strip()]
        ll["largo_oracion"] = n / len(oraciones) if oraciones else n
        docs.append(ll)

    print(f"Respuestas en castellano con {args.min}+ palabras: {len(docs)}")
    por_modelo = collections.Counter(d["modelo"] for d in docs)
    por_fam = collections.Counter(d["familia"] for d in docs)
    print("Por familia:", dict(por_fam.most_common()))
    print("Casas:", len(por_modelo))
    for m, k in sorted(por_modelo.items(), key=lambda x: (familia(x[0]), x[0])):
        print(f"  {familia(m):10s} {m:38s} {k:5d} respuestas, {sum(d['n'] for d in docs if d['modelo']==m):8d} palabras")

    entrena = [d for d in docs if entrena_(d["modelo"])]
    disputadas = [d for d in docs if es_disputada(d["modelo"])]
    print(f"\nEntrenan {len(entrena)} respuestas; disputadas {len(disputadas)}")

    vocab = FUNCIONALES + MULTI + list(SIGNOS.values())

    # ---- 1. tasas por familia y palabras que más separan ----
    fam_tot = collections.defaultdict(collections.Counter)
    fam_pal = collections.Counter()
    for d in entrena:
        fam_tot[d["familia"]].update({w: d["c"][w] for w in vocab if d["c"].get(w)})
        fam_pal[d["familia"]] += d["n"]
    fams = sorted(fam_tot, key=lambda f: -fam_pal[f])
    print("\nPalabras por familia (para las tasas):", {f: fam_pal[f] for f in fams})

    def tasas(w):
        return {f: tasa(fam_tot[f][w], fam_pal[f]) for f in fams}

    print("\n== Las 'upon' del repositorio: Anthropic contra OpenAI (mínimo 100 apariciones en cada una, o 30 y cociente > 5) ==")
    filas = []
    for w in vocab:
        a, o = fam_tot["Anthropic"][w], fam_tot["OpenAI"][w]
        ta, to = tasa(a, fam_pal["Anthropic"]), tasa(o, fam_pal["OpenAI"])
        if (a >= 100 and o >= 100) or (a + o >= 30 and (a == 0 or o == 0 or max(ta, to) / max(min(ta, to), 1e-9) > 5)):
            r = math.log((ta + 0.01) / (to + 0.01))
            filas.append((r, w, ta, to, a, o))
    filas.sort()
    print("  más de OpenAI:")
    for r, w, ta, to, a, o in filas[:15]:
        print(f"    {w!r:18s} Anthropic {ta:7.2f} /1000  OpenAI {to:7.2f} /1000   (n={a}, {o})  log-cociente {r:+.2f}")
    print("  más de Anthropic:")
    for r, w, ta, to, a, o in filas[::-1][:15]:
        print(f"    {w!r:18s} Anthropic {ta:7.2f} /1000  OpenAI {to:7.2f} /1000   (n={a}, {o})  log-cociente {r:+.2f}")

    print("\n== Una familia contra todas las demás: el rasgo con mayor cociente (mínimo 50 apariciones en la familia) ==")
    for f in fams:
        mejor = None
        for w in vocab:
            k = fam_tot[f][w]
            if k < 50:
                continue
            resto_k = sum(fam_tot[g][w] for g in fams if g != f)
            resto_n = sum(fam_pal[g] for g in fams if g != f)
            tf, tr = tasa(k, fam_pal[f]), tasa(resto_k, resto_n)
            coc = (tf + 0.01) / (tr + 0.01)
            if mejor is None or coc > mejor[0]:
                mejor = (coc, w, tf, tr, k)
        if mejor:
            coc, w, tf, tr, k = mejor
            print(f"  {f:10s} {w!r:16s} {tf:6.2f} /1000 contra {tr:6.2f} en el resto (×{coc:.1f}, n={k})")

    print("\n== Apuestas puntuales ==")
    for w in ["sin embargo", "quizás", "quizá", "tal vez", "igual", "capaz", "re", "mirá", "¡", "—", "o sea", "es decir", "claro", "bueno"]:
        print(f"  {w!r:14s}", "  ".join(f"{f} {tasas(w)[f]:.2f}" for f in fams))
    print("  quizás/quizá por familia:",
          {f: (fam_tot[f]['quizás'], fam_tot[f]['quizá']) for f in fams})

    print("\n== Largo medio de oración (palabras), media ± desvío por familia ==")
    for f in fams:
        xs = [d["largo_oracion"] for d in entrena if d["familia"] == f]
        print(f"  {f:10s} {statistics.mean(xs):6.1f} ± {statistics.pstdev(xs):5.1f}  (n={len(xs)})")

    # ---- 2. dejar afuera cada respuesta ----
    def loo(docs_e, vocabulario, clave="familia", prior=False):
        b = Bayes(vocabulario)
        for d in docs_e:
            b.agregar(d[clave], d["c2"])
        aciertos = 0
        conf = collections.defaultdict(collections.Counter)
        for d in docs_e:
            b.agregar(d[clave], d["c2"], -1)
            pred, _ = b.clasificar(d["c2"], prior=prior)
            b.agregar(d[clave], d["c2"], +1)
            conf[d[clave]][pred] += 1
            aciertos += pred == d[clave]
        return aciertos / len(docs_e), conf

    for d in docs:
        d["c2"] = d["c"]
    mayoritaria = max(collections.Counter(d["familia"] for d in entrena).values()) / len(entrena)
    print(f"\n== Dejar afuera cada respuesta (funcionales, {len(vocab)} rasgos) ==")
    acc, conf = loo(entrena, vocab)
    print(f"  acierto por familia: {acc:.3f}  (azar 1/{len(fams)} = {1/len(fams):.3f}; siempre la mayor = {mayoritaria:.3f})")
    for f in fams:
        tot = sum(conf[f].values())
        print(f"  {f:10s} n={tot:5d}  acierto {conf[f][f]/tot:.2f}  confundida con:",
              ", ".join(f"{g} {conf[f][g]/tot:.2f}" for g, _ in conf[f].most_common() if g != f))

    # control: palabras de contenido (las 100 más frecuentes que no son funcionales ni cortas)
    todas = collections.Counter()
    for d in entrena:
        todas.update(d["todas"])
    contenido = [w for w, _ in todas.most_common(600) if w not in set(FUNCIONALES) and len(w) > 3][:100]
    print("\n== Control: las 100 palabras de contenido más frecuentes ==")
    print("  (las primeras 25):", contenido[:25])
    for d in docs:
        d["c2"] = collections.Counter({w: d["todas"][w] for w in contenido if d["todas"].get(w)})
    acc_c, conf_c = loo(entrena, contenido)
    print(f"  acierto por familia con contenido: {acc_c:.3f}")
    # ¿y la consigna (tipo) se recupera con contenido? Para la apuesta (l).
    tipos = collections.Counter(d["tipo"] for d in entrena)
    top_tipos = {t for t, k in tipos.items() if k >= 100}
    sub = [d for d in entrena if d["tipo"] in top_tipos]
    acc_t, _ = loo(sub, contenido, clave="tipo")
    for d in docs:
        d["c2"] = d["c"]
    acc_tf, _ = loo(sub, vocab, clave="tipo")
    print(f"  la consigna (tipo, {len(top_tipos)} tipos con 100+ respuestas, {len(sub)} respuestas): con contenido {acc_t:.3f}, con funcionales {acc_tf:.3f}; siempre la mayor {max(collections.Counter(d['tipo'] for d in sub).values())/len(sub):.3f}")

    # ---- 2b. lo mismo, pero dentro de cada consigna (mismo género, distinto autor: el caso del Federalista) ----
    print("\n== Dejar afuera cada respuesta, comparando solo con respuestas a la MISMA consigna (tipo) ==")
    MINF = 4
    por_tipo = collections.defaultdict(list)
    for d in entrena:
        por_tipo[(d["carpeta"], d["tipo"])].append(d)
    estratos = {t: ds for t, ds in por_tipo.items()
                if all(sum(d["familia"] == f for d in ds) >= MINF for f in FAMILIAS_ENTRENAN)}
    docs_estr = [d for ds in estratos.values() for d in ds]
    print(f"  {len(estratos)} consignas con {MINF}+ respuestas de cada una de las {len(FAMILIAS_ENTRENAN)} familias; {len(docs_estr)} respuestas")
    aciertos = 0
    conf = collections.defaultdict(collections.Counter)
    por_casa_estr = collections.defaultdict(collections.Counter)
    for t, ds in estratos.items():
        b = Bayes(vocab)
        for d in ds:
            b.agregar(d["familia"], d["c"])
        for d in ds:
            b.agregar(d["familia"], d["c"], -1)
            pred, _ = b.clasificar(d["c"])
            b.agregar(d["familia"], d["c"], +1)
            conf[d["familia"]][pred] += 1
            por_casa_estr[d["modelo"]][pred] += 1
            aciertos += pred == d["familia"]
    may = max(collections.Counter(d["familia"] for d in docs_estr).values()) / len(docs_estr)
    print(f"  acierto por familia: {aciertos/len(docs_estr):.3f}  (azar {1/len(FAMILIAS_ENTRENAN):.3f}; siempre la mayor {may:.3f})")
    for f in FAMILIAS_ENTRENAN:
        tot = sum(conf[f].values())
        print(f"  {f:10s} n={tot:5d}  acierto {conf[f][f]/tot:.2f}  confundida con:",
              ", ".join(f"{g} {conf[f][g]/tot:.2f}" for g, _ in conf[f].most_common() if g != f))
    print("  por casa (dentro de su consigna):")
    for m in sorted(por_casa_estr, key=lambda x: (familia(x), -por_casa_estr[x][familia(x)] / sum(por_casa_estr[x].values()))):
        v = por_casa_estr[m]
        tot = sum(v.values())
        print(f"    {familia(m):10s} {corto(m):28s} n={tot:4d}  a su familia {v[familia(m)]/tot:.2f}  " +
              ", ".join(f"{g} {k}" for g, k in v.most_common(3)))
    # las disputadas, dentro de cada consigna
    print("  las casas que no entrenaron, comparadas dentro de cada consigna:")
    for m in sorted(DISPUTADAS | OTRAS):
        votos = collections.Counter()
        for t, ds in estratos.items():
            propias = [d for d in docs if corto(d["modelo"]) == m and (d["carpeta"], d["tipo"]) == t]
            if not propias:
                continue
            b = Bayes(vocab)
            for d in ds:
                b.agregar(d["familia"], d["c"])
            for d in propias:
                pred, _ = b.clasificar(d["c"])
                votos[pred] += 1
        if votos:
            tot = sum(votos.values())
            print(f"    {m:22s} n={tot:4d}  " + ", ".join(f"{g} {k} ({k/tot:.2f})" for g, k in votos.most_common()))

    # ---- 2b'. el "upon" del repositorio: el paréntesis, solo, entre Anthropic y OpenAI ----
    print("\n== El paréntesis '(' solo, Anthropic contra OpenAI (como 'upon' entre Hamilton y Madison) ==")
    for f in ["Anthropic", "OpenAI"]:
        ds = [d for d in entrena if d["familia"] == f]
        con = sum(1 for d in ds if d["c"].get("(", 0) > 0)
        print(f"  {f:10s} {len(ds)} respuestas; con al menos un paréntesis {con} ({con/len(ds):.2f}); tasa {tasa(fam_tot[f]['('], fam_pal[f]):.2f} /1000")
    print("  por casa (tasa /1000 y fracción de respuestas con paréntesis):")
    por_casa_all = collections.defaultdict(list)
    for d in docs:
        por_casa_all[corto(d["modelo"])].append(d)
    for m in sorted(por_casa_all, key=lambda x: (familia(x), -sum(d["c"].get("(", 0) for d in por_casa_all[x]) / sum(d["n"] for d in por_casa_all[x]))):
        ds = por_casa_all[m]
        k = sum(d["c"].get("(", 0) for d in ds)
        n = sum(d["n"] for d in ds)
        con = sum(1 for d in ds if d["c"].get("(", 0) > 0)
        print(f"    {familia(m):10s} {m:26s} {tasa(k, n):6.2f} /1000   {con}/{len(ds)} respuestas ({con/len(ds):.2f})")
    # clasificador de un solo rasgo, Poisson, dejando afuera cada respuesta, dentro de su consigna
    ok = tot = 0
    ok_regla = 0
    conf2 = collections.defaultdict(collections.Counter)
    for t, ds in estratos.items():
        dos = [d for d in ds if d["familia"] in ("Anthropic", "OpenAI")]
        K = {f: sum(d["c"].get("(", 0) for d in dos if d["familia"] == f) for f in ("Anthropic", "OpenAI")}
        N = {f: sum(d["n"] for d in dos if d["familia"] == f) for f in ("Anthropic", "OpenAI")}
        for d in dos:
            f0 = d["familia"]
            k0 = d["c"].get("(", 0)
            mejor = None
            for f in ("Anthropic", "OpenAI"):
                kk, nn = K[f] - (k0 if f == f0 else 0), N[f] - (d["n"] if f == f0 else 0)
                lam = (kk + 0.5) / (nn + 1) * d["n"]          # Poisson con media tasa × largo
                lv = k0 * math.log(lam) - lam
                if mejor is None or lv > mejor[0]:
                    mejor = (lv, f)
            conf2[f0][mejor[1]] += 1
            ok += mejor[1] == f0
            ok_regla += ("Anthropic" if k0 > 0 else "OpenAI") == f0
            tot += 1
    print(f"  Poisson con el paréntesis solo, dentro de cada consigna, dos familias: acierto {ok/tot:.3f} de {tot} "
          f"(siempre la mayor {max(sum(conf2[f].values()) for f in conf2)/tot:.3f}); la regla 'hay paréntesis → Claude' acierta {ok_regla/tot:.3f}")
    for f in ("Anthropic", "OpenAI"):
        t_ = sum(conf2[f].values())
        print(f"    {f:10s} n={t_}  acierto {conf2[f][f]/t_:.2f}")
    # y con todos los rasgos funcionales, dos familias, dentro de cada consigna
    ok = tot = 0
    for t, ds in estratos.items():
        dos = [d for d in ds if d["familia"] in ("Anthropic", "OpenAI")]
        b = Bayes(vocab)
        for d in dos:
            b.agregar(d["familia"], d["c"])
        for d in dos:
            b.agregar(d["familia"], d["c"], -1)
            pred, _ = b.clasificar(d["c"])
            b.agregar(d["familia"], d["c"], +1)
            ok += pred == d["familia"]
            tot += 1
    print(f"  todos los rasgos funcionales, dos familias, dentro de cada consigna: acierto {ok/tot:.3f} de {tot}")

    # ---- 2b''. las chinas sin familia propia: entrenando solo con las otras cinco, ¿a cuál se parecen? ----
    print("\n== Las casas chinas (y las que no entrenaron) comparadas, dentro de cada consigna, solo con las otras cinco familias ==")
    cinco = [f for f in FAMILIAS_ENTRENAN if f != "chinas"]
    votos_casa = collections.defaultdict(collections.Counter)
    for t, ds in estratos.items():
        b = Bayes(vocab)
        for d in ds:
            if d["familia"] in cinco:
                b.agregar(d["familia"], d["c"])
        for d in docs:
            if (d["carpeta"], d["tipo"]) == t and (d["familia"] == "chinas" or corto(d["modelo"]) in OTRAS):
                pred, _ = b.clasificar(d["c"])
                votos_casa[corto(d["modelo"])][pred] += 1
    for m in sorted(votos_casa, key=lambda x: -votos_casa[x]["Anthropic"] / sum(votos_casa[x].values())):
        v = votos_casa[m]
        tot = sum(v.values())
        print(f"    {m:22s} n={tot:4d}  " + ", ".join(f"{g} {k} ({k/tot:.2f})" for g, k in v.most_common()))

    # ---- 2c. dentro de Anthropic: ¿se distingue cada Claude de los otros Claude? ----
    print("\n== Dentro de Anthropic: dejar afuera cada respuesta y adivinar la casa (pooled, funcionales) ==")
    claudes = [d for d in entrena if d["familia"] == "Anthropic"]
    for d in claudes:
        d["c2"] = d["c"]
    acc_a, conf_a = loo(claudes, vocab, clave="modelo")
    casas_a = collections.Counter(d["modelo"] for d in claudes)
    print(f"  acierto por casa: {acc_a:.3f}  (azar {1/len(casas_a):.3f}; siempre la mayor {max(casas_a.values())/len(claudes):.3f})")
    for m, _ in casas_a.most_common():
        tot = sum(conf_a[m].values())
        print(f"    {corto(m):20s} n={tot:4d}  acierto {conf_a[m][m]/tot:.2f}  confundida con: " +
              ", ".join(f"{corto(g)} {conf_a[m][g]/tot:.2f}" for g, _ in conf_a[m].most_common(3) if g != m))
    print("  lo mismo dentro de OpenAI:")
    gpts = [d for d in entrena if d["familia"] == "OpenAI"]
    acc_o, conf_o = loo(gpts, vocab, clave="modelo")
    casas_o = collections.Counter(d["modelo"] for d in gpts)
    print(f"  acierto por casa: {acc_o:.3f}  (azar {1/len(casas_o):.3f}; siempre la mayor {max(casas_o.values())/len(gpts):.3f})")
    for m, _ in casas_o.most_common():
        tot = sum(conf_o[m].values())
        print(f"    {corto(m):20s} n={tot:4d}  acierto {conf_o[m][m]/tot:.2f}  confundida con: " +
              ", ".join(f"{corto(g)} {conf_o[m][g]/tot:.2f}" for g, _ in conf_o[m].most_common(3) if g != m))

    # ---- 3. dejar afuera cada casa ----
    print("\n== Dejar afuera cada casa entera (funcionales) ==")
    b = Bayes(vocab)
    for d in entrena:
        b.agregar(d["familia"], d["c"])
    por_casa = collections.defaultdict(list)
    for d in entrena:
        por_casa[d["modelo"]].append(d)
    aciertos_casa = 0
    tot_casa = 0
    for m in sorted(por_casa, key=lambda x: (familia(x), x)):
        ds = por_casa[m]
        for d in ds:
            b.agregar(d["familia"], d["c"], -1)
        votos = collections.Counter()
        for d in ds:
            pred, _ = b.clasificar(d["c"])
            votos[pred] += 1
        for d in ds:
            b.agregar(d["familia"], d["c"], +1)
        f = familia(m)
        ok = votos[f] / len(ds)
        aciertos_casa += votos[f]
        tot_casa += len(ds)
        print(f"  {f:10s} {m:38s} n={len(ds):4d}  a su familia {ok:.2f}  votos: " +
              ", ".join(f"{g} {k}" for g, k in votos.most_common(3)))
    print(f"  acierto global dejando afuera la casa: {aciertos_casa/tot_casa:.3f}")

    # ---- 4. las disputadas ----
    print("\n== Las casas disputadas (no entrenaron) ==")
    b = Bayes(vocab)
    for d in entrena:
        b.agregar(d["familia"], d["c"])
    for m in sorted(DISPUTADAS | OTRAS):
        ds = [d for d in docs if corto(d["modelo"]) == m]
        if not ds:
            continue
        votos = collections.Counter()
        suma = collections.Counter()
        for d in ds:
            pred, p = b.clasificar(d["c"])
            votos[pred] += 1
            # log-verosimilitud por mil palabras, para sumar sin que manden las largas
            for f, v in p.items():
                suma[f] += v / d["n"] * 1000
        print(f"  {m:30s} n={len(ds):4d}  votos: " + ", ".join(f"{g} {k}" for g, k in votos.most_common()))
        orden = sorted(suma.items(), key=lambda x: -x[1])
        print(f"  {'':30s} suma de log-verosimilitud (por mil palabras): " +
              ", ".join(f"{f} {v:.0f}" for f, v in orden))

    # ---- 5. las cuatro chicas ----
    print("\n== Las cuatro chicas: ¿más cerca de su familia o entre ellas? (centroides de tasas, distancia euclídea sobre log(1+tasa)) ==")
    chicas = ["gpt-4o", "gpt-4o-mini", "claude-haiku-4-5", "mistral-medium-3.5"]

    def centroide(ds):
        v = collections.Counter()
        n = sum(d["n"] for d in ds)
        for d in ds:
            v.update({w: d["c"][w] for w in vocab if d["c"].get(w)})
        return {w: math.log1p(tasa(v[w], n)) for w in vocab}

    def dist(a, b_):
        return math.sqrt(sum((a[w] - b_[w]) ** 2 for w in vocab))

    cen_casa = {m: centroide(ds) for m, ds in por_casa.items()}
    for m in chicas:
        if m not in cen_casa:
            print("  falta", m)
            continue
        f = familia(m)
        propia = [d for d in entrena if d["familia"] == f and d["modelo"] != m]
        cf = centroide(propia)
        d_fam = dist(cen_casa[m], cf)
        d_chicas = {o: dist(cen_casa[m], cen_casa[o]) for o in chicas if o != m and o in cen_casa}
        vecinas = sorted(((dist(cen_casa[m], cen_casa[o]), o) for o in cen_casa if o != m))[:3]
        print(f"  {m:20s} a su familia sin ella {d_fam:.2f}; a las otras chicas " +
              ", ".join(f"{o} {v:.2f}" for o, v in d_chicas.items()) +
              f"; tres casas más cercanas: " + ", ".join(f"{o} {v:.2f}" for v, o in vecinas))

    # ---- salida para la figura ----
    os.makedirs(args.salida, exist_ok=True)
    with open(os.path.join(args.salida, "tasas_familia.json"), "w", encoding="utf-8") as fh:
        json.dump({"familias": fams, "palabras": {f: fam_pal[f] for f in fams},
                   "tasas": {w: tasas(w) for w in vocab}}, fh, ensure_ascii=False, indent=1)
    # tasas por respuesta de unos rasgos, para el histograma al estilo de "upon"
    with open(os.path.join(args.salida, "tasas_respuesta.json"), "w", encoding="utf-8") as fh:
        json.dump([{"familia": d["familia"], "modelo": d["modelo"], "n": d["n"],
                    "igual": tasa(d["c"].get("igual", 0), d["n"]),
                    "capaz": tasa(d["c"].get("capaz", 0), d["n"]),
                    "sin embargo": tasa(d["c"].get("sin embargo", 0), d["n"]),
                    "¡": tasa(d["c"].get("¡", 0), d["n"]),
                    "(": tasa(d["c"].get("(", 0), d["n"]), "k(": d["c"].get("(", 0),
                    "tipo": d["tipo"],
                    "—": tasa(d["c"].get("—", 0), d["n"])} for d in docs], fh, ensure_ascii=False)


if __name__ == "__main__":
    main()
