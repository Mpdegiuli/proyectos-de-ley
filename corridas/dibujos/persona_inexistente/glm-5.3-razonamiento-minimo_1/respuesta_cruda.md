<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="cielo" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#2b3a67"/>
      <stop offset="100%" stop-color="#0d1029"/>
    </radialGradient>
    <linearGradient id="tunica" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3a7d5d"/>
      <stop offset="100%" stop-color="#1e4636"/>
    </linearGradient>
    <linearGradient id="manto" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#6a4c93"/>
      <stop offset="100%" stop-color="#3c2a5c"/>
    </linearGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffe9a8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#ffe9a8" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <!-- estrellas -->
  <g fill="#fdf6d8">
    <circle cx="30" cy="40" r="1.5"/><circle cx="70" cy="90" r="1"/>
    <circle cx="120" cy="30" r="1.2"/><circle cx="180" cy="60" r="1.5"/>
    <circle cx="250" cy="25" r="1"/><circle cx="310" cy="70" r="1.4"/>
    <circle cx="360" cy="35" r="1.2"/><circle cx="340" cy="120" r="1"/>
    <circle cx="60" cy="150" r="1"/><circle cx="20" cy="200" r="1.3"/>
    <circle cx="370" cy="200" r="1.2"/><circle cx="50" cy="280" r="1"/>
    <circle cx="355" cy="290" r="1.3"/><circle cx="90" cy="330" r="1"/>
    <circle cx="320" cy="340" r="1.1"/>
    <path d="M150 45 l2 5 5 2 -5 2 -2 5 -2 -5 -5 -2 5 -2z" fill="#fff3c4"/>
    <path d="M280 100 l1.5 4 4 1.5 -4 1.5 -1.5 4 -1.5 -4 -4 -1.5 4 -1.5z" fill="#fff3c4"/>
  </g>

  <!-- luna pequeña -->
  <circle cx="345" cy="55" r="16" fill="#e8e3cf" opacity="0.85"/>
  <circle cx="339" cy="50" r="3" fill="#c9c4ae" opacity="0.6"/>
  <circle cx="350" cy="61" r="2" fill="#c9c4ae" opacity="0.6"/>

  <!-- suelo -->
  <path d="M0 330 Q100 315 200 328 T400 325 L400 400 L0 400 Z" fill="#141b3a"/>
  <path d="M0 340 Q120 330 220 340 T400 338" fill="none" stroke="#2b3a67" stroke-width="1.5" opacity="0.6"/>

  <!-- halo -->
  <circle cx="200" cy="120" r="75" fill="url(#halo)" opacity="0.5"/>

  <!-- manto detrás -->
  <path d="M200 175 Q120 200 105 330 L295 330 Q280 200 200 175 Z" fill="url(#manto)"/>

  <!-- cuerpo: túnica -->
  <path d="M200 190 Q160 210 150 260 Q143 300 140 335 L260 335 Q257 300 250 260 Q240 210 200 190 Z" fill="url(#tunica)"/>
  <!-- pliegues -->
  <path d="M200 200 L198 335" stroke="#16352a" stroke-width="1.5" opacity="0.5" fill="none"/>
  <path d="M175 220 Q168 280 165 335" stroke="#16352a" stroke-width="1" opacity="0.4" fill="none"/>
  <path d="M225 220 Q232 280 235 335" stroke="#16352a" stroke-width="1" opacity="0.4" fill="none"/>
  <!-- cinturón -->
  <path d="M156 258 Q200 272 244 258 L246 272 Q200 286 154 272 Z" fill="#c9a227"/>
  <circle cx="200" cy="272" r="6" fill="#e8d44d" stroke="#8a6d1a" stroke-width="1.5"/>

  <!-- brazos -->
  <path d="M158 215 Q120 245 112 285 Q110 295 118 297 Q126 298 128 289 Q136 255 168 232 Z" fill="#2f6b50"/>
  <path d="M242 215 Q280 245 288 285 Q290 295 282 297 Q274 298 272 289 Q264 255 232 232 Z" fill="#2f6b50"/>
  <!-- manos -->
  <circle cx="117" cy="293" r="8" fill="#d9b38c"/>
  <circle cx="283" cy="293" r="8" fill="#d9b38c"/>

  <!-- collar -->
  <path d="M185 195 Q200 212 215 195" fill="none" stroke="#e8d44d" stroke-width="2"/>
  <circle cx="200" cy="208" r="3.5" fill="#e8d44d"/>

  <!-- cuello y cabeza -->
  <rect x="190" y="175" width="20" height="20" rx="6" fill="#c9a075"/>
  <ellipse cx="200" cy="135" rx="34" ry="40" fill="#d9b38c"/>

  <!-- orejas largas y puntiagudas -->
  <path d="M168 122 Q150 95 158 78 Q168 90 172 108 Z" fill="#d9b38c"/>
  <path d="M232 122 Q250 95 242 78 Q232 90 228 108 Z" fill="#d9b38c"/>

  <!-- pelo -->
  <path d="M200 90 Q165 95 163 130 Q162 150 170 158 Q168 138 175 125 Q180 145 200 148 Q220 145 225 125 Q232 138 230 158 Q238 150 237 130 Q235 95 200 90 Z" fill="#4a3760"/>
  <path d="M163 130 Q150 145 152 165 Q156 158 160 155 Z" fill="#4a3760"/>
  <path d="M237 130 Q250 145 248 165 Q244 158 240 155 Z" fill="#4a3760"/>

  <!-- tercer ojo (místico) -->
  <ellipse cx="200" cy="108" rx="7" ry="9" fill="#fff8e1"/>
  <circle cx="200" cy="109" r="4" fill="#7a4cc9"/>
  <circle cx="200" cy="109" r="1.8" fill="#1a1030"/>

  <!-- ojos -->
  <ellipse cx="185" cy="130" rx="7" ry="8" fill="#fff8e1"/>
  <ellipse cx="215" cy="130" rx="7" ry="8" fill="#fff8e1"/>
  <circle cx="185" cy="131" r="3.8" fill="#4c7a3f"/>
  <circle cx="215" cy="131" r="3.8" fill="#4c7a3f"/>
  <circle cx="185" cy="131" r="1.6" fill="#101408"/>
  <circle cx="215" cy="131" r="1.6" fill="#101408"/>
  <circle cx="183.5" cy="129" r="1.1" fill="#fff"/>
  <circle cx="213.5" cy="129" r="1.1" fill="#fff"/>
  <!-- pestañas -->
  <path d="M179 124 Q185 120 191 124" fill="none" stroke="#3a2a50" stroke-width="1.5"/>
  <path d="M209 124 Q215 120 221 124" fill="none" stroke="#3a2a50" stroke-width="1.5"/>

  <!-- nariz y boca -->
  <path d="M198 140 Q200 146 197 149" fill="none" stroke="#b08d63" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M191 158 Q200 164 209 158" fill="none" stroke="#9c5f56" stroke-width="2" stroke-linecap="round"/>

  <!-- pecas luminosas -->
  <circle cx="176" cy="145" r="1.2" fill="#bfe8c9" opacity="0.9"/>
  <circle cx="224" cy="145" r="1.2" fill="#bfe8c9" opacity="0.9"/>
  <circle cx="170" cy="138" r="1" fill="#bfe8c9" opacity="0.7"/>
  <circle cx="230" cy="138" r="1" fill="#bfe8c9" opacity="0.7"/>

  <!-- orbáculo flotante entre sus manos -->
  <line x1="112" y1="293" x2="288" y2="293" stroke="#ffe9a8" stroke-width="1.5" opacity="0.35" stroke-dasharray="4 6"/>
  <circle cx="200" cy="255" r="20" fill="url(#halo)" opacity="0.9"/>
  <circle cx="200" cy="255" r="13" fill="none" stroke="#ffe9a8" stroke-width="2"/>
  <circle cx="200" cy="255" r="7" fill="#a3d9a5" opacity="0.7"/>
  <circle cx="197" cy="252" r="2" fill="#fff"/>
  <path d="M200 242 l3 8 8 3 -8 3 -3 8 -3 -8 -8 -3 8 -3z" fill="#fff3c4"/>

  <!-- constelación dibujada por ella -->
  <g stroke="#ffe9a8" stroke-width="0.8" opacity="0.6" fill="none">
    <path d="M60 60 L95 80 L80 115"/>
    <path d="M95 80 L130 65"/>
  </g>
  <g fill="#ffe9a8" opacity="0.8">
    <circle cx="60" cy="60" r="1.6"/><circle cx="95" cy="80" r="2"/><circle cx="80" cy="115" r="1.6"/><circle cx="130" cy="65" r="1.6"/>
  </g>

  <!-- sombra -->
  <ellipse cx="200" cy="338" rx="85" ry="10" fill="#000" opacity="0.35"/>
</svg>