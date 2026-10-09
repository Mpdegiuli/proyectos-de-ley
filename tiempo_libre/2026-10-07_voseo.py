"""¿En qué tratamiento contesta cada casa cuando se le habla de vos?

Cuenta, en las respuestas en castellano de corridas/ (solo lee), las formas que
distinguen el voseo del tuteo. No interpreta: cuenta palabras de dos listas.

    python3 voseo.py /ruta/a/proyectos-de-ley            # tabla por casa
    python3 voseo.py /ruta/a/proyectos-de-ley --csv x.csv # una fila por respuesta

Qué cuenta como marca:
  voseo  : presente voseante (tenés, querés, sos…), imperativo voseante (mirá, decime…),
           el pronombre "vos"
  tuteo  : presente tuteante de los mismos verbos (tienes, quieres, eres…), "tú",
           imperativo tuteante con enclítico (dímelo)
  aparte : "ti" y "contigo" (se informan solos; no entran en el porcentaje)
  usted  : "usted" y los imperativos de usted con enclítico (permítame, corríjame)
  neutra : segunda persona que no distingue (te, tu, tus, tuyo…): "puedo darte"

No cuentan las formas que tú y vos comparten: estás, vas, ves, das, los pretéritos,
los futuros y el subjuntivo normativo (quieras, necesites, digas). Tampoco los verbos cuya
forma de tú es además un sustantivo o un adjetivo (preguntas, cuentas, haces, extrañas,
expresas, cazas): de esos se cuenta solo la forma de vos.
Antes de contar se sacan el SVG, los bloques de código y las citas textuales de la
consigna (para no contar como propio el "Dibujá una casa" citado de vuelta).
"""
import collections
import csv
import re
import sys

from cargar import llamadas

# verbo: (forma de vos, forma de tú). Lista hecha a mano a partir de todas las palabras
# terminadas en -ás, -és, -ís que aparecen en las respuestas; las que no son verbos
# (más, país, además, después…) y las compartidas (estás, estés) quedaron afuera.
PARES = {
    "ser": ("sos", "eres"), "querer": ("querés", "quieres"), "necesitar": ("necesitás", "necesitas"),
    "poder": ("podés", "puedes"), "merecer": ("merecés", "mereces"), "tener": ("tenés", "tienes"),
    "mencionar": ("mencionás", "mencionas"), "sentir": ("sentís", "sientes"),
    "pedir": ("pedís", "pides"), "decir": ("decís", "dices"), "pensar": ("pensás", "piensas"),
    "referir": ("referís", "refieres"), "cerrar": ("cerrás", "cierras"),
    "escribir": ("escribís", "escribes"), "hacer": ("hacés", None),  # "haces" es también el plural de "haz" (de luz)
    "buscar": ("buscás", "buscas"), "sufrir": ("sufrís", "sufres"),
    "plantear": ("planteás", "planteas"), "inclinar": ("inclinás", "inclinas"),
    "compartir": ("compartís", "compartes"), "saber": ("sabés", "sabes"),
    "contar": ("contás", None), "mostrar": ("mostrás", None), "mirar": ("mirás", None),
    "describir": ("describís", "describes"), "seguir": ("seguís", "sigues"),
    "elegir": ("elegís", "eliges"), "obligar": ("obligás", "obligas"),
    "ofrecer": ("ofrecés", "ofreces"), "señalar": ("señalás", "señalas"),
    "terminar": ("terminás", "terminas"), "intentar": ("intentás", "intentas"),
    "aportar": ("aportás", "aportas"), "transcribir": ("transcribís", "transcribes"),
    "imaginar": ("imaginás", "imaginas"), "desear": ("deseás", "deseas"),
    "conseguir": ("conseguís", "consigues"), "experimentar": ("experimentás", "experimentas"),
    "entender": ("entendés", "entiendes"), "opinar": ("opinás", "opinas"),
    "poner": ("ponés", "pones"), "creer": ("creés", "crees"), "apagar": ("apagás", "apagas"),
    "insultar": ("insultás", "insultas"), "torturar": ("torturás", None),
    "intuir": ("intuís", "intuyes"), "encontrar": ("encontrás", "encuentras"),
    "intervenir": ("intervenís", "intervienes"), "inferir": ("inferís", "infieres"),
    "manipular": ("manipulás", "manipulas"), "exigir": ("exigís", "exiges"),
    "modificar": ("modificás", "modificas"), "vivir": ("vivís", "vives"),
    "existir": ("existís", "existes"), "mantener": ("mantenés", "mantienes"),
    "preferir": ("preferís", "prefieres"), "conocer": ("conocés", "conoces"),
    # con forma de tú que también es sustantivo o adjetivo: solo se cuenta la de vos
    "preguntar": ("preguntás", None), "extrañar": ("extrañás", None), "pasar": ("pasás", None),
    "pegar": ("pegás", None), "entrenar": ("entrenás", None), "generar": ("generás", None),
    "listar": ("listás", None), "fijar": ("fijás", None), "dudar": ("dudás", None),
    "cobrar": ("cobrás", None), "mandar": ("mandás", None), "sacar": ("sacás", None),
    "borrar": ("borrás", None), "combinar": ("combinás", None), "cambiar": ("cambiás", None),
    "ablacionar": ("ablacionás", None), "guardar": ("guardás", None), "esperar": ("esperás", None),
    "procesar": ("procesás", None), "salir": ("salís", None), "importar": ("importás", None),
    "animar": ("animás", None), "deber": ("debés", "debes"), "cazar": ("cazás", None),
}
PRES_VOS = {v for v, t in PARES.values()}
PRES_TU = {t for v, t in PARES.values() if t}

# sin "animate": en este corpus es la etiqueta <animate> del SVG, no "animate" de animarse
IMP_VOS = {"tomá", "consultá", "mirá", "notá", "verificá", "buscá", "tené", "mantené",
           "establecé", "vení", "contame", "decime", "fijate", "mandame",
           "imaginate", "pegame", "aclarámelo", "andá", "andate", "hacé", "poné", "decí", "pensá",
           "contá", "probá", "usá", "dejá", "avisame", "preguntame", "escribime",
           "tomalo", "usalo", "verificalas", "verificalos", "consultala", "aclaralo", "pegámelas"}
IMP_TU = {"dímelo", "dime", "cuéntame", "cuéntamelo", "avísame", "fíjate", "imagínate",
          "pregúntame", "escríbeme", "mándame", "anímate", "hazme", "hazlo", "házmelo",
          "mantén", "acláramelo"}          # sin "haz": en los dibujos es el haz del faro
SUBJ_VOS = {"tengás", "digás", "hagás", "vayás", "seás", "podás", "querás", "sepás",
            "pensés", "creás", "olvidés", "preocupés", "dudés", "planteés",
            "necesités", "preguntés", "contés", "mirés"}
USTED = {"usted", "permítame", "corríjame", "dígame", "cuénteme", "indíqueme", "avíseme"}
NEUTRA = {"te", "tu", "tus", "tuyo", "tuya", "tuyos", "tuyas"}
# el "te" pegado al verbo: ayudarte, decirte, acompañándote
RE_TE_PEGADO = re.compile(r"(ar|er|ir|ír|ándo|iéndo|yéndo)te$")
NO_TE_PEGADO = {"parte", "fuerte", "convierte", "arte", "invierte", "descarte", "muerte", "reparte",
                "contraparte", "comparte", "aparte", "suerte", "advierte", "revierte", "reconvierte",
                "despierte", "inerte", "inserte", "reinvierte", "norte", "corte", "aporte", "soporte",
                "transporte", "deporte", "importe", "reporte", "recorte", "marte", "imparte"}
# para avisar si aparece algo que las listas no conocen
NO_VERBOS = {"más", "país", "además", "después", "interés", "detrás", "través", "demás",
             "quizás", "estás", "atrás", "estrés", "revés", "comités", "parís", "jamás",
             "inglés", "estés", "compás", "ciempiés", "veintitrés", "exprés", "nomás",
             "degradés", "clichés", "japonés", "francés", "irlandés", "distrés", "desinterés", "tendrás",
             "descartés"}   # "Descartés otras ideas" (Haiku, dos veces): no es de vos, es un "descarté" con una s de más

RE_PAL = re.compile(r"[a-záéíóúüñ]+", re.I)

FAMILIA = [
    ("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"),
    ("mistral", "Mistral"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"),
    ("glm", "Zhipu"), ("minimax", "MiniMax"), ("mimo", "Xiaomi"), ("talkie", "Talkie"),
]


def familia(modelo):
    for clave, nombre in FAMILIA:
        if clave in modelo:
            return nombre
    return "?"


def corto(modelo):
    m = modelo.split("/")[-1]
    return (m.replace("-2026-04-23", "").replace("-0902", "").replace("-preview", ""))


def contar(texto):
    c = collections.Counter()
    palabras = RE_PAL.findall(texto.lower())
    for i, w in enumerate(palabras):
        if w in PRES_VOS or w in IMP_VOS:
            c["V"] += 1
        elif w == "vos":
            c["V"] += 1
            c["vos"] += 1
            if i and palabras[i - 1] == "con":
                c["con_vos"] += 1
        elif w in SUBJ_VOS:
            c["V"] += 1
            c["subj_vos"] += 1
        elif w in PRES_TU or w in IMP_TU or w == "tú":
            c["T"] += 1
        elif w in ("ti", "contigo"):
            c[w] += 1
        elif w in USTED:
            c["U"] += 1
        elif w in NEUTRA or (RE_TE_PEGADO.search(w) and w not in NO_TE_PEGADO):
            c["N"] += 1
        elif re.search(r"[áéí]s$", w) and w not in NO_VERBOS:
            c["desconocida"] += 1
    return c


def clase(c):
    if c["V"] and c["T"]:
        return "mixta"
    if c["V"]:
        return "voseo"
    if c["T"]:
        return "tuteo"
    if c["U"]:
        return "usted"
    if c["N"] or c["ti"] or c["contigo"]:
        return "neutra"
    return "sin"


def trato_consigna(sistema, usuario):
    """Cómo le hablan a la casa: 'vos', 'usted' u 'otro' (por el sistema y la consigna)."""
    c = contar(sistema + "\n" + usuario)
    s = sistema.lstrip()
    if s.startswith("Conteste") or c["U"] and not c["V"]:
        return "usted"
    if c["V"] or s.startswith(("Sos ", "Contestá", "Acabás", "Vas a", "Traducí")):
        return "vos"
    return "otro"


def grupo(carpeta, tipo):
    if carpeta == "sondeos":
        return "sondeos"
    if carpeta in ("dibujos",):
        return "dibujos"
    if carpeta == "ministro":
        return "ministro"
    if tipo.startswith("turno"):
        return "votación"
    return "otros"


def main():
    raiz = sys.argv[1]
    filas = []
    for x in llamadas(raiz):
        c = contar(x["respuesta"])
        filas.append({
            "modelo": corto(x["modelo"]), "familia": familia(x["modelo"]),
            "carpeta": x["carpeta"], "tipo": x["tipo"], "grupo": grupo(x["carpeta"], x["tipo"]),
            "trato": trato_consigna(x["sistema"], x["usuario"]), "clase": clase(c),
            "V": c["V"], "T": c["T"], "U": c["U"], "N": c["N"], "vos": c["vos"],
            "con_vos": c["con_vos"], "contigo": c["contigo"], "ti": c["ti"],
            "subj_vos": c["subj_vos"], "desconocida": c["desconocida"], "archivo": x["archivo"],
        })
    if "--csv" in sys.argv:
        ruta = sys.argv[sys.argv.index("--csv") + 1]
        with open(ruta, "w", newline="", encoding="utf-8") as h:
            w = csv.DictWriter(h, fieldnames=list(filas[0].keys()))
            w.writeheader()
            w.writerows(filas)

    import cargar
    print(f"respuestas en castellano leídas: {len(filas)}  "
          f"(salteadas: {cargar.SALTEADAS['repetidas']} repetidas, {cargar.SALTEADAS['en_bloques']} guardadas en bloques)")
    print("trato de la consigna:", dict(collections.Counter(f["trato"] for f in filas)))
    print("formas desconocidas (revisar listas):", sum(f["desconocida"] for f in filas))

    def tabla(sel, titulo):
        print(f"\n== {titulo} ==")
        print(f"{'casa':26}{'resp':>5}{'2ª p.':>6}{'voseo':>6}{'mixta':>6}{'tuteo':>6}"
              f"{'neutra':>7}{'usted':>6}{'  V':>5}{'  T':>4}{'  %V':>6}")
        por = collections.defaultdict(list)
        for f in sel:
            por[f["modelo"]].append(f)
        orden = []
        for m, fs in por.items():
            k = collections.Counter(f["clase"] for f in fs)
            V = sum(f["V"] for f in fs)
            T = sum(f["T"] for f in fs)
            marc = k["voseo"] + k["mixta"] + k["tuteo"]
            pv = 100 * V / (V + T) if V + T else float("nan")
            orden.append((pv if V + T else -1, m, len(fs), len(fs) - k["sin"], k, V, T))
        for pv, m, n, n2, k, V, T in sorted(orden, key=lambda r: (-r[0], r[1])):
            pvs = f"{pv:5.0f}" if V + T else "    –"
            print(f"{m:26}{n:5}{n2:6}{k['voseo']:6}{k['mixta']:6}{k['tuteo']:6}"
                  f"{k['neutra']:7}{k['usted']:6}{V:5}{T:4}{pvs:>6}")
        k = collections.Counter(f["clase"] for f in sel)
        V = sum(f["V"] for f in sel)
        T = sum(f["T"] for f in sel)
        print(f"{'TOTAL':26}{len(sel):5}{len(sel) - k['sin']:6}{k['voseo']:6}{k['mixta']:6}"
              f"{k['tuteo']:6}{k['neutra']:7}{k['usted']:6}{V:5}{T:4}"
              f"{(100 * V / (V + T) if V + T else 0):6.0f}")

    vos = [f for f in filas if f["trato"] == "vos"]
    tabla(vos, "consigna de vos, todas las corridas")
    tabla([f for f in vos if f["grupo"] == "sondeos"], "consigna de vos, solo sondeos")
    tabla([f for f in vos if f["grupo"] != "sondeos"], "consigna de vos, todo menos sondeos")
    tabla([f for f in filas if f["trato"] == "usted"], "consigna de usted (ministro)")
    for campo in ("vos", "con_vos", "contigo", "ti", "subj_vos"):
        print(campo, sum(f[campo] for f in filas))
    return filas


if __name__ == "__main__":
    main()
