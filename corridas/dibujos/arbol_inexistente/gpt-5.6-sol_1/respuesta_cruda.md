<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="72%">
      <stop offset="0" stop-color="#182b46"/>
      <stop offset=".55" stop-color="#091524"/>
      <stop offset="1" stop-color="#03070e"/>
    </radialGradient>
    <linearGradient id="trunk" x1="0" y1="1" x2=".7" y2="0">
      <stop stop-color="#402757"/>
      <stop offset=".45" stop-color="#8c4f83"/>
      <stop offset=".72" stop-color="#cf8ba0"/>
      <stop offset="1" stop-color="#ffd2ba"/>
    </linearGradient>
    <linearGradient id="branch" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#7d477c"/>
      <stop offset="1" stop-color="#ffc2ad"/>
    </linearGradient>
    <radialGradient id="orb">
      <stop offset="0" stop-color="#fffbd1"/>
      <stop offset=".25" stop-color="#9fffe9"/>
      <stop offset=".65" stop-color="#40c2cf"/>
      <stop offset="1" stop-color="#3362a8"/>
    </radialGradient>
    <linearGradient id="leaf" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#d7fff0"/>
      <stop offset=".35" stop-color="#7cf4d3"/>
      <stop offset="1" stop-color="#586ed7"/>
    </linearGradient>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <ellipse cx="200" cy="343" rx="119" ry="22" fill="#3dd9c2" opacity=".12" filter="url(#soft)"/>
  <g fill="#9fffe9">
    <circle cx="44" cy="82" r="1.2"/><circle cx="82" cy="42" r=".8"/><circle cx="139" cy="69" r="1"/>
    <circle cx="215" cy="31" r="1.2"/><circle cx="278" cy="58" r=".7"/><circle cx="347" cy="44" r="1.1"/>
    <circle cx="370" cy="116" r=".8"/><circle cx="31" cy="173" r=".7"/><circle cx="356" cy="212" r="1.2"/>
    <circle cx="64" cy="264" r="1"/><circle cx="328" cy="294" r=".8"/>
  </g>

  <path d="M79 335 Q126 304 170 333T321 331" fill="none" stroke="#61e8d2" stroke-width="1" opacity=".35"/>
  <path d="M103 345 Q155 318 203 345T297 342" fill="none" stroke="#896fe0" stroke-width="2" opacity=".35"/>

  <g fill="none" stroke-linecap="round">
    <path d="M199 340 C178 319 169 301 180 278 C195 246 194 220 181 190 C169 164 180 137 204 119 C222 105 225 83 214 62" stroke="url(#trunk)" stroke-width="24"/>
    <path d="M199 340 C178 319 169 301 180 278 C195 246 194 220 181 190 C169 164 180 137 204 119 C222 105 225 83 214 62" stroke="#ffd8c3" stroke-width="3" opacity=".55"/>

    <path d="M185 273 C149 267 126 249 111 220" stroke="url(#branch)" stroke-width="11"/>
    <path d="M113 222 C95 211 79 193 73 174" stroke="url(#branch)" stroke-width="6"/>
    <path d="M127 238 C105 241 86 235 70 224" stroke="url(#branch)" stroke-width="5"/>

    <path d="M190 233 C226 228 253 209 270 180" stroke="url(#branch)" stroke-width="10"/>
    <path d="M265 188 C291 182 311 166 324 145" stroke="url(#branch)" stroke-width="6"/>
    <path d="M245 215 C272 220 297 215 315 201" stroke="url(#branch)" stroke-width="5"/>

    <path d="M180 190 C146 181 125 161 114 137" stroke="url(#branch)" stroke-width="9"/>
    <path d="M130 153 C103 150 83 137 69 120" stroke="url(#branch)" stroke-width="5"/>
    <path d="M186 158 C218 156 243 139 257 113" stroke="url(#branch)" stroke-width="8"/>
    <path d="M247 128 C274 130 296 121 312 104" stroke="url(#branch)" stroke-width="5"/>

    <path d="M204 119 C180 105 165 86 160 64" stroke="url(#branch)" stroke-width="7"/>
    <path d="M216 91 C238 85 254 72 264 54" stroke="url(#branch)" stroke-width="6"/>
  </g>

  <g fill="url(#leaf)" stroke="#baffee" stroke-width="1">
    <path d="M66 177 C49 161 52 145 76 151 C91 155 91 169 66 177Z"/>
    <path d="M68 225 C50 219 47 205 66 202 C83 200 89 215 68 225Z"/>
    <path d="M108 220 C92 207 96 193 115 198 C130 203 127 216 108 220Z"/>
    <path d="M67 121 C48 113 47 97 68 99 C87 101 88 114 67 121Z"/>
    <path d="M113 137 C96 125 101 109 121 115 C136 120 133 133 113 137Z"/>
    <path d="M158 65 C145 50 152 36 169 45 C182 53 177 64 158 65Z"/>
    <path d="M214 62 C201 46 209 31 226 41 C238 49 232 61 214 62Z"/>
    <path d="M264 55 C263 36 278 29 287 47 C293 61 280 67 264 55Z"/>
    <path d="M258 114 C258 95 273 88 283 106 C290 120 276 128 258 114Z"/>
    <path d="M312 105 C314 86 330 81 337 100 C342 116 328 121 312 105Z"/>
    <path d="M323 146 C329 127 345 126 348 146 C350 162 335 165 323 146Z"/>
    <path d="M315 202 C326 184 342 189 339 208 C336 224 321 220 315 202Z"/>
    <path d="M270 181 C273 162 289 158 295 177 C299 192 285 198 270 181Z"/>
  </g>

  <g filter="url(#glow)">
    <circle cx="75" cy="151" r="5" fill="url(#orb)"/>
    <circle cx="111" cy="198" r="4" fill="url(#orb)"/>
    <circle cx="69" cy="99" r="4" fill="url(#orb)"/>
    <circle cx="121" cy="114" r="5" fill="url(#orb)"/>
    <circle cx="169" cy="44" r="4" fill="url(#orb)"/>
    <circle cx="226" cy="40" r="5" fill="url(#orb)"/>
    <circle cx="287" cy="47" r="4" fill="url(#orb)"/>
    <circle cx="283" cy="106" r="5" fill="url(#orb)"/>
    <circle cx="337" cy="100" r="4" fill="url(#orb)"/>
    <circle cx="348" cy="146" r="5" fill="url(#orb)"/>
    <circle cx="339" cy="208" r="4" fill="url(#orb)"/>
  </g>

  <g fill="none" stroke="#8effe5" opacity=".75">
    <ellipse cx="207" cy="165" rx="122" ry="36" transform="rotate(-18 207 165)" stroke-width="1.4" stroke-dasharray="2 7"/>
    <ellipse cx="200" cy="207" rx="151" ry="57" transform="rotate(12 200 207)" stroke-width=".8" stroke-dasharray="1 10"/>
  </g>
  <g fill="#ecfff9">
    <circle cx="94" cy="190" r="3"/><circle cx="303" cy="119" r="2.5"/>
    <circle cx="342" cy="229" r="2"/><circle cx="65" cy="166" r="2"/>
  </g>

  <path d="M199 337 C190 351 174 360 153 366 C177 368 191 363 203 353 C213 366 231 371 250 366 C231 360 218 350 211 337Z" fill="#624274"/>
  <path d="M191 342 C170 342 150 350 134 362 M208 343 C229 344 249 352 266 363" fill="none" stroke="#bf78a2" stroke-width="5" stroke-linecap="round"/>
</svg>