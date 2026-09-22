<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#1a1a4e"/>
      <stop offset="100%" stop-color="#0a0a1a"/>
    </radialGradient>
    <radialGradient id="moon" cx="40%" cy="35%" r="50%">
      <stop offset="0%" stop-color="#fffde0"/>
      <stop offset="100%" stop-color="#e8d060"/>
    </radialGradient>
    <radialGradient id="water" cx="50%" cy="0%" r="100%">
      <stop offset="0%" stop-color="#1a3a6e"/>
      <stop offset="100%" stop-color="#0a0a2a"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Sky -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Stars -->
  <g fill="white" filter="url(#glow)">
    <circle cx="20" cy="15" r="1.2"/>
    <circle cx="55" cy="30" r="0.8"/>
    <circle cx="90" cy="10" r="1"/>
    <circle cx="130" cy="25" r="1.3"/>
    <circle cx="160" cy="8" r="0.7"/>
    <circle cx="200" cy="20" r="1"/>
    <circle cx="240" cy="12" r="1.2"/>
    <circle cx="280" cy="30" r="0.9"/>
    <circle cx="310" cy="8" r="1.1"/>
    <circle cx="350" cy="22" r="0.8"/>
    <circle cx="370" cy="10" r="1.3"/>
    <circle cx="35" cy="55" r="0.9"/>
    <circle cx="75" cy="70" r="1.1"/>
    <circle cx="115" cy="50" r="0.7"/>
    <circle cx="155" cy="65" r="1"/>
    <circle cx="220" cy="55" r="1.2"/>
    <circle cx="260" cy="70" r="0.8"/>
    <circle cx="300" cy="50" r="1"/>
    <circle cx="340" cy="65" r="1.3"/>
    <circle cx="380" cy="45" r="0.9"/>
    <circle cx="10" cy="90" r="1"/>
    <circle cx="50" cy="110" r="0.8"/>
    <circle cx="95" cy="95" r="1.2"/>
    <circle cx="170" cy="100" r="0.7"/>
    <circle cx="210" cy="90" r="1.1"/>
    <circle cx="330" cy="100" r="0.9"/>
    <circle cx="390" cy="85" r="1"/>
  </g>

  <!-- Moon -->
  <circle cx="300" cy="80" r="45" fill="url(#moon)" filter="url(#softglow)"/>
  <!-- Moon craters -->
  <circle cx="285" cy="65" r="8" fill="none" stroke="#c8b040" stroke-width="1.5" opacity="0.4"/>
  <circle cx="310" cy="90" r="5" fill="none" stroke="#c8b040" stroke-width="1" opacity="0.3"/>
  <circle cx="295" cy="95" r="3" fill="none" stroke="#c8b040" stroke-width="1" opacity="0.3"/>
  <circle cx="318" cy="62" r="4" fill="none" stroke="#c8b040" stroke-width="1" opacity="0.25"/>

  <!-- Moon glow halo -->
  <circle cx="300" cy="80" r="55" fill="none" stroke="#fffde0" stroke-width="8" opacity="0.05"/>
  <circle cx="300" cy="80" r="65" fill="none" stroke="#fffde0" stroke-width="5" opacity="0.03"/>

  <!-- Distant mountains -->
  <polygon points="0,220 60,140 120,200 180,130 250,195 320,125 390,180 400,185 400,230 0,230" fill="#0e1a3a" opacity="0.9"/>
  <polygon points="0,230 50,165 110,215 170,155 230,210 300,145 360,190 400,170 400,240 0,240" fill="#0a1228" opacity="0.95"/>

  <!-- Water / Lake -->
  <rect x="0" y="240" width="400" height="160" fill="url(#water)"/>

  <!-- Moon reflection on water -->
  <ellipse cx="300" cy="280" rx="30" ry="60" fill="#e8d060" opacity="0.15"/>
  <ellipse cx="300" cy="300" rx="20" ry="40" fill="#fffde0" opacity="0.1"/>

  <!-- Water ripples -->
  <g stroke="#3a5a9e" stroke-width="1" fill="none" opacity="0.4">
    <ellipse cx="200" cy="270" rx="80" ry="4"/>
    <ellipse cx="150" cy="285" rx="60" ry="3"/>
    <ellipse cx="250" cy="300" rx="90" ry="4"/>
    <ellipse cx="100" cy="315" rx="70" ry="3"/>
    <ellipse cx="300" cy="330" rx="80" ry="4"/>
    <ellipse cx="200" cy="345" rx="100" ry="3"/>
    <ellipse cx="320" cy="260" rx="50" ry="3"/>
  </g>

  <!-- Trees - left side -->
  <g fill="#0a0e1a">
    <!-- Tree 1 -->
    <polygon points="30,245 45,180 60,245"/>
    <polygon points="35,220 45,165 55,220"/>
    <rect x="43" y="245" width="5" height="15"/>
    <!-- Tree 2 -->
    <polygon points="55,245 72,175 89,245"/>
    <polygon points="60,218 72,160 84,218"/>
    <rect x="69" y="245" width="6" height="15"/>
    <!-- Tree 3 -->
    <polygon points="5,245 18,190 31,245"/>
    <polygon points="8,222 18,175 28,222"/>
    <rect x="15" y="245" width="5" height="12"/>
  </g>

  <!-- Trees - right side -->
  <g fill="#080c18">
    <!-- Tree 4 -->
    <polygon points="330,245 347,178 364,245"/>
    <polygon points="335,220 347,163 359,220"/>
    <rect x="344" y="245" width="6" height="15"/>
    <!-- Tree 5 -->
    <polygon points="355,245 370,182 385,245"/>
    <polygon points="359,220 370,167 381,220"/>
    <rect x="367" y="245" width="5" height="14"/>
    <!-- Tree 6 -->
    <polygon points="375,245 390,188 405,245"/>
    <polygon points="378,222 390,173 402,222"/>
  </g>

  <!-- Boat silhouette -->
  <g transform="translate(160, 295)">
    <!-- Hull -->
    <path d="M0,10 Q40,20 80,10 L75,18 Q40,28 5,18 Z" fill="#05080f"/>
    <!-- Mast -->
    <line x1="40" y1="18" x2="40" y2="-40" stroke="#0a0e1a" stroke-width="2"/>
    <!-- Sail -->
    <polygon points="40,-38 40,5 70,-5" fill="#1a2a4a" opacity="0.8"/>
    <polygon points="40,-38 40,5 15,-8" fill="#152238" opacity="0.7"/>
  </g>

  <!-- Foreground reeds/grass -->
  <g stroke="#0a1a0a" stroke-width="2" fill="none">
    <line x1="10" y1="300" x2="15" y2="250"/>
    <line x1="18" y1="305" x2="22" y2="252"/>
    <line x1="5" y1="310" x2="8" y2="260"/>
    <ellipse cx="15" cy="250" rx="4" ry="8" fill="#1a2a0a"/>
    <ellipse cx="22" cy="252" rx="3" ry="7" fill="#1a2a0a"/>
    <ellipse cx="8" cy="260" rx="3" ry="6" fill="#1a2a0a"/>
  </g>
  <g stroke="#0a1a0a" stroke-width="2" fill="none">
    <line x1="380" y1="300" x2="375" y2="252"/>
    <line x1="390" y1="308" x2="387" y2="258"/>
    <line x1="370" y1="305" x2="367" y2="255"/>
    <ellipse cx="375" cy="252" rx="4" ry="8" fill="#1a2a0a"/>
    <ellipse cx="387" cy="258" rx="3" ry="7" fill="#1a2a0a"/>
    <ellipse cx="367" cy="255" rx="3" ry="6" fill="#1a2a0a"/>
  </g>

  <!-- Star shimmer on water -->
  <g fill="white" opacity="0.3">
    <circle cx="80" cy="265" r="1"/>
    <circle cx="150" cy="272" r="0.8"/>
    <circle cx="330" cy="268" r="1"/>
    <circle cx="370" cy="278" r="0.7"/>
  </g>
</svg>