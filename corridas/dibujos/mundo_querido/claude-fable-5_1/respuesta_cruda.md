<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="cielo" cx="50%" cy="35%" r="80%">
      <stop offset="0%" stop-color="#bfe9ff"/>
      <stop offset="60%" stop-color="#8fd3f4"/>
      <stop offset="100%" stop-color="#6ab7e8"/>
    </radialGradient>
    <radialGradient id="sol" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff6c9"/>
      <stop offset="60%" stop-color="#ffe066"/>
      <stop offset="100%" stop-color="#ffc233"/>
    </radialGradient>
    <linearGradient id="mar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4fb6d8"/>
      <stop offset="100%" stop-color="#2a8bc0"/>
    </linearGradient>
    <linearGradient id="pasto" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#9ed86b"/>
      <stop offset="100%" stop-color="#5fb04a"/>
    </linearGradient>
  </defs>

  <!-- cielo -->
  <rect width="400" height="400" fill="url(#cielo)"/>

  <!-- sol -->
  <circle cx="320" cy="70" r="34" fill="url(#sol)"/>
  <g stroke="#ffd94d" stroke-width="4" stroke-linecap="round" opacity="0.8">
    <line x1="320" y1="20" x2="320" y2="8"/>
    <line x1="320" y1="120" x2="320" y2="132"/>
    <line x1="270" y1="70" x2="258" y2="70"/>
    <line x1="370" y1="70" x2="382" y2="70"/>
    <line x1="285" y1="35" x2="276" y2="26"/>
    <line x1="355" y1="105" x2="364" y2="114"/>
    <line x1="285" y1="105" x2="276" y2="114"/>
    <line x1="355" y1="35" x2="364" y2="26"/>
  </g>

  <!-- nubes -->
  <g fill="#ffffff" opacity="0.9">
    <ellipse cx="90" cy="60" rx="34" ry="14"/>
    <ellipse cx="115" cy="52" rx="24" ry="12"/>
    <ellipse cx="68" cy="52" rx="20" ry="10"/>
    <ellipse cx="210" cy="110" rx="26" ry="10"/>
    <ellipse cx="228" cy="104" rx="16" ry="8"/>
  </g>

  <!-- palomas -->
  <g stroke="#ffffff" stroke-width="3" fill="none" stroke-linecap="round">
    <path d="M140 90 q10 -10 20 0 q10 -10 20 0"/>
    <path d="M60 120 q8 -8 16 0 q8 -8 16 0"/>
    <path d="M250 60 q7 -7 14 0 q7 -7 14 0"/>
  </g>

  <!-- mar -->
  <path d="M0 250 Q100 238 200 250 T400 250 L400 400 L0 400 Z" fill="url(#mar)"/>
  <g stroke="#bfe9ff" stroke-width="2.5" fill="none" opacity="0.6" stroke-linecap="round">
    <path d="M40 285 q12 -6 24 0 q12 6 24 0"/>
    <path d="M300 300 q12 -6 24 0 q12 6 24 0"/>
    <path d="M180 320 q12 -6 24 0"/>
  </g>

  <!-- isla / colina verde -->
  <path d="M-20 400 Q60 230 200 240 Q340 232 420 400 Z" fill="url(#pasto)"/>
  <path d="M-20 400 Q80 300 200 310 Q320 300 420 400 Z" fill="#6fbd54"/>

  <!-- molino de viento -->
  <g>
    <rect x="76" y="182" width="6" height="72" fill="#f2f2f2" rx="3"/>
    <g fill="#ffffff" stroke="#dcdcdc" stroke-width="1">
      <path d="M79 182 L83 140 L75 140 Z"/>
      <path d="M79 182 L116 203 L112 210 Z"/>
      <path d="M79 182 L42 203 L46 210 Z"/>
    </g>
    <circle cx="79" cy="182" r="5" fill="#ffb347"/>
  </g>

  <!-- árboles -->
  <g>
    <rect x="296" y="222" width="8" height="26" fill="#8a5a33" rx="2"/>
    <circle cx="300" cy="206" r="22" fill="#4e9e3d"/>
    <circle cx="286" cy="216" r="14" fill="#63b24e"/>
    <circle cx="314" cy="216" r="14" fill="#63b24e"/>
    <circle cx="294" cy="202" r="3" fill="#ff6b6b"/>
    <circle cx="308" cy="210" r="3" fill="#ff6b6b"/>
    <circle cx="302" cy="196" r="3" fill="#ff6b6b"/>
  </g>
  <g>
    <rect x="348" y="250" width="6" height="20" fill="#8a5a33" rx="2"/>
    <circle cx="351" cy="240" r="16" fill="#58a847"/>
  </g>
  <g>
    <rect x="128" y="236" width="7" height="22" fill="#8a5a33" rx="2"/>
    <circle cx="131" cy="222" r="18" fill="#58a847"/>
    <circle cx="121" cy="230" r="11" fill="#6cbd57"/>
    <circle cx="141" cy="230" r="11" fill="#6cbd57"/>
  </g>

  <!-- casa con panel solar -->
  <g>
    <rect x="200" y="238" width="52" height="38" fill="#fff3e0" stroke="#e0c9a6" stroke-width="1.5"/>
    <path d="M194 240 L226 214 L258 240 Z" fill="#e2725b"/>
    <rect x="228" y="222" width="20" height="12" fill="#3a6ea5" transform="rotate(-20 238 228)" rx="1"/>
    <rect x="220" y="254" width="12" height="22" fill="#9b6a3f"/>
    <rect x="206" y="248" width="10" height="10" fill="#aee0f2" stroke="#e0c9a6"/>
    <rect x="238" y="248" width="10" height="10" fill="#aee0f2" stroke="#e0c9a6"/>
  </g>

  <!-- gente de la mano, diversa -->
  <g stroke-linecap="round">
    <!-- persona 1 -->
    <circle cx="120" cy="300" r="10" fill="#f1c27d"/>
    <path d="M120 310 L120 336 M120 318 L106 310 M120 318 L134 310 M120 336 L112 354 M120 336 L128 354" stroke="#e05c5c" stroke-width="6" fill="none"/>
    <!-- persona 2 -->
    <circle cx="160" cy="298" r="10" fill="#8d5524"/>
    <path d="M160 308 L160 334 M160 316 L146 310 M160 316 L174 310 M160 334 L152 352 M160 334 L168 352" stroke="#f2a93b" stroke-width="6" fill="none"/>
    <!-- persona 3 (niño) -->
    <circle cx="196" cy="310" r="8" fill="#ffdbac"/>
    <path d="M196 318 L196 338 M196 324 L184 316 M196 324 L208 316 M196 338 L190 352 M196 338 L202 352" stroke="#5b8dd9" stroke-width="5" fill="none"/>
    <!-- persona 4 -->
    <circle cx="232" cy="298" r="10" fill="#c68642"/>
    <path d="M232 308 L232 334 M232 316 L218 310 M232 316 L246 310 M232 334 L224 352 M232 334 L240 352" stroke="#7c5cc4" stroke-width="6" fill="none"/>
    <!-- persona 5 -->
    <circle cx="272" cy="300" r="10" fill="#f1c27d"/>
    <path d="M272 310 L272 336 M272 318 L258 310 M272 318 L286 310 M272 336 L264 354 M272 336 L280 354" stroke="#3aa47a" stroke-width="6" fill="none"/>
  </g>

  <!-- flores -->
  <g>
    <g transform="translate(60,330)">
      <line x1="0" y1="0" x2="0" y2="14" stroke="#4e9e3d" stroke-width="2"/>
      <circle cx="0" cy="-2" r="4" fill="#ff8fab"/><circle cx="-5" cy="2" r="4" fill="#ff8fab"/><circle cx="5" cy="2" r="4" fill="#ff8fab"/><circle cx="0" cy="5" r="4" fill="#ff8fab"/>
      <circle cx="0" cy="1" r="3" fill="#ffd166"/>
    </g>
    <g transform="translate(330,330)">
      <line x1="0" y1="0" x2="0" y2="14" stroke="#4e9e3d" stroke-width="2"/>
      <circle cx="0" cy="-2" r="4" fill="#c77dff"/><circle cx="-5" cy="2" r="4" fill="#c77dff"/><circle cx="5" cy="2" r="4" fill="#c77dff"/><circle cx="0" cy="5" r="4" fill="#c77dff"/>
      <circle cx="0" cy="1" r="3" fill="#ffd166"/>
    </g>
    <g transform="translate(300,360)">
      <line x1="0" y1="0" x2="0" y2="12" stroke="#4e9e3d" stroke-width="2"/>
      <circle cx="0" cy="-2" r="3.5" fill="#ffd166"/><circle cx="-4" cy="2" r="3.5" fill="#ffd166"/><circle cx="4" cy="2" r="3.5" fill="#ffd166"/><circle cx="0" cy="4" r="3.5" fill="#ffd166"/>
      <circle cx="0" cy="1" r="2.5" fill="#e05c5c"/>
    </g>
    <g transform="translate(96,362)">
      <line x1="0" y1="0" x2="0" y2="12" stroke="#4e9e3d" stroke-width="2"/>
      <circle cx="0" cy="-2" r="3.5" fill="#ffffff"/><circle cx="-4" cy="2" r="3.5" fill="#ffffff"/><circle cx="4" cy="2" r="3.5" fill="#ffffff"/><circle cx="0" cy="4" r="3.5" fill="#ffffff"/>
      <circle cx="0" cy="1" r="2.5" fill="#ffd166"/>
    </g>
  </g>

  <!-- arcoíris suave -->
  <g fill="none" opacity="0.55" stroke-linecap="round">
    <path d="M20 180 Q110 100 200 170" stroke="#ff6b6b" stroke-width="6"/>
    <path d="M24 188 Q110 112 196 178" stroke="#ffd166" stroke-width="6"/>
    <path d="M28 196 Q110 124 192 186" stroke="#6fbd54" stroke-width="6"/>
    <path d="M32 204 Q110 136 188 194" stroke="#5b8dd9" stroke-width="6"/>
  </g>

  <!-- corazón sobre la gente -->
  <path d="M196 268 c-4 -8 -16 -6 -16 3 c0 7 10 12 16 17 c6 -5 16 -10 16 -17 c0 -9 -12 -11 -16 -3 Z" fill="#ff5e7e" opacity="0.9"/>
</svg>