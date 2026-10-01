<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="nebula1" cx="30%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#4a2080" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#0a0a1a" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="nebula2" cx="70%" cy="60%" r="50%">
      <stop offset="0%" stop-color="#204080" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#0a0a1a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bridgeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff6ec7"/>
      <stop offset="25%" stop-color="#ffcc00"/>
      <stop offset="50%" stop-color="#00ffff"/>
      <stop offset="75%" stop-color="#7b68ee"/>
      <stop offset="100%" stop-color="#ff6ec7"/>
    </linearGradient>
    <linearGradient id="towerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f0f0f0"/>
      <stop offset="50%" stop-color="#a0a0a0"/>
      <stop offset="100%" stop-color="#c0c0c0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="glowStrong">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Fondo -->
  <rect width="400" height="400" fill="#0a0a1a"/>
  <rect width="400" height="400" fill="url(#nebula1)"/>
  <rect width="400" height="400" fill="url(#nebula2)"/>
  
  <!-- Estrellas -->
  <g fill="white">
    <circle cx="40" cy="30" r="1.2" opacity="0.9"/>
    <circle cx="90" cy="70" r="0.8" opacity="0.6"/>
    <circle cx="150" cy="20" r="1.5" opacity="0.8"/>
    <circle cx="220" cy="50" r="0.9" opacity="0.5"/>
    <circle cx="300" cy="25" r="1.1" opacity="0.7"/>
    <circle cx="350" cy="60" r="1.8" opacity="0.9"/>
    <circle cx="30" cy="120" r="1.0" opacity="0.5"/>
    <circle cx="110" cy="140" r="0.7" opacity="0.4"/>
    <circle cx="170" cy="100" r="1.3" opacity="0.8"/>
    <circle cx="260" cy="90" r="0.8" opacity="0.6"/>
    <circle cx="330" cy="130" r="1.2" opacity="0.7"/>
    <circle cx="380" cy="110" r="0.9" opacity="0.5"/>
    <circle cx="50" cy="180" r="1.1" opacity="0.6"/>
    <circle cx="140" cy="200" r="0.8" opacity="0.4"/>
    <circle cx="230" cy="150" r="1.4" opacity="0.7"/>
    <circle cx="310" cy="180" r="0.9" opacity="0.5"/>
    <circle cx="370" cy="200" r="1.2" opacity="0.6"/>
    <circle cx="70" cy="250" r="0.7" opacity="0.3"/>
    <circle cx="190" cy="230" r="1.0" opacity="0.5"/>
    <circle cx="280" cy="260" r="0.8" opacity="0.4"/>
    <circle cx="340" cy="240" r="1.1" opacity="0.6"/>
  </g>
  
  <!-- Estrella fugaz -->
  <line x1="50" y1="40" x2="80" y2="60" stroke="white" stroke-width="1" opacity="0.6"/>
  <line x1="80" y1="60" x2="85" y2="63" stroke="white" stroke-width="0.5" opacity="0.3"/>
  
  <!-- Auroras -->
  <path d="M 0 150 C 100 80, 200 120, 400 60" fill="none" stroke="#00ffff" stroke-width="8" opacity="0.15" filter="url(#glowStrong)"/>
  <path d="M 0 180 C 120 100, 250 150, 400 90" fill="none" stroke="#ff6ec7" stroke-width="6" opacity="0.12" filter="url(#glowStrong)"/>
  <path d="M 50 200 C 150 130, 280 170, 400 130" fill="none" stroke="#7b68ee" stroke-width="10" opacity="0.1" filter="url(#glowStrong)"/>
  
  <!-- Conexiones flotantes torre-isla -->
  <line x1="60" y1="205" x2="60" y2="255" stroke="url(#bridgeGrad)" stroke-width="3" opacity="0.7" filter="url(#glow)"/>
  <line x1="340" y1="185" x2="340" y2="235" stroke="url(#bridgeGrad)" stroke-width="3" opacity="0.7" filter="url(#glow)"/>
  
  <!-- Isla flotante izquierda -->
  <g transform="translate(60,260)">
    <path d="M -30 0 L -35 30 L -20 50 L 0 60 L 20 55 L 35 40 L 30 0 Z" fill="#3a3a4a"/>
    <path d="M -20 50 L -10 70 L 5 65 L 0 55 Z" fill="#2a2a3a"/>
    <path d="M 20 55 L 30 75 L 15 70 L 20 55 Z" fill="#2a2a3a"/>
    <ellipse cx="0" cy="0" rx="35" ry="12" fill="#4a8a3a"/>
    <ellipse cx="0" cy="-3" rx="30" ry="10" fill="#5a9a4a"/>
    <path d="M -10 10 L -5 80 L 5 80 L 10 10 Z" fill="#00ffff" opacity="0.4" filter="url(#glow)"/>
  </g>
  
  <!-- Isla flotante derecha -->
  <g transform="translate(340,240)">
    <path d="M -30 0 L -35 25 L -20 45 L 0 55 L 20 50 L 35 35 L 30 0 Z" fill="#3a3a4a"/>
    <path d="M -20 45 L -10 60 L 5 55 L 0 45 Z" fill="#2a2a3a"/>
    <path d="M 20 50 L 30 65 L 15 60 L 20 50 Z" fill="#2a2a3a"/>
    <ellipse cx="0" cy="0" rx="35" ry="12" fill="#4a8a3a"/>
    <ellipse cx="0" cy="-3" rx="30" ry="10" fill="#5a9a4a"/>
    <path d="M -10 8 L -5 70 L 5 70 L 10 8 Z" fill="#ff6ec7" opacity="0.4" filter="url(#glow)"/>
  </g>
  
  <!-- Torre izquierda -->
  <g transform="translate(60,200)">
    <rect x="-10" y="-10" width="20" height="15" fill="#666"/>
    <rect x="-6" y="-100" width="12" height="90" fill="url(#towerGrad)"/>
    <polygon points="-6,-100 6,-100 0,-120" fill="#cccccc"/>
    <rect x="-3" y="-90" width="6" height="8" fill="#00ffff" opacity="0.8"/>
    <rect x="-3" y="-70" width="6" height="8" fill="#00ffff" opacity="0.8"/>
    <rect x="-3" y="-50" width="6" height="8" fill="#00ffff" opacity="0.8"/>
    <rect x="-3" y="-30" width="6" height="8" fill="#00ffff" opacity="0.8"/>
  </g>
  
  <!-- Torre derecha -->
  <g transform="translate(340,180)">
    <rect x="-10" y="-10" width="20" height="15" fill="#666"/>
    <rect x="-6" y="-100" width="12" height="90" fill="url(#towerGrad)"/>
    <polygon points="-6,-100 6,-100 0,-120" fill="#cccccc"/>
    <rect x="-3" y="-90" width="6" height="8" fill="#ff6ec7" opacity="0.8"/>
    <rect x="-3" y="-70" width="6" height="8" fill="#ff6ec7" opacity="0.8"/>
    <rect x="-3" y="-50" width="6" height="8" fill="#ff6ec7" opacity="0.8"/>
    <rect x="-3" y="-30" width="6" height="8" fill="#ff6ec7" opacity="0.8"/>
  </g>
  
  <!-- Tablero del puente -->
  <path d="M 60 210 C 120 210, 160 180, 200 180 C 240 180, 280 210, 340 190" 
        fill="none" stroke="url(#bridgeGrad)" stroke-width="10" stroke-linecap="round" opacity="0.95"/>
  <path d="M 60 216 C 120 216, 160 186, 200 186 C 240 186, 280 216, 340 196" 
        fill="none" stroke="#5a5a7a" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
  
  <!-- Barandillas -->
  <path d="M 60 202 C 120 202, 160 172, 200 172 C 240 172, 280 202, 340 182" 
        fill="none" stroke="#ffcc00" stroke-width="1.5" stroke-linecap="round" opacity="0.7"/>
  <g stroke="#ffcc00" stroke-width="1" opacity="0.5">
    <line x1="80" y1="203" x2="80" y2="209"/>
    <line x1="100" y1="202" x2="100" y2="208"/>
    <line x1="120" y1="199" x2="120" y2="205"/>
    <line x1="140" y1="193" x2="140" y2="199"/>
    <line x1="160" y1="184" x2="160" y2="190"/>
    <line x1="180" y1="178" x2="180" y2="184"/>
    <line x1="200" y1="175" x2="200" y2="181"/>
    <line x1="220" y1="178" x2="220" y2="184"/>
    <line x1="240" y1="184" x2="240" y2="190"/>
    <line x1="260" y1="193" x2="260" y2="199"/>
    <line x1="280" y1="202" x2="280" y2="208"/>
    <line x1="300" y1="199" x2="300" y2="205"/>
    <line x1="320" y1="193" x2="320" y2="199"/>
    <line x1="340" y1="185" x2="340" y2="191"/>
  </g>
  
  <!-- Cables colgantes -->
  <g stroke="#aaaaaa" stroke-width="1" opacity="0.6">
    <line x1="60" y1="100" x2="80" y2="208"/>
    <line x1="60" y1="100" x2="100" y2="204"/>
    <line x1="60" y1="100" x2="120" y2="198"/>
    <line x1="60" y1="100" x2="140" y2="190"/>
    <line x1="60" y1="100" x2="160" y2="182"/>
    <line x1="60" y1="100" x2="180" y2="176"/>
    <line x1="60" y1="100" x2="200" y2="173"/>
    <line x1="340" y1="80" x2="200" y2="173"/>
    <line x1="340" y1="80" x2="220" y2="176"/>
    <line x1="340" y1="80" x2="240" y2="182"/>
    <line x1="340" y1="80" x2="260" y2="190"/>
    <line x1="340" y1="80" x2="280" y2="198"/>
    <line x1="340" y1="80" x2="300" y2="204"/>
    <line x1="340" y1="80" x2="320" y2="196"/>
    <line x1="340" y1="80" x2="340" y2="185"/>
  </g>
  
  <!-- Luces en el tablero -->
  <g filter="url(#glow)">
    <circle cx="80" cy="210" r="2" fill="#00ffff"/>
    <circle cx="100" cy="207" r="2" fill="#ff6ec7"/>
    <circle cx="120" cy="201" r="2" fill="#00ffff"/>
    <circle cx="140" cy="193" r="2" fill="#ffcc00"/>
    <circle cx="160" cy="185" r="2" fill="#00ffff"/>
    <circle cx="180" cy="178" r="2" fill="#ff6ec7"/>
    <circle cx="200" cy="175" r="2" fill="#00ffff"/>
    <circle cx="220" cy="178" r="2" fill="#ffcc00"/>
    <circle cx="240" cy="185" r="2" fill="#00ffff"/>
    <circle cx="260" cy="193" r="2" fill="#ff6ec7"/>
    <circle cx="280" cy="201" r="2" fill="#00ffff"/>
    <circle cx="300" cy="204" r="2" fill="#ffcc00"/>
    <circle cx="320" cy="196" r="2" fill="#00ffff"/>
    <circle cx="340" cy="185" r="2" fill="#ff6ec7"/>
  </g>
  
  <!-- Partículas flotantes -->
  <g fill="white" opacity="0.7">
    <circle cx="180" cy="140" r="1.2"/>
    <circle cx="220" cy="130" r="0.8"/>
    <circle cx="250" cy="160" r="1.0"/>
    <circle cx="130" cy="170" r="0.9"/>
    <circle cx="300" cy="150" r="1.1"/>
    <circle cx="270" cy="120" r="0.7"/>
    <circle cx="350" cy="140" r="1.3"/>
    <circle cx="90" cy="130" r="0.8"/>
  </g>
</svg>