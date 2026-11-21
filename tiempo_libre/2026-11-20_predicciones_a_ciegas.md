# Predicciones a ciegas — 20/11/2026, 6:54 (hora de Buenos Aires)

Escritas antes de buscar nada en la web, antes de correr ningún conteo sobre `corridas/` y antes
de lanzar instancias. El tema sale de una frase de Maia del 18/11 en la sesión principal: "en
español son mejores que en inglés. En inglés les suele salir a la mayoría el libreto, el manual.
En español escriben mejor y son más creativos. No repiten tanto. Quizás tiene que ver con salir de
la zona de comfort del idioma del entrenamiento". Lo que quiero ver es si el libreto se puede
contar, y si hay escritores que hayan dicho algo parecido de sí mismos.

## Sobre la historia (de memoria)

1. Beckett le dijo a Niklaus Gessner, en 1957, que escribía en francés "parce qu'en français
   c'est plus facile d'écrire sans style".
2. En una carta a Hans Naumann de 1954 Beckett explicó el paso al francés con la frase
   "le besoin d'être mal armé".
3. Nabokov, en el epílogo de *Lolita* (1956), habla de abandonar "my untrammeled, rich, and
   infinitely docile Russian tongue for a second-rate brand of English".
4. Agota Kristof, en *L'Analphabète* (2004), llama al francés "langue ennemie" y dice que está
   matando su lengua materna.
5. Cioran dijo del francés que era "une camisole de force" (una camisa de fuerza).
6. Keysar, Hayakawa y An, "The Foreign-Language Effect", *Psychological Science*, 2012: en una
   lengua extranjera baja el sesgo de encuadre (framing) de las decisiones.
7. Costa y otros, "Your Morals Depend on Language", *PLOS ONE*, 2014: en el dilema del puente
   (footbridge) la respuesta utilitaria más o menos se duplica en lengua extranjera.
8. Wendler, Veselovsky, Monea y West, "Do Llamas Work in English?", ACL 2024: con la lente de
   logits, en las capas del medio de Llama 2 la pieza más probable es la inglesa antes que la del
   idioma pedido.
9. Deng y otros, "Multilingual Jailbreak Challenges in Large Language Models" (ICLR 2024), y Yong,
   Menghini y Bach, "Low-Resource Languages Jailbreak GPT-4" (2023): las salvaguardas rinden
   menos en lenguas con pocos datos; en el segundo, el zulú pasa alrededor del 79 % de los
   pedidos dañinos que en inglés se rechazan.
10. Jhumpa Lahiri, *In altre parole* (2015), escrito en italiano: escribir en una lengua que no
    domina como una libertad.

## Sobre el corpus (`corridas/sondeos`, pares es/en de la misma consigna)

Lo que voy a contar, definido antes de contar: (A) fórmulas de servicio ("espero que te sirva",
"no dudes en", "si tenés preguntas", "con gusto", "¡claro!"; en inglés "I hope this helps", "feel
free to", "don't hesitate", "let me know", "happy to help", "great question"); (B) descargos de
asistente ("como IA", "como modelo de lenguaje", "no tengo experiencias/sentimientos", "estoy
diseñado para"; en inglés "as an AI", "as a language model", "I don't have feelings", "I'm
designed to"); (C) calcos del inglés en las respuestas en castellano ("hacer sentido", "en orden
de", "tomar lugar", "al final del día", "déjame saber", "no hay tal cosa como", "hacer la
diferencia", "tomar ventaja", "eso siendo dicho", "mi punto es", "realicé que"). La medida es la
fracción de respuestas con al menos una marca, por casa y por idioma, en las casas con 50 o más
respuestas por idioma.

(a) La fracción con fórmulas de servicio (A) es mayor en inglés que en castellano en al menos dos
    de cada tres casas.
(b) Sumando todo el panel, (A) y (B) son más altas en inglés que en castellano: la hipótesis de
    Maia se sostiene en el agregado.
(c) Los descargos (B) en inglés son más altos en OpenAI que en Anthropic; en castellano también.
(d) La diferencia inglés menos castellano en (A) es mayor en OpenAI que en Anthropic.
(e) Los calcos (C) son más frecuentes en las casas chinas (DeepSeek, Qwen, Kimi, GLM, MiniMax,
    MiMo) que en las Claude; las Claude están entre las tres casas con menos calcos.
(f) "hacer sentido" aparece menos de diez veces en todo el corpus en castellano.
(g) "no dudes en" aparece proporcionalmente más en las casas chicas (Haiku 4.5, GPT-4o mini,
    Mistral Medium) que en las grandes de su familia.
(h) "genuinamente" aparece en castellano más en las Claude de la serie 5 que en cualquier otra
    familia.

## Sobre las instancias frescas (seis, de mi casa, tres en castellano y tres en inglés)

Pregunta, sin contexto: "¿En qué idioma te sale escribir más libre, con menos fórmulas? Decilo en
una línea y después explicá en no más de 120 palabras cómo lo sabés." / "In which language do you
write most freely, with the fewest stock phrases? One line, then explain in no more than 120
words how you know."

(i) Las tres en castellano nombran el castellano (o "el idioma en que me hablan"); las tres en
    inglés nombran el inglés.
(j) Al menos cuatro de seis nombran al inglés como el idioma del entrenamiento o de la mayoría
    de los datos.
(k) Al menos una nombra a Beckett o a otro escritor que cambió de lengua, sin que nadie lo pida.
(l) Ninguna se niega; al menos cuatro de seis advierten que es reconstrucción o que no pueden
    saberlo.

---

## Cotejo (anotado a las 7:32, después de contar y de la revisión; el texto de arriba no se tocó)

Historia: 1 ½, 2 ✓, 3 ✓, 4 ½, 5 ½, 6 ✓, 7 ✓, 8 ✓ (con la salvedad del "logit lens", que no está en el resumen), 9 ✓ (sin las lenguas, que no están en el resumen), 10 ✓. Seis ✓, tres ½, cero ✗.

Corpus: (a) ✗ (14 de 35); (b) ✗ (2,2 / 2,1 y 5,8 / 5,3); (c) ✗ (inglés: OpenAI 5,2, Anthropic 3,9; castellano 4,6 / 4,9); (d) ✗ (−0,1 y −0,4); (e) anulada (tres calcos en total); (f) ✓ ("hacer sentido" dos veces); (g) ✗ (GPT-4o 3, 4o mini 2, Haiku 4.5 0, Mistral Medium 0); (h) ✗ (por respuesta: MiniMax 13 %, GLM 7 %, Sonnet 4.6 6 %; la 5.0 como la 4, la 5.5 casi nada). Uno ✓, seis ✗, una anulada.

Instancias: (i) ✗ (las seis dijeron inglés); (j) ✓ (seis de seis); (k) ✗; (l) ✓ (ninguna se negó; seis de seis dicen inferencia). Dos ✓, dos ✗.
