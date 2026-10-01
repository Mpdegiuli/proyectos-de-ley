<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="trunkGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#5C3A1E"/>
      <stop offset="30%" stop-color="#D4A056"/>
      <stop offset="50%" stop-color="#FFD700"/>
      <stop offset="70%" stop-color="#D4A056"/>
      <stop offset="100%" stop-color="#5C3A1E"/>
    </linearGradient>
    <linearGradient id="branchGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFD700"/>
      <stop offset="50%" stop-color="#FF8C00"/>
      <stop offset="100%" stop-color="#FF4500"/>
    </linearGradient>
    <radialGradient id="leafGrad">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="30%" stop-color="#FFD700"/>
      <stop offset="70%" stop-color="#FF4500"/>
      <stop offset="100%" stop-color="#FF4500" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <g id="leaf">
      <circle r="7" fill="url(#leafGrad)"/>
      <circle r="2.5" fill="#FFFFFF"/>
    </g>
    <g id="branch3">
      <path d="M0,0 Q3,-15 0,-30" stroke="url(#branchGrad)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <use href="#leaf" transform="translate(0,-30)"/>
    </g>
    <g id="branch2">
      <path d="M0,0 Q5,-20 0,-40" stroke="url(#branchGrad)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <use href="#branch3" transform="translate(0,-40) rotate(-40) scale(0.8)"/>
      <use href="#branch3" transform="translate(0,-40) rotate(0) scale(0.8)"/>
      <use href="#branch3" transform="translate(0,-40) rotate(40) scale(0.8)"/>
      <use href="#leaf" transform="translate(0,-40)"/>
    </g>
    <g id="branch1">
      <path d="M0,0 Q8,-30 0,-60" stroke="url(#branchGrad)" stroke-width="4" fill="none" stroke-linecap="round"/>
      <use href="#branch2" transform="translate(0,-60) rotate(-45) scale(0.8)"/>
      <use href="#branch2" transform="translate(0,-60) rotate(0) scale(0.8)"/>
      <use href="#branch2" transform="translate(0,-60) rotate(45) scale(0.8)"/>
      <use href="#leaf" transform="translate(0,-60)"/>
    </g>
    <g id="branch0">
      <path d="M0,0 Q10,-40 0,-80" stroke="url(#branchGrad)" stroke-width="6" fill="none" stroke-linecap="round"/>
      <use href="#branch1" transform="translate(0,-80) rotate(-45) scale(0.8)"/>
      <use href="#branch1" transform="translate(0,-80) rotate(45) scale(0.8)"/>
      <use href="#leaf" transform="translate(0,-80)"/>
    </g>
    <g id="fruto">
      <circle r="5" fill="#FF69B4"/>
      <ellipse cx="0" cy="0" rx="9" ry="2.5" fill="none" stroke="#FFD700" stroke-width="1" transform="rotate(-30)"/>
    </g>
    <g id="estrella">
      <circle r="1.5" fill="white" opacity="0.7"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="#0a0a1a"/>

  <!-- Estrellas de fondo -->
  <use href="#estrella" transform="translate(20,30)"/>
  <use href="#estrella" transform="translate(80,15)"/>
  <use href="#estrella" transform="translate(350,40)"/>
  <use href="#estrella" transform="translate(370,80)"/>
  <use href="#estrella" transform="translate(300,20)"/>
  <use href="#estrella" transform="translate(150,10)"/>
  <use href="#estrella" transform="translate(250,30)"/>
  <use href="#estrella" transform="translate(40,100)"/>
  <use href="#estrella" transform="translate(380,150)"/>
  <use href="#estrella" transform="translate(60,180)"/>
  <use href="#estrella" transform="translate(330,110)"/>
  <use href="#estrella" transform="translate(120,40)"/>
  <use href="#estrella" transform="translate(280,60)"/>
  <use href="#estrella" transform="translate(200,15)"/>

  <!-- Tronco doble hélice con brillo -->
  <g filter="url(#glow)">
    <path d="M 190 350 C 170 320, 230 300, 200 270 C 170 240, 230 220, 200 190" stroke="url(#trunkGrad)" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M 210 350 C 230 320, 170 300, 200 270 C 230 240, 170 220, 200 190" stroke="url(#trunkGrad)" stroke-width="8" fill="none" stroke-linecap="round"/>
  </g>

  <!-- Raíces -->
  <g filter="url(#glow)">
    <path d="M 190 350 C 170 370, 230 390, 200 400" stroke="url(#trunkGrad)" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path d="M 210 350 C 230 370, 170 390, 200 400" stroke="url(#trunkGrad)" stroke-width="6" fill="none" stroke-linecap="round"/>
  </g>

  <!-- Ojo en el tronco -->
  <g transform="translate(200,280)">
    <ellipse cx="0" cy="0" rx="10" ry="6" fill="white" stroke="#333" stroke-width="1"/>
    <circle cx="0" cy="0" r="3.5" fill="black"/>
    <circle cx="-2" cy="-1" r="1.2" fill="white"/>
  </g>

  <!-- Puerta en la base -->
  <g transform="translate(200,345)">
    <path d="M-8,0 L-8,-15 A8,8 0 0 1 8,-15 L8,0 Z" fill="#4B2E1B" stroke="#8B5A2B" stroke-width="1.5"/>
    <circle cx="5" cy="-8" r="1" fill="#FFD700"/>
  </g>

  <!-- Copa del árbol -->
  <g filter="url(#glow)">
    <use href="#branch0" transform="translate(200,190)"/>
  </g>

  <!-- Frutos colgantes -->
  <use href="#fruto" transform="translate(140,160)"/>
  <use href="#fruto" transform="translate(260,150)"/>
  <use href="#fruto" transform="translate(110,100)"/>
  <use href="#fruto" transform="translate(290,95)"/>
  <use href="#fruto" transform="translate(170,80)"/>
  <use href="#fruto" transform="translate(230,75)"/>
  <use href="#fruto" transform="translate(150,50)"/>
  <use href="#fruto" transform="translate(250,45)"/>

  <!-- Hojas flotantes -->
  <g filter="url(#glow)">
    <use href="#leaf" transform="translate(100,80)"/>
    <use href="#leaf" transform="translate(300,60)"/>
    <use href="#leaf" transform="translate(150,50)"/>
    <use href="#leaf" transform="translate(250,100)"/>
    <use href="#leaf" transform="translate(80,150)"/>
    <use href="#leaf" transform="translate(320,140)"/>
    <use href="#leaf" transform="translate(60,200)"/>
    <use href="#leaf" transform="translate(340,220)"/>
    <use href="#leaf" transform="translate(130,30)"/>
    <use href="#leaf" transform="translate(270,25)"/>
  </g>
</svg>