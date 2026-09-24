```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a1a3d"/>
      <stop offset="45%" stop-color="#4a3f6b"/>
      <stop offset="70%" stop-color="#a86b8e"/>
      <stop offset="100%" stop-color="#e8b06a"/>
    </linearGradient>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff6d0"/>
      <stop offset="60%" stop-color="#ffd27a"/>
      <stop offset="100%" stop-color="#ffb84d" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b3a67"/>
      <stop offset="100%" stop-color="#0f1a30"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- estrellas tenues arriba -->
  <g fill="#ffffff" opacity="0.6">
    <circle cx="40" cy="30" r="1"/>
    <circle cx="90" cy="15" r="1.2"/>
    <circle cx="150" cy="40" r="0.8"/>
    <circle cx="300" cy="20" r="1"/>
    <circle cx="340" cy="50" r="1.3"/>
    <circle cx="200" cy="10" r="0.9"/>
    <circle cx="250" cy="35" r="1"/>
  </g>

  <!-- sol/luz -->
  <circle cx="200" cy="210" r="90" fill="url(#sun)"/>
  <circle cx="200" cy="210" r="35" fill="#ffe9b0"/>

  <!-- pajaros lejanos, algo de calma -->
  <g stroke="#2a2a40" stroke-width="2" fill="none" opacity="0.7">
    <path d="M120 90 q6 -8 12 0 q6 -8 12 0"/>
    <path d="M260 70 q5 -7 10 0 q5 -7 10 0"/>
    <path d="M170 60 q5 -6 10 0 q5 -6 10 0"/>
  </g>

  <!-- mar -->
  <rect y="230" width="400" height="170" fill="url(#water)"/>
  <g stroke="#ffdca0" stroke-opacity="0.35" stroke-width="2">
    <line x1="60" y1="235" x2="140" y2="235"/>
    <line x1="180" y1="245" x2="230" y2="245"/>
    <line x1="90" y1="255" x2="170" y2="255"/>
    <line x1="220" y1="260" x2="300" y2="260"/>
    <line x1="130" y1="275" x2="270" y2="275"/>
    <line x1="60" y1="295" x2="340" y2="295"/>
  </g>

  <!-- silueta de ciudad, un poco fracturada / grietas de tension -->
  <g fill="#111122">
    <rect x="20" y="180" width="18" height="60"/>
    <rect x="45" y="160" width="14" height="80"/>
    <rect x="65" y="195" width="20" height="45"/>
    <rect x="90" y="150" width="16" height="90"/>
    <rect x="112" y="170" width="22" height="70"/>
    <polygon points="134,240 134,140 150,120 150,240"/>
    <rect x="260" y="175" width="18" height="65"/>
    <rect x="282" y="155" width="14" height="85"/>
    <rect x="300" y="190" width="20" height="50"/>
    <rect x="325" y="140" width="16" height="100"/>
    <polygon points="345,240 345,150 360,130 360,240"/>
    <rect x="365" y="185" width="15" height="55"/>
  </g>

  <!-- ventanas encendidas, algo de humanidad en medio del caos -->
  <g fill="#ffd27a" opacity="0.85">
    <rect x="50" y="175" x2="0" width="3" height="4"/>
    <rect x="50" y="175" width="3" height="4"/>
    <rect x="50" y="190" width="3" height="4"/>
    <rect x="96" y="165" width="3" height="4"/>
    <rect x="96" y="180" width="3" height="4"/>
    <rect x="118" y="185" width="3" height="4"/>
    <rect x="118" y="200" width="3" height="4"/>
    <rect x="138" y="160" width="3" height="4"/>
    <rect x="138" y="180" width="3" height="4"/>
    <rect x="138" y="200" width="3" height="4"/>
    <rect x="286" y="170" width="3" height="4"/>
    <rect x="286" y="190" width="3" height="4"/>
    <rect x="306" y="200" width="3" height="4"/>
    <rect x="330" y="160" width="3" height="4"/>
    <rect x="330" y="180" width="3" height="4"/>
    <rect x="330" y="200" width="3" height="4"/>
    <rect x="349" y="165" width="3" height="4"/>
    <rect x="349" y="185" width="3" height="4"/>
    <rect x="349" y="205" width="3" height="4"/>
  </g>

  <!-- grieta que atraviesa la ciudad, simbolo de fractura/incertidumbre -->
  <path d="M150 240 L170 210 L160 190 L185 160 L175 140" 
        stroke="#ff5c5c" stroke-width="1.5" fill="none" opacity="0.5"/>

  <!-- una pequeña rama con brote verde, esperanza en primer plano -->
  <g transform="translate(30,330)">
    <path d="M0 70 Q10 30 40 10" stroke="#3d2b1f" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="M20 40 Q10 25 5 15" stroke="#3d2b1f" stroke-width="2" fill="none" stroke-linecap="round"/>
    <ellipse cx="3" cy="12" rx="6" ry="10" fill="#6fae5a" transform="rotate(-30 3 12)"/>
    <ellipse cx="42" cy="8" rx="7" ry="12" fill="#8fcf6a" transform="rotate(20 42 8)"/>
    <circle cx="40" cy="10" r="3" fill="#ffd27a"/>
  </g>

  <!-- manos que se alzan, buscando conexion -->
  <g stroke="#0f1a30" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.8">
    <path d="M330 400 L332 350 M332 350 L322 335 M332 350 L332 330 M332 350 L342 335 M332 350 L345 340"/>
  </g>

  <!-- linea de horizonte -->
  <line x1="0" y1="240" x2="400" y2="240" stroke="#ffdca0" stroke-width="1" opacity="0.4"/>

  <!-- reflejo del sol en el agua -->
  <ellipse cx="200" cy="245" rx="30" ry="6" fill="#ffe9b0" opacity="0.5"/>
  <ellipse cx="200" cy="260" rx="45" ry="5" fill="#ffe9b0" opacity="0.3"/>
  <ellipse cx="200" cy="278" rx="60" ry="4" fill="#ffe9b0" opacity="0.2"/>
</svg>
```