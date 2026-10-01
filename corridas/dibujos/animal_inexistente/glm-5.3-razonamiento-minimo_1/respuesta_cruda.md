<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="cielo" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#2b3a67"/>
      <stop offset="60%" stop-color="#1b2440"/>
      <stop offset="100%" stop-color="#0d1226"/>
    </radialGradient>
    <radialGradient id="cuerpo" cx="40%" cy="35%" r="75%">
      <stop offset="0%" stop-color="#8be8d8"/>
      <stop offset="55%" stop-color="#4aa8b8"/>
      <stop offset="100%" stop-color="#2c6a8f"/>
    </radialGradient>
    <radialGradient id="luna" cx="35%" cy="35%" r="70%">
      <stop offset="0%" stop-color="#fffbe8"/>
      <stop offset="100%" stop-color="#e8d9a0"/>
    </radialGradient>
    <linearGradient id="ala" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffd6f2" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#b388e0" stop-opacity="0.7"/>
    </linearGradient>
    <filter id="brillo" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>
  <circle cx="315" cy="78" r="42" fill="url(#luna)" opacity="0.9"/>
  <g fill="#ffffff" opacity="0.7">
    <circle cx="50" cy="50" r="1.5"/><circle cx="120" cy="30" r="1.2"/>
    <circle cx="200" cy="60" r="1.6"/><circle cx="260" cy="25" r="1.1"/>
    <circle cx="370" cy="150" r="1.4"/><circle cx="30" cy="140" r="1.2"/>
    <circle cx="80" cy="220" r="1.5"/><circle cx="350" cy="250" r="1.3"/>
    <circle cx="150" cy="100" r="1"/><circle cx="230" cy="130" r="1.4"/>
  </g>

  <!-- colinas -->
  <path d="M0 400 L0 320 Q60 280 130 318 Q200 355 270 315 Q340 278 400 320 L400 400 Z" fill="#131c33"/>
  <path d="M0 400 L0 355 Q80 330 160 358 Q250 388 330 352 Q370 335 400 345 L400 400 Z" fill="#0b1122"/>

  <!-- Alas -->
  <g>
    <path d="M195 185 Q120 90 55 110 Q85 150 100 190 Q70 200 60 235 Q120 245 195 220 Z" fill="url(#ala)" stroke="#d9b8f0" stroke-width="2">
      <animateTransform attributeName="transform" type="rotate" values="-4 195 200; 5 195 200; -4 195 200" dur="3s" repeatCount="indefinite"/>
    </path>
    <path d="M205 185 Q280 90 345 110 Q315 150 300 190 Q330 200 340 235 Q280 245 205 220 Z" fill="url(#ala)" stroke="#d9b8f0" stroke-width="2">
      <animateTransform attributeName="transform" type="rotate" values="4 205 200; -5 205 200; 4 205 200" dur="3s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- orejas-antena -->
  <path d="M170 118 Q150 60 120 42 Q140 100 158 128 Z" fill="#4aa8b8" stroke="#2c6a8f" stroke-width="2"/>
  <path d="M230 118 Q250 60 280 42 Q260 100 242 128 Z" fill="#4aa8b8" stroke="#2c6a8f" stroke-width="2"/>
  <circle cx="122" cy="44" r="6" fill="#ffe28a" filter="url(#brillo)">
    <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="278" cy="44" r="6" fill="#ffe28a" filter="url(#brillo)">
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
  </circle>

  <!-- cuerpo -->
  <ellipse cx="200" cy="205" rx="62" ry="72" fill="url(#cuerpo)" stroke="#1f4f73" stroke-width="3"/>
  <!-- vientre -->
  <ellipse cx="200" cy="228" rx="36" ry="44" fill="#d9f7ee" opacity="0.85"/>

  <!-- escamas del lomo -->
  <g fill="#2c6a8f" opacity="0.8">
    <path d="M148 175 q6 -12 12 0 q-6 6 -12 0"/>
    <path d="M162 162 q6 -12 12 0 q-6 6 -12 0"/>
    <path d="M226 162 q6 -12 12 0 q-6 6 -12 0"/>
    <path d="M240 175 q6 -12 12 0 q-6 6 -12 0"/>
    <path d="M205 152 q6 -12 12 0 q-6 6 -12 0"/>
  </g>

  <!-- ojos -->
  <circle cx="180" cy="192" r="14" fill="#fdfdf5"/>
  <circle cx="220" cy="192" r="14" fill="#fdfdf5"/>
  <circle cx="183" cy="194" r="7" fill="#1a1a2e">
    <animate attributeName="r" values="7;7;2;7;7" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="217" cy="194" r="7" fill="#1a1a2e">
    <animate attributeName="r" values="7;7;2;7;7" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="185" cy="191" r="2.5" fill="#fff"/>
  <circle cx="219" cy="191" r="2.5" fill="#fff"/>

  <!-- hocico -->
  <path d="M200 206 l-6 9 h12 Z" fill="#1f4f73"/>
  <path d="M200 215 q0 8 8 8 q6 0 6 -6" fill="none" stroke="#1f4f73" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M200 215 q0 8 -8 8 q-6 0 -6 -6" fill="none" stroke="#1f4f73" stroke-width="2.5" stroke-linecap="round"/>

  <!-- bigotes -->
  <g stroke="#d9f7ee" stroke-width="1.5" stroke-linecap="round" opacity="0.8">
    <path d="M170 214 L138 208"/><path d="M170 220 L140 226"/>
    <path d="M230 214 L262 208"/><path d="M230 220 L260 226"/>
  </g>

  <!-- patitas -->
  <path d="M172 268 q-6 20 2 30" stroke="#2c6a8f" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M228 268 q6 20 -2 30" stroke="#2c6a8f" stroke-width="7" fill="none" stroke-linecap="round"/>
  <circle cx="173" cy="301" r="7" fill="#d9f7ee"/>
  <circle cx="227" cy="301" r="7" fill="#d9f7ee"/>

  <!-- cola-estrella -->
  <g filter="url(#brillo)">
    <path d="M200 277 l6 18 19 2 -14 13 4 19 -15 -10 -15 10 4 -19 -14 -13 19 -2 Z" fill="#ffe28a">
      <animateTransform attributeName="transform" type="rotate" values="-10 200 295; 10 200 295; -10 200 295" dur="2.5s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- esporas flotantes -->
  <g fill="#8be8d8">
    <circle cx="90" cy="290" r="3"><animate attributeName="cy" values="290;270;290" dur="4s" repeatCount="indefinite"/></circle>
    <circle cx="320" cy="300" r="2.5"><animate attributeName="cy" values="300;282;300" dur="5s" repeatCount="indefinite"/></circle>
    <circle cx="140" cy="330" r="2"><animate attributeName="cy" values="330;314;330" dur="3.5s" repeatCount="indefinite"/></circle>
    <circle cx="280" cy="335" r="3"><animate attributeName="cy" values="335;318;335" dur="4.5s" repeatCount="indefinite"/></circle>
  </g>

  <!-- firma -->
  <text x="200" y="388" text-anchor="middle" font-family="serif" font-size="13" fill="#8be8d8" opacity="0.7">Lepidopticeto lunar</text>
</svg>