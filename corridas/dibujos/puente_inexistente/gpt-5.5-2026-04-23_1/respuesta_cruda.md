<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#120b2f"/>
      <stop offset="0.55" stop-color="#1d3b73"/>
      <stop offset="1" stop-color="#87d7c7"/>
    </linearGradient>
    <linearGradient id="road" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ffd36a"/>
      <stop offset="0.45" stop-color="#f85fa3"/>
      <stop offset="1" stop-color="#55f4ff"/>
    </linearGradient>
    <linearGradient id="stone" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f5e7ff"/>
      <stop offset="1" stop-color="#5d7cff"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#fff8b8" stop-opacity="1"/>
      <stop offset="0.45" stop-color="#9cf6ff" stop-opacity=".65"/>
      <stop offset="1" stop-color="#9cf6ff" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="322" cy="65" r="42" fill="url(#glow)"/>
  <circle cx="96" cy="83" r="3" fill="#fff"/>
  <circle cx="154" cy="35" r="2" fill="#fff"/>
  <circle cx="258" cy="28" r="2.5" fill="#fff"/>
  <circle cx="347" cy="128" r="2" fill="#fff"/>
  <circle cx="51" cy="142" r="2" fill="#fff"/>

  <path d="M0 310 C55 284 88 315 139 292 C191 269 236 302 282 282 C333 260 366 286 400 268 L400 400 L0 400 Z" fill="#15345e"/>
  <path d="M0 330 C58 311 99 337 147 319 C206 297 245 333 300 306 C340 288 366 307 400 297 L400 400 L0 400 Z" fill="#0b203f"/>
  <path d="M21 351 C92 330 154 365 223 341 C286 319 337 348 396 326" fill="none" stroke="#67ffdf" stroke-opacity=".35" stroke-width="2"/>

  <ellipse cx="68" cy="277" rx="64" ry="18" fill="#07243d" opacity=".55"/>
  <ellipse cx="333" cy="252" rx="58" ry="15" fill="#07243d" opacity=".55"/>

  <path d="M24 278 C42 236 61 225 79 187 C90 164 101 149 114 166 C132 188 115 224 133 250 C147 270 116 286 79 290 C53 293 33 290 24 278 Z" fill="url(#stone)"/>
  <path d="M286 251 C305 211 313 183 337 153 C350 137 363 148 367 171 C373 206 390 222 382 248 C375 270 338 269 310 265 C292 262 282 259 286 251 Z" fill="url(#stone)"/>
  <path d="M74 252 L111 161 L126 259 Z" fill="#fff" opacity=".15"/>
  <path d="M331 236 L349 152 L364 250 Z" fill="#fff" opacity=".16"/>

  <path d="M62 247 C117 121 272 100 344 221" fill="none" stroke="#ffe46a" stroke-width="6" stroke-linecap="round"/>
  <path d="M62 247 C117 121 272 100 344 221" fill="none" stroke="#ff4ea3" stroke-width="2" stroke-dasharray="7 8" stroke-linecap="round"/>
  <path d="M57 262 C118 182 238 174 352 236" fill="none" stroke="#56f6ff" stroke-width="5" stroke-linecap="round"/>
  <path d="M57 262 C118 182 238 174 352 236" fill="none" stroke="#ffffff" stroke-width="1.4" stroke-dasharray="3 9" opacity=".7"/>

  <path d="M60 250 C126 214 184 209 240 216 C285 222 319 232 351 239 L337 254 C288 243 246 238 200 241 C151 245 103 259 62 278 Z" fill="url(#road)"/>
  <path d="M60 250 C126 214 184 209 240 216 C285 222 319 232 351 239" fill="none" stroke="#fff6c8" stroke-width="3" opacity=".75"/>
  <path d="M62 278 C103 259 151 245 200 241 C246 238 288 243 337 254" fill="none" stroke="#0c1847" stroke-width="4" opacity=".45"/>

  <g stroke="#dffcff" stroke-width="1.4" opacity=".85">
    <path d="M83 233 L99 213"/>
    <path d="M112 222 L128 200"/>
    <path d="M144 216 L157 190"/>
    <path d="M177 214 L188 180"/>
    <path d="M212 214 L222 178"/>
    <path d="M246 218 L255 186"/>
    <path d="M280 225 L289 197"/>
    <path d="M312 233 L323 210"/>
  </g>

  <g fill="none" stroke="#affcff" stroke-opacity=".5">
    <path d="M79 187 C130 313 281 69 338 153"/>
    <path d="M114 166 C139 280 292 107 367 171"/>
    <path d="M69 245 C162 151 242 301 355 223"/>
  </g>

  <g fill="#fff9b1">
    <circle cx="62" cy="250" r="4"/>
    <circle cx="101" cy="227" r="3"/>
    <circle cx="144" cy="216" r="3"/>
    <circle cx="189" cy="214" r="3"/>
    <circle cx="235" cy="216" r="3"/>
    <circle cx="280" cy="225" r="3"/>
    <circle cx="323" cy="235" r="3"/>
    <circle cx="351" cy="239" r="4"/>
  </g>

  <g opacity=".9">
    <circle cx="198" cy="154" r="18" fill="url(#glow)" filter="url(#blur)"/>
    <circle cx="198" cy="154" r="8" fill="#fffbd2"/>
    <path d="M198 95 C213 124 213 184 198 213 C183 184 183 124 198 95 Z" fill="none" stroke="#fffbd2" stroke-width="2"/>
    <path d="M150 154 C179 139 217 139 246 154 C217 169 179 169 150 154 Z" fill="none" stroke="#fffbd2" stroke-width="2"/>
  </g>

  <path d="M38 292 C77 304 106 305 142 292" fill="none" stroke="#82ffe7" stroke-width="1.5" opacity=".45"/>
  <path d="M290 273 C322 284 355 282 386 267" fill="none" stroke="#82ffe7" stroke-width="1.5" opacity=".45"/>

  <g fill="#0b1636" opacity=".7">
    <path d="M50 285 l11-28 l9 31 Z"/>
    <path d="M91 290 l14-33 l12 30 Z"/>
    <path d="M318 266 l10-28 l11 30 Z"/>
    <path d="M357 260 l9-26 l13 25 Z"/>
  </g>
</svg>