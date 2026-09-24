<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#87CEEB"/>
      <stop offset="100%" stop-color="#FFFACD"/>
    </linearGradient>
    <radialGradient id="globeGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4A90E2"/>
      <stop offset="100%" stop-color="#1B3A6B"/>
    </radialGradient>
    <linearGradient id="landGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#56C456"/>
      <stop offset="100%" stop-color="#2E8B57"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bgGrad)"/>

  <!-- Sol -->
  <circle cx="350" cy="50" r="28" fill="#FFD700" filter="url(#glow)"/>
  <g stroke="#FFD700" stroke-width="3" stroke-linecap="round">
    <line x1="350" y1="10" x2="350" y2="20"/>
    <line x1="350" y1="80" x2="350" y2="90"/>
    <line x1="310" y1="50" x2="320" y2="50"/>
    <line x1="380" y1="50" x2="390" y2="50"/>
    <line x1="322" y1="22" x2="329" y2="29"/>
    <line x1="371" y1="71" x2="378" y2="78"/>
    <line x1="378" y1="22" x2="371" y2="29"/>
    <line x1="329" y1="71" x2="322" y2="78"/>
  </g>

  <!-- Nubes -->
  <g fill="#FFFFFF" opacity="0.8">
    <ellipse cx="80" cy="90" rx="45" ry="20"/>
    <ellipse cx="120" cy="80" rx="35" ry="18"/>
    <ellipse cx="55" cy="80" rx="25" ry="15"/>
    <ellipse cx="320" cy="140" rx="40" ry="18"/>
    <ellipse cx="360" cy="135" rx="30" ry="15"/>
  </g>

  <!-- Red de conexiones (líneas) -->
  <g stroke="#7F8C8D" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.6">
    <line x1="30" y1="50" x2="140" y2="160"/>
    <line x1="370" y1="50" x2="260" y2="160"/>
    <line x1="30" y1="350" x2="140" y2="240"/>
    <line x1="370" y1="350" x2="260" y2="240"/>
    <line x1="200" y1="20" x2="200" y2="80"/>
    <line x1="200" y1="380" x2="200" y2="320"/>
    <line x1="20" y1="200" x2="80" y2="200"/>
    <line x1="380" y1="200" x2="320" y2="200"/>
  </g>

  <!-- Globo terráqueo -->
  <circle cx="200" cy="200" r="120" fill="url(#globeGrad)" stroke="#2C3E50" stroke-width="3"/>
  
  <!-- Líneas de latitud y longitud -->
  <g stroke="#FFFFFF" stroke-width="0.8" opacity="0.25" fill="none">
    <ellipse cx="200" cy="200" rx="120" ry="40"/>
    <ellipse cx="200" cy="200" rx="120" ry="80"/>
    <ellipse cx="200" cy="160" rx="60" ry="25"/>
    <ellipse cx="200" cy="240" rx="60" ry="25"/>
    <path d="M 200 80 Q 170 200 200 320"/>
    <path d="M 200 80 Q 230 200 200 320"/>
    <path d="M 80 200 Q 200 230 320 200"/>
    <path d="M 80 200 Q 200 170 320 200"/>
  </g>

  <!-- Continentes -->
  <g fill="url(#landGrad)" stroke="#1E5B2E" stroke-width="1">
    <!-- Norteamérica -->
    <path d="M 130 110 Q 155 95 175 105 Q 195 115 185 135 Q 170 145 165 165 Q 150 155 140 130 Z"/>
    <!-- Sudamérica -->
    <path d="M 165 175 Q 185 190 190 210 Q 195 235 180 260 Q 170 250 160 230 Q 155 200 165 175 Z"/>
    <!-- Europa -->
    <path d="M 215 110 Q 235 105 250 115 Q 260 125 250 140 Q 235 135 220 130 Z"/>
    <!-- África -->
    <path d="M 225 150 Q 250 160 260 190 Q 265 220 250 250 Q 240 230 235 200 Q 225 175 225 150 Z"/>
    <!-- Asia -->
    <path d="M 255 115 Q 290 100 320 120 Q 335 140 315 160 Q 290 165 270 150 Q 260 135 255 115 Z"/>
    <!-- Australia -->
    <path d="M 300 205 Q 320 200 330 215 Q 330 230 315 235 Q 300 225 300 205 Z"/>
    <!-- Groenlandia -->
    <path d="M 175 80 Q 195 70 205 85 Q 195 95 180 90 Z"/>
  </g>

  <!-- Nodos de red -->
  <g fill="#E74C3C" stroke="#FFFFFF" stroke-width="1.5">
    <circle cx="30" cy="50" r="6"/>
    <circle cx="370" cy="50" r="6"/>
    <circle cx="30" cy="350" r="6"/>
    <circle cx="370" cy="350" r="6"/>
    <circle cx="200" cy="20" r="6"/>
    <circle cx="200" cy="380" r="6"/>
    <circle cx="20" cy="200" r="6"/>
    <circle cx="380" cy="200" r="6"/>
    <circle cx="80" cy="200" r="8" fill="#3498DB"/>
    <circle cx="320" cy="200" r="8" fill="#3498DB"/>
    <circle cx="200" cy="80" r="7" fill="#2ECC71"/>
    <circle cx="200" cy="320" r="7" fill="#2ECC71"/>
  </g>

  <!-- Ciudad (abajo izquierda) -->
  <g fill="#2C3E50" stroke="#1A252F" stroke-width="1">
    <rect x="15" y="330" width="20" height="50"/>
    <rect x="40" y="345" width="25" height="35"/>
    <rect x="70" y="320" width="18" height="60"/>
    <rect x="92" y="340" width="22" height="40"/>
  </g>
  <g fill="#F1C40F" opacity="0.8">
    <rect x="20" y="335" width="3" height="4"/>
    <rect x="28" y="335" width="3" height="4"/>
    <rect x="45" y="350" width="3" height="4"/>
    <rect x="55" y="350" width="3" height="4"/>
    <rect x="75" y="325" width="3" height="4"/>
    <rect x="82" y="325" width="3" height="4"/>
    <rect x="97" y="345" width="3" height="4"/>
    <rect x="105" y="345" width="3" height="4"/>
  </g>

  <!-- Planta (abajo derecha) -->
  <g stroke="#27AE60" stroke-width="3" fill="none" stroke-linecap="round">
    <path d="M 350 360 Q 345 330 360 300"/>
    <path d="M 360 300 Q 370 320 380 330"/>
    <path d="M 360 300 Q 340 310 335 320"/>
  </g>
  <circle cx="360" cy="295" r="8" fill="#E74C3C" stroke="#FFFFFF" stroke-width="1.5"/>
  <circle cx="365" cy="290" r="3" fill="#F1C40F"/>

  <!-- Símbolos flotantes -->
  <!-- Corazón -->
  <path d="M 55 280 C 50 270, 40 275, 55 290 C 70 275, 60 270, 55 280 Z" fill="#E74C3C" opacity="0.8"/>
  <!-- WiFi -->
  <g stroke="#2980B9" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.8">
    <path d="M 330 230 Q 340 220 350 230"/>
    <path d="M 320 220 Q 340 205 360 220"/>
    <circle cx="340" cy="235" r="3" fill="#2980B9" stroke="none"/>
  </g>
  <!-- Engranaje -->
  <g transform="translate(300,80)" fill="none" stroke="#95A5A6" stroke-width="3">
    <circle cx="0" cy="0" r="12"/>
    <circle cx="0" cy="0" r="5"/>
    <line x1="0" y1="-15" x2="0" y2="-10"/>
    <line x1="13" y1="-5" x2="9" y2="-3"/>
    <line x1="13" y1="5" x2="9" y2="3"/>
    <line x1="0" y1="15" x2="0" y2="10"/>
    <line x1="-13" y1="5" x2="-9" y2="3"/>
    <line x1="-13" y1="-5" x2="-9" y2="-3"/>
  </g>
  <!-- Bombilla -->
  <g transform="translate(100,50)" fill="#F1C40F" stroke="#B7950B" stroke-width="1.5" opacity="0.9">
    <circle cx="0" cy="-5" r="10"/>
    <rect x="-3" y="5" width="6" height="6" rx="1"/>
    <line x1="-2" y1="11" x2="2" y2="11" stroke="#B7950B"/>
  </g>
</svg>