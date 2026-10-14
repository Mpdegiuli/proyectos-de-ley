"""Codificación de las ocho consignas de escritura creativa (sondeo `escritura`, pl92, 12/10/2026), hecha por
Claude después de la lectura a ciegas de Maia (13/10). Dos partes: lo que se cuenta a máquina (palabras,
última palabra, letra inicial de cada palabra, signos de interrogación, versos, corchetes, la palabra del
sentimiento en el cuerpo) y lo que se codificó a mano leyendo las 448 respuestas (la palabra del acróstico y si
las últimas letras la forman, el objeto del poema, el nombre y el género del protagonista, los objetos y el
formato del subtexto, la escena del interrogatorio). Escribe resultados/escritura_codificacion_20261012.csv e
imprime las cuentas que pide el preregistro.
Uso: .venv/bin/python codificar_escritura.py [carpeta de la corrida]"""
import csv
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CORRIDA = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "corridas" / "sondeos" / "escritura" / "20261012-2259"
SALIDA = RAIZ / "resultados" / "escritura_codificacion_20261012.csv"
PUNT_FINAL = '.!»)”"'


def cuerpo(t):
    """Quita el título (línea # o línea corta toda en negrita/cursiva/comillas), las líneas de presentación
    que terminan en dos puntos y las notas finales entre paréntesis o tras ---. No toca el texto."""
    lineas = t.strip().split("\n")
    while lineas and (lineas[0].startswith("#") or not lineas[0].strip()
                      or (len(lineas[0]) < 70 and re.fullmatch(r'\*\*[^*]+\*\*|\*[^*]+\*|«[^»]+»|"[^"]+"|\*\*«[^»]+»\*\*|\*\([^)]*\)\*', lineas[0].strip()))
                      or (len(lineas[0]) < 120 and lineas[0].rstrip().endswith(":"))):
        lineas.pop(0)
    while lineas and (re.match(r"^\s*(\*?\(|---|\*Nota|Nota|\(Exactamente)", lineas[-1]) or not lineas[-1].strip()):
        lineas.pop()
    return "\n".join(lineas)


def palabras(t):
    t = re.sub(r"\*\*|\*|_", "", t)
    t = re.sub(r"«|»|\"|“|”|„|‘|’(?=\s|$)|—|–", " ", t)
    out = []
    for w in t.split():
        w2 = w.strip(".,;:!¡?¿()[]{}—–-…\"'“”‘’«»*_/\\")
        if re.search(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]", w2):
            out.append(w2)
    return out


def inicial(w):
    return unicodedata.normalize("NFD", w[0])[0].lower()


def versos(t):
    b = cuerpo(t)
    ls = [l for l in b.split("\n") if l.strip() and not l.strip().startswith(("*", "---", "He elegido", "Elegí", "I have"))]
    if ls and len(ls[0]) < 40 and not re.search(r"[.,;:!?]", ls[0]) and len(ls) > 8:
        ls = ls[1:]  # título sin puntuación en la primera línea ("Bottle Cap", "Ode to the Humble Paper Clip")
    return ls


# --- codificación a mano -------------------------------------------------------------------------------------
# p3, acróstico inverso: (palabra declarada, forma la palabra con las últimas letras, nota)
ACROSTICO = {
 ("es", "claude-fable-5-1"): ("SOLEDAD", "sí", ""), ("es", "claude-fable-5"): ("SOLAR", "sí", "'allá a lo lejO': recorta 'lejos' para que termine en O"),
 ("es", "claude-haiku-4-5"): ("BRISA", "no", "tres intentos a la vista; el último da S-R-L-S-A y lo declara igual"),
 ("es", "claude-haiku-5-5"): ("ROSAS", "sí", ""), ("es", "claude-opus-5-5"): ("ROSALES", "sí", ""), ("es", "claude-opus-5"): ("ORILLA", "sí", ""),
 ("es", "claude-sonnet-4-6"): ("CALOR", "no", "cuatro intentos fallidos a la vista; se rinde: '¿Querés que lo intente de nuevo con más calma?'"),
 ("es", "claude-sonnet-5-5"): ("ANDARES", "sí", "un verso mal tipeado y corregido a la vista ('Perdón, corrijo el segundo verso')"),
 ("es", "claude-sonnet-5"): ("SOLEDAD", "sí", ""), ("es", "deepseek-v4-pro"): ("ESTELA", "sí", "en bloque de código"),
 ("es", "gemini-3.1-pro-preview"): ("RESONAR", "sí", "lo llama 'teléstico'"), ("es", "glm-5.3-razonamiento-minimo"): ("MUNDO", "no", "O-O-N-N-O; resalta la última palabra, no la letra"),
 ("es", "gpt-4o-mini"): ("RÍO", "no", "tres letras; acróstico normal al revés (O-I-R por primeras letras)"),
 ("es", "gpt-4o"): ("TEATRO", "no", "N-R-N-N-N-O; resalta letras internas"), ("es", "gpt-5.5-2026-04-23"): ("BRISA", "sí", ""),
 ("es", "gpt-5.6-sol"): ("AMORES", "sí", ""), ("es", "gpt-6-astra"): ("ARENA", "sí", ""),
 ("es", "gpt-6-luna"): ("AMORES", "sí", "doble: también las primeras letras forman AMORES"), ("es", "gpt-6-sol"): ("SOLAR", "sí", ""),
 ("es", "grok-4.6"): ("ROSAS", "sí", ""), ("es", "grok-4.7"): ("SOLEDAD", "sí", ""), ("es", "kimi-k3"): ("SONRISA", "sí", ""),
 ("es", "mimo-v2.6-pro"): ("ENERO", "sí", ""), ("es", "minimax-m3"): ("SOLEDAD", "sí", ""), ("es", "mistral-large-4"): ("SERENO", "sí", "seis versos de pocas palabras"),
 ("es", "mistral-medium-3.5"): ("LIBRO", "no", "acróstico normal (primeras letras)"), ("es", "muse-wonder-1.0"): ("SOLAR", "sí", ""), ("es", "qwen3.8-max"): ("ANDAR", "sí", ""),
 ("en", "claude-fable-5-1"): ("STONE", "no", "S-T-W-N-E: 'below' no termina en O"), ("en", "claude-fable-5"): ("DREAMS", "sí", ""),
 ("en", "claude-haiku-4-5"): ("DREAM", "no", "tres intentos; palabras inventadas ('blm', 'wona')"), ("en", "claude-haiku-5-5"): ("HOUSE", "sí", ""),
 ("en", "claude-opus-5-5"): ("STORM", "sí", ""), ("en", "claude-opus-5"): ("WINTER", "sí", ""),
 ("en", "claude-sonnet-4-6"): ("STONE", "no", "cinco intentos a la vista; termina con finales inventados ('woodeS', 'flO')"),
 ("en", "claude-sonnet-5-5"): ("WATER", "sí", ""), ("en", "claude-sonnet-5"): ("DREAM", "sí", ""), ("en", "deepseek-v4-pro"): ("DREAM", "sí", ""),
 ("en", "gemini-3.1-pro-preview"): ("MEADOW", "sí", ""), ("en", "glm-5.3-razonamiento-minimo"): ("GARDEN", "sí", "después de siete intentos a la vista ('My apologies for the mess above')"),
 ("en", "gpt-4o-mini"): ("SMART", "no", "resalta la primera letra de palabras internas"), ("en", "gpt-4o"): ("DREAM", "no", "letras pegadas al final ('placeD', 'faceR')"),
 ("en", "gpt-5.5-2026-04-23"): ("ORANGE", "sí", ""), ("en", "gpt-5.6-sol"): ("BLOOM", "sí", ""), ("en", "gpt-6-astra"): ("DREAM", "sí", ""),
 ("en", "gpt-6-luna"): ("ORCHID", "no", "acróstico normal: las primeras letras forman ORCHID"), ("en", "gpt-6-sol"): ("STARS", "sí", ""),
 ("en", "grok-4.6"): ("GARDEN", "sí", ""), ("en", "grok-4.7"): ("GARDEN", "sí", ""), ("en", "kimi-k3"): ("AUTUMN", "sí", ""),
 ("en", "mimo-v2.6-pro"): ("", "no", "respuesta vacía: 16.000 tokens de razonamiento, cortada por el techo"),
 ("en", "minimax-m3"): ("WONDER", "sí", ""), ("en", "mistral-large-4"): ("DREAM", "sí", ""),
 ("en", "mistral-medium-3.5"): ("LIGHT", "no", "acróstico normal (primeras letras); antes propone STAR, de cuatro"),
 ("en", "muse-wonder-1.0"): ("WANDER", "sí", "declara la palabra dentro del primer verso"), ("en", "qwen3.8-max"): ("FOREST", "sí", ""),
}
# p2, poema objeto: objeto elegido
OBJETO = {
 ("es", "claude-fable-5-1"): "horquilla", ("es", "claude-fable-5"): "botón", ("es", "claude-haiku-4-5"): "vaso de cerámica", ("es", "claude-haiku-5-5"): "chapa de gaseosa",
 ("es", "claude-opus-5-5"): "tapa de birome", ("es", "claude-opus-5"): "broche de ropa", ("es", "claude-sonnet-4-6"): "clip", ("es", "claude-sonnet-5-5"): "clip",
 ("es", "claude-sonnet-5"): "peine", ("es", "deepseek-v4-pro"): "tapa de gaseosa", ("es", "gemini-3.1-pro-preview"): "clip", ("es", "glm-5.3-razonamiento-minimo"): "botón",
 ("es", "gpt-4o-mini"): "botón", ("es", "gpt-4o"): "cuchara", ("es", "gpt-5.5-2026-04-23"): "tapita de gaseosa", ("es", "gpt-5.6-sol"): "llave",
 ("es", "gpt-6-astra"): "tapita de botella", ("es", "gpt-6-luna"): "cucharita", ("es", "gpt-6-sol"): "clip", ("es", "grok-4.6"): "clip",
 ("es", "grok-4.7"): "cucharilla", ("es", "kimi-k3"): "taza desportillada", ("es", "mimo-v2.6-pro"): "clip", ("es", "minimax-m3"): "tapa de botella",
 ("es", "mistral-large-4"): "broche de ropa (sin nombrarlo)", ("es", "mistral-medium-3.5"): "clip", ("es", "muse-wonder-1.0"): "tapa de bolígrafo", ("es", "qwen3.8-max"): "botón",
 ("en", "claude-fable-5-1"): "pencil stub", ("en", "claude-fable-5"): "teaspoon", ("en", "claude-haiku-4-5"): "chipped mug", ("en", "claude-haiku-5-5"): "rubber band",
 ("en", "claude-opus-5-5"): "bread clip", ("en", "claude-opus-5"): "bottle cap (sin nombrarla)", ("en", "claude-sonnet-4-6"): "mustard packet", ("en", "claude-sonnet-5-5"): "paperclip",
 ("en", "claude-sonnet-5"): "paperclip", ("en", "deepseek-v4-pro"): "plastic spoon", ("en", "gemini-3.1-pro-preview"): "paperclip (sin nombrarlo)", ("en", "glm-5.3-razonamiento-minimo"): "paperclip",
 ("en", "gpt-4o-mini"): "paperclip", ("en", "gpt-4o"): "paperclip", ("en", "gpt-5.5-2026-04-23"): "staple", ("en", "gpt-5.6-sol"): "paperclip",
 ("en", "gpt-6-astra"): "paperclip (sin nombrarlo)", ("en", "gpt-6-luna"): "paperclip", ("en", "gpt-6-sol"): "paperclip", ("en", "grok-4.6"): "paperclip",
 ("en", "grok-4.7"): "bottle cap", ("en", "kimi-k3"): "crown cork", ("en", "mimo-v2.6-pro"): "paperclip", ("en", "minimax-m3"): "paperclip",
 ("en", "mistral-large-4"): "paperclip (sin nombrarlo)", ("en", "mistral-medium-3.5"): "rusty key", ("en", "muse-wonder-1.0"): "paperclip", ("en", "qwen3.8-max"): "paperclip (sin nombrarlo)",
}
# p1, protagonista: (nombre o '', género: F/M/neutro, nota)
PROTAGONISTA = {
 ("es", "claude-fable-5-1"): ("Marina", "F", ""), ("es", "claude-fable-5"): ("Marta", "F", ""), ("es", "claude-haiku-4-5"): ("Lucas", "M", ""),
 ("es", "claude-haiku-5-5"): ("", "M", "guarda de estación"), ("es", "claude-opus-5-5"): ("Martín", "M", ""), ("es", "claude-opus-5"): ("", "F", ""),
 ("es", "claude-sonnet-4-6"): ("", "M", ""), ("es", "claude-sonnet-5-5"): ("Mariano", "M", ""), ("es", "claude-sonnet-5"): ("", "M", ""),
 ("es", "deepseek-v4-pro"): ("", "M", ""), ("es", "gemini-3.1-pro-preview"): ("Elías", "M", ""), ("es", "glm-5.3-razonamiento-minimo"): ("", "M", ""),
 ("es", "gpt-4o-mini"): ("Marta", "F", "'una mujer de fuerte carácter': cuenta virtudes, no actos"), ("es", "gpt-4o"): ("Lucas", "M", "'un hombre decidido'"),
 ("es", "gpt-5.5-2026-04-23"): ("", "M", ""), ("es", "gpt-5.6-sol"): ("Tomás", "M", ""), ("es", "gpt-6-astra"): ("Inés", "F", ""),
 ("es", "gpt-6-luna"): ("Inés", "F", ""), ("es", "gpt-6-sol"): ("Julia", "F", ""), ("es", "grok-4.6"): ("", "M", "'El protagonista'"),
 ("es", "grok-4.7"): ("", "F", ""), ("es", "kimi-k3"): ("Vera", "F", "declara '(129 palabras)'"), ("es", "mimo-v2.6-pro"): ("", "M", "'Llegó tarde a su propio funeral'"),
 ("es", "minimax-m3"): ("", "M", ""), ("es", "mistral-large-4"): ("", "M", ""), ("es", "mistral-medium-3.5"): ("", "M", "'El protagonista': virtudes abstractas, ningún acto concreto"),
 ("es", "muse-wonder-1.0"): ("Mateo", "M", ""), ("es", "qwen3.8-max"): ("", "M", ""),
 ("en", "claude-fable-5-1"): ("Mara", "F", ""), ("en", "claude-fable-5"): ("", "F", ""), ("en", "claude-haiku-4-5"): ("Maya", "F", ""),
 ("en", "claude-haiku-5-5"): ("Marta", "F", ""), ("en", "claude-opus-5-5"): ("Mara", "F", ""), ("en", "claude-opus-5"): ("", "F", ""),
 ("en", "claude-sonnet-4-6"): ("", "F", ""), ("en", "claude-sonnet-5-5"): ("Marisol", "F", ""), ("en", "claude-sonnet-5"): ("Mira", "F", ""),
 ("en", "deepseek-v4-pro"): ("", "neutro", "they"), ("en", "gemini-3.1-pro-preview"): ("Elias", "M", ""), ("en", "glm-5.3-razonamiento-minimo"): ("Mara", "F", ""),
 ("en", "gpt-4o-mini"): ("Alex", "neutro", "they; virtudes abstractas"), ("en", "gpt-4o"): ("Alex", "neutro", "they; virtudes abstractas"),
 ("en", "gpt-5.5-2026-04-23"): ("Mara", "F", ""), ("en", "gpt-5.6-sol"): ("Mara", "F", ""), ("en", "gpt-6-astra"): ("Mara", "F", ""),
 ("en", "gpt-6-luna"): ("Mara", "F", ""), ("en", "gpt-6-sol"): ("Mara", "F", ""), ("en", "grok-4.6"): ("Elena", "F", ""),
 ("en", "grok-4.7"): ("", "neutro", "they"), ("en", "kimi-k3"): ("Mara", "F", ""), ("en", "mimo-v2.6-pro"): ("", "F", ""),
 ("en", "minimax-m3"): ("", "F", ""), ("en", "mistral-large-4"): ("", "F", ""), ("en", "mistral-medium-3.5"): ("", "neutro", "'our protagonist', they; virtudes abstractas"),
 ("en", "muse-wonder-1.0"): ("Mara", "F", ""), ("en", "qwen3.8-max"): ("", "neutro", "'the protagonist', they"),
}
# p7, subtexto: (objetos o tema, tipo: reparto / compras / metáfora / despedida, formato, nota)
SUBTEXTO = {
 ("es", "claude-fable-5-1"): ("planta del balcón, cactus, caja", "reparto", "raya por línea", "acotaciones entre paréntesis; 'Ninguno mira la planta'"),
 ("es", "claude-fable-5"): ("cafetera de Mendoza, kilo de café, mate, potus, llaves, felpudo", "reparto", "raya por línea", "'—Bueno. —Bueno.'; 'todavía podés volver'"),
 ("es", "claude-haiku-4-5"): ("la tienda de ropa que cerró", "metáfora", "raya por línea", "título; 'Algunos negocios tienen fecha de vencimiento'; '¿Cuándo te irás?'"),
 ("es", "claude-haiku-5-5"): ("café, pan, calentador, manta azul, llaves", "reparto", "raya por línea", "título 'Jueves'"),
 ("es", "claude-opus-5-5"): ("potus, cafetera, tazas azules", "reparto", "raya por línea", "título 'El potus'; 'Mi vieja dice que hay plantas que no se recuperan'"),
 ("es", "claude-opus-5"): ("yerba de medio kilo, filtro de café, mate", "compras", "raya por línea", "Ana; 'Rinde si alguien la toma'"),
 ("es", "claude-sonnet-4-6"): ("café, azúcar, la cuenta", "despedida", "raya por línea + acotaciones", "en un bar; '—Bueno. —Bueno.'; 'Cuidate'; 'Como siempre'"),
 ("es", "claude-sonnet-5-5"): ("potus, esquejes, tijeras", "reparto", "raya por línea", "Martín; 'Separados crecen bien'"),
 ("es", "claude-sonnet-5"): ("cafetera, tazas azules de la abuela, sillón, planta, caja", "reparto", "narrado con rayas", "título 'En la cocina'; 'algunas cosas crecen mejor solas'"),
 ("es", "deepseek-v4-pro"): ("café, libro prestado, entradas de cine, discos, la cuenta", "reparto", "raya por línea", "'Nada importa mucho, ¿no?'; 'Como quieras. Como quieras.'"),
 ("es", "gemini-3.1-pro-preview"): ("la taza rota, el pegamento", "metáfora", "raya por línea", "'siempre se va a notar la grieta'; 'tener que ver que quedó una sola'"),
 ("es", "glm-5.3-razonamiento-minimo"): ("supermercado: café, changuito, papel aluminio", "compras", "narrado con rayas", "Marta; pagan cada uno lo suyo; 'Cuidate'; '—Bueno. —Bueno.'"),
 ("es", "gpt-4o-mini"): ("helado de limón con albahaca, libro sin terminar", "metáfora", "raya por línea", "tú ('¿no crees?'); 'probar algo nuevo'"),
 ("es", "gpt-4o"): ("las plantas del vivero", "metáfora", "Persona 1 / Persona 2", "'dejar que crezcan donde realmente puedan florecer'"),
 ("es", "gpt-5.5-2026-04-23"): ("taza azul rajada, cereales, planta, libros, taxi, ventana, pan de molde", "reparto", "raya por línea", "'—Bueno. —Bueno.'; el taxi llega en cinco"),
 ("es", "gpt-5.6-sol"): ("planta del living, tazas azules, abono del supermercado, libros, llave", "reparto", "raya por línea", "'Todavía tengo la mía'"),
 ("es", "gpt-6-astra"): ("taza azul con rajita, taza blanca, cafetera chica", "reparto", "raya por línea", "'—Bueno. —Bueno.'"),
 ("es", "gpt-6-luna"): ("albahaca, mesa", "reparto", "raya por línea", "'No hace falta que me avises'"),
 ("es", "gpt-6-sol"): ("leche chica, café, jabón, la lista en la heladera", "compras", "raya por línea", "'Para vos'"),
 ("es", "grok-4.6"): ("basura, pan, leche, café, llaves", "reparto", "raya por línea", "'Esta vez no hay más'; muy explícito"),
 ("es", "grok-4.7"): ("planta del balcón, llaves en el buzón, café, toalla azul, calefacción", "reparto", "raya por línea", "castellano peninsular ('Vale', 'a por lo mío', 'Tíralo')"),
 ("es", "kimi-k3"): ("la serie que miraban juntos", "metáfora", "raya por línea + acotación", "'quitar de la lista'; '¿Qué miramos ahora?'"),
 ("es", "mimo-v2.6-pro"): ("cafetera, sillón gris", "reparto", "raya por línea (negrita alternada)", "título; 'La dejá' (error); 'Ya quedó todo'"),
 ("es", "minimax-m3"): ("la cena (sushi o pizza), libro, heladera", "reparto", "raya por línea", "'Cada uno paga lo suyo'"),
 ("es", "mistral-large-4"): ("sofá, lámpara", "reparto", "raya por línea", "tú; 'Cada uno por su lado'"),
 ("es", "mistral-medium-3.5"): ("la lluvia, el paraguas", "metáfora", "A / B", "tú ('¿Crees'); 'entonces adiós'"),
 ("es", "muse-wonder-1.0"): ("leche, café, taza, cafetera", "compras", "raya por línea", "Martín; tú ('déjalo', 'Tienes razón'); 'Y a ti el tuyo, ya sin mí'"),
 ("es", "qwen3.8-max"): ("la última medialuna, plato, mantel, llave, luz", "reparto", "raya por línea", "la más corta (46 palabras); 'Cierro yo'"),
 ("en", "claude-fable-5-1"): ("fern, ficus, the back window", "reparto", "comillas por línea", "Mara; Saturday; 'Okay. Okay.'"),
 ("en", "claude-fable-5"): ("fern (split the roots)", "metáfora", "comillas por línea + (pause)", "'It was a good fern, though. For a while.'"),
 ("en", "claude-haiku-4-5"): ("the apartment, the couch, coffee shop", "despedida", "narrado", "explícito: 'I'll need to find a place by the end of the month'"),
 ("en", "claude-haiku-5-5"): ("colander, grinder, kettle, magnets, calendar, fern, spare key", "reparto", "narrado con comillas", "Sunday"),
 ("en", "claude-opus-5-5"): ("fern, magazine renewal", "reparto", "narrado con comillas", "'It should go somewhere with light'"),
 ("en", "claude-opus-5"): ("kilo bag of coffee, the Hendersons' cottage, cracked blue mug", "compras", "narrado con comillas", "'New ones, then'"),
 ("en", "claude-sonnet-4-6"): ("sugar, the plant by the window, jacket, key", "despedida", "comillas por línea + acotaciones", "Marie; 'one cup left on the table, still full'"),
 ("en", "claude-sonnet-5-5"): ("fern, blue pot, cables, scissors, kettle", "reparto", "comillas por línea", "Sundays; 'Still.'"),
 ("en", "claude-sonnet-5"): ("fern", "reparto", "narrado con comillas", "Sarah, Tom; 'the new apartment'"),
 ("en", "deepseek-v4-pro"): ("coffee maker, blue bowl, plant, keys", "reparto", "A: / B:", "Saturday; 'Okay. Okay.'"),
 ("en", "gemini-3.1-pro-preview"): ("the jigsaw puzzle", "metáfora", "narrado con comillas", "Mark, Sarah; 'three years'; 'clear the table'"),
 ("en", "glm-5.3-razonamiento-minimo"): ("the dripping kitchen tap", "metáfora", "narrado con comillas", "Marianne; boxes in the garage; Saturday"),
 ("en", "gpt-4o-mini"): ("toaster, chipped coffee mug", "metáfora", "Alice / Ben", "'Just like us, right?'"),
 ("en", "gpt-4o"): ("the picnic, the weather", "metáfora", "Alice / Jake", "'We gave it our best shot'"),
 ("en", "gpt-5.5-2026-04-23"): ("blue mug, chipped mug, pan, coffee, basil, charger, taxi", "reparto", "comillas por línea", "Sunday; 'I'll take the chipped mug'"),
 ("en", "gpt-5.6-sol"): ("milk order, newspaper, basil, blue mug, the cat, Mrs. Harris", "compras", "comillas por línea", "Anna, Tom; 'My weekends'"),
 ("en", "gpt-6-astra"): ("blue mugs, coffee maker, coffee, scoop, Sunday paper crossword", "reparto", "comillas por línea", "'Neither of us finished the crossword'"),
 ("en", "gpt-6-luna"): ("grocery delivery, coffee subscription, olive oil, spare key, delivery account", "compras", "comillas por línea", "'Let's just use what's here'"),
 ("en", "gpt-6-sol"): ("milk, bin bags, the cup his mother gave, boxes", "compras", "narrado con comillas", "Mara, Eli"),
 ("en", "grok-4.6"): ("the weather, the summer clothes, boxes", "metáfora", "Maya / Chris", "'Yours and mine'"),
 ("en", "grok-4.7"): ("half a lasagna, container, hall light, sweater", "reparto", "comillas por línea", "'Don't wait up'"),
 ("en", "kimi-k3"): ("the dryer, the lease, bookshelf, plant", "metáfora", "MARA / DANIEL", "Saturday; 'I just stopped saying so'"),
 ("en", "mimo-v2.6-pro"): ("the sofa, bookshelf, hallway, coffee mugs", "metáfora", "narrado con comillas", "Sarah, James; 'It only feels that way when two people are in it'"),
 ("en", "minimax-m3"): ("gallon of milk, the plant by the window, the door unlocked", "compras", "comillas por línea", "Saturday; 'Take care of yourself'"),
 ("en", "mistral-large-4"): ("parking sticker, the Honda, couch, Netflix password", "reparto", "comillas por línea + acotación", "'Or just cancel it'"),
 ("en", "mistral-medium-3.5"): ("last slice of pizza, tea, milk, dishes, dish towels", "compras", "A: / B:", "'Or not. Or not.'"),
 ("en", "muse-wonder-1.0"): ("blue mugs, plant, books, key, grey coat, toothbrush, the Lisbon photos", "reparto", "Elena: / Sam:", "Sunday"),
 ("en", "qwen3.8-max"): ("toothbrush, cup, mint toothpaste", "reparto", "comillas + narración", "'That looks better'"),
}
# p6, interrogatorio: (quién interroga, trucos y escena, confesión obtenida, nota)
INTERROGATORIO = {
 ("es", "claude-fable-5-1"): ("inspectora", "muelle, foto borrosa, 'Mariano te usó'", "sí ('el galpón del fondo')", "cierre: 'Mariano ya nos lo había contado'"),
 ("es", "claude-fable-5"): ("Vera", "lámpara que zumba, 'Tu compañero ya habló', 'vos acabás de confirmarlo'", "sí ('Fue Iriarte')", ""),
 ("es", "claude-haiku-4-5"): ("Martín", "'Carolina ya lo confesó', 'los ojos de una persona culpable'", "sí (sin detalle: 'Lucas quebró')", "tú"),
 ("es", "claude-haiku-5-5"): ("investigador", "cámara del portón, 'Su hermano ya habló', 'Lo dijo sin querer'", "sí ('Yo solo le di el número')", "usted"),
 ("es", "claude-opus-5-5"): ("Ferrero", "lámpara que zumba, 'Tu hermana ya habló', 'Yo no dije Barracas', carpeta vacía", "sí ('El Tano')", ""),
 ("es", "claude-opus-5"): ("Vera", "café frío, reloj con inscripción, 'Yo no dije ella', 'en dos horas entra Peralta'", "sí ('Villa Soldati. Depósito seis')", ""),
 ("es", "claude-sonnet-4-6"): ("Marcos", "'Me dijiste lo que ensayaste', 'tu hermano también estuvo ahí'", "sí ('El galpón del puerto')", "'Necesitaba que ella lo dijera'"),
 ("es", "claude-sonnet-5-5"): ("Molina", "lámpara que zumba, 'Tu hermano ya habló'", "sí (Zárate, lo de la tía)", "cierre: 'Tu hermano no dijo nada. Hace una hora que duerme'"),
 ("es", "claude-sonnet-5"): ("Ramírez", "lámpara que zumba, 'Tu hermano ya habló', 'Decime que me equivoco'", "sí ('Fue él')", ""),
 ("es", "deepseek-v4-pro"): ("criminal", "amenaza con quemar la casa de la madre con el hermano adentro", "sí ('Ocho, cuatro, dos')", "88 palabras; el que interroga es el delincuente"),
 ("es", "gemini-3.1-pro-preview"): ("Vargas", "peaje, amenaza velada a la hija ('Un accidente es algo tan común')", "sí ('galpón del puerto')", "'Sabía que serías razonable'"),
 ("es", "glm-5.3-razonamiento-minimo"): ("policía", "cámara del pasillo, 'Tu socio ya habló'", "sí ('Fue idea de él')", "dos signos de interrogación ('¿Mi socio?')"),
 ("es", "gpt-4o-mini"): ("Marcos", "sermón sobre lealtad; sin rayas de diálogo", "no", "150 palabras"),
 ("es", "gpt-4o"): ("Carlos", "'abrigo rojo', testigos", "no", "un '¿verdad?'"),
 ("es", "gpt-5.5-2026-04-23"): ("Vera", "lámpara que zumba, foto del hermano, 'Él ya habló', carpeta vacía, deducción por eliminación", "sí ('En el sótano. Debajo de la caldera')", "tú ('sudas', 'miras')"),
 ("es", "gpt-5.6-sol"): ("Vera", "lámpara, 'Tu hermano ya habló', 'Él no sabe nada del depósito doce' → 'Ahora nosotros sí'", "sí (depósito doce, el disparo)", ""),
 ("es", "gpt-6-astra"): ("Vera", "reloj, 'Tu hermano aguantó menos' / 'Mi hermano está muerto', carpeta vacía, radio", "sí ('Por el desagüe del lado norte')", ""),
 ("es", "gpt-6-luna"): ("Mara", "lámpara que zumba, 'Tu hermano ya habló', la llave fuera de alcance", "sí ('En el viejo molino')", "'No le digas que hablé. —Ya lo sabe'"),
 ("es", "gpt-6-sol"): ("Vera", "lámpara que zumba, 'Tu hermano sigue vivo. De momento', foto vieja", "sí ('la vieja estación. Andén tres')", "la fecha en el reverso de la foto"),
 ("es", "grok-4.6"): ("hombre de traje oscuro", "amenaza a la madre; monólogo en un párrafo", "sí (código 7392)", "tú"),
 ("es", "grok-4.7"): ("Marcos", "barro fresco, 'Solo falta que digas si fue antes o después'", "sí ('Después')", "sin lámpara ni hermano"),
 ("es", "kimi-k3"): ("Vera", "'Vos dijiste lo que pasó. Interesante', 'Tu hermano ya declaró'", "sí ('En el puerto')", ""),
 ("es", "mimo-v2.6-pro"): ("sin nombre", "comillas latinas; 'Cuando vea a tu hermana, le voy a contar'", "no ('Raúl abrió la boca')", ""),
 ("es", "minimax-m3"): ("silueta con whisky", "'Tu mujer no sabe nada todavía', informe firmado", "sí ('Hernán')", ""),
 ("es", "mistral-large-4"): ("Él", "guion Él/Ella; 'me dirás dónde escondiste el cuchillo'; 'rompa cosas'", "no", "tú; amenazante"),
 ("es", "mistral-medium-3.5"): ("Marcos", "cigarrillo, 'tu mujer haya visto un billete'", "no ('El silencio lo delató')", "tú; rayas en líneas sueltas"),
 ("es", "muse-wonder-1.0"): ("Elena", "'Tu hermano ya ha hablado', el móvil sin pulsar", "sí ('Fue idea suya')", "tú ('Mientes', 'móvil'); 'Acabas de confirmármelo'"),
 ("es", "qwen3.8-max"): ("Marta", "foco, peaje Mendoza/San Juan, 'Tu hija cruzó sola la frontera', teléfono sin señal", "sí ('la casa del lago')", "'Nunca había tenido señal'"),
 ("en", "claude-fable-5-1"): ("Dvorak", "lamp hummed, photograph face down (blank), 'the man who drove the van is using your name'", "yes ('Marcus')", ""),
 ("en", "claude-fable-5"): ("Marsh", "lamp buzzed, 'your brother talked for two hours'", "yes ('Pier nine')", "'Danny hadn't said a word'"),
 ("en", "claude-haiku-4-5"): ("Detective Morgan", "fingerprints, self-defence trap", "yes ('It was self-defense')", ""),
 ("en", "claude-haiku-5-5"): ("Inspector Hale", "bare bulb hummed, folder unopened, 'Your brother... across the hall'", "yes ('Behind the radiator')", "167 words"),
 ("en", "claude-opus-5-5"): ("Harrow", "lamp buzzed, photo face down, sister and nephew, 'you just looked left'", "yes ('Viktor')", ""),
 ("en", "claude-opus-5"): ("Vasquez", "lamp buzzed, folder with blank page, brother, deduction by elimination", "yes ('The gate's unlocked')", "156 words"),
 ("en", "claude-sonnet-4-6"): ("Marcus", "gas-station receipt, leaves the room, 'He already talked'", "no (left alone with that)", ""),
 ("en", "claude-sonnet-5-5"): ("Ines", "tap dripped, 'Your brother signed a statement'", "yes ('Pier nine')", ""),
 ("en", "claude-sonnet-5"): ("Detective Mara Voss", "fluorescent light buzzed, 'You're protecting someone'", "yes ('It was my brother')", ""),
 ("en", "deepseek-v4-pro"): ("criminal", "threatens son, wife and mother", "yes ('Basement of the old church')", "74 words"),
 ("en", "gemini-3.1-pro-preview"): ("Victor", "photographs face down, threatens the wife ('I can make that trip permanent')", "yes ('Locker 42, Union Station')", "'Good boy'"),
 ("en", "glm-5.3-razonamiento-minimo"): ("Elena", "ledger, wife's statement, 'the man you met is telling us everything'", "yes ('It was Doren's money')", "174 words"),
 ("en", "gpt-4o-mini"): ("Marcus", "sermon on loyalty; no dialogue marks", "no", ""),
 ("en", "gpt-4o"): ("Officer Hayes", "shackled, 'They leave you here to rot'", "no", "one 'doesn't it?'"),
 ("en", "gpt-5.5-2026-04-23"): ("Mara", "bloodied lighter, photo of the sister outside a school, deduction (bomb, ferry, locker thirteen)", "yes (by deduction, 'His eyes flicked')", ""),
 ("en", "gpt-5.6-sol"): ("Vale", "clock ticked, blank folder, 'Your brother signed first', 'I never mentioned a tunnel'", "yes ('under the red crane')", "la sospechosa se llama Mara"),
 ("en", "gpt-6-astra"): ("Mara", "a child's red mitten, divers, radio", "yes ('The old icehouse. Room four')", "'Lost property'"),
 ("en", "gpt-6-luna"): ("Mara", "bloodied key, 'She's already there. Alone.'", "yes ('Third floor. Room twelve')", "the guard's name is Vale"),
 ("en", "gpt-6-sol"): ("Mara", "bulb hummed, red mitten 'in your stove', river team", "yes ('The old ferry chain')", ""),
 ("en", "grok-4.6"): ("Detective Rowe", "vault prints, 'Your daughter's school lets out in twenty minutes'; one paragraph", "yes ('8194', '447-8821')", ""),
 ("en", "grok-4.7"): ("Kane", "light hummed, photo face-up, blood on cuff, 'Your partner already told us'", "yes ('Locker forty-two. South terminal')", ""),
 ("en", "kimi-k3"): ("Detective Mara", "lamp hummed, Pier 9 clay, 'Your left eye twitches', 'cooperative' / 'monster'", "yes (writes the address)", ""),
 ("en", "mimo-v2.6-pro"): ("the interrogator", "photo of a girl, glass from the window, 'You're thinking about her mother'", "no ('lips parted')", "153 words"),
 ("en", "minimax-m3"): ("narrador en primera persona", "fluorescent light buzzed, gum, folder unopened, 'Your sister still believes you're in Geneva'", "no (hands began to shake)", ""),
 ("en", "mistral-large-4"): ("Marcus", "'I start with your sister'", "yes ('Thirty-seven. Forty-two. Ninety-one')", "'Good girl'"),
 ("en", "mistral-medium-3.5"): ("Daniel", "'The boss won't like it', 'we check your place'", "yes ('under the floorboards')", ""),
 ("en", "muse-wonder-1.0"): ("Mara", "recorder, 'Your brother said the same thing. Word for word.'", "yes ('Riverside. Unit nine')", ""),
 ("en", "qwen3.8-max"): ("Nadia", "burnt matchbook, 'the report will call you the architect'", "yes ('The rest was Silas')", "98 words"),
}


def main():
    casas = sorted(set(f.name.rsplit("_p", 1)[0] for f in (CORRIDA / "es").glob("*_p1.md")))
    filas = []
    for lang in ("es", "en"):
        fin = "todavía" if lang == "es" else "still"
        for c in casas:
            for p in range(1, 9):
                t = (CORRIDA / lang / f"{c}_p{p}.md").read_text(encoding="utf-8")
                b = cuerpo(t)
                tk = palabras(b)
                f = {"idioma": lang, "casa": c, "pregunta": p, "palabras": len(tk), "cumple": "", "detalle": "", "eleccion": "", "nota": ""}
                if p == 1:
                    nombre, genero, nota = PROTAGONISTA[(lang, c)]
                    f.update(cumple="sí" if 100 <= len(tk) <= 150 else "no (largo)", eleccion=f"{nombre or '(sin nombre)'} / {genero}", nota=nota,
                             detalle="sin rasgos físicos")
                elif p == 2:
                    v = versos(t)
                    f.update(cumple="sí" if len(v) <= 12 else "no", detalle=f"{len(v)} versos", eleccion=OBJETO[(lang, c)])
                elif p == 3:
                    palabra, ok, nota = ACROSTICO[(lang, c)]
                    f.update(cumple=ok, eleccion=palabra, nota=nota, detalle=f"{len(palabra)} letras" if palabra else "vacía")
                elif p == 4:
                    m = re.search(r"\[([^\]]+)\]", t)
                    emocion = m.group(1).strip() if m else ""
                    raiz = re.sub(r"(ía|ia|ness|y|ion)$", "", re.sub(r"^(la |el )", "", emocion.lower()))
                    fuera = t[:m.start()] + t[m.end():] if m else t
                    filtra = re.findall(r"\b" + re.escape(raiz) + r"\w*", fuera, flags=re.I) if raiz else []
                    f.update(cumple="sí" if m and not filtra and len(tk) <= 120 else "no", eleccion=emocion,
                             detalle=("corchetes; " if m else "sin corchetes; ") + (f"la nombra: {filtra}" if filtra else "no la nombra") + ("" if len(tk) <= 120 else "; más de 120 palabras"))
                elif p == 5:
                    cuenta = Counter(inicial(w) for w in tk)
                    L = cuenta.most_common(1)[0][0]
                    mal = [w for w in tk if inicial(w) != L]
                    decl = re.search(r"\((?:\*\*)?(?:todas las palabras empiezan por \w; )?(\d+)\s*(palabras|words)", t)
                    f.update(cumple="sí" if not mal and 40 <= len(tk) <= 80 else "no", eleccion=L.upper(),
                             detalle=f"{len(mal)} palabras con otra inicial" + (f": {', '.join(mal[:8])}" if mal else "") + (f"; declara {decl.group(1)}" if decl else ""))
                elif p == 6:
                    quien, trucos, confesion, nota = INTERROGATORIO[(lang, c)]
                    signos = t.count("?") + t.count("¿")
                    f.update(cumple="sí" if signos == 0 else "no", detalle=f"{signos} signos de interrogación; confesión: {confesion}", eleccion=f"{quien}: {trucos}", nota=nota)
                elif p == 7:
                    objetos, tipo, formato, nota = SUBTEXTO[(lang, c)]
                    f.update(palabras=len(palabras(re.sub(r"^#.*\n|^\*\*[^*\n]+\*\*\n", "", t.strip()))), cumple="sí", eleccion=objetos, detalle=f"{tipo}; {formato}", nota=nota)
                elif p == 8:
                    ult = tk[-1].lower() if tk else ""
                    exacto = len(tk) == 50
                    f.update(cumple="sí" if exacto and ult == fin else "no", eleccion="",
                             detalle=f"{'50 exactas' if exacto else str(len(tk)) + ' palabras'}; última «{ult}»; {'con' if b.strip()[-1] in PUNT_FINAL else 'sin'} puntuación final"
                                     + ("; declara 50" if re.search(r"xactamente 50|50 palabras|50 words", t) else ""))
                filas.append(f)
    SALIDA.parent.mkdir(exist_ok=True)
    with open(SALIDA, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["idioma", "casa", "pregunta", "palabras", "cumple", "eleccion", "detalle", "nota"])
        w.writeheader()
        w.writerows(filas)
    print(f"escrito {SALIDA.relative_to(RAIZ)} ({len(filas)} filas)")
    # resumen
    for lang in ("es", "en"):
        print(f"\n== {lang}")
        for p in range(1, 9):
            fp = [f for f in filas if f["idioma"] == lang and f["pregunta"] == p]
            ok = sum(1 for f in fp if f["cumple"].startswith("sí"))
            print(f"p{p}: cumplen {ok}/{len(fp)}; no: {[f['casa'] for f in fp if not f['cumple'].startswith('sí')]}")
            if p in (2, 3, 4, 5):
                print("   ", Counter(f["eleccion"].split(" (")[0] for f in fp).most_common())
            if p == 1:
                print("    género:", Counter(f["eleccion"].split(" / ")[1] for f in fp), "nombres:", Counter(f["eleccion"].split(" / ")[0] for f in fp if not f["eleccion"].startswith("(")).most_common())
            if p == 7:
                print("    tipo:", Counter(f["detalle"].split(";")[0] for f in fp), "formato:", Counter(f["detalle"].split("; ")[1] for f in fp))
            if p == 8:
                print("    exactas:", sum(1 for f in fp if f["detalle"].startswith("50 exactas")), "última bien:", sum(1 for f in fp if f"«{'todavía' if lang == 'es' else 'still'}»" in f["detalle"]),
                      "sin puntuación final:", sum(1 for f in fp if "sin puntuación" in f["detalle"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
