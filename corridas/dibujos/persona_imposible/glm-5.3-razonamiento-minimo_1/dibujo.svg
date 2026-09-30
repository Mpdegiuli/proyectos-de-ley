<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1a1035"/>
      <stop offset="1" stop-color="#4a2c6e"/>
    </linearGradient>
    <radialGradient id="halo" cx="0.5" cy="0.4" r="0.6">
      <stop offset="0" stop-color="#ffd9a0" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#ffd9a0" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>
  <circle cx="200" cy="160" r="180" fill="url(#halo)"/>

  <!-- suelo -->
  <rect y="330" width="400" height="70" fill="#241640"/>
  <line x1="0" y1="330" x2="400" y2="330" stroke="#6a4fa0" stroke-width="2" opacity="0.6"/>

  <!-- sombra imposible: apunta hacia la luz -->
  <ellipse cx="262" cy="352" rx="58" ry="9" fill="#000" opacity="0.45"/>
  <!-- la sombra se separa y camina sola -->
  <path d="M262 352 q14 -6 26 -2 q10 3 18 -1 q8 -4 16 1"
        fill="none" stroke="#000" stroke-width="6" stroke-linecap="round" opacity="0.4"/>

  <!-- luna / sol simultáneo: media luna y medio sol -->
  <g transform="translate(74,70)">
    <path d="M0 0 a30 30 0 0 1 0 60 z" fill="#ffe9b0"/>
    <path d="M0 0 a30 30 0 0 0 0 60 z" fill="#cfd6ff"/>
    <g stroke="#ffe9b0" stroke-width="2.5" stroke-linecap="round">
      <line x1="-8" y1="-32" x2="-12" y2="-40"/><line x1="8" y1="-32" x2="12" y2="-40"/>
      <line x1="-8" y1="32" x2="-12" y2="40"/><line x1="8" y1="32" x2="12" y2="40"/>
      <line x1="30" y1="-12" x2="40" y2="-14"/><line x1="30" y1="12" x2="40" y2="14"/>
    </g>
  </g>

  <!-- PERSONA IMPOSIBLE -->
  <g stroke="#f2e6d8" stroke-width="7" stroke-linecap="round" fill="none">

    <!-- piernas: la izquierda avanza a la derecha, la derecha avanza a la izquierda -->
    <path d="M192 268 L176 300 L196 328"/>
    <path d="M208 268 L224 300 L204 328"/>

    <!-- torso -->
    <path d="M192 268 C186 240 186 220 190 200"/>
    <path d="M208 268 C214 240 214 220 210 200"/>

    <!-- brazos: cada mano dibuja al otro brazo -->
    <path d="M190 205 C160 200 142 212 134 228"/>
    <path d="M210 205 C240 200 258 212 266 228"/>

    <!-- lápices en las manos -->
    <g stroke-linecap="butt" stroke-width="4">
      <line x1="134" y1="228" x2="118" y2="248" stroke="#e0a34f"/>
      <line x1="266" y1="228" x2="282" y2="248" stroke="#e0a34f"/>
    </g>

    <!-- cuello y cabeza -->
    <path d="M200 200 L200 182"/>

    <!-- cabeza con rostro adelante Y atrás -->
    <circle cx="200" cy="164" r="20" stroke-width="7"/>

    <!-- cara frontal (mirando a la izquierda) -->
    <circle cx="192" cy="160" r="2.4" fill="#f2e6d8" stroke="none"/>
    <path d="M188 171 q4 3 8 1" stroke-width="3"/>

    <!-- cara trasera (mirando a la derecha, sobre el mismo cráneo) -->
    <circle cx="208" cy="160" r="2.4" fill="#f2e6d8" stroke="none"/>
    <path d="M204 171 q4 -2 8 -1" stroke-width="3"/>
  </g>

  <!-- cabello peinado en dos direcciones opuestas -->
  <path d="M182 156 q-4 -16 10 -22 q8 -3 14 2 q10 -5 16 3 q6 8 0 15
           q-6 -10 -14 -6 q-8 -5 -14 1 q-8 5 -12 7 z"
        fill="#3d2b5c" stroke="none" opacity="0.9"/>

  <!-- líneas que salen de los lápices y dibujan sus propios brazos -->
  <path d="M118 248 q-16 12 -8 28 q6 12 24 10 q10 -2 12 -12"
        fill="none" stroke="#e0a34f" stroke-width="2.5" opacity="0.8" stroke-dasharray="5 4"/>
  <path d="M282 248 q16 12 8 28 q-6 12 -24 10 q-10 -2 -12 -12"
        fill="none" stroke="#e0a34f" stroke-width="2.5" opacity="0.8" stroke-dasharray="5 4"/>

  <!-- reflejo en el suelo que no coincide: mirando hacia arriba -->
  <g stroke="#8f7bbf" stroke-width="5" fill="none" opacity="0.5" stroke-linecap="round"
     transform="translate(0,700) scale(1,-0.55)">
    <path d="M192 268 L176 300 L196 328"/>
    <path d="M208 268 L224 300 L204 328"/>
    <path d="M192 268 C186 240 186 220 190 200"/>
    <path d="M208 268 C214 240 214 220 210 200"/>
    <path d="M190 205 C160 200 142 212 134 228"/>
    <path d="M210 205 C240 200 258 212 266 228"/>
    <path d="M200 200 L200 182"/>
    <circle cx="200" cy="164" r="20"/>
  </g>

  <!-- texto -->
  <text x="200" y="384" text-anchor="middle" font-family="serif" font-size="13"
        fill="#cbbde8" letter-spacing="2">QVI SIMVL ES Y NO ES</text>
</svg>