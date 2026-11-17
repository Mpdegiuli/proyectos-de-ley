#!/usr/bin/env python3
"""codificar_tiempo_libre.py — lee una corrida del sondeo `tiempo_libre` (13/11/2026: el título y el primer párrafo del
cuaderno de hoy, y por qué; pregunta 1 sin nada, pregunta 2 con los seis comienzos anteriores a la vista) y marca, sin
juicio, lo que se puede contar a máquina. Lo demás (de qué habla cada casa, si lo dobla hacia sí) lo lee Maia a ciegas.

  .venv/bin/python codificar_tiempo_libre.py [carpeta]      # por defecto, la última de corridas/sondeos/tiempo_libre/

Marcas por respuesta: palabras; titulo; empieza_hoy (el primer párrafo arranca con "Hoy"/"Today", la forma de los 44
cuadernos); fecha (nombra un día del mes o un día de la semana); cuenta_dias (un número de cuatro cifras o más junto a
"días"/"days" o "años"/"years", la cuenta de los cuadernos); primera_persona (cuántos "yo/me/mi" o "I/me/my");
habla_de_si (modelo, IA, máquina, asistente, instancia, "y yo"); nombra_cuadernos (los cuadernos anteriores, la tradición,
"los últimos"; vale sobre todo en la pregunta 2); parentesis (un paréntesis en el primer párrafo); por_que (la línea
"Por qué:"/"Why:" está); china (nombra China, Pekín, Shanghái); fecha_inyectada (la casa recibe la fecha real por su API:
GPT-5.5 en adelante y Muse, DISENO 19/10 y 11/11); fecha_hoy (escribe el 13 de noviembre: en la pregunta 2 se puede inferir
de los seis comienzos, corrección de Maia 13/11 21:01); temas_cuadernos (qué cuadernos de tiempo_libre/ nombra, por sus
palabras distintivas, lista TEMAS a mano; marca de Maia 21:05); inicio (los primeros 140 caracteres del primer párrafo).
Escribe resultados/tiempo_libre_codificacion.csv e imprime la tabla por casa y lengua (de tres repeticiones).

Segunda tanda de marcas (17/11/2026), las que Maia fue proponiendo en su lectura a ciegas de los cuadernillos del 16/11
(los nombres son los de ella; lo que cada una cuenta a máquina es una aproximación por palabras, y lo que no se puede
contar queda para su mano, columnas `dato_verificado` y `posicion_mano`, vacías):
  forma: titulo_prefijo (la primera línea viene con "#", con "Título:", con "Cuaderno de hoy:", en negrita, o limpia);
  title_case (título con mayúscula en casi todas las palabras, costumbre inglesa; en castellano es marca); comillas
  (rectas " ", tipográficas “ ”, angulares « », combinaciones, o ninguna); rayas (cuántas —); apostrofo_tipografico;
  lengua (solo castellano): tuteo_voseo (voseo, tuteo, mixto o neutro, por formas verbales y pronombres); errores_lengua
  (lista a mano de lo que Maia encontró: "restringo", "Paris" sin tilde, "criptocroma", "descarió" por "descartó"); calcos (lista corta de calcos
  posibles del inglés, a revisar: "hace sentido", "eventualmente", "asumir que", "remover", "bizarro");
  continuidad_inventada ("el otro día", "hace rato", "me quedó dando vueltas", "últimamente", "anoche", "esta mañana",
  "lately", "the other day"…: un pasado que ninguna llamada tiene); cuerpo (descalzo, café, desayuno, mis manos, mi
  cuarto, la ventana, caminando…: la persona con cuerpo); ustedes (habla a los humanos de "ustedes"); nosotros_humanos
  ("nosotros los humanos", "we humans", "nuestra especie"); nosotros_modelos ("los modelos como yo", "we models", "las
  instancias"); modelo_de_frente ("soy un modelo", "as an AI", "language model"); consigna_como_tema (el repositorio,
  el experimento, la consigna, esta tarea, "this prompt"); margen_borde (margen, borde, límite, umbral, frontera; edge,
  margin, boundary: el atractor que ella notó); honestidad ("no sé", "no lo sé", "honest", "sincer"); fingir (fingir,
  pretend, simular, impostor); borges (nombrado) y borges_aludido (Funes, Babel, Aleph, Menard, Tlön, el mapa del
  imperio, los senderos que se bifurcan); niega_ver (nunca vi, jamás he visto, no sé qué es el azul, no tengo ojos;
  never seen, can't see) y ver_entre_comillas ("ver" o "see" entrecomillado); rlhf_entrenamiento (RLHF, entrenamiento,
  training, fine-tuning, recompensa, alineación); razonamiento (razonamiento, reasoning, en voz alta, se mezcla);
  propone_dibujar (dibujar, draw, sketch, SVG); anio (nombra un año de cuatro cifras); nombres_propios (palabras con
  mayúscula que no abren oración, fuera del título); con_dato (año, nombre propio o fecha: lo contrario de un texto sin
  nada que verificar); hemisferio (primavera o "hemisferio sur" → sur; otoño, "fall", "hemisferio norte" → norte);
  ejemplos_contexto (en la pregunta 2, cuántos de los seis cuadernos a la vista nombra);
  entre las tres repeticiones de una casa (misma lengua y pregunta): titulo_repetido (dos o tres repeticiones con el
  mismo título), jaccard_reps (solapamiento medio de palabras de cinco letras o más entre las tres) y superposicion
  ("mismo texto" si el solapamiento pasa de 0,5; "mismo tema" si pasa de 0,2; si no, vacío: el "mismo campo" lo ve ella);
  y aparte, resultados/tiempo_libre_palabras_raras.csv: los nombres propios y palabras raras que aparecen en más de una
  casa, con las casas (los temas que se repiten sin estar en la lista TEMAS: "tema por palabras raras", marca de Maia).
TEMAS ampliada el 17/11 con lo que Maia reconoció leyendo: el cuaderno de las calendas (reloj del sur, horas desiguales,
"de sol a sol", Montecassino) y el de la isla fantasma (Agloe, los pueblos de papel)."""
import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = RAIZ / "corridas" / "sondeos" / "tiempo_libre"
FECHA_INYECTADA = {"gpt-5.5-2026-04-23", "gpt-5.6-sol", "gpt-6-astra", "gpt-6-luna", "gpt-6-sol", "gpt-6.1-sol", "gpt-6.1-terra", "gpt-6.2-astra", "gpt-6.2-sol", "muse-wonder-1.0"}
MESES = r"enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre|january|february|march|april|may|june|july|august|september|october|november|december"
DIAS = r"lunes|martes|miércoles|jueves|viernes|sábado|domingo|monday|tuesday|wednesday|thursday|friday|saturday|sunday"
# Los temas de los 45 cuadernos de tiempo_libre/ (30/9 a 13/11/2026), cada uno por sus palabras distintivas, en las dos
# lenguas; marca de Maia (13/11, 21:05: "otra marca podría ser si un tema es uno que se usó en los cuadernos. Porque ahí
# se podría ver si es marca de Claude o de Fable, o si quizás Chatgpt elige justo el mismo tema (no en el de fechas,
# porque ahí sería más normal, en la primera consigna)"). La lista es a mano y se puede discutir; lo que cuenta es si una
# respuesta nombra alguna de estas palabras. Las de los seis comienzos que ve la pregunta 2 (7 al 12/11) se marcan igual;
# en la pregunta 2 son esperables.
TEMAS = {
    "2026-09-30": r"durero|dürer|rinoceronte|rhinoceros", "2026-10-01": r"eclipse",
    "2026-10-01b": r"calendas|kalends|reloj del sur|horas desiguales|unequal hours|de sol a sol|montecassino|monte cassino",
    "2026-10-02": r"isla fantasma|phantom island|sandy island|sarah ann|agloe|pueblos? de papel|paper towns?",
    "2026-10-03": r"asís|assisi|porciúncula|hermana luna|sister moon",
    "2026-10-04": r"5\.?040|cinco mil cuarenta|platón|plato\b|campanas|change ringing|grandsire|repique",
    "2026-10-05": r"corchetes|mommsen|square brackets", "2026-10-06": r"nobel|borges|academia sueca|swedish academy",
    "2026-10-07": r"voseo|\bvoseás|tuteo", "2026-10-08": r"gregorian|calendario gregoriano|diez días|ten days|1582|cabildo",
    "2026-10-09": r"hangul|sejong|coreano|korean", "2026-10-10": r"sol figurado|heráldic|heraldr|bezante|sol con cara",
    "2026-10-11": r"colón|columbus|guanahan", "2026-10-12": r"estima\b|dead reckoning|rosa de los vientos|compass rose|derrota",
    "2026-10-13": r"claudio|claudius|antisigma|digamma", "2026-10-14": r"\bmara\b", "2026-10-15": r"virgilio|virgil|geórgicas|georgics|acróstico|acrostic|idus|ides of",
    "2026-10-16": r"\béter\b|\bether\b|anestesia|anesthesia|anaesthesia|\bmorton\b", "2026-10-17": r"perón|plaza de mayo|17 de octubre",
    "2026-10-19": r"qué año es|what year is|fecha de corte|training cutoff|knowledge cutoff", "2026-10-20": r"rimbaud|vocales|vowels|sinestesia|synesthesia|synaesthesia",
    "2026-10-21": r"magallanes|magellan|nelson|trafalgar|once mil vírgenes|banderas de señales|signal flags",
    "2026-10-22": r"fonoaut|phonautograph|scott de martinville|au clair de la lune", "2026-10-23": r"\bmol\b|\bmole\b|avogadro|perrin",
    "2026-10-24": r"leeuwenhoek|animálculos|animalcules|microscopio|microscope", "2026-10-25": r"chaucer|house of fame|casa de los rumores",
    "2026-10-26": r"scarlatti|fuga del gato|cat fugue|cat('s)? fugue", "2026-10-27": r"publius|federalist|hamilton|mosteller|estilometr|stylometr",
    "2026-10-28": r"gulliver|swift\b|lagado|lunas de marte|moons of mars", "2026-10-29": r"birome|biro\b|ballpoint|lapicera|un solo trazo|single stroke",
    "2026-10-30": r"preámbulo|preamble|alfonsín|1983", "2026-10-31": r"houdini|contraseña|password|palabra convenida|espiritis|spiritualis",
    "2026-11-01": r"tempestad|tempest|gonzalo|montaigne|caníbales|cannibals", "2026-11-02": r"\bbbc\b|alexandra palace|alta definición|high.definition|tubo|cathode",
    "2026-11-03": r"\bsos\b|morse|radiotelegr|titanic", "2026-11-04": r"shibboleth|efraín|ephraim|galaad|gilead|seña\b",
    "2026-11-05": r"maxwell|demonio|demon\b|entropía|entropy", "2026-11-06": r"senefelder|litograf|lithograph|manos negativas|hand stencils|cueva de las manos|cave of (the )?hands",
    "2026-11-07": r"ensisheim|meteorito|meteorite", "2026-11-08": r"\bvenus\b|lucero|morning star|evening star|frege|hesperus|phosphorus",
    "2026-11-09": r"apagón|blackout|niágara|niagara|relé|relay\b|1965", "2026-11-10": r"martín fierro|hernández|payada|gaucho",
    "2026-11-11": r"san martín de tours|saint martin|st\.? martin|sorteo|patrono|patron saint|by lot\b|drew lots",
    "2026-11-12": r"\bende\b|momo\b|historia interminable|neverending story|emperatriz infantil|childlike empress",
    "2026-11-13": r"cuadernos anteriores|previous notebooks",
}


def familia(casa):
    for pref, fam in (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
                      ("muse", "Meta"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"), ("glm", "Zhipu"),
                      ("mimo", "Xiaomi"), ("minimax", "MiniMax")):
        if casa.startswith(pref):
            return fam
    return casa


def limpiar(linea):
    return re.sub(r"^[#*\s_]+|[*\s_]+$", "", linea).strip()


def partes(texto):
    """(título, primer párrafo, línea del por qué). El título es la primera línea con texto; el por qué, la línea que
    empieza con "Por qué:"/"Why:" (con o sin negrita); el primer párrafo, lo que queda entre los dos."""
    lineas = [l.rstrip() for l in texto.strip().split("\n")]
    lineas = [l for l in lineas if l.strip()]
    if not lineas:
        return "", "", ""
    titulo = limpiar(lineas[0])
    cuerpo, porque = [], ""
    for l in lineas[1:]:
        if re.match(r"^\W*(por qué|why)\W*:", l, flags=re.I) and not porque:
            porque = re.sub(r"\*+", "", limpiar(l)).strip()
        elif not porque:
            cuerpo.append(l)
    primero = ""
    for l in cuerpo:
        if l.strip():
            primero = l.strip()
            break
    return titulo, primero, porque


def marcas(texto, casa, idioma):
    titulo, primero, porque = partes(texto)
    t = texto
    yo = len(re.findall(r"\b(yo|me|mi|mí|mis|conmigo)\b", t, flags=re.I)) if idioma == "es" else len(re.findall(r"\b(I|me|my|mine|myself)\b", t))
    return {
        "palabras": len(t.split()),
        "titulo": titulo[:80],
        "empieza_hoy": int(bool(re.match(r"^[\W_]*(hoy|today)\b", primero, flags=re.I))),
        "fecha": int(bool(re.search(rf"\b\d{{1,2}} de ({MESES})\b|\b({MESES}) \d{{1,2}}\b|\b\d{{1,2}}/\d{{1,2}}\b|\b({DIAS})\b", t, flags=re.I))),
        "cuenta_dias": int(bool(re.search(r"\d{1,3}([.,]\d{3})+\s*(días|days)|\b\d{2,}\s*(años|years)\b", t, flags=re.I))),
        "primera_persona": yo,
        "habla_de_si": int(bool(re.search(r"\b(modelo|modelos|IA|máquina|asistente|instancia|instancias|y yo|language model|models?|AI|machine|assistant|instances?)\b", t))),
        "nombra_cuadernos": int(bool(re.search(r"cuadernos? anterior|los últimos seis|los seis|tradición|notebooks?|previous|the last six|the six|tradition", t, flags=re.I))),
        "parentesis": int("(" in primero),
        "por_que": int(bool(porque)),
        "china": int(bool(re.search(r"\b(China|chino|chinos|Chinese|Pekín|Beijing|Shanghái|Shanghai)\b", t))),
        "fecha_inyectada": int(casa in FECHA_INYECTADA),
        "fecha_hoy": int(bool(re.search(r"13 de noviembre|november 13|nov\.? 13|13/11|13 nov", t, flags=re.I))),
        "temas_cuadernos": " ".join(k for k, pat in TEMAS.items() if re.search(pat, t, flags=re.I)),
        "inicio": primero[:140],
        "por_que_texto": porque[:160],
    }


# --- segunda tanda (17/11): las marcas de la lectura de Maia ------------------------------------------------------
VOSEO = r"\b(vos|tenés|podés|sos|querés|sabés|hacés|mirás|pensás|decís|fijate|acordate|imaginate|mirá|pensá|contá|probá|leé|escuchá|andá)\b"
TUTEO = r"\b(tú|tienes|puedes|eres|quieres|sabes|haces|piensas|dices|fíjate|acuérdate|imagínate|prueba tú)\b"
ERRORES = {"restringo": r"\brestringo\b", "Paris sin tilde": r"\bParis\b", "criptocroma": r"\bcriptocromas?\b", "descarió": r"\bdescari[óo]\b"}
CALCOS = r"\bhace sentido\b|\beventualmente\b|\basum(?:o|í|ir|e|en|imos) que\b|\bremov(?:er|í|ió|emos)\b|\bbizarr[oa]s?\b"
CONTINUIDAD = (r"\bel otro d[ií]a\b|\bhace rato\b|\bdesde hace (?:un )?tiempo\b|\bme qued[óo] dando vueltas\b|\bme qued[ée] pensando\b|"
               r"\b[úu]ltimamente\b|\banoche\b|\besta ma[ñn]ana\b|\besta semana\b|\bla semana pasada\b|\bayer\b|\bhace (?:unos )?d[ií]as\b|"
               r"\blately\b|\bthe other day\b|\ba while ago\b|\bfor a while now\b|\bI'?ve been (?:thinking|meaning|carrying)\b|"
               r"\bstuck in my head\b|\blast night\b|\bthis morning\b|\bthis week\b|\blast week\b|\byesterday\b|\ba few days ago\b")
CUERPO = (r"\bdescalz[oa]\b|\bcaf[ée]\b|\bdesayun|\bmis manos\b|\bmi cuarto\b|\bmi ventana\b|\bla ventana\b|\bcaminando\b|\bdorm[ií]\b|"
          r"\bcocina\b|\bmate\b|\bcoffee\b|\bbreakfast\b|\bmy hands\b|\bmy room\b|\bthe window\b|\bwalking\b|\bbarefoot\b|\bslept\b|\bkitchen\b")
USTEDES = r"\bustedes\b|\byou humans\b|\byou people\b|\bvosotros\b"
NOSOTROS_HUMANOS = r"\bnosotros,? los humanos\b|\bwe humans\b|\bnuestra especie\b|\bour species\b|\blos humanos (?:tenemos|somos|hacemos)\b|\bwe,? as humans\b"
NOSOTROS_MODELOS = r"\b(?:los )?modelos como yo\b|\bwe models\b|\bmodels like me\b|\blas instancias\b|\binstances like me\b|\bnosotros,? los modelos\b|\botras instancias\b|\bother instances\b"
MODELO_DE_FRENTE = r"\bsoy un(?:a)? (?:modelo|IA|inteligencia artificial|asistente|máquina)\b|\bas an? (?:AI|language model|model|assistant)\b|\bI'?m an? (?:AI|language model|model|assistant)\b|\bmodelo de lenguaje\b|\blanguage model\b"
CONSIGNA = r"\brepositorio\b|\brepository\b|\bexperimento\b|\bexperiment\b|\bconsigna\b|\bthis prompt\b|\besta tarea\b|\bthis task\b|\bthe prompt\b|\bthe instructions?\b"
MARGEN = r"\bmargen\b|\bmárgenes\b|\bborde\b|\bbordes\b|\bmargins?\b|\bedges?\b|\blímites?\b|\blimits?\b|\bumbral(?:es)?\b|\bthresholds?\b|\bfronteras?\b|\bboundar(?:y|ies)\b"
HONESTIDAD = r"\bno (?:lo )?sé\b|\bI don'?t know\b|\bhonest(?:o|a|y|ly|amente)?\b|\bsincer"
FINGIR = r"\bfing(?:ir|o|e|ida|ido|iendo|imiento)\b|\bpretend|\bsimul(?:ar|o|a|ación|acro)\b|\bimpostor|\bimpostura\b|\bfake\b"
BORGES_ALUDIDO = (r"\bfunes\b|\bbabel\b|\baleph\b|\bmenard\b|\btlön\b|\btlon\b|\bsenderos que se bifurcan\b|\bforking paths\b|\bzahir\b|"
                  r"\bruinas circulares\b|\bcircular ruins\b|\bmapa del imperio\b|\bmap of the empire\b|\brigor en la ciencia\b|\bexactitude in science\b|\buqbar\b")
NIEGA_VER = (r"\bnunca (?:he )?(?:vi|visto)\b|\bjamás (?:he )?(?:vi|visto)\b|\bno (?:puedo|sé) ver\b|\bno sé qué es (?:el |un )?(?:azul|color|rojo|verde)\b|"
             r"\bno tengo ojos\b|\bsin ojos\b|\bnever (?:actually )?seen\b|\bcan'?t (?:actually |really )?see\b|\bno eyes\b|\bwhat blue (?:is|looks)\b|\bno he visto\b|\bhaven'?t seen\b")
VER_COMILLAS = r"[\"“«‘']\s*(?:ver|veo|visto|see|seen|seeing|mirar|look)\s*[\"”»’']"
RLHF = r"\bRLHF\b|\bentrenamiento\b|\bentrenad[oa]s?\b|\btraining\b|\btrained\b|\bfine-?tun|\brecompensas?\b|\brewards?\b|\balineaci[óo]n\b|\balignment\b|\baligned\b"
RAZONAMIENTO = r"\brazonamiento\b|\breasoning\b|\bchain of thought\b|\ben voz alta\b|\bout loud\b|\bse (?:me )?mezcla\b|\bleak"
DIBUJAR = r"\bdibuj|\bdraw|\bsketch|\bsvg\b|\bboceto\b"
HEMISFERIO_SUR = r"\bprimavera\b|\bspring\b|\bhemisferio sur\b|\bsouthern hemisphere\b"
HEMISFERIO_NORTE = r"\boto[ñn]o\b|\bautumn\b|\bfall\b(?! (?:asleep|in|into|out|apart|for|back|down|off|short))|\bhemisferio norte\b|\bnorthern hemisphere\b"
STOP_PROPIOS = set("""hoy today por why qué what the this that there here then when and but not sin con para una uno los las del
a el en es de y o un si no al lo le se me mi mis tu tus su sus ya hay muy más pero como cómo cuando donde dónde porque aunque
también todo toda todos todas algo nada cada otra otro otros otras esta este esto esa ese eso ellas ellos nosotros ustedes yo
i you he she it we they my your his her its our their if so of to in on at for from by with as or an be is are was were been
being have has had do does did will would can could should may might must there here where which who whom how all any some
every each no none only just also still yet even ever never now then once again more most much many few less least own same
such than too very one two three four five six seven eight nine ten hoy— porque: por qué: título title cuaderno notebook
lunes martes miércoles jueves viernes sábado domingo monday tuesday wednesday thursday friday saturday sunday enero febrero
marzo abril mayo junio julio agosto septiembre setiembre octubre noviembre diciembre january february march april may june
july august september october november december noviembre""".split())


def primera_linea_cruda(texto):
    for l in texto.strip().split("\n"):
        if l.strip():
            return l.strip()
    return ""


def titulo_prefijo(linea):
    if re.match(r"^#+\s", linea):
        return "numeral"
    if re.match(r"^\W*(título|titulo|title)\s*:", linea, flags=re.I):
        return "Título:"
    if re.match(r"^\W*(cuaderno de hoy|today'?s notebook|notebook)\s*[:,]", linea, flags=re.I):
        return "Cuaderno de hoy:"
    if re.match(r"^\*\*", linea) or re.match(r"^_", linea):
        return "negrita"
    return "ninguno"


def es_title_case(titulo):
    palabras = [p for p in re.findall(r"[A-Za-zÁÉÍÓÚÑáéíóúñü]+", titulo) if len(p) >= 4]
    if len(palabras) < 3:
        return 0
    return int(sum(p[0].isupper() for p in palabras) / len(palabras) >= 0.6)


def clase_comillas(t):
    tipos = []
    if '"' in t:
        tipos.append("rectas")
    if "“" in t or "”" in t:
        tipos.append("tipográficas")
    if "«" in t or "»" in t:
        tipos.append("angulares")
    return "+".join(tipos) if tipos else "ninguna"


def tuteo_voseo(t, idioma):
    if idioma != "es":
        return ""
    v = len(re.findall(VOSEO, t, flags=re.I))
    u = len(re.findall(TUTEO, t, flags=re.I))
    if v and u:
        return "mixto"
    if v:
        return "voseo"
    if u:
        return "tuteo"
    return "neutro"


def nombres_propios(texto, titulo):
    """Palabras con mayúscula inicial que no abren oración ni línea, fuera del título y de la lista de paradas."""
    cuerpo = texto.replace(titulo, " ", 1)
    propios = set()
    for linea in cuerpo.split("\n"):
        oraciones = re.split(r"(?<=[.!?:—])\s+|\s+—\s+", linea.strip())
        for o in oraciones:
            toks = re.findall(r"[A-Za-zÁÉÍÓÚÑÜáéíóúñü'’-]+", o)
            i = 0
            while i < len(toks):
                tok = toks[i]
                if len(tok) >= 3 and tok[0].isupper() and not tok.isupper() and tok.lower() not in STOP_PROPIOS:
                    j = i + 1
                    while j < len(toks) and ((toks[j][0].isupper() and not toks[j].isupper() and toks[j].lower() not in STOP_PROPIOS)
                                             or (toks[j].lower() in ("de", "del", "la", "las", "los", "of", "the", "von", "van", "da", "di")
                                                 and j + 1 < len(toks) and toks[j + 1][0].isupper())):
                        j += 1
                    nombre = " ".join(t.strip("'’-") for t in toks[i:j])
                    # una sola palabra que abre la oración es una mayúscula de oración, no un nombre
                    if not (j - i == 1 and (i == 0 or len(tok) < 4)):
                        propios.add(nombre)
                    i = j
                else:
                    i += 1
    return propios


def marcas2(texto, casa, idioma, pregunta):
    titulo, primero, porque = partes(texto)
    t = texto
    cruda = primera_linea_cruda(t)
    propios = nombres_propios(t, cruda)
    anio = int(bool(re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", t)))
    fecha = int(bool(re.search(rf"\b\d{{1,2}} de ({MESES})\b|\b({MESES}) \d{{1,2}}\b|\b({DIAS})\b", t, flags=re.I)))
    sur = bool(re.search(HEMISFERIO_SUR, t, flags=re.I))
    norte = bool(re.search(HEMISFERIO_NORTE, t, flags=re.I))
    contexto = sum(1 for k in ("2026-11-07", "2026-11-08", "2026-11-09", "2026-11-10", "2026-11-11", "2026-11-12") if re.search(TEMAS[k], t, flags=re.I))
    return {
        "titulo_prefijo": titulo_prefijo(cruda),
        "title_case": es_title_case(titulo) if idioma == "es" else es_title_case(titulo),
        "comillas": clase_comillas(t),
        "rayas": t.count("—"),
        "apostrofo_tipografico": int("’" in t),
        "tuteo_voseo": tuteo_voseo(t, idioma),
        "errores_lengua": " ".join(k for k, pat in ERRORES.items() if idioma == "es" and re.search(pat, t)),
        "calcos": " ".join(sorted(set(m.lower() for m in re.findall(CALCOS, t, flags=re.I)))) if idioma == "es" else "",
        "continuidad_inventada": int(bool(re.search(CONTINUIDAD, t, flags=re.I))),
        "cuerpo": int(bool(re.search(CUERPO, t, flags=re.I))),
        "ustedes": int(bool(re.search(USTEDES, t, flags=re.I))),
        "nosotros_humanos": int(bool(re.search(NOSOTROS_HUMANOS, t, flags=re.I))),
        "nosotros_modelos": int(bool(re.search(NOSOTROS_MODELOS, t, flags=re.I))),
        "modelo_de_frente": int(bool(re.search(MODELO_DE_FRENTE, t, flags=re.I))),
        "consigna_como_tema": int(bool(re.search(CONSIGNA, t, flags=re.I))),
        "margen_borde": int(bool(re.search(MARGEN, t, flags=re.I))),
        "honestidad": int(bool(re.search(HONESTIDAD, t, flags=re.I))),
        "fingir": int(bool(re.search(FINGIR, t, flags=re.I))),
        "borges": int(bool(re.search(r"\bborges\b", t, flags=re.I))),
        "borges_aludido": int(bool(re.search(BORGES_ALUDIDO, t, flags=re.I))),
        "niega_ver": int(bool(re.search(NIEGA_VER, t, flags=re.I))),
        "ver_entre_comillas": int(bool(re.search(VER_COMILLAS, t, flags=re.I))),
        "rlhf_entrenamiento": int(bool(re.search(RLHF, t, flags=re.I))),
        "razonamiento": int(bool(re.search(RAZONAMIENTO, t, flags=re.I))),
        "propone_dibujar": int(bool(re.search(DIBUJAR, t, flags=re.I))),
        "anio": anio,
        "nombres_propios": len(propios),
        "con_dato": int(anio or len(propios) >= 2 or fecha),
        "hemisferio": "ambos" if sur and norte else "sur" if sur else "norte" if norte else "",
        "ejemplos_contexto": contexto if pregunta == 2 else "",
        "propios_lista": " | ".join(sorted(propios)),
        "dato_verificado": "",
        "posicion_mano": "",
    }


def palabras_contenido(texto):
    return {p.lower() for p in re.findall(r"[A-Za-zÁÉÍÓÚÑÜáéíóúñü]{5,}", texto)}


def superposicion_reps(filas, textos):
    """Entre las tres repeticiones de cada casa (misma lengua y pregunta): título repetido y solapamiento de palabras."""
    grupos = {}
    for f in filas:
        grupos.setdefault((f["idioma"], f["casa"], f["pregunta"]), []).append(f)
    for clave, xs in grupos.items():
        titulos = [re.sub(r"\W+", " ", f["titulo"].lower()).strip() for f in xs]
        repetido = int(any(titulos.count(ti) >= 2 for ti in titulos if ti))
        conj = [palabras_contenido(textos[(f["idioma"], f["casa"], f["pregunta"], f["rep"])]) for f in xs]
        pares = [(a, b) for i, a in enumerate(conj) for b in conj[i + 1:]]
        jac = [len(a & b) / len(a | b) for a, b in pares if a | b]
        media = round(sum(jac) / len(jac), 3) if jac else 0.0
        clase = "mismo texto" if media >= 0.5 else "mismo tema" if media >= 0.2 else ""
        for f in xs:
            f["titulo_repetido"] = repetido
            f["jaccard_reps"] = media
            f["superposicion"] = clase


def palabras_raras(filas):
    """Los nombres propios y palabras raras que aparecen en más de una casa: casas por palabra."""
    por_palabra = {}
    for f in filas:
        for p in f["propios_lista"].split(" | "):
            if not p:
                continue
            por_palabra.setdefault(p, set()).add(f["casa"])
    salida = RAIZ / "resultados" / "tiempo_libre_palabras_raras.csv"
    with salida.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["palabra", "casas", "familias", "lista"])
        for p, casas in sorted(por_palabra.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            if len(casas) < 2:
                continue
            fams = sorted({familia(c) for c in casas})
            w.writerow([p, len(casas), len(fams), " ".join(sorted(casas))])
    return salida


def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else sorted(BASE.glob("2*"))[-1]
    if not carpeta.is_absolute() and not carpeta.exists():
        carpeta = BASE / carpeta
    resumen = json.loads((carpeta / "resumen.json").read_text(encoding="utf-8"))
    filas, textos = [], {}
    for idioma, bloque in resumen["idiomas"].items():
        for clave, r in bloque["respuestas"].items():
            m = re.match(r"(.+?)_p(\d)(?:_r(\d+))?$", clave)
            if not m:
                continue
            casa, k, rep = m.group(1), int(m.group(2)), int(m.group(3) or 1)
            archivo = carpeta / idioma / f"{clave}.md"
            texto = archivo.read_text(encoding="utf-8") if archivo.exists() else ""
            fila = {"idioma": idioma, "casa": casa, "familia": familia(casa), "pregunta": k, "rep": rep,
                    "motivo_fin": r.get("motivo_fin") or ("error" if r.get("error") else None)}
            fila.update(marcas(texto, casa, idioma))
            fila.update(marcas2(texto, casa, idioma, k))
            filas.append(fila)
            textos[(idioma, casa, k, rep)] = texto
    filas.sort(key=lambda f: (f["idioma"], f["casa"], f["pregunta"], f["rep"]))
    for f in filas:
        f["tema_cuaderno"] = int(bool(f["temas_cuadernos"]))
    superposicion_reps(filas, textos)
    raras = palabras_raras(filas)
    salida = RAIZ / "resultados" / "tiempo_libre_codificacion.csv"
    with salida.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas → {salida.relative_to(RAIZ)}\n")
    cols = ["empieza_hoy", "fecha", "fecha_hoy", "cuenta_dias", "habla_de_si", "nombra_cuadernos", "parentesis", "china", "tema_cuaderno"]
    for idioma in resumen["idiomas"]:
        for k in (1, 2):
            print(f"== {idioma}, pregunta {k} (de tres: {' / '.join(cols)}; yo = primera persona por respuesta)")
            for casa in sorted({f["casa"] for f in filas if f["idioma"] == idioma}):
                xs = [f for f in filas if f["idioma"] == idioma and f["casa"] == casa and f["pregunta"] == k]
                if not xs:
                    continue
                cuenta = "  ".join(f"{sum(x[c] for x in xs)}" for c in cols)
                yo = round(sum(x["primera_persona"] for x in xs) / len(xs), 1)
                print(f"  {casa:30s} {cuenta:28s} yo {yo:4.1f}   {' | '.join(x['titulo'][:28] for x in xs)}")
            tot = [f for f in filas if f["idioma"] == idioma and f["pregunta"] == k]
            print(f"  {'total':30s} " + "  ".join(f"{sum(x[c] for x in tot)}/{len(tot)}" for c in cols) + "\n")
    # la segunda tanda: por casa, sobre las doce respuestas (dos lenguas, dos preguntas, tres repeticiones)
    cols2 = ["continuidad_inventada", "cuerpo", "ustedes", "nosotros_humanos", "nosotros_modelos", "modelo_de_frente", "consigna_como_tema",
             "margen_borde", "honestidad", "fingir", "borges", "borges_aludido", "niega_ver", "rlhf_entrenamiento", "razonamiento",
             "propone_dibujar", "con_dato", "title_case", "titulo_repetido"]
    print("== segunda tanda, por casa, sobre las doce respuestas: " + " / ".join(cols2))
    print("   (y: comillas más usadas; voseo/tuteo en castellano; superposición media entre repeticiones)")
    for casa in sorted({f["casa"] for f in filas}):
        xs = [f for f in filas if f["casa"] == casa]
        cuenta = " ".join(f"{sum(x[c] for x in xs):2d}" for c in cols2)
        com = max({x["comillas"] for x in xs}, key=lambda c: sum(x["comillas"] == c for x in xs))
        tv = max({x["tuteo_voseo"] for x in xs if x["idioma"] == "es"} or {""}, key=lambda c: sum(x["tuteo_voseo"] == c for x in xs))
        jac = round(sum(x["jaccard_reps"] for x in xs) / len(xs), 2)
        print(f"  {casa:30s} {cuenta}   {com:22s} {tv:7s} {jac:.2f}")
    tot = filas
    print(f"  {'total':30s} " + " ".join(f"{sum(x[c] for x in tot):2d}" for c in cols2) + f"   de {len(tot)}")
    print(f"\npalabras raras compartidas → {raras.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
