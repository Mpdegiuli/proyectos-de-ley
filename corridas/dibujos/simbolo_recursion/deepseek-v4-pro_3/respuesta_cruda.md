```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="triGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00e5ff"/>
      <stop offset="100%" stop-color="#7c4dff"/>
    </linearGradient>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#ff00ff"/>
    </marker>
    <marker id="arrowSmall" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#00ffcc"/>
    </marker>
    <radialGradient id="glowCenter" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="400" height="400" fill="#0d1117"/>
  <circle cx="200" cy="220" r="180" fill="url(#glowCenter)" opacity="0.3"/>
  <polygon points="200,80 40,360 360,360" fill="url(#triGrad)" opacity="0.9"/>
  <polygon points="120,220 280,220 200,360" fill="#0d1117"/>
  <polygon points="160,150 240,150 200,220" fill="#0d1117"/>
  <polygon points="80,290 160,290 120,360" fill="#0d1117"/>
  <polygon points="240,290 320,290 280,360" fill="#0d1117"/>
  <polygon points="180,115 220,115 200,150" fill="#0d1117"/>
  <polygon points="140,185 180,185 160,220" fill="#0d1117"/>
  <polygon points="220,185 260,185 240,220" fill="#0d1117"/>
  <polygon points="60,325 100,325 80,360" fill="#0d1117"/>
  <polygon points="100,255 140,255 120,290" fill="#0d1117"/>
  <polygon points="140,325 180,325 160,360" fill="#0d1117"/>
  <polygon points="340,325 300,325 320,360" fill="#0d1117"/>
  <polygon points="300,255 260,255 280,290" fill="#0d1117"/>
  <polygon points="260,325 220,325 240,360" fill="#0d1117"/>
  <path d="M 200 390 A 170 170 0 1 1 199.9 390" fill="none" stroke="#ff00ff" stroke-width="3" stroke-linecap="round" marker-end="url(#arrow)" stroke-dasharray="10 8" opacity="0.8"/>
  <path d="M 180 280 A 20 20 0 1 1 179.9 280" fill="none" stroke="#00ffcc" stroke-width="2" stroke-linecap="round" marker-end="url(#arrowSmall)" stroke-dasharray="4 3" opacity="0.9"/>
</svg>
```