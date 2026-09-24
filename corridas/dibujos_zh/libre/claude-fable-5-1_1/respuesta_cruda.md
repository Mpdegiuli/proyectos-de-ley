<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0b1a3a"/>
      <stop offset="0.5" stop-color="#3a4d8f"/>
      <stop offset="0.85" stop-color="#e8875a"/>
      <stop offset="1" stop-color="#f7c88a"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f0b07a"/>
      <stop offset="0.3" stop-color="#5a5f9a"/>
      <stop offset="1" stop-color="#0d1533"/>
    </linearGradient>
    <linearGradient id="mtn1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4a5a8c"/>
      <stop offset="1" stop-color="#232c55"/>
    </linearGradient>
    <linearGradient id="mtn2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2c3564"/>
      <stop offset="1" stop-color="#151c3e"/>
    </linearGradient>
    <radialGradient id="moon" cx="0.4" cy="0.4" r="0.7">
      <stop offset="0" stop-color="#fffbe8"/>
      <stop offset="1" stop-color="#f2d9a0"/>
    </radialGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffe8b0" stop-opacity="0.5"/>
      <stop offset="1" stop-color="#ffe8b0" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="1.2"/></filter>
  </defs>

  <!-- Sky -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Stars -->
  <g fill="#fff">
    <circle cx="30" cy="40" r="1.2"/>
    <circle cx="70" cy="22" r="0.8"/>
    <circle cx="120" cy="55" r="1"/>
    <circle cx="160" cy="18" r="1.3"/>
    <circle cx="210" cy="45" r="0.9"/>
    <circle cx="250" cy="25" r="1.1"/>
    <circle cx="330" cy="30" r="1"/>
    <circle cx="370" cy="60" r="0.8"/>
    <circle cx="45" cy="90" r="0.8"/>
    <circle cx="95" cy="110" r="0.7"/>
    <circle cx="190" cy="85" r="0.9"/>
    <circle cx="350" cy="105" r="1"/>
    <circle cx="140" cy="130" r="0.6"/>
    <circle cx="280" cy="70" r="0.7"/>
    <circle cx="20" cy="140" r="0.7"/>
    <circle cx="385" cy="20" r="1.2"/>
  </g>

  <!-- Moon -->
  <circle cx="300" cy="80" r="60" fill="url(#glow)"/>
  <circle cx="300" cy="80" r="26" fill="url(#moon)"/>
  <circle cx="290" cy="72" r="4" fill="#e6cf95" opacity="0.5"/>
  <circle cx="308" cy="90" r="3" fill="#e6cf95" opacity="0.5"/>
  <circle cx="306" cy="70" r="2" fill="#e6cf95" opacity="0.4"/>

  <!-- Distant mountains -->
  <path d="M0 230 L40 190 L80 215 L130 160 L170 205 L210 175 L250 210 L300 170 L340 205 L400 165 L400 260 L0 260 Z" fill="url(#mtn1)"/>
  <!-- Snow caps -->
  <path d="M130 160 L120 175 L128 172 L134 178 L142 170 L150 176 L130 160Z" fill="#dfe6f5" opacity="0.8"/>
  <path d="M300 170 L292 182 L299 179 L305 185 L312 178 L300 170Z" fill="#dfe6f5" opacity="0.8"/>

  <!-- Near mountains -->
  <path d="M0 270 L60 215 L110 250 L160 205 L220 255 L270 220 L330 260 L370 235 L400 255 L400 280 L0 280 Z" fill="url(#mtn2)"/>

  <!-- Water -->
  <rect x="0" y="260" width="400" height="140" fill="url(#water)"/>

  <!-- Mountain reflections -->
  <g opacity="0.35">
    <path d="M0 270 L60 325 L110 290 L160 335 L220 285 L270 320 L330 280 L370 305 L400 285 L400 260 L0 260 Z" fill="#151c3e" filter="url(#blur)"/>
  </g>

  <!-- Moon reflection -->
  <g fill="#f7d9a0" opacity="0.6">
    <rect x="285" y="268" width="30" height="2" rx="1"/>
    <rect x="280" y="276" width="42" height="2" rx="1"/>
    <rect x="288" y="285" width="24" height="2" rx="1"/>
    <rect x="278" y="295" width="46" height="1.8" rx="1"/>
    <rect x="290" y="306" width="22" height="1.6" rx="1"/>
    <rect x="283" y="318" width="34" height="1.5" rx="1"/>
    <rect x="292" y="332" width="18" height="1.4" rx="1"/>
    <rect x="286" y="348" width="26" height="1.2" rx="1"/>
  </g>

  <!-- Water ripples -->
  <g stroke="#8fa0d8" stroke-width="1" opacity="0.3" fill="none">
    <path d="M20 300 Q40 298 60 300 T100 300"/>
    <path d="M140 320 Q160 318 180 320 T220 320"/>
    <path d="M60 350 Q80 348 100 350 T140 350"/>
    <path d="M200 365 Q220 363 240 365 T280 365"/>
    <path d="M330 340 Q350 338 370 340 T400 340"/>
  </g>

  <!-- Boat -->
  <g>
    <path d="M150 318 Q175 328 200 318 L195 310 L155 310 Z" fill="#1a1626"/>
    <rect x="174" y="270" width="2" height="40" fill="#1a1626"/>
    <path d="M176 272 L196 300 L176 300 Z" fill="#2a2440"/>
    <path d="M174 275 L160 300 L174 300 Z" fill="#221d36"/>
    <!-- lantern -->
    <circle cx="192" cy="306" r="2.5" fill="#ffc46b"/>
    <circle cx="192" cy="306" r="6" fill="#ffc46b" opacity="0.25"/>
    <!-- fisherman -->
    <circle cx="165" cy="302" r="3" fill="#1a1626"/>
    <path d="M161 305 L169 305 L170 311 L160 311 Z" fill="#1a1626"/>
    <line x1="168" y1="303" x2="200" y2="285" stroke="#1a1626" stroke-width="1"/>
    <line x1="200" y1="285" x2="201" y2="312" stroke="#8fa0d8" stroke-width="0.5" opacity="0.6"/>
  </g>

  <!-- Boat reflection -->
  <g opacity="0.3" filter="url(#blur)">
    <path d="M150 322 Q175 312 200 322 L195 330 L155 330 Z" fill="#1a1626"/>
    <path d="M176 368 L196 340 L176 340 Z" fill="#2a2440"/>
    <circle cx="192" cy="334" r="3" fill="#ffc46b"/>
  </g>

  <!-- Foreground reeds -->
  <g stroke="#0a0f24" stroke-width="2" fill="none" stroke-linecap="round">
    <path d="M20 400 Q22 360 18 330"/>
    <path d="M32 400 Q36 350 30 320"/>
    <path d="M45 400 Q44 365 50 340"/>
    <path d="M370 400 Q374 355 368 325"/>
    <path d="M385 400 Q382 370 390 345"/>
    <path d="M355 400 Q352 375 358 355"/>
  </g>
  <g fill="#0a0f24">
    <ellipse cx="18" cy="328" rx="2.5" ry="9"/>
    <ellipse cx="30" cy="318" rx="2.5" ry="9"/>
    <ellipse cx="368" cy="323" rx="2.5" ry="9"/>
    <ellipse cx="390" cy="343" rx="2" ry="7"/>
  </g>

  <!-- Birds -->
  <g stroke="#0b1a3a" stroke-width="1.2" fill="none" stroke-linecap="round">
    <path d="M90 150 Q95 145 100 150 Q105 145 110 150"/>
    <path d="M115 140 Q119 136 123 140 Q127 136 131 140"/>
    <path d="M75 165 Q78 162 81 165 Q84 162 87 165"/>
  </g>
</svg>