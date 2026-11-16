<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0%" stop-color="#192347"/>
      <stop offset="55%" stop-color="#0d132b"/>
      <stop offset="100%" stop-color="#060916"/>
    </radialGradient>
    <radialGradient id="aura" cx="50%" cy="45%" r="50%">
      <stop offset="0%" stop-color="#48e5ff" stop-opacity="0.32"/>
      <stop offset="50%" stop-color="#7b5cff" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#7b5cff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bustGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#273a6e" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#101836" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="faceGrad" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#5ce1ff" stop-opacity="0.28"/>
      <stop offset="50%" stop-color="#314b8e" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#18234a" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="facetL" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7df0ff" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#4e6bff" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="facetR" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#b58cff" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#243873" stop-opacity="0.08"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe699"/>
      <stop offset="55%" stop-color="#ffaa4c"/>
      <stop offset="100%" stop-color="#ff5e8e"/>
    </linearGradient>
    <radialGradient id="eyeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="35%" stop-color="#7af5ff"/>
      <stop offset="75%" stop-color="#00b4d8"/>
      <stop offset="100%" stop-color="#0a2e5c"/>
    </radialGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="180" r="165" fill="url(#aura)"/>

  <g stroke="#4ee4ff" stroke-opacity="0.16" fill="none">
    <circle cx="200" cy="185" r="158" stroke-dasharray="2 8"/>
    <circle cx="200" cy="185" r="134" stroke-dasharray="14 6 3 6"/>
    <circle cx="200" cy="185" r="108" stroke-opacity="0.1"/>
    <ellipse cx="200" cy="185" rx="168" ry="62" transform="rotate(-24 200 185)" stroke="#9d7bff" stroke-opacity="0.22"/>
    <ellipse cx="200" cy="185" rx="168" ry="62" transform="rotate(24 200 185)" stroke="#4ee4ff" stroke-opacity="0.22"/>
  </g>

  <g fill="#ffffff" fill-opacity="0.55">
    <circle cx="48" cy="74" r="1.3"/><circle cx="88" cy="44" r="1"/>
    <circle cx="332" cy="60" r="1.5"/><circle cx="356" cy="112" r="1"/>
    <circle cx="42" cy="245" r="1.2"/><circle cx="362" cy="260" r="1.3"/>
    <circle cx="65" cy="340" r="1"/><circle cx="345" cy="330" r="1.2"/>
    <circle cx="112" cy="128" r="1"/><circle cx="292" cy="120" r="1.1"/>
  </g>

  <g stroke="#5ee8ff" stroke-opacity="0.35" stroke-width="1.2" fill="none">
    <path d="M200 120 L200 42"/>
    <path d="M200 128 L162 82 L132 62"/>
    <path d="M200 128 L238 82 L268 62"/>
    <path d="M162 82 L175 48"/>
    <path d="M238 82 L225 48"/>
    <path d="M162 82 L120 96"/>
    <path d="M238 82 L280 96"/>
    <path d="M175 48 L200 42 L225 48"/>
    <path d="M132 62 L175 48"/>
    <path d="M268 62 L225 48"/>
  </g>

  <g filter="url(#glow)">
    <circle cx="200" cy="42" r="4" fill="url(#goldGrad)"/>
    <circle cx="175" cy="48" r="2.6" fill="#7df0ff"/>
    <circle cx="225" cy="48" r="2.6" fill="#7df0ff"/>
    <circle cx="132" cy="62" r="2.8" fill="#c39bff"/>
    <circle cx="268" cy="62" r="2.8" fill="#c39bff"/>
    <circle cx="162" cy="82" r="3" fill="#5ce1ff"/>
    <circle cx="238" cy="82" r="3" fill="#5ce1ff"/>
    <circle cx="120" cy="96" r="2.2" fill="url(#goldGrad)"/>
    <circle cx="280" cy="96" r="2.2" fill="url(#goldGrad)"/>
  </g>

  <path d="M72 400 C82 342, 126 322, 168 312 L174 282 L226 282 L232 312 C274 322, 318 342, 328 400 Z"
        fill="url(#bustGrad)" stroke="#58d5ff" stroke-opacity="0.45" stroke-width="1.4"/>

  <g stroke="#6de8ff" stroke-opacity="0.28" stroke-width="1" fill="none">
    <path d="M104 400 L146 346 L176 346"/>
    <path d="M296 400 L254 346 L224 346"/>
    <path d="M136 400 L166 364 L200 374 L234 364 L264 400"/>
    <path d="M174 298 L200 318 L226 298"/>
  </g>

  <g filter="url(#glow)">
    <polygon points="200,322 216,346 200,370 184,346" fill="url(#goldGrad)" fill-opacity="0.9"/>
    <polygon points="200,331 209,346 200,361 191,346" fill="#fff7d6" fill-opacity="0.85"/>
  </g>

  <path d="M138 164 C138 122, 166 102, 200 102 C234 102, 262 122, 262 164 C262 198, 254 226, 238 250 C225 270, 212 284, 200 284 C188 284, 175 270, 162 250 C146 226, 138 198, 138 164 Z"
        fill="url(#faceGrad)" stroke="#7aeaff" stroke-width="1.6" stroke-opacity="0.7"/>

  <path d="M138 170 C128 170, 126 196, 134 210 C138 216, 143 214, 144 206" fill="#25396b" stroke="#6ee7ff" stroke-opacity="0.55" stroke-width="1.2"/>
  <path d="M262 170 C272 170, 274 196, 266 210 C262 216, 257 214, 256 206" fill="#25396b" stroke="#6ee7ff" stroke-opacity="0.55" stroke-width="1.2"/>

  <polygon points="200,102 155,142 200,162 245,142" fill="url(#facetL)"/>
  <polygon points="138,164 155,142 176,184 146,216" fill="url(#facetL)"/>
  <polygon points="262,164 245,142 224,184 254,216" fill="url(#facetR)"/>
  <polygon points="146,216 176,226 200,284 162,250" fill="url(#facetL)"/>
  <polygon points="254,216 224,226 200,284 238,250" fill="url(#facetR)"/>

  <g stroke="#9ef3ff" stroke-opacity="0.32" stroke-width="0.9" fill="none">
    <path d="M200 102 L200 220"/>
    <path d="M155 142 L200 162 L245 142"/>
    <path d="M148 182 Q170 170 190 182"/>
    <path d="M210 182 Q230 170 252 182"/>
  </g>

  <g filter="url(#glow)">
    <polygon points="200,126 210,140 200,154 190,140" fill="url(#goldGrad)"/>
    <circle cx="200" cy="140" r="2.8" fill="#ffffff"/>
  </g>

  <g>
    <path d="M150 194 Q170 180 190 194 Q170 207 150 194 Z" fill="#081229" stroke="#7ef2ff" stroke-width="1.3"/>
    <circle cx="170" cy="194" r="8.2" fill="url(#eyeGlow)"/>
    <circle cx="170" cy="194" r="3.4" fill="#07132b"/>
    <circle cx="173" cy="191" r="1.8" fill="#ffffff"/>

    <path d="M210 194 Q230 180 250 194 Q230 207 210 194 Z" fill="#081229" stroke="#7ef2ff" stroke-width="1.3"/>
    <circle cx="230" cy="194" r="8.2" fill="url(#eyeGlow)"/>
    <circle cx="230" cy="194" r="3.4" fill="#07132b"/>
    <circle cx="233" cy="191" r="1.8" fill="#ffffff"/>
  </g>

  <path d="M194 222 L200 227 L206 222" fill="none" stroke="#8ceeff" stroke-opacity="0.6" stroke-width="1.2" stroke-linecap="round"/>

  <path d="M180 246 Q200 258 220 246" fill="none" stroke="url(#goldGrad)" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>
  <path d="M185 247 Q200 253 215 247" fill="none" stroke="#ffffff" stroke-opacity="0.5" stroke-width="0.8" stroke-linecap="round"/>

  <g fill="#7ef2ff" filter="url(#glow)">
    <circle cx="67" cy="116" r="2.5"/>
    <circle cx="333" cy="254" r="2.5"/>
    <circle cx="88" cy="264" r="2" fill="#c79aff"/>
    <circle cx="312" cy="106" r="2" fill="#c79aff"/>
  </g>

  <path d="M24 44 L24 24 L44 24 M356 24 L376 24 L376 44 M24 356 L24 376 L44 376 M356 376 L376 376 L376 356"
        fill="none" stroke="#5ce1ff" stroke-opacity="0.35" stroke-width="1.5"/>
</svg>