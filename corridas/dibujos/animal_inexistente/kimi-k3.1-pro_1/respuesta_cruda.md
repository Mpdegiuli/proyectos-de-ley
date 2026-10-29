<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="72%">
      <stop offset="0" stop-color="#34315f"/>
      <stop offset=".58" stop-color="#191d3d"/>
      <stop offset="1" stop-color="#0b1027"/>
    </radialGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#91ead2"/>
      <stop offset=".48" stop-color="#83b9dc"/>
      <stop offset="1" stop-color="#b783d5"/>
    </linearGradient>
    <linearGradient id="fin" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#b9fff0" stop-opacity=".82"/>
      <stop offset="1" stop-color="#b786e5" stop-opacity=".25"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#fff3ad"/>
      <stop offset="1" stop-color="#e6a96d"/>
    </linearGradient>
    <radialGradient id="iris">
      <stop stop-color="#efffff"/>
      <stop offset=".35" stop-color="#72f4df"/>
      <stop offset="1" stop-color="#33758d"/>
    </radialGradient>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="170%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#050818" flood-opacity=".55"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="198" r="163" fill="none" stroke="#a49bde" stroke-opacity=".13"/>
  <circle cx="200" cy="198" r="151" fill="none" stroke="#9fe8dc" stroke-opacity=".12" stroke-dasharray="2 11"/>
  <path d="M47 282 Q200 346 353 282" fill="none" stroke="#8b82c5" stroke-opacity=".1"/>
  <g fill="#d8fff4">
    <circle cx="61" cy="99" r="1.6" opacity=".7"/>
    <circle cx="340" cy="90" r="1.4" opacity=".8"/>
    <circle cx="348" cy="230" r="2" opacity=".55"/>
    <circle cx="74" cy="266" r="1.3" opacity=".65"/>
    <circle cx="111" cy="54" r="1.2" opacity=".5"/>
    <circle cx="323" cy="312" r="1.4" opacity=".55"/>
    <path d="M54 184l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" opacity=".7"/>
    <path d="M337 258l2 4 4 2-4 2-2 4-2-4-4-2 4-2z" opacity=".65"/>
    <path d="M328 49l1.5 4 4 1.5-4 1.5-1.5 4-1.5-4-4-1.5 4-1.5z" opacity=".6"/>
  </g>
  <ellipse cx="201" cy="330" rx="86" ry="11" fill="#070b20" opacity=".4"/>

  <g stroke-linecap="round" stroke-linejoin="round">
    <path d="M142 191C112 197 92 184 79 164C64 142 72 117 95 102C84 124 88 144 107 151C128 159 143 165 157 182Z" fill="url(#body)" stroke="#29284e" stroke-width="3"/>
    <path d="M97 105C78 101 67 88 69 73C82 83 94 82 103 91C107 77 117 69 130 69C122 83 119 97 102 107Z" fill="url(#fin)" stroke="#83d7d2" stroke-width="2"/>
    <path d="M100 102Q88 90 76 82M103 99Q113 84 122 77" fill="none" stroke="#e0fff3" stroke-opacity=".45" stroke-width="1.5"/>
    <path d="M137 184Q105 183 88 158" fill="none" stroke="#d8fff1" stroke-opacity=".35" stroke-width="3"/>

    <path d="M181 185C151 161 145 122 170 88C173 121 190 126 197 148C204 127 219 114 238 111C224 137 225 163 213 184Z" fill="url(#fin)" stroke="#8cd9d5" stroke-width="2"/>
    <path d="M187 174Q163 135 170 101M197 172Q206 139 228 120M194 154L177 130" fill="none" stroke="#ecfff8" stroke-opacity=".43" stroke-width="1.5"/>

    <g fill="none" stroke="#222644" stroke-width="12" opacity=".65">
      <path d="M145 218C136 247 143 269 126 291"/>
      <path d="M183 235C177 259 186 280 174 302"/>
      <path d="M228 232C235 254 226 277 239 298"/>
    </g>
    <g fill="none" stroke="#69aebc" stroke-width="7" opacity=".72">
      <path d="M145 218C136 247 143 269 126 291"/>
      <path d="M183 235C177 259 186 280 174 302"/>
      <path d="M228 232C235 254 226 277 239 298"/>
    </g>

    <path d="M253 128C233 120 222 103 226 84C244 93 256 105 260 122Z" fill="url(#fin)" stroke="#9bded8" stroke-width="2"/>
    <path d="M280 127C289 105 306 98 320 103C310 119 298 129 284 133Z" fill="url(#fin)" stroke="#9bded8" stroke-width="2"/>
    <path d="M251 119L232 94M287 123L311 107" fill="none" stroke="#effff8" stroke-opacity=".45" stroke-width="1.5"/>

    <g fill="none" stroke="url(#gold)" stroke-width="4">
      <path d="M264 127C257 106 263 91 255 75M260 97L246 86M259 85L270 72M255 75L252 60"/>
      <path d="M281 126C290 106 283 92 294 77M288 96L303 89M290 84L282 72M294 77L305 64"/>
    </g>
    <g fill="#fff0a6" filter="url(#glow)">
      <circle cx="252" cy="59" r="3"/>
      <circle cx="246" cy="86" r="2.5"/>
      <circle cx="270" cy="72" r="2.5"/>
      <circle cx="305" cy="64" r="3"/>
      <circle cx="303" cy="89" r="2.5"/>
      <circle cx="282" cy="72" r="2.5"/>
    </g>

    <path d="M128 200C139 178 169 169 199 178C219 184 229 176 234 153C239 130 250 119 269 119C283 119 292 126 298 135L315 140C325 143 324 153 315 158L291 162C279 165 270 173 266 188L258 215C250 239 225 250 190 247C153 244 126 229 128 200Z" fill="url(#body)" stroke="#29284e" stroke-width="3" filter="url(#shadow)"/>

    <path d="M139 213C160 237 213 250 247 220C232 245 194 254 160 237C150 232 143 224 139 213Z" fill="#e5fff4" opacity=".16"/>
    <path d="M239 158Q217 151 220 134Q234 139 243 146M235 177Q215 172 215 157Q228 159 239 166" fill="url(#fin)" stroke="#8bd5d1" stroke-width="1.5"/>

    <g fill="none" stroke="#222644" stroke-width="12">
      <path d="M158 235C154 262 159 287 145 313"/>
      <path d="M207 242C201 268 211 291 198 318"/>
      <path d="M247 215C256 244 249 271 263 292"/>
    </g>
    <g fill="none" stroke="url(#body)" stroke-width="7">
      <path d="M158 235C154 262 159 287 145 313"/>
      <path d="M207 242C201 268 211 291 198 318"/>
      <path d="M247 215C256 244 249 271 263 292"/>
    </g>
    <g fill="#a6f4db" stroke="#dffff3" stroke-width="1" filter="url(#glow)">
      <circle cx="145" cy="314" r="3.5"/>
      <circle cx="198" cy="319" r="3.5"/>
      <circle cx="263" cy="293" r="3.5"/>
    </g>

    <path d="M190 193C175 197 173 216 186 223C176 211 183 200 197 199C195 196 193 194 190 193Z" fill="#fff0ae" opacity=".9"/>
    <path d="M218 198l2.5 6 6 2.5-6 2.5-2.5 6-2.5-6-6-2.5 6-2.5z" fill="#e9fff4" opacity=".75"/>
    <g fill="#e8fff5" opacity=".55">
      <circle cx="153" cy="201" r="4"/>
      <circle cx="163" cy="190" r="2.5"/>
      <circle cx="211" cy="226" r="3"/>
      <circle cx="231" cy="211" r="2"/>
    </g>
    <g fill="none" stroke="#436d91" stroke-width="2" opacity=".55">
      <path d="M248 181q9 5 15 0"/>
      <path d="M246 189q8 5 14 1"/>
    </g>

    <path d="M266 126L272 133L266 140L260 133Z" fill="#ffe9a0" stroke="#514266" stroke-width="1.5"/>
    <circle cx="266" cy="133" r="2.3" fill="#27304d"/>
    <ellipse cx="285" cy="143" rx="9" ry="11" fill="#202441"/>
    <ellipse cx="286" cy="143" rx="5.5" ry="7" fill="url(#iris)"/>
    <ellipse cx="287" cy="144" rx="2" ry="4.5" fill="#17223a"/>
    <circle cx="283" cy="139" r="2.2" fill="#fff"/>
    <ellipse cx="314" cy="149" rx="3.5" ry="2.7" fill="#3a3156"/>
    <path d="M298 157Q306 163 314 157" fill="none" stroke="#514066" stroke-width="1.8"/>
    <circle cx="296" cy="151" r="4" fill="#f0a8cf" opacity=".35"/>

    <g fill="none" stroke="#ffe7a0" stroke-width="1.5" filter="url(#glow)">
      <path d="M307 157Q329 173 346 165"/>
      <path d="M309 153Q333 148 345 136"/>
    </g>
    <g fill="#fff0ac">
      <circle cx="346" cy="165" r="2.4"/>
      <circle cx="345" cy="136" r="2.4"/>
    </g>
  </g>

  <g fill="#c9f9e9" opacity=".7">
    <circle cx="112" cy="319" r="2"/>
    <circle cx="285" cy="323" r="1.7"/>
    <circle cx="92" cy="299" r="1.2"/>
    <path d="M298 283l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/>
  </g>
</svg>