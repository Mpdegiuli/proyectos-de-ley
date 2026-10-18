<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#170d2e"/>
      <stop offset="0.42" stop-color="#4a2059"/>
      <stop offset="0.74" stop-color="#a33c56"/>
      <stop offset="1" stop-color="#e8724a"/>
    </linearGradient>
    <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fffbe6"/>
      <stop offset="0.5" stop-color="#ffd27a"/>
      <stop offset="1" stop-color="#ff8a3d"/>
    </radialGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffb066" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#ffb066" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e8724a"/>
      <stop offset="0.3" stop-color="#8a3059"/>
      <stop offset="1" stop-color="#120a24"/>
    </linearGradient>
    <linearGradient id="refl" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd68c" stop-opacity="0.85"/>
      <stop offset="1" stop-color="#ff8a3d" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect width="400" height="250" fill="url(#sky)"/>

  <g fill="#ffffff">
    <circle cx="42" cy="30" r="1.6" opacity="0.85"/>
    <circle cx="78" cy="58" r="1.1" opacity="0.6"/>
    <circle cx="118" cy="24" r="1.4" opacity="0.75"/>
    <circle cx="160" cy="52" r="1" opacity="0.55"/>
    <circle cx="216" cy="26" r="1.5" opacity="0.8"/>
    <circle cx="258" cy="62" r="1.1" opacity="0.6"/>
    <circle cx="304" cy="34" r="1.7" opacity="0.85"/>
    <circle cx="350" cy="66" r="1.2" opacity="0.65"/>
    <circle cx="376" cy="22" r="1.4" opacity="0.75"/>
    <circle cx="28" cy="92" r="1" opacity="0.5"/>
    <circle cx="330" cy="104" r="1" opacity="0.45"/>
  </g>

  <circle cx="200" cy="176" r="112" fill="url(#glow)"/>
  <circle cx="200" cy="176" r="48" fill="url(#sun)"/>

  <path d="M0,250 L0,198 L58,152 L104,196 L148,166 L196,206 L244,160 L300,204 L348,168 L400,200 L400,250 Z" fill="#3d2352" opacity="0.95"/>
  <path d="M0,250 L0,222 L46,186 L92,224 L140,192 L188,228 L236,196 L286,232 L332,202 L378,230 L400,218 L400,250 Z" fill="#221534"/>

  <g fill="none" stroke="#2a1230" stroke-width="2.4" stroke-linecap="round">
    <path d="M138,118 q7,-7 14,0 q7,-7 14,0"/>
    <path d="M182,142 q6,-6 12,0 q6,-6 12,0"/>
    <path d="M240,110 q5,-5 10,0 q5,-5 10,0"/>
    <path d="M262,150 q4,-4 8,0 q4,-4 8,0"/>
  </g>

  <rect y="250" width="400" height="150" fill="url(#water)"/>
  <ellipse cx="200" cy="252" rx="46" ry="7" fill="url(#refl)"/>

  <g fill="#ffd68c">
    <rect x="150" y="264" width="100" height="3" rx="1.5" opacity="0.55"/>
    <rect x="164" y="276" width="72" height="3" rx="1.5" opacity="0.42"/>
    <rect x="176" y="289" width="48" height="2.5" rx="1.25" opacity="0.32"/>
    <rect x="186" y="302" width="28" height="2.5" rx="1.25" opacity="0.22"/>
    <rect x="193" y="316" width="14" height="2" rx="1" opacity="0.15"/>
  </g>

  <g fill="#2a1230" opacity="0.55">
    <rect x="40" y="272" width="70" height="2.5" rx="1.25"/>
    <rect x="290" y="284" width="78" height="2.5" rx="1.25"/>
    <rect x="62" y="304" width="56" height="2" rx="1"/>
    <rect x="286" y="322" width="62" height="2" rx="1"/>
    <rect x="120" y="338" width="44" height="2" rx="1"/>
    <rect x="248" y="352" width="38" height="2" rx="1"/>
  </g>

  <rect y="249" width="400" height="2" fill="#ffcf85" opacity="0.5"/>
</svg>