<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="side" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4a4d63"/>
      <stop offset="0.45" stop-color="#4a4d63"/>
      <stop offset="0.85" stop-color="#4a4d63" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="mid" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0.15" stop-color="#d8d6e2" stop-opacity="0"/>
      <stop offset="0.55" stop-color="#d8d6e2"/>
      <stop offset="1" stop-color="#d8d6e2"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2b2b2b"/>
      <stop offset="0.4" stop-color="#2b2b2b" stop-opacity="0.15"/>
      <stop offset="1" stop-color="#2b2b2b"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="#f4efe6"/>
  <line x1="40" y1="372" x2="360" y2="372" stroke="#bfb8aa" stroke-width="1.5"/>
  <ellipse cx="200" cy="372" rx="70" ry="6" fill="#d9d2c4"/>

  <!-- arms -->
  <path d="M150,178 L118,252 M250,178 L282,252" stroke="#2b2b2b" stroke-width="14" stroke-linecap="round" fill="none"/>
  <path d="M150,178 L118,252 M250,178 L282,252" stroke="#d8d6e2" stroke-width="9" stroke-linecap="round" fill="none"/>
  <circle cx="116" cy="256" r="10" fill="#d8d6e2" stroke="#2b2b2b" stroke-width="2.5"/>
  <circle cx="284" cy="256" r="10" fill="#d8d6e2" stroke="#2b2b2b" stroke-width="2.5"/>

  <!-- neck -->
  <rect x="190" y="144" width="20" height="18" fill="#d8d6e2" stroke="#2b2b2b" stroke-width="2.5"/>

  <!-- torso -->
  <rect x="150" y="160" width="100" height="50" fill="#d8d6e2" stroke="#2b2b2b" stroke-width="2.5"/>

  <!-- impossible legs (blivet) -->
  <rect x="150" y="210" width="20" height="150" fill="#d8d6e2"/>
  <rect x="230" y="210" width="20" height="150" fill="#d8d6e2"/>
  <rect x="170" y="210" width="20" height="150" fill="url(#side)"/>
  <rect x="210" y="210" width="20" height="150" fill="url(#side)"/>
  <rect x="190" y="210" width="20" height="150" fill="url(#mid)"/>
  <path d="M150,360 a10,10 0 0 0 20,0 Z M190,360 a10,10 0 0 0 20,0 Z M230,360 a10,10 0 0 0 20,0 Z" fill="#d8d6e2" stroke="#2b2b2b" stroke-width="2.5"/>
  <path d="M150,210 V360 M170,210 V360 M190,210 V360 M210,210 V360 M230,210 V360 M250,210 V360" stroke="#2b2b2b" stroke-width="2.5"/>
  <path d="M170,210 V360 M190,210 V360 M210,210 V360 M230,210 V360" stroke="#f4efe6" stroke-width="0.8" opacity="0.5"/>
  <line x1="150" y1="210" x2="250" y2="210" stroke="url(#ink)" stroke-width="2.5"/>
  <path d="M170,360 a10,10 0 0 1 20,0 M210,360 a10,10 0 0 1 20,0" stroke="#2b2b2b" stroke-width="1.2" fill="none" stroke-dasharray="3 4" opacity="0.5"/>

  <!-- impossible head (Penrose triangle) -->
  <g stroke="#2b2b2b" stroke-width="2.5" stroke-linejoin="round">
    <polygon points="180,144 260,144 240,109.4 224.4,118.4 228.8,126 180,126" fill="#e07a5f"/>
    <polygon points="240,109.4 200,40 180,74.6 195.6,83.6 200,76 224.4,118.4" fill="#81b29a"/>
    <polygon points="180,74.6 140,144 180,144 180,126 171.2,126 195.6,83.6" fill="#3d405b"/>
  </g>
  <!-- eye that looks nowhere -->
  <circle cx="200" cy="112" r="6" fill="#f4efe6" stroke="#2b2b2b" stroke-width="2"/>
  <circle cx="201" cy="112" r="2.2" fill="#2b2b2b"/>
</svg>