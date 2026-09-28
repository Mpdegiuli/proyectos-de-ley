<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x2="0" y2="1">
      <stop stop-color="#17234d"/>
      <stop offset=".58" stop-color="#514b83"/>
      <stop offset="1" stop-color="#f0a978"/>
    </linearGradient>
    <linearGradient id="roof" x2=".9" y2="1">
      <stop stop-color="#ffb56f"/>
      <stop offset="1" stop-color="#d65d79"/>
    </linearGradient>
    <linearGradient id="wall" x2="1" y2="1">
      <stop stop-color="#f8dba6"/>
      <stop offset="1" stop-color="#dc8d82"/>
    </linearGradient>
    <linearGradient id="side" x2="1" y2="1">
      <stop stop-color="#91c8bd"/>
      <stop offset="1" stop-color="#4c7894"/>
    </linearGradient>
    <radialGradient id="portal">
      <stop stop-color="#fff7ba"/>
      <stop offset=".38" stop-color="#9ce7e0"/>
      <stop offset="1" stop-color="#7967bd"/>
    </radialGradient>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="322" cy="76" r="26" fill="#ffe4a4" opacity=".16" filter="url(#glow)"/>
  <circle cx="322" cy="76" r="17" fill="#ffe4a4"/>
  <circle cx="329" cy="70" r="17" fill="#26305e"/>
  <path d="M0 270Q48 235 94 267T190 257T294 268T400 244V400H0Z" fill="#313d70" opacity=".52"/>
  <path d="M0 308Q65 276 132 305T265 300T400 284V400H0Z" fill="#242f5b" opacity=".68"/>
  <g fill="#fff0c4">
    <circle cx="43" cy="62" r="1.5"/><circle cx="81" cy="103" r="1.2"/>
    <circle cx="119" cy="42" r="1.7"/><circle cx="174" cy="76" r="1.2"/>
    <circle cx="247" cy="40" r="1.4"/><circle cx="365" cy="139" r="1.5"/>
    <circle cx="40" cy="177" r="1.4"/><circle cx="356" cy="211" r="1.1"/>
    <circle cx="76" cy="218" r="1.2"/><circle cx="276" cy="105" r="1.1"/>
  </g>
  <path d="M58 79l3 7 7 3-7 3-3 7-3-7-7-3 7-3zM351 113l2 5 5 2-5 2-2 5-2-5-5-2 5-2zM92 147l2 4 4 2-4 2-2 4-2-4-4-2 4-2z" fill="#fff0c4"/>

  <!-- The house hangs over its own little sky -->
  <ellipse cx="208" cy="314" rx="113" ry="17" fill="#171e49" opacity=".6"/>
  <ellipse cx="208" cy="309" rx="85" ry="10" fill="none" stroke="#83d8d2" stroke-width="3" opacity=".8"/>
  <ellipse cx="208" cy="309" rx="58" ry="6" fill="none" stroke="#f9bb91" stroke-width="2" opacity=".7"/>

  <path d="M145 262L130 301M270 264L283 298M199 278L199 307" stroke="#efbd8d" stroke-width="7" stroke-linecap="round"/>
  <path d="M120 301l20 1M273 299l21-2M189 309l21 0" stroke="#6c7798" stroke-width="4" stroke-linecap="round"/>

  <!-- Walls, turned slightly into two different directions -->
  <path d="M111 156L204 111L204 281L139 267Z" fill="url(#wall)" stroke="#734f70" stroke-width="3"/>
  <path d="M204 111L303 153L287 270L204 281Z" fill="url(#side)" stroke="#354c73" stroke-width="3"/>
  <path d="M111 156L204 111L303 153L278 165L203 133L126 170Z" fill="#f4c28a" opacity=".5"/>

  <!-- Roof like a folded, impossible paper hat -->
  <path d="M73 159L197 47L330 143L303 153L204 111L111 156Z" fill="url(#roof)" stroke="#633f6c" stroke-width="4" stroke-linejoin="round"/>
  <path d="M197 47L211 118L204 111L111 156L73 159Z" fill="#f1a866" opacity=".8"/>
  <path d="M197 47L330 143L303 153L204 111L211 118Z" fill="#bf5c83" opacity=".72"/>
  <path d="M73 159Q112 149 146 162" fill="none" stroke="#ffe0a3" stroke-width="4" stroke-linecap="round"/>
  <path d="M204 111Q256 126 303 153" fill="none" stroke="#ffe0a3" stroke-width="3" opacity=".8"/>

  <!-- Chimney and its wandering smoke -->
  <path d="M258 95L260 61L285 69L288 123Z" fill="#8b5778" stroke="#503c69" stroke-width="3"/>
  <path d="M256 62L260 54L289 62L285 70Z" fill="#f6bd82" stroke="#503c69" stroke-width="3"/>
  <path d="M274 51C250 37 290 29 278 17C268 7 296 8 301 18" fill="none" stroke="#f8d6b1" stroke-width="4" stroke-linecap="round" opacity=".8"/>
  <circle cx="301" cy="18" r="3" fill="#fff0c4"/>

  <!-- Portal door -->
  <path d="M147 263L147 204Q147 181 169 174Q191 181 191 204L191 277Z" fill="#704d78" stroke="#563f70" stroke-width="4"/>
  <path d="M153 261L153 205Q153 187 169 181Q185 187 185 205L185 273Z" fill="url(#portal)"/>
  <path d="M159 203Q169 188 180 203" fill="none" stroke="#fff4ca" stroke-width="2" opacity=".9"/>
  <circle cx="178" cy="242" r="2.5" fill="#ffe9a7"/>
  <circle cx="163" cy="223" r="1.5" fill="#fff"/>
  <circle cx="174" cy="212" r="1.2" fill="#fff"/>

  <!-- Windows that don't agree about perspective -->
  <path d="M215 158L250 171L248 207L215 197Z" fill="#34466e" stroke="#f8d39a" stroke-width="4"/>
  <path d="M220 164L245 174L243 200L220 193Z" fill="#f6c978"/>
  <path d="M232 169L231 197M219 181L244 187" stroke="#8a6275" stroke-width="2"/>
  <path d="M263 184L286 178L282 211L260 216Z" fill="#34466e" stroke="#f8d39a" stroke-width="4"/>
  <path d="M267 187L281 184L278 207L264 210Z" fill="#f4bd79"/>
  <path d="M273 185L271 209M263 198L280 194" stroke="#8a6275" stroke-width="2"/>
  <path d="M126 184L138 178L138 209L126 215Z" fill="#45587c" stroke="#ffe0a4" stroke-width="3"/>
  <path d="M132 181L132 211" stroke="#ffe0a4" stroke-width="2"/>

  <!-- A staircase curls away from the front door and climbs into nowhere -->
  <path d="M169 277C163 305 112 301 108 327C105 349 154 354 185 339C217 324 209 304 187 301" fill="none" stroke="#513e76" stroke-width="18" stroke-linecap="round"/>
  <path d="M169 277C163 305 112 301 108 327C105 349 154 354 185 339C217 324 209 304 187 301" fill="none" stroke="#f3bd88" stroke-width="12" stroke-linecap="round"/>
  <path d="M159 293L174 296M145 302L158 310M128 311L141 319M119 324L132 330M121 338L136 339M139 347L151 342M160 346L167 336M178 335L183 325M190 316L184 309" stroke="#fff0c3" stroke-width="2" stroke-linecap="round"/>
  <path d="M108 327Q92 329 91 343Q105 355 121 350" fill="#91c8bd" stroke="#e8c797" stroke-width="2"/>

  <!-- Small floating cloudlets -->
  <path d="M47 286Q49 278 58 280Q61 270 72 274Q80 269 85 279Q96 279 96 288Q95 295 84 294H57Q45 295 47 286Z" fill="#c4d8d4" opacity=".82"/>
  <path d="M318 257Q320 250 328 252Q332 243 340 248Q349 245 352 254Q363 253 362 262Q361 268 350 268H326Q316 268 318 257Z" fill="#e8c9ba" opacity=".78"/>
  <path d="M38 302l5 2-5 2-2 5-2-5-5-2 5-2 2-5zM341 292l4 2-4 2-2 4-2-4-4-2 4-2 2-4z" fill="#fff0c4"/>
</svg>