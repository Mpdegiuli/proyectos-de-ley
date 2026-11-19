<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="sky" cx="45%" cy="38%" r="72%">
      <stop offset="0%" stop-color="#1e2d5a"/>
      <stop offset="55%" stop-color="#101836"/>
      <stop offset="100%" stop-color="#070b1a"/>
    </radialGradient>
    <radialGradient id="aura" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#56cfe1" stop-opacity="0.32"/>
      <stop offset="60%" stop-color="#7400b8" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#070b1a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bodyG" x1="20%" y1="10%" x2="85%" y2="95%">
      <stop offset="0%" stop-color="#72efdd"/>
      <stop offset="35%" stop-color="#4ea8de"/>
      <stop offset="75%" stop-color="#483d8b"/>
      <stop offset="100%" stop-color="#241b4e"/>
    </linearGradient>
    <linearGradient id="headG" x1="15%" y1="15%" x2="85%" y2="85%">
      <stop offset="0%" stop-color="#80ffdb"/>
      <stop offset="45%" stop-color="#5390d9"/>
      <stop offset="100%" stop-color="#3a2d73"/>
    </linearGradient>
    <linearGradient id="chestG" x1="30%" y1="0%" x2="70%" y2="100%">
      <stop offset="0%" stop-color="#f0fffc"/>
      <stop offset="55%" stop-color="#a8f9ff"/>
      <stop offset="100%" stop-color="#5e60ce"/>
    </linearGradient>
    <linearGradient id="wing1" x1="0%" y1="90%" x2="100%" y2="10%">
      <stop offset="0%" stop-color="#5e60ce" stop-opacity="0.88"/>
      <stop offset="48%" stop-color="#b5179e" stop-opacity="0.72"/>
      <stop offset="82%" stop-color="#48bfe3" stop-opacity="0.82"/>
      <stop offset="100%" stop-color="#80ffdb" stop-opacity="0.92"/>
    </linearGradient>
    <linearGradient id="wing2" x1="0%" y1="100%" x2="90%" y2="0%">
      <stop offset="0%" stop-color="#3a0ca3" stop-opacity="0.82"/>
      <stop offset="55%" stop-color="#7209b7" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#4cc9f0" stop-opacity="0.78"/>
    </linearGradient>
    <linearGradient id="tailG" x1="0%" y1="60%" x2="100%" y2="20%">
      <stop offset="0%" stop-color="#483d8b"/>
      <stop offset="45%" stop-color="#48bfe3"/>
      <stop offset="80%" stop-color="#c77dff"/>
      <stop offset="100%" stop-color="#ffe66d"/>
    </linearGradient>
    <linearGradient id="frillG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff9ebb"/>
      <stop offset="55%" stop-color="#c77dff"/>
      <stop offset="100%" stop-color="#48bfe3"/>
    </linearGradient>
    <linearGradient id="rockG" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" stop-color="#222a4a"/>
      <stop offset="35%" stop-color="#141930"/>
      <stop offset="100%" stop-color="#090c1a"/>
    </linearGradient>
    <radialGradient id="eyeG" cx="42%" cy="38%" r="58%">
      <stop offset="0%" stop-color="#19123b"/>
      <stop offset="68%" stop-color="#291d5c"/>
      <stop offset="100%" stop-color="#64dfdf"/>
    </radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="7"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="220" cy="205" r="155" fill="url(#aura)"/>

  <g fill="#e0fbfc" opacity="0.75">
    <circle cx="38" cy="36" r="1.2"/><circle cx="128" cy="32" r="1.5"/><circle cx="195" cy="48" r="1"/>
    <circle cx="255" cy="28" r="1.4"/><circle cx="348" cy="42" r="1.6"/><circle cx="372" cy="86" r="1.1"/>
    <circle cx="48" cy="148" r="1.2"/><circle cx="28" cy="212" r="1.4"/><circle cx="72" cy="255" r="1"/>
    <circle cx="374" cy="182" r="1.3"/><circle cx="352" cy="312" r="1.1"/><circle cx="152" cy="64" r="0.9"/>
    <path d="M322 60 l2 6 6 2-6 2-2 6-2-6-6-2 6-2z" fill="#ffe66d" opacity="0.85"/>
    <path d="M58 188 l1.5 4.5 4.5 1.5-4.5 1.5-1.5 4.5-1.5-4.5-4.5-1.5 4.5-1.5z" fill="#80ffdb" opacity="0.8"/>
  </g>

  <circle cx="66" cy="68" r="34" fill="#ffe66d" opacity="0.16" filter="url(#soft)"/>
  <path d="M68 42 A26 26 0 1 0 90 80 A21 21 0 1 1 68 42 Z" fill="#fff3b0" filter="url(#glow)"/>

  <g id="back-wing">
    <path d="M206 196 C198 140 226 84 274 62 C292 54 304 68 296 92 C288 118 298 134 282 158 C264 184 236 198 212 204 Z" fill="url(#wing2)" stroke="#80ffdb" stroke-width="1" stroke-opacity="0.5"/>
    <path d="M210 194 C228 148 256 106 286 76 M212 196 C240 162 268 134 286 116 M214 198 C242 180 264 166 278 150" stroke="#a8f9ff" stroke-width="0.9" stroke-opacity="0.45" fill="none"/>
    <circle cx="268" cy="96" r="9" fill="#1b1440" fill-opacity="0.65" stroke="#ffe66d" stroke-width="1.3"/>
    <circle cx="268" cy="96" r="4" fill="#64dfdf" filter="url(#glow)"/>
  </g>

  <g id="tail">
    <path d="M245 282 C288 308 338 304 358 264 C374 232 354 198 326 206 C306 212 308 236 326 238 C340 240 344 224 334 220" fill="none" stroke="url(#tailG)" stroke-width="10" stroke-linecap="round"/>
    <path d="M250 286 C296 328 362 324 374 272 C382 238 362 194 328 198 C354 204 364 234 352 262 C336 298 288 304 248 282 Z" fill="url(#tailG)" opacity="0.52"/>
    <path d="M262 294 C308 338 370 336 382 288 C362 316 314 316 268 290 Z" fill="#80ffdb" opacity="0.32"/>
    <path d="M326 206 C312 188 292 196 296 216 C302 204 316 206 324 214 Z" fill="#ffe66d" opacity="0.72" filter="url(#glow)"/>
    <circle cx="348" cy="274" r="2.2" fill="#ffe66d" filter="url(#glow)"/>
    <circle cx="364" cy="242" r="2" fill="#80ffdb" filter="url(#glow)"/>
    <circle cx="316" cy="302" r="2.3" fill="#ff9ebb" filter="url(#glow)"/>
  </g>

  <g id="ground">
    <path d="M25 400 Q58 318 195 312 Q335 306 385 400 Z" fill="url(#rockG)"/>
    <path d="M62 346 Q135 314 218 313 Q292 313 344 342 Q278 326 198 328 Q120 330 62 346 Z" fill="#2a9d8f" opacity="0.45"/>
    <ellipse cx="204" cy="322" rx="64" ry="10" fill="#070a18" opacity="0.7"/>
  </g>

  <g id="creature-body">
    <path d="M174 244 C166 274 162 296 156 318 C154 323 164 325 170 322 C173 320 174 312 175 302 C179 282 186 266 192 248 Z" fill="#322a66"/>
    <path d="M224 276 C230 296 236 308 228 318 C222 325 244 326 250 318 C256 310 256 286 248 268 Z" fill="#2e255e"/>
    <path d="M172 192 C202 188 232 206 248 238 C264 270 264 306 242 318 C224 328 198 320 190 302 C180 282 174 260 166 236 C160 218 162 198 172 192 Z" fill="url(#bodyG)"/>
    <path d="M196 248 C194 276 192 298 188 320 C187 325 198 327 204 323 C207 320 207 312 208 300 C210 278 214 262 216 246 Z" fill="url(#bodyG)"/>
    <g fill="#80ffdb" opacity="0.8" filter="url(#glow)">
      <ellipse cx="222" cy="248" rx="4.5" ry="2.2" transform="rotate(-24 222 248)"/>
      <ellipse cx="234" cy="264" rx="5.5" ry="2.5" transform="rotate(-16 234 264)"/>
      <ellipse cx="238" cy="282" rx="4" ry="2" transform="rotate(-8 238 282)"/>
      <circle cx="160" cy="321" r="1.6"/><circle cx="192" cy="323" r="1.7"/><circle cx="235" cy="321" r="1.6"/>
    </g>

    <g id="neck-frills">
      <path d="M156 186 C136 188 124 202 132 212 C142 206 152 204 162 202 Z" fill="url(#frillG)" opacity="0.85"/>
      <path d="M162 194 C140 204 134 222 146 228 C156 218 164 212 172 208 Z" fill="url(#frillG)" opacity="0.9"/>
      <path d="M196 188 C216 192 226 206 216 216 C206 208 198 206 190 204 Z" fill="url(#frillG)" opacity="0.85"/>
      <path d="M188 196 C208 206 214 224 202 230 C192 220 186 214 178 208 Z" fill="url(#frillG)" opacity="0.9"/>
    </g>

    <path d="M162 202 C158 226 168 250 184 262 C198 250 206 230 200 206 C190 214 184 208 180 200 C174 208 168 208 162 202 Z" fill="url(#chestG)"/>
    <path d="M172 214 C172 232 178 244 184 252 C190 242 194 228 192 214" fill="none" stroke="#ffffff" stroke-width="1.3" stroke-opacity="0.65" stroke-linecap="round"/>
  </g>

  <g id="head-group">
    <path d="M158 142 C148 118 148 96 160 88 C170 98 176 120 176 144 Z" fill="#3a2d73"/>
    <path d="M160 138 C154 120 155 104 161 97 C167 106 171 122 170 138 Z" fill="#ff9ebb" opacity="0.72"/>

    <g id="antennae" fill="none" stroke-linecap="round">
      <path d="M150 144 C138 112 114 90 90 96 C78 99 78 112 88 114" stroke="#80ffdb" stroke-width="2.2"/>
      <path d="M140 124 L126 118 M132 114 L118 106 M122 104 L110 94 M110 98 L100 86 M98 96 L92 84 M134 126 L124 134 M122 114 L112 122 M108 104 L102 114" stroke="#a8f9ff" stroke-width="1.2" opacity="0.85"/>
      <circle cx="88" cy="114" r="3.2" fill="#ffe66d" stroke="none" filter="url(#glow)"/>

      <path d="M164 138 C154 102 132 72 104 72 C90 72 86 84 96 89" stroke="#80ffdb" stroke-width="2.4"/>
      <path d="M156 116 L142 108 M148 102 L134 92 M138 88 L126 76 M124 78 L116 66 M110 73 L104 62 M150 116 L140 124 M138 100 L128 108 M124 86 L116 96" stroke="#c77dff" stroke-width="1.3" opacity="0.9"/>
      <circle cx="96" cy="89" r="3.6" fill="#80ffdb" stroke="none" filter="url(#glow)"/>
    </g>

    <path d="M180 148 C196 124 214 106 226 106 C224 124 212 146 194 166 Z" fill="url(#headG)"/>
    <path d="M186 150 C198 132 210 118 219 116 C216 130 206 146 192 158 Z" fill="#ff9ebb" opacity="0.8"/>

    <path d="M156 138 C178 136 196 152 198 172 C200 188 188 202 170 202 C154 202 142 196 132 188 C124 184 120 179 124 173 C130 165 138 158 144 148 C148 141 151 138 156 138 Z" fill="url(#headG)"/>
    <path d="M126 177 C134 186 152 198 172 198 C184 198 192 190 194 180 C184 190 164 192 146 184 Z" fill="#e0fbfc" opacity="0.65"/>

    <path d="M144 149 L148 155 L144 161 L140 155 Z" fill="#ffe66d" filter="url(#glow)"/>
    <circle cx="144" cy="155" r="1.4" fill="#ffffff"/>

    <g id="eye">
      <ellipse cx="158" cy="168" rx="11.5" ry="12.5" transform="rotate(-8 158 168)" fill="url(#eyeG)"/>
      <path d="M147 166 C150 156 164 154 170 163" fill="none" stroke="#100b29" stroke-width="2.6" stroke-linecap="round"/>
      <ellipse cx="157" cy="167" rx="5.5" ry="7" fill="#0b0820"/>
      <circle cx="153" cy="162" r="3.4" fill="#ffffff"/>
      <circle cx="162" cy="172" r="1.6" fill="#80ffdb"/>
      <path d="M150 174 C155 178 162 178 166 174" fill="none" stroke="#80ffdb" stroke-width="1.3" opacity="0.85"/>
    </g>

    <path d="M123 175 C124 172 128 172 129 175 C128 177 125 178 123 175 Z" fill="#231942"/>
    <path d="M126 178 C128 183 135 184 140 181" fill="none" stroke="#231942" stroke-width="1.5" stroke-linecap="round"/>
    <g fill="#ffe66d" opacity="0.9" filter="url(#glow)">
      <circle cx="174" cy="178" r="1.6"/><circle cx="180" cy="182" r="1.3"/><circle cx="170" cy="184" r="1.1"/>
    </g>
  </g>

  <g id="hero-wing">
    <path d="M210 202 C226 154 274 106 346 98 C368 96 376 114 362 136 C348 158 358 174 338 190 C322 202 308 200 296 204 C316 214 318 238 296 250 C272 264 238 244 214 218 Z" fill="url(#wing1)" stroke="#a8f9ff" stroke-width="1.3" stroke-opacity="0.75"/>
    <g stroke="#e0fbfc" stroke-width="1" stroke-opacity="0.55" fill="none">
      <path d="M214 204 C252 166 298 134 356 112"/>
      <path d="M216 206 C262 178 308 158 350 148"/>
      <path d="M216 208 C264 196 306 188 338 184"/>
      <path d="M216 212 C252 218 282 228 298 242"/>
    </g>
    <circle cx="318" cy="140" r="14" fill="#181038" fill-opacity="0.72" stroke="#ffe66d" stroke-width="1.8"/>
    <circle cx="318" cy="140" r="7.5" fill="#4cc9f0" filter="url(#glow)"/>
    <circle cx="315" cy="137" r="2.6" fill="#ffffff"/>
    <circle cx="282" cy="228" r="9.5" fill="#181038" fill-opacity="0.7" stroke="#ff9ebb" stroke-width="1.5"/>
    <circle cx="282" cy="228" r="4.5" fill="#ffe66d" filter="url(#glow)"/>
    <path d="M354 106 C358 112 356 120 350 126" fill="none" stroke="#ffe66d" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>
  </g>

  <g id="foreground-flora">
    <path d="M104 334 Q102 318 106 308" stroke="#64dfdf" stroke-width="2" fill="none"/>
    <path d="M94 312 Q106 294 118 312 Q106 316 94 312 Z" fill="#80ffdb" filter="url(#glow)"/>
    <path d="M122 332 Q124 322 122 316" stroke="#64dfdf" stroke-width="1.6" fill="none"/>
    <path d="M114 318 Q122 308 130 318 Q122 321 114 318 Z" fill="#c77dff" filter="url(#glow)"/>
    <path d="M286 334 Q288 320 284 312" stroke="#64dfdf" stroke-width="1.8" fill="none"/>
    <path d="M275 315 Q284 302 294 315 Q284 318 275 315 Z" fill="#ffe66d" filter="url(#glow)"/>
    <g stroke="#2a9d8f" stroke-width="1.8" fill="none" stroke-linecap="round">
      <path d="M84 344 Q78 326 68 320"/><path d="M90 342 Q90 326 94 318"/>
      <path d="M298 338 Q306 322 316 318"/><path d="M306 342 Q314 330 324 328"/>
    </g>
  </g>

  <g id="spores" filter="url(#glow)">
    <circle cx="96" cy="142" r="2.4" fill="#ffe66d"/>
    <circle cx="118" cy="248" r="2.2" fill="#80ffdb"/>
    <circle cx="136" cy="278" r="1.6" fill="#c77dff"/>
    <circle cx="234" cy="96" r="2.2" fill="#ffe66d"/>
    <circle cx="332" cy="82" r="2.5" fill="#80ffdb"/>
    <circle cx="368" cy="166" r="2" fill="#ff9ebb"/>
    <circle cx="294" cy="276" r="2.3" fill="#80ffdb"/>
    <circle cx="268" cy="348" r="1.8" fill="#ffe66d"/>
    <circle cx="148" cy="350" r="1.6" fill="#80ffdb"/>
  </g>
</svg>