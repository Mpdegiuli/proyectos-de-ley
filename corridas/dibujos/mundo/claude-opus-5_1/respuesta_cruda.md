<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#17243f"/>
      <stop offset="60%" stop-color="#0c1428"/>
      <stop offset="100%" stop-color="#05070f"/>
    </radialGradient>
    <radialGradient id="ocean" cx="38%" cy="32%" r="80%">
      <stop offset="0%" stop-color="#1d4e78"/>
      <stop offset="70%" stop-color="#102a46"/>
      <stop offset="100%" stop-color="#081626"/>
    </radialGradient>
    <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#46a97a"/>
      <stop offset="100%" stop-color="#1f6b52"/>
    </linearGradient>
    <linearGradient id="dry" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#c88a45"/>
      <stop offset="100%" stop-color="#7d4f2c"/>
    </linearGradient>
    <filter id="glow" x="-70%" y="-70%" width="240%" height="240%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="8"/>
    </filter>
    <clipPath id="globe"><circle cx="200" cy="180" r="115"/></clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#cfe4ff">
    <circle cx="34" cy="42" r="1.3" opacity=".8"/><circle cx="72" cy="22" r="1" opacity=".5"/>
    <circle cx="118" cy="55" r="1.6" opacity=".7"/><circle cx="330" cy="36" r="1.4" opacity=".8"/>
    <circle cx="368" cy="78" r="1" opacity=".5"/><circle cx="286" cy="24" r="1.1" opacity=".6"/>
    <circle cx="22" cy="140" r="1.2" opacity=".6"/><circle cx="378" cy="168" r="1.3" opacity=".6"/>
    <circle cx="58" cy="300" r="1" opacity=".45"/><circle cx="352" cy="286" r="1.2" opacity=".5"/>
    <circle cx="160" cy="18" r="1" opacity=".45"/><circle cx="240" cy="44" r="1.2" opacity=".55"/>
  </g>

  <circle cx="200" cy="180" r="140" fill="#3b7fc4" opacity=".16" filter="url(#soft)"/>

  <circle cx="200" cy="180" r="115" fill="url(#ocean)"/>

  <g clip-path="url(#globe)">
    <path d="M118,118 C142,96 176,102 192,120 C206,136 196,164 172,174 C148,184 120,172 112,150 Z" fill="url(#land)"/>
    <path d="M212,100 C244,88 282,106 288,132 C294,160 264,178 236,170 C214,164 198,132 212,100 Z" fill="url(#dry)" opacity=".92"/>
    <path d="M146,200 C172,188 200,204 206,230 C212,258 190,280 168,274 C146,268 136,230 146,200 Z" fill="url(#land)"/>
    <path d="M232,196 C258,186 280,206 276,228 C271,252 246,260 232,242 C221,228 220,204 232,196 Z" fill="url(#dry)" opacity=".85"/>
    <path d="M96,232 C112,224 126,236 122,252 C118,268 98,272 90,258 Z" fill="url(#land)" opacity=".8"/>

    <g stroke="#7fe3ff" stroke-width=".7" fill="none" opacity=".33">
      <ellipse cx="200" cy="180" rx="115" ry="38"/>
      <ellipse cx="200" cy="180" rx="115" ry="75"/>
      <ellipse cx="200" cy="180" rx="38" ry="115"/>
      <ellipse cx="200" cy="180" rx="76" ry="115"/>
      <line x1="85" y1="180" x2="315" y2="180"/>
      <line x1="200" y1="65" x2="200" y2="295"/>
    </g>

    <g stroke="#ff9a4d" stroke-width="2" fill="none" filter="url(#glow)" opacity=".9">
      <path d="M92,148 L128,162 L116,188 L158,202 L146,234 L186,248 L196,290"/>
      <path d="M158,202 L206,190 L248,206 L268,240"/>
      <path d="M128,162 L170,142 L214,152"/>
    </g>

    <g fill="#ffd7a0" filter="url(#glow)">
      <circle cx="128" cy="162" r="2.6"/><circle cx="158" cy="202" r="2.6"/>
      <circle cx="206" cy="190" r="2.2"/><circle cx="248" cy="206" r="2.2"/>
      <circle cx="170" cy="142" r="2"/><circle cx="186" cy="248" r="2.4"/>
    </g>

    <g stroke="#8ff0ff" stroke-width=".9" fill="none" opacity=".75">
      <path d="M240,120 L286,146 L262,192 L300,214"/>
      <path d="M240,120 L206,150 L162,120"/>
      <path d="M262,192 L214,230 L176,262"/>
      <path d="M286,146 L310,110"/>
    </g>
    <g fill="#bff6ff" filter="url(#glow)">
      <circle cx="240" cy="120" r="3"/><circle cx="286" cy="146" r="2.6"/>
      <circle cx="262" cy="192" r="3"/><circle cx="300" cy="214" r="2.2"/>
      <circle cx="206" cy="150" r="2.2"/><circle cx="162" cy="120" r="2.4"/>
      <circle cx="214" cy="230" r="2.6"/><circle cx="176" cy="262" r="2.2"/>
      <circle cx="310" cy="110" r="2"/>
    </g>

    <circle cx="200" cy="180" r="115" fill="none" stroke="#000" stroke-width="30" opacity=".35"/>
    <ellipse cx="150" cy="130" rx="60" ry="46" fill="#ffffff" opacity=".07"/>
  </g>

  <circle cx="200" cy="180" r="115" fill="none" stroke="#9fd8ff" stroke-width="1.2" opacity=".55"/>

  <g transform="rotate(-22 200 180)" fill="none" stroke="#9fd8ff" opacity=".45">
    <ellipse cx="200" cy="180" rx="168" ry="52" stroke-width="1" stroke-dasharray="5 9"/>
  </g>
  <g transform="rotate(-22 200 180)" fill="#e8f6ff" filter="url(#glow)">
    <circle cx="368" cy="180" r="3"/><circle cx="32" cy="180" r="2.4"/>
    <circle cx="288" cy="132" r="2"/>
  </g>

  <path d="M0,352 C70,336 130,362 200,352 C270,342 330,362 400,348 L400,400 L0,400 Z" fill="#070b16"/>
  <path d="M0,358 C70,344 130,368 200,358 C270,348 330,368 400,354 L400,400 L0,400 Z" fill="#04060d"/>

  <g fill="#0d1526" stroke="#8ff0ff" stroke-width=".6" opacity=".9">
    <g transform="translate(64,352)"><circle cy="-22" r="5"/><path d="M-7,0 C-7,-14 7,-14 7,0 Z"/></g>
    <g transform="translate(92,354)"><circle cy="-19" r="4.4"/><path d="M-6,0 C-6,-12 6,-12 6,0 Z"/></g>
    <g transform="translate(146,350)"><circle cy="-24" r="5.4"/><path d="M-8,0 C-8,-15 8,-15 8,0 Z"/></g>
    <g transform="translate(258,351)"><circle cy="-21" r="4.8"/><path d="M-7,0 C-7,-13 7,-13 7,0 Z"/></g>
    <g transform="translate(288,354)"><circle cy="-18" r="4.2"/><path d="M-6,0 C-6,-11 6,-11 6,0 Z"/></g>
    <g transform="translate(330,352)"><circle cy="-22" r="5"/><path d="M-7,0 C-7,-14 7,-14 7,0 Z"/></g>
  </g>

  <g transform="translate(200,352)">
    <path d="M0,0 L0,-34" stroke="#57c98a" stroke-width="2.4" fill="none"/>
    <path d="M0,-20 C-14,-24 -18,-36 -4,-34 C-2,-28 -1,-24 0,-20 Z" fill="#57c98a"/>
    <path d="M0,-27 C14,-31 19,-44 4,-42 C1,-36 0,-31 0,-27 Z" fill="#7fe0a4"/>
    <circle cx="0" cy="-46" r="10" fill="#ffd27f" opacity=".22" filter="url(#glow)"/>
  </g>

  <g opacity=".75" fill="#9fd8ff">
    <circle cx="112" cy="316" r="1.6"/><circle cx="182" cy="308" r="1.2"/>
    <circle cx="242" cy="320" r="1.4"/><circle cx="312" cy="312" r="1.1"/>
  </g>
</svg>