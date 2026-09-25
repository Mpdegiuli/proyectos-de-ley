```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="glow-heavy" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.1" />
    </pattern>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.5" fill="#00e5ff" opacity="0.6" />
    </pattern>
    <radialGradient id="globeCore" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#0055ff" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="lineGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00e5ff" />
      <stop offset="100%" stop-color="#0055ff" />
    </linearGradient>
    <linearGradient id="lineGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="100%" stop-color="#a200ff" />
    </linearGradient>
  </defs>

  <!-- Background Layers -->
  <rect width="400" height="400" fill="#050510" />
  <rect width="400" height="400" fill="url(#grid)" />
  <rect width="400" height="400" fill="url(#dots)" />

  <!-- Cyberspace Perspective Grid -->
  <g stroke="#00e5ff" fill="none" opacity="0.3">
    <line x1="0" y1="380" x2="400" y2="380" stroke-width="0.5"/>
    <line x1="0" y1="340" x2="400" y2="340" stroke-width="0.5"/>
    <line x1="0" y1="310" x2="400" y2="310" stroke-width="0.5"/>
    <line x1="0" y1="290" x2="400" y2="290" stroke-width="0.5"/>
    <line x1="0" y1="275" x2="400" y2="275" stroke-width="0.5"/>
    <line x1="0" y1="265" x2="400" y2="265" stroke-width="0.5"/>
    <line x1="200" y1="265" x2="0" y2="400" stroke-width="0.5"/>
    <line x1="200" y1="265" x2="100" y2="400" stroke-width="0.5"/>
    <line x1="200" y1="265" x2="200" y2="400" stroke-width="0.5"/>
    <line x1="200" y1="265" x2="300" y2="400" stroke-width="0.5"/>
    <line x1="200" y1="265" x2="400" y2="400" stroke-width="0.5"/>
    <line x1="200" y1="265" x2="-50" y2="400" stroke-width="0.5"/>
    <line x1="200" y1="265" x2="450" y2="400" stroke-width="0.5"/>
  </g>

  <!-- Global Core Sphere -->
  <g transform="translate(200, 200)">
    <circle cx="0" cy="0" r="110" fill="url(#globeCore)" />
    <g stroke="#00e5ff" fill="none" opacity="0.7">
      <circle cx="0" cy="0" r="100" stroke-width="1.5" />
      <ellipse cx="0" cy="0" rx="100" ry="30" stroke-width="1" />
      <ellipse cx="0" cy="0" rx="100" ry="60" stroke-width="1" />
      <ellipse cx="0" cy="0" rx="30" ry="100" stroke-width="1" />
      <ellipse cx="0" cy="0" rx="60" ry="100" stroke-width="1" />
      <ellipse cx="0" cy="0" rx="100" ry="90" stroke-width="1" />
      <ellipse cx="0" cy="0" rx="90" ry="100" stroke-width="1" />
      <ellipse cx="0" cy="0" rx="70" ry="100" transform="rotate(45)" stroke-width="1" />
      <ellipse cx="0" cy="0" rx="100" ry="70" transform="rotate(-45)" stroke-width="1" />
    </g>
    <circle cx="0" cy="0" r="20" fill="#00e5ff" filter="url(#glow)" opacity="0.6" />
  </g>

  <!-- Neural Network Connections -->
  <g fill="none" stroke-width="1.5">
    <g stroke="url(#lineGrad1)" filter="url(#glow)">
      <path d="M 60 80 Q 150 150 200 200" />
      <path d="M 330 60 Q 250 150 200 200" />
      <path d="M 60 320 Q 150 250 200 200" />
      <path d="M 340 310 Q 250 250 200 200" />
      <path d="M 100 30 Q 150 150 200 200" />
      <path d="M 300 370 Q 250 250 200 200" />
      <path d="M 40 200 Q 130 180 200 200" />
      <path d="M 360 180 Q 270 180 200 200" />
    </g>
    <g stroke="url(#lineGrad2)" filter="url(#glow)">
      <path d="M 80 100 Q 200 80 320 100" />
      <path d="M 70 300 Q 200 320 330 300" />
      <path d="M 50 150 Q 150 250 80 350" />
      <path d="M 350 150 Q 250 250 320 350" />
      <path d="M 150 350 Q 200 300 250 350" />
    </g>
    <g stroke="#f0e68c" fill="none" stroke-width="1" stroke-dasharray="4 4" filter="url(#glow)">
      <path d="M 100 30 Q 40 200 80 350" />
      <path d="M 300 370 Q 360 200 320 100" />
      <path d="M 40 200 Q 200 80 320 100" />
      <path d="M 360 180 Q 200 320 80 350" />
    </g>
  </g>

  <!-- Network Nodes -->
  <g>
    <g fill="#00e5ff" filter="url(#glow)">
      <circle cx="60" cy="80" r="4" />
      <circle cx="330" cy="60" r="4" />
      <circle cx="60" cy="320" r="4" />
      <circle cx="340" cy="310" r="4" />
      <circle cx="100" cy="30" r="3" />
      <circle cx="300" cy="370" r="3" />
      <circle cx="40" cy="200" r="3" />
      <circle cx="360" cy="180" r="3" />
    </g>
    <g fill="#ff007f" filter="url(#glow)">
      <circle cx="80" cy="100" r="4" />
      <circle cx="320" cy="100" r="4" />
      <circle cx="80" cy="350" r="5" />
      <circle cx="320" cy="350" r="5" />
      <circle cx="70" cy="300" r="3" />
      <circle cx="330" cy="300" r="3" />
      <circle cx="50" cy="150" r="3" />
      <circle cx="350" cy="150" r="3" />
    </g>
    <g fill="#ffffff" filter="url(#glow)">
      <circle cx="200" cy="20" r="2" />
      <circle cx="200" cy="380" r="2" />
      <circle cx="10" cy="200" r="2" />
      <circle cx="390" cy="200" r="2" />
      <circle cx="150" cy="120" r="2" />
      <circle cx="250" cy="280" r="2" />
    </g>
  </g>

  <!-- Signal Rings -->
  <g fill="none" stroke-width="1.5">
    <circle cx="60" cy="80" r="8" stroke="#00e5ff" opacity="0.6" />
    <circle cx="60" cy="80" r="14" stroke="#00e5ff" opacity="0.3" />
    <circle cx="340" cy="310" r="10" stroke="#00e5ff" opacity="0.6" />
    <circle cx="340" cy="310" r="16" stroke="#00e5ff" opacity="0.3" />
    <circle cx="80" cy="350" r="9" stroke="#ff007f" opacity="0.6" />
    <circle cx="80" cy="350" r="15" stroke="#ff007f" opacity="0.3" />
    <circle cx="320" cy="100" r="8" stroke="#ff007f" opacity="0.6" />
  </g>

  <!-- Data Streams & Matrix Code -->
  <g font-family="monospace" font-size="8" fill="#00e5ff" opacity="0.7">
    <text x="35" y="100">01001</text>
    <text x="35" y="110">11010</text>
    <text x="35" y="120">10100</text>
    <text x="350" y="280">10110</text>
    <text x="350" y="290">01011</text>
    <text x="350" y="300">11001</text>
    <text x="150" y="40">0110</text>
    <text x="150" y="50">1001</text>
    <text x="280" y="360">1111</text>
    <text x="280" y="370">0000</text>
  </g>
  <g font-family="monospace" font-size="8" fill="#ff007f" opacity="0.7">
    <text x="55" y="340">01011</text>
    <text x="55" y="350">10010</text>
    <text x="320" y="80">11010</text>
    <text x="320" y="90">01100</text>
    <text x="120" y="380">0010</text>
    <text x="120" y="390">1101</text>
  </g>
  <g font-family="monospace" font-size="10" fill="#f0e68c" opacity="0.8" filter="url(#glow)">
    <text x="180" y="30">AI</text>
    <text x="220" y="370">DATA</text>
    <text x="10" y="180">0</text>
    <text x="380" y="180">1</text>
  </g>

  <!-- Geometric Overlay -->
  <g fill="none" stroke="#00e5ff" stroke-width="1" opacity="0.5">
    <rect x="120" y="120" width="160" height="160" transform="rotate(45 200 200)" />
    <polygon points="200,140 260,200 200,260 140,200" />
  </g>
</svg>
```