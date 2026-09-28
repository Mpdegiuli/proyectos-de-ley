<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="cielo" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#1a2a4a"/>
      <stop offset="60%" stop-color="#0d1530"/>
      <stop offset="100%" stop-color="#060a1a"/>
    </radialGradient>
    <radialGradient id="mundo" cx="40%" cy="35%" r="80%">
      <stop offset="0%" stop-color="#3a7bd5"/>
      <stop offset="55%" stop-color="#1e4a8a"/>
      <stop offset="100%" stop-color="#0f2447"/>
    </radialGradient>
    <radialGradient id="brillo" cx="35%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="grieta" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ff9a56"/>
      <stop offset="100%" stop-color="#ffd166"/>
    </linearGradient>
  </defs>

  <!-- fondo nocturno -->
  <rect width="400" height="400" fill="url(#cielo)"/>

  <!-- estrellas -->
  <g fill="#ffffff">
    <circle cx="30" cy="40" r="1.2" opacity="0.8"/>
    <circle cx="80" cy="25" r="0.8" opacity="0.6"/>
    <circle cx="140" cy="50" r="1" opacity="0.7"/>
    <circle cx="210" cy="30" r="1.3" opacity="0.9"/>
    <circle cx="290" cy="45" r="0.9" opacity="0.6"/>
    <circle cx="350" cy="28" r="1.1" opacity="0.8"/>
    <circle cx="375" cy="70" r="0.8" opacity="0.5"/>
    <circle cx="45" cy="90" r="0.9" opacity="0.6"/>
    <circle cx="330" cy="110" r="1" opacity="0.7"/>
    <circle cx="20" cy="160" r="0.8" opacity="0.5"/>
    <circle cx="380" cy="180" r="0.9" opacity="0.6"/>
    <circle cx="25" cy="300" r="1" opacity="0.6"/>
    <circle cx="370" cy="330" r="1.1" opacity="0.7"/>
    <circle cx="60" cy="360" r="0.8" opacity="0.5"/>
    <circle cx="340" cy="375" r="0.9" opacity="0.6"/>
    <circle cx="180" cy="15" r="0.9" opacity="0.7"/>
  </g>

  <!-- halo del mundo -->
  <circle cx="200" cy="200" r="125" fill="none" stroke="#4a90d9" stroke-width="18" opacity="0.12"/>
  <circle cx="200" cy="200" r="118" fill="none" stroke="#4a90d9" stroke-width="6" opacity="0.2"/>

  <!-- el mundo -->
  <circle cx="200" cy="200" r="110" fill="url(#mundo)"/>

  <!-- continentes imaginarios -->
  <g fill="#2f9e6e" opacity="0.85">
    <path d="M150 130 q20 -18 45 -10 q18 6 12 24 q-6 16 -28 14 q-10 12 -26 6 q-18 -8 -12 -22 q4 -9 9 -12z"/>
    <path d="M235 165 q22 -6 34 8 q10 12 2 26 q-10 16 -28 10 q-16 -6 -16 -22 q0 -14 8 -22z"/>
    <path d="M130 210 q16 -4 24 8 q8 14 -2 28 q-8 12 -24 8 q-16 -6 -14 -22 q2 -16 16 -22z"/>
    <path d="M190 255 q26 -10 42 4 q12 12 2 24 q-14 14 -34 8 q-18 -6 -18 -20 q0 -10 8 -16z"/>
    <path d="M255 235 q12 -2 16 8 q4 10 -6 16 q-12 6 -18 -4 q-4 -12 8 -20z"/>
  </g>

  <!-- grietas del mundo, con luz saliendo -->
  <g stroke="url(#grieta)" fill="none" stroke-linecap="round">
    <path d="M175 100 q10 30 -5 55 q-12 22 2 45" stroke-width="2.5" opacity="0.9"/>
    <path d="M240 120 q-8 25 8 45" stroke-width="2" opacity="0.7"/>
    <path d="M160 260 q18 12 40 8" stroke-width="2" opacity="0.7"/>
  </g>

  <!-- brotes verdes creciendo de las grietas -->
  <g stroke="#7ee08a" stroke-width="2" fill="none" stroke-linecap="round">
    <path d="M172 198 q-2 -14 -10 -20"/>
    <path d="M172 198 q4 -12 12 -16"/>
    <path d="M248 165 q2 -12 10 -16"/>
    <path d="M200 268 q2 -10 10 -13"/>
  </g>
  <g fill="#7ee08a">
    <ellipse cx="161" cy="176" rx="4" ry="2.5" transform="rotate(-35 161 176)"/>
    <ellipse cx="185" cy="180" rx="4" ry="2.5" transform="rotate(30 185 180)"/>
    <ellipse cx="259" cy="147" rx="4" ry="2.5" transform="rotate(35 259 147)"/>
    <ellipse cx="211" cy="253" rx="4" ry="2.5" transform="rotate(25 211 253)"/>
  </g>

  <!-- brillo atmosférico -->
  <circle cx="200" cy="200" r="110" fill="url(#brillo)"/>

  <!-- red de conexiones humanas alrededor -->
  <g stroke="#ffd166" stroke-width="1" opacity="0.55" fill="none">
    <path d="M110 105 Q60 60 90 40"/>
    <path d="M290 105 Q340 55 315 35"/>
    <path d="M105 295 Q55 335 75 365"/>
    <path d="M295 295 Q350 340 330 368"/>
    <path d="M90 40 Q200 -10 315 35"/>
    <path d="M75 365 Q200 415 330 368"/>
    <path d="M90 40 Q20 200 75 365"/>
    <path d="M315 35 Q385 200 330 368"/>
  </g>

  <!-- puntos de luz: personas -->
  <g>
    <circle cx="90" cy="40" r="4.5" fill="#ffd166"/>
    <circle cx="90" cy="40" r="8" fill="#ffd166" opacity="0.25"/>
    <circle cx="315" cy="35" r="4.5" fill="#ffd166"/>
    <circle cx="315" cy="35" r="8" fill="#ffd166" opacity="0.25"/>
    <circle cx="75" cy="365" r="4.5" fill="#ffd166"/>
    <circle cx="75" cy="365" r="8" fill="#ffd166" opacity="0.25"/>
    <circle cx="330" cy="368" r="4.5" fill="#ffd166"/>
    <circle cx="330" cy="368" r="8" fill="#ffd166" opacity="0.25"/>
    <circle cx="110" cy="105" r="3" fill="#ffe9a8"/>
    <circle cx="290" cy="105" r="3" fill="#ffe9a8"/>
    <circle cx="105" cy="295" r="3" fill="#ffe9a8"/>
    <circle cx="295" cy="295" r="3" fill="#ffe9a8"/>
  </g>

  <!-- pequeña luna testigo -->
  <g>
    <circle cx="345" cy="80" r="14" fill="#e8e8f0"/>
    <circle cx="350" cy="76" r="3" fill="#c9c9d8"/>
    <circle cx="341" cy="85" r="2" fill="#c9c9d8"/>
  </g>

  <!-- cometa de esperanza -->
  <g opacity="0.85">
    <path d="M55 130 L95 118" stroke="#ffffff" stroke-width="1.5" opacity="0.5"/>
    <path d="M60 136 L95 122" stroke="#ffffff" stroke-width="1" opacity="0.3"/>
    <circle cx="97" cy="119" r="3" fill="#ffffff"/>
  </g>
</svg>