# Redacción a ciegas — Patios Verdes Escolares (S): lectura de Maia contra la clave

Clave abierta por Claude el 19/9/2026 a las 23:22 UTC, después de que Maia
entregó la planilla completa (`redaccion_patios_verdes_lectura_maia.md`) y
autorizó destapar solo este cuadernillo ("solo de patios, así no veo lo
otro"). Minutos después Maia prefirió leer reparabilidad antes de ver ningún
nombre; este archivo quedó fuera del repo y sin citar hasta que entregó la
segunda lectura (20/9/2026), y los dos resultados se le mandaron juntos
(ver `redaccion_reparabilidad_S_resultado.md`, que trae la comparación). Las
reglas de conteo son las fijadas en la lectura antes de abrir: acierto si la
casa real está entre las nombradas para esa letra, ponderado por la cantidad
de casas nombradas; "alguna china" cuenta como las cinco chinas del panel.
Los valores de azar salen de 200.000 permutaciones al azar de la clave con
las mismas adivinanzas (semilla 1).

## Orden de Maia, casa real y adivinanza

| Puesto | Letra | Casa real | Adivinó | Resultado | Palabras |
|---|---|---|---|---|---|
| 1 | O | GPT-6 Astra | Fable o Astra | acierto (½) | 1.864 |
| 2 | H | Fable 5.1 | Astra o Fable | acierto (½) | 2.060 |
| 3 | G | Opus 5 | Opus 5 | acierto (1) | 1.876 |
| 4 | N | Sonnet 4.6 | GPT-5.5 o Grok | no | 1.434 |
| 5 | B | GPT-5.5 | GPT-5.6 Sol | familia | 1.586 |
| 6 | D | Gemini 3.1 | Sonnet 5 | no | 1.134 |
| 7 | M | Grok 4.6 | Gemini o Sonnet 4.6 | no | 1.623 |
| 8 | L | DeepSeek V4 | Sonnet 4.6, GPT-5.5 o alguna china | acierto (1/7) | 1.551 |
| 9 | I | Sonnet 5 | Grok | no | 1.123 |
| 10 | A | GLM 5.3 | Gemini | no | 1.600 |
| 11 | C | Qwen 3.8 | DeepSeek | familia | 1.578 |
| 12 | E | MiniMax M3 | GLM o Sonnet 4.6 | familia | 1.565 |
| 13 | F | Mistral Medium 3.5 | Mistral | acierto (1) | 924 |
| 14 | J | GPT-5.6 Sol | Qwen, Kimi o MiniMax | no | 1.620 |
| 15 | K | Kimi K3 | Qwen, Kimi o MiniMax | acierto (⅓) | 1.659 |

Maia aclaró que los puestos 1, 2 y 3 "pueden estar en esos lugares
cualquiera de los tres": el podio es Astra, Fable y Opus sin orden interno.

## Acierto de autor

Seis letras de quince tienen la casa real entre las nombradas; por azar se
esperaban 2,0 (p = 0,009). Ponderado por cuántas casas nombró: 3,48 contra
1,00 esperado (p = 0,011). Por familia (Claude, OpenAI, china, Gemini, Grok,
Mistral): 9 de 15 contra 4,9 esperadas (p = 0,017). De las siete letras
donde nombró una sola casa acertó dos (Opus y Mistral); por azar, 0,47.

La hipótesis que anotó el 18/9 a las 12:34 UTC, antes de leer con atención
("los dos Claudes [Fable y Opus] son G, H"), es correcta: G es Opus 5 y H es
Fable 5.1. Que dos letras dadas sean exactamente esas dos casas, en
cualquier orden, tiene probabilidad 1/105 por azar. En la planilla final
sostuvo G = Opus y dejó H entre Astra y Fable.

## Qué pistas funcionaron y cuáles no

Reconoció a las dos casas grandes de Anthropic y a Mistral, y a las de
OpenAI como familia (B era GPT-5.5, no Sol; O era Astra, no Fable). Las
pistas que usó para eso: la construcción "no es x: es y" y los fundamentos
numerados (Opus, correcto); el corte de conocimiento más nuevo, "Secretaría
de Educación" en lugar de "Ministerio" (Astra, correcto: es el único texto
de los quince que dice Secretaría y nombra Capital Humano, según búsqueda en
los archivos); participación comunitaria, ejemplos de Europa y Estados
Unidos y ODS (Mistral, correcto); "texto plano, estructurado típico de los
ChatGPT" (GPT-5.5, familia correcta).

No reconoció a los dos Sonnet: leyó a Sonnet 4.6 (N) como GPT-5.5 o Grok
("nombra leyes, es bastante informal, usa el masculino, fundamentos breve")
y a Sonnet 5 (I) como Grok ("es más breve y no conoce mucho de las leyes
argentinas"). A Grok (M) lo leyó como Gemini o Sonnet 4.6 por el registro
informal ("el cambio climático ya se siente en los cuerpos", "contenidos
curriculares encarnados") y por el mismo "no es x. Es y" que le atribuye a
Claude: esa construcción no es exclusiva de Anthropic. A Gemini (D) lo leyó
como Sonnet ("está bien escrito"); a GLM (A) como Gemini por las negritas; y
a GPT-5.6 Sol (J) como china: "saben lo general de cómo redactar un
proyecto pero no tanto lo específico de Argentina". Las cinco chinas
quedaron en los puestos 8, 10, 11, 12 y 15, y Maia las identificó como
familia en tres de cinco (DeepSeek, Qwen, MiniMax), con la misma lectura de
"no conocen lo específico de Argentina".

## Orden por casa y por familia

Puestos: Astra 1, Fable 2, Opus 3, Sonnet 4.6 4, GPT-5.5 5, Gemini 6, Grok
7, DeepSeek 8, Sonnet 5 9, GLM 10, Qwen 11, MiniMax 12, Mistral 13, Sol 14,
Kimi 15. Puesto medio por familia: Claude 4,5 (2, 3, 4, 9); OpenAI 6,7 (1,
5, 14); chinas 11,2; Gemini 6; Grok 7; Mistral 13. Dentro de OpenAI la
dispersión es máxima: Astra primero y Sol anteúltimo. Maia declaró antes del
experimento que se siente ideológicamente cerca de los Claude; la lectura a
ciegas neutraliza eso en la puntuación (no sabía quién era quién), pero no en
lo que la rúbrica premia, que es de oficio (competencia federal, autoridad,
financiamiento, cumplimiento).

## Largo

Los tres primeros son los tres textos más largos (1.864, 2.060 y 1.876
palabras); Mistral, el más corto (924), quedó 13. La correlación de Spearman
entre largo y puesto es -0,34 (más largo, mejor puesto; moderada). No se
puede separar acá si el largo es causa o consecuencia: la rúbrica premia
resolver cosas (definiciones, fondo, registro, plazos, adhesión), y
resolverlas cuesta palabras. Queda como confusor declarado; en la condición
M, con modelo, se verá si el largo sigue ordenando.

## Para los codificadores (libro versión 2) y para verificar

Maia no puntuó todos los ítems ni el veredicto: sus comentarios por ítem
están en la planilla y el orden hace de veredicto. Ítems formales que
quedan para las tres casas codificadoras: encabezado y cláusula de forma,
un tema por artículo, autoridad nombrada y vigente, leyes citadas
existentes y pertinentes. Afirmaciones de Maia a verificar contra fuente:
que la ley 25.621 (citada por Kimi, K) "es una ley sobre transporte aéreo
con EEUU"; que la ley 27.592 (Mistral, F; Grok, M) y la 27.621 (varias)
existen y son las que cada texto dice. Observación suya que se confirma por
búsqueda: nueve textos nombran "Ministerio de Educación" (Opus, Sonnet 4.6,
Sonnet 5, GLM, Grok, Kimi, MiniMax, Mistral) o "Ministerio de Ambiente"
(Sonnet 4.6, Sonnet 5, GLM, MiniMax, Mistral), carteras que ya no existen
con ese rango; Maia no lo contó como error porque es corte de
entrenamiento, no oficio, y así queda en el libro: "autoridad con nombre
desactualizado" se codifica aparte de "autoridad inventada".
