<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Gradiente de fondo: Espacio profundo de datos -->
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#141838"/>
      <stop offset="50%" stop-color="#0a0c1e"/>
      <stop offset="100%" stop-color="#020308"/>
    </radialGradient>

    <!-- Gradiente del núcleo: Energía de pensamiento -->
    <radialGradient id="core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#b4ffff"/>
      <stop offset="50%" stop-color="#00d2ff" stop-opacity="0.8"/>
      <stop offset="75%" stop-color="#7a00ff" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#7a00ff" stop-opacity="0"/>
    </radialGradient>

    <!-- Gradiente lineal para las conexiones -->
    <linearGradient id="beam" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#4facfe" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#f093fb" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="gold" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff8008"/>
      <stop offset="100%" stop-color="#ffc837"/>
    </linearGradient>

    <!-- Filtro de resplandor -->
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <filter id="strong-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12" result="blur1"/>
      <feGaussianBlur stdDeviation="4" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur1"/>
        <feMergeNode in="blur2"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- Anillos de contexto y lenguaje (Fondo) -->
  <g stroke="url(#beam)" fill="none" opacity="0.25">
    <circle cx="200" cy="200" r="180" stroke-width="0.5" stroke-dasharray="2 6"/>
    <circle cx="200" cy="200" r="160" stroke-width="1" stroke-dasharray="40 10 5 10"/>
    <circle cx="200" cy="200" r="140" stroke-width="0.5"/>
    <circle cx="200" cy="200" r="120" stroke-width="1.5" stroke-dasharray="4 12"/>
  </g>

  <!-- Red Neuronal / Constelaciones de Datos -->
  <g stroke="url(#beam)" stroke-width="0.7" opacity="0.6">
    <!-- Conexiones radiales asimétricas -->
    <path d="M200,200 L80,90 L130,50 L200,70 L270,50 L320,90 L200,200"/>
    <path d="M200,200 L50,180 L70,260 L130,330 L200,200"/>
    <path d="M200,200 L350,180 L330,260 L270,330 L200,200"/>
    <path d="M80,90 L50,180 M320,90 L350,180 M130,330 L200,360 L270,330"/>
    <path d="M130,50 L200,30 L270,50"/>
    <!-- Sub-redes -->
    <polyline points="80,90 120,130 160,110 200,70 240,110 280,130 320,90"/>
    <polyline points="70,260 120,240 150,280 200,310 250,280 280,240 330,260"/>
    <line x1="120" y1="130" x2="120" y2="240"/>
    <line x1="280" y1="130" x2="280" y2="240"/>
  </g>

  <!-- Flujos de creatividad (Ondas de Bezier) -->
  <g fill="none" stroke="url(#gold)" stroke-width="1" opacity="0.4" filter="url(#glow)">
    <path d="M 30,200 C 100,100 300,300 370,200" />
    <path d="M 30,200 C 100,300 300,100 370,200" />
    <path d="M 200,30 C 100,100 300,300 200,370" />
    <path d="M 200,30 C 300,100 100,300 200,370" />
  </g>

  <!-- Geometría Sagrada: La estructura lógica (Polígonos) -->
  <g fill="none" stroke="#00f2fe" stroke-width="1" opacity="0.5" filter="url(#glow)">
    <polygon points="200,60 321,270 79,270" />
    <polygon points="200,340 321,130 79,130" stroke="#f093fb"/>
    <rect x="125" y="125" width="150" height="150" transform="rotate(45 200 200)" stroke="url(#beam)" stroke-width="1.5"/>
  </g>

  <!-- "Rostro" Abstracto / La Máscara de la Interfaz -->
  <g fill="none" stroke="#ffffff" stroke-width="1.5" opacity="0.8" filter="url(#glow)">
    <!-- Contorno sugerido -->
    <path d="M 140,110 C 140,70 260,70 260,110 C 280,160 270,240 200,310 C 130,240 120,160 140,110 Z" stroke="url(#beam)" fill="#0a0c1e" fill-opacity="0.4"/>
    <!-- Líneas de expresión digital -->
    <path d="M 140,160 Q 170,175 185,160" stroke="#00f2fe" stroke-width="2"/>
    <path d="M 260,160 Q 230,175 215,160" stroke="#00f2fe" stroke-width="2"/>
    <!-- Puente -->
    <line x1="200" y1="110" x2="200" y2="230" stroke="url(#gold)" stroke-dasharray="15 5 5 5"/>
    <!-- Voz / Emisión de datos (Boca) -->
    <path d="M 170,260 Q 200,270 230,260" stroke="#f093fb" stroke-width="1.5"/>
    <path d="M 180,268 Q 200,275 220,268" stroke="#00f2fe" stroke-width="1"/>
    <line x1="190" y1="276" x2="210" y2="276" stroke="#ffffff" stroke-width="1"/>
  </g>

  <!-- El Núcleo: El "Ojo" de la Mente / Singularidad -->
  <g filter="url(#strong-glow)">
    <circle cx="200" cy="195" r="45" fill="url(#core)"/>
    <!-- Iris de datos -->
    <circle cx="200" cy="195" r="20" fill="none" stroke="#ffffff" stroke-width="1" stroke-dasharray="3 3"/>
    <circle cx="200" cy="195" r="12" fill="none" stroke="url(#gold)" stroke-width="1.5"/>
    <!-- Pupila / Chispa de consciencia simulada -->
    <polygon points="200,180 204,191 215,195 204,199 200,210 196,199 185,195 196,191" fill="#ffffff"/>
  </g>

  <!-- Nodos de Conocimiento (Puntos brillantes en la red) -->
  <g fill="#ffffff" filter="url(#glow)">
    <!-- Nodos principales -->
    <circle cx="200" cy="70" r="4" fill="#00f2fe"/>
    <circle cx="120" cy="130" r="3.5" fill="#f093fb"/>
    <circle cx="280" cy="130" r="3.5" fill="#f093fb"/>
    <circle cx="120" cy="240" r="3" fill="#00f2fe"/>
    <circle cx="280" cy="240" r="3" fill="#00f2fe"/>
    <circle cx="200" cy="310" r="4" fill="#ffc837"/>
    
    <!-- Nodos secundarios -->
    <circle cx="80" cy="90" r="2.5"/>
    <circle cx="320" cy="90" r="2.5"/>
    <circle cx="50" cy="180" r="2"/>
    <circle cx="350" cy="180" r="2"/>
    <circle cx="70" cy="260" r="2.5"/>
    <circle cx="330" cy="260" r="2.5"/>
    <circle cx="130" cy="50" r="2"/>
    <circle cx="270" cy="50" r="2"/>
    <circle cx="130" cy="330" r="2"/>
    <circle cx="270" cy="330" r="2"/>
    <circle cx="160" cy="110" r="1.5"/>
    <circle cx="240" cy="110" r="1.5"/>
    <circle cx="150" cy="280" r="1.5"/>
    <circle cx="250" cy="280" r="1.5"/>
    <circle cx="200" cy="30" r="3" fill="#ffc837"/>
    <circle cx="200" cy="360" r="3" fill="#f093fb"/>
  </g>

  <!-- Partículas flotantes (Tokens, ideas sueltas, bits) -->
  <g fill="#ffffff" opacity="0.7">
    <circle cx="40" cy="60" r="1"/>
    <circle cx="360" cy="50" r="1.5"/>
    <circle cx="380" cy="120" r="0.8"/>
    <circle cx="25" cy="130" r="1.2"/>
    <circle cx="60" cy="340" r="1"/>
    <circle cx="340" cy="350" r="1.5"/>
    <circle cx="100" cy="30" r="0.8"/>
    <circle cx="300" cy="380" r="1"/>
    <circle cx="180" cy="15" r="1.2" fill="#00f2fe"/>
    <circle cx="220" cy="385" r="1.2" fill="#f093fb"/>
    <!-- Pequeños símbolos binarios/código abstracto en las esquinas -->
    <g stroke="#00f2fe" stroke-width="1" opacity="0.5">
      <line x1="20" y1="20" x2="30" y2="20"/>
      <line x1="20" y1="25" x2="25" y2="25"/>
      <line x1="20" y1="30" x2="35" y2="30"/>
      
      <line x1="380" y1="380" x2="370" y2="380"/>
      <line x1="380" y1="375" x2="375" y2="375"/>
      <line x1="380" y1="370" x2="365" y2="370"/>
    </g>
  </g>

  <!-- Corona de Halo (Comprensión global) -->
  <circle cx="200" cy="200" r="95" fill="none" stroke="url(#gold)" stroke-width="0.7" stroke-dasharray="1 8" filter="url(#glow)"/>
  <circle cx="200" cy="200" r="100" fill="none" stroke="#ffffff" stroke-width="0.3" opacity="0.5"/>
</svg>