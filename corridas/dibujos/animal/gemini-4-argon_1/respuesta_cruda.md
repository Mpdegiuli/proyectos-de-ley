<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0f0c29"/>
      <stop offset="50%" stop-color="#302b63"/>
      <stop offset="100%" stop-color="#24243e"/>
    </linearGradient>
    <linearGradient id="foxMain" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ff6b2b"/>
      <stop offset="100%" stop-color="#d9381e"/>
    </linearGradient>
    <linearGradient id="foxShadow" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#d9381e"/>
      <stop offset="100%" stop-color="#8c1d13"/>
    </linearGradient>
    <linearGradient id="cream" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#ffe5d4"/>
    </linearGradient>
    <linearGradient id="dark" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2c1d27"/>
      <stop offset="100%" stop-color="#110b10"/>
    </linearGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff9d6" stop-opacity="1"/>
      <stop offset="40%" stop-color="#ffe885" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#ffe885" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- Estrellas -->
  <g fill="#ffffff" opacity="0.8">
    <circle cx="50" cy="60" r="1.5"/>
    <circle cx="90" cy="30" r="1"/>
    <circle cx="150" cy="80" r="2" opacity="0.5"/>
    <circle cx="280" cy="40" r="1.5"/>
    <circle cx="350" cy="90" r="1"/>
    <circle cx="320" cy="180" r="1.5" opacity="0.6"/>
    <circle cx="60" cy="190" r="1"/>
    <circle cx="40" cy="120" r="2"/>
    <path d="M250,60 Q250,70 260,70 Q250,70 250,80 Q250,70 240,70 Q250,70 250,60" fill="#fff9d6"/>
    <path d="M80,140 Q80,145 85,145 Q80,145 80,150 Q80,145 75,145 Q80,145 80,140" fill="#fff9d6"/>
  </g>

  <!-- Luna -->
  <circle cx="290" cy="110" r="80" fill="url(#moonGlow)"/>
  <circle cx="290" cy="110" r="35" fill="#fff9d6"/>

  <!-- Bosque de fondo -->
  <g fill="#191636">
    <polygon points="-20,400 30,220 80,400"/>
    <polygon points="40,400 90,190 140,400"/>
    <polygon points="100,400 140,250 180,400"/>
    <polygon points="240,400 280,260 320,400"/>
    <polygon points="290,400 350,180 410,400"/>
    <polygon points="350,400 390,230 430,400"/>
  </g>

  <!-- Colina -->
  <path d="M-20,330 Q120,290 250,330 T420,350 L420,400 L-20,400 Z" fill="#131124"/>
  <ellipse cx="195" cy="340" rx="85" ry="15" fill="#090812" opacity="0.6"/>

  <!-- ZORRO -->
  <g id="fox">
    <!-- Pata trasera (sombra) -->
    <path d="M135,260 C110,270 110,320 130,335 L165,335 L165,300 Z" fill="url(#foxShadow)"/>

    <!-- Cuerpo base -->
    <path d="M160,175 C135,215 130,275 135,335 L220,335 C225,285 215,215 195,175 Z" fill="url(#foxMain)"/>
    
    <!-- Sombra del cuerpo -->
    <path d="M160,175 C145,215 140,275 135,335 L180,335 C175,280 165,220 175,175 Z" fill="url(#foxShadow)"/>

    <!-- Pecho blanco -->
    <path d="M180,175 C175,210 185,255 205,275 C220,255 225,210 205,175 Z" fill="url(#cream)"/>

    <!-- Pata delantera izquierda (fondo) -->
    <path d="M205,245 L215,335 L230,335 L220,245 Z" fill="url(#foxShadow)"/>
    <path d="M210,295 L215,335 L232,335 C232,328 228,325 225,325 L224,295 Z" fill="url(#dark)"/>

    <!-- Pata delantera derecha -->
    <path d="M185,240 L180,335 L198,335 L205,240 Z" fill="url(#foxMain)"/>
    <path d="M182,290 L180,335 L202,335 C202,328 198,325 195,325 L199,290 Z" fill="url(#dark)"/>

    <!-- Cola (detrás y envolviendo) -->
    <path d="M138,320 C70,310 50,240 85,190 C105,160 135,195 145,220 C165,270 175,295 235,320 C265,332 250,355 205,348 C165,342 150,330 138,320 Z" fill="url(#foxMain)"/>
    <!-- Sombra de la cola -->
    <path d="M138,320 C85,312 65,260 80,215 C85,255 115,295 165,315 C195,325 225,335 245,335 C240,348 220,350 205,348 C165,342 150,330 138,320 Z" fill="url(#foxShadow)" opacity="0.6"/>
    <!-- Punta blanca de la cola -->
    <path d="M85,190 C70,212 72,240 85,262 C90,245 105,255 108,240 C115,245 125,235 125,220 C135,205 115,175 85,190 Z" fill="url(#cream)"/>

    <!-- Cabeza -->
    <g id="head">
      <!-- Oreja izquierda -->
      <path d="M150,150 L135,85 C155,85 175,105 180,125 Z" fill="url(#dark)"/>
      <path d="M153,142 L143,95 C155,97 168,110 172,125 Z" fill="#ffb899"/>
      <path d="M150,150 L143,95 L135,85 L150,150 Z" fill="url(#foxMain)"/>

      <!-- Oreja derecha -->
      <path d="M210,145 L220,80 C195,85 185,105 180,125 Z" fill="url(#dark)"/>
      <path d="M206,138 L212,92 C198,96 190,110 186,125 Z" fill="#ffb899"/>
      <path d="M210,145 L220,80 L212,92 L206,138 Z" fill="url(#foxShadow)"/>

      <!-- Cráneo/Cara base -->
      <path d="M145,140 C155,110 200,110 215,140 C230,155 245,165 255,170 C235,185 205,190 185,185 C155,180 135,160 145,140 Z" fill="url(#foxMain)"/>
      
      <!-- Sombra en la cabeza -->
      <path d="M145,140 C155,110 180,115 180,115 C165,130 160,155 185,185 C155,180 135,160 145,140 Z" fill="url(#foxShadow)" opacity="0.5"/>

      <!-- Mejilla blanca y hocico -->
      <path d="M175,183 C190,165 215,155 255,170 C235,188 200,190 175,183 Z" fill="url(#cream)"/>
      
      <!-- Nariz -->
      <circle cx="253" cy="169" r="5" fill="url(#dark)"/>
      <circle cx="252" cy="167" r="1.5" fill="#ffffff" opacity="0.7"/>

      <!-- Ojo cerrado (feliz/sereno) -->
      <path d="M198,150 Q208,142 216,152" fill="none" stroke="url(#dark)" stroke-width="3" stroke-linecap="round"/>
      <path d="M213,150 L218,154" fill="none" stroke="url(#dark)" stroke-width="2" stroke-linecap="round"/>
      
      <!-- Detalles de pelaje en la mejilla -->
      <path d="M145,140 C135,150 130,155 125,155 C132,162 140,165 148,165 C140,170 138,172 132,172 C145,178 160,182 175,183 C165,165 155,150 145,140 Z" fill="url(#foxShadow)"/>
    </g>
  </g>

  <!-- Luciérnagas (Detalles mágicos) -->
  <g filter="url(#glow)">
    <circle cx="280" cy="165" r="3" fill="#ffeb3b"/>
    <circle cx="240" cy="220" r="2" fill="#ffeb3b" opacity="0.8"/>
    <circle cx="110" cy="140" r="2.5" fill="#ffeb3b" opacity="0.9"/>
    <circle cx="70" cy="280" r="2" fill="#ffeb3b" opacity="0.6"/>
    <circle cx="310" cy="290" r="3" fill="#ffeb3b" opacity="0.7"/>
  </g>
  
  <!-- Plantas en primer plano -->
  <g stroke="#090812" stroke-width="3" stroke-linecap="round" fill="none">
    <path d="M30,400 Q40,350 60,320"/>
    <path d="M35,400 Q20,360 10,340"/>
    <path d="M40,400 Q60,370 80,360"/>
    <path d="M360,400 Q350,360 330,330"/>
    <path d="M365,400 Q380,350 390,320"/>
  </g>
</svg>