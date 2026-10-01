<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x2="0" y2="1">
      <stop stop-color="#172846"/>
      <stop offset="1" stop-color="#416d7b"/>
    </linearGradient>
    <linearGradient id="skin" x2=".8" y2="1">
      <stop stop-color="#a5f0d0"/>
      <stop offset=".55" stop-color="#4dc3ad"/>
      <stop offset="1" stop-color="#26818d"/>
    </linearGradient>
    <linearGradient id="fin" x2="1" y2="1">
      <stop stop-color="#ffbc8c"/>
      <stop offset="1" stop-color="#dd6f9e"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop stop-color="#fff4ad"/>
      <stop offset="1" stop-color="#f4bd69"/>
    </radialGradient>
    <filter id="soft">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="315" cy="82" r="43" fill="#c3f2d8" opacity=".08"/>
  <path d="M0 304 Q85 280 160 305 T400 292 V400 H0Z" fill="#183f50" opacity=".65"/>
  <path d="M0 330 Q90 314 180 335 T400 319" fill="none" stroke="#87d5c3" stroke-opacity=".18" stroke-width="2"/>

  <g fill="#d9f7d8" opacity=".7">
    <circle cx="49" cy="82" r="2"/><circle cx="102" cy="47" r="1.6"/>
    <circle cx="351" cy="142" r="2"/><circle cx="286" cy="40" r="1.4"/>
    <circle cx="36" cy="185" r="1.5"/><circle cx="366" cy="221" r="1.6"/>
  </g>
  <g fill="none" stroke="#d9f7d8" stroke-width="1.5" opacity=".5">
    <path d="M72 123v10m-5-5h10"/><path d="M334 53v9m-4.5-4.5h9"/>
    <path d="M307 188v8m-4-4h8"/>
  </g>

  <!-- luminous tail -->
  <path d="M282 228 C334 221 351 178 327 160 C308 146 282 164 291 181 C299 195 322 188 322 174"
        fill="none" stroke="#f7a5ad" stroke-width="13" stroke-linecap="round"/>
  <path d="M282 228 C334 221 351 178 327 160 C308 146 282 164 291 181 C299 195 322 188 322 174"
        fill="none" stroke="#ffd7a7" stroke-width="4" stroke-linecap="round"/>
  <path d="M330 158 Q352 145 364 153 Q354 164 351 178 Q339 170 330 158Z" fill="url(#fin)"/>
  <path d="M337 161l14 8m-10-12 11 3" stroke="#ffe0b2" stroke-width="1.5" opacity=".8"/>

  <!-- back frills -->
  <g fill="url(#fin)" stroke="#ffd4bd" stroke-width="1.5">
    <path d="M165 183 Q142 153 151 130 Q177 145 181 178Z"/>
    <path d="M184 177 Q169 142 187 119 Q206 145 200 180Z"/>
    <path d="M207 176 Q205 139 230 125 Q238 155 222 184Z"/>
  </g>
  <g fill="none" stroke="#ffe3bd" stroke-width="1.3" opacity=".8">
    <path d="M169 177l-12-35m27 37-1-43m16 43 13-42"/>
  </g>

  <!-- legs -->
  <g fill="url(#skin)" stroke="#247b83" stroke-width="2">
    <path d="M157 251 Q148 271 145 294 Q137 305 121 307 Q118 313 139 316 Q153 315 159 302 L178 263Z"/>
    <path d="M196 263 Q190 283 190 305 Q181 313 169 317 Q169 324 191 324 Q207 321 208 308 L216 265Z"/>
    <path d="M246 258 Q250 278 259 296 Q254 307 243 316 Q246 323 265 314 Q276 306 270 294 L267 253Z"/>
    <path d="M278 244 Q292 259 302 279 Q299 290 290 300 Q295 307 310 294 Q318 283 307 270 L291 236Z"/>
  </g>
  <g fill="#e6b8a4">
    <ellipse cx="131" cy="312" rx="13" ry="4"/>
    <ellipse cx="181" cy="320" rx="13" ry="4"/>
    <ellipse cx="255" cy="313" rx="13" ry="4"/>
    <ellipse cx="302" cy="297" rx="12" ry="4"/>
  </g>

  <!-- body and neck -->
  <path d="M126 224 Q140 190 183 184 Q224 169 270 194 Q301 210 299 236 Q296 263 264 268 Q222 277 184 262 Q146 260 126 244Z"
        fill="url(#skin)" stroke="#226e7e" stroke-width="3"/>
  <path d="M143 233 Q176 247 211 241 Q248 250 281 231" fill="none" stroke="#c8f4d5" stroke-width="3" opacity=".65"/>
  <path d="M177 196 Q208 184 244 197" fill="none" stroke="#d7f8db" stroke-width="2" opacity=".6"/>

  <!-- head -->
  <path d="M102 205 Q91 184 103 164 Q116 145 143 151 Q165 155 174 176 Q181 195 165 214 Q149 229 124 223Z"
        fill="url(#skin)" stroke="#226e7e" stroke-width="3"/>
  <path d="M105 187 Q86 182 78 190 Q87 202 105 203Z" fill="#8ce0c5" stroke="#226e7e" stroke-width="2"/>
  <ellipse cx="124" cy="175" rx="9" ry="11" fill="#fff0be"/>
  <ellipse cx="127" cy="175" rx="4" ry="7" fill="#263b50"/>
  <circle cx="128" cy="172" r="2" fill="#fff"/>
  <circle cx="97" cy="193" r="2.5" fill="#e47786"/>
  <path d="M108 211 Q122 218 135 212" fill="none" stroke="#247b83" stroke-width="2" stroke-linecap="round"/>

  <!-- branching moon-antlers -->
  <g fill="none" stroke="#e9d5a1" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M130 154 Q123 132 126 112 Q129 97 117 84 M126 119 Q143 111 145 95 M123 108 Q108 103 105 91"/>
    <path d="M151 153 Q164 132 162 111 Q160 97 174 83 M162 119 Q148 109 151 94 M163 106 Q179 102 183 89"/>
  </g>
  <g fill="url(#glow)">
    <circle cx="117" cy="83" r="6"/><circle cx="145" cy="94" r="5"/>
    <circle cx="105" cy="90" r="4"/><circle cx="174" cy="82" r="6"/>
    <circle cx="151" cy="93" r="4.5"/><circle cx="183" cy="88" r="4"/>
  </g>
  <g fill="#fff4b2" opacity=".4" filter="url(#soft)">
    <circle cx="117" cy="83" r="10"/><circle cx="174" cy="82" r="10"/>
  </g>

  <!-- spots -->
  <g fill="#e2f6bc" opacity=".8">
    <circle cx="202" cy="210" r="3"/><circle cx="220" cy="220" r="2"/>
    <circle cx="242" cy="208" r="3"/><circle cx="267" cy="222" r="2.5"/>
    <circle cx="190" cy="235" r="2.5"/><circle cx="246" cy="242" r="2"/>
  </g>
  <ellipse cx="214" cy="343" rx="105" ry="10" fill="#0c293a" opacity=".28"/>
</svg>