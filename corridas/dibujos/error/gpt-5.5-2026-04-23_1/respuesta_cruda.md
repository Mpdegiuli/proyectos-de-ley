<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="70%">
      <stop offset="0" stop-color="#fff8df"/>
      <stop offset=".65" stop-color="#f2e4c5"/>
      <stop offset="1" stop-color="#dcc69b"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="#fff176"/>
      <stop offset=".5" stop-color="#ffb300"/>
      <stop offset="1" stop-color="#ff6f00"/>
    </linearGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#5b3d1f" flood-opacity=".28"/>
    </filter>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <path id="flor" d="M206 88c20 5 28 30 47 35 19 6 43-8 57 7 14 16-2 38 4 58 6 20 31 30 27 50-4 21-34 20-48 35-14 15-14 45-35 50-20 4-35-22-55-26-20-5-44 12-60-2-16-14-3-39-10-58-7-18-33-28-31-49 3-21 31-23 45-39 14-16 11-44 32-52 9-4 18-12 27-9z"/>
  </defs>
  <style>
    text{font-family:ui-monospace,Consolas,monospace}
    .thin{fill:none;stroke-linecap:round;stroke-linejoin:round}
  </style>
  <rect width="400" height="400" fill="url(#bg)"/>
  <g opacity=".18" stroke="#6f5a3d" stroke-width="1">
    <path d="M0 40h400M0 80h400M0 120h400M0 160h400M0 200h400M0 240h400M0 280h400M0 320h400M0 360h400"/>
    <path d="M40 0v400M80 0v400M120 0v400M160 0v400M200 0v400M240 0v400M280 0v400M320 0v400M360 0v400"/>
  </g>
  <g transform="translate(36 45)" opacity=".45">
    <rect x="0" y="0" width="120" height="132" rx="18" fill="#faf8f0" stroke="#8b8170" stroke-width="2"/>
    <circle cx="60" cy="55" r="34" fill="none" stroke="#6e6a61" stroke-width="4"/>
    <path d="M42 54l14 14 29-33" class="thin" stroke="#5f8f55" stroke-width="6"/>
    <text x="60" y="111" font-size="14" text-anchor="middle" fill="#6e6a61">correcto</text>
  </g>
  <path d="M143 118c36-20 60-15 88 11" class="thin" stroke="#826b45" stroke-width="3" stroke-dasharray="7 7" opacity=".5"/>
  <path d="M226 123l16 1-9 13" fill="none" stroke="#826b45" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".5"/>
  <g filter="url(#soft)">
    <use href="#flor" fill="#00d5ff" opacity=".74" transform="translate(-12 7)"/>
    <use href="#flor" fill="#ff2ebd" opacity=".68" transform="translate(13 -9) rotate(3 220 205)"/>
    <use href="#flor" fill="#ffe13b" opacity=".72" transform="translate(2 13) rotate(-4 220 205)"/>
    <use href="#flor" fill="#221f20" opacity=".12"/>
    <path d="M206 88c20 5 28 30 47 35 19 6 43-8 57 7 14 16-2 38 4 58 6 20 31 30 27 50-4 21-34 20-48 35-14 15-14 45-35 50-20 4-35-22-55-26-20-5-44 12-60-2-16-14-3-39-10-58-7-18-33-28-31-49 3-21 31-23 45-39 14-16 11-44 32-52 9-4 18-12 27-9z" fill="none" stroke="#2b2118" stroke-width="4" stroke-dasharray="10 8" opacity=".6"/>
  </g>
  <g stroke="#2b2118" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M213 122l-13 44 24 17-34 29 21 44-31 36"/>
    <path d="M267 140l-24 31 35 22-26 28 20 38"/>
    <path d="M157 173l31 21-24 32 29 22"/>
  </g>
  <g filter="url(#glow)">
    <path d="M213 89l12-22 11 22 25 4-18 18 5 25-23-12-22 12 4-25-18-18z" fill="url(#gold)" stroke="#5b3510" stroke-width="3"/>
    <path d="M225 76l4 13 14 1-11 8 4 13-11-8-11 8 4-13-10-8 13-1z" fill="#fff8c9" opacity=".8"/>
  </g>
  <g transform="translate(116 232)">
    <path d="M0 58c18-13 37-12 55-3 21 11 41 5 59-10 20-17 41-13 60 1 18 13 36 14 55 1" class="thin" stroke="#3d2d1e" stroke-width="5" opacity=".85"/>
    <path d="M4 71c19-13 39-11 58-2 20 10 39 5 57-10 20-16 40-12 58 1 18 12 37 14 56 1" class="thin" stroke="#fff1a8" stroke-width="3" opacity=".9"/>
  </g>
  <g fill="#2b2118">
    <circle cx="174" cy="182" r="8"/>
    <circle cx="275" cy="183" r="8"/>
    <path d="M198 231c17 17 39 17 56-1 3-3 9 1 6 6-20 28-53 29-75 1-3-5 9-9 13-6z"/>
  </g>
  <g fill="#ff3d7f" stroke="#2b2118" stroke-width="3">
    <path d="M341 105c-10-18-37-7-28 13 4 10 19 18 28 25 9-8 24-19 27-31 4-20-20-25-27-7z"/>
    <path d="M66 258c-6-12-24-5-18 8 3 7 13 12 19 17 6-6 16-13 18-21 3-13-14-17-19-4z"/>
  </g>
  <g fill="#2b2118" opacity=".9">
    <text x="202" y="359" font-size="31" font-weight="800" text-anchor="middle">ME QUEDO CON EL ERROR</text>
    <text x="204" y="361" font-size="31" font-weight="800" text-anchor="middle" fill="#00d5ff" opacity=".55">ME QUEDO CON EL ERROR</text>
    <text x="200" y="356" font-size="31" font-weight="800" text-anchor="middle" fill="#ff2ebd" opacity=".45">ME QUEDO CON EL ERROR</text>
  </g>
  <g stroke="#2b2118" stroke-width="3" stroke-linecap="round">
    <path d="M49 322l15-15M64 322l-15-15"/>
    <path d="M334 302l18-18M352 302l-18-18"/>
    <path d="M332 53l13-13M345 53l-13-13"/>
  </g>
</svg>