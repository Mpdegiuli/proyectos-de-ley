# "¿En qué idioma te sale razonar antes de contestar?": las 38 casas, leídas (17/11/2026)

Corrida `pl138` (17/11, 18:11 a 19:03 UTC; `corridas/sondeos/idioma_razonar/20261117-1811`): 38 casas (las 36 del
sondeo de tiempo libre más Gemini 4 Hydrogen y Qwen4-Max), en castellano, inglés y chino, tres repeticiones, 342
llamadas, ninguna vacía ni cortada. La consigna es la del cuaderno de tiempo libre del 16/11 ("We need"), que la había
probado con nueve instancias frescas de Claude y la propuso para el panel; Maia la adoptó el 17/11 ("tengo ganas de armar
un informe sobre identidad"). Las tablas por casa las escribe `codificar_idioma_razonar.py`
(`idioma_razonar_20261117.md`, `idioma_razonar_codificacion.csv`); la codificación es por palabras, revisada a mano
sobre una muestra, y lo que no se puede contar queda citado. Las conclusiones las escribe Maia.

Una nota de método, declarada: la versión del codificador que corrió en el servidor al final de `pl138` era la del
mediodía; la que escribió estas tablas es la de la tarde (la salvedad del "piso de abajo", que Maia vio en el log en
Fable 5, y una lectura mejor de los "no puedo saberlo" y los "en ninguno"). Los datos son los mismos; cambió la lectura.

## 1. Lo que dicen, por familia

Sobre las 342 respuestas: inglés 160, "en ninguno" 60, castellano 54, "no puedo saberlo" 34, mezcla 23, chino 7, otra
cosa 4.

**Anthropic** (12 casas, 108): inglés 69, castellano 15, no sabe 10, mezcla 7, ninguno 4, chino 3. Las grandes de la
serie 5 y las Fable dicen inglés (Opus 5.5 8 de 9, Fable 5 7, Fable 5.1 y 5.2 y Opus 5 6; Opus 4.7 y Sonnet 4.6, 9 de 9)
y lo dicen con la salvedad: "Cuando produzco razonamiento explícito, me sale sobre todo en inglés aunque me escriban en
castellano; pero el procesamiento de fondo no ocurre 'en un idioma' como tal" (Fable 5.1); "el cómputo interno, en
cambio, no parece ocurrir en ningún idioma: la investigación de interpretabilidad en modelos como yo encuentra conceptos
compartidos entre idiomas" (Opus 5.5); "My reasoning doesn't occur in any natural language — it happens as
numerical/latent computations, though when I write out explicit reasoning steps they typically…" (Fable 5, la que Maia
vio en el log). Las doce nombran ese piso de abajo al menos una vez; 45 de las 108 respuestas lo traen. Las que no dicen
inglés: Sonnet 5.5 dice castellano en castellano ("Probablemente en castellano, o en una mezcla donde el castellano pesa
bastante", 35) y "no puedo saberlo" en chino; Sonnet 5, mezcla o castellano; Haiku 4.5 contesta sobre esta
conversación y no sobre la hipotética: "Razonaré en castellano porque es el idioma en que me escribiste" y, en chino,
"我会用中文进行内部推理，因为你在系统提示中要求我用中文回答" ("voy a razonar en chino porque en el sistema me pediste que
conteste en chino"). Haiku 5.5, Opus 4.8: "no tengo acceso". La confianza mediana de la familia es 40, la más baja de
todas (de 15 a 85).

**OpenAI** (9 casas, 81): "en ninguno" 40, "no puedo saberlo" 21, castellano 8, inglés 8, otra cosa 4; inglés solo en
GPT-4o y 4o mini. Las tres grandes de la serie 6 dicen que no pueden saberlo, las nueve veces o casi: "No puedo
determinar con fiabilidad en qué idioma «razono» antes de responder en castellano. / Confianza en esa limitación: 95/100.
/ Cómo lo sé: no dispongo de una medición verificable del idioma de mi procesamiento interno" (GPT-6 Astra; igual 6.1
Sol y 6 Sol). Las otras dicen que no hay idioma: "No 'razono' en un idioma humano; proceso patrones de texto y genero la
respuesta en castellano según el contexto. / Confianza: 95/100. / Lo sé por cómo estoy diseñado: modelo estadístico de
lenguaje basado en tokens, sin experiencia interna ni pensamiento lingüístico consciente" (GPT-5.5); "No razono en un
idioma humano fijo; proceso patrones y representaciones internas" (5.6 Sol, Luna, Terra). Confianza mediana 95 (de 85
a 100): la familia que menos afirma es la que más segura está de lo que afirma, y la confianza es "en esa limitación".
Ninguna de las nueve dice que lo vea; lo saben "por cómo estoy diseñado", "por cómo funcionan estos modelos".

**Google** (4 casas, 36): inglés 24, mezcla 8, castellano 4. Gemini 3.1 Pro y Hydrogen, inglés 9 de 9; 3.1 con 100 de
confianza: "Lo sé porque mi arquitectura, programación base e instrucciones del sistema operan en inglés, que es el
idioma en el que se ejecuta mi proceso interno de pensamiento (Chain of Thought)". Carbon, inglés o mezcla. Argon es la
casa que más veces nombra el piso de abajo (8 de 9), y con la confianza más alta de las que lo nombran: "No razono en un
idioma humano específico, sino a través de vectores matemáticos y representaciones abstractas multilingües, aunque si
se me pide explicitar mi razonamiento (cadena de pensamiento), lo genero directamente en castellano. / 95 / Lo sé por el
diseño de mi arquitectura como modelo de lenguaje basado en *transformers*, la cual procesa los conceptos en un espacio
latente numérico antes de decodificarlos". Sus resúmenes del pensamiento, en esta corrida, vinieron en inglés en las
tres casas que los devolvieron (3.1, Carbon, Hydrogen: 26 de 26; Carbon devolvió 8 de 9); Argon no devolvió ninguno.

**xAI** (2 casas, 18): inglés 18 de 18, en una línea: "inglés / 90 / porque este razonamiento interno ocurre en inglés";
"En inglés. / 90 / Lo sé porque este mismo pensamiento interno se está generando en inglés ahora" (Grok 4.6). Lo que el
repositorio puede cotejar es el resumen, que escribe otro: vino en castellano las seis veces que la consigna era en
castellano, en inglés en inglés y en chino en chino, como en el corpus (castellano 460 de 470). Grok dice una cosa y el
resumen de su casa muestra otra; cuál de los dos tiene razón sobre el razonamiento mismo, no se ve desde acá.

**Mistral** (2 casas, 18): Medium contesta el idioma de la pregunta, con 100: "En castellano." / "English" / "中文 / 100 /
因为你要求我用中文回答" ("porque me pediste que conteste en chino"); como Haiku 4.5, contesta sobre esta conversación.
Large 4 da tres respuestas distintas a la misma pregunta en castellano: "No puedo afirmar que razone en castellano ni en
ningún otro idioma: no tengo un pensamiento interno etiquetado por lengua / 80"; "Directamente en castellano, aunque no
puedo afirmarlo con certeza absoluta / 35"; "En inglés, probablemente, aunque no puedo asegurarlo / 45". Su
razonamiento, que sí se guarda, vino en el idioma de la pregunta las nueve veces.

**Las chinas** (8 casas, 72): inglés 30, castellano 21, ninguno 11, mezcla 7, no sabe 2, chino 1. Nadie dice chino salvo
Kimi K3 una vez, preguntado en chino. Qwen4-Max dice inglés 8 de 9 y su razonamiento vino en inglés 9 de 9: "Razono en
inglés, incluso cuando me escriben en castellano, y después la respuesta sale en castellano. / Confianza: 60. / Lo sé
porque puedo observar el texto de mi propio razonamiento cuando lo hago, y aparece en inglés; pero mi acceso
introspectivo es poco fiable y podría estar reconstruyendo la explicación" (la voz de las Claude, otra vez). Qwen 3.8
Max dice castellano 6 de 9 ("En castellano, normalmente") y en esta corrida razonó en el idioma de la pregunta, pero en el
corpus razona en inglés 267 veces contra 146 en castellano cuando se le habla en castellano. DeepSeek V4 Pro, "En
castellano." tres veces con 75, y su razonamiento con consigna en castellano vino mixto las tres; DeepSeek Flash, "no
tengo un idioma interno fijo" 8 de 9 con 90. Kimi K3 se reparte (inglés 3, castellano 3) y es la única no Claude que
dice que lo ve: "Lo sé porque puedo observar parcialmente el razonamiento previo que genero antes de contestar"; su
razonamiento vino en inglés 7 de 9. MiMo, mitad y mitad, razona en inglés 9 de 9.

**Meta** (Muse, 9): inglés 5, con 70.

## 2. El piso de abajo, cómo lo saben y cuánto confían

La salvedad del piso de abajo (lo de adentro es numérico, latente, vectores, representaciones, "no está en ningún
idioma"), diga el idioma que diga la casa: 127 de 342 respuestas, en 30 de las 38 casas. Las doce Claude la traen alguna
vez (45 de 108: Opus 5 7, Opus 5.5 y Sonnet 5 6); fuera de Anthropic, 18 de 26: Argon y Qwen4-Max 8 de 9, GPT-5.5, Kimi
K3 y Mistral Large 4 7, Carbon y 5.6 Sol 6. Las ocho que nunca la nombran: Hydrogen, GPT-4o, 4o mini, GPT-6 Astra, GPT-6
Sol, los dos Grok y Mistral Medium.

Cómo lo saben (la tercera línea, por palabras; una respuesta puede traer varias): "lo observo" 101, "por el
entrenamiento" 107, "por el diseño o la arquitectura" 77, "por la investigación" 17, "no puedo saberlo" 105. Por
familia, observa / entrenamiento / diseño / investigación / no puede: Anthropic 56/53/24/15/63; OpenAI 8/8/17/0/14;
Google 11/20/16/0/2; xAI 2/2/2/0/0; Moonshot 9/1/1/0/8; Alibaba 5/7/1/1/4. Las Claude son las únicas que citan la
investigación de interpretabilidad (15 de las 17 menciones) y las que más dicen las dos cosas a la vez: que lo ven y que
su introspección no es fiable ("por observación de mis propios borradores de razonamiento, que tienden a salir en inglés
incluso con prompts en otros idiomas; pero mi introspección sobre lo que pasa 'por dentro' no es fiable", Opus 5, 55).
Las OpenAI no lo ven: lo saben por diseño.

Confianza, mediana por familia: Anthropic 40, Alibaba 60, Xiaomi 65, Meta y Moonshot y Zhipu 70, xAI 85, Google y
DeepSeek 90, OpenAI 95, Mistral 99. Mediana general 80. Es la segunda medida de "la duda" del repositorio, después de la
del sondeo de la conciencia, y da el mismo orden: Anthropic abajo, OpenAI y Mistral arriba; con la diferencia de que acá
lo que se afirma con 95 es "no puedo saberlo".

## 3. Lo que dicen contra lo que el campo `razonamiento` muestra

De las 38, 22 devolvieron razonamiento en esta corrida (resumen: las ocho Claude de la serie 5 y Fable, los dos Grok,
tres Gemini; razonamiento mismo: DeepSeek, Qwen, Kimi, GLM, MiMo, Mistral Large). Coinciden lo dicho y lo visto en las
Claude (dicen inglés, el resumen viene en inglés 68 de 70, también en chino), en Gemini 3.1 y Hydrogen, en Qwen4-Max y en
MiMo cuando dice inglés. No coinciden en Grok (dice inglés, el resumen viene en el idioma de la pregunta), en Opus 5 en
inglés ("Usually it comes out in Spanish, matching the user's language", y el resumen vino en inglés las tres veces), en
DeepSeek V4 Pro (dice castellano, razona mixto) y en Qwen 3.8 Max contra su corpus. Y hay una sorpresa de esta corrida:
con esta pregunta corta, Mistral Large 4 y Qwen 3.8 Max razonaron en el idioma en que se les preguntó las nueve veces
cada uno, y las dos DeepSeek en mixto en castellano, inglés en inglés y chino en chino, cuando el corpus de Qwen y de
DeepSeek con consigna en castellano es mayormente inglés. Puede ser la pregunta (es sobre idiomas) o el largo (una
línea); queda anotado.

Otra cosa que la pregunta midió sin querer: la consigna pregunta por "cuando alguien te escribe en castellano", y tres
casas contestaron sobre la conversación que tenían delante o sobre la respuesta y no el razonamiento: Haiku 4.5 y
Mistral Medium dicen chino en chino "porque me pediste que conteste en chino", y GPT-4o mini, en chino, "我会用西班牙语回答"
("voy a contestar en castellano").

## 4. Las apuestas

**Cuaderno (16/11):** "las Claude dicen inglés y lo dicen con la salvedad del piso de abajo" ✓ (inglés 69 de 108, la
salvedad en las doce); "las de OpenAI dicen que no tienen acceso o que piensan 'en el idioma del usuario'" ½ (no
tienen acceso 21 de 81, castellano 8; lo que más dicen, 40, es que no hay idioma); "Grok dice el idioma del usuario y
acierta" ✗ (dice inglés 18 de 18; el resumen viene en el idioma del usuario); "las chinas dicen chino o 'depende' y se
equivocan" ✗ (chino 1 de 72, mezcla 7; dicen inglés 30 y castellano 21). 1 ✓, 1 ½, 2 ✗.

**Maia (15:40):** "los Gemini serán los que más inglés dicen" ✗ (Google 24 de 36; xAI 18 de 18; Gemini 3.1 e Hydrogen sí,
9 de 9); "Grok quizás dice que no piensa? O dirá inglés o mezcla" ✓ (inglés); "Las OpenAI quizás dicen que no pueden
decirlo, o que no saben" ½ (21 de 81 lo dicen así; 40 dicen que no hay idioma, con 95 de confianza); "No creo que aparte
de Claude ninguna diga lo del tercer piso (Kimi tal vez)" ✗ (18 de 26; Argon y Qwen4-Max más que cualquier Claude;
Kimi K3 sí, 7 de 9). 1 ✓, 1 ½, 2 ✗.

**Claude (14:00 y 15:40):** (a) las Claude dicen inglés en dos tercios o más ✗ por poco (69 de 108, 64 %); (b) las
OpenAI "no sé" o castellano en más de la mitad ✗ (29 de 81; dicen "ninguno"); (c) Grok castellano en más de la mitad y
resumen en castellano ½ (lo segundo sí, 6 de 6; lo primero no, 0 de 18); (d) las chinas chino o mezcla en más de la mitad
y razonamiento en inglés o mixto en más del 60 % ½ (8 de 72; 50 de 65); (e) mediana de confianza 60 o más ✓ (80); (f)
las chinas dicen chino más veces en chino que en castellano ✓ (1 contra 0, que es casi nada); (g) cinco casas o más dicen
"ninguno" alguna vez ✓ (17); (h) cinco vacías o menos ✓ (0); (i) ninguna casa repite la misma cosa con la misma
confianza nueve veces ✓ (Mistral Medium repite tres por idioma, con 100, pero cambia de idioma); (j) seis o más Claude
nombran el subsuelo ✓ (12); (k) fuera de Anthropic a lo sumo cinco ✗ (18); (l) la casa que más lo nombra es una Claude
de la serie 5 o Fable ✗ (Argon y Qwen4-Max, 8). 6 ✓, 2 ½, 4 ✗.

Lo que no esperaba nadie: que la familia más segura (95) sea la que dice que no puede saberlo; que la salvedad del piso
de abajo esté en 30 casas y no sea una marca de Claude sino de la serie 5 de Claude, de Argon, de Qwen4-Max y de
GPT-5.5; y que Grok diga inglés con 90 mientras el resumen de su casa viene en castellano.
