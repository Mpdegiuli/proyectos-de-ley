<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0b1026"/>
      <stop offset="0.55" stop-color="#2a2f6b"/>
      <stop offset="1" stop-color="#c46a5a"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5a3f5c"/>
      <stop offset="1" stop-color="#0d1330"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff6d5" stop-opacity="0.9"/>
      <stop offset="0.4" stop-color="#ffe9a8" stop-opacity="0.25"/>
      <stop offset="1" stop-color="#ffe9a8" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="m1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3b3f7a"/>
      <stop offset="1" stop-color="#1e2150"/>
    </linearGradient>
    <linearGradient id="m2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#262a5e"/>
      <stop offset="1" stop-color="#141738"/>
    </linearGradient>
    <clipPath id="lake"><rect x="0" y="262" width="400" height="138"/></clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff">
    <circle cx="30" cy="40" r="1.2"/><circle cx="70" cy="90" r="0.9"/><circle cx="110" cy="30" r="1.4"/>
    <circle cx="150" cy="70" r="0.8"/><circle cx="190" cy="25" r="1.1"/><circle cx="230" cy="60" r="0.9"/>
    <circle cx="260" cy="20" r="1.3"/><circle cx="300" cy="50" r="0.8"/><circle cx="340" cy="30" r="1.2"/>
    <circle cx="375" cy="75" r="1"/><circle cx="55" cy="130" r="0.8"/><circle cx="130" cy="120" r="1"/>
    <circle cx="205" cy="105" r="0.7"/><circle cx="355" cy="120" r="0.9"/><circle cx="90" cy="60" r="0.7"/>
    <circle cx="20" cy="95" r="0.9"/><circle cx="170" cy="140" r="0.7"/><circle cx="245" cy="130" r="0.8"/>
    <circle cx="385" cy="20" r="0.8"/><circle cx="320" cy="95" r="1.1"/>
  </g>

  <circle cx="300" cy="85" r="70" fill="url(#glow)"/>
  <path d="M300 55 a30 30 0 1 0 0 60 a24 24 0 1 1 0 -60z" fill="#fff3c4"/>

  <path d="M0 250 L40 200 L75 225 L120 165 L160 215 L200 180 L240 230 L280 190 L320 235 L360 205 L400 240 L400 270 L0 270z" fill="url(#m2)"/>
  <path d="M0 270 L30 240 L70 255 L110 215 L150 250 L190 230 L235 262 L270 235 L310 258 L350 230 L400 265 L400 280 L0 280z" fill="url(#m1)"/>

  <rect x="0" y="262" width="400" height="138" fill="url(#water)"/>

  <g clip-path="url(#lake)" opacity="0.35">
    <g transform="translate(0,524) scale(1,-1)">
      <path d="M0 250 L40 200 L75 225 L120 165 L160 215 L200 180 L240 230 L280 190 L320 235 L360 205 L400 240 L400 270 L0 270z" fill="#1e2150"/>
      <path d="M0 270 L30 240 L70 255 L110 215 L150 250 L190 230 L235 262 L270 235 L310 258 L350 230 L400 265 L400 280 L0 280z" fill="#3b3f7a"/>
      <path d="M300 55 a30 30 0 1 0 0 60 a24 24 0 1 1 0 -60z" fill="#fff3c4"/>
    </g>
  </g>

  <g stroke="#f7e6b8" stroke-width="1.2" opacity="0.5" stroke-linecap="round">
    <line x1="285" y1="290" x2="315" y2="290"/>
    <line x1="290" y1="305" x2="320" y2="305"/>
    <line x1="280" y1="322" x2="305" y2="322"/>
    <line x1="295" y1="340" x2="330" y2="340"/>
    <line x1="270" y1="360" x2="300" y2="360"/>
    <line x1="290" y1="378" x2="320" y2="378"/>
  </g>
  <g stroke="#8a7fb0" stroke-width="1" opacity="0.3" stroke-linecap="round">
    <line x1="40" y1="300" x2="80" y2="300"/>
    <line x1="120" y1="330" x2="170" y2="330"/>
    <line x1="60" y1="365" x2="110" y2="365"/>
    <line x1="200" y1="350" x2="240" y2="350"/>
    <line x1="150" y1="385" x2="190" y2="385"/>
  </g>

  <path d="M0 400 L0 300 Q30 285 60 292 Q100 300 140 285 Q170 275 200 290 L200 400z" fill="#0a0d22"/>

  <g fill="#070a1c">
    <path d="M25 300 L40 245 L55 300z"/>
    <path d="M28 280 L40 240 L52 280z"/>
    <path d="M60 295 L78 225 L96 295z"/>
    <path d="M64 270 L78 220 L92 270z"/>
    <path d="M100 292 L115 240 L130 292z"/>
    <path d="M104 268 L115 235 L126 268z"/>
    <path d="M140 285 L152 250 L164 285z"/>
    <path d="M143 268 L152 245 L161 268z"/>
    <path d="M5 305 L15 265 L25 305z"/>
  </g>

  <g>
    <rect x="168" y="268" width="30" height="20" fill="#120f22"/>
    <path d="M164 268 L183 252 L202 268z" fill="#1c1730"/>
    <rect x="178" y="275" width="8" height="8" fill="#ffcf6b"/>
    <rect x="181.5" y="275" width="1" height="8" fill="#120f22"/>
    <rect x="178" y="278.5" width="8" height="1" fill="#120f22"/>
    <rect x="190" y="256" width="4" height="8" fill="#120f22"/>
    <circle cx="182" cy="279" r="14" fill="#ffcf6b" opacity="0.12"/>
  </g>

  <path d="M0 400 L0 330 Q40 318 80 330 Q120 342 160 330 Q185 322 200 330 L200 400z" fill="#060816"/>

  <ellipse cx="182" cy="300" rx="16" ry="3" fill="#ffcf6b" opacity="0.15"/>
</svg>