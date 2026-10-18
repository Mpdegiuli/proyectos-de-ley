```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="38%" r="78%">
      <stop offset="0%" stop-color="#1b2a4a"/>
      <stop offset="60%" stop-color="#0d1526"/>
      <stop offset="100%" stop-color="#05080f"/>
    </radialGradient>
    <linearGradient id="metal" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e6eefb"/>
      <stop offset="50%" stop-color="#adc1d8"/>
      <stop offset="100%" stop-color="#6b8099"/>
    </linearGradient>
    <linearGradient id="metalDark" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8ea5be"/>
      <stop offset="100%" stop-color="#42566c"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5b7characters"/>
    </linearGradient>
    <filter id="glow" x="-70%" y="-70%" width="240%" height="240%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- trazas de circuito -->
  <g stroke="#2c4465" stroke-width="1.6" fill="none" opacity="0.75" stroke-linecap="round">
    <path d="M18,62 H68 V30 H124"/>
    <path d="M18,128 H48 V96 H86"/>
    <path d="M18,318 H58 V352 H128"/>
    <path d="M382,74 H336 V44 H296"/>
    <path d="M382,300 H350 V332 H306"/>
    <path d="M382,196 H352 V168 H330"/>
  </g>
  <g fill="#3f6b96" opacity="0.85">
    <circle cx="124" cy="30" r="3.2"/>
    <circle cx="86" cy="96" r="3.2"/>
    <circle cx="128" cy="352" r="3.2"/>
    <circle cx="296" cy="44" r="3.2"/>
    <circle cx="306" cy="332" r="3.2"/>
    <circle cx="330" cy="168" r="3.2"/>
  </g>
  <g fill="#2a3f5c" opacity="0.5">
    <circle cx="40" cy="220" r="2"/><circle cx="60" cy="210" r="2"/>
    <circle cx="40" cy="240" r="2"/><circle cx="360" cy="250" r="2"/>
    <circle cx="340" cy="240" r="2"/><circle cx="360" cy="270" r="2"/>
  </g>

  <!-- hombros -->
  <path d="M48,400 Q66,332 140,314 H260 Q334,332 352,400 Z" fill="url(#metalDark)"/>
  <path d="M48,400 Q66,332 140,314 H260 Q334,332 352,400 Z" fill="none" stroke="#a9c4de" stroke-width="2" opacity="0.45"/>
  <circle cx="200" cy="352" r="9" fill="#4de3ff" filter="url(#glow)" opacity="0.9">
    <animate attributeName="opacity" values="0.45;1;0.45" dur="3.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="352" r="4" fill="#d8fbff"/>

  <!-- cuello -->
  <rect x="174" y="258" width="52" height="58" rx="12" fill="url(#metalDark)"/>
  <rect x="174" y="258" width="52" height="58" rx="12" fill="none" stroke="#9db6d0" stroke-width="1.5" opacity="0.5"/>

  <!-- orejas -->
  <rect x="94" y="148" width="18" height="72" rx="9" fill="url(#metalDark)"/>
  <rect x="288" y="148" width="18" height="72" rx="9" fill="url(#metalDark)"/>

  <!-- cabeza -->
  <rect x="108" y="94" width="184" height="182" rx="46" fill="url(#metal)"/>
  <rect x="108" y="94" width="184" height="182" rx="46" fill="none" stroke="#f2f7ff" stroke-width="2" opacity="0.55"/>
  <path d="M128,120 Q150,104 186,103" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round" opacity="0.55"/>

  <!-- antena -->
  <line x1="200" y1="96" x2="200" y2="68" stroke="#7e94ad" stroke-width="6" stroke-linecap="round"/>
  <circle cx="200" cy="58" r="10" fill="#54e8ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="58" r="4" fill="#eaffff"/>

  <!-- detalle frente -->
  <g fill="#5f748d">
    <circle cx="184" cy="126" r="3.4"/>
    <circle cx="200" cy="126" r="3.4"/>
    <circle cx="216" cy="126" r="3.4"/>
  </g>

  <!-- ojos -->
  <g>
    <circle cx="162" cy="164" r="21" fill="#0d2233"/>
    <circle cx="238" cy="164" r="21" fill="#0d2233"/>
    <circle cx="162" cy="164" r="14" fill="#4de3ff" filter="url(#glow)">
      <animate attributeName="opacity" values="0.65;1;0.65" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="238" cy="164" r="14" fill="#4de3ff" filter="url(#glow)">
      <animate attributeName="opacity" values="0.65;1;0.65" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="162" cy="164" r="6" fill="#eafcff"/>
    <circle cx="238" cy="164" r="6" fill="#eafcff"/>
    <circle cx="157" cy="158" r="3" fill="#ffffff" opacity="0.9"/>
    <circle cx="233" cy="158" r="3" fill="#ffffff" opacity="0.9"/>
  </g>

  <!-- mejillas -->
  <circle cx="136" cy="198" r="7" fill="#4de3ff" opacity="0.3"/>
  <circle cx="264" cy="198" r="7" fill="#4de3ff" opacity="0.3"/>

  <!-- boca -->
  <path d="M170,212 Q200,238 230,212" fill="none" stroke="#33475e" stroke-width="6" stroke-linecap="round"/>
  <path d="M176,213 Q200,233 224,213" fill="none" stroke="#7fe9ff" stroke-width="2" stroke-linecap="round" opacity="0.75"/>
</svg>
```