<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="75%">
      <stop offset="0%" stop-color="#1a2340"/>
      <stop offset="60%" stop-color="#0d1226"/>
      <stop offset="100%" stop-color="#05070f"/>
    </radialGradient>
    <radialGradient id="core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#9be8ff"/>
      <stop offset="70%" stop-color="#3aa0d8"/>
      <stop offset="100%" stop-color="#1a4a7a" stop-opacity="0.1"/>
    </radialGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#5ec8f0" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#5ec8f0" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="head" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b3d66"/>
      <stop offset="100%" stop-color="#15203d"/>
    </linearGradient>
    <filter id="blurSoft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- estrellas de fondo -->
  <g fill="#cfe9ff">
    <circle cx="40" cy="60" r="1.2" opacity="0.7"/>
    <circle cx="360" cy="45" r="1" opacity="0.5"/>
    <circle cx="330" cy="330" r="1.4" opacity="0.6"/>
    <circle cx="70" cy="330" r="1" opacity="0.5"/>
    <circle cx="200" cy="25" r="1.2" opacity="0.6"/>
    <circle cx="120" cy="35" r="0.9" opacity="0.4"/>
    <circle cx="290" cy="370" r="1" opacity="0.4"/>
    <circle cx="30" cy="200" r="1" opacity="0.4"/>
    <circle cx="375" cy="210" r="1.2" opacity="0.5"/>
    <circle cx="55" cy="120" r="0.8" opacity="0.4"/>
  </g>

  <!-- halo -->
  <circle cx="200" cy="195" r="150" fill="url(#halo)"/>

  <!-- red neuronal: nodos -->
  <g id="network">
    <!-- capa 1 -->
    <circle cx="105" cy="130" r="4" fill="#7fd8f7"/>
    <circle cx="105" cy="190" r="4" fill="#7fd8f7"/>
    <circle cx="105" cy="250" r="4" fill="#7fd8f7"/>
    <!-- capa 2 -->
    <circle cx="155" cy="110" r="4.5" fill="#a4e4fb"/>
    <circle cx="155" cy="165" r="4.5" fill="#a4e4fb"/>
    <circle cx="155" cy="225" r="4.5" fill="#a4e4fb"/>
    <circle cx="155" cy="280" r="4.5" fill="#a4e4fb"/>
    <!-- capa 3 -->
    <circle cx="215" cy="95" r="4.5" fill="#a4e4fb"/>
    <circle cx="215" cy="150" r="4.5" fill="#a4e4fb"/>
    <circle cx="215" cy="205" r="4.5" fill="#a4e4fb"/>
    <circle cx="215" cy="260" r="4.5" fill="#a4e4fb"/>
    <!-- capa 4 -->
    <circle cx="275" cy="120" r="4" fill="#7fd8f7"/>
    <circle cx="275" cy="180" r="4" fill="#7fd8f7"/>
    <circle cx="275" cy="240" r="4" fill="#7fd8f7"/>
    <!-- salida -->
    <circle cx="320" cy="150" r="3.5" fill="#c8f1ff"/>
    <circle cx="320" cy="195" r="3.5" fill="#c8f1ff"/>
    <circle cx="320" cy="240" r="3.5" fill="#c8f1ff"/>

    <!-- conexiones -->
    <g stroke="#4a90c4" stroke-width="1" opacity="0.45">
      <line x1="105" y1="130" x2="155" y2="110"/>
      <line x1="105" y1="130" x2="155" y2="165"/>
      <line x1="105" y1="190" x2="155" y2="165"/>
      <line x1="105" y1="190" x2="155" y2="225"/>
      <line x1="105" y1="250" x2="155" y2="225"/>
      <line x1="105" y1="250" x2="155" y2="280"/>
      <line x1="155" y1="110" x2="215" y2="95"/>
      <line x1="155" y1="110" x2="215" y2="150"/>
      <line x1="155" y1="165" x2="215" y2="150"/>
      <line x1="155" y1="165" x2="215" y2="205"/>
      <line x1="155" y1="225" x2="215" y2="205"/>
      <line x1="155" y1="225" x2="215" y2="260"/>
      <line x1="155" y1="280" x2="215" y2="260"/>
      <line x1="215" y1="95" x2="275" y2="120"/>
      <line x1="215" y1="150" x2="275" y2="120"/>
      <line x1="215" y1="150" x2="275" y2="180"/>
      <line x1="215" y1="205" x2="275" y2="180"/>
      <line x1="215" y1="205" x2="275" y2="240"/>
      <line x1="215" y1="260" x2="275" y2="240"/>
      <line x1="275" y1="120" x2="320" y2="150"/>
      <line x1="275" y1="180" x2="320" y2="150"/>
      <line x1="275" y1="180" x2="320" y2="195"/>
      <line x1="275" y1="240" x2="320" y2="195"/>
      <line x1="275" y1="240" x2="320" y2="240"/>
    </g>
  </g>

  <!-- cabeza -->
  <g>
    <path d="M200 90 C 150 90 130 135 132 180 C 133 215 140 240 152 262 C 160 276 168 288 175 300 C 182 311 190 318 200 318 C 210 318 218 311 225 300 C 232 288 240 276 248 262 C 260 240 267 215 268 180 C 270 135 250 90 200 90 Z"
          fill="url(#head)" stroke="#5ec8f0" stroke-width="1.5" opacity="0.95"/>

    <!-- circuitos internos -->
    <g stroke="#3a8fc4" stroke-width="1.2" fill="none" opacity="0.55">
      <path d="M155 190 h20 l10 10 h15"/>
      <path d="M155 230 h25 l8 -8 h12"/>
      <path d="M245 190 h-20 l-10 12 h-14"/>
      <path d="M200 130 v18"/>
      <path d="M170 150 l15 15"/>
      <path d="M230 150 l-15 15"/>
      <path d="M200 260 v16"/>
    </g>
    <g fill="#7fd8f7">
      <circle cx="200" cy="130" r="2.5"/>
      <circle cx="200" cy="148" r="2"/>
      <circle cx="170" cy="150" r="2"/>
      <circle cx="230" cy="150" r="2"/>
      <circle cx="185" cy="165" r="2"/>
      <circle cx="215" cy="165" r="2"/>
      <circle cx="200" cy="200" r="2.5"/>
      <circle cx="200" cy="260" r="2"/>
      <circle cx="200" cy="276" r="2.5"/>
    </g>

    <!-- ojos: anillos de datos -->
    <g filter="url(#glow)">
      <circle cx="163" cy="190" r="17" fill="none" stroke="#9be8ff" stroke-width="2.5"/>
      <circle cx="163" cy="190" r="10" fill="none" stroke="#5ec8f0" stroke-width="1.2" opacity="0.7"/>
      <circle cx="163" cy="190" r="3.5" fill="#e6f9ff"/>
      <circle cx="237" cy="190" r="17" fill="none" stroke="#9be8ff" stroke-width="2.5"/>
      <circle cx="237" cy="190" r="10" fill="none" stroke="#5ec8f0" stroke-width="1.2" opacity="0.7"/>
      <circle cx="237" cy="190" r="3.5" fill="#e6f9ff"/>
    </g>
    <!-- parpados sutiles -->
    <path d="M148 182 Q 163 170 178 182" fill="none" stroke="#0d1226" stroke-width="3" opacity="0.6"/>
    <path d="M222 182 Q 237 170 252 182" fill="none" stroke="#0d1226" stroke-width="3" opacity="0.6"/>

    <!-- boca: onda de habla -->
    <path d="M172 250 q7 -10 14 0 q7 10 14 0 q7 -10 14 0 q7 10 14 0"
          fill="none" stroke="#7fd8f7" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>

    <!-- antena -->
    <line x1="200" y1="90" x2="200" y2="66" stroke="#5ec8f0" stroke-width="2"/>
    <circle cx="200" cy="60" r="5" fill="#9be8ff" filter="url(#glow)"/>
  </g>

  <!-- símbolo infinito en la frente -->
  <path d="M188 118 c-6 -8 -18 -8 -18 0 c0 8 12 8 18 0 c6 -8 18 -8 18 0 c0 8 -12 8 -18 0 Z"
        fill="none" stroke="#7fd8f7" stroke-width="1.6" opacity="0.9"/>

  <!-- partículas flotantes -->
  <g fill="#9be8ff" opacity="0.8">
    <circle cx="90" cy="300" r="1.8"/>
    <circle cx="315" cy="80" r="2"/>
    <circle cx="120" cy="70" r="1.5"/>
    <circle cx="300" cy="310" r="1.8"/>
    <circle cx="160" cy="352" r="1.4"/>
    <circle cx="250" cy="358" r="1.6"/>
    <circle cx="60" cy="255" r="1.4"/>
    <circle cx="345" cy="255" r="1.5"/>
  </g>

  <!-- anillos orbitales -->
  <ellipse cx="200" cy="195" rx="160" ry="55" fill="none" stroke="#3a6f9c" stroke-width="1" opacity="0.35" transform="rotate(-12 200 195)"/>
  <ellipse cx="200" cy="195" rx="150" ry="42" fill="none" stroke="#3a6f9c" stroke-width="1" opacity="0.25" transform="rotate(18 200 195)"/>
  <circle cx="348" cy="160" r="3" fill="#c8f1ff" filter="url(#glow)"/>
  <circle cx="52" cy="232" r="3" fill="#c8f1ff" filter="url(#glow)"/>

  <!-- texto -->
  <text x="200" y="385" text-anchor="middle" font-family="monospace" font-size="11" fill="#7fd8f7" opacity="0.75" letter-spacing="3">AN AUTO-PORTRAIT</text>
</svg>