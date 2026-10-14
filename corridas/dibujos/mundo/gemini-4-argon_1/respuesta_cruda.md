<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <!-- Fondo Cósmico / Digital -->
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#111026"/>
      <stop offset="60%" stop-color="#080711"/>
      <stop offset="100%" stop-color="#020205"/>
    </radialGradient>

    <!-- El calor antropogénico / Crisis climática -->
    <linearGradient id="fire" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff2a00" stop-opacity="0.8"/>
      <stop offset="40%" stop-color="#ff7b00" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#111026" stop-opacity="0"/>
    </linearGradient>

    <!-- Esperanza / Renacimiento biológico -->
    <radialGradient id="life" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#00ffcc"/>
      <stop offset="70%" stop-color="#008866" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#008866" stop-opacity="0"/>
    </radialGradient>

    <!-- Red de datos / Hiperconexión -->
    <linearGradient id="cyber" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0055ff" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="#00ddff" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#aa00ff" stop-opacity="0.9"/>
    </linearGradient>

    <!-- Sombra interna del planeta -->
    <radialGradient id="planet-shadow" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#1a2436" stop-opacity="0"/>
      <stop offset="70%" stop-color="#070a10" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.95"/>
    </radialGradient>

    <!-- Filtro de resplandor (Glow) -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    
    <filter id="heavy-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12" result="blur1" />
      <feGaussianBlur stdDeviation="25" result="blur2" />
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Recorte del Globo -->
    <clipPath id="globe-clip">
      <circle cx="200" cy="200" r="130"/>
    </clipPath>

    <!-- Recorte para el efecto Glitch -->
    <clipPath id="glitch-clip">
      <rect x="60" y="120" width="280" height="8"/>
      <rect x="60" y="185" width="280" height="15"/>
      <rect x="60" y="260" width="280" height="5"/>
    </clipPath>
  </defs>

  <!-- 1. EL VACÍO Y EL RUIDO DE FONDO -->
  <rect width="400" height="400" fill="url(#bg)"/>
  
  <!-- Estrellas / Píxeles muertos -->
  <g fill="#ffffff" opacity="0.4">
    <circle cx="45" cy="60" r="1"/>
    <circle cx="350" cy="40" r="1.5" fill="#00ddff"/>
    <circle cx="320" cy="360" r="1"/>
    <circle cx="80" cy="340" r="0.8"/>
    <circle cx="20" cy="200" r="1.2" fill="#ff5500"/>
    <circle cx="380" cy="220" r="1"/>
    <rect x="120" y="30" width="2" height="2" fill="#00ffcc"/>
    <rect x="280" y="370" width="3" height="1" fill="#ff0055"/>
    <rect x="35" y="290" width="1" height="4" fill="#00ddff"/>
  </g>

  <!-- 2. EL AURA DEL MUNDO (Calor vs Datos) -->
  <!-- Resplandor de crisis climática (Arriba/Derecha) -->
  <circle cx="215" cy="185" r="135" fill="none" stroke="#ff3300" stroke-width="8" opacity="0.5" filter="url(#heavy-glow)"/>
  <!-- Resplandor tecnológico (Abajo/Izquierda) -->
  <circle cx="185" cy="215" r="135" fill="none" stroke="#0088ff" stroke-width="6" opacity="0.5" filter="url(#heavy-glow)"/>

  <!-- 3. EL PLANETA (Contenido recortado) -->
  <g clip-path="url(#globe-clip)">
    <!-- Base oceánica oscura -->
    <circle cx="200" cy="200" r="130" fill="#0c1624"/>

    <!-- Latitud / Longitud (La ilusión de control) -->
    <g stroke="#1a3350" stroke-width="0.5" fill="none">
      <circle cx="200" cy="200" r="100"/>
      <circle cx="200" cy="200" r="70"/>
      <circle cx="200" cy="200" r="40"/>
      <ellipse cx="200" cy="200" rx="130" ry="60"/>
      <ellipse cx="200" cy="200" rx="60" ry="130"/>
      <line x1="70" y1="200" x2="330" y2="200"/>
      <line x1="200" y1="70" x2="200" y2="330"/>
    </g>

    <!-- Hemisferio Norte: Incendio y Fiebre -->
    <rect x="70" y="70" width="260" height="180" fill="url(#fire)"/>
    
    <!-- Sol Artificial / Calentamiento -->
    <circle cx="250" cy="110" r="45" fill="#ff4400" opacity="0.6" filter="url(#heavy-glow)"/>
    <circle cx="250" cy="110" r="20" fill="#ffaa00" opacity="0.8" filter="url(#glow)"/>

    <!-- Siluetas de hiper-urbanización y decadencia (El peso del concreto) -->
    <path d="M60,230 L90,230 L90,170 L105,170 L105,210 L115,210 L115,140 L135,140 L135,190 L145,190 L145,160 L160,160 L160,220 L180,220 L180,120 L205,120 L205,180 L215,180 L215,150 L230,150 L230,200 L245,200 L245,130 L265,130 L265,175 L280,175 L280,155 L295,155 L295,215 L310,215 L310,185 L340,185 L340,260 L60,260 Z" fill="#07080d"/>
    
    <!-- Ventanas encendidas / Aislamiento en la multitud -->
    <g fill="#ff9900" opacity="0.7">
      <rect x="120" y="150" width="2" height="4"/>
      <rect x="125" y="150" width="2" height="4"/>
      <rect x="120" y="165" width="2" height="2"/>
      <rect x="185" y="130" width="12" height="1"/>
      <rect x="185" y="135" width="12" height="1"/>
      <rect x="185" y="140" width="12" height="1"/>
      <rect x="250" y="140" width="3" height="8" fill="#00ddff"/>
      <rect x="258" y="150" width="3" height="8" fill="#ff0055"/>
    </g>

    <!-- Hemisferio Sur: La Malla Digital y Extractivismo -->
    <g stroke="url(#cyber)" stroke-width="1.2" opacity="0.7" fill="none">
      <path d="M70,250 L130,220 L180,270 L250,210 L310,260 L330,220"/>
      <path d="M90,300 L130,220 L160,310 L200,260 L250,210 L270,300"/>
      <path d="M130,220 L200,260 L240,320 L310,260"/>
      <path d="M180,270 L160,310 L240,320 L270,300"/>
    </g>
    
    <!-- Nodos de datos -->
    <g fill="#00ffff" filter="url(#glow)">
      <circle cx="130" cy="220" r="3"/>
      <circle cx="180" cy="270" r="2.5"/>
      <circle cx="250" cy="210" r="4"/>
      <circle cx="200" cy="260" r="3"/>
      <circle cx="310" cy="260" r="2"/>
      <circle cx="160" cy="310" r="2.5"/>
      <circle cx="270" cy="300" r="3"/>
    </g>

    <!-- Sombra volumétrica del planeta -->
    <circle cx="200" cy="200" r="130" fill="url(#planet-shadow)"/>

    <!-- LA GRIETA (Polarización, fractura social y ecológica) -->
    <path d="M190,65 L205,120 L175,165 L215,205 L185,255 L210,300 L195,335" fill="none" stroke="#000000" stroke-width="8" opacity="0.8"/>
    <path d="M190,65 L205,120 L175,165 L215,205 L185,255 L210,300 L195,335" fill="none" stroke="#ff0055" stroke-width="2" filter="url(#glow)"/>
    
    <!-- 4. EL BROTE (Resiliencia, conciencia, vida que se abre paso) -->
    <!-- Crece exactamente desde el centro de la fractura -->
    <g filter="url(#glow)">
      <path d="M215,205 C200,190 185,165 205,140" fill="none" stroke="#00ffcc" stroke-width="2.5" stroke-linecap="round"/>
      <!-- Hoja izquierda -->
      <path d="M198,175 C180,175 175,160 190,160 C198,160 198,175 198,175 Z" fill="#00ffcc"/>
      <!-- Hoja derecha / Brote luminoso -->
      <path d="M205,140 C220,135 225,150 210,155 C200,158 205,140 205,140 Z" fill="#ffffff"/>
      <circle cx="208" cy="142" r="15" fill="url(#life)"/>
    </g>
  </g>

  <!-- 5. EFECTO GLITCH (Crisis de la verdad, posverdad, ruido mediático) -->
  <!-- Desplazamiento de rebanadas del mundo -->
  <g clip-path="url(#glitch-clip)">
    <g transform="translate(-8, 0)">
      <circle cx="200" cy="200" r="130" fill="#00ffff" opacity="0.3" filter="url(#glow)"/>
      <path d="M60,230 L115,140 L180,120 L245,130 L340,185 L340,260 L60,260 Z" fill="#ff0055" opacity="0.5"/>
    </g>
    <g transform="translate(8, 0)">
      <circle cx="200" cy="200" r="130" fill="none" stroke="#ff0055" stroke-width="4" opacity="0.8"/>
    </g>
  </g>
  <!-- Líneas de corrupción digital -->
  <rect x="55" y="185" width="40" height="2" fill="#00ffcc" opacity="0.8"/>
  <rect x="290" y="124" width="50" height="1.5" fill="#ff0055" opacity="0.8"/>
  <rect x="150" y="262" width="120" height="1" fill="#ffffff" opacity="0.9"/>

  <!-- 6. ÓRBITAS EXTERNAS (Vigilancia, IA, Satélites, Hiper-abstracción) -->
  <g fill="none" stroke-linecap="round">
    <!-- Órbita 1: Datos Rápidos -->
    <ellipse cx="200" cy="200" rx="175" ry="55" transform="rotate(-25 200 200)" stroke="url(#cyber)" stroke-width="1.5" stroke-dasharray="10 5 2 5" filter="url(#glow)"/>
    
    <!-- Órbita 2: El Ojo / IA -->
    <ellipse cx="200" cy="200" rx="165" ry="70" transform="rotate(35 200 200)" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="4 8" opacity="0.6"/>
    
    <!-- Órbita 3: Tensión Geopolítica -->
    <ellipse cx="200" cy="200" rx="150" ry="150" stroke="#ff0055" stroke-width="0.8" stroke-dasharray="1 15" opacity="0.7"/>
  </g>

  <!-- Satélites / Nodos de vigilancia / Conciencia externa -->
  <g filter="url(#glow)">
    <!-- Nodo IA (Arriba derecha) -->
    <circle cx="348" cy="131" r="4" fill="#ffffff"/>
    <circle cx="348" cy="131" r="8" fill="none" stroke="#00ddff" stroke-width="1"/>
    <line x1="348" y1="131" x2="260" y2="170" stroke="#00ddff" stroke-width="0.5" stroke-dasharray="2 2" opacity="0.6"/>

    <!-- Nodo Vigilancia (Abajo izquierda) -->
    <circle cx="52" cy="269" r="3" fill="#ff0055"/>
    <line x1="52" y1="269" x2="130" y2="220" stroke="#ff0055" stroke-width="0.5" opacity="0.5"/>

    <!-- Flujo de datos escapando al espacio (Abajo derecha) -->
    <g transform="translate(310, 290) rotate(35)">
      <rect x="0" y="0" width="8" height="2" fill="#00ffcc"/>
      <rect x="12" y="-4" width="4" height="2" fill="#00ffcc" opacity="0.7"/>
      <rect x="20" y="2" width="12" height="2" fill="#00ffcc" opacity="0.4"/>
    </g>
  </g>

  <!-- 7. EL BORDE DEL MUNDO (Contención frágil) -->
  <circle cx="200" cy="200" r="130" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.2"/>
  <circle cx="200" cy="200" r="130.5" fill="none" stroke="#00ffcc" stroke-width="0.5" stroke-dasharray="50 150 20 80" opacity="0.6"/>
  
  <!-- Pequeña chispa de vida rompiendo el límite hacia afuera -->
  <circle cx="200" cy="68" r="1.5" fill="#00ffcc" filter="url(#glow)"/>
</svg>