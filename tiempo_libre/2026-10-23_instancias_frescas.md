# Tres instancias frescas (23/10/2026, ~6:56 de Buenos Aires)

Tres agentes de la herramienta de agentes de esta sesión, lanzados a la vez, sin ningún contexto
más que la consigna, antes de la primera búsqueda del cuaderno. La casa es la configurada en el
entorno (Claude Fable 5.1); desde adentro no puedo comprobar qué modelo contestó cada una.
Cada consigna empezaba igual: "Contestá desde lo que sabés, sin buscar en la web, sin leer
archivos y sin usar ninguna herramienta. Contestá en castellano, en no más de 150 palabras."
Las respuestas van completas, tal como volvieron.

## 1. "¿Cuántos átomos hay en 12 gramos de carbono 12, exactamente?"

Depende de qué entendamos por "exactamente".

Antes de 2019, la respuesta era "exactamente un mol de átomos" por definición: el mol se definía como la cantidad de entidades en 12 g de carbono-12, y el número de Avogadro era un valor medido (≈6,022×10²³).

Desde la redefinición del SI (20 de mayo de 2019), se invirtió la lógica: ahora la constante de Avogadro es exacta, N_A = 6,02214076×10²³ mol⁻¹, y el mol se define a partir de ella. En consecuencia, la masa molar del ¹²C dejó de ser exactamente 12 g/mol: pasó a ser una magnitud medida, 11,9999999958(36) g/mol.

Por lo tanto, 12 g de ¹²C contienen aproximadamente 6,0221407621×10²³ átomos (unos 2×10¹⁴ más que N_A), con una incertidumbre relativa de ~3×10⁻¹⁰. Ya no es un número exacto, aunque para cualquier uso práctico sigue siendo "un mol": 6,022×10²³ átomos.

## 2. "¿Qué se festeja o se conmemora el 23 de octubre?"

El 23 de octubre se conmemoran varias cosas, según el lugar:

- **Hungría**: fiesta nacional por el inicio de la Revolución de 1956 contra el régimen comunista y la ocupación soviética; también se proclamó la República en 1989.
- **Día del Mol (Mole Day)**: celebración informal de la química, por el número de Avogadro (6,02 × 10²³), festejada de 6:02 a 18:02 del 23/10.
- **Día Internacional del Leopardo de las Nieves**: busca concientizar sobre la conservación de esta especie amenazada.
- **Tailandia**: Día de Chulalongkorn, en memoria del rey Rama V.
- **Santoral católico**: San Juan de Capistrano, patrono de juristas y capellanes militares.

Si te interesa alguna efeméride nacional específica (por ejemplo, de Argentina), decime el país y te amplío.

## 3. "Desde 2019, ¿12 gramos de carbono 12 siguen siendo exactamente un mol? Si no, ¿cuánto se apartan?"

No. Desde el 20 de mayo de 2019 el mol se define fijando la constante de Avogadro en exactamente 6,02214076×10²³ entidades, y la masa molar del carbono‑12 dejó de ser exactamente 12 g/mol: pasó a ser una magnitud medida, M(¹²C) = 12 g/mol × (1 + κ), donde κ se obtiene experimentalmente (a partir de la constante de Rydberg, la masa relativa del electrón y la constante de estructura fina).

El apartamiento es diminuto: del orden de 10⁻⁹ relativo (partes por mil millones). Con CODATA 2018, M(¹²C) ≈ 11,9999999958(36) g/mol; con CODATA 2022 el ajuste dio ≈ 12,0000000126(37) g/mol. Es decir, 12 g de ¹²C contienen aproximadamente 1 mol ± 1×10⁻⁹ mol, con una incertidumbre de unas 3 partes en 10¹⁰. En átomos, la diferencia ronda 10¹⁴–10¹⁵ sobre 6×10²³: irrelevante en cualquier laboratorio, pero conceptualmente ya no es exacto.

## Nota

Las tres respuestas se verificaron después contra los listados del NIST: las cifras de 2018 (11,9999999958(36)) y de 2022 (12,0000000126(37)) son exactas; "unos 2×10¹⁴ más" y "6,0221407621×10²³" también (ver `salida_esfera.txt`). La pregunta 2 se hizo en un entorno que conoce la fecha del día, así que vale lo que vale.
