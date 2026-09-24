```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="sky" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="60%" stop-color="#16213e"/>
      <stop offset="100%" stop-color="#0f3460"/>
    </radialGradient>
    <radialGradient id="screenGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="moonGrad" cx="40%" cy="35%" r="50%">
      <stop offset="0%" stop-color="#e8e8d0"/>
      <stop offset="100%" stop-color="#b0b090"/>
    </radialGradient>
    <filter id="blur1">
      <feGaussianBlur stdDeviation="2"/>
    </filter>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="groundGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a1a1a"/>
      <stop offset="100%" stop-color="#0a0a0a"/>
    </linearGradient>
    <linearGradient id="buildingGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1c1c2e"/>
      <stop offset="100%" stop-color="#252540"/>
    </linearGradient>
  </defs>

  <!-- Sky -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Stars -->
  <g fill="white">
    <circle cx="30" cy="20" r="1" opacity="0.8"/>
    <circle cx="70" cy="45" r="0.8" opacity="0.6"/>
    <circle cx="110" cy="15" r="1.2" opacity="0.9"/>
    <circle cx="150" cy="55" r="0.7" opacity="0.5"/>
    <circle cx="200" cy="10" r="1" opacity="0.8"/>
    <circle cx="240" cy="38" r="0.9" opacity="0.7"/>
    <circle cx="280" cy="18" r="1.1" opacity="0.9"/>
    <circle cx="320" cy="50" r="0.8" opacity="0.6"/>
    <circle cx="360" cy="25" r="1" opacity="0.8"/>
    <circle cx="50" cy="80" r="0.7" opacity="0.5"/>
    <circle cx="90" cy="65" r="1" opacity="0.7"/>
    <circle cx="340" cy="70" r="0.8" opacity="0.6"/>
    <circle cx="380" cy="60" r="1" opacity="0.8"/>
    <circle cx="170" cy="30" r="0.6" opacity="0.5"/>
    <circle cx="130" cy="75" r="0.9" opacity="0.7"/>
  </g>

  <!-- Moon -->
  <circle cx="320" cy="70" r="28" fill="url(#moonGrad)" filter="url(#blur1)" opacity="0.4"/>
  <circle cx="320" cy="70" r="22" fill="url(#moonGrad)"/>
  <circle cx="310" cy="62" r="3" fill="#c8c8a8" opacity="0.4"/>
  <circle cx="328" cy="75" r="2" fill="#c8c8a8" opacity="0.3"/>
  <circle cx="318" cy="82" r="1.5" fill="#c8c8a8" opacity="0.35"/>

  <!-- City silhouette - back layer -->
  <g fill="#111122" opacity="0.9">
    <rect x="0" y="220" width="30" height="180"/>
    <rect x="20" y="200" width="25" height="200"/>
    <rect x="50" y="230" width="20" height="170"/>
    <rect x="60" y="210" width="30" height="190"/>
    <rect x="100" y="240" width="25" height="160"/>
    <rect x="115" y="215" width="20" height="185"/>
    <rect x="145" y="235" width="35" height="165"/>
    <rect x="190" y="225" width="25" height="175"/>
    <rect x="205" y="205" width="20" height="195"/>
    <rect x="235" y="238" width="30" height="162"/>
    <rect x="270" y="218" width="25" height="182"/>
    <rect x="285" y="230" width="35" height="170"/>
    <rect x="330" y="222" width="30" height="178"/>
    <rect x="355" y="210" width="25" height="190"/>
    <rect x="375" y="228" width="30" height="172"/>
  </g>

  <!-- City silhouette - front layer -->
  <g fill="#0d0d1a">
    <rect x="0" y="260" width="40" height="140"/>
    <rect x="35" y="245" width="30" height="155"/>
    <rect x="55" y="255" width="45" height="145"/>
    <polygon points="77,248 85,230 93,248" fill="#0d0d1a"/>
    <rect x="105" y="262" width="35" height="138"/>
    <rect x="135" y="250" width="50" height="150"/>
    <rect x="155" y="240" width="20" height="160"/>
    <rect x="185" y="258" width="40" height="142"/>
    <rect x="220" y="248" width="35" height="152"/>
    <polygon points="237,242 244,225 251,242" fill="#0d0d1a"/>
    <rect x="260" y="255" width="45" height="145"/>
    <rect x="300" y="262" width="30" height="138"/>
    <rect x="325" y="250" width="40" height="150"/>
    <rect x="360" y="258" width="45" height="142"/>
  </g>

  <!-- Ground -->
  <rect x="0" y="320" width="400" height="80" fill="url(#groundGrad)"/>

  <!-- Street -->
  <rect x="0" y="340" width="400" height="60" fill="#111111"/>
  <!-- Street lines -->
  <line x1="0" y1="370" x2="400" y2="370" stroke="#333" stroke-width="1"/>
  <rect x="30" y="368" width="40" height="4" fill="#444" rx="1"/>
  <rect x="120" y="368" width="40" height="4" fill="#444" rx="1"/>
  <rect x="210" y="368" width="40" height="4" fill="#444" rx="1"/>
  <rect x="300" y="368" width="40" height="4" fill="#444" rx="1"/>

  <!-- Street puddle reflection -->
  <ellipse cx="200" cy="360" rx="80" ry="8" fill="#1a2a3a" opacity="0.5"/>
  <ellipse cx="200" cy="360" rx="40" ry="4" fill="#00d4ff" opacity="0.08"/>

  <!-- Person sitting on bench with phone -->
  <!-- Bench -->
  <rect x="150" y="330" width="70" height="5" rx="2" fill="#2a2a2a"/>
  <rect x="155" y="335" width="5" height="10" fill="#222"/>
  <rect x="210" y="335" width="5" height="10" fill="#222"/>

  <!-- Person body -->
  <rect x="175" y="308" width="18" height="22" rx="3" fill="#1e3a5f"/>
  <!-- Head -->
  <circle cx="184" cy="302" r="9" fill="#c8a882"/>
  <!-- Hair -->
  <ellipse cx="184" cy="295" rx="9" ry="5" fill="#3a2a1a"/>
  <!-- Arms -->
  <rect x="165" y="312" width="12" height="5" rx="2" fill="#1e3a5f" transform="rotate(10,171,314)"/>
  <rect x="191" y="312" width="12" height="5" rx="2" fill="#1e3a5f" transform="rotate(-10,197,314)"/>
  <!-- Hands holding phone -->
  <rect x="179" y="318" width="10" height="14" rx="2" fill="#2a2a2a"/>
  <!-- Phone screen glow -->
  <rect x="180" y="319" width="8" height="12" rx="1" fill="#00d4ff" opacity="0.8"/>
  <rect x="180" y="319" width="8" height="12" rx="1" fill="url(#screenGlow)"/>
  <!-- Legs -->
  <rect x="175" y="328" width="7" height="8" rx="1" fill="#1a1a3a"/>
  <rect x="185" y="328" width="7" height="8" rx="1" fill="#1a1a3a"/>

  <!-- Phone glow on face -->
  <ellipse cx="184" cy="308" rx="7" ry="5" fill="#00d4ff" opacity="0.1"/>

  <!-- Notifications floating up from phone -->
  <g filter="url(#glow)" opacity="0.7">
    <rect x="196" y="305" width="16" height="10" rx="2" fill="#e74c3c"/>
    <text x="204" y="313" font-size="7" fill="white" text-anchor="middle">3</text>
    <rect x="196" y="292" width="22" height="10" rx="2" fill="#3498db"/>
    <text x="207" y="300" font-size="6" fill="white" text-anchor="middle">like</text>
    <rect x="200" y="279" width="18" height="10" rx="2" fill="#2ecc71"/>
    <text x="209" y="287" font-size="6" fill="white" text-anchor="middle">msg</text>
  </g>

  <!-- Street lamp -->
  <rect x="90" y="275" width="4" height="70" fill="#2a2a2a"/>
  <ellipse cx="92" cy="273" rx="12" ry="4" fill="#333"/>
  <ellipse cx="92" cy="272" rx="5" ry="3" fill="#ffdd88" opacity="0.9"/>
  <!-- Lamp glow -->
  <ellipse cx="92" cy="290" rx="18" ry="20" fill="#ffdd88" opacity="0.06" filter="url(#blur1)"/>

  <!-- Another lamp -->
  <rect x="300" y="278" width="4" height="67" fill="#2a2a2a"/>
  <ellipse cx="302" cy="276" rx="12" ry="4" fill="#333"/>
  <ellipse cx="302" cy="275" rx="5" ry="3" fill="#ffdd88" opacity="0.9"/>
  <ellipse cx="302" cy="292" rx="18" ry="20" fill="#ffdd88" opacity="0.06" filter="url(#blur1)"/>

  <!-- Windows lit up in buildings -->
  <g fill="#ffcc44" opacity="0.6">
    <rect x="25" y="215" width="5" height="7"/>
    <rect x="35" y="225" width="5" height="7"/>
    <rect x="65" y="220" width="5" height="7"/>
    <rect x="65" y="235" width="5" height="7"/>
    <rect x="120" y="218" width="5" height="7"/>
    <rect x="150" y="242" width="5" height="7"/>
    <rect x="162" y="248" width="5" height="7"/>
    <rect x="210" y="210" width="5" height="7"/>
    <rect x="240" y="243" width="5" height="7"/>
    <rect x="275" y="225" width="5" height="7"/>
    <rect x="290" y="235" width="5" height="7"/>
    <rect x="335" y="228" width="5" height="7"/>
    <rect x="360" y="218" width="5" height="7"/>
  </g>
  <!-- Blue screen windows -->
  <g fill="#00d4ff" opacity="0.5">
    <rect x="30" y="235" width="5" height="7"/>
    <rect x="70" y="248" width="5" height="7"/>
    <rect x="130" y="258" width="5" height="7"/>
    <rect x="200" y="230" width="5" height="7"/>
    <rect x="250" y="260" width="5" height="7"/>
    <rect x="295" y="248" width="5" height="7"/>
    <rect x="370" y="230" width="5" height="7"/>
  </g>

  <!-- Fog / smog layer -->
  <rect x="0" y="290" width="400" height="50" fill="#0a0a15" opacity="0.3"/>

  <!-- Title text subtle -->
  <text x="200" y="395" font-size="8" fill="#334" text-anchor="middle" font-family="monospace" opacity="0.5">2025</text>
</svg>
```