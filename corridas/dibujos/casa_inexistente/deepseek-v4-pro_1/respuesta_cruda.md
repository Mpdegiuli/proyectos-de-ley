<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b1026"/>
      <stop offset="50%" stop-color="#3a1c71"/>
      <stop offset="100%" stop-color="#6a2c70"/>
    </linearGradient>
    <radialGradient id="bodyGrad" cx="35%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#ffe066"/>
      <stop offset="45%" stop-color="#f4a261"/>
      <stop offset="80%" stop-color="#c14a3a"/>
      <stop offset="100%" stop-color="#7b2c21"/>
    </radialGradient>
    <linearGradient id="topGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e9c46a"/>
      <stop offset="100%" stop-color="#dda15e"/>
    </linearGradient>
    <linearGradient id="doorGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8b5a2b"/>
      <stop offset="100%" stop-color="#5c3a1e"/>
    </linearGradient>
    <radialGradient id="windowGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff3b0"/>
      <stop offset="70%" stop-color="#ffb703"/>
      <stop offset="100%" stop-color="#e85d04"/>
    </radialGradient>
    <linearGradient id="baseGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6c3e1d"/>
      <stop offset="100%" stop-color="#3e2210"/>
    </linearGradient>
  </defs>

  <!-- Cielo -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Luna -->
  <circle cx="330" cy="60" r="25" fill="#fff9c4" opacity="0.95"/>
  <circle cx="322" cy="54" r="5" fill="#f0e5a0" opacity="0.6"/>
  <circle cx="338" cy="68" r="4" fill="#f0e5a0" opacity="0.5"/>
  <circle cx="328" cy="66" r="3" fill="#f0e5a0" opacity="0.7"/>

  <!-- Estrellas -->
  <g fill="#ffffff" opacity="0.8">
    <circle cx="50" cy="50" r="1.5"/>
    <circle cx="120" cy="30" r="2"/>
    <circle cx="200" cy="60" r="1.5"/>
    <circle cx="280" cy="20" r="2.5"/>
    <circle cx="360" cy="110" r="1.8"/>
    <circle cx="30" cy="140" r="2"/>
    <circle cx="90" cy="100" r="1.5"/>
    <circle cx="320" cy="140" r="2"/>
    <circle cx="250" cy="100" r="1.5"/>
    <circle cx="150" cy="130" r="2"/>
  </g>

  <!-- Nubes de fondo -->
  <g fill="#ffffff" opacity="0.15">
    <circle cx="80" cy="300" r="40"/>
    <circle cx="120" cy="280" r="50"/>
    <circle cx="160" cy="300" r="45"/>
    <circle cx="320" cy="310" r="55"/>
    <circle cx="360" cy="290" r="40"/>
  </g>

  <!-- Cuerpo de la tetera -->
  <ellipse cx="200" cy="260" rx="140" ry="110" fill="url(#bodyGrad)" stroke="#4a1c0d" stroke-width="3"/>

  <!-- Base inferior -->
  <ellipse cx="200" cy="370" rx="70" ry="15" fill="url(#baseGrad)" stroke="#3e2210" stroke-width="2"/>

  <!-- Tapa -->
  <ellipse cx="200" cy="150" rx="90" ry="18" fill="url(#topGrad)" stroke="#4a1c0d" stroke-width="2"/>
  <ellipse cx="200" cy="148" rx="82" ry="12" fill="#f4a261" opacity="0.6"/>

  <!-- Pomo de la tapa -->
  <circle cx="200" cy="130" r="10" fill="#e76f51" stroke="#4a1c0d" stroke-width="2"/>
  <circle cx="197" cy="127" r="3" fill="#ffd166" opacity="0.8"/>

  <!-- Banderín -->
  <line x1="200" y1="130" x2="200" y2="95" stroke="#4a1c0d" stroke-width="2"/>
  <path d="M 200 95 L 220 100 L 200 105 Z" fill="#e63946" stroke="#4a1c0d" stroke-width="1"/>

  <!-- Chimenea -->
  <rect x="180" y="95" width="40" height="40" rx="3" fill="#a0522d" stroke="#4a1c0d" stroke-width="2"/>
  <ellipse cx="200" cy="95" rx="20" ry="7" fill="#caf0f8" stroke="#4a1c0d" stroke-width="1.5"/>

  <!-- Humo -->
  <path d="M 200 90 C 215 70, 180 60, 190 40 C 200 20, 170 15, 180 5" stroke="#ffffff" stroke-width="6" fill="none" opacity="0.35" stroke-linecap="round"/>

  <!-- Asa -->
  <path d="M 330 200 C 385 180, 395 255, 360 315 C 345 335, 320 330, 315 310 C 350 285, 350 215, 330 200 Z" fill="url(#bodyGrad)" stroke="#4a1c0d" stroke-width="2.5"/>

  <!-- Pico -->
  <path d="M 70 210 C 25 180, 15 130, 40 100 C 50 115, 65 150, 78 190 Z" fill="url(#bodyGrad)" stroke="#4a1c0d" stroke-width="2.5"/>

  <!-- Reloj en el cuerpo -->
  <circle cx="200" cy="210" r="20" fill="#fff3b0" stroke="#4a1c0d" stroke-width="2.5"/>
  <line x1="200" y1="210" x2="200" y2="195" stroke="#3e2723" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="200" y1="210" x2="210" y2="210" stroke="#3e2723" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="200" cy="210" r="2" fill="#3e2723"/>

  <!-- Puerta -->
  <path d="M 170 370 L 170 290 A 30 30 0 0 1 230 290 L 230 370 Z" fill="url(#doorGrad)" stroke="#3e2723" stroke-width="4"/>
  <line x1="200" y1="290" x2="200" y2="370" stroke="#3e2723" stroke-width="2" opacity="0.4"/>
  <line x1="170" y1="330" x2="230" y2="330" stroke="#3e2723" stroke-width="2" opacity="0.4"/>
  <circle cx="218" cy="335" r="4" fill="#ffd700" stroke="#3e2723" stroke-width="1.5"/>

  <!-- Letrero junto a la puerta -->
  <rect x="145" y="300" width="18" height="14" rx="2" fill="#dda15e" stroke="#3e2723" stroke-width="1.5"/>
  <circle cx="154" cy="306" r="3" fill="#e63946" stroke="#3e2723" stroke-width="1"/>

  <!-- Ventanas -->
  <circle cx="120" cy="240" r="22" fill="url(#windowGrad)" stroke="#4a1c0d" stroke-width="5"/>
  <line x1="98" y1="240" x2="142" y2="240" stroke="#4a1c0d" stroke-width="3"/>
  <line x1="120" y1="218" x2="120" y2="262" stroke="#4a1c0d" stroke-width="3"/>

  <circle cx="280" cy="240" r="22" fill="url(#windowGrad)" stroke="#4a1c0d" stroke-width="5"/>
  <line x1="258" y1="240" x2="302" y2="240" stroke="#4a1c0d" stroke-width="3"/>
  <line x1="280" y1="218" x2="280" y2="262" stroke="#4a1c0d" stroke-width="3"/>

  <!-- Enredadera decorativa -->
  <path d="M 95 320 Q 150 280 200 315 T 305 300" stroke="#2d6a4f" stroke-width="3" fill="none"/>
  <ellipse cx="130" cy="310" rx="5" ry="3" fill="#40916c" transform="rotate(-30 130 310)"/>
  <ellipse cx="180" cy="318" rx="5" ry="3" fill="#40916c" transform="rotate(20 180 318)"/>
  <ellipse cx="240" cy="312" rx="5" ry="3" fill="#40916c" transform="rotate(-15 240 312)"/>
  <ellipse cx="285" cy="305" rx="5" ry="3" fill="#40916c" transform="rotate(30 285 305)"/>

  <!-- Nubes de soporte debajo -->
  <g fill="#ffffff" opacity="0.55">
    <circle cx="120" cy="385" r="30"/>
    <circle cx="155" cy="380" r="25"/>
    <circle cx="190" cy="388" r="32"/>
    <circle cx="250" cy="382" r="28"/>
    <circle cx="290" cy="388" r="34"/>
    <circle cx="330" cy="380" r="26"/>
  </g>
  <g fill="#ffffff" opacity="0.35">
    <circle cx="100" cy="395" r="25"/>
    <circle cx="170" cy="398" r="22"/>
    <circle cx="230" cy="395" r="20"/>
    <circle cx="310" cy="398" r="24"/>
  </g>

  <!-- Escalera colgante -->
  <line x1="175" y1="370" x2="170" y2="400" stroke="#d4a373" stroke-width="3"/>
  <line x1="225" y1="370" x2="230" y2="400" stroke="#d4a373" stroke-width="3"/>
  <line x1="174" y1="378" x2="226" y2="378" stroke="#bc6c25" stroke-width="3" stroke-linecap="round"/>
  <line x1="173" y1="386" x2="227" y2="386" stroke="#bc6c25" stroke-width="3" stroke-linecap="round"/>
  <line x1="172" y1="394" x2="228" y2="394" stroke="#bc6c25" stroke-width="3" stroke-linecap="round"/>
</svg>