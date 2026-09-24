```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#1a1f3a"/>
      <stop offset="100%" stop-color="#0a0d1f"/>
    </radialGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7dd3fc" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#7dd3fc" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="core" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a78bfa"/>
      <stop offset="50%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- scattered stars/nodes background -->
  <g fill="#7dd3fc" opacity="0.5">
    <circle cx="30" cy="50" r="1.5"/>
    <circle cx="370" cy="40" r="1.2"/>
    <circle cx="350" cy="120" r="1"/>
    <circle cx="20" cy="200" r="1.3"/>
    <circle cx="380" cy="250" r="1.5"/>
    <circle cx="50" cy="350" r="1.2"/>
    <circle cx="330" cy="370" r="1.4"/>
    <circle cx="15" cy="120" r="1"/>
    <circle cx="200" cy="20" r="1.3"/>
  </g>

  <!-- outer neural network web -->
  <g stroke="#4c6ef5" stroke-width="0.6" opacity="0.35">
    <line x1="200" y1="200" x2="60" y2="90"/>
    <line x1="200" y1="200" x2="340" y2="90"/>
    <line x1="200" y1="200" x2="60" y2="310"/>
    <line x1="200" y1="200" x2="340" y2="310"/>
    <line x1="200" y1="200" x2="30" y2="200"/>
    <line x1="200" y1="200" x2="370" y2="200"/>
    <line x1="200" y1="200" x2="200" y2="30"/>
    <line x1="200" y1="200" x2="200" y2="370"/>
    <line x1="60" y1="90" x2="200" y2="30"/>
    <line x1="340" y1="90" x2="200" y2="30"/>
    <line x1="60" y1="310" x2="200" y2="370"/>
    <line x1="340" y1="310" x2="200" y2="370"/>
  </g>
  <g fill="#93c5fd">
    <circle cx="60" cy="90" r="3"/>
    <circle cx="340" cy="90" r="3"/>
    <circle cx="60" cy="310" r="3"/>
    <circle cx="340" cy="310" r="3"/>
    <circle cx="30" cy="200" r="3"/>
    <circle cx="370" cy="200" r="3"/>
    <circle cx="200" cy="30" r="3"/>
    <circle cx="200" cy="370" r="3"/>
  </g>

  <!-- glow behind head -->
  <circle cx="200" cy="190" r="150" fill="url(#glow)" opacity="0.5"/>

  <!-- head shape: abstract hexagon-ish "face" -->
  <g filter="url(#softGlow)">
    <path d="M200 70
             L290 115
             L300 210
             L245 290
             L155 290
             L100 210
             L110 115
             Z"
          fill="#111633" stroke="url(#core)" stroke-width="3"/>
  </g>

  <!-- inner circuit lines on face -->
  <g stroke="#60a5fa" stroke-width="1" opacity="0.5" fill="none">
    <path d="M130 140 L160 140 L160 170"/>
    <path d="M270 140 L240 140 L240 170"/>
    <path d="M150 250 L150 220 L180 220"/>
    <path d="M250 250 L250 220 L220 220"/>
    <circle cx="160" cy="170" r="3" fill="#60a5fa"/>
    <circle cx="240" cy="170" r="3" fill="#60a5fa"/>
    <circle cx="180" cy="220" r="3" fill="#60a5fa"/>
    <circle cx="220" cy="220" r="3" fill="#60a5fa"/>
  </g>

  <!-- eyes: glowing nodes -->
  <g>
    <circle cx="160" cy="185" r="14" fill="#0a0d1f" stroke="#a78bfa" stroke-width="2"/>
    <circle cx="240" cy="185" r="14" fill="#0a0d1f" stroke="#a78bfa" stroke-width="2"/>
    <circle cx="160" cy="185" r="6" fill="#7dd3fc">
      <animate attributeName="r" values="6;8;6" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="240" cy="185" r="6" fill="#7dd3fc">
      <animate attributeName="r" values="6;8;6" dur="3s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- nose bridge line -->
  <line x1="200" y1="195" x2="200" y2="225" stroke="#4c6ef5" stroke-width="1.5" opacity="0.6"/>

  <!-- mouth: soft curved smile made of segments/circuit -->
  <path d="M165 250 Q200 275 235 250" stroke="url(#core)" stroke-width="3" fill="none" stroke-linecap="round"/>
  <circle cx="165" cy="250" r="3" fill="#34d399"/>
  <circle cx="235" cy="250" r="3" fill="#34d399"/>
  <circle cx="200" cy="266" r="3" fill="#34d399"/>

  <!-- circuit lines emanating from head, like "thoughts" -->
  <g stroke="#7dd3fc" stroke-width="1" opacity="0.5" fill="none">
    <path d="M110 130 Q70 110 50 70"/>
    <path d="M290 130 Q330 110 350 70"/>
    <path d="M105 230 Q60 250 40 300"/>
    <path d="M295 230 Q340 250 360 300"/>
  </g>
  <g fill="#7dd3fc">
    <circle cx="50" cy="70" r="2.5"/>
    <circle cx="350" cy="70" r="2.5"/>
    <circle cx="40" cy="300" r="2.5"/>
    <circle cx="360" cy="300" r="2.5"/>
  </g>

  <!-- small floating data particles -->
  <g fill="#a78bfa" opacity="0.7">
    <circle cx="80" cy="160" r="2">
      <animate attributeName="cy" values="160;150;160" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="320" cy="170" r="2">
      <animate attributeName="cy" values="170;160;170" dur="3.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="200" cy="330" r="2">
      <animate attributeName="cy" values="330;320;330" dur="3s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- subtle top "antenna" node, like an AI crown -->
  <line x1="200" y1="70" x2="200" y2="45" stroke="#60a5fa" stroke-width="2"/>
  <circle cx="200" cy="40" r="6" fill="url(#core)">
    <animate attributeName="r" values="6;9;6" dur="2.5s" repeatCount="indefinite"/>
  </circle>

  <!-- label -->
  <text x="200" y="386" text-anchor="middle" font-family="monospace" font-size="12" fill="#7dd3fc" opacity="0.7">a mind made of light and logic</text>
</svg>
```