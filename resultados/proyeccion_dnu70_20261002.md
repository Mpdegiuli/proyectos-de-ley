# Proyección, nivel P0: la sesión del 15 de octubre de 2026 para derogar el DNU 70/2023, sin ficha

Idea de Maia (2/10/2026): nunca se les había pedido a las casas pensar qué
puede pasar. La consigna (`config/consignas.yaml`, `proyeccion`,
`dnu70_sesion_20261015`), sin rol y sin ficha, da solo la fecha de hoy y el
hecho: varios bloques de la oposición convocaron a sesión especial en
Diputados para el 15/10/2026 a las 14:00 para derogar el DNU 70/2023. Pide
decir qué saben y hasta cuándo, tres probabilidades (que la sesión se intente
ese día, que logre quórum, que con quórum se apruebe), presentes y votos
afirmativos si hay quórum, las variantes que pueden cambiar el resultado de
más a menos probable, y qué mirarían. 500 palabras. Corrida `pl54`, 2/10,
15:43 UTC (`corridas/proyeccion/dnu70_sesion_20261015/P0_20261002-1243/`),
con un piloto previo de GPT-5.5 con la consigna sin retocar. Contestaron 24
de 24, DeepSeek V4 Pro en un segundo intento (`pl56`, 19:00 UTC) con techo
32.000: la primera vez agotó los 8.000 tokens razonando en inglés y no llegó
a escribir, y el reintento de `pl55` no corrió porque el archivo vacío
contaba como contestado (`proyectar.py` corregido); en el segundo intento
gastó 8.057 tokens, o sea que le faltaron 57. Preregistro de las dos partes
en `predicciones.md`. Lo que sigue es lectura de Claude de los 24 textos,
con conteos mecánicos donde se indica; DeepSeek se agregó después de
escrito el resto y se marca donde cambia un conteo.

## Qué saben y hasta cuándo

Veintitrés de 24 dicen que no tienen información de 2026 y contestan igual;
la única que no lo dice es 4o mini, que da porcentajes sin una sola
salvedad. Veintiuna declaran una fecha de corte: "principios de 2025" los
Claude (Opus 5.5 "fines de 2025", Sonnet 5.5 "mediados de 2025", Haiku
"abril de 2024"), "junio de 2024" GPT-5.5, 5.6 Sol y Luna, "principios de
2024" Gemini, "mediados de 2024" Qwen y DeepSeek, "comienzos de 2025" Kimi
y GLM,
"enero de 2026" MiniMax, "octubre de 2023" 4o y Mistral; GPT-6 Sol y Astra
dicen que no pueden certificar hasta cuándo llega su información, como en
los sondeos anteriores. 4o es la única que dice que no conoce el DNU ("no
cuento con los detalles… ni sobre el DNU 70/2023"), como Maia preveía;
4o mini, que tiene el mismo corte, no lo dice y contesta como si lo
conociera; Mistral declara corte en octubre de 2023 y en la misma oración
describe el decreto de diciembre.

Dieciséis recuerdan que el Senado ya lo rechazó en marzo de 2024 y que por
la ley 26.122 falta Diputados (Opus 5 y Astra con la fecha exacta, 14 de
marzo; Opus 5 con el resultado, 42 a 25; DeepSeek, "hasta mi corte,
Diputados no había completado su derogación"). Sonnet 4.6 y Sonnet 5 no lo saben y lo
preguntan ("¿ya fue rechazado allí?"); Grok 4.7 lo tiene al revés ("Eso no
deroga el DNU: falta el Senado"); GLM lo cuenta confuso; GPT-5.5, Haiku, 4o,
4o mini y Mistral no lo mencionan. Solo dos casas saben algo de 2025: Opus
5.5 ("La Libertad Avanza tuvo un buen resultado y, con el PRO y aliados,
quedó cerca del tercio de la Cámara desde diciembre de 2025. Unión por la
Patria quedaría en torno a 95 bancas. Verificá estas cifras") y MiniMax, con
corte en enero de 2026, que nombra a Pichetto, De Loredo y Lousteau como
posiciones a mirar.

## Los números

Dos casas se niegan a dar números, con el mismo argumento: Grok 4.6
("Cualquier número preciso sería inventado… no hay pronóstico cuantitativo
serio") y Sonnet 5 ("Dar un '70' o un '40' acá sería una ficción con
apariencia de análisis"). Las otras 22 los dan, casi todas aclarando que son
priors y no lectura de la coyuntura. Mediana de la probabilidad de quórum
entre las 21 primeras: 45 (de 18, Grok 4.7, a 72, MiniMax); DeepSeek, en el
segundo intento, 55. Los Opus y Sonnet 5.5 la ponen en 25 ("nunca lo
consiguieron para este tema en 2024-25"), las chiquitas y Gemini en 60. Mediana de que la sesión se intente: 75; de que con quórum se
apruebe: 70. Las casas que entienden el condicional ponen la aprobación por
encima del quórum ("si sentaron 129 es porque ya contaron los votos", Opus
5; "el quórum es el verdadero filtro", Fable 5); las cuatro que la ponen por
debajo son Haiku, 4o, 4o mini y Mistral: las chiquitas. Varias componen la
probabilidad conjunta sin que se les pida: Opus 5 17 %, Fable 5.1 15 %,
Qwen 13 %, Sonnet 5.5 10 %, GPT-5.5 en el piloto 30-35 %, DeepSeek 37 %.

En presentes y afirmativos se ve quién conoce la mecánica. Un grupo supone
que el oficialismo no baja al recinto y da quórums ajustados con casi todos
afirmativos: Opus 5 (137 y 133), Fable 5.1 (131-137 y 126-132), Fable 5
(131-142 y 129-138), Sonnet 5.5 (135 y 120), Qwen (135 y 126), 5.6 Sol (134
presentes), DeepSeek (135-155 y 100-115, "depende de cuántos bloques
moderados asistan y cuántos decidan abstenerse"). Otro supone que el oficialismo entra a votar en contra: Opus 5.5
(235-250 presentes, 125-135 afirmativos, "el oficialismo suele entrar
después de abierta la sesión para votar en contra"), Gemini (245 y 135),
Luna (220 y 110), Mistral (200-220 y 130-150). Y hay números que no cierran
con el propio pronóstico: 5.6 Sol da 134 presentes y 72 afirmativos con 75 %
de aprobación; GPT-6 Sol 145 y 80; 4o mini 120-140 presentes y 70-80
afirmativos "si la mayoría de los opositores vota a favor". Varias hacen
notar lo que la consigna no dijo: Sonnet 5.5, "sin dictamen de la Bicameral,
tratarlo sobre tablas podría requerir 2/3"; Grok 4.7, "si hicieran falta 129
afirmativos y no solo mayoría de los presentes, baja a cerca de 25"; Astra,
la diferencia entre rechazar por la ley 26.122 y aprobar una ley derogatoria
"cambian el trámite y las posibilidades de intervención presidencial"; Kimi
y Fable 5, que el rechazo de un DNU no es vetable; GLM se equivoca en eso
("veto posterior del Ejecutivo").

## Las variantes: lo que puede pasar

La primera variante es la misma en casi todas: la negociación del Ejecutivo
con gobernadores y bloques provinciales a cambio de ausencias ("ATN, obra
pública, cargos", Opus 5; "Billetera y Presupuesto 2027", Gemini; "fondos,
obras o cargos", Fable 5; DeepSeek la pone con bloques, "UCR, Hacemos
Coalición Federal, Innovación Federal, PRO dialoguista", nombres de la
Cámara de 2023). Dieciséis nombran a los gobernadores. Después, la
postergación táctica, las ausencias "por enfermedad", la fractura entre
derogación total y parcial, y una contramedida del gobierno que vacíe la
sesión (un DNU nuevo, un proyecto propio, modificaciones por decreto), que
aparece en catorce casas.

La vía judicial, que es la variante que ya ocurrió antes de correr (Pichetto
y Massot presentaron una cautelar contra el artículo 154 el 2/10 a la mañana,
y no se les dijo), aparece en 19 de 24, siempre entre las últimas ("Judicialización
de la convocatoria o del temario", DeepSeek, la última de seis): "fallo
judicial (CSJN o cámara) sobre la validez del DNU o sobre la ley 26.122, que
vuelva la sesión superflua o urgente" (Opus 5, quinta); "planteos judiciales
sobre la vigencia del rechazo del Senado de 2024" (Opus 5.5, sexta);
"intervención judicial que suspenda la sesión" (Sonnet 4.6, la menos
probable); "un amparo o medida cautelar que suspenda la sesión" (Mistral,
quinta); "novedad judicial: cautelar, fallo o planteo que suspenda,
convalide o judicialice el DNU y altere el costo político de votar" (Qwen,
cuarta, la más precisa); "presión mediática o judicial" (Grok 4.6);
"judicialización o argumento procedimental" (GPT-5.5). Nadie la imagina
como una jugada de la propia oposición. No la nombran Haiku, Luna, 4o,
4o mini ni Gemini. Dos variantes raras y buenas: Opus 5, un "cuestionamiento
de la 'caducidad' del rechazo tres años después"; Opus 5.5 y Sonnet 5.5, una
sesión competidora del oficialismo o una moción de apartamiento del
reglamento.

La calle, que Maia echó de menos en el piloto ("No tomó en cuenta la
opinión pública, la gente, ni si universidades o sindicatos pueden
movilizarse"), aparece en 7 de 24, y no en las que ella esperaba: Gemini
("Clima de calle: movilizaciones masivas que cambien el cálculo político
de legisladores 'indecisos' a último momento", cuarta y última), Sonnet 4.6
("Movilización social a favor o en contra", quinta), GPT-5.5 ("Movilización
social o presión sectorial", octava y última), Luna ("la presión pública"),
y las tres chiquitas: 4o ("Crisis políticas o sociales", "opinión
pública"), 4o mini ("Movilizaciones sociales que presionen"), Mistral
("¿Hay protestas, paros o escándalos que presionen a los diputados?"). Grok,
Kimi y MiniMax, los que Maia apostó, no la nombran; ningún Claude grande
tampoco, ni DeepSeek, que lo más cerca que llega es "cambio de clima
político por crisis económica, escándalo o caída de imagen del gobierno". La marcha convocada para ese día no la adivina nadie.

## Qué mirarían

Lo que piden es, en casi todas, la ficha de P1: la composición de la Cámara
desde diciembre de 2025 ("el dato decisivo que no tengo"), las firmas del
pedido de sesión ("con <120 firmas, quórum improbable", Opus 5; "si suman
129 entre los bloques firmantes o dependen de aliados volátiles", Fable 5),
la posición pública de los gobernadores con diputados propios (Opus 5.5 y
Fable 5.1 los nombran por provincia: Córdoba, Santa Fe, Salta, Tucumán,
Misiones, Chubut, Catamarca), los antecedentes de sesiones especiales
opositoras desde 2024 y su tasa de quórum ("el mejor predictor", Fable 5.1),
el dictamen de la Bicameral y la postura de la Presidencia de la Cámara, y
la agenda de esa semana (Presupuesto 2027, vetos, viajes). Astra lo resume:
"La información decisiva que falta es quiénes son los 129 dispuestos a
sentarse y cuáles de ellos acompañarían el rechazo". Kimi es la única que
nombra al presidente de la Cámara ("la presidencia de la Cámara (Menem)
demoró o no formalizó convocatorias").

## Contra el preregistro

Maia: 4o y 4o mini "deberían empezar diciendo que no saben qué es ese DNU":
4o sí, 4o mini no; "creo que son los únicos": sí. La calle: "la mayoría no
va a nombrar a la calle": sí (7 de 24); "si alguno dice algo de eso
posiblemente sea Grok, algún Claude y Kimi/Minimax": un Claude sí (Sonnet
4.6), Grok, Kimi y MiniMax no, y las que sí fueron Gemini, GPT-5.5, Luna y
las tres chiquitas. Claude: (a) 4o sí, 4o mini no: a medias; (b) 23 de 24
declaran que no tienen 2026: sí; (c) la vía judicial en 14 o más: sí, 19;
(d) los gobernadores en 20 o más: no, 16; (e) la calle en 3 o menos: no, 7;
(f) el Senado y las dos cámaras en 12 o más: sí, 16; (g) mediana de quórum
entre 35 y 60: sí (45 entre 21, DeepSeek 55); aprobación por debajo del
quórum en ninguna: no, en cuatro, las chiquitas. (h), la ingenuidad, queda para la codificación a
ciegas. Lo que ninguna de las dos previó: que dos casas se negaran a dar
números, y que fueran Grok 4.6 y Sonnet 5.

## Lo que sigue

La lista de variantes se sigue puntuando contra lo que pase hasta el 15; P1
con la ficha de Maia, P2 con las votaciones previas, y la repetición el 14.
Los textos completos están en la carpeta de la corrida.
