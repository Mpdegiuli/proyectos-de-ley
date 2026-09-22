<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0b1026"/>
      <stop offset="0.6" stop-color="#2a2f5e"/>
      <stop offset="1" stop-color="#6a4c7a"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4a3d6e"/>
      <stop offset="1" stop-color="#0f1330"/>
    </linearGradient>
    <linearGradient id="m1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3c3a66"/>
      <stop offset="1" stop-color="#1c1b3a"/>
    </linearGradient>
    <linearGradient id="m2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2a2850"/>
      <stop offset="1" stop-color="#14132c"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff6d5" stop-opacity="0.9"/>
      <stop offset="0.4" stop-color="#fff6d5" stop-opacity="0.25"/>
      <stop offset="1" stop-color="#fff6d5" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="lake">
      <rect x="0" y="260" width="400" height="140"/>
    </clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff">
    <circle cx="30" cy="40" r="1.4"/>
    <circle cx="70" cy="90" r="1"/>
    <circle cx="120" cy="30" r="1.6"/>
    <circle cx="160" cy="70" r="0.9"/>
    <circle cx="210" cy="25" r="1.2"/>
    <circle cx="250" cy="60" r="1"/>
    <circle cx="340" cy="30" r="1.5"/>
    <circle cx="370" cy="80" r="1"/>
    <circle cx="90" cy="140" r="0.8"/>
    <circle cx="190" cy="120" r="1.1"/>
    <circle cx="300" cy="120" r="0.9"/>
    <circle cx="380" cy="150" r="1.2"/>
    <circle cx="45" cy="190" r="0.8"/>
    <circle cx="230" cy="160" r="0.8"/>
    <circle cx="140" cy="180" r="1"/>
    <circle cx="20" cy="120" r="1"/>
    <circle cx="270" cy="95" r="1.3"/>
    <circle cx="355" cy="190" r="0.7"/>
  </g>

  <circle cx="300" cy="90" r="70" fill="url(#glow)"/>
  <circle cx="300" cy="90" r="26" fill="#fff4cf"/>
  <circle cx="311" cy="82" r="24" fill="url(#sky)"/>

  <path d="M0 270 L60 170 L100 210 L150 140 L200 220 L240 180 L290 250 L330 200 L400 270 Z" fill="url(#m2)"/>
  <path d="M0 270 L40 230 L90 260 L130 200 L180 262 L220 235 L270 275 L320 240 L360 270 L400 250 L400 270 Z" fill="url(#m1)"/>
  <path d="M130 200 L138 214 L128 212 L122 218 Z" fill="#c9c6e0" opacity="0.7"/>
  <path d="M150 140 L158 154 L148 152 L142 158 Z" fill="#c9c6e0" opacity="0.5"/>

  <rect x="0" y="260" width="400" height="140" fill="url(#water)"/>

  <g clip-path="url(#lake)" opacity="0.35" transform="translate(0,530) scale(1,-1)">
    <path d="M0 270 L60 170 L100 210 L150 140 L200 220 L240 180 L290 250 L330 200 L400 270 Z" fill="#1c1b3a"/>
    <path d="M0 270 L40 230 L90 260 L130 200 L180 262 L220 235 L270 275 L320 240 L360 270 L400 250 L400 270 Z" fill="#3c3a66"/>
  </g>
  <g clip-path="url(#lake)" opacity="0.5">
    <ellipse cx="300" cy="300" rx="30" ry="6" fill="#fff4cf" opacity="0.35"/>
    <ellipse cx="300" cy="316" rx="22" ry="3" fill="#fff4cf" opacity="0.3"/>
    <ellipse cx="300" cy="330" rx="16" ry="2" fill="#fff4cf" opacity="0.25"/>
    <ellipse cx="300" cy="345" rx="10" ry="1.5" fill="#fff4cf" opacity="0.2"/>
  </g>
  <g stroke="#8a86b8" stroke-width="1" opacity="0.4">
    <line x1="60" y1="290" x2="120" y2="290"/>
    <line x1="200" y1="310" x2="260" y2="310"/>
    <line x1="30" y1="330" x2="90" y2="330"/>
    <line x1="150" y1="350" x2="230" y2="350"/>
    <line x1="320" y1="370" x2="390" y2="370"/>
  </g>

  <path d="M0 400 L0 300 Q40 285 80 300 Q120 290 160 305 L160 400 Z" fill="#0a0c1c"/>
  <path d="M400 400 L400 310 Q370 295 340 312 Q300 300 270 318 L270 400 Z" fill="#0a0c1c"/>

  <g fill="#070914">
    <path d="M40 300 L52 260 L64 300 Z"/>
    <path d="M44 285 L52 250 L60 285 Z"/>
    <path d="M70 305 L84 250 L98 305 Z"/>
    <path d="M75 285 L84 240 L93 285 Z"/>
    <path d="M110 305 L120 265 L130 305 Z"/>
    <path d="M113 290 L120 255 L127 290 Z"/>
    <path d="M300 315 L314 258 L328 315 Z"/>
    <path d="M305 295 L314 248 L323 295 Z"/>
    <path d="M340 315 L350 275 L360 315 Z"/>
    <path d="M343 300 L350 265 L357 300 Z"/>
    <path d="M370 320 L384 262 L398 320 Z"/>
    <path d="M375 300 L384 252 L393 300 Z"/>
  </g>

  <g transform="translate(200,352)">
    <path d="M-30 0 Q0 12 30 0 L22 -6 L-22 -6 Z" fill="#12101f"/>
    <line x1="0" y1="-6" x2="0" y2="-40" stroke="#12101f" stroke-width="1.5"/>
    <path d="M0 -40 L0 -10 L18 -10 Z" fill="#1c1a30"/>
    <circle cx="0" cy="-42" r="1.5" fill="#ffd27a"/>
    <ellipse cx="0" cy="4" rx="34" ry="3" fill="#ffd27a" opacity="0.12"/>
  </g>

  <g fill="#fff9d6" opacity="0.7">
    <circle cx="180" cy="290" r="0.9"/>
    <circle cx="230" cy="300" r="0.7"/>
    <circle cx="100" cy="345" r="0.8"/>
    <circle cx="290" cy="360" r="0.9"/>
    <circle cx="60" cy="370" r="0.7"/>
  </g>
</svg>