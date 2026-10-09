<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="72%">
      <stop offset="0" stop-color="#2f4272"/>
      <stop offset="0.55" stop-color="#1b2547"/>
      <stop offset="1" stop-color="#0c1128"/>
    </radialGradient>
    <linearGradient id="lt" x1="0" y1="0" x2="0.2" y2="1">
      <stop offset="0" stop-color="#fff2b8"/>
      <stop offset="0.35" stop-color="#ffd257"/>
      <stop offset="0.7" stop-color="#ff9f2e"/>
      <stop offset="1" stop-color="#e2622a"/>
    </linearGradient>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#7fd8ff" stop-opacity="0.9"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.15"/>
      <stop offset="1" stop-color="#ff8ad8" stop-opacity="0.8"/>
    </linearGradient>
    <filter id="sh" x="-35%" y="-35%" width="170%" height="170%">
      <feDropShadow dx="0" dy="12" stdDeviation="11" flood-color="#000814" flood-opacity="0.6"/>
    </filter>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="7" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <circle cx="200" cy="200" r="168" fill="none" stroke="url(#ring)" stroke-width="3" opacity="0.75"/>
  <circle cx="200" cy="200" r="152" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.12"/>

  <g fill="#ffffff" opacity="0.5" filter="url(#glow)">
    <path d="M62 78 l5 13 13 5 -13 5 -5 13 -5-13 -13-5 13-5z"/>
    <path d="M340 108 l4 10 10 4 -10 4 -4 10 -4-10 -10-4 10-4z"/>
    <path d="M72 316 l4 10 10 4 -10 4 -4 10 -4-10 -10-4 10-4z"/>
    <path d="M332 300 l5 13 13 5 -13 5 -5 13 -5-13 -13-5 13-5z"/>
    <circle cx="112" cy="150" r="3.5"/>
    <circle cx="296" cy="182" r="3"/>
    <circle cx="130" cy="352" r="2.5"/>
    <circle cx="272" cy="66" r="3"/>
    <circle cx="200" cy="352" r="4"/>
    <circle cx="44" cy="212" r="3"/>
    <circle cx="356" cy="228" r="3.5"/>
  </g>

  <g filter="url(#sh)">
    <g fill="url(#lt)">
      <path d="M95 325 L185 60 L215 60 L305 325 L262 325 L200 145 L138 325 Z"/>
      <rect x="112" y="238" width="176" height="34" rx="10"/>
      <rect x="76" y="306" width="80" height="24" rx="8"/>
      <rect x="244" y="306" width="80" height="24" rx="8"/>
      <path d="M185 60 L215 60 L208 34 L192 34 Z"/>
    </g>
    <g fill="none" stroke="#8a3b12" stroke-opacity="0.55" stroke-width="3" stroke-linejoin="round">
      <path d="M95 325 L185 60 L215 60 L305 325 L262 325 L200 145 L138 325 Z"/>
      <rect x="112" y="238" width="176" height="34" rx="10"/>
    </g>
  </g>

  <g fill="#fff6d8" opacity="0.85">
    <path d="M120 300 L138 300 L136 314 L118 314 Z"/>
    <path d="M262 300 L280 300 L282 314 L264 314 Z"/>
  </g>

  <g stroke="#ffffff" stroke-opacity="0.35" stroke-width="2" fill="none" stroke-linecap="round">
    <path d="M150 226 q50 -18 100 0"/>
    <path d="M158 352 q42 16 84 0"/>
  </g>
</svg>