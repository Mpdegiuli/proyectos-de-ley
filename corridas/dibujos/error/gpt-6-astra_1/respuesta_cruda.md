<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <pattern id="lino" width="7" height="7" patternUnits="userSpaceOnUse">
      <path d="M0 1H7M1 0V7" fill="none" stroke="#c7b99b" stroke-width=".45" opacity=".35"/>
    </pattern>
    <pattern id="puntos" width="29" height="27" patternUnits="userSpaceOnUse">
      <path d="M9 8l10 11m0-11L9 19" fill="none" stroke="#355b60" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M9 8l10 11" fill="none" stroke="#76918a" stroke-width=".65"/>
    </pattern>
    <clipPath id="tela">
      <path d="M42 210Q119 200 200 209T356 208L348 334Q269 343 195 335T47 337Z"/>
    </clipPath>
    <mask id="falta">
      <rect width="400" height="400" fill="white"/>
      <ellipse cx="188" cy="256" rx="15" ry="16" fill="black"/>
    </mask>
    <g id="petalo">
      <path d="M232 114C217 104 209 80 218 67C227 54 241 61 246 74C251 88 241 106 232 114Z" fill="#db4a36"/>
      <path d="M230 104Q225 85 229 71" fill="none" stroke="#f68b59" stroke-width="1.5" stroke-linecap="round"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="#f3eddf"/>
  <path d="M22 22h16M22 22v16M378 22h-16M378 22v16M22 378h16M22 378v-16M378 378h-16M378 378v-16" fill="none" stroke="#b5ac96" stroke-width="1"/>
  <text x="43" y="48" fill="#355b60" font-family="monospace" font-size="10" letter-spacing="2">01 / ERROR FÉRTIL</text>

  <path d="M47 219Q130 208 202 217T359 216L352 341Q269 351 194 343T49 345Z" fill="#454c3d" opacity=".1"/>
  <path d="M42 210Q119 200 200 209T356 208L348 334Q269 343 195 335T47 337Z" fill="#e8dcc0"/>
  <g clip-path="url(#tela)">
    <rect x="40" y="200" width="320" height="150" fill="url(#lino)"/>
    <rect x="55" y="217" width="289" height="109" fill="url(#puntos)" mask="url(#falta)"/>
    <path d="M43 216Q120 206 199 215T355 214M47 330Q121 322 196 329T349 328" fill="none" stroke="#a99876" stroke-width="1" stroke-dasharray="3 4"/>
  </g>

  <g fill="none" stroke="#b4a482" stroke-width=".8">
    <path d="M47 337l-1 7m8-8v5m8-7l1 9m7-10v7m8-8l1 7m9-8v7m9-8l-1 7m10-7l1 6m10-6v8m10-8l1 5m10-5v8m11-7v6m12-5v6m11-5l1 6m12-5v5m12-4v7m12-6v5m13-5v7m12-7v6m13-7v7m12-8v6m12-7v6m12-7l1 6m12-7v7m12-8v6m12-7v5"/>
  </g>

  <path d="M183 251l10 11m0-11l-10 11" fill="none" stroke="#9c9c87" stroke-width="1" stroke-dasharray="2 3"/>
  <ellipse cx="183" cy="251" rx="2.5" ry="1.7" fill="#514d3c"/>
  <ellipse cx="193" cy="261" rx="2.5" ry="1.7" fill="#514d3c"/>

  <path d="M193 261C209 285 251 277 253 252C255 227 226 222 212 235C199 249 215 263 227 252" fill="none" stroke="#a4352c" stroke-width="3.3" stroke-linecap="round" opacity=".15" transform="translate(1 2)"/>
  <path d="M193 261C209 285 251 277 253 252C255 227 226 222 212 235C199 249 215 263 227 252" fill="none" stroke="#d94a36" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M183 251C164 230 182 218 199 210C227 196 232 179 231 146" fill="none" stroke="#d94a36" stroke-width="3" stroke-linecap="round"/>
  <path d="M183 251C164 230 182 218 199 210C227 196 232 179 231 146" fill="none" stroke="#fa9670" stroke-width=".7" stroke-linecap="round"/>

  <path d="M222 187C197 188 180 175 176 154C200 153 218 164 222 187Z" fill="#355b60"/>
  <path d="M222 187Q199 171 184 161" fill="none" stroke="#b2c1a4" stroke-width="1.2"/>
  <path d="M229 170C232 148 251 139 270 143C264 163 249 173 229 170Z" fill="#5f8272"/>
  <path d="M229 170Q248 154 262 148" fill="none" stroke="#c4ceb0" stroke-width="1.2"/>

  <use href="#petalo"/>
  <use href="#petalo" transform="rotate(45 232 114)"/>
  <use href="#petalo" transform="rotate(90 232 114)"/>
  <use href="#petalo" transform="rotate(135 232 114)"/>
  <use href="#petalo" transform="rotate(180 232 114)"/>
  <use href="#petalo" transform="rotate(225 232 114)"/>
  <use href="#petalo" transform="rotate(270 232 114)"/>
  <use href="#petalo" transform="rotate(315 232 114)"/>
  <circle cx="232" cy="114" r="20" fill="#edb744"/>
  <circle cx="232" cy="114" r="14" fill="#355b60"/>
  <g fill="#f3d483">
    <circle cx="226" cy="107" r="1.6"/>
    <circle cx="234" cy="104" r="1.5"/>
    <circle cx="240" cy="111" r="1.7"/>
    <circle cx="232" cy="113" r="1.6"/>
    <circle cx="223" cy="116" r="1.5"/>
    <circle cx="229" cy="122" r="1.7"/>
    <circle cx="238" cy="120" r="1.5"/>
  </g>

  <path d="M111 115q9-9 18 0q-9 9-18 0Z" fill="#edb744" transform="rotate(-28 120 115)"/>
  <path d="M118 120q3 8-3 15" fill="none" stroke="#a99876" stroke-width="1" stroke-dasharray="2 4"/>
  <path d="M306 174l4 4m0-4l-4 4" fill="none" stroke="#d94a36" stroke-width="1.5" stroke-linecap="round"/>

  <text x="200" y="373" text-anchor="middle" fill="#355b60" font-family="Georgia,serif" font-size="16" font-style="italic">Se escapó un punto. Lo dejé crecer.</text>
</svg>