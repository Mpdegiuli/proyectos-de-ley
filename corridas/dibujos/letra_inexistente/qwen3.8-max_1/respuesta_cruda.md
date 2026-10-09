<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="70" y1="60" x2="340" y2="340">
      <stop offset="0" stop-color="#7dd3fc"/>
      <stop offset=".5" stop-color="#c084fc"/>
      <stop offset="1" stop-color="#fb7185"/>
    </linearGradient>
    <radialGradient id="bg" cx=".5" cy=".42" r=".8">
      <stop offset="0" stop-color="#1e293b"/>
      <stop offset="1" stop-color="#020617"/>
    </radialGradient>
    <filter id="f" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="10" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <g fill="none" stroke="url(#g)" stroke-linecap="round" stroke-linejoin="round" filter="url(#f)">
    <path d="M172 72C118 152 116 248 170 330" stroke-width="30"/>
    <path d="M172 72C252 38 322 96 296 162 272 220 188 218 180 162 174 124 216 106 244 136" stroke-width="30"/>
    <path d="M170 330C232 334 288 300 296 232" stroke-width="30"/>
    <path d="M104 218C168 192 238 192 300 218" stroke-width="20"/>
    <path d="M312 56C326 44 346 42 358 52" stroke-width="14"/>
    <circle cx="86" cy="96" r="12" fill="url(#g)" stroke="none"/>
  </g>
</svg>