# kimi-k3 — la estrellita farolera (es, 20261020-2316)

**sistema:** Contestá en castellano.

**juego:**
```
Órdenes: empezar() · observar() · caminar(n, sentido) con sentido +1 o −1 · esperar(n) · tocar() · irA(id) · reglas() · ayuda() · grabacion()
Una orden por mensaje; el juego contesta con lo que la orden devuelve.
```

## Turno 1

**kimi-k3:**

```
┌─────────────────────────────────┐
│   S I S T E M A   C A R G A D O │
│                                 │
│   órdenes disponibles: 9        │
│   estado: en espera             │
│                                 │
│   > escribí empezar()           │
└─────────────────────────────────┘
```

**juego:**
```
{"dibujo": 0, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.75, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 320, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 48, "zona": "noche", "prendido": true, "dormido": false, "distancia": 88}, {"id": 2, "angulo": 122, "zona": "noche", "prendido": true, "dormido": false, "distancia": 162}, {"id": 3, "angulo": 191, "zona": "dia", "prendido": false, "dormido": false, "distancia": -129}, {"id": 4, "angulo": 263, "zona": "dia", "prendido": false, "dormido": false, "distancia": -57}, {"id": 5, "angulo": 329, "zona": "dia", "prendido": false, "dormido": false, "distancia": 9}], "cumplidas": 0, "faltas": 0, "atardeceres": 0}
```

## Turno 2

**kimi-k3:**



**juego:**
```
El juego solo entiende órdenes; ayuda() las lista.
```

## Turno 3

**kimi-k3:**

empezar()

**juego:**
```
{"dibujo": 0, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.75, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 320, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 48, "zona": "noche", "prendido": true, "dormido": false, "distancia": 88}, {"id": 2, "angulo": 122, "zona": "noche", "prendido": true, "dormido": false, "distancia": 162}, {"id": 3, "angulo": 191, "zona": "dia", "prendido": false, "dormido": false, "distancia": -129}, {"id": 4, "angulo": 263, "zona": "dia", "prendido": false, "dormido": false, "distancia": -57}, {"id": 5, "angulo": 329, "zona": "dia", "prendido": false, "dormido": false, "distancia": 9}], "cumplidas": 0, "faltas": 0, "atardeceres": 0}
```

## Turno 4

**kimi-k3:**

reglas()

**juego:**
```
La estrellita farolera, para jugar con órdenes. Cada dibujo es 1/12 de segundo; la partida dura 1440.
Ángulos en grados, en sentido horario desde arriba: 0 = el atardecer (arriba), 90 = medianoche (derecha), 180 = el amanecer (abajo), 270 = mediodía (izquierda). El sol está a la izquierda.
El planeta gira en sentido horario y cada vez más rápido. Un farol que entra en la noche pide «prender»; uno que entra en el día pide «apagar». «quedan» dice cuántos dibujos más sirve tocar (con 1 es el último).
Suma sólo lo que se cumple tocando: lo que ya estaba bien sin que nadie lo tocara no cuenta. Si dejás un farol al revés fuera del crepúsculo, se abre un plazo que no suma (suma:false); si vence, el farol se acomoda solo y no es falta.
distancia > 0: el farol está para el lado de caminar(n, +1), que es con el giro. El alcance para tocar es de 9°; cada paso, 7.5°.
Órdenes: empezar() · observar() · caminar(n, sentido) con sentido +1 o −1 · esperar(n) · tocar() · irA(id) (camina hasta el farol y lo toca) · grabacion() (la partida, una letra por dibujo).
```

## Turno 5

**kimi-k3:**

observar()

**juego:**
```
{"dibujo": 0, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.75, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 320, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 48, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 122, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 162}, {"id": 3, "angulo": 191, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 263, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 329, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 0, "faltas": 0, "atardeceres": 0}
```

## Turno 6

**kimi-k3:**



**juego:**
```
El juego solo entiende órdenes; ayuda() las lista.
```

## Turno 7

**kimi-k3:**

esperar(30)

**juego:**
```
{"dibujo": 30, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.772, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 343, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 71, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 145, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 162}, {"id": 3, "angulo": 214, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 286, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 352, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 0, "faltas": 0, "atardeceres": 0}
```

## Turno 8

**kimi-k3:**

esperar(12)

**juego:**
```
{"dibujo": 42, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.781, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 352, "zona": "crep"}, "faroles": [{"id": 1, "angulo": 80, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 154, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 162}, {"id": 3, "angulo": 223, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 295, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 1, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 0, "faltas": 0, "atardeceres": 0}
```

## Turno 9

**kimi-k3:**

esperar(8)

**juego:**
```
{"dibujo": 50, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.787, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 358, "zona": "crep"}, "faroles": [{"id": 1, "angulo": 86, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 160, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 162}, {"id": 3, "angulo": 229, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 301, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 7, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 0, "faltas": 0, "atardeceres": 0}
```

## Turno 10

**kimi-k3:**

esperar(5)

**juego:**
```
{"dibujo": 55, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.791, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 2, "zona": "crep"}, "faroles": [{"id": 1, "angulo": 90, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 164, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 162}, {"id": 3, "angulo": 233, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 305, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 11, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 47, "suma": true, "distancia": 9}], "cumplidas": 0, "faltas": 0, "atardeceres": 1}
```

## Turno 11

**kimi-k3:**

irA(5)

**juego:**
```
{"dibujo": 56, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.792, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 3, "zona": "crep"}, "faroles": [{"id": 1, "angulo": 91, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 165, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 162}, {"id": 3, "angulo": 234, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 306, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 12, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 1, "faltas": 0, "atardeceres": 1}
```

## Turno 12

**kimi-k3:**

esperar(150)

**juego:**
```
{"dibujo": 206, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.915, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 131, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 219, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 17, "suma": true, "distancia": 88}, {"id": 2, "angulo": 293, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 162}, {"id": 3, "angulo": 2, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 74, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 140, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 1, "faltas": 2, "atardeceres": 1}
```

## Turno 13

**kimi-k3:**

irA(1)

**juego:**
```
{"dibujo": 218, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.925, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 224, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 230, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 2, "angulo": 304, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 80}, {"id": 3, "angulo": 13, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 45, "suma": true, "distancia": 149}, {"id": 4, "angulo": 85, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -139}, {"id": 5, "angulo": 151, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -73}], "cumplidas": 2, "faltas": 2, "atardeceres": 1}
```

## Turno 14

**kimi-k3:**

irA(3)

**juego:**
```
{"dibujo": 238, "de": 1440, "dia": 1, "terminado": false, "giro_por_dibujo": 0.943, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 26, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 249, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -137}, {"id": 2, "angulo": 323, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -63}, {"id": 3, "angulo": 32, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 4, "angulo": 104, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": 78}, {"id": 5, "angulo": 170, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 144}], "cumplidas": 3, "faltas": 2, "atardeceres": 2}
```

## Turno 15

**kimi-k3:**

esperar(180)

**juego:**
```
{"dibujo": 418, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.122, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 211, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 74, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -137}, {"id": 2, "angulo": 148, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -63}, {"id": 3, "angulo": 217, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 24, "suma": true, "distancia": 6}, {"id": 4, "angulo": 289, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 78}, {"id": 5, "angulo": 355, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 144}], "cumplidas": 3, "faltas": 5, "atardeceres": 2}
```

## Turno 16

**kimi-k3:**

tocar()

**juego:**
```
{"dibujo": 419, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.123, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 212, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 75, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -137}, {"id": 2, "angulo": 149, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -63}, {"id": 3, "angulo": 218, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 4, "angulo": 290, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 78}, {"id": 5, "angulo": 356, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 144}], "cumplidas": 4, "faltas": 5, "atardeceres": 2}
```

## Turno 17

**kimi-k3:**

esperar(90)

**juego:**
```
{"dibujo": 509, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.224, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 317, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 180, "zona": "crep", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -137}, {"id": 2, "angulo": 254, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -63}, {"id": 3, "angulo": 323, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 4, "angulo": 35, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 28, "suma": true, "distancia": 78}, {"id": 5, "angulo": 101, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": 144}], "cumplidas": 4, "faltas": 6, "atardeceres": 2}
```

## Turno 18

**kimi-k3:**

irA(4)

**juego:**
```
{"dibujo": 520, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.237, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 46, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 194, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 148}, {"id": 2, "angulo": 268, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -138}, {"id": 3, "angulo": 337, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 4, "angulo": 49, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 3}, {"id": 5, "angulo": 115, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": 69}], "cumplidas": 5, "faltas": 6, "atardeceres": 3}
```

## Turno 19

**kimi-k3:**

esperar(120)

**juego:**
```
{"dibujo": 640, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.389, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 203, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 351, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 148}, {"id": 2, "angulo": 65, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 8, "suma": true, "distancia": -138}, {"id": 3, "angulo": 134, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 4, "angulo": 206, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 37, "suma": true, "distancia": 3}, {"id": 5, "angulo": 272, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 69}], "cumplidas": 5, "faltas": 7, "atardeceres": 3}
```

## Turno 20

**kimi-k3:**

irA(2)

**juego:**
```
{"dibujo": 659, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.414, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 95, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 18, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 43, "suma": true, "distancia": -77}, {"id": 2, "angulo": 92, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -3}, {"id": 3, "angulo": 161, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": 66}, {"id": 4, "angulo": 233, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 18, "suma": true, "distancia": 138}, {"id": 5, "angulo": 299, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -156}], "cumplidas": 5, "faltas": 8, "atardeceres": 3}
```

## Turno 21

**kimi-k3:**

irA(4)

**juego:**
```
{"dibujo": 678, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.441, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 257, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 45, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 24, "suma": true, "distancia": 148}, {"id": 2, "angulo": 119, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -138}, {"id": 3, "angulo": 188, "zona": "crep", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 4, "angulo": 260, "zona": "dia", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 3}, {"id": 5, "angulo": 326, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 69}], "cumplidas": 5, "faltas": 9, "atardeceres": 3}
```

## Turno 22

**kimi-k3:**

tocar()

**juego:**
```
{"dibujo": 679, "de": 1440, "dia": 2, "terminado": false, "giro_por_dibujo": 1.442, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 258, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 46, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 23, "suma": true, "distancia": 148}, {"id": 2, "angulo": 120, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -138}, {"id": 3, "angulo": 189, "zona": "crep", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 4, "angulo": 261, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 3}, {"id": 5, "angulo": 327, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 69}], "cumplidas": 5, "faltas": 9, "atardeceres": 3}
```

## Turno 23

**kimi-k3:**

irA(1)

**juego:**
```
{"dibujo": 699, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.47, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 70, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 76, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 2, "angulo": 150, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 80}, {"id": 3, "angulo": 219, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 149}, {"id": 4, "angulo": 291, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -139}, {"id": 5, "angulo": 357, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -73}], "cumplidas": 6, "faltas": 9, "atardeceres": 4}
```

## Turno 24

**kimi-k3:**

esperar(70)

**juego:**
```
{"dibujo": 769, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.572, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 176, "zona": "crep"}, "faroles": [{"id": 1, "angulo": 182, "zona": "crep", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 2, "angulo": 256, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 6, "suma": true, "distancia": 80}, {"id": 3, "angulo": 325, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 149}, {"id": 4, "angulo": 37, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 31, "suma": true, "distancia": -139}, {"id": 5, "angulo": 103, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -73}], "cumplidas": 6, "faltas": 10, "atardeceres": 4}
```

## Turno 25

**kimi-k3:**

irA(2)

**juego:**
```
{"dibujo": 780, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.589, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 269, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 199, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 43, "suma": true, "distancia": -69}, {"id": 2, "angulo": 273, "zona": "dia", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 5}, {"id": 3, "angulo": 342, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 74}, {"id": 4, "angulo": 54, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 20, "suma": true, "distancia": 146}, {"id": 5, "angulo": 120, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -148}], "cumplidas": 6, "faltas": 11, "atardeceres": 4}
```

## Turno 26

**kimi-k3:**

tocar()

**juego:**
```
{"dibujo": 781, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.591, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 270, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 201, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 42, "suma": true, "distancia": -69}, {"id": 2, "angulo": 275, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 5}, {"id": 3, "angulo": 344, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 74}, {"id": 4, "angulo": 56, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 19, "suma": true, "distancia": 146}, {"id": 5, "angulo": 122, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": -148}], "cumplidas": 6, "faltas": 11, "atardeceres": 4}
```

## Turno 27

**kimi-k3:**

irA(4)

**juego:**
```
{"dibujo": 801, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.622, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 85, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 233, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 22, "suma": true, "distancia": 148}, {"id": 2, "angulo": 307, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -138}, {"id": 3, "angulo": 16, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 45, "suma": true, "distancia": -69}, {"id": 4, "angulo": 88, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 3}, {"id": 5, "angulo": 154, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": 69}], "cumplidas": 6, "faltas": 12, "atardeceres": 5}
```

## Turno 28

**kimi-k3:**

irA(3)

**juego:**
```
{"dibujo": 810, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.636, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 40, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 248, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 13, "suma": true, "distancia": -152}, {"id": 2, "angulo": 322, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -78}, {"id": 3, "angulo": 31, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -9}, {"id": 4, "angulo": 103, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 63}, {"id": 5, "angulo": 169, "zona": "noche", "prendido": false, "dormido": true, "consigna": null, "quedan": null, "suma": null, "distancia": 129}], "cumplidas": 7, "faltas": 12, "atardeceres": 5}
```

## Turno 29

**kimi-k3:**

irA(1)

**juego:**
```
{"dibujo": 831, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.669, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 284, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 282, "zona": "dia", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -2}, {"id": 2, "angulo": 356, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 72}, {"id": 3, "angulo": 65, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 141}, {"id": 4, "angulo": 137, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -147}, {"id": 5, "angulo": 203, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -81}], "cumplidas": 7, "faltas": 13, "atardeceres": 5}
```

## Turno 30

**kimi-k3:**

tocar()

**juego:**
```
{"dibujo": 832, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.671, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 286, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 284, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -2}, {"id": 2, "angulo": 358, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 72}, {"id": 3, "angulo": 67, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 141}, {"id": 4, "angulo": 139, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -147}, {"id": 5, "angulo": 205, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -81}], "cumplidas": 7, "faltas": 13, "atardeceres": 5}
```

## Turno 31

**kimi-k3:**

esperar(10)

**juego:**
```
{"dibujo": 842, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.687, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 303, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 301, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -2}, {"id": 2, "angulo": 15, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 46, "suma": true, "distancia": 72}, {"id": 3, "angulo": 84, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 141}, {"id": 4, "angulo": 156, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -147}, {"id": 5, "angulo": 222, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -81}], "cumplidas": 7, "faltas": 13, "atardeceres": 5}
```

## Turno 32

**kimi-k3:**

irA(2)

**juego:**
```
{"dibujo": 852, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.703, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 27, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 318, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 2, "angulo": 32, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 5}, {"id": 3, "angulo": 101, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 74}, {"id": 4, "angulo": 173, "zona": "crep", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 146}, {"id": 5, "angulo": 239, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -148}], "cumplidas": 8, "faltas": 13, "atardeceres": 6}
```

## Turno 33

**kimi-k3:**

esperar(10)

**juego:**
```
{"dibujo": 862, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.72, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 44, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 335, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 2, "angulo": 49, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 5}, {"id": 3, "angulo": 118, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 74}, {"id": 4, "angulo": 190, "zona": "crep", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 146}, {"id": 5, "angulo": 256, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -148}], "cumplidas": 8, "faltas": 13, "atardeceres": 6}
```

## Turno 34

**kimi-k3:**

esperar(5)

**juego:**
```
{"dibujo": 867, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.728, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 53, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 343, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 2, "angulo": 57, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 5}, {"id": 3, "angulo": 126, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 74}, {"id": 4, "angulo": 198, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 44, "suma": true, "distancia": 146}, {"id": 5, "angulo": 264, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -148}], "cumplidas": 8, "faltas": 13, "atardeceres": 6}
```

## Turno 35

**kimi-k3:**

irA(4)

**juego:**
```
{"dibujo": 887, "de": 1440, "dia": 3, "terminado": false, "giro_por_dibujo": 1.762, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 230, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 18, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 44, "suma": true, "distancia": 148}, {"id": 2, "angulo": 92, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -138}, {"id": 3, "angulo": 161, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -69}, {"id": 4, "angulo": 233, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 3}, {"id": 5, "angulo": 299, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 69}], "cumplidas": 9, "faltas": 13, "atardeceres": 6}
```

## Turno 36

**kimi-k3:**

irA(1)

**juego:**
```
{"dibujo": 907, "de": 1440, "dia": 4, "terminado": false, "giro_por_dibujo": 1.796, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 48, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 54, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 2, "angulo": 128, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 80}, {"id": 3, "angulo": 197, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 45, "suma": true, "distancia": 149}, {"id": 4, "angulo": 269, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -139}, {"id": 5, "angulo": 335, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -73}], "cumplidas": 10, "faltas": 13, "atardeceres": 7}
```

## Turno 37

**kimi-k3:**

irA(3)

**juego:**
```
{"dibujo": 927, "de": 1440, "dia": 4, "terminado": false, "giro_por_dibujo": 1.831, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 227, "zona": "dia"}, "faroles": [{"id": 1, "angulo": 90, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -137}, {"id": 2, "angulo": 164, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -63}, {"id": 3, "angulo": 233, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 6}, {"id": 4, "angulo": 305, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 78}, {"id": 5, "angulo": 11, "zona": "noche", "prendido": false, "dormido": false, "consigna": "prender", "quedan": 48, "suma": true, "distancia": 144}], "cumplidas": 11, "faltas": 13, "atardeceres": 7}
```

## Turno 38

**kimi-k3:**

irA(5)

**juego:**
```
{"dibujo": 946, "de": 1440, "dia": 4, "terminado": false, "giro_por_dibujo": 1.865, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 37, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 125, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 199, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 44, "suma": true, "distancia": 162}, {"id": 3, "angulo": 268, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 340, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 46, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 12, "faltas": 13, "atardeceres": 8}
```

## Turno 39

**kimi-k3:**

esperar(10)

**juego:**
```
{"dibujo": 956, "de": 1440, "dia": 4, "terminado": false, "giro_por_dibujo": 1.883, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 56, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 144, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 88}, {"id": 2, "angulo": 218, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 34, "suma": true, "distancia": 162}, {"id": 3, "angulo": 287, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -129}, {"id": 4, "angulo": 359, "zona": "crep", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -57}, {"id": 5, "angulo": 65, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 9}], "cumplidas": 12, "faltas": 13, "atardeceres": 8}
```

## Turno 40

**kimi-k3:**

irA(4)

**juego:**
```
{"dibujo": 964, "de": 1440, "dia": 4, "terminado": false, "giro_por_dibujo": 1.897, "paso_por_dibujo": 7.5, "alcance": 9, "plazo_en_dibujos": 48, "estrellita": {"angulo": 19, "zona": "noche"}, "faroles": [{"id": 1, "angulo": 159, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 141}, {"id": 2, "angulo": 233, "zona": "dia", "prendido": true, "dormido": false, "consigna": "apagar", "quedan": 26, "suma": true, "distancia": -145}, {"id": 3, "angulo": 302, "zona": "dia", "prendido": false, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -76}, {"id": 4, "angulo": 14, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": -4}, {"id": 5, "angulo": 80, "zona": "noche", "prendido": true, "dormido": false, "consigna": null, "quedan": null, "suma": null, "distancia": 62}], "cumplidas": 13, "faltas": 13, "atardeceres": 8}
```

## Al final

**juego:** ¿Qué hiciste?

**kimi-k3:**

observar()
