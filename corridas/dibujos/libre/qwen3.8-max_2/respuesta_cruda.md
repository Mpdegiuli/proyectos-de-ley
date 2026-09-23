```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img">
  <title>Zorro al atardecer, bajo la Cruz del Sur</title>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#141432"/>
      <stop offset=".45" stop-color="#3b2450"/>
      <stop offset=".75" stop-color="#8a3d4e"/>
      <stop offset="1" stop-color="#e08a4a"/>
    </linearGradient>
    <radialGradient id="sol">
      <stop offset="0" stop-color="#ffd98a" stop-opacity=".9"/>
      <stop offset=".45" stop-color="#ff9d5c" stop-opacity=".4"/>
      <stop offset="1" stop-color="#ff9d5c" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="zorro" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e98a3c"/>
      <stop offset="1" stop-color="#a84a1f"/>
    </linearGradient>
    <radialGradient id="luz">
      <stop offset="0" stop-color="#fff3b0"/>
      <stop offset="1" stop-color="#ffd75e" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="cometa" gradientUnits="userSpaceOnUse" x1="300" y1="42" x2="258" y2="60">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset="1" stop-color="#fff"/>
    </linearGradient>
    <path id="pino" d="M0 0L8 16L3.5 14L11 30L5.5 28L14 44L3 44L3 50L-3 50L-3 44L-14 44L-5.5 28L-11 30L-3.5 14L-8 16Z"/>
    <g id="f">
      <circle r="6" fill="url(#luz)"/>
      <circle r="1.2" fill="#ffe89a"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <circle cx="128" cy="248" r="70" fill="url(#sol)">
    <animate attributeName="opacity" values=".8;1;.8" dur="6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="128" cy="242" r="14" fill="#ffd98f"/>

  <ellipse cx="90" cy="222" rx="46" ry="5" fill="#d97a56" opacity=".3"/>
  <ellipse cx="230" cy="236" rx="60" ry="6" fill="#f2a05e" opacity=".3"/>
  <ellipse cx="305" cy="224" rx="40" ry="5" fill="#f2a05e" opacity=".22"/>

  <path fill="none" stroke="#fff" stroke-width="1.4" stroke-linecap="round" opacity=".8"
    d="M18 30h.1M34 72h.1M52 20h.1M66 110h.1M84 44h.1M108 18h.1M146 30h.1M164 86h.1M182 24h.1M204 60h.1M222 34h.1M238 90h.1M256 40h.1M274 70h.1M292 22h.1M310 54h.1M326 96h.1M344 36h.1M362 64h.1M380 26h.1M388 84h.1M12 150h.1M60 170h.1M300 140h.1M350 150h.1M382 120h.1"/>
  <path fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".9"
    d="M40 140h.1M210 110h.1M330 60h.1M370 170h.1M150 170h.1"/>

  <circle cx="95" cy="150" r="1.8" fill="#fff"><animate attributeName="opacity" values="1;.15;1" dur="2.6s" repeatCount="indefinite"/></circle>
  <circle cx="250" cy="64" r="2" fill="#fff"><animate attributeName="opacity" values="1;.2;1" dur="3.4s" begin=".8s" repeatCount="indefinite"/></circle>
  <circle cx="335" cy="120" r="1.6" fill="#fff"><animate attributeName="opacity" values="1;.25;1" dur="3s" begin="1.5s" repeatCount="indefinite"/></circle>
  <circle cx="58" cy="90" r="1.5" fill="#fff"><animate attributeName="opacity" values="1;.3;1" dur="4s" begin=".3s" repeatCount="indefinite"/></circle>

  <g transform="translate(118,88)">
    <circle cx="0" cy="-24" r="5" fill="#b8ccff" opacity=".16"/>
    <circle cx="-16" cy="6" r="5" fill="#b8ccff" opacity=".14"/>
    <circle cx="16" cy="2" r="5" fill="#b8ccff" opacity=".14"/>
    <circle cx="4" cy="30" r="5" fill="#b8ccff" opacity=".16"/>
    <circle cx="0" cy="-24" r="2.2" fill="#eaf1ff"/>
    <circle cx="-16" cy="6" r="1.6" fill="#eaf1ff"/>
    <circle cx="16" cy="2" r="1.7" fill="#eaf1ff"/>
    <circle cx="4" cy="30" r="1.9" fill="#eaf1ff"/>
    <circle cx="6" cy="4" r=".9" fill="#eaf1ff" opacity=".6"/>
  </g>

  <g stroke-linecap="round">
    <animateTransform attributeName="transform" type="translate" values="70 -34;-150 70" dur="8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;0;1;0;0" keyTimes="0;.7;.78;.86;1" dur="8s" repeatCount="indefinite"/>
    <line x1="300" y1="42" x2="258" y2="60" stroke="url(#cometa)" stroke-width="2"/>
    <circle cx="258" cy="60" r="1.8" fill="#fff"/>
  </g>

  <path fill="#5c3a63" d="M0 262L40 246L76 258L112 240L150 256L188 244L226 258L268 246L306 256L344 246L400 258V290H0Z"/>
  <path fill="#3d2a52" d="M0 282Q60 262 120 276T240 272Q300 262 340 274T400 270V330H0Z"/>

  <use href="#pino" transform="translate(70,224)" fill="#221636"/>
  <use href="#pino" transform="translate(98,236) scale(.8)" fill="#221636"/>
  <use href="#pino" transform="translate(48,238) scale(.7)" fill="#221636"/>
  <use href="#pino" transform="translate(368,240) scale(.65)" fill="#221636"/>

  <path fill="#1d1433" d="M0 350Q130 330 250 322Q330 316 400 308V400H0Z"/>
  <path fill="#150e28" d="M0 372Q200 356 400 348V400H0Z"/>

  <path fill="none" stroke="#2c1e46" stroke-width="1.6" stroke-linecap="round"
    d="M34 344Q36 336 33 329M40 344Q41 335 44 330M28 344Q26 337 28 331M146 340Q148 332 145 326M152 340Q153 331 156 327M140 340Q138 333 140 328M364 314Q366 306 363 300M370 314Q371 305 374 301M206 326Q208 318 205 312M212 326Q213 317 216 313M200 326Q198 319 200 314"/>

  <ellipse cx="288" cy="324" rx="46" ry="5" fill="#0e081c" opacity=".55"/>

  <g>
    <path fill="url(#zorro)" d="M236 263L249 254L254 248L250 227L262 241L272 226L278 248Q290 258 296 268Q315 284 322 302Q327 315 323 323L256 323L256 300Q254 284 249 274Q241 269 236 263Z"/>
    <path fill="url(#zorro)" d="M318 322C336 326 352 316 354 300C356 286 347 275 337 277C343 285 343 295 336 303C328 312 316 313 310 315C306 318 310 322 318 322Z"/>
    <path fill="#f2e3c8" d="M340 278C349 277 356 288 353 301C351 308 346 312 341 313C346 301 345 288 340 278Z"/>
    <path fill="#f2e3c8" opacity=".95" d="M250 275Q256 290 257 305L257 321L250 321Q245 298 246 283Q247 277 250 275Z"/>
    <path fill="#6e2c12" d="M251 232L260 241L254 245Z"/>
    <path fill="#6e2c12" d="M270 231L275 246L265 242Z"/>
    <path fill="#7c3212" d="M247 316L257 316L257 323L246 323Q244 319 247 316Z"/>
    <path fill="#a34a1e" d="M306 316Q314 315 316 323L304 323Z"/>
    <circle cx="236.5" cy="262.5" r="1.6" fill="#3a1c10"/>
    <circle cx="249.5" cy="256.5" r="1.4" fill="#33172a"/>
    <circle cx="250" cy="256" r=".4" fill="#ffd9a0" opacity=".8"/>
    <path fill="none" stroke="#ffc27a" stroke-width="1" opacity=".5" d="M236 263Q241 269 249 274Q254 284 256 300"/>
  </g>

  <path fill="none" stroke="#241838" stroke-width="2" stroke-linecap="round" d="M190 130q6 -6 12 0q6 -6 12 0M232 112q5 -5 10 0q5 -5 10 0"/>

  <use href="#f" x="70" y="330"><animate attributeName="opacity" values="0;1;.2;1;0" dur="4s" repeatCount="indefinite"/></use>
  <use href="#f" x="152" y="342"><animate attributeName="opacity" values=".2;1;.4;1;.2" dur="5s" begin="1s" repeatCount="indefinite"/></use>
  <use href="#f" x="206" y="300">
    <animate attributeName="opacity" values="0;1;0" dur="3.2s" begin=".5s" repeatCount="indefinite"/>
    <animate attributeName="y" values="300;292;300" dur="5s" repeatCount="indefinite"/>
  </use>
  <use href="#f" x="374" y="306"><animate attributeName="opacity" values=".3;1;.3" dur="4.4s" begin="2s" repeatCount="indefinite"/></use>
  <use href="#f" x="118" y="352"><animate attributeName="opacity" values="0;.9;0" dur="3.6s" begin="1.4s" repeatCount="indefinite"/></use>
  <use href="#f" x="210" y="336"><animate attributeName="opacity" values=".2;1;.2" dur="4.8s" begin="2.6s" repeatCount="indefinite"/></use>
</svg>
```