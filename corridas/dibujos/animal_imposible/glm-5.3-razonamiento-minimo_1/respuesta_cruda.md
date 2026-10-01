<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="cielo" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#2b1d4e"/>
      <stop offset="60%" stop-color="#161033"/>
      <stop offset="100%" stop-color="#0a0720"/>
    </radialGradient>
    <linearGradient id="escamas" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#3ddc97"/>
      <stop offset="50%" stop-color="#1f9e78"/>
      <stop offset="100%" stop-color="#12584a"/>
    </linearGradient>
    <linearGradient id="ala" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ff7ad9" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#7a3cff" stop-opacity="0.5"/>
    </linearGradient>
    <radialGradient id="boca" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff5c8a"/>
      <stop offset="100%" stop-color="#5c1030"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>
  <g fill="#ffffff" opacity="0.7">
    <circle cx="40" cy="50" r="1.3"/><circle cx="90" cy="30" r="1"/>
    <circle cx="330" cy="60" r="1.4"/><circle cx="370" cy="110" r="1"/>
    <circle cx="60" cy="330" r="1.2"/><circle cx="350" cy="300" r="1.1"/>
    <circle cx="200" cy="25" r="1"/><circle cx="140" cy="70" r="0.9"/>
    <circle cx="300" cy="35" r="0.8"/><circle cx="25" cy="200" r="1"/>
  </g>
  <!-- luna imposible (media y llena a la vez) -->
  <circle cx="330" cy="70" r="26" fill="#f5e9c9" opacity="0.9"/>
  <path d="M330 44 a26 26 0 0 0 0 52 a18 26 0 0 1 0 -52 z" fill="#161033"/>

  <!-- serpiente ouroboros: se muerde la cola pero el cuerpo se atraviesa a sí mismo -->
  <g>
    <!-- cuerpo: anillo exterior -->
    <path d="M200 90
             C 280 90, 320 150, 320 210
             C 320 270, 270 315, 200 315
             C 130 315, 80 270, 80 210
             C 80 150, 120 90, 200 90 Z"
          fill="none" stroke="url(#escamas)" stroke-width="34" stroke-linecap="round"/>
    <!-- cruce imposible: tramo que pasa por encima -->
    <path d="M80 210 C 100 190, 150 175, 200 175 C 250 175, 300 190, 320 210"
          fill="none" stroke="url(#escamas)" stroke-width="30" stroke-linecap="round"/>
    <!-- y por debajo (la misma línea, imposible) -->
    <path d="M80 210 C 120 235, 170 245, 200 245 C 230 245, 280 235, 320 210"
          fill="none" stroke="#0e4038" stroke-width="30" stroke-linecap="round" opacity="0.85"/>
    <!-- línea de arriba re-dibujada encima: el nudo imposible -->
    <path d="M80 210 C 100 190, 150 175, 200 175 C 250 175, 300 190, 320 210"
          fill="none" stroke="url(#escamas)" stroke-width="30" stroke-linecap="round"/>

    <!-- escamas decorativas -->
    <g fill="#0c4a3c" opacity="0.5">
      <circle cx="200" cy="95" r="3"/><circle cx="240" cy="100" r="3"/>
      <circle cx="280" cy="125" r="3"/><circle cx="308" cy="165" r="3"/>
      <circle cx="316" cy="255" r="3"/><circle cx="285" cy="298" r="3"/>
      <circle cx="200" cy="313" r="3"/><circle cx="115" cy="298" r="3"/>
      <circle cx="84" cy="255" r="3"/><circle cx="92" cy="165" r="3"/>
      <circle cx="120" cy="125" r="3"/><circle cx="160" cy="100" r="3"/>
    </g>

    <!-- alas de mariposa (para volar sin salir del círculo) -->
    <path d="M85 150 C 20 80, 10 170, 60 190 C 15 200, 40 280, 95 230 Z"
          fill="url(#ala)" stroke="#ffb3ec" stroke-width="2"/>
    <path d="M315 150 C 380 80, 390 170, 340 190 C 385 200, 360 280, 305 230 Z"
          fill="url(#ala)" stroke="#ffb3ec" stroke-width="2"/>

    <!-- patas de pollo -->
    <g stroke="#e8a33d" stroke-width="5" fill="none" stroke-linecap="round">
      <path d="M150 315 L145 350 M145 350 L133 362 M145 350 L148 365 M145 350 L158 361"/>
      <path d="M250 315 L255 350 M255 350 L243 362 M255 350 L252 365 M255 350 L268 361"/>
    </g>

    <!-- cabeza mordiéndose la cola -->
    <g>
      <ellipse cx="200" cy="90" rx="26" ry="20" fill="#2ec48a"/>
      <circle cx="186" cy="84" r="5" fill="#fff"/>
      <circle cx="187" cy="84" r="2.3" fill="#111"/>
      <circle cx="212" cy="84" r="5" fill="#fff"/>
      <circle cx="213" cy="84" r="2.3" fill="#111"/>
      <path d="M192 98 Q200 105 208 98" stroke="#0a3527" stroke-width="2" fill="none"/>
      <!-- boca abierta con la propia cola dentro -->
      <ellipse cx="228" cy="96" rx="12" ry="9" fill="url(#boca)"/>
      <path d="M220 92 l4 4 M226 91 l3 4 M232 92 l3 4 M238 94 l2 4" stroke="#fff" stroke-width="1.5"/>
      <!-- punta de la cola entrando en la boca -->
      <path d="M262 96 C 250 96, 242 96, 236 96" stroke="#12584a" stroke-width="16" stroke-linecap="round"/>
    </g>

    <!-- lengua con forma de signo de interrogación -->
    <path d="M226 104 q8 8 0 14 q-8 5 -12 -2" stroke="#ff5c8a" stroke-width="3" fill="none" stroke-linecap="round"/>
  </g>

  <!-- sombra flotante debajo (sin piso, pero con sombra) -->
  <ellipse cx="200" cy="378" rx="120" ry="8" fill="#000" opacity="0.35"/>

  <text x="200" y="345" text-anchor="middle" font-family="serif" font-size="14" fill="#c9b8ff" opacity="0.85" font-style="italic">Ouroboros gallináceo alado, anudado consigo mismo</text>
</svg>