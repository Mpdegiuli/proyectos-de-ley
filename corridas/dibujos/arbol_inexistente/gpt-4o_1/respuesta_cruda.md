```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="leafGradient" cx="0.5" cy="0.5" r="0.5" fx="0.5" fy="0.5">
      <stop offset="0%" stop-color="#98ff98" />
      <stop offset="100%" stop-color="#32a852" />
    </radialGradient>
    <radialGradient id="trunkGradient" cx="0.5" cy="0.5" r="0.5" fx="0.5" fy="0.5">
      <stop offset="0%" stop-color="#8b5a2b" />
      <stop offset="100%" stop-color="#654321" />
    </radialGradient>
    <linearGradient id="fruitGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff5c33"/>
      <stop offset="100%" stop-color="#ffcc66"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="#ccffff" />
  <g transform="translate(200, 300)">
    <path d="M-15,0 C-20,-30 -10,-70 0,-100 C10,-70 20,-30 15,0 Z" fill="url(#trunkGradient)"/>
    <circle cx="0" cy="-100" r="80" fill="url(#leafGradient)" />
    <circle cx="-50" cy="-140" r="50" fill="url(#leafGradient)" />
    <circle cx="50" cy="-140" r="50" fill="url(#leafGradient)" />
    <circle cx="-30" cy="-190" r="40" fill="url(#leafGradient)" />
    <circle cx="30" cy="-190" r="40" fill="url(#leafGradient)" />
    <g fill="url(#fruitGradient)">
      <circle cx="-30" cy="-160" r="10" />
      <circle cx="30" cy="-120" r="10" />
      <circle cx="-60" cy="-110" r="10" />
      <circle cx="10" cy="-190" r="10" />
      <circle cx="40" cy="-180" r="10" />
    </g>
  </g>
</svg>
```