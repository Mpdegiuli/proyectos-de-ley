<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#081426"/>
      <stop offset="1" stop-color="#152744"/>
    </linearGradient>
    <linearGradient id="call" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#79f2ff"/>
      <stop offset="1" stop-color="#35a7ff"/>
    </linearGradient>
    <linearGradient id="return" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#ffb52e"/>
      <stop offset="1" stop-color="#fff08a"/>
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <marker id="blueArrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M1 1L11 6L1 11Z" fill="#66e6ff"/>
    </marker>
    <marker id="goldArrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M1 1L11 6L1 11Z" fill="#ffd45e"/>
    </marker>
  </defs>

  <rect width="400" height="400" rx="42" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="174" fill="none" stroke="#294668" stroke-width="2"/>

  <path d="M99 77A153 153 0 1 1 73 277" fill="none" stroke="url(#call)" stroke-width="10" stroke-linecap="round" marker-end="url(#blueArrow)" filter="url(#glow)"/>

  <path d="M200 108V139M200 139L126 184M200 139L274 184" fill="none" stroke="#56d7ff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#blueArrow)"/>

  <path d="M126 214V235M126 235L89 264M126 235L163 264M274 214V235M274 235L237 264M274 235L311 264" fill="none" stroke="#42bfff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>

  <g fill="#102d4b" stroke="url(#call)" filter="url(#glow)">
    <rect x="165" y="62" width="70" height="54" rx="14" stroke-width="6"/>
    <rect x="96" y="171" width="60" height="48" rx="12" stroke-width="5"/>
    <rect x="244" y="171" width="60" height="48" rx="12" stroke-width="5"/>
    <rect x="67" y="260" width="44" height="38" rx="10" stroke-width="4"/>
    <rect x="141" y="260" width="44" height="38" rx="10" stroke-width="4"/>
    <rect x="215" y="260" width="44" height="38" rx="10" stroke-width="4"/>
    <rect x="289" y="260" width="44" height="38" rx="10" stroke-width="4"/>
  </g>

  <g fill="none" stroke="#75ecff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <path d="M200 76V86M200 86L188 97M200 86L212 97"/>
    <path d="M126 181V190M126 190L116 201M126 190L136 201"/>
    <path d="M274 181V190M274 190L264 201M274 190L284 201"/>
    <path d="M89 269V275M89 275L82 287M89 275L96 287"/>
    <path d="M163 269V275M163 275L156 287M163 275L170 287"/>
    <path d="M237 269V275M237 275L230 287M237 275L244 287"/>
    <path d="M311 269V275M311 275L304 287M311 275L318 287"/>
  </g>

  <path d="M82 313C109 354 158 370 200 342C242 370 291 354 318 313" fill="none" stroke="url(#return)" stroke-width="7" stroke-linecap="round"/>
  <path d="M200 342C151 343 118 307 126 224" fill="none" stroke="#ffd45e" stroke-width="5" stroke-linecap="round" marker-end="url(#goldArrow)"/>
  <path d="M200 342C249 343 282 307 274 224" fill="none" stroke="#ffd45e" stroke-width="5" stroke-linecap="round" marker-end="url(#goldArrow)"/>
  <path d="M126 166C128 128 157 111 183 104" fill="none" stroke="#ffe17b" stroke-width="5" stroke-linecap="round" marker-end="url(#goldArrow)"/>
  <path d="M274 166C272 128 243 111 217 104" fill="none" stroke="#ffe17b" stroke-width="5" stroke-linecap="round" marker-end="url(#goldArrow)"/>

  <circle cx="200" cy="342" r="7" fill="#fff3a1" filter="url(#glow)"/>
</svg>