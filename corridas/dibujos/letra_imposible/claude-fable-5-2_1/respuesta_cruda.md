<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="cyl" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#d9cfb8"/>
      <stop offset="0.25" stop-color="#fffaf0"/>
      <stop offset="0.6" stop-color="#e2d8c2"/>
      <stop offset="1" stop-color="#a2967f"/>
    </linearGradient>
    <linearGradient id="gO" gradientUnits="userSpaceOnUse" x1="140" y1="0" x2="265" y2="0">
      <stop offset="0" stop-color="#e3a93f" stop-opacity="1"/>
      <stop offset="1" stop-color="#e3a93f" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="gB" gradientUnits="userSpaceOnUse" x1="140" y1="0" x2="265" y2="0">
      <stop offset="0" stop-color="#27375f" stop-opacity="1"/>
      <stop offset="1" stop-color="#27375f" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="gP" gradientUnits="userSpaceOnUse" x1="165" y1="0" x2="265" y2="0">
      <stop offset="0" stop-color="#f2ecdf" stop-opacity="1"/>
      <stop offset="1" stop-color="#f2ecdf" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="#f2ecdf"/>

  <!-- tres brazos cilíndricos -->
  <rect x="106" y="85" width="224" height="46" fill="url(#cyl)"/>
  <rect x="156" y="177" width="144" height="46" fill="url(#cyl)"/>
  <rect x="110" y="269" width="220" height="46" fill="url(#cyl)"/>

  <!-- el brazo del medio se disuelve en vacío -->
  <rect x="156" y="177" width="144" height="46" fill="url(#gP)"/>

  <!-- dos brazos prismáticos -->
  <polygon points="60,131 106,85 330,85 330,131" fill="url(#gO)"/>
  <rect x="110" y="131" width="220" height="46" fill="url(#gB)"/>
  <polygon points="110,269 156,223 330,223 330,269" fill="url(#gO)"/>
  <rect x="110" y="269" width="220" height="46" fill="url(#gB)"/>

  <!-- lomo -->
  <rect x="60" y="131" width="50" height="184" fill="#27375f"/>
  <polygon points="110,177 156,177 156,223 110,269" fill="#c65a34"/>

  <!-- contornos -->
  <path d="M106 85H330 M60 131H330 M110 177H300 M156 223H300 M110 269H330 M60 315H330 M106 85L60 131V315 M110 177V269L156 223V177"
        fill="none" stroke="#1b1a22" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- tapas -->
  <g fill="#c65a34" stroke="#1b1a22" stroke-width="3">
    <ellipse cx="330" cy="108" rx="11" ry="23"/>
    <ellipse cx="300" cy="200" rx="11" ry="23"/>
    <ellipse cx="330" cy="292" rx="11" ry="23"/>
  </g>
</svg>