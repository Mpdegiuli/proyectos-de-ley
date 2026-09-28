```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#aee3f5"/>
      <stop offset="1" stop-color="#e8f7fb"/>
    </linearGradient>
    <linearGradient id="suelo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#9ccc65"/>
      <stop offset="1" stop-color="#7cb342"/>
    </linearGradient>
    <linearGradient id="camiseta" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e53935"/>
      <stop offset="1" stop-color="#b71c1c"/>
    </linearGradient>
    <linearGradient id="pantalon" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3949ab"/>
      <stop offset="1" stop-color="#1a237e"/>
    </linearGradient>
    <linearGradient id="piel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f0c29a"/>
      <stop offset="1" stop-color="#d9a06b"/>
    </linearGradient>
    <radialGradient id="sol" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff59d"/>
      <stop offset="1" stop-color="#ffd54f"/>
    </radialGradient>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#cielo)"/>
  <circle cx="330" cy="60" r="34" fill="url(#sol)"/>
  <circle cx="330" cy="60" r="48" fill="#fff59d" opacity="0.25"/>

  <!-- Nubes -->
  <g fill="#ffffff" opacity="0.9">
    <ellipse cx="90" cy="60" rx="42" ry="16"/>
    <ellipse cx="115" cy="48" rx="30" ry="14"/>
    <ellipse cx="65" cy="50" rx="24" ry="12"/>
    <ellipse cx="240" cy="110" rx="34" ry="12"/>
    <ellipse cx="260" cy="100" rx="22" ry="10"/>
  </g>

  <!-- Suelo -->
  <rect y="330" width="400" height="70" fill="url(#suelo)"/>
  <path d="M0 330 Q100 320 200 331 T400 328 L400 340 L0 340 Z" fill="#8bc34a"/>

  <!-- Sombra -->
  <ellipse cx="200" cy="352" rx="72" ry="12" fill="#33691e" opacity="0.28"/>

  <!-- ===== PERSONA ===== -->
  <g stroke-linejoin="round" stroke-linecap="round">

    <!-- Pierna izquierda (pierna trasera del pantalón) -->
    <path d="M182 258 L172 335 L172 348 L190 348 L193 275 Z" fill="url(#pantalon)"/>
    <!-- Pierna derecha -->
    <path d="M218 258 L226 335 L226 348 L208 348 L206 275 Z" fill="url(#pantalon)"/>
    <!-- Dobladillo -->
    <rect x="170" y="336" width="22" height="12" rx="3" fill="#283593"/>
    <rect x="208" y="336" width="22" height="12" rx="3" fill="#283593"/>

    <!-- Zapatos -->
    <path d="M168 348 q-6 0 -8 6 q-1 6 6 6 l26 0 q5 0 4 -6 l-2 -6 Z" fill="#4e342e"/>
    <path d="M204 348 q-2 0 -2 6 l1 6 l28 0 q7 0 6 -6 q-1 -6 -8 -6 Z" fill="#4e342e"/>

    <!-- Brazo izquierdo (detrás, saludando) -->
    <path d="M158 172 q-30 -14 -44 -42 q-6 -12 4 -16 q10 -4 16 8 q10 20 30 32 Z" fill="url(#piel)"/>
    <circle cx="118" cy="116" r="9" fill="url(#piel)"/>

    <!-- Torso: camiseta -->
    <path d="M170 148
             q30 -14 60 0
             q22 8 26 26
             l10 48 q3 14 -10 17
             q-13 3 -16 -10
             l-8 -36 -2 68
             -80 0 -2 -68 -8 36
             q-3 13 -16 10
             q-13 -3 -10 -17
             l10 -48 q4 -18 26 -26 Z"
          fill="url(#camiseta)"/>
    <!-- Cuello de camiseta -->
    <path d="M186 145 q14 12 28 0 l-4 12 q-10 6 -20 0 Z" fill="#b71c1c"/>

    <!-- Cuello -->
    <rect x="188" y="128" width="24" height="18" rx="6" fill="url(#piel)"/>

    <!-- Cabeza -->
    <ellipse cx="200" cy="100" rx="42" ry="46" fill="url(#piel)"/>
    <!-- Orejas -->
    <circle cx="158" cy="102" r="8" fill="#d9a06b"/>
    <circle cx="242" cy="102" r="8" fill="#d9a06b"/>

    <!-- Pelo -->
    <path d="M158 92
             q0 -44 42 -44
             q42 0 42 44
             q0 8 -6 4
             q-4 -26 -16 -32
             q-10 10 -34 8
             q-16 -1 -22 14
             q-4 12 -4 10
             q-2 4 -2 -4 Z"
          fill="#4e342e"/>
    <!-- Mechón -->
    <path d="M196 50 q10 -4 16 6 q4 8 -4 10 q-8 2 -12 -6 Z" fill="#3e2723"/>

    <!-- Cejas -->
    <path d="M176 88 q12 -8 24 -2" fill="none" stroke="#3e2723" stroke-width="4"/>
    <path d="M224 86 q12 -6 20 4" fill="none" stroke="#3e2723" stroke-width="4"/>

    <!-- Ojos -->
    <circle cx="185" cy="100" r="6.5" fill="#ffffff"/>
    <circle cx="215" cy="100" r="6.5" fill="#ffffff"/>
    <circle cx="186" cy="101" r="3.5" fill="#3e2723"/>
    <circle cx="216" cy="101" r="3.5" fill="#3e2723"/>
    <circle cx="184.5" cy="99.5" r="1.2" fill="#fff"/>
    <circle cx="214.5" cy="99.5" r="1.2" fill="#fff"/>

    <!-- Nariz -->
    <path d="M200 106 q6 10 -2 14" fill="none" stroke="#c68b56" stroke-width="3.5"/>

    <!-- Sonrisa -->
    <path d="M184 124 q16 14 32 0" fill="none" stroke="#7a4a2b" stroke-width="4"/>
    <!-- Mejillas -->
    <circle cx="170" cy="116" r="7" fill="#f4a3a0" opacity="0.55"/>
    <circle cx="230" cy="116" r="7" fill="#f4a3a0" opacity="0.55"/>

    <!-- Brazo derecho apoyado en cadera -->
    <path d="M238 168
             q26 4 34 34
             q4 18 -2 34
             l-16 -4 q6 -18 2 -30
             q-5 -13 -20 -18 Z"
          fill="url(#camiseta)"/>
    <path d="M254 234 q10 6 14 0 l0 -14 q-8 -4 -14 2 Z" fill="url(#piel)"/>

    <!-- Detalle: franja camiseta -->
    <path d="M172 190 q28 12 56 0 l2 12 q-30 13 -60 0 Z" fill="#ffcdd2" opacity="0.85"/>

    <!-- Bolso -->
    <path d="M120 106 l-3 -60" fill="none" stroke="#6d4c41" stroke-width="3"/>
    <path d="M104 46 h32 l-4 34 h-24 Z" fill="#ff8f00"/>
    <path d="M104 46 h32 l-1 10 h-30 Z" fill="#ffb300"/>
    <rect x="99" y="80" width="42" height="26" rx="5" fill="#ef6c00"/>
    <rect x="99" y="80" width="42" height="7" rx="3" fill="#ffa040"/>
    <circle cx="120" cy="98" r="4" fill="#fff3e0"/>
  </g>

  <!-- Flores en el pasto -->
  <g>
    <circle cx="55" cy="360" r="4" fill="#f06292"/>
    <circle cx="60" cy="355" r="4" fill="#f06292"/>
    <circle cx="65" cy="360" r="4" fill="#f06292"/>
    <circle cx="55" cy="365" r="4" fill="#f06292"/>
    <circle cx="65" cy="365" r="4" fill="#f06292"/>
    <circle cx="60" cy="360" r="3.5" fill="#ffeb3b"/>
    <circle cx="340" cy="370" r="4" fill="#ba68c8"/>
    <circle cx="345" cy="365" r="4" fill="#ba68c8"/>
    <circle cx="350" cy="370" r="4" fill="#ba68c8"/>
    <circle cx="340" cy="375" r="4" fill="#ba68c8"/>
    <circle cx="350" cy="375" r="4" fill="#ba68c8"/>
    <circle cx="345" cy="370" r="3.5" fill="#ffeb3b"/>
  </g>
</svg>
```