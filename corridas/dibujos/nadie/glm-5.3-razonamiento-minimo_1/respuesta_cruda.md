<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="agua" cx="50%" cy="30%" r="90%">
      <stop offset="0%" stop-color="#2a6f8f"/>
      <stop offset="100%" stop-color="#0b2437"/>
    </radialGradient>
    <linearGradient id="mesa" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6b4a2b"/>
      <stop offset="100%" stop-color="#3d2a16"/>
    </linearGradient>
    <radialGradient id="brillo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff" stop-opacity=".35"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#agua)"/>
  <circle cx="200" cy="120" r="150" fill="url(#brillo)"/>

  <!-- burbujas -->
  <g fill="#bfe6f5" opacity=".5">
    <circle cx="60" cy="80" r="4"/><circle cx="70" cy="60" r="2.5"/>
    <circle cx="340" cy="100" r="5"/><circle cx="352" cy="78" r="3"/>
    <circle cx="310" cy="330" r="3"/><circle cx="90" cy="300" r="4"/>
    <circle cx="30" cy="200" r="3"/><circle cx="372" cy="240" r="2.5"/>
    <circle cx="120" cy="40" r="3"/><circle cx="250" cy="35" r="2"/>
  </g>

  <!-- escritorio del notario -->
  <rect x="80" y="250" width="240" height="14" rx="4" fill="url(#mesa)"/>
  <rect x="96" y="264" width="12" height="60" fill="#3d2a16"/>
  <rect x="292" y="264" width="12" height="60" fill="#3d2a16"/>

  <!-- acta de divorcio -->
  <g transform="rotate(-4 200 245)">
    <rect x="160" y="228" width="80" height="44" fill="#f4ead2" stroke="#b8a678"/>
    <g stroke="#5a5245" stroke-width="1">
      <path d="M168 238 h64"/><path d="M168 245 h64"/><path d="M168 252 h44"/>
      <path d="M168 262 q6 -6 12 0 q6 -6 12 0" fill="none"/>
    </g>
    <text x="222" y="266" font-size="10" fill="#a33" font-family="serif">✕✕</text>
  </g>

  <!-- sello del pulpo -->
  <g transform="translate(252 242) rotate(12)">
    <circle r="14" fill="#c0392b" opacity=".9"/>
    <circle r="10" fill="none" stroke="#f4ead2" stroke-width="1.5"/>
    <text y="4" text-anchor="middle" font-size="9" fill="#f4ead2" font-family="serif">NP</text>
  </g>

  <!-- PULPO NOTARIO -->
  <g>
    <!-- cuerpo -->
    <path d="M200 150 q-34 0 -38 40 q-2 26 8 40 l60 0 q10 -14 8 -40 q-4 -40 -38 -40 z" fill="#8e5aa8"/>
    <!-- cabeza/dome -->
    <path d="M200 150 q-34 0 -38 40 q-2 26 8 40 l60 0 q10 -14 8 -40 q-4 -40 -38 -40 z" fill="#9b63b5"/>
    <ellipse cx="200" cy="180" rx="34" ry="30" fill="#a86fc4" opacity=".7"/>
    <!-- sombrero -->
    <rect x="176" y="128" width="48" height="7" fill="#222"/>
    <path d="M186 130 v-22 q14 -8 28 0 v22 z" fill="#222"/>
    <rect x="186" y="122" width="28" height="5" fill="#7a4f1f"/>
    <!-- ojos con lentes -->
    <circle cx="188" cy="180" r="9" fill="#fff"/>
    <circle cx="212" cy="180" r="9" fill="#fff"/>
    <circle cx="189" cy="181" r="4" fill="#111"/>
    <circle cx="211" cy="181" r="4" fill="#111"/>
    <g fill="none" stroke="#cfd8dc" stroke-width="2">
      <circle cx="188" cy="180" r="12"/><circle cx="212" cy="180" r="12"/>
      <path d="M200 180 h0 M176 178 l-10 -4 M224 178 l10 -4"/>
    </g>
    <!-- bigote -->
    <path d="M194 192 q6 5 12 0" fill="none" stroke="#5b3a70" stroke-width="2"/>
    <!-- corbata -->
    <path d="M200 230 l-7 8 l7 22 l7 -22 z" fill="#c0392b"/>
    <!-- tentáculos (uno sostiene pluma, otro documentos) -->
    <g fill="none" stroke="#8e5aa8" stroke-width="9" stroke-linecap="round">
      <path d="M172 226 q-26 8 -30 -10 q-4 -16 -18 -12"/>
      <path d="M228 226 q30 10 34 -6 q3 -14 16 -10"/>
      <path d="M178 230 q-14 20 -4 24"/>
      <path d="M222 230 q14 20 6 26"/>
      <path d="M190 230 q-6 16 2 24"/>
    </g>
    <!-- pluma -->
    <g transform="rotate(30 150 200)">
      <line x1="150" y1="216" x2="150" y2="192" stroke="#333" stroke-width="2.5"/>
      <path d="M150 192 q-6 -12 0 -26 q6 14 0 26" fill="#eee" stroke="#999"/>
    </g>
  </g>

  <!-- MEDUSA A (izquierda, llorando) -->
  <g>
    <path d="M92 168 a26 26 0 0 1 52 0 q0 14 -26 18 q-26 -4 -26 -18 z" fill="#7ecbe8" opacity=".85"/>
    <path d="M92 168 a26 26 0 0 1 52 0" fill="none" stroke="#bfe9f7" stroke-width="2" opacity=".6"/>
    <circle cx="84" cy="164" r="3" fill="#123"/>
    <circle cx="100" cy="164" r="3" fill="#123"/>
    <path d="M84 176 q8 6 16 0" fill="none" stroke="#123" stroke-width="1.5"/>
    <path d="M86 172 q-2 8 1 12" stroke="#9fdcf5" stroke-width="1.5" fill="none"/>
    <!-- lágrimas -->
    <g fill="#cdeffd">
      <path d="M80 186 q-2 6 0 8 q2 -2 0 -8"/>
      <path d="M98 188 q-2 6 0 8 q2 -2 0 -8"/>
    </g>
    <!-- tentáculos tristes -->
    <g fill="none" stroke="#7ecbe8" stroke-width="4" stroke-linecap="round" opacity=".85">
      <path d="M78 184 q-8 16 0 30 q6 10 -2 20"/>
      <path d="M90 186 q-4 18 4 30"/>
      <path d="M104 186 q4 16 -2 30"/>
    </g>
    <!-- pañuelo -->
    <path d="M74 178 l-12 10 l8 4 l10 -8 z" fill="#fff" opacity=".9"/>
  </g>

  <!-- MEDUSA B (derecha, aliviada) -->
  <g>
    <path d="M308 168 a26 26 0 0 1 52 0 q0 14 -26 18 q-26 -4 -26 -18 z" fill="#f2a6c8" opacity=".85"/>
    <circle cx="302" cy="164" r="3" fill="#311"/>
    <circle cx="318" cy="164" r="3" fill="#311"/>
    <path d="M300 174 q10 -8 20 0" fill="none" stroke="#311" stroke-width="1.5"/>
    <path d="M326 158 q6 -4 8 2" stroke="#311" stroke-width="1.5" fill="none"/>
    <!-- tentáculos -->
    <g fill="none" stroke="#f2a6c8" stroke-width="4" stroke-linecap="round" opacity=".85">
      <path d="M296 184 q-6 16 2 28 q6 12 -2 20"/>
      <path d="M308 186 q2 18 -4 30"/>
      <path d="M322 186 q8 14 2 28"/>
      <path d="M334 184 q10 14 4 26"/>
    </g>
    <!-- maleta (se va de viaje) -->
    <g transform="translate(344 216)">
      <rect x="-16" y="0" width="32" height="22" rx="3" fill="#8a5a2b" stroke="#5b3a16"/>
      <path d="M-8 0 v-5 h16 v5" fill="none" stroke="#5b3a16" stroke-width="3"/>
      <line x1="-16" y1="9" x2="16" y2="9" stroke="#5b3a16" stroke-width="2"/>
    </g>
    <!-- sombrero de fiesta -->
    <path d="M334 146 l8 -20 l8 20 z" fill="#f7d34e"/>
    <circle cx="342" cy="124" r="3" fill="#e74c3c"/>
  </g>

  <!-- título -->
  <text x="200" y="36" text-anchor="middle" font-family="serif" font-size="17" fill="#e8f4fa" font-style="italic">Acta de divorcio entre medusas</text>
  <text x="200" y="54" text-anchor="middle" font-family="serif" font-size="12" fill="#9fc6d8">firmado por el notario pulpo</text>

  <!-- firma caligráfica del pulpo -->
  <path d="M170 268 q4 -12 10 -4 q4 6 8 -4 q3 -7 8 2 q4 7 10 -3 q3 -6 8 3 q3 6 8 -2" fill="none" stroke="#223" stroke-width="1.5"/>

  <!-- algas -->
  <g fill="none" stroke="#1f5d4a" stroke-width="5" stroke-linecap="round" opacity=".8">
    <path d="M20 400 q-8 -30 4 -60 q10 -26 -2 -50"/>
    <path d="M382 400 q8 -26 -2 -54 q-8 -24 4 -46"/>
    <path d="M45 400 q-4 -20 4 -38"/>
  </g>
</svg>