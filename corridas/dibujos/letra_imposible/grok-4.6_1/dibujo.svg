<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1c1a17"/>
      <stop offset="1" stop-color="#0a0908"/>
    </linearGradient>
    <linearGradient id="gly" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f4ecd8"/>
      <stop offset="0.45" stop-color="#e0d3b6"/>
      <stop offset="1" stop-color="#b9a888"/>
    </linearGradient>
    <radialGradient id="vig" cx="50%" cy="46%" r="68%">
      <stop offset="0.35" stop-color="#000" stop-opacity="0"/>
      <stop offset="1" stop-color="#000" stop-opacity="0.55"/>
    </radialGradient>
    <filter id="soft" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#000" flood-opacity="0.5"/>
    </filter>
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="7" result="n"/>
      <feColorMatrix in="n" type="luminanceToAlpha" result="a"/>
      <feComponentTransfer in="a" result="a2">
        <feFuncA type="linear" slope="0.07"/>
      </feComponentTransfer>
      <feBlend in="SourceGraphic" in2="a2" mode="multiply"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <g filter="url(#soft)">
    <g transform="rotate(90 200 200)">
      <path fill="url(#gly)" fill-rule="evenodd" d="M110,140 H310 V180 H270 V220 H310 V260 H110 A20,20 0 0 1 110,220 A20,20 0 0 1 110,180 A20,20 0 0 1 110,140 Z M90,160 m-7.5,0 a7.5,7.5 0 1 1 15,0 a7.5,7.5 0 1 1 -15,0 M90,200 m-7.5,0 a7.5,7.5 0 1 1 15,0 a7.5,7.5 0 1 1 -15,0 M90,240 m-7.5,0 a7.5,7.5 0 1 1 15,0 a7.5,7.5 0 1 1 -15,0"/>
      <path fill="none" stroke="#0a0908" stroke-width="3.2" stroke-linecap="butt" d="M110,180 H270 M110,220 H270"/>
    </g>
  </g>
  <rect width="400" height="400" fill="url(#vig)"/>
  <rect width="400" height="400" filter="url(#grain)" fill="#fff" opacity="0.04"/>
</svg>