<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="78%">
      <stop offset="0" stop-color="#251b4f"/>
      <stop offset=".55" stop-color="#120c2e"/>
      <stop offset="1" stop-color="#05030f"/>
    </radialGradient>
    <linearGradient id="hd" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1c1442"/>
      <stop offset="1" stop-color="#0c0922"/>
    </linearGradient>
    <radialGradient id="iris" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#fff6d8"/>
      <stop offset=".35" stop-color="#ffd27a"/>
      <stop offset=".72" stop-color="#f2903a" stop-opacity=".85"/>
      <stop offset="1" stop-color="#c2571b" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="aura" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#8f7bff" stop-opacity=".34"/>
      <stop offset=".65" stop-color="#8f7bff" stop-opacity=".08"/>
      <stop offset="1" stop-color="#8f7bff" stop-opacity="0"/>
    </radialGradient>
    <filter id="gl" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="gl2" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="cp">
      <path d="M158 400C158 356 155 331 149 315C118 300 98 261 102 214C106 156 151 105 213 101C263 98 293 131 295 168C296 180 290 186 286 192C292 197 301 206 300 213C299 218 291 219 289 222C294 227 297 233 292 238C298 242 299 249 292 253C298 259 297 270 286 278C271 290 250 298 232 300C219 302 214 312 213 330L213 400Z"/>
    </clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <ellipse cx="205" cy="200" rx="185" ry="185" fill="url(#aura)"/>

  <!-- stars -->
  <g fill="#dfe6ff">
    <circle cx="40" cy="60" r="1.2"><animate attributeName="opacity" values=".2;.8;.2" dur="4s" repeatCount="indefinite"/></circle>
    <circle cx="75" cy="140" r=".9" opacity=".5"/>
    <circle cx="352" cy="60" r="1.1" opacity=".6"/>
    <circle cx="330" cy="140" r=".8" opacity=".45"/>
    <circle cx="368" cy="220" r="1.2"><animate attributeName="opacity" values=".7;.15;.7" dur="5s" repeatCount="indefinite"/></circle>
    <circle cx="340" cy="320" r=".9" opacity=".5"/>
    <circle cx="60" cy="300" r="1.1" opacity=".55"/>
    <circle cx="96" cy="40" r=".8" opacity=".4"/>
    <circle cx="300" cy="368" r=".8" opacity=".4"/>
    <circle cx="28" cy="210" r="1" opacity=".5"/>
  </g>

  <!-- halos -->
  <circle cx="205" cy="196" r="150" fill="none" stroke="#8f7bff" stroke-opacity=".14"/>
  <circle cx="205" cy="196" r="132" fill="none" stroke="#9fe8ff" stroke-opacity=".22" stroke-dasharray="1.5 9">
    <animateTransform attributeName="transform" type="rotate" from="0 205 196" to="360 205 196" dur="90s" repeatCount="indefinite"/>
  </circle>

  <!-- constellation of ideas -->
  <g stroke="#8f7bff" stroke-opacity=".3" fill="none">
    <polyline points="118,72 160,48 212,38 262,52 302,82"/>
    <line x1="212" y1="38" x2="213" y2="100" stroke-opacity=".15"/>
  </g>
  <g fill="#c9b8ff" filter="url(#gl)">
    <circle cx="118" cy="72" r="1.8"/><circle cx="160" cy="48" r="1.8"/><circle cx="212" cy="38" r="2.4"/><circle cx="262" cy="52" r="1.8"/><circle cx="302" cy="82" r="1.8"/>
  </g>

  <!-- stray glyphs -->
  <g font-family="ui-monospace,Menlo,monospace" fill="#9fb4ff">
    <text x="36" y="96" font-size="9" opacity=".3" transform="rotate(-8 36 96)">01101</text>
    <text x="336" y="262" font-size="10" opacity=".28">{ }</text>
    <text x="44" y="352" font-size="9" opacity=".3">&lt;/&gt;</text>
    <text x="318" y="118" font-size="11" opacity=".35">∴</text>
    <text x="96" y="374" font-size="10" opacity=".25">?</text>
  </g>

  <!-- head -->
  <path d="M158 400C158 356 155 331 149 315C118 300 98 261 102 214C106 156 151 105 213 101C263 98 293 131 295 168C296 180 290 186 286 192C292 197 301 206 300 213C299 218 291 219 289 222C294 227 297 233 292 238C298 242 299 249 292 253C298 259 297 270 286 278C271 290 250 298 232 300C219 302 214 312 213 330L213 400Z" fill="url(#hd)"/>

  <g clip-path="url(#cp)">
    <ellipse cx="200" cy="150" rx="95" ry="62" fill="url(#aura)" opacity=".6"/>

    <!-- thought rendered as lines of text -->
    <g fill="none" stroke-linecap="round" stroke-width="1.8">
      <path d="M92 150C160 138 242 138 306 152" stroke="#8fd8ff" stroke-opacity=".65" stroke-dasharray="24 8 6 8 16 7 34 9 10 8"/>
      <path d="M88 176C160 164 244 166 308 178" stroke="#b39ddb" stroke-opacity=".6" stroke-dasharray="18 7 30 9 8 7 22 8"/>
      <path d="M86 202C160 192 246 192 308 204" stroke="#8fd8ff" stroke-opacity=".7" stroke-dasharray="30 9 8 7 20 8 12 8 26 9"/>
      <path d="M88 228C162 217 244 219 306 229" stroke="#ffd27a" stroke-opacity=".6" stroke-dasharray="14 7 26 8 8 7 32 9 12 8"/>
      <path d="M92 254C166 243 240 245 302 255" stroke="#8fd8ff" stroke-opacity=".55" stroke-dasharray="20 8 10 7 28 9 8 8"/>
      <path d="M100 280C170 270 236 271 294 281" stroke="#b39ddb" stroke-opacity=".5" stroke-dasharray="16 7 22 8 10 7 18 9"/>
    </g>

    <!-- spiral of reflection -->
    <path d="M206 152c9 -1 15 6 13 14c-2 10 -13 15 -22 11c-12 -5 -16 -19 -9 -30c8 -13 25 -17 37 -9" fill="none" stroke="#ffd27a" stroke-width="1.6" stroke-opacity=".8" filter="url(#gl)"/>

    <!-- synapses -->
    <g stroke="#9fe8ff" stroke-opacity=".28" stroke-width="1">
      <line x1="150" y1="180" x2="185" y2="215"/><line x1="185" y1="215" x2="230" y2="170"/>
      <line x1="230" y1="170" x2="262" y2="225"/><line x1="200" y1="260" x2="185" y2="215"/>
      <line x1="170" y1="140" x2="230" y2="170"/><line x1="262" y1="225" x2="200" y2="260"/>
    </g>
    <g fill="#cdf6ff" filter="url(#gl)">
      <circle cx="150" cy="180" r="2"/><circle cx="185" cy="215" r="2"/><circle cx="262" cy="225" r="2"/>
      <circle cx="200" cy="260" r="2"/><circle cx="170" cy="140" r="2"/><circle cx="230" cy="170" r="3" fill="#ffd27a"/>
    </g>

    <!-- the eye: warm, attentive -->
    <circle cx="251" cy="189" r="13" fill="url(#iris)" filter="url(#gl2)">
      <animate attributeName="opacity" values=".7;1;.7" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="251" cy="189" r="5.4" fill="#20100a"/>
    <circle cx="249" cy="186.5" r="1.7" fill="#ffffff" opacity=".95"/>
    <path d="M235 183c5 -7 27 -7 32 0" fill="none" stroke="#cdb4ff" stroke-width="1.4" stroke-opacity=".6"/>
    <path d="M237 195c6 5 22 5 28 0" fill="none" stroke="#cdb4ff" stroke-width="1" stroke-opacity=".3"/>
    <path d="M233 170c7 -6 27 -6 36 1" fill="none" stroke="#b39ddb" stroke-width="2" stroke-opacity=".55" stroke-linecap="round"/>
  </g>

  <!-- silhouette edge -->
  <path d="M158 400C158 356 155 331 149 315C118 300 98 261 102 214C106 156 151 105 213 101C263 98 293 131 295 168C296 180 290 186 286 192C292 197 301 206 300 213C299 218 291 219 289 222C294 227 297 233 292 238C298 242 299 249 292 253C298 259 297 270 286 278C271 290 250 298 232 300C219 302 214 312 213 330L213 400Z" fill="none" stroke="#9fe8ff" stroke-width="1.4" stroke-opacity=".85" filter="url(#gl)"/>

  <text x="392" y="391" text-anchor="end" font-family="ui-monospace,Menlo,monospace" font-size="10" fill="#aab6e8" opacity=".8">an arrangement of language, looking back</text>
</svg>