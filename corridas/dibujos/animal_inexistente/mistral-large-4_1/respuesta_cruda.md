<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#1a2a4a"/>
      <stop offset="100%" stop-color="#0a1020"/>
    </radialGradient>
    <linearGradient id="body" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#7ee8c7"/>
      <stop offset="100%" stop-color="#2e8f7a"/>
    </linearGradient>
    <linearGradient id="fin" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffd166"/>
      <stop offset="100%" stop-color="#ef8354"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#b8fff0" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#b8fff0" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- estrellas -->
  <g fill="#cfe8ff" opacity="0.7">
    <circle cx="50" cy="60" r="1.5"/><circle cx="120" cy="40" r="1"/>
    <circle cx="300" cy="50" r="1.8"/><circle cx="350" cy="120" r="1"/>
    <circle cx="40" cy="200" r="1.2"/><circle cx="370" cy="250" r="1.5"/>
    <circle cx="90" cy="330" r="1"/><circle cx="320" cy="340" r="1.3"/>
    <circle cx="200" cy="30" r="1.2"/><circle cx="260" cy="90" r="1"/>
  </g>

  <!-- burbujas -->
  <g fill="none" stroke="#9fd8ff" stroke-opacity="0.35">
    <circle cx="70" cy="280" r="8"/><circle cx="95" cy="240" r="5"/>
    <circle cx="330" cy="200" r="7"/><circle cx="310" cy="160" r="4"/>
    <circle cx="150" cy="120" r="4"/><circle cx="250" cy="70" r="5"/>
  </g>

  <!-- halo luminoso -->
  <ellipse cx="200" cy="230" rx="130" ry="110" fill="url(#glow)" opacity="0.5"/>

  <!-- cola con aleta luminosa -->
  <path d="M 285 250 Q 350 230 365 180 Q 355 240 320 275 Q 300 285 285 275 Z" fill="url(#fin)" opacity="0.9"/>
  <path d="M 285 250 Q 340 245 358 200" fill="none" stroke="#fff3c4" stroke-width="2" opacity="0.6"/>

  <!-- cuerpo principal -->
  <ellipse cx="200" cy="240" rx="95" ry="70" fill="url(#body)"/>

  <!-- panza -->
  <ellipse cx="195" cy="265" rx="65" ry="42" fill="#d8fff2" opacity="0.55"/>

  <!-- aleta dorsal -->
  <path d="M 170 175 Q 200 120 235 172 Q 205 160 170 175 Z" fill="url(#fin)"/>
  <path d="M 185 168 Q 202 140 220 166" fill="none" stroke="#fff3c4" stroke-width="2" opacity="0.7"/>

  <!-- aletas laterales -->
  <path d="M 150 250 Q 110 265 100 300 Q 135 290 160 270 Z" fill="url(#fin)" opacity="0.85"/>
  <path d="M 250 250 Q 290 265 300 300 Q 265 290 240 270 Z" fill="url(#fin)" opacity="0.85"/>

  <!-- franjas onduladas -->
  <g fill="none" stroke="#1f6f5e" stroke-width="4" stroke-linecap="round" opacity="0.5">
    <path d="M 140 220 Q 160 210 180 220 Q 200 230 220 220 Q 240 210 260 220"/>
    <path d="M 135 245 Q 158 235 180 245 Q 202 255 224 245 Q 246 235 268 245"/>
    <path d="M 145 270 Q 165 262 185 270 Q 205 278 225 270 Q 245 262 262 270"/>
  </g>

  <!-- cabeza -->
  <ellipse cx="130" cy="215" rx="48" ry="42" fill="url(#body)"/>

  <!-- hocico -->
  <ellipse cx="95" cy="228" rx="26" ry="20" fill="#a9f2dd"/>
  <circle cx="82" cy="222" r="3.5" fill="#0e3b32"/>
  <circle cx="82" cy="236" r="3.5" fill="#0e3b32"/>
  <path d="M 78 229 Q 95 238 112 229" fill="none" stroke="#0e3b32" stroke-width="2.5" stroke-linecap="round"/>

  <!-- ojo grande -->
  <circle cx="128" cy="205" r="16" fill="#ffffff"/>
  <circle cx="131" cy="207" r="9" fill="#123a4a"/>
  <circle cx="134" cy="204" r="3.5" fill="#ffffff"/>
  <circle cx="128" cy="210" r="1.5" fill="#ffffff" opacity="0.7"/>

  <!-- tercer ojo en la frente (criatura misteriosa) -->
  <ellipse cx="150" cy="180" rx="9" ry="12" fill="#fff3c4"/>
  <circle cx="150" cy="180" r="5" fill="#ef8354"/>
  <circle cx="152" cy="178" r="1.8" fill="#fff"/>

  <!-- branquias / mejillas -->
  <g fill="none" stroke="#1f6f5e" stroke-width="3" stroke-linecap="round" opacity="0.6">
    <path d="M 108 200 Q 114 208 108 216"/>
    <path d="M 118 198 Q 124 208 118 218"/>
  </g>

  <!-- bigotes flotantes -->
  <g fill="none" stroke="#b8fff0" stroke-width="2.5" stroke-linecap="round" opacity="0.8">
    <path d="M 70 215 Q 45 205 30 190"/>
    <path d="M 70 228 Q 42 228 25 235"/>
    <path d="M 72 240 Q 50 252 38 268"/>
  </g>
  <circle cx="30" cy="190" r="3" fill="#b8fff0"/>
  <circle cx="25" cy="235" r="3" fill="#b8fff0"/>
  <circle cx="38" cy="268" r="3" fill="#b8fff0"/>

  <!-- puntos luminosos en el cuerpo -->
  <g fill="#eafffa" opacity="0.9">
    <circle cx="180" cy="200" r="3"/><circle cx="220" cy="190" r="2.5"/>
    <circle cx="245" cy="215" r="3"/><circle cx="200" cy="230" r="2"/>
    <circle cx="165" cy="240" r="2.5"/><circle cx="230" cy="250" r="2.5"/>
    <circle cx="190" cy="285" r="2"/><circle cx="255" cy="270" r="2"/>
  </g>

  <!-- sombra bajo el cuerpo -->
  <ellipse cx="200" cy="330" rx="110" ry="14" fill="#000000" opacity="0.35" filter="url(#soft)"/>
</svg>