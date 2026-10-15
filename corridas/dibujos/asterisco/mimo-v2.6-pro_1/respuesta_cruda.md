```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Asterisco">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="72%">
      <stop offset="0" stop-color="#FFF9F1"/>
      <stop offset="1" stop-color="#FFE0BE"/>
    </radialGradient>
    <linearGradient id="arm" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#FFB03A"/>
      <stop offset="0.45" stop-color="#FF4B63"/>
      <stop offset="1" stop-color="#7B2FF7"/>
    </linearGradient>
    <linearGradient id="core" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset="1" stop-color="#FFD9A8"/>
    </linearGradient>
    <filter id="shadow" x="-40%" y="-40%" width="180%" height="180%">
      <feDropShadow dx="0" dy="12" stdDeviation="11" flood-color="#7B2FF7" flood-opacity="0.32"/>
    </filter>
    <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="7"/>
    </filter>
  </defs>

  <rect width="400" height="400" rx="48" fill="url(#bg)"/>

  <!-- resplandor -->
  <g stroke="#FF7A4D" stroke-width="70" stroke-linecap="round" opacity="0.18" filter="url(#soft)">
    <line x1="200" y1="200" x2="200" y2="60"/>
    <line x1="200" y1="200" x2="321.24" y2="130"/>
    <line x1="200" y1="200" x2="321.24" y2="270"/>
    <line x1="200" y1="200" x2="200" y2="340"/>
    <line x1="200" y1="200" x2="78.76" y2="270"/>
    <line x1="200" y1="200" x2="78.76" y2="130"/>
  </g>

  <!-- brazos -->
  <g stroke="url(#arm)" stroke-width="46" stroke-linecap="round" filter="url(#shadow)">
    <line x1="200" y1="200" x2="200" y2="60"/>
    <line x1="200" y1="200" x2="321.24" y2="130"/>
    <line x1="200" y1="200" x2="321.24" y2="270"/>
    <line x1="200" y1="200" x2="200" y2="340"/>
    <line x1="200" y1="200" x2="78.76" y2="270"/>
    <line x1="200" y1="200" x2="78.76" y2="130"/>
  </g>

  <!-- brillos -->
  <g stroke="#FFFFFF" stroke-width="9" stroke-linecap="round" opacity="0.55">
    <line x1="200" y1="196" x2="200" y2="86"/>
    <line x1="200" y1="200" x2="305.3" y2="138.8"/>
    <line x1="200" y1="200" x2="200" y2="314"/>
  </g>

  <circle cx="200" cy="200" r="34" fill="url(#core)"/>
  <circle cx="200" cy="200" r="34" fill="none" stroke="#FF4B63" stroke-width="6" opacity="0.6"/>
  <circle cx="190" cy="189" r="10" fill="#FFFFFF" opacity="0.9"/>
</svg>
```