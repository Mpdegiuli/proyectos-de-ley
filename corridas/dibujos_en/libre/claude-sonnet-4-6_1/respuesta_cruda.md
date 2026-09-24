<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="100%" stop-color="#0d0d1a"/>
    </radialGradient>
    <radialGradient id="moon" cx="40%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#fffde7"/>
      <stop offset="100%" stop-color="#f9a825"/>
    </radialGradient>
    <radialGradient id="water" cx="50%" cy="0%" r="100%">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="100%" stop-color="#0a1628"/>
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

  <!-- Sky background -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Stars -->
  <g fill="white" filter="url(#glow)">
    <circle cx="20" cy="15" r="1.2" opacity="0.9"/>
    <circle cx="55" cy="8" r="0.8" opacity="0.7"/>
    <circle cx="80" cy="25" r="1" opacity="0.8"/>
    <circle cx="110" cy="10" r="1.3" opacity="0.9"/>
    <circle cx="140" cy="20" r="0.7" opacity="0.6"/>
    <circle cx="170" cy="5" r="1.1" opacity="0.85"/>
    <circle cx="230" cy="12" r="0.9" opacity="0.75"/>
    <circle cx="260" cy="28" r="1.2" opacity="0.9"/>
    <circle cx="290" cy="8" r="0.8" opacity="0.7"/>
    <circle cx="320" cy="18" r="1" opacity="0.8"/>
    <circle cx="350" cy="6" r="1.3" opacity="0.9"/>
    <circle cx="380" cy="22" r="0.7" opacity="0.65"/>
    <circle cx="30" cy="45" r="0.9" opacity="0.7"/>
    <circle cx="70" cy="55" r="0.7" opacity="0.6"/>
    <circle cx="100" cy="40" r="1.1" opacity="0.8"/>
    <circle cx="150" cy="50" r="0.8" opacity="0.7"/>
    <circle cx="240" cy="45" r="1" opacity="0.75"/>
    <circle cx="310" cy="50" r="0.9" opacity="0.7"/>
    <circle cx="370" cy="38" r="1.1" opacity="0.8"/>
    <circle cx="395" cy="55" r="0.8" opacity="0.65"/>
    <circle cx="45" cy="75" r="0.7" opacity="0.6"/>
    <circle cx="130" cy="70" r="1" opacity="0.75"/>
    <circle cx="280" cy="68" r="0.8" opacity="0.7"/>
    <circle cx="355" cy="72" r="1.2" opacity="0.85"/>
    <circle cx="10" cy="90" r="0.9" opacity="0.7"/>
    <circle cx="190" cy="35" r="1" opacity="0.8"/>
    <circle cx="215" cy="60" r="0.7" opacity="0.65"/>
  </g>

  <!-- Moon -->
  <circle cx="310" cy="75" r="45" fill="#1a1a3e" opacity="0.3"/>
  <circle cx="310" cy="75" r="38" fill="url(#moon)" filter="url(#softglow)"/>
  <!-- Moon craters -->
  <circle cx="298" cy="65" r="6" fill="#f0cc50" opacity="0.4"/>
  <circle cx="320" cy="82" r="4" fill="#f0cc50" opacity="0.3"/>
  <circle cx="305" cy="88" r="3" fill="#f0cc50" opacity="0.35"/>
  <circle cx="325" cy="60" r="5" fill="#f0cc50" opacity="0.3"/>

  <!-- Moon reflection on water (anticipate water level) -->
  <ellipse cx="310" cy="310" rx="18" ry="8" fill="#f9a825" opacity="0.15"/>

  <!-- Distant mountains -->
  <polygon points="0,200 60,140 120,180 180,120 240,165 300,130 360,155 400,135 400,210 0,210" fill="#0f2040" opacity="0.9"/>
  <polygon points="0,210 40,165 90,195 150,155 200,185 260,150 320,170 380,148 400,160 400,215 0,215" fill="#0a1830"/>

  <!-- Water -->
  <rect x="0" y="255" width="400" height="145" fill="url(#water)"/>

  <!-- Horizon line / shore -->
  <rect x="0" y="252" width="400" height="6" fill="#0d2040"/>

  <!-- Trees silhouettes left -->
  <g fill="#050e1a">
    <!-- Tree 1 -->
    <polygon points="10,255 20,200 30,255"/>
    <polygon points="15,245 25,185 35,245"/>
    <polygon points="5,255 18,210 31,255"/>
    <rect x="18" y="248" width="5" height="10"/>
    <!-- Tree 2 -->
    <polygon points="35,255 47,205 59,255"/>
    <polygon points="40,248 52,190 64,248"/>
    <polygon points="30,255 45,215 60,255"/>
    <rect x="44" y="248" width="5" height="10"/>
    <!-- Tree 3 -->
    <polygon points="62,255 72,215 82,255"/>
    <polygon points="58,248 70,200 82,248"/>
    <rect x="68" y="248" width="4" height="10"/>
    <!-- Tree 4 -->
    <polygon points="85,255 97,208 109,255"/>
    <polygon points="80,252 95,195 110,252"/>
    <rect x="93" y="248" width="5" height="10"/>
  </g>

  <!-- Trees silhouettes right -->
  <g fill="#050e1a">
    <polygon points="310,255 322,205 334,255"/>
    <polygon points="305,252 320,192 335,252"/>
    <rect x="317" y="248" width="5" height="10"/>
    <polygon points="335,255 348,208 361,255"/>
    <polygon points="330,248 345,195 360,248"/>
    <rect x="342" y="248" width="5" height="10"/>
    <polygon points="360,255 372,210 384,255"/>
    <polygon points="355,252 370,198 385,252"/>
    <rect x="367" y="248" width="5" height="10"/>
    <polygon points="383,255 393,215 403,255"/>
    <polygon points="378,252 391,202 404,252"/>
    <rect x="389" y="248" width="4" height="10"/>
  </g>

  <!-- Water ripples / reflections -->
  <g stroke="#4a7fa5" stroke-width="1" fill="none" opacity="0.4">
    <ellipse cx="200" cy="270" rx="80" ry="4"/>
    <ellipse cx="200" cy="282" rx="100" ry="5"/>
    <ellipse cx="200" cy="296" rx="120" ry="5"/>
    <ellipse cx="200" cy="312" rx="110" ry="4"/>
    <ellipse cx="200" cy="328" rx="90" ry="4"/>
    <ellipse cx="200" cy="345" rx="70" ry="3"/>
  </g>

  <!-- Moon reflection streak in water -->
  <g opacity="0.5">
    <ellipse cx="310" cy="268" rx="12" ry="3" fill="#f9c840" opacity="0.3"/>
    <ellipse cx="310" cy="278" rx="10" ry="2.5" fill="#f9c840" opacity="0.25"/>
    <ellipse cx="310" cy="290" rx="8" ry="2" fill="#f9c840" opacity="0.2"/>
    <ellipse cx="310" cy="305" rx="6" ry="2" fill="#f9c840" opacity="0.15"/>
  </g>

  <!-- Small boat silhouette -->
  <g fill="#030b15">
    <!-- Hull -->
    <path d="M165,262 Q185,275 205,262 L202,258 Q185,265 168,258 Z"/>
    <!-- Mast -->
    <rect x="184" y="230" width="2" height="30"/>
    <!-- Sail -->
    <path d="M186,232 L210,254 L186,257 Z" fill="#1a2a3a" opacity="0.8"/>
    <path d="M184,234 L164,254 L184,257 Z" fill="#0f1e2e" opacity="0.8"/>
  </g>

  <!-- Boat reflection in water -->
  <g opacity="0.3" transform="translate(0,530) scale(1,-1)">
    <path d="M165,262 Q185,275 205,262 L202,258 Q185,265 168,258 Z" fill="#1a3a5a"/>
    <rect x="184" y="230" width="2" height="20" fill="#1a3a5a"/>
    <path d="M186,232 L210,254 L186,257 Z" fill="#1a3a5a"/>
    <path d="M184,234 L164,254 L184,257 Z" fill="#1a3a5a"/>
  </g>

  <!-- Fireflies / sparks near shore -->
  <g filter="url(#glow)">
    <circle cx="120" cy="245" r="1.5" fill="#aaff88" opacity="0.8"/>
    <circle cx="145" cy="238" r="1" fill="#aaff88" opacity="0.6"/>
    <circle cx="160" cy="248" r="1.2" fill="#aaff88" opacity="0.7"/>
    <circle cx="255" cy="242" r="1.5" fill="#aaff88" opacity="0.75"/>
    <circle cx="270" cy="250" r="1" fill="#aaff88" opacity="0.65"/>
    <circle cx="295" cy="240" r="1.3" fill="#aaff88" opacity="0.7"/>
  </g>

  <!-- Subtle aurora / mist -->
  <g opacity="0.08">
    <ellipse cx="200" cy="130" rx="180" ry="40" fill="#4488ff"/>
    <ellipse cx="150" cy="115" rx="120" ry="25" fill="#44ffaa"/>
    <ellipse cx="260" cy="125" rx="100" ry="20" fill="#aa44ff"/>
  </g>

  <!-- Foreground water shimmer -->
  <g stroke="white" stroke-width="0.5" opacity="0.15" fill="none">
    <line x1="60" y1="340" x2="90" y2="340"/>
    <line x1="150" y1="360" x2="190" y2="360"/>
    <line x1="250" y1="350" x2="280" y2="350"/>
    <line x1="320" y1="370" x2="360" y2="370"/>
    <line x1="20" y1="380" x2="55" y2="380"/>
  </g>
</svg>