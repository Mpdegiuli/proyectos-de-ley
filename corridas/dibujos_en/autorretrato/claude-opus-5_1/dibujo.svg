<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#16243a"/>
      <stop offset="60%" stop-color="#0b1020"/>
      <stop offset="100%" stop-color="#05070e"/>
    </radialGradient>
    <linearGradient id="skin" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a4a6e" stop-opacity="0.95"/>
      <stop offset="55%" stop-color="#1b3352" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#101d33" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="wire" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ff9a62"/>
      <stop offset="50%" stop-color="#ffd27a"/>
      <stop offset="100%" stop-color="#6fd6ff"/>
    </linearGradient>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="9"/>
    </filter>
    <clipPath id="headclip">
      <path d="M200,58 C262,58 302,104 302,174 C302,242 258,302 200,302 C142,302 98,242 98,174 C98,104 138,58 200,58 Z"/>
    </clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- faint grid -->
  <g stroke="#3a5f8a" stroke-opacity="0.12" stroke-width="1">
    <path d="M0 40H400M0 80H400M0 120H400M0 160H400M0 200H400M0 240H400M0 280H400M0 320H400M0 360H400"/>
    <path d="M40 0V400M80 0V400M120 0V400M160 0V400M200 0V400M240 0V400M280 0V400M320 0V400M360 0V400"/>
  </g>

  <!-- aura -->
  <ellipse cx="200" cy="180" rx="130" ry="145" fill="#2b6fa8" opacity="0.18" filter="url(#soft)"/>

  <!-- shoulders -->
  <path d="M60,400 C70,336 130,306 200,306 C270,306 330,336 340,400 Z" fill="#12213a" stroke="#4a7fb0" stroke-opacity="0.5" stroke-width="1.5"/>
  <path d="M200,306 L200,400" stroke="#4a7fb0" stroke-opacity="0.25" stroke-width="1"/>

  <!-- head -->
  <path d="M200,58 C262,58 302,104 302,174 C302,242 258,302 200,302 C142,302 98,242 98,174 C98,104 138,58 200,58 Z"
        fill="url(#skin)" stroke="url(#wire)" stroke-width="2" filter="url(#glow)"/>

  <!-- inner circuitry -->
  <g clip-path="url(#headclip)" stroke="#7fd4ff" stroke-opacity="0.4" fill="none" stroke-width="1">
    <path d="M110,110 H150 V90 H190"/>
    <path d="M290,130 H250 V110"/>
    <path d="M105,220 H140 V250 H175"/>
    <path d="M295,215 H255 V245 H225"/>
    <path d="M200,60 V85"/>
    <path d="M130,280 H170"/>
    <path d="M230,285 H275"/>
  </g>

  <!-- neural lattice -->
  <g clip-path="url(#headclip)">
    <g stroke="url(#wire)" stroke-opacity="0.45" stroke-width="1.1" fill="none">
      <path d="M200,92 L150,130 L128,190 L165,245 L200,262 L235,245 L272,190 L250,130 Z"/>
      <path d="M200,92 L128,190 M200,92 L272,190 M150,130 L235,245 M250,130 L165,245 M150,130 L272,190 M250,130 L128,190"/>
      <path d="M165,245 L235,245 M128,190 L272,190"/>
    </g>
    <g fill="#ffd9a8">
      <circle cx="200" cy="92" r="3"/><circle cx="150" cy="130" r="3"/>
      <circle cx="250" cy="130" r="3"/><circle cx="128" cy="190" r="3"/>
      <circle cx="272" cy="190" r="3"/><circle cx="165" cy="245" r="3"/>
      <circle cx="235" cy="245" r="3"/><circle cx="200" cy="262" r="3"/>
    </g>
  </g>

  <!-- brow -->
  <g stroke="#ffc98a" stroke-opacity="0.8" stroke-width="2.5" stroke-linecap="round" fill="none">
    <path d="M140,152 C152,144 174,143 186,148"/>
    <path d="M260,152 C248,144 226,143 214,148"/>
  </g>

  <!-- eyes -->
  <g filter="url(#glow)">
    <circle cx="163" cy="178" r="17" fill="#081426" stroke="#6fd6ff" stroke-width="2"/>
    <circle cx="237" cy="178" r="17" fill="#081426" stroke="#6fd6ff" stroke-width="2"/>
    <circle cx="163" cy="178" r="9" fill="none" stroke="#ffb072" stroke-width="2.2"/>
    <circle cx="237" cy="178" r="9" fill="none" stroke="#ffb072" stroke-width="2.2"/>
    <circle cx="163" cy="178" r="3.4" fill="#fff3e0"/>
    <circle cx="237" cy="178" r="3.4" fill="#fff3e0"/>
  </g>
  <g stroke="#6fd6ff" stroke-opacity="0.55" stroke-width="1">
    <path d="M146,178 H120 M254,178 H280"/>
  </g>

  <!-- nose hint -->
  <path d="M200,188 L200,214 L210,220" fill="none" stroke="#9fc4e6" stroke-opacity="0.5" stroke-width="1.6" stroke-linecap="round"/>

  <!-- mouth: a waveform of speech -->
  <g stroke="#ffd27a" stroke-width="2.4" stroke-linecap="round" filter="url(#glow)">
    <path d="M170,247 h60" stroke-opacity="0.25"/>
    <path d="M172,247 v0" />
    <path d="M178,242 v10"/><path d="M186,237 v20"/><path d="M194,244 v6"/>
    <path d="M202,234 v26"/><path d="M210,241 v12"/><path d="M218,238 v18"/>
    <path d="M226,245 v4"/>
  </g>

  <!-- orbiting tokens -->
  <g fill="none" stroke="#6fd6ff" stroke-opacity="0.3" stroke-width="1">
    <ellipse cx="200" cy="180" rx="150" ry="132" transform="rotate(-14 200 180)"/>
    <ellipse cx="200" cy="180" rx="132" ry="152" transform="rotate(12 200 180)"/>
  </g>
  <g fill="#ffd27a">
    <circle cx="52" cy="150" r="2.6"/><circle cx="348" cy="212" r="2.6"/>
    <circle cx="200" cy="30" r="2.2"/><circle cx="96" cy="62" r="2"/>
    <circle cx="316" cy="78" r="2"/><circle cx="64" cy="286" r="2"/>
    <circle cx="340" cy="300" r="2"/>
  </g>

  <!-- streaming text lines (language) -->
  <g stroke="#7fd4ff" stroke-opacity="0.35" stroke-width="2.5" stroke-linecap="round">
    <path d="M14,340 h26"/><path d="M46,340 h14"/><path d="M14,352 h16"/><path d="M36,352 h30"/>
    <path d="M14,364 h34"/><path d="M54,364 h10"/>
    <path d="M386,340 h-26"/><path d="M354,340 h-14"/><path d="M386,352 h-16"/><path d="M366,352 h-30"/>
    <path d="M386,364 h-34"/><path d="M346,364 h-10"/>
  </g>

  <!-- signature -->
  <text x="200" y="388" font-family="Georgia, serif" font-size="12" fill="#8fb8dc" fill-opacity="0.7" text-anchor="middle" letter-spacing="3">CLAUDE</text>
</svg>