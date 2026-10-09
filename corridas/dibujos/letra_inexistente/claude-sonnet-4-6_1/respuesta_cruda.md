```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="100%" stop-color="#0a0a0f"/>
    </radialGradient>
    <linearGradient id="letterGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e8c97e"/>
      <stop offset="40%" stop-color="#f5e6a3"/>
      <stop offset="100%" stop-color="#c4933f"/>
    </linearGradient>
    <linearGradient id="strokeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe8a0"/>
      <stop offset="100%" stop-color="#a06820"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="4" dy="6" stdDeviation="5" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- Decoración de fondo sutil -->
  <circle cx="200" cy="200" r="160" fill="none" stroke="#2a2a4a" stroke-width="1" opacity="0.5"/>
  <circle cx="200" cy="200" r="140" fill="none" stroke="#2a2a4a" stroke-width="0.5" opacity="0.3"/>

  <!-- Letra inventada: forma que combina elementos verticales, 
       un lazo superior asimétrico, un trazo diagonal y una espuela inferior -->
  <g filter="url(#shadow)">

    <!-- Trazo principal vertical izquierdo con serifa superior -->
    <path d="
      M 120 80
      Q 115 75 110 78
      Q 118 85 120 95
      L 120 310
      Q 120 325 130 330
      Q 125 335 118 338
      Q 112 332 115 320
      L 115 95
      Q 113 82 105 78
      Q 110 70 122 72
      Z
    " fill="url(#letterGrad)" stroke="url(#strokeGrad)" stroke-width="0.8"/>

    <!-- Vástago vertical izquierdo limpio -->
    <rect x="115" y="85" width="18" height="240" rx="3" fill="url(#letterGrad)"/>

    <!-- Serifa superior izquierda -->
    <ellipse cx="124" cy="85" rx="22" ry="6" fill="url(#letterGrad)" stroke="url(#strokeGrad)" stroke-width="0.5"/>

    <!-- Serifa inferior izquierda con espuela -->
    <path d="M 100 325 Q 115 330 133 326 Q 140 332 145 342 Q 135 338 115 336 Q 95 335 93 327 Z"
          fill="url(#letterGrad)" stroke="url(#strokeGrad)" stroke-width="0.5"/>

    <!-- Lazo superior: curva cerrada asimétrica hacia la derecha -->
    <path d="
      M 133 88
      Q 160 70 210 75
      Q 260 80 270 115
      Q 278 148 250 168
      Q 225 185 190 180
      Q 165 176 148 162
      Q 138 152 133 140
    " fill="none" stroke="url(#strokeGrad)" stroke-width="0" />

    <path d="
      M 133 88
      C 155 65 215 65 255 90
      C 295 115 290 165 255 182
      C 225 197 185 190 162 172
      C 142 157 133 138 133 118
      Z
    " fill="url(#letterGrad)" stroke="url(#strokeGrad)" stroke-width="1.5"/>

    <!-- Agujero del lazo superior (hueco interior) -->
    <path d="
      M 145 100
      C 160 85 215 83 245 103
      C 272 122 268 160 242 170
      C 218 180 180 174 160 157
      C 143 143 140 120 145 100
      Z
    " fill="url(#bg)" opacity="0.85"/>

    <!-- Trazo diagonal característico: desde la unión del lazo hacia abajo-derecha -->
    <path d="
      M 200 175
      C 220 190 255 230 275 285
      C 285 315 278 335 265 340
      C 252 345 240 335 235 318
      C 228 298 210 258 195 235
      C 185 218 178 200 185 188
      Z
    " fill="url(#letterGrad)" stroke="url(#strokeGrad)" stroke-width="0.8"/>

    <!-- Refinar el trazo diagonal con forma de cuña -->
    <path d="
      M 195 182
      L 215 178
      C 238 215 268 268 278 300
      C 285 325 278 344 263 348
      C 248 352 234 340 228 315
      C 218 285 200 240 188 210
      C 183 197 186 184 195 182
      Z
    " fill="url(#letterGrad)"/>

    <!-- Pequeño ornamento: punta con serifa en el extremo del trazo diagonal -->
    <path d="M 248 340 Q 260 355 270 350 Q 272 342 263 338 Q 255 342 248 340 Z"
          fill="url(#letterGrad)" stroke="url(#strokeGrad)" stroke-width="0.6"/>

    <!-- Trazo horizontal medio: conecta el vástago izquierdo con el cuerpo -->
    <path d="
      M 133 192
      C 148 186 170 184 190 186
      C 178 194 158 196 133 200
      Z
    " fill="url(#letterGrad)" stroke="url(#strokeGrad)" stroke-width="0.5"/>

    <!-- Línea horizontal decorativa (como travesaño único, asimétrico) -->
    <path d="
      M 124 215
      C 145 209 175 208 200 212
      C 185 220 158 221 124 224
      Z
    " fill="url(#letterGrad)" opacity="0.9"/>

    <!-- Detalle de luz / reflejo en el lazo superior -->
    <path d="
      M 155 95
      C 170 84 205 82 230 92
      C 215 88 185 87 160 97
      Z
    " fill="white" opacity="0.18"/>

    <!-- Detalle de luz en vástago -->
    <rect x="119" y="90" width="5" height="200" rx="2" fill="white" opacity="0.12"/>

  </g>

  <!-- Partículas decorativas alrededor -->
  <g opacity="0.4" fill="#e8c97e">
    <circle cx="80" cy="120" r="1.5"/>
    <circle cx="75" cy="200" r="1"/>
    <circle cx="82" cy="280" r="1.5"/>
    <circle cx="330" cy="150" r="1"/>
    <circle cx="325" cy="250" r="1.5"/>
    <circle cx="320" cy="180" r="1"/>
    <circle cx="200" cy="370" r="1.5"/>
    <circle cx="160" cy="365" r="1"/>
    <circle cx="240" cy="368" r="1"/>
  </g>

  <!-- Nombre de la letra en la parte inferior -->
  <text x="200" y="392" font-family="Georgia, serif" font-size="11" fill="#6a5a30"
        text-anchor="middle" letter-spacing="3" opacity="0.7">VHÆR</text>
</svg>
```