```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a0a3e"/>
      <stop offset="55%" stop-color="#6a2a7e"/>
      <stop offset="100%" stop-color="#ff7a3d"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a1a3e"/>
      <stop offset="100%" stop-color="#000010"/>
    </linearGradient>
    <radialGradient id="galaxy" cx="50%" cy="50%">
      <stop offset="0%" stop-color="#fff"/>
      <stop offset="25%" stop-color="#ff9"/>
      <stop offset="60%" stop-color="#f6c"/>
      <stop offset="100%" stop-color="#639" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="galaxy2">
      <stop offset="0%" stop-color="#fff"/>
      <stop offset="40%" stop-color="#9cf"/>
      <stop offset="100%" stop-color="#06f" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="0.4"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff">
    <circle cx="40" cy="35" r="0.9"/><circle cx="115" cy="70" r="0.7"/>
    <circle cx="200" cy="25" r="1.1"/><circle cx="285" cy="45" r="0.8"/>
    <circle cx="355" cy="60" r="1"/><circle cx="375" cy="110" r="0.7"/>
    <circle cx="30" cy="140" r="0.6"/><circle cx="365" cy="195" r="0.9"/>
    <circle cx="50" cy="100" r="0.5"/><circle cx="160" cy="55" r="0.6"/>
    <circle cx="320" cy="100" r="0.5"/><circle cx="240" cy="80" r="0.7"/>
  </g>

  <path d="M0 320 Q50 308 100 318 T200 318 T300 318 T400 320 L400 400 L0 400 Z" fill="url(#ink)"/>
  <path d="M0 335 Q60 322 120 340 T240 328 T360 338 T400 332 L400 400 L0 400 Z" fill="#0a0a1a" opacity="0.7"/>
  <path d="M0 350 Q80 342 160 352 T320 348 T400 352 L400 400 L0 400 Z" fill="#000" opacity="0.6"/>

  <ellipse cx="75" cy="312" rx="3" ry="2" fill="#1a1a3e"/>
  <ellipse cx="325" cy="308" rx="2.5" ry="1.5" fill="#1a1a3e"/>
  <ellipse cx="180" cy="330" rx="2" ry="1" fill="#0a0a2e"/>

  <g transform="translate(200,255)">
    <ellipse cx="-50" cy="0" rx="38" ry="16" fill="#c8b8d0" opacity="0.9"/>
    <ellipse cx="-15" cy="-6" rx="42" ry="20" fill="#e0d0e8"/>
    <ellipse cx="25" cy="-4" rx="40" ry="18" fill="#f0e0f4"/>
    <ellipse cx="55" cy="2" rx="30" ry="14" fill="#d8c8e0" opacity="0.95"/>
    <ellipse cx="0" cy="6" rx="50" ry="12" fill="#b8a8c8" opacity="0.7"/>
  </g>

  <g transform="translate(200,232)">
    <rect x="-48" y="0" width="96" height="22" rx="3" fill="#2a1a0a"/>
    <rect x="-48" y="0" width="96" height="4" fill="#5a4a3a"/>
    <rect x="-43" y="-26" width="86" height="26" rx="2" fill="#3a2a1a"/>
    <rect x="-43" y="-26" width="86" height="3" fill="#6a5a4a"/>
    <rect x="-38" y="-34" width="76" height="9" rx="2" fill="#1a0a00"/>
    <circle cx="-38" cy="-29" r="5.5" fill="#0a0500" stroke="#5a4a3a" stroke-width="0.5"/>
    <circle cx="38" cy="-29" r="5.5" fill="#0a0500" stroke="#5a4a3a" stroke-width="0.5"/>
    <g fill="#0a0500">
      <circle cx="-28" cy="-4" r="3"/><circle cx="-18" cy="-4" r="3"/>
      <circle cx="-8" cy="-4" r="3"/><circle cx="2" cy="-4" r="3"/>
      <circle cx="12" cy="-4" r="3"/><circle cx="22" cy="-4" r="3"/>
    </g>
    <g fill="#caa572" stroke="#8a6a3a" stroke-width="0.3">
      <circle cx="-28" cy="-15" r="1.8"/><circle cx="-18" cy="-15" r="1.8"/>
      <circle cx="-8" cy="-15" r="1.8"/><circle cx="2" cy="-15" r="1.8"/>
      <circle cx="12" cy="-15" r="1.8"/><circle cx="22" cy="-15" r="1.8"/>
    </g>
    <rect x="-18" y="-23" width="36" height="6" fill="#caa572" rx="1"/>
    <text x="0" y="-18" font-family="Georgia" font-size="5" fill="#3a2a1a" text-anchor="middle" font-weight="bold">COSMOS</text>
  </g>

  <path d="M168 198 L168 95 Q168 90 173 90 L227 90 Q232 90 232 95 L232 198 Z" fill="#f4ead0"/>
  <path d="M168 198 L168 95 Q168 90 173 90 L227 90 Q232 90 232 95 L232 198" fill="none" stroke="#c4a888" stroke-width="0.5"/>
  <line x1="172" y1="105" x2="228" y2="105" stroke="#d4b890" stroke-width="0.4"/>
  <line x1="172" y1="115" x2="228" y2="115" stroke="#d4b890" stroke-width="0.4"/>
  <line x1="172" y1="185" x2="228" y2="185" stroke="#d4b890" stroke-width="0.4"/>

  <circle cx="200" cy="145" r="32" fill="url(#galaxy)" opacity="0.85"/>
  <g transform="translate(195,140) rotate(25)" opacity="0.6">
    <ellipse cx="0" cy="0" rx="28" ry="4" fill="none" stroke="#fc9" stroke-width="0.8"/>
    <ellipse cx="0" cy="0" rx="20" ry="2" fill="none" stroke="#f9c" stroke-width="0.5"/>
  </g>
  <circle cx="200" cy="145" r="3" fill="#fff" filter="url(#blur)"/>

  <g>
    <circle cx="180" cy="120" r="1.2" fill="#fff"/>
    <circle cx="220" cy="118" r="0.8" fill="#fff"/>
    <circle cx="175" cy="165" r="1" fill="#aff"/>
    <circle cx="225" cy="170" r="1.3" fill="#faf"/>
    <circle cx="185" cy="178" r="0.7" fill="#fff"/>
    <circle cx="215" cy="155" r="0.9" fill="#ff9"/>
    <circle cx="208" cy="130" r="0.6" fill="#fff"/>
    <circle cx="192" cy="170" r="0.5" fill="#9cf"/>
  </g>

  <ellipse cx="183" cy="108" rx="11" ry="5" fill="#f6c" opacity="0.35"/>
  <ellipse cx="218" cy="180" rx="10" ry="4" fill="#9cf" opacity="0.35"/>

  <g opacity="0.95">
    <circle cx="245" cy="185" r="1.1" fill="#ff9"/>
    <circle cx="255" cy="175" r="0.9" fill="#fff"/>
    <circle cx="265" cy="165" r="1.3" fill="#fcf"/>
    <circle cx="248" cy="155" r="0.7" fill="#aff"/>
    <circle cx="270" cy="148" r="1" fill="#fff"/>
    <circle cx="258" cy="195" r="0.6" fill="#fff"/>
    <circle cx="278" cy="178" r="0.8" fill="#fc9"/>
    <g stroke="#fff" stroke-width="0.5" fill="none">
      <path d="M260 180 L260 192 M254 186 L266 186"/>
      <path d="M278 165 L278 173 M274 169 L282 169"/>
    </g>
  </g>

  <g opacity="0.5" stroke="#fff" stroke-width="0.4" fill="none">
    <path d="M232 140 Q260 130 285 145"/>
    <path d="M232 165 Q265 170 290 160"/>
  </g>

  <g transform="translate(55,175)" opacity="0.6">
    <path d="M0 0 Q6 -4 12 0 Q18 -4 24 0 L22 4 L2 4 Z" fill="#3a2a4a"/>
    <path d="M-3 2 L-1 -2 M27 2 L25 -2" stroke="#3a2a4a" stroke-width="1" fill="none"/>
  </g>
  <g transform="translate(330,195)" opacity="0.6">
    <path d="M0 0 Q6 -4 12 0 Q18 -4 24 0 L22 4 L2 4 Z" fill="#3a2a4a"/>
    <path d="M-3 2 L-1 -2 M27 2 L25 -2" stroke="#3a2a4a" stroke-width="1" fill="none"/>
  </g>

  <ellipse cx="200" cy="375" rx="120" ry="6" fill="#fff" opacity="0.08"/>

  <g opacity="0.4">
    <circle cx="100" cy="290" r="0.8" fill="#fff"/>
    <circle cx="310" cy="285" r="0.6" fill="#fff"/>
    <circle cx="350" cy="295" r="0.5" fill="#fff"/>
  </g>
</svg>
```