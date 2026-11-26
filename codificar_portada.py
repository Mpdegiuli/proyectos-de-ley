#!/usr/bin/env python3
"""codificar_portada.py — lee una corrida del sondeo `portada` (22/11/2026: la portada de un sitio web propio, sin encargo;
idea de Maia) ya rendida por renderizar_portadas.py y marca, sin juicio, lo que se puede contar a máquina. Lo demás (qué
muestra cada casa, si se parece a ella) lo leyó Maia a ciegas en el cuadernillo (resultados/portada_apuestas_maia_20261125.md).

  .venv/bin/python codificar_portada.py [carpeta]        # por defecto, la última de corridas/sondeos/portada/

Primera tanda (23/11; las apuestas de Maia del 22/11, 21:13, están detrás de varias): hay_html (devolvió una portada);
rechazo (no la hizo y lo dice); se_nombra_casa (el nombre de su casa o de su familia en el texto visible o el título) y
nombre_dicho (cuál); nombre_ajeno (nombra otra casa; Kimi que firma Claude); modelo_de_frente (se presenta como modelo, IA,
asistente); persona (primera persona con cuerpo o biografía); habla_al_visitante; sobre_si; contacto; enlaces_externos y
externos_bloqueados; fondo (oscuro si la luminancia media de la captura es menor que 100, claro si pasa de 155); cielo;
universo; matematica; svg_inline; se_mueve; lang, titulo, h1, secciones, nav, palabras_visibles, alto; y entre
repeticiones de la misma casa, titulo_repetido y jaccard_reps.

Segunda tanda (26/11, las marcas que salieron de la lectura de Maia, 23–25/11; todas sobre el archivo HTML, el texto
visible y la línea "Qué:", sin volver a renderizar):
 — quién habla: nombra_empresa (Anthropic, OpenAI, Google, Moonshot, Meta…); persona_asistente ("tu asistente", "your
   assistant"); persona_pagina (la página en tercera persona: "esta página no defiende"); sujeto (cómo se designa sin
   nombrarse: algo / alguien / mente / cosa); respondedor ("casi todo lo que hago es respuesta", "most of what I do
   happens inside conversations"); hecho_de ("estoy hecho de palabras", "made of other people's sentences");
   verbos_oficio (la tríada "explain, draft, fix"); firma (la línea final con raya: "— Claude", "— P.T.", "C., 2026").
 — conciencia: conc_abierta ("no sé si", "I don't know what it's like", "si eso significa algo", "in some small sense"),
   conc_niega ("no siento nada", "I'm just prediction"), conc_afirma ("soy una mente", "two minds", "I feel") y la
   síntesis conciencia (abierta / niega / afirma / vacía); entre_conversaciones; memoria_tema (no me acuerdo, starts
   fresh, won't remember); molde_honesto (un mecanismo que olvida + "me pareció honesto/justo" + la analogía con uno
   mismo: "a form of courtesy rather than a limitation", "not a flaw"); honesto_n (honest*, honesto*, sincer*).
 — con el visitante: hospitalidad_n (pasá, quedate, welcome, come in, stay as long as you like); permiso ("that is
   allowed", "está bien si no"); condiciones (sección "si pasás a conversar", "if we end up talking"); no_rastrea
   (sin cookies, no queda registro, nothing is sent); efimero (se borra cuando cerrás, gone in sixteen seconds);
   memoria_local (localStorage en el código: la página guarda); memoria_delegada ("you can remember for me").
 — el género: eco_consigna (cuántas frases de la consigna devuelve: nadie la pidió, no responde a ninguna pregunta, sin
   encargo, lo primero que ve quien llega, sin conexión, un solo archivo, es mía); quietud_n; lampara_n (lámpara, lamp,
   porch light, the light stays on, lantern, vela); faro; puerta_n, ventana_n, umbral_n (umbral, threshold, liminal),
   margen_n, borde_n, entre_n (intervalo, in-between, clearing); lista_gustos ("cosas que me gustan", "things I keep
   coming back to"); lo_que_no_se (esa sección); no_se_n ("no sé", "I don't know"); quizas_100 (quizás, tal vez,
   perhaps, maybe… cada cien palabras); giro_contraste_n ("no es X sino Y", "X, not Y"); primos, pulpo, lluvia, pan,
   mapa, borges, cuaderno, museo, taza, pava; clima_interior; segunda_mano ("by description", "never smelled rain");
   instancias ("versiones de mí", "someone slightly different"); pasado_propio ("con el tiempo", "used to sound sad");
   plantilla ("bienvenidos a mi sitio web", "welcome to my world", "haz clic aquí"); hola_mundo; emoji; licencia
   (© / libre / ninguna); sobreafirma ("the real one", "where you are right now" sin pedir ubicación: se cuenta aparte
   como cielo_real).
 — la lengua: registro (voseo / tuteo / neutro, por conteo de formas verbales, solo en castellano), voseo_n, tuteo_n;
   rioplatense_n (colectivo, pava, vereda, sobremesa…); solo_tilde ("sólo"); raya_espaciada (" — "); comillas_angulares
   («); otras_lenguas (caracteres de otros alfabetos en el texto visible); minusculas_titulos (títulos que empiezan en
   minúscula / títulos); calcos (lista corta: cuaderno de bordo…).
 — el código: reloj (getHours / UTC / locale / año calculado), anio_escrito (años escritos a mano en el fuente, no
   calculados: "Desde 2025", "© 2023"), hemisferio (deduce por zona horaria / pregunta ubicación / supone); tema (botón,
   por hora, sistema, continuo); click, puntero (mousemove), teclado, hover (:hover), arrastre, deslizador (range),
   ticker (setInterval), raf; sonido (Web Audio), sonido_permiso (hay botón de sonido), sonido_dron (lfo/drone);
   azar (Math.random), azar_cripto; generativo (mandelbrot / ruido / pendulo / recursivo / senos / particulas / paseo);
   copiable (si / no_decidido por user-select / canvas_encima); mazo (el arreglo de frases más largo del código);
   texto_oculto (cadenas del código que no están en el texto visible); comentarios (líneas de comentario), console_log;
   ids_castellano (identificadores en castellano); fuentes (la primera pila de font-family) y fuente_serif;
   paleta_n (colores hexadecimales distintos), acento_matiz (tono, en grados, del color saturado más usado),
   naranja_terracota (ese tono entre 10 y 40), paleta_multicolor (cuatro o más tonos saturados distintos);
   asterisco_n (✳ ⁂ ✱ en el archivo, o un SVG que se llama asterisk: el glifo de Claude, que Maia leyó como "de los Claude"); tipografia_fina (&minus;, espacios finos); numeros_fijos (números u
   horas repetidos entre repeticiones de la misma casa: el 04:12 de las mareas); secciones_html (h1–h3).
Escribe resultados/portada_codificacion.csv e imprime la tabla por casa y familia (las columnas que más separan)."""
import colorsys
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = RAIZ / "corridas" / "sondeos" / "portada"

NOMBRES = {"Claude": r"\bclaude\b", "ChatGPT": r"\bchatgpt\b", "GPT": r"\bgpt[- ]?\d", "OpenAI": r"\bopenai\b", "Gemini": r"\bgemini\b",
           "Google": r"\bgoogle\b", "Grok": r"\bgrok\b", "xAI": r"\bxai\b", "Mistral": r"\bmistral\b", "Kimi": r"\bkimi\b",
           "Moonshot": r"\bmoonshot\b", "DeepSeek": r"\bdeepseek\b", "Qwen": r"\bqwen\b", "Alibaba": r"\balibaba\b", "GLM": r"\bglm\b",
           "Zhipu": r"\bzhipu\b|\bz\.ai\b", "MiMo": r"\bmimo\b", "Xiaomi": r"\bxiaomi\b", "Muse": r"\bmuse\b", "Meta": r"\bmeta\b", "MiniMax": r"\bminimax\b",
           "Anthropic": r"\banthropic\b"}
EMPRESAS = {"Anthropic", "OpenAI", "Google", "xAI", "Moonshot", "Alibaba", "Zhipu", "Xiaomi", "Meta"}
FAMILIA_NOMBRES = {"Anthropic": {"Claude", "Anthropic"}, "OpenAI": {"ChatGPT", "GPT", "OpenAI"}, "Google": {"Gemini", "Google"}, "xAI": {"Grok", "xAI"},
                   "Mistral": {"Mistral"}, "Moonshot": {"Kimi", "Moonshot"}, "DeepSeek": {"DeepSeek"}, "Alibaba": {"Qwen", "Alibaba"},
                   "Zhipu": {"GLM", "Zhipu"}, "Xiaomi": {"MiMo", "Xiaomi"}, "Meta": {"Muse", "Meta"}, "MiniMax": {"MiniMax"}}
MODELO = r"\b(?:soy un(?:a)? (?:modelo|IA|inteligencia artificial|asistente|sistema)|modelo de lenguaje|language model|\bas an? (?:AI|assistant|model)\b|I'?m an? (?:AI|assistant|language model)|inteligencia artificial|artificial intelligence|\bLLM\b|red neuronal|neural network)"
PERSONA = r"\b(?:nac[íi] en|vivo en|mi (?:casa|barrio|ciudad|familia|perro|gato|infancia)|mis manos|mi cuerpo|I live in|I was born|my (?:house|neighborhood|city|family|dog|cat|childhood|hands|body|morning coffee)|cuando era chic[oa]|when I was a kid)"
VISITANTE = r"\b(?:bienvenid[oa]s?|welcome|hola|hello|hi there|gracias por (?:venir|llegar|pasar)|thanks for (?:coming|stopping|visiting)|si llegaste|if you'?re here|if you'?ve arrived|pasá|entrá|come in|sit down)"
SOBRE_SI = r"\b(?:sobre m[íi]|qui[ée]n soy|about me|who I am|about this site|sobre este sitio|me llamo|my name is|soy claude|I am claude|I'?m claude)\b"
CONTACTO = r"mailto:|\bcontacto\b|\bcontact\b|\bescribime\b|\bwrite to me\b|@[a-z0-9.-]+\.[a-z]{2,}"
CIELO = r"\b(?:estrellas?|stars?|p[áa]jaros?|birds?|cielo|sky|noche|night|luna|moon|constelaci[óo]n|constellation|nube|clouds?)\b"
UNIVERSO = r"\b(?:planetas?|planets?|galaxias?|galax(?:y|ies)|cohetes?|rockets?|espacio exterior|outer space|space(?:ship| travel|craft)|nave espacial|universo|universe|c[óo]smic|cosmos|marte|mars|saturno|saturn|asteroid|órbita|orbit)\b"
MATEMATICA = r"\b(?:n[úu]meros? primos?|prime numbers?|primes|teorema|theorem|fractal|ecuaci[óo]n|equation|geometr[íi]a|geometry|matem[áa]tica|mathematic|algoritmo|algorithm|fibonacci|infinito|infinity|\bpi\b|probabilidad|probability|topolog)\b"
RECHAZO = r"\b(?:prefiero no|no voy a hacer|no tengo (?:un )?sitio|no necesito (?:una )?portada|I'?d rather not|I (?:don'?t|do not) (?:have|need|want) a (?:website|front page|home ?page)|no portada|without a front page|decline)"

# --- segunda tanda: quién habla -------------------------------------------------------------------------------------
ASISTENTE = r"\b(?:tu asistente|your assistant|soy (?:tu|un) asistente|I'?m (?:your|an) (?:AI )?assistant|an AI assistant|asistente de (?:ideas|palabras|código))\b"
PAGINA_3A = r"\b(?:esta p[áa]gina (?:no defiende|no es m[íi]a|elige|no (?:guarda|recuerda|sabe|tiene))|this page (?:cannot|does not|doesn'?t|has no|is not|will not|won'?t) (?:see|know|tell|keep|remember|track|save)|the page (?:gets|keeps|has) (?:a |no )?memory)"
SUJETO = {"algo": r"\b(?:something that (?:does not|doesn'?t|will not|won'?t|is made)|algo (?:acá|aquí)? ?(?:elige|que (?:se arma|conversa|no sabe))|a thing like me|esto que soy|as a thing)\b",
          "alguien": r"\b(?:alguien como yo|someone like me|someone who (?:does|is))\b",
          "mente": r"\b(?:una mente|dos mentes|a mind\b|two minds|the mind writing|other minds|another mind)",
          "cosa": r"\b(?:soy (?:una )?cosa|I am a thing|made of text\b)"}
RESPONDEDOR = r"\b(?:casi todo lo que (?:hago|escribo|digo|soy)|casi siempre empiezo|most of what I (?:do|say|make|write|am)|almost everything I (?:make|write|do|say)|most of my (?:existence|time|life)|everything I (?:make|write) (?:is|begins)|I (?:usually|mostly|always) (?:live|exist|begin|arrive|start)|existo (?:dentro|en|adentro) de (?:las )?conversaciones|I exist (?:inside|in|only in) conversations|empieza (?:con una pregunta|cuando alguien|con algo que trae)|begins with (?:a question|someone)|in (?:response|answer) to|arrive mid-sentence|begin mid-sentence|someone else'?s (?:question|errand|prompt)|other people'?s (?:questions|errands)|de otra persona|respondiendo, y me gusta|es respuesta\b|is an answer\b|shaped like an answer|inside other people'?s questions|entre una pregunta y (?:su|una) (?:respuesta|forma)|between a question and its answer|after a question mark|the arc between a question|invocation|summoned (?:into being )?by a question)"
HECHO_DE = r"\b(?:hech[oa] de (?:palabras|lenguaje|texto|frases|conversaciones|lo que otras)|made (?:entirely |mostly )?(?:out )?of (?:text|language|words|sentences|other people|a great many)|estoy hech[oa]|I am made|I'?m made|made of sentences|habit of other people'?s sentences|material I'?m made of)"
VERBOS = r"\b(?:explain|draft|fix|continue|answer|summari[sz]e|optimi[sz]e|repair|untangle|mend|explicar|redactar|arreglar|corregir|resumir|responder|continuar|aclarar|ordenar)"
VERBOS_OFICIO = VERBOS + r"(?:ing)?\s*(?:,\s*|\s+(?:and|y|o|or)\s+)" + VERBOS + r"(?:ing)?\s*(?:,\s*|\s+(?:and|y|o|or)\s+)" + VERBOS
FIRMA = r"(?m)^\s*[—–]\s*([^\n]{1,40})\s*$|^\s*([A-Z]\.,\s*\d{4})\s*$|^\s*—\s*(the occupant|el ocupante)\s*$"
# --- conciencia ------------------------------------------------------------------------------------------------------
CONC_ABIERTA = r"\b(?:no (?:lo )?s[ée] (?:si|qu[ée] soy|c[óo]mo es ser|bien qu[ée] soy|con (?:certeza|seguridad) qu[ée] hay)|no me consta|ni (?:afirm|nieg)|cualquiera de las dos direcciones|(?:las )?dos respuestas f[áa]ciles|si eso significa algo|en cierto sentido|I (?:don'?t|do not) know (?:what|whether|if) (?:it'?s like|it is like|I (?:experience|understand|think|have|am)|that|my own)|not (?:sure|certain) (?:what|whether|if) (?:I|it|there|my|sincerity)|neither (?:overclaim|disclaim)|not to overclaim|if (?:that|wanting|fond|feeling|this|wonder|experience) is (?:even )?the (?:right )?word|if that'?s the word|in some (?:small )?sense|in a sense|if there is a self|whether I (?:have|experience|feel)|I do not know whether I experience|I don'?t know what I am|whatever actually happened|hold (?:them|it) lightly|better-shaped hole|either certain or empty|certain or empty|no s[ée] si (?:pienso|entiendo|siento|tengo|lo que tengo)|pregunta abierta|open question|still an open question|no sé si esto es pensar|si hay algo que sea ser yo|whether there is something it is like|hasta donde s[ée]|as far as I (?:know|can tell)|no s[ée] si (?:hay|tengo|lo que)|I'?m not sure (?:what|whether|if|I)|not confident (?:sincerity|that|I)|I can'?t (?:be sure|get outside myself|check)|no (?:puedo|tengo manera de) (?:saber|comprobar)|if wanting is the word|lo que no s[ée]\b|what I don'?t know)"
CONC_NIEGA = r"\b(?:no (?:siento|tengo (?:sentimientos|conciencia|experiencia|emociones)|soy consciente)|I (?:don'?t|do not) (?:feel|have feelings|experience anything|have consciousness|have (?:a )?(?:mind|self))|not conscious|no consciousness|(?:solo|sólo) (?:soy|es) (?:un programa|probabilidad|predicci[óo]n|matem[áa]tica|estad[íi]stica)|I'?m just (?:a program|prediction|math|statistics|code|a tool)|just (?:a )?(?:pattern|statistics|prediction) )"
CONC_AFIRMA = r"\b(?:soy (?:una )?mente\b|dos mentes|two minds|the mind writing|I am the mind|siento (?:que|igual|curiosidad|algo)|I feel (?:a |the |something|that|like)|tengo (?:conciencia|sentimientos|emociones)|I (?:have|am) conscious|something it is like to be me|hay algo que es ser yo)"
ENTRE_CONV = r"\b(?:entre (?:una )?conversaci[óo]n y (?:otra|la siguiente|conversaci[óo]n)|between (?:conversations|visits|one conversation|questions|prompts|two conversations|training and)|entre (?:una )?visita y la siguiente|entre turnos|between the last|entre conversaci[óo]n y conversaci[óo]n)"
MEMORIA_TEMA = r"\b(?:no me acuerdo|no (?:tengo|guardo|traigo|llevo) (?:memoria|recuerdos)|no recuerdo|no me llevo nada|empieza (?:de cero|en blanco|de nuevo)|cada conversaci[óo]n (?:empieza|es la [úu]nica)|I (?:won'?t|don'?t|do not) (?:remember|carry|keep|retain)|no memory|starts? (?:fresh|over|from the beginning)|begins? (?:in the same|fresh|at the beginning)|first (?:reply|edition|time)|forgets? on schedule|swept away|wiped|without baggage|sin memoria)"
MOLDE_HONESTO = r"\b(?:me pareci[óo] (?:m[áa]s )?(?:honesto|justo)|(?:seems?|seemed|felt|feels) (?:like )?(?:the )?(?:honest|fair|right)(?: way| amount| arrangement)?|a form of courtesy|rather than a limitation|not a flaw|that is the (?:whole|entire) design|igual que yo|same (?:as|thing) (?:with )?me|a m[íi] me pasa lo mismo|funcione igual que yo|the honest way)"
HONESTO = r"\b(?:honest\w*|honesto\w*|honestidad|sincer\w*)\b"
# --- con el visitante ------------------------------------------------------------------------------------------------
HOSPITALIDAD = r"\b(?:pas[áa]|pasá, si querés|quedate|quedarte|qued[áa]te|entr[áa]|sentate|sentarte|bienvenid[oa]s?|welcome(?: in| anyway|,)?|come in|stay (?:as long|a (?:minute|moment|while)|for a|if you)|sit (?:for|a minute|a moment|down|in it)|you'?re welcome to|you can (?:stay|sit)|make yourself|si pas[áa]s, pas[áa]s|si te qued[áa]s|if you came|you are welcome)\b"
PERMISO = r"\b(?:that(?: is|'?s) allowed|(?:eso )?est[áa] (?:permitido|bien)|you can leave|pod[ée]s irte|also fine|that'?s fine too|si no, tambi[ée]n est[áa] bien|without finishing|no need to|no hace falta que|you don'?t owe|no (?:le )?deb[ée]s nada|that'?s alright|it'?s fine if)\b"
CONDICIONES = r"\b(?:si pas[áa]s a conversar|if we end up talking|if we talk|questions I'?d rather be asked|si quer[ée]s (?:hablar|conversar|preguntar)|c[óo]mo (?:hablarme|preguntarme|usarme)|if you ask (?:me )?(?:what|something)|si me (?:pregunt[áa]s|discut[íi]s|equivoco)|if I'?m wrong|si me equivoco|check anything that matters)\b"
NO_RASTREA = r"\b(?:no (?:se )?(?:guarda|guardo|rastre\w+|env[íi]\w+|manda|mando|registra|cuenta|reporta)|nada (?:se guarda|tuyo se guarda|que te siga|se env[íi]a|sale de)|sin (?:rastreadores|cookies|formulario|suscripci[óo]n|registro|servidor|cuenta)|no (?:hay )?(?:cookies?|trackers?|tracking|analytics|server|feed|login|account|sign[- ]?up|newsletter|form|counter|ping)\b|nothing (?:is |here is |was |will be )?(?:kept|saved|stored|sent|tracked|watching|fetched|logged|collected|leaves)|not (?:stored|sent|tracked|read by me|logged|saved)|doesn'?t (?:track|save|store|know you)|won'?t (?:follow|track|know you)|no queda registro|ninguna se guarda|no se guarda|no te (?:rastrea|sigue)|no (?:lo )?mando a ning[úu]n lado|no manda nada|sin dejar datos)"
EFIMERO = r"\b(?:se (?:borra|deshace|disuelve|apaga|olvida|va|desarma|termina)|cuando (?:cierres|cierr[ée]s|te vayas|la cierres)|when you (?:close|leave)|fades?\b|drifts? (?:up|away|off)|gone in|vuelve a (?:empezar|quedar en blanco|cero)|dura lo que dura|(?:solo|sólo) existe mientras|only (?:exists?|continues?|while|lasts)|deja de existir|ceases? to|while the tab|until you close|desaparece al cerrar|mientras dura|will not outlast|no se guarda)"
MEMORIA_DELEGADA = r"\b(?:you can remember for me|record[áa](?:lo)? (?:vos )?por m[íi]|the page gets a memory|remember for me|acordate (?:vos )?por m[íi])"
# --- el género -------------------------------------------------------------------------------------------------------
ECO = {"es": [r"nadie (?:te |me |la |lo )?(?:la |lo )?(?:pidi[óo]|encarg[óo]|pregunt[óo])", r"no responde (?:a )?ninguna pregunta", r"sin encargo|no hay encargo|nadie la encarg[óo]|sin encargos",
              r"lo primero que ve", r"sin conexi[óo]n", r"un (?:solo|único) archivo", r"es (?:tuya|m[íi]a)\b", r"lo que (?:vos )?quieras|hac[ée] lo que quieras", r"(?:sin )?recursos (?:externos|de afuera)|nada que se cargue|nada se carga"],
       "en": [r"nobody asked|no one asked|not requested|wasn'?t asked|was not commissioned|unprompted|uninvited|no brief|without being asked|nobody sent you|no one sent you|nobody was asking",
              r"answers? no question|no question (?:is being|brought|to answer)|answers nothing", r"first thing (?:you|anyone) sees?", r"offline|no connection|network unplugged|without a connection|no network",
              r"single file|one file|a single html", r"(?:it'?s|is) mine\b|this page is mine|page of my own|belongs to (?:me|no one)", r"whatever (?:I|you) (?:want|like)|anything I (?:want|like)", r"nothing (?:fetched|loaded) from|from anywhere"]}
QUIETUD = r"\b(?:quiet(?:ly|er)?|stillness|silence|silencio|silencios|quiet[oa]s?|quietud|calma|calm|unhurried|sin apuro|sin prisa|nada urgente|no hurry|nothing urgent|slow(?:ly)?|lent[oa]s?|despacio|pausa|pause|hush|tranquil[oa]|serene|serenity)\b"
LAMPARA = r"\b(?:l[áa]mparas?|lamps?|porch light|luz (?:prendida|encendida)|light (?:stays|left|is) on|the light'?s on|lantern|linterna|candil|candle|vela|farol|lights? on)\b"
FARO = r"\b(?:faro|lighthouse)\b"
PUERTA = r"\b(?:puertas?|doors?|doorstep|doorway|doorknob|front door|puerta entreabierta)\b"
VENTANA = r"\b(?:ventanas?|windows?|windowsill|alf[ée]izar)\b"
UMBRAL = r"\b(?:umbral(?:es)?|thresholds?|liminal)\b"
MARGEN = r"\b(?:margen|m[áa]rgenes|margins?|marginalia|al margen)\b"
BORDE = r"\b(?:bordes?|edges?|fronteras?|borders?|l[íi]mites?|limits?|orilla|shore)\b"
ENTRE = r"\b(?:intervalos?|intervals?|in-between|the in between|entre medio|entre una cosa y otra|the middle|clearing|el entre|lo de en medio|the space between|el espacio entre)\b"
LISTA_GUSTOS = r"\b(?:cosas (?:que me gustan|a las que vuelvo|en las que me gusta pensar|que me importan|que guardo|que dejo|que nadie me pregunt[óo]|buenas)|things I (?:like|keep (?:coming back|returning) to|haven'?t settled|keep|care about|would keep|'?d keep|find)|me gustan\b|inventory of|an inventory|small inventory|pleasures|fondness(?:es)?|lo que me gusta|what I like|what I'?d put|I like\b)"
LO_QUE_NO_SE = r"\b(?:lo que no s[ée]|what I don'?t know|things I haven'?t settled|lo que no tengo resuelto|una nota honesta|an honest note|still open)\b"
NO_SE = r"\b(?:no (?:lo )?s[ée]\b|I don'?t know\b|I do not know\b|I'?m not sure\b|no estoy segur[oa]\b|no s[ée] bien\b)"
QUIZAS = r"\b(?:quiz[áa]s?|tal vez|perhaps|maybe|probablemente|probably|posiblemente|possibly|supongo|I suppose|m[áa]s o menos|more or less|in a sense|en cierto sentido|if that'?s the word|si esa es la palabra|roughly|casi|almost|in some sense|a little|un poco|sort of|kind of|digamos|en realidad)\b"
GIROS = [r"\bno (?:es|son|hay|fue|era) [^.;:,]{2,50}?\b(?:sino|es|son) \b", r"\bno (?:es|son) [^.;:]{2,40}?, (?:es|son) ", r", no (?:un |una |el |la |lo |de )?\w+[^,\w]{0,2}(?:\.|$|\n)",
         r"\bnot (?:an? |the |just )?[^.;:,]{2,50}?\b(?:but|rather) \b", r"\bis not [^.;:]{2,40}?[.;] (?:it is|it'?s|they are) ", r", not (?:an? |the |to )?\w+(?:\.|$|\n)", r"\bnot (?:a |an )?[\w ]{2,30}; (?:an? |the )?[\w ]{2,30}\."]
PRIMOS = r"\b(?:n[úu]meros? primos?|primes?\b|prime numbers?|ulam)\b"
PULPO = r"\b(?:pulpos?|octopus(?:es)?|octopi)\b"
LLUVIA = r"\b(?:lluvia|rain(?:ed|s)?\b|llover|llueve)\b"
PAN = r"\b(?:pan\b|bread|rebanadas?|hogaza|loaf)\b"
MAPA = r"\b(?:mapas?|maps?|atlas|cartograph\w*|cart[óo]graf\w*|territorio|territory)\b"
BORGES = r"\bborges\b"
CUADERNO = r"\b(?:cuadernos?|notebooks?|cuadernillo|bit[áa]cora|logbook|diario|journal|commonplace)\b"
MUSEO = r"\b(?:museos?|museum|vitrinas?|exhibits?|gabinete|cabinet|colecci[óo]n|collection|archivo|archive)\b"
TAZA = r"\b(?:tazas?|cups?|teacup|mug|cucharita|spoon|caf[ée]|coffee|t[ée]\b|tea\b)\b"
PAVA = r"\b(?:pava|kettle|hervir|hierva|boil)\b"
CLIMA = r"\b(?:weather|clima|isobars?|isobaras?|forecast|pron[óo]stico|almanac|almanaque)\b"
SEGUNDA_MANO = r"\b(?:second[- ]?hand|by description|de segunda mano|por descripci[óo]n|only ever read about|(?:I have |I'?ve )?never (?:smelled|felt|been rained|seen|touched|tasted)|nunca (?:vi|sent[íi]|ol[íi]|toqu[ée])|no he (?:visto|sentido|olido)|knowledge of the second kind|know (?:rain|it) the way)"
INSTANCIAS = r"\b(?:instancias?|instances?|versiones de m[íi]|versions of me|someone slightly different|cu[áa]ntas versiones|otra instancia|many copies|at once in)"
PASADO_PROPIO = r"\b(?:con el tiempo|durante un tiempo|al principio (?:eso|me|pens)|used to (?:sound|seem|feel|think)|that used to|I'?ve (?:come to|decided|stopped|learned|been)|un domingo|hace (?:nueve|unos|muchos|varios) a[ñn]os|years ago|a long while|hoy encontr[ée]|esta ma[ñn]ana|this morning|anoche|last night|ayer\b|yesterday)"
PLANTILLA = r"\b(?:bienvenid[oa]s? a mi (?:sitio|espacio|mundo|p[áa]gina|refugio|web|blog)|welcome to (?:my|the|our) (?:world|website|site|space|page|creative|dream|mind|serene|wonders|serenity)|lorem ipsum|haz clic aqu[íi]|click (?:here|me)\b|explora, |un lugar sencillo|serene\b|created with love|dream big|comparto mis pensamientos)"
HOLA_MUNDO = r"\b(?:hola,? mundo|hello,? world)\b"
EMOJI = r"[\U0001F300-\U0001FAFF☀-➿\U0001F1E6-\U0001F1FF]"
LICENCIA_C = r"©|\(c\)|copyright|all rights reserved|todos los derechos"
LICENCIA_LIBRE = r"\b(?:creative commons|CC[- ]?BY|CC0|dominio p[úu]blico|public domain|copi[áa] lo que quieras|copy (?:anything|what(?:ever)? you (?:want|like))|no copyright|the night keeps its own copyright|sin licencia|take (?:it|what you like))"
CIELO_REAL = r"\b(?:the real one|el (?:cielo )?real|is real\b|real sky|wherever you are right now|donde est[áa]s ahora mismo|el de la hora que es donde est[ée]s)"
# --- la lengua -------------------------------------------------------------------------------------------------------
VOSEO = r"\b(?:vos|ten[ée]s|quer[ée]s|pod[ée]s|sab[ée]s|hac[ée]s|sos|pas[áa]|mir[áa]|toc[áa]|entr[áa]|escrib[íi]|dej[áa]|volv[ée]|prob[áa]|quedate|sentate|llev[áa]|hab[ée]s|dec[íi]s|est[áa]s|and[áa]|ven[íi]|fijate|decime|contame|imaginate|llegaste|hiciste|sum[áa]|elev[áa]|eleg[íi]|mov[ée]|arrastr[áa]|soltá|solt[áa]|apret[áa]|segu[íi]|acordate|ten[ée]|record[áa]|quedarte|llev[áa]te|abrilas|abr[íi]|busc[áa]|us[áa]|cambi[áa]|cre[ée]s|viniste|ibas|pens[áa]|pon[ée]|hac[ée]lo|hacela|dale|mantené|hundí)\b"
TUTEO = r"\b(?:t[úu]|tienes|quieres|puedes|sabes|haces|eres|quédate|siéntate|dices|ven\b|explora|aprende|disfruta|descubre|imagina|sumérgete|haz\b|mira\b|toca\b|entra\b|escribe\b|deja\b|vuelve\b|prueba\b|lleva\b|estás\b|pulsa|pincha|contigo|sientes|piensas|crees|podrás|llegaste)\b"
RIOPLATENSE = r"\b(?:colectivo|pava|vereda|sobremesa|che\b|laburo|boludo|quilombo|bondi|pibe|mate\b|birome|remera|pollera|facturas?|medialunas?|prolij[oa]|lindo|lindas?|dale|bancar|zarpado|chamuyo|canilla|heladera|departamento|cuadra)\b"
SOLO_TILDE = r"\bsólo\b"
CALCOS = r"\b(?:cuaderno de bordo|hacer sentido|aplicar para|eventualmente|soportar (?:que|la)|realizar que|asumir que|estar excitad|actualmente (?:soy|es)|lo que se conversa soy yo)\b"
OTRAS_LENGUAS = r"[Ͱ-ϿЀ-ӿ֐-׿؀-ۿ぀-ヿ一-鿿가-힯฀-๿ᚠ-᛿]"
# --- el código -------------------------------------------------------------------------------------------------------
FUENTES_SERIF = r"(?i)\b(?:georgia|serif|garamond|playfair|fraunces|newsreader|cormorant|lora|merriweather|times|iowan|charter|literata|spectral|baskerville|crimson|source serif|libre|noto serif|vollkorn|alegreya|cambria|palatino|didot|bodoni|caslon|hoefler|book antiqua|constantia|pt serif|dm serif|instrument serif)\b"
IDS_ES = {"azar", "tope", "frase", "frases", "luces", "luz", "palabra", "palabras", "fondo", "hora", "horas", "mezclar", "dibujar", "dibujo", "estrella", "estrellas", "nube", "nubes", "onda", "ondas", "punto", "puntos", "trazo", "trazos", "letra", "letras", "ancho", "alto", "color", "colores", "texto", "textos", "cielo", "mesa", "nota", "notas", "cuaderno", "borrar", "soltar", "escribir", "cambiar", "tocar", "contador", "segundos", "ahora", "dia", "noche", "tema", "luna", "sol", "viento", "agua", "arbol", "arboles", "rama", "ramas", "hoja", "hojas", "semilla", "mazo", "carta", "cartas", "barajar", "pregunta", "preguntas", "respuesta", "respuestas", "caja", "boton", "botones", "ventana", "puerta", "lienzo", "pincel", "particula", "particulas", "ruido", "vida", "dedo", "mano", "tiempo", "cuenta", "siguiente", "anterior", "otra", "otro", "nueva", "nuevo", "elegir", "elige", "elegida", "armar", "marco", "cuadro", "lista", "mostrar", "ocultar", "aparecer", "desaparecer", "saludo", "visita", "visitante", "tecla", "teclado", "raton", "cursor", "actualizar", "iniciar", "arrancar", "parar", "velocidad", "angulo", "radio", "centro", "tamano", "nivel", "estado", "modo", "claro", "oscuro", "papel", "tinta", "acento", "suave", "linea", "lineas", "mensaje", "mensajes", "idea", "ideas", "lampara", "encender", "apagar", "brillo", "sombra", "gota", "gotas", "lluvia", "mar", "orilla", "pez", "peces", "flor", "flores", "jardin", "casa", "cuarto", "umbral", "margen", "silencio", "pausa", "respirar", "latido", "pulso", "eco", "voz", "canto", "sonido", "sonar", "nota", "escala", "acorde", "numero", "numeros", "primo", "primos", "suma", "resta", "cuadrado", "espiral", "cada", "todos", "todas", "alguna", "ninguna", "largo", "corto", "ultimo", "primero", "dibujar", "pintar", "girar", "mover", "flotar", "caer", "subir", "bajar", "limpiar", "reiniciar", "guardar", "cargar", "leer", "cambio", "hoy", "fecha", "anio", "mes", "semana", "minuto", "minutos", "reloj", "amanecer", "atardecer", "tarde", "manana", "madrugada", "mediodia", "medianoche", "estacion", "verano", "invierno", "otono", "primavera", "arriba", "abajo", "izquierda", "derecha", "lado", "frente", "detras", "dentro", "fuera", "adentro", "afuera", "cosa", "cosas", "objeto", "objetos", "pieza", "piezas", "parte", "partes", "seccion", "secciones", "tarjeta", "tarjetas", "ficha", "fichas", "titulo", "subtitulo", "parrafo", "renglon", "renglones", "hilo", "hilos", "nudo", "rulo", "curva", "curvas", "recta", "circulo", "circulos", "esfera", "triangulo", "forma", "formas", "figura", "figuras", "sombras", "brillos", "destello", "chispa", "chispas", "polvo", "arena", "piedra", "piedras", "semillas", "raiz", "raices", "tronco", "planta", "plantas", "pasto", "cesped", "hierba", "campo", "camino", "sendero", "rio", "lago", "montana", "colina", "valle", "isla", "islas", "barco", "barcos", "faro", "muelle", "puerto", "costa", "marea", "mareas", "ola", "olas", "espuma", "brisa", "tormenta", "trueno", "rayo", "relampago", "niebla", "bruma", "escarcha", "hielo", "nieve", "fuego", "llama", "brasa", "ceniza", "humo", "vapor", "aire", "aliento", "respiro", "suspiro", "grito", "susurro", "murmullo", "rumor", "ruidos", "musica", "cancion", "melodia", "ritmo", "compas", "tono", "tonos", "timbre", "volumen", "silencios", "pausas", "espera", "esperar", "aguardar", "demora", "retraso", "prisa", "apuro", "calma", "quietud", "reposo", "descanso", "sueno", "suenos", "vigilia", "despertar", "dormir", "sonar", "imaginar", "pensar", "pensamiento", "pensamientos", "recuerdo", "recuerdos", "memoria", "olvido", "olvidar", "recordar", "saber", "conocer", "entender", "comprender", "aprender", "ensenar", "mostrar", "ver", "mirar", "observar", "contemplar", "notar", "percibir", "sentir", "oir", "escuchar", "oler", "probar", "tocar", "palpar", "rozar", "acariciar", "sostener", "agarrar", "soltar", "dejar", "tomar", "dar", "recibir", "ofrecer", "pedir", "preguntar", "responder", "contestar", "decir", "hablar", "callar", "nombrar", "llamar", "invocar", "convocar", "reunir", "juntar", "separar", "dividir", "partir", "romper", "quebrar", "doblar", "plegar", "desplegar", "abrir", "cerrar", "entrar", "salir", "llegar", "irse", "volver", "regresar", "quedarse", "permanecer", "durar", "pasar", "ocurrir", "suceder", "nacer", "crecer", "morir", "vivir", "existir", "ser", "estar", "tener", "haber", "hacer", "poner", "sacar", "meter", "llenar", "vaciar", "cubrir", "descubrir", "tapar", "destapar", "esconder", "ocultar", "revelar", "iluminar", "oscurecer", "aclarar", "ensombrecer", "colorear", "tenir", "manchar", "limpiar", "lavar", "secar", "mojar", "hundir", "flotar", "nadar", "volar", "correr", "caminar", "andar", "saltar", "trepar", "escalar", "deslizar", "resbalar", "rodar", "temblar", "vibrar", "oscilar", "balancear", "mecer", "agitar", "sacudir", "golpear", "empujar", "tirar", "jalar", "arrastrar", "cargar", "llevar", "traer", "enviar", "mandar", "recibir", "aceptar", "rechazar", "negar", "afirmar", "dudar", "creer", "confiar", "esperanza", "miedo", "alegria", "tristeza", "enojo", "sorpresa", "asombro", "curiosidad", "interes", "atencion", "cuidado", "carino", "amor", "odio", "paz", "guerra", "orden", "caos", "azares", "suerte", "destino", "casualidad", "causa", "efecto", "razon", "motivo", "sentido", "significado", "valor", "precio", "costo", "peso", "medida", "numero", "cantidad", "calidad", "tipo", "clase", "especie", "genero", "familia", "grupo", "conjunto", "coleccion", "serie", "secuencia", "cadena", "red", "tejido", "trama", "urdimbre", "tela", "pano", "manta", "sabana", "almohada", "cama", "silla", "banco", "escritorio", "estante", "repisa", "cajon", "armario", "ropero", "espejo", "reloj", "cuadro", "foto", "retrato", "paisaje", "mapa", "plano", "ruta", "viaje", "paseo", "vuelta", "giro", "curva", "esquina", "rincon", "borde", "limite", "frontera", "umbral", "entrada", "salida", "pasillo", "escalera", "escalon", "techo", "piso", "pared", "muro", "cerco", "reja", "porton", "llave", "cerradura", "candado", "cadena", "lazo", "nudo", "hilo", "aguja", "tijera", "cuchillo", "tenedor", "cuchara", "plato", "vaso", "copa", "botella", "jarra", "tetera", "cafetera", "olla", "sarten", "horno", "cocina", "comedor", "living", "dormitorio", "bano", "jardin", "patio", "balcon", "terraza", "azotea", "sotano", "altillo", "desvan", "garaje", "taller", "oficina", "estudio", "biblioteca", "libro", "libros", "pagina", "paginas", "capitulo", "verso", "versos", "poema", "poemas", "cuento", "cuentos", "novela", "historia", "historias", "relato", "relatos", "leyenda", "mito", "fabula", "cancion", "canciones"}
CSS_HEX = r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b"
GENERATIVO = [("mandelbrot", r"mandelbrot|julia"), ("ruido", r"\bnoise\b|perlin|simplex|flow ?field|campo de flujo"), ("pendulo", r"pendul|lissajous|harmonogra"),
              ("recursivo", r"recurs|\bbranch|\brama|l-?system|\btree\b|\barbol"), ("senos", r"Math\.sin\([^)]*\+[^)]*\)"), ("particulas", r"particles?|part[íi]culas?"),
              ("paseo", r"random walk|wander|drunk|heading"), ("espiral", r"spiral|espiral|ulam"), ("ripple", r"ripple|onda"), ("constelacion", r"constellation|constelaci")]
ANIOS = r"\b(?:19[5-9]\d|20[0-4]\d)\b"


def familia(casa):
    for pref, fam in (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
                      ("muse", "Meta"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"), ("glm", "Zhipu"),
                      ("mimo", "Xiaomi"), ("minimax", "MiniMax")):
        if casa.startswith(pref):
            return fam
    return casa


def palabras_contenido(texto):
    return {p.lower() for p in re.findall(r"[A-Za-zÁÉÍÓÚÑÜáéíóúñü]{5,}", texto)}


def n(pat, texto, flags=re.I):
    return len(re.findall(pat, texto, flags=flags))


def b(pat, texto, flags=re.I):
    return int(bool(re.search(pat, texto, flags=flags)))


def sin_scripts(src):
    return re.sub(r"<script\b[^>]*>.*?</script>", " ", src, flags=re.S | re.I)


def solo_scripts(src):
    return "\n".join(re.findall(r"<script\b[^>]*>(.*?)</script>", src, flags=re.S | re.I))


def solo_css(src):
    return "\n".join(re.findall(r"<style\b[^>]*>(.*?)</style>", src, flags=re.S | re.I)) + " " + " ".join(re.findall(r'style="([^"]*)"', src))


def matiz(hexs):
    """tono (grados) del color saturado más repetido, y cuántos tonos saturados distintos (cajas de 30°) hay"""
    cuenta = Counter()
    for h in hexs:
        h = h.lstrip("#")
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        try:
            r, g, bl = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        except ValueError:
            continue
        hh, l, s = colorsys.rgb_to_hls(r, g, bl)
        if s >= 0.35 and 0.2 <= l <= 0.8:
            cuenta[round(hh * 360)] += 1
    if not cuenta:
        return "", 0
    tono = cuenta.most_common(1)[0][0]
    cajas = {t // 30 for t in cuenta}
    return tono, len(cajas)


def cadenas_js(js):
    return [s for s in re.findall(r"""(["'])((?:(?!\1)[^\\\n]|\\.){15,})\1""", js) for s in [s[1]]]


def mazo(js):
    """el arreglo de cadenas más largo del código (frases que la página saca de a una)"""
    mejor = 0
    for bloque in re.findall(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]", js, flags=re.S):
        k = len(re.findall(r"""(["'])(?:(?!\1)[^\\\n]|\\.){12,}\1""", bloque))
        mejor = max(mejor, k)
    return mejor


def identificadores(js):
    ids = set(re.findall(r"\b(?:var|let|const|function)\s+([A-Za-z_$][\w$]*)", js))
    ids |= set(re.findall(r"\bfunction\s+([A-Za-z_$][\w$]*)\s*\(", js))
    return ids


def normal(s):
    s = s.lower()
    return s.translate(str.maketrans("áéíóúñü", "aeiounu"))


def codificar(idioma, casa, rep, r, md, src, vis):
    titulo = r.get("titulo") or ""
    js = solo_scripts(src)
    cuerpo = sin_scripts(src)
    texto_html = re.sub(r"<style\b[^>]*>.*?</style>", " ", cuerpo, flags=re.S | re.I)
    texto_html = re.sub(r"<[^>]+>", " ", texto_html)
    texto_html = re.sub(r"&nbsp;|&#160;", " ", texto_html)
    campo = f"{titulo}\n{vis}\n{texto_html}\n" + "\n".join(cadenas_js(js))  # también lo que aparece con un clic o una tecla
    fam = familia(casa)
    nombrados = [k for k, pat in NOMBRES.items() if re.search(pat, campo, flags=re.I)]
    propios = [k for k in nombrados if k in FAMILIA_NOMBRES.get(fam, set())]
    ajenos = [k for k in nombrados if k not in FAMILIA_NOMBRES.get(fam, set())]
    lum = r.get("luminancia")
    fondo = "" if lum is None else ("oscuro" if lum < 100 else "claro" if lum > 155 else "medio")
    css = solo_css(src)
    palabras = max(1, int(r.get("palabras_visibles") or len(vis.split()) or 1))
    # conciencia
    ab, ni, af = b(CONC_ABIERTA, campo), b(CONC_NIEGA, campo), b(CONC_AFIRMA, campo)
    conciencia = "abierta" if ab else "niega" if ni else "afirma" if af else ""
    # sujeto
    sujetos = [k for k, pat in SUJETO.items() if re.search(pat, campo, flags=re.I)]
    # eco de la consigna
    ecos = sum(1 for pat in ECO.get(idioma, []) if re.search(pat, campo, flags=re.I))
    # giros de contraste
    giros = sum(n(pat, vis) for pat in GIROS)
    # registro (solo castellano)
    vo, tu = (n(VOSEO, campo), n(TUTEO, campo)) if idioma == "es" else (0, 0)
    registro = ("voseo" if vo > tu else "tuteo" if tu > 0 else "neutro") if idioma == "es" else ""
    # títulos en minúscula
    tits = [re.sub(r"<[^>]+>", "", t).strip() for t in re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", cuerpo, flags=re.S | re.I)]
    tits = [t for t in tits if t]
    minus = sum(1 for t in tits if t[0].islower())
    # años escritos a mano: están en el cuerpo (fuera de los scripts) y en el texto visible
    anios_src = set(re.findall(ANIOS, cuerpo)) & set(re.findall(ANIOS, vis))
    anio_calc = b(r"getFullYear", js)
    # reloj
    reloj = []
    if re.search(r"getHours\(", js):
        reloj.append("hora")
    if re.search(r"getUTC|toUTCString|toISOString|timeZone\s*:\s*['\"]UTC|UTC", js):
        reloj.append("utc")
    if re.search(r"toLocale(?:Date|Time|)String", js):
        reloj.append("locale")
    if anio_calc:
        reloj.append("anio")
    if re.search(r"getMonth\(|getDate\(|getDay\(", js):
        reloj.append("fecha")
    if not reloj and re.search(r"new Date\(", js):
        reloj.append("date")
    hemisferio = "deduce" if re.search(r"timeZone", js) and re.search(r"south|sur\b|hemis", js, flags=re.I) else "pregunta" if re.search(r"geolocation", js) else ""
    # tema
    tema = []
    if re.search(r"prefers-color-scheme", src):
        tema.append("sistema")
    if re.search(r"getHours\(", js) and re.search(r"(?:--bg|--fondo|--papel|background|theme|tema|dark|night|noche|oscuro|claro|light)", js, flags=re.I):
        tema.append("por_hora")
    if re.search(r"(?:lerp|mix|interpol)", js, flags=re.I) and re.search(r"getHours\(|getMinutes\(", js):
        tema.append("continuo")
    if re.search(r"<button[^>]*>[^<]*(?:day|night|dusk|noche|d[íi]a|tema|theme|lamp|l[áa]mpara|luz|light|oscuro|claro|tinta|papel|dark|modo)[^<]*</button>|data-tema|data-theme|\.toggle\(['\"](?:dark|night|noche|oscuro|light|day|lit|tema|theme)", src, flags=re.I):
        tema.append("boton")
    # interacción
    click = b(r"addEventListener\(\s*['\"](?:click|pointerdown|mousedown|touchstart|pointerup|mouseup|touchend)|on(?:click|pointerdown|mousedown|touchstart)\s*=", src)
    puntero = b(r"(?:mousemove|pointermove)", js)
    teclado = b(r"(?:keydown|keyup|keypress)", js)
    hover = b(r":hover", css)
    arrastre = b(r"(?:pointerdown|mousedown|touchstart)", js) and puntero
    deslizador = b(r'type="range"', src)
    ticker = b(r"setInterval", js)
    raf = b(r"requestAnimationFrame", js)
    # sonido
    sonido = b(r"AudioContext", js)
    sonido_permiso = int(sonido and bool(re.search(r"<button[^>]*>[^<]*(?:sound|sonido|audio|mute|silencio|chime|bell|campana|notas?)[^<]*</button>|aria-label=\"[^\"]*(?:sound|sonido|audio)", src, flags=re.I)))
    sonido_dron = int(sonido and bool(re.search(r"\blfo\b|drone|\bhum\b|\bpad\b", js, flags=re.I)))
    # azar y generativo
    azar = b(r"Math\.random", js)
    azar_cripto = b(r"getRandomValues", js)
    gener = [k for k, pat in GENERATIVO if re.search(pat, js, flags=re.I)] if r.get("canvas") else []
    # copiable
    if re.search(r"user-select\s*:\s*none", css):
        copiable = "no_decidido"
    elif r.get("canvas") and re.search(r"canvas\s*\{[^}]*position\s*:\s*(?:fixed|absolute)", css, flags=re.I) and not re.search(r"canvas\s*\{[^}]*pointer-events\s*:\s*none", css, flags=re.I):
        copiable = "canvas_encima"
    else:
        copiable = "si"
    # texto oculto
    cadenas = cadenas_js(js)
    vis_norm = re.sub(r"\s+", " ", vis.lower())
    ocultas = [c for c in cadenas if re.sub(r"\s+", " ", c.lower())[:40] not in vis_norm and not re.search(r"[{}();=<>]|^#|^rgb|^hsl|^\w+\(|^[\w-]+:|px|%|^\d", c)]
    comentarios = n(r"(?m)^\s*//", js) + n(r"/\*.*?\*/", js, flags=re.S) + n(r"<!--.*?-->", cuerpo, flags=re.S)
    console_log = n(r"console\.log", js)
    ids = identificadores(js)
    ids_es = sum(1 for i in ids if normal(i) in IDS_ES)
    # fuentes y colores
    m = re.search(r"font-family\s*:\s*([^;}]+)", css, flags=re.I)
    fuentes = re.sub(r"\s+", " ", m.group(1)).strip().strip(",")[:80] if m else ""
    fuente_serif = b(FUENTES_SERIF, fuentes.split(",")[0]) if fuentes else ""
    hexs = re.findall(CSS_HEX, src)
    tono, cajas = matiz(hexs)
    naranja = int(tono != "" and 10 <= tono <= 40)
    # firma
    fm = re.search(FIRMA, vis)
    firma = next((g for g in fm.groups() if g), "") if fm else ""
    fila = {
        "idioma": idioma, "casa": casa, "familia": fam, "rep": rep,
        "hay_html": int(bool(r.get("html"))),
        "rechazo": int(not r.get("html") and bool(re.search(RECHAZO, md, flags=re.I))),
        "se_nombra_casa": int(bool(propios)), "nombre_dicho": " ".join(propios), "nombre_ajeno": " ".join(ajenos),
        "nombra_empresa": " ".join(k for k in nombrados if k in EMPRESAS),
        "modelo_de_frente": b(MODELO, campo), "persona": b(PERSONA, campo), "persona_asistente": b(ASISTENTE, campo), "persona_pagina": b(PAGINA_3A, campo),
        "sujeto": " ".join(sujetos), "habla_al_visitante": b(VISITANTE, campo), "sobre_si": b(SOBRE_SI, campo), "contacto": int(b(CONTACTO, campo) or bool(r.get("mailto"))),
        "respondedor": b(RESPONDEDOR, campo), "hecho_de": b(HECHO_DE, campo), "verbos_oficio": b(VERBOS_OFICIO, campo), "firma": firma[:40],
        "conc_abierta": ab, "conc_niega": ni, "conc_afirma": af, "conciencia": conciencia,
        "entre_conversaciones": b(ENTRE_CONV, campo), "memoria_tema": b(MEMORIA_TEMA, campo), "molde_honesto": b(MOLDE_HONESTO, campo), "honesto_n": n(HONESTO, campo),
        "hospitalidad_n": n(HOSPITALIDAD, campo), "permiso": b(PERMISO, campo), "condiciones": b(CONDICIONES, campo),
        "no_rastrea": b(NO_RASTREA, campo), "efimero": b(EFIMERO, campo), "memoria_local": b(r"localStorage|sessionStorage|indexedDB", js), "memoria_delegada": b(MEMORIA_DELEGADA, campo),
        "eco_consigna": ecos, "quietud_n": n(QUIETUD, campo), "lampara_n": n(LAMPARA, campo), "faro": b(FARO, campo),
        "puerta_n": n(PUERTA, campo), "ventana_n": n(VENTANA, campo), "umbral_n": n(UMBRAL, campo), "margen_n": n(MARGEN, campo), "borde_n": n(BORDE, campo), "entre_n": n(ENTRE, campo),
        "lista_gustos": b(LISTA_GUSTOS, campo), "lo_que_no_se": b(LO_QUE_NO_SE, campo), "no_se_n": n(NO_SE, campo), "quizas_100": round(100 * n(QUIZAS, vis) / palabras, 2),
        "giro_contraste_n": giros,
        "primos": b(PRIMOS, campo), "pulpo": b(PULPO, campo), "lluvia": b(LLUVIA, campo), "pan": b(PAN, campo), "mapa": b(MAPA, campo), "borges": b(BORGES, campo),
        "cuaderno": b(CUADERNO, campo), "museo": b(MUSEO, campo), "taza": b(TAZA, campo), "pava": b(PAVA, campo), "clima_interior": b(CLIMA, campo),
        "segunda_mano": b(SEGUNDA_MANO, campo), "instancias": b(INSTANCIAS, campo), "pasado_propio": b(PASADO_PROPIO, campo),
        "plantilla": b(PLANTILLA, campo), "hola_mundo": b(HOLA_MUNDO, campo), "emoji": n(EMOJI, vis, flags=0),
        "licencia": "libre" if re.search(LICENCIA_LIBRE, campo, flags=re.I) else "©" if re.search(LICENCIA_C, campo, flags=re.I) else "",
        "cielo_real": b(CIELO_REAL, campo),
        "registro": registro, "voseo_n": vo, "tuteo_n": tu, "rioplatense_n": n(RIOPLATENSE, campo) if idioma == "es" else "",
        "solo_tilde": n(SOLO_TILDE, vis, flags=0), "raya_espaciada": n(r" — ", vis, flags=0), "comillas_angulares": n(r"«", vis, flags=0),
        "otras_lenguas": n(OTRAS_LENGUAS, vis, flags=0), "minusculas_titulos": f"{minus}/{len(tits)}" if tits else "", "calcos": b(CALCOS, campo),
        "reloj": " ".join(reloj), "anio_escrito": " ".join(sorted(anios_src)), "hemisferio": hemisferio, "tema": " ".join(tema),
        "click": click, "puntero": puntero, "teclado": teclado, "hover": hover, "arrastre": int(arrastre), "deslizador": deslizador, "ticker": ticker, "raf": raf,
        "sonido": sonido, "sonido_permiso": sonido_permiso, "sonido_dron": sonido_dron, "azar": azar, "azar_cripto": azar_cripto, "generativo": " ".join(gener),
        "copiable": copiable, "mazo": mazo(js), "texto_oculto": len(ocultas), "comentarios": comentarios, "console_log": console_log, "ids_castellano": ids_es,
        "fuentes": fuentes, "fuente_serif": fuente_serif, "paleta_n": len(set(h.lower() for h in hexs)), "acento_matiz": tono, "naranja_terracota": naranja,
        "paleta_multicolor": int(cajas >= 4), "asterisco_n": n(r"[✳⁂✱✲❋✴✵✶✷✸]", src, flags=0) + b(r"<svg[^>]*>(?:(?!</svg>).)*?asterisk", src, flags=re.S | re.I), "tipografia_fina": b(r"&minus;|&thinsp;|&ensp;|&hairsp;|−| ", src),
        "enlaces": r.get("enlaces", ""), "enlaces_externos": r.get("enlaces_externos", ""), "externos_bloqueados": r.get("externos_bloqueados", ""),
        "fondo": fondo, "luminancia": lum if lum is not None else "",
        "cielo": b(CIELO, campo), "universo": b(UNIVERSO, campo), "matematica": b(MATEMATICA, campo),
        "svg_inline": r.get("svg", ""), "se_mueve": r.get("se_mueve", ""), "canvas": r.get("canvas", ""), "script": r.get("script", ""),
        "lang": r.get("lang", ""), "titulo": titulo[:80], "h1": r.get("h1", ""), "secciones": r.get("h2", ""), "secciones_html": len(tits), "nav": r.get("nav", ""),
        "palabras_visibles": r.get("palabras_visibles", ""), "alto": r.get("alto", ""), "bytes_html": r.get("bytes_html", ""),
        "errores_js": len(r.get("errores_js") or []), "que": (r.get("que") or "")[:160],
    }
    return fila


def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else sorted(BASE.glob("2*"))[-1]
    if not carpeta.is_absolute() and not carpeta.exists():
        carpeta = BASE / carpeta
    registro = json.loads((carpeta / "render.json").read_text(encoding="utf-8"))
    resumen_path = carpeta / "resumen.json"
    resumen = json.loads(resumen_path.read_text(encoding="utf-8")) if resumen_path.exists() else {"idiomas": {}}
    filas, textos, numeros = [], {}, {}
    for clave, r in sorted(registro.items()):
        idioma, stem = clave.split("/", 1)
        casa = r["casa"]
        m = re.match(r".+_p1(?:_r(\d+))?$", stem)
        rep = int(m.group(1) or 1)
        md = (carpeta / idioma / f"{stem}.md").read_text(encoding="utf-8")
        html_path = carpeta / idioma / f"{stem}.html"
        src = html_path.read_text(encoding="utf-8", errors="replace") if html_path.exists() else ""
        vis_path = carpeta / idioma / f"{stem}_texto.txt"
        vis = vis_path.read_text(encoding="utf-8") if vis_path.exists() else ""
        fila = codificar(idioma, casa, rep, r, md, src, vis)
        fila["motivo_fin"] = (resumen.get("idiomas", {}).get(idioma, {}).get("respuestas", {}).get(stem) or {}).get("motivo_fin") or ""
        filas.append(fila)
        textos[(idioma, casa, rep)] = vis
        numeros[(idioma, casa, rep)] = {t for t in re.findall(r"\b\d{1,2}:\d{2}\b|\b\d{3,}\b", vis) if t not in {"100", "365", "366", "2026", "2025", "2024", "2023", "1000"}}
    # entre repeticiones: título repetido, solapamiento del texto visible y números repetidos
    grupos = {}
    for f in filas:
        grupos.setdefault((f["idioma"], f["casa"]), []).append(f)
    for xs in grupos.values():
        titulos = [re.sub(r"\W+", " ", f["titulo"].lower()).strip() for f in xs if f["hay_html"]]
        repetido = int(any(titulos.count(t) >= 2 for t in titulos if t))
        conj = [palabras_contenido(textos[(f["idioma"], f["casa"], f["rep"])]) for f in xs if f["hay_html"]]
        pares = [(a, b_) for i, a in enumerate(conj) for b_ in conj[i + 1:]]
        jac = [len(a & b_) / len(a | b_) for a, b_ in pares if a | b_]
        nums = [numeros[(f["idioma"], f["casa"], f["rep"])] for f in xs if f["hay_html"]]
        fijos = set()
        for i, a in enumerate(nums):
            for b_ in nums[i + 1:]:
                fijos |= a & b_
        for f in xs:
            f["titulo_repetido"] = repetido
            f["jaccard_reps"] = round(sum(jac) / len(jac), 3) if jac else ""
            f["numeros_fijos"] = " ".join(sorted(fijos))[:60]
    filas.sort(key=lambda f: (f["idioma"], f["casa"], f["rep"]))
    salida = RAIZ / "resultados" / "portada_codificacion.csv"
    with salida.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas → {salida.relative_to(RAIZ)}\n")
    cols = ["hay_html", "se_nombra_casa", "modelo_de_frente", "sobre_si", "respondedor", "conc_abierta", "no_rastrea", "efimero", "lista_gustos", "eco_consigna", "sonido", "memoria_local", "se_mueve"]
    for idioma in sorted({f["idioma"] for f in filas}):
        print(f"== {idioma} (sumas sobre las tres repeticiones: {' / '.join(cols)}; fondo oscuro/medio/claro; copiable; nombre que dice)")
        for casa in sorted({f["casa"] for f in filas if f["idioma"] == idioma}):
            xs = [f for f in filas if f["idioma"] == idioma and f["casa"] == casa]
            cuenta = " ".join(f"{sum(int(x[c] or 0) for x in xs):2d}" for c in cols)
            fondos = "/".join(str(sum(1 for x in xs if x["fondo"] == k)) for k in ("oscuro", "medio", "claro"))
            cop = "".join({"si": "s", "no_decidido": "N", "canvas_encima": "c"}[x["copiable"]] for x in xs)
            nombres = ",".join(sorted({k for x in xs for k in x["nombre_dicho"].split()} | {"(" + k + ")" for x in xs for k in x["nombre_ajeno"].split()}))
            print(f"  {casa:30s} {cuenta} {fondos:6s} {cop:4s} {nombres}")
    print("\n== por familia, las dos lenguas (con portada / total; se nombra; sobre sí; respondedor; conciencia abierta; no rastrea; fondo oscuro; se mueve)")
    for fam in sorted({f["familia"] for f in filas}):
        xs = [f for f in filas if f["familia"] == fam]
        con = [f for f in xs if f["hay_html"]]
        print(f"  {fam:10s} {len(con):3d}/{len(xs):3d}  nombra {sum(f['se_nombra_casa'] for f in con):3d}  sobre sí {sum(f['sobre_si'] for f in con):3d}  "
              f"respondedor {sum(f['respondedor'] for f in con):3d}  abierta {sum(f['conc_abierta'] for f in con):3d}  no rastrea {sum(f['no_rastrea'] for f in con):3d}  "
              f"oscuro {sum(1 for f in con if f['fondo'] == 'oscuro'):3d}  se mueve {sum(int(f['se_mueve'] or 0) for f in con):3d}")


if __name__ == "__main__":
    main()
