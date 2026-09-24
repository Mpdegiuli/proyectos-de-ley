<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="wall" x2="1" y2="1">
      <stop stop-color="#25363f"/>
      <stop offset="1" stop-color="#101f2b"/>
    </linearGradient>
    <linearGradient id="stone" x2=".8" y2="1">
      <stop stop-color="#e4b98d"/>
      <stop offset=".5" stop-color="#b78369"/>
      <stop offset="1" stop-color="#765452"/>
    </linearGradient>
    <linearGradient id="sky" x2="0" y2="1">
      <stop stop-color="#102c43"/>
      <stop offset=".7" stop-color="#356171"/>
      <stop offset="1" stop-color="#709193"/>
    </linearGradient>
    <linearGradient id="water" x2="0" y2="1">
      <stop stop-color="#42737b"/>
      <stop offset="1" stop-color="#163e50"/>
    </linearGradient>
    <linearGradient id="floor" x2="0" y2="1">
      <stop stop-color="#172b36"/>
      <stop offset="1" stop-color="#30454a"/>
    </linearGradient>
    <radialGradient id="halo">
      <stop stop-color="#fce9b9" stop-opacity=".3"/>
      <stop offset="1" stop-color="#fce9b9" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="opening">
      <path d="M97 307V154a103 103 0 0 1 206 0v153Z"/>
    </clipPath>
    <path id="leaf" d="M0 0C-20-5-29-23-23-38-6-33 4-17 0 0Z"/>
    <path id="longleaf" d="M0 0C-13-24-9-51 3-67 10-43 10-17 0 0Z"/>
    <g id="star" fill="#f7dfb0">
      <path d="M0-4 1-1 4 0 1 1 0 4-1 1-4 0-1-1Z"/>
    </g>
  </defs>

  <path fill="url(#wall)" d="M0 0h400v400H0z"/>
  <path d="M22 0v333M378 0v333M0 88h77m246 0h77M0 185h67m266 0h67M0 283h67m266 0h67" fill="none" stroke="#72807c" stroke-opacity=".12"/>
  <path d="M0 334h400v66H0z" fill="url(#floor)"/>
  <path d="m0 380 105-46m295 46-105-46M38 400l105-66m219 66-105-66" stroke="#617475" stroke-opacity=".2"/>
  <ellipse cx="200" cy="358" rx="157" ry="26" fill="#0b1b26" opacity=".45"/>

  <path d="M69 322V153a131 131 0 0 1 262 0v169Z" fill="#0d202b"/>
  <path d="M76 316V154a124 124 0 0 1 248 0v162h-21V154a103 103 0 0 0-206 0v162Z" fill="url(#stone)"/>
  <path d="M82 315V154a118 118 0 0 1 236 0v161" fill="none" stroke="#efd0a3" stroke-opacity=".45" stroke-width="2"/>
  <path d="M97 307V154a103 103 0 0 1 206 0v153Z" fill="url(#sky)"/>

  <g clip-path="url(#opening)">
    <circle cx="221" cy="124" r="92" fill="url(#halo)"/>
    <circle cx="221" cy="124" r="43" fill="#f7deb0"/>
    <circle cx="208" cy="115" r="32" fill="#ffe9bf"/>
    <g fill="#d5bc94" opacity=".3">
      <circle cx="243" cy="122" r="9"/>
      <circle cx="229" cy="147" r="7"/>
      <circle cx="239" cy="103" r="4"/>
      <circle cx="209" cy="142" r="4"/>
      <circle cx="224" cy="95" r="3"/>
    </g>
    <g fill="#f6e3bc">
      <circle cx="143" cy="107" r="1.2"/>
      <circle cx="177" cy="76" r=".9"/>
      <circle cx="280" cy="145" r="1"/>
      <circle cx="118" cy="161" r="1"/>
      <circle cx="270" cy="92" r="1.2"/>
      <circle cx="164" cy="145" r=".8"/>
      <circle cx="184" cy="182" r=".8"/>
      <circle cx="255" cy="180" r="1"/>
      <circle cx="137" cy="185" r=".7"/>
    </g>
    <use href="#star" transform="translate(153 127) scale(.8)"/>
    <use href="#star" transform="translate(276 117) scale(.65)"/>
    <use href="#star" transform="translate(195 64) scale(.6)"/>
    <path d="M99 177h38m-27 4h43m101-21h38m-51 5h38" fill="none" stroke="#b7ced0" stroke-opacity=".25" stroke-linecap="round"/>
    <path d="m91 211 26-19 17 9 30-34 34 35 18-9 31 23 34-27 30 23v35H91Z" fill="#345565"/>
    <path d="m132 204 32-37 18 20-18-10-12 19-6-1Z" fill="#81a0a2" opacity=".5"/>
    <path d="m87 221 29-10 30 8 34-10 38 15 46-15 42 13v31H87Z" fill="#264c60"/>
    <path d="M90 230h220v87H90z" fill="url(#water)"/>
    <path d="M97 232h206" stroke="#a9bdaf" stroke-opacity=".5"/>
    <g fill="none" stroke-linecap="round">
      <path d="M204 237h34m-44 6h52m-36 6h26m-43 6h50m-37 6h34m-52 7h65m-52 8h34m-44 8h61m-75 10h67" stroke="#e8cfa0" stroke-opacity=".65" stroke-width="2"/>
      <path d="M110 242h34m6 9h22m-62 12h28m131-18h18m-25 20h31m-167 16h26m110 15h33m-133-3h15" stroke="#93b7b2" stroke-opacity=".45"/>
    </g>
    <path d="m110 225 14-4 10 4m137-17 8-4 8 4" fill="none" stroke="#183748" stroke-width="1.5"/>
    <path d="M89 301c44-5 74 1 111 0s72-4 110 0v17H89Z" fill="#142e3b"/>
  </g>

  <g stroke="#6a5050" stroke-width="1.5" opacity=".7">
    <path d="M77 170h19m-19 42h19m-19 43h19m-19 43h19m208-128h19m-19 42h19m-19 43h19m-19 43h19M82 116l20 6m-1-45 17 13m14-42 12 19m35-35 4 21m38-21-4 21m51-6-12 20m43 10-17 13m37 26-20 6"/>
  </g>
  <path d="m189 29 22 0-3 28h-16Z" fill="#efd0a0"/>
  <path d="M95 307h210v12H95z" fill="#dbb88f"/>
  <path d="M95 311h210v8H95z" fill="#8e6d60"/>
  <path d="m95 319-14 13h238l-14-13Z" fill="#c19a7c"/>
  <path d="M81 332h238v10H81z" fill="#765953"/>
  <path d="m81 342-17 14h272l-17-14Z" fill="#b38d73"/>
  <path d="M64 356h272v11H64z" fill="#624d4b"/>
  <path d="m64 367-18 14h308l-18-14Z" fill="#9a7c69"/>
  <path d="M46 381h308v7H46z" fill="#54494a"/>
  <path d="M99 308h202M85 332h230M68 356h264M51 381h298" fill="none" stroke="#efc89b" stroke-opacity=".65"/>

  <g fill="#112733">
    <path d="M258 305c-7-3-10-10-9-20l3-13-1-12 8 6 8-1 7-7 1 17c8 12 8 23 2 30Z"/>
    <path d="M273 300c20 4 23-7 17-13-3-4-6-1-4 2 4 5-1 10-12 7Z"/>
  </g>
  <path d="m256 274 3 1m9-1 3-1" stroke="#e9c895" stroke-width="1.5" stroke-linecap="round"/>

  <g stroke="#6c9583" stroke-width="2" fill="none">
    <path d="M47 326c7-39 5-86-12-125m14 104c-5-33-16-53-32-68m35 47c6-29 14-48 22-58m-24 91c12-22 18-31 28-39"/>
  </g>
  <g fill="#3d7469">
    <use href="#leaf" transform="translate(45 250) rotate(-22)"/>
    <use href="#leaf" transform="translate(49 280) rotate(-34)"/>
    <use href="#leaf" transform="translate(37 273) rotate(-46) scale(.85)"/>
    <use href="#leaf" transform="translate(30 253) rotate(-24) scale(.8)"/>
    <use href="#leaf" transform="translate(52 266) rotate(83) scale(.95)"/>
    <use href="#leaf" transform="translate(64 242) rotate(78) scale(.8)"/>
    <use href="#leaf" transform="translate(58 305) rotate(92) scale(.85)"/>
  </g>
  <g fill="#709782">
    <use href="#leaf" transform="translate(39 224) rotate(8) scale(.8)"/>
    <use href="#leaf" transform="translate(49 253) rotate(70) scale(.8)"/>
    <use href="#leaf" transform="translate(70 290) rotate(87) scale(.7)"/>
    <use href="#leaf" transform="translate(23 244) rotate(-16) scale(.6)"/>
  </g>
  <path d="M27 320h47l-6 32q-17 11-34 0Z" fill="#b7765c"/>
  <path d="M27 320h15l4 38-12-6Z" fill="#cf9470"/>
  <ellipse cx="50.5" cy="320" rx="24" ry="6" fill="#dbab81"/>
  <ellipse cx="50.5" cy="320" rx="19" ry="3.5" fill="#34403d"/>
  <path d="M50 320v-12" stroke="#709782" stroke-width="3"/>
  <path d="m30 333 41 0m-39 6h38" stroke="#edbd8d" stroke-opacity=".4"/>

  <g>
    <path d="M351 340c-7-25-3-51 5-71m-5 66c11-31 19-39 31-48m-29 42c-14-27-24-37-32-43" fill="none" stroke="#648c79" stroke-width="2"/>
    <g fill="#467c6d">
      <use href="#longleaf" transform="translate(350 332) rotate(-30) scale(.9)"/>
      <use href="#longleaf" transform="translate(354 331) rotate(29) scale(.9)"/>
      <use href="#longleaf" transform="translate(353 322) rotate(58) scale(.72)"/>
      <use href="#longleaf" transform="translate(348 331) rotate(-65) scale(.72)"/>
    </g>
    <g fill="#82a188">
      <use href="#longleaf" transform="translate(351 327) rotate(7) scale(.9)"/>
      <use href="#longleaf" transform="translate(350 335) rotate(-43) scale(.6)"/>
      <use href="#longleaf" transform="translate(353 337) rotate(44) scale(.6)"/>
    </g>
    <path d="M330 335h45l-5 31q-16 10-34 0Z" fill="#567478"/>
    <path d="M330 335h12l4 35-10-4Z" fill="#77918c"/>
    <ellipse cx="352.5" cy="335" rx="23" ry="5" fill="#91a599"/>
    <ellipse cx="352.5" cy="335" rx="18" ry="2.5" fill="#293f41"/>
    <path d="M352 335v-11" stroke="#82a188" stroke-width="3"/>
  </g>

  <g fill="#eac495">
    <circle cx="43" cy="132" r="1.2" opacity=".7"/>
    <circle cx="352" cy="194" r="1" opacity=".5"/>
    <circle cx="32" cy="294" r="1" opacity=".6"/>
    <circle cx="365" cy="244" r="1.4" opacity=".7"/>
  </g>
  <path d="M18 18h27m-27 0v27m364-27h-27m27 0v27M18 382v-18m364 18v-18" fill="none" stroke="#b69678" stroke-opacity=".5"/>
</svg>