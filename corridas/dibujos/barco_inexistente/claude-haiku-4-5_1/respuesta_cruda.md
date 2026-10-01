```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="waterGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1E90FF;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="hullGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#FF6B35;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#D32F2F;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Water -->
  <rect width="400" height="400" fill="url(#waterGradient)"/>
  <circle cx="80" cy="100" r="25" fill="#87CEEB" opacity="0.6"/>
  <circle cx="320" cy="150" r="30" fill="#87CEEB" opacity="0.5"/>
  <circle cx="150" cy="280" r="20" fill="#87CEEB" opacity="0.7"/>
  
  <!-- Waves -->
  <path d="M 0 320 Q 50 310 100 320 T 200 320 T 300 320 T 400 320" stroke="#B0E0E6" stroke-width="2" fill="none" opacity="0.8"/>
  <path d="M 0 350 Q 50 340 100 350 T 200 350 T 300 350 T 400 350" stroke="#B0E0E6" stroke-width="2" fill="none" opacity="0.6"/>
  
  <!-- Hull (main body) -->
  <ellipse cx="200" cy="240" rx="85" ry="35" fill="url(#hullGradient)" filter="url(#shadow)"/>
  <path d="M 120 240 L 100 280 L 300 280 L 280 240" fill="#C41E3A" opacity="0.8"/>
  
  <!-- Propeller-like fins at stern -->
  <g transform="translate(95, 260)">
    <circle cx="0" cy="0" r="8" fill="#FFD700"/>
    <path d="M 0 -12 L 8 -2 L 0 2 L -8 -2 Z" fill="#FFA500"/>
    <path d="M -2 -8 L 8 0 L 2 8 L -8 0 Z" fill="#FF8C00"/>
  </g>
  
  <!-- Conning tower/cabin -->
  <rect x="170" y="180" width="60" height="50" rx="8" fill="#2C3E50" filter="url(#shadow)"/>
  <circle cx="200" cy="195" r="8" fill="#4FA3FF"/>
  <rect x="180" y="210" width="40" height="15" fill="#87CEEB" opacity="0.7"/>
  
  <!-- Rotating radar dome on top -->
  <circle cx="200" cy="170" r="18" fill="#95A5A6" filter="url(#shadow)"/>
  <circle cx="200" cy="170" r="15" fill="#BDC3C7" opacity="0.6"/>
  <circle cx="200" cy="170" r="10" fill="#7F8C8D"/>
  <line x1="200" y1="160" x2="200" y2="145" stroke="#34495E" stroke-width="2"/>
  
  <!-- Three sails/wings extending from hull -->
  <g transform="translate(200, 180)">
    <!-- Left sail -->
    <polygon points="0 0 -45 -70 -35 10" fill="#FFB6C1" opacity="0.7" filter="url(#shadow)"/>
    <line x1="0" y1="0" x2="-45" y2="-70" stroke="#FF69B4" stroke-width="2"/>
    
    <!-- Center sail -->
    <polygon points="0 0 0 -90 30 10" fill="#DDA0DD" opacity="0.7" filter="url(#shadow)"/>
    <line x1="0" y1="0" x2="0" y2="-90" stroke="#BA55D3" stroke-width="2"/>
    
    <!-- Right sail -->
    <polygon points="0 0 45 -70 35 10" fill="#FFB6C1" opacity="0.7" filter="url(#shadow)"/>
    <line x1="0" y1="0" x2="45" y2="-70" stroke="#FF69B4" stroke-width="2"/>
  </g>
  
  <!-- Glowing energy spheres around ship -->
  <circle cx="120" cy="200" r="6" fill="#00FF00" opacity="0.6" filter="url(#shadow)"/>
  <circle cx="280" cy="220" r="6" fill="#00FF00" opacity="0.6" filter="url(#shadow)"/>
  <circle cx="200" cy="140" r="8" fill="#00FFFF" opacity="0.5" filter="url(#shadow)"/>
  
  <!-- Energy lines connecting spheres -->
  <line x1="200" y1="140" x2="200" y2="170" stroke="#00FFFF" stroke-width="1" opacity="0.4"/>
  <line x1="120" y1="200" x2="200" y2="240" stroke="#00FF00" stroke-width="1" opacity="0.4"/>
  <line x1="280" y1="220" x2="200" y2="240" stroke="#00FF00" stroke-width="1" opacity="0.4"/>
  
  <!-- Floating bubbles behind ship -->
  <circle cx="280" cy="260" r="4" fill="#87CEEB" opacity="0.5"/>
  <circle cx="290" cy="270" r="3" fill="#87CEEB" opacity="0.4"/>
  <circle cx="285" cy="280" r="2.5" fill="#87CEEB" opacity="0.3"/>
  
  <!-- Flag at bow -->
  <polygon points="110 185 100 165 130 170" fill="#FF4500" filter="url(#shadow)"/>
</svg>
```