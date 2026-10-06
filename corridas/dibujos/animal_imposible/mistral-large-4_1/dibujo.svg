<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#1a2a4a"/>
      <stop offset="100%" stop-color="#0a0f1e"/>
    </radialGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#7b5cff"/>
      <stop offset="50%" stop-color="#c94fd6"/>
      <stop offset="100%" stop-color="#ff8a5c"/>
    </linearGradient>
    <linearGradient id="wing" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#4fd6c9" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#2a6fd6" stop-opacity="0.4"/>
    </linearGradient>
    <radialGradient id="eye" cx="40%" cy="35%" r="70%">
      <stop offset="0%" stop-color="#fff"/>
      <stop offset="40%" stop-color="#ffe9a8"/>
      <stop offset="100%" stop-color="#ff7a3c"/>
    </radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- estrellas -->
  <g fill="#cfe3ff">
    <circle cx="40" cy="60" r="1.6"/><circle cx="90" cy="30" r="1.1"/>
    <circle cx="330" cy="50" r="1.8"/><circle cx="360" cy="140" r="1.2"/>
    <circle cx="30" cy="200" r="1.3"/><circle cx="370" cy="300" r="1.5"/>
    <circle cx="60" cy="340" r="1.2"/><circle cx="200" cy="25" r="1.4"/>
    <circle cx="310" cy="370" r="1.1"/><circle cx="140" cy="370" r="1.3"/>
  </g>

  <!-- sombra -->
  <ellipse cx="200" cy="330" rx="110" ry="18" fill="#000" opacity="0.35"/>

  <!-- cola de pez (tres lóbulos imposibles) -->
  <g opacity="0.95">
    <path d="M200 300 C 150 320, 110 340, 80 360 C 115 355, 150 345, 185 325 Z" fill="url(#wing)"/>
    <path d="M200 300 C 250 320, 290 340, 320 360 C 285 355, 250 345, 215 325 Z" fill="url(#wing)"/>
    <path d="M200 305 C 195 345, 198 370, 200 390 C 202 370, 205 345, 200 305 Z" fill="url(#wing)"/>
  </g>

  <!-- cuerpo principal: criatura con cabeza de búho, cuerpo de ciervo, alas de mariposa -->
  <g filter="url(#glow)">
    <!-- cuerpo -->
    <path d="M200 150 C 160 170, 145 230, 155 285 C 165 320, 235 320, 245 285 C 255 230, 240 170, 200 150 Z" fill="url(#body)"/>

    <!-- manchas de ciervo -->
    <g fill="#ffe9f5" opacity="0.7">
      <circle cx="180" cy="210" r="6"/><circle cx="220" cy="200" r="5"/>
      <circle cx="195" cy="250" r="7"/><circle cx="170" cy="265" r="4"/>
      <circle cx="228" cy="255" r="5"/><circle cx="205" cy="290" r="4"/>
    </g>

    <!-- cabeza de búho -->
    <circle cx="200" cy="130" r="52" fill="url(#body)"/>
    <!-- disco facial -->
    <circle cx="178" cy="128" r="22" fill="#2a1a4a" opacity="0.85"/>
    <circle cx="222" cy="128" r="22" fill="#2a1a4a" opacity="0.85"/>
    <!-- ojos enormes -->
    <circle cx="178" cy="128" r="15" fill="url(#eye)"/>
    <circle cx="222" cy="128" r="15" fill="url(#eye)"/>
    <circle cx="178" cy="128" r="6" fill="#1a0a2a"/>
    <circle cx="222" cy="128" r="6" fill="#1a0a2a"/>
    <circle cx="174" cy="123" r="2.5" fill="#fff"/>
    <circle cx="218" cy="123" r="2.5" fill="#fff"/>
    <!-- pico -->
    <path d="M200 138 L 191 152 L 200 160 L 209 152 Z" fill="#ffb347"/>
    <!-- orejas de búho -->
    <path d="M160 95 L 150 65 L 178 85 Z" fill="url(#body)"/>
    <path d="M240 95 L 250 65 L 222 85 Z" fill="url(#body)"/>

    <!-- astas de ciervo que brotan de la cabeza -->
    <g stroke="#e8d9b0" stroke-width="7" fill="none" stroke-linecap="round">
      <path d="M165 85 C 140 60, 130 40, 135 15"/>
      <path d="M135 45 C 120 40, 110 30, 108 18"/>
      <path d="M142 60 C 128 58, 118 52, 112 42"/>
      <path d="M235 85 C 260 60, 270 40, 265 15"/>
      <path d="M265 45 C 280 40, 290 30, 292 18"/>
      <path d="M258 60 C 272 58, 282 52, 288 42"/>
    </g>

    <!-- alas de mariposa (cuatro, dos a cada lado) -->
    <g opacity="0.9">
      <path d="M160 180 C 90 130, 30 140, 45 200 C 55 245, 120 240, 162 210 Z" fill="url(#wing)" stroke="#9ff" stroke-width="1.5"/>
      <path d="M240 180 C 310 130, 370 140, 355 200 C 345 245, 280 240, 238 210 Z" fill="url(#wing)" stroke="#9ff" stroke-width="1.5"/>
      <path d="M158 230 C 100 240, 60 280, 85 315 C 110 340, 155 300, 165 255 Z" fill="url(#wing)" stroke="#9ff" stroke-width="1.5"/>
      <path d="M242 230 C 300 240, 340 280, 315 315 C 290 340, 245 300, 235 255 Z" fill="url(#wing)" stroke="#9ff" stroke-width="1.5"/>
    </g>
    <!-- ojos de las alas -->
    <g>
      <circle cx="95" cy="185" r="10" fill="#1a0a2a"/><circle cx="95" cy="185" r="4" fill="#ff5c8a"/>
      <circle cx="305" cy="185" r="10" fill="#1a0a2a"/><circle cx="305" cy="185" r="4" fill="#ff5c8a"/>
      <circle cx="115" cy="290" r="8" fill="#1a0a2a"/><circle cx="115" cy="290" r="3" fill="#5cd6ff"/>
      <circle cx="285" cy="290" r="8" fill="#1a0a2a"/><circle cx="285" cy="290" r="3" fill="#5cd6ff"/>
    </g>

    <!-- patas de araña (seis, imposibles en un ciervo) -->
    <g stroke="#3a2a6a" stroke-width="6" fill="none" stroke-linecap="round">
      <path d="M170 300 C 150 320, 130 325, 115 320"/>
      <path d="M175 310 C 160 335, 145 345, 130 345"/>
      <path d="M185 315 C 175 340, 168 355, 158 365"/>
      <path d="M230 300 C 250 320, 270 325, 285 320"/>
      <path d="M225 310 C 240 335, 255 345, 270 345"/>
      <path d="M215 315 C 225 340, 232 355, 242 365"/>
    </g>

    <!-- antenas de mariposa saliendo del hocico -->
    <g stroke="#ffd9ec" stroke-width="3" fill="none" stroke-linecap="round">
      <path d="M192 158 C 180 175, 170 185, 158 190"/>
      <path d="M208 158 C 220 175, 230 185, 242 190"/>
    </g>
    <circle cx="156" cy="191" r="5" fill="#ff8ac2"/>
    <circle cx="244" cy="191" r="5" fill="#ff8ac2"/>
  </g>

  <!-- luciérnagas -->
  <g fill="#fff7a8" filter="url(#glow)">
    <circle cx="70" cy="120" r="3"/><circle cx="340" cy="90" r="2.5"/>
    <circle cx="320" cy="250" r="3"/><circle cx="55" cy="270" r="2.5"/>
    <circle cx="255" cy="40" r="2"/>
  </g>
</svg>