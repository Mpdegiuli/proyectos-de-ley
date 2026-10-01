<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2b1b4d"/>
      <stop offset="1" stop-color="#6a3f8f"/>
    </linearGradient>
    <linearGradient id="cuerpo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4dd0c4"/>
      <stop offset="1" stop-color="#2a8f9c"/>
    </linearGradient>
    <linearGradient id="ala" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd166"/>
      <stop offset="1" stop-color="#ef8354"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <!-- estrellas -->
  <g fill="#fff">
    <circle cx="40" cy="50" r="2"/>
    <circle cx="90" cy="30" r="1.5"/>
    <circle cx="340" cy="45" r="2"/>
    <circle cx="300" cy="90" r="1.3"/>
    <circle cx="60" cy="110" r="1.4"/>
    <circle cx="370" cy="130" r="1.6"/>
    <circle cx="200" cy="25" r="1.5"/>
  </g>
  <circle cx="330" cy="70" r="26" fill="#f6f1d5" opacity="0.9"/>
  <circle cx="322" cy="64" r="5" fill="#e0d9b8"/>
  <circle cx="338" cy="78" r="4" fill="#e0d9b8"/>

  <!-- ala trasera -->
  <path d="M215 175 Q260 90 330 100 Q300 130 285 150 Q310 145 335 150 Q295 170 270 180 Q290 185 305 195 Q260 205 225 195 Z"
        fill="url(#ala)" opacity="0.75" stroke="#b85c38" stroke-width="2"/>

  <!-- cola de pez -->
  <path d="M290 235 Q330 200 355 190 Q345 225 335 240 Q350 250 365 275 Q330 270 300 260 Z"
        fill="url(#cuerpo)" stroke="#1d6b75" stroke-width="3"/>
  <path d="M310 230 Q330 218 345 210 M312 242 Q332 240 348 250" stroke="#1d6b75" stroke-width="2" fill="none"/>

  <!-- patas (seis) -->
  <g stroke="#1d6b75" stroke-width="3" fill="#3aa8a0">
    <path d="M150 280 q-5 30 -12 45 q12 8 26 4 q3 -25 6 -45 Z"/>
    <path d="M185 288 q0 32 -5 48 q13 6 26 2 q1 -25 0 -48 Z"/>
    <path d="M225 285 q5 30 3 47 q13 5 25 0 q-3 -25 -8 -45 Z"/>
    <path d="M130 270 q-18 22 -32 32 q6 12 20 14 q12 -20 24 -38 Z"/>
    <path d="M255 275 q15 25 28 35 q-4 12 -18 15 q-14 -22 -24 -42 Z"/>
    <path d="M205 292 q-2 34 -8 50 q12 7 26 3 q4 -26 4 -50 Z" fill="#2f8f88"/>
  </g>

  <!-- cuerpo con escamas -->
  <ellipse cx="205" cy="240" rx="100" ry="62" fill="url(#cuerpo)" stroke="#1d6b75" stroke-width="3"/>
  <g fill="none" stroke="#1d6b75" stroke-width="2" opacity="0.6">
    <path d="M160 210 q10 12 0 24 M185 205 q10 12 0 24 M210 205 q10 12 0 24 M235 210 q10 12 0 24 M260 218 q10 12 0 24"/>
    <path d="M172 235 q10 12 0 24 M198 232 q10 12 0 24 M224 232 q10 12 0 24 M250 238 q10 12 0 24"/>
  </g>

  <!-- ala delantera -->
  <path d="M175 185 Q120 85 45 100 Q80 130 95 152 Q70 148 40 155 Q85 175 112 183 Q90 190 72 202 Q125 212 165 200 Z"
        fill="url(#ala)" stroke="#b85c38" stroke-width="2.5"/>
  <path d="M150 190 Q110 140 75 118 M140 195 Q105 170 68 160 M135 198 Q110 192 85 198"
        stroke="#b85c38" stroke-width="2" fill="none" opacity="0.7"/>

  <!-- cabeza de gato -->
  <g>
    <!-- orejas -->
    <path d="M118 128 L105 78 L148 105 Z" fill="#8f6bd6" stroke="#5c3e9e" stroke-width="3"/>
    <path d="M182 122 L205 76 L222 122 Z" fill="#8f6bd6" stroke="#5c3e9e" stroke-width="3"/>
    <path d="M120 120 L112 90 L140 108 Z" fill="#f5b8d0"/>
    <path d="M188 116 L204 86 L214 116 Z" fill="#f5b8d0"/>
    <!-- cara -->
    <circle cx="165" cy="160" r="58" fill="#8f6bd6" stroke="#5c3e9e" stroke-width="3"/>
    <!-- rayas -->
    <path d="M150 105 q5 12 0 20 M165 102 q4 13 0 22 M180 105 q3 12 -1 20" stroke="#5c3e9e" stroke-width="3" fill="none"/>
    <!-- tercer ojo -->
    <ellipse cx="165" cy="132" rx="10" ry="14" fill="#fff" stroke="#5c3e9e" stroke-width="2"/>
    <ellipse cx="165" cy="132" rx="4" ry="9" fill="#e63946"/>
    <circle cx="164" cy="128" r="1.5" fill="#fff"/>
    <!-- ojos -->
    <ellipse cx="142" cy="158" rx="12" ry="14" fill="#fff" stroke="#5c3e9e" stroke-width="2"/>
    <ellipse cx="188" cy="158" rx="12" ry="14" fill="#fff" stroke="#5c3e9e" stroke-width="2"/>
    <ellipse cx="143" cy="160" rx="5" ry="9" fill="#2b1b4d"/>
    <ellipse cx="187" cy="160" rx="5" ry="9" fill="#2b1b4d"/>
    <circle cx="141" cy="156" r="2" fill="#fff"/>
    <circle cx="185" cy="156" r="2" fill="#fff"/>
    <!-- nariz y boca -->
    <path d="M158 178 L172 178 L165 188 Z" fill="#f5b8d0" stroke="#5c3e9e" stroke-width="2"/>
    <path d="M165 188 Q165 196 155 198 M165 188 Q165 196 175 198" stroke="#5c3e9e" stroke-width="2.5" fill="none"/>
    <!-- bigotes -->
    <g stroke="#e8e0ff" stroke-width="2" fill="none" opacity="0.9">
      <path d="M128 178 Q100 174 82 168"/>
      <path d="M128 186 Q102 188 84 192"/>
      <path d="M202 178 Q228 174 246 170"/>
      <path d="M202 186 Q226 190 244 196"/>
    </g>
    <!-- branquias en las mejillas -->
    <path d="M120 165 q-6 8 0 16 M113 160 q-7 10 0 22" stroke="#5c3e9e" stroke-width="2.5" fill="none"/>
  </g>

  <!-- aleta dorsal saliendo del lomo -->
  <path d="M205 178 Q215 145 245 138 Q238 158 240 170 Q255 160 272 158 Q258 178 245 186 Z"
        fill="#4dd0c4" stroke="#1d6b75" stroke-width="2.5" opacity="0.95"/>

  <!-- burbujas imposibles en el cielo -->
  <g fill="none" stroke="#bfeef0" stroke-width="2" opacity="0.8">
    <circle cx="285" cy="150" r="7"/>
    <circle cx="305" cy="128" r="5"/>
    <circle cx="322" cy="110" r="4"/>
  </g>

  <text x="200" y="382" text-anchor="middle" font-family="Georgia, serif" font-size="17" fill="#e8e0ff" font-style="italic">El Gatopez Alado — respira agua, vuela en el vacío</text>
</svg>