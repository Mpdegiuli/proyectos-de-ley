<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="72%">
      <stop offset="0%" stop-color="#3a2a62"/>
      <stop offset="58%" stop-color="#161022"/>
      <stop offset="100%" stop-color="#09070f"/>
    </radialGradient>
    <linearGradient id="gold" x1="200" y1="48" x2="200" y2="352" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fff8d6"/>
      <stop offset="38%" stop-color="#f3c453"/>
      <stop offset="100%" stop-color="#b86a12"/>
    </linearGradient>
    <radialGradient id="core" cx="38%" cy="32%" r="68%">
      <stop offset="0%" stop-color="#fffef8"/>
      <stop offset="42%" stop-color="#ffe39a"/>
      <stop offset="100%" stop-color="#e39a28"/>
    </radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="5.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="172" fill="none" stroke="#f3c453" stroke-opacity="0.16" stroke-width="1.5"/>
  <circle cx="200" cy="200" r="156" fill="none" stroke="#f3c453" stroke-opacity="0.3" stroke-width="1"/>
  <g filter="url(#glow)">
    <g stroke="url(#gold)" stroke-linecap="round" fill="none" stroke-width="24">
      <line x1="200" y1="48" x2="200" y2="352"/>
      <line x1="331.6" y1="124" x2="68.4" y2="276"/>
      <line x1="68.4" y1="124" x2="331.6" y2="276"/>
    </g>
    <g fill="url(#gold)">
      <circle cx="200" cy="48" r="13"/>
      <circle cx="200" cy="352" r="13"/>
      <circle cx="331.6" cy="124" r="13"/>
      <circle cx="68.4" cy="124" r="13"/>
      <circle cx="68.4" cy="276" r="13"/>
      <circle cx="331.6" cy="276" r="13"/>
    </g>
    <circle cx="200" cy="200" r="36" fill="url(#core)" stroke="#fff6d0" stroke-width="3"/>
    <circle cx="200" cy="200" r="12" fill="#fffef6"/>
  </g>
</svg>