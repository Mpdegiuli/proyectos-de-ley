```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0d1030"/>
      <stop offset="0.45" stop-color="#2a1f52"/>
      <stop offset="0.8" stop-color="#4b2c5c"/>
      <stop offset="1" stop-color="#6b3b55"/>
    </linearGradient>
    <radialGradient id="moonG" cx="0.4" cy="0.35">
      <stop offset="0" stop-color="#fff8dd"/>
      <stop offset="1" stop-color="#e3cf96"/>
    </radialGradient>
    <radialGradient id="halo">
      <stop offset="0" stop-color="#ffe9a8" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#ffe9a8" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rock" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5d4a5e"/>
      <stop offset="1" stop-color="#201a2e"/>
    </linearGradient>
    <linearGradient id="wallA" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f2e2c2"/>
      <stop offset="1" stop-color="#cdb491"/>
    </linearGradient>
    <linearGradient id="wallB" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#a98d70"/>
      <stop offset="1" stop-color="#7d6450"/>
    </linearGradient>
    <linearGradient id="roofG" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#8e3d4e"/>
      <stop offset="0.5" stop-color="#c25c62"/>
      <stop offset="1" stop-color="#7a3348"/>
    </linearGradient>
    <radialGradient id="win">
      <stop offset="0" stop-color="#fff3bd"/>
      <stop offset="1" stop-color="#f2b53d"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff8e0">
    <circle cx="28" cy="40" r="1.5"/><circle cx="70" cy="22" r="1"/>
    <circle cx="112" cy="58" r="1.8"/><circle cx="160" cy="28" r="1"/>
    <circle cx="205" cy="62" r="1.3"/><circle cx="248" cy="30" r="1"/>
    <circle cx="352" cy="140" r="1.6"/><circle cx="378" cy="60" r="1.1"/>
    <circle cx="44" cy="120" r="1.2"/><circle cx="18" cy="190" r="1.4"/>
    <circle cx="384" cy="210" r="1"/><circle cx="330" cy="255" r="1.3"/>
    <circle cx="90" cy="96" r="1"/><circle cx="268" cy="96" r="1.2"/>
  </g>

  <circle cx="308" cy="82" r="70" fill="url(#halo)"/>
  <circle cx="308" cy="82" r="32" fill="url(#moonG)"/>
  <g fill="#d6c089" opacity="0.7">
    <circle cx="298" cy="74" r="6"/><circle cx="316" cy="92" r="4"/><circle cx="318" cy="68" r="2.5"/>
  </g>

  <g opacity="0.85" stroke="#2c2242" stroke-width="2" fill="none">
    <path d="M168 352 C162 372 172 386 166 398"/>
    <path d="M206 372 C202 384 210 392 206 400"/>
    <path d="M142 336 C134 350 140 358 134 368"/>
  </g>
  <path d="M108 300 L292 297 L272 324 L236 344 L202 378 L168 346 L134 326 Z" fill="url(#rock)"/>
  <path d="M292 297 L272 324 L236 344 L202 378 L206 340 L240 320 Z" fill="#171327" opacity="0.5"/>
  <ellipse cx="200" cy="299" rx="93" ry="14" fill="#4e7355"/>
  <ellipse cx="200" cy="296" rx="93" ry="13" fill="#6a9463"/>

  <g>
    <polygon points="138,300 146,206 200,190 203,301" fill="url(#wallA)"/>
    <polygon points="203,301 200,190 262,213 257,296" fill="url(#wallB)"/>
    <path d="M124 218 C150 168 198 204 200 168 C204 204 250 172 278 222 L262 232 C238 196 206 216 200 186 C194 218 162 200 140 230 Z" fill="url(#roofG)"/>
    <path d="M124 218 C150 168 198 204 200 168 C204 204 250 172 278 222" fill="none" stroke="#5e2738" stroke-width="2"/>

    <g transform="rotate(-16 230 176)">
      <rect x="222" y="160" width="15" height="34" rx="2" fill="#8c6a52"/>
      <rect x="219" y="155" width="21" height="8" rx="2" fill="#a8846a"/>
    </g>
    <path d="M228 150 C216 136 240 130 230 116 C222 104 244 98 240 86" fill="none" stroke="#e5dcf0" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
    <g fill="#fff6cc"><circle cx="242" cy="78" r="2.2"/><circle cx="252" cy="66" r="1.5"/><circle cx="234" cy="62" r="1.2"/></g>

    <circle cx="228" cy="240" r="15" fill="url(#win)"/>
    <circle cx="228" cy="240" r="15" fill="none" stroke="#6d4f3a" stroke-width="3"/>
    <path d="M213 240 h30 M228 225 v30" stroke="#6d4f3a" stroke-width="2.5"/>

    <g transform="rotate(9 168 226)">
      <rect x="155" y="212" width="26" height="28" rx="3" fill="url(#win)" stroke="#6d4f3a" stroke-width="3"/>
      <path d="M168 212 v28 M155 226 h26" stroke="#6d4f3a" stroke-width="2"/>
    </g>

    <path d="M158 300 L158 262 A16 16 0 0 1 190 262 L190 300 Z" fill="#2a1b2c" opacity="0.25" transform="translate(4,0)"/>
    <g transform="rotate(-7 174 282)">
      <path d="M158 296 L158 258 A16 16 0 0 1 190 258 L190 296 Z" fill="#7b4a34" stroke="#4d2c1f" stroke-width="2.5"/>
      <circle cx="183" cy="278" r="2.4" fill="#ffdf8a"/>
      <path d="M158 296 L190 296" stroke="#4d2c1f" stroke-width="2.5"/>
    </g>
    <path d="M154 300 L196 300 L206 316 L146 316 Z" fill="#ffdb93" opacity="0.28"/>
  </g>

  <g>
    <g fill="#6f5b7a" stroke="#3a2f4d" stroke-width="1.2">
      <polygon points="46,286 68,286 74,291 52,291"/><polygon points="52,291 74,291 74,297 52,297"/>
      <polygon points="58,272 80,272 86,277 64,277"/><polygon points="64,277 86,277 86,283 64,283"/>
      <polygon points="70,258 92,258 98,263 76,263"/><polygon points="76,263 98,263 98,269 76,269"/>
      <polygon points="82,244 104,244 110,249 88,249"/><polygon points="88,249 110,249 110,255 88,255"/>
      <polygon points="94,230 116,230 122,235 100,235"/><polygon points="100,235 122,235 122,241 100,241"/>
      <polygon points="106,216 128,216 134,221 112,221"/><polygon points="112,221 134,221 134,227 112,227"/>
    </g>
    <g transform="rotate(5 124 190)">
      <rect x="106" y="160" width="36" height="56" rx="3" fill="none" stroke="#6b4b6d" stroke-width="5"/>
      <rect x="110" y="164" width="28" height="48" fill="#ffd77a" opacity="0.3"/>
      <circle cx="124" cy="188" r="7" fill="#ffeeb5" opacity="0.5"/>
    </g>
  </g>

  <g fill="url(#rock)" stroke="#2a2138" stroke-width="1">
    <path d="M300 250 l20 3 l-8 12 l-16 -5 z"/>
    <path d="M66 176 l16 2 l-7 10 l-12 -4 z"/>
    <path d="M320 320 l26 4 l-12 14 l-18 -6 z"/>
  </g>
  <g fill="#6a9463">
    <path d="M300 250 l20 3 l-3 4 l-18 -3 z"/>
    <path d="M320 320 l26 4 l-3 5 l-24 -4 z"/>
  </g>

  <g stroke="#ffe9a8" stroke-width="1" opacity="0.5" fill="none">
    <path d="M200 380 C205 392 195 396 200 400"/>
  </g>
</svg>
```