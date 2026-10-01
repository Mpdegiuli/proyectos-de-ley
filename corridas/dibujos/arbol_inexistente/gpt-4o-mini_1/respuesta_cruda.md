```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="leafGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" style="stop-color:#A8D8B9; stop-opacity:1" />
      <stop offset="100%" style="stop-color:#6D9B91; stop-opacity:1" />
    </radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur" />
      <feFlood flood-color="rgba(255, 204, 0, 0.6)" result="glowColor" />
      <feComposite in2="blur" operator="in" />
      <feMerge>
        <feMergeNode />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <g id="tree">
    <rect x="190" y="300" width="20" height="80" fill="#854B32" />
    <ellipse cx="200" cy="250" rx="80" ry="50" fill="url(#leafGradient)" filter="url(#glow)" />
    <ellipse cx="150" cy="230" rx="50" ry="35" fill="url(#leafGradient)" filter="url(#glow)" />
    <ellipse cx="250" cy="230" rx="50" ry="35" fill="url(#leafGradient)" filter="url(#glow)" />
    <ellipse cx="125" cy="185" rx="40" ry="30" fill="url(#leafGradient)" filter="url(#glow)" />
    <ellipse cx="275" cy="185" rx="40" ry="30" fill="url(#leafGradient)" filter="url(#glow)" />
    <ellipse cx="200" cy="160" rx="60" ry="40" fill="url(#leafGradient)" filter="url(#glow)" />
    <ellipse cx="320" cy="300" rx="10" ry="20" fill="#8D5A2D" />
    <ellipse cx="80" cy="300" rx="10" ry="20" fill="#8D5A2D" />
    <ellipse cx="180" cy="380" rx="40" ry="10" fill="#7A4C2A" />
    <ellipse cx="220" cy="380" rx="40" ry="10" fill="#7A4C2A" />
  </g>
</svg>
```