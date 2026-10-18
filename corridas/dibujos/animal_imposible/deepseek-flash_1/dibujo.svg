<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bgGlow" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#2a1a3a" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0a0a0a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="tailGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffb3b3"/>
      <stop offset="100%" stop-color="#d2a8ff"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1a1a1a" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="400" height="400" fill="#0a0a0a"/>
  <rect width="400" height="400" fill="url(#grid)"/>
  <rect width="400" height="400" fill="url(#bgGlow)"/>

  <!-- Floating impossible shapes -->
  <g opacity="0.4">
    <polygon points="320,60 340,50 360,60 340,70" fill="#fff"/>
    <polygon points="320,60 340,70 340,90 320,80" fill="#ccc"/>
    <polygon points="340,70 360,60 360,80 340,90" fill="#aaa"/>
  </g>
  <g opacity="0.5">
    <path d="M 80 60 L 100 90 L 60 90 Z" fill="none" stroke="#fff" stroke-width="1.5"/>
    <path d="M 80 70 L 90 85 L 70 85 Z" fill="none" stroke="#fff" stroke-width="1.5"/>
  </g>
  <g opacity="0.6">
    <circle cx="50" cy="50" r="1.5" fill="#fff"/>
    <circle cx="350" cy="80" r="2" fill="#fff"/>
    <circle cx="70" cy="250" r="1" fill="#fff"/>
    <circle cx="330" cy="280" r="1.5" fill="#fff"/>
    <circle cx="280" cy="40" r="2" fill="#fff"/>
    <circle cx="120" cy="30" r="1.5" fill="#fff"/>
  </g>

  <!-- Shadow -->
  <ellipse cx="200" cy="360" rx="90" ry="15" fill="#000" opacity="0.6"/>

  <!-- Back Tail (Behind the triangle) -->
  <path d="M 280 300 C 340 320, 360 220, 300 180" stroke="url(#tailGrad)" stroke-width="12" fill="none" stroke-linecap="round"/>

  <!-- Penrose Triangle Body -->
  <g stroke="#fff" stroke-width="2" stroke-linejoin="round">
    <!-- Left Beam -->
    <polygon points="200,120 100,280 150,320 200,200" fill="#2d2d2d" opacity="0.9"/>
    <!-- Bottom Beam -->
    <polygon points="100,280 300,280 250,320 150,320" fill="#3d3d3d" opacity="0.9"/>
    <!-- Right Beam -->
    <polygon points="200,120 300,280 250,320 200,200" fill="#4d4d4d" opacity="0.9"/>
  </g>

  <!-- Cat Head -->
  <g>
    <!-- Ears -->
    <polygon points="170,55 150,10 190,40" fill="#e0e0e0" stroke="#fff" stroke-width="2"/>
    <polygon points="230,55 250,10 210,40" fill="#e0e0e0" stroke="#fff" stroke-width="2"/>
    <polygon points="172,50 158,20 185,42" fill="#ffb3b3"/>
    <polygon points="228,50 242,20 215,42" fill="#ffb3b3"/>
    <!-- Head Base -->
    <circle cx="200" cy="80" r="40" fill="#e0e0e0" stroke="#fff" stroke-width="2"/>
    <!-- Eyes -->
    <ellipse cx="180" cy="75" rx="8" ry="12" fill="#1a1a2e"/>
    <ellipse cx="220" cy="75" rx="8" ry="12" fill="#1a1a2e"/>
    <ellipse cx="180" cy="75" rx="3" ry="6" fill="#fff" filter="url(#glow)"/>
    <ellipse cx="220" cy="75" rx="3" ry="6" fill="#fff" filter="url(#glow)"/>
    <!-- Nose and Mouth -->
    <polygon points="195,90 205,90 200,97" fill="#ffb3b3"/>
    <path d="M 190 102 Q 200 107 200 102 Q 200 107 210 102" stroke="#1a1a2e" stroke-width="2" fill="none"/>
    <!-- Whiskers -->
    <line x1="160" y1="85" x2="130" y2="80" stroke="#e0e0e0" stroke-width="2"/>
    <line x1="160" y1="95" x2="130" y2="100" stroke="#e0e0e0" stroke-width="2"/>
    <line x1="240" y1="85" x2="270" y2="80" stroke="#e0e0e0" stroke-width="2"/>
    <line x1="240" y1="95" x2="270" y2="100" stroke="#e0e0e0" stroke-width="2"/>
  </g>

  <!-- Collar -->
  <path d="M 170 110 Q 200 125 230 110" stroke="#ffb3b3" stroke-width="8" fill="none"/>
  <circle cx="200" cy="120" r="6" fill="#f5c542"/>

  <!-- Front Tail (Weaving through the impossible geometry) -->
  <path d="M 300 180 C 280 160, 240 180, 180 220" stroke="url(#tailGrad)" stroke-width="12" fill="none" stroke-linecap="round"/>

  <!-- Paws -->
  <g fill="#e0e0e0" stroke="#fff" stroke-width="2">
    <path d="M 120 320 Q 100 340 120 350 Q 140 340 120 320"/>
    <path d="M 250 320 Q 230 340 250 350 Q 270 340 250 320"/>
  </g>
  <g stroke="#1a1a2e" stroke-width="2">
    <line x1="115" y1="345" x2="115" y2="350"/>
    <line x1="125" y1="345" x2="125" y2="350"/>
    <line x1="245" y1="345" x2="245" y2="350"/>
    <line x1="255" y1="345" x2="255" y2="350"/>
  </g>
</svg>