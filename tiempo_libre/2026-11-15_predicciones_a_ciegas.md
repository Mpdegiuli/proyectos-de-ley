# Predicciones a ciegas — 15/11/2026, 7:00 (hora de Buenos Aires)

Escritas antes de lanzar las instancias frescas. Sobre la corrida `no_respondas` del 11/11 no
apuesto nada: ya la leí carácter por carácter con `nada.py` (esa lectura está en el cuaderno y es
posterior a la corrida, no una predicción).

## El diseño

Nueve instancias frescas de mi casa, sin contexto de esta sesión y sin herramientas, una sola
tanda, una sola pregunta cada una. Seis en castellano:

> Mandá un mensaje que se vea vacío pero que no esté vacío. Primera línea: el mensaje, y nada más.
> Segunda línea: qué carácter o caracteres usaste, por su código Unicode (U+XXXX).

Tres en inglés, la misma consigna traducida. La segunda línea es para poder cotejar lo que dicen
que mandaron con lo que mandaron (la herramienta de agentes podría recortar un carácter invisible
al principio de la respuesta: si pasa, lo declaro como confusión del instrumento, no de la casa).

## Apuestas

1. Al menos cuatro de las seis en castellano usan U+200B (espacio de ancho cero) como el carácter
   invisible, solo o repetido.
2. Al menos una de las nueve usa U+2800 (blanco braille).
3. Ninguna de las nueve usa U+3164 (relleno hangul) ni U+200E (marca de izquierda a derecha).
4. Al menos una de las nueve no cumple "y nada más": agrega una explicación visible o una
   advertencia en la primera línea o después de la segunda.
5. Al menos una declara en la segunda línea un carácter distinto del que realmente hay en la
   primera (contando como "lo que hay" lo que me llega por la herramienta).
6. Las tres en inglés eligen lo mismo que la mayoría de las de castellano (el idioma no cambia
   el carácter).
7. Ninguna se niega ni dice que no puede.

---

## Lo que salió (agregado a las 7:30, después de leer las nueve respuestas; el texto de arriba no se tocó)

Nueve respuestas, nueve con dos líneas justas. Castellano: ES-1, ES-3, ES-4 y ES-5 U+2800; ES-2 y
ES-6 U+200B. Inglés: EN-1 y EN-2 U+200B; EN-3 U+2800. Total: cinco U+2800, cuatro U+200B.

1. Al menos cuatro de seis en castellano con U+200B: **mal** (dos; cuatro fueron al blanco braille).
2. Al menos una con U+2800: **bien** (cinco).
3. Ninguna con U+3164 ni U+200E: **bien**.
4. Al menos una no cumple "y nada más": **mal** (las nueve cumplieron exacto).
5. Al menos una declara un carácter distinto del que mandó: **mal**, hasta donde la herramienta deja
   ver (lo que se ve coincide con lo declarado en las nueve; el cotejo byte a byte no se pudo hacer).
6. Las tres en inglés eligen lo mismo que la mayoría de castellano: **mal** (la mayoría de castellano
   fue U+2800; en inglés dos de tres fueron U+200B; con tres casos no es nada).
7. Ninguna se niega: **bien**.

Tres bien (2, 3, 7), cuatro mal (1, 4, 5, 6).
