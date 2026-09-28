```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b1055"/>
      <stop offset="50%" stop-color="#7597de"/>
      <stop offset="100%" stop-color="#ffd9a0"/>
    </linearGradient>
    <linearGradient id="wall" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f0d9b5"/>
      <stop offset="100%" stop-color="#c9a876"/>
    </linearGradient>
    <linearGradient id="roof" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e85d75"/>
      <stop offset="100%" stop-color="#b23a52"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff6c9" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fff6c9" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="rock" cx="30%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#8b7bb8"/>
      <stop offset="100%" stop-color="#4a3c6e"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- estrellas -->
  <circle cx="40" cy="40" r="1.5" fill="#fff"/>
  <circle cx="90" cy="20" r="1" fill="#fff"/>
  <circle cx="150" cy="55" r="1.3" fill="#fff"/>
  <circle cx="320" cy="30" r="1.5" fill="#fff"/>
  <circle cx="360" cy="70" r="1" fill="#fff"/>
  <circle cx="270" cy="25" r="1.2" fill="#fff"/>
  <circle cx="60" cy="90" r="1" fill="#fff"/>

  <!-- luna -->
  <circle cx="330" cy="90" r="28" fill="#fff3d0" opacity="0.9"/>
  <circle cx="322" cy="82" r="28" fill="#2b1055" opacity="0.35"/>

  <!-- nubes flotantes -->
  <ellipse cx="90" cy="130" rx="45" ry="14" fill="#ffffff" opacity="0.25"/>
  <ellipse cx="130" cy="120" rx="35" ry="11" fill="#ffffff" opacity="0.2"/>

  <!-- roca flotante base de la casa -->
  <g>
    <path d="M120 260 Q100 300 150 320 Q200 340 260 320 Q310 300 280 265 Q300 250 270 235 Q230 210 180 220 Q130 225 120 260 Z" fill="url(#rock)"/>
    <path d="M130 265 Q160 300 220 300 Q270 298 275 270" fill="none" stroke="#2f2350" stroke-width="2" opacity="0.5"/>
    <ellipse cx="200" cy="330" rx="90" ry="10" fill="#000" opacity="0.15"/>
  </g>

  <!-- raices/cuerdas colgando -->
  <path d="M150 280 Q145 300 140 315" stroke="#5c4a35" stroke-width="2" fill="none" opacity="0.6"/>
  <path d="M250 280 Q258 300 265 318" stroke="#5c4a35" stroke-width="2" fill="none" opacity="0.6"/>
  <path d="M200 300 Q202 315 198 330" stroke="#5c4a35" stroke-width="2" fill="none" opacity="0.5"/>

  <!-- cuerpo principal de la casa, torcida -->
  <g transform="rotate(-4 200 210)">
    <rect x="140" y="160" width="120" height="90" fill="url(#wall)" stroke="#7a5a34" stroke-width="2"/>
    
    <!-- techo curvo asimétrico -->
    <path d="M125 165 Q200 90 285 170 Q260 155 200 150 Q150 150 125 165 Z" fill="url(#roof)" stroke="#7a2438" stroke-width="2"/>
    
    <!-- chimenea torcida -->
    <path d="M225 130 L235 60 L250 62 L242 132 Z" fill="#9a7350" stroke="#5c4429" stroke-width="1.5"/>
    <path d="M232 62 Q245 45 260 55" stroke="#cfcfcf" stroke-width="4" fill="none" opacity="0.6" stroke-linecap="round"/>
    <path d="M240 45 Q255 30 268 42" stroke="#cfcfcf" stroke-width="3" fill="none" opacity="0.4" stroke-linecap="round"/>

    <!-- ventana redonda con luz -->
    <circle cx="200" cy="195" r="26" fill="url(#glow)"/>
    <circle cx="200" cy="195" r="20" fill="#3a2a55" stroke="#7a5a34" stroke-width="3"/>
    <circle cx="200" cy="195" r="20" fill="#ffe9a8" opacity="0.85"/>
    <line x1="200" y1="175" x2="200" y2="215" stroke="#7a5a34" stroke-width="2"/>
    <line x1="180" y1="195" x2="220" y2="195" stroke="#7a5a34" stroke-width="2"/>

    <!-- puerta ovalada torcida -->
    <path d="M150 250 Q150 205 168 200 Q186 205 186 250 Z" fill="#5c3a24" stroke="#3a2414" stroke-width="2"/>
    <circle cx="178" cy="228" r="2.5" fill="#e8c97a"/>

    <!-- ventana pequeña triangular -->
    <path d="M235 210 L250 190 L265 210 Z" fill="#ffe9a8" stroke="#7a5a34" stroke-width="2"/>

    <!-- vigas decorativas -->
    <line x1="140" y1="180" x2="260" y2="180" stroke="#7a5a34" stroke-width="1.5" opacity="0.5"/>
    <line x1="140" y1="230" x2="260" y2="230" stroke="#7a5a34" stroke-width="1.5" opacity="0.5"/>
  </g>

  <!-- torre lateral pequeña con techo cónico, flotando aparte -->
  <g transform="rotate(3 300 220)">
    <rect x="278" y="190" width="40" height="55" fill="#dfc59a" stroke="#7a5a34" stroke-width="2"/>
    <path d="M270 192 L298 150 L326 192 Z" fill="#b23a52" stroke="#7a2438" stroke-width="2"/>
    <circle cx="298" cy="212" r="8" fill="#ffe9a8" stroke="#7a5a34" stroke-width="1.5"/>
    <path d="M278 245 Q285 255 278 265" stroke="#5c4a35" stroke-width="2" fill="none" opacity="0.5"/>
  </g>

  <!-- puente colgante entre roca y torre -->
  <path d="M260 235 Q290 245 278 245" fill="none" stroke="#5c4a35" stroke-width="2" opacity="0.6"/>

  <!-- pajaros -->
  <path d="M60 150 Q65 145 70 150 Q75 145 80 150" stroke="#fff" stroke-width="1.5" fill="none" opacity="0.7"/>
  <path d="M100 130 Q105 125 110 130 Q115 125 120 130" stroke="#fff" stroke-width="1.5" fill="none" opacity="0.6"/>

  <!-- luciernagas alrededor de la casa -->
  <circle cx="160" cy="270" r="2" fill="#fff6c9" opacity="0.8"/>
  <circle cx="255" cy="255" r="1.8" fill="#fff6c9" opacity="0.7"/>
  <circle cx="130" cy="240" r="1.5" fill="#fff6c9" opacity="0.6"/>
  <circle cx="290" cy="230" r="1.6" fill="#fff6c9" opacity="0.65"/>
</svg>
```