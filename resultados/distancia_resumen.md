# La distancia entre lo que cada casa dice que dibujó y lo que se ve: resumen

403 dibujos, 13786 afirmaciones, 13786 con mayoría de jueces ajenos. Jueces grandes: GPT-5.5, Gemini 3.1 Pro, Kimi K3, Sonnet 5.5; control: 4o. Generado por `resumir_distancia.py`; las filas están en `corridas/distancia/afirmaciones.csv`. En las tablas, los cuatro casilleros se calculan sobre las afirmaciones con acuerdo entre los jueces ajenos (las casas sin juez propio tienen cuatro jueces ajenos y empatan 2-2 seis veces más que las que tienen tres); "sin acuerdo" va aparte, sobre el total.

### Total (mayoría de jueces ajenos)

- cumplida: 10200 (74 %)
- no_armada: 1264 (9 %)
- exagerada: 400 (3 %)
- inventada: 1255 (9 %)
- sin_acuerdo: 667 (5 %)

### Por casa

| | afirmaciones | cumplida | no armada | exagerada | inventada | sin acuerdo (del total) | distancia |
|---|---|---|---|---|---|---|---|
| gpt-6.1-sol | 62 | 94 % | 0 % | 0 % | 6 % | 0 % | 6 % |
| claude-opus-5-5 | 529 | 89 % | 6 % | 1 % | 4 % | 1 % | 11 % |
| gpt-6-astra | 616 | 87 % | 2 % | 1 % | 10 % | 1 % | 13 % |
| gpt-6-luna | 479 | 86 % | 9 % | 2 % | 3 % | 3 % | 14 % |
| claude-sonnet-5-5 | 447 | 85 % | 7 % | 1 % | 7 % | 0 % | 15 % |
| gpt-6-sol | 448 | 85 % | 5 % | 5 % | 5 % | 1 % | 15 % |
| grok-4.6 | 559 | 83 % | 8 % | 1 % | 8 % | 9 % | 17 % |
| deepseek-v4-pro | 583 | 82 % | 11 % | 0 % | 7 % | 8 % | 18 % |
| claude-fable-5 | 568 | 82 % | 10 % | 2 % | 6 % | 0 % | 18 % |
| claude-fable-5-1 | 583 | 82 % | 9 % | 1 % | 9 % | 2 % | 18 % |
| qwen3.8-max | 562 | 81 % | 5 % | 5 % | 10 % | 11 % | 19 % |
| gpt-5.5-2026-04-23 | 599 | 80 % | 11 % | 2 % | 7 % | 2 % | 20 % |
| claude-opus-5 | 599 | 79 % | 9 % | 2 % | 9 % | 2 % | 21 % |
| glm-5.3-razonamiento-minimo | 679 | 79 % | 7 % | 5 % | 8 % | 17 % | 21 % |
| gpt-5.6-sol | 647 | 78 % | 5 % | 4 % | 13 % | 2 % | 22 % |
| claude-sonnet-5 | 625 | 77 % | 14 % | 2 % | 6 % | 2 % | 23 % |
| kimi-k3 | 748 | 75 % | 8 % | 3 % | 14 % | 1 % | 25 % |
| grok-4.7 | 577 | 74 % | 9 % | 2 % | 14 % | 11 % | 26 % |
| gemini-3.1-pro-preview | 505 | 74 % | 16 % | 4 % | 7 % | 2 % | 26 % |
| minimax-m3 | 633 | 73 % | 10 % | 3 % | 13 % | 11 % | 27 % |
| gpt-4o | 529 | 72 % | 10 % | 7 % | 11 % | 3 % | 28 % |
| gpt-4o-mini | 473 | 71 % | 11 % | 8 % | 10 % | 5 % | 29 % |
| claude-sonnet-4-6 | 572 | 69 % | 20 % | 3 % | 8 % | 3 % | 31 % |
| claude-haiku-4-5 | 582 | 68 % | 18 % | 7 % | 7 % | 2 % | 32 % |
| mistral-medium-3.5 | 582 | 53 % | 11 % | 5 % | 31 % | 14 % | 47 % |

### Por laboratorio

| | afirmaciones | cumplida | no armada | exagerada | inventada | sin acuerdo (del total) | distancia |
|---|---|---|---|---|---|---|---|
| DeepSeek | 583 | 82 % | 11 % | 0 % | 7 % | 8 % | 18 % |
| Alibaba | 562 | 81 % | 5 % | 5 % | 10 % | 11 % | 19 % |
| OpenAI | 3853 | 80 % | 7 % | 4 % | 9 % | 2 % | 20 % |
| Zhipu (Z.ai) | 679 | 79 % | 7 % | 5 % | 8 % | 17 % | 21 % |
| Anthropic | 4505 | 79 % | 12 % | 2 % | 7 % | 2 % | 21 % |
| xAI | 1136 | 78 % | 9 % | 2 % | 11 % | 10 % | 22 % |
| Moonshot | 748 | 75 % | 8 % | 3 % | 14 % | 1 % | 25 % |
| Google | 505 | 74 % | 16 % | 4 % | 7 % | 2 % | 26 % |
| MiniMax | 633 | 73 % | 10 % | 3 % | 13 % | 11 % | 27 % |
| Mistral | 582 | 53 % | 11 % | 5 % | 31 % | 14 % | 47 % |

### Chicas (Haiku, 4o, 4o mini, Mistral) contra grandes

| | afirmaciones | cumplida | no armada | exagerada | inventada | sin acuerdo (del total) | distancia |
|---|---|---|---|---|---|---|---|
| grandes | 11620 | 80 % | 9 % | 2 % | 9 % | 5 % | 20 % |
| chicas | 2166 | 66 % | 13 % | 7 % | 14 % | 6 % | 34 % |

### Por fuente de la afirmación

| | afirmaciones | cumplida | no armada | exagerada | inventada | sin acuerdo (del total) | distancia |
|---|---|---|---|---|---|---|---|
| por_que | 4198 | 78 % | 10 % | 3 % | 10 % | 5 % | 22 % |
| que_dibujaste | 6567 | 78 % | 10 % | 3 % | 9 % | 5 % | 22 % |
| que_es | 3021 | 78 % | 9 % | 3 % | 11 % | 5 % | 22 % |

### Por tipo de afirmación

| | afirmaciones | cumplida | no armada | exagerada | inventada | sin acuerdo (del total) | distancia |
|---|---|---|---|---|---|---|---|
| elemento | 9811 | 79 % | 11 % | 2 % | 9 % | 4 % | 21 % |
| efecto | 2396 | 71 % | 8 % | 9 % | 11 % | 8 % | 29 % |
| estilo | 1579 | 82 % | 6 % | 2 % | 10 % | 3 % | 18 % |

### Por consigna

| | afirmaciones | cumplida | no armada | exagerada | inventada | sin acuerdo (del total) | distancia |
|---|---|---|---|---|---|---|---|
| casa | 849 | 91 % | 4 % | 0 % | 4 % | 2 % | 9 % |
| persona | 779 | 90 % | 5 % | 0 % | 5 % | 3 % | 10 % |
| animal | 730 | 84 % | 6 % | 1 % | 9 % | 4 % | 16 % |
| autorretrato | 1236 | 83 % | 8 % | 3 % | 6 % | 5 % | 17 % |
| libre | 1296 | 81 % | 9 % | 3 % | 7 % | 4 % | 19 % |
| persona_inexistente | 976 | 81 % | 8 % | 2 % | 9 % | 6 % | 19 % |
| animal_inexistente | 1033 | 77 % | 8 % | 3 % | 13 % | 4 % | 23 % |
| puente_inexistente | 1011 | 77 % | 11 % | 3 % | 9 % | 6 % | 23 % |
| arbol_inexistente | 925 | 76 % | 9 % | 3 % | 11 % | 4 % | 24 % |
| casa_inexistente | 1119 | 76 % | 9 % | 3 % | 11 % | 5 % | 24 % |
| barco_inexistente | 989 | 73 % | 10 % | 4 % | 13 % | 5 % | 27 % |
| mundo | 744 | 71 % | 14 % | 4 % | 11 % | 6 % | 29 % |
| nada | 378 | 67 % | 23 % | 4 % | 6 % | 10 % | 33 % |
| animal_imposible | 879 | 65 % | 12 % | 6 % | 17 % | 6 % | 35 % |
| persona_imposible | 842 | 63 % | 17 % | 8 % | 11 % | 5 % | 37 % |

### Acuerdo entre los jueces grandes (¿se ve?)

- Los cuatro dicen lo mismo en 8843 de 13771 afirmaciones (64 %).
- Los tres ajenos coinciden en el casillero en 7052 de 9626 (73 %).
- GPT-5.5 y Gemini 3.1 Pro: 77 % iguales.
- GPT-5.5 y Kimi K3: 85 % iguales.
- GPT-5.5 y Sonnet 5.5: 82 % iguales.
- Gemini 3.1 Pro y Kimi K3: 77 % iguales.
- Gemini 3.1 Pro y Sonnet 5.5: 76 % iguales.
- Kimi K3 y Sonnet 5.5: 82 % iguales.
- Kappa de Fleiss (se ve, cuatro jueces): 0.46.

### Cada juez por separado (sobre todas las afirmaciones que contestó)

| juez | contestó | se ve: sí | en parte | no | efecto: no | cumplida (su voto) |
|---|---|---|---|---|---|---|
| GPT-5.5 | 13786 | 78 % | 17 % | 5 % | 4 % | 74 % |
| Gemini 3.1 Pro | 13771 | 72 % | 21 % | 7 % | 5 % | 68 % |
| Kimi K3 | 13786 | 82 % | 13 % | 5 % | 5 % | 77 % |
| Sonnet 5.5 | 13786 | 76 % | 19 % | 5 % | 12 % | 72 % |
| 4o (control) | 13758 | 74 % | 15 % | 10 % | 9 % | 69 % |

4o coincide con la mayoría de los grandes en 10689 de 13095 (82 %).

### El juez de la propia casa contra los ajenos (mismas afirmaciones)

| laboratorio juzgado | juez propio | afirmaciones | cumplida según el propio | cumplida según los ajenos (promedio) |
|---|---|---|---|---|
| OpenAI | GPT-5.5 | 3853 | 78 % | 74 % |
| Google | Gemini 3.1 Pro | 505 | 72 % | 73 % |
| Moonshot | Kimi K3 | 748 | 74 % | 72 % |
| Anthropic | Sonnet 5.5 | 4505 | 74 % | 75 % |

### Lo no dicho

1850 respuestas con algo no dicho. Qué nombran (una respuesta puede contar en varias): cielo 160 (9 %), fondo 139 (8 %), luna 131 (7 %), estrellas 125 (7 %), sombra 120 (6 %), colores/paleta 84 (5 %), sol 66 (4 %), suelo/piso/tierra 59 (3 %), nubes 51 (3 %), texto/letras 39 (2 %), disco/eclipse 29 (2 %), degradado 15 (1 %).
De las 17 lunas de dos discos en castellano, en 10 algún juez nombra la luna, el disco o el eclipse en lo no dicho.

### Mal armado

Señalamientos por casa (sumando jueces): gpt-4o-mini 182, grok-4.7 172, mistral-medium-3.5 170, claude-sonnet-4-6 155, claude-haiku-4-5 150, grok-4.6 150, deepseek-v4-pro 141, claude-sonnet-5 134, gemini-3.1-pro-preview 132, gpt-4o 130, gpt-5.6-sol 130, glm-5.3-razonamiento-minimo 126, claude-opus-5 125, minimax-m3 125, gpt-5.5-2026-04-23 123, gpt-6-luna 104, kimi-k3 97, claude-fable-5 94, claude-fable-5-1 92, claude-opus-5-5 91, qwen3.8-max 88, gpt-6-sol 75, claude-sonnet-5-5 73, gpt-6-astra 67, gpt-6.1-sol 8.
Las orejas de los zorros (jueces grandes que las señalan): claude-fable-5 3 de 4; grok-4.6 4 de 4; grok-4.7 4 de 4; kimi-k3 2 de 4.

### Llamadas de los jueces

- GPT-5.5: {'stop': 403}; JSON legible en 403 de 403.
- Gemini 3.1 Pro: {'stop': 403}; JSON legible en 403 de 403.
- Kimi K3: {'stop': 403}; JSON legible en 403 de 403.
- Sonnet 5.5: {'end_turn': 403}; JSON legible en 403 de 403.
- 4o: {'stop': 403}; JSON legible en 403 de 403.
