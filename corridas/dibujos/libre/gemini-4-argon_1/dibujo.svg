<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <!-- Cielo nocturno y resplandor -->
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#05021a"/>
      <stop offset="35%" stop-color="#150838"/>
      <stop offset="65%" stop-color="#3c115e"/>
      <stop offset="85%" stop-color="#871f69"/>
      <stop offset="100%" stop-color="#d4425c"/>
    </linearGradient>
    
    <!-- Sol/Luna gigante -->
    <linearGradient id="sun" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff3b0"/>
      <stop offset="40%" stop-color="#ffaa5c"/>
      <stop offset="80%" stop-color="#e83f6f"/>
      <stop offset="100%" stop-color="#820b57"/>
    </linearGradient>

    <!-- Agua -->
    <linearGradient id="water" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#6b1557"/>
      <stop offset="30%" stop-color="#2e0a38"/>
      <stop offset="70%" stop-color="#110421"/>
      <stop offset="100%" stop-color="#05010a"/>
    </linearGradient>

    <!-- Montañas lejanas -->
    <linearGradient id="mnt-far" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4e1661"/>
      <stop offset="100%" stop-color="#9e2a63"/>
    </linearGradient>

    <!-- Montañas cercanas -->
    <linearGradient id="mnt-mid" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#28093b"/>
      <stop offset="100%" stop-color="#61144b"/>
    </linearGradient>

    <!-- Filtro de resplandor -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    
    <filter id="soft-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="25" result="blur" />
    </filter>

    <!-- Estrella base -->
    <g id="star">
      <path d="M 0,-4 C 1,-1 1,-1 4,0 C 1,1 1,1 0,4 C -1,1 -1,1 -4,0 C -1,-1 -1,-1 0,-4 Z" fill="#ffffff"/>
    </g>
    
    <!-- Luciérnaga / Orbe -->
    <radialGradient id="orb">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#70ffdf"/>
      <stop offset="100%" stop-color="#70ffdf" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Fondo del cielo -->
  <rect width="400" height="270" fill="url(#sky)"/>

  <!-- Resplandor mágico en el cielo -->
  <circle cx="200" cy="180" r="120" fill="#ff5c77" opacity="0.3" filter="url(#soft-glow)"/>
  <path d="M -50,100 Q 150,20 250,120 T 450,80" fill="none" stroke="#70ffdf" stroke-width="15" opacity="0.15" filter="url(#soft-glow)"/>
  <path d="M -20,60 Q 200,150 300,40 T 420,100" fill="none" stroke="#d05ce3" stroke-width="20" opacity="0.15" filter="url(#soft-glow)"/>

  <!-- Estrellas de fondo (puntos) -->
  <g fill="#ffffff" opacity="0.7">
    <circle cx="30" cy="40" r="1"/>
    <circle cx="80" cy="20" r="1.5"/>
    <circle cx="150" cy="50" r="1"/>
    <circle cx="220" cy="15" r="1"/>
    <circle cx="280" cy="60" r="1.5"/>
    <circle cx="350" cy="30" r="1"/>
    <circle cx="380" cy="80" r="1"/>
    <circle cx="50" cy="100" r="1.5"/>
    <circle cx="120" cy="90" r="0.8"/>
    <circle cx="310" cy="110" r="1"/>
    <circle cx="190" cy="70" r="1.2"/>
    <circle cx="20" cy="150" r="1"/>
    <circle cx="360" cy="140" r="1.5"/>
    <circle cx="90" cy="140" r="0.8"/>
    <circle cx="260" cy="90" r="0.8"/>
  </g>

  <!-- Estrellas brillantes (cruces) -->
  <use href="#star" x="80" y="60" transform="scale(0.8)"/>
  <use href="#star" x="320" y="40" transform="scale(1.2)"/>
  <use href="#star" x="200" y="30" transform="scale(0.6)"/>
  <use href="#star" x="40" y="120" transform="scale(0.7)"/>
  <use href="#star" x="350" y="100" transform="scale(0.9)"/>
  <use href="#star" x="150" y="25" transform="scale(1)"/>

  <!-- Planeta / Luna lejana -->
  <circle cx="320" cy="80" r="12" fill="#150838"/>
  <path d="M 320,68 A 12,12 0 0,1 320,92 A 8,12 0 0,0 320,68 Z" fill="#ffaa5c" opacity="0.8" transform="rotate(-30 320 80)"/>

  <!-- El Gran Sol / Luna -->
  <circle cx="200" cy="195" r="75" fill="url(#sun)" filter="url(#glow)"/>
  
  <!-- Anillos cósmicos alrededor del sol -->
  <ellipse cx="200" cy="195" rx="110" ry="15" fill="none" stroke="#ffcf96" stroke-width="1" opacity="0.4" transform="rotate(-12 200 195)"/>
  <ellipse cx="200" cy="195" rx="130" ry="20" fill="none" stroke="#ff5c77" stroke-width="0.5" opacity="0.3" transform="rotate(-12 200 195)"/>

  <!-- Nubes lejanas -->
  <g fill="#230733" opacity="0.5">
    <path d="M 20,180 Q 40,170 60,178 T 100,175 T 130,182 L 20,182 Z"/>
    <path d="M 270,150 Q 290,140 310,148 T 360,145 T 390,152 L 270,152 Z"/>
    <path d="M 110,130 Q 130,122 150,128 T 190,126 L 110,130 Z"/>
  </g>

  <!-- Montañas Lejanas -->
  <path d="M 0,270 L 0,200 L 40,170 L 85,210 L 130,160 L 170,220 L 190,205 L 220,235 L 270,150 L 320,200 L 350,175 L 400,210 L 400,270 Z" fill="url(#mnt-far)"/>

  <!-- Niebla entre montañas -->
  <rect x="0" y="210" width="400" height="60" fill="url(#sky)" opacity="0.3"/>

  <!-- Montañas Medias -->
  <path d="M 0,270 L 0,220 L 65,180 L 110,230 L 145,205 L 180,250 L 230,240 L 260,190 L 310,230 L 340,195 L 375,225 L 400,205 L 400,270 Z" fill="url(#mnt-mid)"/>

  <!-- El Mar / Lago -->
  <rect x="0" y="265" width="400" height="135" fill="url(#water)"/>

  <!-- Reflejo del Sol en el agua -->
  <g opacity="0.8" filter="url(#glow)">
    <ellipse cx="200" cy="270" rx="65" ry="3" fill="#ffaa5c"/>
    <ellipse cx="200" cy="277" rx="58" ry="2.5" fill="#ffaa5c"/>
    <ellipse cx="200" cy="284" rx="50" ry="2" fill="#ff8866"/>
    <ellipse cx="200" cy="290" rx="45" ry="2" fill="#ff8866"/>
    <ellipse cx="200" cy="296" rx="38" ry="1.5" fill="#e83f6f"/>
    <ellipse cx="200" cy="302" rx="32" ry="1.5" fill="#e83f6f"/>
    <ellipse cx="200" cy="308" rx="25" ry="1.5" fill="#e83f6f"/>
    <ellipse cx="200" cy="315" rx="20" ry="1" fill="#b51a63"/>
    <ellipse cx="200" cy="322" rx="15" ry="1" fill="#b51a63"/>
    <ellipse cx="200" cy="330" rx="10" ry="1" fill="#b51a63"/>
    <ellipse cx="200" cy="338" rx="5" ry="0.5" fill="#b51a63"/>
  </g>
  
  <!-- Olas oscuras superpuestas al reflejo para dar textura -->
  <g fill="#2e0a38" opacity="0.7">
    <ellipse cx="170" cy="273" rx="30" ry="1.5"/>
    <ellipse cx="230" cy="280" rx="25" ry="1.5"/>
    <ellipse cx="180" cy="287" rx="20" ry="1.5"/>
    <ellipse cx="220" cy="293" rx="25" ry="1"/>
    <ellipse cx="185" cy="300" rx="15" ry="1"/>
    <ellipse cx="210" cy="305" rx="18" ry="1.5"/>
    <ellipse cx="190" cy="312" rx="12" ry="1"/>
    <ellipse cx="205" cy="319" rx="10" ry="1"/>
  </g>

  <!-- Líneas de brillo en el agua (lejanas) -->
  <g stroke="#ff5c77" stroke-width="0.5" opacity="0.5">
    <line x1="50" y1="275" x2="90" y2="275"/>
    <line x1="310" y1="272" x2="360" y2="272"/>
    <line x1="80" y1="285" x2="110" y2="285"/>
    <line x1="280" y1="288" x2="320" y2="288"/>
    <line x1="30" y1="295" x2="70" y2="295"/>
    <line x1="340" y1="300" x2="380" y2="300"/>
    <line x1="100" y1="310" x2="140" y2="310"/>
    <line x1="260" y1="315" x2="290" y2="315"/>
  </g>

  <!-- Costa / Rocas en primer plano (Siluetas) -->
  <!-- Izquierda -->
  <path d="M 0,255 L 35,258 L 65,265 L 0,268 Z" fill="#160321"/>
  <path d="M 0,290 L 50,295 L 85,310 L 40,320 L 0,325 Z" fill="#0c0214"/>
  <!-- Derecha -->
  <path d="M 400,250 L 340,258 L 310,265 L 400,268 Z" fill="#160321"/>
  <path d="M 400,320 L 330,330 L 290,345 L 310,360 L 400,370 Z" fill="#09010f"/>

  <!-- Acantilado principal en primer plano (Izquierda inferior) -->
  <path d="M 0,350 Q 80,340 120,365 T 180,400 L 0,400 Z" fill="#05010a"/>
  
  <!-- Árbol retorcido en el acantilado -->
  <path d="M 60,360 Q 65,330 55,310 Q 45,290 65,270 Q 75,260 90,255 Q 70,265 65,280 Q 60,295 70,310 Q 85,290 105,285 Q 85,295 75,315 Q 70,335 75,360 Z" fill="#05010a"/>
  <!-- Ramas extra -->
  <path d="M 58,300 Q 40,295 30,280 Q 45,290 56,295 Z" fill="#05010a"/>
  <path d="M 65,275 Q 55,260 60,245 Q 60,260 68,272 Z" fill="#05010a"/>
  <!-- Follaje mágico (Brillante) -->
  <g fill="#70ffdf" opacity="0.8" filter="url(#glow)">
    <circle cx="92" cy="253" r="3"/>
    <circle cx="85" cy="258" r="2"/>
    <circle cx="107" cy="284" r="2.5"/>
    <circle cx="98" cy="288" r="1.5"/>
    <circle cx="28" cy="278" r="2"/>
    <circle cx="35" cy="283" r="1.5"/>
    <circle cx="60" cy="243" r="2.5"/>
    <circle cx="55" cy="250" r="1.5"/>
    <circle cx="75" cy="265" r="2"/>
  </g>

  <!-- El Viajero y el Bote (Centro-Derecha en el agua) -->
  <g transform="translate(230, 325) scale(0.9)">
    <!-- Sombra/Reflejo del bote -->
    <path d="M -35,5 Q 0,12 35,5 Q 20,18 -20,18 Z" fill="#020005" opacity="0.6"/>
    <!-- Bote -->
    <path d="M -40,0 Q -35,10 0,10 Q 35,10 45,-5 Q 30,2 0,2 Q -30,2 -40,0 Z" fill="#05010a"/>
    <!-- Viajero (Silueta con capa) -->
    <path d="M -10,3 Q -8,-15 -2,-22 C -2,-25 3,-25 3,-22 Q 8,-15 5,3 Z" fill="#05010a"/>
    <!-- Cabeza/Sombrero -->
    <circle cx="0" cy="-26" r="3.5" fill="#05010a"/>
    <path d="M -8,-24 Q 0,-29 8,-24 Q 0,-26 -8,-24 Z" fill="#05010a"/>
    <!-- Vara / Remo -->
    <line x1="3" y1="-15" x2="22" y2="-28" stroke="#05010a" stroke-width="1.5"/>
    <!-- Farol mágico colgando de la vara -->
    <line x1="21" y1="-27" x2="21" y2="-20" stroke="#05010a" stroke-width="0.8"/>
    <circle cx="21" cy="-18" r="6" fill="url(#orb)" filter="url(#glow)"/>
    <circle cx="21" cy="-18" r="2" fill="#ffffff"/>
    <!-- Reflejo de la luz del farol en el agua -->
    <ellipse cx="21" cy="8" rx="8" ry="2" fill="#70ffdf" opacity="0.4" filter="url(#glow)"/>
    <ellipse cx="21" cy="12" rx="4" ry="1" fill="#70ffdf" opacity="0.2"/>
  </g>

  <!-- Aves volando hacia el sol -->
  <g fill="none" stroke="#1a0526" stroke-width="1.2" stroke-linecap="round">
    <path d="M 140,190 Q 144,185 148,189 Q 152,185 156,190"/>
    <path d="M 155,180 Q 158,176 161,179 Q 164,176 167,180"/>
    <path d="M 130,175 Q 133,172 136,174 Q 139,172 142,175" stroke-width="1"/>
    <path d="M 165,172 Q 167,169 169,171 Q 171,169 173,172" stroke-width="0.8"/>
    <path d="M 240,165 Q 243,161 246,164 Q 249,161 252,165" stroke-width="1"/>
    <path d="M 255,158 Q 257,155 259,157 Q 261,155 263,158" stroke-width="0.8"/>
  </g>

  <!-- Luciérnagas / Partículas de magia flotando -->
  <g>
    <circle cx="100" cy="350" r="5" fill="url(#orb)"/>
    <circle cx="100" cy="350" r="1" fill="#fff"/>
    
    <circle cx="150" cy="320" r="4" fill="url(#orb)"/>
    <circle cx="150" cy="320" r="0.8" fill="#fff"/>

    <circle cx="80" cy="290" r="6" fill="url(#orb)"/>
    <circle cx="80" cy="290" r="1.2" fill="#fff"/>

    <circle cx="120" cy="260" r="3" fill="url(#orb)"/>
    <circle cx="120" cy="260" r="0.5" fill="#fff"/>

    <circle cx="280" cy="350" r="5" fill="url(#orb)"/>
    <circle cx="280" cy="350" r="1" fill="#fff"/>

    <circle cx="340" cy="300" r="7" fill="url(#orb)"/>
    <circle cx="340" cy="300" r="1.5" fill="#fff"/>

    <circle cx="310" cy="240" r="4" fill="url(#orb)"/>
    <circle cx="310" cy="240" r="0.8" fill="#fff"/>
    
    <circle cx="210" cy="280" r="3" fill="url(#orb)"/>
    <circle cx="210" cy="280" r="0.6" fill="#fff"/>
  </g>

  <!-- Estrella fugaz -->
  <path d="M 250,40 L 180,90" stroke="url(#sky)" stroke-width="2" opacity="0.5"/>
  <linearGradient id="meteor" x1="100%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="80%" stop-color="#70ffdf" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="1"/>
  </linearGradient>
  <line x1="270" y1="25" x2="210" y2="75" stroke="url(#meteor)" stroke-width="1.5" stroke-linecap="round" filter="url(#glow)"/>
  <circle cx="210" cy="75" r="1.5" fill="#ffffff" filter="url(#glow)"/>

  <!-- Silueta de vegetación en primerísimo plano (Esquina inferior derecha) -->
  <g fill="#020005">
    <path d="M 350,400 Q 360,370 380,350 Q 365,375 360,400 Z"/>
    <path d="M 365,400 Q 375,380 395,365 Q 380,385 375,400 Z"/>
    <path d="M 340,400 Q 345,380 330,360 Q 350,375 348,400 Z"/>
    <path d="M 30,400 Q 40,375 20,355 Q 45,375 40,400 Z"/>
    <path d="M 45,400 Q 60,380 75,370 Q 55,385 52,400 Z"/>
  </g>

  <!-- Marco sutil / Viñeta oscura en los bordes -->
  <radialGradient id="vignette" cx="50%" cy="50%" r="50%">
    <stop offset="80%" stop-color="#000000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#020005" stop-opacity="0.6"/>
  </radialGradient>
  <rect width="400" height="400" fill="url(#vignette)" pointer-events="none"/>

</svg>