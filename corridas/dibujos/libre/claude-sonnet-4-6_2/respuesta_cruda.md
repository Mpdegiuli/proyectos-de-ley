<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#1a1a4e"/>
      <stop offset="100%" stop-color="#0a0a1a"/>
    </radialGradient>
    <radialGradient id="moon" cx="40%" cy="35%" r="55%">
      <stop offset="0%" stop-color="#fffde0"/>
      <stop offset="100%" stop-color="#c8b860"/>
    </radialGradient>
    <radialGradient id="water" cx="50%" cy="0%" r="100%">
      <stop offset="0%" stop-color="#1a2a5e"/>
      <stop offset="100%" stop-color="#050a15"/>
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
    <circle cx="30" cy="20" r="1.2"/>
    <circle cx="75" cy="45" r="0.8"/>
    <circle cx="120" cy="15" r="1.5"/>
    <circle cx="160" cy="35" r="0.9"/>
    <circle cx="200" cy="10" r="1.1"/>
    <circle cx="250" cy="30" r="0.7"/>
    <circle cx="300" cy="18" r="1.3"/>
    <circle cx="350" cy="40" r="0.9"/>
    <circle cx="380" cy="12" r="1.2"/>
    <circle cx="55" cy="70" r="0.8"/>
    <circle cx="95" cy="90" r="1.0"/>
    <circle cx="145" cy="65" r="0.7"/>
    <circle cx="185" cy="80" r="1.1"/>
    <circle cx="230" cy="55" r="0.8"/>
    <circle cx="275" cy="75" r="0.9"/>
    <circle cx="320" cy="60" r="1.2"/>
    <circle cx="365" cy="85" r="0.7"/>
    <circle cx="15" cy="100" r="0.9"/>
    <circle cx="42" cy="130" r="0.8"/>
    <circle cx="340" cy="100" r="1.0"/>
    <circle cx="390" cy="120" r="0.7"/>
    <circle cx="22" cy="55" r="1.0"/>
    <circle cx="108" cy="110" r="0.8"/>
    <circle cx="260" cy="95" r="0.9"/>
  </g>

  <!-- Moon glow halo -->
  <circle cx="300" cy="80" r="42" fill="#fffde0" opacity="0.08"/>
  <circle cx="300" cy="80" r="36" fill="#fffde0" opacity="0.1"/>

  <!-- Moon -->
  <circle cx="300" cy="80" r="30" fill="url(#moon)" filter="url(#softglow)"/>
  <!-- Moon craters -->
  <circle cx="290" cy="70" r="5" fill="#b8a440" opacity="0.5"/>
  <circle cx="312" cy="88" r="3.5" fill="#b8a440" opacity="0.4"/>
  <circle cx="298" cy="92" r="2.5" fill="#b8a440" opacity="0.35"/>

  <!-- Mountains background -->
  <polygon points="0,220 60,140 120,200 180,130 240,195 300,145 360,190 400,150 400,280 0,280" fill="#0f1535"/>
  <!-- Mountains midground -->
  <polygon points="0,280 50,200 110,250 170,185 230,245 290,195 350,240 400,200 400,290 0,290" fill="#0d1228"/>

  <!-- Water / Lake -->
  <rect x="0" y="285" width="400" height="115" fill="url(#water)"/>

  <!-- Moon reflection on water -->
  <ellipse cx="300" cy="310" rx="20" ry="6" fill="#fffde0" opacity="0.15"/>
  <rect x="288" y="285" width="24" height="130" fill="url(#moonreflection)" opacity="0.12"/>
  <line x1="300" y1="285" x2="300" y2="400" stroke="#fffde0" stroke-width="18" opacity="0.05"/>
  <line x1="300" y1="285" x2="300" y2="400" stroke="#fffde0" stroke-width="8" opacity="0.06"/>
  <line x1="300" y1="285" x2="300" y2="400" stroke="#fffde0" stroke-width="3" opacity="0.15"/>

  <!-- Water ripples -->
  <ellipse cx="300" cy="320" rx="35" ry="4" fill="none" stroke="#fffde0" stroke-width="0.8" opacity="0.15"/>
  <ellipse cx="300" cy="340" rx="50" ry="5" fill="none" stroke="#fffde0" stroke-width="0.7" opacity="0.1"/>
  <ellipse cx="300" cy="360" rx="65" ry="6" fill="none" stroke="#fffde0" stroke-width="0.6" opacity="0.08"/>

  <!-- Horizontal water shimmer lines -->
  <line x1="0" y1="300" x2="400" y2="300" stroke="#2a3a7a" stroke-width="1" opacity="0.3"/>
  <line x1="0" y1="315" x2="400" y2="315" stroke="#2a3a7a" stroke-width="0.8" opacity="0.25"/>
  <line x1="0" y1="330" x2="400" y2="330" stroke="#2a3a7a" stroke-width="0.7" opacity="0.2"/>
  <line x1="0" y1="350" x2="400" y2="350" stroke="#2a3a7a" stroke-width="0.6" opacity="0.15"/>
  <line x1="0" y1="370" x2="400" y2="370" stroke="#2a3a7a" stroke-width="0.5" opacity="0.12"/>

  <!-- Pine trees left -->
  <g fill="#060e1c">
    <!-- Tree 1 -->
    <polygon points="40,285 55,220 70,285"/>
    <polygon points="35,270 55,200 75,270"/>
    <polygon points="30,255 55,175 80,255"/>
    <rect x="50" y="283" width="10" height="10" fill="#040a14"/>
    <!-- Tree 2 -->
    <polygon points="78,285 90,230 102,285"/>
    <polygon points="74,272 90,210 106,272"/>
    <polygon points="70,258 90,188 110,258"/>
    <rect x="86" y="283" width="8" height="8" fill="#040a14"/>
    <!-- Tree 3 -->
    <polygon points="10,285 22,238 34,285"/>
    <polygon points="6,272 22,218 38,272"/>
    <rect x="18" y="283" width="8" height="8" fill="#040a14"/>
  </g>

  <!-- Pine trees right -->
  <g fill="#060e1c">
    <!-- Tree 1 -->
    <polygon points="355,285 370,222 385,285"/>
    <polygon points="350,270 370,202 390,270"/>
    <polygon points="345,255 370,178 395,255"/>
    <rect x="365" y="283" width="10" height="10" fill="#040a14"/>
    <!-- Tree 2 -->
    <polygon points="320,285 333,228 346,285"/>
    <polygon points="316,272 333,208 350,272"/>
    <polygon points="312,258 333,185 354,258"/>
    <rect x="328" y="283" width="10" height="8" fill="#040a14"/>
    <!-- Tree 3 -->
    <polygon points="385,285 395,245 405,285"/>
    <polygon points="382,270 395,228 408,270"/>
    <rect x="391" y="283" width="8" height="7" fill="#040a14"/>
  </g>

  <!-- Shooting star -->
  <line x1="100" y1="50" x2="140" y2="70" stroke="white" stroke-width="1.5" opacity="0.8" stroke-linecap="round"/>
  <circle cx="100" cy="50" r="1.5" fill="white" opacity="0.9"/>

  <!-- Foreground dark ground -->
  <rect x="0" y="282" width="400" height="6" fill="#04080f"/>

  <!-- Atmospheric fog near horizon -->
  <rect x="0" y="270" width="400" height="20" fill="#1a2a5e" opacity="0.12"/>
</svg>