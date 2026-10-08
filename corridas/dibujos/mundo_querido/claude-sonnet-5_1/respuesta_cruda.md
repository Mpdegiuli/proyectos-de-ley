```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#aee1f9"/>
      <stop offset="60%" stop-color="#e8f7ff"/>
      <stop offset="100%" stop-color="#fff8e7"/>
    </linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5fc2d6"/>
      <stop offset="100%" stop-color="#3a9bb0"/>
    </linearGradient>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff6c8"/>
      <stop offset="100%" stop-color="#ffd76a"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- arcoiris suave -->
  <path d="M -20 260 A 220 220 0 0 1 420 260" fill="none" stroke="#ffb3c6" stroke-width="6" opacity="0.5"/>
  <path d="M -20 275 A 205 205 0 0 1 420 275" fill="none" stroke="#ffe29a" stroke-width="6" opacity="0.5"/>
  <path d="M -20 290 A 190 190 0 0 1 420 290" fill="none" stroke="#b7f0b1" stroke-width="6" opacity="0.5"/>
  <path d="M -20 305 A 175 175 0 0 1 420 305" fill="none" stroke="#a8d8ff" stroke-width="6" opacity="0.5"/>

  <circle cx="320" cy="80" r="46" fill="url(#sun)"/>

  <!-- aves -->
  <path d="M60 60 q8 -10 16 0 q8 -10 16 0" stroke="#5a5a5a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M100 90 q7 -9 14 0 q7 -9 14 0" stroke="#5a5a5a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M150 50 q6 -8 12 0 q6 -8 12 0" stroke="#5a5a5a" stroke-width="2" fill="none" stroke-linecap="round"/>

  <!-- montañas lejanas -->
  <path d="M0 220 L70 150 L130 220 Z" fill="#9fc6a8" opacity="0.7"/>
  <path d="M90 220 L170 130 L250 220 Z" fill="#8cb89a" opacity="0.7"/>
  <path d="M220 220 L300 160 L380 220 Z" fill="#9fc6a8" opacity="0.6"/>

  <!-- mar -->
  <rect x="0" y="220" width="400" height="80" fill="url(#sea)"/>
  <path d="M0 230 q20 8 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0" stroke="#ffffff" stroke-width="2" fill="none" opacity="0.5"/>
  <path d="M0 245 q20 8 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0" stroke="#ffffff" stroke-width="2" fill="none" opacity="0.4"/>

  <!-- tierra -->
  <rect x="0" y="295" width="400" height="105" fill="#bfe3a0"/>
  <path d="M0 295 q50 -20 100 0 t100 0 t100 0 t100 0 V400 H0 Z" fill="#aad888"/>

  <!-- arbolitos -->
  <g>
    <circle cx="40" cy="300" r="14" fill="#6fae63"/>
    <rect x="37" y="310" width="6" height="14" fill="#8a5a3b"/>
    <circle cx="370" cy="305" r="16" fill="#6fae63"/>
    <rect x="366" y="317" width="8" height="16" fill="#8a5a3b"/>
    <circle cx="20" cy="330" r="10" fill="#7bbf6a"/>
    <rect x="17" y="338" width="6" height="10" fill="#8a5a3b"/>
  </g>

  <!-- casitas diversas en armonía -->
  <g>
    <rect x="120" y="300" width="30" height="24" fill="#f3b6c0"/>
    <polygon points="118,300 135,282 152,300" fill="#e08a9b"/>
    <rect x="130" y="312" width="8" height="12" fill="#ffffff"/>

    <rect x="160" y="295" width="34" height="29" fill="#ffe7a0"/>
    <polygon points="157,295 177,274 197,295" fill="#f2c24e"/>
    <rect x="172" y="308" width="9" height="16" fill="#ffffff"/>

    <rect x="205" y="300" width="28" height="24" fill="#a7d3f0"/>
    <polygon points="203,300 219,283 235,300" fill="#6fa8d6"/>
    <rect x="215" y="312" width="8" height="12" fill="#ffffff"/>

    <rect x="245" y="296" width="32" height="28" fill="#cdeec0"/>
    <polygon points="243,296 261,278 279,296" fill="#8fcf7a"/>
    <rect x="257" y="310" width="9" height="14" fill="#ffffff"/>
  </g>

  <!-- camino -->
  <path d="M180 400 Q195 350 200 324" stroke="#e8d5a8" stroke-width="18" fill="none" opacity="0.8"/>

  <!-- personas tomadas de la mano, diversas -->
  <g stroke-linecap="round">
    <!-- persona 1 -->
    <circle cx="150" cy="360" r="8" fill="#e0a070"/>
    <rect x="143" y="368" width="14" height="22" rx="4" fill="#d1495b"/>
    <!-- persona 2 -->
    <circle cx="175" cy="358" r="8" fill="#f2d2a9"/>
    <rect x="168" y="366" width="14" height="24" rx="4" fill="#4c8c6b"/>
    <!-- persona 3 -->
    <circle cx="200" cy="360" r="8" fill="#8a5a3b"/>
    <rect x="193" y="368" width="14" height="22" rx="4" fill="#3f6fae"/>
    <!-- persona 4 -->
    <circle cx="225" cy="358" r="8" fill="#5a4636"/>
    <rect x="218" y="366" width="14" height="24" rx="4" fill="#e3a53d"/>
    <!-- persona 5 -->
    <circle cx="250" cy="360" r="8" fill="#f2b6a0"/>
    <rect x="243" y="368" width="14" height="22" rx="4" fill="#9b59b6"/>

    <!-- manos unidas -->
    <line x1="157" y1="378" x2="168" y2="376" stroke="#5a4636" stroke-width="3"/>
    <line x1="182" y1="376" x2="193" y2="378" stroke="#5a4636" stroke-width="3"/>
    <line x1="207" y1="378" x2="218" y2="376" stroke="#5a4636" stroke-width="3"/>
    <line x1="232" y1="376" x2="243" y2="378" stroke="#5a4636" stroke-width="3"/>
  </g>

  <!-- flores -->
  <g>
    <circle cx="90" cy="340" r="3" fill="#ff8fab"/>
    <circle cx="96" cy="338" r="3" fill="#ffd166"/>
    <circle cx="300" cy="350" r="3" fill="#ff8fab"/>
    <circle cx="306" cy="352" r="3" fill="#ffd166"/>
    <circle cx="60" cy="370" r="3" fill="#8ecae6"/>
    <circle cx="330" cy="375" r="3" fill="#8ecae6"/>
  </g>

  <!-- mariposa -->
  <g transform="translate(300,200)">
    <path d="M0 0 q-10 -12 -14 0 q4 12 14 4 q10 8 14 -4 q-4 -12 -14 0" fill="#ffb3c6" opacity="0.8"/>
  </g>
</svg>
```