<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="110" y1="60" x2="300" y2="330">
      <stop offset="0" stop-color="#0ea5e9"/>
      <stop offset=".5" stop-color="#6366f1"/>
      <stop offset="1" stop-color="#d946ef"/>
    </linearGradient>
    <linearGradient id="a" gradientUnits="userSpaceOnUse" x1="106" y1="284" x2="262" y2="100">
      <stop offset="0" stop-color="#f59e0b"/>
      <stop offset="1" stop-color="#ef4444"/>
    </linearGradient>
    <radialGradient id="bg" cx=".5" cy=".42" r=".75">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="1" stop-color="#eef2f7"/>
    </radialGradient>
    <filter id="sh" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="7" stdDeviation="9" flood-color="#4f46e5" flood-opacity=".28"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <circle cx="200" cy="192" r="138" fill="none" stroke="#dbe3ec" stroke-width="2"/>

  <g stroke="#c3cedb" stroke-width="1.5" stroke-dasharray="5 8" opacity=".9">
    <line x1="46" y1="100" x2="354" y2="100"/>
    <line x1="46" y1="290" x2="354" y2="290"/>
    <line x1="46" y1="56" x2="354" y2="56"/>
  </g>

  <g filter="url(#sh)">
    <g fill="none" stroke="url(#g)" stroke-linecap="round" stroke-linejoin="round">
      <path d="M150 112 C245 92 292 138 292 182 C292 228 240 262 150 248" stroke-width="26"/>
      <path d="M150 100 L150 290" stroke-width="26"/>
      <path d="M150 290 C200 332 272 322 302 268" stroke-width="20"/>
    </g>
    <path d="M106 284 L262 100" fill="none" stroke="url(#a)" stroke-width="13" stroke-linecap="round"/>
    <circle cx="150" cy="56" r="14" fill="url(#a)"/>
    <path d="M222 162 L246 186 L222 210 L198 186 Z" fill="url(#a)"/>
  </g>

  <g fill="#9fb0c3">
    <circle cx="66" cy="120" r="4"/>
    <circle cx="338" cy="286" r="4"/>
    <rect x="330" y="104" width="8" height="8" rx="2" transform="rotate(45 334 108)"/>
    <rect x="62" y="278" width="8" height="8" rx="2" transform="rotate(45 66 282)"/>
  </g>
</svg>