<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1b1b4b"/>
      <stop offset="0.55" stop-color="#c2477a"/>
      <stop offset="1" stop-color="#ffb26b"/>
    </linearGradient>
    <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff6c8"/>
      <stop offset="0.6" stop-color="#ffd166"/>
      <stop offset="1" stop-color="#ff9e5e" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="lake" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff9a5e"/>
      <stop offset="0.4" stop-color="#7a3b7a"/>
      <stop offset="1" stop-color="#1e1e4a"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff">
    <circle cx="40" cy="40" r="1.5"/>
    <circle cx="110" cy="25" r="1"/>
    <circle cx="170" cy="60" r="1.2"/>
    <circle cx="250" cy="30" r="1.5"/>
    <circle cx="320" cy="55" r="1"/>
    <circle cx="370" cy="20" r="1.3"/>
    <circle cx="80" cy="90" r="1"/>
    <circle cx="290" cy="100" r="1"/>
    <circle cx="20" cy="120" r="1.2"/>
    <circle cx="360" cy="130" r="1"/>
  </g>

  <circle cx="200" cy="230" r="110" fill="url(#sun)"/>
  <circle cx="200" cy="230" r="48" fill="#ffe79a"/>

  <path d="M0 240 L60 180 L100 215 L150 160 L200 225 L250 170 L300 210 L345 165 L400 235 L400 250 L0 250Z" fill="#5a2a6b" opacity="0.85"/>
  <path d="M0 250 L50 215 L90 240 L140 200 L190 248 L240 205 L290 240 L340 210 L400 250Z" fill="#3a1d55"/>

  <rect y="250" width="400" height="150" fill="url(#lake)"/>

  <g stroke="#ffd98a" stroke-linecap="round" opacity="0.85">
    <line x1="170" y1="258" x2="230" y2="258" stroke-width="4"/>
    <line x1="160" y1="270" x2="240" y2="270" stroke-width="4"/>
    <line x1="175" y1="283" x2="225" y2="283" stroke-width="3.5"/>
    <line x1="165" y1="297" x2="235" y2="297" stroke-width="3"/>
    <line x1="180" y1="312" x2="220" y2="312" stroke-width="3"/>
    <line x1="175" y1="330" x2="225" y2="330" stroke-width="2.5"/>
    <line x1="185" y1="350" x2="215" y2="350" stroke-width="2"/>
  </g>

  <g>
    <path d="M60 330 Q100 322 140 330 L132 340 Q100 346 68 340Z" fill="#1a1338"/>
    <path d="M100 328 L100 280" stroke="#1a1338" stroke-width="2"/>
    <path d="M100 282 L100 322 L128 322Z" fill="#f4b183"/>
    <path d="M98 286 L98 322 L78 322Z" fill="#e07a5f"/>
  </g>

  <path d="M0 400 L0 365 Q40 350 80 372 Q120 385 160 370 L160 400Z" fill="#120d2b"/>
  <path d="M400 400 L400 350 Q360 340 330 365 Q300 385 270 375 L270 400Z" fill="#120d2b"/>

  <g fill="#120d2b">
    <path d="M350 352 L350 290 M350 320 L336 306 M350 305 L364 292" stroke="#120d2b" stroke-width="3" fill="none"/>
    <path d="M30 368 L30 310 M30 335 L18 322 M30 322 L42 310" stroke="#120d2b" stroke-width="3" fill="none"/>
  </g>

  <g fill="#1a1338">
    <path d="M280 120 q8 -8 16 0 q8 -8 16 0 q-8 3 -16 8 q-8 -5 -16 -8z"/>
    <path d="M320 90 q6 -6 12 0 q6 -6 12 0 q-6 2 -12 6 q-6 -4 -12 -6z"/>
    <path d="M80 130 q5 -5 10 0 q5 -5 10 0 q-5 2 -10 5 q-5 -3 -10 -5z"/>
  </g>
</svg>