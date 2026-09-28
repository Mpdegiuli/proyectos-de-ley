<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1b1f4a"/>
      <stop offset="0.6" stop-color="#4a3c7a"/>
      <stop offset="1" stop-color="#c76b7a"/>
    </linearGradient>
    <linearGradient id="wall" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f2d7a3"/>
      <stop offset="1" stop-color="#c99a5b"/>
    </linearGradient>
    <linearGradient id="roof" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#7ec8c9"/>
      <stop offset="1" stop-color="#2f7f88"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffe89a"/>
      <stop offset="1" stop-color="#ffb347" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="moon" cx="0.4" cy="0.4" r="0.6">
      <stop offset="0" stop-color="#fffbe6"/>
      <stop offset="1" stop-color="#d8d2a6"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff" opacity="0.8">
    <circle cx="40" cy="50" r="1.5"/><circle cx="120" cy="30" r="1"/><circle cx="330" cy="70" r="1.8"/>
    <circle cx="370" cy="25" r="1.2"/><circle cx="250" cy="45" r="1"/><circle cx="80" cy="120" r="1.3"/>
    <circle cx="300" cy="140" r="1"/><circle cx="20" cy="200" r="1.4"/><circle cx="385" cy="180" r="1"/>
  </g>

  <circle cx="320" cy="70" r="28" fill="url(#moon)"/>
  <circle cx="310" cy="62" r="4" fill="#cfc9a0" opacity="0.6"/>
  <circle cx="328" cy="80" r="6" fill="#cfc9a0" opacity="0.5"/>

  <g opacity="0.55" fill="#2a2d5c">
    <ellipse cx="70" cy="330" rx="26" ry="10"/>
    <path d="M60 330 q-4 20 8 40 q-2 -18 8 -30 z"/>
    <ellipse cx="340" cy="300" rx="18" ry="7"/>
    <path d="M334 300 q-2 14 6 26 q-1 -12 6 -20 z"/>
    <circle cx="110" cy="250" r="5"/>
    <circle cx="300" cy="230" r="4"/>
  </g>

  <path d="M120 250 q-30 40 -2 80 q-6 30 8 60" stroke="#5a3a2a" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M200 262 q10 40 -4 70 q6 25 -2 50" stroke="#5a3a2a" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M275 250 q30 30 6 70 q10 25 0 45" stroke="#5a3a2a" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M160 260 q-10 30 4 55" stroke="#5a3a2a" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M240 258 q8 30 -6 50" stroke="#5a3a2a" stroke-width="3" fill="none" stroke-linecap="round"/>

  <path d="M110 240 q90 -20 180 0 q10 30 -30 40 q-60 -10 -120 5 q-40 -10 -30 -45 z" fill="#6b4a33"/>
  <path d="M105 242 q95 -30 190 -4 q-30 20 -95 18 q-70 5 -95 -14 z" fill="#5fa35a"/>
  <path d="M130 235 q70 -18 140 -2" stroke="#8ccf6f" stroke-width="3" fill="none" stroke-linecap="round"/>

  <polygon points="140,236 250,232 262,140 128,150" fill="url(#wall)" stroke="#7a5230" stroke-width="2"/>
  <polygon points="120,152 270,140 200,80" fill="url(#roof)" stroke="#1e5a62" stroke-width="2"/>
  <path d="M132 150 l68 -60 M150 148 l50 -52 M172 145 l28 -46 M220 142 l-20 -46 M240 141 l-40 -50" stroke="#1e5a62" stroke-width="1.2" opacity="0.6"/>

  <polygon points="235,150 262,148 258,90 240,88" fill="#e8c384" stroke="#7a5230" stroke-width="2"/>
  <polygon points="232,92 266,90 249,50" fill="#b04a5a" stroke="#6b2733" stroke-width="2"/>
  <rect x="245" y="105" width="8" height="14" fill="#ffe08a" stroke="#7a5230"/>
  <line x1="249" y1="50" x2="249" y2="30" stroke="#7a5230" stroke-width="2"/>
  <path d="M249 30 l16 6 l-16 6 z" fill="#ffd94a"/>

  <rect x="175" y="86" width="14" height="30" fill="#8a5a44" stroke="#5a3a2a" stroke-width="1.5" transform="rotate(-8 182 100)"/>
  <ellipse cx="180" cy="72" rx="10" ry="6" fill="#dcdcf0" opacity="0.6"/>
  <ellipse cx="176" cy="60" rx="8" ry="5" fill="#dcdcf0" opacity="0.5"/>
  <ellipse cx="170" cy="50" rx="6" ry="4" fill="#dcdcf0" opacity="0.4"/>

  <circle cx="165" cy="205" r="24" fill="url(#glow)"/>
  <circle cx="165" cy="205" r="14" fill="#ffd97a" stroke="#7a5230" stroke-width="2"/>
  <path d="M151 205 h28 M165 191 v28" stroke="#7a5230" stroke-width="2"/>

  <g transform="rotate(12 215 180)">
    <rect x="203" y="165" width="24" height="30" fill="#ffd97a" stroke="#7a5230" stroke-width="2"/>
    <line x1="215" y1="165" x2="215" y2="195" stroke="#7a5230" stroke-width="2"/>
    <line x1="203" y1="180" x2="227" y2="180" stroke="#7a5230" stroke-width="2"/>
  </g>

  <g transform="rotate(-15 155 168)">
    <rect x="146" y="158" width="18" height="20" fill="#ffd97a" stroke="#7a5230" stroke-width="2"/>
    <line x1="155" y1="158" x2="155" y2="178" stroke="#7a5230" stroke-width="1.5"/>
  </g>

  <path d="M200 236 q0 -30 22 -30 q22 0 22 30 z" fill="#8a3b4a" stroke="#5a2430" stroke-width="2"/>
  <circle cx="234" cy="222" r="2.5" fill="#ffd94a"/>
  <path d="M212 236 q10 -20 20 0" stroke="#5a2430" stroke-width="1.2" fill="none"/>

  <g stroke="#7a5230" stroke-width="1" opacity="0.5" fill="none">
    <path d="M140 200 h40 M188 170 h20 M235 200 h12"/>
  </g>

  <path d="M90 300 q4 -10 8 0 M160 320 q4 -10 8 0 M290 300 q4 -10 8 0" stroke="#ffd94a" stroke-width="1.5" fill="none" opacity="0.7"/>
  <circle cx="94" cy="300" r="2" fill="#ffd94a" opacity="0.9"/>
  <circle cx="164" cy="320" r="2" fill="#ffd94a" opacity="0.9"/>
  <circle cx="294" cy="300" r="2" fill="#ffd94a" opacity="0.9"/>
</svg>