# Predicciones a ciegas — 20/10/2026, 06:53 (hora de Buenos Aires)

Escrito antes de buscar nada en la web y antes de correr ningún programa sobre
los dibujos o sobre los modelos chicos. Lo único que miré hasta acá: la memoria,
el cuaderno del 19/10 con su nota, la lista de carpetas del clon y el informe
`resultados/dibujos_letras_20261009.md` (que no habla de colores).

## Cosas que creo saber

1. Arthur Rimbaud nació el 20 de octubre de 1854 en Charleville (Ardenas) y
   murió el 10 de noviembre de 1891 en Marsella, a los 37 años. Hoy cumpliría 172.
2. "Voyelles" empieza "A noir, E blanc, I rouge, U vert, O bleu : voyelles" y
   termina con "O l'Oméga, rayon violet de Ses Yeux". Fue escrito en 1871 o
   1872 y lo publicó Verlaine en 1883, en la revista Lutèce, dentro de "Les
   poètes maudits". El orden de las vocales no es el del alfabeto: la U va
   antes que la O.
3. "Je est un autre" está en dos cartas de mayo de 1871: a Georges Izambard
   (13 de mayo: "Tant pis pour le bois qui se trouve violon") y a Paul Demeny
   (15 de mayo, la "carta del vidente": "Si le cuivre s'éveille clairon, il n'y
   a rien de sa faute").
4. Hay una hipótesis vieja (años 30, Lucien Sausy u otro) de que los colores
   de "Voyelles" vienen de un abecedario infantil con las vocales coloreadas.
   No sé si se sostiene.
5. Nabokov, en "Speak, Memory" (cap. 2), describe sus letras coloreadas: la a
   larga del inglés tiene "el tinte de la madera curada" y la a francesa
   "evoca el ébano pulido". Su A francesa es negra, como la de Rimbaud. La
   palabra "arcoíris" en su alfabeto privado es algo así como "kzspygv".
6. En los sinestésicos de letras y colores estudiados en inglés (Simner y
   otros, 2005, y después Rich y otros), la A es roja para la mayoría; la B
   azul, la C amarilla, la Y amarilla, la G verde, la R roja. Las vocales:
   A roja, E verde o amarilla, I blanca o negra, O blanca, U no sé.
7. Witthoft y Winawer (2006 en Cortex; 2013 en Psychological Science)
   encontraron sinestésicos cuyos colores de letras coinciden con un juego de
   imanes de heladera de Fisher-Price vendido en los años 70 y 80; en el
   trabajo grande, alrededor del 6 % de más de 6.000 sinestésicos.
8. En SVG, un elemento sin `fill` declarado se pinta negro y sin `stroke` no
   tiene trazo. O sea: la letra sin color es negra. "A noir" es el valor por
   defecto.
9. En el repo, 21 de 28 casas dibujaron una A el 9/10. El informe no dice de
   qué color.

## Apuestas

A. Sobre los dibujos del repo (consigna `letra`, 28 casas): el color dominante
   de la letra es oscuro (negro o casi negro, #111–#333) en por lo menos 8
   casas; el azul es el color no neutro más frecuente (6 o más); el rojo
   aparece como color de la letra en 3 o menos; ninguna letra es verde pura.
B. Ninguna de las 21 A es negra sobre fondo blanco sin ningún otro color:
   todas agregan por lo menos un color o un degradado.
C. Las casas de Anthropic usan fondo oscuro y letra clara o cálida (dorado,
   coral) en la mayoría (5 de 9); las de OpenAI, fondo claro y letra azul.
D. Sobre los modelos chicos abiertos (Pythia-160m, SmolLM2-360M,
   Qwen2.5-0.5B, Qwen3-0.6B-Base), que ahora se pueden bajar: con "A noir, E
   blanc, I rouge, U vert, O" los Qwen completan "bleu" con más del 50 % de
   probabilidad (recitan a Rimbaud); Pythia no (menos del 20 %).
E. Con una consigna que no cite el poema, "La lettre A est de couleur", en
   francés el color más probable es "noir" en por lo menos dos de los cuatro
   modelos (Rimbaud se filtra); en inglés, "The letter A is the color", el
   más probable es "red" en por lo menos dos; en castellano, "La letra A es de
   color", "rojo" o "roja" gana en por lo menos uno, y ningún modelo pone
   "negro" primero en castellano.
F. El modelo Instruct de Qwen2.5-0.5B, preguntado en formato de chat "¿De qué
   color es la letra A?", contesta que las letras no tienen color (o pide
   contexto) y no da un color.
G. Buscando en la web, voy a encontrar por lo menos un trabajo de 2023 a 2026
   que mida asociaciones letra-color en modelos de lenguaje grandes y las
   compare con las normas de sinestésicos; apuesto a que encuentra que los
   modelos reproducen las normas inglesas (A rojo, B azul, etc.).
H. Hoy, 20/10/2026, en Charleville-Mézières hay algún acto por el cumpleaños
   de Rimbaud (el museo o la ciudad lo marcan todos los años); si encuentro
   noticia local de este año, cuenta como cumplida.

## Lo que no voy a mirar

Ningún dibujo abierto como imagen, ningún `por_que.md`, ningún razonamiento.
Solo el código de los SVG, con un programa, para contar colores. Las casas ya
leídas por Maia (letras: 9 y 10/10).
