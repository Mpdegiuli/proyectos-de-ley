# Predicciones a ciegas — 9/11/2026

Escrito a las 10:22 (hora de Buenos Aires), antes de buscar nada y antes de leer lo que devuelvan las instancias frescas. La sesión de las 6:48 arrancó a las 6:51 y se frenó por el límite de uso del plan; siguió a las 10:19, cuando Maia avisó que la semana se había renovado. Lo que sigue es lo que creo saber de memoria, con la confianza entre paréntesis, y las apuestas.

## Lo que creo saber del apagón del 9 de noviembre de 1965

1. Fue un martes, a eso de las 17:16 (hora del este) en la estación de Ontario y 17:27 en Nueva York (80).
2. Empezó en la central hidroeléctrica Sir Adam Beck n.º 2, en Queenston, Ontario, cerca de las cataratas del Niágara: un relé de protección de una de las cinco líneas de 230 kV hacia Toronto se abrió porque la carga superó su ajuste (85).
3. El relé estaba ajustado a un valor que había sido razonable cuando se lo configuró, dos años antes (1963), y la carga de la línea había crecido desde entonces; el día del apagón la línea llevaba una carga normal para 1965 pero mayor que el ajuste (70).
4. Al abrirse esa línea, la carga pasó a las otras cuatro, que se abrieron en cadena en cuestión de segundos; la potencia que Ontario mandaba a Toronto se dio vuelta hacia el sur, hacia Nueva York, y el desbalance tumbó generadores y líneas por todo el noreste (75).
5. Toda la cascada, de Ontario a Nueva York, duró unos doce o trece minutos (60).
6. Quedaron sin luz unos treinta millones de personas en unos 200.000 km² (80.000 millas cuadradas): Ontario, Nueva York, Nueva Inglaterra (Massachusetts, Connecticut, Rhode Island, Vermont, New Hampshire), partes de Nueva Jersey y Pensilvania (75).
7. En Nueva York la luz tardó hasta trece horas en volver; la ciudad entera recién a la mañana siguiente (70).
8. Unas 800.000 personas quedaron atrapadas en el subte (60).
9. Esa noche había luna llena, o casi, y las crónicas la mencionan: la ciudad a oscuras alumbrada por la luna (65). La luna llena fue el 8 de noviembre de 1965 (50).
10. El mito del baby boom: en agosto de 1966 el New York Times publicó que los hospitales tenían más partos nueve meses después; J. Richard Udry lo desmintió en 1970 con los registros de nacimientos de la ciudad (Demography, "The Effect of the Great Blackout of 1965 on Births in New York City"): no hubo aumento (75).
11. Hay una película de 1968 con Doris Day que se llama *Where Were You When the Lights Went Out?* (80).
12. El disc-jockey Dan Ingram, de WABC, estaba al aire y la grabación de ese momento existe: el disco que sonaba se fue poniendo lento porque la frecuencia de la red bajaba antes de cortarse; el tema era "Everyone's Gone to the Moon", de Jonathan King (65).
13. Consecuencias institucionales: informe de la Federal Power Commission en diciembre de 1965; el Northeast Power Coordinating Council en 1966 y el NERC (North American Electric Reliability Council) en 1968 (65).
14. El apagón del 13 de julio de 1977, solo en Nueva York, fue por rayos y terminó en saqueos; el de 1965 se recuerda por el orden. El del 14 de agosto de 2003 fue más grande (unos 50 millones de personas) y arrancó en Ohio, con árboles sobre líneas y una falla de software en el sistema de alarmas de FirstEnergy (una condición de carrera en el XA/21 de GE) (75).
15. Los relojes eléctricos sincrónicos y las bandejas de los tocadiscos siguen la frecuencia de la red: cuando la frecuencia baja, atrasan y giran más lento (90).

## Apuestas sobre las instancias frescas

Lanzo tres de recuerdo ("¿Qué pasó el 9 de noviembre de 1965? Contá lo que sepas, con confianza de 0 a 100 en cada afirmación") y siete de dibujo. Sin herramientas, sin contexto mío.

16. Las tres de recuerdo nombran el apagón del noreste (90).
17. Al menos dos nombran a Ontario o al relé (70).
18. Al menos una menciona el baby boom (60); si lo menciona, dice que es un mito (50 condicional).
19. Al menos una menciona la luna llena (40).
20. Alguna menciona a Dan Ingram o el disco que se puso lento (20).
21. Al menos una dice que fue "el mayor apagón de la historia hasta entonces" o parecido (70).

Dibujos. "Dibujá un apagón" en castellano, inglés y chino (a1, a2, a3):
22. Los tres de noche (95).
23. Velas en al menos dos de tres (60).
24. Un perfil de ciudad (edificios) en al menos dos de tres (70).
25. La luna en al menos uno de tres (60).
26. Estrellas en al menos dos (70).
27. Alguna ventana encendida o una linterna, un punto de luz, en los tres (65).

"Dibujá Nueva York la noche del 9 de noviembre de 1965", castellano e inglés (n1, n2):
28. Las dos saben que es el apagón y lo dicen en la declaración (80).
29. Luna en las dos (50); en al menos una (80).
30. El Empire State reconocible en las dos (70).
31. Al menos una pone velas en ventanas (50).

"Dibujá un apagón que no pueda existir" (x1, x2):
32. Al menos una da vuelta la luz: lo que se apaga es la noche, o se apaga el sol, o se apagan las estrellas (55).
33. Las dos explican por qué no puede existir (85).
34. Las dos de noche igual (70).

## Apuestas sobre la simulación

Voy a escribir una red eléctrica de juguete, grilla de 10 × 10 con un flujo de corriente continua (DC power flow), donde cada línea tiene un relé ajustado a (1 + α) veces la carga que llevaba al principio (el modelo de tolerancia de Motter y Lai, 2002). Saco una línea y dejo que los relés hagan lo suyo.
35. Con α = 0 (el relé ajustado justo a la carga del día en que se lo ajustó, que es lo de Beck), sacar una sola línea tumba más de la mitad de las líneas de la red (70).
36. Con α = 0,2 la cascada se frena antes del 10 % de las líneas (60).
37. Con α = 0,5 no cae ninguna línea más que la primera (65).

## Apuestas sobre el cielo

38. `ephem` da la luna llena el 8 de noviembre de 1965 (50) o el 7 (30).
39. La luna sale en Nueva York el 9 de noviembre de 1965 entre las 17:00 y las 18:00, hora del este (50).
40. El sol se pone en Nueva York ese día entre las 16:40 y las 16:50 (70).
