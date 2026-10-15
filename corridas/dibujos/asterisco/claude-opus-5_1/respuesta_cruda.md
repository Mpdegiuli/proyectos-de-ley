```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0%" stop-color="#fdfcf7"/>
      <stop offset="100%" stop-color="#ddd6c4"/>
    </radialGradient>
    <linearGradient id="arm" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ff6b4a"/>
      <stop offset="50%" stop-color="#e03a3a"/>
      <stop offset="100%" stop-color="#8e1b3a"/>
    </linearGradient>
    <filter id="sh" x="-40%" y="-40%" width="180%" height="180%">
      <feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="#3a1020" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="150" fill="none" stroke="#c9bfa7" stroke-width="2" stroke-dasharray="4 10"/>

  <g filter="url(#sh)">
    <g fill="url(#arm)" stroke="#5e1026" stroke-width="3" stroke-linejoin="round">
      <g>
        <path d="M200 200 L186 70 Q200 54 214 70 Z"/>
      </g>
      <g transform="rotate(60 200 200)">
        <path d="M200 200 L186 70 Q200 54 214 70 Z"/>
      </g>
      <g transform="rotate(120 200 200)">
        <path d="M200 200 L186 70 Q200 54 214 70 Z"/>
      </g>
      <g transform="rotate(180 200 200)">
        <path d="M200 200 L186 70 Q200 54 214 70 Z"/>
      </g>
      <g transform="rotate(240 200 200)">
        <path d="M200 200 L186 70 Q200 54 214 70 Z"/>
      </g>
      <g transform="rotate(300 200 200)">
        <path d="M200 200 L186 70 Q200 54 214 70 Z"/>
      </g>
    </g>
    <circle cx="200" cy="200" r="22" fill="#e03a3a" stroke="#5e1026" stroke-width="3"/>
    <circle cx="193" cy="193" r="7" fill="#ffd0b8" opacity="0.8"/>
  </g>
</svg>
```