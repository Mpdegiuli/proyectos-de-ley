<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="cielo" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#1a2340"/>
      <stop offset="60%" stop-color="#0d1226"/>
      <stop offset="100%" stop-color="#05070f"/>
    </radialGradient>
    <radialGradient id="luna" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fffbe8"/>
      <stop offset="100%" stop-color="#c9c2a0"/>
    </radialGradient>
    <radialGradient id="orbe" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d8fff4"/>
      <stop offset="45%" stop-color="#54e0c7"/>
      <stop offset="100%" stop-color="#1a7a6e" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="tronco" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#2b1d3a"/>
      <stop offset="50%" stop-color="#6b4a7a"/>
      <stop offset="100%" stop-color="#241833"/>
    </linearGradient>
    <linearGradient id="suelo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a2140"/>
      <stop offset="100%" stop-color="#0b0918"/>
    </linearGradient>
    <filter id="brillo" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>
  <circle cx="320" cy="70" r="30" fill="url(#luna)" opacity="0.9"/>
  <circle cx="308" cy="62" r="6" fill="#b8b190" opacity="0.5"/>
  <circle cx="330" cy="80" r="4" fill="#b8b190" opacity="0.4"/>

  <g fill="#ffffff">
    <circle cx="40" cy="45" r="1.4" opacity="0.9"/>
    <circle cx="90" cy="30" r="1" opacity="0.7"/>
    <circle cx="150" cy="60" r="1.2" opacity="0.8"/>
    <circle cx="210" cy="25" r="1" opacity="0.6"/>
    <circle cx="255" cy="55" r="1.3" opacity="0.8"/>
    <circle cx="365" cy="120" r="1.1" opacity="0.7"/>
    <circle cx="30" cy="110" r="1" opacity="0.6"/>
    <circle cx="70" cy="150" r="1.2" opacity="0.7"/>
    <circle cx="370" cy="40" r="1.2" opacity="0.8"/>
    <circle cx="340" cy="160" r="1" opacity="0.5"/>
    <circle cx="130" cy="110" r="1" opacity="0.5"/>
  </g>

  <rect y="330" width="400" height="70" fill="url(#suelo)"/>
  <ellipse cx="200" cy="338" rx="150" ry="12" fill="#3a2f55" opacity="0.6"/>

  <!-- Raíces -->
  <g fill="none" stroke="url(#tronco)" stroke-linecap="round">
    <path d="M200 335 C 170 340, 150 348, 120 352 C 105 354, 90 350, 78 356" stroke-width="7"/>
    <path d="M200 335 C 230 342, 255 350, 285 353 C 300 355, 318 351, 330 357" stroke-width="7"/>
    <path d="M195 338 C 188 348, 172 356, 160 368" stroke-width="5"/>
    <path d="M205 338 C 214 348, 232 356, 246 366" stroke-width="5"/>
  </g>

  <!-- Tronco espiralado -->
  <g fill="none" stroke="url(#tronco)" stroke-linecap="round">
    <path d="M200 338 C 205 320, 185 305, 197 288 C 210 271, 186 255, 198 238 C 208 224, 192 210, 200 195" stroke-width="14"/>
    <path d="M200 338 C 205 320, 185 305, 197 288 C 210 271, 186 255, 198 238 C 208 224, 192 210, 200 195" stroke-width="6" stroke="#8a5f9e" opacity="0.5"/>
  </g>
  <path d="M203 320 C 190 312, 208 300, 196 292 M202 296 C 214 288, 194 276, 204 268 M203 254 C 190 248, 208 236, 198 230" fill="none" stroke="#c39ad6" stroke-width="1.5" opacity="0.6"/>

  <!-- Copa: anillos flotantes -->
  <g fill="none" stroke-linecap="round">
    <path d="M200 196 C 160 186, 122 188, 92 200" stroke="#5a3d70" stroke-width="6"/>
    <path d="M200 196 C 240 184, 278 186, 308 200" stroke="#5a3d70" stroke-width="6"/>
    <path d="M200 192 C 175 170, 140 160, 112 162" stroke="#6b4a7a" stroke-width="5"/>
    <path d="M200 192 C 225 168, 260 158, 288 162" stroke="#6b4a7a" stroke-width="5"/>
    <path d="M200 188 C 200 165, 195 142, 186 124" stroke="#7a5588" stroke-width="4"/>
    <path d="M200 188 C 205 162, 218 140, 234 126" stroke="#7a5588" stroke-width="4"/>
  </g>

  <!-- Hojas cristal -->
  <g fill="#54e0c7" opacity="0.85">
    <path d="M92 200 l-8 -14 l8 -6 l8 8 z" />
    <path d="M76 192 l-10 -10 l4 -9 l11 6 z" opacity="0.7"/>
    <path d="M108 194 l10 -12 l9 4 l-7 9 z" opacity="0.7"/>
    <path d="M308 200 l8 -14 l-8 -6 l-8 8 z"/>
    <path d="M324 192 l10 -10 l-4 -9 l-11 6 z" opacity="0.7"/>
    <path d="M292 194 l-10 -12 l-9 4 l7 9 z" opacity="0.7"/>
    <path d="M112 162 l-6 -12 l7 -7 l8 7 z" opacity="0.8"/>
    <path d="M96 154 l-9 -8 l3 -8 l9 5 z" opacity="0.6"/>
    <path d="M130 158 l8 -10 l9 3 l-6 8 z" opacity="0.6"/>
    <path d="M288 162 l6 -12 l-7 -7 l-8 7 z" opacity="0.8"/>
    <path d="M304 154 l9 -8 l-3 -8 l-9 5 z" opacity="0.6"/>
    <path d="M270 158 l-8 -10 l-9 3 l6 8 z" opacity="0.6"/>
    <path d="M186 124 l-4 -13 l8 -5 l6 9 z" opacity="0.8"/>
    <path d="M176 110 l-10 -6 l1 -9 l9 2 z" opacity="0.6"/>
    <path d="M234 126 l6 -12 l-7 -7 l-8 7 z" opacity="0.8"/>
    <path d="M246 112 l10 -6 l-1 -9 l-9 2 z" opacity="0.6"/>
  </g>

  <!-- Orbes luminosos -->
  <g filter="url(#brillo)">
    <circle cx="150" cy="178" r="9" fill="url(#orbe)"/>
    <circle cx="255" cy="172" r="8" fill="url(#orbe)"/>
    <circle cx="200" cy="140" r="10" fill="url(#orbe)"/>
    <circle cx="120" cy="168" r="6" fill="url(#orbe)"/>
    <circle cx="285" cy="168" r="6" fill="url(#orbe)"/>
    <circle cx="210" cy="105" r="7" fill="url(#orbe)"/>
    <circle cx="90" cy="200" r="5" fill="url(#orbe)"/>
    <circle cx="310" cy="200" r="5" fill="url(#orbe)"/>
  </g>

  <!-- Hojas cayendo -->
  <g fill="#54e0c7">
    <path d="M150 250 l-4 6 l5 2 l3 -5 z" opacity="0.7"/>
    <path d="M260 240 l4 6 l-5 2 l-3 -5 z" opacity="0.6"/>
    <path d="M225 290 l-3 5 l4 2 l2 -4 z" opacity="0.5"/>
    <path d="M170 300 l3 5 l-4 2 l-2 -4 z" opacity="0.5"/>
  </g>
  <circle cx="235" cy="270" r="2.5" fill="#54e0c7" opacity="0.7"/>
  <circle cx="185" cy="275" r="2" fill="#54e0c7" opacity="0.6"/>

  <!-- Reflexión en el suelo -->
  <ellipse cx="200" cy="345" rx="70" ry="6" fill="#54e0c7" opacity="0.15"/>
</svg>