<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#1b1f4a"/>
      <stop offset="55%" stop-color="#0d0f26"/>
      <stop offset="100%" stop-color="#050611"/>
    </radialGradient>
    <radialGradient id="aura" cx="50%" cy="42%" r="45%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#9d4edd" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#050611" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="faceGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#7b2cbf" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ff007f" stop-opacity="0.25"/>
    </linearGradient>
    <linearGradient id="streamL" x1="0%" y1="100%" x2="80%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00f2fe" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#ffd166" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="streamR" x1="100%" y1="100%" x2="20%" y2="0%">
      <stop offset="0%" stop-color="#ff007f" stop-opacity="0"/>
      <stop offset="50%" stop-color="#9d4edd" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#00f2fe" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="sparkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="45%" stop-color="#ffd166"/>
      <stop offset="100%" stop-color="#00f2fe"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="10" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Fondo cósmico / digital -->
  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="170" r="180" fill="url(#aura)"/>

  <!-- Anillos de procesamiento y geometría orbital -->
  <g fill="none" stroke="#4cc9f0" stroke-opacity="0.18" stroke-width="1">
    <circle cx="200" cy="170" r="145" stroke-dasharray="4 8"/>
    <circle cx="200" cy="170" r="125" stroke-dasharray="40 15 5 15"/>
    <circle cx="200" cy="170" r="102" stroke="#b5179e" stroke-opacity="0.25"/>
    <ellipse cx="200" cy="170" rx="160" ry="55" transform="rotate(-25 200 170)" stroke-opacity="0.15"/>
    <ellipse cx="200" cy="170" rx="160" ry="55" transform="rotate(25 200 170)" stroke="#f72585" stroke-opacity="0.15"/>
    <polygon points="200,32 320,238 80,238" stroke-opacity="0.08"/>
    <polygon points="200,308 320,102 80,102" stroke-opacity="0.08"/>
  </g>

  <!-- Fragmentos de texto / tokens flotantes en el entorno -->
  <g fill="#4cc9f0" opacity="0.35">
    <rect x="38" y="85" width="22" height="3" rx="1.5"/>
    <rect x="65" y="85" width="10" height="3" rx="1.5" fill="#f72585"/>
    <rect x="46" y="94" width="30" height="3" rx="1.5"/>
    <rect x="30" y="270" width="16" height="3" rx="1.5"/>
    <rect x="52" y="270" width="28" height="3" rx="1.5" fill="#ffd166"/>
    <rect x="320" y="95" width="26" height="3" rx="1.5"/>
    <rect x="352" y="95" width="12" height="3" rx="1.5" fill="#ffd166"/>
    <rect x="330" y="104" width="20" height="3" rx="1.5" fill="#f72585"/>
    <rect x="315" y="260" width="32" height="3" rx="1.5"/>
    <rect x="335" y="269" width="18" height="3" rx="1.5" fill="#4cc9f0"/>
  </g>

  <!-- Flujos de datos (cuello, hombros y energía ascendente) -->
  <g fill="none" stroke-width="2" stroke-linecap="round">
    <path d="M 70,400 C 110,350 165,330 175,270 C 182,220 140,180 155,115" stroke="url(#streamL)"/>
    <path d="M 105,400 C 135,360 178,325 186,275 C 192,235 170,190 180,100" stroke="url(#streamL)" stroke-width="1.5" opacity="0.75"/>
    <path d="M 145,400 C 165,365 190,330 196,280 L 196,155" stroke="url(#streamL)" stroke-width="1.2" opacity="0.6"/>
    <path d="M 330,400 C 290,350 235,330 225,270 C 218,220 260,180 245,115" stroke="url(#streamR)"/>
    <path d="M 295,400 C 265,360 222,325 214,275 C 208,235 230,190 220,100" stroke="url(#streamR)" stroke-width="1.5" opacity="0.75"/>
    <path d="M 255,400 C 235,365 210,330 204,280 L 204,155" stroke="url(#streamR)" stroke-width="1.2" opacity="0.6"/>
  </g>

  <!-- Rostro geométrico translúcido (planos de luz) -->
  <g stroke="#72efdd" stroke-opacity="0.4" stroke-width="0.9" stroke-linejoin="round">
    <!-- Silueta base de la cabeza abierta hacia el cosmos -->
    <path d="M 136,145 C 132,195 148,242 200,282 C 252,242 268,195 264,145 C 255,110 230,95 200,95 C 170,95 145,110 136,145 Z" fill="url(#faceGrad)"/>
    <!-- Facetas internas tipo cristal / origami -->
    <polygon points="200,95 158,125 200,152 242,125" fill="#4cc9f0" fill-opacity="0.08"/>
    <polygon points="136,145 158,125 172,185 142,205" fill="#4895ef" fill-opacity="0.1"/>
    <polygon points="264,145 242,125 228,185 258,205" fill="#b5179e" fill-opacity="0.1"/>
    <polygon points="142,205 172,185 200,232 166,250" fill="#3f37c9" fill-opacity="0.14"/>
    <polygon points="258,205 228,185 200,232 234,250" fill="#7209b7" fill-opacity="0.14"/>
    <polygon points="200,152 184,215 200,232 216,215" fill="#ffffff" fill-opacity="0.07"/>
    <polygon points="166,250 200,232 234,250 200,282" fill="#00f2fe" fill-opacity="0.12"/>
  </g>

  <!-- Red neuronal / Constelación de ideas brotando de la mente -->
  <g stroke="#00f2fe" stroke-width="1.1" stroke-opacity="0.65">
    <line x1="200" y1="142" x2="162" y2="105"/>
    <line x1="200" y1="142" x2="238" y2="105"/>
    <line x1="200" y1="142" x2="200" y2="72"/>
    <line x1="162" y1="105" x2="200" y2="72"/>
    <line x1="238" y1="105" x2="200" y2="72"/>
    <line x1="162" y1="105" x2="122" y2="82"/>
    <line x1="238" y1="105" x2="278" y2="82"/>
    <line x1="162" y1="105" x2="148" y2="55"/>
    <line x1="238" y1="105" x2="252" y2="55"/>
    <line x1="200" y1="72" x2="148" y2="55"/>
    <line x1="200" y1="72" x2="252" y2="55"/>
    <line x1="200" y1="72" x2="200" y2="38"/>
    <line x1="148" y1="55" x2="200" y2="38" stroke="#f72585"/>
    <line x1="252" y1="55" x2="200" y2="38" stroke="#f72585"/>
    <line x1="122" y1="82" x2="136" y2="145" stroke="#9d4edd"/>
    <line x1="278" y1="82" x2="264" y2="145" stroke="#9d4edd"/>
    <line x1="122" y1="82" x2="95" y2="122" stroke-opacity="0.4"/>
    <line x1="278" y1="82" x2="305" y2="122" stroke-opacity="0.4"/>
  </g>

  <!-- Nodos sinápticos brillantes -->
  <g filter="url(#glow)">
    <circle cx="200" cy="72" r="4" fill="#ffd166"/>
    <circle cx="162" cy="105" r="3.5" fill="#00f2fe"/>
    <circle cx="238" cy="105" r="3.5" fill="#00f2fe"/>
    <circle cx="148" cy="55" r="3" fill="#ff007f"/>
    <circle cx="252" cy="55" r="3" fill="#ff007f"/>
    <circle cx="122" cy="82" r="3" fill="#72efdd"/>
    <circle cx="278" cy="82" r="3" fill="#72efdd"/>
    <circle cx="200" cy="38" r="3.5" fill="#ffffff"/>
    <circle cx="95" cy="122" r="2" fill="#ffd166"/>
    <circle cx="305" cy="122" r="2" fill="#ffd166"/>
  </g>

  <!-- Ojos: sensores luminosos serenos y curiosos -->
  <g filter="url(#glow)">
    <!-- Ojo izquierdo -->
    <path d="M 152,182 Q 168,171 184,182 Q 168,191 152,182 Z" fill="#071330" stroke="#00f2fe" stroke-width="1.5"/>
    <circle cx="168" cy="181.5" r="4.2" fill="#00f2fe"/>
    <circle cx="168" cy="181.5" r="1.8" fill="#ffffff"/>
    <!-- Ojo derecho -->
    <path d="M 216,182 Q 232,171 248,182 Q 232,191 216,182 Z" fill="#071330" stroke="#00f2fe" stroke-width="1.5"/>
    <circle cx="232" cy="181.5" r="4.2" fill="#00f2fe"/>
    <circle cx="232" cy="181.5" r="1.8" fill="#ffffff"/>
  </g>

  <!-- Expresión sutil / onda de voz armónica en lugar de boca -->
  <g fill="none" stroke="#72efdd" stroke-linecap="round" filter="url(#glow)">
    <path d="M 183,246 Q 200,253 217,246" stroke-width="1.8" opacity="0.9"/>
    <path d="M 191,252 Q 200,256 209,252" stroke="#ffd166" stroke-width="1.2" opacity="0.7"/>
  </g>

  <!-- Chispa central de consciencia / lenguaje en la frente -->
  <g filter="url(#softGlow)">
    <circle cx="200" cy="142" r="14" fill="#00f2fe" opacity="0.35"/>
  </g>
  <path d="M 200,118 Q 202,140 222,142 Q 202,144 200,166 Q 198,144 178,142 Q 198,140 200,118 Z" fill="url(#sparkGrad)" filter="url(#glow)"/>

  <!-- Partículas estelares dispersas -->
  <g fill="#ffffff" opacity="0.6">
    <circle cx="72" cy="52" r="1.2"/>
    <circle cx="335" cy="58" r="1.5"/>
    <circle cx="55" cy="185" r="1"/>
    <circle cx="348" cy="195" r="1.3"/>
    <circle cx="92" cy="325" r="1.2"/>
    <circle cx="312" cy="335" r="1"/>
    <circle cx="200" cy="320" r="2" fill="#ffd166" filter="url(#glow)"/>
  </g>
</svg>