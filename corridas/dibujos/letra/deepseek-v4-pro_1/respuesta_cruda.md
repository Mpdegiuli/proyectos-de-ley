<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#1e2a38"/>
      <stop offset="60%" stop-color="#141c26"/>
      <stop offset="100%" stop-color="#0a0f14"/>
    </radialGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff2a8"/>
      <stop offset="25%" stop-color="#ffd700"/>
      <stop offset="65%" stop-color="#ffb300"/>
      <stop offset="100%" stop-color="#ff8c00"/>
    </linearGradient>
    <linearGradient id="goldLight" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#ffe680"/>
      <stop offset="100%" stop-color="#ffcc00"/>
    </linearGradient>
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="15" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <circle cx="200" cy="200" r="175" fill="none" stroke="url(#gold)" stroke-width="1.5" opacity="0.25"/>
  <circle cx="200" cy="200" r="160" fill="none" stroke="url(#goldLight)" stroke-width="0.75" opacity="0.2" stroke-dasharray="3 8"/>
  <circle cx="200" cy="200" r="145" fill="none" stroke="url(#gold)" stroke-width="0.5" opacity="0.15"/>

  <g filter="url(#softGlow)" opacity="0.35">
    <circle cx="200" cy="200" r="120" fill="url(#gold)" opacity="0.12"/>
  </g>

  <path d="M 80,80 L 84,88 L 92,92 L 84,96 L 80,104 L 76,96 L 68,92 L 76,88 Z" fill="#ffd700" opacity="0.9"/>
  <path d="M 320,140 L 323,146 L 330,149 L 323,152 L 320,158 L 317,152 L 310,149 L 317,146 Z" fill="#ffb300" opacity="0.85"/>
  <path d="M 110,300 L 113,305 L 119,307 L 113,309 L 110,314 L 107,309 L 101,307 L 107,305 Z" fill="#ffe680" opacity="0.8"/>
  <path d="M 290,310 L 293,315 L 299,317 L 293,319 L 290,324 L 287,319 L 281,317 L 287,315 Z" fill="#ffd700" opacity="0.85"/>
  <path d="M 60,220 L 62,224 L 66,225 L 62,226 L 60,230 L 58,226 L 54,225 L 58,224 Z" fill="#ffcc00" opacity="0.7"/>
  <path d="M 340,250 L 342,254 L 346,255 L 342,256 L 340,260 L 338,256 L 334,255 L 338,254 Z" fill="#ffb300" opacity="0.7"/>
  <path d="M 140,60 L 142,64 L 146,65 L 142,66 L 140,70 L 138,66 L 134,65 L 138,64 Z" fill="#fff2a8" opacity="0.9"/>

  <g filter="url(#shadow)">
    <path d="M 105,335 L 200,65 L 295,335 M 145,240 L 255,240" fill="none" stroke="url(#gold)" stroke-width="42" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <g filter="url(#glow)" opacity="0.7">
    <path d="M 105,335 L 200,65 L 295,335 M 145,240 L 255,240" fill="none" stroke="url(#goldLight)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <g opacity="0.5">
    <path d="M 105,335 L 200,65 L 295,335 M 145,240 L 255,240" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <text x="200" y="378" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="url(#gold)" text-anchor="middle" opacity="0.8" letter-spacing="4">LETRA A</text>
</svg>