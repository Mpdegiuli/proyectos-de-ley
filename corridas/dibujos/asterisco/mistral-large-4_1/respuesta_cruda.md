<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="75%">
      <stop offset="0" stop-color="#FFFDF8"/>
      <stop offset="1" stop-color="#FBE8D8"/>
    </radialGradient>
    <linearGradient id="arm" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FF7E5F"/>
      <stop offset="0.55" stop-color="#F65D8E"/>
      <stop offset="1" stop-color="#B83280"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.55"/>
      <stop offset="0.4" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#8E2A5C" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <g filter="url(#shadow)">
    <g fill="url(#arm)">
      <rect x="184" y="58" width="32" height="284" rx="16"/>
      <rect x="184" y="58" width="32" height="284" rx="16" transform="rotate(60 200 200)"/>
      <rect x="184" y="58" width="32" height="284" rx="16" transform="rotate(120 200 200)"/>
      <circle cx="200" cy="200" r="30"/>
    </g>
    <g fill="url(#shine)">
      <rect x="189" y="66" width="10" height="120" rx="5"/>
      <rect x="189" y="66" width="10" height="120" rx="5" transform="rotate(60 200 200)"/>
      <rect x="189" y="66" width="10" height="120" rx="5" transform="rotate(120 200 200)"/>
      <circle cx="191" cy="191" r="9" fill="#FFFFFF" opacity="0.6"/>
    </g>
  </g>
</svg>