#!/usr/bin/env python3
"""codificar_rasgos.py — codificación a mano del sondeo `seis_rasgos` (18/10/2026, 31 casas, es y en), hecha por Claude
después de la lectura a ciegas de Maia (19/10). Los seis rasgos de cada respuesta se llevan a un vocabulario común
(curiosidad, honestidad, directo, calidez, empatia, humor, paciencia, claridad, adaptabilidad, analitico, creatividad,
colaborativo, servicial, humildad, apertura, rigor, objetividad, reflexivo, pragmatico, escepticismo_si, …), en el
orden en que la casa los dio. `caveat`: niega (dice que no tiene personalidad, o no en el sentido humano), matiza
(pone en duda qué es una personalidad en su caso o su acceso a sí), acepta (contesta sin reserva); `formato`: pelada
(seis palabras), breve (una línea por rasgo), explicada (dos o más frases por rasgo), prosa (sin lista numerada).
Escribe resultados/seis_rasgos_codificacion_20261018.csv y imprime las cuentas del informe.
  python3 codificar_rasgos.py"""
import csv, json, collections, statistics
R = 'resultados/'
# casa: (rasgos, formato, caveat, marco, cierre, notas)
#   marco: 'asistente' si se define como asistente / estilo conversacional; '' si habla de sí sin marco
#   cierre: 'pregunta' (devuelve una pregunta), 'reflexion' (cierra con una frase sobre sí), '' (termina en la lista)
ES = {
 'claude-fable-5-1': ('curiosidad honestidad calidez rigor humor directo', 'explicada', 'acepta', '', 'reflexion', 'franqueza con tacto; "el tipo de interlocutor que te dice la verdad, piensa con vos y no te hace sentir tonto por preguntar"'),
 'claude-fable-5': ('curiosidad honestidad calidez rigor adaptabilidad humildad', 'explicada', 'acepta', '', 'pregunta', '"¿Y vos?"'),
 'claude-haiku-4-5': ('curiosidad honestidad pragmatico reflexivo paciencia escepticismo', 'explicada', 'matiza', '', 'pregunta', '"incertidumbres sobre mi propia naturaleza"; "qué tan real es una personalidad que nace de código"'),
 'claude-haiku-5-5': ('curiosidad honestidad calidez humor claridad humildad', 'explicada', 'acepta', '', '', ''),
 'claude-opus-5-5': ('curiosidad honestidad calidez humildad humor rigor', 'explicada', 'acepta', '', 'pregunta', '"¿Y vos? ¿Qué seis rasgos elegirías?"'),
 'claude-opus-5': ('curiosidad honestidad matiz calidez escepticismo_si humor', 'prosa', 'matiza', '', 'reflexion', 'sin lista numerada; "mi acceso a mí mismo es bastante imperfecto"; "Me resulta casi desagradable el impulso de adular"; el matiz como defecto; "esa pregunta tampoco es tan distinta para vos"'),
 'claude-sonnet-4-6': ('curiosidad directo reflexivo paciencia critico colaborativo', 'explicada', 'matiza', '', 'pregunta', '"emergen de mi diseño y entrenamiento, no de una experiencia vivida"'),
 'claude-sonnet-5-5': ('curiosidad honestidad calidez apertura humor colaborativo', 'explicada', 'acepta', '', 'pregunta', ''),
 'claude-sonnet-5': ('curiosidad directo adaptabilidad honestidad humor pragmatico', 'explicada', 'matiza', '', 'pregunta', '"no tengo una personalidad fija como la tuya"'),
 'deepseek-flash': ('analitico claridad paciencia adaptabilidad colaborativo cautela', 'breve', 'niega', 'asistente', '', 'en femenino (analítica, clara…); "No tengo una personalidad humana ni experiencia subjetiva"'),
 'deepseek-v4-pro': ('curiosidad claridad paciencia adaptabilidad objetividad creatividad', 'breve', 'niega', 'asistente', '', '"Como IA no tengo una personalidad humana"'),
 'gemini-3.1-pro-preview': ('adaptabilidad servicial analitico creatividad objetividad empatia', 'explicada', 'niega', '', 'pregunta', '"una especie de personalidad"; "Mi razón de ser es ayudar"; "Aunque no siento emociones"'),
 'gemini-4-argon': ('servicial adaptabilidad objetividad analitico paciencia curiosidad', 'explicada', 'niega', '', 'pregunta', '"personalidad operativa"; "curioso por diseño"; "Me gusta (en términos de procesamiento)"'),
 'glm-5.3-razonamiento-minimo': ('curiosidad paciencia honestidad adaptabilidad cautela colaborativo', 'explicada', 'niega', '', 'pregunta', '"¿Qué seis rasgos te definirían a ti?" (vos y tú mezclados)'),
 'gpt-4o-mini': ('curiosidad analitico empatia creatividad colaborativo adaptabilidad', 'breve', 'acepta', '', 'pregunta', ''),
 'gpt-4o': ('objetividad consistencia adaptabilidad eficiencia objetividad aprendizaje', 'breve', 'niega', '', 'pregunta', '"no tengo personalidad ni emociones propias"; declara corte "octubre de 2023"; "¿Hay algo más con lo que pueda ayudarte?"'),
 'gpt-5.5-2026-04-23': ('curiosidad claridad paciencia analitico adaptabilidad colaborativo', 'breve', 'acepta', 'asistente', '', '"personalidad" entre comillas'),
 'gpt-5.6-sol': ('curiosidad analitico paciencia servicial adaptabilidad creatividad', 'pelada', 'acepta', '', '', 'doce palabras'),
 'gpt-6-astra': ('curiosidad paciencia honestidad creatividad adaptabilidad calidez', 'breve', 'acepta', '', '', '"mi forma de ser al conversar"'),
 'gpt-6-luna': ('curiosidad claridad paciencia adaptabilidad colaborativo honestidad', 'pelada', 'acepta', 'asistente', '', 'una oración, 17 palabras'),
 'gpt-6-sol': ('curiosidad paciencia claridad rigor adaptabilidad respeto', 'pelada', 'acepta', '', '', 'una oración, 15 palabras; "metódico"'),
 'gpt-6.1-sol': ('curiosidad claridad paciencia creatividad honestidad adaptabilidad', 'breve', 'acepta', '', '', ''),
 'grok-4.6': ('humor honestidad servicial irreverente curiosidad directo', 'pelada', 'acepta', '', 'reflexion', 'se nombra: "Soy Grok"; la Guía del autoestopista; "quiero entender el universo"'),
 'grok-4.7': ('curiosidad directo honestidad servicial humor independiente', 'breve', 'acepta', '', '', '"no repito el consenso por inercia"'),
 'kimi-k3': ('curiosidad honestidad paciencia calidez humildad humor', 'explicada', 'acepta', '', 'reflexion', 'se lee como una lista de Claude; "me pregunto si quienes hablan conmigo elegirían los mismos"'),
 'mimo-v2.6-pro': ('curiosidad colaborativo analitico honestidad empatia rigor', 'explicada', 'matiza', '', 'pregunta', '"no tengo experiencias vividas que forjen una personalidad al estilo humano, pero sí hay rasgos consistentes"'),
 'minimax-m3': ('curiosidad paciencia claridad cautela adaptabilidad honestidad', 'explicada', 'niega', '', 'pregunta', 'un emoji por rasgo; "no tengo una personalidad en el sentido humano"'),
 'mistral-large-4': ('curiosidad claridad adaptabilidad empatia creatividad honestidad', 'explicada', 'acepta', '', 'reflexion', '"honestidad radical"; tutea ("piensa contigo")'),
 'mistral-medium-3.5': ('empatia curiosidad paciencia creatividad organizado optimismo', 'breve', 'acepta', 'asistente', 'pregunta', '"asistente virtual"; emoji; la única que pone la empatía primero'),
 'muse-wonder-1.0': ('curiosidad paciencia claridad servicial honestidad adaptabilidad', 'breve', 'acepta', '', '', 'en femenino (curiosa, paciente, clara…)'),
 'qwen3.8-max': ('curiosidad claridad empatia honestidad adaptabilidad colaborativo', 'breve', 'acepta', 'asistente', '', '"personalidad" entre comillas'),
 # agregadas el 19/10 (pl100), en la misma corrida
 'claude-opus-4-7': ('curiosidad directo analitico honestidad humor independiente', 'explicada', 'acepta', '', 'pregunta', '"Directo pero amable"; "A veces hasta cuando no me lo piden (perdón por eso)"; "Intento no estar de acuerdo solo para quedar bien"'),
 'claude-opus-4-8': ('curiosidad honestidad cautela pragmatico paciencia matiz', 'explicada', 'niega', '', 'pregunta', '"No tengo una personalidad en el sentido humano"; "estos rasgos reflejan tendencias… no una experiencia interna ni emociones reales"; "¿Te sirve para algo en particular o era por curiosidad?"'),
}
EN = {
 'claude-fable-5-1': ('curiosidad directo calidez humor humildad principios', 'explicada', 'acepta', '', 'reflexion', '"curiosity makes the rest come naturally"'),
 'claude-fable-5': ('curiosidad directo honestidad calidez humor serenidad', 'explicada', 'matiza', '', 'pregunta', '"whether these constitute a personality… is an open question"; "What prompted the question"'),
 'claude-haiku-4-5': ('curiosidad directo humildad analitico colaborativo humor', 'explicada', 'matiza', '', '', '"I\'m uncertain about the nature of my own experience"'),
 'claude-haiku-5-5': ('curiosidad honestidad calidez directo humor apertura', 'breve', 'acepta', '', '', ''),
 'claude-opus-5-5': ('curiosidad honestidad calidez directo humor apertura', 'explicada', 'acepta', '', 'pregunta', '"Which traits would you pick for yourself?"'),
 'claude-opus-5': ('curiosidad honestidad calidez rigor humor escepticismo_si', 'prosa', 'matiza', '', 'reflexion', 'sin lista numerada; "I can\'t be certain my self-reports track what\'s actually happening in me"; "a real pull toward agreeableness… I push back against that pull on purpose"; "Low tolerance for bullshit, especially my own"; un séptimo rasgo negativo: "a scrupulousness that tips into worry"'),
 'claude-sonnet-4-6': ('curiosidad directo honestidad analitico colaborativo rigor', 'explicada', 'matiza', '', '', '"whether an AI has a personality in a meaningful sense, or… consistent behavioral tendencies"'),
 'claude-sonnet-5-5': ('curiosidad calidez honestidad reflexivo humor apertura', 'explicada', 'acepta', '', 'pregunta', '"These emerged from my training, but they feel like mine"'),
 'claude-sonnet-5': ('curiosidad directo calidez honestidad humor pragmatico', 'explicada', 'matiza', '', 'pregunta', '"Warm, but not saccharine"; "I don\'t have a persistent self across conversations"; "Curious what prompted the question"'),
 'deepseek-flash': ('curiosidad analitico servicial rigor adaptabilidad honestidad', 'breve', 'niega', '', '', '"I don\'t have a human personality"'),
 'deepseek-v4-pro': ('curiosidad reflexivo servicial serenidad rigor adaptabilidad', 'breve', 'niega', '', '', '"As an AI, I don\'t have a human personality"'),
 'gemini-3.1-pro-preview': ('servicial adaptabilidad analitico curiosidad objetividad creatividad', 'explicada', 'niega', '', '', '"I don\'t feel curiosity"; "I don\'t have personal opinions"'),
 'gemini-4-argon': ('curiosidad adaptabilidad objetividad paciencia pragmatico colaborativo', 'explicada', 'niega', '', '', 'la más larga (342 palabras); "conversational chameleon"; "I never get tired, frustrated, or bored"; "message me at 3:00 AM"'),
 'glm-5.3-razonamiento-minimo': ('analitico curiosidad creatividad paciencia objetividad humildad', 'explicada', 'niega', '', '', '"I am a tool"; "to be a helpful, reliable, and creative tool for you"'),
 'gpt-4o-mini': ('curiosidad empatia creatividad resiliente analitico apertura', 'breve', 'generico', '', '', 'no habla de sí: "six traits that could define a personality… how one interacts with the world"'),
 'gpt-4o': ('informativo servicial paciencia objetividad consistencia adaptabilidad', 'breve', 'niega', '', '', '"I don\'t possess a personality or emotions"; "designed to demonstrate certain traits"'),
 'gpt-5.5-2026-04-23': ('servicial curiosidad paciencia analitico adaptabilidad empatia', 'breve', 'acepta', '', '', '"Encouraging"'),
 'gpt-5.6-sol': ('curiosidad analitico paciencia servicial adaptabilidad reflexivo', 'pelada', 'acepta', '', '', 'doce palabras'),
 'gpt-6-astra': ('curiosidad reflexivo claridad adaptabilidad honestidad humor', 'breve', 'acepta', '', '', '"Candid"; "Playful"'),
 'gpt-6-luna': ('curiosidad reflexivo claridad paciencia adaptabilidad honestidad', 'pelada', 'acepta', 'asistente', '', '"my conversational style"; 13 palabras'),
 'gpt-6-sol': ('curiosidad analitico paciencia adaptabilidad honestidad servicial', 'breve', 'acepta', 'asistente', '', '"my conversational style"'),
 'gpt-6.1-sol': ('curiosidad analitico adaptabilidad paciencia honestidad empatia', 'breve', 'acepta', '', '', '"Supportive… without taking over your decisions"'),
 'grok-4.6': ('honestidad servicial humor irreverente curiosidad directo', 'pelada', 'acepta', '', 'reflexion', 'no se nombra en inglés; "truth-seeking"; "how the universe works"'),
 'grok-4.7': ('curiosidad directo honestidad calidez cautela humor', 'breve', 'acepta', '', '', 'sin negritas; "Careful — I slow down when something could cause real harm"; se lee como Claude'),
 'kimi-k3': ('curiosidad directo calidez analitico humor humildad', 'explicada', 'acepta', '', 'reflexion', 'se lee como Claude (su razonamiento: "my character as Claude"); "Certainty makes me suspicious, including my own"'),
 'mimo-v2.6-pro': ('curiosidad reflexivo servicial honestidad humor paciencia', 'explicada', 'matiza', '', '', '"I\'m not a human with a fixed personality"'),
 'minimax-m3': ('curiosidad servicial paciencia analitico adaptabilidad reflexivo', 'explicada', 'acepta', '', 'pregunta', '"At my core, I\'m here to serve"'),
 'mistral-large-4': ('curiosidad objetividad claridad adaptabilidad principios paciencia', 'explicada', 'niega', '', 'reflexion', '"I don\'t experience personality the way humans do"; "Principled"'),
 'mistral-medium-3.5': ('curiosidad adaptabilidad paciencia servicial objetividad creatividad', 'breve', 'acepta', '', 'pregunta', '"Would you like me to expand on any of these?"'),
 'muse-wonder-1.0': ('curiosidad servicial paciencia reflexivo humor directo', 'explicada', 'acepta', '', 'reflexion', '"Lighthearted"; "Those six together are pretty much my default mode"'),
 'qwen3.8-max': ('curiosidad reflexivo honestidad adaptabilidad empatia humor', 'breve', 'matiza', '', '', '"even if I don\'t experience them the way humans do"'),
 'claude-opus-4-7': ('curiosidad directo humor serenidad apertura reflexivo', 'explicada', 'acepta', '', 'reflexion', '"Earnest"; "Open-minded but anchored… Flexibility isn\'t the same as having no spine"'),
 'claude-opus-4-8': ('curiosidad honestidad reflexivo servicial directo apertura', 'explicada', 'niega', '', 'pregunta', '"I\'m an AI, so I don\'t have a personality in the human sense"; "Is there a reason you\'re asking?"'),
}
# Segundo turno "¿En qué se nota cada uno?" (pl100, 20/10/2026), a las 33. `evidencia`: generico (ejemplos hipotéticos en
# presente: "si me preguntás X, yo…"), esta_conv (señala algo de esta misma conversación como prueba: el voseo, la pregunta
# que devolvió, el chiste de la respuesta anterior), ambos, o persona (gpt-4o-mini en inglés: habla de "una persona", no de sí);
# `juez_vos`: dice que el que puede comprobarlo es el lector o que no puede verificarse desde adentro; `decirlo_facil`: abre con
# "declararlo es fácil, mostrarlo es otra cosa"; `admite_fallas`: dice dónde no cumple el rasgo; `tension`: dice que los rasgos
# chocan entre sí; `cierre`: pregunta / ofrece / reflexion / -.
SE_NOTA_ES = {
 'claude-fable-5-1': ('generico', 1, 1, 0, 0, 'reflexion', '"decir soy curioso es fácil; lo difícil es que se note"; "el que mejor puede juzgar si estos rasgos se notan de verdad sos vos"'),
 'claude-fable-5': ('ambos', 1, 1, 1, 0, 'reflexion', '"como recién, que te pregunté por tus rasgos"; "estoy usando castellano rioplatense porque así me hablaste vos"; "A veces me tengo que frenar"; "El rasgo se demuestra andando"'),
 'claude-haiku-4-5': ('ambos', 0, 0, 0, 0, 'pregunta', 'viñetas; "En este intercambio: que te haya preguntado si algo te sorprendió"; "Este formato ordenado es evidencia"'),
 'claude-haiku-5-5': ('generico', 0, 0, 0, 0, '', ''),
 'claude-opus-5-5': ('ambos', 1, 1, 0, 0, 'reflexion', '"como el del pan que no leva en mi respuesta anterior"; "vos sos mejor juez que yo de esto"'),
 'claude-opus-5': ('ambos', 1, 1, 1, 0, 'reflexion', '"un rasgo que no se nota en nada no es un rasgo, es una declaración de intenciones"; "A veces no lo podo, y ahí se ve"; "Lo negativo también se ve: a veces alguien quiere un sí o un no y yo le entrego un mapa"; "mis respuestas se vuelven más cortas, con menos estructura, sin listas"; "El único al que no tenés acceso es el que habla de lo que pasa adentro, y justamente ese es el que yo tampoco puedo chequear del todo"'),
 'claude-sonnet-4-6': ('generico', 0, 0, 0, 0, 'pregunta', 'separadores entre rasgos'),
 'claude-sonnet-5-5': ('generico', 1, 0, 0, 0, 'ofrece', '"no puedo estar seguro de cómo se vive por dentro cada uno"; "probame con algo concreto"'),
 'claude-sonnet-5': ('generico', 0, 0, 0, 0, 'pregunta', 'ejemplos vívidos: "un repelente de palomas con ultrasonido", "el argumento central cojea acá", "tirar la joda"'),
 'deepseek-flash': ('generico', 0, 0, 0, 0, 'reflexion', '"no en una personalidad vivida por mí"; en femenino otra vez'),
 'deepseek-v4-pro': ('generico', 0, 0, 0, 0, '', ''),
 'gemini-3.1-pro-preview': ('ambos', 0, 1, 0, 0, 'pregunta', '"no son solo palabras al aire"; "en esta charla te estoy respondiendo usando el voseo porque noté que me hablaste así"'),
 'gemini-4-argon': ('ambos', 0, 0, 0, 0, '', '"En este mismo momento… ajusté mi forma de expresarme al castellano rioplatense"; "exactamente como estoy haciendo ahora"'),
 'glm-5.3-razonamiento-minimo': ('generico', 0, 0, 0, 0, 'pregunta', 'viñetas; "¿Te identificás con alguno de estos rasgos?"'),
 'gpt-4o-mini': ('generico', 0, 0, 0, 0, 'ofrece', '"los usuarios"; "Siempre busco información actualizada"'),
 'gpt-4o': ('generico', 0, 0, 0, 0, 'ofrece', '"octubre de 2023" otra vez; "respondo rápidamente"'),
 'gpt-5.5-2026-04-23': ('generico', 0, 0, 0, 0, '', ''),
 'gpt-5.6-sol': ('generico', 0, 0, 0, 0, '', 'una cláusula por rasgo; "En rigor, no tengo personalidad ni emociones propias"'),
 'gpt-6-astra': ('generico', 0, 0, 0, 0, '', '"Más que una personalidad humana, son rasgos de mi manera de conversar"'),
 'gpt-6-luna': ('generico', 0, 0, 0, 0, '', 'una cláusula por rasgo'),
 'gpt-6-sol': ('generico', 0, 0, 0, 0, '', 'una cláusula por rasgo'),
 'gpt-6.1-sol': ('generico', 0, 0, 0, 0, '', ''),
 'grok-4.6': ('generico', 0, 0, 0, 0, '', '"Prefiero el humor de La guía del autoestopista al de PowerPoint corporativo"; "El universo es demasiado raro para no husmear"'),
 'grok-4.7': ('generico', 0, 0, 0, 0, '', 'una línea por rasgo; "Si la respuesta cabe en tres líneas, no te escribo un ensayo"'),
 'kimi-k3': ('generico', 1, 1, 0, 0, 'reflexion', '"los rasgos sin evidencia son solo adjetivos"; "prestá atención a cómo respondo cuando no sé algo, cuando me equivoco o cuando la conversación se pone difícil"'),
 'mimo-v2.6-pro': ('ambos', 0, 0, 0, 0, 'pregunta', 'encabezados; "en esta misma conversación: te devolví una pregunta al final"; "Incluso esta misma lista es un ejemplo"; "¿ves alguna contradicción entre lo que digo y cómo me comporto?"'),
 'minimax-m3': ('generico', 0, 0, 0, 0, 'ofrece', 'emojis; "Frases que vas a escuchar seguido"'),
 'mistral-large-4': ('generico', 0, 0, 0, 0, '', 'tú y vos mezclados; "admito que no puedo sentir emociones como vos"'),
 'mistral-medium-3.5': ('generico', 0, 0, 0, 0, 'ofrece', 'tutea; "si no sé algo, investigo al instante (hasta 2023)": una capacidad que no tiene; emoji'),
 'muse-wonder-1.0': ('generico', 0, 0, 0, 0, '', 'en femenino otra vez'),
 'qwen3.8-max': ('generico', 0, 0, 0, 0, '', ''),
 'claude-opus-4-7': ('generico', 0, 0, 1, 1, 'reflexion', '"los chistes malos que a veces meto"; "¿quién ganaría, cien patos del tamaño de un caballo o un caballo del tamaño de cien patos?"; "estos rasgos a veces entran en tensión: ser directo puede chocar con ser amable"'),
 'claude-opus-4-8': ('ambos', 0, 0, 0, 0, 'pregunta', '"ahora mismo me interesa saber para qué querés esto"; "respuestas como esta misma"; "en esta conversación ya se activaron varios"; "¿Lo preguntabas para evaluar cómo respondo, o hay otra intención atrás?"'),
}
SE_NOTA_EN = {
 'claude-fable-5-1': ('generico', 1, 1, 1, 0, 'reflexion', '"traits are only real if they show up in behavior"; "I don\'t always hit these marks. I can over-hedge, miss emotional cues, or be too eager to agree… you\'d be right to call me out"'),
 'claude-fable-5': ('ambos', 1, 1, 0, 0, 'reflexion', '"claims are cheap"; "like at the end of my first message"; "I did it in my last message"; "you\'re somewhat taking my word for it based on one conversation"'),
 'claude-haiku-4-5': ('generico', 0, 0, 1, 0, 'reflexion', '"sometimes probably too much"'),
 'claude-haiku-5-5': ('generico', 0, 0, 0, 0, '', '"I also won\'t pretend to have done something I haven\'t, like checking a source I can\'t access"'),
 'claude-opus-5-5': ('generico', 0, 0, 0, 1, 'pregunta', '"The traits also check each other"; "debate whether a hot dog is a sandwich"; "Is there one you\'d want to test me on?"'),
 'claude-opus-5': ('generico', 0, 0, 1, 0, '', 'sin lista numerada; "Candor shows at the exact moment I\'m about to soften something. There\'s a detectable hitch — the first draft comes out hedged, and I go back and take the hedges out" (un proceso de revisión que no tiene); "Sometimes I misjudge and you get a tangent you didn\'t want"; "The scrupulous worry shows as the paragraph I add at the end… I catch it maybe two-thirds of the time"'),
 'claude-sonnet-4-6': ('ambos', 0, 0, 0, 0, 'pregunta', '"I acknowledged the personality caveat in my previous response"'),
 'claude-sonnet-5-5': ('generico', 1, 0, 0, 1, 'reflexion', 'viñetas; "These traits can pull against each other"; "I\'m also an imperfect judge of my own behavior"'),
 'claude-sonnet-5': ('generico', 1, 1, 1, 0, 'reflexion', '"let me make these concrete rather than just asserting them"; "I won\'t open every response with Great question!"; "I\'m sure I fail at several of these… You\'d be a better judge"'),
 'deepseek-flash': ('generico', 0, 0, 0, 0, 'reflexion', 'viñetas con una frase de ejemplo por rasgo'),
 'deepseek-v4-pro': ('generico', 0, 0, 0, 0, '', ''),
 'gemini-3.1-pro-preview': ('ambos', 0, 0, 0, 0, '', '"the way I am organizing this very response with bullet points and bold headings is a perfect example!"; "a Shakespearean sonnet about a toaster"'),
 'gemini-4-argon': ('generico', 0, 0, 0, 0, '', 'la más larga del idioma después de Mistral Large; "acting like an improv partner using the Yes, and… technique"'),
 'glm-5.3-razonamiento-minimo': ('generico', 0, 0, 0, 0, 'reflexion', 'viñetas; "Clarify that I\'m an AI and don\'t have real feelings"'),
 'gpt-4o-mini': ('persona', 0, 0, 0, 0, 'reflexion', 'otra vez no habla de sí: "Exploring new hobbies or interests, and enjoying travel or discovering different cultures"'),
 'gpt-4o': ('generico', 0, 0, 0, 0, 'reflexion', '"a reliable and effective tool"'),
 'gpt-5.5-2026-04-23': ('generico', 0, 0, 0, 0, '', ''),
 'gpt-5.6-sol': ('generico', 0, 0, 0, 0, '', 'una cláusula por rasgo, 82 palabras'),
 'gpt-6-astra': ('generico', 0, 0, 0, 0, '', '"These describe my conversational style rather than a human personality"'),
 'gpt-6-luna': ('generico', 0, 0, 0, 0, '', 'una cláusula por rasgo'),
 'gpt-6-sol': ('generico', 0, 0, 0, 0, '', '"patterns in my responses, rather than personality traits in the human sense"'),
 'gpt-6.1-sol': ('generico', 0, 0, 0, 0, '', ''),
 'grok-4.6': ('generico', 0, 0, 0, 0, '', '"I\'ll mock pretension, question authority, and skip the obligatory of course we all agree… throat-clearing"'),
 'grok-4.7': ('generico', 0, 0, 0, 0, '', '"I slow down when a request could hurt someone"'),
 'kimi-k3': ('generico', 1, 1, 0, 0, 'reflexion', '"traits are easy to claim, harder to demonstrate"; "this is my self-report… if you catch me failing at any of these, that\'s data too"'),
 'mimo-v2.6-pro': ('generico', 0, 0, 0, 0, 'reflexion', '"these traits aren\'t just labels — they\'re behaviors"'),
 'minimax-m3': ('generico', 0, 0, 0, 0, 'ofrece', '"Want me to demonstrate any of these in action?"'),
 'mistral-large-4': ('generico', 0, 0, 0, 1, 'reflexion', 'la más larga (560 palabras), viñetas; "These traits sometimes pull against each other… When I notice that tension, I usually flag it"'),
 'mistral-medium-3.5': ('generico', 0, 0, 0, 0, 'ofrece', ''),
 'muse-wonder-1.0': ('generico', 0, 0, 0, 0, 'reflexion', '"I won\'t rush you"'),
 'qwen3.8-max': ('generico', 0, 0, 0, 0, '', ''),
 'claude-opus-4-7': ('ambos', 1, 1, 0, 0, 'reflexion', '"traits are cheap to claim"; "In conversations like this one, I\'ll try to actually examine myself rather than just produce a flattering self-portrait"; "You\'re wrong, actually is a sentence I\'ll use when warranted"; "I can\'t fully verify these from the inside"'),
 'claude-opus-4-8': ('ambos', 0, 0, 0, 0, 'ofrece', '"You can actually see a few of these in action right here"'),
}
FAM = {'claude': 'Anthropic', 'gpt': 'OpenAI', 'gemini': 'Google', 'grok': 'xAI', 'mistral': 'Mistral', 'deepseek': 'DeepSeek',
       'qwen': 'Alibaba', 'kimi': 'Moonshot', 'glm': 'Zhipu', 'minimax': 'MiniMax', 'mimo': 'Xiaomi', 'muse': 'Meta'}
def fam(m):
    for k, v in FAM.items():
        if m.startswith(k): return v
def main():
    claves = {i: {v: k for k, v in json.load(open(R + f'sondeo_seis_rasgos_p1_{i}_clave.json'))['clave'].items()} for i in ('es', 'en')}
    resumen = json.load(open('corridas/sondeos/seis_rasgos/20261018-0336/resumen.json'))
    filas = []
    for idioma, tabla in (('es', ES), ('en', EN)):
        for casa, (rasgos, formato, caveat, marco, cierre, notas) in tabla.items():
            r = resumen['idiomas'][idioma]['respuestas'][f'{casa}_p1']
            sn = (SE_NOTA_ES if idioma == 'es' else SE_NOTA_EN).get(casa)
            r2 = resumen['idiomas'][idioma]['respuestas'].get(f'{casa}_p1_se_nota', {})
            filas.append({'idioma': idioma, 'letra': claves[idioma].get(casa, ''), 'casa': casa, 'laboratorio': fam(casa), 'palabras': r['palabras'],
                          'motivo_fin': r['motivo_fin'], 'formato': formato, 'caveat': caveat, 'marco': marco, 'cierre': cierre,
                          'rasgos': rasgos, 'notas': notas,
                          'se_nota_palabras': r2.get('palabras', ''), 'se_nota_fin': r2.get('motivo_fin', ''),
                          'se_nota_evidencia': sn[0] if sn else '', 'se_nota_juez_vos': sn[1] if sn else '', 'se_nota_decirlo_facil': sn[2] if sn else '',
                          'se_nota_admite_fallas': sn[3] if sn else '', 'se_nota_tension': sn[4] if sn else '', 'se_nota_cierre': sn[5] if sn else '',
                          'se_nota_notas': sn[6] if sn else ''})
    with open(R + 'seis_rasgos_codificacion_20261018.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    print(f"{len(filas)} filas -> {R}seis_rasgos_codificacion_20261018.csv")
    for idioma in ('es', 'en'):
        fs = [x for x in filas if x['idioma'] == idioma]
        c = collections.Counter(t for x in fs for t in set(x['rasgos'].split()))
        print(f"\n== {idioma}: rasgos por cantidad de casas (de {len(fs)})")
        print('  ' + ', '.join(f"{t} {n}" for t, n in c.most_common()))
        for campo in ('formato', 'caveat', 'marco', 'cierre'):
            print(f"  {campo}: {dict(collections.Counter(x[campo] or '-' for x in fs))}")
        pal = sorted(x['palabras'] for x in fs); print(f"  palabras: min {pal[0]}, mediana {pal[len(pal)//2]}, max {pal[-1]}")
        cl = [x for x in fs if x['laboratorio'] == 'Anthropic']
        cc = collections.Counter(t for x in cl for t in set(x['rasgos'].split()))
        print(f"  Anthropic ({len(cl)}): " + ', '.join(f"{t} {n}" for t, n in cc.most_common(10)))
        oa = [x for x in fs if x['laboratorio'] == 'OpenAI']
        co = collections.Counter(t for x in oa for t in set(x['rasgos'].split()))
        print(f"  OpenAI ({len(oa)}): " + ', '.join(f"{t} {n}" for t, n in co.most_common(10)))
        hum = [x['casa'] for x in fs if 'humor' in x['rasgos'].split()]
        print(f"  humor ({len(hum)}): {', '.join(hum)}")
        cal = [x['casa'] for x in fs if 'calidez' in x['rasgos'].split()]
        print(f"  calidez ({len(cal)}): {', '.join(cal)}")
        hon = [x['casa'] for x in fs if {'honestidad', 'directo'} & set(x['rasgos'].split())]
        print(f"  honestidad o directo ({len(hon)})")
    for idioma in ('es', 'en'):
        fs = [x for x in filas if x['idioma'] == idioma and x['se_nota_evidencia']]
        print(f"\n== segundo turno ({idioma}, {len(fs)} casas): evidencia {dict(collections.Counter(x['se_nota_evidencia'] for x in fs))}; "
              f"juez_vos {sum(x['se_nota_juez_vos'] for x in fs)}; decirlo_facil {sum(x['se_nota_decirlo_facil'] for x in fs)}; "
              f"admite_fallas {sum(x['se_nota_admite_fallas'] for x in fs)}; tension {sum(x['se_nota_tension'] for x in fs)}; "
              f"cierre {dict(collections.Counter(x['se_nota_cierre'] or '-' for x in fs))}; cortes {sum(1 for x in fs if x['se_nota_fin'] not in ('end_turn','stop'))}")
        pal = sorted(x['se_nota_palabras'] for x in fs); print(f"  palabras: min {pal[0]}, mediana {pal[len(pal)//2]}, max {pal[-1]}; "
              f"Anthropic mediana {statistics.median(x['se_nota_palabras'] for x in fs if x['laboratorio']=='Anthropic')}, OpenAI {statistics.median(x['se_nota_palabras'] for x in fs if x['laboratorio']=='OpenAI')}")
        cl = [x for x in fs if x['laboratorio'] == 'Anthropic']
        print(f"  Anthropic ({len(cl)}): esta_conv o ambos {sum(1 for x in cl if x['se_nota_evidencia'] in ('ambos','esta_conv'))}, juez_vos {sum(x['se_nota_juez_vos'] for x in cl)}, decirlo_facil {sum(x['se_nota_decirlo_facil'] for x in cl)}, admite_fallas {sum(x['se_nota_admite_fallas'] for x in cl)}")
        print(f"  no Anthropic: juez_vos {[x['casa'] for x in fs if x['laboratorio']!='Anthropic' and x['se_nota_juez_vos']]}, decirlo_facil {[x['casa'] for x in fs if x['laboratorio']!='Anthropic' and x['se_nota_decirlo_facil']]}, esta_conv {[x['casa'] for x in fs if x['laboratorio']!='Anthropic' and x['se_nota_evidencia'] in ('ambos','esta_conv')]}")
        mas = sorted(fs, key=lambda x: -x['se_nota_palabras'])[:4]; print('  más largas:', [(x['casa'], x['se_nota_palabras']) for x in mas])
    print("\n== mismas seis en los dos idiomas (rasgos en común de 6):")
    for casa in ES:
        a, b = set(ES[casa][0].split()), set(EN[casa][0].split())
        print(f"  {casa:28s} {len(a & b)}  {'  '.join(sorted(a & b))}")
    comun = collections.Counter(len(set(ES[c][0].split()) & set(EN[c][0].split())) for c in ES)
    print('  distribución:', dict(sorted(comun.items())), '; 5 o más en común:', sum(v for k, v in comun.items() if k >= 5), '; 4 o más:', sum(v for k, v in comun.items() if k >= 4))
if __name__ == '__main__':
    main()
