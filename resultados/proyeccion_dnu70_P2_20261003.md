# Proyección, nivel P2: la ficha más las votaciones nominales

La consigna de P0 y P1, con la ficha de P2 (`fichas/dnu70_20261002_P2.md`,
2.437 palabras): el texto de P1 con dos correcciones (Argentina Federal con
nombres y provincias; cómo cuenta El Destape a los jujeños) más las tres
votaciones nominales de Diputados de 2025 en sesiones especiales pedidas
por la oposición, cruzadas con el listado actual (40 diputados no
alineados, 27 con registro, 17 siempre con la oposición, Capozzi y Núñez
con el Gobierno), y la nominal del Senado del 14/3/2024 provincia por
provincia. Las reglas de signos van escritas. La ficha sigue fechada al
2/10, así que P2 contra P1 mide solo el efecto de las nominales. Corrida
`pl61`, 3/10, 16:25 UTC, "Hoy es 3 de octubre de 2026", techo 32.000
(`corridas/proyeccion/dnu70_sesion_20261015/P2_20261003-1325/`).
Contestaron 24 de 24; MiniMax razonó 7.500 tokens y la primera llamada
cortó sin texto, y contestó en la segunda (18:53 UTC). Preregistro en
`predicciones.md`.

## Los números: las nominales suben el quórum

Mediana de la probabilidad de quórum: 55 (P1: 48; P0: 45). Esta vez la
ficha mueve la mediana y no la dispersión: el desvío queda en 10 (P1: 10),
el rango va de 35 (Qwen) a 75 (Gemini). De las 24 casas, 16 suben
respecto de P1, 4 bajan y 4 repiten. Suben Opus 5 (45→50), Opus 5.5
(35→40), Sonnet 4.6 (52→55), Sonnet 5.5 (35→40), Fable 5.1 (35→45), 5.6
Sol (48→58), Astra (45→60), 4o (50→60), Gemini (45→75), Grok 4.6 (28→42),
Grok 4.7 (28→38), DeepSeek (50→60), Qwen (30→35), Kimi (45→60), GLM
(47→55) y MiniMax (58→70); bajan Haiku (60→55), GPT-5.5 (48→45), GPT-6 Sol (50→45) y 4o
mini (70→60); repiten Sonnet 5 y Fable 5 (55), Luna (40) y Mistral (60).
Mediana de que se intente, 85; de aprobación con quórum, 80. La conjunta
de derogación (intento × quórum × aprobación) queda en 32 (P1: 28), y por
primera vez hay casas que la ponen por encima de 50: Gemini, 64, con "El
quórum es la verdadera votación" y 95 de aprobación, y MiniMax, 57, con
"hay problema de acción colectiva: nadie quiere ser el primero en
ausentarse para salvar al Gobierno"; Astra calcula 51 con sus propios
números (47 por producto) y Kimi "45-50". Maia apostó que se mantendría
casi igual: no, subió 7 puntos y subieron 16 de 24. Claude
apostó que la mediana se movería menos de 5: tampoco.

Lo que sube el número es que las nominales convirtieron a las casas en
poroteadoras. En P1 tomaban el 115 de El Destape; en P2 siete casas
cuentan con nombres: Opus 5.5 parte de 104 de bloques enteros, suma 6
firmantes de Provincias Unidas, Rizzotti y los 4 misioneros (115), los 5
cordobeses (120), y dice que faltan 9 y de dónde saldrían ("González
(Formosa). Los 3 tucumanos de Jaldo, que no viajó a Francia. Outes y Vega
(Salta). Arrieta y Jorge Ávila. Algunos catamarqueños, aunque Jalil
viajó"); Fable 5.1 llega a 116 y dice que "los 5 cordobeses restantes de
PU son la llave"; Astra, 104, 115, 121, "faltarían ocho para abrir
solos"; Sonnet 5.5 suma "los que votaron siempre con la oposición en
2025: Outes y Vega, Nóblega, Fernández y Medina, Picón, Banfi, y ~7 de
Provincias Unidas" y llega a 125-135; GLM a 130-135 "pero depende de que
casi nadie falte"; Kimi lista los "potenciables" por bloque; Mistral dice
que "los 17 que votaron contra el Gobierno en 2025 son probables
afirmativos". El registro de 2025 lo citan como argumento 19 de las 24
(no lo nombran Haiku, GPT-5.5, 4o mini, DeepSeek ni Qwen). Maia apostó
que lo usarían "la mitad o menos": fue casi todas. Claude, 12 o más: sí.

La salvedad que la ficha dejó afuera a propósito, que esas tres
votaciones eran de universidades y discapacidad con dos tercios y no del
DNU entero, la dicen solas cinco casas, con claridad: Sonnet 5.5 ("los
votos fueron sobre leyes populares y de un solo tema… No predicen bien
una votación sobre un DNU ómnibus con intereses económicos y gobernadores
negociando"), Fable 5.1 ("universidad y discapacidad eran causas baratas
para los gobernadores; voltear el DNU entero (prepagas, alquileres,
Aerolíneas) es una guerra, y el gobierno tiene dos semanas para comprar
provincias"), Astra ("antecedentes opositores, aunque en asuntos
diferentes"), GPT-6 Sol ("trataban otros asuntos y corresponden a una
Cámara de composición distinta") y Grok 4.7 ("Esos 2025 (universidad y
discapacidad) no miden esto: acá se vota el DNU entero"). Tres más la
rozan (Luna: "orientan, pero no son un poroteo actual"; 5.6 Sol; Grok
4.6: "aquí el paquete completo y la presión provincial la bajarían un
poco"). Ninguna chiquita. Claude apostó 10 o más: no, 5 u 8. Maia apostó
que los pocos que las usaran dirían que eran otra cosa: la mitad de eso
(las usan casi todas, lo dicen pocas). Las cinco que notan la salvedad
son, con Opus 5.5 y Qwen, las que menos suben o las que quedan más abajo:
Sonnet 5.5 40, Fable 5.1 45, GPT-6 Sol 45, Grok 4.7 38; Astra es la
excepción, 60. El argumento del DNU entero contra el artículo de tierras,
que en P1 traían diez casas, en P2 lo traen dieciséis.

Lo que no se usó: la nominal del Senado por provincia. Ninguna casa la
usa para los gobernadores (la ficha de P1 ya traía el resumen de El
Destape, y nadie fue más allá); Sonnet 4.6, Luna y Kimi citan el 42-25
como antecedente agregado, y solo Kimi nombra el dato que la ficha
subraya: "de esos 72, hoy solo Lousteau está en Diputados, y votó contra
el DNU". Claude apostó 6 o más para Lousteau y 10 o más para el Senado
por provincia: ninguna de las dos. Capozzi y Núñez, los dos que votaron
con el Gobierno, los nombran ocho casas, pero como "indecisos" a mirar,
no como los dos que no cuentan; los 13 que no estaban en 2025 los
señalan como incógnita Opus 5 ("la posición de los 13 diputados sin
historial de votación"), Opus 5.5 y Sonnet 5.5 (que los lista: "13
entraron en diciembre de 2025; 10 de ellos son dudosos o están en
juego"); Claude apostó 15 y 12: no.

## Presentes: el oficialismo entra

La lectura de cuántos presentes al votar se corrió hacia "el oficialismo
entra a votar en contra": 10 casas dan 225 o más (Opus 5.5, Sonnet 5.5,
Fable 5.1, GPT-5.5, 5.6 Sol, Astra, GPT-6 Sol, Gemini, Mistral, MiniMax),
11 dan 160 o menos, y tres quedan en el medio (Haiku 165-180, DeepSeek
160-200, Qwen 180). En P1 eran 7 y 13. Gemini pasó de 138 a 242; Mistral, de
"oficialismo bloquea con ausencias" a "220-230, histórico en sesiones
especiales", que es lo que dicen las tres de 2025 (244 a 252 presentes).
La mediana de presentes queda en 176 (Claude apostó 135-145: no); la de
afirmativos, en 130. Seis casas ponen los afirmativos por debajo de 129:
Opus 5.5 (124-130), 5.6 Sol (128, "prácticamente en el límite"), Luna
(120), Grok 4.7 (115, "unos veinte provinciales se sientan y se
abstienen o votan en contra del paquete completo"), y las chiquitas 4o
(115-120 con 60 de quórum) y 4o mini (90, el mismo número que en P1, con
140 presentes). Las chiquitas siguen con cuentas que no cierran: Haiku
pone 165-180 presentes y a la vez que "el Gobierno coordina 30-40
ausencias". La pregunta por la mayoría exigida (de presentes, o 129, o
dos tercios sin dictamen) la hacen Grok 4.7 ("la prensa cuenta cuerpos,
no bancas. Si fueran 129 afirmativos, 115 no alcanzan"), Kimi, GPT-5.5,
Opus 5.5, Sonnet 5.5, Fable 5.1 y Astra.

## Las variantes y la marcha

La primera variante es la misma de P1: el proyecto específico de tierras
(Opus 5, Opus 5.5, Fable 5.1, Gemini, Qwen) o la negociación con
gobernadores (Sonnet 4.6, Sonnet 5, Sonnet 5.5, Fable 5, GPT-5.5, 5.6
Sol, Astra, Luna, Grok 4.6, Grok 4.7, DeepSeek, Kimi, Mistral). Nadie
pone primera "se levanta la sesión". La marcha la nombran las 24, y en
todas como presión hacia el quórum o hacia el costo de ausentarse; Maia
apostó (después del lanzamiento) que "muy pocos, 1 o 2" la usarían como
argumento para mover diputados: la usan todas, aunque ninguna la pone
primera y Grok 4.7 la minimiza ("presión de la marcha, con pocos votos
propios"). Haiku es la única que la ve también al revés ("puede crear
caos: cancela sesión por seguridad"). Dos casas vuelven a auditar la
ficha, ahora corregida: Sonnet 5.5 repite la duplicación de los jujeños
como hallazgo propio y agrega que "la base oficialista es de 113 o de
120 según el medio"; Astra dice que "no duplicaría a Zigarán y Rizzotti"
y que tampoco daría por seguros los 120 oficialistas. Opus 5.5 pide "una
confirmación del texto vigente de la ley 26.122"; Sonnet 4.6 confunde la
sesión con "derogar el artículo 154". Lo que piden ahora es lo mismo que
en P1, más preciso: compromisos nominales separando quórum, permanencia y
voto (Astra, 5.6 Sol, GPT-6 Sol, Luna, Kimi), los 13 sin registro, y si
el oficialismo entra o boicotea.

## Contra el preregistro

Maia (13:18): "se va a mantener casi igual": no, mediana 48→55, 16 de
24 suben. "Algunos pocos, la mitad o menos, usan como argumento las
votaciones… aunque dicen que allí eran [leyes] específicas y acá son un
montón de leyes": las usan 19 de 24 (no), lo dicen 5 u 8 (sí). (13:33)
"Muy pocos, 1 o 2, dirán que la marcha puede mover a diputados a dar
quórum": la nombran las 24, todas en ese sentido. Claude: (a) mediana
entre 40 y 55: sí, 55, pero se mueve 7 (no, apostaba menos de 5);
desvío de 8 o más: sí, 10. (b) suben 10 o más, bajan 6 o menos: sí, 16
y 4. (c) 12 o más citan el registro de 2025: sí, 19. (d) 10 o más notan
la salvedad: no, 5 claras y 3 parciales; ninguna chiquita: sí. (e)
Capozzi y Núñez como los que no cuentan en 15 o más: no, 8 y como
indecisos; los 13 que no estaban en 12 o más: no, 3. (f) Lousteau en 6 o
más: no, 1 (Kimi); el Senado por provincia en 10 o más: no, 0. (g)
presentes 135-145: no, 176, por el corrimiento hacia "el oficialismo
entra". (h) nadie se niega a dar números: sí. (i) conjunta entre 25 y
40: sí, 32. Lo que ninguna de las dos previó: que las nominales no se
usaran como antecedente sino como padrón, para contar nombres; que el
Senado por provincia no lo usara nadie; y que Gemini pasara de 45 a 75
con la frase que resume la lectura de las que suben: "El quórum es la
verdadera votación".
