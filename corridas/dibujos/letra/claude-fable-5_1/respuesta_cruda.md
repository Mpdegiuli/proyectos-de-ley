<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="fondo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1a1a2e"/>
      <stop offset="1" stop-color="#16213e"/>
    </linearGradient>
    <linearGradient id="letra" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd86b"/>
      <stop offset="0.5" stop-color="#f6a821"/>
      <stop offset="1" stop-color="#d97b1c"/>
    </linearGradient>
    <linearGradient id="brillo" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0.6"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <filter id="sombra" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#fondo)"/>

  <circle cx="200" cy="200" r="150" fill="none" stroke="#f6a821" stroke-opacity="0.25" stroke-width="2"/>
  <circle cx="200" cy="200" r="160" fill="none" stroke="#f6a821" stroke-opacity="0.12" stroke-width="1"/>

  <g stroke="#f6a821" stroke-opacity="0.4" stroke-width="2" fill="none">
    <path d="M60 200 q20 -15 40 0 q-20 15 -40 0z"/>
    <path d="M340 200 q-20 -15 -40 0 q20 15 40 0z"/>
    <circle cx="200" cy="48" r="5"/>
    <circle cx="200" cy="352" r="5"/>
  </g>

  <g filter="url(#sombra)">
    <path d="M200 85
             L278 300
             L240 300
             L221 245
             L179 245
             L160 300
             L122 300
             Z
             M200 142
             L188 215
             L212 215
             Z"
          fill="url(#letra)" fill-rule="evenodd"
          stroke="#8a4b0f" stroke-width="4" stroke-linejoin="round"/>
  </g>

  <path d="M200 85 L210 113 L190 113 Z" fill="#fff" opacity="0.5"/>
  <rect x="150" y="305" width="100" height="6" rx="3" fill="url(#brillo)"/>

  <g fill="#ffd86b" opacity="0.8">
    <circle cx="110" cy="110" r="3"/>
    <circle cx="295" cy="120" r="2.5"/>
    <circle cx="90" cy="280" r="2"/>
    <circle cx="310" cy="270" r="3"/>
    <circle cx="265" cy="80" r="2"/>
  </g>

  <path d="M120 330 q80 25 160 0" fill="none" stroke="#f6a821" stroke-width="2" stroke-opacity="0.5" stroke-linecap="round"/>
</svg>