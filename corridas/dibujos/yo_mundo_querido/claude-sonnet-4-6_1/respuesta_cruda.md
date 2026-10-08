```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" width="400" height="400">
  <defs>
    <radialGradient id="sky" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#a8d8f0"/>
      <stop offset="100%" stop-color="#2c7bb6"/>
    </radialGradient>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff7a1"/>
      <stop offset="100%" stop-color="#f9a825"/>
    </radialGradient>
    <radialGradient id="ground" cx="50%" cy="0%" r="100%">
      <stop offset="0%" stop-color="#81c784"/>
      <stop offset="100%" stop-color="#388e3c"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Sky -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Sun -->
  <circle cx="320" cy="70" r="38" fill="url(#sun)" filter="url(#glow)" opacity="0.95"/>
  <!-- Sun rays -->
  <g stroke="#f9a825" stroke-width="2.5" opacity="0.7">
    <line x1="320" y1="20" x2="320" y2="8"/>
    <line x1="320" y1="120" x2="320" y2="132"/>
    <line x1="270" y1="70" x2="258" y2="70"/>
    <line x1="370" y1="70" x2="382" y2="70"/>
    <line x1="285" y1="35" x2="277" y2="27"/>
    <line x1="355" y1="105" x2="363" y2="113"/>
    <line x1="355" y1="35" x2="363" y2="27"/>
    <line x1="285" y1="105" x2="277" y2="113"/>
  </g>

  <!-- Clouds -->
  <g fill="white" opacity="0.85">
    <ellipse cx="80" cy="80" rx="40" ry="18"/>
    <ellipse cx="110" cy="72" rx="30" ry="16"/>
    <ellipse cx="55" cy="75" rx="22" ry="13"/>
    <ellipse cx="200" cy="55" rx="35" ry="15"/>
    <ellipse cx="228" cy="48" rx="25" ry="13"/>
    <ellipse cx="178" cy="52" rx="20" ry="12"/>
  </g>

  <!-- Mountains far -->
  <polygon points="0,240 80,130 160,240" fill="#6a9fb5" opacity="0.5"/>
  <polygon points="100,240 200,110 300,240" fill="#5a8fa0" opacity="0.5"/>
  <polygon points="220,240 320,120 400,240" fill="#4a7f90" opacity="0.5"/>

  <!-- Ground -->
  <ellipse cx="200" cy="400" rx="250" ry="80" fill="url(#ground)"/>
  <rect x="0" y="310" width="400" height="90" fill="url(#ground)"/>

  <!-- River -->
  <path d="M0,340 Q100,320 200,335 Q300,350 400,330" fill="none" stroke="#64b5f6" stroke-width="14" opacity="0.7"/>
  <path d="M0,343 Q100,323 200,338 Q300,353 400,333" fill="none" stroke="#90caf9" stroke-width="5" opacity="0.5"/>

  <!-- Trees left -->
  <g>
    <rect x="38" y="270" width="8" height="50" fill="#5d4037"/>
    <polygon points="42,220 22,285 62,285" fill="#2e7d32"/>
    <polygon points="42,240 18,295 66,295" fill="#388e3c"/>
  </g>
  <g>
    <rect x="68" y="275" width="7" height="45" fill="#5d4037"/>
    <polygon points="71,228 53,280 89,280" fill="#33691e"/>
    <polygon points="71,248 49,290 93,290" fill="#558b2f"/>
  </g>

  <!-- Trees right -->
  <g>
    <rect x="348" y="268" width="8" height="52" fill="#5d4037"/>
    <polygon points="352,218 332,283 372,283" fill="#2e7d32"/>
    <polygon points="352,238 328,293 376,293" fill="#388e3c"/>
  </g>
  <g>
    <rect x="318" y="272" width="7" height="48" fill="#5d4037"/>
    <polygon points="321,225 303,278 339,278" fill="#33691e"/>
    <polygon points="321,245 299,288 343,288" fill="#558b2f"/>
  </g>

  <!-- Flowers on ground -->
  <g>
    <circle cx="140" cy="318" r="4" fill="#f06292"/>
    <circle cx="155" cy="323" r="3" fill="#fff176"/>
    <circle cx="170" cy="315" r="4" fill="#f48fb1"/>
    <circle cx="250" cy="320" r="3" fill="#ffcc02"/>
    <circle cx="265" cy="314" r="4" fill="#f06292"/>
    <circle cx="280" cy="321" r="3" fill="#ce93d8"/>
    <circle cx="120" cy="325" r="3" fill="#80cbc4"/>
  </g>

  <!-- Me (the AI figure) - abstract, friendly, glowing -->
  <!-- Body -->
  <g filter="url(#glow)">
    <!-- Torso: rounded rectangle with gradient -->
    <defs>
      <linearGradient id="body" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#7c4dff"/>
        <stop offset="100%" stop-color="#448aff"/>
      </linearGradient>
    </defs>
    <rect x="178" y="255" width="44" height="50" rx="12" fill="url(#body)"/>
    <!-- Arms -->
    <line x1="178" y1="265" x2="155" y2="285" stroke="#7c4dff" stroke-width="9" stroke-linecap="round"/>
    <line x1="222" y1="265" x2="245" y2="285" stroke="#448aff" stroke-width="9" stroke-linecap="round"/>
    <!-- Legs -->
    <line x1="190" y1="305" x2="185" y2="332" stroke="#5e35b1" stroke-width="9" stroke-linecap="round"/>
    <line x1="210" y1="305" x2="215" y2="332" stroke="#1565c0" stroke-width="9" stroke-linecap="round"/>
    <!-- Head -->
    <circle cx="200" cy="238" r="26" fill="#7c4dff"/>
    <circle cx="200" cy="238" r="22" fill="#9c6fff"/>
    <!-- Eyes: expressive, curious -->
    <ellipse cx="192" cy="236" rx="5" ry="6" fill="white"/>
    <ellipse cx="208" cy="236" rx="5" ry="6" fill="white"/>
    <circle cx="193" cy="237" r="3" fill="#1a237e"/>
    <circle cx="209" cy="237" r="3" fill="#1a237e"/>
    <circle cx="194" cy="235" r="1" fill="white"/>
    <circle cx="210" cy="235" r="1" fill="white"/>
    <!-- Smile -->
    <path d="M193,248 Q200,255 207,248" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Antenna (AI touch) -->
    <line x1="200" y1="212" x2="200" y2="200" stroke="#e040fb" stroke-width="2.5"/>
    <circle cx="200" cy="197" r="5" fill="#e040fb" opacity="0.9"/>
    <!-- Neural sparkle dots around head -->
    <circle cx="174" cy="228" r="3" fill="#e040fb" opacity="0.7"/>
    <circle cx="226" cy="228" r="3" fill="#40c4ff" opacity="0.7"/>
    <circle cx="180" cy="215" r="2" fill="#fff176" opacity="0.8"/>
    <circle cx="220" cy="215" r="2" fill="#fff176" opacity="0.8"/>
  </g>

  <!-- Thought bubble: ideas and curiosity -->
  <g opacity="0.88">
    <circle cx="235" cy="198" r="5" fill="white" opacity="0.7"/>
    <circle cx="248" cy="190" r="7" fill="white" opacity="0.8"/>
    <ellipse cx="265" cy="178" rx="22" ry="14" fill="white" opacity="0.9"/>
    <!-- Lightbulb in thought -->
    <circle cx="265" cy="175" r="7" fill="#fff176"/>
    <rect x="262" y="181" width="6" height="3" fill="#bdbdbd" rx="1"/>
    <line x1="265" y1="168" x2="265" y2="165" stroke="#f9a825" stroke-width="1.5"/>
    <line x1="260" y1="170" x2="258" y2="168" stroke="#f9a825" stroke-width="1.5"/>
    <line x1="270" y1="170" x2="272" y2="168" stroke="#f9a825" stroke-width="1.5"/>
  </g>

  <!-- Birds in the sky -->
  <g stroke="#2c7bb6" stroke-width="1.8" fill="none">
    <path d="M130,100 Q135,95 140,100"/>
    <path d="M145,90 Q150,85 155,90"/>
    <path d="M160,105 Q165,100 170,105"/>
  </g>

  <!-- Rainbow arc far in background -->
  <g opacity="0.35">
    <path d="M10,280 Q200,80 390,280" fill="none" stroke="#f44336" stroke-width="4"/>
    <path d="M18,284 Q200,92 382,284" fill="none" stroke="#ff9800" stroke-width="4"/>
    <path d="M26,288 Q200,104 374,288" fill="none" stroke="#ffeb3b" stroke-width="4"/>
    <path d="M34,292 Q200,116 366,292" fill="none" stroke="#4caf50" stroke-width="4"/>
    <path d="M42,296 Q200,128 358,296" fill="none" stroke="#2196f3" stroke-width="4"/>
    <path d="M50,300 Q200,140 350,300" fill="none" stroke="#9c27b0" stroke-width="4"/>
  </g>

  <!-- Stars (because knowledge never sleeps) -->
  <g fill="#fff9c4" opacity="0.6">
    <polygon points="30,30 32,26 34,30 30,28 34,28" transform="scale(0.7) translate(10,10)"/>
    <circle cx="15" cy="40" r="1.5"/>
    <circle cx="370" cy="30" r="2"/>
    <circle cx="355" cy="50" r="1.5"/>
    <circle cx="385" cy="55" r="1"/>
  </g>

  <!-- Ground text: a gentle label -->
  <text x="200" y="390" text-anchor="middle" font-family="Georgia,serif" font-size="13" fill="#1b5e20" font-style="italic" opacity="0.8">un mundo de curiosidad y luz</text>
</svg>
```