<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="400" height="400" fill="#0a0a2e"/>
  
  <!-- Stars -->
  <circle cx="30" cy="20" r="1.5" fill="white" opacity="0.8"/>
  <circle cx="80" cy="50" r="1" fill="white" opacity="0.6"/>
  <circle cx="150" cy="15" r="1.5" fill="white" opacity="0.9"/>
  <circle cx="220" cy="35" r="1" fill="white" opacity="0.7"/>
  <circle cx="300" cy="20" r="1.5" fill="white" opacity="0.8"/>
  <circle cx="370" cy="45" r="1" fill="white" opacity="0.6"/>
  <circle cx="350" cy="80" r="1.5" fill="white" opacity="0.9"/>
  <circle cx="60" cy="100" r="1" fill="white" opacity="0.5"/>
  <circle cx="390" cy="130" r="1.5" fill="white" opacity="0.7"/>
  <circle cx="10" cy="160" r="1" fill="white" opacity="0.6"/>
  
  <!-- Circuit board lines - representing AI neural network -->
  <g stroke="#1a3a6e" stroke-width="1" fill="none" opacity="0.5">
    <line x1="0" y1="200" x2="400" y2="200"/>
    <line x1="200" y1="0" x2="200" y2="400"/>
    <line x1="0" y1="100" x2="400" y2="100"/>
    <line x1="0" y1="300" x2="400" y2="300"/>
    <line x1="100" y1="0" x2="100" y2="400"/>
    <line x1="300" y1="0" x2="300" y2="400"/>
  </g>
  
  <!-- Glowing orb / head shape -->
  <defs>
    <radialGradient id="headGrad" cx="50%" cy="45%" r="50%">
      <stop offset="0%" stop-color="#4fc3f7"/>
      <stop offset="40%" stop-color="#1565c0"/>
      <stop offset="100%" stop-color="#0a0a2e"/>
    </radialGradient>
    <radialGradient id="glowGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4fc3f7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#4fc3f7" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="eyeGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="white"/>
      <stop offset="40%" stop-color="#80deea"/>
      <stop offset="100%" stop-color="#006064"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="softglow">
      <feGaussianBlur stdDeviation="8" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Outer glow halo -->
  <ellipse cx="200" cy="185" rx="120" ry="130" fill="url(#glowGrad)"/>
  
  <!-- Neck -->
  <rect x="175" y="290" width="50" height="60" rx="10" fill="url(#headGrad)" opacity="0.9"/>
  
  <!-- Shoulders -->
  <ellipse cx="200" cy="360" rx="100" ry="30" fill="#1565c0" opacity="0.8"/>
  
  <!-- Head -->
  <ellipse cx="200" cy="190" rx="100" ry="115" fill="url(#headGrad)"/>
  
  <!-- Head outline glow -->
  <ellipse cx="200" cy="190" rx="100" ry="115" fill="none" stroke="#4fc3f7" stroke-width="2" opacity="0.6" filter="url(#glow)"/>
  
  <!-- Binary data streams on sides of head -->
  <g fill="#4fc3f7" font-family="monospace" font-size="8" opacity="0.4">
    <text x="108" y="150">01</text>
    <text x="108" y="165">10</text>
    <text x="108" y="180">11</text>
    <text x="108" y="195">00</text>
    <text x="275" y="150">10</text>
    <text x="275" y="165">01</text>
    <text x="275" y="180">11</text>
    <text x="275" y="195">00</text>
  </g>
  
  <!-- Eyes -->
  <ellipse cx="165" cy="185" rx="22" ry="20" fill="url(#eyeGrad)" filter="url(#glow)"/>
  <ellipse cx="235" cy="185" rx="22" ry="20" fill="url(#eyeGrad)" filter="url(#glow)"/>
  
  <!-- Eye pupils - hexagonal/digital -->
  <circle cx="165" cy="185" r="10" fill="#003f51"/>
  <circle cx="235" cy="185" r="10" fill="#003f51"/>
  
  <!-- Pupil inner glow -->
  <circle cx="165" cy="185" r="5" fill="#00e5ff" filter="url(#glow)"/>
  <circle cx="235" cy="185" r="5" fill="#00e5ff" filter="url(#glow)"/>
  
  <!-- Eye shine -->
  <circle cx="170" cy="180" r="3" fill="white" opacity="0.8"/>
  <circle cx="240" cy="180" r="3" fill="white" opacity="0.8"/>
  
  <!-- Nose - subtle geometric -->
  <path d="M200 200 L193 225 L207 225" fill="none" stroke="#4fc3f7" stroke-width="1.5" opacity="0.5"/>
  
  <!-- Mouth - slight smile, digital style -->
  <path d="M178 248 Q200 262 222 248" fill="none" stroke="#4fc3f7" stroke-width="2.5" stroke-linecap="round" filter="url(#glow)" opacity="0.9"/>
  
  <!-- Eyebrows - geometric -->
  <path d="M145 162 L185 158" stroke="#80deea" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
  <path d="M215 158 L255 162" stroke="#80deea" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
  
  <!-- Neural network nodes on forehead -->
  <circle cx="200" cy="118" r="5" fill="#00e5ff" filter="url(#glow)" opacity="0.8"/>
  <circle cx="175" cy="128" r="3" fill="#4fc3f7" opacity="0.7"/>
  <circle cx="225" cy="128" r="3" fill="#4fc3f7" opacity="0.7"/>
  <line x1="200" y1="118" x2="175" y2="128" stroke="#4fc3f7" stroke-width="1" opacity="0.5"/>
  <line x1="200" y1="118" x2="225" y2="128" stroke="#4fc3f7" stroke-width="1" opacity="0.5"/>
  <line x1="175" y1="128" x2="165" y2="145" stroke="#4fc3f7" stroke-width="1" opacity="0.4"/>
  <line x1="225" y1="128" x2="235" y2="145" stroke="#4fc3f7" stroke-width="1" opacity="0.4"/>
  
  <!-- Label -->
  <text x="200" y="395" text-anchor="middle" fill="#4fc3f7" font-family="monospace" font-size="11" opacity="0.8">Claude · AI · Anthropic</text>
</svg>