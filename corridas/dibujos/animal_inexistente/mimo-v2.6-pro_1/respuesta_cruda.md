<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#120c30"/><stop offset="1" stop-color="#2e1252"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="45%" r="55%">
      <stop offset="0" stop-color="#6ee7ff" stop-opacity=".38"/><stop offset="1" stop-color="#6ee7ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="w1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ffb054"/><stop offset=".5" stop-color="#e5397f"/><stop offset="1" stop-color="#7b2ff7"/>
    </linearGradient>
    <linearGradient id="bd" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3ef0cf"/><stop offset="1" stop-color="#1c63a6"/>
    </linearGradient>
    <linearGradient id="horn" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ffe27a"/><stop offset="1" stop-color="#ff8a3d"/>
    </linearGradient>
    <g id="wing">
      <path d="M196 172 C142 92 42 88 38 156 C35 212 118 226 192 200 Z" fill="url(#w1)" stroke="#ffd9c2" stroke-width="2" stroke-opacity=".55"/>
      <path d="M193 206 C150 232 100 272 118 308 C138 340 182 292 197 248 Z" fill="url(#w1)" stroke="#ffd9c2" stroke-width="2" stroke-opacity=".55"/>
      <path d="M188 192 C138 164 92 142 52 150" fill="none" stroke="#ffe9d2" stroke-width="1.6" opacity=".5"/>
      <path d="M186 200 C140 190 100 190 68 200" fill="none" stroke="#ffe9d2" stroke-width="1.6" opacity=".38"/>
      <path d="M190 232 C162 258 138 282 128 300" fill="none" stroke="#ffe9d2" stroke-width="1.6" opacity=".45"/>
      <circle cx="88" cy="152" r="13" fill="#ffe27a" opacity=".85"/>
      <circle cx="88" cy="152" r="6" fill="#5c1560" opacity=".7"/>
      <circle cx="132" cy="196" r="8" fill="#fff2c2" opacity=".7"/>
      <circle cx="150" cy="272" r="9" fill="#ffe27a" opacity=".7"/>
    </g>
    <g id="leg" fill="none" stroke="url(#bd)" stroke-linecap="round">
      <path d="M186 296 C158 316 146 348 162 366 C174 379 191 370 186 356" stroke-width="9"/>
      <path d="M178 284 C146 292 122 316 128 338 C133 355 152 350 150 336" stroke-width="7"/>
      <path d="M198 306 C196 334 190 358 176 376" stroke-width="8"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="195" r="185" fill="url(#glow)"/>
  <g fill="#fff" opacity=".75">
    <circle cx="45" cy="55" r="1.8"/><circle cx="332" cy="42" r="2.2"/><circle cx="372" cy="122" r="1.5"/>
    <circle cx="28" cy="152" r="1.4"/><circle cx="358" cy="332" r="1.8"/><circle cx="52" cy="336" r="1.6"/>
    <circle cx="118" cy="28" r="1.3"/><circle cx="282" cy="26" r="1.5"/><circle cx="372" cy="228" r="1.3"/>
    <circle cx="22" cy="262" r="1.2"/><circle cx="212" cy="382" r="1.4"/><circle cx="112" cy="376" r="1.2"/>
  </g>

  <use href="#wing"/>
  <use href="#wing" transform="translate(400,0) scale(-1,1)"/>

  <path d="M214 300 C258 314 292 348 268 374 C250 392 226 378 238 360" fill="none" stroke="url(#bd)" stroke-width="11" stroke-linecap="round"/>
  <use href="#leg"/>
  <use href="#leg" transform="translate(400,0) scale(-1,1)"/>

  <path d="M200 122 C172 142 162 202 170 252 C177 294 200 322 200 322 C200 322 223 294 230 252 C238 202 228 142 200 122 Z" fill="url(#bd)" stroke="#8ff5e6" stroke-width="2" stroke-opacity=".5"/>
  <path d="M200 150 C193 190 192 246 200 296" fill="none" stroke="#0c4d78" stroke-width="2" opacity=".45"/>
  <path d="M182 214 C176 232 176 254 182 272" fill="none" stroke="#a8fff0" stroke-width="2" opacity=".35"/>
  <path d="M218 214 C224 232 224 254 218 272" fill="none" stroke="#a8fff0" stroke-width="2" opacity=".35"/>

  <ellipse cx="200" cy="152" rx="36" ry="31" fill="url(#bd)" stroke="#8ff5e6" stroke-width="2" stroke-opacity=".5"/>
  <path d="M170 132 C158 112 162 92 176 92 C188 92 190 112 182 128 Z" fill="#2fe0c4" stroke="#8ff5e6" stroke-width="1.5"/>
  <path d="M230 132 C242 112 238 92 224 92 C212 92 210 112 218 128 Z" fill="#2fe0c4" stroke="#8ff5e6" stroke-width="1.5"/>

  <path d="M200 122 C200 94 216 76 232 82 C248 88 246 112 228 116 C214 119 208 108 215 101" fill="none" stroke="url(#horn)" stroke-width="8" stroke-linecap="round"/>

  <circle cx="185" cy="152" r="12" fill="#fdf6ff"/><circle cx="187" cy="154" r="6.5" fill="#160e33"/>
  <circle cx="184" cy="150" r="2.4" fill="#fff"/>
  <circle cx="215" cy="152" r="12" fill="#fdf6ff"/><circle cx="213" cy="154" r="6.5" fill="#160e33"/>
  <circle cx="212" cy="150" r="2.4" fill="#fff"/>
  <circle cx="200" cy="128" r="8" fill="#ffe27a"/><circle cx="200" cy="128" r="3.4" fill="#5c1560"/>
  <path d="M192 172 C197 179 203 179 208 172" fill="none" stroke="#0c4d78" stroke-width="3" stroke-linecap="round"/>
  <circle cx="168" cy="166" r="7" fill="#ff7b9c" opacity=".45"/>
  <circle cx="232" cy="166" r="7" fill="#ff7b9c" opacity=".45"/>
</svg>