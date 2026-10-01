```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#cfe8f3"/>
      <stop offset="100%" stop-color="#e9f6e0"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#8a5cf6"/>
      <stop offset="100%" stop-color="#4fb0c6"/>
    </linearGradient>
    <radialGradient id="spot" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd86b"/>
      <stop offset="100%" stop-color="#ff9f43"/>
    </radialGradient>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="url(#sky)"/>
  <ellipse cx="200" cy="360" rx="180" ry="20" fill="#000" opacity="0.08"/>

  <!-- patas traseras -->
  <g stroke="#3d7a8c" stroke-width="10" stroke-linecap="round">
    <line x1="150" y1="290" x2="140" y2="345"/>
    <line x1="250" y1="290" x2="260" y2="345"/>
  </g>
  <ellipse cx="138" cy="350" rx="16" ry="8" fill="#3d7a8c"/>
  <ellipse cx="262" cy="350" rx="16" ry="8" fill="#3d7a8c"/>

  <!-- patas delanteras -->
  <g stroke="#3d7a8c" stroke-width="9" stroke-linecap="round">
    <line x1="175" y1="300" x2="165" y2="350"/>
    <line x1="225" y1="300" x2="235" y2="350"/>
  </g>
  <ellipse cx="163" cy="354" rx="14" ry="7" fill="#3d7a8c"/>
  <ellipse cx="237" cy="354" rx="14" ry="7" fill="#3d7a8c"/>

  <!-- cola -->
  <path d="M260,250 Q330,230 340,170 Q345,150 325,155 Q330,190 280,220 Z" fill="url(#body)"/>
  <circle cx="335" cy="160" r="14" fill="url(#spot)"/>

  <!-- cuerpo -->
  <ellipse cx="200" cy="260" rx="90" ry="60" fill="url(#body)"/>

  <!-- manchas en el cuerpo -->
  <circle cx="160" cy="250" r="10" fill="url(#spot)" opacity="0.8"/>
  <circle cx="200" cy="290" r="8" fill="url(#spot)" opacity="0.8"/>
  <circle cx="240" cy="240" r="7" fill="url(#spot)" opacity="0.8"/>

  <!-- cuello -->
  <path d="M170,220 Q160,150 190,100 Q210,80 220,100 Q200,150 210,220 Z" fill="url(#body)"/>

  <!-- cabeza -->
  <g>
    <ellipse cx="205" cy="90" rx="45" ry="38" fill="url(#body)"/>
    <!-- orejas -->
    <path d="M175,60 Q160,30 185,35 Q185,55 195,65 Z" fill="#4fb0c6"/>
    <path d="M235,60 Q255,30 230,35 Q228,55 220,65 Z" fill="#4fb0c6"/>
    <!-- cuernos pequeños tipo caracol -->
    <circle cx="180" cy="55" r="6" fill="#ffd86b"/>
    <circle cx="230" cy="55" r="6" fill="#ffd86b"/>

    <!-- ojos grandes -->
    <circle cx="188" cy="90" r="12" fill="#fff"/>
    <circle cx="222" cy="90" r="12" fill="#fff"/>
    <circle cx="190" cy="92" r="6" fill="#222"/>
    <circle cx="220" cy="92" r="6" fill="#222"/>
    <circle cx="192" cy="89" r="2" fill="#fff"/>
    <circle cx="222" cy="89" r="2" fill="#fff"/>

    <!-- hocico / pico suave -->
    <path d="M195,105 Q205,120 215,105 Q210,115 205,115 Q200,115 195,105 Z" fill="#ff9f43"/>

    <!-- antenas tipo mariposa -->
    <path d="M205,55 Q195,30 175,20" stroke="#ff9f43" stroke-width="3" fill="none" stroke-linecap="round"/>
    <circle cx="175" cy="20" r="5" fill="#ff9f43"/>
    <path d="M205,55 Q215,30 235,20" stroke="#ff9f43" stroke-width="3" fill="none" stroke-linecap="round"/>
    <circle cx="235" cy="20" r="5" fill="#ff9f43"/>
  </g>

  <!-- alitas pequeñas decorativas en la espalda -->
  <path d="M150,230 Q120,210 100,230 Q120,245 150,245 Z" fill="#c9aefc" opacity="0.8"/>
  <path d="M250,230 Q280,210 300,230 Q280,245 250,245 Z" fill="#c9aefc" opacity="0.8"/>

  <!-- pequeñas burbujas flotando (detalle fantástico) -->
  <circle cx="80" cy="120" r="4" fill="#fff" opacity="0.6"/>
  <circle cx="320" cy="90" r="6" fill="#fff" opacity="0.5"/>
  <circle cx="340" cy="250" r="3" fill="#fff" opacity="0.6"/>
</svg>
```