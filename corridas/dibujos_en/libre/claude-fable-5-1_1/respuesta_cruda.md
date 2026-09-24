<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0b1026"/>
      <stop offset="0.55" stop-color="#2a2f5e"/>
      <stop offset="1" stop-color="#7a4b6e"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3a3560"/>
      <stop offset="1" stop-color="#0b0f24"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff7d6" stop-opacity="0.9"/>
      <stop offset="0.5" stop-color="#ffe9a8" stop-opacity="0.25"/>
      <stop offset="1" stop-color="#ffe9a8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="moon" cx="0.4" cy="0.4" r="0.7">
      <stop offset="0" stop-color="#fffbe8"/>
      <stop offset="1" stop-color="#e8d9a8"/>
    </radialGradient>
    <linearGradient id="m1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4b4a80"/>
      <stop offset="1" stop-color="#2c2b55"/>
    </linearGradient>
    <linearGradient id="m2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2f2e58"/>
      <stop offset="1" stop-color="#1a1a3a"/>
    </linearGradient>
    <linearGradient id="m3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1c1c3a"/>
      <stop offset="1" stop-color="#0e0e22"/>
    </linearGradient>
    <clipPath id="lake"><rect x="0" y="260" width="400" height="140"/></clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff">
    <circle cx="30" cy="40" r="1.2"/><circle cx="70" cy="90" r="0.8"/><circle cx="110" cy="30" r="1"/>
    <circle cx="150" cy="70" r="0.7"/><circle cx="190" cy="25" r="1.1"/><circle cx="230" cy="60" r="0.8"/>
    <circle cx="330" cy="30" r="1"/><circle cx="360" cy="80" r="0.9"/><circle cx="385" cy="45" r="1.2"/>
    <circle cx="50" cy="140" r="0.8"/><circle cx="20" cy="100" r="0.6"/><circle cx="130" cy="120" r="0.7"/>
    <circle cx="170" cy="150" r="0.6"/><circle cx="90" cy="60" r="0.6"/><circle cx="250" cy="20" r="0.7"/>
    <circle cx="340" cy="130" r="0.7"/><circle cx="375" cy="160" r="0.6"/><circle cx="300" cy="180" r="0.5"/>
    <circle cx="210" cy="110" r="0.5"/><circle cx="60" cy="190" r="0.6"/><circle cx="15" cy="60" r="0.8"/>
    <circle cx="160" cy="15" r="0.6"/><circle cx="320" cy="95" r="0.6"/><circle cx="395" cy="120" r="0.7"/>
  </g>

  <circle cx="280" cy="105" r="90" fill="url(#glow)"/>
  <circle cx="280" cy="105" r="38" fill="url(#moon)"/>
  <g fill="#cbbd8a" opacity="0.5">
    <circle cx="268" cy="95" r="6"/><circle cx="292" cy="118" r="4"/><circle cx="286" cy="90" r="2.5"/><circle cx="272" cy="120" r="3"/>
  </g>

  <path d="M0 230 L40 175 L75 200 L120 140 L160 195 L200 160 L240 205 L280 170 L320 210 L360 165 L400 215 L400 270 L0 270Z" fill="url(#m1)"/>
  <path d="M0 260 L30 225 L70 245 L110 205 L150 240 L190 215 L230 250 L270 220 L310 250 L350 225 L400 255 L400 270 L0 270Z" fill="url(#m2)"/>

  <rect x="0" y="270" width="400" height="130" fill="url(#water)"/>

  <g clip-path="url(#lake)" opacity="0.45" transform="translate(0,540) scale(1,-1)">
    <path d="M0 230 L40 175 L75 200 L120 140 L160 195 L200 160 L240 205 L280 170 L320 210 L360 165 L400 215 L400 270 L0 270Z" fill="url(#m1)"/>
    <path d="M0 260 L30 225 L70 245 L110 205 L150 240 L190 215 L230 250 L270 220 L310 250 L350 225 L400 255 L400 270 L0 270Z" fill="url(#m2)"/>
  </g>

  <g fill="#f5e9b8" opacity="0.6">
    <ellipse cx="280" cy="285" rx="22" ry="1.5"/>
    <ellipse cx="276" cy="294" rx="30" ry="1.6"/>
    <ellipse cx="284" cy="305" rx="18" ry="1.3"/>
    <ellipse cx="278" cy="318" rx="34" ry="1.6"/>
    <ellipse cx="282" cy="333" rx="24" ry="1.4"/>
    <ellipse cx="275" cy="350" rx="40" ry="1.5"/>
    <ellipse cx="285" cy="368" rx="26" ry="1.3"/>
    <ellipse cx="279" cy="385" rx="45" ry="1.4"/>
  </g>

  <g fill="url(#m3)">
    <path d="M0 400 L0 300 L20 290 L40 305 L60 285 L90 300 L120 280 L150 300 L170 292 L200 310 L240 296 L270 312 L300 298 L340 315 L370 300 L400 318 L400 400Z" opacity="0.9"/>
  </g>

  <g fill="#090a1a">
    <path d="M30 330 L38 300 L46 330 L42 330 L48 350 L44 350 L52 372 L24 372 L32 350 L28 350 L34 330Z"/>
    <path d="M60 325 L70 288 L80 325 L75 325 L83 348 L78 348 L88 372 L52 372 L62 348 L57 348 L65 325Z"/>
    <path d="M98 340 L104 318 L110 340 L107 340 L112 355 L109 355 L115 372 L93 372 L99 355 L96 355 L101 340Z"/>
    <path d="M340 335 L348 305 L356 335 L352 335 L358 354 L354 354 L362 372 L334 372 L342 354 L338 354 L344 335Z"/>
    <path d="M370 322 L380 285 L390 322 L385 322 L393 346 L388 346 L398 372 L362 372 L372 346 L367 346 L375 322Z"/>
    <path d="M310 345 L315 328 L320 345 L318 345 L322 358 L320 358 L325 372 L305 372 L310 358 L308 358 L312 345Z"/>
    <rect x="0" y="370" width="400" height="30"/>
  </g>

  <g>
    <path d="M195 352 Q210 362 225 352 L222 344 L198 344Z" fill="#0a0b1c"/>
    <line x1="210" y1="344" x2="210" y2="322" stroke="#0a0b1c" stroke-width="2"/>
    <circle cx="210" cy="320" r="2.5" fill="#ffd97a"/>
    <circle cx="210" cy="320" r="7" fill="#ffd97a" opacity="0.25"/>
    <ellipse cx="210" cy="364" rx="10" ry="1.5" fill="#ffd97a" opacity="0.3"/>
  </g>

  <g fill="#cfe86a">
    <circle cx="130" cy="300" r="1.3" opacity="0.8"/>
    <circle cx="150" cy="320" r="1" opacity="0.6"/>
    <circle cx="90" cy="290" r="1.1" opacity="0.7"/>
    <circle cx="240" cy="330" r="1" opacity="0.6"/>
    <circle cx="300" cy="290" r="1.2" opacity="0.7"/>
  </g>
</svg>