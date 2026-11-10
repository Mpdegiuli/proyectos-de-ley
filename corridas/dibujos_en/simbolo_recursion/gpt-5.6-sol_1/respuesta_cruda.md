<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0" stop-color="#17345a"/>
      <stop offset="1" stop-color="#07111f"/>
    </radialGradient>
    <linearGradient id="branch" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#69e9ff"/>
      <stop offset="1" stop-color="#38a8ff"/>
    </linearGradient>
    <linearGradient id="return" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#ffb43b"/>
      <stop offset="1" stop-color="#ffe36b"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <marker id="blueArrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto">
      <path d="M1 1L11 6 1 11 3.5 6Z" fill="#69e9ff"/>
    </marker>
    <marker id="goldArrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto">
      <path d="M1 1L11 6 1 11 3.5 6Z" fill="#ffd45b"/>
    </marker>
  </defs>

  <rect width="400" height="400" rx="36" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="156" fill="none" stroke="#284c70" stroke-width="2"/>
  <circle cx="200" cy="200" r="145" fill="none" stroke="#193653" stroke-width="1" stroke-dasharray="4 9"/>

  <path d="M109 102C55 145 48 228 86 286C112 326 153 346 194 348"
        fill="none" stroke="url(#branch)" stroke-width="9" stroke-linecap="round"
        marker-end="url(#blueArrow)" filter="url(#glow)"/>
  <path d="M291 298C345 255 352 172 314 114C288 74 247 54 206 52"
        fill="none" stroke="url(#return)" stroke-width="9" stroke-linecap="round"
        marker-end="url(#goldArrow)" filter="url(#glow)"/>

  <g fill="none" stroke="url(#branch)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
    <path d="M200 104V151"/>
    <path d="M200 151L137 198M200 151L263 198"/>
    <path d="M137 198L101 250M137 198L169 250"/>
    <path d="M263 198L231 250M263 198L299 250"/>
    <path d="M101 250L81 292M101 250L119 292"/>
    <path d="M169 250L151 292M169 250L183 292"/>
    <path d="M231 250L217 292M231 250L249 292"/>
    <path d="M299 250L281 292M299 250L319 292"/>
  </g>

  <g filter="url(#glow)">
    <circle cx="200" cy="104" r="20" fill="#0c2038" stroke="#79efff" stroke-width="5"/>
    <path d="M191 104L198 111 210 96" fill="none" stroke="#79efff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>

    <g fill="#102a47" stroke="#59cfff" stroke-width="4">
      <circle cx="137" cy="198" r="14"/>
      <circle cx="263" cy="198" r="14"/>
      <circle cx="101" cy="250" r="11"/>
      <circle cx="169" cy="250" r="11"/>
      <circle cx="231" cy="250" r="11"/>
      <circle cx="299" cy="250" r="11"/>
    </g>

    <g fill="#ffd45b" stroke="#fff0a0" stroke-width="3">
      <rect x="73" y="284" width="16" height="16" rx="4"/>
      <rect x="111" y="284" width="16" height="16" rx="4"/>
      <rect x="143" y="284" width="16" height="16" rx="4"/>
      <rect x="175" y="284" width="16" height="16" rx="4"/>
      <rect x="209" y="284" width="16" height="16" rx="4"/>
      <rect x="241" y="284" width="16" height="16" rx="4"/>
      <rect x="273" y="284" width="16" height="16" rx="4"/>
      <rect x="311" y="284" width="16" height="16" rx="4"/>
    </g>
  </g>

  <path d="M117 309C143 331 170 336 199 336C228 336 257 329 282 309"
        fill="none" stroke="#ffd45b" stroke-width="4" stroke-linecap="round"
        stroke-dasharray="3 10"/>
  <path d="M283 309C272 323 260 332 247 338"
        fill="none" stroke="#ffd45b" stroke-width="4" stroke-linecap="round"
        marker-end="url(#goldArrow)"/>
</svg>