<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <!-- Marcadores de flecha para el llamado y el retorno -->
    <marker id="call-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ff3366" />
    </marker>
    <marker id="ret-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#00ffcc" />
    </marker>

    <!-- El "Marco de Pila" (Stack Frame) o "Función" base -->
    <g id="frame">
      <!-- Fondo y borde del marco -->
      <rect x="-150" y="-150" width="300" height="300" rx="24" fill="#101426" stroke="#3b4d80" stroke-width="6" />
      <!-- Barra superior del entorno de ejecución -->
      <path d="M -150 -110 L 150 -110" stroke="#3b4d80" stroke-width="4" />
      <circle cx="-120" cy="-130" r="8" fill="#ff5f56" />
      <circle cx="-95" cy="-130" r="8" fill="#ffbd2e" />
      <circle cx="-70" cy="-130" r="8" fill="#27c93f" />
      
      <!-- Símbolo de división de problema (Árbol binario / Divide y vencerás) -->
      <path d="M -110 -60 L -90 -30 M -110 -60 L -130 -30" stroke="#526b9c" stroke-width="4" stroke-linecap="round" />
      <circle cx="-110" cy="-60" r="6" fill="#00ffcc" />
      <circle cx="-90" cy="-30" r="5" fill="#3b4d80" />
      <circle cx="-130" cy="-30" r="5" fill="#3b4d80" />

      <!-- Bucle de autollamado en las esquinas (Ouroboros / Auto-referencia) -->
      <path d="M 110 -130 A 10 10 0 1 1 100 -120" fill="none" stroke="#ff3366" stroke-width="3" marker-end="url(#call-arrow)" />
    </g>

    <!-- Conectores entre nivel padre y nivel hijo (Paso recursivo y Retorno) -->
    <g id="step">
      <!-- Flecha de Llamada Recursiva (Profundización) -->
      <path d="M -140 0 C -115 0, -115 15, -96 15" fill="none" stroke="#ff3366" stroke-width="4" marker-end="url(#call-arrow)" />
      <!-- Flecha de Retorno (Backtracking / Resolución) -->
      <path d="M 90 -15 C 115 -15, 115 0, 134 0" fill="none" stroke="#00ffcc" stroke-width="4" stroke-dasharray="6,4" marker-end="url(#ret-arrow)" />
    </g>
    
    <!-- Resplandor para el Caso Base -->
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Fondo general -->
  <rect width="400" height="400" fill="#080a12" />

  <!-- Árbol fractal sutil de fondo para reforzar la idea de ramificación recursiva -->
  <g stroke="#182039" stroke-width="2" fill="none">
    <path d="M 200 400 L 200 350 L 100 250 L 50 150 M 100 250 L 150 150" />
    <path d="M 200 350 L 300 250 L 250 150 M 300 250 L 350 150" />
  </g>

  <!-- Contenedor principal centrado -->
  <g transform="translate(200, 200)">
    
    <!-- NIVEL 0 (Función Principal) -->
    <use href="#frame" />
    <use href="#step" />

    <!-- NIVEL 1 (Primera llamada recursiva: Escala 0.6, Rotación suave para efecto espiral) -->
    <g transform="scale(0.6) rotate(8)">
      <use href="#frame" />
      <use href="#step" />
      
      <!-- NIVEL 2 (Segunda llamada recursiva) -->
      <g transform="scale(0.6) rotate(8)">
        <use href="#frame" />
        <use href="#step" />
        
        <!-- NIVEL 3 (Tercera llamada recursiva) -->
        <g transform="scale(0.6) rotate(8)">
          <use href="#frame" />
          <use href="#step" />
          
          <!-- NIVEL 4 (CASO BASE / Condición de corte) -->
          <g transform="scale(0.6) rotate(8)">
            <rect x="-150" y="-150" width="300" height="300" rx="40" fill="#00ffcc" opacity="0.2" />
            <!-- Diamante de decisión/parada brillante -->
            <polygon points="0,-110 110,0 0,110 -110,0" fill="#00ffcc" filter="url(#glow)" />
            <circle cx="0" cy="0" r="40" fill="#101426" />
            <circle cx="0" cy="0" r="20" fill="#ff3366" />
          </g>
          
        </g>
      </g>
    </g>

    <!-- Gran flecha exterior que simboliza que la función global se envuelve a sí misma -->
    <path d="M 0 -175 C 130 -175, 185 -100, 185 0 C 185 100, 120 175, 10 175" fill="none" stroke="#ff3366" stroke-width="5" stroke-linecap="round" marker-end="url(#call-arrow)" />
    <path d="M -10 175 C -120 175, -185 100, -185 0 C -185 -95, -135 -165, -20 -174" fill="none" stroke="#00ffcc" stroke-width="5" stroke-dasharray="10,8" stroke-linecap="round" marker-end="url(#ret-arrow)" />
    
  </g>
</svg>