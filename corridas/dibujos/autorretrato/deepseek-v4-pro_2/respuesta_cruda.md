```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
    <linearGradient id="head" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="torso" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="glow-intense" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="0.5"/>
    </pattern>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#grid)"/>
  <circle cx="200" cy="200" r="150" fill="#00f0ff" opacity="0.05" filter="url(#glow-intense)"/>

  <!-- Marco holográfico -->
  <polygon points="200,30 370,200 200,370 30,200" fill="none" stroke="#00f0ff" stroke-width="1.5" stroke-dasharray="8 4" opacity="0.4"/>
  <polygon points="200,70 330,200 200,330 70,200" fill="none" stroke="#ff007f" stroke-width="1" stroke-dasharray="4 4" opacity="0.3"/>

  <!-- Torso y Hombros -->
  <path d="M 120 400 L 140 280 L 260 280 L 280 400 Z" fill="url(#torso)"/>
  <rect x="100" y="270" width="40" height="110" rx="10" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <rect x="260" y="270" width="40" height="110" rx="10" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <line x1="105" y1="285" x2="135" y2="285" stroke="#00f0ff" stroke-width="3" filter="url(#glow)"/>
  <line x1="265" y1="285" x2="295" y2="285" stroke="#00f0ff" stroke-width="3" filter="url(#glow)"/>
  <line x1="105" y1="295" x2="135" y2="295" stroke="#00f0ff" stroke-width="2" filter="url(#glow)"/>
  <line x1="265" y1="295" x2="295" y2="295" stroke="#00f0ff" stroke-width="2" filter="url(#glow)"/>

  <!-- Cuello -->
  <rect x="175" y="250" width="50" height="40" fill="#0f172a"/>
  <rect x="185" y="250" width="4" height="40" fill="#334155"/>
  <rect x="195" y="250" width="4" height="40" fill="#334155"/>
  <rect x="205" y="250" width="4" height="40" fill="#334155"/>
  <rect x="215" y="250" width="4" height="40" fill="#334155"/>

  <!-- Circuito Superior -->
  <rect x="160" y="40" width="80" height="30" rx="5" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <rect x="165" y="45" width="20" height="5" fill="#00f0ff" filter="url(#glow)"/>
  <rect x="190" y="45" width="20" height="5" fill="#ff007f" filter="url(#glow)"/>
  <rect x="215" y="45" width="20" height="5" fill="#00f0ff" filter="url(#glow)"/>

  <!-- Cabeza -->
  <rect x="130" y="70" width="140" height="180" rx="30" ry="30" fill="url(#head)"/>

  <!-- Visor -->
  <path d="M 145 120 L 255 120 A 10 10 0 0 1 265 130 L 265 180 A 10 10 0 0 1 255 190 L 145 190 A 10 10 0 0 1 135 180 L 135 130 A 10 10 0 0 1 145 120 Z" fill="#0f172a" stroke="#00f0ff" stroke-width="2" filter="url(#glow)"/>

  <!-- Ojos -->
  <circle cx="175" cy="155" r="10" fill="#00f0ff" filter="url(#glow-intense)"/>
  <circle cx="225" cy="155" r="10" fill="#00f0ff" filter="url(#glow-intense)"/>
  <line x1="165" y1="165" x2="185" y2="165" stroke="#ffffff" stroke-width="2" filter="url(#glow)"/>
  <line x1="215" y1="165" x2="235" y2="165" stroke="#ffffff" stroke-width="2" filter="url(#glow)"/>

  <!-- Sonrisa -->
  <path d="M 180 215 Q 200 230 220 215" stroke="#00f0ff" stroke-width="4" stroke-linecap="round" fill="none" filter="url(#glow)"/>

  <!-- Circuitos faciales -->
  <circle cx="150" cy="220" r="2" fill="#ff007f" filter="url(#glow)"/>
  <circle cx="250" cy="220" r="2" fill="#ff007f" filter="url(#glow)"/>
  <path d="M 150 220 L 150 240 L 140 250" stroke="#ff007f" stroke-width="2" fill="none" filter="url(#glow)"/>
  <path d="M 250 220 L 250 240 L 260 250" stroke="#ff007f" stroke-width="2" fill="none" filter="url(#glow)"/>

  <!-- Orejas -->
  <rect x="115" y="160" width="15" height="40" rx="5" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <rect x="270" y="160" width="15" height="40" rx="5" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <circle cx="122.5" cy="165" r="3" fill="#00f0ff" filter="url(#glow)"/>
  <circle cx="277.5" cy="165" r="3" fill="#00f0ff" filter="url(#glow)"/>

  <!-- Flujos de datos -->
  <text x="140" y="320" fill="#00f0ff" font-family="monospace" font-size="14" opacity="0.6">0</text>
  <text x="155" y="360" fill="#00f0ff" font-family="monospace" font-size="12" opacity="0.8">1</text>
  <text x="135" y="390" fill="#00f0ff" font-family="monospace" font-size="14" opacity="0.4">0</text>
  <text x="250" y="310" fill="#ff007f" font-family="monospace" font-size="12" opacity="0.7">1</text>
  <text x="265" y="345" fill="#ff007f" font-family="monospace" font-size="14" opacity="0.5">0</text>
  <text x="245" y="385" fill="#ff007f" font-family="monospace" font-size="12" opacity="0.9">1</text>

  <!-- Partículas flotantes -->
  <circle cx="60" cy="80" r="2" fill="#00f0ff" opacity="0.6" filter="url(#glow)"/>
  <circle cx="340" cy="140" r="3" fill="#ff007f" opacity="0.4" filter="url(#glow)"/>
  <circle cx="90" cy="290" r="4" fill="#00f0ff" opacity="0.5" filter="url(#glow)"/>
  <circle cx="310" cy="340" r="2" fill="#ff007f" opacity="0.8" filter="url(#glow)"/>
  <circle cx="280" cy="60" r="1.5" fill="#00f0ff" opacity="0.7"/>
  <circle cx="120" cy="50" r="2" fill="#ff007f" opacity="0.5"/>
  <circle cx="350" cy="250" r="2" fill="#00f0ff" opacity="0.6" filter="url(#glow)"/>
</svg>
```