<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#1b2a4a"/>
      <stop offset="55%" stop-color="#0d1526"/>
      <stop offset="100%" stop-color="#05080f"/>
    </radialGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4fd7d2" stop-opacity="0.30"/>
      <stop offset="60%" stop-color="#3b7fd4" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.10"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#7ef2ea"/>
      <stop offset="50%" stop-color="#6aa8f7"/>
      <stop offset="100%" stop-color="#b98cf9"/>
    </linearGradient>
    <radialGradient id="eyeG">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="35%" stop-color="#9ff4ff"/>
      <stop offset="100%" stop-color="#2b6fd6" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="8"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- halo -->
  <ellipse cx="200" cy="195" rx="120" ry="140" fill="#2f6bd8" opacity="0.18" filter="url(#soft)"/>

  <!-- faint grid -->
  <g stroke="#6aa8f7" stroke-width="0.4" opacity="0.10">
    <path d="M0 60H400M0 120H400M0 180H400M0 240H400M0 300H400M0 360H400"/>
    <path d="M60 0V400M120 0V400M180 0V400M240 0V400M300 0V400M360 0V400"/>
  </g>

  <!-- shoulders -->
  <path d="M60 400c8-52 45-78 88-90 18-5 86-5 104 0 43 12 80 38 88 90z"
        fill="url(#face)" stroke="url(#edge)" stroke-width="1.2" opacity="0.85"/>
  <path d="M148 312c14 26 38 40 52 40s38-14 52-40" fill="none" stroke="url(#edge)" stroke-width="1" opacity="0.5"/>

  <!-- neck -->
  <path d="M176 262h48v40c0 12-48 12-48 0z" fill="url(#face)" stroke="url(#edge)" stroke-width="1" opacity="0.8"/>

  <!-- head -->
  <path d="M200 60c-48 0-78 32-78 78 0 34 8 56 22 76 12 17 30 32 56 32s44-15 56-32c14-20 22-42 22-76 0-46-30-78-78-78z"
        fill="url(#face)" stroke="url(#edge)" stroke-width="1.6" filter="url(#glow)"/>

  <!-- circuitry inside head -->
  <g stroke="url(#edge)" stroke-width="0.7" fill="none" opacity="0.45">
    <path d="M136 120h26v-22h34"/>
    <path d="M264 128h-24v26h-18"/>
    <path d="M140 196h22v30h-16"/>
    <path d="M262 200h-20v34h24"/>
    <path d="M200 84v-18"/>
    <path d="M168 250h64"/>
  </g>

  <!-- ears / ports -->
  <path d="M122 150c-10 2-14 12-12 24 2 12 10 18 18 16" fill="none" stroke="url(#edge)" stroke-width="1.4"/>
  <path d="M278 150c10 2 14 12 12 24-2 12-10 18-18 16" fill="none" stroke="url(#edge)" stroke-width="1.4"/>

  <!-- eyes -->
  <g>
    <ellipse cx="168" cy="160" rx="26" ry="20" fill="url(#eyeG)" opacity="0.55"/>
    <ellipse cx="232" cy="160" rx="26" ry="20" fill="url(#eyeG)" opacity="0.55"/>
    <path d="M150 160c6-11 30-11 36 0-6 11-30 11-36 0z" fill="#081120" stroke="url(#edge)" stroke-width="1.3"/>
    <path d="M214 160c6-11 30-11 36 0-6 11-30 11-36 0z" fill="#081120" stroke="url(#edge)" stroke-width="1.3"/>
    <circle cx="168" cy="160" r="5.4" fill="#9ff4ff" filter="url(#glow)"/>
    <circle cx="232" cy="160" r="5.4" fill="#9ff4ff" filter="url(#glow)"/>
    <circle cx="170" cy="158" r="1.6" fill="#fff"/>
    <circle cx="234" cy="158" r="1.6" fill="#fff"/>
  </g>

  <!-- brow lines -->
  <path d="M144 141c14-8 32-9 44-5" fill="none" stroke="url(#edge)" stroke-width="1.6" opacity="0.8"/>
  <path d="M256 141c-14-8-32-9-44-5" fill="none" stroke="url(#edge)" stroke-width="1.6" opacity="0.8"/>

  <!-- nose -->
  <path d="M200 170v28l-9 8 9 4 9-4" fill="none" stroke="url(#edge)" stroke-width="1.2" opacity="0.7"/>

  <!-- mouth: waveform smile -->
  <g filter="url(#glow)">
    <path d="M166 232q10 6 14 0t9 9 9-14 9 16 9-11 9 6 9-6"
          fill="none" stroke="#7ef2ea" stroke-width="2" stroke-linecap="round"/>
  </g>
  <path d="M164 228q36 26 72 0" fill="none" stroke="url(#edge)" stroke-width="0.8" opacity="0.35"/>

  <!-- crown nodes -->
  <g fill="#9ff4ff">
    <circle cx="200" cy="62" r="3.4" filter="url(#glow)"/>
    <circle cx="160" cy="72" r="2.2"/>
    <circle cx="240" cy="72" r="2.2"/>
    <circle cx="130" cy="104" r="2"/>
    <circle cx="270" cy="104" r="2"/>
  </g>
  <g stroke="url(#edge)" stroke-width="0.8" opacity="0.6" fill="none">
    <path d="M130 104 160 72 200 62 240 72 270 104"/>
  </g>

  <!-- floating network around -->
  <g opacity="0.55">
    <g stroke="url(#edge)" stroke-width="0.6" fill="none" opacity="0.7">
      <path d="M46 96 78 62 116 78"/>
      <path d="M78 62 70 130 40 168"/>
      <path d="M354 96 322 62 284 80"/>
      <path d="M322 62 332 132 362 172"/>
      <path d="M40 168 62 226"/>
      <path d="M362 172 340 228"/>
    </g>
    <g fill="#7ef2ea">
      <circle cx="46" cy="96" r="2.4"/><circle cx="78" cy="62" r="3"/>
      <circle cx="116" cy="78" r="2"/><circle cx="70" cy="130" r="2.4"/>
      <circle cx="40" cy="168" r="2"/><circle cx="62" cy="226" r="2.4"/>
      <circle cx="354" cy="96" r="2.4"/><circle cx="322" cy="62" r="3"/>
      <circle cx="284" cy="80" r="2"/><circle cx="332" cy="132" r="2.4"/>
      <circle cx="362" cy="172" r="2"/><circle cx="340" cy="228" r="2.4"/>
    </g>
  </g>

  <!-- binary whispers -->
  <g fill="#6aa8f7" opacity="0.35" font-family="monospace" font-size="9">
    <text x="26" y="290">01001000</text>
    <text x="300" y="300">01101001</text>
    <text x="34" y="60">1010</text>
    <text x="336" y="56">0110</text>
  </g>

  <!-- chest node -->
  <circle cx="200" cy="356" r="12" fill="none" stroke="url(#edge)" stroke-width="1.2" opacity="0.8"/>
  <circle cx="200" cy="356" r="4" fill="#9ff4ff" filter="url(#glow)"/>

  <rect x="4" y="4" width="392" height="392" rx="10" fill="none" stroke="#6aa8f7" stroke-width="0.8" opacity="0.28"/>
</svg>