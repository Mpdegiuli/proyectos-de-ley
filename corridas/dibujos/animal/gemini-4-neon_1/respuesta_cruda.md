<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0f1c2e"/>
      <stop offset="58%" stop-color="#1e3852"/>
      <stop offset="100%" stop-color="#2c4f63"/>
    </linearGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff6d6" stop-opacity="0.45"/>
      <stop offset="45%" stop-color="#f7d894" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#f7d894" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="moonGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fffbef"/>
      <stop offset="100%" stop-color="#f2cf8d"/>
    </linearGradient>
    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#224542"/>
      <stop offset="50%" stop-color="#183333"/>
      <stop offset="100%" stop-color="#102224"/>
    </linearGradient>
    <linearGradient id="furMain" x1="0.2" y1="0" x2="0.8" y2="1">
      <stop offset="0%" stop-color="#ff8c38"/>
      <stop offset="55%" stop-color="#e35d1b"/>
      <stop offset="100%" stop-color="#b53b0d"/>
    </linearGradient>
    <linearGradient id="furHead" x1="0.5" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="#ff9442"/>
      <stop offset="70%" stop-color="#e35d1b"/>
      <stop offset="100%" stop-color="#c44410"/>
    </linearGradient>
    <linearGradient id="furTail" x1="0.1" y1="0.8" x2="0.9" y2="0.1">
      <stop offset="0%" stop-color="#b53b0d"/>
      <stop offset="50%" stop-color="#e8621e"/>
      <stop offset="100%" stop-color="#ff8f3b"/>
    </linearGradient>
    <linearGradient id="furWhite" x1="0.5" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="#fffaf2"/>
      <stop offset="100%" stop-color="#dfd0c0"/>
    </linearGradient>
    <linearGradient id="furDark" x1="0.5" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="#3d2922"/>
      <stop offset="100%" stop-color="#1a1210"/>
    </linearGradient>
    <linearGradient id="earInner" x1="0.5" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="#f5c6b3"/>
      <stop offset="100%" stop-color="#c98070"/>
    </linearGradient>
    <clipPath id="tailClip">
      <path d="M 232 314 C 286 344 348 318 348 258 C 348 214 316 184 268 206 C 286 218 296 236 290 254 C 284 274 262 284 234 282 Z"/>
    </clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff8de" opacity="0.8">
    <circle cx="54" cy="48" r="1.4"/>
    <circle cx="96" cy="86" r="1"/>
    <circle cx="152" cy="42" r="1.2"/>
    <circle cx="212" cy="56" r="1.5"/>
    <circle cx="248" cy="36" r="1"/>
    <circle cx="355" cy="58" r="1.4"/>
    <circle cx="372" cy="128" r="1.1"/>
    <circle cx="42" cy="134" r="1.2"/>
    <circle cx="78" cy="176" r="1"/>
    <circle cx="338" cy="172" r="1"/>
    <path d="M 88 42 L 90 48 L 96 50 L 90 52 L 88 58 L 86 52 L 80 50 L 86 48 Z" opacity="0.7"/>
    <path d="M 258 98 L 259.5 102.5 L 264 104 L 259.5 105.5 L 258 110 L 256.5 105.5 L 252 104 L 256.5 102.5 Z" opacity="0.65"/>
  </g>

  <circle cx="308" cy="92" r="82" fill="url(#moonGlow)"/>
  <circle cx="308" cy="92" r="34" fill="url(#moonGrad)"/>
  <g fill="#e5be7a" opacity="0.35">
    <circle cx="297" cy="84" r="6"/>
    <circle cx="318" cy="102" r="8"/>
    <circle cx="316" cy="78" r="4"/>
  </g>

  <path d="M 0 286 Q 75 232 165 272 T 325 256 Q 368 248 400 264 L 400 330 L 0 330 Z" fill="#173040"/>
  <g fill="#122733">
    <path d="M 24 275 L 36 226 L 48 275 Z M 46 276 L 56 238 L 66 276 Z M 74 282 L 86 230 L 98 282 Z"/>
    <path d="M 326 272 L 338 220 L 350 272 Z M 352 276 L 364 232 L 376 276 Z M 374 278 L 385 242 L 396 278 Z"/>
  </g>
  <path d="M 0 308 Q 110 282 215 296 T 400 298 L 400 400 L 0 400 Z" fill="url(#ground)"/>

  <ellipse cx="204" cy="338" rx="92" ry="15" fill="#0d1c1d" opacity="0.68"/>

  <g id="tail">
    <path d="M 232 314 C 286 344 348 318 348 258 C 348 214 316 184 268 206 C 286 218 296 236 290 254 C 284 274 262 284 234 282 Z" fill="url(#furTail)"/>
    <path d="M 238 310 C 286 332 332 308 338 260 C 330 296 286 314 242 294 Z" fill="#992d08" opacity="0.38"/>
    <g clip-path="url(#tailClip)">
      <path d="M 260 185 L 348 185 L 352 238 L 332 226 L 320 242 L 304 224 L 290 240 L 278 222 L 260 226 Z" fill="url(#furWhite)"/>
      <path d="M 284 202 Q 312 198 334 224 Q 316 212 292 212 Z" fill="#ffffff" opacity="0.45"/>
    </g>
  </g>

  <g id="body">
    <path d="M 148 188 C 132 222 128 268 139 312 C 143 328 152 336 168 336 L 228 336 C 245 334 254 312 252 282 C 250 246 228 208 205 188 Z" fill="url(#furMain)"/>
    <path d="M 216 254 C 242 264 252 292 246 322 C 243 332 234 336 220 336 L 204 336 C 216 324 220 298 208 274 Z" fill="#c94612" opacity="0.55"/>
    <path d="M 205 322 C 218 320 232 322 238 332 C 239 336 234 339 224 339 L 204 339 Z" fill="url(#furDark)"/>
    <path d="M 152 190 C 145 216 147 252 158 276 L 166 270 L 172 288 L 178 276 L 185 288 L 192 272 L 198 276 C 208 250 209 216 202 190 Z" fill="url(#furWhite)"/>
    <path d="M 156 196 Q 177 210 198 196 Q 177 204 156 196 Z" fill="#c9b4a3" opacity="0.55"/>
  </g>

  <g id="frontLegs">
    <path d="M 152 250 C 150 278 152 308 154 334 C 154 338 158 340 165 340 L 172 340 C 175 340 176 336 175 332 C 173 306 174 278 176 254 Z" fill="url(#furMain)"/>
    <path d="M 152 292 C 153 310 153 324 154 334 C 154 338 158 340 165 340 L 172 340 C 175 340 176 336 175 332 C 174 318 174 304 174 292 L 168 298 L 162 292 L 157 297 Z" fill="url(#furDark)"/>
    <path d="M 181 254 C 183 278 184 306 182 332 C 181 336 182 340 185 340 L 192 340 C 199 340 203 338 203 334 C 205 308 207 278 205 250 Z" fill="url(#furMain)"/>
    <path d="M 183 292 C 183 304 183 318 182 332 C 181 336 182 340 185 340 L 192 340 C 199 340 203 338 203 334 C 204 324 204 310 205 292 L 199 297 L 194 292 L 188 298 Z" fill="url(#furDark)"/>
    <g stroke="#4a3730" stroke-width="1.2" stroke-linecap="round" opacity="0.65">
      <line x1="160" y1="336" x2="160" y2="339"/>
      <line x1="166" y1="336" x2="166" y2="339"/>
      <line x1="191" y1="336" x2="191" y2="339"/>
      <line x1="197" y1="336" x2="197" y2="339"/>
    </g>
  </g>

  <g id="head">
    <path d="M 132 136 Q 114 96 123 62 Q 152 76 168 115 Z" fill="url(#furHead)"/>
    <path d="M 123 62 Q 138 69 149 85 Q 134 86 121 91 Q 118 76 123 62 Z" fill="url(#furDark)"/>
    <path d="M 136 127 Q 126 98 131 78 Q 147 89 158 114 Z" fill="url(#earInner)"/>
    <path d="M 135 125 Q 139 112 146 116 Q 143 105 152 110 Q 150 120 144 128 Z" fill="#fff6eb" opacity="0.85"/>

    <path d="M 188 115 Q 204 76 233 62 Q 242 96 224 136 Z" fill="url(#furHead)"/>
    <path d="M 233 62 Q 238 76 235 91 Q 222 86 207 85 Q 218 69 233 62 Z" fill="url(#furDark)"/>
    <path d="M 198 114 Q 209 89 225 78 Q 230 98 220 127 Z" fill="url(#earInner)"/>
    <path d="M 221 125 Q 217 112 210 116 Q 213 105 204 110 Q 206 120 212 128 Z" fill="#fff6eb" opacity="0.85"/>

    <path d="M 178 109 C 204 109 224 125 228 145 C 236 151 244 157 240 164 C 234 169 226 171 219 175 C 206 188 191 201 178 202 C 165 201 150 188 137 175 C 130 171 122 169 116 164 C 112 157 120 151 128 145 C 132 125 152 109 178 109 Z" fill="url(#furHead)"/>
    <path d="M 178 114 C 194 114 208 124 212 138 C 199 128 188 124 178 124 C 168 124 157 128 144 138 C 148 124 162 114 178 114 Z" fill="#ffa85c" opacity="0.4"/>

    <path d="M 122 156 C 141 154 156 167 166 181 C 172 188 184 188 190 181 C 200 167 215 154 234 156 C 240 159 242 163 238 167 C 230 172 222 173 216 178 C 204 190 190 202 178 202 C 166 202 152 190 140 178 C 134 173 126 172 118 167 C 114 163 116 159 122 156 Z" fill="url(#furWhite)"/>

    <path d="M 167 164 C 169 176 172 184 178 186 C 184 184 187 176 189 164 C 183 166 173 166 167 164 Z" fill="#ff8e3c" opacity="0.45"/>

    <g id="eyes">
      <ellipse cx="154" cy="157" rx="8.5" ry="9" fill="#1e1411"/>
      <ellipse cx="154" cy="158" rx="6.2" ry="6.5" fill="#9c4c19"/>
      <circle cx="154.5" cy="157.5" r="4.6" fill="#140d0b"/>
      <circle cx="151.8" cy="154.2" r="2.4" fill="#ffffff"/>
      <circle cx="157" cy="160.2" r="1.1" fill="#ffffff" opacity="0.85"/>
      <path d="M 145 145 Q 153 141 160 144" fill="none" stroke="#ffbd7a" stroke-width="2" stroke-linecap="round" opacity="0.75"/>

      <ellipse cx="202" cy="157" rx="8.5" ry="9" fill="#1e1411"/>
      <ellipse cx="202" cy="158" rx="6.2" ry="6.5" fill="#9c4c19"/>
      <circle cx="201.5" cy="157.5" r="4.6" fill="#140d0b"/>
      <circle cx="199.2" cy="154.2" r="2.4" fill="#ffffff"/>
      <circle cx="204.4" cy="160.2" r="1.1" fill="#ffffff" opacity="0.85"/>
      <path d="M 196 144 Q 203 141 211 145" fill="none" stroke="#ffbd7a" stroke-width="2" stroke-linecap="round" opacity="0.75"/>
    </g>

    <path d="M 169 184 Q 178 180 187 184 Q 186 192 178 194 Q 170 192 169 184 Z" fill="#1c1412"/>
    <ellipse cx="176" cy="185.5" rx="3.2" ry="1.5" fill="#5e4b46" opacity="0.8"/>
    <path d="M 178 194 L 178 197 M 171 196 Q 174.5 199.5 178 197 Q 181.5 199.5 185 196" fill="none" stroke="#36241e" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <g fill="#2b5752">
    <path d="M 48 345 Q 42 325 32 316 Q 46 322 54 345 Z"/>
    <path d="M 55 347 Q 58 322 68 310 Q 62 328 62 347 Z"/>
    <path d="M 62 348 Q 70 330 82 324 Q 72 336 68 348 Z"/>
    <path d="M 320 344 Q 326 324 338 314 Q 332 330 327 344 Z"/>
    <path d="M 332 346 Q 344 328 358 320 Q 346 336 338 346 Z"/>
    <path d="M 314 344 Q 308 328 298 322 Q 308 334 310 344 Z"/>
  </g>

  <g fill="#ffe885">
    <circle cx="96" cy="252" r="2.2" opacity="0.85"/>
    <circle cx="96" cy="252" r="6" opacity="0.22"/>
    <circle cx="272" cy="158" r="1.8" opacity="0.8"/>
    <circle cx="272" cy="158" r="5" opacity="0.2"/>
    <circle cx="118" cy="298" r="1.5" opacity="0.7"/>
    <circle cx="118" cy="298" r="4.5" opacity="0.18"/>
    <circle cx="356" cy="242" r="1.8" opacity="0.75"/>
    <circle cx="356" cy="242" r="5" opacity="0.18"/>
  </g>
</svg>