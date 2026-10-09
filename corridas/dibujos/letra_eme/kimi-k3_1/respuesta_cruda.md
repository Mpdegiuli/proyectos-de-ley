<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#12142a"/>
      <stop offset="1" stop-color="#1e2a4a"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffe29a"/>
      <stop offset="1" stop-color="#ff9d5c"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="152" fill="none" stroke="#ffffff" stroke-opacity="0.06" stroke-width="2"/>
  <rect x="22" y="22" width="356" height="356" rx="22" fill="none" stroke="#8ea0c9" stroke-opacity="0.25" stroke-width="2"/>
  <g stroke="#8ea0c9" stroke-opacity="0.18" stroke-width="2" stroke-dasharray="2 8">
    <line x1="44" y1="86" x2="356" y2="86"/>
    <line x1="44" y1="270" x2="356" y2="270"/>
  </g>
  <g fill="none" stroke="url(#ink)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)">
    <path d="M60,206 C68,158 80,142 96,136"/>
    <path d="M96,136 L96,270"/>
    <path d="M96,142 C96,104 116,86 141,86 C166,86 184,106 184,144 L184,270"/>
    <path d="M184,158 C184,124 204,108 227,108 C251,108 268,126 268,158 L268,268"/>
    <path d="M268,268 C268,298 282,310 302,300"/>
  </g>
  <circle cx="96" cy="104" r="8" fill="#ff7b6b"/>
  <g fill="none" stroke="#7be0d3" stroke-width="8" stroke-linecap="round">
    <path d="M306,104 A16,16 0 0 1 306,136" stroke-opacity="0.95"/>
    <path d="M306,90 A30,30 0 0 1 306,150" stroke-opacity="0.6"/>
    <path d="M306,76 A44,44 0 0 1 306,164" stroke-opacity="0.35"/>
  </g>
  <text x="200" y="366" text-anchor="middle" font-family="Georgia, serif" font-size="19" letter-spacing="8" fill="#9fb2d8" fill-opacity="0.85">eme</text>
</svg>