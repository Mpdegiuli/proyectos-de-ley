```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="sky" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#1a0533"/>
      <stop offset="100%" stop-color="#0d1f3c"/>
    </radialGradient>
    <radialGradient id="glow1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff00ff" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#ff00ff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00ffff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00ffff" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur1">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
    <filter id="blur2">
      <feGaussianBlur stdDeviation="6"/>
    </filter>
    <filter id="blur3">
      <feGaussianBlur stdDeviation="1.5"/>
    </filter>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Estrellas -->
  <g fill="white" opacity="0.7">
    <circle cx="30" cy="20" r="1"/>
    <circle cx="80" cy="45" r="0.8"/>
    <circle cx="120" cy="15" r="1.2"/>
    <circle cx="200" cy="30" r="0.9"/>
    <circle cx="270" cy="18" r="1"/>
    <circle cx="340" cy="35" r="0.7"/>
    <circle cx="370" cy="12" r="1.1"/>
    <circle cx="50" cy="70" r="0.8"/>
    <circle cx="310" cy="60" r="0.9"/>
    <circle cx="150" cy="55" r="0.7"/>
    <circle cx="380" cy="80" r="1"/>
    <circle cx="20" cy="110" r="0.8"/>
    <circle cx="390" cy="140" r="0.7"/>
  </g>

  <!-- Suelo luminoso -->
  <ellipse cx="200" cy="390" rx="180" ry="25" fill="#2a0a4a" opacity="0.8"/>
  <ellipse cx="200" cy="385" rx="130" ry="15" fill="#3d0f6b" opacity="0.5"/>

  <!-- Tronco cristalino - hecho de prismas translúcidos -->
  <!-- Tronco principal con facetas -->
  <polygon points="185,370 195,200 205,200 215,370" fill="#4a1a8a" opacity="0.7"/>
  <polygon points="185,370 195,200 200,210 200,375" fill="#7a2adf" opacity="0.5"/>
  <polygon points="215,370 205,200 200,210 200,375" fill="#2a0a5a" opacity="0.6"/>

  <!-- Líneas de cristal en tronco -->
  <line x1="197" y1="200" x2="188" y2="370" stroke="#cc88ff" stroke-width="0.5" opacity="0.6"/>
  <line x1="200" y1="200" x2="200" y2="370" stroke="#ff88ff" stroke-width="0.5" opacity="0.4"/>

  <!-- Raíces cristalinas -->
  <path d="M190,360 Q170,370 150,380 Q140,385 130,382" fill="none" stroke="#7a2adf" stroke-width="3" opacity="0.7"/>
  <path d="M190,360 Q170,370 150,380 Q140,385 130,382" fill="none" stroke="#cc88ff" stroke-width="1" opacity="0.5"/>
  <path d="M195,365 Q180,380 165,390 Q158,395 145,395" fill="none" stroke="#7a2adf" stroke-width="2.5" opacity="0.6"/>
  <path d="M210,360 Q230,370 250,380 Q260,385 272,383" fill="none" stroke="#7a2adf" stroke-width="3" opacity="0.7"/>
  <path d="M210,360 Q230,370 250,380 Q260,385 272,383" fill="none" stroke="#cc88ff" stroke-width="1" opacity="0.5"/>
  <path d="M205,365 Q220,378 238,390 Q248,395 258,394" fill="none" stroke="#7a2adf" stroke-width="2" opacity="0.6"/>

  <!-- RAMAS - formas imposibles, crecen en espiral y se dividen en cristales -->

  <!-- Rama izquierda principal -->
  <path d="M197,280 Q160,260 130,240 Q110,228 95,215" fill="none" stroke="#8833cc" stroke-width="4" opacity="0.8"/>
  <path d="M197,280 Q160,260 130,240 Q110,228 95,215" fill="none" stroke="#ee88ff" stroke-width="1.5" opacity="0.6"/>

  <!-- Sub-ramas izq -->
  <path d="M130,240 Q115,220 105,200 Q100,185 108,170" fill="none" stroke="#8833cc" stroke-width="2.5" opacity="0.7"/>
  <path d="M130,240 Q115,220 105,200 Q100,185 108,170" fill="none" stroke="#ee88ff" stroke-width="1" opacity="0.5"/>
  <path d="M110,225 Q95,218 80,225 Q68,230 60,220" fill="none" stroke="#6622aa" stroke-width="2" opacity="0.7"/>

  <!-- Rama derecha principal -->
  <path d="M203,270 Q240,250 268,228 Q285,215 298,200" fill="none" stroke="#8833cc" stroke-width="4" opacity="0.8"/>
  <path d="M203,270 Q240,250 268,228 Q285,215 298,200" fill="none" stroke="#ee88ff" stroke-width="1.5" opacity="0.6"/>

  <!-- Sub-ramas der -->
  <path d="M268,228 Q280,210 275,190 Q272,175 280,162" fill="none" stroke="#8833cc" stroke-width="2.5" opacity="0.7"/>
  <path d="M268,228 Q280,210 275,190 Q272,175 280,162" fill="none" stroke="#ee88ff" stroke-width="1" opacity="0.5"/>
  <path d="M285,215 Q302,210 315,220 Q325,228 335,218" fill="none" stroke="#6622aa" stroke-width="2" opacity="0.7"/>

  <!-- Rama central hacia arriba -->
  <path d="M200,200 Q198,175 200,155 Q202,138 198,120" fill="none" stroke="#9944dd" stroke-width="3.5" opacity="0.8"/>
  <path d="M200,200 Q198,175 200,155 Q202,138 198,120" fill="none" stroke="#ff99ff" stroke-width="1" opacity="0.5"/>

  <!-- HOJAS IMPOSIBLES - hexágonos cristalinos flotantes que emiten luz -->

  <!-- Cluster izquierdo superior -->
  <g opacity="0.85" filter="url(#blur3)">
    <polygon points="95,215 85,200 90,183 108,178 118,193 113,210" fill="#00ffcc" opacity="0.3"/>
    <polygon points="95,215 85,200 90,183 108,178 118,193 113,210" fill="none" stroke="#00ffcc" stroke-width="1"/>
  </g>
  <polygon points="95,215 85,200 90,183 108,178 118,193 113,210" fill="none" stroke="#88ffee" stroke-width="0.5" opacity="0.8"/>

  <g filter="url(#blur3)">
    <polygon points="108,170 98,156 102,140 118,136 128,150 124,166" fill="#ff00aa" opacity="0.3"/>
    <polygon points="108,170 98,156 102,140 118,136 128,150 124,166" fill="none" stroke="#ff00aa" stroke-width="1"/>
  </g>
  <polygon points="108,170 98,156 102,140 118,136 128,150 124,166" fill="none" stroke="#ff88cc" stroke-width="0.5" opacity="0.8"/>

  <g filter="url(#blur3)">
    <polygon points="60,220 50,206 54,190 70,186 80,200 76,216" fill="#ffff00" opacity="0.25"/>
    <polygon points="60,220 50,206 54,190 70,186 80,200 76,216" fill="none" stroke="#ffff00" stroke-width="1"/>
  </g>

  <!-- Cluster derecho -->
  <g filter="url(#blur3)">
    <polygon points="298,200 288,186 292,169 308,165 318,179 314,196" fill="#00ffcc" opacity="0.3"/>
    <polygon points="298,200 288,186 292,169 308,165 318,179 314,196" fill="none" stroke="#00ffcc" stroke-width="1"/>
  </g>
  <polygon points="298,200 288,186 292,169 308,165 318,179 314,196" fill="none" stroke="#88ffee" stroke-width="0.5" opacity="0.8"/>

  <g filter="url(#blur3)">
    <polygon points="280,162 270,148 274,132 290,128 300,142 296,158" fill="#ff6600" opacity="0.3"/>
    <polygon points="280,162 270,148 274,132 290,128 300,142 296,158" fill="none" stroke="#ff6600" stroke-width="1"/>
  </g>

  <g filter="url(#blur3)">
    <polygon points="335,218 325,204 329,188 345,184 355,198 351,214" fill="#ff00aa" opacity="0.3"/>
    <polygon points="335,218 325,204 329,188 345,184 355,198 351,214" fill="none" stroke="#ff00aa" stroke-width="1"/>
  </g>

  <!-- Cluster central - copa -->
  <g filter="url(#blur3)">
    <polygon points="198,120 183,103 187,83 205,77 220,94 216,114" fill="#aa00ff" opacity="0.35"/>
    <polygon points="198,120 183,103 187,83 205,77 220,94 216,114" fill="none" stroke="#dd66ff" stroke-width="1.2"/>
  </g>
  <polygon points="198,120 183,103 187,83 205,77 220,94 216,114" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>

  <!-- Cristal corona -->
  <g filter="url(#blur3)">
    <polygon points="200,78 188,62 192,44 208,40 220,56 216,74" fill="#ffffff" opacity="0.2"/>
    <polygon points="200,78 188,62 192,44 208,40 220,56 216,74" fill="none" stroke="#ffffff" stroke-width="1.5"/>
  </g>

  <!-- Líneas internas de los cristales (estructura fractal interna) -->
  <line x1="200" y1="78" x2="204" y2="58" stroke="white" stroke-width="0.5" opacity="0.4"/>
  <line x1="188" y1="62" x2="210" y2="56" stroke="white" stroke-width="0.5" opacity="0.3"/>

  <!-- Partículas flotantes / esporas luminosas -->
  <g fill="#ff88ff" filter="url(#blur1)">
    <circle cx="140" cy="160" r="3" opacity="0.7"/>
    <circle cx="260" cy="150" r="2.5" opacity="0.6"/>
    <circle cx="75" cy="175" r="2" opacity="0.5"/>
    <circle cx="330" cy="180" r="3" opacity="0.6"/>
    <circle cx="165" cy="100" r="2" opacity="0.5"/>
    <circle cx="235" cy="110" r="2.5" opacity="0.6"/>
    <circle cx="200" cy="50" r="3" opacity="0.7"/>
    <circle cx="350" cy="140" r="2" opacity="0.4"/>
    <circle cx="55" cy="195" r="2" opacity="0.4"/>
  </g>

  <!-- Halos de luz alrededor de la copa -->
  <ellipse cx="200" cy="90" rx="60" ry="40" fill="url(#glow1)" filter="url(#blur2)"/>
  <ellipse cx="200" cy="90" rx="35" ry="25" fill="url(#glow2)" filter="url(#blur2)"/>

  <!-- Halo izquierdo -->
  <ellipse cx="100" cy="195" rx="40" ry="28" fill="url(#glow2)" filter="url(#blur2)" opacity="0.6"/>

  <!-- Halo derecho -->
  <ellipse cx="300" cy="185" rx="40" ry="28" fill="url(#glow1)" filter="url(#blur2)" opacity="0.5"/>

  <!-- Reflejo en suelo -->
  <ellipse cx="200" cy="388" rx="90" ry="8" fill="#9933ff" opacity="0.2" filter="url(#blur1)"/>

  <!-- Pequeñas runas / símbolos en el tronco -->
  <g stroke="#ff88ff" stroke-width="0.7" fill="none" opacity="0.5">
    <path d="M196,250 L204,250 M200,245 L200,255"/>
    <path d="M196,290 Q200,285 204,290 Q204,296 200,298 Q196,296 196,290"/>
    <path d="M196,320 L200,313 L204,320 L196,320"/>
  </g>
</svg>
```