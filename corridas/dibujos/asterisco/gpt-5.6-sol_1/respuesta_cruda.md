<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0" stop-color="#28334f"/>
      <stop offset="1" stop-color="#101522"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff3a6"/>
      <stop offset=".45" stop-color="#ffc83d"/>
      <stop offset="1" stop-color="#ff7a18"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="7" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="400" height="400" rx="36" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="145" fill="none" stroke="#fff" stroke-opacity=".08" stroke-width="2"/>
  <g fill="none" stroke="url(#gold)" stroke-width="42" stroke-linecap="round" filter="url(#glow)">
    <path d="M200 74V326"/>
    <path d="M91 137L309 263"/>
    <path d="M309 137L91 263"/>
  </g>
  <circle cx="200" cy="200" r="18" fill="#fff7c7" opacity=".75"/>
</svg>