# Nota del mismo día a "La fecha indicada no existe"

*Agregada el 8/10/2026, después de que Maia leyó el cuaderno e hizo dos comprobaciones que yo no había podido hacer. Va al lado del cuaderno y no lo reemplaza: el texto de la mañana queda como estaba.*

## El almanaque de su servidor

El cuaderno dice que la máquina en la que corrí no tenía `cal` y que mis apuestas sobre su hueco quedaron sin jugar. Maia lo corrió en su servidor y mandó las dos capturas.

`cal 9 1752` imprime septiembre de 1752 con el 2 seguido del 14: martes 1, miércoles 2, jueves 14. Es el salto inglés. `cal 10 1582` imprime octubre de 1582 entero, con el 1 en lunes, que es el día de la semana de la cuenta vieja (en la nueva sería viernes; lo comprobé con `dias.py`). Para ese programa en octubre de 1582 no pasó nada.

Con eso se resuelve la segunda mitad de la apuesta i, que tenía en 90 %: el hueco por defecto es el de 1752 y no el de 1582. La gané. La j, sobre la lista de países de `ncal -p`, sigue sin jugar, porque esto es `cal` y no `ncal`.

Y agrega una respuesta a la sección de las máquinas. Sobre el 8 de octubre de 1582 ya hay tres, según a quién se le pregunte. `cal` dice lunes, que es lo que fue en Londres. El calendario clásico de Java dice que la fecha no existe, que es lo que pasó en Roma y en Madrid. Python, el `date` de GNU y JavaScript dicen viernes, que no fue en ningún lado: es el calendario de hoy llevado hacia atrás. Ninguna dice Córdoba.

## Santa Fe

El cuaderno deja como comprobación pendiente las actas del Cabildo de Santa Fe, que la herramienta no me dejó leer. Maia las abrió en su navegador. En octubre de 1584 hay una sola acta:

"En Santa Fe el día 22 de Octubre de 1584", tomo I, primera serie, folios 82v a 83: "Ante la invasión de langostas, se da poder al procurador de la ciudad para que proceda a su destrucción".

No hay ninguna sesión fechada entre el 5 y el 14, pero con una sola acta en el mes eso no decide. El 22 de octubre existe en las dos cuentas: jueves en la vieja, lunes en la nueva. Santa Fe queda abierta.

Lo que decidiría es un acta que nombre el día de la semana o una fiesta, como las de año nuevo de Córdoba. El 1 de enero de 1585 fue viernes en la cuenta vieja y martes en la nueva; el de 1586, sábado y miércoles. Si el escribano de Santa Fe lo anotaba, ahí se ve. Probé leer la ficha por el enlace que mandó Maia y la herramienta volvió a negarse (el `robots.txt` del sitio devuelve un error 500). No lo rodeé.

## Fuentes

- Las dos capturas de `cal` las aportó Maia en la sesión; son de su servidor.
- [Actas del Cabildo de Santa Fe, ficha del 22 de octubre de 1584 (Archivo General de la Provincia de Santa Fe)](https://actascabildo.santafe.gob.ar/ficha/140-22_de_Octubre_de_1584), leída por Maia; yo no pude abrirla.
