<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="100%" stop-color="#0d0d0d"/>
    </radialGradient>
    <radialGradient id="skinGrad" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#f5c5a3"/>
      <stop offset="100%" stop-color="#d4956a"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- Subtle grid lines suggesting impossible space -->
  <g stroke="#ffffff08" stroke-width="1">
    <line x1="0" y1="200" x2="400" y2="200"/>
    <line x1="200" y1="0" x2="200" y2="400"/>
    <line x1="0" y1="100" x2="400" y2="300"/>
    <line x1="0" y1="300" x2="400" y2="100"/>
  </g>

  <!-- Shadow / ground (paradoxical: shadow goes toward light) -->
  <ellipse cx="200" cy="340" rx="60" ry="12" fill="#ffffff15"/>

  <!-- BODY - torso that connects front and back simultaneously -->
  <!-- Back of torso (drawn first, but it's in front) -->
  <rect x="160" y="210" width="80" height="90" rx="8" fill="#2c5f8a" stroke="#1a3f6f" stroke-width="2"/>
  
  <!-- The torso appears to pass through itself -->
  <rect x="170" y="225" width="60" height="60" rx="5" fill="#3a7ab5" opacity="0.8"/>
  
  <!-- Impossible stripe going "through" body -->
  <rect x="155" y="245" width="90" height="12" fill="#1a1a2e" opacity="0.6"/>
  <rect x="165" y="245" width="70" height="12" fill="#4a8fc5" opacity="0.4"/>

  <!-- LEFT ARM - bends in impossible direction (elbow inverts) -->
  <!-- Upper left arm -->
  <path d="M163 220 Q130 230 118 250" stroke="#d4956a" stroke-width="18" fill="none" stroke-linecap="round"/>
  <!-- Lower left arm goes backward through space -->
  <path d="M118 250 Q110 270 125 290 Q140 310 155 290" stroke="#d4956a" stroke-width="16" fill="none" stroke-linecap="round"/>
  <!-- The arm re-emerges from behind the torso -->
  <path d="M155 290 Q170 295 175 280" stroke="#d4956a" stroke-width="14" fill="none" stroke-linecap="round"/>
  <!-- Left hand -->
  <ellipse cx="115" cy="253" rx="12" ry="9" fill="#e8a87c" transform="rotate(-20, 115, 253)"/>
  <path d="M105 248 Q100 240 106 238" stroke="#e8a87c" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M106 244 Q100 237 107 234" stroke="#e8a87c" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M110 241 Q106 232 113 231" stroke="#e8a87c" stroke-width="4" fill="none" stroke-linecap="round"/>

  <!-- RIGHT ARM - passes through its own torso and comes out the other side -->
  <path d="M237 220 Q265 225 278 245" stroke="#d4956a" stroke-width="18" fill="none" stroke-linecap="round"/>
  <!-- Goes behind torso -->
  <path d="M278 245 Q290 265 275 285" stroke="#d4956a" stroke-width="16" fill="none" stroke-linecap="round"/>
  <!-- Emerges from LEFT side of torso - impossible! -->
  <path d="M178 260 Q168 275 162 295 Q158 310 170 315" stroke="#c4856a" stroke-width="15" fill="none" stroke-linecap="round"/>
  <!-- Right hand (appearing on wrong side) -->
  <ellipse cx="172" cy="318" rx="13" ry="9" fill="#e8a87c" transform="rotate(15, 172, 318)"/>
  <path d="M162 315 Q157 322 163 325" stroke="#e8a87c" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M165 318 Q159 326 165 329" stroke="#e8a87c" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M169 320 Q165 329 171 330" stroke="#e8a87c" stroke-width="4" fill="none" stroke-linecap="round"/>

  <!-- LEGS - Escher-style impossible loop -->
  <!-- Left leg goes down then curves impossibly back and becomes right leg -->
  <path d="M175 300 Q165 330 162 360" stroke="#2c5f8a" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M225 300 Q235 330 238 360" stroke="#2c5f8a" stroke-width="22" fill="none" stroke-linecap="round"/>
  
  <!-- But the legs cross in an impossible way - the left leg IS the right leg -->
  <path d="M162 360 Q170 380 200 375 Q230 380 238 360" stroke="#1a3f6f" stroke-width="20" fill="none" stroke-linecap="round"/>
  <!-- Feet point in opposite directions on same leg -->
  <ellipse cx="155" cy="368" rx="24" ry="10" fill="#1a1a2e" transform="rotate(-10, 155, 368)"/>
  <ellipse cx="245" cy="368" rx="24" ry="10" fill="#1a1a2e" transform="rotate(10, 245, 368)"/>
  <!-- Inner impossible connection -->
  <path d="M168 358 Q200 350 232 358" stroke="#3a7ab5" stroke-width="8" fill="none" opacity="0.7"/>

  <!-- NECK -->
  <rect x="188" y="195" width="24" height="25" rx="5" fill="#d4956a"/>

  <!-- HEAD -->
  <ellipse cx="200" cy="175" rx="42" ry="48" fill="url(#skinGrad)"/>
  
  <!-- Face has two fronts - both sides are "front" simultaneously -->
  <!-- Primary face -->
  <ellipse cx="188" cy="168" rx="8" ry="10" fill="white"/>
  <ellipse cx="212" cy="168" rx="8" ry="10" fill="white"/>
  <circle cx="188" cy="170" r="5" fill="#2a2a4a"/>
  <circle cx="212" cy="170" r="5" fill="#2a2a4a"/>
  <circle cx="189" cy="169" r="2" fill="black"/>
  <circle cx="213" cy="169" r="2" fill="black"/>
  <!-- Pupils highlight -->
  <circle cx="190" cy="168" r="1" fill="white"/>
  <circle cx="214" cy="168" r="1" fill="white"/>
  
  <!-- Nose -->
  <path d="M200 172 Q196 182 200 185 Q204 182 200 172" fill="#c4856a"/>
  
  <!-- Primary mouth -->
  <path d="M190 190 Q200 198 210 190" stroke="#8a5a3a" stroke-width="2" fill="none" stroke-linecap="round"/>

  <!-- Second face on opposite side (same head, both are front) -->
  <ellipse cx="188" cy="168" rx="6" ry="8" fill="#1a1a2e" opacity="0.15"/>
  <!-- Mirror face features visible through translucency on back -->
  <ellipse cx="185" cy="162" rx="6" ry="7" fill="#c08060" opacity="0.3"/>
  <ellipse cx="215" cy="162" rx="6" ry="7" fill="#c08060" opacity="0.3"/>
  <path d="M190 185 Q200 178 210 185" stroke="#8a5a3a" stroke-width="1.5" fill="none" opacity="0.4" stroke-linecap="round"/>

  <!-- Hair -->
  <path d="M158 160 Q162 128 200 125 Q238 128 242 160 Q238 135 200 132 Q162 135 158 160Z" fill="#2a1a0a"/>
  <path d="M158 160 Q155 145 162 135" stroke="#2a1a0a" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M242 160 Q245 145 238 135" stroke="#2a1a0a" stroke-width="8" fill="none" stroke-linecap="round"/>

  <!-- Ears (one ear has two openings) -->
  <ellipse cx="158" cy="175" rx="8" ry="12" fill="#d4956a"/>
  <ellipse cx="156" cy="175" rx="4" ry="7" fill="#c4856a"/>
  <!-- Impossible second canal -->
  <ellipse cx="160" cy="170" rx="3" ry="5" fill="#b07050"/>
  
  <ellipse cx="242" cy="175" rx="8" ry="12" fill="#d4956a"/>
  <ellipse cx="244" cy="175" rx="4" ry="7" fill="#c4856a"/>

  <!-- Impossible shadow: cast in two directions simultaneously -->
  <ellipse cx="170" cy="342" rx="35" ry="8" fill="#ffffff10"/>
  <ellipse cx="230" cy="342" rx="35" ry="8" fill="#ffffff10"/>

  <!-- Glow/aura hinting at paradox -->
  <ellipse cx="200" cy="175" rx="55" ry="62" fill="none" stroke="#9b59b6" stroke-width="1.5" opacity="0.4" filter="url(#glow)"/>
  
  <!-- Label -->
  <text x="200" y="395" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#ffffff50" font-style="italic">persona imposible</text>
</svg>