<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.15" y2="1">
      <stop offset="0%" stop-color="#1c1f2a"/>
      <stop offset="52%" stop-color="#0c0e14"/>
      <stop offset="100%" stop-color="#05060a"/>
    </linearGradient>
    <radialGradient id="spot" cx="50%" cy="40%" r="46%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.075"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="vig" cx="50%" cy="48%" r="70%">
      <stop offset="58%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.62"/>
    </radialGradient>
    <linearGradient id="L" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fffaf3"/>
      <stop offset="100%" stop-color="#e6d8c4"/>
    </linearGradient>
    <linearGradient id="R" x1="1" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#dccdb8"/>
      <stop offset="100%" stop-color="#c3b29c"/>
    </linearGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff9f1"/>
      <stop offset="42%" stop-color="#f2e4ce"/>
      <stop offset="100%" stop-color="#dcc8ac"/>
    </linearGradient>
    <linearGradient id="wound" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#9ee7ff"/>
      <stop offset="55%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#ff7d9c"/>
    </linearGradient>
    <filter id="sh" x="-45%" y="-45%" width="190%" height="190%">
      <feDropShadow dx="0" dy="18" stdDeviation="8" flood-color="#000000" flood-opacity="0.55"/>
    </filter>
    <filter id="g" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="1" seed="4"/>
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0.05 0"/>
    </filter>
    <clipPath id="rleg">
      <polygon points="200,74 226,74 292,308 250,308"/>
    </clipPath>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#spot)"/>
  <circle cx="200" cy="196" r="158" fill="none" stroke="#f4eadc" stroke-opacity="0.045" stroke-width="1"/>
  <circle cx="200" cy="196" r="112" fill="none" stroke="#f4eadc" stroke-opacity="0.035" stroke-width="1"/>
  <ellipse cx="200" cy="334" rx="124" ry="11" fill="#000000" opacity="0.42"/>
  <g filter="url(#sh)">
    <polygon points="174,74 108,308 98,322 164,88" fill="#c9b79f"/>
    <polygon points="108,308 150,308 160,322 118,322" fill="#4a3d32"/>
    <polygon points="174,74 200,74 150,308 108,308" fill="url(#L)"/>
    <polygon points="226,74 292,308 304,322 238,88" fill="#7d6a58"/>
    <polygon points="250,308 292,308 304,322 262,322" fill="#3c322a"/>
    <polygon points="200,74 226,74 292,308 250,308" fill="url(#R)"/>
    <polygon points="164,60 238,60 226,74 174,74" fill="#fffaf2"/>
    <polygon points="200,92 178,164 222,164" fill="#000000" opacity="0.16"/>
    <polygon points="116,166 236,166 242,194 122,194" fill="url(#bar)"/>
    <polygon points="122,194 242,194 248,207 116,207" fill="#6d5b49"/>
    <rect x="190" y="158" width="120" height="56" fill="#cfc0ab" clip-path="url(#rleg)"/>
    <polygon points="228,166 286,166 292,194 234,194" fill="url(#bar)"/>
    <polygon points="234,194 292,194 298,207 240,207" fill="#6d5b49"/>
    <polyline points="228,166 234,194 240,207" fill="none" stroke="url(#wound)" stroke-width="1.35" stroke-linecap="round"/>
    <path d="M128 171 H226" fill="none" stroke="#ffffff" stroke-opacity="0.55" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M240 171 H280" fill="none" stroke="#ffffff" stroke-opacity="0.7" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M178 78 H222" fill="none" stroke="#ffffff" stroke-opacity="0.45" stroke-width="1.2" stroke-linecap="round"/>
  </g>
  <rect width="400" height="400" fill="url(#vig)"/>
  <rect width="400" height="400" filter="url(#g)"/>
</svg>