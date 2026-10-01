```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .trunk { fill: #8B4513; }
      .branch { fill: none; stroke: #654321; stroke-width: 2; }
      .leaf { fill: #FF1493; opacity: 0.8; }
      .flower { fill: #FFD700; }
      .fruit { fill: #00CED1; }
    </style>
    <radialGradient id="sky" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#E0FFFF;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <rect width="400" height="400" fill="url(#sky)"/>
  <rect y="300" width="400" height="100" fill="#90EE90"/>
  
  <!-- Tronco principal ondulante -->
  <path d="M 200 350 Q 190 320 195 290 Q 200 260 190 230 Q 185 200 200 170" class="branch" stroke-width="8" stroke="#8B4513" fill="none"/>
  
  <!-- Raíces cristalinas -->
  <g class="leaf" opacity="0.6">
    <polygon points="200,350 180,370 185,360"/>
    <polygon points="200,350 220,370 215,360"/>
    <polygon points="200,350 200,375 195,365"/>
  </g>
  
  <!-- Ramas principales arqueadas -->
  <path d="M 200 170 Q 140 140 100 120" class="branch" stroke-width="6"/>
  <path d="M 200 170 Q 260 140 300 120" class="branch" stroke-width="6"/>
  <path d="M 200 170 Q 150 200 120 240" class="branch" stroke-width="5"/>
  <path d="M 200 170 Q 250 200 280 240" class="branch" stroke-width="5"/>
  
  <!-- Sub-ramas -->
  <path d="M 100 120 Q 70 100 50 90" class="branch" stroke-width="4"/>
  <path d="M 100 120 Q 90 150 85 180" class="branch" stroke-width="4"/>
  <path d="M 300 120 Q 330 100 350 90" class="branch" stroke-width="4"/>
  <path d="M 300 120 Q 310 150 315 180" class="branch" stroke-width="4"/>
  <path d="M 120 240 Q 90 260 70 280" class="branch" stroke-width="4"/>
  <path d="M 280 240 Q 310 260 330 280" class="branch" stroke-width="4"/>
  
  <!-- Hojas rosadas flotantes en las ramas -->
  <ellipse cx="50" cy="85" rx="8" ry="12" fill="#FF1493" transform="rotate(-30 50 85)"/>
  <ellipse cx="350" cy="85" rx="8" ry="12" fill="#FF1493" transform="rotate(30 350 85)"/>
  <ellipse cx="85" cy="175" rx="8" ry="12" fill="#FF1493" transform="rotate(-45 85 175)"/>
  <ellipse cx="315" cy="175" rx="8" ry="12" fill="#FF1493" transform="rotate(45 315 175)"/>
  <ellipse cx="70" cy="275" rx="8" ry="12" fill="#FF1493" transform="rotate(-60 70 275)"/>
  <ellipse cx="330" cy="275" rx="8" ry="12" fill="#FF1493" transform="rotate(60 330 275)"/>
  
  <!-- Flores doradas en puntas -->
  <circle cx="50" cy="90" r="6" class="flower"/>
  <circle cx="350" cy="90" r="6" class="flower"/>
  <circle cx="85" cy="180" r="5" class="flower"/>
  <circle cx="315" cy="180" r="5" class="flower"/>
  <circle cx="70" cy="280" r="5" class="flower"/>
  <circle cx="330" cy="280" r="5" class="flower"/>
  
  <!-- Frutos turquesas en el centro -->
  <circle cx="200" cy="220" r="7" class="fruit"/>
  <circle cx="210" cy="200" r="7" class="fruit"/>
  <circle cx="190" cy="200" r="7" class="fruit"/>
  <circle cx="205" cy="180" r="6" class="fruit"/>
  <circle cx="195" cy="180" r="6" class="fruit"/>
  
  <!-- Hojas en espiral alrededor del tronco central -->
  <g class="leaf">
    <ellipse cx="220" cy="250" rx="10" ry="16" fill="#FF1493" transform="rotate(20 220 250)"/>
    <ellipse cx="180" cy="250" rx="10" ry="16" fill="#FF1493" transform="rotate(-20 180 250)"/>
    <ellipse cx="225" cy="210" rx="10" ry="16" fill="#FF1493" transform="rotate(45 225 210)"/>
    <ellipse cx="175" cy="210" rx="10" ry="16" fill="#FF1493" transform="rotate(-45 175 210)"/>
    <ellipse cx="230" cy="170" rx="9" ry="15" fill="#FF1493" transform="rotate(70 230 170)"/>
    <ellipse cx="170" cy="170" rx="9" ry="15" fill="#FF1493" transform="rotate(-70 170 170)"/>
  </g>
  
  <!-- Venas de luz en el árbol -->
  <line x1="200" y1="170" x2="200" y2="150" stroke="#FFD700" stroke-width="1" opacity="0.5"/>
  <line x1="190" y1="230" x2="170" y2="240" stroke="#FFD700" stroke-width="1" opacity="0.5"/>
  <line x1="210" y1="230" x2="230" y2="240" stroke="#FFD700" stroke-width="1" opacity="0.5"/>
</svg>
```