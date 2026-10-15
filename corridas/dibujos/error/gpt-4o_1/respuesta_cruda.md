```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="grad1" cx="50%" cy="50%" r="50%" fx="70%" fy="30%">
      <stop offset="0%" style="stop-color:rgb(255,223,186);stop-opacity:1"/>
      <stop offset="100%" style="stop-color:rgb(255,182,193);stop-opacity:1"/>
    </radialGradient>
    <radialGradient id="grad2" cx="50%" cy="50%" r="50%" fx="30%" fy="70%">
      <stop offset="0%" style="stop-color:rgb(173,216,230);stop-opacity:1"/>
      <stop offset="100%" style="stop-color:rgb(255,245,238);stop-opacity:1"/>
    </radialGradient>
    <filter id="f1" x="0" y="0">
      <feTurbulence type="fractalNoise" baseFrequency="0.01" numOctaves="5"/>
      <feDisplacementMap in="SourceGraphic" scale="10"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#grad1)" />
  <circle cx="200" cy="200" r="100" fill="url(#grad2)" filter="url(#f1)" />
  <ellipse cx="140" cy="160" rx="20" ry="30" fill="url(#grad2)" />
  <ellipse cx="260" cy="160" rx="20" ry="30" fill="url(#grad2)" />
  <path d="M150 250 C180 300, 220 300, 250 250" stroke="rgb(255,99,71)" stroke-width="5" fill="none" />
  <line x1="190" y1="170" x2="200" y2="180" stroke="rgb(255,20,147)" stroke-width="3" />
  <line x1="210" y1="170" x2="200" y2="180" stroke="rgb(255,20,147)" stroke-width="3" />
  <polygon points="200,300 180,340 220,340" fill="rgb(255,69,0)" opacity="0.7" />
  <text x="100" y="390" font-family="sans-serif" font-size="20" fill="rgb(50,205,50)">Perfection in Imperfection</text>
</svg>
```