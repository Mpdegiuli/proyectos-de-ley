<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="perg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f6ecd2"/>
      <stop offset="1" stop-color="#e6d3a8"/>
    </linearGradient>
    <linearGradient id="oro" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff2a8"/>
      <stop offset="0.45" stop-color="#d9a92e"/>
      <stop offset="1" stop-color="#8a5a12"/>
    </linearGradient>
    <linearGradient id="rojo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#c8283a"/>
      <stop offset="1" stop-color="#7a0f1e"/>
    </linearGradient>
    <radialGradient id="fondo" cx="0.5" cy="0.5" r="0.7">
      <stop offset="0" stop-color="#2a4a8a"/>
      <stop offset="1" stop-color="#132650"/>
    </radialGradient>
    <pattern id="puntos" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="1.6" fill="#d9a92e" opacity="0.55"/>
    </pattern>
    <filter id="sombra" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="4" dy="5" stdDeviation="3" flood-color="#000" flood-opacity="0.45"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#perg)"/>

  <rect x="30" y="30" width="340" height="340" rx="6" fill="url(#oro)"/>
  <rect x="40" y="40" width="320" height="320" rx="4" fill="url(#fondo)"/>
  <rect x="40" y="40" width="320" height="320" fill="url(#puntos)"/>
  <rect x="46" y="46" width="308" height="308" fill="none" stroke="#d9a92e" stroke-width="1.5"/>

  <g fill="none" stroke="#5e9c4a" stroke-width="4" stroke-linecap="round">
    <path d="M60,340 C80,280 60,240 90,200 S80,120 70,70"/>
    <path d="M340,60 C320,120 340,160 310,200 S320,280 330,330"/>
    <path d="M90,200 c-20,-5 -25,-25 -10,-30 c10,-3 15,8 6,12"/>
    <path d="M310,200 c20,5 25,25 10,30 c-10,3 -15,-8 -6,-12"/>
  </g>
  <g fill="#6fb35a" stroke="#2f5e26" stroke-width="1.5">
    <path d="M72,300 q-20,-10 -8,-28 q14,12 8,28z"/>
    <path d="M82,240 q22,-6 24,14 q-18,4 -24,-14z"/>
    <path d="M78,130 q-20,0 -16,-20 q18,4 16,20z"/>
    <path d="M328,100 q20,0 16,20 q-18,-4 -16,-20z"/>
    <path d="M318,160 q-22,6 -24,-14 q18,-4 24,14z"/>
    <path d="M326,270 q20,10 8,28 q-14,-12 -8,-28z"/>
  </g>
  <g fill="#c8283a" stroke="#d9a92e" stroke-width="1.5">
    <circle cx="70" cy="70" r="7"/>
    <circle cx="330" cy="330" r="7"/>
    <circle cx="60" cy="340" r="5"/>
    <circle cx="340" cy="60" r="5"/>
  </g>

  <g filter="url(#sombra)">
    <path d="M100,96 C130,62 168,66 198,88 S256,112 296,78" fill="none" stroke="url(#oro)" stroke-width="20" stroke-linecap="round"/>
    <path d="M100,96 C130,62 168,66 198,88 S256,112 296,78" fill="none" stroke="url(#rojo)" stroke-width="10" stroke-linecap="round"/>

    <path d="M92,128 H170 V140 H156 L248,262 V140 H232 V128 H308 V140 H294 V320 H254 L152,186 V308 H168 V320 H92 V308 H108 V140 H92 Z"
          fill="url(#oro)" stroke="#5a3a08" stroke-width="2" stroke-linejoin="round"/>
    <path d="M116,146 H146 L256,292 V146 H286 V312 H258 L146,164 V312 H116 Z"
          fill="url(#rojo)"/>
  </g>

  <g fill="#fff2a8" opacity="0.9">
    <circle cx="131" cy="230" r="4"/>
    <circle cx="271" cy="230" r="4"/>
    <path d="M200,222 l5,9 l-5,9 l-5,-9z"/>
  </g>
  <g fill="none" stroke="#fff2a8" stroke-width="1.5" opacity="0.8">
    <path d="M131,170 v40 M131,250 v40"/>
    <path d="M271,170 v40 M271,250 v40"/>
  </g>
</svg>