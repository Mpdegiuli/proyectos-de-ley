<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-labelledby="title desc">
  <title id="title">Un mundo agrietado, todavía vivo</title>
  <desc id="desc">La Tierra, entre incendios y brotes, tiene sus grietas unidas por luz. Una red de conexiones la rodea y varias personas sostienen juntas su horizonte.</desc>
  <defs>
    <radialGradient id="night" cx="50%" cy="43%" r="72%">
      <stop stop-color="#213d51"/>
      <stop offset=".58" stop-color="#102333"/>
      <stop offset="1" stop-color="#080f20"/>
    </radialGradient>
    <linearGradient id="ocean" x1="0" y1="1" x2="1" y2="0">
      <stop stop-color="#263a56"/>
      <stop offset=".48" stop-color="#196779"/>
      <stop offset="1" stop-color="#69b6b0"/>
    </linearGradient>
    <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#e7b878"/>
      <stop offset=".4" stop-color="#a9c398"/>
      <stop offset="1" stop-color="#4c9d87"/>
    </linearGradient>
    <linearGradient id="heat">
      <stop stop-color="#f37548" stop-opacity=".75"/>
      <stop offset="1" stop-color="#f37548" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hands" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#e7bda0"/>
      <stop offset="1" stop-color="#8a6675"/>
    </linearGradient>
    <radialGradient id="halo">
      <stop stop-color="#63dfc5" stop-opacity=".2"/>
      <stop offset="1" stop-color="#63dfc5" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
    <clipPath id="world">
      <circle cx="200" cy="185" r="108"/>
    </clipPath>
  </defs>

  <path fill="url(#night)" d="M0 0h400v400H0z"/>
  <circle cx="204" cy="189" r="177" fill="url(#halo)"/>

  <g fill="#dae9dd">
    <circle cx="36" cy="43" r="1.2" opacity=".7"/>
    <circle cx="93" cy="28" r=".8"/>
    <circle cx="162" cy="47" r="1"/>
    <circle cx="258" cy="26" r="1.4" opacity=".6"/>
    <circle cx="349" cy="47" r="1"/>
    <circle cx="373" cy="129" r="1.3"/>
    <circle cx="26" cy="182" r=".9"/>
    <circle cx="52" cy="266" r="1"/>
    <circle cx="357" cy="274" r=".8"/>
    <circle cx="330" cy="335" r="1.1"/>
    <circle cx="65" cy="353" r=".8"/>
  </g>
  <path d="M308 57v10m-5-5h10M62 115v8m-4-4h8" stroke="#d4e8d7" stroke-width="1" opacity=".6"/>

  <g fill="none" stroke="#77b8b4" stroke-width=".8">
    <ellipse cx="200" cy="190" rx="172" ry="69" transform="rotate(-28 200 190)" opacity=".3"/>
    <ellipse cx="200" cy="190" rx="158" ry="116" transform="rotate(29 200 190)" opacity=".18" stroke-dasharray="3 7"/>
    <path d="M47 150 86 75 181 59 303 100 353 222 291 297 122 303 47 150" opacity=".15"/>
  </g>
  <g fill="#e4c788">
    <circle cx="86" cy="75" r="3"/>
    <circle cx="353" cy="222" r="3"/>
    <circle cx="122" cy="303" r="2.5"/>
  </g>
  <g transform="translate(316 92) rotate(30)">
    <path d="M-20-8h13v16h-13zm27 0h13v16H7z" fill="#518292" stroke="#b9d3ce" stroke-width=".7"/>
    <path d="M-16-8V8m5-16V8M11-8V8m5-16V8" stroke="#bad2c8" stroke-width=".5"/>
    <path d="M-6-5H6V5H-6z" fill="#e5c68e"/>
    <path d="M0-5v-8m-3 0h6" stroke="#e5c68e"/>
  </g>

  <circle cx="200" cy="185" r="111" fill="none" stroke="#90e3d0" stroke-opacity=".18" stroke-width="5"/>
  <g clip-path="url(#world)">
    <circle cx="200" cy="185" r="108" fill="url(#ocean)"/>
    <g fill="none" stroke="#c0eee2" stroke-width=".7" opacity=".19">
      <ellipse cx="200" cy="185" rx="46" ry="108"/>
      <ellipse cx="200" cy="185" rx="87" ry="108"/>
      <ellipse cx="200" cy="185" rx="108" ry="35"/>
      <ellipse cx="200" cy="185" rx="108" ry="75"/>
      <path d="M92 185h216M200 77v216"/>
    </g>

    <g fill="url(#land)" stroke="#bad8ac" stroke-width=".6" stroke-linejoin="round">
      <path d="m105 122 15-16 18-4 8 7 19-9 16 10-4 12-13 7-3 12-17 2-6 14 8 13-9 8-8-13-11-4-8-16-10-4z"/>
      <path d="m147 174 16 6 12 18 14 6-3 18-11 12-4 24-10 15-7-16 1-17-10-17-2-21-8-13z"/>
      <path d="m177 91 17-9 15 7-7 16-15 5-10-7z"/>
      <path d="m207 127 13-11 17 3 6-12 22 2 11-10 31 25-3 28-17-2-10 13-13-6-9 10-13-7-6-15-15 4-10-7-9 4-7-7z"/>
      <path d="m214 150 20 3 15 18 5 17-11 15-5 22-13 9-10-19-2-21-11-12-5-18z"/>
      <path d="m259 174 10 11 3 14-8 5-7-13-8-9z"/>
      <path d="m275 211 17-6 17 12-3 20-14 9-21-5-5-15z"/>
      <path d="m242 227 5 7-2 13-5-4z"/>
      <path d="m116 280 41-3 23 7 33-5 18 4 33-9 24 12-36 17-97-1z"/>
    </g>

    <path d="M85 77h132v223H85z" fill="url(#heat)"/>

    <g fill="none" stroke="#e9f1dd" stroke-linecap="round" opacity=".5">
      <path d="M115 127q10-8 23-2m-18 5 25 1" stroke-width="3"/>
      <path d="M231 101q16-8 32 0m-22 5h31" stroke-width="3"/>
      <path d="M264 249q15-6 28-2" stroke-width="2"/>
      <path d="M183 251q13-5 24 1" stroke-width="2"/>
    </g>

    <g fill="#f6954c">
      <path d="M124 151q-8-8 0-20-1 7 5 8 5-5 3-9 12 16 1 22z"/>
      <path d="M156 213q-9-7-1-20 0 7 5 9l3-10q12 14 2 23z"/>
    </g>
    <g fill="#ffd48a">
      <path d="M125 150q-4-5 2-10 0 5 4 5l-1 6z"/>
      <path d="M157 213q-3-5 2-9l4 10z"/>
    </g>
    <g fill="none" stroke="#e1b59e" opacity=".3" stroke-width="3" stroke-linecap="round">
      <path d="M125 122q-9-9-1-18t-3-16"/>
      <path d="M157 185q-8-7-3-15"/>
    </g>

    <path d="m203 78-12 33 16 23-14 25 18 22-13 21 13 19-19 29 12 19-5 24" fill="none" stroke="#122e3b" stroke-width="9" stroke-linejoin="round"/>
    <g fill="none" stroke="#ffcf79" stroke-linejoin="round">
      <path d="m203 78-12 33 16 23-14 25 18 22-13 21 13 19-19 29 12 19-5 24" stroke-width="5" filter="url(#glow)" opacity=".7"/>
      <path d="m203 78-12 33 16 23-14 25 18 22-13 21 13 19-19 29 12 19-5 24" stroke-width="2.3"/>
      <path d="m193 159-15-5-7-14m40 81 18 4 10 12m-32-103 16 2 7-8" stroke-width="1.3"/>
    </g>
    <g fill="#fff1b7">
      <circle cx="193" cy="159" r="2.8"/>
      <circle cx="211" cy="221" r="2.5"/>
      <circle cx="191" cy="111" r="2"/>
    </g>

    <g stroke="#153e3b" stroke-width="2" fill="#9fdb9b">
      <path d="M273 148v-23"/>
      <path d="M273 137q-15 0-16-12 14-2 16 12z"/>
      <path d="M273 130q0-14 14-16 2 13-14 16z"/>
      <path d="M284 234v-15"/>
      <path d="M284 226q-11-1-11-9 10-1 11 9z"/>
      <path d="M284 221q1-10 11-10 0 10-11 10z"/>
    </g>
  </g>
  <circle cx="200" cy="185" r="108" fill="none" stroke="#d0edda" stroke-width="1.2" opacity=".6"/>

  <g fill="none" stroke="#78b9b0" stroke-linecap="round">
    <path d="M318 286v-48m0 1-15-9m15 9 16-9m-16 9v-18" stroke-width="2"/>
    <circle cx="318" cy="239" r="2" fill="#d1ddbc"/>
    <path d="M344 300v-36m0 0-12-6m12 6 12-8m-12 8-2-15" stroke-width="1.5"/>
  </g>
  <g fill="#26394b" stroke="#795962" stroke-width=".7">
    <path d="M41 284v-29h15v-19h7v22h14v-31h8v28h9v29z"/>
    <path d="M59 235v-16h4v16m16-10v-18h5v18"/>
  </g>
  <path d="M61 214q-14-12-5-23t-5-24m31 35q-9-9-3-16" fill="none" stroke="#be8275" stroke-width="4" opacity=".2" stroke-linecap="round"/>

  <path d="M98 400 86 349q-3-12 3-21l30-46q5-6 9-2 4 3 0 10l-15 26q-3 6 2 8 5 2 9-4l24-25q8-8 13-3 4 5-3 12l-18 25q-5 9-1 19l20 52z" fill="url(#hands)"/>
  <path d="m302 400 12-51q3-12-3-21l-30-46q-5-6-9-2-4 3 0 10l15 26q3 6-2 8-5 2-9-4l-24-25q-8-8-13-3-4 5 3 12l18 25q5 9 1 19l-20 52z" fill="url(#hands)"/>
  <path d="M92 344q11-7 23-4m-18 15q11-7 21-4m190-7q-11-7-23-4m18 15q-11-7-21-4" fill="none" stroke="#725b70" stroke-width="1.3" opacity=".5"/>

  <path d="M139 326q61 16 122 0" fill="none" stroke="#edcf9b" stroke-width="2"/>
  <g stroke="#edcf9b" stroke-width="2" stroke-linecap="round" fill="none">
    <path d="m163 326 3-15 6-1 4 18m-10-11-10 3m15-6 9 8"/>
    <path d="m193 330 2-15h8l4 16m-12-13-15 4m23-4 13 4"/>
    <path d="m226 329 2-18 6-1 4 17m-10-13-12 8m18-8 11 4"/>
  </g>
  <g fill="#edcf9b">
    <circle cx="169" cy="304" r="4"/>
    <circle cx="199" cy="307" r="4"/>
    <circle cx="231" cy="303" r="4"/>
  </g>

  <path d="M200 378v-29" fill="none" stroke="#87c9a0" stroke-width="2"/>
  <path d="M200 364q-19 0-22-15 18-1 22 15zm0-8q2-18 21-21-1 19-21 21z" fill="#87c9a0"/>
  <path d="m180 350 20 14 19-27" fill="none" stroke="#c8e6b3" stroke-width=".8"/>
  <ellipse cx="200" cy="380" rx="31" ry="2" fill="#a4d8b6" opacity=".17"/>
</svg>