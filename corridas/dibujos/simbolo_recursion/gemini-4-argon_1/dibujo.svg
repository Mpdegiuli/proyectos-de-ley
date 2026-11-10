<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <!-- Marcadores de flecha para llamadas y retornos -->
    <marker id="arrow-call" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#00e5ff" />
    </marker>
    <marker id="arrow-ret" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ff9100" />
    </marker>
    <marker id="arrow-loop" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#a855f7" />
    </marker>

    <!-- Efecto de resplandor -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <!-- Plantilla de una rama recursiva (Llamada azul + Retorno naranja) -->
    <g id="branch">
      <path d="M -15 24 Q -65 65 -90 120" fill="none" stroke="#00e5ff" stroke-width="5" marker-end="url(#arrow-call)" />
      <path d="M -80 128 Q -35 85 -5 30" fill="none" stroke="#ff9100" stroke-width="4" stroke-dasharray="6,6" marker-end="url(#arrow-ret)" />
    </g>

    <!-- Nodo de Función (Estado estándar) -->
    <g id="node-func">
      <circle cx="0" cy="0" r="32" fill="#1e1b4b" stroke="#00e5ff" stroke-width="4" filter="url(#glow)" />
      <!-- Bucle interno de autorreferencia -->
      <path d="M -12 -6 A 14 14 0 1 1 12 -6" fill="none" stroke="#a855f7" stroke-width="3.5" marker-end="url(#arrow-loop)" />
      <circle cx="0" cy="6" r="4" fill="#00e5ff" />
    </g>

    <!-- Nodo de Caso Base (Condición de parada) -->
    <g id="node-base">
      <!-- Octágono de STOP / Condición de corte -->
      <polygon points="-14,-34 14,-34 34,-14 34,14 14,34 -14,34 -34,14 -34,-14" fill="#064e3b" stroke="#10b981" stroke-width="4" filter="url(#glow)" />
      <!-- Símbolo de tierra/finalización y valor concreto de retorno -->
      <line x1="-16" y1="6" x2="16" y2="6" stroke="#10b981" stroke-width="4" stroke-linecap="round" />
      <line x1="-10" y1="14" x2="10" y2="14" stroke="#10b981" stroke-width="4" stroke-linecap="round" />
      <circle cx="0" cy="-10" r="8" fill="#ff9100" filter="url(#glow)" />
    </g>

    <!-- Pila de llamadas (Call Stack) en el fondo -->
    <linearGradient id="stack-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3b0764" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#090a0f" stop-opacity="0.1" />
    </linearGradient>
  </defs>

  <!-- Fondo Oscuro -->
  <rect width="400" height="400" fill="#090a0f" />

  <!-- Representación de la Pila de Ejecución (Frames anidados de fondo) -->
  <g stroke="#a855f7" stroke-opacity="0.2" fill="url(#stack-grad)">
    <rect x="20" y="20" width="360" height="360" rx="24" stroke-width="3" />
    <rect x="45" y="135" width="310" height="230" rx="18" stroke-width="2" />
    <rect x="70" y="250" width="260" height="105" rx="12" stroke-width="1" />
    <rect x="95" y="315" width="210" height="35" rx="6" stroke-width="0.5" />
  </g>

  <!-- Símbolo de Función Abstracta: Llaves { } gigantes a los lados -->
  <path d="M 35 50 Q 15 50 15 70 L 15 180 Q 15 200 5 200 Q 15 200 15 220 L 15 330 Q 15 350 35 350" fill="none" stroke="#334155" stroke-width="4" stroke-linecap="round" />
  <path d="M 365 50 Q 385 50 385 70 L 385 180 Q 385 200 395 200 Q 385 200 385 220 L 385 330 Q 385 350 365 350" fill="none" stroke="#334155" stroke-width="4" stroke-linecap="round" />

  <!-- Entrada Principal (Input) y Salida Principal (Output/Return) -->
  <path d="M 160 10 L 185 38" fill="none" stroke="#00e5ff" stroke-width="4" marker-end="url(#arrow-call)" />
  <path d="M 215 38 L 240 10" fill="none" stroke="#ff9100" stroke-width="4" stroke-dasharray="5,5" marker-end="url(#arrow-ret)" />

  <!-- ==================== ÁRBOL RECURSIVO FRACTAL ==================== -->

  <!-- NIVEL 3 (Casos Base - Profundidad máxima) -->
  <!-- Sub-ramas desde (50, 295) -->
  <use href="#branch" transform="translate(50, 295) scale(0.28)" />
  <use href="#branch" transform="translate(50, 295) scale(-0.28, 0.28)" />
  <use href="#node-base" transform="translate(20, 340) scale(0.28)" />
  <use href="#node-base" transform="translate(80, 340) scale(0.28)" />

  <!-- Sub-ramas desde (140, 295) -->
  <use href="#branch" transform="translate(140, 295) scale(0.28)" />
  <use href="#branch" transform="translate(140, 295) scale(-0.28, 0.28)" />
  <use href="#node-base" transform="translate(110, 340) scale(0.28)" />
  <use href="#node-base" transform="translate(170, 340) scale(0.28)" />

  <!-- Sub-ramas desde (260, 295) -->
  <use href="#branch" transform="translate(260, 295) scale(0.28)" />
  <use href="#branch" transform="translate(260, 295) scale(-0.28, 0.28)" />
  <use href="#node-base" transform="translate(230, 340) scale(0.28)" />
  <use href="#node-base" transform="translate(290, 340) scale(0.28)" />


  <!-- NIVEL 2 (Paso Recursivo Intermedio) -->
  <!-- Ramas desde (95, 210) -->
  <use href="#branch" transform="translate(95, 210) scale(0.5)" />
  <use href="#branch" transform="translate(95, 210) scale(-0.5, 0.5)" />
  <use href="#node-func" transform="translate(50, 295) scale(0.5)" />
  <use href="#node-func" transform="translate(140, 295) scale(0.5)" />

  <!-- Ramas desde (305, 210) - Árbol asimétrico (muestra corte temprano / poda) -->
  <use href="#branch" transform="translate(305, 210) scale(0.5)" />
  <use href="#branch" transform="translate(305, 210) scale(-0.5, 0.5)" />
  <use href="#node-func" transform="translate(260, 295) scale(0.5)" />
  <!-- Caso base alcanzado antes en la rama derecha -->
  <use href="#node-base" transform="translate(350, 295) scale(0.5)" />


  <!-- NIVEL 1 (Primera División / Divide & Conquer) -->
  <!-- Ramas desde la Raíz (200, 65) -->
  <use href="#branch" transform="translate(200, 65) scale(0.95)" />
  <use href="#branch" transform="translate(200, 65) scale(-0.95, 0.95)" />
  <use href="#node-func" transform="translate(95, 210) scale(0.75)" />
  <use href="#node-func" transform="translate(305, 210) scale(0.75)" />


  <!-- NIVEL 0 (Nodo Raíz / Problema Original) -->
  <use href="#node-func" transform="translate(200, 65) scale(1.15)" />


  <!-- ==================== META-SÍMBOLO CENTRAL ==================== -->
  <!-- Triángulo de Sierpinski (Icono universal de recursión/fractales) en el centro del árbol -->
  <g transform="translate(200, 195) scale(0.9)" stroke="#a855f7" stroke-width="1.5" fill="none" opacity="0.7" filter="url(#glow)">
    <polygon points="0,-40 -35,20 35,20" stroke-width="2" />
    <polygon points="0,20 -17.5,-10 17.5,-10" fill="#a855f7" fill-opacity="0.2" />
    <polygon points="-17.5,20 -26.25,5 -8.75,5" fill="#a855f7" fill-opacity="0.2" />
    <polygon points="17.5,20 8.75,5 26.25,5" fill="#a855f7" fill-opacity="0.2" />
    <polygon points="0,-10 -8.75,-25 8.75,-25" fill="#a855f7" fill-opacity="0.2" />
  </g>

  <!-- Indicador de Puntos Suspensivos (Profundidad N / Inducción) en la base -->
  <g fill="#10b981" opacity="0.8">
    <circle cx="50" cy="375" r="3" />
    <circle cx="50" cy="385" r="2" />
    <circle cx="50" cy="392" r="1" />
    
    <circle cx="140" cy="375" r="3" />
    <circle cx="140" cy="385" r="2" />
    <circle cx="140" cy="392" r="1" />

    <circle cx="260" cy="375" r="3" />
    <circle cx="260" cy="385" r="2" />
    <circle cx="260" cy="392" r="1" />
  </g>
</svg>