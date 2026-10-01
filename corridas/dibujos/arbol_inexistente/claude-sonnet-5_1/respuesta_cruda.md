```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="30%" r="80%">
      <stop offset="0%" stop-color="#2b1055"/>
      <stop offset="60%" stop-color="#1a0a33"/>
      <stop offset="100%" stop-color="#0a0518"/>
    </radialGradient>
    <linearGradient id="trunkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4a3b6b"/>
      <stop offset="50%" stop-color="#6b4f9e"/>
      <stop offset="100%" stop-color="#3a2d5c"/>
    </linearGradient>
    <radialGradient id="leafGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7ef9ff"/>
      <stop offset="60%" stop-color="#2dd4da"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </radialGradient>
    <radialGradient id="fruitGlow" cx="40%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#fff4c2"/>
      <stop offset="50%" stop-color="#ffcb3d"/>
      <stop offset="100%" stop-color="#e68a00"/>
    </radialGradient>
    <filter id="blur1"><feGaussianBlur stdDeviation="3"/></filter>
    <filter id="blur2"><feGaussianBlur stdDeviation="6"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- estrellas -->
  <g fill="#ffffff" opacity="0.8">
    <circle cx="30" cy="40" r="1.2"/>
    <circle cx="80" cy="20" r="0.8"/>
    <circle cx="340" cy="50" r="1.5"/>
    <circle cx="370" cy="90" r="1"/>
    <circle cx="20" cy="120" r="1"/>
    <circle cx="300" cy="30" r="0.7"/>
    <circle cx="150" cy="15" r="1"/>
    <circle cx="250" cy="70" r="0.9"/>
    <circle cx="50" cy="80" r="1.1"/>
    <circle cx="380" cy="150" r="0.8"/>
  </g>

  <!-- luna -->
  <circle cx="330" cy="60" r="22" fill="#fff8e1" opacity="0.9" filter="url(#blur1)"/>
  <circle cx="330" cy="60" r="22" fill="#fff8e1"/>
  <circle cx="338" cy="52" r="5" fill="#2b1055" opacity="0.4"/>
  <circle cx="325" cy="68" r="3" fill="#2b1055" opacity="0.3"/>

  <!-- suelo -->
  <ellipse cx="200" cy="370" rx="190" ry="25" fill="#160a2e"/>
  <ellipse cx="200" cy="365" rx="150" ry="14" fill="#241342" opacity="0.7"/>

  <!-- raices -->
  <g stroke="#3a2d5c" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.9">
    <path d="M190 340 Q160 355 120 365"/>
    <path d="M205 340 Q240 358 280 368"/>
    <path d="M198 345 Q195 360 190 372"/>
  </g>

  <!-- tronco espiral -->
  <path d="M185 345 
           C170 310 210 290 190 255
           C175 225 205 205 192 175
           C182 150 200 130 198 110"
        stroke="url(#trunkGrad)" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M185 345 
           C170 310 210 290 190 255
           C175 225 205 205 192 175
           C182 150 200 130 198 110"
        stroke="#9b7fd4" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.5"/>

  <!-- textura espiral del tronco -->
  <g stroke="#2a1f45" stroke-width="2" fill="none" opacity="0.6">
    <path d="M178 330 Q195 325 200 310"/>
    <path d="M183 290 Q200 285 198 270"/>
    <path d="M180 240 Q198 235 195 220"/>
    <path d="M188 190 Q200 185 195 170"/>
  </g>

  <!-- ramas espirales -->
  <g stroke="url(#trunkGrad)" stroke-width="9" fill="none" stroke-linecap="round">
    <path d="M198 110 C 170 100 150 70 160 40 C 165 25 185 20 195 30"/>
    <path d="M198 110 C 230 95 260 100 275 75 C 285 58 270 40 255 45"/>
    <path d="M195 150 C 150 140 120 155 100 130"/>
    <path d="M196 140 C 240 135 270 150 295 135"/>
    <path d="M192 175 C 160 185 140 210 110 205"/>
    <path d="M194 165 C 235 180 260 195 290 185"/>
  </g>

  <!-- hojas cristalinas (poligonos) agrupadas en racimos -->
  <g filter="url(#blur1)" opacity="0.5">
    <circle cx="160" cy="35" r="30" fill="url(#leafGlow)"/>
    <circle cx="265" cy="45" r="28" fill="url(#leafGlow)"/>
    <circle cx="95" cy="120" r="26" fill="url(#leafGlow)"/>
    <circle cx="300" cy="130" r="30" fill="url(#leafGlow)"/>
    <circle cx="100" cy="195" r="24" fill="url(#leafGlow)"/>
    <circle cx="295" cy="180" r="26" fill="url(#leafGlow)"/>
  </g>

  <g fill="url(#leafGlow)" stroke="#e0ffff" stroke-width="0.8">
    <!-- racimo 1 -->
    <polygon points="160,15 170,30 160,45 150,30"/>
    <polygon points="140,25 150,38 140,52 130,38"/>
    <polygon points="180,25 190,38 180,52 170,38"/>
    <polygon points="160,40 170,52 160,64 150,52"/>

    <!-- racimo 2 -->
    <polygon points="265,25 275,38 265,52 255,38"/>
    <polygon points="245,35 255,48 245,60 235,48"/>
    <polygon points="285,35 295,48 285,60 275,48"/>
    <polygon points="265,50 273,60 265,70 257,60"/>

    <!-- racimo 3 -->
    <polygon points="95,100 104,112 95,124 86,112"/>
    <polygon points="78,112 87,124 78,136 69,124"/>
    <polygon points="112,112 121,124 112,136 103,124"/>

    <!-- racimo 4 -->
    <polygon points="300,112 310,124 300,136 290,124"/>
    <polygon points="282,122 291,134 282,146 273,134"/>
    <polygon points="318,122 327,134 318,146 309,134"/>
    <polygon points="300,136 308,146 300,156 292,146"/>

    <!-- racimo 5 -->
    <polygon points="100,178 109,190 100,202 91,190"/>
    <polygon points="84,188 92,200 84,212 76,200"/>
    <polygon points="116,188 124,200 116,212 108,200"/>

    <!-- racimo 6 -->
    <polygon points="295,165 304,177 295,189 286,177"/>
    <polygon points="278,175 286,187 278,199 270,187"/>
    <polygon points="312,175 320,187 312,199 304,187"/>
  </g>

  <!-- frutos luminosos -->
  <g filter="url(#blur2)" opacity="0.6">
    <circle cx="150" cy="35" r="10" fill="url(#fruitGlow)"/>
    <circle cx="270" cy="50" r="9" fill="url(#fruitGlow)"/>
    <circle cx="90" cy="130" r="8" fill="url(#fruitGlow)"/>
    <circle cx="200" cy="200" r="9" fill="url(#fruitGlow)"/>
  </g>
  <g fill="url(#fruitGlow)" stroke="#fff3cc" stroke-width="0.5">
    <circle cx="150" cy="35" r="6"/>
    <circle cx="270" cy="50" r="5.5"/>
    <circle cx="90" cy="130" r="5"/>
    <circle cx="200" cy="200" r="5.5"/>
    <circle cx="115" cy="190" r="4.5"/>
    <circle cx="290" cy="175" r="4.5"/>
  </g>

  <!-- particulas flotantes magicas -->
  <g fill="#aef9ff" opacity="0.7">
    <circle cx="130" cy="90" r="2"/>
    <circle cx="240" cy="110" r="1.5"/>
    <circle cx="70" cy="160" r="1.8"/>
    <circle cx="320" cy="200" r="1.5"/>
    <circle cx="180" cy="280" r="2"/>
    <circle cx="220" cy="260" r="1.3"/>
  </g>
</svg>
```