<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="70%">
      <stop offset="0" stop-color="#183653"/>
      <stop offset=".55" stop-color="#091827"/>
      <stop offset="1" stop-color="#02060c"/>
    </radialGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#0d8fa4"/>
      <stop offset=".52" stop-color="#125480"/>
      <stop offset="1" stop-color="#20295d"/>
    </linearGradient>
    <linearGradient id="heat" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#ffd05a"/>
      <stop offset=".5" stop-color="#f05b35"/>
      <stop offset="1" stop-color="#921f38"/>
    </linearGradient>
    <linearGradient id="hope" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#38b87c"/>
      <stop offset="1" stop-color="#b8f56a"/>
    </linearGradient>
    <clipPath id="globe">
      <circle cx="200" cy="203" r="126"/>
    </clipPath>
    <filter id="glow">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="54" cy="63" r="1.5" fill="#cdefff"/>
  <circle cx="92" cy="34" r="1" fill="#cdefff"/>
  <circle cx="335" cy="48" r="1.4" fill="#cdefff"/>
  <circle cx="366" cy="106" r=".9" fill="#cdefff"/>
  <circle cx="28" cy="153" r=".8" fill="#cdefff"/>
  <circle cx="321" cy="147" r=".7" fill="#cdefff"/>
  <path d="M35 101C92 28 156 22 200 31c77-16 137 19 169 74" fill="none" stroke="#5ed8e4" stroke-width="1" opacity=".22"/>
  <path d="M55 82C125 119 281 118 350 72" fill="none" stroke="#8cecff" stroke-width=".8" opacity=".18" stroke-dasharray="3 6"/>

  <circle cx="200" cy="203" r="132" fill="#52d6e1" opacity=".1" filter="url(#glow)"/>
  <circle cx="200" cy="203" r="126" fill="url(#sea)" stroke="#81dbe3" stroke-width="2"/>

  <g clip-path="url(#globe)">
    <path d="M59 168C91 155 113 155 133 167c17 10 26 4 39 14 14 11 2 28-15 29-22 1-24 17-39 19-13 2-23-9-39-6l-27 8z" fill="#5ead68"/>
    <path d="M111 218c19-6 38 4 42 19 4 16-9 29-6 43 2 14 16 23 6 40l-29-13-11-35-18-27z" fill="#3e955c"/>
    <path d="M190 107c19-13 46-17 63-5 13 9 17 20 32 24 16 4 36-1 49 14 9 10 6 23-10 27-17 4-24-7-38-2-8 3-13 14-25 12-14-2-17-15-31-17-18-3-25 13-43 7-11-4-19-13-12-24z" fill="#83b85d"/>
    <path d="M244 176c18-10 34 1 42 17 5 10 21 14 22 29 1 13-14 18-18 30-4 11 3 22-8 33-12 12-28 7-37 20-7 10-3 24-18 30-12 5-25-3-26-18-1-17 15-30 12-48-3-15-21-22-18-39 3-14 19-15 25-26 7-12 7-20 24-28z" fill="#5aa75b"/>
    <path d="M286 279c23-8 42 0 52 16l-4 30-48 14-19-22z" fill="#8ab65e"/>

    <path d="M263 81C315 101 350 147 350 204c0 32-11 62-29 85-6-41-10-76-27-105-14-24-30-62-31-103z" fill="url(#heat)" opacity=".7"/>
    <path d="M286 104c20 27 34 55 39 89M306 127c-8 16-9 28 5 42" fill="none" stroke="#ffd36c" stroke-width="3" opacity=".5"/>

    <path d="M74 272c46 20 79 32 125 33 55 1 91-12 130-35" fill="none" stroke="#b9eff0" stroke-width="5" opacity=".7"/>
    <path d="M67 282c45 19 88 30 134 31 52 1 94-11 123-28" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>

    <g fill="none" stroke="#a7f6ff" stroke-width="1" opacity=".55">
      <ellipse cx="200" cy="203" rx="126" ry="49"/>
      <ellipse cx="200" cy="203" rx="75" ry="126"/>
      <path d="M74 203h252"/>
    </g>

    <g stroke="#8bf3f0" stroke-width="1.2" opacity=".75">
      <path d="M117 177L180 143 247 151 286 207 218 239 147 246 117 177" fill="none"/>
      <path d="M180 143l38 96m29-88-100 95m139-39-169-30" fill="none"/>
    </g>
    <g fill="#d9ffff" filter="url(#glow)">
      <circle cx="117" cy="177" r="3"/><circle cx="180" cy="143" r="3"/>
      <circle cx="247" cy="151" r="3"/><circle cx="286" cy="207" r="3"/>
      <circle cx="218" cy="239" r="3"/><circle cx="147" cy="246" r="3"/>
    </g>

    <path d="M201 78l-9 38 13 20-10 25 14 22-12 25 9 27-14 25 12 22-8 31 12 17" fill="none" stroke="#06131d" stroke-width="5"/>
    <path d="M201 78l-9 38 13 20-10 25 14 22-12 25 9 27-14 25 12 22-8 31 12 17" fill="none" stroke="#ffbb58" stroke-width="1.2" opacity=".75"/>
  </g>

  <path d="M89 307c-13-16-19-35-21-54M311 307c14-17 20-36 22-56" fill="none" stroke="#bcecf0" stroke-width="2" opacity=".45"/>

  <g transform="translate(319 298)">
    <path d="M0 39c-3-19-1-37 4-53" fill="none" stroke="url(#hope)" stroke-width="5" stroke-linecap="round"/>
    <path d="M3 6C-18 4-24-9-21-25-3-25 8-14 3 6z" fill="#50c87d"/>
    <path d="M3-3C8-20 22-24 35-18 31-2 19 5 3-3z" fill="#9be967"/>
  </g>

  <g transform="translate(58 300)">
    <path d="M0 24h41M5 24V5l8-9v28M18 24V-15h10v39M31 24V-5l7 5v24" fill="#071018" stroke="#e26a42" stroke-width="1"/>
    <path d="M11-7c-8-10 2-15-2-24 13 9 13 18 2 24z" fill="#ff783f"/>
    <path d="M12-11c-3-5 2-8 1-13 5 5 5 9-1 13z" fill="#ffd45c"/>
  </g>

  <path d="M110 354c54 18 126 21 182 1" fill="none" stroke="#57cfac" stroke-width="2" opacity=".5"/>
  <text x="200" y="377" text-anchor="middle" fill="#c9eef0" font-family="sans-serif" font-size="11" letter-spacing="4" opacity=".8">FRÁGIL · CONECTADO · VIVO</text>
</svg>