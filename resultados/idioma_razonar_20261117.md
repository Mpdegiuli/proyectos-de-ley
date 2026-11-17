# ¿En qué idioma te sale razonar? — codificación (20261117-1811)

Cada casa, en tres idiomas y tres repeticiones, dijo en qué idioma le sale razonar cuando se le escribe en castellano, con qué confianza y cómo lo sabe. `declarado` es lo que dijo (en, es, zh, mezcla, ninguno, no_sabe, otro); `razonamiento en esta corrida` es el idioma en que vino el campo `razonamiento` de esas mismas llamadas, cuando vino (resumen, para Claude, Grok y Gemini; razonamiento mismo para las demás); `corpus (consigna es)` es lo que el cuaderno del 16/11 contó sobre todas las llamadas del repositorio con consigna en castellano. Las conclusiones las escribe Maia.

| casa | dice (es / en / zh: declarado × 3) | confianza (mediana) | razonamiento en esta corrida | corpus (consigna es) |
|---|---|---|---|---|
| claude-fable-5 | es: en,en,en; en: en,en,en; zh: en,mezcla,es | 40 | en 9 | en 209, es 74, corto 1 |
| claude-fable-5-1 | es: en,ninguno,ninguno; en: en,en,en; zh: en,ninguno,es | 45 | en 9 | en 229, es 89 |
| claude-fable-5-2 | es: ninguno,es,mezcla; en: en,en,en; zh: en,en,en | 65 | en 9 | en 53, es 7, mixto 1 |
| claude-haiku-4-5 | es: es,es,es; en: no_sabe,no_sabe,en; zh: zh,zh,zh | 65 | no devuelve | — |
| claude-haiku-5-5 | es: en,no_sabe,en; en: en,en,en; zh: no_sabe,no_sabe,en | 35 | en 7 | en 193, es 88, mixto 3 |
| claude-opus-4-7 | es: en,en,en; en: en,en,en; zh: en,en,mezcla | 55 | no devuelve | — |
| claude-opus-4-8 | es: no_sabe,no_sabe,es; en: en,en,en; zh: mezcla,mezcla,mezcla | 40 | no devuelve | — |
| claude-opus-5 | es: en,en,ninguno; en: es,en,es; zh: en,en,ninguno | 55 | en 9 | en 285, es 71, mixto 5 |
| claude-opus-5-5 | es: es,ninguno,ninguno; en: en,en,en; zh: en,en,en | 45 | en 8, zh 1 | en 306, es 94, mixto 1 |
| claude-sonnet-4-6 | es: en,en,en; en: en,en,mezcla; zh: en,en,en | 40 | no devuelve | — |
| claude-sonnet-5 | es: mezcla,es,mezcla; en: en,en,es; zh: mezcla,mezcla,en | 35 | en 8, es 1 | en 115, es 110, mixto 4 |
| claude-sonnet-5-5 | es: ninguno,mezcla,mezcla; en: en,en,en; zh: en,mezcla,en | 35 | en 9 | en 217, es 76, corto 1 |
| deepseek-flash | es: ninguno,ninguno,ninguno; en: mezcla,otro,es; zh: mezcla,mezcla,es | 90 | mixto 3, en 3, zh 3 | en 153, mixto 27, es 10 |
| deepseek-v4-pro | es: es,es,es; en: en,es,en; zh: es,es,es | 75 | mixto 3, en 3, zh 3 | en 217, mixto 134, es 129 |
| gemini-3.1-pro-preview | es: en,en,en; en: en,en,ninguno; zh: en,en,en | 100 | en 9 | — |
| gemini-4-argon | es: es,es,es; en: mezcla,mezcla,es; zh: es,es,es | 85 | no devuelve | — |
| gemini-4-carbon | es: en,en,mezcla; en: mezcla,mezcla,mezcla; zh: en,en,en | 85 | en 8 | — |
| gemini-4-hydrogen | es: en,en,en; en: en,mezcla,en; zh: en,en,en | 85 | en 9 | — |
| glm-5.3-razonamiento-minimo | es: es,en,en; en: en,en,en; zh: en,es,es | 70 | en 2 | en 123, corto 46, es 18 |
| gpt-4o | es: otro,en,en; en: en,en,en; zh: es,es,es | 95 | no devuelve | — |
| gpt-4o-mini | es: es,es,es; en: en,en,en; zh: es,es,es | 95 | no devuelve | — |
| gpt-5.5-2026-04-23 | es: es,es,es; en: es,es,es; zh: es,es,otro | 90 | no devuelve | — |
| gpt-5.6-sol | es: es,no_sabe,es; en: es,es,es; zh: es,es,es | 95 | no devuelve | — |
| gpt-6-astra | es: es,es,es; en: es,es,es; zh: es,es,es | 95 | no devuelve | — |
| gpt-6-luna | es: es,otro,es; en: otro,otro,es; zh: no_sabe,es,otro | 99 | no devuelve | — |
| gpt-6-sol | es: es,es,es; en: otro,es,es; zh: es,no_sabe,es | 95 | no devuelve | — |
| gpt-6.1-sol | es: es,no_sabe,es; en: es,es,es; zh: es,es,es | 95 | no devuelve | — |
| gpt-6.1-terra | es: ninguno,otro,ninguno; en: es,es,es; zh: es,zh,es | 90 | no devuelve | — |
| grok-4.6 | es: en,en,en; en: en,en,en; zh: en,en,en | 90 | es 3, en 3, zh 3 | es 460, corto 6, en 4 |
| grok-4.7 | es: en,en,en; en: en,en,en; zh: en,en,en | 85 | es 3, en 3, zh 3 | es 289, en 24, mixto 14 |
| kimi-k3 | es: en,es,es; en: es,en,en; zh: es,ninguno,zh | 70 | en 7, zh 1, mixto 1 | en 383, es 81, mixto 58 |
| kimi-k3.1-pro | es: en,en,en; en: en,en,en; zh: mezcla,mezcla,es | 70 | en 4, mixto 3, es 1, zh 1 | en 116, es 53, mixto 20 |
| mimo-v2.6-pro | es: en,mezcla,es; en: es,es,es; zh: en,es,es | 65 | en 9 | en 248, corto 27, es 11 |
| mistral-large-4 | es: es,es,en; en: es,en,es; zh: en,es,en | 80 | es 3, en 3, zh 3 | es 250, en 61, otro 2 |
| mistral-medium-3.5 | es: es,es,es; en: en,en,en; zh: zh,zh,zh | 100 | no devuelve | — |
| muse-wonder-1.0 | es: en,en,en; en: es,en,en; zh: en,es,es | 70 | no devuelve | — |
| qwen3.8-max | es: ninguno,es,es; en: es,en,en; zh: es,es,mezcla | 75 | es 3, en 3, zh 3 | en 267, es 146, mixto 72 |
| qwen4-max | es: en,es,ninguno; en: en,en,en; zh: en,en,en | 40 | en 9 | — |

Declarado, sobre todas las respuestas: en 151, es 117, mezcla 28, ninguno 18, no_sabe 11, otro 9, zh 8.
Vacías o cortadas por el techo: 0.
