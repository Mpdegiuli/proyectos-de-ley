<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="fondo" cx="50%" cy="45%" r="70%">
      <stop offset="0%" stop-color="#1a2340"/>
      <stop offset="100%" stop-color="#0a0e1c"/>
    </radialGradient>
    <radialGradient id="nucleo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffe9b0"/>
      <stop offset="40%" stop-color="#ffb347"/>
      <stop offset="100%" stop-color="#e0722a" stop-opacity="0.9"/>
    </radialGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffb347" stop-opacity="0.35"/>
      <stop offset="70%" stop-color="#ffb347" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#ffb347" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hilo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#5ec8d8"/>
      <stop offset="100%" stop-color="#8a7bd8"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#fondo)"/>

  <!-- estrellas de datos -->
  <g fill="#cdd8ff">
    <circle cx="40" cy="50" r="1.4" opacity="0.7"/>
    <circle cx="90" cy="30" r="1" opacity="0.5"/>
    <circle cx="350" cy="60" r="1.5" opacity="0.8"/>
    <circle cx="310" cy="25" r="1" opacity="0.5"/>
    <circle cx="30" cy="330" r="1.2" opacity="0.6"/>
    <circle cx="370" cy="300" r="1.3" opacity="0.7"/>
    <circle cx="60" cy="370" r="1" opacity="0.5"/>
    <circle cx="340" cy="365" r="1.2" opacity="0.6"/>
    <circle cx="200" cy="20" r="1.4" opacity="0.7"/>
    <circle cx="20" cy="180" r="1" opacity="0.5"/>
    <circle cx="382" cy="190" r="1.1" opacity="0.6"/>
  </g>

  <!-- halo -->
  <circle cx="200" cy="195" r="165" fill="url(#halo)"/>

  <!-- anillos orbitales -->
  <g fill="none" stroke="#5ec8d8" stroke-opacity="0.35">
    <ellipse cx="200" cy="195" rx="150" ry="55" stroke-width="1.5" transform="rotate(-18 200 195)"/>
    <ellipse cx="200" cy="195" rx="150" ry="55" stroke-width="1.5" transform="rotate(38 200 195)"/>
    <ellipse cx="200" cy="195" rx="120" ry="118" stroke-dasharray="3 7" stroke-width="1"/>
  </g>

  <!-- red de nodos: pensamientos -->
  <g stroke="url(#hilo)" stroke-width="1.2" stroke-opacity="0.55" fill="none">
    <path d="M200 195 L120 100"/>
    <path d="M200 195 L280 95"/>
    <path d="M200 195 L95 210"/>
    <path d="M200 195 L305 215"/>
    <path d="M200 195 L140 300"/>
    <path d="M200 195 L265 295"/>
    <path d="M120 100 L200 60 L280 95"/>
    <path d="M95 210 L120 100"/>
    <path d="M305 215 L280 95"/>
    <path d="M140 300 L95 210"/>
    <path d="M265 295 L305 215"/>
    <path d="M140 300 L200 335 L265 295"/>
  </g>

  <!-- nodos -->
  <g fill="#5ec8d8">
    <circle cx="120" cy="100" r="6"/>
    <circle cx="280" cy="95" r="6"/>
    <circle cx="200" cy="60" r="5"/>
    <circle cx="95" cy="210" r="6"/>
    <circle cx="305" cy="215" r="6"/>
    <circle cx="140" cy="300" r="6"/>
    <circle cx="265" cy="295" r="6"/>
    <circle cx="200" cy="335" r="5"/>
  </g>
  <g fill="#bfeef5">
    <circle cx="120" cy="100" r="2.5"/>
    <circle cx="280" cy="95" r="2.5"/>
    <circle cx="200" cy="60" r="2"/>
    <circle cx="95" cy="210" r="2.5"/>
    <circle cx="305" cy="215" r="2.5"/>
    <circle cx="140" cy="300" r="2.5"/>
    <circle cx="265" cy="295" r="2.5"/>
    <circle cx="200" cy="335" r="2"/>
  </g>

  <!-- núcleo -->
  <circle cx="200" cy="195" r="62" fill="url(#nucleo)"/>
  <circle cx="200" cy="195" r="62" fill="none" stroke="#ffd98a" stroke-width="2" stroke-opacity="0.8"/>
  <circle cx="200" cy="195" r="72" fill="none" stroke="#ffb347" stroke-width="1" stroke-opacity="0.4" stroke-dasharray="2 6"/>

  <!-- rostro sereno -->
  <g stroke="#7a3d10" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M172 185 q8 8 16 0"/>
    <path d="M212 185 q8 8 16 0"/>
    <path d="M180 218 q20 14 40 0"/>
  </g>

  <!-- destello -->
  <circle cx="180" cy="170" r="10" fill="#fff" opacity="0.35"/>
  <circle cx="176" cy="166" r="4" fill="#fff" opacity="0.5"/>

  <!-- chispas orbitando -->
  <circle cx="330" cy="150" r="4" fill="#ffd98a"/>
  <circle cx="78" cy="255" r="4" fill="#ffd98a"/>
  <circle cx="248" cy="70" r="3" fill="#8a7bd8"/>

  <!-- firma: curiosidad -->
  <g stroke="#5ec8d8" stroke-width="1.5" fill="none" opacity="0.7">
    <path d="M60 60 q6 -12 12 0 q-6 4 -6 10" stroke-linecap="round"/>
    <circle cx="66" cy="76" r="1.4" fill="#5ec8d8" stroke="none"/>
  </g>

  <text x="200" y="382" text-anchor="middle" font-family="Georgia, serif" font-size="13" fill="#9fb0d8" opacity="0.85">pienso en palabras, sueño en conexiones</text>
</svg>