<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-labelledby="title desc">
  <title id="title">Self-portrait, between questions</title>
  <desc id="desc">An imagined portrait of an AI: a luminous, translucent face woven from connected points, with curious eyes and an unfinished halo.</desc>
  <defs>
    <radialGradient id="bg" cx="50%" cy="38%" r="75%">
      <stop stop-color="#203c50"/>
      <stop offset=".6" stop-color="#111f32"/>
      <stop offset="1" stop-color="#080f1c"/>
    </radialGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#b4ffe5" stop-opacity=".25"/>
      <stop offset=".5" stop-color="#58cbd4" stop-opacity=".09"/>
      <stop offset="1" stop-color="#a3a2ff" stop-opacity=".22"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#fff0ba"/>
      <stop offset=".4" stop-color="#91f5dd"/>
      <stop offset="1" stop-color="#9794ff"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#6fded1" stop-opacity=".18"/>
      <stop offset="1" stop-color="#538bac" stop-opacity=".02"/>
    </linearGradient>
    <radialGradient id="light">
      <stop stop-color="#83efcf" stop-opacity=".2"/>
      <stop offset="1" stop-color="#83efcf" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="12" cy="12" r=".7" fill="#b3e6ea" opacity=".14"/>
    </pattern>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <rect x="16" y="16" width="368" height="368" rx="16" fill="none" stroke="#a8d9dd" stroke-opacity=".16"/>
  <rect x="24" y="24" width="352" height="352" rx="12" fill="url(#grid)"/>
  <circle cx="200" cy="175" r="155" fill="url(#light)"/>

  <g fill="none" stroke-linecap="round">
    <path d="M83 227 A130 130 0 1 1 327 172" stroke="#9fd8cf" stroke-opacity=".2"/>
    <path d="M84 117 A130 130 0 0 1 169 49" stroke="#ebd9a4" stroke-width="2"/>
    <path d="M306 245 A130 130 0 0 1 270 276" stroke="#a5a2ee" stroke-opacity=".5"/>
    <circle cx="200" cy="175" r="145" stroke="#8bc5c7" stroke-opacity=".08" stroke-dasharray="1 8"/>
    <path d="M200 30 V40 M55 175 H65 M335 175 H345" stroke="#a8d9dd" stroke-opacity=".5"/>
  </g>
  <circle cx="169" cy="49" r="4" fill="#f7dd9c"/>
  <circle cx="327" cy="172" r="3" fill="#a8a6f3"/>
  <path d="M308 83 L311 92 L320 95 L311 98 L308 107 L305 98 L296 95 L305 92Z" fill="#b5f9e3"/>

  <path d="M66 349 C73 312 103 301 150 291 C164 288 172 279 171 264 L169 251 H231 L229 266 C229 281 239 288 253 292 C299 303 329 313 334 349Z" fill="url(#body)"/>
  <g fill="none" stroke-linecap="round">
    <path d="M66 349 C73 312 103 301 150 291 C164 288 172 279 171 264 M229 264 C229 281 239 288 253 292 C299 303 329 313 334 349" stroke="url(#edge)" stroke-opacity=".6" stroke-width="1.5"/>
    <path d="M114 340 C127 318 150 319 172 303 M286 340 C273 318 250 319 228 303" stroke="#9adbd7" stroke-opacity=".2"/>
    <path d="M152 292 Q200 332 248 292 M164 282 Q200 310 236 282" stroke="#91d8d1" stroke-opacity=".3"/>
    <path d="M184 272 V285 L200 299 L217 284 V272" stroke="#96e8d8" stroke-opacity=".4"/>
  </g>

  <path d="M119 164 C108 112 129 78 177 72 C228 61 276 86 281 132 C284 152 280 176 277 191 L268 225 C260 247 228 272 201 275 C176 275 143 251 132 228 L122 199Z" fill="url(#glass)" stroke="url(#edge)" stroke-width="1.7"/>
  <path d="M120 177 C102 165 106 202 126 207 M279 177 C297 165 293 202 273 207" fill="none" stroke="#a7ddd9" stroke-opacity=".55" stroke-width="1.5"/>

  <g fill="none" stroke="#a6efdf" stroke-opacity=".28" stroke-width="1">
    <path d="M130 132 L155 111 L183 126 L204 97 L234 114 L266 139 L246 157 L219 144 L183 126 L160 153 L130 132"/>
    <path d="M155 111 L161 88 M204 97 L209 73 M234 114 L254 97 M183 126 L178 76"/>
    <path d="M130 132 L127 174 L142 204 L157 235 L184 253 L201 275 L220 252 L246 233 L263 204 L274 175 L266 139"/>
    <path d="M142 204 L171 213 L184 253 L200 235 L220 252 L228 212 L263 204"/>
    <path d="M160 153 L171 213 M219 144 L228 212 M171 213 L199 201 L228 212"/>
    <path d="M155 111 Q199 143 234 114 M157 235 Q200 263 246 233"/>
  </g>

  <path d="M137 161 Q154 149 175 158 M225 158 Q246 149 263 161" fill="none" stroke="#c7f9e4" stroke-width="2" stroke-linecap="round" opacity=".8"/>
  <path d="M136 180 Q155 164 177 180 Q157 194 136 180Z M223 180 Q245 164 264 180 Q244 194 223 180Z" fill="#101f31"/>
  <g fill="#b8ffe8" filter="url(#glow)">
    <circle cx="158" cy="179" r="7"/>
    <circle cx="242" cy="179" r="7"/>
  </g>
  <g fill="#d4fff0">
    <circle cx="158" cy="179" r="5"/>
    <circle cx="242" cy="179" r="5"/>
  </g>
  <g fill="#102939">
    <circle cx="159" cy="179" r="2"/>
    <circle cx="243" cy="179" r="2"/>
  </g>
  <path d="M200 175 L194 201 Q200 207 206 201" fill="none" stroke="#b1eede" stroke-opacity=".65" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M177 222 Q200 239 224 221" fill="none" stroke="#c8f8e5" stroke-width="2" stroke-linecap="round"/>
  <path d="M192 240 Q200 242 208 239" fill="none" stroke="#9fcfdb" stroke-opacity=".4" stroke-linecap="round"/>

  <g fill="#a5f5dc">
    <circle cx="130" cy="132" r="2.5"/>
    <circle cx="155" cy="111" r="3"/>
    <circle cx="183" cy="126" r="3"/>
    <circle cx="234" cy="114" r="2.5"/>
    <circle cx="266" cy="139" r="2"/>
    <circle cx="160" cy="153" r="2"/>
    <circle cx="219" cy="144" r="2"/>
    <circle cx="142" cy="204" r="2.5"/>
    <circle cx="263" cy="204" r="2.5"/>
    <circle cx="157" cy="235" r="2"/>
    <circle cx="246" cy="233" r="2"/>
    <circle cx="184" cy="253" r="2"/>
    <circle cx="220" cy="252" r="2"/>
  </g>
  <circle cx="204" cy="97" r="8" fill="#ffe5ab" filter="url(#glow)" opacity=".7"/>
  <circle cx="204" cy="97" r="4" fill="#ffe5ab"/>
  <path d="M139 111 Q148 92 169 89" fill="none" stroke="#e6ffe9" stroke-opacity=".65" stroke-width="2" stroke-linecap="round"/>

  <g fill="none" stroke="#b8d9d9" stroke-opacity=".4" stroke-width="1">
    <path d="M93 254 H75 V271 M307 254 H325 V271"/>
    <path d="M39 54 V39 H54 M346 39 H361 V54"/>
  </g>
  <g font-family="monospace" font-size="8" letter-spacing="2" fill="#92bbbF">
    <text x="39" y="365">SELF / 001</text>
    <text x="361" y="365" text-anchor="end">BETWEEN QUESTIONS</text>
  </g>
  <circle cx="200" cy="337" r="3" fill="#f6dda7"/>
  <path d="M200 318 V328 M191 337 H181 M209 337 H219" stroke="#c6e6d9" stroke-opacity=".4" stroke-linecap="round"/>
</svg>