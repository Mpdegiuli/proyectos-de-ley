```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0b051a"/>
      <stop offset="100%" stop-color="#020105"/>
    </radialGradient>
    
    <filter id="g1" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="1.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="g2" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="huge" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="25"/>
    </filter>

    <!-- 12-fold Lotus Symmetry -->
    <g id="s1">
      <path d="M 200 200 C 215 150, 240 70, 200 15 C 160 70, 185 150, 200 200" fill="none" stroke="#FFD700" stroke-width="1.2"/>
      <path d="M 200 200 C 208 140, 220 80, 200 35 C 180 80, 192 140, 200 200" fill="rgba(255, 0, 127, 0.15)" stroke="#FF007F" stroke-width="1"/>
      <path d="M 200 200 Q 210 160 200 120 Q 190 160 200 200" fill="rgba(0, 243, 255, 0.2)" stroke="#00F3FF" stroke-width="1"/>
      <circle cx="200" cy="15" r="2.5" fill="#00F3FF"/>
      <polygon points="200,65 204,75 200,85 196,75" fill="#00F3FF"/>
      <line x1="200" y1="35" x2="200" y2="65" stroke="#00F3FF" stroke-width="1"/>
      <line x1="200" y1="85" x2="200" y2="120" stroke="#FFD700" stroke-width="0.5" stroke-dasharray="3 3"/>
    </g>
    <g id="s2"><use href="#s1"/><use href="#s1" transform="rotate(180 200 200)"/></g>
    <g id="s4"><use href="#s2"/><use href="#s2" transform="rotate(90 200 200)"/></g>
    <g id="s12"><use href="#s4"/><use href="#s4" transform="rotate(30 200 200)"/><use href="#s4" transform="rotate(60 200 200)"/></g>

    <!-- 24-fold Spiral Lattice Symmetry -->
    <g id="t1">
      <path d="M 200 120 C 260 100, 250 40, 200 15" fill="none" stroke="#9D00FF" stroke-width="1" opacity="0.8"/>
      <path d="M 200 120 C 140 100, 150 40, 200 15" fill="none" stroke="#00F3FF" stroke-width="0.8" opacity="0.6"/>
      <path d="M 200 15 Q 224 5 247.8 21.3" fill="none" stroke="#FFD700" stroke-width="1"/>
      <circle cx="200" cy="180" r="1.5" fill="#FFD700"/>
    </g>
    <g id="t2"><use href="#t1"/><use href="#t1" transform="rotate(180 200 200)"/></g>
    <g id="t4"><use href="#t2"/><use href="#t2" transform="rotate(90 200 200)"/></g>
    <g id="t12"><use href="#t4"/><use href="#t4" transform="rotate(30 200 200)"/><use href="#t4" transform="rotate(60 200 200)"/></g>
    <g id="t24"><use href="#t12"/><use href="#t12" transform="rotate(15 200 200)"/></g>
    
    <!-- 6-fold Inner Geometry -->
    <g id="u1">
      <polygon points="200,65 215,85 200,105 185,85" fill="none" stroke="#00F3FF" stroke-width="1.2"/>
      <circle cx="200" cy="65" r="3" fill="#FF007F"/>
      <line x1="200" y1="65" x2="200" y2="15" stroke="rgba(255,255,255,0.25)" stroke-width="0.5"/>
    </g>
    <g id="u2"><use href="#u1"/><use href="#u1" transform="rotate(180 200 200)"/></g>
    <g id="u6"><use href="#u2"/><use href="#u2" transform="rotate(60 200 200)"/><use href="#u2" transform="rotate(120 200 200)"/></g>
  </defs>

  <!-- Deep Space Background -->
  <rect width="400" height="400" fill="url(#bg)"/>
  
  <!-- Glowing Nebulas -->
  <circle cx="80" cy="80" r="60" fill="#9D00FF" opacity="0.3" filter="url(#huge)"/>
  <circle cx="320" cy="320" r="80" fill="#00F3FF" opacity="0.2" filter="url(#huge)"/>
  <circle cx="300" cy="100" r="70" fill="#FF007F" opacity="0.25" filter="url(#huge)"/>

  <!-- Distant Starfield & Constellations -->
  <path d="M20,40 h1 M70,90 h1 M120,30 h1 M350,60 h1 M380,120 h1 M310,40 h1 M40,250 h1 M80,350 h1 M150,380 h1 M340,360 h1 M380,280 h1 M250,370 h1" stroke="#FFF" stroke-linecap="round" stroke-width="1.5" opacity="0.8"/>
  <path d="M40,50 h1 M90,120 h1 M150,50 h1 M320,80 h1 M360,150 h1 M280,20 h1 M20,200 h1 M60,300 h1 M120,350 h1 M300,380 h1 M350,320 h1 M200,380 h1" stroke="#FFD700" stroke-linecap="round" stroke-width="1" opacity="0.5"/>
  
  <polyline points="40,50 90,120 150,50" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="0.5"/>
  <polyline points="320,80 360,150 280,20" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="0.5"/>
  <polyline points="20,200 60,300 120,350" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="0.5"/>

  <!-- Outer Glyph Ring (Animated) -->
  <circle cx="200" cy="200" r="192" fill="none" stroke="#00F3FF" stroke-width="1.5" stroke-dasharray="1 4 1 8 2 12 1 4" opacity="0.6">
    <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="200s" repeatCount="indefinite"/>
  </circle>

  <!-- Core Mandala Layers (Animated) -->
  <g filter="url(#g1)">
    <!-- Counter-Clockwise Spiral Torus -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360 200 200" to="0 200 200" dur="180s" repeatCount="indefinite"/>
      <use href="#t24"/>
    </g>
    
    <!-- Clockwise Lotus Layers -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="120s" repeatCount="indefinite"/>
      <use href="#s12"/>
    </g>

    <!-- Fast Clockwise Inner Structure -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="90s" repeatCount="indefinite"/>
      <use href="#u6"/>
    </g>
  </g>

  <!-- Hexagram Grids (Static Anchors) -->
  <g filter="url(#g1)">
    <!-- R=120 Cyan Hexagram -->
    <polygon points="200,80 303.92,260 96.08,260" fill="none" stroke="rgba(0,243,255,0.4)" stroke-width="1"/>
    <polygon points="200,320 303.92,140 96.08,140" fill="none" stroke="rgba(0,243,255,0.4)" stroke-width="1"/>
    <!-- R=65 Gold Hexagram -->
    <polygon points="200,135 256.29,232.5 143.71,232.5" fill="none" stroke="rgba(255,215,0,0.6)" stroke-width="1.2"/>
    <polygon points="200,265 256.29,167.5 143.71,167.5" fill="none" stroke="rgba(255,215,0,0.6)" stroke-width="1.2"/>
  </g>

  <!-- Concentric Astrolabe Rings -->
  <circle cx="200" cy="200" r="185" fill="none" stroke="#FFD700" stroke-width="1" opacity="0.7"/>
  <circle cx="200" cy="200" r="181" fill="none" stroke="#00F3FF" stroke-width="0.5" stroke-dasharray="3 6"/>
  
  <circle cx="200" cy="200" r="120" fill="none" stroke="#FF007F" stroke-width="1.5" stroke-dasharray="8 4" opacity="0.9">
    <animateTransform attributeName="transform" type="rotate" from="360 200 200" to="0 200 200" dur="60s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="200" r="116" fill="none" stroke="#9D00FF" stroke-width="4" opacity="0.4"/>
  
  <circle cx="200" cy="200" r="65" fill="none" stroke="#FFD700" stroke-width="1.2"/>
  <circle cx="200" cy="200" r="62" fill="none" stroke="#00F3FF" stroke-width="1" stroke-dasharray="2 4">
    <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="30s" repeatCount="indefinite"/>
  </circle>

  <!-- Orbital Mechanism 1 (Outer Planet) -->
  <g>
    <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="45s" repeatCount="indefinite"/>
    <path d="M 200 200 L 330.8 69.2" stroke="rgba(255,215,0,0.4)" stroke-width="1"/>
    <g transform="translate(330.8, 69.2)">
       <circle cx="0" cy="0" r="8" fill="#FF007F" filter="url(#g2)"/>
       <circle cx="0" cy="0" r="14" fill="none" stroke="#00F3FF" stroke-width="1.5" stroke-dasharray="2 3"/>
       <circle cx="0" cy="0" r="18" fill="none" stroke="#FFD700" stroke-width="0.5"/>
       <line x1="-22" y1="0" x2="-14" y2="0" stroke="#00F3FF" stroke-width="1"/>
       <line x1="14" y1="0" x2="22" y2="0" stroke="#00F3FF" stroke-width="1"/>
       <line x1="0" y1="-22" x2="0" y2="-14" stroke="#00F3FF" stroke-width="1"/>
       <line x1="0" y1="14" x2="0" y2="22" stroke="#00F3FF" stroke-width="1"/>
    </g>
  </g>

  <!-- Orbital Mechanism 2 (Mid Planet) -->
  <g>
    <animateTransform attributeName="transform" type="rotate" from="360 200 200" to="0 200 200" dur="60s" repeatCount="indefinite"/>
    <path d="M 200 200 L 115.1 284.9" stroke="rgba(0,243,255,0.4)" stroke-width="1"/>
    <g transform="translate(115.1, 284.9)">
       <circle cx="0" cy="0" r="5" fill="#FFD700" filter="url(#g2)"/>
       <circle cx="0" cy="0" r="10" fill="none" stroke="#FF007F" stroke-width="1.5"/>
       <circle cx="0" cy="0" r="15" fill="none" stroke="#9D00FF" stroke-width="1.5" stroke-dasharray="1 4"/>
    </g>
  </g>

  <!-- Orbital Mechanism 3 (Inner Moon) -->
  <g>
    <animateTransform attributeName="transform" type="rotate" from="360 200 200" to="0 200 200" dur="25s" repeatCount="indefinite"/>
    <path d="M 200 200 L 256.29 167.5" stroke="rgba(255,0,127,0.5)" stroke-width="1"/>
    <g transform="translate(256.29, 167.5)">
        <circle cx="0" cy="0" r="3" fill="#00F3FF" filter="url(#g2)"/>
        <circle cx="0" cy="0" r="7" fill="none" stroke="#FFD700" stroke-width="1"/>
    </g>
  </g>

  <!-- Central Jewel (Static Anchoring Core) -->
  <circle cx="200" cy="200" r="22" fill="#080315" stroke="#FF007F" stroke-width="1.5" filter="url(#g1)"/>
  <polygon points="200,185 213,207.5 187,207.5" fill="#00F3FF" opacity="0.9"/>
  <polygon points="200,215 213,192.5 187,192.5" fill="#00F3FF" opacity="0.6"/>
  <circle cx="200" cy="200" r="4" fill="#FFD700" filter="url(#g2)"/>
  <circle cx="200" cy="200" r="1.5" fill="#FFF"/>
</svg>
```