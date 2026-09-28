<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#15163f"/>
      <stop offset=".55" stop-color="#684b87"/>
      <stop offset="1" stop-color="#ed9b78"/>
    </linearGradient>
    <linearGradient id="wall" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#ffd98c"/>
      <stop offset="1" stop-color="#d96a62"/>
    </linearGradient>
    <linearGradient id="side" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#753f65"/>
      <stop offset="1" stop-color="#3b3159"/>
    </linearGradient>
    <linearGradient id="roof" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#63d2c6"/>
      <stop offset="1" stop-color="#227e92"/>
    </linearGradient>
    <radialGradient id="moon">
      <stop stop-color="#fffbd0"/>
      <stop offset=".55" stop-color="#ffe5a0"/>
      <stop offset="1" stop-color="#ffb06e" stop-opacity=".1"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="0" dy="7" stdDeviation="7" flood-color="#171329" flood-opacity=".5"/>
    </filter>
    <pattern id="tiles" width="18" height="13" patternUnits="userSpaceOnUse">
      <path d="M0 13Q9 2 18 13M-9 0Q0 11 9 0M9 0Q18 11 27 0" fill="none" stroke="#bce7cc" stroke-width="1.3" opacity=".55"/>
    </pattern>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="316" cy="76" r="44" fill="#ffd982" opacity=".18" filter="url(#glow)"/>
  <circle cx="316" cy="76" r="29" fill="url(#moon)"/>
  <circle cx="305" cy="68" r="4" fill="#d59c70" opacity=".35"/>
  <circle cx="327" cy="85" r="6" fill="#d59c70" opacity=".25"/>

  <g fill="#fff6d0">
    <circle cx="45" cy="62" r="1.7"/><circle cx="83" cy="39" r="1"/>
    <circle cx="132" cy="76" r="1.4"/><circle cx="229" cy="42" r="1.5"/>
    <circle cx="267" cy="102" r="1"/><circle cx="364" cy="42" r="1.4"/>
    <path d="M179 38l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" opacity=".8"/>
    <path d="M62 117l1.5 4 4 1.5-4 1.5-1.5 4-1.5-4-4-1.5 4-1.5z" opacity=".7"/>
  </g>

  <g opacity=".32" fill="#332650">
    <path d="M0 276l43-38 34 31 43-60 38 50 43-25 44 39 38-54 48 43 39-30 30 31v137H0z"/>
  </g>

  <ellipse cx="200" cy="350" rx="122" ry="23" fill="#211c3e" opacity=".45" filter="url(#glow)"/>

  <g filter="url(#shadow)">
    <path d="M88 296Q98 316 123 323l73 26 79-25q27-8 38-30l-52 8-61-7-58 9z" fill="#463954"/>
    <path d="M123 323l73 26 79-25-1 10-77 30-75-29z" fill="#28243d"/>
    <path d="M142 304q13 33 3 60" fill="none" stroke="#82b77e" stroke-width="4"/>
    <path d="M145 330q-18-8-22 8 14 2 22 10M145 343q18-12 25 2-14 6-24 11" fill="#55a474"/>
    <path d="M259 304q-11 29-2 54" fill="none" stroke="#82b77e" stroke-width="4"/>
    <path d="M257 328q17-9 22 6-12 4-21 11" fill="#55a474"/>

    <path d="M103 170L198 105l99 67-24 25-74-48-75 50z" fill="url(#roof)"/>
    <path d="M198 105l99 67-15 7-84-55-84 57-11-11z" fill="#9ce0c0"/>
    <path d="M103 170L198 105l99 67-99-48z" fill="url(#tiles)" opacity=".75"/>

    <path d="M124 178l74-54v171l-74 9z" fill="url(#wall)"/>
    <path d="M198 124l84 55-9 125-75-9z" fill="url(#side)"/>

    <path d="M124 178l74-54v19l-74 54z" fill="#fff0ac" opacity=".4"/>
    <path d="M198 124l84 55-2 24-82-55z" fill="#201f48" opacity=".18"/>

    <g transform="translate(144 186) skewY(-8)">
      <rect width="35" height="45" rx="17" fill="#593b67" stroke="#ffdfa0" stroke-width="4"/>
      <path d="M17.5 2v41M2 22h31" stroke="#ffdfa0" stroke-width="3"/>
      <circle cx="10" cy="13" r="4" fill="#9ce8e1" opacity=".75"/>
    </g>

    <path d="M218 176l39 23-3 48-37-13z" fill="#25234b" stroke="#9ce0c0" stroke-width="4"/>
    <path d="M237 187l-1 54M218 205l38 20" stroke="#9ce0c0" stroke-width="3"/>
    <path d="M222 181q14-13 30 11" fill="none" stroke="#fff6bb" stroke-width="2" opacity=".7"/>

    <path d="M154 258l31-3v43l-31 4z" fill="#53395c" stroke="#ffe1a0" stroke-width="4"/>
    <path d="M162 267l15-2v17l-15 2z" fill="#1d2148"/>
    <circle cx="178" cy="287" r="2.5" fill="#a6e9c9"/>

    <path d="M198 295l75 9-17-18-58-8z" fill="#312949"/>
    <path d="M206 279l48 7 10-10-55-8z" fill="#7dd0bd"/>
    <path d="M209 268l55 8-8-14-43-6z" fill="#342b52"/>
    <path d="M213 256l43 6 9-10-48-7z" fill="#7dd0bd"/>
    <path d="M217 245l48 7-8-14-36-5z" fill="#342b52"/>

    <path d="M158 143q-8-39 9-53 17-14 8-35" fill="none" stroke="#384a58" stroke-width="9" stroke-linecap="round"/>
    <path d="M158 143q-8-39 9-53 17-14 8-35" fill="none" stroke="#a6d6c1" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 8"/>
    <path d="M169 60q-11-11 2-19 13 10 4 22z" fill="#ffc47c" opacity=".85"/>

    <g transform="rotate(-8 94 195)">
      <path d="M63 174h58v43H63z" fill="#422f58" stroke="#ffc989" stroke-width="4"/>
      <path d="M92 174v43M63 195h58" stroke="#ffc989" stroke-width="3"/>
      <path d="M70 185q10-12 20 0t20 0" fill="none" stroke="#86ddd1" stroke-width="3"/>
      <path d="M121 178l22 14-22 21z" fill="#2a294e" stroke="#ffc989" stroke-width="3"/>
    </g>

    <path d="M279 203q41-12 50 17 8 29-17 48" fill="none" stroke="#84d8c2" stroke-width="7" stroke-linecap="round"/>
    <path d="M312 268l-4-19 19 8z" fill="#84d8c2"/>
    <path d="M322 218q-8 9 2 15 10-8 0-16z" fill="#ffd58f"/>
  </g>

  <g>
    <path d="M55 318q21-17 40 1-20-5-40 0z" fill="#3c5264"/>
    <path d="M306 328q18-20 38-2-21-6-38 2z" fill="#3c5264"/>
    <path d="M90 330q-9-16 1-29 12 14 1 29M99 330q2-18 17-25 3 18-15 26" fill="#67ad83"/>
    <path d="M297 335q-5-20 10-30 8 19-8 31M308 336q4-17 19-20-1 17-18 22" fill="#67ad83"/>
  </g>

  <g fill="none" stroke="#fff4c3" stroke-width="2" opacity=".65">
    <path d="M30 146q21-15 42 0"/>
    <path d="M326 139q18-12 36 0"/>
  </g>
  <g fill="#fff4c3">
    <path d="M28 146l7-2-3 6zM72 146l-7-2 3 6z"/>
    <path d="M324 139l7-2-3 6zM362 139l-7-2 3 6z"/>
  </g>
</svg>