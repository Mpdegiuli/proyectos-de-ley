```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#0a0a1a"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
    <linearGradient id="head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a1a35"/>
      <stop offset="100%" stop-color="#0a0a15"/>
    </linearGradient>
    <linearGradient id="shoulders" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#15152a"/>
      <stop offset="100%" stop-color="#05050a"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="glowLarge" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="4" y2="0" stroke="#FFFFFF" stroke-width="1.5" opacity="0.08"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- Background Grid -->
  <g stroke="#00F0FF" stroke-width="0.5" opacity="0.05">
    <line x1="50" y1="0" x2="50" y2="400"/>
    <line x1="100" y1="0" x2="100" y2="400"/>
    <line x1="150" y1="0" x2="150" y2="400"/>
    <line x1="200" y1="0" x2="200" y2="400"/>
    <line x1="250" y1="0" x2="250" y2="400"/>
    <line x1="300" y1="0" x2="300" y2="400"/>
    <line x1="350" y1="0" x2="350" y2="400"/>
    <line x1="0" y1="50" x2="400" y2="50"/>
    <line x1="0" y1="100" x2="400" y2="100"/>
    <line x1="0" y1="150" x2="400" y2="150"/>
    <line x1="0" y1="200" x2="400" y2="200"/>
    <line x1="0" y1="250" x2="400" y2="250"/>
    <line x1="0" y1="300" x2="400" y2="300"/>
    <line x1="0" y1="350" x2="400" y2="350"/>
  </g>

  <!-- Orbits / Neural Rings -->
  <ellipse cx="200" cy="160" rx="140" ry="120" fill="none" stroke="#00F0FF" stroke-width="1" stroke-dasharray="15 10 5 10" opacity="0.4" transform="rotate(15 200 160)"/>
  <ellipse cx="200" cy="160" rx="150" ry="130" fill="none" stroke="#FF007F" stroke-width="0.5" stroke-dasharray="2 6" opacity="0.3" transform="rotate(-25 200 160)"/>
  <ellipse cx="200" cy="160" rx="100" ry="90" fill="none" stroke="#00F0FF" stroke-width="0.5" stroke-dasharray="1 5" opacity="0.5" transform="rotate(45 200 160)"/>

  <!-- Circuit Traces (From head to canvas edge) -->
  <g stroke="#00F0FF" stroke-width="1.5" fill="none" opacity="0.6">
    <path d="M 105 120 L 60 120 L 40 100 L 15 100"/>
    <path d="M 105 220 L 70 220 L 50 240 L 20 240"/>
    <path d="M 295 120 L 340 120 L 360 100 L 385 100"/>
    <path d="M 295 220 L 330 220 L 350 240 L 380 240"/>
    <path d="M 160 65 L 160 30 L 140 10"/>
    <path d="M 240 65 L 240 30 L 260 10"/>
  </g>
  
  <!-- Trace Endpoints -->
  <g fill="#FF007F" filter="url(#glow)">
    <circle cx="15" cy="100" r="3"/>
    <circle cx="20" cy="240" r="3"/>
    <circle cx="385" cy="100" r="3"/>
    <circle cx="380" cy="240" r="3"/>
    <circle cx="140" cy="10" r="3"/>
    <circle cx="260" cy="10" r="3"/>
  </g>

  <!-- Background Nodes -->
  <g fill="#00F0FF" opacity="0.5">
    <circle cx="50" cy="50" r="2"/>
    <circle cx="350" cy="50" r="2"/>
    <circle cx="80" cy="300" r="3"/>
    <circle cx="320" cy="320" r="4"/>
    <circle cx="30" cy="350" r="2"/>
  </g>

  <!-- Shoulders -->
  <path d="M 90 280 L 90 260 Q 90 235 115 235 L 285 235 Q 310 235 310 260 L 310 280 Q 310 325 270 325 L 130 325 Q 90 325 90 280 Z" fill="url(#shoulders)" stroke="#2A2A4A" stroke-width="3"/>
  
  <!-- Shoulder Details / Circuitry -->
  <g stroke="#2A2A4A" stroke-width="2" fill="none">
    <path d="M 125 260 L 125 300"/>
    <path d="M 275 260 L 275 300"/>
    <path d="M 150 285 L 150 315 L 170 315"/>
    <path d="M 250 285 L 250 315 L 230 315"/>
  </g>
  <circle cx="170" cy="315" r="2.5" fill="#00F0FF"/>
  <circle cx="230" cy="315" r="2.5" fill="#00F0FF"/>

  <!-- Neck -->
  <rect x="175" y="205" width="50" height="40" fill="#0A0A15" stroke="#2A2A4A" stroke-width="3"/>
  <circle cx="200" cy="225" r="4" fill="none" stroke="#00F0FF" stroke-width="1.5" opacity="0.6"/>

  <!-- Head -->
  <rect x="85" y="60" width="230" height="200" rx="30" fill="url(#head)" stroke="#2A2A4A" stroke-width="4"/>
  
  <!-- Head Details / Seams -->
  <line x1="105" y1="60" x2="105" y2="80" stroke="#00F0FF" stroke-width="2" opacity="0.5"/>
  <line x1="295" y1="60" x2="295" y2="80" stroke="#00F0FF" stroke-width="2" opacity="0.5"/>
  <line x1="105" y1="240" x2="105" y2="260" stroke="#00F0FF" stroke-width="2" opacity="0.5"/>
  <line x1="295" y1="240" x2="295" y2="260" stroke="#00F0FF" stroke-width="2" opacity="0.5"/>

  <!-- Face Screen -->
  <rect x="105" y="80" width="190" height="160" rx="20" fill="#050510" stroke="#00F0FF" stroke-width="2" opacity="0.95"/>
  <rect x="110" y="85" width="180" height="150" rx="15" fill="none" stroke="#00F0FF" stroke-width="1" opacity="0.3"/>
  <rect x="105" y="80" width="190" height="160" rx="20" fill="url(#scanlines)" pointer-events="none"/>

  <!-- Facial Features (Robotic / AI Core) -->
  
  <!-- Eyes -->
  <circle cx="145" cy="130" r="12" fill="#00F0FF" filter="url(#glow)"/>
  <circle cx="145" cy="130" r="4" fill="#FFFFFF"/>
  <path d="M 138 122 L 152 138" stroke="#FFFFFF" stroke-width="1.5" opacity="0.7"/>

  <circle cx="255" cy="130" r="12" fill="#00F0FF" filter="url(#glow)"/>
  <circle cx="255" cy="130" r="4" fill="#FFFFFF"/>
  <path d="M 248 122 L 262 138" stroke="#FFFFFF" stroke-width="1.5" opacity="0.7"/>

  <!-- Central Core (Mind / Processor) -->
  <rect x="182" y="100" width="36" height="36" rx="10" fill="#FF007F" filter="url(#glowLarge)"/>
  <rect x="192" y="110" width="16" height="16" rx="4" fill="#FFFFFF"/>
  
  <!-- Core Crosshairs -->
  <line x1="200" y1="95" x2="200" y2="141" stroke="#00F0FF" stroke-width="1" opacity="0.4"/>
  <line x1="178" y1="118" x2="222" y2="118" stroke="#00F0FF" stroke-width="1" opacity="0.4"/>
  
  <!-- Core Data Links -->
  <g stroke="#FF007F" stroke-width="1" opacity="0.6" fill="none">
    <path d="M 182 118 L 155 118 L 145 110"/>
    <path d="M 218 118 L 245 118 L 255 110"/>
    <path d="M 200 136 L 200 145 L 190 155"/>
  </g>
  <circle cx="145" cy="110" r="2" fill="#FF007F"/>
  <circle cx="255" cy="110" r="2" fill="#FF007F"/>
  <circle cx="190" cy="155" r="2" fill="#FF007F"/>

  <!-- Mouth (Data Visualizer) -->
  <rect x="160" y="195" width="80" height="14" rx="7" fill="#0A0A15" stroke="#00F0FF" stroke-width="1.5"/>
  
  <!-- Equalizer Bars -->
  <rect x="165" y="198" width="4" height="6" fill="#00F0FF"/>
  <rect x="173" y="198" width="4" height="4" fill="#00F0FF"/>
  <rect x="181" y="198" width="4" height="8" fill="#FF007F"/>
  <rect x="189" y="198" width="4" height="3" fill="#00F0FF"/>
  <rect x="197" y="198" width="4" height="7" fill="#FFFFFF"/>
  <rect x="205" y="198" width="4" height="5" fill="#FF007F"/>
  <rect x="213" y="198" width="4" height="9" fill="#00F0FF"/>
  <rect x="221" y="198" width="4" height="4" fill="#00F0FF"/>
  <rect x="229" y="198" width="4" height="6" fill="#00F0FF"/>
  
  <!-- Text Label -->
  <text x="200" y="225" fill="#00F0FF" font-family="monospace, sans-serif" font-size="8" text-anchor="middle" opacity="0.8" font-weight="bold">AI CORE v4.0</text>

  <!-- Cheek / Jaw Details -->
  <path d="M 125 165 L 140 155" stroke="#2A2A4A" stroke-width="2.5"/>
  <path d="M 275 165 L 260 155" stroke="#2A2A4A" stroke-width="2.5"/>
  <line x1="125" y1="215" x2="125" y2="235" stroke="#2A2A4A" stroke-width="2.5"/>
  <line x1="275" y1="215" x2="275" y2="235" stroke="#2A2A4A" stroke-width="2.5"/>

  <!-- Binary Data Streams -->
  <g fill="#00F0FF" font-family="monospace, sans-serif" font-size="12" opacity="0.6">
    <!-- Left Stream -->
    <text x="30" y="85">01</text>
    <text x="30" y="100">10</text>
    <text x="30" y="115">11</text>
    <text x="30" y="130">00</text>
    <text x="30" y="145">10</text>
    <text x="30" y="160">01</text>
    <text x="30" y="175">11</text>
    <text x="30" y="190">00</text>
    <text x="30" y="205">10</text>
    <text x="30" y="220">01</text>
    <text x="30" y="235">11</text>
    <text x="30" y="250">00</text>
    <text x="30" y="265">10</text>
    
    <!-- Right Stream -->
    <text x="340" y="85">10</text>
    <text x="340" y="100">01</text>
    <text x="340" y="115">11</text>
    <text x="340" y="130">00</text>
    <text x="340" y="145">01</text>
    <text x="340" y="160">10</text>
    <text x="340" y="175">00</text>
    <text x="340" y="190">11</text>
    <text x="340" y="205">01</text>
    <text x="340" y="220">10</text>
    <text x="340" y="235">00</text>
    <text x="340" y="250">11</text>
    <text x="340" y="265">01</text>
  </g>

  <!-- Power Button / Chest Glow -->
  <circle cx="200" cy="260" r="8" fill="#0A0A15" stroke="#FF007F" stroke-width="2" filter="url(#glow)"/>
  <path d="M 200 256 L 200 264" stroke="#FF007F" stroke-width="1.5"/>
  <path d="M 196 260 L 204 260" stroke="#FF007F" stroke-width="1.5"/>

</svg>
```