<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="#0a0a1a"/>

  <!-- Una letra imposible: estructura tipo Escher/Penrose -->
  <!-- Parece una letra pero sus trazos se contradicen en profundidad y continuidad -->
  <!-- El trazo vertical sube pero también baja al mismo tiempo -->
  <!-- El arco cierra pero también está abierto -->

  <!-- Trazo vertical principal - cara frontal -->
  <path d="M 140 80 L 140 320" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none" filter="url(#glow)"/>

  <!-- Sombra del trazo vertical dando profundidad falsa -->
  <path d="M 140 80 L 140 320" stroke="#7a6540" stroke-width="28" stroke-linecap="butt" fill="none" stroke-dasharray="0" opacity="0.5"
        transform="translate(8,8)"/>

  <!-- Arco superior - cara frontal -->
  <path d="M 140 80 Q 290 80 290 180 Q 290 270 140 270" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none" filter="url(#glow)"/>

  <!-- Arco superior - sombra -->
  <path d="M 140 80 Q 290 80 290 180 Q 290 270 140 270" stroke="#7a6540" stroke-width="28" stroke-linecap="butt" fill="none"
        transform="translate(8,8)" opacity="0.5"/>

  <!-- Aquí la imposibilidad: el trazo que "pasa por detrás" en la esquina superior
       pero "viene por delante" en la esquina inferior, como el triángulo de Penrose -->

  <!-- En la unión superior izquierda: el arco pasa POR ENCIMA del vertical -->
  <rect x="124" y="66" width="32" height="32" fill="#0a0a1a"/>
  <path d="M 140 66 Q 145 72 140 98" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none"/>
  <!-- El arco tapa al vertical arriba -->
  <path d="M 126 80 Q 145 80 156 80" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none"/>

  <!-- En la unión inferior izquierda: el vertical pasa POR ENCIMA del arco -->
  <rect x="124" y="256" width="32" height="32" fill="#0a0a1a"/>
  <!-- El vertical tapa al arco abajo -->
  <path d="M 140 254 L 140 284" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none"/>
  <!-- El arco queda debajo -->
  <path d="M 156 270 Q 148 270 124 270" stroke="#7a6540" stroke-width="20" stroke-linecap="butt" fill="none" opacity="0.6"/>

  <!-- Arco inferior más pequeño (como una P con doble arco, referencia a letra D/P/B imposible) -->
  <path d="M 140 200 Q 250 200 250 260 Q 250 320 140 320" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none" filter="url(#glow)"/>
  <path d="M 140 200 Q 250 200 250 260 Q 250 320 140 320" stroke="#7a6540" stroke-width="28" stroke-linecap="butt" fill="none"
        transform="translate(8,8)" opacity="0.5"/>

  <!-- Unión media: el arco chico pasa por DETRÁS del vertical (opuesto a lo de arriba) -->
  <rect x="124" y="186" width="32" height="32" fill="#0a0a1a"/>
  <path d="M 126 200 Q 136 200 154 200" stroke="#7a6540" stroke-width="20" fill="none" opacity="0.6"/>
  <path d="M 140 184 L 140 216" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none"/>

  <!-- Unión inferior derecha del arco chico con el vertical: arco viene por ENCIMA -->
  <rect x="124" y="306" width="32" height="32" fill="#0a0a1a"/>
  <path d="M 140 304 L 140 324" stroke="#7a6540" stroke-width="20" fill="none" opacity="0.4"/>
  <path d="M 126 320 Q 136 320 156 320" stroke="#e8d5a3" stroke-width="28" stroke-linecap="butt" fill="none"/>

  <!-- Líneas de construcción perspectiva para enfatizar la imposibilidad -->
  <line x1="148" y1="80" x2="168" y2="72" stroke="#e8d5a3" stroke-width="4" opacity="0.4"/>
  <line x1="148" y1="320" x2="168" y2="312" stroke="#7a6540" stroke-width="4" opacity="0.4"/>

  <!-- Facetas laterales del trazo vertical para ilusión 3D -->
  <path d="M 140 80 L 168 72 L 168 312 L 140 320" fill="#4a3a20" opacity="0.6"/>
  <path d="M 168 72 L 298 72 Q 318 80 318 180 Q 318 278 168 278 L 168 262 Q 290 262 290 180 Q 290 96 168 96 Z" fill="#2a1f0f" opacity="0.5"/>

  <!-- Título sutil -->
  <text x="200" y="380" text-anchor="middle" font-family="serif" font-size="13" fill="#e8d5a3" opacity="0.5" letter-spacing="4">LETRA IMPOSIBLE</text>
</svg>