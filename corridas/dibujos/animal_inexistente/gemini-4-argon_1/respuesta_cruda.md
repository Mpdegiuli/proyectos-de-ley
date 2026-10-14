<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1a103c"/>
      <stop offset="100%" stop-color="#080417"/>
    </radialGradient>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff6b8b"/>
      <stop offset="50%" stop-color="#9b51e0"/>
      <stop offset="100%" stop-color="#2d9cdb"/>
    </linearGradient>
    <linearGradient id="wingGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#56ccf2" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#f2c94c" stop-opacity="0.3"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#6fcf97" stop-opacity="1"/>
      <stop offset="100%" stop-color="#6fcf97" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hornGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f2994a"/>
      <stop offset="100%" stop-color="#f2c94c"/>
    </linearGradient>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>
  
  <!-- Partículas brillantes -->
  <g fill="url(#glow)">
    <circle cx="80" cy="100" r="15"/>
    <circle cx="320" cy="80" r="20"/>
    <circle cx="350" cy="250" r="12"/>
    <circle cx="50" cy="280" r="18"/>
    <circle cx="200" cy="40" r="10"/>
  </g>

  <!-- Sombra en el suelo -->
  <ellipse cx="200" cy="360" rx="110" ry="20" fill="#04020b" opacity="0.8"/>

  <!-- Ala Izquierda (Fondo) -->
  <g transform="translate(150, 180) rotate(-20)">
    <path d="M0,0 C-80,-100 -140,-40 -90,20 C-120,60 -60,100 0,40 Z" fill="url(#wingGrad)" stroke="#56ccf2" stroke-width="2"/>
    <path d="M0,0 C-50,-50 -90,-20 -60,15" fill="none" stroke="#fff" stroke-width="1" opacity="0.5"/>
    <path d="M-60,15 C-80,40 -40,70 0,40" fill="none" stroke="#fff" stroke-width="1" opacity="0.5"/>
  </g>

  <!-- Cola de Pavo Real / Planta -->
  <g stroke-linecap="round" fill="none">
    <path d="M260,260 Q340,220 350,140 Q360,90 320,80" stroke="#2d9cdb" stroke-width="8"/>
    <path d="M260,260 Q360,260 380,190" stroke="#2d9cdb" stroke-width="6"/>
    <circle cx="320" cy="80" r="12" fill="#f2c94c" stroke="#9b51e0" stroke-width="4"/>
    <circle cx="320" cy="80" r="4" fill="#1a103c"/>
    <circle cx="380" cy="190" r="8" fill="#6fcf97" stroke="#2d9cdb" stroke-width="3"/>
  </g>

  <!-- Tentáculos Traseros (Patas) -->
  <path d="M150,280 C120,330 80,320 90,350 C95,365 130,350 160,300" fill="#7b3eb6"/>
  <path d="M240,280 C270,330 310,320 300,350 C295,365 260,350 230,300" fill="#1f7a9c"/>

  <!-- Cuerpo Principal -->
  <path d="M130,170 C100,220 110,300 190,310 C270,320 300,270 270,210 C250,170 220,190 190,170 Z" fill="url(#bodyGrad)"/>

  <!-- Manchas Bioluminiscentes del Cuerpo -->
  <g fill="#6fcf97" opacity="0.8">
    <ellipse cx="220" cy="240" rx="8" ry="12" transform="rotate(20 220 240)"/>
    <ellipse cx="245" cy="255" rx="5" ry="8" transform="rotate(35 245 255)"/>
    <ellipse cx="200" cy="265" rx="6" ry="10" transform="rotate(10 200 265)"/>
    <circle cx="255" cy="230" r="4"/>
  </g>

  <!-- Tentáculos Delanteros (Patas) con Ventosas -->
  <g>
    <path d="M140,270 C110,320 130,370 160,360 C180,355 160,320 175,290" fill="url(#bodyGrad)"/>
    <circle cx="140" cy="340" r="4" fill="#f2c94c"/>
    <circle cx="152" cy="350" r="4" fill="#f2c94c"/>
    <circle cx="135" cy="325" r="3" fill="#f2c94c"/>
    
    <path d="M210,285 C210,340 250,375 270,355 C285,340 250,320 245,285" fill="url(#bodyGrad)"/>
    <circle cx="240" cy="345" r="4" fill="#f2c94c"/>
    <circle cx="255" cy="350" r="4" fill="#f2c94c"/>
    <circle cx="230" cy="330" r="3" fill="#f2c94c"/>
  </g>

  <!-- Ala Derecha (Frente) -->
  <g transform="translate(210, 200) rotate(15)">
    <path d="M0,0 C60,-120 150,-60 100,10 C140,50 80,110 0,50 Z" fill="url(#wingGrad)" stroke="#f2c94c" stroke-width="2"/>
    <path d="M0,0 C40,-60 100,-30 70,10" fill="none" stroke="#fff" stroke-width="1.5" opacity="0.6"/>
    <path d="M70,10 C100,40 60,80 0,50" fill="none" stroke="#fff" stroke-width="1.5" opacity="0.6"/>
    <circle cx="70" cy="-20" r="5" fill="#fff" opacity="0.6"/>
    <circle cx="60" cy="40" r="8" fill="#fff" opacity="0.4"/>
  </g>

  <!-- Cabeza y Cuello Peludo -->
  <path d="M160,120 C110,130 100,190 140,210 C180,230 220,200 210,150 C205,125 180,115 160,120 Z" fill="url(#bodyGrad)"/>
  
  <!-- Melena de Hojas/Plumas -->
  <path d="M120,160 Q90,150 100,130 Q115,140 130,135 Q105,115 125,100 Q140,115 150,120 Q140,90 165,85 Q175,105 180,120 Q195,95 215,105 Q205,125 205,140 Q230,135 235,155 Q215,165 205,170" fill="#ff6b8b" stroke="#9b51e0" stroke-width="2" stroke-linejoin="round"/>

  <!-- Orejas de Mariposa/Zorro -->
  <path d="M135,125 C100,90 70,120 115,150 Z" fill="#9b51e0" stroke="#ff6b8b" stroke-width="3"/>
  <path d="M195,125 C230,90 260,120 215,150 Z" fill="#9b51e0" stroke="#ff6b8b" stroke-width="3"/>
  <path d="M130,130 C110,110 95,125 115,140 Z" fill="#f2c94c"/>
  <path d="M200,130 C220,110 235,125 215,140 Z" fill="#f2c94c"/>

  <!-- Cuernos de Coral -->
  <path d="M150,115 C140,80 110,70 115,50 C120,65 135,65 140,50 C145,65 155,80 160,115 Z" fill="url(#hornGrad)"/>
  <path d="M180,115 C190,80 220,70 215,50 C210,65 195,65 190,50 C185,65 175,80 170,115 Z" fill="url(#hornGrad)"/>

  <!-- Ojos (Tres) -->
  <!-- Ojo Central -->
  <ellipse cx="165" cy="135" rx="12" ry="8" fill="#fff" stroke="#7b3eb6" stroke-width="2"/>
  <circle cx="165" cy="135" r="5" fill="#eb5757"/>
  <circle cx="165" cy="135" r="2" fill="#000"/>
  <circle cx="167" cy="133" r="1.5" fill="#fff"/>

  <!-- Ojo Izquierdo -->
  <circle cx="140" cy="160" r="10" fill="#1a103c" stroke="#ff6b8b" stroke-width="2"/>
  <circle cx="140" cy="160" r="6" fill="#6fcf97"/>
  <ellipse cx="140" cy="160" rx="2" ry="6" fill="#1a103c"/>
  <circle cx="137" cy="157" r="2" fill="#fff"/>

  <!-- Ojo Derecho -->
  <circle cx="190" cy="160" r="10" fill="#1a103c" stroke="#ff6b8b" stroke-width="2"/>
  <circle cx="190" cy="160" r="6" fill="#6fcf97"/>
  <ellipse cx="190" cy="160" rx="2" ry="6" fill="#1a103c"/>
  <circle cx="187" cy="157" r="2" fill="#fff"/>

  <!-- Trompa / Pico / Boca -->
  <path d="M155,175 C160,165 170,165 175,175 C185,195 170,220 155,215 C145,210 155,200 160,195 C165,190 150,185 155,175 Z" fill="#f2994a" stroke="#d97724" stroke-width="2"/>
  
  <!-- Bigotes Flotantes -->
  <path d="M145,180 Q100,170 80,190 Q60,210 70,220" fill="none" stroke="#56ccf2" stroke-width="3" stroke-linecap="round"/>
  <path d="M185,180 Q230,170 250,190 Q270,210 260,220" fill="none" stroke="#56ccf2" stroke-width="3" stroke-linecap="round"/>
  <circle cx="70" cy="220" r="5" fill="#56ccf2"/>
  <circle cx="260" cy="220" r="5" fill="#56ccf2"/>

  <!-- Detalles brillantes adicionales -->
  <circle cx="165" cy="115" r="3" fill="#f2c94c"/>
  <circle cx="125" cy="180" r="2" fill="#fff" opacity="0.8"/>
  <circle cx="205" cy="180" r="2" fill="#fff" opacity="0.8"/>
  <circle cx="120" cy="190" r="3" fill="#6fcf97" opacity="0.6"/>
  <circle cx="210" cy="190" r="3" fill="#6fcf97" opacity="0.6"/>
</svg>