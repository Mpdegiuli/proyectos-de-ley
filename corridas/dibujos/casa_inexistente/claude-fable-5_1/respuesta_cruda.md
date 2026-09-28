<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2b1055"/>
      <stop offset="0.5" stop-color="#7597de"/>
      <stop offset="1" stop-color="#ffd9a0"/>
    </linearGradient>
    <radialGradient id="luna" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fffbe6"/>
      <stop offset="0.7" stop-color="#ffe9b0"/>
      <stop offset="1" stop-color="#ffe9b0" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="pared" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#c9b8e8"/>
      <stop offset="1" stop-color="#8a6fc0"/>
    </linearGradient>
    <linearGradient id="techo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff8fa3"/>
      <stop offset="1" stop-color="#c9184a"/>
    </linearGradient>
    <linearGradient id="isla" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5fbf6e"/>
      <stop offset="0.3" stop-color="#3e8e50"/>
      <stop offset="1" stop-color="#4a3728"/>
    </linearGradient>
    <radialGradient id="ventluz" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff3b0"/>
      <stop offset="1" stop-color="#f4a261"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <!-- estrellas -->
  <g fill="#fff">
    <circle cx="40" cy="40" r="1.6"/><circle cx="90" cy="25" r="1.1"/>
    <circle cx="150" cy="50" r="1.4"/><circle cx="230" cy="30" r="1.2"/>
    <circle cx="330" cy="45" r="1.6"/><circle cx="370" cy="90" r="1.1"/>
    <circle cx="60" cy="95" r="1.2"/><circle cx="290" cy="70" r="1"/>
    <circle cx="200" cy="15" r="1.3"/><circle cx="20" cy="140" r="1"/>
  </g>

  <!-- luna -->
  <circle cx="330" cy="70" r="45" fill="url(#luna)"/>
  <circle cx="330" cy="70" r="24" fill="#fff8dc"/>
  <circle cx="322" cy="64" r="5" fill="#f0e4b8"/>
  <circle cx="338" cy="78" r="3.5" fill="#f0e4b8"/>

  <!-- isla flotante -->
  <g>
    <path d="M110 285 Q200 265 290 285 Q285 330 255 355 Q225 385 200 375 Q160 380 135 345 Q112 315 110 285 Z" fill="url(#isla)"/>
    <path d="M110 285 Q200 262 290 285 Q200 305 110 285 Z" fill="#6ccc7c"/>
    <!-- raíces colgantes -->
    <path d="M170 368 q-4 14 3 22" stroke="#3a2b1f" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M215 372 q5 12 -2 20" stroke="#3a2b1f" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M240 358 q8 10 4 18" stroke="#3a2b1f" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  </g>

  <!-- rocas flotando alrededor -->
  <g fill="#5a4a3a">
    <ellipse cx="80" cy="330" rx="14" ry="9"/>
    <ellipse cx="325" cy="315" rx="11" ry="7"/>
    <ellipse cx="350" cy="255" rx="7" ry="5"/>
    <ellipse cx="55" cy="250" rx="8" ry="5"/>
  </g>
  <g fill="#79c47f">
    <path d="M66 326 q14 -7 28 0 l-4 -6 -20 0 z"/>
    <path d="M314 311 q11 -5 22 0 l-3 -5 -16 0 z"/>
  </g>

  <!-- escaleras al cielo -->
  <g fill="#e8d5a3" stroke="#b09b6a" stroke-width="1">
    <rect x="118" y="255" width="34" height="8" rx="2"/>
    <rect x="98" y="230" width="34" height="8" rx="2" transform="rotate(-6 115 234)"/>
    <rect x="80" y="203" width="34" height="8" rx="2" transform="rotate(-12 97 207)"/>
    <rect x="66" y="174" width="34" height="8" rx="2" transform="rotate(-18 83 178)"/>
    <rect x="58" y="143" width="34" height="8" rx="2" transform="rotate(-24 75 147)"/>
  </g>
  <!-- puerta flotante al final de la escalera -->
  <g transform="rotate(-10 70 105)">
    <rect x="52" y="78" width="36" height="56" rx="16" fill="#5e3b8c" stroke="#e8d5a3" stroke-width="2.5"/>
    <circle cx="80" cy="108" r="2.5" fill="#ffd166"/>
  </g>

  <!-- casa torcida -->
  <g>
    <!-- cuerpo principal, inclinado -->
    <path d="M150 285 L160 175 L250 168 L256 283 Z" fill="url(#pared)" stroke="#5e4a8a" stroke-width="2"/>
    <!-- piso superior más ancho, desafiando gravedad -->
    <path d="M148 178 L156 122 L262 116 L266 172 Z" fill="#e3d3f7" stroke="#5e4a8a" stroke-width="2"/>
    <!-- techo invertido (embudo) -->
    <path d="M138 122 L200 62 L272 116 Z" fill="url(#techo)" stroke="#8c1236" stroke-width="2" stroke-linejoin="round"/>
    <path d="M138 122 L272 116 L264 128 L146 132 Z" fill="#a4133c"/>
    <!-- torrecita sobre el techo, invertida -->
    <path d="M186 62 L214 62 L206 20 L194 20 Z" fill="#8a6fc0" stroke="#5e4a8a" stroke-width="2"/>
    <circle cx="200" cy="16" r="8" fill="#ffd166" stroke="#e09f3e" stroke-width="2"/>
    <!-- chimenea que sale de lado, humo en espiral -->
    <rect x="246" y="80" width="14" height="26" fill="#a4133c" transform="rotate(35 253 93)"/>
    <path d="M270 70 q14 -10 6 -20 q-8 -8 2 -16 q10 -7 4 -16" stroke="#e6e6fa" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.85"/>

    <!-- puerta en el piso de arriba (sin escalera) -->
    <rect x="176" y="132" width="26" height="40" rx="12" fill="#5e3b8c" stroke="#3f2a63" stroke-width="2"/>
    <circle cx="196" cy="154" r="2.2" fill="#ffd166"/>
    <!-- alfombrita voladora bajo esa puerta -->
    <path d="M170 180 q19 -7 38 0 q-19 7 -38 0 Z" fill="#e07a5f" stroke="#b85c47" stroke-width="1.5"/>

    <!-- ventanas de formas raras -->
    <circle cx="230" cy="148" r="13" fill="url(#ventluz)" stroke="#5e4a8a" stroke-width="2.5"/>
    <path d="M230 135 v26 M217 148 h26" stroke="#5e4a8a" stroke-width="2"/>
    <path d="M180 200 l16 -6 4 18 -16 6 Z" fill="url(#ventluz)" stroke="#5e4a8a" stroke-width="2.5"/>
    <ellipse cx="228" cy="238" rx="10" ry="15" fill="url(#ventluz)" stroke="#5e4a8a" stroke-width="2.5" transform="rotate(15 228 238)"/>
    <!-- ventana triangular en el techo -->
    <path d="M200 108 l-11 -14 22 -1 Z" fill="url(#ventluz)" stroke="#8c1236" stroke-width="2"/>

    <!-- puerta principal, de costado en la pared -->
    <g transform="rotate(-90 168 262)">
      <rect x="152" y="240" width="30" height="44" rx="14" fill="#ff9f1c" stroke="#c76f00" stroke-width="2.5"/>
      <circle cx="176" cy="264" r="2.5" fill="#5e3b8c"/>
    </g>
  </g>

  <!-- árbol que crece hacia abajo desde la isla -->
  <path d="M285 340 q4 20 -6 34" stroke="#4a3728" stroke-width="6" fill="none" stroke-linecap="round"/>
  <circle cx="279" cy="382" r="14" fill="#6ccc7c"/>
  <circle cx="292" cy="374" r="10" fill="#5fbf6e"/>
  <circle cx="268" cy="372" r="9" fill="#79c47f"/>

  <!-- farolito colgando de la isla -->
  <line x1="140" y1="352" x2="140" y2="372" stroke="#3a2b1f" stroke-width="2"/>
  <circle cx="140" cy="379" r="7" fill="#ffd166" stroke="#e09f3e" stroke-width="2"/>
  <circle cx="140" cy="379" r="12" fill="#ffd166" opacity="0.25"/>

  <!-- pajaritos -->
  <path d="M95 120 q6 -6 12 0 q6 -6 12 0" stroke="#2b1055" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M300 170 q5 -5 10 0 q5 -5 10 0" stroke="#2b1055" stroke-width="2" fill="none" stroke-linecap="round"/>
</svg>