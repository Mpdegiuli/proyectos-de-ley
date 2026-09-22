<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="45%" cy="45%" r="70%">
      <stop offset="0%" stop-color="#0a122a"/>
      <stop offset="50%" stop-color="#050711"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
    
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f3ff"/>
      <stop offset="50%" stop-color="#7b00ff"/>
      <stop offset="100%" stop-color="#ff00ea"/>
    </linearGradient>

    <linearGradient id="wireGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff00ea"/>
      <stop offset="100%" stop-color="#00f3ff"/>
    </linearGradient>

    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1"/>
      <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="heavyGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur1"/>
      <feGaussianBlur in="SourceGraphic" stdDeviation="12" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <line x1="15" y1="13" x2="15" y2="17" stroke="#00f3ff" stroke-width="1" opacity="0.3"/>
      <line x1="13" y1="15" x2="17" y2="15" stroke="#00f3ff" stroke-width="1" opacity="0.3"/>
      <circle cx="0" cy="0" r="0.5" fill="#ff00ea" opacity="0.3"/>
    </pattern>

    <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="4" y2="0" stroke="#000000" stroke-width="2" opacity="0.4"/>
    </pattern>

    <path id="txtPath" d="M 40,200 A 160,160 0 1,1 360,200 A 160,160 0 1,1 40,200" />

    <g id="sector">
      <!-- Facets -->
      <polygon points="200,200 200,120 269.28,160" fill="url(#coreGrad)" opacity="0.15"/>
      <polygon points="200,120 269.28,160 234.64,140" fill="#ffffff" opacity="0.1"/>
      
      <!-- Structural Core Hexagon Lines -->
      <line x1="200" y1="200" x2="200" y2="120" stroke="#00f3ff" stroke-width="1" opacity="0.6"/>
      <line x1="200" y1="120" x2="269.28" y2="160" stroke="#ff00ea" stroke-width="1.5" filter="url(#glow)"/>
      
      <!-- Outer Neural Branches -->
      <path d="M 200 120 L 200 70 L 220 50 L 220 25" fill="none" stroke="url(#wireGrad)" stroke-width="1.5" filter="url(#glow)"/>
      <circle cx="220" cy="25" r="2.5" fill="#ffffff" filter="url(#glow)"/>
      <circle cx="220" cy="25" r="5" fill="none" stroke="#00f3ff" stroke-width="1"/>
      
      <!-- Side Circuit offshoot -->
      <path d="M 200 95 L 230 65 L 260 65" fill="none" stroke="#00f3ff" stroke-width="1" stroke-dasharray="3 2"/>
      <rect x="260" y="63" width="5" height="4" fill="#ff00ea" filter="url(#glow)"/>
      
      <!-- Inner details -->
      <line x1="200" y1="160" x2="234.64" y2="180" stroke="#ffffff" stroke-width="1" opacity="0.7"/>
      <circle cx="200" cy="160" r="1.5" fill="#fff"/>
    </g>
  </defs>

  <!-- Backgrounds -->
  <rect width="100%" height="100%" fill="url(#bg)"/>
  <rect width="100%" height="100%" fill="url(#grid)"/>

  <!-- Orbital Rings -->
  <circle cx="200" cy="200" r="175" fill="none" stroke="#00f3ff" stroke-width="0.5" opacity="0.2"/>
  <circle cx="200" cy="200" r="140" fill="none" stroke="#ff00ea" stroke-width="1" opacity="0.3" stroke-dasharray="4 8"/>
  <circle cx="200" cy="200" r="125" fill="none" stroke="#00f3ff" stroke-width="1" opacity="0.5" stroke-dasharray="60 10 20 10 5 10"/>
  <circle cx="200" cy="200" r="95" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.1"/>

  <!-- Asymmetrical Arcs / Glitches -->
  <path d="M 40 200 A 160 160 0 0 1 120 61" fill="none" stroke="#ff00ea" stroke-width="3" filter="url(#glow)" opacity="0.8"/>
  <path d="M 338 120 A 160 160 0 0 1 300 324" fill="none" stroke="#00f3ff" stroke-width="2" filter="url(#glow)" opacity="0.9"/>
  
  <circle cx="120" cy="61" r="3" fill="#ffffff" filter="url(#glow)"/>
  <circle cx="338" cy="120" r="2" fill="#ffffff"/>

  <!-- Binary Data Ring -->
  <text font-family="'Courier New', monospace" font-size="10.5" fill="#00f3ff" opacity="0.5" letter-spacing="3.5">
    <textPath href="#txtPath" textLength="980" startOffset="0%">01010011 01011001 01010011 01010100 01000101 01001101 01001111 01001110 01001100 01001001 01001110 01000101 00100000 01000001 01010111 01000001 01001011 01000101 00100000 01111000</textPath>
  </text>

  <!-- 6-Way Symmetrical Core -->
  <g filter="url(#glow)">
    <use href="#sector" />
    <use href="#sector" transform="rotate(60 200 200)" />
    <use href="#sector" transform="rotate(120 200 200)" />
    <use href="#sector" transform="rotate(180 200 200)" />
    <use href="#sector" transform="rotate(240 200 200)" />
    <use href="#sector" transform="rotate(300 200 200)" />
  </g>

  <!-- Center Singularity / Pupil -->
  <g filter="url(#heavyGlow)">
    <circle cx="200" cy="200" r="16" fill="url(#coreGrad)" opacity="0.6"/>
    <circle cx="200" cy="200" r="7" fill="#ffffff"/>
    <!-- Cross Star -->
    <polygon points="200,180 203,197 220,200 203,203 200,220 197,203 180,200 197,197" fill="#00f3ff"/>
  </g>
  <circle cx="200" cy="200" r="3" fill="#ff00ea"/>

  <!-- Floating Data Motes -->
  <g fill="#ffffff" opacity="0.9" filter="url(#glow)">
    <circle cx="100" cy="110" r="1.5"/>
    <circle cx="280" cy="80" r="2"/>
    <circle cx="90" cy="270" r="1"/>
    <circle cx="310" cy="300" r="2.5"/>
    <circle cx="150" cy="340" r="1.5"/>
    <circle cx="50" cy="190" r="1"/>
  </g>

  <!-- HUD Elements -->
  <g font-family="'Courier New', monospace