<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <!-- Marcadores de flecha para llamadas y retornos -->
    <marker id="arrow-call" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#00e5ff" />
    </marker>
    <marker id="arrow-ret" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ff007f" />
    </marker>

    <!-- Filtros de resplandor -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-strong" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur1" />
      <feGaussianBlur stdDeviation="3" result="blur2" />
      <feMerge>
        <feMergeNode in="blur1" />
        <feMergeNode in="blur2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Gradiente de fondo -->
    <radialGradient id="bg-grad" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#16192b" />
      <stop offset="100%" stop-color="#090a10" />
    </radialGradient>

    <!-- Plantilla de un "Marco de Ejecución" (Stack Frame) con un árbol binario dentro -->
    <g id="frame">
      <!-- Caja de función / entorno -->
      <rect x="-150" y="-150" width="300" height="300" rx="24" fill="#101426" fill-opacity="0.75" stroke="#00e5ff" stroke-width="3" filter="url(#glow)" />
      
      <!-- Símbolos de código abstracto { } en los bordes laterales -->
      <path d="M -130 -70 C -142 -70 -142 -15 -130 -15 C -142 -15 -142 0 -148 0 C -142 0 -142 15 -130 15 C -142 15 -142 70 -130 70" fill="none" stroke="#4a5580" stroke-width="3" stroke-linecap="round" />
      <path d="M 130 -70 C 142 -70 142 -15 130 -15 C 142 -15 142 0 148 0 C 142 0 142 15 130 15 C 142 15 142 70 130 70" fill="none" stroke="#4a5580" stroke-width="3" stroke-linecap="round" />

      <!-- Sub-estructura de división del problema (Divide & Conquer) -->
      <line x1="0" y1="-115" x2="-70" y2="-65" stroke="#ff007f" stroke-width="2.5" stroke-dasharray="5,5" />
      <line x1="0" y1="-115" x2="70" y2="-65" stroke="#ff007f" stroke-width="2.5" stroke-dasharray="5,5" />
      <circle cx="0" cy="-115" r="9" fill="#00e5ff" />
      <circle cx="-70" cy="-65" r="6" fill="#ff007f" />
      <circle cx="70" cy="-65" r="6" fill="#ff007f" />

      <!-- Puntos de anclaje del flujo -->
      <circle cx="-150" cy="-40" r="4" fill="#00e5ff" />
      <circle cx="150" cy="40" r="4" fill="#ff007f" />
    </g>

    <!-- Transición de llamada recursiva (Izquierda: hacia adentro) y retorno (Derecha: hacia afuera) -->
    <g id="step">
      <!-- Flecha de llamada: profundiza al siguiente nivel -->
      <path d="M -150 -40 C -125 -40 -125 -24 -103 -24" fill="none" stroke="#00e5ff" stroke-width="3" marker-end="url(#arrow-call)" filter="url(#glow)" />
      <!-- Flecha de retorno: emerge del nivel inferior con la solución -->
      <path d="M 96 24 C 122 24 122 40 142 40" fill="none" stroke="#ff007f" stroke-width="3" stroke-dasharray="4,3" marker-end="url(#arrow-ret)" filter="url(#glow)" />
    </g>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg-grad)" />

  <!-- Triángulo de Sierpinski de fondo (Geometría Fractal / Recursiva) -->
  <g stroke="#ffffff" stroke-width="1" fill="none" opacity="0.04" transform="translate(0, 25)">
    <polygon points="200,20 20,340 380,340" stroke-width="2" />
    <polygon points="110,180 290,180 200,340" stroke-width="1.5" />
    <polygon points="155,100 245,100 200,180" />
    <polygon points="65,260 155,260 110,340" />
    <polygon points="245,260 335,260 290,340" />
    <!-- Nivel 3 del fractal -->
    <polygon points="177.5,60 222.5,60 200,100" />
    <polygon points="132.5,140 177.5,140 155,180" />
    <polygon points="222.5,140 267.5,140 245,180" />
    <polygon points="42.5,300 87.5,300 65,340" />
    <polygon points="132.5,300 177.5,300 155,340" />
    <polygon points="222.5,300 267.5,300 245,340" />
    <polygon points="312.5,300 357.5,300 335,340" />
  </g>

  <!-- Escena Principal Centrada -->
  <g transform="translate(200, 200)">

    <!-- Bucle Principal Externo (Auto-referencia / F(n) llamándose a sí misma) -->
    <path d="M 0 -150 C -90 -210 90 -210 5 -153" fill="none" stroke="#00e5ff" stroke-width="2.5" marker-end="url(#arrow-call)" filter="url(#glow)" />
    <path d="M 0 150 C 90 210 -90 210 -5 153" fill="none" stroke="#ff007f" stroke-width="2.5" stroke-dasharray="5,3" marker-end="url(#arrow-ret)" filter="url(#glow)" />

    <!-- Nivel 0 (Problema Original) -->
    <g>
      <use href="#frame" />
      <use href="#step" />
    </g>

    <!-- Nivel 1 (Subproblema 1) -->
    <g transform="scale(0.64)">
      <use href="#frame" />
      <use href="#step" />
    </g>

    <!-- Nivel 2 (Subproblema 2) -->
    <g transform="scale(0.4096)">
      <use href="#frame" />
      <use href="#step" />
    </g>

    <!-- Nivel 3 (Subproblema 3) -->
    <g transform="scale(0.2621)">
      <use href="#frame" />
      <use href="#step" />
    </g>

    <!-- Nivel 4 (Subproblema 4) -->
    <g transform="scale(0.1677)">
      <use href="#frame" />
    </g>

    <!-- Conexión final hacia el Caso Base -->
    <path d="M -25.1 -6.7 C -18 -6.7 -15 -2 -11 -1" fill="none" stroke="#00e5ff" stroke-width="1.5" />
    <path d="M 11 1 C 15 2 18 6.7 25.1 6.7" fill="none" stroke="#ff007f" stroke-width="1.5" />

    <!-- CASO BASE (Condición de corte / Solución trivial en el centro) -->
    <g filter="url(#glow-strong)">
      <polygon points="0,-12 12,0 0,12 -12,0" fill="#00ff88" stroke="#ffffff" stroke-width="1.5" />
      <circle cx="0" cy="0" r="3" fill="#ffffff" />
    </g>

  </g>

  <!-- Pila de Llamadas (Call Stack) en las esquinas inferiores como refuerzo conceptual -->
  <!-- Push (Izquierda) -->
  <g transform="translate(25, 330)" opacity="0.7">
    <rect x="0" y="40" width="35" height="8" rx="2" fill="#00e5ff" />
    <rect x="4" y="28" width="27" height="8" rx="2" fill="#00e5ff" opacity="0.8" />
    <rect x="8" y="16" width="19" height="8" rx="2" fill="#00e5ff" opacity="0.6" />
    <rect x="12" y="4" width="11" height="8" rx="2" fill="#00ff88" />
    <path d="M -8 45 L -8 5" fill="none" stroke="#00e5ff" stroke-width="2" marker-end="url(#arrow-call)" />
  </g>
  
  <!-- Pop (Derecha) -->
  <g transform="translate(340, 330)" opacity="0.7">
    <rect x="0" y="40" width="35" height="8" rx="2" fill="#ff007f" />
    <rect x="4" y="28" width="27" height="8" rx="2" fill="#ff007f" opacity="0.8" />
    <rect x="8" y="16" width="19" height="8" rx="2" fill="#ff007f" opacity="0.6" />
    <rect x="12" y="4" width="11" height="8" rx="2" fill="#00ff88" />
    <path d="M 43 5 L 43 45" fill="none" stroke="#ff007f" stroke-width="2" stroke-dasharray="3,2" marker-end="url(#arrow-ret)" />
  </g>
</svg>