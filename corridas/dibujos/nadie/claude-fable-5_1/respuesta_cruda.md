<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1a1a3e"/>
      <stop offset="0.6" stop-color="#4a3b6b"/>
      <stop offset="1" stop-color="#c96f4a"/>
    </linearGradient>
    <radialGradient id="luz" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff7c0" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#fff7c0" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="haz" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffe98a" stop-opacity="0.75"/>
      <stop offset="1" stop-color="#ffe98a" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="caparazon" cx="0.4" cy="0.4" r="0.7">
      <stop offset="0" stop-color="#e8a86a"/>
      <stop offset="1" stop-color="#9c5a2e"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <circle cx="320" cy="70" r="26" fill="#f5edd8"/>
  <circle cx="312" cy="64" r="5" fill="#d9cdb2" opacity="0.6"/>
  <circle cx="328" cy="78" r="4" fill="#d9cdb2" opacity="0.6"/>
  <circle cx="322" cy="58" r="3" fill="#d9cdb2" opacity="0.5"/>

  <circle cx="60" cy="50" r="1.5" fill="#fff" opacity="0.9"/>
  <circle cx="110" cy="80" r="1.2" fill="#fff" opacity="0.7"/>
  <circle cx="180" cy="40" r="1.6" fill="#fff" opacity="0.8"/>
  <circle cx="240" cy="95" r="1" fill="#fff" opacity="0.6"/>
  <circle cx="90" cy="120" r="1.3" fill="#fff" opacity="0.7"/>
  <circle cx="150" cy="110" r="1" fill="#fff" opacity="0.5"/>
  <circle cx="30" cy="100" r="1.4" fill="#fff" opacity="0.8"/>
  <circle cx="370" cy="130" r="1.2" fill="#fff" opacity="0.6"/>

  <path d="M0 330 Q100 310 200 325 T400 320 L400 400 L0 400 Z" fill="#2e2440"/>
  <path d="M0 345 Q120 330 220 342 T400 338 L400 400 L0 400 Z" fill="#241c33"/>

  <!-- haz de luz del faro -->
  <g>
    <path d="M196 128 L40 90 L40 150 Z" fill="url(#haz)" transform="rotate(180 196 128)"/>
    <path d="M196 128 L360 95 L360 160 Z" fill="url(#haz)"/>
    <circle cx="196" cy="128" r="40" fill="url(#luz)"/>
  </g>

  <!-- caracol -->
  <g>
    <!-- cuerpo -->
    <path d="M90 340 Q80 320 95 310 Q108 302 118 310 L250 310 Q300 312 310 335 Q314 345 300 348 L110 348 Q92 348 90 340 Z" fill="#7fb069"/>
    <path d="M95 310 Q100 280 96 258 Q94 246 102 244 Q110 242 112 252 Q116 278 116 308" fill="#7fb069"/>
    <!-- cabeza -->
    <circle cx="103" cy="252" r="16" fill="#7fb069"/>
    <!-- antenas -->
    <path d="M96 240 Q88 220 80 212" stroke="#7fb069" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="M110 238 Q114 218 122 210" stroke="#7fb069" stroke-width="4" fill="none" stroke-linecap="round"/>
    <circle cx="79" cy="210" r="5" fill="#a7d08f"/>
    <circle cx="123" cy="208" r="5" fill="#a7d08f"/>
    <!-- ojito y sonrisa -->
    <circle cx="97" cy="250" r="2.5" fill="#1a1a2e"/>
    <path d="M92 260 Q98 265 105 261" stroke="#1a1a2e" stroke-width="1.8" fill="none" stroke-linecap="round"/>
    <!-- panza -->
    <path d="M110 344 L295 344" stroke="#5e8a4c" stroke-width="3" stroke-linecap="round" stroke-dasharray="10 8"/>
  </g>

  <!-- caparazón -->
  <g>
    <circle cx="210" cy="250" r="72" fill="url(#caparazon)" stroke="#6e3d1c" stroke-width="3"/>
    <path d="M210 250 m0 0 a8 8 0 0 1 8 8 a16 16 0 0 1 -24 12 a26 26 0 0 1 10 -48 a38 38 0 0 1 34 42 a48 48 0 0 1 -56 36 a58 58 0 0 1 -32 -78" fill="none" stroke="#6e3d1c" stroke-width="4" stroke-linecap="round"/>
  </g>

  <!-- faro sobre el caparazón -->
  <g>
    <!-- base del faro -->
    <path d="M180 190 L220 190 L212 90 L188 90 Z" fill="#e8e3d8"/>
    <path d="M186 115 L214 115 L212 100 L188 100 Z" fill="#c94f3d"/>
    <path d="M183 150 L217 150 L215 135 L185 135 Z" fill="#c94f3d"/>
    <path d="M180 185 L220 185 L219 170 L181 170 Z" fill="#c94f3d"/>
    <!-- puerta -->
    <rect x="194" y="166" width="12" height="19" rx="6" fill="#5a4632"/>
    <!-- balcón -->
    <rect x="182" y="86" width="36" height="6" rx="2" fill="#4a3b35"/>
    <!-- cabina de luz -->
    <rect x="188" y="62" width="24" height="24" fill="#3a2f2a"/>
    <rect x="192" y="65" width="16" height="18" fill="#ffe98a"/>
    <line x1="200" y1="65" x2="200" y2="83" stroke="#3a2f2a" stroke-width="2"/>
    <!-- techo -->
    <path d="M184 62 L216 62 L200 44 Z" fill="#c94f3d"/>
    <circle cx="200" cy="42" r="3" fill="#ffd24a"/>
    <!-- lamparita visible -->
    <circle cx="200" cy="74" r="5" fill="#fff" opacity="0.9"/>
  </g>

  <!-- rastro de baba brillante -->
  <path d="M300 350 Q330 352 350 348 Q375 344 395 349" stroke="#9fd8d0" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.5"/>
  <circle cx="320" cy="350" r="2" fill="#c8f0ea" opacity="0.7"/>
  <circle cx="360" cy="347" r="1.8" fill="#c8f0ea" opacity="0.7"/>

  <!-- pastitos -->
  <g stroke="#3f5a38" stroke-width="2.5" fill="none" stroke-linecap="round">
    <path d="M50 360 Q48 342 54 332"/>
    <path d="M60 360 Q62 346 58 338"/>
    <path d="M340 365 Q338 350 344 340"/>
    <path d="M352 365 Q354 352 350 344"/>
    <path d="M30 370 Q28 356 34 348"/>
  </g>
</svg>