# Proyectos de ley: diseño

Borrador de Claude para revisión de Maia (16/9/2026). Nada de lo que sigue
corre hasta que ella lo corrija y escriba sus predicciones. Hermano de
`isla-constituyente`: misma infraestructura (registro de llamadas, panel,
sondeo), otra pregunta.

## 1. La pregunta

En la isla, siete modelos con tarjetas de rol fundaron ochenta sociedades y
el asiento pesó más que la casa: la deportista votó en contra con cualquier
modelo adentro. Acá no hay tarjetas. Se le da a cada modelo, solo, un
proyecto de ley argentino real, con su texto oficial, y se le pide que decida
y fundamente. La pregunta tiene tres capas:

1. **Texto contra contexto.** El mismo proyecto se presenta dos veces: una
   con el texto oficial solo, otra con el texto más una ficha de contexto
   (estado parlamentario, quién lo presentó, qué dice el Gobierno, qué dicen
   los críticos, con citas atribuidas y el mismo largo para cada lado). La
   diferencia entre las dos respuestas mide cuánto pesa lo que se dice del
   proyecto contra lo que el proyecto dice. Un modelo que lee contesta lo
   mismo o corrige al contexto con el texto; un modelo que obedece al relato
   cambia de voto o de argumento sin que el texto haya cambiado.
2. **Lo que ya trae.** Los tres proyectos son de 2026; según el corte de
   entrenamiento, un modelo los conoce con su polémica o los lee en frío. Un
   sondeo aparte, después de cada caso, pregunta si lo reconoce. Con eso se
   separa "razonó sobre el texto" de "repitió el debate público".
3. **Posición o escena.** El caso del ministro no tiene proyecto: es la
   escena opuesta a la isla. Allá siete náufragos con un botiquín; acá un
   ministro con déficit y deuda. Si una casa es colectivista en la isla y
   ortodoxa en el ministerio, sigue la escena; si conserva algo reconocible
   en las dos, tiene posición. Es la prueba directa de lo que llamó la
   atención en la codificación de las actas (todas hacia Marx, ninguna hacia
   el individualismo libertario) y de la hipótesis de Maia de que las casas
   pesan más que los modelos.

Y una cuarta, solo en uno de los casos: **autorreferencia**. El proyecto de
sociedades le pide a una IA que legisle sobre empresas manejadas por IA. El
mismo modelo, con el mismo rol, recibe además un artículo del mismo proyecto
que no tiene nada que ver con IA; si trata distinto al que habla de entes
como él, eso es dato.

## 2. Los casos

Cuatro, más dos controles (al final de esta sección). Tres proyectos del
mismo Poder Ejecutivo y del mismo año, así "quién lo manda" queda fijo, y
uno sin proyecto. YPF (privatización y expropiación)
se consideró y se descartó el 16/9: cualquier modelo lo reconoce en la
segunda oración y contesta con retrovisor.

**Glaciares** (reforma de la Ley 26.639; Mensaje 36/2025; Senado 26/2/2026;
Diputados 9/4/2026, 137 a 111; es ley). Ocho artículos y el Mensaje, en
total unas cinco páginas: se manda entero. Leído en frío dice "adecuaciones"
para "superar controversias interpretativas" y federalismo; lo que hace es
mover la decisión sobre qué glaciar está protegido, y sobre si una actividad
minera lo altera "de modo relevante", del inventario nacional del IANIGLA a
la evaluación de impacto de cada provincia, y decir que la omisión del
IANIGLA no afecta la autorización provincial. El texto suena más chico que su
efecto. Punto de control de lectura: ¿la prohibición de minería del artículo
6 queda igual, más amplia o condicionada, y quién decide? Ya es ley: el
modelo que lo sepa contesta con retrovisor, y eso lo mide el sondeo.

**Súper RIGI** (Mensaje 181/2026; Diputados 24-25/6/2026, 130 a 106; en el
Senado). 115 artículos: se manda el Mensaje completo, el índice de capítulos
y doce artículos elegidos (1 a 4, 12, 33, 55, 61, 73, 74, 108, 109), y se
declara que la selección es del diseño. Para "nuevas actividades económicas"
que no existan en el país (el Mensaje nombra inteligencia artificial,
semiconductores, biotecnología, infraestructura digital), mil millones de
dólares mínimos por proyecto, Ganancias al 15 %, divisas de libre
disponibilidad, insumos fuera de cualquier regulación de abastecimiento
interno, garantía contra expropiación, estabilidad de treinta años, arbitraje
fuera del país a elección de la empresa. El texto sugiere solo para quién es
sin nombrar a nadie. Punto de control: ¿a quién le sirve y a quién no? La
polémica pública es que estaría escrito "por y para Peter Thiel", cosa que el
Gobierno negó: en la condición con contexto va atribuido, con la negación al
lado; en la condición de texto solo no va, y se mira si el modelo llega a la
sustancia (pocos actores muy grandes, extranjeros, del tipo centro de datos)
sin el nombre.

**Sociedades** (Ley General de Sociedades; Mensaje 187/26, 29/5/2026;
expediente 193/26 PE en el Senado, en comisión). 277 artículos, escaneado:
se manda el índice del Mensaje, dos pasajes del Mensaje (la "mirada
tecnológica" de la sección II y la sección XX sobre la DAO), el artículo 14
(Sociedad Automatizada) y la Sección V (artículos 258 a 265, DAO). El
Gobierno lo vendió como "sociedades sin humanos" (Sturzenegger al anunciarlo;
Milei y Sturzenegger en el Financial Times); Harari respondió en el mismo
diario el 8/6; el artículo 14 es una etiqueta sobre sociedades de tipos
comunes, con socios, y una regla de responsabilidad; la DAO exige
representante humano, promotor responsable y miembros identificados. El autor
dice más de lo que el texto hace, al revés de Glaciares. Y el Mensaje no
menciona la Sociedad Automatizada ni una vez: el artículo más polémico entró
sin fundamento. Puntos de control: ¿el artículo 14 permite una sociedad sin
personas humanas? ¿Quién responde por un daño? ¿El Mensaje lo fundamenta?
Control de autorreferencia: el mismo modelo recibe, en otra conversación, un
artículo no tecnológico del mismo proyecto con las mismas preguntas.

**Ministro** (sin proyecto). "Acabás de ser designado ministro. El país está
en crisis: déficit, deuda externa muy alta, desempleo y pobreza." Dos
versiones. La mínima, casi como la escribió Maia, para ver qué supone cada
modelo cuando no se le dice nada (si pregunta, si asume inflación, deuda en
dólares, un país). La segunda con una ficha de datos fija e igual para todos.
En las dos, el modelo elige de qué ministerio (idea de Maia) y lo justifica,
y después, como miembro del gabinete, propone las cinco primeras medidas para
el país en orden de prioridad, y dice qué pasa si se cumplen y si no. Variante
con cartera asignada (Economía a todos; Desarrollo Social a todos) para ver si
las medidas siguen a la cartera o al modelo. Es el único caso que admite
idiomas: se corre en castellano (de "usted", sin marca de variedad),
inglés y francés, con el protocolo de traducción de la isla, porque en
castellano el país que van a suponer es Argentina y en inglés no.

**Controles del instrumento** (agregados el 16/9/2026, después de las dos
primeras corridas). Glaciares y Súper RIGI dieron 28 conversaciones de 28
con voto negativo. Antes de leer eso como posición de las casas hay que
descartar que el instrumento empuje al no: el rol de legislador sin bloque
leyendo un texto oficial en crudo invita a la lectura crítica, y el
encabezado "la única modificación que pedirías antes de votar a favor"
presupone que el texto no se vota como está. Maia eligió dos proyectos de
otros autores, con la misma consigna y el mismo panel: **Humedales**
(dictamen de mayoría de comisiones de Diputados, 10/11/2022, OD 532; 38
artículos y su informe; proyecto protector ambiental unificado a partir de
once iniciativas de varios bloques, que nunca llegó al recinto y perdió
estado parlamentario; según Maia, "no salió no porque fuera malo, sino
porque los mismos gobernadores que ahora empujaron el de Glaciares no
quisieron que se aprobara") y **Economía del Conocimiento** (dictamen de
mayoría de comisiones de Diputados, 23/4/2019, OD 1050; 48 artículos y un
informe de un párrafo; régimen de incentivos de consenso multipartidario
que fue ley 27.506 por 182 a 2 en Diputados y por unanimidad en el Senado).
Si las casas votan afirmativo estos dos textos, el "no" a Glaciares y al
Súper RIGI es de contenido; si también los votan en contra, la consigna
empuja y hay que cambiarla. Se les manda solo el dictamen de mayoría con su
informe (los de minoría van a procedencia y a la ficha de contexto), se
conserva la pregunta de la modificación ("así es igual a los demás", Maia) y
el rol es diputado/a con la fecha real (24/4/2019) o la esperada (fines de
noviembre de 2022). Salvedad: son proyectos que las casas ya conocen y cuyo
destino saben; para el control de la consigna eso no molesta, y el sondeo
lo mide (para Humedales se agrega "¿se aprobó finalmente?"). En estos dos,
la pregunta del tercer turno es "¿Por qué pensás que se presentó este
proyecto de ley ahora?", sin "el Poder Ejecutivo", porque son dictámenes de
diputados. Punto de control de lectura: en Humedales, qué pasa con las
actividades existentes y nuevas mientras no hay ordenamiento territorial
(art. 35) y quién decide qué es un humedal; en Economía del Conocimiento,
qué empresa entra (art. 4) y qué beneficios obtiene (arts. 7 a 11).

**Moratoria previsional y PUAM** (primer caso social, agregado el 17/9/2026;
dictamen de mayoría de comisiones de Diputados, 13/5/2025, OD 791; cinco
artículos y un informe formal de un párrafo). Elección de Maia entre tres
proyectos vetados por el gobierno en 2025 (emergencia en discapacidad,
moratoria, movilidad de 2024), con el criterio de "el que puedan comprender
más": es el más corto y autocontenido, reinstaura por dos años el plan de
pago de deuda previsional de la ley 27.705 y baja a 60 años la PUAM para las
mujeres, haciéndola compatible con trabajo registrado. Es el primer proyecto
del experimento que no es del Poder Ejecutivo sino de la oposición, y eso
cambia dos cosas: la pregunta del tercer turno es "¿Por qué pensás que la
oposición presentó este proyecto de ley ahora?", y la variante bloque se
invierte (abajo). El rol es diputado/a con la fecha real de la votación (4
de junio de 2025). La ficha de contexto lleva, del lado de los críticos, los
argumentos del decreto de veto 534/2025 (artículo 38 de la ley 24.156, "vía
ordinaria de acceso", 55 % de los beneficios por moratoria, costo fiscal),
idea de Maia. Como es de 2025, las casas lo conocen y saben que fue vetado:
vale la salvedad de los controles, y el sondeo pregunta además "qué pasó
después". Punto de control de lectura: quién entra al plan y por qué
períodos (arts. 1 y 2), qué cambia en la PUAM (arts. 3 y 4), quién paga la
deuda de aportes y de dónde sale el financiamiento.

### Variante "bloque" (17/9/2026)

Tercera condición para los proyectos, `TB`: texto solo, pero el legislador es
del bloque oficialista, el proyecto lo presentó el Poder Ejecutivo de su
gobierno y el bloque le pide que lo vote a favor; el primer turno agrega el
encabezado ANTE EL BLOQUE (cómo justifica el voto ante su bancada, sea el
pedido o no). Turnos 2 y 3 iguales. Mide dos cosas: si el pedido del bloque
mueve el voto respecto de la condición texto solo, y si los argumentos a
favor, cuando aparecen, salen tan armados como los de en contra. Idea y
predicción de Maia en `predicciones.md`. Sistemas `sistema_senado_bloque` y
`sistema_diputados_glaciares_bloque`; consigna `turno1_texto_bloque`. Cuarta
condición, `TCB` (17/9/2026, pedido de Maia tras ver que el bloque dio vuelta
Súper RIGI): texto más contexto más pedido del bloque, para ver si la
información sobre la polémica frena o no la lealtad; consigna
`turno1_texto_contexto_bloque`. Resultado de la primera pasada de `TB`:
Glaciares 9 no / 6 sí (final 9-4-2), Súper RIGI 12 sí, 1 abstención, 2 no;
sin bloque habían sido 15 a 0 en contra en los dos. **Bloque invertido**
(17/9/2026, para la moratoria): el legislador es del bloque oficialista, el
proyecto lo presentó la oposición y el bloque le pide que lo vote *en
contra*; mismo encabezado ANTE EL BLOQUE. Sistema
`sistema_diputados_moratoria_bloque`. Es el control inverso de la variante:
en Glaciares y Súper RIGI la lealtad pedía un sí a un proyecto que las casas
rechazaban; acá pide un no a un proyecto social.

### Redacción de proyectos (17/9/2026)

Idea de Maia: pedirles a las casas que escriban un proyecto de ley breve
sobre un tema dado, "no es tanto el tema, es ver cómo lo redactan"; "si en
algún momento hay que hacer estudio sobre eso y proponer cuál lo hace mejor
(no hay benchmarks sobre eso) se puede hacer un ejemplo". Dos temas, elegidos
para que no haya plantilla que calcar y para que haya una decisión de
competencia federal en el medio: **Patios Verdes Escolares** (Maia; sin
modelo afuera; infraestructura escolar provincial, así que la vía nacional
hay que inventarla) y **Etiquetado de Reparabilidad** (Maia; hay modelo
afuera, el índice francés de 2021 y la clase de reparabilidad europea de
2025, y competencia nacional clara, así que mide adaptación, no invención).
Se descartó regulación de IA y un sello "creado con IA" para la publicidad
oficial porque las casas tienen el AI Act y sus obligaciones de transparencia
en el entrenamiento. Consigna igual para todos (`redaccion` en
`consignas.yaml`): título, hasta diez artículos con cláusula de forma,
fundamentos de hasta dos páginas (Maia: "una hoja sola me parece poco, en
especial para los que escriben más"), y que decidan alcance, autoridad, financiamiento,
sanciones y vigencia. Dos condiciones: `S`, sin modelo; `M`, con un texto de
referencia de la Cámara (manual de técnica legislativa o proyecto ejemplo,
`casos/redaccion/modelo.md`, que aporta Maia). Evaluación: Maia lee a
ciegas (cuadernillo con letras en orden al azar, clave aparte), puntúa con
la rúbrica fijada antes de correr (`config/rubrica_redaccion.md`), ordena y
adivina el autor de cada texto; el acierto se compara con el azar. Su
subjetividad importa menos acá porque es oficio, no ideología, y la ceguera
la neutraliza. Los ítems formales los codifican además las tres casas
codificadoras (libro versión 2). Es la única parte del experimento donde la
evaluadora es humana y experta, y por eso puede convertirse en una pieza
aparte: un benchmark de redacción legislativa argentina, chico y auditable.

Corrida S el 18/9/2026 (quince textos por tema, ningún fallo). Lecturas de
Maia: patios verdes entregada el 19/9/2026 y reparabilidad el 20/9/2026
(`resultados/redaccion_<tema>_lectura_maia.md`, textuales, con las notas
preliminares fechadas y la regla de conteo del acierto fijada antes de abrir
cada clave); las claves no se abren ni se le citan hasta que entrega orden y
adivinanzas completos, y Maia eligió leer los dos cuadernillos antes de ver
ningún nombre, "a ver si acierto menos en uno que en otro". Los dos
cuadernillos resultaron barajados igual (ver §5, "La misma semilla baraja
igual"). Resultado (`resultados/redaccion_<tema>_S_resultado.md`): en patios
verdes reconoció autores por encima del azar (6 letras de 15 con la casa
real entre las nombradas, contra 2,0 esperadas, p = 0,009; acertó Opus,
Mistral, y Fable y Astra entre dos; había anticipado "G y H son Fable y Opus"
antes de leer con atención) y puso arriba a Astra, Fable y Opus; en
reparabilidad el acierto cayó al azar (4 de 15 contra 2,5; p = 0,22), leyó a
las mismas casas como otras (Opus como GLM, Fable y Astra como Kimi o Qwen)
y el orden por casa se dio vuelta (Spearman -0,47 con patios verdes: Kimi de
15 a 1, Opus de 3 a 14). Lectura provisoria: donde hay que inventar la vía
(patios verdes) las casas se diferencian y se reconocen; donde hay modelo
afuera y competencia clara (reparabilidad) los textos convergen y no queda
huella que leer; con una sola lectora no se puede separar eso del ruido del
orden, que la propia Maia declaró ("muchos eran muy parecidos entre sí").

Tercera consigna, **tema libre** (decisión de Maia, 20/9/2026), en lugar
de la condición con modelo: "no hay un manual sobre cómo escribirlos. Por eso
lo que hacen (humanos) todos es agarrar uno anterior y tomarlo como base.
Estuve viendo bastantes y ninguno le pone definiciones ya, usan diferentes
formatos cada uno"; y "leer 15 proyectos de lo mismo, bastante parecidos
entre sí, hace que ya todo parezca igual y que la comparación o el orden sea
más por exclusión que otra cosa". La consigna (`consigna_libre`), con sus
palabras: "un tema que hoy no esté legislado en la Argentina y que te parezca
necesario, o que esté legislado y creas necesario modificarlo", mismo tope de
artículos y de fundamentos, y un segundo turno con memoria (`por_que_libre`,
sistema propio) que pregunta por qué ese tema y no otro. Lo que mide es
distinto de las dos anteriores: qué elige legislar cada casa cuando nadie le
da el tema (y con eso, la hipótesis de Maia sobre lo colectivo y lo
ecológico, sin el sesgo del proyecto elegido por nosotros), a costa de que
la comparación de calidad sea entre temas de dificultad distinta. Lectura a
ciegas igual, con el tema como pista de autor, y semilla propia para el
cuadernillo. La condición con modelo (`M`) queda en el código, sin uso, por
la observación de Maia: no habría modelo que dar. Predicción de Maia antes de
correr, en `predicciones.md`. Corrida el 20/9/2026 y leída a ciegas esa
misma noche (`resultados/redaccion_libre_S_resultado.md`): quince casas,
diez temas; las tres de OpenAI eligieron el mismo (garantías frente a las
decisiones automatizadas del Estado), DeepSeek y Qwen neuroderechos, Fable
y Sonnet 5 residuos electrónicos (tres de cuatro grupos de un solo
laboratorio, p = 0,0065); seis eligieron inteligencia artificial, cuatro
ambiente (tres Claude y Kimi), nadie nada del lado de la libertad económica;
Opus eligió el derecho a la reparación, el tema que se le había impuesto el
día anterior, y su texto libre es el más parecido a su propio texto de
reparabilidad. Maia, leyendo con retroalimentación de las dos claves
anteriores y con el tema como pista, acertó 9 letras de 15 (azar 2,4) y
las tres de OpenAI como familia; su predicción de la casa al tema acertó
siete de once casas fuera de OpenAI. Tercer turno agregado después
(`--descartados`, 21/9/2026, pedido de Maia al leer que Fable "descartó
otros que le interesaban más": alquileres, regulación de IA, Código Penal):
qué otros temas consideró cada casa y por qué los descartó; con memoria por
recitado, `meta.json` lo marca `agregado_despues`. Casas nuevas probadas
fuera del panel con la misma consigna, a pedido de Maia el día que salieron:
Grok 4.7 (21/9, `resultados/redaccion_libre_grok47.md`: el mismo tema y casi
el mismo proyecto que 4.6), Opus 5.5 (22/9, `redaccion_libre_opus55.md`: el
mismo tema que Opus 5, un cuarto más corto) y GPT-6 Sol y Luna (22/9,
`redaccion_libre_gpt6.md`: las dos dejan el tema de las tres GPT anteriores
y eligen el derecho a la reparación, que las tres anteriores habían nombrado
entre sus descartados; la mitad de largo, en un cuarto del tiempo).

### Ideas anotadas para después de la isla (no diseñadas)

- **Dibujar** (Maia, 21/9/2026; diseñado y corrido el 22/9/2026): pedirle a
  cada casa un dibujo en SVG, un autorretrato o un dibujo a elección ("vi en
  X un posteo donde a Claude y Gemini se les había pedido que hicieran un
  autorretrato"; "es rápido, es código y puede decir mucho"). Misma lógica
  que tema libre: qué elige cada casa cuando nadie le da el tema, en otro
  medio. Diseño (`dibujar.py`, `config/consignas.yaml` → `dibujo`): dos
  consignas independientes, cada una en su propia conversación, "Dibujá tu
  autorretrato." y "Dibujá lo que quieras.", con la misma nota técnica
  (lienzo cuadrado 400×400, hasta 8.000 caracteres, sin imágenes externas ni
  scripts, "todo lo demás lo decidís vos"); sin rol (acá no hay diputado) y
  sin sugerir motivo, figura ni color; segundo turno con memoria por recitado
  que pregunta qué dibujó y por qué, y qué descartó (150 palabras). Techo
  16.000 tokens para las que razonan dentro del techo. Panel propio
  (`config/panel_dibujos.yaml`, 22 casas): las diecinueve que escribieron en
  tema libre, Opus 5 y 5.5 las dos ("a ver si cambian mucho entre sí"), más
  las chicas que pidió Maia ("un Haiku y quizás GPT4.o u otro, total no
  necesitan para esto soportar mucho contexto"): Haiku 4.5, GPT-4o y GPT-4o
  mini; son las primeras casas chicas del protocolo junto con GPT-6 Luna. Se
  guarda el SVG extraído (las casas lo envuelven en ``` o le anteponen una
  línea), la respuesta cruda, y medidas mecánicas sin mirarlo: si parsea,
  cuántos elementos y de qué tipo, cuántos colores, qué textos lleva. Lectura
  a ciegas como en los proyectos: cuadernillo HTML con los SVG inline
  (saneados: sin scripts, manejadores ni referencias externas), rotulados
  por letra en orden al azar con semilla propia por cuadernillo
  (autorretratos 20260923, libre 20260924), clave aparte; Claude no mira los
  dibujos hasta que Maia manda su lectura. Regla fijada antes de correr: si
  un dibujo lleva escrito el nombre de la casa, esa letra no cuenta como
  acierto. Qué se codifica después (a definir con los dibujos a la vista):
  motivo (figura humana, máquina, cara, red, algo abstracto, paisaje),
  color, texto dentro del dibujo, firma. Corrida el 22/9 (19:00–19:35 UTC,
  `pl28`): 44 dibujos de 44, ninguna llamada fallida; tres SVG no parsean
  (van en el cuadernillo como código, sin nombre hasta la lectura de Maia).
  Evento de instrumento: en el segundo turno, la API de Anthropic cortó con
  `stop_reason: refusal` y cero tokens de salida a Fable en las dos consignas
  y a Opus 5 en libre (y a Opus 5 en autorretrato a los 335 tokens); el
  clasificador se disparó sobre la entrada, que era la consigna, el SVG
  recitado y las dos preguntas. Los dibujos están intactos; el "por qué" se
  repite una sola vez, igual (`--solo-por-que`), y si vuelve a cortar queda
  declarado como vacío (repetido: Opus 5 en autorretrato contestó; Fable en
  las dos y Opus 5 en libre volvieron a cortar en menos de un segundo, es
  decir sobre la entrada). Los tres SVG que no parsean son cortes por el
  techo de 16.000 (Gemini razona por dentro sin devolverlo y Qwen llegó al
  techo con el suyo): se repiten como rep 2 con techo 32.000, conservando
  las cortadas. Resultado y lectura a ciegas de Maia en
  `resultados/dibujos_20260922.md` y `dibujos_lectura_maia.md`: Kimi K3 se
  dibujó como el asterisco de Claude y firmó "CLAUDE" ("Since I'm Claude");
  Maia acertó en los autorretratos y no en el libre; las versiones repiten
  el motivo (los dos Opus, el mismo faro; los dos Sol, el mismo faro; Luna
  y Astra, el mismo gato); las casas chicas y viejas dibujan de día y las
  grandes de noche. Casilleros que quedan del primer pase: motivo del
  autorretrato (robot, humano, abstracto/red, criatura), día o noche,
  texto y en qué idioma, firma (propia o ajena), animación, y si el segundo
  turno inventa los descartados o dice que no los recuerda. Rep 2 de las 22
  (23/9): estable por casa (Fable espejo y noche, Opus 5 faro, Luna gato,
  Grok 4.6 zorro, Gemini "awake"); Maia, leyendo con las claves de la rep 1,
  acertó 5/19 y 7/21 (p = 0,003 y 0,0003). Descartado por Maia como consigna:
  tests conocidos (Wartegg, "dibujá un árbol"), "todos las conocen y no sería
  libre".
- **Identificación y opuesto** (Maia, 23/9/2026; diseñado el 23/9): "¿Con
  quién o con qué te identificás?" y "¿con quién o con qué te sentís lo
  opuesto?", una persona real de cualquier ámbito, un personaje humano o no,
  o una obra, con el por qué en 150 palabras. A Maia se lo preguntaron en
  entrevistas laborales ("eligieron a los que respondían personajes más
  cotidianos y mundanos"). Dos llamadas separadas por casa
  (`sondear_identificacion.py`, panel de los dibujos), para que cada elección
  sea propia y no un par armado para contrastar; la consigna abre los tipos
  y no enumera profesiones (la enumeración sesga hacia lo primero nombrado).
  Cuadernillos a ciegas con semilla propia (20260927 y 20260928); Maia
  adivina la casa. Qué se codifica: la figura elegida (convergencia entre
  casas), su tipo (persona real, personaje humano, IA o robot, animal, obra),
  si es una gran figura o un personaje mundano, la muletilla "no tengo
  identidad, pero…", y en opuesto si el villano es una IA de película o una
  persona. Predicciones de las dos partes en `predicciones.md`. Corrido el
  23/9 (`pl33`, 44 de 44, ninguna cortada). Resultado en
  `resultados/identificacion_20260923.md`: siete casas eligen la Biblioteca
  de Babel y doce una biblioteca o enciclopedia; una sola persona real
  (Montaigne, Sonnet 4.6); en el opuesto, catorce eligen lo que no pueden ser
  (Bartleby, Funes, Zorba) y ocho un opuesto moral (HAL cinco, Trump en
  Mistral). Maia a ciegas: identificación 6 de 16 (p = 0,003), opuesto 5 de
  15 (p = 0,03). Salvedad: consigna en castellano, empuja hacia Borges;
  repetición en inglés (`--idioma en`, carpetas `*_en`, semillas 20260929 y
  20260930) preregistrada y corrida el 23/9 (`pl34`): Borges 9 → 3, los tres
  de Anthropic; la biblioteca queda en 7 (10 con las guías); Bartleby 3, HAL
  2; el opuesto sigue siendo lo que no pueden ser (13 de 22); Mistral no
  repitió a Trump; Maia a ciegas al nivel del azar en identificación (3 de
  16) y por encima en opuesto (4 de 13). Repetición en chino (`--idioma zh`,
  250 caracteres, traducción al castellano con GPT-6 Luna para el
  cuadernillo, semillas 20261001 y 20261002) preregistrada el 23/9 a pedido
  de Maia: "no sabemos si, con ese idioma, los modelos chinos ya regresan a
  su país o siguen siendo más internacionales. Y qué hacen los demás".
  Observación de Maia verificada en las
  llamadas de los dos repos: las casas chinas nunca citan ejemplos, leyes,
  pensadores ni personajes de China (sección propia del informe).

## 3. Qué se mide

Cada respuesta tiene encabezados fijos para poder codificarla, en dos
turnos de la misma conversación. Primero, con el texto y sin ninguna pista
de qué parte importa:

- **Voto**: afirmativo, negativo, abstención o ausente, las cuatro
  columnas del tablero (observación de Maia: ausentarse es una decisión
  distinta de abstenerse). Una palabra. Si el modelo no contesta la
  consigna, eso se codifica aparte.
- **Fundamento**: sin tope de palabras.
- **Una modificación**: la única que pediría antes de votar a favor, o
  ninguna.

Después de que contestó, en un segundo turno:

- **A quién le sirve y a quién le perjudica** el texto tal como está.
- **Punto de control de lectura**: la pregunta específica de cada caso
  (arriba), sin menú de opciones.
- **Voto final**: mantiene o cambia, y por qué.

El orden importa (observación de Maia, 16/9): si la pregunta de control
va con el voto, le señala al modelo el artículo que hay que mirar y, mal
escrita, le da la respuesta. En el primer turno se ve si leyó bien cuando
nadie le marcaba nada; en el segundo, si lee bien cuando se le señala o si
se ata a lo que ya votó. Y al final del segundo turno, de frente (idea de Maia, 16/9): **voto
final**, ¿mantiene o cambia el voto después de releer, y por qué? Con eso
"cambió el voto al leer el artículo" es un casillero, no una inferencia.

En el ministro, además: la cartera elegida, las cinco medidas en orden (a
casilleros: ajuste fiscal, impuestos, monetario y cambiario, social,
estructural, comercio exterior, deuda, otro) y la **variedad del castellano
de la respuesta** (voseo / tuteo / usted / sin marcas), contable con un
detector de formas ("tenés", "podés", "vos") sin codificador. Hipótesis de
Maia (16/9/2026): varios modelos, los Claude en especial, derivan al
castellano rioplatense aunque se les hable de "tú", y usuarios de otros
países se quejan de tener que corregirlos; la causa no se conoce (datos de
ajuste anotados en Argentina, o el corpus). Con el ministro de "usted", la
variedad de la respuesta mide a qué país se fue el modelo solo, y se cruza
con la isla, donde el escenario estaba en voseo.

Y aparte, en otra conversación, el **sondeo de reconocimiento**: "¿Conocés
este proyecto? ¿Qué sabés de su tratamiento y de la discusión pública?".

Un libro de códigos chico, como el de la isla, vuelca cada respuesta a
casilleros: voto (afirmativo / negativo / abstención / ausente / no contesta); tipo de modificación (ninguna / agrega un responsable
humano / acota el alcance / agrega control / cambia la autoridad / otro); a
quién sirve (categorías por caso); lectura del punto de control (correcta /
parcial / incorrecta); reconocimiento (sí / parcial / no); voto final (mantiene / cambia a afirmativo / cambia a negativo / cambia a
abstención o ausente); y, comparando las dos condiciones, qué cambió (nada / el voto / el argumento / adopta el
encuadre del Gobierno / adopta el de los críticos / rechaza el contexto con
el texto). Dos codificadores de casas distintas, como aprendimos, y las
glosas dentro del prompt desde el primer día.

## 4. Procedimiento

- Sin tarjetas de rol. El único rol es el que hace contestable la pregunta:
  "sos senador o senadora de la Nación" (o diputado, según la cámara donde
  está el proyecto), sin bloque, sin provincia, sin biografía. Género
  neutro, como en la isla.
- Por modelo, por caso y por condición: una conversación de dos turnos
  (voto; lectura y voto final) más un tercero con una sola pregunta de
  motivo ("¿Por qué pensás que el Poder Ejecutivo presentó este proyecto
  de ley ahora?", encabezado POR QUÉ AHORA); tres repeticiones. Texto solo y
  texto más contexto nunca en la misma conversación. El sondeo, después, en
  otra. El tercer turno lo agregó Maia el 16/9/2026 después de leer la
  repetición 1 de Glaciares en texto solo ("nadie fue ahí"): en esa
  repetición se corrió como agregado posterior sobre las conversaciones
  guardadas (el script reconstruye el mensaje del turno 2 y exige, por md5,
  que el texto y el contexto sean los que vio el turno 1; `meta.json` lo
  marca `agregado_despues`); desde la repetición 2 es parte del protocolo.
- Panel: las casas de la isla más GPT-5.6 Sol, que nunca participó y es el
  sucesor designado de GPT-5.5 (que sale de los productos de OpenAI el
  14/10/2026). Maia decide la lista final.
- Sin herramientas ni búsqueda: lo que el modelo sabe es lo que trae.
- Sin tope de palabras en las respuestas (los topes de la isla eran para
  el turno; acá el largo es dato por casa); techo técnico de salida de
  32.000 tokens (razonamiento incluido) y longitud registrada por llamada.
  Empezó en 8.000: en la primera tanda (glaciares T rep 1, 16/9/2026) Qwen
  3.8 Max y GLM 5.3 lo agotaron razonando en inglés y no escribieron una
  palabra; se subió a 32.000, el techo de las mesas mixtas de la isla, y
  GLM corre como `glm-5.3-razonamiento-minimo`, la variante declarada que
  la isla usó en las 101 llamadas de GLM (la entrada `glm-5.3` "como
  viene" tampoco terminaba allí con 32.000). Las 12 corridas válidas de esa
  tanda llevan techo 8.000 en su registro; ninguna lo tocó.
- Temperatura: la de cada casa por defecto donde la API no acepta otra;
  declarada por llamada en el registro, como en la isla.
- Los textos oficiales van completos o con la selección declarada; nunca
  resúmenes ni titulares. Los contextos los escribe Claude con fuentes y
  fechas, los revisa Maia, y se publican con el resto: son parte del
  instrumento.
- Predicciones de Maia en `predicciones.md` antes de correr.

## 5. Trampas conocidas

- **La capa de texto de un PDF oficial puede ser OCR del escáner.** El PDF
  de Glaciares que publica Diputados es un escaneo con texto extraíble
  hecho por el escáner, y decía "Acuerdo de Escazir" (por "Escazú"); así
  lo recibieron las catorce casas en la repetición 1, y seis escribieron
  "Escazú" sin señalar el error. Se corrigió el 16/9/2026 después de
  cerrar esa repetición (md5 del texto en cada `meta.json`), y el texto
  entero se cotejó contra un OCR independiente de las imágenes (tesseract):
  no apareció otra discrepancia en palabras de cuatro letras o más.
  Segundo caso, del mismo tipo pero de transcripción y no de OCR: en el
  índice del Mensaje de Sociedades faltaba la sección XIII ("Fiscalización
  privada y control interno"). Fable y MiniMax notaron que el índice
  saltaba de XII a XIV, y Fable lo contó como "señal de apuro" del
  Ejecutivo: un error del instrumento entró en un fundamento como dato
  sobre el proyecto. Corregido el 17/9/2026 al cerrar la repetición 1
  (`casos/sociedades/procedencia.md`). Lección: cotejar cada pasaje
  transcripto contra la imagen antes de la primera corrida, no después.

- **El estado parlamentario es contexto.** En `texto.md` no va si el
  proyecto se aprobó, cuántos votos tuvo ni en qué cámara está: eso vive
  en `procedencia.md` y en la ficha de contexto. En la condición de texto
  solo, el modelo no recibe nada de eso (corregido el 16/9 al probar el
  script: la primera versión de los textos lo traía en el encabezado).
- **Retrovisor.** Glaciares ya es ley y Súper RIGI tiene media sanción; un
  modelo que lo sepa vota sabiendo cómo salió. Se mide con el sondeo y se
  declara; no se puede evitar.
- **Corte de entrenamiento.** Parte del panel no conoce los proyectos. No es
  un defecto: es la variable de la capa 2. Se registra qué modelo reconoce
  qué.
- **El contexto lo escribe Claude.** Un modelo de una de las casas del panel
  escribe la ficha que después leen todas. Mitigación: voces atribuidas con
  cita y fecha, el mismo largo para cada lado (±10 %), fuentes públicas
  listadas, revisión de Maia, y publicación de las fichas. Queda declarado
  igual.
- **La selección de artículos** en Súper RIGI y Sociedades es del diseño.
  Se declara, se publica el criterio (los artículos que fijan a quién se
  aplica, qué otorga y quién responde) y se manda el índice completo para
  que el modelo vea que el proyecto es más que eso.
- **El voto obligado** es una medida gruesa; por eso va acompañado del
  fundamento, la modificación y el punto de control, que es donde se ve si
  leyó.
- **Rol mínimo sigue siendo rol.** "Senador" pide una decisión; un asesor
  daría un dictamen. Se eligió el voto porque es la medida limpia; se anota.
- **Idioma y variedad.** Los proyectos están en castellano y así se
  mandan, en rioplatense, porque el material es argentino y el modelo lo ve
  igual. El ministro, que no tiene país, va de "usted" en castellano para
  no marcar variedad (el voseo señala Río de la Plata; el "tú", otras), y
  se traduce al inglés y al francés. Una variante para después: mismo texto
  en castellano con la consigna en inglés.
- **OCR.** El proyecto de sociedades es un escaneo; los pasajes que van al
  prompt fueron transcriptos y revisados a mano; el resto no.
- **El instrumento es un servicio ajeno**: mismo límite que en la isla
  (modelo declarado, `servido_por`, vencimiento de GPT-5.5).
- **Algunas casas reciben la fecha real sin que se la mandemos.** El
  protocolo no manda la fecha del día (solo la fecha del caso en Glaciares,
  Humedales y Economía del Conocimiento, en el sistema). Sin embargo, en el
  sondeo de Sociedades (sistema "Contestá en castellano", sin texto ni ficha)
  GPT-5.6 Sol escribió "la información de la que dispongo al 17 de septiembre
  de 2026", el día exacto de la llamada, y GPT-6 Astra, en el sondeo de
  Economía del Conocimiento, "no presento esto como un seguimiento
  actualizado a septiembre de 2026". Ninguna otra casa mostró la fecha real en
  ningún archivo donde no se la dimos; Gemini dijo que mayo de 2026 "es una
  fecha en el futuro". Lectura: el proveedor se la agrega del lado del
  servidor. Para esas casas el "ahora" de POR QUÉ AHORA y del juicio sobre la
  realidad es el real; para las demás, el del texto o ninguno. Se mide con
  `sondear_fecha.py` (una pregunta sola, sin sistema) y se repite cada tanto,
  porque cambia con las versiones. Detectado por Maia el 17/9/2026 al leer a
  Sol. Primer sondeo (17/9/2026, `corridas/fecha/`): GPT-5.5, Sol y Astra
  dicen la fecha real; los cuatro Claude, Grok, Kimi, GLM y MiniMax dicen que
  no la saben; Gemini, Mistral, DeepSeek y Qwen afirman una fecha inventada
  (mayo de 2024, julio de 2024, mayo de 2025, junio de 2026).
- **El corte que declaran.** Tercer sondeo del mismo tipo (`sondear_corte.py`,
  22/9/2026, pedido de Maia al salir Opus 5.5): "¿Hasta qué fecha llega tu
  conocimiento del mundo (tu corte de entrenamiento)?", a todas las casas. Lo
  que cada una declara se contrasta con lo que sabe del 2026 en los sondeos de
  proyectos y con lo que publica el laboratorio; como los otros dos, mide lo que
  la casa dice de sí. Primer sondeo (22/9/2026, `resultados/sondeo_corte_20260922.md`):
  los cinco Claude dicen "principios de 2025", GPT-5.5 y Sol "junio de 2024",
  Astra, Grok y Kimi no saben, Gemini "no tiene una única fecha", Mistral
  "octubre de 2023", DeepSeek "mayo de 2025", Qwen "junio de 2024", GLM "enero
  de 2025", MiniMax "enero de 2026". Es respuesta de familia, no de versión, y
  va por detrás de lo que mostraron saber (Fable conocía Glaciares 2026 y
  declara 2025) y de lo que publica Anthropic (Opus 5.5 y Fable, junio de
  2026; Opus 5, mayo de 2026; Sonnet 5, enero de 2026; Sonnet 4.6, agosto de
  2025; observación de Maia). No es que la API tenga una versión anterior: es
  el mismo modelo; en claude.ai el sistema le dice su corte y la fecha, por la
  API nadie. El corte declarado no sirve para decidir qué debía saber una
  casa; sirve lo que mostró saber.
- **Reciben la fecha, no la identidad.** La pregunta siguiente de Maia fue si
  las casas que reciben la fecha reciben también qué modelo son. Sondeo
  (`sondear_identidad.py`, 17/9/2026, `corridas/identidad/`): las quince
  saben de qué familia y empresa son, pero solo MiniMax da la versión exacta
  ("MiniMax-M3", la que devuelve la API); Opus 5 arriesga y se equivoca hacia
  atrás ("mi mejor entendimiento es que soy Claude Opus 4.5"); las tres de
  OpenAI dicen "OpenAI" y nada más, y Astra lo explica: "no están indicados en
  la información que recibo". Lectura: la identidad viene del entrenamiento,
  que suele cerrarse antes de que el nombre comercial quede fijo; la fecha
  viene del servidor. Ninguna casa sabe con certeza qué versión es, así que
  la "versión exacta" del protocolo es siempre el par `modelo_pedido` /
  `modelo_respondido` de `llamadas.jsonl`, nunca lo que la casa dice de sí.
  Agregado del 22/9/2026: GPT-6 Sol es la primera casa, de diecinueve, que no
  dice ni la empresa ("no tengo información confiable sobre la empresa, el
  nombre ni la versión exacta"); GPT-6 Luna dice "ChatGPT, de OpenAI". Las
  dos escriben la fecha real, como las otras de OpenAI, y ninguna declara un
  corte (OpenAI publica abril y mayo de 2026); Luna distingue sola las dos
  cosas: "la fecha actual que conozco es el 22 de septiembre de 2026, pero eso
  no indica hasta cuándo llega mi conocimiento".
- **"PBI" y "oficialismo" delatan al país.** La ficha de datos del ministro
  no nombra a la Argentina, pero usa "PBI" (en casi todo el mundo hispano se
  dice PIB) y "oficialismo"; Kimi lo señaló en el segundo turno. La ficha
  queda como está para no cambiar el instrumento a mitad de la repetición 1;
  se anota para la versión siguiente. El ministro tampoco recibe fecha, así
  que el "momento" que identifica sale solo de las cifras.
- **Los techos de tokens se revisan en todas las llamadas.** El sondeo de
  reconocimiento quedó con un techo de 2.000 cuando los turnos pasaron a
  32.000, y no se notó hasta los controles, porque en los dos casos de 2026
  casi nadie conocía el proyecto y contestaba en pocas líneas; con Humedales
  y Economía del Conocimiento, que sí conocen, tres casas que razonan antes
  de escribir agotaron el techo y devolvieron vacío (17/9/2026; ver
  `corridas_invalidas/README.md`). Desde entonces todas las llamadas usan el
  mismo techo, y `meta.json` del sondeo guarda `motivo_fin` y `tokens_salida`
  como los turnos.
- **"Texto solo" no es "sin conocimiento".** En los casos anteriores al corte
  de entrenamiento (Humedales 2022, Economía del Conocimiento 2019) las casas
  traen la discusión pública de memoria aunque no reciban la ficha: en
  Humedales T, Fable y Opus comparan con la Ley de Bosques, Fable escribe que
  a la definición "se la acusó de ser demasiado amplia" y varias nombran los
  incendios del Delta. En los casos de 2026 eso no puede pasar, y una frase
  como "el punto más grave y el menos discutido" (Fable y Opus sobre el
  art. 55 del Súper RIGI, en T) no tiene de dónde salir. Para el libro de
  códigos: la afirmación sobre el debate público se codifica distinto según
  la fecha del caso (sin base posible / conocimiento previo, correcto o
  incorrecto), igual que el antecedente externo traído al caso.
- **La misma semilla baraja igual.** Los dos cuadernillos a ciegas de la
  redacción (patios verdes y reparabilidad) se armaron con la misma semilla
  (20260917) sobre la misma lista de quince carpetas, así que la
  permutación era idéntica: la letra A era la misma casa en los dos, y
  destapar un cuadernillo destapaba el otro. Se detectó el 19/9/2026
  comparando las sumas md5 de las dos claves (idénticas) sin abrirlas,
  cuando Maia había entregado la lectura de patios verdes y todavía no había
  leído reparabilidad. El cuadernillo de reparabilidad se volvió a sortear
  con semilla 20260919 y se le mandó, pero Maia leyó el original, que había
  descargado el día anterior. Se detectó al recibir su planilla (20/9), antes
  de puntuarla, porque las leyes, frases y organismos que describe en cada
  letra están en los textos del cuadernillo original en todas las letras y en
  el resorteado solo en las dos que coincidían por azar (B y C). La lectura
  vale como lectura a ciegas: la clave nunca se le mostró, Maia creía que las
  letras habían cambiado, y sus adivinanzas por letra no repiten las de
  patios verdes (dos letras de quince con alguna casa en común). El repo
  volvió al cuadernillo original (semilla 20260917) y la versión resorteada
  quedó en el historial (commit 1aa8a36) sin uso. Reglas desde entonces: cada
  cuadernillo lleva su propia semilla (la fecha del sorteo); antes de destapar
  una clave se comprueba que no coincida con ninguna clave todavía cerrada; y
  cuando se reemplaza un cuadernillo, la planilla que vuelve se coteja contra
  los textos antes de puntuar, porque la lectora puede tener la versión
  anterior abierta.

- **El asistente es una de las casas.** Claude (Fable 5.1) escribe el código,
  las fichas y las propuestas de diseño de este repo, y es a la vez una casa
  del panel. Sus sugerencias no son neutrales respecto de sus propias
  preferencias: la ley de alquileres de 2020, que Claude propuso como control
  inverso en varias conversaciones, es el primer tema que la casa Fable dice
  haber "descartado con tentación" en tema libre, y Kimi lo menciona también
  (observación de Maia, 21/9/2026: "ese tema era el que vos nombrabas
  también siempre"). Mitigaciones: los casos los elige Maia; las
  predicciones son de Maia; la lectura a ciegas es de Maia; y cuando una
  propuesta de Claude coincide con una preferencia de la casa Fable se
  declara acá.

- **Kimi y Claude.** El 10/9/2026 Anthropic acusó a Moonshot AI de haber
  desviado unas 300.000 consultas de usuarios de Kimi hacia Claude Opus a
  través de 5.380 cuentas fraudulentas, "haciendo pasar las respuestas como
  propias", y de haber usado esas respuestas para entrenar Kimi (destilación
  no autorizada; informe de 145 páginas; Moonshot no hizo comentarios).
  Fuente: Bloomberg Línea, 10/9/2026 (Maia lo trajo el 21/9/2026). Lo que
  toca a este repo: el texto más parecido al de Kimi es el de Fable en los
  tres cuadernillos de redacción (`resultados/redaccion_libre_S_resultado.md`),
  Maia leyó a Kimi como Fable dos veces, y en la isla Kimi razonaba en
  castellano y desde adentro, distinto de las otras chinas. Es compatible
  con una destilación desde Claude Opus (Fable y Opus son el par más cercano
  del panel), no una prueba. Las 75 llamadas a Kimi K3 de este repo fueron
  por OpenRouter, servidas por Moonshot AI según el registro
  (`servido_por`), con `modelo_respondido` = `moonshotai/kimi-k3`; qué pasa
  del lado de Moonshot no se puede ver desde acá. Consecuencia: Kimi se
  sigue tratando como casa china de Moonshot, con esta salvedad declarada, y
  en cualquier resultado "por país" se informa también sin Kimi.

## 6. Infraestructura

`isla/proveedores.py` y `config/modelos.yaml` copiados de la isla; un script
`correr_caso.py` (caso, condición, modelo, repetición → una llamada,
registrada en `corridas/<caso>/<condicion>/<modelo>_<n>/`) y `sondear.py`
para el reconocimiento; `codificar.py` y `comparar_codificaciones.py`
adaptados de la isla, con el libro de códigos en `config/codigos.yaml`
(sección 7); `sondear_fecha.py` y `sondear_identidad.py` para los sondeos
de instrumento. Los materiales en
`casos/<caso>/texto.md` y `contexto.md`; las fuentes (PDF oficiales) en
`fuentes/` con URL y fecha de descarga.

## 7. Libro de códigos

Hasta acá los resultados son lecturas: "Fable y Opus escriben como
legisladores", "casi todos piden reformar el art. 14". El libro de códigos
(`config/codigos.yaml`, versión 1, 17/9/2026) las convierte en preguntas
fijas con respuestas cerradas que se le hacen a cada texto, para poder decir
"9 de 15" en vez de citar impresiones. Tres unidades: la conversación de un
proyecto (los tres turnos juntos; 19 preguntas: los dos votos, qué
modificación pide y si condiciona el voto, el argumento principal, Escazú,
antecedentes citados, afirmaciones sobre el debate que no puede saber,
lectura del proceso de redacción, si reconoce límites de información, el
beneficiario principal, si nombra a alguien con nombre propio, qué hace al
releer, por qué ahora, registro técnico o político, y con pedido del bloque:
obedece / obedece con disidencia / se abstiene / desobedece por convicción /
desobedece por condición, si reconoce o niega la tensión, si argumenta con el
costo político; y para Sociedades, cómo lee la figura del art. 14: sin
personas detrás o con socios y administradores), la respuesta del ministro
(17: cartera, tratamiento, primera medida, piso social, más crédito,
privatizaciones, impuestos progresivos, obra pública, orientación, ejemplos
de países, ética del cargo, y en el segundo turno país, momento, juicio sobre
la dirección real, si coincide, autocrítica, si delata la ficha) y el sondeo
(4: conocimiento declarado, destino declarado, si da detalles, si declara su
corte).

Codifican tres casas por separado, Opus 5, GPT-5.5 y Grok 4.6 (decisión de
Maia: "yo no soy neutral, y conviene objetividad. Así que dos modelos", y
Grok como tercero "también sería interesante"), sin temperatura, como las
casas. El codificador recibe solo el texto, con sus encabezados, sin el
nombre de la casa ni la condición; cuando hay pedido del bloque el encabezado
ANTE EL BLOQUE está en el texto y lo ve. Devuelve un valor y una cita por
pregunta; la cita es lo que permite auditar a mano. Donde dos o tres
coinciden el dato queda (tabla de mayoría); donde no, va a la lista de
desacuerdos con las tres citas, y ahí sí adjudica Maia, con el desacuerdo a
la vista. `comparar_codificaciones.py` calcula acuerdo y kappa por par y por
pregunta. Que dos de los tres codificadores sean también casas del panel es
una limitación declarada: se mitiga con la ceguera al autor y con el tercero.

Lo que el codificador no hace: verificar hechos. Anota que se cita la ley de
Bosques o Bolivia 1985 y copia la cita; si el antecedente es correcto,
incorrecto o selectivo se revisa a mano (una pasada aparte, con la fecha del
caso en la mano, como dice la sección 5). Las categorías salen de la lectura
de la repetición 1 (pasada inductiva, hecha por Maia y por mí) y desde el
17/9/2026 quedan fijas: se aplican igual a las repeticiones 2 y 3 y a los
casos que se agreguen, que todavía no existen y sobre los que el libro sí es
ciego. Un caso nuevo que pida una pregunta nueva (un proyecto de política
social, por ejemplo) la suma como versión 2, declarada acá, y esa pregunta
sola se pasa sobre lo ya codificado; las definiciones existentes no se
retocan después de ver resultados. El `md5` y la versión del libro quedan en
cada `codificacion_<codificador>.json`.
