```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#16213e;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="letterGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e94560;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#f5a623;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e94560;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="6" dy="8" stdDeviation="6" flood-color="#e94560" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg)" />

  <!-- Círculos decorativos de fondo -->
  <circle cx="60" cy="60" r="80" fill="none" stroke="#e94560" stroke-width="1" opacity="0.15"/>
  <circle cx="60" cy="60" r="55" fill="none" stroke="#f5a623" stroke-width="1" opacity="0.1"/>
  <circle cx="340" cy="340" r="90" fill="none" stroke="#e94560" stroke-width="1" opacity="0.15"/>
  <circle cx="340" cy="340" r="60" fill="none" stroke="#f5a623" stroke-width="1" opacity="0.1"/>

  <!-- Puntos decorativos -->
  <circle cx="30" cy="200" r="3" fill="#e94560" opacity="0.4"/>
  <circle cx="370" cy="200" r="3" fill="#e94560" opacity="0.4"/>
  <circle cx="200" cy="30" r="3" fill="#f5a623" opacity="0.4"/>
  <circle cx="200" cy="370" r="3" fill="#f5a623" opacity="0.4"/>

  <!-- Letra R construida con paths -->
  <!-- Sombra / capa inferior para efecto 3D -->
  <g transform="translate(8,10)" opacity="0.3">
    <!-- Palo vertical izquierdo -->
    <rect x="82" y="62" width="42" height="276" rx="6" fill="#e94560"/>
    <!-- Joroba superior -->
    <path d="M 124 62 
             L 124 62
             C 180 62 230 90 230 152
             C 230 214 180 242 124 242
             L 124 242
             L 124 62 Z" fill="#e94560"/>
    <!-- Pata diagonal -->
    <path d="M 130 230 L 260 338 L 220 338 L 90 230 Z" fill="#e94560"/>
  </g>

  <!-- Letra R principal -->
  <g filter="url(#shadow)">
    <!-- Palo vertical izquierdo -->
    <rect x="74" y="52" width="42" height="276" rx="6" fill="url(#letterGrad)"/>

    <!-- Joroba (bowel) - la parte curva superior -->
    <path d="M 116 52 
             L 116 52
             C 178 52 228 82 228 148
             C 228 214 178 240 116 240
             L 116 240
             L 116 196
             C 152 196 184 180 184 148
             C 184 116 152 96 116 96
             L 116 52 Z" fill="url(#letterGrad)"/>

    <!-- Pata diagonal de la R -->
    <path d="M 122 226 L 258 328 L 208 328 L 74 226 Z" fill="url(#letterGrad)"/>
  </g>

  <!-- Brillo / highlight en la letra -->
  <g opacity="0.35" filter="url(#glow)">
    <!-- Highlight palo vertical -->
    <rect x="74" y="52" width="14" height="276" rx="4" fill="white"/>
    <!-- Highlight joroba -->
    <path d="M 116 52 
             C 155 52 195 68 215 98
             C 200 72 165 60 116 60
             L 116 52 Z" fill="white"/>
  </g>

  <!-- Puntos de luz reflejados -->
  <circle cx="95" cy="80" r="5" fill="white" opacity="0.25"/>
  <circle cx="170" cy="70" r="3" fill="white" opacity="0.2"/>

  <!-- Líneas decorativas horizontales -->
  <line x1="50" y1="375" x2="350" y2="375" stroke="#e94560" stroke-width="1.5" opacity="0.3" stroke-dasharray="4,6"/>
  <line x1="50" y1="25" x2="350" y2="25" stroke="#f5a623" stroke-width="1.5" opacity="0.3" stroke-dasharray="4,6"/>

  <!-- Detalles esquinas -->
  <path d="M 20 20 L 50 20 L 50 23 L 23 23 L 23 50 L 20 50 Z" fill="#e94560" opacity="0.6"/>
  <path d="M 380 20 L 350 20 L 350 23 L 377 23 L 377 50 L 380 50 Z" fill="#e94560" opacity="0.6"/>
  <path d="M 20 380 L 50 380 L 50 377 L 23 377 L 23 350 L 20 350 Z" fill="#f5a623" opacity="0.6"/>
  <path d="M 380 380 L 350 380 L 350 377 L 377 377 L 377 350 L 380 350 Z" fill="#f5a623" opacity="0.6"/>
</svg>
```