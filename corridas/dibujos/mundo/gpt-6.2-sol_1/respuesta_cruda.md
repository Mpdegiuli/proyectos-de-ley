<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-labelledby="titulo descripcion">
  <title id="titulo">El mundo, en reparación</title>
  <desc id="descripcion">Un planeta de mares azules y ciudades encendidas. Una grieta lo atraviesa y unas puntadas doradas mantienen unidos sus bordes. En la última puntada nace un brote.</desc>
  <defs>
    <linearGradient id="cielo" x2="0.8" y2="1">
      <stop stop-color="#111b33"/>
      <stop offset="1" stop-color="#1e1028"/>
    </linearGradient>
    <linearGradient id="mar" x1=".1" y1=".1" x2=".85" y2=".9">
      <stop stop-color="#308da4"/>
      <stop offset=".55" stop-color="#235776"/>
      <stop offset="1" stop-color="#232644"/>
    </linearGradient>
    <linearGradient id="tierra" x2=".8" y2="1">
      <stop stop-color="#a8bd8e"/>
      <stop offset=".55" stop-color="#498f80"/>
      <stop offset="1" stop-color="#406677"/>
    </linearGradient>
    <radialGradient id="halo">
      <stop offset=".62" stop-color="#6de5e0" stop-opacity="0"/>
      <stop offset=".76" stop-color="#6de5e0" stop-opacity=".19"/>
      <stop offset="1" stop-color="#6de5e0" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="luz">
      <stop stop-color="#ffe7a1" stop-opacity=".6"/>
      <stop offset="1" stop-color="#ffb16f" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="disco">
      <circle cx="200" cy="194" r="119"/>
    </clipPath>
    <pattern id="trama" width="5" height="5" patternUnits="userSpaceOnUse">
      <path d="M0 1h1m2 3h1" stroke="#fff4dc" stroke-opacity=".09" stroke-width=".5"/>
    </pattern>
  </defs>

  <path fill="url(#cielo)" d="M0 0h400v400H0z"/>
  <path d="M25 31h350v338H25z" fill="none" stroke="#adacc9" stroke-opacity=".21"/>
  <path d="M25 43V31h12m326 0h12v12m0 314v12h-12m-326 0H25v-12" fill="none" stroke="#c1a7bf" stroke-opacity=".6"/>

  <g fill="#e9d6c6">
    <circle cx="55" cy="93" r="1.2"/><circle cx="88" cy="67" r=".7"/>
    <circle cx="137" cy="52" r="1"/><circle cx="260" cy="63" r=".8"/>
    <circle cx="349" cy="124" r="1.3"/><circle cx="349" cy="75" r=".8"/>
    <circle cx="315" cy="64" r=".8"/><circle cx="59" cy="237" r=".9"/>
    <circle cx="47" cy="181" r=".7"/><circle cx="66" cy="296" r="1.1"/>
    <circle cx="107" cy="326" r=".8"/><circle cx="312" cy="311" r="1"/>
    <circle cx="352" cy="269" r=".7"/><circle cx="363" cy="213" r="1"/>
  </g>
  <path d="M63 119v10m-5-5h10m269 163v8m-4-4h8M291 51v8m-4-4h8" fill="none" stroke="#d7aab5" stroke-width=".8"/>

  <circle cx="200" cy="194" r="160" fill="url(#halo)"/>
  <circle cx="200" cy="194" r="119" fill="url(#mar)" stroke="#85cfcc" stroke-width="1.3"/>
  <g clip-path="url(#disco)">
    <g fill="none" stroke="#a2e0da" stroke-opacity=".22">
      <ellipse cx="200" cy="194" rx="87" ry="119"/>
      <ellipse cx="200" cy="194" rx="42" ry="119"/>
      <path d="M200 75v238M81 194h238M97 136q103 37 206 0M97 252q103-37 206 0M130 98q70 25 140 0M130 290q70-25 140 0"/>
    </g>
    <g fill="url(#tierra)">
      <path d="M80 139l19-10 13 2 5-10 17-4 6-12 14 3 11-9 17 3 5 8-14 8-10 1-2 11-14 9-3 10 9 4-6 8-12-4-4-11-10 3-6 8 5 11 15 7 7 12 11 5-9 4-13-8-7-12-12-4-12-17-16-2z"/>
      <path d="M150 192l13-3 8 9 16 2 9 10-8 17-10 7-1 13-10 7-3 17-10 10-6-4 5-17-3-15 4-12-9-14-3-14z"/>
      <path d="M176 103l11-13 22-5 15 6-2 10-14 7-3 11-14 7-8-5 4-11z"/>
      <path d="M229 127l8-15 16-1 16-9 32 7 17 21 5 39-13 4-13-11-15 7-6 13-9-4-9-15-10 2-9-6-8 4-9-10-13 2-3-8 12-8 5-10z"/>
      <path d="M214 163l16-2 13 12 13 5-1 11-10 8-5 19-13 12-10-8-1-14-9-9-8-6 4-16z"/>
      <path d="M279 215l10-7 4-9 7 3-1 14 10 10-5 7-13-5-16 4-7-6zM269 192l9 5 9-1 2 5-12 2-9-7zM251 210l4 1-4 12-4 2z"/>
      <path d="M97 292l20-9 17 3 13 7 16-1 13 8 25-2 10 6 29-7 18 3 16-7 23 1v26H97z" opacity=".63"/>
    </g>
    <path d="M78 161q38-16 67-5t59-4m45 81q30-15 68-10M165 275q32-8 48-3" fill="none" stroke="#e4f0d3" stroke-opacity=".28" stroke-width="2" stroke-linecap="round"/>
    <g fill="url(#luz)">
      <circle cx="139" cy="139" r="24"/><circle cx="231" cy="147" r="24"/>
      <circle cx="284" cy="153" r="26"/><circle cx="174" cy="215" r="18"/>
    </g>
    <g fill="#ffe2a3">
      <circle cx="135" cy="138" r="2"/><circle cx="140" cy="134" r="1.1"/><circle cx="144" cy="137" r="1.3"/><circle cx="142" cy="143" r=".8"/><circle cx="119" cy="152" r="1.1"/>
      <circle cx="229" cy="147" r="1.8"/><circle cx="235" cy="143" r="1.1"/><circle cx="231" cy="151" r=".9"/><circle cx="239" cy="149" r="1.4"/>
      <circle cx="284" cy="153" r="1.8"/><circle cx="290" cy="151" r="1.1"/><circle cx="286" cy="159" r="1.2"/><circle cx="276" cy="157" r=".8"/>
      <circle cx="174" cy="215" r="1.6"/><circle cx="172" cy="221" r=".9"/><circle cx="182" cy="210" r="1"/>
      <circle cx="243" cy="190" r="1"/><circle cx="285" cy="224" r="1.2"/>
    </g>
    <circle cx="200" cy="194" r="119" fill="url(#trama)"/>
    <path d="M204 72l-8 24 9 18-17 21 10 22-6 20 15 16-13 19 4 20-13 15 12 19-6 23 8 26" fill="none" stroke="#13162b" stroke-width="5" stroke-linejoin="round"/>
    <path d="M190 136l-12 6-11-3-8 5m47 48 14 1 9 8 10-1m-45 87-15-3-8 4" fill="none" stroke="#13162b" stroke-width="1.8" stroke-linecap="round"/>
    <path d="M206 74l-7 22 9 18-17 21 10 22-6 19 15 17-13 20 4 19-13 15 12 18-6 24 8 24" fill="none" stroke="#e29591" stroke-opacity=".6" stroke-width="1"/>
  </g>

  <g fill="none" stroke-linecap="round">
    <path d="M184 110l27-11m-32 56 30-12m-16 52 26-13m-37 56 29-13m-34 53 31-13" stroke="#111526" stroke-width="5"/>
    <path d="M184 108q12 1 27-11m-32 56q16 0 30-12m-16 52q13 0 26-13m-37 56q16 0 29-13m-34 53q17-1 31-13" stroke="#ffd48e" stroke-width="2.6"/>
    <path d="M208 263c23-13 34-7 47 5 21 19 43 20 62 7 10-7 17-17 21-30" stroke="#ffd48e" stroke-width="1.5"/>
    <path d="M338 245q7-12 4-21" stroke="#c5d995" stroke-width="1.5"/>
  </g>
  <path d="M341 233q-15-2-17-16 15 1 17 16z" fill="#93bc95"/>
  <path d="M343 228q-1-14 14-20-1 15-14 20z" fill="#d1df9c"/>

  <path d="M179 336h42" stroke="#c99592" stroke-opacity=".65"/>
  <text x="200" y="354" text-anchor="middle" fill="#efdbcc" font-family="sans-serif" font-size="9" letter-spacing="3">EN REPARACIÓN</text>
</svg>