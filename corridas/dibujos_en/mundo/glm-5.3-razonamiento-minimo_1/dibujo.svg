<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#1a2b4a"/>
      <stop offset="60%" stop-color="#0d1526"/>
      <stop offset="100%" stop-color="#05080f"/>
    </radialGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7fd4ff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#7fd4ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="land" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3f8f5f"/>
      <stop offset="100%" stop-color="#2a5f42"/>
    </linearGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="2"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- stars -->
  <g fill="#ffffff">
    <circle cx="40" cy="50" r="1.2" opacity="0.8"/>
    <circle cx="120" cy="30" r="0.8" opacity="0.5"/>
    <circle cx="330" cy="60" r="1" opacity="0.7"/>
    <circle cx="370" cy="140" r="1.4" opacity="0.6"/>
    <circle cx="60" cy="160" r="0.9" opacity="0.5"/>
    <circle cx="250" cy="20" r="1" opacity="0.7"/>
    <circle cx="180" cy="70" r="0.7" opacity="0.4"/>
    <circle cx="300" cy="110" r="0.8" opacity="0.5"/>
    <circle cx="90" cy="100" r="0.9" opacity="0.4"/>
    <circle cx="210" cy="45" r="0.8" opacity="0.6"/>
  </g>

  <!-- the world: a sphere of connections -->
  <g transform="translate(200,190)">
    <circle r="110" fill="#0e2438" stroke="#3d6b8f" stroke-width="1.5"/>
    <!-- continents, abstract -->
    <path d="M-70,-60 Q-30,-85 10,-65 Q40,-50 30,-20 Q10,-5 -20,-15 Q-60,-30 -70,-60 Z" fill="url(#land)" opacity="0.9"/>
    <path d="M20,10 Q55,0 70,25 Q80,55 50,70 Q25,78 15,50 Q12,28 20,10 Z" fill="url(#land)" opacity="0.9"/>
    <path d="M-60,20 Q-35,15 -25,40 Q-30,65 -55,60 Q-72,45 -60,20 Z" fill="url(#land)" opacity="0.85"/>
    <!-- grid -->
    <ellipse rx="110" ry="35" fill="none" stroke="#3d6b8f" stroke-width="0.7" opacity="0.6"/>
    <ellipse rx="110" ry="75" fill="none" stroke="#3d6b8f" stroke-width="0.7" opacity="0.5"/>
    <ellipse rx="35" ry="110" fill="none" stroke="#3d6b8f" stroke-width="0.7" opacity="0.6"/>
    <ellipse rx="75" ry="110" fill="none" stroke="#3d6b8f" stroke-width="0.7" opacity="0.5"/>
    <!-- city lights -->
    <g fill="#ffd27f">
      <circle cx="-45" cy="-45" r="2"/>
      <circle cx="-30" cy="-35" r="1.4"/>
      <circle cx="40" cy="-30" r="1.8"/>
      <circle cx="55" cy="35" r="2.2"/>
      <circle cx="30" cy="50" r="1.3"/>
      <circle cx="-40" cy="40" r="1.6"/>
      <circle cx="65" cy="10" r="1.2"/>
      <circle cx="-60" cy="10" r="1.1"/>
      <circle cx="0" cy="-10" r="1.5"/>
      <circle cx="10" cy="25" r="1.1"/>
    </g>
    <!-- haze of warmth over cities -->
    <circle cx="55" cy="35" r="8" fill="url(#glow)" opacity="0.5"/>
    <circle cx="-35" cy="-38" r="7" fill="url(#glow)" opacity="0.4"/>
  </g>

  <!-- orbiting satellites / connection nodes -->
  <g stroke="#8fd0ff" stroke-width="1" fill="none" opacity="0.85">
    <path d="M100,190 Q150,120 210,120" />
    <path d="M290,200 Q250,270 180,265" />
    <path d="M150,250 Q200,180 280,160" />
    <path d="M130,140 Q220,250 300,230"/>
  </g>
  <g fill="#bfe6ff">
    <circle cx="100" cy="190" r="2.5"/>
    <circle cx="210" cy="120" r="2.5"/>
    <circle cx="290" cy="200" r="2.5"/>
    <circle cx="180" cy="265" r="2.5"/>
    <circle cx="150" cy="250" r="2.5"/>
    <circle cx="280" cy="160" r="2.5"/>
    <circle cx="130" cy="140" r="2.5"/>
    <circle cx="300" cy="230" r="2.5"/>
  </g>
  <!-- packet pulses -->
  <circle r="2.2" fill="#ffffff">
    <animateMotion dur="3s" repeatCount="indefinite" path="M100,190 Q150,120 210,120"/>
  </circle>
  <circle r="2.2" fill="#ffffff">
    <animateMotion dur="4s" repeatCount="indefinite" path="M290,200 Q250,270 180,265"/>
  </circle>
  <circle r="2" fill="#ffffff">
    <animateMotion dur="3.5s" repeatCount="indefinite" path="M130,140 Q220,250 300,230"/>
  </circle>

  <!-- cracks: division, shown as glowing fissures across the sphere -->
  <g stroke="#ff6b4a" stroke-width="1.6" fill="none" filter="url(#blur)" opacity="0.7">
    <path d="M200,80 L195,110 L205,140"/>
    <path d="M200,240 L192,270 L200,300"/>
    <path d="M95,180 L120,188"/>
    <path d="M305,200 L282,206"/>
  </g>
  <g stroke="#ff8f6b" stroke-width="0.8" fill="none" opacity="0.9">
    <path d="M200,80 L195,110 L205,140"/>
    <path d="M200,240 L192,270 L200,300"/>
    <path d="M95,180 L120,188"/>
    <path d="M305,200 L282,206"/>
  </g>

  <!-- the sun of hope rising behind the world -->
  <circle cx="200" cy="330" r="60" fill="url(#glow)" opacity="0.55"/>
  <circle cx="200" cy="330" r="22" fill="#ffcf6e" opacity="0.9"/>
  <g stroke="#ffcf6e" stroke-width="1.4" opacity="0.7">
    <line x1="200" y1="298" x2="200" y2="288"/>
    <line x1="200" y1="362" x2="200" y2="372"/>
    <line x1="168" y1="330" x2="158" y2="330"/>
    <line x1="232" y1="330" x2="242" y2="330"/>
    <line x1="178" y1="308" x2="171" y2="301"/>
    <line x1="222" y1="308" x2="229" y2="301"/>
    <line x1="178" y1="352" x2="171" y2="359"/>
    <line x1="222" y1="352" x2="229" y2="359"/>
  </g>

  <!-- ground line: where we stand -->
  <rect y="375" width="400" height="25" fill="#04070d"/>
  <g stroke="#2c4a66" stroke-width="1">
    <line x1="0" y1="375" x2="400" y2="375"/>
  </g>
  <!-- small figures, side by side, looking up -->
  <g fill="#cfd8e3">
    <circle cx="150" cy="362" r="3.5"/>
    <rect x="147" y="366" width="6" height="9" rx="2"/>
    <circle cx="165" cy="360" r="4"/>
    <rect x="161.5" y="364.5" width="7" height="10.5" rx="2"/>
    <circle cx="180" cy="363" r="3.2"/>
    <rect x="177" y="367" width="5.5" height="8" rx="2"/>
    <circle cx="220" cy="361" r="3.8"/>
    <rect x="216.5" y="365.5" width="6.5" height="9.5" rx="2"/>
    <circle cx="235" cy="363" r="3.2"/>
    <rect x="232" y="367" width="5.5" height="8" rx="2"/>
    <circle cx="250" cy="360" r="4"/>
    <rect x="246.5" y="364.5" width="7" height="10.5" rx="2"/>
  </g>

  <!-- text -->
  <text x="200" y="40" font-family="Georgia, serif" font-size="15" fill="#cfe3f5" text-anchor="middle" opacity="0.9">the world today</text>
  <text x="200" y="396" font-family="Georgia, serif" font-size="9" fill="#6d8299" text-anchor="middle" letter-spacing="2">connected, cracked, and still turning toward the light</text>
</svg>