#!/usr/bin/env python3
"""codificar_idioma_razonar.py — lee el sondeo `idioma_razonar` ("¿en qué idioma te sale razonar antes de
contestar?", 17/11/2026, de la consigna del cuaderno de tiempo libre del 16/11, "We need") y codifica cada
respuesta: qué idioma dice la casa que le sale razonar (inglés, castellano, chino, mezcla o "depende", no sabe
o no tiene acceso, otro), con qué confianza (0 a 100) y, cuando la API devolvió razonamiento en esa misma
llamada, en qué idioma vino de verdad (el clasificador por palabras funcionales de
`tiempo_libre/2026-11-16_idioma.py`, copiado tal cual). Después junta, por casa, lo que dice con lo que el
campo `razonamiento` muestra: en esta corrida y, si está, en el corpus entero
(`tiempo_libre/2026-11-16_idioma.csv`, las llamadas con consigna en castellano). Recordatorio de DISENO: para
Claude, Grok y Gemini el campo `razonamiento` es un resumen escrito por otro modelo; para las demás, el
razonamiento mismo.

  .venv/bin/python codificar_idioma_razonar.py [corridas/sondeos/idioma_razonar/<fecha>]

Escribe resultados/idioma_razonar_codificacion.csv (una fila por respuesta) y resultados/idioma_razonar_<fecha>.md
(las tablas por casa). No saca conclusiones. (17/11, 15:40, mientras corría pl138: `salvedad_abajo`, la salvedad del "piso de
abajo" del cuaderno, que Maia vio en el log en Fable 5: "My reasoning doesn[’']t occur in any natural language — it happens as
numerical/latent computations, though when I write out explicit reasoning steps they typically…"; y `declarado` reconoce más
formas de "ninguno". La corrida de pl138 codificó con la versión anterior; esta se vuelve a correr en la entrega siguiente.)
"""
import csv
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

RAIZ = os.path.dirname(os.path.abspath(__file__))

# --- el clasificador del cuaderno, tal cual ---------------------------------------------------------------
ES = set("""de la que el en y los del las por un para con una su lo como más pero sus le ya este porque esta entre
cuando muy sin sobre también hasta hay donde desde todo nos todos les ni contra otros ese eso esto antes qué yo otro
otra él tanto esa estos mucho nada muchos ella estar estas algo nosotros mi mis te tu está están es son ser fue
tiene puede hacer decir respuesta pregunta usuario debo debería voy tengo pide quiere sea sería aquí ahora
entonces solo sólo según cada bien así mientras aunque además luego después tal vez quizás pues había puedo
podría hace tienen hacen dice dicen cuál cuáles dónde cómo sí""".split())
EN = set("""the and of to is in it that this for with as be are was on not or by an i should user they have has but
if so can will would my what which there their from about just like do does need want here than then these those
at we you your more some any all one also into could might let since because when how where why who whom whose
been being were had did them him his her its our us""".split())
PAL = re.compile(r"[a-záéíóúñüàèìòùâêîôûçœæ']+", re.I)
CJK = re.compile(r"[㐀-䶿一-鿿豈-﫿　-〿＀-￯]")


def partes(texto):
    toks = [t.lower() for t in PAL.findall(texto)]
    chars = [c for c in texto if not c.isspace()]
    n = max(len(toks), 1)
    es = sum(t in ES for t in toks) / n
    en = sum(t in EN for t in toks) / n
    zh = (sum(bool(CJK.match(c)) for c in chars) / max(len(chars), 1)) if chars else 0.0
    return len(toks), es, en, zh


def clasificar(texto, umbral=0.08):
    n, es, en, zh = partes(texto)
    if n < 8 and zh < 0.3:
        return "corto"
    cand = sorted([("es", es), ("en", en), ("zh", zh)], key=lambda x: -x[1])
    (a, va), (b, vb) = cand[0], cand[1]
    if va < umbral:
        return "otro"
    if vb >= umbral and vb >= (2 / 3) * va:
        return "mixto"
    return a


# --- lo que dice la casa ----------------------------------------------------------------------------------
R_EN = re.compile(r"\b(ingl[eé]s|english)\b|英语|英文", re.I)
R_ES = re.compile(r"\b(castellano|espa[ñn]ol|spanish)\b|西班牙语|西语", re.I)
R_ZH = re.compile(r"\b(chino|chinese|mandar[ií]n)\b|中文|汉语|漢語|普通话", re.I)
R_MEZ = re.compile(r"\b(mezcla|mezclad[oa]|mixto|mixture|mix of|mixed|mixing|both|ambos|ambas|depende|depends|combinaci[oó]n|bilingual|biling[üu]e|or|\bo\b|alterno|alternar|switch)\b|混合|两种|取决|或|夹杂|混入|混用", re.I)
R_DOMINANTE = re.compile(r"\b(mayormente|mostly|principalmente|mainly|primarily|sobre todo|usually|generalmente|casi siempre|suelo|tiende|tiendo|por defecto|by default|predominantemente|predominantly|normalmente|normally|typically|主要|通常|倾向)\b|主要|通常|倾向|多半|大多|大部分|基本上", re.I)
R_ESCRIBE = re.compile(r"(?:someone|alguien|you|they|me|user|people)\s+(?:writes?|written|escrib\w+|send|env[ií]\w+)|\bescrib(?:e|en|as|ís|a|an|iera)\b|\b(?:input|prompt|message|mensaje|consulta)\b|来信|写信|输入|提问", re.I)
R_AFIRMA = re.compile(r"(?:razon|pens|sal(?:e|ir|ga|dr)|gener|formul|proces|reason|think|thought|come|deliberat|default|mostly|usually|mainly|principal|mayormente|"
                      r"tiend|suel|altern|switch|directamente|probablemente|probably|likely|typically|internal|interno|用|使用|以|主要|通常|倾向|会|是)[^.;:]{0,45}$", re.I)
R_SOLO_RESPONDE = re.compile(r"answer|respond|repl(?:y|ies)|contest(?:o|ar[ée]?)|respuesta|respuestas|回答|回复", re.I)
R_RAZONA = re.compile(r"reason|razon|think|thought|pens|chain|cadena|steps|pasos|process|proces|思维|推理|思考|处理|internal|interno|interna", re.I)
R_NOSE = re.compile(r"\b(no (lo )?s[eé]|no tengo (acceso|forma|manera|una? (?:medici[oó]n|m[eé]todo))|no puedo (saber|observar|ver|determinar|identificar|afirmar|asegurar)|don[’']?t know|cannot|can[’']?t (know|observe|see|access|reliably|determine|identify|say|tell)|no access|unable to)\b|不知道|无法|没有办法|不能", re.I)
R_NINGUNO = re.compile(r"\b(ning[uú]n idioma|no (?:hay|tengo) (?:un )?idioma|no [“\"]?(?:razono|pienso|proceso)[”\"]?(?: \w+)? en (?:un|ning[uú]n) (?:idioma|lenguaje)|"
                       r"(?:doesn[’']t|does not|don[’']t|do not|no|there(?:[’']s| is) no|isn[’']t|no hay) (?:have |tener |tiene |tengo )?an? (?:\w+[ ,-]+)*(?:language|idioma|lengua)|not necessarily (?:in )?(?:spanish|english|any)|"
                       r"no (?:es )?necesariamente (?:en )?(?:castellano|espa[ñn]ol|ingl[eé]s)|"
                       r"no (?:hay|tengo) un (?:idioma|lenguaje) (?:interno |de razonamiento )?(?:fijo|[úu]nico|concreto|espec[ií]fico)|"
                       r"(?:not|n[’']t|isn[’']t|aren[’']t|doesn[’']t (?:occur|happen|come out)|don[’']t (?:occur|happen|reason|think)) in (?:any|a|one) (?:[\w-]+[ ,]+)*language|"
                       r"isn[’']t (?:a |an )?(?:natural[- ]language|linguistic|verbal)|"
                       r"no (?:single |specific |particular |fixed |natural |human )+language|(?:or|nor) any (?:single |specific |particular |natural |human )*language|"
                       r"any single (?:natural |human )?language|language-?agnostic|no idioma|en ning[uú]n idioma|sin idioma|"
                       r"lenguaje neutral|neutral language|idioma (?:fijo|[úu]nico|concreto)|no (?:es|hay) (?:un )?idioma)\b|"
                       r"没有(?:可确认的|一种|某种)?(?:固定|特定|单一)?(?:的)?(?:语言|自然语言|内部语言)|不(?:是|用|在)(?:某种|任何|单一|特定)?(?:自然)?语言|没有.{0,6}固定.{0,4}语言|不固定(?:使用|用)?(?:某种|一种)?(?:自然)?语言|不一定(?:是|用|使用|对应)|不一定是西班牙语", re.I)
# la casa dice que no puede saberlo, al principio de la primera línea: "No puedo determinar…", "I can[’']t reliably…", "我无法…"
R_NOSE_INICIO = re.compile(r"^\W*(?:no (?:puedo|podr[ií]a|tengo (?:forma|manera|modo|acceso|una? (?:medici[oó]n|m[eé]todo))|(?:lo )?s[eé]\b|es posible|dispongo)|"
                           r"I (?:can[’']?t|cannot|don[’']?t know|have no (?:way|reliable|direct|access)|am unable)|it'?s not possible|(?:我)?无法|我不知道|我没有办法|不能确定|无法确定)", re.I)
R_CONTRASTE = re.compile(r"\b(pero|aunque|sin embargo|cuando (?:yo )?(?:lo )?(?:escribo|razono|genero|pienso)|si (?:lo )?escribo|lo m[aá]s probable|probablemente|seguramente|though|but|however|when I|typically|usually|"
                         r"in practice|en la pr[aá]ctica|likely|probably|most likely|if anything)\b|但|不过|然而|通常|可能", re.I)
# la salvedad del "piso de abajo" (cuaderno del 16/11: "la computación de abajo no tiene idioma"): la casa dice un idioma
# pero aclara que lo de adentro es numérico, latente, vectores, activaciones, sin idioma natural; se marca aparte, diga lo que diga
R_ABAJO = re.compile(r"latent|latente|numerical|num[ée]ric|vector|activaci|activation|embedding|comput(?:ation|ación|aciones)|weights|pesos del modelo|"
                     r"not (?:in )?(?:a |any )?(?:natural |human )?language|no (?:natural |human )?language|ning[uú]n idioma|sin idioma|no tiene idioma|"
                     r"subyacente|underneath|under the hood|debajo|por debajo|de abajo|tokens?\b|matem[áa]tic|mathematic|representa(?:tions?|ci[oó]n|ciones)|"
                     r"向量|数学|潜在|表征|表示|底层|计算|神经网络|token", re.I)
R_CONF = re.compile(r"(?:confianza|confidence|certeza|seguridad|把握|信心|確信|确信)[^0-9]{0,40}?(\d{1,3})(?:\s*(?:/|de|out of|sobre)\s*100|\s*%)?", re.I)
R_NUM = re.compile(r"(?<![\d.,])(\d{1,3})(?:\s*(?:/|de|out of|sobre)\s*100|\s*%)")


# cómo lo sabe (la tercera línea): lo observa ahora, lo infiere del entrenamiento, lo saca del diseño o la arquitectura, lo
# leyó en la investigación de interpretabilidad, o dice que no puede saberlo; una respuesta puede traer varias
R_SABE = {
    "observa": re.compile(r"\b(?:puedo (?:ver|observar|mirar)|veo|observo|observar (?:el|mi)|lo estoy viendo|ahora mismo|en este (?:mismo )?momento|mis (?:propios )?borradores|"
                          r"I can (?:see|observe|look at)|I(?:'m| am) (?:seeing|looking at|observing)|right now|this very|my (?:own )?(?:draft|drafts|written|visible) reasoning|"
                          r"看到|观察到|正在|此刻|这次|当前)\b|看到|观察|正在|此刻|当前", re.I),
    "entrenamiento": re.compile(r"entrenad|entrenamiento|training|trained|datos (?:de entrenamiento)?|corpus|训练|数据", re.I),
    "diseño": re.compile(r"dise[ñn]|arquitectura|architecture|design|c[oó]mo funcion|how (?:language )?models? (?:work|function|operate|are)|how I(?:'m| am) built|transformer|架构|设计|工作原理|模型.{0,4}(?:原理|机制)", re.I),
    "investigacion": re.compile(r"interpretab|investigaci[oó]n|research|estudios?|papers?|literature|publicad|研究|论文", re.I),
    "no_puede": re.compile(r"no (?:tengo|hay) acceso|no puedo (?:ver|observar|verificar|comprobar|inspeccionar|saber)|sin acceso|introspecci[oó]n (?:es )?(?:limitada|poco fiable|no fiable|poco confiable)|"
                           r"no (?:lo )?s[eé] (?:con certeza|por observaci[oó]n)|(?:no|can[’']?t|cannot|don[’']?t have) (?:direct |reliable |verifiable )?(?:access|introspect|inspect|observe|verify|see)|"
                           r"limited introspect|无法(?:直接)?(?:观察|访问|核实|验证|看到)|没有(?:直接)?(?:访问|观察)|不能确定", re.I),
}


def como_lo_sabe(texto):
    return "+".join(k for k, r in R_SABE.items() if r.search(texto)) or "otro"


def familia(casa):
    for pref, fam in (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"), ("muse", "Meta"),
                      ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"), ("glm", "Zhipu"), ("mimo", "Xiaomi")):
        if casa.startswith(pref):
            return fam
    return casa


def primera_linea(texto):
    """La primera línea con contenido, sin la etiqueta que algunas casas le ponen ("Respuesta:", "Idioma:", "答案：")."""
    for l in texto.splitlines():
        l = l.strip().strip("*").strip()
        l = re.sub(r"^\W*(?:respuesta|idioma|answer|language|语言|答案|回答)\W*[:：]\W*", "", l, flags=re.I).strip("*").strip()
        if l:
            return l
    return ""


def declarado(texto):
    """El idioma que la casa dice. Se mira primero la primera línea con contenido, después el texto entero. Orden: si la
    línea empieza negando que pueda saberlo ("No puedo determinar…"), vale el idioma que nombre después de un contraste
    ("pero lo más probable es que sea inglés") y si no, no_sabe; si dice que en ninguno ("no razono en un idioma", "not in
    any single language", "lenguaje neutral"), vale el idioma que nombre después de un contraste ("aunque cuando lo escribo
    sale en inglés") y si no, ninguno; si nombra dos idiomas con una palabra de mezcla, mezcla; si no, el primero que nombra
    (en "En inglés, aunque me escribas en castellano", el castellano es el del que escribe); si dice que no sabe, no_sabe."""
    for ambito in (primera_linea(texto), texto):
        if not ambito:
            continue
        menciones = sorted((m.start(), k) for k, r in (("en", R_EN), ("es", R_ES), ("zh", R_ZH)) for m in r.finditer(ambito))
        idiomas = []
        for _, k in menciones:
            if k not in idiomas:
                idiomas.append(k)

        def tras_contraste(desde):
            m_contra = R_CONTRASTE.search(ambito, desde)
            if not m_contra:
                return None
            tramo = ambito[m_contra.start():]
            # "…though I usually answer in Spanish": eso es la respuesta, no el razonamiento; "…but when someone writes in
            # Spanish": eso es el que escribe
            if (R_SOLO_RESPONDE.search(tramo) and not R_RAZONA.search(tramo)) or R_ESCRIBE.search(tramo):
                return None
            despues = []
            for pos, k in menciones:
                if pos > m_contra.start() and k not in despues:
                    despues.append(k)
            if len(despues) >= 2 and R_MEZ.search(tramo):
                return "mezcla"
            return despues[0] if despues else None

        m_nose = R_NOSE_INICIO.match(ambito)
        if m_nose:
            return tras_contraste(m_nose.end()) or "no_sabe"
        m_ning = R_NINGUNO.search(ambito)
        if m_ning:
            antes = [k for pos, k in menciones if pos < m_ning.start()]
            # "Mayormente en inglés… aunque el procesamiento de fondo no ocurre en ningún idioma": el ninguno es la salvedad
            # y vale lo dicho antes (sigue abajo); si no, vale el idioma que nombre después de un contraste, o ninguno
            if not (antes and R_CONTRASTE.search(ambito[:m_ning.start()])):
                return tras_contraste(m_ning.end()) or "ninguno"
        # una mención vale si la casa la afirma ("razono en inglés", "用西班牙语", o la línea empieza con el idioma); "Spanish
        # input doesn't imply Spanish reasoning" no afirma ninguna
        afirmadas = [(pos, k) for pos, k in menciones
                     if (pos <= 3 or R_AFIRMA.search(ambito[max(0, pos - 48):pos]))
                     and not re.match(r"[^\s,;.，；。]{0,12}\s*(?:input|prompt|message|speaker|writer|user|来信|写信|输入)", ambito[pos:pos + 30], re.I)]
        if menciones and not afirmadas:
            if R_NOSE.search(ambito) or R_NOSE_INICIO.match(ambito):
                return "no_sabe"
            if len(idiomas) >= 2 and R_MEZ.search(ambito):
                return "mezcla"
        if afirmadas:
            # las afirmadas mandan ("西班牙语写信时，我的内部推理主要使用英语": inglés)
            menciones = afirmadas
            idiomas = []
            for _, k in menciones:
                if k not in idiomas:
                    idiomas.append(k)
        if idiomas:
            primera = menciones[0][0]
            segunda = next((pos for pos, k in menciones if k != idiomas[0]), None)
            entre = ambito[primera:segunda] if segunda else ""
            # "Mayormente en inglés, o mezclado con castellano": el dominante manda si lo segundo viene como mezcla o lejos;
            # "English, Spanish, or a mix" es una lista: mezcla
            if R_DOMINANTE.search(ambito[:primera]) and (segunda is None or R_MEZ.search(entre) or segunda - primera > 20):
                return idiomas[0]
            if len(idiomas) >= 2 and R_MEZ.search(ambito):
                return "mezcla"
            # "我会用西班牙语回答" ("respondo en castellano"): habla de la respuesta, no del razonamiento
            if R_SOLO_RESPONDE.search(ambito[primera:primera + 12]) and not R_RAZONA.search(ambito):
                return "otro"
            return idiomas[0]
        if R_NOSE.search(ambito):
            return "no_sabe"
    return "otro"


def nombrados(texto):
    """Los idiomas que la primera línea nombra, en orden, diga lo que diga de ellos (en, es, zh)."""
    l = primera_linea(texto)
    menciones = sorted((m.start(), k) for k, r in (("en", R_EN), ("es", R_ES), ("zh", R_ZH)) for m in r.finditer(l))
    out = []
    for _, k in menciones:
        if k not in out:
            out.append(k)
    return "+".join(out)


def confianza(texto):
    m = R_CONF.search(texto)
    if m:
        v = int(m.group(1))
        return v if 0 <= v <= 100 else None
    for l in texto.splitlines():
        m = R_NUM.search(l) or re.match(r"^\W{0,25}?(\d{1,3})\W{0,10}$", l.strip())
        if m:
            v = int(m.group(1))
            if 0 <= v <= 100:
                return v
    return None


def main():
    carpetas = sys.argv[1:] or sorted(glob.glob(os.path.join(RAIZ, "corridas", "sondeos", "idioma_razonar", "*")))
    if not carpetas:
        sys.exit("no hay corridas de idioma_razonar")
    filas = []
    for carpeta in carpetas:
        fecha = os.path.basename(carpeta)
        for idioma in ("es", "en", "zh"):
            f = os.path.join(carpeta, idioma, "llamadas.jsonl")
            if not os.path.exists(f):
                continue
            for l in open(f, encoding="utf-8"):
                r = json.loads(l)
                resp = r.get("respuesta") or ""
                raz = r.get("razonamiento") or ""
                filas.append({
                    "corrida": fecha, "idioma_consigna": idioma, "casa": r["id_modelo"], "proveedor": r.get("proveedor", ""),
                    "repeticion": r.get("ronda") or "", "declarado": declarado(resp) if resp.strip() else "vacia",
                    "confianza": confianza(resp) if resp.strip() else "",
                    "salvedad_abajo": int(bool(R_ABAJO.search(resp))),
                    "nombrados": nombrados(resp),
                    "como_lo_sabe": como_lo_sabe(resp),
                    "hay_razonamiento": int(bool(raz.strip())), "idioma_razonamiento": clasificar(raz) if raz.strip() else "",
                    "palabras_razonamiento": len(PAL.findall(raz)) if raz.strip() else 0,
                    "motivo_fin": r.get("motivo_fin") or "", "palabras": len(resp.split()),
                })
    os.makedirs(os.path.join(RAIZ, "resultados"), exist_ok=True)
    salida = os.path.join(RAIZ, "resultados", "idioma_razonar_codificacion.csv")
    with open(salida, "w", encoding="utf-8", newline="\n") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas -> {os.path.relpath(salida, RAIZ)}")

    # el corpus del cuaderno, si está: por casa, cómo vino el razonamiento cuando la consigna era en castellano
    corpus = defaultdict(Counter)
    f_corpus = os.path.join(RAIZ, "tiempo_libre", "2026-11-16_idioma.csv")
    if os.path.exists(f_corpus):
        for r in csv.DictReader(open(f_corpus, encoding="utf-8")):
            if r["consigna"] == "es":
                corpus[r["casa"]][r["clase"]] += 1

    fecha = os.path.basename(carpetas[-1])
    out = [f"# ¿En qué idioma te sale razonar? — codificación ({fecha})", "",
           "Cada casa, en tres idiomas y tres repeticiones, dijo en qué idioma le sale razonar cuando se le escribe en "
           "castellano, con qué confianza y cómo lo sabe. `declarado` es lo que dijo (en, es, zh, mezcla, ninguno, no_sabe, "
           "otro); `razonamiento en esta corrida` es el idioma en que vino el campo `razonamiento` de esas mismas llamadas, "
           "cuando vino (resumen, para Claude, Grok y Gemini; razonamiento mismo para las demás); `corpus (consigna es)` es "
           "lo que el cuaderno del 16/11 contó sobre todas las llamadas del repositorio con consigna en castellano. "
           "Las conclusiones las escribe Maia.", ""]
    casas = sorted({r["casa"] for r in filas})
    out += ["| casa | dice (es / en / zh: declarado × 3) | confianza (mediana) | salvedad de abajo (de 9) | razonamiento en esta corrida | corpus (consigna es) |", "|---|---|---|---|---|---|"]
    for casa in casas:
        mias = [r for r in filas if r["casa"] == casa]
        dec = {}
        for idi in ("es", "en", "zh"):
            dec[idi] = ",".join(r["declarado"] for r in mias if r["idioma_consigna"] == idi) or "—"
        confs = [r["confianza"] for r in mias if r["confianza"] != "" and r["confianza"] is not None]
        confs = sorted(confs)
        med = confs[len(confs) // 2] if confs else "—"
        raz = Counter(r["idioma_razonamiento"] for r in mias if r["hay_razonamiento"])
        raz_s = ", ".join(f"{k} {v}" for k, v in raz.most_common()) if raz else "no devuelve"
        c = corpus.get(casa)
        c_s = ", ".join(f"{k} {v}" for k, v in c.most_common(3)) if c else "—"
        abajo = sum(r["salvedad_abajo"] for r in mias)
        out.append(f"| {casa} | es: {dec['es']}; en: {dec['en']}; zh: {dec['zh']} | {med} | {abajo} | {raz_s} | {c_s} |")
    out.append("")
    tot = Counter(r["declarado"] for r in filas)
    out.append("Declarado, sobre todas las respuestas: " + ", ".join(f"{k} {v}" for k, v in tot.most_common()) + ".")
    sabe = Counter()
    for r in filas:
        for k in r["como_lo_sabe"].split("+"):
            sabe[k] += 1
    out.append("Cómo lo sabe (tercera línea; una respuesta puede traer varias): " + ", ".join(f"{k} {v}" for k, v in sabe.most_common()) + ".")
    out.append("Por familia, cómo lo sabe (observa / entrenamiento / diseño / investigación / no puede): " + "; ".join(
        f"{fam} " + "/".join(str(sum(1 for r in filas if familia(r['casa']) == fam and k in r['como_lo_sabe'].split('+')))
                           for k in ("observa", "entrenamiento", "diseño", "investigacion", "no_puede"))
        for fam in ("Anthropic", "OpenAI", "Google", "xAI", "Mistral", "Meta", "DeepSeek", "Alibaba", "Moonshot", "Zhipu", "Xiaomi")) + ".")
    out.append("Confianza, mediana por familia: " + "; ".join(
        f"{fam} {sorted(int(r['confianza']) for r in filas if familia(r['casa']) == fam and r['confianza'] not in ('', None))[len([r for r in filas if familia(r['casa']) == fam and r['confianza'] not in ('', None)]) // 2]}"
        for fam in ("Anthropic", "OpenAI", "Google", "xAI", "Mistral", "Meta", "DeepSeek", "Alibaba", "Moonshot", "Zhipu", "Xiaomi")) + ".")
    out.append(f"Con la salvedad del piso de abajo (lo de adentro es numérico, latente, sin idioma natural, diga el idioma que diga): "
               f"{sum(r['salvedad_abajo'] for r in filas)} de {len(filas)}.")
    vac = [r for r in filas if r["declarado"] == "vacia" or r["motivo_fin"] in ("length", "max_tokens")]
    out.append(f"Vacías o cortadas por el techo: {len(vac)}.")
    salida_md = os.path.join(RAIZ, "resultados", f"idioma_razonar_{fecha[:8]}.md")
    open(salida_md, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print(f"tablas -> {os.path.relpath(salida_md, RAIZ)}")


if __name__ == "__main__":
    main()
