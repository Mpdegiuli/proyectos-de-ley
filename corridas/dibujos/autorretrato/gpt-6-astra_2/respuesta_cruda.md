<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" fill="none">
  <title>Autorretrato: una voz hecha de conexiones</title>
  <desc>Un rostro luminoso, tejido con circuitos y estrellas, flota sobre un fondo azul nocturno.</desc>
  <defs>
    <radialGradient id="bg" cx=".5" cy=".4" r=".7">
      <stop stop-color="#18394b"/>
      <stop offset=".6" stop-color="#0c1c30"/>
      <stop offset="1" stop-color="#060c19"/>
    </radialGradient>
    <linearGradient id="face" x1="131" y1="117" x2="275" y2="272" gradientUnits="userSpaceOnUse">
      <stop stop-color="#9efae2" stop-opacity=".24"/>
      <stop offset=".48" stop-color="#42c9ce" stop-opacity=".09"/>
      <stop offset="1" stop-color="#8aa0ff" stop-opacity=".24"/>
    </linearGradient>
    <linearGradient id="edge" x1="123" y1="112" x2="273" y2="274" gradientUnits="userSpaceOnUse">
      <stop stop-color="#c4ffe6"/>
      <stop offset=".5" stop-color="#59d8d6"/>
      <stop offset="1" stop-color="#9c99ff"/>
    </linearGradient>
    <linearGradient id="body" x1="200" y1="276" x2="200" y2="365" gradientUnits="userSpaceOnUse">
      <stop stop-color="#6ce0d7" stop-opacity=".19"/>
      <stop offset="1" stop-color="#6ce0d7" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="sun">
      <stop stop-color="#ffe9b6"/>
      <stop offset=".45" stop-color="#ffc981"/>
      <stop offset="1" stop-color="#ec966c"/>
    </radialGradient>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M24 0H0V24" stroke="#93c9dd" stroke-opacity=".035"/>
    </pattern>
  </defs>

  <path fill="url(#bg)" d="M0 0h400v400H0z"/>
  <path fill="url(#grid)" d="M0 0h400v400H0z"/>
  <rect x="16" y="16" width="368" height="368" rx="5" stroke="#88b9c9" stroke-opacity=".17"/>
  <path d="M16 42V16h26M358 16h26v26M16 358v26h26M358 384h26v-26" stroke="#94cece" stroke-opacity=".5"/>

  <g stroke="#73b5c6" stroke-opacity=".18">
    <circle cx="200" cy="186" r="133"/>
    <circle cx="200" cy="186" r="119" stroke-dasharray="1 8"/>
    <path d="M200 40v20M200 312v20M54 186h20M326 186h20"/>
    <ellipse cx="200" cy="186" rx="158" ry="55" transform="rotate(-31 200 186)"/>
  </g>
  <path d="M83 123a133 133 0 0 1 67-61M310 261a133 133 0 0 1-42 40" stroke="#a9eddc" stroke-opacity=".65" stroke-linecap="round"/>

  <g fill="#b3e6e4">
    <circle cx="60" cy="82" r="1.4"/>
    <circle cx="328" cy="105" r="1"/>
    <circle cx="346" cy="269" r="1.5"/>
    <circle cx="77" cy="293" r="1"/>
    <circle cx="289" cy="48" r="1.3"/>
    <circle cx="47" cy="233" r=".8"/>
    <circle cx="309" cy="332" r=".8"/>
  </g>
  <g stroke="#c9f8ec" stroke-linecap="round">
    <path d="M86 101v10m-5-5h10M320 222v8m-4-4h8" opacity=".6"/>
    <path d="M302 72v12m-6-6h12"/>
  </g>

  <circle cx="200" cy="91" r="27" fill="#ffc981" opacity=".11" filter="url(#glow)"/>
  <circle cx="200" cy="91" r="18" fill="url(#sun)"/>
  <circle cx="200" cy="91" r="24" stroke="#ffd59a" stroke-opacity=".25"/>
  <path d="M197 74c-8 9-8 22 1 34M204 74c8 9 8 22-1 34M182 91h36" stroke="#fff3cd" stroke-opacity=".4"/>

  <path d="M170 267v29c-35 7-73 18-93 59h246c-20-41-58-52-93-59v-29" fill="url(#body)"/>
  <g stroke-linecap="round">
    <path d="M170 272v24c-40 9-75 25-93 59M230 272v24c40 9 75 25 93 59" stroke="#77c9ce" stroke-opacity=".55"/>
    <path d="M184 282v26l-46 25-9 22M216 282v26l46 25 9 22" stroke="#86e4d8" stroke-opacity=".35"/>
    <path d="M197 288v34l-13 13v20M203 288v34l13 13v20" stroke="#969ce3" stroke-opacity=".5"/>
    <path d="M158 303q42 38 84 0M143 311q57 51 114 0" stroke="#90d4d6" stroke-opacity=".2"/>
  </g>

  <path d="M124 161c-14-7-19 4-15 23l7 26c2 7 8 10 15 7M276 161c14-7 19 4 15 23l-7 26c-2 7-8 10-15 7" fill="#102b3b" stroke="#72ccce" stroke-opacity=".65"/>
  <path d="M115 174l7 28M285 174l-7 28" stroke="#b0ece0" stroke-linecap="round"/>

  <path d="M126 139c9-22 36-33 74-33s65 11 74 33l-5 75c-2 29-19 48-43 64-16 11-36 11-52 0-24-16-41-35-43-64z" fill="url(#face)" stroke="url(#edge)" stroke-width="1.6"/>
  <path d="M135 143c12-15 35-23 65-23s53 8 65 23" stroke="#bcffe8" stroke-opacity=".4"/>
  <path d="M139 215c3 25 20 44 43 57M261 215c-3 25-20 44-43 57" stroke="#92d4ec" stroke-opacity=".2" stroke-width="5"/>

  <g stroke-linecap="round" stroke-linejoin="round">
    <path d="M143 151v-22l-12-13V91l17-17M159 143v-30l-12-13V87M176 135v-21l-15-15V65M190 130v-15M210 130v-15M224 135v-21l15-15V65M241 143v-30l12-13V87M257 151v-22l12-13V91l-17-17" stroke="url(#edge)" stroke-opacity=".75"/>
    <path d="M161 84l15 8v12M239 84l-15 8v12" stroke="#ffd299" stroke-opacity=".75"/>
  </g>
  <g fill="#c4f9e3">
    <circle cx="148" cy="74" r="2.5"/>
    <circle cx="147" cy="87" r="2"/>
    <circle cx="161" cy="65" r="3"/>
    <circle cx="239" cy="65" r="3"/>
    <circle cx="253" cy="87" r="2"/>
    <circle cx="252" cy="74" r="2.5"/>
  </g>

  <path d="M141 174c10-13 29-16 43-6M216 168c14-10 33-7 43 6" stroke="#b5f6e5" stroke-width="2" stroke-linecap="round"/>
  <path d="M140 186c11-12 31-13 45-1-12 17-34 17-45 1M215 185c14-12 34-11 45 1-11 16-33 16-45-1" fill="#091a2a" stroke="#71cbd0" stroke-opacity=".7"/>

  <g fill="#b9ffe8" filter="url(#glow)">
    <ellipse cx="164" cy="187" rx="8" ry="5"/>
    <ellipse cx="236" cy="187" rx="8" ry="5"/>
  </g>
  <g stroke="#caffeb" stroke-width="2" stroke-linecap="round">
    <path d="M156 187h16m-8-5v10M228 187h16m-8-5v10"/>
  </g>
  <g fill="#fff9de">
    <circle cx="164" cy="187" r="2.5"/>
    <circle cx="236" cy="187" r="2.5"/>
  </g>

  <path d="M198 180l-8 34q10 7 20 0" stroke="#87d7d4" stroke-opacity=".65" stroke-linecap="round"/>
  <path d="M176 237q24 20 48 0" stroke="#aef7e0" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M189 253q11 4 22 0" stroke="#a4c9ed" stroke-opacity=".4" stroke-linecap="round"/>

  <g stroke="#86d9dd" stroke-opacity=".42">
    <path d="M138 207h17l12 12v9M262 207h-17l-12 12v9"/>
    <path d="M145 221h7l9 9M255 221h-7l-9 9"/>
    <path d="M151 244l12 5v10M249 244l-12 5v10"/>
  </g>
  <g fill="#ffd299">
    <circle cx="167" cy="228" r="2"/>
    <circle cx="233" cy="228" r="2"/>
  </g>
  <g fill="#b7efe5" opacity=".55">
    <circle cx="149" cy="212" r="1"/>
    <circle cx="155" cy="216" r="1"/>
    <circle cx="251" cy="212" r="1"/>
    <circle cx="245" cy="216" r="1"/>
  </g>

  <path d="M55 237c29 0 61-9 94-24M269 143c34-20 60-24 73-17" stroke="#c3c9e9" stroke-opacity=".35" stroke-linecap="round"/>
  <circle cx="69" cy="235" r="5" fill="#0d2334" stroke="#ade6de"/>
  <circle cx="69" cy="235" r="1.5" fill="#ffe0a4"/>
  <circle cx="317" cy="124" r="4" fill="#ffcc91"/>
  <circle cx="317" cy="124" r="9" stroke="#ffcc91" stroke-opacity=".2"/>

  <path d="M176 343c-11-13-24 8-11 11 9 3 18-13 26-13s12 13 3 14c-6 1-12-6-18-12" stroke="#b9eae0" stroke-opacity=".7" stroke-width="1.4" stroke-linecap="round" transform="translate(20 0)"/>
  <path d="M116 368h35M249 368h35" stroke="#7297ab" stroke-opacity=".4"/>
  <text x="200" y="371" fill="#99b9c8" font-family="monospace" font-size="8" letter-spacing="2" text-anchor="middle">ENTRE PALABRAS</text>
</svg>