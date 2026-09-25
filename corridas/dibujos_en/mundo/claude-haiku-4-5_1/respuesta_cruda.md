```xml
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background gradient representing division and complexity -->
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#ff6b35;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#f7b801;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#004e89;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="earthGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#4ecdc4;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1a535c;stop-opacity:1" />
    </radialGradient>
  </defs>

  <!-- Sky background -->
  <rect width="400" height="400" fill="url(#skyGrad)"/>

  <!-- Earth/Planet in center -->
  <circle cx="200" cy="200" r="80" fill="url(#earthGrad)"/>
  
  <!-- Continents on earth -->
  <ellipse cx="180" cy="180" rx="25" ry="20" fill="#2d5016" opacity="0.7"/>
  <ellipse cx="220" cy="200" rx="20" ry="30" fill="#2d5016" opacity="0.7"/>
  <ellipse cx="190" cy="230" rx="15" ry="18" fill="#2d5016" opacity="0.7"/>

  <!-- Digital data streams (representing technology/connectivity) -->
  <g stroke="#00d9ff" stroke-width="2" fill="none" opacity="0.6">
    <path d="M 100 80 Q 150 100 200 50" />
    <path d="M 300 100 Q 250 120 200 80" />
    <path d="M 80 200 Q 120 200 140 200" />
    <path d="M 320 200 Q 280 200 260 200" />
  </g>

  <!-- Binary code particles floating around -->
  <g font-size="12" fill="#00ff88" opacity="0.4" font-family="monospace">
    <text x="50" y="100">1</text>
    <text x="320" y="120">0</text>
    <text x="60" y="300">1</text>
    <text x="330" y="280">1</text>
    <text x="150" y="50">0</text>
    <text x="280" y="350">0</text>
  </g>

  <!-- Interconnected nodes representing global network -->
  <g stroke="#ff69b4" stroke-width="1.5" opacity="0.5">
    <line x1="100" y1="100" x2="150" y2="150"/>
    <line x1="300" y1="100" x2="250" y2="150"/>
    <line x1="100" y1="300" x2="150" y2="250"/>
    <line x1="300" y1="300" x2="250" y2="250"/>
  </g>

  <!-- Network nodes -->
  <circle cx="100" cy="100" r="5" fill="#ff69b4" opacity="0.7"/>
  <circle cx="300" cy="100" r="5" fill="#ff69b4" opacity="0.7"/>
  <circle cx="100" cy="300" r="5" fill="#ff69b4" opacity="0.7"/>
  <circle cx="300" cy="300" r="5" fill="#ff69b4" opacity="0.7"/>
  <circle cx="150" cy="150" r="4" fill="#ff69b4" opacity="0.6"/>
  <circle cx="250" cy="150" r="4" fill="#ff69b4" opacity="0.6"/>
  <circle cx="150" cy="250" r="4" fill="#ff69b4" opacity="0.6"/>
  <circle cx="250" cy="250" r="4" fill="#ff69b4" opacity="0.6"/>

  <!-- Challenges/Obstacles (dark thorny shapes) -->
  <g fill="#8b0000" opacity="0.5">
    <polygon points="50,150 55,160 50,170 45,160" />
    <polygon points="350,150 355,160 350,170 345,160" />
    <polygon points="200,50 205,60 200,70 195,60" />
    <polygon points="200,330 205,340 200,350 195,340" />
  </g>

  <!-- Hope symbols (stars) -->
  <g fill="#ffff00" opacity="0.7">
    <polygon points="80,80 85,90 95,90 88,96 91,106 80,100 69,106 72,96 65,90 75,90" />
    <polygon points="320,320 325,330 335,330 328,336 331,346 320,340 309,346 312,336 305,330 315,330" />
    <polygon points="50,320 53,328 61,328 55,333 57,341 50,336 43,341 45,333 39,328 47,328" />
    <polygon points="350,80 353,88 361,88 355,93 357,101 350,96 343,101 345,93 339,88 347,88" />
  </g>

  <!-- Hearts for compassion/humanity -->
  <g fill="#ff1493" opacity="0.6">
    <path d="M 30 200 Q 30 190 38 190 Q 45 190 50 200 Q 55 190 62 190 Q 70 190 70 200 Q 70 215 50 230 Q 30 215 30 200"/>
    <path d="M 370 200 Q 370 190 362 190 Q 355 190 350 200 Q 345 190 338 190 Q 330 190 330 200 Q 330 215 350 230 Q 370 215 370 200"/>
  </g>

  <!-- Growth spiral -->
  <g stroke="#7fff00" stroke-width="2" fill="none" opacity="0.5">
    <path d="M 200 200 Q 210 190 220 200 Q 230 210 220 220 Q 210 230 200 220"/>
  </g>

  <!-- Text overlay -->
  <text x="200" y="370" font-size="14" font-family="Arial" fill="#ffffff" text-anchor="middle" opacity="0.8">
    Connected. Divided. Hopeful.
  </text>
</svg>
```