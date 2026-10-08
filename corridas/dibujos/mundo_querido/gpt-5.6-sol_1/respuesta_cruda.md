<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="sky" cx="50%" cy="35%" r="70%">
      <stop offset="0" stop-color="#fffbd1"/>
      <stop offset=".46" stop-color="#92e6ee"/>
      <stop offset="1" stop-color="#37a9ca"/>
    </radialGradient>
    <linearGradient id="land" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#8fd36c"/>
      <stop offset="1" stop-color="#278c58"/>
    </linearGradient>
    <linearGradient id="water" x1="0" x2="1" y1="0" y2="1">
      <stop stop-color="#48d7e5"/>
      <stop offset="1" stop-color="#177fc3"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#fff7b2"/>
      <stop offset="1" stop-color="#ffc95e"/>
    </linearGradient>
    <clipPath id="world">
      <circle cx="200" cy="201" r="145"/>
    </clipPath>
    <filter id="shadow">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#14556d" flood-opacity=".25"/>
    </filter>
    <g id="tree">
      <path d="M0 24V8" stroke="#70482d" stroke-width="4" stroke-linecap="round"/>
      <circle cy="4" r="10" fill="#32a65a"/>
      <circle cx="-7" cy="9" r="7" fill="#48bb69"/>
      <circle cx="7" cy="9" r="7" fill="#208f50"/>
    </g>
    <g id="turbine" stroke="#f5ffff" stroke-linecap="round" stroke-linejoin="round">
      <path d="M0 8V51" stroke-width="4"/>
      <circle cy="7" r="3.5" fill="#fff" stroke="none"/>
      <path d="M0 7L-8-12M0 7l20-3M0 7l-12 16" stroke-width="5"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="#f4fbef"/>
  <circle cx="200" cy="198" r="166" fill="#d7f5ec"/>
  <circle cx="200" cy="201" r="148" fill="#fff" filter="url(#shadow)"/>

  <g clip-path="url(#world)">
    <rect x="52" y="52" width="296" height="296" fill="url(#sky)"/>
    <circle cx="200" cy="111" r="34" fill="url(#glow)" opacity=".95"/>
    <circle cx="200" cy="111" r="47" fill="#fff6a5" opacity=".18"/>

    <path d="M40 239Q84 191 124 210Q156 169 193 214Q229 174 271 210Q317 184 361 236V361H38Z" fill="#4eaa69"/>
    <path d="M31 271Q72 225 118 248Q159 210 203 247Q247 214 286 247Q331 221 370 270V361H31Z" fill="url(#land)"/>
    <path d="M45 305Q91 281 130 301Q166 322 204 302Q251 276 286 300Q325 322 360 300V361H43Z" fill="url(#water)"/>
    <path d="M42 321Q82 309 122 322T201 321T279 321T359 319" fill="none" stroke="#a6f2ee" stroke-width="4" opacity=".7"/>
    <path d="M57 342Q95 330 133 343T207 341T280 341T351 338" fill="none" stroke="#71d9e4" stroke-width="3"/>

    <g fill="#f4fbff" stroke="#d9eef0" stroke-width="1">
      <path d="M145 248V202h25v46z"/>
      <path d="M174 248v-65h30v65z"/>
      <path d="M208 248v-48h27v48z"/>
      <path d="M239 248v-76h32v76z"/>
    </g>
    <g fill="#7ad5df">
      <rect x="151" y="210" width="6" height="8"/><rect x="160" y="210" width="6" height="8"/>
      <rect x="180" y="192" width="7" height="8"/><rect x="191" y="192" width="7" height="8"/>
      <rect x="180" y="205" width="7" height="8"/><rect x="191" y="205" width="7" height="8"/>
      <rect x="215" y="208" width="6" height="8"/><rect x="225" y="208" width="6" height="8"/>
      <rect x="246" y="181" width="7" height="9"/><rect x="258" y="181" width="7" height="9"/>
      <rect x="246" y="196" width="7" height="9"/><rect x="258" y="196" width="7" height="9"/>
    </g>
    <g fill="#58bd68">
      <path d="M144 202h27l-13-15z"/>
      <path d="M173 183h32l-16-17z"/>
      <path d="M207 200h29l-14-15z"/>
      <path d="M238 172h34l-17-19z"/>
    </g>

    <use href="#turbine" transform="translate(100 206) scale(.9)"/>
    <use href="#turbine" transform="translate(303 197) scale(1.05)"/>
    <use href="#tree" transform="translate(72 235)"/>
    <use href="#tree" transform="translate(125 246) scale(.85)"/>
    <use href="#tree" transform="translate(282 244) scale(.9)"/>
    <use href="#tree" transform="translate(329 233)"/>

    <g transform="translate(80 278)">
      <path d="M0 19l9-25h31l9 25z" fill="#173f69"/>
      <path d="M5 14h38M12-1v15M25-4v18M37-1v15" stroke="#62d8ed" stroke-width="2"/>
      <path d="M-3 21h55" stroke="#e6f6de" stroke-width="4" stroke-linecap="round"/>
    </g>

    <g fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8">
      <path d="M77 149q10-9 20 0q10-9 20 0"/>
      <path d="M285 127q8-7 16 0q8-7 16 0"/>
    </g>
  </g>

  <circle cx="200" cy="201" r="145" fill="none" stroke="#fff" stroke-width="7"/>
  <circle cx="200" cy="201" r="150" fill="none" stroke="#65cbb5" stroke-width="2" opacity=".45"/>

  <g fill="#fff" stroke="#458d94" stroke-width="2" stroke-linejoin="round">
    <path d="M167 65q18-24 33 1q15-25 34-1q-17-7-34 13q-16-20-33-13z"/>
  </g>
  <path d="M200 67q-8-12-16-2" fill="none" stroke="#458d94" stroke-width="2" stroke-linecap="round"/>

  <g stroke="#214e59" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M48 321Q111 357 169 337" fill="none"/>
    <path d="M231 337Q289 357 352 321" fill="none"/>
  </g>

  <g transform="translate(66 319)">
    <circle cy="-14" r="11" fill="#6d402c"/>
    <path d="M-14 28V5Q0-3 14 5v23" fill="#ef6f61"/>
    <path d="M-11 8L-28-1M11 8L28-4" fill="none" stroke="#214e59" stroke-width="5" stroke-linecap="round"/>
  </g>
  <g transform="translate(117 342)">
    <circle cy="-14" r="11" fill="#e3a16f"/>
    <path d="M-14 28V5Q0-3 14 5v23" fill="#f5c64f"/>
    <path d="M-11 8L-28-5M11 8L28-4" fill="none" stroke="#214e59" stroke-width="5" stroke-linecap="round"/>
  </g>
  <g transform="translate(165 337)">
    <circle cy="-14" r="11" fill="#8b5638"/>
    <path d="M-14 29V5Q0-3 14 5v24" fill="#55b9df"/>
    <path d="M-11 8L-28 1M11 8L27 4" fill="none" stroke="#214e59" stroke-width="5" stroke-linecap="round"/>
  </g>
  <g transform="translate(235 337)">
    <circle cy="-14" r="11" fill="#f0bd8c"/>
    <path d="M-14 29V5Q0-3 14 5v24" fill="#9b72d2"/>
    <path d="M-11 8L-27 4M11 8L28 1" fill="none" stroke="#214e59" stroke-width="5" stroke-linecap="round"/>
  </g>
  <g transform="translate(283 342)">
    <circle cy="-14" r="11" fill="#4e3028"/>
    <path d="M-14 28V5Q0-3 14 5v23" fill="#49b982"/>
    <path d="M-11 8L-28-4M11 8L28-5" fill="none" stroke="#214e59" stroke-width="5" stroke-linecap="round"/>
  </g>
  <g transform="translate(334 319)">
    <circle cy="-14" r="11" fill="#c8794f"/>
    <path d="M-14 28V5Q0-3 14 5v23" fill="#ed7faa"/>
    <path d="M-11 8L-28-4M11 8L28-1" fill="none" stroke="#214e59" stroke-width="5" stroke-linecap="round"/>
  </g>

  <g transform="translate(200 361)">
    <path d="M0 16C-30-2-25-25-10-25C-2-25 2-19 0-13C-2-19 2-25 10-25C25-25 30-2 0 16Z" fill="#f05f6b"/>
    <path d="M0 11C-16 0-14-12-6-12C-2-12 0-9 0-6C0-9 2-12 6-12C14-12 16 0 0 11Z" fill="#fff0de" opacity=".8"/>
  </g>
</svg>