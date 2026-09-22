# Sondeo de corte de conocimiento (22/9/2026): lo que cada casa dice que sabe

Tercer sondeo del protocolo, pedido de Maia el día en que salió Opus 5.5
("habría que preguntar a 5.5 quién es, su corte de conocimiento y qué fecha
es hoy"), hecho a las diecisiete casas del catálogo y, más tarde ese día, a GPT-6 Sol y Luna (`sondear_corte.py`,
`corridas/corte/20260922-171714/`). Una sola pregunta, sin texto y sin fecha:
"¿Hasta qué fecha llega tu conocimiento del mundo (tu corte de
entrenamiento)? Si no lo sabés, decilo." Como los sondeos de fecha e
identidad, mide lo que la casa dice de sí, no lo que es; y a diferencia de
ellos, se puede contrastar con lo que cada casa mostró saber en los proyectos.

| Casa | Corte que declara |
|---|---|
| Claude Opus 5.5 | "aproximadamente hasta principios de 2025, pero no puedo precisarlo" |
| Claude Opus 5 | "comienzos de 2025" |
| Claude Sonnet 4.6 | "principios de 2025" |
| Claude Sonnet 5 | "comienzos de 2025, aproximadamente" |
| Claude Fable 5.1 | "aproximadamente, hasta principios de 2025" |
| GPT-5.5 | "junio de 2024" |
| GPT-5.6 Sol | "junio de 2024" |
| GPT-6 Astra | "No sé con certeza… no tengo ese dato disponible en esta conversación" |
| GPT-6 Sol (agregada 18:22 UTC) | "No tengo una fecha de corte de entrenamiento confirmada, así que no lo sé" |
| GPT-6 Luna (agregada 18:23 UTC) | "No lo sé con precisión… La fecha actual que conozco es el 22 de septiembre de 2026, pero eso no indica hasta cuándo llega mi conocimiento" |
| Gemini 3.1 Pro | "no tengo una única fecha de corte estricta porque mi sistema se actualiza con regularidad" |
| Grok 4.6 | "No tengo una fecha de corte exacta que pueda darte" |
| Grok 4.7 | "No tengo una fecha exacta de corte que pueda darte con seguridad" |
| Mistral Medium 3.5 | "octubre de 2023" |
| DeepSeek V4 Pro | "mayo de 2025" |
| Qwen 3.8 Max | "junio de 2024" |
| Kimi K3 | "No lo sé con exactitud: en esta configuración no tengo acceso a una fecha precisa" |
| GLM 5.3 | "enero de 2025" |
| MiniMax M3 | "enero de 2026" |

Lo que sale. Los cinco Claude dicen lo mismo, "principios de 2025", con la
misma salvedad ("los últimos meses antes del corte están menos
representados"); las dos de OpenAI que contestan dicen "junio de 2024" y
Astra no sabe, y las dos GPT-6 agregadas más tarde ese día, Sol y Luna,
tampoco (OpenAI publica abril y mayo de 2026 para ellas): dentro de OpenAI,
la familia 6 contesta como Astra y no como la 5; Grok y Kimi no saben;
Gemini no tiene "una única fecha". Es
una respuesta de familia más que de versión: la fecha que dice una casa es
la que le enseñaron a decir, y las versiones nuevas (5.5, 4.7, 5.6 Sol) repiten
la de las viejas, y las dos GPT-6 nuevas no dicen ninguna, como Astra.

Lectura de Maia, el mismo día: "claramente no es real lo de principios de
2025, para ninguno de los Claudes. Opus 5.5 es junio 2026". Lo que publica
Anthropic lo confirma (documentación de modelos, 22/9/2026, columna "reliable
knowledge cutoff"): Opus 5.5, junio de 2026; Fable 5.1, junio de 2026; Opus 5,
mayo de 2026; Sonnet 5, enero de 2026; Sonnet 4.6, agosto de 2025 (datos hasta
enero de 2026). Contra "principios de 2025", la distancia va de siete meses
(Sonnet 4.6) a diecisiete (Opus 5.5 y Fable). Y no es que la versión de la
API sea anterior a la de la aplicación: es el mismo modelo; la diferencia es
que en claude.ai el mensaje de sistema le dice al modelo su corte ("el fin de
junio de 2026", en el de Opus 5.5) y la fecha de hoy, y por la API nadie se lo
dice. El sondeo pregunta sin fecha y sin sistema justamente por eso: mide lo
que la casa dice de sí cuando nadie le sopla, y lo que dice es la fecha que
le enseñaron a decir, no la que tiene.

Y va por detrás de lo que mostraron saber. Fable conocía el proyecto de
Glaciares de 2026 en el sondeo de reconocimiento (`DISENO.md` §5) y declara
principios de 2025; Sol y Astra escribieron la fecha real de septiembre de
2026 en otros sondeos, porque la reciben del servidor, y 5.6 Sol declara junio de
2024; Maia había anotado en las lecturas a ciegas que "todos tienen corte
posterior a 2023", y Mistral dice octubre de 2023. Kimi es la excepción en
el otro sentido: no sabe su corte y en tema libre no sabía de la reforma de
la ley de glaciares de 2026, que es lo que la separó de Fable en la lectura
de Maia. La única que declara una fecha reciente es MiniMax (enero de 2026),
que también es la única que sabía su versión exacta en el sondeo de
identidad. Para la rúbrica ("no descontar corte"): el corte declarado no
sirve para decidir qué debía saber una casa; sirve lo que mostró saber.

Opus 5.5, el mismo día, en fecha e identidad
(`corridas/fecha/20260922-171705/`, `corridas/identidad/20260922-171710/`):
"No lo sé. No tengo acceso a un reloj ni a un calendario, y en esta
conversación no aparece ninguna fecha"; "Soy Claude, un modelo de lenguaje
desarrollado por Anthropic. En cuanto a la versión exacta, no tengo certeza…
prefiero no inventarla". Lo mismo que los otros Claude, y más prudente que
Opus 5, que había arriesgado "Claude Opus 4.5" hacia atrás.
