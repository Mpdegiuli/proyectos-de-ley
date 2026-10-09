<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1a1a2e"/>
      <stop offset="1" stop-color="#16213e"/>
    </linearGradient>
    <linearGradient id="letter" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd45e"/>
      <stop offset="0.5" stop-color="#f0a500"/>
      <stop offset="1" stop-color="#e25822"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="0.4" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="4"/>
    </filter>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- textura sutil de puntos -->
  <g fill="#ffffff" opacity="0.06">
    <circle cx="30" cy="40" r="2"/><circle cx="90" cy="20" r="1.5"/><circle cx="150" cy="55" r="2"/>
    <circle cx="220" cy="25" r="1.5"/><circle cx="290" cy="48" r="2"/><circle cx="360" cy="30" r="1.5"/>
    <circle cx="50" cy="110" r="1.5"/><circle cx="200" cy="90" r="2"/><circle cx="340" cy="120" r="1.5"/>
    <circle cx="25" cy="200" r="1.5"/><circle cx="375" cy="210" r="1.5"/><circle cx="60" cy="290" r="2"/>
    <circle cx="130" cy="330" r="1.5"/><circle cx="250" cy="350" r="2"/><circle cx="330" cy="300" r="1.5"/>
    <circle cx="370" cy="370" r="2"/><circle cx="35" cy="365" r="1.5"/><circle cx="110" cy="180" r="1.2"/>
    <circle cx="300" cy="170" r="1.2"/><circle cx="180" cy="300" r="1.2"/><circle cx="280" cy="240" r="1.2"/>
  </g>

  <!-- halo detrás de la letra -->
  <circle cx="200" cy="205" r="150" fill="url(#letter)" opacity="0.10" filter="url(#soft)"/>
  <circle cx="200" cy="205" r="110" fill="#ffd45e" opacity="0.08" filter="url(#soft)"/>

  <!-- sombra proyectada de la letra -->
  <g transform="translate(8,12)" fill="#000000" opacity="0.35" filter="url(#soft)">
    <path d="M200 60 L130 320 L163 320 L182 250 L218 250 L237 320 L270 320 Z"/>
    <rect x="190" y="215" width="20" height="20" rx="3"/>
  </g>

  <!-- letra A -->
  <g filter="url(#glow)">
    <!-- contorno principal -->
    <path d="M200 60
             C 196 60 192 64 190 70
             L 128 306 C 126 314 130 320 138 320
             L 158 320 C 165 320 169 316 171 310
             L 180 278
             L 220 278
             L 229 310
             C 231 316 235 320 242 320
             L 262 320
             C 270 320 274 314 272 306
             L 210 70
             C 208 64 204 60 200 60 Z"
          fill="url(#letter)" stroke="#7a3b00" stroke-width="3" stroke-linejoin="round"/>

    <!-- barra transversal -->
    <path d="M172 232 L228 232
             C 233 232 236 235 236 240
             L 236 252
             C 236 257 233 260 228 260
             L 172 260
             C 167 260 164 257 164 252
             L 164 240
             C 164 235 167 232 172 232 Z"
          fill="url(#letter)" stroke="#7a3b00" stroke-width="3" stroke-linejoin="round"/>

    <!-- triángulo interior (contraforma) -->
    <path d="M200 118 L216 250 L184 250 Z" fill="#16213e"/>
    <path d="M200 118 L216 250 L184 250 Z" fill="none" stroke="#7a3b00" stroke-width="3" stroke-linejoin="round"/>

    <!-- recorte bajo la barra -->
    <rect x="187" y="262" width="26" height="20" fill="#16213e" stroke="#7a3b00" stroke-width="3" rx="2"/>
  </g>

  <!-- brillo lateral izquierdo de las astas -->
  <path d="M200 68 L 194 88 L 146 300 L 140 306 C 136 312 138 316 144 316
           L 152 316 C 157 316 160 313 161 308
           L 199 96 Z" fill="url(#shine)" opacity="0.8"/>

  <!-- brillo en la barra -->
  <path d="M168 236 L 172 236 L 172 248 L 168 248 Z" fill="#ffffff" opacity="0.5" rx="2"/>
  <rect x="168" y="236" width="8" height="10" rx="2" fill="#ffffff" opacity="0.4"/>

  <!-- pequeño destello arriba -->
  <circle cx="212" cy="78" r="4" fill="#ffffff" opacity="0.85"/>
  <circle cx="219" cy="85" r="2" fill="#ffffff" opacity="0.6"/>

  <!-- base / suelo -->
  <ellipse cx="200" cy="336" rx="120" ry="12" fill="#000000" opacity="0.3" filter="url(#soft)"/>

  <!-- línea decorativa -->
  <line x1="120" y1="356" x2="280" y2="356" stroke="#ffd45e" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
  <line x1="150" y1="364" x2="250" y2="364" stroke="#f0a500" stroke-width="1.5" stroke-linecap="round" opacity="0.35"/>
</svg>