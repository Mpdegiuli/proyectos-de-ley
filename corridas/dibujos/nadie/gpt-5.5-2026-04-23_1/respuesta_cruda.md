<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%">
      <stop offset="0" stop-color="#23345f"/>
      <stop offset=".65" stop-color="#11162c"/>
      <stop offset="1" stop-color="#070812"/>
    </radialGradient>
    <linearGradient id="glass" x1="120" y1="50" x2="285" y2="340">
      <stop offset="0" stop-color="#e8ffff" stop-opacity=".55"/>
      <stop offset=".45" stop-color="#8ed8ff" stop-opacity=".18"/>
      <stop offset="1" stop-color="#d7ffff" stop-opacity=".35"/>
    </linearGradient>
    <linearGradient id="isle" x1="160" y1="210" x2="235" y2="300">
      <stop offset="0" stop-color="#99e16f"/>
      <stop offset=".55" stop-color="#54452d"/>
      <stop offset="1" stop-color="#23191b"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .s{stroke-linecap:round;stroke-linejoin:round}
      .ink{stroke:#0b1022;stroke-width:3}
      .thin{stroke:#d9f8ff;stroke-width:1.4;opacity:.65}
      .star{fill:#fff3a8;filter:url(#glow)}
    </style>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <g opacity=".85">
    <circle class="star" cx="45" cy="55" r="1.7"/><circle class="star" cx="338" cy="44" r="1.3"/>
    <circle class="star" cx="367" cy="111" r="2"/><circle class="star" cx="71" cy="145" r="1.2"/>
    <circle class="star" cx="306" cy="176" r="1.5"/><circle class="star" cx="29" cy="248" r="1.4"/>
    <circle class="star" cx="358" cy="294" r="1.1"/><circle class="star" cx="100" cy="34" r="1.1"/>
    <path d="M323 78l4 8 8 1-6 6 1 8-7-4-8 4 2-8-6-6 8-1z" fill="#ffd78a" opacity=".85"/>
  </g>
  <ellipse cx="200" cy="356" rx="135" ry="15" fill="#000" opacity=".35"/>
  <g class="s">
    <path d="M137 69c-27 37-33 82-24 130 8 45 31 86 58 117h58c27-31 50-72 58-117 9-48 3-93-24-130-32-16-94-16-126 0z" fill="url(#glass)" stroke="#d8fbff" stroke-width="3"/>
    <path d="M142 65c28-13 88-13 116 0" fill="none" stroke="#fff" stroke-width="7" opacity=".42"/>
    <path d="M125 82c32 13 118 13 150 0M121 315c43 17 115 17 158 0" fill="none" class="thin"/>
    <path d="M166 78c-22 55-18 145 11 223M245 78c21 58 15 145-22 223" fill="none" class="thin"/>
  </g>
  <g class="s">
    <ellipse cx="201" cy="264" rx="72" ry="17" fill="#20314a" opacity=".42"/>
    <path d="M133 254c16-33 47-50 81-45 32 5 51 24 57 49-37 21-97 25-138-4z" fill="url(#isle)" class="ink"/>
    <path d="M145 254c34 12 82 10 113-2" fill="none" stroke="#b8f28a" stroke-width="4"/>
    <path d="M173 274l-8 28M194 269l3 36M225 268l13 32" stroke="#2b1c20" stroke-width="5"/>
  </g>
  <g class="s" transform="translate(0 2)">
    <ellipse cx="199" cy="211" rx="35" ry="28" fill="#8b58d7" class="ink"/>
    <path d="M177 205c2-21 15-33 26-31 12 2 20 16 19 35" fill="#a574ee" class="ink"/>
    <circle cx="190" cy="196" r="5" fill="#fff"/><circle cx="211" cy="196" r="5" fill="#fff"/>
    <circle cx="191" cy="197" r="2" fill="#101426"/><circle cx="210" cy="197" r="2" fill="#101426"/>
    <path d="M196 209c6 4 13 3 18-2" fill="none" stroke="#30133f" stroke-width="2"/>
    <path d="M171 218c-22 0-25-23-45-17M169 226c-25 9-18 30-39 37M184 236c-20 18-7 33-22 51M215 236c21 18 8 33 24 51M230 226c25 9 18 30 40 37M228 218c22 0 25-23 46-17" fill="none" stroke="#7843c0" stroke-width="9"/>
    <path d="M126 201l-17-12 5-11 23 17M129 263l-22 5-6-12 26-5M162 287l-4 21-13-1 4-24M239 287l4 21 13-1-4-24M270 263l22 5 6-12-26-5M273 201l17-12-5-11-23 17" fill="#d7c3ff" class="ink"/>
  </g>
  <g class="s">
    <rect x="113" y="172" width="35" height="27" rx="3" fill="#ffe8a8" class="ink"/>
    <path d="M118 180h24M118 188h15" stroke="#70451a" stroke-width="2"/>
    <text x="118" y="170" font-family="monospace" font-size="8" fill="#fff7ca">nube 13</text>
    <path d="M124 154c7-12 20-9 21 4 9 0 13 12 4 18h-34c-8-7 0-20 9-22z" fill="#edf8ff" class="ink"/>
    <path d="M127 181l4 8 4-8M139 180l3 7 3-7" stroke="#4aa3ff" stroke-width="2"/>
    <rect x="254" y="176" width="31" height="35" rx="5" fill="#baf7ff" class="ink"/>
    <path d="M262 183l15 20M277 183l-15 20" stroke="#ff6b54" stroke-width="3"/>
    <text x="251" y="173" font-family="monospace" font-size="8" fill="#fff7ca">relámpago</text>
    <rect x="164" y="145" width="23" height="37" rx="4" fill="#ffe3f5" class="ink"/>
    <path d="M176 151v24M168 163h16M170 155l12 16M182 155l-12 16" stroke="#73c9ff" stroke-width="2"/>
    <rect x="219" y="145" width="25" height="37" rx="4" fill="#eaffc5" class="ink"/>
    <path d="M224 169c4-15 10-15 15 0" fill="none" stroke="#f25ca2" stroke-width="3"/>
    <path d="M224 169c4 8 11 8 15 0" fill="none" stroke="#ffcf4a" stroke-width="3"/>
  </g>
  <g class="s" transform="translate(0 -3)">
    <path d="M80 121c45-29 197-29 240 0" fill="none" stroke="#f5d66e" stroke-width="3" opacity=".75"/>
    <rect x="116" y="100" width="21" height="14" rx="3" fill="#ffcf4a" class="ink"/>
    <circle cx="121" cy="116" r="3" fill="#1a1731"/><circle cx="133" cy="116" r="3" fill="#1a1731"/>
    <path d="M145 100h19v14h-19z" fill="#7ee0ff" class="ink"/>
    <circle cx="150" cy="116" r="3" fill="#1a1731"/><circle cx="161" cy="116" r="3" fill="#1a1731"/>
    <path d="M174 100h17v14h-17z" fill="#ff8ba7" class="ink"/>
    <circle cx="179" cy="116" r="3" fill="#1a1731"/><circle cx="188" cy="116" r="3" fill="#1a1731"/>
    <path d="M197 91l8 8 11-5-5 11 8 8-12-1-6 10-3-12-12-3 10-6z" fill="#fff0a4" class="ink"/>
  </g>
  <g class="s">
    <path d="M197 57c-6-16 5-29 20-21 13 7 8 24-8 27" fill="none" stroke="#ffb86b" stroke-width="5"/>
    <path d="M205 59c2-10 12-9 15-3" fill="none" stroke="#ffe1a7" stroke-width="3"/>
    <circle cx="200" cy="63" r="7" fill="#ffcf4a" class="ink"/>
    <path d="M200 70v44" stroke="#ffcf4a" stroke-width="4"/>
  </g>
  <g class="s">
    <path d="M156 329c28 16 61 17 91 0" fill="none" stroke="#d8fbff" stroke-width="5"/>
    <rect x="119" y="326" width="162" height="22" rx="11" fill="#1d2542" stroke="#d8fbff" stroke-width="3"/>
    <text x="139" y="341" font-family="monospace" font-size="11" fill="#fff3a8">archivo de climas imposibles</text>
  </g>
  <g opacity=".75" filter="url(#glow)">
    <path d="M68 315c11-12 22-12 32 0 11-12 22-12 33 0" fill="none" stroke="#9cf7ff" stroke-width="2"/>
    <path d="M297 263c10-11 19-11 29 0 10-11 19-11 29 0" fill="none" stroke="#ffd1fa" stroke-width="2"/>
    <circle cx="91" cy="93" r="5" fill="none" stroke="#fff3a8" stroke-width="2"/>
    <circle cx="329" cy="206" r="7" fill="none" stroke="#9cf7ff" stroke-width="2"/>
  </g>
</svg>