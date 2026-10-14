<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <!-- Fondo Cósmico -->
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#1a103c"/>
      <stop offset="50%" stop-color="#0a0618"/>
      <stop offset="100%" stop-color="#020106"/>
    </radialGradient>

    <!-- Brillo Mágico -->
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    
    <!-- Brillo Suave -->
    <filter id="soft-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="15"/>
    </filter>

    <!-- Gradiente del Hueco (Vórtice) -->
    <radialGradient id="void" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#000000"/>
      <stop offset="60%" stop-color="#0d0420"/>
      <stop offset="85%" stop-color="#ff007f" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </radialGradient>

    <!-- Gradiente de Alas de Cristal -->
    <linearGradient id="wing-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.7"/>
      <stop offset="40%" stop-color="#ff00aa" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#7000ff" stop-opacity="0.1"/>
    </linearGradient>

    <!-- Gradiente de Tentáculos (Fusión de materia y nada) -->
    <linearGradient id="tentacle-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff00aa"/>
      <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#0a0618" stop-opacity="0"/>
    </linearGradient>

    <!-- Caras del Cubo Imposible -->
    <linearGradient id="face-top" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#80ffdb"/>
      <stop offset="100%" stop-color="#00b4d8"/>
    </linearGradient>
    <linearGradient id="face-left" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7209b7"/>
      <stop offset="100%" stop-color="#3a0ca3"/>
    </linearGradient>
    <linearGradient id="face-right" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f72585"/>
      <stop offset="100%" stop-color="#b5179e"/>
    </linearGradient>

    <!-- Ojo Dimensional -->
    <radialGradient id="eye-iris" cx="50%" cy="50%" r="50%">
      <stop offset="20%" stop-color="#ffbe0b"/>
      <stop offset="70%" stop-color="#fb5607"/>
      <stop offset="100%" stop-color="#ff006e"/>
    </radialGradient>

    <!-- Plantilla de Ojo Flotante -->
    <g id="floating-eye">
      <path d="M -20 0 Q 0 -15 20 0 Q 0 15 -20 0 Z" fill="#10002b" stroke="#00f0ff" stroke-width="1.5"/>
      <circle cx="0" cy="0" r="7" fill="url(#eye-iris)"/>
      <polygon points="0,-5 2,0 0,5 -2,0" fill="#000"/>
      <circle cx="3" cy="-2" r="1.5" fill="#fff"/>
    </g>
    
    <!-- Plantilla de Pata-Reloj -->
    <g id="clock-leg">
      <path d="M 0,0 L -15,30 L 5,60 L -5,90" fill="none" stroke="url(#face-right)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="-15" cy="30" r="6" fill="#1a103c" stroke="#ffbe0b" stroke-width="1.5"/>
      <circle cx="5" cy="60" r="4" fill="#1a103c" stroke="#00f0ff" stroke-width="1"/>
      <!-- Pie que gotea hacia arriba -->
      <path d="M -5,90 C -10,100 0,100 -5,90 C -8,80 -2,80 -5,70" fill="#00f0ff" filter="url(#glow)"/>
    </g>
  </defs>

  <!-- Fondo -->
  <rect width="100%" height="100%" fill="url(#bg)"/>

  <!-- Aura de fondo -->
  <circle cx="200" cy="200" r="120" fill="#7209b7" opacity="0.3" filter="url(#soft-glow)"/>
  <circle cx="200" cy="180" r="80" fill="#00f0ff" opacity="0.2" filter="url(#soft-glow)"/>

  <!-- Estrellas / Partículas -->
  <g fill="#fff" opacity="0.6">
    <circle cx="50" cy="60" r="1"/>
    <circle cx="350" cy="80" r="1.5" filter="url(#glow)"/>
    <circle cx="80" cy="320" r="1"/>
    <circle cx="320" cy="350" r="2" filter="url(#glow)"/>
    <circle cx="150" cy="40" r="0.5"/>
    <circle cx="280" cy="30" r="1"/>
    <circle cx="40" cy="180" r="1.5"/>
    <circle cx="360" cy="220" r="1"/>
  </g>

  <!-- ALAS ORIGAMI (4ª Dimensión) - Trasera -->
  <g stroke="#00f0ff" stroke-width="0.5" fill="url(#wing-grad)" filter="url(#glow)">
    <!-- Ala Izquierda -->
    <polygon points="150,180 40,90 70,150"/>
    <polygon points="150,180 70,150 20,180"/>
    <polygon points="150,180 20,180 60,220"/>
    <polygon points="150,180 60,220 90,260"/>
    <!-- Ala Derecha -->
    <polygon points="250,180 360,90 330,150"/>
    <polygon points="250,180 330,150 380,180"/>
    <polygon points="250,180 380,180 340,220"/>
    <polygon points="250,180 340,220 310,260"/>
  </g>

  <!-- TENTÁCULOS DE HUMO / ESPACIO NEGATIVO -->
  <g fill="none" stroke-linecap="round">
    <path d="M 170,240 C 140,300 200,330 160,390" stroke="url(#tentacle-grad)" stroke-width="12" filter="url(#glow)"/>
    <path d="M 230,240 C 260,290 190,340 240,390" stroke="url(#tentacle-grad)" stroke-width="10" filter="url(#glow)"/>
    <path d="M 200,250 C 180,310 220,350 200,400" stroke="url(#tentacle-grad)" stroke-width="16"/>
    <!-- Tentáculos que se disuelven en puntos -->
    <circle cx="165" cy="360" r="3" fill="#00f0ff"/>
    <circle cx="155" cy="380" r="1.5" fill="#00f0ff"/>
    <circle cx="235" cy="370" r="2" fill="#ff00aa"/>
    <circle cx="200" cy="385" r="4" fill="#7209b7"/>
  </g>

  <!-- PATAS ARTICULADAS EN EL TIEMPO -->
  <use href="#clock-leg" x="150" y="230" transform="rotate(15 150 230)"/>
  <use href="#clock-leg" x="250" y="230" transform="scale(-1, 1) translate(-500, 0) rotate(15 250 230)"/>

  <!-- COLA DE MÖBIUS / ESCALERA INFINITA -->
  <g stroke="#ffbe0b" stroke-width="1" fill="none" opacity="0.8">
    <path d="M 200,260 C 280,280 320,350 260,370 C 200,390 100,330 140,280" stroke="url(#face-right)" stroke-width="8" stroke-dasharray="4 2"/>
  </g>

  <!-- CUERPO CENTRAL: AGUJERO NEGRO CON CORAZÓN DE PEZ -->
  <circle cx="200" cy="200" r="55" fill="url(#void)"/>
  
  <!-- Pez Astral nadando en la nada (Órgano interno) -->
  <g transform="translate(200, 200) rotate(-30)">
    <path d="M -20,0 Q 0,-15 20,0 Q 0,15 -20,0 M 20,0 L 35,-10 L 30,0 L 35,10 Z" fill="#00f0ff" opacity="0.8" filter="url(#glow)"/>
    <circle cx="-10" cy="-3" r="2" fill="#ff00aa"/>
  </g>
  <g transform="translate(200, 200) rotate(150) scale(0.7)">
    <path d="M -20,0 Q 0,-15 20,0 Q 0,15 -20,0 M 20,0 L 35,-10 L 30,0 L 35,10 Z" fill="#ff00aa" opacity="0.8" filter="url(#glow)"/>
    <circle cx="-10" cy="-3" r="2" fill="#00f0ff"/>
  </g>

  <!-- EL TOROIDE IMPOSIBLE (Cuerpo Exterior) -->
  <!-- Construido con fragmentos que se solapan de forma ilógica -->
  <g stroke="#10002b" stroke-width="1.5" stroke-linejoin="round">
    <!-- Segmento Superior Izquierdo (Pasa por debajo pero termina arriba) -->
    <path d="M 200,100 L 120,150 L 120,230 L 150,245 L 150,170 L 220,125 Z" fill="url(#face-top)"/>
    
    <!-- Segmento Izquierdo (Conecta el frente con el fondo imposiblemente) -->
    <path d="M 120,150 L 150,170 L 150,250 L 200,280 L 200,310 L 120,260 Z" fill="url(#face-left)"/>
    
    <!-- Segmento Inferior (Giro de Penrose) -->
    <path d="M 150,250 L 230,200 L 260,220 L 200,260 L 200,310 L 280,260 L 280,180 L 250,165 L 250,240 L 170,290 Z" fill="url(#face-right)"/>

    <!-- Segmento Derecho (Cierra el bucle rompiendo la perspectiva) -->
    <path d="M 280,260 L 250,240 L 250,160 L 200,130 L 200,100 L 280,150 Z" fill="url(#face-left)"/>
    
    <!-- Puente Imposible Central (Conecta las caras internas) -->
    <polygon points="150,170 200,140 250,160 230,175 200,160 170,180" fill="url(#face-top)"/>
  </g>

  <!-- ESCALERAS DE ESCHER SOBRE EL CUERPO -->
  <g fill="#ffbe0b" opacity="0.9">
    <polygon points="200,102 208,107 130,155 122,150"/>
    <polygon points="212,110 220,115 142,163 134,158"/>
    <polygon points="122,160 135,168 135,175 122,167"/>
    <polygon points="122,175 135,183 135,190 122,182"/>
    <polygon points="122,190 135,198 135,205 122,197"/>
    <polygon points="122,205 135,213 135,220 122,212"/>
    <polygon points="122,220 135,228 135,235 122,227"/>
  </g>

  <!-- CABEZA / CORONA HIPER-DIMENSIONAL -->
  <!-- No está unida al cuerpo, flota en una relación geométrica -->
  <g transform="translate(200, 75)">
    <!-- Aureola de Teseracto -->
    <polygon points="0,-50 -40,-20 -20,20 20,20 40,-20" fill="none" stroke="#00f0ff" stroke-width="1" stroke-dasharray="3,3"/>
    <polygon points="0,-35 -25,-10 -15,10 15,10 25,-10" fill="none" stroke="#ff00aa" stroke-width="1.5" filter="url(#glow)"/>
    <!-- Líneas de conexión 4D -->
    <line x1="0" y1="-50" x2="0" y2="-35" stroke="#80ffdb" stroke-width="1"/>
    <line x1="-40" y1="-20" x2="-25" y2="-10" stroke="#80ffdb" stroke-width="1"/>
    <line x1="40" y1="-20" x2="25" y2="-10" stroke="#80ffdb" stroke-width="1"/>
    <line x1="-20" y1="20" x2="-15" y2="10" stroke="#80ffdb" stroke-width="1"/>
    <line x1="20" y1="20" x2="15" y2="10" stroke="#80ffdb" stroke-width="1"/>

    <!-- Ojo Principal (Mira hacia adentro y hacia afuera) -->
    <use href="#floating-eye" transform="scale(1.5)"/>
    
    <!-- Cuernos de Humo Sólido -->
    <path d="M -30,-10 C -70,-40 -50,-70 -90,-60 C -60,-30 -80,0 -40,5 Z" fill="url(#face-top)" filter="url(#glow)"/>
    <path d="M 30,-10 C 70,-40 50,-70 90,-60 C 60,-30 80,0 40,5 Z" fill="url(#face-top)" filter="url(#glow)"/>
  </g>

  <!-- MÚLTIPLES OJOS ORBITALES (Rompen la profundidad) -->
  <!-- Este ojo está detrás del ala pero delante del cuerpo -->
  <use href="#floating-eye" x="100" y="130" transform="rotate(-25 100 130) scale(0.8)"/>
  <use href="#floating-eye" x="300" y="130" transform="rotate(25 300 130) scale(0.8)"/>
  <use href="#floating-eye" x="80" y="240" transform="rotate(45 80 240) scale(0.6)"/>
  <use href="#floating-eye" x="320" y="240" transform="rotate(-45 320 240) scale(0.6)"/>
  
  <!-- Ojo vertical en la base de la paradoja -->
  <use href="#floating-eye" x="200" y="295" transform="rotate(90 200 295) scale(0.9)"/>

  <!-- ELEMENTOS DE PARADOJA FINAL (Superposición imposible) -->
  <!-- Una línea de energía que entra por el fondo y sale por el frente sin cruzar el medio -->
  <path d="M 200,200 L 200,130" stroke="#ffbe0b" stroke-width="3" filter="url(#glow)"/>
  <path d="M 200,200 L 260,240" stroke="#00f0ff" stroke-width="3" filter="url(#glow)"/>
  <path d="M 200,200 L 130,240" stroke="#ff00aa" stroke-width="3" filter="url(#glow)"/>
  
  <!-- Cubo pequeño flotando que proyecta sombra hacia arriba -->
  <g transform="translate(200, 340)">
    <polygon points="0,-10 -10,-5 0,0 10,-5" fill="#80ffdb"/>
    <polygon points="-10,-5 -10,7 0,12 0,0" fill="#7209b7"/>
    <polygon points="0,0 0,12 10,7 10,-5" fill="#f72585"/>
  </g>
  
  <!-- Geometría Sagrada Incompleta (El límite de su realidad) -->
  <circle cx="200" cy="200" r="175" fill="none" stroke="url(#wing-grad)" stroke-width="0.5" stroke-dasharray="10 5 2 5"/>
  <circle cx="200" cy="200" r="180" fill="none" stroke="#00f0ff" stroke-width="0.5" stroke-dasharray="1 8"/>
  <polygon points="200,15 360,290 40,290" fill="none" stroke="#ff00aa" stroke-width="0.3" opacity="0.5"/>
  <polygon points="200,385 360,110 40,110" fill="none" stroke="#00f0ff" stroke-width="0.3" opacity="0.5"/>

</svg>