<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-label="Self-portrait as a friendly AI">
  <defs>
    <linearGradient id="bg" x2="1" y2="1">
      <stop stop-color="#101b38"/>
      <stop offset="1" stop-color="#172044"/>
    </linearGradient>
    <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#88e9e3"/>
      <stop offset=".48" stop-color="#4a85b9"/>
      <stop offset="1" stop-color="#7468b9"/>
    </linearGradient>
    <linearGradient id="face" x2="1" y2="1">
      <stop stop-color="#213a60"/>
      <stop offset="1" stop-color="#1b254b"/>
    </linearGradient>
    <linearGradient id="body" x2="1" y2="1">
      <stop stop-color="#344f7b"/>
      <stop offset="1" stop-color="#282d60"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop stop-color="#5de5db" stop-opacity=".24"/>
      <stop offset="1" stop-color="#5de5db" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft">
      <feGaussianBlur stdDeviation="7"/>
    </filter>
    <clipPath id="frame">
      <rect width="400" height="400" rx="28"/>
    </clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="400" height="400" fill="url(#bg)"/>
    <circle cx="200" cy="176" r="188" fill="url(#glow)"/>
    <circle cx="200" cy="171" r="145" fill="none" stroke="#7ddbdc" stroke-opacity=".12"/>
    <circle cx="200" cy="171" r="159" fill="none" stroke="#a496ee" stroke-opacity=".08" stroke-dasharray="2 9"/>

    <g fill="#a2ede8">
      <circle cx="55" cy="88" r="2" opacity=".7"/>
      <circle cx="340" cy="67" r="2.5" opacity=".6"/>
      <circle cx="355" cy="234" r="2" opacity=".6"/>
      <circle cx="43" cy="263" r="1.5" opacity=".7"/>
    </g>
    <g stroke="#91d9e5" stroke-opacity=".4" stroke-linecap="round">
      <path d="M72 140v12m-6-6h12M328 145v12m-6-6h12M313 286v8m-4-4h8M87 287v8m-4-4h8"/>
    </g>

    <!-- Antenna and shoulders -->
    <path d="M200 89V70" stroke="#70b9ce" stroke-width="9" stroke-linecap="round"/>
    <circle cx="200" cy="62" r="10" fill="#68e4d6" filter="url(#soft)"/>
    <circle cx="200" cy="62" r="7" fill="#a7fff0"/>
    <path d="M117 291c-41 4-68 31-73 89h312c-5-58-32-85-73-89Z" fill="#111a39" stroke="#6280ad" stroke-width="3"/>
    <path d="M115 302c-27 5-44 26-49 78h268c-5-52-22-73-49-78l-42-15h-86Z" fill="url(#body)"/>
    <path d="M113 313c-15 8-23 27-27 67m201-67c15 8 23 27 27 67" fill="none" stroke="#85b7d9" stroke-opacity=".45" stroke-width="3"/>
    <path d="M162 268v31q38 32 76 0v-31" fill="#213252" stroke="#69a4bf" stroke-width="4"/>
    <path d="M166 295q34 25 68 0" fill="none" stroke="#71e3d8" stroke-opacity=".6" stroke-width="3"/>

    <!-- Ears and head -->
    <rect x="65" y="158" width="30" height="66" rx="13" fill="#415d8a" stroke="#76b5d2" stroke-width="3"/>
    <rect x="305" y="158" width="30" height="66" rx="13" fill="#415d8a" stroke="#76b5d2" stroke-width="3"/>
    <path d="M78 178v26m244-26v26" stroke="#82f0e1" stroke-width="4" stroke-linecap="round"/>
    <rect x="84" y="84" width="232" height="205" rx="54" fill="#101b36" stroke="url(#metal)" stroke-width="7"/>
    <rect x="96" y="96" width="208" height="181" rx="44" fill="url(#face)" stroke="#8ce5e1" stroke-opacity=".3" stroke-width="2"/>
    <path d="M113 147q10-34 43-38h88q33 4 43 38" fill="none" stroke="#d3ffff" stroke-opacity=".14" stroke-width="5" stroke-linecap="round"/>
    <path d="M172 95h56" stroke="#a5f7ed" stroke-opacity=".6" stroke-width="4" stroke-linecap="round"/>

    <!-- Face -->
    <path d="M128 169q17-13 36-5m72 0q19-8 36 5" fill="none" stroke="#8fe3df" stroke-opacity=".55" stroke-width="4" stroke-linecap="round"/>
    <ellipse cx="150" cy="190" rx="19" ry="24" fill="#65eee0" opacity=".18" filter="url(#soft)"/>
    <ellipse cx="250" cy="190" rx="19" ry="24" fill="#65eee0" opacity=".18" filter="url(#soft)"/>
    <rect x="135" y="177" width="30" height="34" rx="15" fill="#91f8e8"/>
    <rect x="235" y="177" width="30" height="34" rx="15" fill="#91f8e8"/>
    <circle cx="145" cy="185" r="5" fill="#fff"/>
    <circle cx="245" cy="185" r="5" fill="#fff"/>
    <path d="M169 231q31 29 62 0" fill="none" stroke="#9df6e8" stroke-width="6" stroke-linecap="round"/>
    <g fill="#e18fb7" opacity=".7">
      <circle cx="117" cy="218" r="3"/><circle cx="126" cy="222" r="2"/>
      <circle cx="283" cy="218" r="3"/><circle cx="274" cy="222" r="2"/>
    </g>
    <path d="M191 151l9-10 9 10-9 10Z" fill="#9af9e9" opacity=".75"/>

    <!-- Chest emblem -->
    <circle cx="200" cy="339" r="27" fill="#1a2b4c" stroke="#75c8d0" stroke-width="2"/>
    <circle cx="200" cy="339" r="19" fill="#65e8dd" opacity=".2" filter="url(#soft)"/>
    <path d="M200 322l4.3 12.7L217 339l-12.7 4.3L200 356l-4.3-12.7L183 339l12.7-4.3Z" fill="#a6fff0"/>
    <path d="M136 344h29m70 0h29" stroke="#77c7d0" stroke-opacity=".6" stroke-width="3" stroke-linecap="round"/>
  </g>
</svg>