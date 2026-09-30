```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#1c1c20"/>
      <stop offset="100%" stop-color="#0b0b0d"/>
    </radialGradient>
    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="7"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.8  0 0 0 0 0.8  0 0 0 0 0.85  0 0 0 0.9 -0.25"/>
    </filter>
    <filter id="dust" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="turbulence" baseFrequency="0.012" numOctaves="2" seed="3"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.6  0 0 0 0 0.62  0 0 0 0 0.7  0 0 0 0.35 -0.05"/>
      <feGaussianBlur stdDeviation="2"/>
    </filter>
    <radialGradient id="hole" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#000"/>
      <stop offset="62%" stop-color="#000"/>
      <stop offset="100%" stop-color="#fff"/>
    </radialGradient>
    <mask id="absence">
      <rect width="400" height="400" fill="#fff"/>
      <circle cx="200" cy="200" r="120" fill="url(#hole)"/>
    </mask>
    <radialGradient id="rim" cx="50%" cy="50%" r="50%">
      <stop offset="70%" stop-color="#000" stop-opacity="0"/>
      <stop offset="92%" stop-color="#8a8c96" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <g mask="url(#absence)">
    <rect width="400" height="400" filter="url(#dust)"/>
    <rect width="400" height="400" filter="url(#grain)" opacity="0.55"/>
  </g>

  <circle cx="200" cy="200" r="112" fill="#000"/>
  <circle cx="200" cy="200" r="130" fill="url(#rim)"/>
</svg>
```