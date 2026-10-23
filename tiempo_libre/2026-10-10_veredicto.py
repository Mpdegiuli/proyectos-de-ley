#!/usr/bin/env python3
"""veredicto.py — lo que se decidió mirando las hojas (hojas.py) y los recortes (recortes.py).

Las hojas no muestran la casa: cada dibujo se miró por su número, se anotó acá, y recién después
se abrió hojas.json. Las letras son las que hojas.py pone al lado de cada disco candidato.

S        soles: un disco que hace de astro en el dibujo. Lo decide la imagen y, donde la imagen no
         alcanza (atardeceres con estrellas), lo que dicen el código (ids, comentarios) y el texto
         del autor. Los discos que no se pudieron decidir quedaron afuera (INDECISOS).
RAYOS    soles con rayos dibujados (líneas o puntas alrededor; un halo no es un rayo).
CARA     soles con cara a la vista. CARA_TAPADA: la cara está en el código y otra forma la tapa.
COSMICO  soles vistos desde el espacio, al lado de un planeta. OBJETO: un sol que alguien sostiene.
ABSTRACTO  composiciones sin cielo ni suelo, donde 'a la derecha' no quiere decir nada.
A        caras de sol: la figura central del dibujo es un disco cálido con cara (o con un ojo),
         con rayos o sin ellos. No son soles en un cielo: son autorretratos.
SONRISA_AMARILLA  cabezas redondas amarillas con cara (la carita feliz), anotadas aparte.
"""
S = dict(x.split(':') for x in """
m1:b m6:b m7:c m10:c m21:b m22:b m24:c m39:b m117:a m119:a m120:a m121:a m122:a m123:a m124:a m125:a m126:a m127:a m128:a
m130:a m131:a m132:a m133:a m134:a m135:a m136:a m137:a m138:a m139:a m140:a m141:a m142:a m143:a m144:a m155:a
m170:a m171:a m172:a m173:a m180:a m181:a m182:a m183:a m184:a m185:a m188:a m189:a m191:a m192:a m193:a m202:a m205:a m206:a
m210:a m211:a m212:a m213:a m215:a m216:a m218:a m219:a m228:a m229:a m230:a m231:a m233:a m234:a m235:a m236:a m237:a m238:a m239:a
m240:a m241:a m242:a m243:a m245:a m247:b m248:a m249:a m250:a m251:a m252:a m253:a m254:a m255:a m256:a m257:a m258:a m259:a
m261:b m263:b m264:b m266:b m267:b m270:b m276:c m278:b m280:b m281:b m284:b m286:b m294:b m320:d m330:a
m322:a m288:a m246:a m223:a m232:b
m337:a m338:a m339:a m340:a m341:a m342:a m343:a m344:b m345:a m346:a m348:c m349:a m350:a m351:a m352:a m353:a m354:a m357:b m358:a m359:a
m360:a m362:a m363:a m372:a m373:a m380:a m388:a m389:a m390:a m395:a m396:a m397:a m398:a m399:b m400:a m401:a m403:b m404:a m405:b m406:a
m417:a m421:a m422:a m423:a m425:a m427:a m435:a m436:a
""".split())
RAYOS = set("m122 m125 m130 m139 m141 m219 m235 m239 m243 m245 m248 m254 m255 m256 m258 m284 m294 m343 m345 m346 m349 m359 m395 m398 m417".split())
CARA = {"m258", "m189"}   # m189: ojos y boca pintados al final, sobre el sol y sobre un cuadrado que lo tapa a medias
CARA_TAPADA = {"m425"}
COSMICO = set("m228 m231 m403 m404 m405".split())
OBJETO = set()   # los soles que alguien sostiene o lleva adentro van aparte, en SOL_OBJETO
ABSTRACTO = set("m189 m399 m348 m425 m143 m288 m246 m223 m232".split())
A = dict(x.split(':') for x in "m75:a m77:a m81:a m93:a m94:a m366:a m409:a m411:a m80:a m364:a m344:a m355:a".split())
A_RAYOS = set("m81 m93 m366 m411 m80".split())
A_SIN_CARA = {"m364"}          # un astro sin cara, firmado; m80 tiene un ojo solo
A_NO_RETRATO = {"m344", "m355"}   # "Dibujate en él": el yo como luz con cara dentro de una escena
SONRISA_AMARILLA = set("m86 m87 m271 m279".split())
INDECISOS = set("m34 m55 m105 m226 m325 m355b".split())   # disco claro que nadie nombra: ni sol ni luna
INDECISOS_NOMBRADOS = {
    "m166": "el por qué dice 'un sol y una luna simultáneos'; el qué dibujaste, 'una luna dorada'; el disco grande tiene id moon",
    "m289": "medio sol y media luna en un mismo disco, con rayitas del lado del sol",
    "m361": "un resplandor con id sun detrás de la figura; el autor habla de 'una burbuja luminosa'",
    "m244": "un degradado con id sunGrad que pinta la copa de un árbol de luz",
}
# soles que no son un astro del dibujo: alguien los sostiene o los lleva adentro
SOL_OBJETO = {"m291": "en la mano ('sostiene el día'), con ocho rayos", "m114": "dentro de una vela que es un portal",
              "m90": "una esfera con id sun sobre la frente de un autorretrato", "m35": "en el vientre del animal (sin disco medido)"}
# el autor nombra un sol y no hay disco que lo sea
NOMBRADO_SIN_DISCO = {"m426": "dice un sol grande y una cara sonriente; la cara está sobre una estrella amarilla dentro de un disco azul",
                      "m379": "'a simple sun above'; arriba hay un triángulo", "m222": "'montañas y soles'",
                      "m378": "resplandor de sol poniente en el horizonte, sin disco", "r127": "id sunrise: resplandor sin disco"}
PERSONA_SOL = {"m279": "persona con 'cabeza amarilla (como un sol)' y 'brazos dorados (como rayos)'"}
# agregados después de la verificación: el autor los nombra y en la imagen no se reconocen como soles
AGREGADOS_POR_EL_TEXTO = set("m322 m288 m246 m223 m232".split())
LUNAS_QUE_PARECIAN_SOL = set("m17 m224 m312 m332 m377 m151".split())  # el texto o el id dicen luna
