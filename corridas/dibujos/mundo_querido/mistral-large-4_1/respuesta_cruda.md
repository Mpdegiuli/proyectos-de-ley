<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#aee2ff"/>
      <stop offset=".55" stop-color="#e6f8ff"/>
      <stop offset="1" stop-color="#fff4dd"/>
    </linearGradient>
    <radialGradient id="mar" cx=".35" cy=".3" r="1">
      <stop offset="0" stop-color="#8fdcff"/>
      <stop offset="1" stop-color="#1e88c7"/>
    </radialGradient>
    <radialGradient id="sol" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#fff8b0"/>
      <stop offset="1" stop-color="#ffb300"/>
    </radialGradient>
    <clipPath id="globo"><circle cx="200" cy="210" r="85"/></clipPath>
    <g id="mano">
      <ellipse cx="0" cy="7" rx="11" ry="13"/>
      <rect x="-10.5" y="-11" width="4.6" height="16" rx="2.3"/>
      <rect x="-5.4" y="-15.5" width="4.6" height="20" rx="2.3"/>
      <rect x="-0.3" y="-14.5" width="4.6" height="19" rx="2.3"/>
      <rect x="4.8" y="-10.5" width="4.6" height="15" rx="2.3"/>
      <rect x="8" y="-1" width="12" height="5" rx="2.5" transform="rotate(-38 8 -1)"/>
    </g>
    <path id="cor" d="M0 4 C-6 -3 -14 1 -12 8 C-10 14 -3 18 0 22 C3 18 10 14 12 8 C14 1 6 -3 0 4 Z"/>
    <path id="ave" d="M0 0 Q4 -5 8 0 Q12 -5 16 0" fill="none" stroke="#455a64" stroke-width="1.7" stroke-linecap="round"/>
    <g id="nube">
      <ellipse cx="0" cy="0" rx="20" ry="13"/>
      <ellipse cx="-17" cy="3" rx="13" ry="9"/>
      <ellipse cx="17" cy="3" rx="14" ry="10"/>
    </g>
    <g id="arb">
      <rect x="-1.6" y="0" width="3.2" height="7" fill="#795548"/>
      <circle cx="0" cy="-3.5" r="6" fill="#2e7d32"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <g fill="#ffffff" opacity=".85">
    <circle cx="36" cy="42" r="1.8"/><circle cx="372" cy="52" r="1.6"/>
    <circle cx="352" cy="24" r="1.4"/><circle cx="24" cy="150" r="1.5"/>
    <circle cx="382" cy="140" r="1.7"/><circle cx="150" cy="34" r="1.4"/>
  </g>

  <g stroke="#ffb300" stroke-width="4" stroke-linecap="round">
    <line x1="55" y1="13" x2="55" y2="23"/>
    <line x1="55" y1="13" x2="55" y2="23" transform="rotate(45 55 55)"/>
    <line x1="55" y1="13" x2="55" y2="23" transform="rotate(90 55 55)"/>
    <line x1="55" y1="13" x2="55" y2="23" transform="rotate(135 55 55)"/>
    <line x1="55" y1="13" x2="55" y2="23" transform="rotate(180 55 55)"/>
    <line x1="55" y1="13" x2="55" y2="23" transform="rotate(225 55 55)"/>
    <line x1="55" y1="13" x2="55" y2="23" transform="rotate(270 55 55)"/>
    <line x1="55" y1="13" x2="55" y2="23" transform="rotate(315 55 55)"/>
  </g>
  <circle cx="55" cy="55" r="26" fill="url(#sol)"/>
  <circle cx="47" cy="51" r="2.6" fill="#6d4c41"/>
  <circle cx="63" cy="51" r="2.6" fill="#6d4c41"/>
  <circle cx="42" cy="58" r="3" fill="#ff8a80" opacity=".6"/>
  <circle cx="68" cy="58" r="3" fill="#ff8a80" opacity=".6"/>
  <path d="M46 61 Q55 69 64 61" fill="none" stroke="#6d4c41" stroke-width="2.5" stroke-linecap="round"/>

  <g fill="none" stroke-width="7" opacity=".7">
    <path d="M50 300 A150 150 0 0 1 350 300" stroke="#e53935"/>
    <path d="M57 300 A143 143 0 0 1 343 300" stroke="#fb8c00"/>
    <path d="M64 300 A136 136 0 0 1 336 300" stroke="#fdd835"/>
    <path d="M71 300 A129 129 0 0 1 329 300" stroke="#43a047"/>
    <path d="M78 300 A122 122 0 0 1 322 300" stroke="#1e88e5"/>
    <path d="M85 300 A115 115 0 0 1 315 300" stroke="#8e24aa"/>
  </g>

  <g fill="#ffffff" opacity=".92">
    <use href="#nube" transform="translate(96 122)"/>
    <use href="#nube" transform="translate(318 108) scale(.85)"/>
    <use href="#nube" transform="translate(58 252) scale(.7)"/>
    <use href="#nube" transform="translate(344 218) scale(.75)"/>
  </g>

  <path d="M0 372 Q25 360 50 372 T100 372 T150 372 T200 372 T250 372 T300 372 T350 372 T400 372 L400 400 L0 400 Z" fill="#4fc3f7" opacity=".75"/>
  <path d="M0 387 Q25 377 50 387 T100 387 T150 387 T200 387 T250 387 T300 387 T350 387 T400 387 L400 400 L0 400 Z" fill="#0288d1" opacity=".65"/>

  <circle cx="200" cy="210" r="85" fill="url(#mar)"/>
  <g clip-path="url(#globo)">
    <path d="M130 180 Q140 150 175 155 Q205 160 200 185 Q190 210 160 205 Q135 200 130 180 Z" fill="#66bb6a"/>
    <path d="M225 235 Q240 215 270 225 Q295 235 285 260 Q265 280 240 270 Q220 255 225 235 Z" fill="#43a047"/>
    <path d="M160 265 Q175 250 195 260 Q205 275 190 288 Q168 292 158 280 Z" fill="#66bb6a"/>
    <circle cx="256" cy="164" r="12" fill="#81c784"/>
    <circle cx="150" cy="240" r="8" fill="#81c784"/>
    <use href="#arb" transform="translate(162 172)"/>
    <use href="#arb" transform="translate(176 166) scale(.8)"/>
    <use href="#arb" transform="translate(256 234)"/>
    <use href="#arb" transform="translate(243 240) scale(.75)"/>
    <use href="#arb" transform="translate(180 264) scale(.85)"/>
    <ellipse cx="168" cy="158" rx="42" ry="20" fill="#ffffff" opacity=".3" transform="rotate(-28 168 158)"/>
  </g>
  <circle cx="200" cy="210" r="85" fill="none" stroke="#ffffff" stroke-width="4" opacity=".9"/>

  <g>
    <use href="#mano" transform="translate(200 210) rotate(0) translate(0 -122) rotate(180)" fill="#f1c27d"/>
    <use href="#mano" transform="translate(200 210) rotate(45) translate(0 -122) rotate(180)" fill="#8d5524"/>
    <use href="#mano" transform="translate(200 210) rotate(90) translate(0 -122) rotate(180)" fill="#ffdbac"/>
    <use href="#mano" transform="translate(200 210) rotate(135) translate(0 -122) rotate(180)" fill="#a0522d"/>
    <use href="#mano" transform="translate(200 210) rotate(180) translate(0 -122) rotate(180)" fill="#c68642"/>
    <use href="#mano" transform="translate(200 210) rotate(225) translate(0 -122) rotate(180)" fill="#e0ac69"/>
    <use href="#mano" transform="translate(200 210) rotate(270) translate(0 -122) rotate(180)" fill="#6b4226"/>
    <use href="#mano" transform="translate(200 210) rotate(315) translate(0 -122) rotate(180)" fill="#d7a06b"/>
  </g>

  <g opacity=".92">
    <use href="#cor" transform="translate(122 58) scale(1.15)" fill="#ef5350"/>
    <use href="#cor" transform="translate(298 66) scale(.95)" fill="#ec407a"/>
    <use href="#cor" transform="translate(352 158) scale(.75)" fill="#e53935"/>
    <use href="#cor" transform="translate(52 168) scale(.85)" fill="#f06292"/>
    <use href="#cor" transform="translate(338 296) scale(.65)" fill="#ef5350"/>
    <use href="#cor" transform="translate(66 316) scale(.7)" fill="#ec407a"/>
  </g>

  <g>
    <use href="#ave" transform="translate(140 88)"/>
    <use href="#ave" transform="translate(258 52) scale(.85)"/>
    <use href="#ave" transform="translate(316 176) scale(.9)"/>
    <use href="#ave" transform="translate(76 196) scale(.8)"/>
    <use href="#ave" transform="translate(216 34) scale(.7)"/>
  </g>
</svg>