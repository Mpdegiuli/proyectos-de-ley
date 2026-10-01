<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="night" cx=".5" cy=".4" r=".75">
      <stop stop-color="#233b50"/>
      <stop offset="1" stop-color="#090f25"/>
    </radialGradient>
    <linearGradient id="wood" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#327b83"/>
      <stop offset=".48" stop-color="#85cab7"/>
      <stop offset="1" stop-color="#dfedbd"/>
    </linearGradient>
    <linearGradient id="leaf" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#347586"/>
      <stop offset="1" stop-color="#95e8cb"/>
    </linearGradient>
    <linearGradient id="rose" x2=".8" y2="1">
      <stop stop-color="#ffd7a6"/>
      <stop offset="1" stop-color="#d76f95"/>
    </linearGradient>
    <radialGradient id="glass" cx=".35" cy=".25" r=".8">
      <stop stop-color="#b9ffeb" stop-opacity=".3"/>
      <stop offset=".7" stop-color="#75c6d8" stop-opacity=".06"/>
      <stop offset="1" stop-color="#6ac3d0" stop-opacity=".35"/>
    </radialGradient>
    <linearGradient id="rock" x2=".3" y2="1">
      <stop stop-color="#305264"/>
      <stop offset="1" stop-color="#111b33"/>
    </linearGradient>
    <g id="blade">
      <path d="M0 0C-25-9-27-38-11-58C8-42 15-17 0 0Z" fill="url(#leaf)" stroke="#b3edcf" stroke-width=".7"/>
      <path d="M0 0Q-12-29-11-58M-5-20l-13-11M-8-33l10-10" fill="none" stroke="#183f54" stroke-width="1" opacity=".6"/>
      <ellipse cx="-10" cy="-29" rx="5" ry="8" fill="#183f54"/>
      <ellipse cx="-10" cy="-30" rx="2" ry="4" fill="#f7dfab"/>
    </g>
    <g id="petal">
      <path d="M0 0C-19-11-20-35-5-49C12-29 13-11 0 0Z" fill="url(#rose)"/>
      <path d="M0-2Q-6-25-5-44" fill="none" stroke="#fff0c5" stroke-width=".8"/>
    </g>
    <g id="fruit">
      <circle r="22" fill="url(#glass)" stroke="#a4ded6" stroke-width=".8"/>
      <path d="M-16-6A17 17 0 0 1-5-17" fill="none" stroke="#e0fff1" stroke-width="1.6" stroke-linecap="round"/>
      <path d="M5-12A13 13 0 1 0 9 10A11 11 0 0 1 5-12Z" fill="#ffe2a6"/>
      <ellipse rx="29" ry="6" transform="rotate(-22)" fill="none" stroke="#e6b883" stroke-width=".9"/>
      <circle cx="17" cy="-10" r="2" fill="#fff1c4"/>
      <path d="M-3-22L0-26L3-22" fill="#e6b883"/>
    </g>
    <g id="spark" fill="#f8d69d">
      <path d="M0-5L1.3-1.3L5 0L1.3 1.3L0 5L-1.3 1.3L-5 0L-1.3-1.3Z"/>
    </g>
  </defs>

  <path fill="url(#night)" d="M0 0H400V400H0Z"/>
  <circle cx="201" cy="171" r="134" fill="#669e9e" opacity=".055"/>
  <circle cx="201" cy="171" r="125" fill="none" stroke="#7cafad" stroke-width=".6" opacity=".18"/>
  <path d="M57 251A159 159 0 0 1 308 53M336 93A159 159 0 0 1 347 233" fill="none" stroke="#d6d6ac" stroke-width=".6" opacity=".22"/>
  <g fill="#bbdbcf" opacity=".65">
    <circle cx="39" cy="84" r="1"/><circle cx="69" cy="42" r=".8"/>
    <circle cx="129" cy="30" r="1.1"/><circle cx="262" cy="34" r=".8"/>
    <circle cx="350" cy="63" r="1"/><circle cx="370" cy="153" r=".8"/>
    <circle cx="31" cy="190" r=".8"/><circle cx="52" cy="284" r="1.2"/>
    <circle cx="360" cy="288" r="1"/><circle cx="319" cy="343" r=".7"/>
    <circle cx="87" cy="357" r=".8"/><circle cx="283" cy="378" r=".8"/>
    <circle cx="31" cy="330" r=".6"/><circle cx="373" cy="366" r=".7"/>
  </g>
  <use href="#spark" transform="translate(324 80) scale(.8)"/>
  <use href="#spark" transform="translate(44 136) scale(.65)"/>
  <use href="#spark" transform="translate(352 241) scale(.8)"/>
  <use href="#spark" transform="translate(106 291) scale(.5)"/>

  <ellipse cx="202" cy="366" rx="63" ry="7" fill="#020a1d" opacity=".35"/>
  <path d="M120 314L149 343L175 345L199 369L219 344L247 338L278 314Z" fill="url(#rock)"/>
  <path d="M143 320L175 345L165 321M199 326V369L219 344L226 321M247 338L249 318" fill="none" stroke="#568486" stroke-width=".8" opacity=".45"/>
  <path d="M120 314Q150 298 189 303Q238 297 278 314Q244 334 199 329Q151 332 120 314Z" fill="#275764"/>
  <path d="M124 314Q191 296 275 314Q212 325 154 318" fill="none" stroke="#85bba8" stroke-width="1"/>
  <ellipse cx="201" cy="313" rx="56" ry="8" fill="#a4d6b8" opacity=".12"/>

  <g fill="none" stroke="url(#wood)" stroke-linecap="round" stroke-linejoin="round">
    <path d="M196 305C182 274 184 247 200 224C219 196 218 174 203 145C190 122 197 99 210 75" stroke-width="15"/>
    <path d="M191 253C179 224 152 213 137 190C120 165 131 141 111 121" stroke-width="9"/>
    <path d="M207 213C232 199 241 181 252 159C264 135 288 129 305 111" stroke-width="8"/>
    <path d="M202 147C179 146 168 127 156 110C148 96 135 88 120 84" stroke-width="6"/>
    <path d="M137 187C117 177 104 160 78 158" stroke-width="5"/>
    <path d="M128 161C147 149 150 132 148 115" stroke-width="4"/>
    <path d="M239 183C258 187 280 178 290 164" stroke-width="5"/>
    <path d="M257 151C246 132 249 113 258 96" stroke-width="5"/>
    <path d="M204 118C225 112 232 96 236 81" stroke-width="4"/>
    <path d="M287 129L312 135" stroke-width="3"/>
  </g>

  <path d="M185 310C177 286 177 265 190 245C218 204 224 193 205 155C216 184 210 204 194 225C171 254 172 281 180 298C174 307 154 306 144 314C164 310 178 314 187 309Z" fill="#1b4e61"/>
  <path d="M204 278C196 294 204 302 220 306L250 317L226 314L208 310L216 322L199 313L189 319L172 322L184 314L171 309L151 314C168 301 184 308 189 298Z" fill="url(#wood)"/>
  <g fill="none" stroke="#f2d39a" stroke-linecap="round">
    <path d="M195 309C180 280 186 255 202 231C231 187 208 164 203 144" stroke-width="1.7"/>
    <path d="M190 240C174 216 151 210 140 187" stroke-width="1"/>
    <path d="M220 203Q239 184 252 160" stroke-width="1"/>
    <path d="M197 307L218 312M186 306L165 312" stroke-width=".9"/>
  </g>

  <use href="#blade" transform="translate(111 125) rotate(-48) scale(.9)"/>
  <use href="#blade" transform="translate(115 130) rotate(20) scale(.72)"/>
  <use href="#blade" transform="translate(82 159) rotate(-76) scale(.78)"/>
  <use href="#petal" transform="translate(94 161) rotate(-28) scale(.72)"/>
  <use href="#blade" transform="translate(148 135) rotate(30) scale(.8)"/>
  <use href="#petal" transform="translate(149 114) rotate(-6) scale(.66)"/>
  <use href="#blade" transform="translate(129 88) rotate(-55) scale(.85)"/>
  <use href="#petal" transform="translate(166 123) rotate(24) scale(.63)"/>
  <use href="#blade" transform="translate(207 85) rotate(-16) scale(.85)"/>
  <use href="#petal" transform="translate(211 76) rotate(37) scale(.8)"/>
  <use href="#blade" transform="translate(236 87) rotate(45) scale(.66)"/>
  <use href="#blade" transform="translate(258 110) rotate(-16) scale(.69)"/>
  <use href="#petal" transform="translate(261 106) rotate(41) scale(.72)"/>
  <use href="#blade" transform="translate(295 123) rotate(62) scale(.83)"/>
  <use href="#petal" transform="translate(303 115) rotate(14) scale(.72)"/>
  <use href="#blade" transform="translate(285 173) rotate(72) scale(.86)"/>
  <use href="#petal" transform="translate(279 179) rotate(113) scale(.58)"/>
  <use href="#blade" transform="translate(159 214) rotate(-69) scale(.62)"/>
  <use href="#blade" transform="translate(222 221) rotate(64) scale(.65)"/>

  <g fill="none" stroke="#e4c393" stroke-width=".9">
    <path d="M88 161Q94 175 91 188"/>
    <path d="M169 128Q177 146 171 166"/>
    <path d="M313 134Q322 160 313 193"/>
    <path d="M257 161Q269 175 265 226"/>
    <path d="M235 84Q228 67 240 53"/>
  </g>
  <use href="#fruit" transform="translate(91 211) scale(.9)"/>
  <use href="#fruit" transform="translate(171 183) scale(.65)"/>
  <use href="#fruit" transform="translate(313 213) scale(.78)"/>
  <use href="#fruit" transform="translate(265 248) scale(.85)"/>
  <use href="#fruit" transform="translate(241 44) scale(.44)"/>

  <g fill="#f4d5a0">
    <path d="M73 261Q68 270 73 273Q79 270 73 261Z"/>
    <path d="M288 285Q283 294 288 297Q294 294 288 285Z"/>
    <path d="M169 354Q165 362 169 364Q173 362 169 354Z"/>
    <path d="M230 361Q226 369 230 371Q234 369 230 361Z"/>
  </g>
  <g fill="none" stroke="#a8dbcb" stroke-width=".7" opacity=".7">
    <ellipse cx="74" cy="278" rx="9" ry="2"/>
    <ellipse cx="288" cy="303" rx="10" ry="2.5"/>
    <path d="M147 272q-12-8-18 1q10-3 15 5M303 57q10-9 17-3q-10-1-13 8"/>
  </g>
  <use href="#spark" transform="translate(215 263) scale(.65)"/>
  <use href="#spark" transform="translate(119 249) scale(.55)"/>
  <use href="#spark" transform="translate(283 61) scale(.45)"/>
  <circle cx="200" cy="381" r="2" fill="#f4d5a0"/>
</svg>