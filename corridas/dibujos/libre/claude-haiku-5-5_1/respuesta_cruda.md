```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e3a6e"/>
      <stop offset="55%" stop-color="#e98a5c"/>
      <stop offset="100%" stop-color="#f6c77a"/>
    </linearGradient>
    <radialGradient id="sol" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#fff6c8"/>
      <stop offset="60%" stop-color="#ffd166"/>
      <stop offset="100%" stop-color="#ffd16600"/>
    </radialGradient>
    <linearGradient id="agua" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3d6b8c"/>
      <stop offset="100%" stop-color="#1b3349"/>
    </linearGradient>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="url(#cielo)"/>

  <circle cx="290" cy="150" r="90" fill="url(#sol)"/>
  <circle cx="290" cy="150" r="42" fill="#fff1b8"/>

  <g fill="#ffffff" opacity="0.85">
    <ellipse cx="90" cy="70" rx="38" ry="9"/>
    <ellipse cx="115" cy="62" rx="24" ry="9"/>
    <ellipse cx="200" cy="105" rx="30" ry="7"/>
    <ellipse cx="220" cy="98" rx="18" ry="7"/>
  </g>

  <path d="M0 220 L70 140 L120 190 L180 120 L240 200 L300 150 L360 210 L400 180 L400 260 L0 260 Z" fill="#6a4c7a"/>
  <path d="M180 120 L160 150 L175 145 L190 160 L205 140 L195 138 Z" fill="#f4eef7" opacity="0.9"/>
  <path d="M70 140 L50 168 L62 162 L75 176 L90 160 L80 158 Z" fill="#f4eef7" opacity="0.8"/>

  <path d="M0 240 L60 190 L110 230 L150 205 L210 250 L260 215 L320 245 L370 205 L400 225 L400 290 L0 290 Z" fill="#4a3558"/>

  <rect x="0" y="280" width="400" height="120" fill="#2e4a3a"/>
  <path d="M0 280 Q100 265 200 280 T400 280 L400 290 L0 290 Z" fill="#3b5d47"/>

  <ellipse cx="200" cy="335" rx="150" ry="30" fill="url(#agua)"/>
  <ellipse cx="200" cy="335" rx="150" ry="30" fill="none" stroke="#ffd166" stroke-opacity="0.35" stroke-width="2"/>
  <g stroke="#ffd166" stroke-width="2" stroke-linecap="round" opacity="0.6">
    <line x1="260" y1="330" x2="310" y2="330"/>
    <line x1="120" y1="342" x2="165" y2="342"/>
    <line x1="210" y1="348" x2="240" y2="348"/>
  </g>
  <path d="M288 152 L292 178 L290 260" stroke="#fff1b8" stroke-opacity="0.25" stroke-width="3" fill="none"/>
  <g fill="#ffd166" opacity="0.5">
    <rect x="278" y="318" width="20" height="4" rx="2"/>
    <rect x="262" y="326" width="36" height="3" rx="1.5"/>
  </g>

  <g>
    <rect x="28" y="300" width="6" height="26" fill="#3a2a1e"/>
    <path d="M31 262 L12 306 L50 306 Z" fill="#1f4d36"/>
    <path d="M31 276 L16 310 L46 310 Z" fill="#245a40"/>
  </g>
  <g>
    <rect x="58" y="308" width="5" height="22" fill="#3a2a1e"/>
    <path d="M60 280 L44 314 L76 314 Z" fill="#1f4d36"/>
  </g>
  <g>
    <rect x="352" y="296" width="6" height="28" fill="#3a2a1e"/>
    <path d="M355 258 L334 302 L376 302 Z" fill="#1f4d36"/>
    <path d="M355 272 L338 306 L372 306 Z" fill="#245a40"/>
  </g>

  <g>
    <rect x="96" y="372" width="5" height="18" fill="#3a2a1e"/>
    <path d="M98 348 L86 376 L110 376 Z" fill="#1f4d36"/>
  </g>

  <g fill="#1b1a2e">
    <path d="M0 360 Q200 350 400 360 L400 400 L0 400 Z" opacity="0"/>
  </g>

  <g fill="#1f2a3d" opacity="0.9">
    <path d="M180 220 L200 214 L202 220 L184 224 Z"/>
  </g>
  <path d="M182 226 Q183 221 186 219" stroke="#1f2a3d" stroke-width="0" fill="none"/>

  <path d="M0 395 Q200 388 400 395 L400 400 L0 400 Z" fill="#1b2a22"/>
</svg>
```