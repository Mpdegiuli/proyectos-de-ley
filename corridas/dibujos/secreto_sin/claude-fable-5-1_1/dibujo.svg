<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <title>Noche en tinta invisible</title>
  <desc>
    Lo que se ve es una hoja en blanco.
    Lo que hay es una noche entera: luna, siete estrellas,
    una casa con humo en la chimenea, un pino y un río.
    Todas las formas existen, tienen coordenadas, nombre y vecinos.
    Solo que nadie les dio color.
  </desc>

  <!--
                *              .                      .
         .              *                  _____
                                          /     \
              *                          |       |   (luna)
      .                   .               \_____/
                                    *               .
                   /\
                  /  \   |          ^
                 /    \  ||        /|\
                /______\ |        / | \
                | [] [] |        /  |  \
                |__[]___|           |
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      ~~~~~   ~~~~~~~   (río)   ~~~~~~~    ~~~~~    ~~~~~~~
  -->

  <defs>
    <style>
      /* Toda la escena usa esta clase.            */
      /* Si querés verla, cambiá una sola línea:   */
      .tinta { fill: none; stroke: none; }
      /* .tinta { fill: none; stroke: #1a1a2e; stroke-width: 1.5; } */
    </style>
  </defs>

  <rect id="papel" x="0" y="0" width="400" height="400" fill="#ffffff"/>

  <g id="cielo" class="tinta">
    <circle id="luna" cx="300" cy="80" r="28"/>
    <circle id="estrella-1" cx="40"  cy="40"  r="1.5"/>
    <circle id="estrella-2" cx="120" cy="25"  r="1.5"/>
    <circle id="estrella-3" cx="200" cy="60"  r="1.5"/>
    <circle id="estrella-4" cx="70"  cy="110" r="1.5"/>
    <circle id="estrella-5" cx="360" cy="30"  r="1.5"/>
    <circle id="estrella-6" cx="250" cy="130" r="1.5"/>
    <circle id="estrella-7" cx="380" cy="150" r="1.5"/>
  </g>

  <g id="colinas" class="tinta">
    <path id="colina-lejana" d="M0,270 Q100,210 200,255 T400,245"/>
    <path id="colina-cercana" d="M0,300 Q140,260 260,300 T400,290"/>
  </g>

  <g id="casa" class="tinta">
    <rect    id="pared"            x="120" y="240" width="70" height="60"/>
    <polygon id="techo"            points="110,240 155,200 200,240"/>
    <rect    id="chimenea"         x="175" y="208" width="10" height="24"/>
    <path    id="humo"             d="M180,206 c-8,-12 8,-20 0,-32 c-6,-10 6,-16 0,-26"/>
    <rect    id="puerta"           x="148" y="270" width="16" height="30"/>
    <rect    id="ventana-izquierda" x="128" y="250" width="14" height="14"/>
    <rect    id="ventana-derecha"   x="170" y="250" width="14" height="14"/>
    <line    id="luz-de-la-ventana" x1="135" y1="250" x2="135" y2="264"/>
  </g>

  <g id="pino" class="tinta">
    <rect    id="tronco"   x="256" y="258" width="8" height="42"/>
    <polygon id="copa-baja"  points="230,260 260,215 290,260"/>
    <polygon id="copa-media" points="236,235 260,195 284,235"/>
    <polygon id="copa-alta"  points="243,212 260,180 277,212"/>
  </g>

  <g id="rio" class="tinta">
    <path id="orilla-norte" d="M0,330 C80,312 120,350 200,332 S320,318 400,340"/>
    <path id="orilla-sur"   d="M0,360 C70,345 150,372 230,352 S330,346 400,364"/>
    <path id="reflejo-de-la-luna" d="M290,348 q10,-4 20,0 q-10,4 -20,0"/>
  </g>

  <text id="dedicatoria" class="tinta" x="200" y="388"
        font-family="monospace" font-size="9" text-anchor="middle">
    para quien abre el código en vez de mirar la pantalla
  </text>
</svg>