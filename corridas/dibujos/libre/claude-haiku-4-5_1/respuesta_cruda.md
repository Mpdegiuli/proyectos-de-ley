```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Fondo degradado -->
  <defs>
    <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#E0F6FF;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="sunGradient">
      <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FFA500;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <!-- Cielo -->
  <rect width="400" height="400" fill="url(#skyGradient)"/>
  
  <!-- Sol -->
  <circle cx="320" cy="80" r="40" fill="url(#sunGradient)"/>
  
  <!-- Montañas -->
  <polygon points="0,250 100,120 200,200 300,100 400,250 400,400 0,400" fill="#8B7355"/>
  <polygon points="0,280 80,160 160,240 250,130 350,280 400,280 400,400 0,400" fill="#A0826D"/>
  
  <!-- Nieve en montañas -->
  <polygon points="100,120 60,180 140,180" fill="#FFFFFF"/>
  <polygon points="300,100 250,170 350,170" fill="#FFFFFF"/>
  <polygon points="200,200 160,240 240,240" fill="#FFFFFF"/>
  
  <!-- Árboles -->
  <g id="tree1">
    <rect x="45" y="240" width="8" height="30" fill="#654321"/>
    <polygon points="49,210 25,245 73,245" fill="#228B22"/>
    <polygon points="49,225 30,250 68,250" fill="#32CD32"/>
  </g>
  
  <g id="tree2" transform="translate(120,0)">
    <rect x="45" y="240" width="8" height="30" fill="#654321"/>
    <polygon points="49,210 25,245 73,245" fill="#228B22"/>
    <polygon points="49,225 30,250 68,250" fill="#32CD32"/>
  </g>
  
  <g id="tree3" transform="translate(240,0)">
    <rect x="45" y="240" width="8" height="30" fill="#654321"/>
    <polygon points="49,210 25,245 73,245" fill="#228B22"/>
    <polygon points="49,225 30,250 68,250" fill="#32CD32"/>
  </g>
  
  <!-- Casa -->
  <rect x="280" y="260" width="80" height="70" fill="#D2691E"/>
  
  <!-- Techo -->
  <polygon points="280,260 320,220 360,260" fill="#8B4513"/>
  
  <!-- Puerta -->
  <rect x="305" y="290" width="30" height="40" fill="#654321"/>
  <circle cx="333" cy="310" r="3" fill="#FFD700"/>
  
  <!-- Ventanas -->
  <rect x="285" y="270" width="15" height="15" fill="#87CEEB"/>
  <line x1="292.5" y1="270" x2="292.5" y2="285" stroke="#333" stroke-width="1"/>
  <line x1="285" y1="277.5" x2="300" y2="277.5" stroke="#333" stroke-width="1"/>
  
  <rect x="345" y="270" width="15" height="15" fill="#87CEEB"/>
  <line x1="352.5" y1="270" x2="352.5" y2="285" stroke="#333" stroke-width="1"/>
  <line x1="345" y1="277.5" x2="360" y2="277.5" stroke="#333" stroke-width="1"/>
  
  <!-- Humo de chimenea -->
  <circle cx="318" cy="210" r="6" fill="#D3D3D3" opacity="0.7"/>
  <circle cx="315" cy="195" r="7" fill="#D3D3D3" opacity="0.5"/>
  <circle cx="322" cy="180" r="8" fill="#D3D3D3" opacity="0.3"/>
  
  <!-- Chimenea -->
  <rect x="313" y="220" width="10" height="40" fill="#A0522D"/>
  
  <!-- Cerca -->
  <line x1="120" y1="310" x2="260" y2="310" stroke="#8B4513" stroke-width="3"/>
  <rect x="130" y="300" width="4" height="15" fill="#8B4513"/>
  <rect x="150" y="300" width="4" height="15" fill="#8B4513"/>
  <rect x="170" y="300" width="4" height="15" fill="#8B4513"/>
  <rect x="190" y="300" width="4" height="15" fill="#8B4513"/>
  <rect x="210" y="300" width="4" height="15" fill="#8B4513"/>
  <rect x="230" y="300" width="4" height="15" fill="#8B4513"/>
  <rect x="250" y="300" width="4" height="15" fill="#8B4513"/>
  
  <!-- Flores silvestres -->
  <circle cx="140" cy="320" r="3" fill="#FF1493"/>
  <circle cx="160" cy="325" r="3" fill="#FFB6C1"/>
  <circle cx="180" cy="318" r="3" fill="#FF69B4"/>
  <circle cx="200" cy="322" r="3" fill="#FF1493"/>
  <circle cx="220" cy="320" r="3" fill="#FFB6C1"/>
  
  <!-- Nubes -->
  <ellipse cx="50" cy="50" rx="30" ry="20" fill="#FFFFFF" opacity="0.8"/>
  <ellipse cx="80" cy="55" rx="25" ry="18" fill="#FFFFFF" opacity="0.8"/>
  <ellipse cx="20" cy="60" rx="20" ry="15" fill="#FFFFFF" opacity="0.8"/>
  
  <ellipse cx="350" cy="100" rx="28" ry="18" fill="#FFFFFF" opacity="0.7"/>
  <ellipse cx="375" cy="105" rx="22" ry="16" fill="#FFFFFF" opacity="0.7"/>
</svg>
```