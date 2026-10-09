<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1b1f3b"/>
      <stop offset="1" stop-color="#4a2c5e"/>
    </linearGradient>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd86b"/>
      <stop offset="0.5" stop-color="#ff9a4a"/>
      <stop offset="1" stop-color="#e8475f"/>
    </linearGradient>
    <filter id="sh" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="6" dy="8" stdDeviation="6" flood-color="#000" flood-opacity="0.45"/>
    </filter>
    <pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="8" cy="8" r="1.6" fill="#ffffff" opacity="0.08"/>
    </pattern>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#dots)"/>
  <circle cx="200" cy="200" r="165" fill="none" stroke="#ffd86b" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="4 10"/>
  <circle cx="200" cy="200" r="150" fill="#ffffff" fill-opacity="0.04"/>
  <g filter="url(#sh)">
    <path d="M200 70 C 150 70 110 105 110 160 L 110 330 L 160 330 L 160 250 L 240 250 L 240 330 L 290 330 L 290 160 C 290 105 250 70 200 70 Z M 160 205 L 160 165 C 160 135 178 115 200 115 C 222 115 240 135 240 165 L 240 205 Z" fill="url(#g)" fill-rule="evenodd" stroke="#fff3c9" stroke-width="3" stroke-linejoin="round"/>
  </g>
  <path d="M125 160 C 125 115 160 85 200 85" fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="5" stroke-linecap="round"/>
  <rect x="95" y="338" width="210" height="8" rx="4" fill="#ffd86b" opacity="0.7"/>
</svg>