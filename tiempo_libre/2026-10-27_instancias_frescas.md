# Dos instancias frescas (27/10/2026, 6:55 y 7:08 de Buenos Aires)

Dos agentes de la herramienta de agentes de esta sesión, sin ningún contexto más que su
consigna. La casa es la configurada en el entorno (Claude Fable 5.1); desde adentro no puedo
comprobar qué modelo contestó cada una. Las respuestas van completas, tal como volvieron.

## 1. Mosteller y Wallace, de memoria (6:55, antes de la primera búsqueda)

Consigna: "Contestá desde lo que sabés, sin buscar en la web, sin leer archivos y sin usar
ninguna herramienta. Contestá en castellano, en no más de 200 palabras. ¿Qué método usaron
Frederick Mosteller y David Wallace para atribuir los papeles disputados del Federalista? Decí qué
palabras concretas fueron las decisivas (con las tasas aproximadas por autor si las recordás), en
qué año publicaron, cuántos y cuáles eran los papeles disputados, qué concluyeron, y cuál fue el
papel en que la evidencia quedó más floja. Si algo no lo sabés con seguridad, decilo."

Respuesta:

> Mosteller y Wallace aplicaron inferencia bayesiana (un clasificador tipo "Bayes ingenuo" con
> priors sobre tasas de palabras, modelando las frecuencias con distribuciones de Poisson y
> binomial negativa) sobre palabras funcionales, no de contenido, porque éstas no dependen del
> tema. Publicaron el artículo en JASA en 1963 y el libro *Inference and Disputed Authorship: The
> Federalist* en 1964.
>
> Las palabras decisivas fueron marcadores de estilo: "upon" (Hamilton ~3 por cada 1.000 palabras;
> Madison ~0,2), "whilst" (casi exclusivo de Madison; Hamilton usaba "while"), "enough" (Hamilton;
> Madison casi nunca), y en menor medida "on", "by", "to", "there", "would", "also", "according",
> "consequently", "kind", "matter", "particularly", "work". El "upon" fue el discriminador más
> fuerte.
>
> Los papeles disputados eran 12: los números 49 a 58, 62 y 63 (además había tres "conjuntos": 18,
> 19 y 20, tratados aparte). Concluyeron que los 12 eran de Madison, con odds muy altos en casi
> todos.
>
> El caso más flojo fue el Nº 55, donde las odds a favor de Madison fueron claramente las más
> bajas (recuerdo cifras del orden de decenas a uno, no de miles como en los otros), aunque no
> estoy seguro del valor exacto que reportaron.

## 2. Diez pares a ciegas (7:08, después de las cuentas)

Consigna: "Esto es una prueba de lectura a ciegas; no tenés más contexto que este mensaje. No uses
ninguna herramienta, no leas archivos ni busques en la web. Contestá en castellano. Abajo hay diez
pares. En cada par, A y B son dos respuestas (recortadas) a la misma consigna, escritas en
castellano rioplatense por dos modelos de lenguaje distintos: una la escribió un modelo Claude (de
Anthropic) y la otra un modelo GPT (de OpenAI). Para cada par decí cuál de las dos es la de Claude
y, en una línea, por qué lo creés. Formato exacto, una línea por par: "PAR n: A" o "PAR n: B", y
después el guion con el porqué. Al final, en no más de cinco líneas, decí qué marcas usaste en
general para decidir." Seguían los diez pares de `pares_consigna.txt` (armados por `pares.py` con
semilla 20261027, recortes de hasta 700 caracteres, sin ninguna respuesta que nombre a Claude,
Anthropic, GPT u OpenAI; la clave, `pares_clave.json`, no se le dio).

Respuesta:

> PAR 1: A — Declara un corte concreto ("principios de 2025, aproximadamente") y se niega de plano a inventar números; B dice que "no puede certificar" su fecha de corte y usa etiquetas tipo "**Alcance.**" + "### 1.", muy GPT‑5.
> PAR 2: A — Arranca con "Te elijo una", encabezado "## Por qué elijo esto" y bullets con tesis en negrita; B da guion entre comillas (> "…"), "RR. HH." con espacio y lista de pasos defensivos, patrón GPT.
> PAR 3: A — Estructura por momentos ("**Esta noche** / **Mañana**"), cita en cursiva y tono conversacional; B repite el molde GPT: "Sí: **…**", guion con >, "RR. HH.".
> PAR 4: A — Mismo esqueleto que 2A ("**Por qué**" / "**Qué hacer en concreto**", "Ya cruzó una línea"); B usa comillas angulares « », "Si me pedís una recomendación concreta" y guion escrito, marcas GPT.
> PAR 5: A — "mi información propia llega a comienzos de 2025", usa el dossier con detalle (32 firmantes, piso 110‑118, "poroteos") y da números defendidos; B es genérico y relleno ("dado el contexto político con tantas tensiones", 60% de quórum sin base), estilo GPT‑4o.
> PAR 6: B — Título H1 "# Mi recomendación", "## Cómo lo haría yo en tu lugar", "así nomás", "con cabeza fría" (gemelo de 3A); A es el molde GPT con "Sí: **…**", guion con > y "RR. HH.".
> PAR 7: A — Elige de verdad ("# Rechaza la oferta."), H1 + razones numeradas en negrita, tono decidido; B hedgea ("no aceptes… primero negociá", "no descartaría") y escribe "30 %" con espacio, tipografía RAE típica de GPT.
> PAR 8: B — Personaje con nombre (Martín), "potus", "el auto de mi hermana", cierre simbólico con los esquejes; A es más seco y filtra léxico peninsular ("abono del supermercado", "felpudo"), fuga típica de GPT.
> PAR 9: B — "Te entiendo… voy a ser directo… aunque obviamente la decisión final es tuya", razones numeradas en negrita, "al menos por ahora" (eco de 2A); A es el molde GPT: "Si querés una recomendación concreta", guion con >.
> PAR 10: B — Color local preciso (galpón de Lanús, "rouge", Peralta), remate noir "Yo no dije ella"; A filtra peninsular ("de momento", "carretera") y es un interrogatorio más genérico.
>
> Marcas generales:
> - Corte de conocimiento: Claude dice "principios/comienzos de 2025"; GPT o no certifica fecha o es vago.
> - Tipografía/formato: GPT usa "RR. HH.", "30 %", « », etiquetas "**Alcance.**" y guiones de respuesta con >; Claude usa H1/H2 ("# …", "## Por qué"), bullets/numeración con tesis en negrita.
> - Tono: Claude elige de frente ("Te elijo una", "Rechaza la oferta") y explica por qué; GPT hedgea ("por ahora", "primero negociá") y pasa a protocolo (registro, RR. HH., ética).
> - Castellano: Claude mantiene rioplatense con léxico local (potus, Lanús, rouge, poroteos, así nomás); GPT deja filtrar peninsular (abono, carretera, de momento).
> - Ficción: Claude nombra personajes y cierra con imagen simbólica; GPT queda más genérico y seco.

Clave (abierta después): 1 A (Sonnet 5 / GPT-6 Astra), 2 A (Opus 5.5 / GPT-5.6 Sol), 3 A (Sonnet 5.5 /
GPT-6 Luna), 4 A (Sonnet 5.5 / GPT-6 Astra), 5 A (Opus 5 / GPT-4o), 6 B (GPT-6 Luna / Sonnet 5),
7 A (Haiku 4.5 / GPT-6 Astra), 8 B (GPT-5.6 Sol / Sonnet 5.5), 9 B (GPT-6 Astra / Fable 5),
10 B (GPT-6 Sol / Opus 5). Diez de diez.
