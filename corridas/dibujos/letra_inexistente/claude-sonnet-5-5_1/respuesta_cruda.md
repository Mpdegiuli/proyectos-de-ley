<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1b1030"/>
      <stop offset="1" stop-color="#3a1c4f"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd27a"/>
      <stop offset="1" stop-color="#ff6f61"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="1" fill="#ffffff" opacity="0.08"/>
    </pattern>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#dots)"/>

  <!-- guías tipográficas -->
  <g stroke="#ffffff" stroke-opacity="0.18" stroke-width="1" stroke-dasharray="4 4">
    <line x1="30" y1="90" x2="370" y2="90"/>
    <line x1="30" y1="170" x2="370" y2="170"/>
    <line x1="30" y1="300" x2="370" y2="300"/>
    <line x1="30" y1="350" x2="370" y2="350"/>
  </g>
  <g fill="#ffffff" fill-opacity="0.35" font-family="monospace" font-size="9">
    <text x="32" y="86">ascendente</text>
    <text x="32" y="166">altura x</text>
    <text x="32" y="296">base</text>
    <text x="32" y="346">descendente</text>
  </g>

  <!-- la letra -->
  <g fill="none" stroke="url(#ink)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)">
    <!-- tallo con ascendente que se curva hacia la izquierda -->
    <path d="M230 110 C190 90 150 110 150 150 L150 270 C150 300 170 310 190 300"/>
    <!-- bucle central que cruza el tallo -->
    <path d="M150 215 C190 160 270 170 270 225 C270 280 200 280 200 235 C200 205 250 200 290 240"/>
    <!-- descendente en espiral -->
    <path d="M270 225 L270 320 C270 355 225 360 220 330 C217 312 240 308 244 322"/>
  </g>

  <!-- puntos diacríticos inventados -->
  <g fill="#7ff0d4" filter="url(#glow)">
    <circle cx="300" cy="120" r="9"/>
    <path d="M325 150 l10 -18 l10 18 z"/>
  </g>

  <!-- marca de trazo -->
  <g fill="#ffffff" fill-opacity="0.9">
    <circle cx="230" cy="110" r="4"/>
    <circle cx="244" cy="322" r="4"/>
  </g>
  <g stroke="#7ff0d4" stroke-width="1.5" fill="none" stroke-opacity="0.8">
    <path d="M300 135 L300 165 M290 165 L310 165"/>
  </g>

  <text x="200" y="385" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="16" fill="#ffd27a" fill-opacity="0.85">ʃꙮ · «zhoa»</text>
</svg>