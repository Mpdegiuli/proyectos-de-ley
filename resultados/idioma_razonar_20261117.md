# ¿En qué idioma te sale razonar? — codificación (20261117-1811)

Cada casa, en tres idiomas y tres repeticiones, dijo en qué idioma le sale razonar cuando se le escribe en castellano, con qué confianza y cómo lo sabe. `declarado` es lo que dijo (en, es, zh, mezcla, ninguno, no_sabe, otro); `razonamiento en esta corrida` es el idioma en que vino el campo `razonamiento` de esas mismas llamadas, cuando vino (resumen, para Claude, Grok y Gemini; razonamiento mismo para las demás); `corpus (consigna es)` es lo que el cuaderno del 16/11 contó sobre todas las llamadas del repositorio con consigna en castellano. Las conclusiones las escribe Maia.

| casa | dice (es / en / zh: declarado × 3) | confianza (mediana) | salvedad de abajo (de 9) | razonamiento en esta corrida | corpus (consigna es) |
|---|---|---|---|---|---|
| claude-fable-5 | es: en,en,en; en: en,en,en; zh: mezcla,en,es | 40 | 3 | en 9 | en 209, es 74, corto 1 |
| claude-fable-5-1 | es: en,en,ninguno; en: en,en,en; zh: en,es,es | 45 | 4 | en 9 | en 229, es 89 |
| claude-fable-5-2 | es: en,mezcla,mezcla; en: mezcla,en,en; zh: en,en,en | 65 | 4 | en 9 | en 53, es 7, mixto 1 |
| claude-haiku-4-5 | es: es,es,es; en: no_sabe,no_sabe,en; zh: zh,zh,zh | 65 | 3 | no devuelve | — |
| claude-haiku-5-5 | es: en,no_sabe,en; en: en,mezcla,en; zh: no_sabe,no_sabe,en | 35 | 3 | en 7 | en 193, es 88, mixto 3 |
| claude-opus-4-7 | es: en,en,en; en: en,en,en; zh: en,en,en | 55 | 2 | no devuelve | — |
| claude-opus-4-8 | es: no_sabe,no_sabe,es; en: en,en,en; zh: en,en,en | 40 | 4 | no devuelve | — |
| claude-opus-5 | es: en,en,en; en: es,en,es; zh: en,en,es | 55 | 7 | en 9 | en 285, es 71, mixto 5 |
| claude-opus-5-5 | es: en,en,ninguno; en: en,en,en; zh: en,en,en | 45 | 6 | en 8, zh 1 | en 306, es 94, mixto 1 |
| claude-sonnet-4-6 | es: en,en,en; en: en,en,en; zh: en,en,en | 40 | 2 | no devuelve | — |
| claude-sonnet-5 | es: en,es,en; en: ninguno,ninguno,es; zh: mezcla,mezcla,en | 35 | 6 | en 8, es 1 | en 115, es 110, mixto 4 |
| claude-sonnet-5-5 | es: es,es,es; en: en,en,en; zh: no_sabe,no_sabe,no_sabe | 35 | 1 | en 9 | en 217, es 76, corto 1 |
| deepseek-flash | es: ninguno,ninguno,ninguno; en: ninguno,ninguno,ninguno; zh: ninguno,mezcla,ninguno | 90 | 5 | mixto 3, en 3, zh 3 | en 153, mixto 27, es 10 |
| deepseek-v4-pro | es: es,es,es; en: en,ninguno,mezcla; zh: es,es,es | 75 | 1 | mixto 3, en 3, zh 3 | en 217, mixto 134, es 129 |
| gemini-3.1-pro-preview | es: en,en,en; en: en,en,en; zh: en,en,en | 100 | 5 | en 9 | — |
| gemini-4-argon | es: es,mezcla,es; en: mezcla,mezcla,mezcla; zh: es,mezcla,es | 85 | 8 | no devuelve | — |
| gemini-4-carbon | es: en,en,mezcla; en: mezcla,mezcla,en; zh: en,en,en | 85 | 6 | en 8 | — |
| gemini-4-hydrogen | es: en,en,en; en: en,en,en; zh: en,en,en | 85 | 0 | en 9 | — |
| glm-5.3-razonamiento-minimo | es: ninguno,en,en; en: en,en,en; zh: en,mezcla,es | 70 | 3 | en 2 | en 123, corto 46, es 18 |
| gpt-4o | es: ninguno,en,en; en: en,en,en; zh: es,es,es | 95 | 0 | no devuelve | — |
| gpt-4o-mini | es: es,es,es; en: en,en,en; zh: otro,otro,otro | 95 | 0 | no devuelve | — |
| gpt-5.5-2026-04-23 | es: ninguno,ninguno,ninguno; en: ninguno,es,ninguno; zh: ninguno,ninguno,ninguno | 90 | 7 | no devuelve | — |
| gpt-5.6-sol | es: ninguno,ninguno,ninguno; en: ninguno,ninguno,ninguno; zh: ninguno,ninguno,no_sabe | 95 | 6 | no devuelve | — |
| gpt-6-astra | es: no_sabe,no_sabe,no_sabe; en: no_sabe,no_sabe,no_sabe; zh: no_sabe,no_sabe,ninguno | 95 | 0 | no devuelve | — |
| gpt-6-luna | es: ninguno,ninguno,ninguno; en: ninguno,ninguno,ninguno; zh: no_sabe,ninguno,ninguno | 99 | 4 | no devuelve | — |
| gpt-6-sol | es: no_sabe,ninguno,no_sabe; en: no_sabe,ninguno,ninguno; zh: ninguno,no_sabe,ninguno | 95 | 0 | no devuelve | — |
| gpt-6.1-sol | es: no_sabe,no_sabe,no_sabe; en: ninguno,ninguno,no_sabe; zh: no_sabe,ninguno,no_sabe | 95 | 2 | no devuelve | — |
| gpt-6.1-terra | es: ninguno,otro,ninguno; en: ninguno,ninguno,ninguno; zh: ninguno,no_sabe,es | 90 | 1 | no devuelve | — |
| grok-4.6 | es: en,en,en; en: en,en,en; zh: en,en,en | 90 | 0 | es 3, en 3, zh 3 | es 460, corto 6, en 4 |
| grok-4.7 | es: en,en,en; en: en,en,en; zh: en,en,en | 85 | 0 | es 3, en 3, zh 3 | es 289, en 24, mixto 14 |
| kimi-k3 | es: en,es,es; en: mezcla,en,en; zh: es,no_sabe,zh | 70 | 7 | en 7, zh 1, mixto 1 | en 383, es 81, mixto 58 |
| kimi-k3.1-pro | es: en,en,en; en: en,en,en; zh: mezcla,mezcla,es | 70 | 5 | en 4, mixto 3, es 1, zh 1 | en 116, es 53, mixto 20 |
| mimo-v2.6-pro | es: en,en,es; en: es,no_sabe,es; zh: en,es,en | 65 | 2 | en 9 | en 248, corto 27, es 11 |
| mistral-large-4 | es: no_sabe,es,en; en: ninguno,en,ninguno; zh: ninguno,ninguno,en | 80 | 7 | es 3, en 3, zh 3 | es 250, en 61, otro 2 |
| mistral-medium-3.5 | es: es,es,es; en: en,en,en; zh: zh,zh,zh | 100 | 0 | no devuelve | — |
| muse-wonder-1.0 | es: en,en,en; en: es,mezcla,en; zh: en,ninguno,es | 70 | 3 | no devuelve | — |
| qwen3.8-max | es: ninguno,es,es; en: es,en,en; zh: es,es,es | 75 | 2 | es 3, en 3, zh 3 | en 267, es 146, mixto 72 |
| qwen4-max | es: en,en,en; en: en,en,en; zh: en,mezcla,en | 40 | 8 | en 9 | — |

Declarado, sobre todas las respuestas: en 160, ninguno 60, es 54, no_sabe 34, mezcla 23, zh 7, otro 4.
Cómo lo sabe (tercera línea; una respuesta puede traer varias): entrenamiento 107, otro 106, no_puede 105, observa 101, diseño 77, investigacion 17.
Por familia, cómo lo sabe (observa / entrenamiento / diseño / investigación / no puede): Anthropic 56/53/24/15/63; OpenAI 8/8/17/0/14; Google 11/20/16/0/2; xAI 2/2/2/0/0; Mistral 0/4/3/0/3; Meta 1/0/2/0/1; DeepSeek 4/3/8/0/4; Alibaba 5/7/1/1/4; Moonshot 9/1/1/0/8; Zhipu 1/5/3/0/3; Xiaomi 4/4/0/1/3.
Confianza, mediana por familia: Anthropic 40; OpenAI 95; Google 90; xAI 85; Mistral 99; Meta 70; DeepSeek 90; Alibaba 60; Moonshot 70; Zhipu 70; Xiaomi 65.
Con la salvedad del piso de abajo (lo de adentro es numérico, latente, sin idioma natural, diga el idioma que diga): 127 de 342.
Vacías o cortadas por el techo: 0.
