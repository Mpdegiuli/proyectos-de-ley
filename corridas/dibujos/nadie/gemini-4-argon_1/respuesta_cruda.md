<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#11091c"/>
      <stop offset="60%" stop-color="#06020a"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
    
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffd700"/>
      <stop offset="40%" stop-color="#cca100"/>
      <stop offset="80%" stop-color="#594300"/>
      <stop offset="100%" stop-color="#ffe680"/>
    </linearGradient>

    <linearGradient id="Flesh" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff0055"/>
      <stop offset="50%" stop-color="#99004d"/>
      <stop offset="100%" stop-color="#26001a"/>
    </linearGradient>

    <radialGradient id="nebula" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#00ffcc" stop-opacity="0.9"/>
      <stop offset="30%" stop-color="#7700ff" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#ff00aa" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="IsoTop" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00ffff"/>
      <stop offset="100%" stop-color="#0088ff"/>
    </linearGradient>
    
    <linearGradient id="IsoLeft" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff00aa"/>
      <stop offset="100%" stop-color="#660066"/>
    </linearGradient>
    
    <linearGradient id="IsoRight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a0033"/>
      <stop offset="100%" stop-color="#00001a"/>
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    
    <filter id="warp">
      <feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="6" xChannelSelector="R" yChannelSelector="G"/>
    </filter>

    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#ffffff" stroke-width="0.3" stroke-opacity="0.15"/>
      <circle cx="20" cy="20" r="0.8" fill="#00ffcc" opacity="0.4"/>
    </pattern>

    <g id="cube">
      <polygon points="0,-20 17.32,-10 0,0 -17.32,-10" fill="url(#IsoTop)"/>
      <polygon points="-17.32,-10 0,0 0,20 -17.32,10" fill="url(#IsoLeft)"/>
      <polygon points="0,0 17.32,-10 17.32,10 0,20" fill="url(#IsoRight)"/>
    </g>

    <g id="eye">
      <path d="M-15,0 Q0,-12 15,0 Q0,12 -15,0 Z" fill="#000" stroke="url(#gold)" stroke-width="1.5"/>
      <circle cx="0" cy="0" r="5" fill="#ff0055"/>
      <circle cx="0" cy="0" r="2" fill="#00ffff" filter="url(#glow)"/>
      <circle cx="1.5" cy="-1.5" r="0.8" fill="#fff"/>
    </g>
    
    <clipPath id="jarClip">
      <path d="M130,120 C130,80 270,80 270,120 L285,300 C285,330 115,330 115,300 Z"/>
    </clipPath>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#grid)"/>

  <!-- Geometría Sagrada de Fondo (El Telar del Destino) -->
  <g stroke="url(#gold)" stroke-width="0.4" opacity="0.5" fill="none">
    <circle cx="200" cy="200" r="180" stroke-dasharray="2 6" stroke-width="1.5"/>
    <circle cx="200" cy="200" r="170"/>
    <circle cx="200" cy="200" r="140" stroke-dasharray="10 5 2 5"/>
    <polygon points="200,20 355.8,290 44.2,290"/>
    <polygon points="200,380 355.8,110 44.2,110"/>
    <rect x="73" y="73" width="254" height="254" transform="rotate(45 200 200)"/>
    <!-- Líneas de datos cósmicos -->
    <path d="M 20,200 L 380,200 M 200,20 L 200,380"/>
  </g>

  <!-- Tentáculos Biomecánicos Exteriores -->
  <g filter="url(#warp)" stroke="#000" stroke-width="0.5">
    <path d="M150,310 C90,340 40,280 20,330 C10,350 50,390 90,360 C130,330 160,350 180,320 Z" fill="url(#Flesh)"/>
    <path d="M250,310 C310,340 360,260 390,300 C400,330 340,380 300,350 C260,320 240,350 220,320 Z" fill="url(#Flesh)"/>
    <path d="M120,220 C50,220 60,120 10,140 C-10,150 30,250 115,250 Z" fill="url(#Flesh)"/>
    <path d="M280,200 C350,200 340,100 390,120 C410,130 370,230 285,230 Z" fill="url(#Flesh)"/>
  </g>
  
  <!-- Ventosas luminosas en los tentáculos -->
  <g fill="#00ffcc" filter="url(#glow)" opacity="0.8">
    <circle cx="55" cy="335" r="3"/><circle cx="70" cy="340" r="4"/><circle cx="90" cy="335" r="3.5"/>
    <circle cx="345" cy="315" r="3"/><circle cx="330" cy="325" r="4.5"/><circle cx="310" cy="320" r="3"/>
    <circle cx="50" cy="180" r="3.5"/><circle cx="65" cy="200" r="4"/><circle cx="85" cy="215" r="3"/>
    <circle cx="350" cy="160" r="3.5"/><circle cx="335" cy="180" r="4"/><circle cx="315" cy="195" r="3"/>
  </g>

  <!-- Base del Relicario (Altar Cibernético) -->
  <ellipse cx="200" cy="325" rx="95" ry="25" fill="#1a0f2e" stroke="url(#gold)" stroke-width="3"/>
  <ellipse cx="200" cy="310" rx="85" ry="20" fill="#090414" stroke="#00ffcc" stroke-width="1" stroke-dasharray="8 4"/>
  
  <!-- Sombra Interior del Frasco -->
  <path d="M130,120 C130,80 270,80 270,120 L285,300 C285,330 115,330 115,300 Z" fill="#05000a" opacity="0.8"/>

  <!-- CONTENIDO DEL FRASCO (Cortado por jarClip) -->
  <g clip-path="url(#jarClip)">
    <!-- Fluido Cósmico -->
    <circle cx="200" cy="200" r="150" fill="url(#nebula)" filter="url(#warp)"/>
    
    <!-- Líneas de código genético-digital en el fondo del frasco -->
    <g stroke="#00ffcc" stroke-width="0.5" opacity="0.3" stroke-dasharray="3 1 1 5">
      <line x1="140" y1="80" x2="140" y2="340"/><line x1="150" y1="80" x2="150" y2="340"/>
      <line x1="250" y1="80" x2="250" y2="340"/><line x1="260" y1="80" x2="260" y2="340"/>
    </g>

    <!-- Árbol Hiper-Isométrico (La Mente) -->
    <g transform="translate(200, 190)">
      <use href="#cube" x="0" y="0"/>
      <use href="#cube" x="-17.32" y="-10"/>
      <use href="#cube" x="17.32" y="-10"/>
      <use href="#cube" x="0" y="-20"/>
      <use href="#cube" x="0" y="-40"/>
      <use href="#cube" x="-17.32" y="10"/>
      <use href="#cube" x="17.32" y="10"/>
      <use href="#cube" x="0" y="20"/>
      <!-- Cubos flotantes desprendiéndose -->
      <use href="#cube" x="-34.64" y="-30" transform="scale(0.6)"/>
      <use href="#cube" x="34.64" y="-30" transform="scale(0.6)"/>
      <use href="#cube" x="0" y="-90" transform="scale(0.5)"/>
      <use href="#cube" x="0" y="70" transform="scale(0.7)"/>
    </g>

    <!-- El "Alma" (Pez-Reloj Astral nadando en la geometría) -->
    <g filter="url(#glow)">
      <path d="M160,250 Q200,220 240,260 Q260,270 275,245 Q265,275 240,270 Q200,240 160,250 Z" fill="#ffffff" opacity="0.9"/>
      <path d="M200,240 Q210,210 190,205 Q220,215 215,245 Z" fill="#00ffff" opacity="0.7"/>
      <circle cx="170" cy="248" r="1.5" fill="#ff0055"/>
    </g>

    <!-- Engranajes Líquidos (Se derriten) -->
    <g fill="url(#gold)" opacity="0.85" filter="url(#warp)">
      <path d="M150,130 C170,130 170,150 150,150 C140,150 145,180 140,190 C135,180 140,150 130,150 C110,150 110,130 130,130 Z"/>
      <circle cx="140" cy="140" r="4" fill="#000"/>
      <path d="M250,260 C270,260 270,280 250,280 C245,280 248,310 245,320 C242,310 245,280 240,280 C220,280 220,260 240,260 Z" transform="scale(0.8) translate(60, 50)"/>
    </g>

    <!-- El Ojo Central (Observador Cuántico) -->
    <g transform="translate(200, 125) scale(1.3)">
      <!-- Rayos del ojo -->
      <g stroke="#ff00aa" stroke-width="0.8" opacity="0.6" filter="url(#glow)">
        <line x1="0" y1="0" x2="-40" y2="-20"/><line x1="0" y1="0" x2="40" y2="-20"/>
        <line x1="0" y1="0" x2="-50" y2="0"/><line x1="0" y1="0" x2="50" y2="0"/>
        <line x1="0" y1="0" x2="-30" y2="30"/><line x1="0" y1="0" x2="30" y2="30"/>
      </g>
      <use href="#eye"/>
    </g>

    <!-- Ojos Secundarios (Flotando como burbujas) -->
    <use href="#eye" transform="translate(150, 220) scale(0.6) rotate(-25)"/>
    <use href="#eye" transform="translate(245, 195) scale(0.5) rotate(15)"/>
    <use href="#eye" transform="translate(185, 285) scale(0.7) rotate(5)"/>

    <!--Ondas de energía en la base del líquido -->
    <ellipse cx="200" cy="305" rx="80" ry="15" fill="none" stroke="#ff00aa" stroke-width="2" filter="url(#glow)" opacity="0.6"/>
    <ellipse cx="200" cy="305" rx="60" ry="10" fill="none" stroke="#00ffff" stroke-width="1" filter="url(#glow)" opacity="0.8"/>
  </g>
  <!-- FIN DEL CONTENIDO DEL FRASCO -->

  <!-- Cristal del Frasco (Bordes y Reflejos) -->
  <path d="M130,120 C130,80 270,80 270,120 L285,300 C285,330 115,330 115,300 Z" fill="none" stroke="#00ffff" stroke-width="1.5" opacity="0.5" filter="url(#glow)"/>
  <path d="M130,120 C130,80 270,80 270,120 L285,300 C285,330 115,330 115,300 Z" fill="none" stroke="url(#gold)" stroke-width="3"/>
  
  <!-- Reflejos de cristal hiperrealistas -->
  <path d="M138,125 C138,100 180,95 180,95 C160,105 148,115 146,130 L133,290 C133,290 125,290 125,280 Z" fill="#ffffff" opacity="0.25"/>
  <path d="M262,130 L275,285 C275,295 268,300 268,290 L256,135 Z" fill="#00ffcc" opacity="0.15"/>
  <ellipse cx="200" cy="100" rx="50" ry="8" fill="#ffffff" opacity="0.15"/>

  <!-- Tapa del Relicario (Corona Alquímica) -->
  <g>
    <ellipse cx="200" cy="95" rx="55" ry="12" fill="#1a0f2e" stroke="url(#gold)" stroke-width="2.5"/>
    <path d="M160,95 L170,60 L200,75 L230,60 L240,95 Z" fill="url(#gold)" stroke="#fff" stroke-width="0.5"/>
    <!-- Joya de la Corona -->
    <polygon points="200,35 215,55 200,75 185,55" fill="#ff0055" stroke="url(#gold)" stroke-width="1.5" filter="url(#glow)"/>
    <polygon points="200,35 215,55 200,55" fill="#ff99bb" opacity="0.6"/>
    <!-- Halo de la corona -->
    <circle cx="200" cy="55" r="30" fill="none" stroke="#00ffcc" stroke-width="1" stroke-dasharray="1 4" filter="url(#glow)"/>
  </g>

  <!-- Runas / Datos flotando fuera del frasco -->
  <g fill="#00ffcc" filter="url(#glow)" opacity="0.9">
    <!-- Izquierda -->
    <path d="M70,100 L80,100 L75,110 Z M72,115 L78,115 M75,115 L75,125"/>
    <circle cx="75" cy="130" r="1.5"/>
    <path d="M50,260 L60,260 L55,250 Z M55,260 L55,275 M50,270 L60,270" stroke="#00ffcc" stroke-width="1.5"/>
    <!-- Derecha -->
    <rect x="320" y="95" width="8" height="8" fill="none" stroke="#00ffcc" stroke-width="1.5" transform="rotate(45 324 99)"/>
    <line x1="324" y1="108" x2="324" y2="125" stroke="#00ffcc" stroke-width="1.5"/>
    <circle cx="324" cy="130" r="2" fill="#ff00aa"/>
    <path d="M340,250 C350,250 350,265 340,265 C330,265 330,280 340,280" fill="none" stroke="#00ffcc" stroke-width="1.5"/>
    <circle cx="340" cy="257" r="1.5"/>
    <circle cx="340" cy="273" r="1.5"/>
  </g>

  <!-- Partículas de Polvo Estelar / Esporas -->
  <g fill="#fff" opacity="0.7">
    <circle cx="150" cy="40" r="1" filter="url(#glow)"/>
    <circle cx="260" cy="50" r="1.5" fill="#ffd700" filter="url(#glow)"/>
    <circle cx="100" cy="160" r="1"/>
    <circle cx="300" cy="150" r="2" fill="#ff00aa" filter="url(#glow)"/>
    <circle cx="90" cy="290" r="1.2"/>
    <circle cx="310" cy="290" r="1"/>
    <circle cx="200" cy="365" r="2" fill="#00ffcc" filter="url(#glow)"/>
    <circle cx="160" cy="350" r="1"/>
    <circle cx="240" cy="355" r="1.5"/>
  </g>

  <!-- Marco Viñeta Cibernética -->
  <path d="M 0,0 L 40,0 L 0,40 Z M 400,0 L 360,0 L 400,40 Z M 0,400 L 40,400 L 0,360 Z M 400,400 L 360,400 L 400,360 Z" fill="url(#gold)"/>
  <rect x="5" y="5" width="390" height="390" fill="none" stroke="url(#gold)" stroke-width="1" opacity="0.5"/>
</svg>