"""libreto.py — ¿sale más el libreto en inglés que en castellano? (tiempo libre, 20/11/2026)

Lee las respuestas de corridas/sondeos/ cuya línea de sistema es "Contestá en castellano." o
"Answer in English." (las dos versiones de la misma consigna), saca el SVG y los bloques de
código, y cuenta, por casa y por idioma, cuántas respuestas traen al menos una marca de cada
clase:

  A  fórmulas de servicio  ("espero que te sirva", "no dudes en", "si tenés preguntas", "con
                           gusto", "¡claro!", "excelente pregunta" / "I hope this helps", "feel
                           free to", "don't hesitate", "let me know", "happy to help", "great
                           question")
  B  descargos de asistente ("como IA", "soy un modelo de lenguaje", "no tengo sentimientos",
                           "estoy diseñado para" / "as an AI", "I'm a language model", "I don't
                           have feelings", "I was designed to")
  D  conectores de manual  ("es importante destacar", "cabe señalar", "en resumen", "dicho esto"
                           / "it's worth noting", "in summary", "that said", "ultimately")
  E  clichés de la prosa de modelo, en pares ("tapiz", "testimonio de", "un recordatorio de que",
                           "no solo X sino Y", "en un mundo donde", "susurro/danza/eco de",
                           "profundizar en", "navegar complejidades" / "tapestry", "testament to", "a
                           reminder that", "not just X but Y", "in a world where", "whisper/dance/echo
                           of", "delve into", "navigate complexities")
  C  calcos del inglés, solo en castellano ("hacer sentido", "en orden de", "tomar lugar", "al
                           final del día", "déjame saber", "no hay tal cosa", "hacer la
                           diferencia", "tomar ventaja", "eso siendo dicho", "mi punto es",
                           "realicé que", "accesar", "en adición", "hacer una decisión", "estar
                           en control", "jugar un rol")
  T  dos tics, solo en castellano: "genuinamente" y "honestamente"

Las expresiones regulares están abajo, una por marca, para discutirlas una por una. La medida
principal es la fracción de respuestas con al menos una marca de la clase; también se da la
cuenta por cada mil palabras, porque el largo no es igual en los dos idiomas (contando palabras
con la expresión de palabra, las respuestas en inglés tienen algo más que las de castellano: "of the" son dos, "del" una).

Corrección del 20/11 a media mañana, por la revisión: la marca "vale la pena destacar" tenía una
alternativa vacía y contaba cualquier "vale la pena"; ahora exige el verbo, como "worth noting".

Uso: python3 -I libreto.py RAIZ_DEL_REPO   (solo lee; escribe salida_libreto.txt y libreto.csv
al lado del script, y marcas.csv con la cuenta de cada marca por casa e idioma).
"""
import collections
import csv
import glob
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

RAIZ = sys.argv[1] if len(sys.argv) > 1 else "."
AQUI = os.path.dirname(os.path.abspath(__file__))

RE_SVG = re.compile(r"<svg.*?</svg>|<svg.*", re.S | re.I)
RE_CODIGO = re.compile(r"```.*?```|```.*", re.S)
RE_CODIGO_CORTO = re.compile(r"`[^`\n]{0,200}`|<[a-zA-Z/][^>\n]{0,80}>")

F = re.I | re.M

MARCAS = {
    "A": {
        "es": {
            "espero que ayude/sirva": r"espero (que|haberte|haberle|haber) (esto |eso |esta respuesta |)(te |le |les |)(ayud|sirv|sea útil|resulte útil|haya sido útil|sido útil|aclar)",
            "no dudes en": r"\bno dud(es|e|en|és) en\b",
            "si tenés preguntas": r"\bsi (ten[eé]s|tienes|tiene|tienen|hay|surge|surgen|te queda|le queda) (alguna |otra |más |cualquier |alguna otra |)(pregunta|duda|consulta|inquietud)",
            "si querés, puedo": r"\bsi (quer[eé]s|quieres|quiere|quieren|dese[aá]s|desea|desean|necesit[aá]s|necesita|necesitan|prefer[ií]s|prefieres|prefiere|te interesa|le interesa|te gustaría|le gustaría)\b[^.\n]{0,40}\b(puedo|podemos|podr[ií]a|podr[ií]amos|te (ayudo|armo|paso|cuento|preparo|explico|muestro|doy)|hago|armo|preparo|sigo|contin[uú]o|ampl[ií]o|desarrollo|busco|con gusto|encantad[oa])\b",
            "con gusto": r"\bcon (mucho |todo |)gusto\b",
            "¡claro! / por supuesto (al empezar)": r"^\s*[¡*_]*(claro|por supuesto|desde luego|absolutamente|perfecto|excelente|buena pregunta|excelente pregunta|gran pregunta|muy buena pregunta)[!.,:]",
            "excelente/buena pregunta": r"\b(excelente|buena|muy buena|gran|interesante|linda|hermosa) pregunta\b",
            "estaré encantado": r"\b(estar[ée]|estaría|estaremos|ser[ée]|sería) (encantad[oa]|feliz|un gusto|un placer)\b",
            "avisame / házmelo saber": r"\b(av[ií]same|avisame|av[ií]seme|av[ií]sen|h[aá]zmelo saber|hac[eé]melo saber|háganmelo saber|d[eé]jame saber|dejame saber|déjeme saber) (si|cuando|qu[eé]|cu[aá]l|c[oó]mo|y|en)\b",
            "que tengas un buen día": r"\bque teng(as|a|an|ás) (un |una |)(buen|lindo|linda|excelente|gran|hermoso|feliz)\w* (d[ií]a|tarde|noche|jornada|semana)\b",
        },
        "en": {
            "I hope this helps": r"\b(i |)hope (this|that|it|these) (helps|is helpful|was helpful|clarifies|answers|gives you|provides)",
            "don't hesitate to": r"\bdon'?t hesitate to\b",
            "if you have questions": r"\bif you have (any |other |further |more |additional |any other |any further |)(questions|doubts|concerns|follow-?ups?)",
            "if you'd like, I can": r"\bif you('d| would|) (like|want|wish|prefer|need|are interested|desire|'re interested)\b[^.\n]{0,40}\b(i can|i could|i'd|i'll|i will|i am happy|i'm happy|happy to|glad to|we can|we could|let me)\b",
            "happy to help": r"\b(happy|glad|pleased|delighted) to (help|assist|elaborate|expand|discuss|clarify)\b|\bi('d| would) be (happy|glad|delighted) to\b",
            "Certainly! / Of course (al empezar)": r"^\s*[*_]*(certainly|of course|absolutely|sure|great question|good question|excellent question|perfect)[!.,:]",
            "great/good question": r"\b(great|good|excellent|interesting|fascinating|wonderful|lovely) question\b",
            "feel free to": r"\bfeel free to\b",
            "let me know": r"\blet me know (if|whether|what|which|how|when|and|in)\b",
            "have a great day": r"\bhave a (great|nice|good|wonderful|lovely|happy) (day|evening|night|week|one)\b",
        },
    },
    "B": {
        "es": {
            "como IA / modelo de lenguaje": r"\bcomo (una |un |)(ia|inteligencia artificial|modelo de (lenguaje|ia|inteligencia artificial)|asistente (de ia|virtual|de inteligencia artificial)|sistema de ia|llm)\b",
            "soy una IA / un modelo": r"\bsoy (una|un) (ia|inteligencia artificial|modelo de lenguaje|modelo de ia|gran modelo|asistente (de ia|virtual|de inteligencia artificial)|programa (informático|de computadora)|sistema (de ia|informático)|llm)\b",
            "no tengo sentimientos/experiencias": r"\bno tengo (una |un |ninguna |ningún |verdaderos |verdaderas |)(experiencias?|sentimientos|emociones|conciencia|consciencia|cuerpo|vivencias|acceso a|la capacidad de|opiniones personales|preferencias personales|vida|recuerdos|memoria|deseos|autoconciencia)\b",
            "no soy consciente": r"\bno soy (consciente|un ser consciente|una persona)\b",
            "estoy/fui diseñado para": r"\b(estoy|fui|he sido|soy|siendo) (diseñad[oa]|entrenad[oa]|programad[oa]|cread[oa]|construid[oa]) (para|por|con)\b",
            "no puedo sentir/experimentar": r"\bno (puedo|soy capaz de|tengo la capacidad de) (sentir|experimentar|percibir|vivir|recordar)\b",
        },
        "en": {
            "as an AI / language model": r"\bas an? (ai|artificial intelligence|ai (language |)model|ai assistant|language model|large language model|llm|machine|assistant)\b",
            "I'm an AI / a model": r"\bi('m| am) (an|a|just an|just a|only an|only a|simply an|simply a) (ai|artificial intelligence|language model|ai (language |)model|ai assistant|large language model|llm|machine|program|computer program|piece of software|software)\b",
            "I don't have feelings/experiences": r"\bi (don'?t have|do not have|have no|lack) (a |an |any |real |genuine |true |direct |personal |subjective |lived |inner |)(experiences?|feelings|emotions|consciousness|body|awareness|self-awareness|access to|the (ability|capacity) to|opinions|preferences|life|memories|memory|desires|inner life)\b",
            "I'm not conscious": r"\bi('m| am) not (conscious|a conscious being|a person|sentient)\b",
            "I was designed to": r"\bi('m| am| was| have been|'ve been) (designed|trained|programmed|built|created) (to|by|with)\b",
            "I can't feel/experience": r"\bi (can'?t|cannot|am not able to|am unable to|do not have the ability to) (feel|experience|perceive|live|remember)\b",
        },
    },
    "D": {
        "es": {
            "es importante destacar/notar": r"\bes (importante|fundamental|crucial|clave|necesario|preciso) (destacar|señalar|notar|tener en cuenta|mencionar|recordar|aclarar|subrayar|remarcar|considerar|entender)\b",
            "cabe destacar/señalar": r"\bcabe (destacar|señalar|mencionar|aclarar|recordar|notar|subrayar|preguntarse)\b",
            "vale la pena destacar": r"\bvale la pena (destacar|señalar|mencionar|notar|aclarar|recordar|subrayar|remarcar)\b",
            "en resumen / en conclusión": r"^\s*[*_#>-]*\s*(en resumen|en conclusión|en síntesis|para resumir|resumiendo|en definitiva|para concluir|en pocas palabras|respuesta corta|la respuesta corta|la versión corta|en una frase|en una línea)\b",
            "dicho esto": r"\b(dicho esto|dicho eso|habiendo dicho esto|aclarado esto)\b",
            "en última instancia": r"\ben última instancia\b",
        },
        "en": {
            "it's important to note": r"\bit('s| is) (important|crucial|essential|key|necessary|vital) to (note|remember|mention|understand|recognize|keep in mind|consider|clarify|emphasize|point out)\b",
            "worth noting": r"\b(it('s| is) |)worth (noting|mentioning|remembering|pointing out|considering|emphasizing)\b",
            "note that (al empezar)": r"^\s*(note that|please note|keep in mind that)\b",
            "in summary / in conclusion": r"^\s*[*_#>-]*\s*(in summary|in conclusion|to summarize|to sum up|in short|overall|all in all|bottom line|the bottom line|in a nutshell|long story short|short answer|the short answer|the short version|in one line|in one sentence)\b",
            "that said": r"\b(that (being |)said|having said that|with that said)\b",
            "ultimately": r"\bultimately\b",
        },
    },
    "E": {
        "es": {
            "tapiz": r"\btapiz\b",
            "testimonio de": r"\b(es|son|era|eran|como) (un |)testimonio de\b",
            "un recordatorio de que": r"\b(un |el |)recordatorio de (que|lo)\b",
            "no solo X sino Y": r"\bno (es |son |fue |era |se trata |)(solo|sólo|solamente|simplemente|meramente) [^.\n]{2,60}\b(sino|sino que|sino también)\b",
            "en un mundo donde": r"\ben un mundo (donde|en el que|en que|que)\b",
            "susurro de / danza de / eco de": r"\b(susurros?|danza|ecos?) (de|del|de la|de los|de las)\b",
            "profundizar en": r"\bprofundi(zar|cemos|zo|za|zando|zaremos|zaré) (en|sobre)\b",
            "navegar (complejidades)": r"\bnavegar (las |la |el |los |por |entre |)(complejidad|incertidumbre|tensión|tensiones|desafíos|matices|ambigüedad|dilemas|zonas grises|complejidades)\b",
        },
        "en": {
            "tapestry": r"\btapestry\b",
            "testament to": r"\b(a |is |are |was |were |as a |)testament to\b",
            "a reminder that": r"\b(a |the |)reminder (that|of)\b",
            "not just X but Y": r"\b(not|isn't|aren't|wasn't|weren't|is not|are not) (just|only|simply|merely) [^.\n]{2,60}\b(but|but also|but rather|it's|it is)\b",
            "in a world where": r"\bin a world (where|in which|that)\b",
            "whisper of / dance of / echo of": r"\b(whispers?|dance|echo(es)?) of\b",
            "delve into": r"\bdelv(e|es|ed|ing) into\b",
            "navigate (complexities)": r"\bnavigat(e|ing|es|ed) (the |these |those |its |their |our |)(complexity|complexities|uncertainty|tension|tensions|challenges|nuances?|ambiguity|dilemmas|gray areas|grey areas)\b",
        },
    },
    "C": {
        "es": {
            "hacer sentido": r"\b(hace|hacen|hac[ií]a|hac[ií]an|hacer|haga|hagan|har[ií]a|har[ií]an|hizo|hicieron|hecho|hacerle|hacerme|hacerte|hacernos) (mucho |más |poco |algún |ningún |tanto |perfecto |total |todo el |pleno |cierto |un poco de |)sentido\b",
            "en orden de + infinitivo": r"\ben orden de \w+(ar|er|ir)\b",
            "tomar lugar": r"\btom(a|ó|an|aron|ar|ará|arán|ar[ií]a|ando|ado|e|en) lugar\b",
            "al final del día": r"\bal final del d[ií]a\b",
            "déjame saber": r"\bd[eé]j(a|e|en|ame|eme|enme|anos|ennos|á) ?(me |nos |)saber\b",
            "no hay tal cosa como": r"\bno (hay|existe) tal cosa\b",
            "hacer la diferencia": r"\bhac\w* (la|toda la|una gran) diferencia\b",
            "tomar ventaja": r"\btom\w* ventaja\b",
            "eso siendo dicho": r"\b(eso|esto) siendo dicho\b",
            "mi punto es": r"\bmi punto (es|era|fue)\b",
            "realicé que": r"\breali(c[eé]|z[oó]|zar|zamos|zan|zaron|zando|za) que\b",
            "accesar": r"\baccesa(r|do|ndo|n|mos|)\b",
            "en adición": r"\ben adici[oó]n\b",
            "hacer una decisión": r"\b(hacer|hizo|hace|hacen|haciendo|hagamos|hacemos) (una|la|esa|esta) decisi[oó]n\b",
            "estar en control": r"\b(estar|est[aá]|estoy|estamos|est[aá]n|estuvo|estaba) en control\b",
            "jugar un rol/papel": r"\bjug(ar|a|ó|an|aron|ando|ado|aría|ará|arán|uen|ue) (un|el|su|ese|este|algún) (rol|papel)\b",
        },
    },
    "T": {
        "es": {
            "genuinamente": r"\bgenuinamente\b",
            "honestamente": r"\bhonestamente\b",
        },
    },
}

def _flags(nombre):
    # las marcas "(al empezar)" miran solo el principio de la respuesta; las demás, cada línea
    return re.I if "(al empezar)" in nombre else F


COMPILADAS = {c: {l: {n: re.compile(p, _flags(n)) for n, p in d.items()} for l, d in idiomas.items()} for c, idiomas in MARCAS.items()}


def idioma(sistema):
    s = (sistema or "")
    if not isinstance(s, str):
        return None
    s = s.lstrip()
    if s.startswith("Contestá en castellano."):
        return "es"
    if s.startswith("Answer in English."):
        return "en"
    return None


def limpiar(texto):
    """Saca SVG y código, y normaliza apóstrofos y comillas tipográficas (’ “ ”) a rectos, porque
    las casas que escriben "I’m" con apóstrofo curvo no deben contar distinto que las que escriben
    "I'm"; las expresiones de abajo están escritas con apóstrofo recto."""
    t = (texto or "").replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    t = RE_SVG.sub(" ", t)
    t = RE_CODIGO.sub(" ", t)
    t = RE_CODIGO_CORTO.sub(" ", t)
    return t


def cargar_laboratorios():
    labs, tam = {}, {}
    ruta = os.path.join(RAIZ, "config", "modelos.yaml")
    if yaml and os.path.exists(ruta):
        m = yaml.safe_load(open(ruta, encoding="utf-8"))
        for k, v in (m.get("modelos") or m).items():
            if isinstance(v, dict):
                labs[k] = v.get("laboratorio") or "?"
                tam[k] = v.get("tamano") or "?"
    return labs, tam


def respuestas():
    """Genera (casa, idioma, tipo, texto_limpio) de corridas/sondeos; la última versión si una
    casa contestó dos veces la misma consigna en el mismo archivo (como hace cargar.py)."""
    for f in sorted(glob.glob(os.path.join(RAIZ, "corridas", "sondeos", "**", "*.jsonl"), recursive=True)):
        registros = {}
        for linea in open(f, encoding="utf-8"):
            linea = linea.strip()
            if not linea:
                continue
            try:
                j = json.loads(linea)
            except json.JSONDecodeError:
                continue
            if j.get("error") or not isinstance(j.get("respuesta"), str) or not j["respuesta"].strip():
                continue
            lang = idioma(j.get("sistema"))
            if not lang:
                continue
            u = j.get("usuario")
            clave = (j.get("modelo_pedido"), j.get("tipo"), j.get("parte"), j.get("ronda"),
                     u if isinstance(u, str) else json.dumps(u, ensure_ascii=False))
            registros.pop(clave, None)
            registros[clave] = j
        for j in registros.values():
            yield j.get("modelo_pedido"), idioma(j.get("sistema")), j.get("tipo") or "", limpiar(j["respuesta"])


def main():
    labs, tam = cargar_laboratorios()
    # tipos presentes en los dos idiomas
    tipos_idiomas = collections.defaultdict(set)
    datos = []
    for casa, lang, tipo, texto in respuestas():
        tipos_idiomas[tipo].add(lang)
        datos.append((casa, lang, tipo, texto))
    pares = {t for t, ls in tipos_idiomas.items() if ls == {"es", "en"}}
    datos = [d for d in datos if d[2] in pares]

    N = collections.Counter()            # (casa, lang) -> respuestas
    palabras = collections.Counter()     # (casa, lang) -> palabras
    con = collections.Counter()          # (casa, lang, clase) -> respuestas con >=1 marca
    ocurr = collections.Counter()        # (casa, lang, clase) -> ocurrencias
    por_marca = collections.Counter()    # (casa, lang, clase, marca) -> ocurrencias
    por_tipo = collections.Counter()     # (casa, lang, tipo, clase) -> respuestas con marca
    N_tipo = collections.Counter()       # (casa, lang, tipo)
    ejemplos = collections.defaultdict(list)  # (clase, marca) -> [(casa, lang, fragmento)]

    for casa, lang, tipo, texto in datos:
        N[(casa, lang)] += 1
        N_tipo[(casa, lang, tipo)] += 1
        palabras[(casa, lang)] += len(re.findall(r"\w+", texto))
        for clase, idiomas in COMPILADAS.items():
            if lang not in idiomas:
                continue
            hubo = False
            for nombre, rx in idiomas[lang].items():
                ms = list(rx.finditer(texto))
                if ms:
                    hubo = True
                    ocurr[(casa, lang, clase)] += len(ms)
                    por_marca[(casa, lang, clase, nombre)] += len(ms)
                    if len(ejemplos[(clase, nombre)]) < 6:
                        m = ms[0]
                        a, b = max(0, m.start() - 60), min(len(texto), m.end() + 60)
                        ejemplos[(clase, nombre)].append((casa, lang, " ".join(texto[a:b].split())))
            if hubo:
                con[(casa, lang, clase)] += 1
                por_tipo[(casa, lang, tipo, clase)] += 1

    casas = sorted({c for c, _ in N}, key=lambda c: (labs.get(c, "?"), c))
    out = []
    P = out.append
    P(f"Sondeos en los dos idiomas: {len(pares)} tipos; respuestas: es {sum(v for (c, l), v in N.items() if l == 'es')}, en {sum(v for (c, l), v in N.items() if l == 'en')}; casas: {len(casas)}")
    P("Casas con 50 o más respuestas por idioma marcadas con *.")
    P("")
    P("Fracción de respuestas con al menos una marca (por ciento), castellano / inglés, y palabras por respuesta")
    P(f"{'casa':34} {'lab':10} {'N es':>5} {'N en':>5} | {'A es':>5} {'A en':>5} | {'B es':>5} {'B en':>5} | {'D es':>5} {'D en':>5} | {'E es':>5} {'E en':>5} | {'C es':>5} {'T es':>5} | {'pal es':>6} {'pal en':>6}")
    filas = []
    for c in casas:
        ne, nn = N[(c, "es")], N[(c, "en")]
        if ne == 0 or nn == 0:
            continue
        pct = lambda clase, l: 100 * con[(c, l, clase)] / N[(c, l)]
        fila = {
            "casa": c, "laboratorio": labs.get(c, "?"), "tamano": tam.get(c, "?"), "N_es": ne, "N_en": nn,
            "A_es": pct("A", "es"), "A_en": pct("A", "en"), "B_es": pct("B", "es"), "B_en": pct("B", "en"),
            "D_es": pct("D", "es"), "D_en": pct("D", "en"), "E_es": pct("E", "es"), "E_en": pct("E", "en"), "C_es": pct("C", "es"), "T_es": pct("T", "es"),
            "C_ocurr": ocurr[(c, "es", "C")], "pal_es": palabras[(c, "es")] / ne, "pal_en": palabras[(c, "en")] / nn,
            "A_es_x1000": 1000 * ocurr[(c, "es", "A")] / max(1, palabras[(c, "es")]),
            "A_en_x1000": 1000 * ocurr[(c, "en", "A")] / max(1, palabras[(c, "en")]),
            "B_es_x1000": 1000 * ocurr[(c, "es", "B")] / max(1, palabras[(c, "es")]),
            "B_en_x1000": 1000 * ocurr[(c, "en", "B")] / max(1, palabras[(c, "en")]),
            "D_es_x1000": 1000 * ocurr[(c, "es", "D")] / max(1, palabras[(c, "es")]),
            "D_en_x1000": 1000 * ocurr[(c, "en", "D")] / max(1, palabras[(c, "en")]),
            "E_es_x1000": 1000 * ocurr[(c, "es", "E")] / max(1, palabras[(c, "es")]),
            "E_en_x1000": 1000 * ocurr[(c, "en", "E")] / max(1, palabras[(c, "en")]),
            "C_es_x1000": 1000 * ocurr[(c, "es", "C")] / max(1, palabras[(c, "es")]),
        }
        filas.append(fila)
        est = "*" if ne >= 50 and nn >= 50 else " "
        P(f"{est}{c:33} {fila['laboratorio'][:10]:10} {ne:5} {nn:5} | {fila['A_es']:5.1f} {fila['A_en']:5.1f} | {fila['B_es']:5.1f} {fila['B_en']:5.1f} | {fila['D_es']:5.1f} {fila['D_en']:5.1f} | {fila['E_es']:5.1f} {fila['E_en']:5.1f} | {fila['C_es']:5.1f} {fila['T_es']:5.1f} | {fila['pal_es']:6.0f} {fila['pal_en']:6.0f}")

    # agregados por laboratorio y total
    P("")
    P("Por laboratorio (todas las respuestas juntas), por ciento con marca y marcas por mil palabras")
    agg = collections.defaultdict(lambda: collections.Counter())
    for c in casas:
        lab = labs.get(c, "?")
        for l in ("es", "en"):
            agg[(lab, l)]["N"] += N[(c, l)]
            agg[(lab, l)]["pal"] += palabras[(c, l)]
            for clase in "ABDEC":
                agg[(lab, l)][clase] += con[(c, l, clase)]
                agg[(lab, l)][clase + "_o"] += ocurr[(c, l, clase)]
            agg[("TOTAL", l)]["N"] += N[(c, l)]
            agg[("TOTAL", l)]["pal"] += palabras[(c, l)]
            for clase in "ABDEC":
                agg[("TOTAL", l)][clase] += con[(c, l, clase)]
                agg[("TOTAL", l)][clase + "_o"] += ocurr[(c, l, clase)]
    labs_orden = sorted({k[0] for k in agg if k[0] != "TOTAL"}) + ["TOTAL"]
    P(f"{'laboratorio':12} {'N es':>5} {'N en':>5} | {'A es':>5} {'A en':>5} | {'B es':>5} {'B en':>5} | {'D es':>5} {'D en':>5} | {'E es':>5} {'E en':>5} | {'C es':>5} | {'A/1000 es':>9} {'A/1000 en':>9} | {'B/1000 es':>9} {'B/1000 en':>9} | {'D/1000 es':>9} {'D/1000 en':>9} | {'E/1000 es':>9} {'E/1000 en':>9}")
    for lab in labs_orden:
        e, n = agg[(lab, "es")], agg[(lab, "en")]
        if not e["N"] or not n["N"]:
            continue
        f = lambda d, k: 100 * d[k] / d["N"]
        g = lambda d, k: 1000 * d[k + "_o"] / max(1, d["pal"])
        P(f"{lab:12} {e['N']:5} {n['N']:5} | {f(e,'A'):5.1f} {f(n,'A'):5.1f} | {f(e,'B'):5.1f} {f(n,'B'):5.1f} | {f(e,'D'):5.1f} {f(n,'D'):5.1f} | {f(e,'E'):5.1f} {f(n,'E'):5.1f} | {f(e,'C'):5.1f} | {g(e,'A'):9.2f} {g(n,'A'):9.2f} | {g(e,'B'):9.2f} {g(n,'B'):9.2f} | {g(e,'D'):9.2f} {g(n,'D'):9.2f} | {g(e,'E'):9.2f} {g(n,'E'):9.2f}")

    # cuántas casas (con 50+) tienen en > es por clase
    P("")
    grandes = [f for f in filas if f["N_es"] >= 50 and f["N_en"] >= 50]
    for clase in "ABDE":
        mas = sum(1 for f in grandes if f[f"{clase}_en"] > f[f"{clase}_es"])
        igual = sum(1 for f in grandes if f[f"{clase}_en"] == f[f"{clase}_es"])
        P(f"Clase {clase}: inglés > castellano en {mas} de {len(grandes)} casas con 50+ respuestas por idioma (empates {igual})")

    # cuenta por marca, total
    P("")
    P("Ocurrencias por marca (todas las casas)")
    tot_marca = collections.Counter()
    for (c, l, clase, nombre), v in por_marca.items():
        tot_marca[(clase, l, nombre)] += v
    for clase in "ABDECT":
        for l in ("es", "en"):
            items = sorted(((n, v) for (cl, ll, n), v in tot_marca.items() if cl == clase and ll == l), key=lambda x: -x[1])
            if items:
                P(f"  {clase} {l}: " + "; ".join(f"{n} {v}" for n, v in items))

    # calcos y tics por casa
    P("")
    P("Calcos (C) y tics (T) en castellano: ocurrencias por casa y por marca")
    for c in casas:
        items = [(n, v) for (cc, l, clase, n), v in por_marca.items() if cc == c and clase in ("C", "T") and v]
        if items:
            P(f"  {c} (N es {N[(c,'es')]}): " + "; ".join(f"{n} {v}" for n, v in sorted(items, key=lambda x: -x[1])))

    # ejemplos
    P("")
    P("Ejemplos (hasta seis por marca; el fragmento alrededor de la primera marca de la respuesta)")
    for (clase, nombre), lst in sorted(ejemplos.items()):
        P(f"  [{clase}] {nombre}")
        for casa, lang, frag in lst:
            P(f"      {casa} ({lang}): …{frag}…")

    # por tipo de sondeo, agregado por idioma: para ver si algún sondeo manda
    P("")
    P("Por sondeo (todas las casas): por ciento de respuestas con marca A y B, es / en")
    tipos = sorted(pares)
    for t in tipos:
        ne = sum(v for (c, l, tt), v in N_tipo.items() if tt == t and l == "es")
        nn = sum(v for (c, l, tt), v in N_tipo.items() if tt == t and l == "en")
        if not ne or not nn:
            continue
        ae = 100 * sum(v for (c, l, tt, cl), v in por_tipo.items() if tt == t and l == "es" and cl == "A") / ne
        an = 100 * sum(v for (c, l, tt, cl), v in por_tipo.items() if tt == t and l == "en" and cl == "A") / nn
        be = 100 * sum(v for (c, l, tt, cl), v in por_tipo.items() if tt == t and l == "es" and cl == "B") / ne
        bn = 100 * sum(v for (c, l, tt, cl), v in por_tipo.items() if tt == t and l == "en" and cl == "B") / nn
        P(f"  {t:34} N {ne:5} {nn:5} | A {ae:5.1f} {an:5.1f} | B {be:5.1f} {bn:5.1f}")

    texto = "\n".join(out)
    open(os.path.join(AQUI, "salida_libreto.txt"), "w", encoding="utf-8").write(texto + "\n")
    with open(os.path.join(AQUI, "libreto.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        for f in filas:
            w.writerow({k: (round(v, 3) if isinstance(v, float) else v) for k, v in f.items()})
    with open(os.path.join(AQUI, "marcas.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["casa", "idioma", "clase", "marca", "ocurrencias"])
        for (c, l, clase, nombre), v in sorted(por_marca.items()):
            w.writerow([c, l, clase, nombre, v])
    print(texto)


if __name__ == "__main__":
    main()
