<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a1040"/>
      <stop offset="45%" stop-color="#6b2d6b"/>
      <stop offset="78%" stop-color="#e07a4a"/>
      <stop offset="100%" stop-color="#f6c36a"/>
    </linearGradient>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff6d0"/>
      <stop offset="55%" stop-color="#ffb347"/>
      <stop offset="100%" stop-color="#ff7a3c"/>
    </radialGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3a4a7a"/>
      <stop offset="100%" stop-color="#14203a"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="80" cy="48" r="1.2" fill="#fff"/>
  <circle cx="140" cy="32" r="1" fill="#ffe"/>
  <circle cx="210" cy="56" r="1.4" fill="#fff"/>
  <circle cx="260" cy="28" r="1" fill="#fff8e0"/>
  <circle cx="310" cy="44" r="1.1" fill="#fff"/>
  <circle cx="350" cy="70" r="0.9" fill="#fff"/>
  <circle cx="40" cy="90" r="0.8" fill="#fff"/>
  <circle cx="180" cy="22" r="0.7" fill="#fff"/>
  <circle cx="290" cy="18" r="1.2" fill="#fff"/>
  <circle cx="370" cy="36" r="0.8" fill="#ffe"/>
  <circle cx="200" cy="248" r="62" fill="url(#sun)" filter="url(#glow)"/>
  <ellipse cx="200" cy="248" rx="18" ry="6" fill="#fff6c8" opacity="0.7"/>
  <path d="M0 250 C40 230 70 270 110 248 C150 226 170 260 210 244 C250 228 280 268 320 246 C360 224 380 258 400 240 L400 400 L0 400 Z" fill="#2a1848" opacity="0.55"/>
  <path d="M0 280 C50 260 90 300 140 276 C190 252 210 292 260 270 C310 248 340 292 400 266 L400 400 L0 400 Z" fill="#1c1238"/>
  <path d="M0 310 C60 296 100 328 160 308 C220 288 250 330 310 312 C350 300 380 322 400 308 L400 400 L0 400 Z" fill="#120c28"/>
  <rect y="318" width="400" height="82" fill="url(#sea)"/>
  <path d="M0 332 Q50 326 100 334 T200 332 T300 336 T400 330" fill="none" stroke="#f6c36a" stroke-width="1.2" opacity="0.55"/>
  <path d="M0 348 Q40 342 90 350 T180 346 T270 352 T400 344" fill="none" stroke="#ffb07a" stroke-width="0.8" opacity="0.35"/>
  <path d="M0 364 Q60 358 120 366 T240 360 T360 368 T400 362" fill="none" stroke="#fff" stroke-width="0.6" opacity="0.2"/>
  <g fill="#0e0a1c">
    <ellipse cx="70" cy="392" rx="28" ry="6"/>
    <path d="M58 392 C62 360 66 340 74 318 C76 340 80 362 86 392 Z"/>
    <path d="M74 330 C78 318 82 322 80 334" fill="none" stroke="#1a3a28" stroke-width="2"/>
    <circle cx="74" cy="314" r="6" fill="#163828"/>
  </g>
  <g transform="translate(300,300)">
    <path d="M0 20 C8 8 18 4 28 8 C22 14 16 18 8 22 Z" fill="#1a1028"/>
    <path d="M8 22 C16 16 26 18 34 26 C22 24 14 26 6 30 Z" fill="#241838"/>
    <circle cx="26" cy="10" r="1.4" fill="#ffd27a"/>
  </g>
  <path d="M120 150 C128 146 136 150 132 156 C140 150 150 154 144 162 C136 158 128 160 122 156 Z" fill="#2a1840" opacity="0.8"/>
  <path d="M150 120 C156 116 164 120 160 126 C168 120 176 124 170 132 C162 128 154 130 148 126 Z" fill="#1c1230" opacity="0.7"/>
</svg>