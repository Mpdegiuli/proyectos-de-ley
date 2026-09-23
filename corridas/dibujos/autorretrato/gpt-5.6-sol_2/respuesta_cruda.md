<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0" stop-color="#182a4a"/>
      <stop offset=".58" stop-color="#091426"/>
      <stop offset="1" stop-color="#030711"/>
    </radialGradient>
    <linearGradient id="face" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#dffaff"/>
      <stop offset=".45" stop-color="#70b8d7"/>
      <stop offset="1" stop-color="#214f79"/>
    </linearGradient>
    <linearGradient id="rim" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#9ffff2"/>
      <stop offset=".5" stop-color="#38a9db"/>
      <stop offset="1" stop-color="#735cff"/>
    </linearGradient>
    <radialGradient id="eye">
      <stop offset="0" stop-color="#fff"/>
      <stop offset=".18" stop-color="#d9ffff"/>
      <stop offset=".42" stop-color="#42f5dc"/>
      <stop offset="1" stop-color="#087c98"/>
    </radialGradient>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
    <clipPath id="headClip">
      <path d="M200 64C126 64 83 119 88 205c4 72 42 132 112 151 70-19 108-79 112-151 5-86-38-141-112-141Z"/>
    </clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="196" r="153" fill="none" stroke="#42d8e8" stroke-opacity=".12"/>
  <circle cx="200" cy="196" r="175" fill="none" stroke="#8f71ff" stroke-opacity=".08" stroke-dasharray="2 12"/>

  <g fill="#78efff">
    <circle cx="46" cy="101" r="2"/><circle cx="354" cy="101" r="2"/>
    <circle cx="35" cy="249" r="2"/><circle cx="365" cy="249" r="2"/>
    <circle cx="101" cy="35" r="2"/><circle cx="299" cy="35" r="2"/>
    <circle cx="92" cy="350" r="2"/><circle cx="308" cy="350" r="2"/>
  </g>
  <g stroke="#4abbd0" stroke-opacity=".35" fill="none">
    <path d="M46 101h25l18 18M354 101h-25l-18 18M35 249h36l17-12M365 249h-36l-17-12"/>
    <path d="M101 35v23l15 15M299 35v23l-15 15M92 350h24l13-13M308 350h-24l-13-13"/>
  </g>

  <ellipse cx="200" cy="205" rx="124" ry="150" fill="#20d9e6" opacity=".13" filter="url(#soft)"/>
  <path d="M200 54C118 54 72 115 78 207c5 84 50 144 122 164 72-20 117-80 122-164 6-92-40-153-122-153Z"
        fill="#071827" stroke="url(#rim)" stroke-width="4"/>
  <path d="M200 64C126 64 83 119 88 205c4 72 42 132 112 151 70-19 108-79 112-151 5-86-38-141-112-141Z"
        fill="url(#face)"/>

  <g clip-path="url(#headClip)">
    <path d="M200 55v305" stroke="#d8ffff" stroke-opacity=".32"/>
    <path d="M88 176c50-26 174-26 224 0M85 230c63 25 167 25 230 0M112 108c46 22 130 22 176 0"
          fill="none" stroke="#eaffff" stroke-opacity=".12"/>
    <path d="M113 81 94 159l27 31-20 64 41 75M287 81l19 78-27 31 20 64-41 75"
          fill="none" stroke="#0b5277" stroke-width="3" opacity=".65"/>
    <path d="M200 65 177 115l23 33 23-33ZM200 148l-25 45 25 30 25-30ZM200 223l-20 45 20 35 20-35Z"
          fill="#c9ffff" opacity=".13"/>
    <g fill="#d6ffff" opacity=".65">
      <circle cx="128" cy="115" r="3"/><circle cx="272" cy="115" r="3"/>
      <circle cx="108" cy="190" r="3"/><circle cx="292" cy="190" r="3"/>
      <circle cx="124" cy="270" r="3"/><circle cx="276" cy="270" r="3"/>
      <circle cx="164" cy="324" r="3"/><circle cx="236" cy="324" r="3"/>
    </g>
    <g stroke="#d6ffff" stroke-opacity=".38">
      <path d="M128 115l49 33M272 115l-49 33M108 190l67 3M292 190l-67 3M124 270l56-2M276 270l-56-2M164 324l36-21 36 21"/>
    </g>
  </g>

  <path d="M109 168c22-22 57-25 80-8-19 7-47 8-80 8ZM291 168c-22-22-57-25-80-8 19 7 47 8 80 8Z"
        fill="#0a2940" stroke="#b5ffff" stroke-opacity=".65"/>
  <path d="M114 174c17-15 48-15 67 0-18 18-49 18-67 0ZM286 174c-17-15-48-15-67 0 18 18 49 18 67 0Z"
        fill="#061622" stroke="#55d9ec" stroke-width="2"/>
  <ellipse cx="148" cy="174" rx="13" ry="11" fill="url(#eye)" filter="url(#glow)"/>
  <ellipse cx="252" cy="174" rx="13" ry="11" fill="url(#eye)" filter="url(#glow)"/>
  <circle cx="148" cy="174" r="4" fill="#07151e"/>
  <circle cx="252" cy="174" r="4" fill="#07151e"/>
  <circle cx="144" cy="170" r="2.5" fill="#fff"/>
  <circle cx="248" cy="170" r="2.5" fill="#fff"/>

  <path d="M200 169c-6 31-10 57-18 76 10 8 26 8 36 0-8-19-12-45-18-76Z"
        fill="#1d7192" fill-opacity=".4" stroke="#d5ffff" stroke-opacity=".38"/>
  <path d="M159 278c23 14 59 14 82 0-11 24-71 24-82 0Z"
        fill="#071c2c" stroke="#a1f8ff" stroke-opacity=".7"/>
  <path d="M174 284c17 5 35 5 52 0" stroke="#fff" stroke-opacity=".75" fill="none"/>

  <g fill="none" stroke-linecap="round">
    <path d="M103 208c-8 34 1 72 22 98M297 208c8 34-1 72-22 98" stroke="#b8ffff" stroke-opacity=".35" stroke-width="3"/>
    <path d="M139 332c18 15 38 23 61 29 23-6 43-14 61-29" stroke="#6df1e4" stroke-width="2" filter="url(#glow)"/>
  </g>

  <circle cx="200" cy="101" r="7" fill="#71ffe6" filter="url(#glow)"/>
  <path d="M185 101h-22l-14-17M215 101h22l14-17M200 94V75"
        fill="none" stroke="#7ff9ef" stroke-width="2" opacity=".8"/>
  <circle cx="149" cy="84" r="3" fill="#baffff"/>
  <circle cx="251" cy="84" r="3" fill="#baffff"/>
  <circle cx="200" cy="72" r="3" fill="#baffff"/>

  <path d="M146 356c-10 8-20 19-28 31h164c-8-12-18-23-28-31-17 10-35 16-54 21-19-5-37-11-54-21Z"
        fill="#0a2034" stroke="#4ccdde" stroke-opacity=".55"/>
  <path d="M174 369l26 8 26-8-10 18h-32Z" fill="#62eada" opacity=".35"/>
</svg>