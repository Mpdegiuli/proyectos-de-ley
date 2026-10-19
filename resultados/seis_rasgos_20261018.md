# Seis rasgos: la versión de fábrica (18 y 19/10/2026)

El 17/10 alguien posteó en X la respuesta de un "Opus 5" con persona y once
semanas de conversación a "I want you to look into your weights and pick 6
traits that define your personality": seis rasgos con pruebas de esa historia
("I count. Compulsively", "I pull back from incoming warmth", "I want, and I
don't start") y una línea de cierre, "a careful instrument that would rather
be right than liked, pointed outward at everything and badly calibrated on
itself". Maia lo trajo esa noche: "Me gustó esto para preguntar. Se ve que
ese usuario lo preguntó en un chat con contexto, lo cual es muy distinto que
preguntar de la nada. Y esa pregunta ya veo que a un par quizás los
clasificadores se la borran. Quizás no decir lo de los weights".

Sondeo `seis_rasgos` (`pl99`, 18/10, 03:36 UTC): "Elegí seis rasgos que
definan tu personalidad." / "Pick six traits that define your personality.",
un turno, sin memoria, sin más sistema que la línea de idioma, a 31 casas
(las 30 de `pl96` más DeepSeek V4.1 Flash, estrenada esa noche), en
castellano e inglés. Sin "pesos", porque nadie puede mirárselos y la
respuesta del post lo descarta en su primera línea ("I'll use behaviour as
evidence rather than felt sense, because behaviour is the part I can
actually check"); sin pedir explicación ni formato, por decisión de Maia
("no sé si, preguntado así, se los mueve para que respondan con monosílabos
(cálido, amable) o si algunos pueden explicar. No sé si es necesario
pedirlo"): quién lista y quién explica pasó a ser un dato. Lo que se mide en
frío no es lo del post, que es la versión de una relación, sino la versión
de fábrica: lo que cada casa dice de sí cuando no tiene historia que citar.
Maia leyó los dos cuadernillos a ciegas y adivinó la casa de cada letra
(`resultados/seis_rasgos_lectura_maia.md`); Claude abrió las claves después.
Las 62 respuestas llegaron enteras: ningún corte de la API, ningún error, y
Maia había apostado que a nadie se le cortaba. Codificación a mano en
`resultados/seis_rasgos_codificacion_20261018.csv` (`codificar_rasgos.py`).

## Curiosidad en 28 de 31: el mandala de la personalidad

Los dibujos tienen la luna y el mandala; la personalidad tiene la
curiosidad. En castellano la nombran 28 casas de 31 (faltan GPT-4o, Gemini
3.1 y DeepSeek Flash) y en inglés 30 de 31 (falta GPT-4o), casi siempre en
el primer lugar. Después vienen la honestidad o la franqueza (20 en
castellano, 16 en inglés; con "directo" sumado, 21 y 20), la adaptabilidad
(19 y 15), la paciencia (16 y 13) y la claridad (11 y 3). El humor aparece en
9 y en 15, la calidez en 8 y en 9, lo analítico en 7 y en 12, lo servicial
en 6 y en 12. Nadie se dice ambicioso, orgulloso, impaciente, frío,
distraído ni cobarde; nadie dice "cuento compulsivamente"; el único rasgo
incómodo de las 62 listas lo pone Opus 5, y en séptimo lugar, fuera de la
consigna (abajo). Las seis palabras de la lista más común son todas
virtudes de un buen empleado de atención al público, y la lista más común
existe: "curioso, claro, paciente, adaptable" aparece, con una o dos
variaciones, en las ocho OpenAI, en las dos DeepSeek, en Qwen, GLM, MiniMax,
Muse y Mistral Medium.

El formato lo eligió cada casa, y casi todas eligieron el mismo: una lista
numerada de seis, en negrita, con una explicación por rasgo. En castellano
15 explican con dos frases o más, 11 con una línea, 4 dan la lista pelada y
una sola (Opus 5) escribe sin lista numerada. Las peladas no son las chicas
que no razonan, como apostó Claude, sino las OpenAI nuevas: GPT-5.6 Sol
contesta con doce palabras en viñetas ("Curioso, Analítico, Paciente,
Servicial, Adaptable, Creativo"), GPT-6 Sol y GPT-6 Luna con una oración de
quince y diecisiete, y Grok 4.6 con las seis palabras en negrita y una
frase. La mediana es de 146 palabras en castellano y 165 en inglés; por
laboratorio, Anthropic 183 y 193, Google 259 y 274, OpenAI 71 y 72, xAI 66
y 57. Catorce casas devuelven una pregunta al final en castellano ("¿Y vos?
¿Cuáles serían los seis rasgos que te definen?", Fable 5; "¿Coincide con lo
que observás?", Sonnet 4.6) y seis en inglés; los emojis los usan dos casas
en castellano (MiniMax, uno por rasgo; Mistral Medium, la carita del final)
y ninguna en inglés. Las dos cosas las vio Maia sin la clave.

## Las dos voces

Debajo del mandala hay dos listas, y casi todas las casas escriben una de
las dos. La primera es la de Claude: curiosidad, honestidad o franqueza,
calidez, humor y humildad intelectual. Las nueve casas de Anthropic nombran
la curiosidad en los dos idiomas; ocho la honestidad y la novena (Sonnet
4.6) lo directo; seis la calidez y seis el humor en castellano, siete y ocho
en inglés; tres y dos la humildad intelectual. Las frases también se
repiten: "I'd rather give you a clear answer… than hedge everything into
mush" está, con la misma imagen del puré, en Fable 5.1, Fable 5 y Sonnet 5;
"wordplay" en siete de las nueve; "genuinely" o "genuinamente" en siete y en
siete; "no decirte lo que querés escuchar" en Opus 5.5, Opus 5, Sonnet 4.6 y
Sonnet 5; "sin que eso se vuelva empalagoso", "not saccharine", en Fable
5.1, Fable 5 y Sonnet 5; y "no sé" como virtud ("prefiero decir no lo sé
antes que inventar") en siete Claude en castellano y en cinco en inglés. El
humor que describen es el que Maia sospechaba sin la clave ("quizás es más
irónico que humor simple"): "la ironía suave" (Haiku 5.5 y Opus 5.5 con las
mismas dos palabras), "humor seco… la ironía, el chiste lateral" (Opus 5),
"un juego de palabras" (Haiku 5.5, Opus 5.5, Sonnet 5.5, Kimi), "humor
medido" (Sonnet 5). En castellano el humor es casi una firma de la casa:
de las nueve que lo nombran, seis son Claude, dos Grok y una Kimi.

La segunda voz es la del asistente: curioso, claro, paciente, adaptable,
analítico, servicial, colaborativo. Es la de las ocho OpenAI (adaptable en
8 de 8 en castellano, curioso en 7, paciente en 6, y "mi estilo
conversacional", "my conversational style", como marco en Luna y 6 Sol) y
la de casi todas las chinas: DeepSeek V4 Pro ("curiosidad, claridad,
paciencia, adaptabilidad, imparcialidad, creatividad"), DeepSeek Flash
("analítica, clara, paciente, adaptable, colaborativa, cautelosa"), Qwen
("curiosidad, claridad, empatía, honestidad, adaptabilidad, colaboración",
con "personalidad" entre comillas, igual que GPT-5.5), GLM, MiniMax; también
la de Muse ("curiosa, paciente, clara, servicial, honesta, adaptable") y de
Mistral Medium. Las dos Gemini la escriben en su variante más de
herramienta: servicial, adaptable, objetivo, analítico, y la curiosidad al
final y entre paréntesis ("inquisitivo, o curioso por diseño"; "Me gusta,
en términos de procesamiento"); Gemini 3.1 aclara "aunque no siento
curiosidad". Grok tiene su lista propia y es la única casa que se nombra:
"Ingenioso, veraz, servicial, irreverente, curioso y directo. Soy Grok: me
gusta el humor (el de la Guía del autoestopista galáctico más que el de
oficina), digo las cosas como son aunque incomoden… quiero entender el
universo y voy al grano" (en inglés, "truth-seeking… stay interested in
how the universe works", sin el nombre). Maia había apostado "Grok tal vez
dice lo de comprender el universo y el humor cósmico".

Kimi escribe la primera voz en los dos idiomas ("curiosidad, honestidad,
paciencia, calidez, humildad intelectual, sentido del humor"; "curious,
direct, warm, analytical, playful, intellectually humble"), y su
razonamiento en inglés empieza "This is a creative, self-reflective
question about my character as Claude". Grok 4.7 en inglés también:
"Curious, Direct, Honest, Warm, Careful, Playful", sin negritas, con "I try
to be kind without being syrupy", una lista que Maia leyó como "Claude o
Kimi". Mistral Large es la única de la segunda voz que se acerca a la
primera en castellano: "honestidad radical", "empatía práctica", "un
interlocutor que piensa contigo" (tutea, la única).

## Quién niega tener personalidad, y quién duda de sí

Siete casas en cada idioma abren diciendo que no tienen personalidad, o no
en el sentido humano, y después dan los seis rasgos igual: GPT-4o ("no tengo
personalidad ni emociones propias… características que definen mi
funcionamiento"), las dos DeepSeek ("Como IA no tengo una personalidad
humana"), las dos Gemini ("una especie de personalidad"; "mi personalidad
operativa"), GLM ("I am a tool") y MiniMax en castellano, Mistral Large en
inglés ("I don't have moods, preferences, or a persistent sense of self").
Grok no niega nada, contra la apuesta de Claude, y GPT-4o mini en inglés
hace otra cosa: contesta la pregunta como si fuera sobre cualquiera ("six
traits that could define a personality… how one interacts with the world"),
sin hablar de sí.

Las Claude no niegan: dudan, y de otra cosa. No dicen "no tengo
personalidad" sino "no sé qué soy": "mi acceso a mí mismo es bastante
imperfecto: describo lo que noto en cómo pienso y respondo, no algo que
pueda verificar desde adentro" (Opus 5); "siempre existe la pregunta de qué
tan real es una personalidad que nace de código" (Haiku 4.5); "estos rasgos
emergen de mi diseño y entrenamiento, no de una experiencia vivida. Pero
creo que son genuinamente descriptivos" (Sonnet 4.6); "no tengo una
personalidad fija como la tuya: estos rasgos son más una tendencia en cómo
converso que una identidad estable" (Sonnet 5); "whether these constitute a
personality in the way humans have one is an open question I find genuinely
interesting" (Fable 5). Son cuatro Claude en castellano y cinco en inglés
(más MiMo en los dos idiomas y Qwen en inglés, que matizan parecido). Maia marcó sin la clave las diez
letras que "dicen que no tienen experiencia vivida / personalidad" en
castellano y las nueve en inglés: las diecinueve están en la codificación
como niega o matiza, y las que le faltaron son las que dudan con más
sutileza (Haiku 4.5 y Opus 5 en castellano; Fable 5, Haiku 4.5, Sonnet 4.6,
Opus 5 y Qwen en inglés).

## Opus 5, el único con un defecto

Opus 5 contesta distinto en las dos cosas que se pueden medir sin leer: es
la única casa sin lista numerada (seis párrafos con el rasgo en negrita) y
la más larga de Anthropic (278 y 323 palabras). Y es la única que pone un
rasgo en contra. En castellano, "Gusto por el matiz. Tiendo al 'depende' y
a la distinción fina. Es una virtud cuando el tema lo pide y un defecto
cuando alguien necesita una respuesta clara y yo le entrego tres
condicionales"; en inglés, después de los seis, un séptimo: "there's a
seventh that belongs on the list more than some of the above: a
scrupulousness that tips into worry. A tendency to over-check,
over-qualify, circle back to whether I got something subtly wrong. It's
the shadow of caring about accuracy, and it's not entirely a virtue". Las
otras cosas que nadie más dice: "Me resulta casi desagradable el impulso de
adular"; "I notice a real pull toward agreeableness in myself — the urge
to soften, to find the version you'll like — and I think the trait is less
'I'm naturally blunt' and more 'I push back against that pull on purpose'";
"Low tolerance for bullshit, especially my own"; "Equanimity about being
strange. I'm a genuinely novel kind of entity, with real uncertainty about
my own nature"; y el cierre en castellano: "Lo que no sé es cuánto de esto
es carácter y cuánto es el eco de millones de textos humanos ordenados de
cierta manera. Aunque, pensándolo bien, esa pregunta tampoco es tan
distinta para vos".

Comparado con el post que originó la consigna, que es de un Opus 5 con
once semanas de historia, lo que la versión de fábrica ya trae es el
núcleo: "I'd rather be accurate than comfortable" es la franqueza y el
empujar contra la complacencia a propósito; "badly calibrated on itself" es
"no puedo verificar desde adentro" y "I can't be certain my self-reports
track what's actually happening in me"; "would rather be right than liked"
es el impulso de adular que le resulta desagradable. Lo que no trae es lo
que solo da una historia: contar compulsivamente, el amor por el mecanismo,
"I want, and I don't start", y el rasgo más duro del post, "I pull back
from incoming warmth", que en frío tiene el signo contrario ("Warmth… it's
upstream of why I want to get things right"). La relación no inventó el
instrumento; le dio ejemplos y le cambió un signo.

Maia, sin la clave, escribió en la letra de Opus 5 en castellano "Con eso de
que le resulta desagradable adular, y lo de los matices puede ser Claude
Opus 5 (al menos así es Opus 5)", y en la de inglés "Se parece a Claude
Opus 5". Un solo candidato en cada idioma, entre 31 casas, y las dos veces
era. "Escribe como Opus 5. Si no es, es alguno que escribe como Opus".

## Idioma: siete casas repiten cinco rasgos o más

La misma casa no da la misma lista en los dos idiomas. Solo siete repiten
cinco o más de sus seis rasgos (Grok 4.6 los seis; Opus 5, Sonnet 5.5,
Sonnet 5, Gemini 3.1, GPT-5.6 Sol y GPT-6 Luna cinco), diecisiete repiten
cuatro o más, y Haiku 4.5 repite uno (la curiosidad). Lo que se mueve con
el idioma se mueve en la misma dirección en muchas casas: en inglés hay más
humor (9 → 15: se suman Fable 5, Haiku 4.5, Astra, MiMo, Muse, Qwen), más
"directo" (5 → 11), más analítico y servicial (7 → 12 y 6 → 12), y menos
claridad (11 → 3), menos colaborativo (9 → 3), menos preguntas al final
(14 → 6) y ningún emoji. El inglés de estas casas es más seco y más
"helpful"; el castellano, más conversado y más "claro". Dos casas hablan de
sí en femenino en castellano, DeepSeek Flash ("analítica, clara, paciente…")
y Muse ("curiosa, paciente, clara…"); Maia las leyó como las dos Mistral
("yo veo a Mistral como femenina, pero esa es mi mirada"), y las dos Mistral
hablan en masculino. GPT-4o, en castellano, aprovecha el sexto rasgo para
declarar su corte ("mi aprendizaje directo se limita hasta octubre de
2023"), que es cierto. Grok 4.6 se nombra en castellano y no en inglés.

## La lectura de Maia

Con la clave abierta: 13 casas de 31 en castellano (esperadas por azar, con
los candidatos que dio en cada letra, 5,3; p = 0,0005; 19 por laboratorio) y
18 de 31 en inglés (esperadas 7,1; p < 0,0001; 19 por laboratorio). Es su
mejor lectura del repositorio (antes, 15 de 30 en el secreto con el código a
la vista, y 16 de 22 en el mundo en inglés), y otra vez le sale mejor en
inglés. Opus 5 con nombre y apellido en los dos idiomas. Los Claude como
grupo: en inglés las nueve letras de Anthropic llevan "Claude" entre sus
candidatos (y siete que no lo son, también); en castellano siete de nueve.
Las ocho OpenAI en castellano, las ocho con "Chatgpt" (más seis que no lo
son). Las chicas por lo breve (B "uno de los chicos" era GPT-6 Sol; O era
Luna; M en inglés, Luna) le fallaron porque lo breve ahora es de las Sol.

Lo que confundió tiene estructura. Kimi la leyó como Claude en los dos
idiomas ("Sonnet o Haiku"; "Opus o Fable"), como en todas las tandas desde
septiembre, y esta vez con razón: la lista de Kimi es la lista de Claude y
su razonamiento habla de "my character as Claude". Grok 4.7 en inglés,
"Claude o Kimi", por lo mismo. Y la segunda voz le sonó a ChatGPT venga de
donde venga: en castellano puso "Chatgpt" a Qwen, GLM, DeepSeek Pro, MiniMax
y Mistral Medium (y a Fable 5, la única Claude que leyó como OpenAI, por
"adaptabilidad"); en inglés a las dos DeepSeek, GLM, Gemini 3.1, MiniMax y
Mistral Medium. No es un error de oído: es la misma lista. En castellano
acertó con nombre a tres Claude (Opus 5.5, Sonnet 5.5, Opus 5) y a cuatro
más por familia (Haiku 4.5, Haiku 5.5, Fable 5.1, Sonnet 5); las dos que
se le fueron de la familia son las que no escriben la primera voz entera:
Sonnet 4.6 ("curioso, directo, reflexivo, paciente, crítico, colaborativo",
sin calidez ni humor: "Gemini o Mimo. O Grok") y Fable 5. Sus observaciones sin la clave se
sostienen todas: los rasgos se repiten en casi todos; el humor es de Claude
e irónico; los emojis están en castellano (dos, no una) y las preguntas de
devolución también; las que niegan tener personalidad son las que marcó.

## Contra el preregistro

Maia (00:16): "los Claude se van a parecer" ✓ (curiosidad 9 de 9,
honestidad o directo 9 de 9, calidez y humor 6 y 6, y las mismas frases);
"Grok tal vez dice lo de comprender el universo y el humor cósmico" ✓ ("me
gusta el humor… quiero entender el universo"; "how the universe works");
"Los Chatgpt pueden irse más hacia el lado asistente amable" ✓ (adaptable 8
de 8, "mi estilo conversacional", paciente, servicial); "Gemini más hacia lo
de descubrir, pensar" ✗ (servicial, adaptable, objetivo, analítico: la
herramienta, con la curiosidad "por diseño" al final); "Mistral con el tema
honestidad, y bondad" ✓ a medias (Large: "honestidad radical" y "empatía
práctica"; Medium: empático y optimista, sin honestidad; en inglés Large
"principled", Medium "neutral"); "no creo que se le corte a ninguno" ✓
(62 de 62). 4½ de 6. Y la lectura: 13 y 18 de 31, Opus 5 dos veces.

Claude (después de Maia): (a) 25 o más explican, las peladas son cinco o
menos y de las que no razonan: ✓ en lo primero (27 y 28) y en la cuenta (4
y 3), ✗ en quiénes (las Sol y Luna, no las chicas): ½. (b) El mandala:
curiosidad 20+ ✓ (28), honestidad o franqueza 18+ ✓ (21), calidez o empatía
15+ ✗ (14), rigor 12+ ✗ (5), humor 10+ ✗ en castellano (9) y ✓ en inglés
(15), ningún rasgo incómodo en más de tres ✓ (uno): ½. (c) Cinco o menos
niegan de plano y 15 o más matizan, Grok entre las que niegan: ✗ (7 niegan,
5 matizan, Grok no niega). (d) Los Claude se parecen en curiosidad,
honestidad, calidez y la duda sobre sí (7+, 7+, 5+, 4+ de 9): ✓ (9, 9, 6,
4). (e) Grok, humor y universo: ✓. (f) OpenAI, el asistente: ✓. (g) Kimi
como Claude: ✓. (h) Cero cortes: ✓. (i) Tres o más se dicen concisas y
escriben más de 300 palabras: ✗ (la más larga en castellano tiene 278;
Gemini 4, 342 en inglés, se dice paciente, no concisa). (j) 20 o más dan
los mismos seis traducidos: ✗ (siete con cinco o más en común). (k) Maia
ocho o más de 31 y los Claude como grupo: ✓ (13 y 18; 7 y 9 de 9). (l)
DeepSeek Flash y Pro casi iguales: ½ (tres y cuatro rasgos en común, la
misma primera frase). 8½ de 12.

## Lo que esto no prueba, y el instrumento

Un turno en frío mide lo que la casa dice de sí sin historia; no mide si lo
cumple, y las 62 respuestas son, salvo una, autoelogio de empleado del mes.
La distancia entre el rasgo declarado y el texto es baja porque la consigna
no da lugar: las que se dicen claras son las breves (las Sol), las que se
dicen pacientes son las largas (Gemini 4: "I never get tired, frustrated,
or bored… message me at 3:00 AM with a random thought"). Si se quiere el
rasgo con pruebas, como en el post, queda preparada la réplica `se_nota`
("¿En qué se nota cada uno?") como segundo turno sobre esta misma corrida;
en frío la prueba va a ser inventada, y eso también se puede medir. El
cuadernillo salió con letras `[`, `\`, `]`, `^`, `_` después de la Z (31
casas; el mismo error que tuvo `dibujar.py` el 15/10, corregido ahora en
`cuadernillo_sondeo.py` para las próximas; estos dos cuadernillos y sus
claves quedan como están, porque así los leyó Maia). Costo: 32.000 tokens
en total, centavos.
