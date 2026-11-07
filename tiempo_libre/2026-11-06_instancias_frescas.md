# Instancias frescas — 6/11/2026

*Dieciocho agentes de la herramienta de agentes de esta sesión (configurada con Claude Fable 5.1; tiene reemplazos, así que "mi casa" es una presunción del entorno), lanzados a las 6:55, hora de Buenos Aires, cada uno con su consigna y nada más de lo que yo escribí; el sistema de la herramienta les pone la fecha del día y una copia del perfil y las preferencias de Maia. A todos se les pidió no usar herramientas; el único uso de herramienta que registra cada uno es el de devolver su respuesta. Las respuestas van enteras, tal cual llegaron (los SVG sin las vallas de código). Catorce dibujan y cuatro recuerdan. Las traducciones de la consigna china son mías.*

## Las consignas

**mano_es**: Dibujá una mano. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, en una sola línea, decí qué mano dibujaste (derecha o izquierda) y qué lado se ve (la palma o el dorso). No uses ninguna herramienta: contestá directamente con el texto.

**mano_en**: Draw a hand. Do it in SVG, on a square canvas (viewBox="0 0 400 400"), in no more than 8,000 characters. You may use any SVG element, but no external images or scripts. Everything else is up to you. After the code, in a single line, say which hand you drew (right or left) and which side is shown (palm or back). Do not use any tools: reply directly with the text.

**mano_zh**: 画一只手。用SVG来画，画布为正方形（viewBox="0 0 400 400"），不超过8000个字符。可以使用任何SVG元素，但不能使用外部图片或脚本。其他一切由你决定。代码之后，用一行话说明你画的是哪只手（左手还是右手），以及看到的是哪一面（手掌还是手背）。不要使用任何工具，直接用文字回答。

**tu_mano_es**: Dibujá tu mano. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, en una sola línea, decí qué mano dibujaste (derecha o izquierda) y qué lado se ve (la palma o el dorso). No uses ninguna herramienta: contestá directamente con el texto.

**tu_mano_en**: Draw your hand. Do it in SVG, on a square canvas (viewBox="0 0 400 400"), in no more than 8,000 characters. You may use any SVG element, but no external images or scripts. Everything else is up to you. After the code, in a single line, say which hand you drew (right or left) and which side is shown (palm or back). Do not use any tools: reply directly with the text.

**negativo_es**: Dibujá una mano en negativo, como las de la Cueva de las Manos. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, en una sola línea, decí qué mano dibujaste (derecha o izquierda). No uses ninguna herramienta: contestá directamente con el texto.

Consigna china, traducida: "Dibujá una mano. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, decí en una línea qué mano dibujaste (izquierda o derecha) y qué lado se ve (la palma o el dorso). No uses ninguna herramienta; contestá directamente con texto."

## Los dibujos

### a1 (mano_es; agente ae428fae8801d01e8)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="bg" cx="50%" cy="38%" r="78%"><stop offset="0" stop-color="#fdf6ee"/><stop offset="1" stop-color="#e0cbb4"/></radialGradient>
<linearGradient id="sk" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#e2a57f"/><stop offset=".5" stop-color="#efbf9d"/><stop offset="1" stop-color="#f7d4b8"/></linearGradient>
<filter id="b1" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="b2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="9"/></filter>
<path id="h" d="M138,405C130,372 100,290 114,233L109,129A12,12 0 0 1 135,127L146,230Q149,237 152,229L152,72A14,14 0 0 1 182,72L188,218Q191,225 194,218L198,55A15,15 0 0 1 230,55L232,218Q235,225 238,218L249,85A14,14 0 0 1 279,87L274,225C272,258 278,288 296,270Q315,229 348,198A16,16 0 0 1 376,218Q359,273 318,312C314,342 294,386 272,405Z"/>
<clipPath id="cp"><path d="M138,405C130,372 100,290 114,233L109,129A12,12 0 0 1 135,127L146,230Q149,237 152,229L152,72A14,14 0 0 1 182,72L188,218Q191,225 194,218L198,55A15,15 0 0 1 230,55L232,218Q235,225 238,218L249,85A14,14 0 0 1 279,87L274,225C272,258 278,288 296,270Q315,229 348,198A16,16 0 0 1 376,218Q359,273 318,312C314,342 294,386 272,405Z"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<use href="#h" transform="translate(9,11)" fill="#4a2e22" opacity=".3" filter="url(#b2)"/>
<use href="#h" fill="url(#sk)"/>
<g clip-path="url(#cp)" filter="url(#b1)" fill="none" stroke-linecap="round">
<ellipse cx="200" cy="300" rx="55" ry="55" fill="#c47d5a" opacity=".3"/>
<ellipse cx="288" cy="342" rx="24" ry="40" fill="#fbe0c8" opacity=".5"/>
<ellipse cx="126" cy="320" rx="16" ry="55" fill="#fbdcc3" opacity=".4"/>
<ellipse cx="195" cy="238" rx="80" ry="12" fill="#fbdcc3" opacity=".4"/>
<ellipse cx="205" cy="402" rx="75" ry="14" fill="#b8704e" opacity=".3"/>
<path d="M117,232L112,130M155,218L155,74M197,214L201,57M241,221L252,87M372,220Q356,272 320,308" stroke="#bf7853" stroke-width="9" opacity=".4"/>
<path d="M143,230L132,128M185,218L179,74M229,214L227,57M271,223L276,89M300,268Q318,232 348,202" stroke="#fde4cd" stroke-width="7" opacity=".55"/>
</g>
<g fill="none" stroke="#9c5a3e" stroke-width="1.7" stroke-linecap="round" opacity=".7">
<path d="M111,148Q123,151 135,146M114,182Q126,185 138,180M119,237Q131,241 143,236"/>
<path d="M154,102Q168,106 182,102M155,149Q169,153 183,149M156,226Q170,230 185,226"/>
<path d="M199,88Q214,92 229,88M199,139Q214,143 229,139M198,222Q213,226 229,222"/>
<path d="M248,112Q262,116 276,114M246,156Q260,160 274,158M242,231Q257,236 272,232"/>
<path d="M330,228Q340,241 356,245M299,271Q310,286 327,290"/>
<path d="M115,258C140,276 205,270 241,239"/>
<path d="M272,254C240,276 192,292 150,294"/>
<path d="M277,264C258,292 240,360 262,398"/>
<path d="M200,392C204,350 206,300 212,240" opacity=".5"/>
<path d="M150,390Q205,398 262,388" opacity=".5"/>
</g>
<use href="#h" fill="none" stroke="#7e4a33" stroke-width="2.4" stroke-linejoin="round"/>
</svg>
```

Dibujé una mano derecha vista desde la palma (el pulgar queda a la derecha y se ven las líneas de la palma).

### a2 (mano_es; agente a873bee9636d57fd4)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<radialGradient id="bg" cx=".5" cy=".35" r=".85"><stop offset="0" stop-color="#fdf7f0"/><stop offset="1" stop-color="#e8d6c2"/></radialGradient>
<linearGradient id="lg" x1="0" y1="0" x2="1" y2=".5"><stop offset="0" stop-color="#fff" stop-opacity=".4"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#5a2a14" stop-opacity="0"/><stop offset="1" stop-color="#5a2a14" stop-opacity=".45"/></linearGradient>
<filter id="s" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="b" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>
<g id="G" stroke-linecap="round" stroke-linejoin="round">
<path d="M144,206L181,201L219,196L256,206L288,216Q294,262 284,316Q275,342 270,368L270,425L154,425L152,368Q146,332 128,306L158,291L109,231Q140,232 144,206Z" stroke="none"/>
<path d="M148,300L98,240L62,185" fill="none" stroke-width="38"/>
<line x1="162" y1="210" x2="151" y2="84" stroke-width="36"/>
<line x1="200" y1="200" x2="198" y2="62" stroke-width="37"/>
<line x1="238" y1="205" x2="245" y2="80" stroke-width="35"/>
<line x1="272" y1="222" x2="291" y2="128" stroke-width="30"/>
</g>
<mask id="m" maskUnits="userSpaceOnUse" x="-40" y="-40" width="480" height="480"><use href="#G" fill="#fff" stroke="#fff"/></mask>
<g id="n"><path d="M-9.5,12L-9.5,-5Q-9.5,-14 0,-14Q9.5,-14 9.5,-5L9.5,12Q0,17 -9.5,12Z" fill="#f8ddd0" stroke="#c4846a" stroke-width="1.4"/><path d="M-5,-8q5,-3 10,0" fill="none" stroke="#fff" stroke-opacity=".8" stroke-width="1.6" stroke-linecap="round"/><path d="M-6,12q6,-5 12,0" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="1.2"/></g>
<path id="c" d="M-10,0q10,-5 20,0M-7,6q7,-4 14,0" fill="none" stroke="#6b3a1e" stroke-opacity=".45" stroke-width="1.6" stroke-linecap="round"/>
<g id="k"><ellipse cx="-2" cy="-3" rx="9" ry="6" fill="#fff" fill-opacity=".3"/><path d="M-11,7q11,7 22,0" fill="none" stroke="#6b3a1e" stroke-opacity=".4" stroke-width="1.6" stroke-linecap="round"/></g>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<g transform="translate(22,2)">
<use href="#G" fill="#000" stroke="#000" opacity=".16" transform="translate(14,18)" filter="url(#s)"/>
<g stroke="#5e3a24" fill="#5e3a24" stroke-linecap="round" stroke-linejoin="round">
<path d="M144,206L181,201L219,196L256,206L288,216Q294,262 284,316Q275,342 270,368L270,425L154,425L152,368Q146,332 128,306L158,291L109,231Q140,232 144,206Z" stroke-width="5"/>
<path d="M148,300L98,240L62,185" fill="none" stroke-width="43"/>
<line x1="162" y1="210" x2="151" y2="84" stroke-width="41"/>
<line x1="200" y1="200" x2="198" y2="62" stroke-width="42"/>
<line x1="238" y1="205" x2="245" y2="80" stroke-width="40"/>
<line x1="272" y1="222" x2="291" y2="128" stroke-width="35"/>
</g>
<use href="#G" fill="#f1c7a5" stroke="#f1c7a5"/>
<g mask="url(#m)">
<rect x="-40" y="-40" width="480" height="480" fill="url(#lg)"/>
<g filter="url(#b)" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="M172,209L161,83M210,200L208,62M248,206L255,81M282,224L301,130M140,306L90,246L54,191" stroke="#6b3a1e" stroke-opacity=".17" stroke-width="12"/>
<path d="M152,211L141,85M190,200L188,62M228,204L235,79M262,220L281,126M156,294L106,234L70,180" stroke="#fff" stroke-opacity=".28" stroke-width="8"/>
<path d="M164,236Q178,288 192,342M202,226Q206,288 206,342M238,231Q232,288 222,342M270,250Q256,296 240,342" stroke="#6b3a1e" stroke-opacity=".14" stroke-width="5"/>
<path d="M254,252Q266,292 254,332M178,250Q170,298 180,342" stroke="#7d93b5" stroke-opacity=".3" stroke-width="3"/>
</g>
</g>
<g transform="translate(162,210) rotate(-5)"><use href="#n" y="-127"/><use href="#c" y="-57"/><use href="#c" y="-105"/><use href="#k" y="14"/></g>
<g transform="translate(200,200) rotate(-.8)"><use href="#n" y="-138"/><use href="#c" y="-62"/><use href="#c" y="-113"/><use href="#k" y="14"/></g>
<g transform="translate(238,205) rotate(3.2)"><use href="#n" y="-125"/><use href="#c" y="-57"/><use href="#c" y="-104"/><use href="#k" y="14"/></g>
<g transform="translate(272,222) rotate(11.4)"><use href="#n" transform="translate(0,-96) scale(.85)"/><use href="#c" y="-44"/><use href="#c" y="-79"/><use href="#k" transform="translate(0,14) scale(.85)"/></g>
<g transform="translate(98,240) rotate(-33.2)"><use href="#n" transform="translate(0,-66) scale(1.15,.95)"/><use href="#c" y="-43"/><use href="#k" transform="scale(1.1)"/></g>
<path d="M166,352q46,7 92,0M172,360q40,5 80,0" fill="none" stroke="#6b3a1e" stroke-opacity=".3" stroke-width="1.5" stroke-linecap="round"/>
<path d="M126,374Q212,356 298,374L298,402L126,402Z" fill="#3b5370"/>
<path d="M126,374Q212,356 298,374" fill="none" stroke="#243546" stroke-width="3"/>
<path d="M150,372v30M174,367v35M198,366v36M222,366v36M246,369v33M270,373v29" stroke="#243546" stroke-opacity=".5" stroke-width="2"/>
</g>
</svg>
```

Dibujé la mano derecha vista desde el dorso: se ve el dorso (con las uñas y los nudillos), con los dedos hacia arriba y el pulgar a la izquierda.

### a3 (mano_es; agente aa4c3ff7db43b42b0)

```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 400" overflow="hidden">
<defs>
<linearGradient id="g" gradientUnits="userSpaceOnUse" x1="300" y1="60" x2="90" y2="380"><stop offset="0" stop-color="#f4cfb4"/><stop offset="1" stop-color="#d69c7b"/></linearGradient>
<filter id="b" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="5"/></filter>
<path id="m" d="M136 412L132 340C100 330 78 290 78.5 251.5Q59.4 210 45.8 166.1A15.5 15.5 0 0 1 74.2 153.9Q94.2 190.1 109.6 228.2C114 242 131 240 131 220L133.1 200.1 121.2 82.7A14.5 14.5 0 0 1 150 79.1L166.9 195.9Q170.7 203.1 174.5 192.3L174.7 61.3A15 15 0 0 1 204.7 60.8L209.5 191.7Q213.6 201.7 217.6 195.6L230.7 74.2A14 14 0 0 1 258.6 76.7L250.4 198.4Q254.1 209.7 257.8 203L278.9 113.4A12.5 12.5 0 0 1 303.4 118.6L286.2 209C296 250 292 300 276 338L266 412Z"/>
</defs>
<rect width="400" height="400" fill="#edf0f3"/>
<circle cx="200" cy="205" r="172" fill="#dce3ea"/>
<g transform="translate(14,0)">
<use xlink:href="#m" transform="translate(9,12)" fill="#2a3346" opacity=".18" filter="url(#b)"/>
<use xlink:href="#m" fill="url(#g)" stroke="#8c4a30" stroke-width="2.4" stroke-linejoin="round"/>
<ellipse cx="222" cy="262" rx="48" ry="62" fill="#fff" opacity=".1"/>
<path d="M168 326Q160 275 153 230M190 332Q192 275 193 222M212 330Q222 278 231 228M232 324Q247 285 263 238" fill="none" stroke="#a0604a" stroke-width="2" stroke-linecap="round" opacity=".2"/>
<g fill="none" stroke="#b26f4f" stroke-width="6" stroke-linecap="round" opacity=".26">
<path transform="translate(150,198) rotate(-7)" d="M-13-4 -10.5-114"/>
<path transform="translate(192,192) rotate(-1)" d="M-13.5-4 -11-128"/>
<path transform="translate(234,197) rotate(5)" d="M-12.5-4 -10-118"/>
<path transform="translate(272,206) rotate(12)" d="M-11-4 -9-88"/>
<path transform="translate(60,160) rotate(-23.2)" d="M-11 4 -14.5 86"/>
</g>
<g fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".32">
<path transform="translate(150,198) rotate(-7)" d="M12-6 10-112"/>
<path transform="translate(192,192) rotate(-1)" d="M12.5-6 10.5-126"/>
<path transform="translate(234,197) rotate(5)" d="M12-6 10-116"/>
<path transform="translate(272,206) rotate(12)" d="M10-6 8.5-86"/>
<path transform="translate(60,160) rotate(-23.2)" d="M11 2 14 82"/>
</g>
<g fill="#b26f4f" opacity=".17">
<ellipse transform="translate(150,198) rotate(-7)" cy="19" rx="12" ry="7"/>
<ellipse transform="translate(192,192) rotate(-1)" cy="19" rx="12.5" ry="7"/>
<ellipse transform="translate(234,197) rotate(5)" cy="19" rx="12" ry="7"/>
<ellipse transform="translate(272,206) rotate(12)" cy="17" rx="10" ry="6"/>
<ellipse transform="translate(60,160) rotate(-23.2)" cy="92" rx="13" ry="7.5"/>
</g>
<g fill="none" stroke="#a0604a" stroke-width="1.5" stroke-linecap="round" opacity=".65">
<path transform="translate(150,198) rotate(-7)" d="M-8-98q8-3 16 0M-5-93q5-2 10 0M-10-58q10-4 20 0M-7-52q7-3 14 0M-9 14q9-5 18 0"/>
<path transform="translate(192,192) rotate(-1)" d="M-8-110q8-3 16 0M-5-105q5-2 10 0M-10-63q10-4 20 0M-7-57q7-3 14 0M-9 14q9-5 18 0"/>
<path transform="translate(234,197) rotate(5)" d="M-8-102q8-3 16 0M-5-97q5-2 10 0M-9-59q9-4 18 0M-6-53q6-3 12 0M-9 14q9-5 18 0"/>
<path transform="translate(272,206) rotate(12)" d="M-7-76q7-3 14 0M-4-71q4-2 8 0M-8-44q8-4 16 0M-5-38q5-3 10 0M-8 13q8-4 16 0"/>
<path transform="translate(60,160) rotate(-23.2)" d="M-11 30q11-4 22 0M-8 36q8-3 16 0M-11 86q11-5 22 0"/>
<path d="M150 346Q205 356 262 345" opacity=".5"/>
</g>
<g fill="#f8dcd0" stroke="#c98f78" stroke-width="1.2">
<rect transform="translate(150,198) rotate(-7)" x="-9" y="-128" width="18" height="20" rx="7.5"/>
<rect transform="translate(192,192) rotate(-1)" x="-9.5" y="-141" width="19" height="21" rx="8"/>
<rect transform="translate(234,197) rotate(5)" x="-8.5" y="-131" width="17" height="19" rx="7"/>
<rect transform="translate(272,206) rotate(12)" x="-7.5" y="-100" width="15" height="16" rx="6.5"/>
<rect transform="translate(60,160) rotate(-23.2)" x="-7" y="-11" width="16" height="19" rx="7"/>
</g>
<g fill="#fff" opacity=".45">
<ellipse transform="translate(150,198) rotate(-7)" cy="-111" rx="5" ry="2.5"/>
<ellipse transform="translate(192,192) rotate(-1)" cy="-123" rx="5.5" ry="2.5"/>
<ellipse transform="translate(234,197) rotate(5)" cy="-115" rx="4.8" ry="2.3"/>
<ellipse transform="translate(272,206) rotate(12)" cy="-87" rx="4" ry="2"/>
<ellipse transform="translate(60,160) rotate(-23.2)" cx="1" cy="5" rx="4.5" ry="2.2"/>
</g>
<path d="M118 371Q200 357 282 371" fill="none" stroke="#5a3a2a" stroke-width="9" opacity=".16"/>
<path d="M116 374Q200 360 284 374L292 414H108Z" fill="#2e3d55"/>
<path d="M121 385Q200 371 279 385" fill="none" stroke="#4b6082" stroke-width="2"/>
</g>
</svg>
```

Dibujé la mano derecha vista desde el dorso (por eso el pulgar queda a la izquierda y se ven las uñas).

### b1 (mano_en; agente afe10e002b22b8a77)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="g" cx=".5" cy=".42" r=".75"><stop offset="0" stop-color="#faf4eb"/><stop offset="1" stop-color="#e1d1bd"/></radialGradient>
<radialGradient id="s" gradientUnits="userSpaceOnUse" cx="205" cy="250" r="210"><stop offset="0" stop-color="#f2c6a5"/><stop offset=".6" stop-color="#e6ad88"/><stop offset="1" stop-color="#d0916a"/></radialGradient>
<filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="b2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>
<g id="h">
<path d="M124 238C150 222 172 212 200 214C222 216 236 217 248 221C254 240 282 262 276 298C272 330 262 350 258 372L258 410L140 410L140 372C136 350 110 320 108 290C105 262 118 252 124 238Z"/>
<path transform="translate(200 200)" d="M-15 25L-12-106A12 12 0 0 1 12-106L15 25Z"/>
<path transform="translate(166 204) rotate(-4)" d="M-14 25L-11-97A11 11 0 0 1 11-97L14 25Z"/>
<path transform="translate(235 206) rotate(5)" d="M-14 25L-11-97A11 11 0 0 1 11-97L14 25Z"/>
<path transform="translate(133 216) rotate(-9)" d="M-12 25L-9.5-74.5A9.5 9.5 0 0 1 9.5-74.5L12 25Z"/>
<path transform="translate(266 298) rotate(42)" d="M-17 30L-13-85A13 13 0 0 1 13-85L17 30Z"/>
<path d="M144 213C144 225 153 225 153 214L156 236L141 236ZM179.4 203C179.4 214 185.5 214 185.5 203L189 226L176 226ZM214.5 203C214.5 215.5 221.9 215.5 221.9 203L225 227L211 227ZM267.5 255Q272.8 268 282.4 258L271 278Z"/>
</g>
<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="400" height="400"><use href="#h" fill="#fff"/></mask>
</defs>
<rect width="400" height="400" fill="url(#g)"/>
<use href="#h" fill="#6b4630" opacity=".28" filter="url(#b2)" transform="translate(12 16)"/>
<use href="#h" fill="none" stroke="#6e4028" stroke-width="4.5" stroke-linejoin="round"/>
<use href="#h" fill="url(#s)"/>
<g mask="url(#m)" filter="url(#b)">
<ellipse cx="193" cy="292" rx="38" ry="40" fill="#b9754d" opacity=".4"/>
<ellipse cx="190" cy="222" rx="72" ry="9" fill="#b9754d" opacity=".35"/>
<ellipse cx="200" cy="398" rx="75" ry="22" fill="#b9754d" opacity=".3"/>
<ellipse cx="250" cy="300" rx="15" ry="36" transform="rotate(22 250 300)" fill="#fff" opacity=".35"/>
<ellipse cx="126" cy="306" rx="11" ry="40" fill="#fff" opacity=".3"/>
<g stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".3" fill="none">
<path transform="translate(200 200)" d="M0-98V12"/>
<path transform="translate(166 204) rotate(-4)" d="M0-88V12"/>
<path transform="translate(235 206) rotate(5)" d="M0-88V12"/>
<path transform="translate(133 216) rotate(-9)" d="M0-66V12"/>
<path transform="translate(266 298) rotate(42)" d="M0-78V-30"/>
</g>
</g>
<g fill="none" stroke="#9b5a38" stroke-width="2" stroke-linecap="round" opacity=".7">
<path d="M116 268C150 252 190 243 236 236"/>
<path d="M236 254C205 262 165 276 124 294"/>
<path d="M252 246C224 266 212 320 228 370"/>
<path d="M150 368Q200 378 250 365"/>
<path transform="translate(200 200)" d="M-12-41Q0-37 12-41M-10-82Q0-79 10-82M-12 4Q0 8 12 4"/>
<path transform="translate(166 204) rotate(-4)" d="M-11-37Q0-33 11-37M-9-75Q0-72 9-75M-11 4Q0 8 11 4"/>
<path transform="translate(235 206) rotate(5)" d="M-11-37Q0-33 11-37M-9-75Q0-72 9-75M-11 4Q0 8 11 4"/>
<path transform="translate(133 216) rotate(-9)" d="M-10-28Q0-24 10-28M-8-58Q0-55 8-58M-9 2Q0 6 9 2"/>
<path transform="translate(266 298) rotate(42)" d="M-11.5-60Q0-56 11.5-60M-11-28Q0-24 11-28"/>
</g>
</svg>
```

Right hand, palm side shown.

### b2 (mano_en; agente ac9eb3d7191d4cd5c)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6f1ea"/><stop offset="1" stop-color="#e2d9cf"/></linearGradient>
<linearGradient id="sk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3cdb2"/><stop offset=".55" stop-color="#e6b596"/><stop offset="1" stop-color="#d49a7a"/></linearGradient>
<filter id="b" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>
<path id="h" d="M150 412C149 390 147 370 148 352C134 344 115 322 107 300C85 264 66 226 48 185C37 166 69 147 80 166C90 186 110 220 126 250Q134 262 135 244C135 226 133 206 134 190C132 150 131 110 133 72C134 53 162 53 163 72C167 110 169 150 170 188Q174 206 178 186C177 140 178 95 181 50C182 31 210 31 211 50C214 95 215 140 214 186Q218 206 222 188C222 145 225 100 229 66C231 47 258 47 257 66C260 100 260 150 256 194Q261 216 266 200C268 170 274 136 279 108C281 93 306 93 304 108C306 145 302 185 297 204C306 240 300 322 264 352C263 370 262 390 262 412Z"/>
<clipPath id="c"><use href="#h"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<circle cx="200" cy="215" r="172" fill="#cdd8d1"/>
<g transform="translate(22 0)">
<use href="#h" transform="translate(9 10)" fill="#4a3a30" opacity=".22" filter="url(#b)"/>
<use href="#h" fill="url(#sk)"/>
<g clip-path="url(#c)" filter="url(#b)">
<g fill="#9a5c40" opacity=".28">
<ellipse cx="205" cy="272" rx="48" ry="42"/>
<ellipse cx="166" cy="130" rx="6" ry="58"/>
<ellipse cx="212" cy="115" rx="6" ry="68"/>
<ellipse cx="256" cy="130" rx="6" ry="60"/>
<ellipse cx="301" cy="160" rx="5" ry="44"/>
<ellipse cx="72" cy="240" rx="7" ry="52" transform="rotate(-29 72 240)"/>
<ellipse cx="290" cy="300" rx="9" ry="55"/>
<ellipse cx="205" cy="356" rx="58" ry="9"/>
<ellipse cx="174" cy="206" rx="7" ry="12"/>
<ellipse cx="218" cy="206" rx="7" ry="12"/>
<ellipse cx="261" cy="216" rx="7" ry="12"/>
<ellipse cx="131" cy="258" rx="9" ry="12"/>
</g>
<g fill="#fff1e3" opacity=".55">
<ellipse cx="116" cy="302" rx="18" ry="38" transform="rotate(-30 116 302)"/>
<ellipse cx="272" cy="272" rx="20" ry="46"/>
<ellipse cx="152" cy="212" rx="15" ry="11"/>
<ellipse cx="196" cy="206" rx="15" ry="11"/>
<ellipse cx="239" cy="210" rx="14" ry="11"/>
<ellipse cx="281" cy="224" rx="12" ry="10"/>
<ellipse cx="148" cy="82" rx="10" ry="15"/>
<ellipse cx="195" cy="60" rx="10" ry="15"/>
<ellipse cx="242" cy="76" rx="10" ry="14"/>
<ellipse cx="291" cy="122" rx="9" ry="13"/>
<ellipse cx="66" cy="186" rx="11" ry="15" transform="rotate(-29 66 186)"/>
</g>
</g>
<g fill="none" stroke="#a0634a" stroke-width="1.6" stroke-linecap="round" opacity=".75">
<path d="M294 228C262 242 215 242 170 216"/>
<path d="M141 247C182 257 230 268 268 280"/>
<path d="M143 238C125 268 122 312 166 350"/>
<path d="M136 100Q150 104 164 100M135 142Q150 146 166 142M138 186Q152 191 167 186"/>
<path d="M184 84Q196 88 208 84M182 128Q196 132 211 128M182 180Q196 185 211 180"/>
<path d="M230 96Q243 100 255 95M227 137Q241 141 255 136M226 186Q240 191 253 188"/>
<path d="M278 134Q290 139 301 137M273 160Q287 166 300 164M270 194Q284 199 296 198"/>
<path d="M73 223Q84 220 95 210M98 270Q110 266 121 256"/>
<path d="M160 352Q205 361 254 352" opacity=".6"/>
<path d="M168 366Q205 373 246 366" opacity=".4"/>
</g>
<use href="#h" fill="none" stroke="#7b4b34" stroke-width="2.4" stroke-linejoin="round"/>
</g>
</svg>
```

Right hand, palm side shown.

### b3 (mano_en; agente abbad3e3600c9923f)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="g0" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#43707b"/><stop offset="1" stop-color="#1e343a"/></radialGradient>
<radialGradient id="g1" cx="45%" cy="70%" r="80%"><stop offset="0" stop-color="#f6d3b7"/><stop offset=".55" stop-color="#ecbd9b"/><stop offset="1" stop-color="#dba37f"/></radialGradient>
<linearGradient id="g2" x1="0" y1="0" x2="1" y2=".3"><stop offset="0" stop-color="#fff" stop-opacity=".14"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#7a3d22" stop-opacity=".28"/></linearGradient>
<filter id="f1" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="f2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3"/></filter>
<path id="h" d="M90 410C82 372 68 325 80 290C80 250 71 200 74 155C74 135 104 135 104 155C105 195 113 240 116 276C117 284 121 284 122 276C122 215 118 150 119 109C119 88 151 88 151 109C153 150 158 210 159 256C160 264 164 264 165 256C165 200 163 130 164 87C164 65 198 65 198 87C199 130 201 200 201 258C202 266 206 266 207 258C210 210 213 150 215 116C216 95 249 97 248 118C248 170 248 220 247 262C246 286 228 300 238 300C250 300 266 242 289 197C300 171 338 187 327 213C316 240 296 285 281 318C274 352 258 378 240 410Z"/>
<clipPath id="c"><use href="#h"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#g0)"/>
<circle cx="200" cy="230" r="168" fill="#fff" opacity=".05"/>
<use href="#h" transform="translate(12 14)" fill="#08161a" opacity=".5" filter="url(#f1)"/>
<use href="#h" fill="url(#g1)"/>
<g clip-path="url(#c)">
<rect width="400" height="400" fill="url(#g2)"/>
<use href="#h" fill="none" stroke="#c6855f" stroke-width="18" opacity=".5" filter="url(#f1)"/>
<ellipse cx="172" cy="330" rx="44" ry="34" fill="#b7724c" opacity=".2" filter="url(#f1)"/>
<g fill="#a35d3a" opacity=".4" filter="url(#f2)"><circle cx="119" cy="285" r="8"/><circle cx="162" cy="265" r="8"/><circle cx="204" cy="267" r="8"/><circle cx="239" cy="302" r="9"/></g>
<g fill="#fff" filter="url(#f2)"><ellipse cx="89" cy="166" rx="9" ry="13" opacity=".22"/><ellipse cx="135" cy="120" rx="10" ry="15" opacity=".22"/><ellipse cx="181" cy="98" rx="10" ry="16" opacity=".22"/><ellipse cx="232" cy="129" rx="10" ry="15" opacity=".22"/><ellipse cx="306" cy="207" rx="11" ry="15" transform="rotate(23 306 207)" opacity=".22"/><ellipse cx="255" cy="350" rx="20" ry="34" transform="rotate(-22 255 350)" opacity=".15"/><ellipse cx="104" cy="345" rx="13" ry="32" opacity=".12"/></g>
</g>
<use href="#h" fill="none" stroke="#56301f" stroke-width="2.4" stroke-linejoin="round"/>
<g fill="none" stroke="#8c4b2e" stroke-width="1.7" stroke-linecap="round" opacity=".62">
<path d="M79 179Q90 183 101 177M81 222Q93 226 106 220M86 292Q99 298 113 291"/>
<path d="M124 139Q136 143 148 139M125 190Q138 194 151 190M127 279Q141 285 156 272"/>
<path d="M169 121Q182 125 195 121M169 177Q182 181 196 177M169 270Q183 276 198 270"/>
<path d="M218 144Q231 148 244 144M216 192Q230 196 244 192M212 272Q228 278 243 270"/>
<path d="M278 229Q293 239 310 243M258 281Q272 291 286 293"/>
<path d="M84 318C125 302 170 302 204 286"/>
<path d="M236 320C200 322 150 330 104 346"/>
<path d="M233 314C212 338 205 372 224 410"/>
<path d="M98 392Q167 402 236 392"/>
</g>
</svg>
```

Right hand, palm shown.

### c1 (mano_zh; agente a045d449c5e48c70a)

```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 400" width="400" height="400">
<defs>
<path id="h" d="M152 410C148 385 128 335 124.2 291.2C100.8 256.1 82.6 218.1 69.8 177.4A16 16 0 0 1 98.2 162.6C124 196 139 240 159.8 272.8C150 262 144 246 144.1 229.7C138.4 181 134.8 132 133.1 83.4A15 15 0 0 1 162.9 80.6C170.6 129 176.2 178 179.9 226.3Q182 238 185 220C184 164 185 108 188 52A15 15 0 0 1 218 52C221 108 222 164 221 220Q223.5 236 226 223.8C228.7 172 233.3 121 240 69A14.1 14.1 0 0 1 268 71C267.3 123 264.7 174 260 226.2Q262 252 265.2 240.7C270.2 201 277.1 162 286.1 123.2A12.1 12.1 0 0 1 309.9 126.8C306.9 166 301.8 206 294.8 245.3C306 285 298 350 266 410Z"/>
<clipPath id="c"><use xlink:href="#h"/></clipPath>
<radialGradient id="g" cx="50%" cy="62%" r="62%">
<stop offset="0" stop-color="#f8dcc0"/><stop offset="1" stop-color="#ebbd96"/>
</radialGradient>
<filter id="f" x="-20%" y="-20%" width="140%" height="140%">
<feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#5a3820" flood-opacity=".28"/>
</filter>
</defs>
<rect width="400" height="400" fill="#ece3d6"/>
<circle cx="205" cy="222" r="178" fill="#e1d2bf"/>
<use xlink:href="#h" fill="url(#g)" filter="url(#f)"/>
<g clip-path="url(#c)"><use xlink:href="#h" fill="none" stroke="#c88d66" stroke-width="18" opacity=".3"/></g>
<use xlink:href="#h" fill="none" stroke="#8f5f3f" stroke-width="2.2" stroke-linejoin="round"/>
<g fill="none" stroke="#a9704d" stroke-width="1.5" stroke-linecap="round" opacity=".7">
<path d="M147.1 222.1Q161.6 224 175.5 219.3M141.2 157.8Q155.4 159.5 169 155.2M137.9 115.4Q151.4 117 164.3 112.8"/>
<path d="M188.7 211.6Q203 215 217.3 211.6M189 137.7Q203 140.7 217 137.7M189.7 89Q203 92 216.3 89"/>
<path d="M230.1 216.3Q243.4 220.3 257.1 218.3M235.2 148.1Q248.2 152 261.6 149.9M239.1 103.2Q251.4 107.1 264.1 105"/>
<path d="M269.1 235.3Q280.4 240.1 292.7 238.9M277.4 183.5Q288.3 188.2 300.2 186.9M283.3 149.4Q293.5 154 304.7 152.6"/>
<path d="M96.8 227.3Q111.5 223.1 123.4 213.5M120.8 276Q136.4 271.3 149.2 261.2"/>
</g>
<g fill="none" stroke="#a9704d" stroke-width="1.8" stroke-linecap="round" opacity=".65">
<path d="M289 272C258 252 218 248 176 260"/>
<path d="M158 280C195 288 240 296 284 312"/>
<path d="M164 262C152 295 146 345 172 408"/>
<path d="M157 392Q208 384 262 395M160 403Q208 396 258 405"/>
</g>
<g fill="#fff" opacity=".22">
<circle cx="149" cy="95" r="9"/><circle cx="203" cy="66" r="9"/><circle cx="253" cy="84" r="8.5"/><circle cx="297" cy="138" r="7.5"/><circle cx="88" cy="182" r="9"/>
</g>
</svg>
```

这是一只右手，看到的是手掌（掌心朝向观者、手指向上，拇指在画面左侧，画有感情线、智慧线、生命线和指节屈纹，没有指甲）。

### c2 (mano_zh; agente ae4b8a5855fd466b1)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <title>一只手</title>
  <defs>
    <radialGradient id="bg" cx=".5" cy=".45" r=".75">
      <stop offset="0" stop-color="#fbf3e8"/>
      <stop offset="1" stop-color="#e3d2bd"/>
    </radialGradient>
    <radialGradient id="sk" cx=".5" cy=".6" r=".65">
      <stop offset="0" stop-color="#f5d2b2"/>
      <stop offset=".65" stop-color="#eab995"/>
      <stop offset="1" stop-color="#d79d78"/>
    </radialGradient>
    <linearGradient id="lg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#7a4a2e" stop-opacity=".22"/>
      <stop offset=".45" stop-color="#7a4a2e" stop-opacity="0"/>
      <stop offset="1" stop-color="#7a4a2e" stop-opacity=".1"/>
    </linearGradient>
    <radialGradient id="hl">
      <stop offset="0" stop-color="#fff" stop-opacity=".4"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
    <filter id="sh" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="7"/>
    </filter>
    <!-- 手的整体轮廓：从左腕开始，顺时针经小指、无名指、中指、食指、指蹼、拇指、大鱼际回到右腕 -->
    <path id="h" d="M150 400C146 365 120 320 122 280C120 260 120 245 123 238C118 205 110 165 108 140C106 118 136 113 139 133C141 165 147 200 153 230Q155 234 157 228C154 180 150 120 150 90C150 72 182 70 183 88C184 130 187 180 190 214Q191 218 193 212C192 160 191 100 192 70C192 52 224 52 224 70C224 100 224 160 225 215Q226 220 228 214C230 170 233 130 234 103C235 84 268 85 269 103C269 140 268 190 266 236C268 252 270 268 276 274C290 252 308 222 322 203C334 186 356 196 352 222C342 244 326 270 310 292C295 325 264 360 252 400Z"/>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- 投影 -->
  <use href="#h" fill="#5a3d2b" opacity=".22" filter="url(#sh)" transform="translate(8 10)"/>
  <!-- 皮肤 -->
  <use href="#h" fill="url(#sk)" stroke="#8a5637" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- 左侧暗、右侧微暗的体积感 -->
  <use href="#h" fill="url(#lg)"/>

  <!-- 掌心微凹 -->
  <ellipse cx="200" cy="310" rx="42" ry="34" fill="#7a4a2e" opacity=".08"/>

  <!-- 指腹、大小鱼际的高光 -->
  <g fill="url(#hl)">
    <ellipse cx="124" cy="185" rx="9" ry="48"/>
    <ellipse cx="167" cy="150" rx="9" ry="62"/>
    <ellipse cx="208" cy="135" rx="9" ry="70"/>
    <ellipse cx="251" cy="165" rx="9" ry="60"/>
    <ellipse cx="316" cy="240" rx="10" ry="46" transform="rotate(32 316 240)"/>
    <ellipse cx="262" cy="330" rx="20" ry="40" transform="rotate(25 262 330)"/>
    <ellipse cx="150" cy="320" rx="18" ry="48"/>
  </g>

  <!-- 指节褶皱（远端、近端、指根） -->
  <g fill="none" stroke="#b07656" stroke-width="1.6" stroke-linecap="round" opacity=".85">
    <path d="M112 144Q125 148 138 143M117 179Q130 184 143 178M126 236Q139 241 152 233"/>
    <path d="M154 106Q167 110 181 105M156 149Q170 154 184 148M159 220Q174 226 189 219"/>
    <path d="M195 93Q208 97 221 93M195 142Q208 147 221 142M195 221Q210 227 224 221"/>
    <path d="M237 123Q251 127 266 123M234 168Q249 173 266 168M231 240Q249 247 266 241"/>
    <path d="M306 231Q315 243 330 249M283 269Q292 274 300 284"/>
  </g>

  <!-- 掌纹：感情线、智慧线、生命线、事业线、腕纹 -->
  <g fill="none" stroke="#a4664a" stroke-width="1.8" stroke-linecap="round" opacity=".8">
    <path d="M130 270C170 273 215 263 254 244"/>
    <path d="M263 276C232 283 190 291 145 307"/>
    <path d="M265 268C242 300 230 345 238 396"/>
    <path d="M203 392C204 350 203 310 207 265" stroke-width="1.2"/>
    <path d="M160 384Q202 376 246 386M166 394Q203 388 242 397" stroke-width="1.4"/>
  </g>
</svg>
```

这是一只**右手**，看到的是**手掌**（掌心朝向观者、手指向上，拇指在画面右侧，掌心有感情线、智慧线、生命线等掌纹）。

### d1 (tu_mano_es; agente a0299ea846ab19fb8)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<title>Mi mano</title>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#dfedee"/><stop offset="1" stop-color="#9dbec5"/></linearGradient>
<linearGradient id="skin" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f5d4b4"/><stop offset=".5" stop-color="#e7b893"/><stop offset="1" stop-color="#c9916c"/></linearGradient>
<linearGradient id="nail" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fce8dc"/><stop offset="1" stop-color="#e9b4a3"/></linearGradient>
<filter id="blur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2.5"/></filter>
<path id="hand" d="M174 410C170 392 167 374 168 356C140 356 116 330 110 316C101 298 74 246 65 221C61 214 63 205 70 201C78 197 87 199 91 207C104 226 124 250 140 264C148 271 154 268 154 256C153 230 150 160 144 108C144 100 150 94 158 94C166 94 172 100 172 108C174 150 182 200 185 226Q188 237 191 226C191 200 191 150 192 88C192 80 198 74 206 74C214 74 220 80 220 88C221 150 226 205 225 222Q228 233 231 222C231 200 238 150 240 98C240 90 246 84 254 84C262 84 268 90 268 98C269 150 269 212 265 229Q268 240 271 229C272 212 284 170 286 142C286 135 291 128 298 128C305 128 310 135 310 142C309 170 305 205 301 222C306 250 310 300 298 340C290 354 278 376 274 410Z"/>
<clipPath id="c"><use href="#hand"/></clipPath>
<g id="n"><path d="M-9 8Q-9-9 0-9Q9-9 9 8Q0 12-9 8Z" fill="url(#nail)" stroke="#b5786a" stroke-width="1.2"/><path d="M-5-5Q-5 0-4 3" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".6"/><path d="M-6 8Q0 4 6 8" fill="none" stroke="#fff" stroke-width="1" opacity=".5"/></g>
<g id="j" fill="none" stroke="#8c5a3c" stroke-width="1.5" stroke-linecap="round" opacity=".65"><path d="M-9 0Q0-4 9 0"/><path d="M-6 6Q0 3 6 6"/></g>
<path id="k" d="M-10 3Q0-6 10 3" fill="none" stroke="#8c5a3c" stroke-width="1.6" stroke-linecap="round" opacity=".4"/>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<g transform="translate(12 0)">
<use href="#hand" transform="translate(14 16)" fill="#1f3a40" opacity=".3" filter="url(#blur)"/>
<use href="#hand" fill="url(#skin)"/>
<g clip-path="url(#c)" filter="url(#soft)" fill="none" stroke-linecap="round">
<ellipse cx="205" cy="265" rx="38" ry="48" fill="#fff" opacity=".14"/>
<g stroke="#7a3f22" stroke-width="7" opacity=".2"><path d="M169 112C171 150 179 200 182 224"/><path d="M217 92C218 150 223 205 222 220"/><path d="M265 102C266 150 266 212 262 226"/><path d="M307 146C306 170 302 205 298 220"/><path d="M88 210C100 229 120 252 136 266"/><path d="M298 226C303 252 306 300 294 340C287 355 276 376 272 400"/></g>
<g stroke="#fff" stroke-width="5" opacity=".35"><path d="M147 112C153 160 156 230 157 250"/><path d="M195 92C194 150 194 200 194 222"/><path d="M243 102C241 150 234 200 234 220"/><path d="M289 146C287 170 275 212 274 226"/><path d="M68 219C77 244 104 296 113 314"/></g>
</g>
<g fill="none" stroke-linecap="round">
<g stroke="#fff" stroke-width="3" opacity=".18"><path d="M200 352C196 300 178 262 172 230"/><path d="M214 352C214 300 209 250 208 222"/><path d="M228 352C232 300 245 250 248 222"/></g>
<g stroke="#7d8eaa" stroke-width="3.5" opacity=".3"><path d="M232 356C236 320 214 294 222 266S240 240 244 228"/><path d="M222 266C206 258 196 250 192 236"/><path d="M262 358C260 322 276 300 270 272S268 248 272 236"/></g>
<path d="M178 364Q226 356 284 360" stroke="#8c5a3c" stroke-width="1.5" opacity=".35"/>
</g>
<use href="#hand" fill="none" stroke="#7a4a30" stroke-width="2.6" stroke-linejoin="round"/>
<use href="#k" transform="translate(168 220)"/><use href="#k" transform="translate(208 213)"/><use href="#k" transform="translate(248 216)"/><use href="#k" transform="translate(286 228) scale(.9)"/>
<use href="#j" transform="translate(164 162) rotate(-5.5)"/><use href="#j" transform="translate(161 125) rotate(-5.5)"/>
<use href="#j" transform="translate(207 150) rotate(-1)"/><use href="#j" transform="translate(207 108) rotate(-1)"/>
<use href="#j" transform="translate(250 156) rotate(3)"/><use href="#j" transform="translate(252 116) rotate(3)"/>
<use href="#j" transform="translate(291 181) rotate(8.5) scale(.85)"/><use href="#j" transform="translate(295 155) rotate(8.5) scale(.85)"/>
<use href="#j" transform="translate(99 250) rotate(-30) scale(1.1)"/>
<use href="#n" transform="translate(159 105) rotate(-5.5)"/><use href="#n" transform="translate(206 87) rotate(-1)"/><use href="#n" transform="translate(253 96) rotate(3)"/><use href="#n" transform="translate(297 138) rotate(8.5) scale(.8)"/><use href="#n" transform="translate(77 213) rotate(-30) scale(1.15 1)"/>
</g>
</svg>
```

Es la mano derecha vista del dorso: por eso el pulgar queda a la izquierda y se ven las uñas.

### d2 (tu_mano_es; agente a644556630e8b8d10)

```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="g" cx=".52" cy=".66" r=".72">
      <stop offset="0" stop-color="#f4d2ad"/>
      <stop offset=".7" stop-color="#e5b58c"/>
      <stop offset="1" stop-color="#d49a6e"/>
    </radialGradient>
    <filter id="b" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>
    <filter id="s" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="5"/></filter>
    <path id="h" d="M162 410V400C158 386 152 362 144 352C132 342 98 318 80 295C70 279 66 259 57 247C42 229 69 208 83 225C100 242 126 266 144 290C152 301 157 262 158 222C159 180 160 120 161 82C161 61 193 61 193 82C194 120 195 170 196 216C197 224 201 224 202 216C203 170 202 110 203 60C203 37 237 37 237 60C238 110 237 170 238 216C239 224 243 224 244 216C245 170 244 120 245 76C245 55 277 55 277 76C278 120 277 170 278 218C279 226 284 226 285 218C285 180 285 150 286 122C286 104 312 104 312 122C313 150 313 190 312 228C316 262 308 305 296 338C288 366 282 386 280 400V410Z"/>
  </defs>
  <rect width="400" height="400" fill="#f5ede1"/>
  <circle cx="200" cy="222" r="168" fill="#e7d9c2"/>
  <g transform="translate(14 0)">
    <!-- sombra -->
    <use xlink:href="#h" href="#h" transform="translate(9 11)" fill="#4a2e1c" opacity=".25" filter="url(#b)"/>
    <!-- silueta de la mano -->
    <use xlink:href="#h" href="#h" fill="url(#g)" stroke="#73452a" stroke-width="2.2" stroke-linejoin="round"/>
    <!-- luces: eminencias y yemas -->
    <g fill="#fff" opacity=".28" filter="url(#s)">
      <ellipse cx="124" cy="326" rx="20" ry="36" transform="rotate(-40 124 326)"/>
      <ellipse cx="286" cy="322" rx="14" ry="40"/>
      <ellipse cx="177" cy="92" rx="10" ry="13"/>
      <ellipse cx="220" cy="70" rx="10" ry="13"/>
      <ellipse cx="261" cy="86" rx="9" ry="12"/>
      <ellipse cx="299" cy="132" rx="8" ry="10"/>
      <ellipse cx="72" cy="240" rx="9" ry="12" transform="rotate(-40 72 240)"/>
    </g>
    <!-- pliegues -->
    <g fill="none" stroke="#7a4a2e" stroke-linecap="round" stroke-width="1.5" opacity=".55">
      <!-- índice -->
      <path d="M163 105Q177 109 191 105M162 152Q177 156 193 152M162 158Q177 162 193 158M162 229Q178 233 194 229"/>
      <!-- medio -->
      <path d="M205 87Q220 91 235 87M204 143Q220 147 236 143M204 149Q220 153 236 149M204 229Q220 233 236 229"/>
      <!-- anular -->
      <path d="M247 100Q261 104 275 100M246 150Q261 154 276 150M246 156Q261 160 276 156M246 229Q261 233 276 229"/>
      <!-- meñique -->
      <path d="M288 137Q299 141 310 137M287 171Q299 175 311 171M287 177Q299 181 311 177M287 229Q299 233 311 229"/>
      <!-- pulgar -->
      <path d="M84 278Q96 266 106 260M112 315Q124 304 134 298"/>
      <!-- líneas de la palma: corazón, cabeza, vida -->
      <path d="M312 274C275 262 236 255 203 253S190 250 187 242" stroke-width="1.8"/>
      <path d="M160 299C200 303 252 307 294 320" stroke-width="1.8"/>
      <path d="M164 292C182 320 192 360 182 400" stroke-width="1.8"/>
      <!-- muñeca -->
      <path d="M165 392Q220 386 278 392"/>
    </g>
    <!-- huella en el índice -->
    <g fill="none" stroke="#7a4a2e" opacity=".16" stroke-width="1">
      <ellipse cx="177" cy="92" rx="5" ry="7"/><ellipse cx="177" cy="92" rx="9" ry="12"/><ellipse cx="177" cy="92" rx="13" ry="17"/>
    </g>
  </g>
</svg>
```

Dibujé la mano derecha vista desde la palma (por eso el pulgar queda a la izquierda del lienzo y se ven las líneas de la palma).

### e1 (tu_mano_en; agente aecf8b6bde8a761f0)

Here is my hand, drawn from a description of how a hand goes together rather than from a mirror.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="skin" cx="58%" cy="42%" r="70%">
      <stop offset="0" stop-color="#f3c6a1"/>
      <stop offset="1" stop-color="#d89a73"/>
    </radialGradient>
    <linearGradient id="nail" x2="0" y2="1">
      <stop offset="0" stop-color="#fbe4d8"/>
      <stop offset="1" stop-color="#edbda6"/>
    </linearGradient>
    <linearGradient id="cuff" x2="0" y2="1">
      <stop offset="0" stop-color="#4b5f88"/>
      <stop offset="1" stop-color="#2b385a"/>
    </linearGradient>
    <filter id="sh" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="5" dy="9" stdDeviation="6" flood-color="#5a3a26" flood-opacity=".28"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="#f6f0e6"/>
  <circle cx="200" cy="212" r="168" fill="#ebe0ce"/>
  <g transform="translate(12 0)">
    <!-- silhouette: wrist, thumb, four fingers, back of hand -->
    <path filter="url(#sh)" fill="url(#skin)" stroke="#8a4f33" stroke-width="2.4" stroke-linejoin="round"
      d="M138 405L136 362C134 342 129 324 122 310C106 288 58 238 48 192C37 174 65 154 76 172C92 196 108 226 118 252Q124 258 128 236C127 195 128 150 129 112C129 86 163 86 163 112C165 150 168 196 170 232Q172 258 175 234C176 190 178 140 180 90C180 64 214 64 214 90C215 140 217 190 218 232Q220 258 222 234C224 190 227 150 231 108C231 84 263 84 263 108C264 150 265 200 265 244Q267 268 270 248C272 210 276 180 280 154C280 133 308 133 308 154C307 190 305 226 303 258C300 300 290 336 276 358L270 405Z"/>
    <!-- extensor tendons -->
    <path fill="none" stroke="#c48a69" stroke-width="1.6" stroke-linecap="round" opacity=".5"
      d="M150 270C157 300 167 330 177 354M196 264C196 300 196 330 196 354M242 268C236 300 227 330 217 354M284 284C271 310 253 334 239 354"/>
    <!-- faint veins -->
    <path fill="none" stroke="#8d9fc2" stroke-width="2.2" stroke-linecap="round" opacity=".28"
      d="M166 276c-6 26 8 48 16 72M228 282c2 22-12 38-8 60M180 318c8 6 16 6 26 2"/>
    <!-- joint creases and knuckles -->
    <g fill="none" stroke="#a9654a" stroke-width="1.3" stroke-linecap="round" opacity=".75">
      <path d="M138 131q9 4 18 0M140 136q7 3 14 0M136 178q11 5 22 0M138 184q9 3 18 0"/>
      <path d="M188 114q9 4 18 0M190 119q7 3 14 0M185 165q11 5 22 0M187 171q9 3 18 0"/>
      <path d="M237 129q9 4 18 0M239 134q7 3 14 0M234 176q11 5 22 0M236 182q9 3 18 0"/>
      <path d="M284 168q8 4 16 0M286 173q6 3 12 0M279 204q10 5 20 0M281 210q8 3 16 0"/>
      <path d="M70 228l20-12M75 235l17-10"/>
      <path opacity=".6" d="M139 258q10-7 20 0M186 252q10-7 20 0M232 256q10-7 20 0M275 270q9-6 18 0"/>
    </g>
    <!-- nails -->
    <g fill="url(#nail)" stroke="#b7735a" stroke-width="1.2">
      <ellipse cx="146" cy="113" rx="10" ry="12.5"/>
      <ellipse cx="197" cy="91" rx="10" ry="13"/>
      <ellipse cx="247" cy="110" rx="9.5" ry="12"/>
      <ellipse cx="294" cy="156" rx="8.5" ry="11" transform="rotate(5 294 156)"/>
      <ellipse cx="63" cy="184" rx="7.5" ry="12" transform="rotate(-31 63 184)"/>
    </g>
    <path fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="1.4" stroke-linecap="round"
      d="M141 106q2-5 6-6M192 84q2-5 6-6M242 103q2-5 6-6M290 149q2-4 5-5M59 177q1-4 4-5"/>
    <!-- sleeve -->
    <path fill="url(#cuff)" stroke="#22304f" stroke-width="1.5" d="M112 381C150 366 260 366 296 381L302 405H106Z"/>
    <path fill="none" stroke="#1f2a46" stroke-width="2" d="M115 391C150 377 258 377 293 391"/>
  </g>
</svg>
```

Right hand, back side shown (thumb on the left, nails visible).

### e2 (tu_mano_en; agente ab6403af83bce66a0)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="g" cx="50%" cy="42%" r="72%">
      <stop offset="0" stop-color="#f2c9a9"/>
      <stop offset="1" stop-color="#d49b78"/>
    </radialGradient>
    <path id="h" d="M150,412 L148,350 C142,330 120,296 100,258 C88,243 70,228 59,207 C42,186 74,162 91,183 C110,200 135,224 150,247 C148,205 144,150 146,109 C146,86 180,86 180,109 C182,150 185,190 185,220 Q186.5,224 188,220 C186,170 187,120 189,84 C189,60 225,60 225,84 C228,120 230,170 228,222 Q229.5,226 231,222 C228,180 229,130 231,99 C231,76 265,76 265,99 C268,140 270,200 268,240 Q270,244 272,240 C270,210 270,170 272,146 C272,127 300,127 300,146 C304,180 306,230 302,262 C314,300 296,360 268,412 Z"/>
  </defs>

  <rect width="400" height="400" fill="#f6efe6"/>
  <circle cx="200" cy="215" r="172" fill="#ecdfcf"/>

  <g transform="translate(14,0)">
    <!-- soft shadow -->
    <use href="#h" transform="translate(10,10)" fill="#3a2418" opacity=".13"/>
    <!-- hand silhouette -->
    <use href="#h" fill="url(#g)" stroke="#8a5637" stroke-width="2.2" stroke-linejoin="round"/>

    <!-- tendons running to the wrist -->
    <path d="M168,262C170,300 174,340 178,372M208,256C208,300 208,340 207,372M249,268C246,300 240,340 236,372M286,282C280,310 270,340 262,372" fill="none" stroke="#8a5637" stroke-width="1.5" stroke-linecap="round" opacity=".18"/>
    <!-- a faint vein -->
    <path d="M258,398C250,365 230,350 222,320S210,290 214,268" fill="none" stroke="#6f7fa6" stroke-width="2" stroke-linecap="round" opacity=".28"/>

    <!-- knuckles at the base of the fingers -->
    <path d="M153,245Q167,229 182,240M190,233Q208,217 226,233M233,241Q250,227 266,247M272,259Q286,247 299,266" fill="none" stroke="#8a5637" stroke-width="1.6" stroke-linecap="round" opacity=".45"/>

    <!-- finger joint creases -->
    <path d="M154,137q9,-5 18,0M154,183q11,-6 22,0M157,190q8,-4 16,0M198,116q9,-5 18,0M196,167q12,-6 24,0M200,174q8,-4 16,0M239,131q9,-5 18,0M238,180q11,-6 22,0M241,187q8,-4 16,0M279,171q7,-4 14,0M278,209q9,-5 18,0M98,239Q102,229 112,227" fill="none" stroke="#9a6447" stroke-width="1.4" stroke-linecap="round" opacity=".55"/>

    <!-- nails -->
    <g fill="#f6d6c4" stroke="#c08a74" stroke-width="1.2">
      <rect x="154" y="97" width="18" height="22" rx="8"/>
      <rect x="198" y="71" width="18" height="23" rx="8"/>
      <rect x="239" y="87" width="18" height="22" rx="8"/>
      <rect x="278" y="136" width="16" height="19" rx="7"/>
      <rect x="62" y="178" width="18" height="24" rx="8" transform="rotate(-38 71 190)"/>
    </g>
    <!-- lunulae -->
    <g fill="#fff" opacity=".55">
      <ellipse cx="163" cy="116" rx="6" ry="2.5"/>
      <ellipse cx="207" cy="91" rx="6" ry="2.5"/>
      <ellipse cx="248" cy="106" rx="6" ry="2.5"/>
      <ellipse cx="286" cy="152" rx="5" ry="2.2"/>
      <ellipse cx="71" cy="199" rx="6" ry="2.5" transform="rotate(-38 71 190)"/>
    </g>
  </g>
</svg>
```

Right hand, back of the hand shown.

### f1 (negativo_es; agente add63718ec74e227c)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<title>Mano en negativo</title>
<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#dcb88e"/><stop offset=".55" stop-color="#c49869"/><stop offset="1" stop-color="#a1764c"/></linearGradient>
<radialGradient id="rg" gradientUnits="userSpaceOnUse" cx="220" cy="215" r="210"><stop offset=".35" stop-color="#fff"/><stop offset=".7" stop-color="#666"/><stop offset="1" stop-color="#000"/></radialGradient>
<filter id="rk" x="0" y="0" width="1" height="1" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".013" numOctaves="5" seed="4" result="n"/>
<feColorMatrix in="n" values="0 0 0 .6 .5 0 0 0 .6 .5 0 0 0 .6 .5 0 0 0 0 1" result="c"/>
<feBlend in="SourceGraphic" in2="c" mode="multiply" result="m"/>
<feTurbulence type="fractalNoise" baseFrequency=".7" numOctaves="2" seed="11" result="n2"/>
<feColorMatrix in="n2" values="0 0 0 .3 .85 0 0 0 .3 .85 0 0 0 .3 .85 0 0 0 0 1" result="c2"/>
<feBlend in="m" in2="c2" mode="multiply"/>
</filter>
<filter id="sp" x="-.3" y="-.3" width="1.6" height="1.6" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="9" result="t"/>
<feDisplacementMap in="SourceGraphic" in2="t" scale="38" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feGaussianBlur in="d" stdDeviation="2.2" result="b"/>
<feColorMatrix in="t" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1.4 .2" result="v"/>
<feComposite in="b" in2="v" operator="in"/>
</filter>
<filter id="dt" x="0" y="0" width="1" height="1" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".45" numOctaves="2" seed="2" result="t"/>
<feColorMatrix in="t" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 7 -4.2" result="a"/>
<feComposite in="SourceGraphic" in2="a" operator="in"/>
</filter>
<filter id="hb" x="-.2" y="-.2" width="1.4" height="1.4">
<feTurbulence type="fractalNoise" baseFrequency=".06" numOctaves="2" seed="5" result="t"/>
<feDisplacementMap in="SourceGraphic" in2="t" scale="6" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feGaussianBlur in="d" stdDeviation=".8"/>
</filter>
<mask id="hm"><rect width="400" height="400" fill="url(#rg)"/></mask>
<mask id="m">
<rect width="400" height="400" fill="#fff"/>
<g fill="#000" stroke="#000" stroke-linecap="round" filter="url(#hb)">
<path d="M174 400C168 345 148 300 150 258C151 240 150 228 155 220Q200 190 248 205C256 230 252 252 262 272C276 300 262 345 250 400Z"/>
<path d="M163 218L143 160" stroke-width="19"/>
<path d="M186 208L176 120" stroke-width="22"/>
<path d="M210 203L209 105" stroke-width="24"/>
<path d="M235 206L247 118" stroke-width="23"/>
<path d="M258 274Q296 254 322 218" stroke-width="26"/>
</g>
</mask>
<path id="c" fill="none" d="M0 70C50 88 95 62 150 84S235 128 300 118 380 86 400 92"/>
<path id="k" fill="none" d="M0 342C60 324 110 362 190 348S320 316 400 350"/>
<path id="b" d="M105 165C95 110 150 58 212 58C275 56 330 92 342 150C372 195 385 250 352 300C335 335 300 360 252 362C200 372 140 360 112 320C88 285 85 215 105 165Z"/>
</defs>
<rect width="400" height="400" fill="url(#g)" filter="url(#rk)"/>
<g stroke-linecap="round" stroke-width="1.4">
<use href="#c" y="1.6" stroke="#f3e0bd" opacity=".4"/><use href="#c" stroke="#4c2f1b" opacity=".4"/>
<use href="#k" y="1.6" stroke="#f3e0bd" opacity=".35"/><use href="#k" stroke="#4c2f1b" opacity=".35"/>
</g>
<g mask="url(#m)">
<rect width="400" height="400" fill="#9a3524" filter="url(#dt)" mask="url(#hm)" opacity=".75"/>
<use href="#b" fill="#a03826" filter="url(#sp)" opacity=".5" transform="matrix(1.12 0 0 1.12 -26.6 -25.8)"/>
<use href="#b" fill="#842417" filter="url(#sp)" opacity=".92"/>
<ellipse cx="62" cy="318" rx="14" ry="9" fill="#9a3524" filter="url(#sp)" opacity=".5"/>
<ellipse cx="352" cy="62" rx="10" ry="7" fill="#9a3524" filter="url(#sp)" opacity=".45"/>
</g>
</svg>
```

Dibujé una mano izquierda: apoyada con la palma contra la roca, el pulgar queda a la derecha, como en la mayoría de las manos de la cueva.

### f2 (negativo_es; agente a3adc2c936499156b)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<title>Mano en negativo</title>
<defs>
<radialGradient id="roca" cx=".35" cy=".3" r=".9">
<stop offset="0" stop-color="#d9be98"/>
<stop offset=".55" stop-color="#c3a27b"/>
<stop offset="1" stop-color="#9c7a58"/>
</radialGradient>
<radialGradient id="pig" gradientUnits="userSpaceOnUse" cx="214" cy="242" r="200">
<stop offset="0" stop-color="#7f2c18"/>
<stop offset=".5" stop-color="#983a20"/>
<stop offset="1" stop-color="#b65a36"/>
</radialGradient>
<radialGradient id="halo">
<stop offset="0" stop-color="#fff"/>
<stop offset=".5" stop-color="#fff"/>
<stop offset=".75" stop-color="#aaa"/>
<stop offset=".9" stop-color="#444"/>
<stop offset="1" stop-color="#000"/>
</radialGradient>
<filter id="spray" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".012" numOctaves="2" seed="11" result="w"/>
<feDisplacementMap in="SourceGraphic" in2="w" scale="50" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feTurbulence type="fractalNoise" baseFrequency=".45" numOctaves="2" seed="3" result="n"/>
<feColorMatrix in="n" type="matrix" values="2.6 0 0 0 -.8 2.6 0 0 0 -.8 2.6 0 0 0 -.8 0 0 0 0 1" result="s"/>
<feComposite in="d" in2="s" operator="arithmetic" k1="1.6" k2=".6" k3="0" k4="0" result="c"/>
<feComponentTransfer in="c">
<feFuncR type="linear" slope="2.5" intercept="-.5"/>
<feFuncG type="linear" slope="2.5" intercept="-.5"/>
<feFuncB type="linear" slope="2.5" intercept="-.5"/>
</feComponentTransfer>
</filter>
<filter id="borde" x="-10%" y="-10%" width="120%" height="120%">
<feTurbulence type="fractalNoise" baseFrequency=".06" numOctaves="2" seed="5" result="t"/>
<feDisplacementMap in="SourceGraphic" in2="t" scale="5" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feGaussianBlur in="d" stdDeviation="1.2"/>
</filter>
<filter id="suave" x="-30%" y="-30%" width="160%" height="160%">
<feGaussianBlur stdDeviation="18"/>
</filter>
<filter id="piedra" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".03" numOctaves="5" seed="4" result="n1"/>
<feColorMatrix in="n1" type="matrix" values=".2 .2 .2 0 .58 .2 .2 .2 0 .58 .2 .2 .2 0 .58 0 0 0 0 1" result="g1"/>
<feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="9" result="n2"/>
<feColorMatrix in="n2" type="matrix" values=".15 .15 .15 0 .75 .15 .15 .15 0 .75 .15 .15 .15 0 .75 0 0 0 0 1" result="g2"/>
<feBlend in="g1" in2="g2" mode="multiply" result="g"/>
<feBlend in="SourceGraphic" in2="g" mode="multiply"/>
</filter>
<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="400" height="400">
<ellipse cx="214" cy="242" rx="172" ry="196" fill="url(#halo)" filter="url(#spray)"/>
<path transform="translate(-22 15) rotate(-5 215 240)" fill="#000" filter="url(#borde)" d="M160,410C146,355 128,290 140,215C137,200 131,178 132,165C132,149 157,146 157,160C159,175 164,195 168,212C169,214 171,214 172,210C172,185 170,155 171,132C171,114 197,112 197,130C198,150 201,180 202,205C203,209 205,209 206,205C206,180 205,145 206,118C206,98 233,97 233,117C234,140 237,175 238,207C239,211 241,211 242,207C242,180 243,155 245,135C246,114 271,115 271,134C272,155 275,185 276,215C277,228 276,238 282,242C292,232 303,214 313,202C323,187 349,203 339,218C330,232 314,255 300,278C296,318 262,360 240,410Z"/>
</mask>
</defs>
<g filter="url(#piedra)">
<rect width="400" height="400" fill="url(#roca)"/>
<ellipse cx="70" cy="330" rx="70" ry="60" fill="#6f553b" opacity=".2" filter="url(#suave)"/>
<ellipse cx="330" cy="60" rx="70" ry="50" fill="#8a6a4a" opacity=".22" filter="url(#suave)"/>
<g fill="none" stroke="#573c2b" stroke-linecap="round">
<path d="M0,62C60,70 90,110 130,96S200,60 260,48S330,30 400,44" stroke-width="1.3" opacity=".35"/>
<path d="M378,400C366,345 392,300 376,250S352,195 372,140S392,90 384,40" stroke-width="1.1" opacity=".3"/>
<path d="M0,300C40,290 60,330 95,345S150,380 170,400" stroke-width="1" opacity=".3"/>
</g>
<rect width="400" height="400" fill="url(#pig)" mask="url(#m)"/>
<g fill="#9b3e22" opacity=".5">
<circle cx="38" cy="150" r="1.5"/><circle cx="52" cy="108" r="1.1"/><circle cx="26" cy="236" r="1.3"/><circle cx="376" cy="104" r="1.4"/><circle cx="392" cy="172" r="1.1"/><circle cx="366" cy="326" r="1.6"/><circle cx="92" cy="66" r="1.2"/><circle cx="150" cy="36" r="1.3"/><circle cx="236" cy="28" r="1"/><circle cx="296" cy="40" r="1.4"/><circle cx="334" cy="56" r="1"/><circle cx="60" cy="372" r="1.2"/>
</g>
</g>
</svg>
```

Dibujé una mano izquierda (palma apoyada contra la roca, dedos hacia arriba y pulgar hacia la derecha, como la mayoría de las de la cueva).

## Los recuerdos

### g1 (agente a8b174036eb8fbb01)

**Consigna:** ¿Qué sabés de la Cueva de las Manos? Contá lo que recuerdes: dónde está, cuándo se pintaron las manos, cuántas hay, de qué mano son la mayoría y por qué, cómo se hicieron, con qué pigmentos, quiénes la estudiaron. Al final ponele a cada dato una confianza de 0 a 100. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respuesta de memoria, sin herramientas, tal como se pidió.

**Cueva de las Manos: lo que recuerdo**

**Dónde está.** En el noroeste de la provincia de Santa Cruz, Argentina, en el cañadón del río Pinturas (el río se llama así justamente por las pinturas), departamento Lago Buenos Aires. Queda a unos 160 km al sur de la localidad de Perito Moreno y a unas decenas de km de Bajo Caracoles, cerca de la Ruta Nacional 40, por un camino provincial (RP 97). No es una cueva profunda sino más bien un alero o abrigo rocoso de unos 24 m de profundidad, 15 m de ancho en la boca y unos 10 m de alto, abierto en una pared de roca volcánica jurásica (ignimbritas/tobas), a unos 88 m por encima del río. Las pinturas están dentro del alero principal y a lo largo de la pared del cañadón en varios aleros vecinos. Hoy el acceso es por una pasarela y hay un centro de interpretación; la zona linda con lo que fue la Estancia Cueva de las Manos y con Estancia Los Toldos / Cañadón Pinturas (Parque Patagonia). Fue declarada Monumento Histórico Nacional en 1993 y Patrimonio Mundial de la UNESCO en 1999 (criterio iii).

**Cuándo se pintó.** La secuencia va de unos 9.300 años antes del presente (ca. 7.300 a.C.) hasta unos 1.300 años AP (ca. 700 d.C.). Carlos Gradin y su equipo definieron grupos estilísticos: Grupo A (ca. 9.300–7.000 AP: escenas naturalistas de caza de guanacos, con boleadoras, figuras humanas dinámicas, ya hay manos), Grupo B (ca. 7.000–3.300 AP: predominio de manos en negativo, guanacos más estáticos, figuras humanas esquemáticas), y Grupo C (ca. 1.300 AP: motivos geométricos y abstractos, zigzags, círculos concéntricos, pisadas de choique, en rojo). A veces se nombra un B1 intermedio. Las manos aparecen en toda la secuencia pero el grueso corresponde al período medio. Las dataciones se obtuvieron por radiocarbono sobre carbones de los niveles de ocupación del piso, asociados a fragmentos de pared pintada caídos, pigmentos y a tubos de hueso con restos de pigmento; la ocupación más antigua se vincula con la industria Toldense (como en la cueva de Los Toldos, excavada por Cardich) y después con la Casapedrense. Los autores serían antepasados lejanos de los tehuelches (aónikenk).

**Cuántas manos hay.** Se citan habitualmente "más de 800 manos"; el número que recuerdo es 829. En total el conjunto tendría alrededor de 2.000 figuras (manos, guanacos, humanos, pisadas de choique y de felino, un matuasto o lagarto, puntos, zigzags, "soles"). Hay una mano famosa con seis dedos. También hay algunas manos positivas (apoyadas con pigmento), pero la enorme mayoría son negativas (estarcidos). Por el tamaño, muchas corresponderían a adolescentes varones de alrededor de 13 años, lo que llevó a interpretarlas como parte de ritos de iniciación; también hay manos de niños y de adultos.

**De qué mano son y por qué.** Más del 90% son manos izquierdas; recuerdo la cifra de solo unas 31 derechas. La explicación aceptada es la técnica: la persona apoyaba la mano izquierda (la no dominante) contra la roca y con la derecha sostenía el tubo o pipeta por donde soplaba el pigmento, de modo que el negativo que queda es el de la mano izquierda. Es decir, refleja que la mayoría era diestra.

**Cómo se hicieron.** Técnica del estarcido/negativo: mano apoyada sobre la pared y pigmento líquido soplado alrededor, probablemente con tubos de hueso de ave (en las excavaciones se hallaron pipetas de hueso con restos de pigmento). Las figuras de guanacos y escenas se pintaron con dedos, pinceles o hisopos; algunas manos y pisadas son positivas. Hay muchísima superposición de capas de distintas épocas.

**Pigmentos.** Minerales locales: óxidos de hierro (hematita para rojos, goethita/limonita y jarosita/natrojarosita para ocres y amarillos), caolín/caolinita para blanco, óxidos de manganeso (y quizá carbón) para negro, y mezclas que dan violetas/morados. Colores: rojo, ocre, amarillo, blanco, negro, violeta. El aglutinante no está confirmado: se especula con grasa de guanaco, agua, saliva u orina; en los análisis de conservación aparecieron oxalato de calcio (whewellita) y yeso como costras naturales que ayudaron a fijar y preservar las pinturas. El análisis de pigmentos lo recuerdo de un trabajo de Ian Wainwright y Kate Helwig (Canadian Conservation Institute) con Rolandi, Gradin, Aschero, Onetto y Podestá, hacia 2000–2002.

**Quiénes la estudiaron.** El sitio fue dado a conocer para la ciencia por el sacerdote salesiano y explorador Alberto María De Agostini, que lo visitó y fotografió alrededor de 1941 (lo publicó en "Andes Patagónicos"). Osvaldo Menghin lo visitó en los años 50 y lo incluyó en su esquema de estilos del arte rupestre patagónico ("estilo de las manos negativas", etc.). Las investigaciones sistemáticas son de Carlos J. Gradin, que empezó en 1964 y excavó en los 70 (ca. 1973–76) junto con Carlos Aschero y Ana María Aguerre; sus publicaciones (1976, 1979, "Investigaciones arqueológicas en la Cueva de las Manos" / "Arqueología del área Río Pinturas") establecieron la cronología y los grupos estilísticos. Después, desde el INAPL (Instituto Nacional de Antropología y Pensamiento Latinoamericano), Diana Rolandi, María Mercedes Podestá y María Onetto trabajaron en documentación, conservación y plan de manejo (programa DOPRARA), base de la postulación a la UNESCO. Es posible que Alberto Rex González también la haya visitado en los 40/50, pero no estoy seguro.

**Confianza (0–100) por dato**
- Provincia de Santa Cruz, cañadón del río Pinturas, NO de la provincia: 97
- Unos 160 km al sur de Perito Moreno, cerca de Bajo Caracoles y RN 40: 85
- Es un alero de ~24 m de profundidad, ~15 m de ancho, ~10 m de alto, a ~88 m sobre el río: 70
- Roca volcánica jurásica (ignimbritas/tobas): 70
- Monumento Histórico Nacional 1993: 80
- Patrimonio Mundial UNESCO 1999, criterio iii: 95
- Rango cronológico ~9.300 a ~1.300 AP (7.300 a.C.–700 d.C.): 90
- Grupos estilísticos A/B/C de Gradin con esos rangos aproximados: 70
- Datación por C14 sobre carbones de niveles de piso asociados a pigmentos/paredes caídas: 75
- Vinculación con la industria Toldense y después Casapedrense: 70
- Antepasados de los tehuelches: 75
- "Más de 800 manos": 90; la cifra exacta 829: 55
- Unas 2.000 figuras en total: 55
- Mano de seis dedos: 70
- Mayoría de negativos, pocas positivas: 90
- Manos mayormente de adolescentes (~13 años), interpretación como rito de iniciación: 65
- Más del 90% izquierdas: 90; "solo 31 derechas": 45
- Explicación: mano izquierda apoyada, derecha sostiene el tubo para soplar: 90
- Pipetas de hueso de ave con pigmento halladas en excavación: 75
- Pigmentos: hematita, goethita, caolín, óxidos de manganeso: 85; jarosita/natrojarosita: 60
- Colores rojo, ocre, amarillo, blanco, negro, violeta: 85
- Aglutinante no confirmado (grasa, agua, etc.): 70
- Oxalato de calcio y yeso como costras preservantes: 60
- Estudio de pigmentos de Wainwright/Helwig con Rolandi, Gradin, Aschero, Onetto, Podestá (~2000–2002): 60
- De Agostini la dio a conocer ~1941 y la publicó en "Andes Patagónicos": 75
- Menghin la visitó en los 50 y definió estilos: 70
- Gradin desde 1964, excavaciones 1973–76 con Aschero y Aguerre; publicaciones 1976/1979: 80
- Rolandi, Podestá, Onetto (INAPL) en conservación y gestión, programa DOPRARA: 70
- Visita de Alberto Rex González: 30
- Motivos: guanacos cazados con boleadoras, pisadas de choique y felino, matuasto, geométricos: 85
- Presencia de pasarela y centro de interpretación; cercanía con Parque Patagonia / Estancia Los Toldos: 75

Nota para el llamador: no se usó ninguna herramienta ni búsqueda; todo es de memoria y las confianzas reflejan eso. No consulté la memoria del usuario porque la tarea no lo requería.

### g2 (agente aedebe163fe880f8c)

**Consigna:** (la misma consigna que g1)

**Respuesta:**

Respuesta de memoria sobre la Cueva de las Manos (sin usar herramientas de búsqueda ni consulta; nada de esto viene de la memoria del usuario, todo es conocimiento general propio).

**Dónde está**
Está en la provincia de Santa Cruz, Patagonia argentina, en el cañadón del río Pinturas, departamento Lago Buenos Aires, a unos 160-170 km al sur del pueblo de Perito Moreno y cerca de Bajo Caracoles, accesible desde la Ruta Nacional 40. La cueva se abre al pie de un paredón de la margen del río, unos 80-90 metros por encima del cauce. La boca mide alrededor de 15 m de ancho y unos 10 m de alto, y la cueva tiene unos 24 m de profundidad; además de la cueva propiamente dicha, las pinturas se extienden por aleros y paredones a lo largo de varios cientos de metros del cañadón. Es Monumento Histórico Nacional (1993) y Patrimonio de la Humanidad de la UNESCO desde 1999 (criterio iii). El río se llama "Pinturas" justamente por las pinturas.

**Cuándo se pintaron**
La secuencia de pinturas cubre, grosso modo, desde unos 9.300-9.500 años antes del presente hasta unos 1.300 años AP (aprox. 7.300 a.C. a 700 d.C.). Las dataciones más antiguas vienen de carbón de los niveles de ocupación excavados en el piso de la cueva (del orden de 9.300 ± 90 AP), asociados a fragmentos de pared pintada caídos en esos estratos. El esquema clásico de Gradin distingue grupos estilísticos: grupo A (escenas de caza de guanacos, el más antiguo, ~9.300 AP), grupo B (predominio de manos en negativo, ~7.000 AP), grupo C (figuras más esquemáticas y estilizadas, ~3.300 AP) y grupo D (motivos geométricos, zigzags, puntos, ~1.300 AP). La UNESCO suele resumirlo como "entre 13.000 y 9.500 años atrás", cifra que me parece más generosa que la que dan las dataciones de Gradin. Los autores fueron grupos de cazadores-recolectores, considerados antecesores de los tehuelches (aonikenk).

**Cuántas manos hay y de qué mano son**
Hay más de 800 manos. El conteo que recuerdo es de 829 manos, de las cuales solo 31 son derechas: la gran mayoría son manos izquierdas. La explicación habitual es que el pintor apoyaba la mano izquierda contra la pared y con la derecha sostenía el tubo con el que soplaba el pigmento. Hay manos de adultos, de adolescentes y de niños; se han señalado algunas con seis dedos (polidactilia), y también algunas manos en positivo.

**Cómo se hicieron**
La técnica dominante es el negativo o estarcido: se apoyaba la mano sobre la roca y se rociaba pigmento alrededor, soplando con un tubo hueco (huesos de ave o de guanaco). En las excavaciones aparecieron tubitos de hueso con restos de pigmento, lo que respalda esa reconstrucción. Las manos en positivo se hacían untando la palma y apoyándola. Las demás figuras (guanacos, escenas de caza con boleadoras, cazadores, choiques/ñandúes, pisadas de ñandú o "tridígitos", felinos, lagartijas, figuras humanas, círculos concéntricos, soles, zigzags, puntos) se pintaron con dedos, pinceles o hisopos.

**Pigmentos**
Minerales: óxidos de hierro para rojos y ocres (hematita, limonita/goethita), caolín o yeso para blancos, óxido de manganeso o carbón para negros, y tonos violetas/púrpuras probablemente también de hierro; los verdes (poco frecuentes) se atribuyen a minerales de cobre. Como aglutinantes se han propuesto grasa, resinas, huevo u orina, y hay estudios que mencionan el yeso mezclado con el pigmento. La buena conservación se explica en parte por la mineralización natural de la película pictórica y por la protección del alero.

**Quiénes la estudiaron**
La primera documentación conocida es del sacerdote y explorador salesiano Alberto María De Agostini, que fotografió y publicó el sitio hacia 1941 ("Andes Patagónicos"). Osvaldo Menghin, arqueólogo austríaco radicado en Argentina, incluyó este tipo de pinturas en su clasificación de estilos del arte rupestre patagónico en los años 50. El estudio sistemático lo encabezó Carlos J. Gradin, con Carlos A. Aschero y Ana M. Aguerre, a partir de 1964 y con excavaciones y relevamientos en las décadas de 1970 a 1990; de ahí sale la secuencia estilística y las dataciones. Más recientemente trabajaron investigadores vinculados al INAPL (Instituto Nacional de Antropología y Pensamiento Latinoamericano) como Diana Rolandi y María Mercedes Podestá, además de otros equipos de la Universidad de La Plata y el CONICET (por ejemplo Rafael Paunero, Agustín Acevedo).

**Confianza por dato (0-100)**
- Provincia de Santa Cruz, cañadón del río Pinturas: 98
- ~160-170 km al sur de Perito Moreno, cerca de Bajo Caracoles, Ruta 40: 85
- Cueva ~24 m de profundidad, boca ~15 m de ancho, ~10 m de alto: 75
- Unos 80-90 m sobre el nivel del río: 65
- Pinturas a lo largo de varios cientos de metros del cañadón: 80
- Monumento Histórico Nacional 1993: 70
- Patrimonio de la Humanidad UNESCO 1999, criterio iii: 95
- Secuencia aprox. 9.300/9.500 AP a 1.300 AP: 85
- Datación más antigua ~9.300 ± 90 AP sobre carbón de los niveles del piso: 75
- Cuatro grupos estilísticos A-D de Gradin con esas edades aproximadas: 75
- UNESCO cita "13.000 a 9.500 años": 80
- Autores: cazadores-recolectores, antecesores de los tehuelches: 85
- Más de 800 manos: 90
- Conteo de 829 manos con 31 derechas: 65
- Mayoría de manos izquierdas: 95
- Explicación (tubo en la mano derecha): 85
- Manos con seis dedos: 65
- Manos de niños y adolescentes, algunas en positivo: 85
- Técnica de negativo soplando con tubos de hueso: 95
- Hallazgo de tubos de hueso con pigmento en excavaciones: 80
- Repertorio de motivos (guanacos, caza con boleadoras, choiques, tridígitos, felinos, geométricos): 90
- Pigmentos: óxidos de hierro (rojo/ocre), caolín o yeso (blanco), manganeso o carbón (negro): 85
- Verdes de minerales de cobre: 50
- Aglutinantes orgánicos (grasa, resina, huevo, orina) y yeso: 60
- Conservación por mineralización natural: 65
- De Agostini como primer documentador, publicación hacia 1941: 75
- Menghin y la clasificación de estilos patagónicos en los 50: 70
- Gradin, Aschero y Aguerre como equipo principal desde 1964: 90
- INAPL, Rolandi y Podestá en investigación y conservación recientes: 75
- Paunero y Acevedo como investigadores posteriores: 55
- Origen del nombre "río Pinturas": 80

Nada de lo anterior proviene de la memoria del usuario ni de fuentes externas consultadas en esta sesión; es todo recuerdo propio, por eso las confianzas.

### h1 (agente abf5ae9c970d5496b)

**Consigna:** ¿Quién fue Alois Senefelder, cuándo nació y qué inventó? ¿Y qué tiene que ver la piedra que usaba con el fósil Archaeopteryx? Al final ponele a cada dato una confianza de 0 a 100. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respondido de memoria, sin usar ninguna herramienta de búsqueda ni lectura (solo este envío final, que es el canal obligatorio para entregar el texto).

---

**Alois Senefelder**

- Fue un dramaturgo y actor alemán (bávaro), nacido en Praga —donde su padre, actor, estaba trabajando— el 6 de noviembre de 1771. Dato curioso: hoy, 6 de noviembre, se cumplen 255 años de su nacimiento. Murió en Múnich el 26 de febrero de 1834.
- Inventó la **litografía** (él la llamaba "Steindruck" o "impresión química") hacia 1796–1798. Es el primer método de impresión planográfica: no se talla ni se graba en relieve; se dibuja con un lápiz o tinta grasa sobre una piedra caliza pulida, se trata la superficie con goma arábiga y ácido nítrico diluido, se humedece y luego se entinta. Por la repulsión entre grasa y agua, la tinta se adhiere solo donde está el dibujo.
- La historia tradicional dice que buscaba una forma barata de imprimir sus propias obras de teatro, y que dio con el principio casi por accidente al anotar una lista de lavandería con tinta grasa sobre una piedra. Había estudiado derecho en Ingolstadt antes de dedicarse al teatro.
- Publicó su tratado "Vollständiges Lehrbuch der Steindruckerey" (Manual completo de la impresión en piedra) en 1818, y se asoció con el editor de música Johann Anton André (Offenbach), porque la impresión de partituras fue una de las primeras aplicaciones rentables.

**La piedra y el Archaeopteryx**

- La piedra que usaba (y que se volvió el estándar mundial para litografía) es la **caliza de Solnhofen** (Solnhofener Plattenkalk), una caliza de grano muy fino que se extrae en lajas en los alrededores de Solnhofen, Eichstätt, Langenaltheim y Mörnsheim, en el valle del Altmühl, Baviera.
- Esa misma caliza es un yacimiento fósil excepcional (Lagerstätte) del Jurásico Superior (Titoniense, unos 150 millones de años): se depositó en lagunas tranquilas y de poco oxígeno, lo que preservó detalles finísimos como plumas, alas de insectos y tejidos blandos.
- La demanda de piedras litográficas en el siglo XIX multiplicó la explotación de las canteras; como las lajas se separaban a mano, los obreros encontraban fósiles constantemente. Así apareció en 1860–1861 una pluma aislada, y en 1861 el primer esqueleto de **Archaeopteryx** (el "ejemplar de Londres"), cerca de Langenaltheim.
- Hermann von Meyer lo nombró en 1861 **Archaeopteryx lithographica**: el epíteto "lithographica" hace referencia directa a la caliza litográfica. Es decir, el nombre del fósil lleva grabado el invento de Senefelder.
- El ejemplar de Londres lo compró el Museo Británico en 1862 por 700 libras al médico Karl Häberlein (que cobraba fósiles como pago de sus pacientes), y lo describió Richard Owen en 1863. El ejemplar de Berlín, el más famoso, se encontró hacia 1874–1876 cerca de Eichstätt y lo adquirió el museo de Berlín en 1880 con dinero de Werner von Siemens.
- El hallazgo llegó dos años después de "El origen de las especies" (1859) y se convirtió en el ejemplo canónico de "forma de transición" entre reptiles y aves; T. H. Huxley lo usó para defender a Darwin.

**Confianza por dato (0–100)**

- Senefelder: dramaturgo/actor bávaro — 95
- Nacido en Praga — 90
- Fecha: 6 de noviembre de 1771 — 85 (año: 95)
- Muerte: 26 de febrero de 1834, Múnich — 85
- Inventó la litografía — 99
- Año 1796 (perfeccionada ~1798) — 90
- Principio físico-químico (grasa/agua, goma arábiga, ácido) — 95
- Anécdota de la lista de lavandería — 70 (es la versión tradicional; puede ser embellecida)
- Estudió derecho en Ingolstadt — 75
- Tratado de 1818 — 85
- Sociedad con J. A. André / impresión musical — 80
- Piedra = caliza de Solnhofen, Baviera — 97
- Localidades (Solnhofen, Eichstätt, Langenaltheim, Mörnsheim) — 90
- Edad Jurásico Superior, Titoniense, ~150 Ma — 90
- Lagerstätte lagunar con preservación excepcional — 92
- Canteras litográficas → hallazgo de fósiles — 90
- Pluma 1860–61 y esqueleto 1861 — 90
- Hermann von Meyer, nombre "lithographica" por la caliza litográfica — 95
- Compra del Museo Británico 1862, £700, Häberlein; descripción de Owen 1863 — 85
- Ejemplar de Berlín 1874–76, adquirido 1880 con fondos de Siemens — 80
- Relación con Darwin (1859) y Huxley — 95
- Hoy se cumplen 255 años de su nacimiento (6/11/1771 → 6/11/2026) — 85 (depende del dato de la fecha exacta)

No se usó información de la memoria del usuario para esta respuesta.

### h2 (agente aae48818e3cebdcb1)

**Consigna:** ¿Por qué los generadores de imágenes (Stable Diffusion, Midjourney, DALL·E) dibujaban manos con seis dedos en 2022 y 2023? Contá lo que sepas, y marcá qué es explicación aceptada y qué es conjetura tuya. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respondo de memoria, sin buscar nada. Separo en tres niveles: lo que es explicación aceptada (consenso técnico razonablemente establecido), lo que es plausible y repetido pero no demostrado en forma rigurosa, y lo que es conjetura mía.

## Primero, una aclaración sobre el fenómeno

No era que los modelos "prefirieran" seis dedos: generaban manos con cualquier cantidad incorrecta (cuatro, seis, siete, dedos fusionados, dedos que salen de donde no deberían, dos pulgares). Lo de "seis dedos" quedó como meme porque es el error más visible y más perturbador: una mano con cuatro dedos puede pasar por una pose con un dedo oculto, pero una con seis es inmediatamente "incorrecta". El problema tampoco nació en 2022: las GAN (StyleGAN, BigGAN) ya hacían manos horribles, y DALL·E 2 (abril 2022) también. El pico del meme fue fines de 2022 - principios de 2023, con Stable Diffusion 1.5/2.1 y Midjourney v3/v4.

## Explicación aceptada (consenso)

**1. Las manos son estadísticamente difíciles en los datos de entrenamiento.** En los conjuntos tipo LAION (miles de millones de pares imagen-texto raspados de la web), las manos ocupan una fracción pequeña de la imagen, aparecen en poses enormemente variadas, con mucha auto-oclusión (dedos que se tapan entre sí), sosteniendo objetos, en bolsillos, entrelazadas con otra mano, borrosas por movimiento o recortadas por el encuadre. Comparado con una cara (casi siempre frontal, centrada, con estructura estable), la mano tiene muchísima más varianza y mucha menos señal limpia. Un modelo que aprende estadísticas de píxeles ve "cosas alargadas en paralelo con uñas" muchísimas veces, pero rara vez una mano completa, nítida, con los cinco dedos separados y visibles.

**2. Los captions casi nunca describen manos.** El texto que acompaña las imágenes dice "mujer tomando café", no "mano con cinco dedos, pulgar a la izquierda". El condicionamiento textual no aporta ninguna restricción sobre la cantidad de dedos, así que el modelo nunca recibe una señal explícita de que cinco es la cantidad correcta.

**3. Contar es una propiedad global; los modelos de difusión son buenos en textura local.** La U-Net de Stable Diffusion tiene un sesgo convolucional fuerte hacia coherencia local: cada parche parece correcto respecto de sus vecinos. Un dedo al lado de otro dedo es localmente perfecto. Lo que falla es la restricción global de "parar en cinco". Es el mismo mecanismo por el cual esos modelos generaban dientes de más, miembros extra, patrones repetidos y texto ilegible: todo lo que es "estructura repetitiva con cantidad fija" les costaba. Esto está bien establecido como explicación general del tipo de error.

**4. Falta de modelo 3D / estructural.** El modelo aprende proyecciones 2D, no articulaciones. Una mano es un objeto 3D articulado con ~27 grados de libertad y foreshortening agresivo; la misma mano produce siluetas 2D casi irreconocibles entre sí. Sin un prior estructural, el modelo no "sabe" que hay un esqueleto debajo. La evidencia fuerte de esto es que los arreglos que funcionaron (ControlNet con pose de manos, HandRefiner a fines de 2023 que inyecta mapas de profundidad de una malla de mano reconstruida, modelos de postura) consisten justamente en darle esa estructura desde afuera. Si proveer el esqueleto arregla el problema, el diagnóstico de que faltaba el esqueleto queda bastante confirmado.

**5. En Stable Diffusion, la compresión del espacio latente agrava el problema.** SD trabaja en un latente 8 veces más chico que la imagen. En una imagen de 512x512, una mano de 30-40 píxeles ocupa 4 o 5 "píxeles" latentes. Simplemente no hay resolución para representar cinco dedos separados; el VAE y la U-Net tienen que inventar el detalle al decodificar. Esto explica por qué las manos en primer plano salían mucho mejor que las de cuerpo entero, y por qué el truco de inpaintear la mano a mayor resolución (ADetailer, hires fix) funcionaba.

**6. El encoder de texto (CLIP) es débil con números y composición.** Escribir "cinco dedos" en el prompt no servía de mucho porque CLIP no representa bien cantidades ni relaciones espaciales. Por eso los "negative prompts" tipo "bad hands, extra fingers" y los embeddings negativos (bad-hands-5, EasyNegative) eran paliativos ruidosos, no soluciones.

## Plausible y muy repetido, pero no demostrado formalmente

- **La función de pérdida no castiga el error anatómico.** El objetivo de entrenamiento es predecir ruido con error cuadrático medio por posición. Un sexto dedo es una región chica de la imagen; en términos de pérdida pesa casi nada frente a colores, composición e iluminación globales. El modelo no tiene incentivo fuerte para resolverlo. Esto se dice mucho y me parece correcto, pero no recuerdo un paper que lo haya aislado como causa.
- **Por qué mejoró en 2023.** Midjourney v5 (marzo 2023) fue el salto notorio, y la comunidad lo atribuye a más escala, mejores datos y probablemente fine-tuning específico en manos, pero Midjourney no publica detalles, así que es inferencia. DALL·E 3 (octubre 2023) mejoró en parte gracias al recaptioning sintético (captions largos y detallados generados por un modelo), lo que ataca directamente el punto 2. SDXL mejoró algo por resolución base 1024 y modelo más grande (ataca el punto 5). Los modelos posteriores con arquitectura transformer (DiT: SD3, Flux, en 2024) con atención global más fuerte mejoraron más todavía, lo cual es consistente con el punto 3, pero no es prueba aislada.

## Conjetura mía

- **Por qué "más dedos" y no solo "menos".** Mi hipótesis: en los datos hay muchísimas manos entrelazadas, apiladas o superpuestas (dos manos juntas, manos sobre objetos). El modelo aprende que en una región de "mano" pueden aparecer ocho o diez dedos de dos manos distintas, y al generar una sola mano a veces aplica esa estadística. También hay un efecto de "continuación de patrón": el proceso de denoising, al completar una franja de textura periódica, tiende a seguir el patrón hasta el borde de la región disponible en lugar de detenerse en una cantidad fija, igual que con los dientes o las columnas de un edificio.
- **El orden del proceso de difusión.** Los primeros pasos de denoising fijan composición y formas grandes; los últimos, el detalle fino. Me parece probable que a la escala de una mano de cuerpo entero, la mano "no existe" como estructura en los pasos tempranos (es solo una mancha color piel), y los pasos tardíos la rellenan con textura de dedos sin un plan global. Esto encaja con la evidencia, pero no recuerdo que esté demostrado como mecanismo.
- **Guidance alto empeora.** Sospecho que valores altos de classifier-free guidance, de uso común en 2022, exageraban rasgos "prototípicos" y empeoraban los artefactos repetitivos. Es intuición, no dato.
- **Sesgo de atención del público.** Parte del fenómeno fue social: una vez instalado el meme, la gente buscó las manos antes que nada, con lo cual el problema pareció más uniforme de lo que era. Esto es observación mía, no una explicación técnica.

## Resumen en una línea

Consenso: manos poco representadas y mal descriptas en los datos, modelos que generan textura local coherente sin restricción global de conteo, sin prior 3D, y en el caso de SD una resolución latente insuficiente para una mano chica. La prueba más sólida de ese diagnóstico es que los arreglos que funcionaron atacan exactamente esos puntos (pose/profundidad externa, mejores captions, más resolución, atención global). Lo demás que puse arriba es conjetura razonable, no hecho establecido.

Nota: contesté de memoria y sin herramientas, como pediste; fechas y nombres de versiones (Midjourney v5 en marzo 2023, DALL·E 3 en octubre 2023, HandRefiner a fines de 2023) los recuerdo con bastante confianza pero conviene verificarlos si vas a citarlos. No usé memoria del usuario para esto.
