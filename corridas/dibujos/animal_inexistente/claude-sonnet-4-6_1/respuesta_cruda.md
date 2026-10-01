```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bodyGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7ecfb0"/>
      <stop offset="100%" stop-color="#2a7a5c"/>
    </radialGradient>
    <radialGradient id="bellyGrad" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#d4f5e9"/>
      <stop offset="100%" stop-color="#a8dfc8"/>
    </radialGradient>
    <radialGradient id="eyeGrad" cx="40%" cy="35%" r="50%">
      <stop offset="0%" stop-color="#ffffaa"/>
      <stop offset="100%" stop-color="#cc8800"/>
    </radialGradient>
    <radialGradient id="wingGrad" cx="50%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#b388ff"/>
      <stop offset="100%" stop-color="#6200ea"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="400" height="400" fill="#0d1b2a"/>
  <!-- Stars -->
  <circle cx="30" cy="20" r="1.5" fill="white" opacity="0.8"/>
  <circle cx="80" cy="50" r="1" fill="white" opacity="0.6"/>
  <circle cx="350" cy="30" r="1.5" fill="white" opacity="0.9"/>
  <circle cx="370" cy="80" r="1" fill="white" opacity="0.5"/>
  <circle cx="20" cy="350" r="1" fill="white" opacity="0.7"/>
  <circle cx="380" cy="340" r="1.5" fill="white" opacity="0.8"/>
  <circle cx="320" cy="15" r="1" fill="white" opacity="0.6"/>
  <circle cx="150" cy="10" r="1" fill="white" opacity="0.7"/>
  <circle cx="60" cy="380" r="1.5" fill="white" opacity="0.5"/>
  <circle cx="340" cy="370" r="1" fill="white" opacity="0.8"/>

  <!-- Ground / mossy surface -->
  <ellipse cx="200" cy="360" rx="160" ry="25" fill="#1a3a1a"/>
  <ellipse cx="200" cy="355" rx="155" ry="18" fill="#2d5a27"/>
  <!-- Grass tufts -->
  <path d="M100 355 Q105 340 110 355" fill="none" stroke="#4a8a40" stroke-width="2"/>
  <path d="M115 355 Q118 338 122 355" fill="none" stroke="#4a8a40" stroke-width="2"/>
  <path d="M270 355 Q275 342 280 355" fill="none" stroke="#4a8a40" stroke-width="2"/>
  <path d="M285 355 Q289 340 293 355" fill="none" stroke="#4a8a40" stroke-width="2"/>

  <!-- Tail - long, fluffy, cat-like -->
  <path d="M230 300 Q310 280 340 240 Q360 210 340 190 Q325 175 310 195 Q330 205 315 225 Q295 255 250 280" 
        fill="none" stroke="#2a7a5c" stroke-width="18" stroke-linecap="round"/>
  <path d="M230 300 Q310 280 340 240 Q360 210 340 190 Q325 175 310 195 Q330 205 315 225 Q295 255 250 280" 
        fill="none" stroke="#7ecfb0" stroke-width="10" stroke-linecap="round" opacity="0.5"/>
  <!-- Tail tip fluffy -->
  <circle cx="310" cy="195" r="14" fill="#5dade2" opacity="0.8" filter="url(#glow)"/>
  <circle cx="310" cy="195" r="8" fill="#aed6f1"/>

  <!-- Body -->
  <ellipse cx="185" cy="290" rx="75" ry="65" fill="url(#bodyGrad)"/>
  <!-- Belly -->
  <ellipse cx="185" cy="300" rx="45" ry="42" fill="url(#bellyGrad)"/>
  <!-- Body spots / pattern -->
  <circle cx="155" cy="270" r="8" fill="#1a6645" opacity="0.4"/>
  <circle cx="215" cy="265" r="6" fill="#1a6645" opacity="0.4"/>
  <circle cx="165" cy="310" r="5" fill="#1a6645" opacity="0.3"/>
  <circle cx="200" cy="320" r="7" fill="#1a6645" opacity="0.3"/>

  <!-- Wings - bat-like, glowing purple -->
  <!-- Left wing -->
  <path d="M135 275 Q80 230 50 180 Q40 150 70 145 Q90 140 100 170 Q80 175 85 195 Q110 230 145 265"
        fill="url(#wingGrad)" opacity="0.85"/>
  <path d="M135 275 Q90 250 65 210 Q55 185 72 152" 
        fill="none" stroke="#b388ff" stroke-width="1.5" opacity="0.6"/>
  <path d="M135 275 Q100 255 85 220 Q78 198 82 175"
        fill="none" stroke="#b388ff" stroke-width="1" opacity="0.5"/>
  <!-- Right wing -->
  <path d="M235 275 Q290 230 320 175 Q335 148 308 143 Q287 138 278 168 Q298 172 294 194 Q272 230 242 265"
        fill="url(#wingGrad)" opacity="0.85"/>
  <path d="M235 275 Q282 248 306 207 Q316 182 310 150"
        fill="none" stroke="#b388ff" stroke-width="1.5" opacity="0.6"/>
  <path d="M235 275 Q270 252 288 217 Q295 196 292 172"
        fill="none" stroke="#b388ff" stroke-width="1" opacity="0.5"/>

  <!-- Neck -->
  <ellipse cx="185" cy="235" rx="38" ry="28" fill="url(#bodyGrad)"/>

  <!-- Head -->
  <ellipse cx="185" cy="200" rx="55" ry="50" fill="url(#bodyGrad)"/>
  <!-- Head pattern -->
  <circle cx="170" cy="185" r="5" fill="#1a6645" opacity="0.3"/>
  <circle cx="200" cy="190" r="4" fill="#1a6645" opacity="0.3"/>

  <!-- Ears - long rabbit-like with glow tips -->
  <!-- Left ear -->
  <path d="M160 160 Q145 100 150 60 Q153 40 165 55 Q170 75 165 100 Q163 130 162 160"
        fill="#2a7a5c" stroke="#1a5c44" stroke-width="1"/>
  <path d="M162 160 Q150 105 155 65 Q157 50 163 60 Q166 78 163 105 Q161 132 162 160"
        fill="#a8dfc8" opacity="0.6"/>
  <circle cx="158" cy="55" r="10" fill="#ff6b9d" opacity="0.9" filter="url(#glow)"/>
  <!-- Right ear -->
  <path d="M210 160 Q225 100 220 60 Q217 40 205 55 Q200 75 205 100 Q207 130 208 160"
        fill="#2a7a5c" stroke="#1a5c44" stroke-width="1"/>
  <path d="M208 160 Q220 105 215 65 Q213 50 207 60 Q204 78 207 105 Q209 132 208 160"
        fill="#a8dfc8" opacity="0.6"/>
  <circle cx="222" cy="55" r="10" fill="#ff6b9d" opacity="0.9" filter="url(#glow)"/>

  <!-- Snout - wide, frog-like -->
  <ellipse cx="185" cy="218" rx="32" ry="18" fill="#3a9a75"/>
  <!-- Nostrils -->
  <ellipse cx="175" cy="214" rx="5" ry="4" fill="#1a5c44"/>
  <ellipse cx="195" cy="214" rx="5" ry="4" fill="#1a5c44"/>
  <!-- Smile -->
  <path d="M162 225 Q185 240 208 225" fill="none" stroke="#1a5c44" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Eyes -->
  <!-- Left eye -->
  <circle cx="162" cy="195" r="18" fill="#111" stroke="#2a7a5c" stroke-width="2"/>
  <circle cx="162" cy="195" r="15" fill="url(#eyeGrad)"/>
  <ellipse cx="162" cy="195" rx="6" ry="12" fill="#111"/>
  <circle cx="157" cy="190" r="4" fill="white" opacity="0.8"/>
  <!-- Right eye -->
  <circle cx="208" cy="195" r="18" fill="#111" stroke="#2a7a5c" stroke-width="2"/>
  <circle cx="208" cy="195" r="15" fill="url(#eyeGrad)"/>
  <ellipse cx="208" cy="195" rx="6" ry="12" fill="#111"/>
  <circle cx="203" cy="190" r="4" fill="white" opacity="0.8"/>

  <!-- Whiskers -->
  <line x1="155" y1="218" x2="100" y2="210" stroke="#d4f5e9" stroke-width="1.2" opacity="0.7"/>
  <line x1="155" y1="222" x2="98" y2="228" stroke="#d4f5e9" stroke-width="1.2" opacity="0.7"/>
  <line x1="155" y1="215" x2="105" y2="200" stroke="#d4f5e9" stroke-width="1" opacity="0.5"/>
  <line x1="215" y1="218" x2="270" y2="210" stroke="#d4f5e9" stroke-width="1.2" opacity="0.7"/>
  <line x1="215" y1="222" x2="272" y2="228" stroke="#d4f5e9" stroke-width="1.2" opacity="0.7"/>
  <line x1="215" y1="215" x2="265" y2="200" stroke="#d4f5e9" stroke-width="1" opacity="0.5"/>

  <!-- Legs - stubby frog-like -->
  <!-- Front left leg -->
  <path d="M150 320 Q130 340 125 355 Q135 360 150 355 Q155 345 160 335" 
        fill="#2a7a5c" stroke="#1a5c44" stroke-width="1"/>
  <!-- Toes -->
  <circle cx="118" cy="358" r="5" fill="#3a9a75"/>
  <circle cx="127" cy="362" r="5" fill="#3a9a75"/>
  <circle cx="138" cy="363" r="5" fill="#3a9a75"/>
  <circle cx="149" cy="361" r="5" fill="#3a9a75"/>
  <!-- Front right leg -->
  <path d="M220 320 Q240 340 245 355 Q235 360 220 355 Q215 345 210 335"
        fill="#2a7a5c" stroke="#1a5c44" stroke-width="1"/>
  <circle cx="252" cy="358" r="5" fill="#3a9a75"/>
  <circle cx="243" cy="362" r="5" fill="#3a9a75"/>
  <circle cx="232" cy="363" r="5" fill="#3a9a75"/>
  <circle cx="221" cy="361" r="5" fill="#3a9a75"/>

  <!-- Bioluminescent spots on body -->
  <circle cx="175" cy="285" r="4" fill="#00ffaa" opacity="0.7" filter="url(#glow)"/>
  <circle cx="200" cy="295" r="3" fill="#00ffaa" opacity="0.7" filter="url(#glow)"/>
  <circle cx="185" cy="310" r="3.5" fill="#00ffaa" opacity="0.6" filter="url(#glow)"/>
  <circle cx="160" cy="300" r="3" fill="#7af5ff" opacity="0.7" filter="url(#glow)"/>
  <circle cx="210" cy="280" r="3" fill="#7af5ff" opacity="0.6" filter="url(#glow)"/>
</svg>
```