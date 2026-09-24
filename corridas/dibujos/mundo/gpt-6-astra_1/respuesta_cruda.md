<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-labelledby="title desc">
  <title id="title">Un mundo que todavía cuidamos</title>
  <desc id="desc">Un planeta agrietado, entre incendios y conexiones luminosas, sostenido por dos manos. De su fractura nace un brote.</desc>
  <defs>
    <radialGradient id="night" cx="53%" cy="42%" r="75%">
      <stop stop-color="#24394b"/>
      <stop offset="1" stop-color="#090f20"/>
    </radialGradient>
    <linearGradient id="sea" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#24354d"/>
      <stop offset=".5" stop-color="#22586a"/>
      <stop offset="1" stop-color="#479d99"/>
    </linearGradient>
    <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#a4c69a"/>
      <stop offset="1" stop-color="#418879"/>
    </linearGradient>
    <linearGradient id="heat" x1="0" x2="1">
      <stop stop-color="#ec7757" stop-opacity=".8"/>
      <stop offset=".65" stop-color="#ec7757" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="handA" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#9b5262"/>
      <stop offset="1" stop-color="#efb28b"/>
    </linearGradient>
    <linearGradient id="handB" x1="1" y1="1" x2="0" y2="0">
      <stop stop-color="#376780"/>
      <stop offset="1" stop-color="#99c6ba"/>
    </linearGradient>
    <radialGradient id="halo">
      <stop stop-color="#6ad2bb" stop-opacity=".19"/>
      <stop offset="1" stop-color="#6ad2bb" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="world">
      <circle cx="200" cy="177" r="108"/>
    </clipPath>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.5"/>
    </filter>
    <pattern id="grain" width="7" height="7" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r=".5" fill="#d8efdb" opacity=".09"/>
    </pattern>
  </defs>

  <path fill="url(#night)" d="M0 0h400v400H0z"/>
  <circle cx="208" cy="174" r="166" fill="url(#halo)"/>
  <path fill="url(#grain)" d="M0 0h400v400H0z"/>

  <g fill="#c5d8d1">
    <circle cx="43" cy="42" r="1.2"/>
    <circle cx="110" cy="29" r=".8"/>
    <circle cx="249" cy="30" r="1"/>
    <circle cx="356" cy="113" r="1.3"/>
    <circle cx="333" cy="246" r=".8"/>
    <circle cx="36" cy="217" r="1"/>
    <circle cx="71" cy="292" r=".7"/>
    <circle cx="296" cy="335" r=".8"/>
    <path d="M65 104v8m-4-4h8M275 59v6m-3-3h6" fill="none" stroke="#c5d8d1" stroke-width=".8"/>
  </g>

  <circle cx="330" cy="52" r="18" fill="#f1b073"/>
  <circle cx="337" cy="47" r="17" fill="#101b2c"/>
  <circle cx="330" cy="52" r="24" fill="none" stroke="#e7a274" stroke-opacity=".13"/>

  <g fill="none" stroke="#9fc9c4" stroke-width=".8">
    <ellipse cx="200" cy="180" rx="166" ry="58" transform="rotate(-29 200 180)" stroke-opacity=".28"/>
    <path d="M51 171C78 54 291 24 345 172" stroke-opacity=".15" stroke-dasharray="3 7"/>
    <path d="M75 269C163 322 294 303 333 221" stroke-opacity=".3"/>
  </g>

  <g transform="translate(64 139) rotate(-29)">
    <path d="M-22-7h14V7h-14zm30 0h14V7H8z" fill="#376079" stroke="#8bb3bc" stroke-width=".8"/>
    <path d="M-15-7V7m30-14V7M-22 0h14M8 0h14" stroke="#90bdc6" stroke-width=".5"/>
    <path d="M-8 0H8" stroke="#d1c9ae"/>
    <rect x="-5" y="-6" width="10" height="12" rx="2" fill="#d9c6a1"/>
    <path d="M0-6v-7m-3 0h6" stroke="#d9c6a1"/>
  </g>

  <circle cx="200" cy="177" r="114" fill="none" stroke="#81cab8" stroke-opacity=".14" stroke-width="5"/>
  <circle cx="200" cy="177" r="109" fill="#82bdae"/>
  <g clip-path="url(#world)">
    <circle cx="200" cy="177" r="108" fill="url(#sea)"/>
    <g fill="none" stroke="#b6ded1" stroke-opacity=".13" stroke-width=".8">
      <ellipse cx="200" cy="177" rx="57" ry="108"/>
      <ellipse cx="200" cy="177" rx="91" ry="108"/>
      <path d="M92 177h216M102 134c61 18 135 18 196 0M102 220c61-18 135-18 196 0M126 98c47 16 101 16 148 0M126 257c47-16 101-16 148 0"/>
    </g>

    <g fill="url(#land)">
      <path d="M106 103l28-19 24 2 13 13-5 13 14 10-12 13-19 2-7 18-15 1-4 16-13-6-8-26-15-8z"/>
      <path d="M145 173l19 3 14 17 17 7-2 18-13 11-4 22-15 18-5-23-10-17 2-21-10-19z"/>
      <path d="M205 89l17-15 28 5 13 13 25 8 22 25-7 22-17 1-9 15-16-9-13 8-10-17-17-6-9-14-15 4-9-12 12-12z"/>
      <path d="M219 147l23 6 13 23-5 18-15 16-5 22-14-2-9-24-12-14 3-22z"/>
      <path d="M262 171l11 3 4 13-6 7-6-10zM282 189l14 8-3 7-13-7z"/>
      <path d="M267 224l20-9 21 12-2 23-21 5-17-13z"/>
      <path d="M173 79l13-9 14 6-6 18-13 8-11-8z"/>
      <path d="M139 274l37-6 20 5 26-7 35 8-10 18h-97z" fill="#c6d8cb"/>
    </g>

    <path d="M88 65h135v232H88z" fill="url(#heat)"/>
    <g fill="#f0a36d">
      <path d="M121 149c-10-12 7-20 2-33 13 9 6 14 12 18 2-6 6-8 6-8 8 17 0 28-10 28z"/>
      <path d="M152 213c-8-10 4-17 2-28 11 8 5 12 10 15l4-6c6 13 0 23-9 23z"/>
    </g>
    <g fill="#ffe0a1">
      <path d="M126 149c-4-6 3-11 3-16 6 7 8 16 1 19z"/>
      <path d="M156 212l4-12c6 8 5 14 0 14z"/>
    </g>
    <g fill="none" stroke="#3e4b56" stroke-width="6" stroke-linecap="round" opacity=".5">
      <path d="M127 115c-18-17 15-23 0-43"/>
      <path d="M151 182c-13-12 10-21-2-34"/>
    </g>

    <path d="M202 66l-9 32 14 23-14 28 15 24-11 24 16 26-9 29 9 39" fill="none" stroke="#142d3b" stroke-width="9"/>
    <path d="M202 66l-9 32 14 23-14 28 15 24-11 24 16 26-9 29 9 39" fill="none" stroke="#f6c780" stroke-width="2.3"/>
    <g stroke="#ffe0a0" stroke-width="2" stroke-linecap="round">
      <path d="M188 95l13 5m-1 17 13 7m-26 21 13 6m1 19 13 5m-23 20 12 4m3 22 13 5m-21 25 13 3m-6 16 13-3"/>
    </g>

    <g fill="none" stroke="#abefd4" stroke-width="1" opacity=".75">
      <path d="M225 116l44 17-32 42 46 61M269 133l19 40-51 2M225 116l12 59-16 38M288 173l-5 63"/>
      <path d="M163 187Q195 124 269 133" stroke-dasharray="2 5"/>
    </g>
    <g fill="#d9ffe7">
      <circle cx="225" cy="116" r="2.5"/>
      <circle cx="269" cy="133" r="3"/>
      <circle cx="237" cy="175" r="3"/>
      <circle cx="288" cy="173" r="2"/>
      <circle cx="221" cy="213" r="2"/>
      <circle cx="283" cy="236" r="3"/>
      <circle cx="163" cy="187" r="2"/>
    </g>
    <path d="M237 92c18 0 28 8 34 19M111 230c11 20 29 33 48 38" fill="none" stroke="#f3e4c5" stroke-width="5" stroke-linecap="round" opacity=".22"/>
  </g>

  <path d="M201 80c-1-16 0-30 9-43" fill="none" stroke="#e5d69d" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M203 63c-16 0-24-10-24-21 17 0 25 8 24 21z" fill="#8ebf91"/>
  <path d="M206 52c-1-15 9-23 23-22-1 14-9 22-23 22z" fill="#b6d8a0"/>
  <path d="M184 47l18 15m7-13 14-14" fill="none" stroke="#355e59" stroke-width=".9"/>

  <g fill="none" stroke="#f2cc8d">
    <path d="M85 268c43 38 110 48 160 34" stroke-opacity=".35"/>
    <circle cx="247" cy="301" r="3" fill="#f2cc8d" stroke="none"/>
  </g>

  <path d="M0 346l43-32 21-34c4-7 11-6 13-1l-10 27 35-23 19-33c4-8 12-7 14-1 1 4-4 15-9 27l-12 19 37-8 29 5c8 2 8 10 1 13l-39 5-41 27-27 27-26 36H0z" fill="url(#handA)"/>
  <path d="M400 346l-43-32-21-34c-4-7-11-6-13-1l10 27-35-23-19-33c-4-8-12-7-14-1-1 4 4 15 9 27l12 19-37-8-29 5c-8 2-8 10-1 13l39 5 41 27 27 27 26 36h48z" fill="url(#handB)"/>
  <g fill="none" stroke-linecap="round">
    <path d="M28 362l53-41 27-7m-42-8-15 23m62-34 18-4m-29 47 24-17" stroke="#723e53" stroke-width="1.5" opacity=".6"/>
    <path d="M372 362l-53-41-27-7m42-8 15 23m-62-34-18-4m29 47-24-17" stroke="#28546b" stroke-width="1.5" opacity=".7"/>
    <path d="M118 267l8-17m47 47-25-3M282 267l-8-17m-47 47 25-3" stroke="#ffe5ba" stroke-width="2" opacity=".55"/>
  </g>

  <path d="M174 342c10 8 42 8 52 0" fill="none" stroke="#adcfc0" stroke-opacity=".25"/>
  <g fill="#f3d28f">
    <circle cx="200" cy="324" r="2"/>
    <circle cx="188" cy="359" r="1"/>
    <circle cx="214" cy="369" r="1.2"/>
  </g>
  <path d="M194 323h12" stroke="#f3d28f" stroke-opacity=".35"/>
  <path d="M200 318v12" stroke="#f3d28f" stroke-opacity=".35"/>
  <circle cx="200" cy="324" r="5" fill="#f3d28f" opacity=".25" filter="url(#glow)"/>
</svg>