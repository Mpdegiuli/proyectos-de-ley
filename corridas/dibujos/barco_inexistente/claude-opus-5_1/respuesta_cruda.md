```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b1033"/>
      <stop offset="45%" stop-color="#23306b"/>
      <stop offset="80%" stop-color="#5b5a93"/>
      <stop offset="100%" stop-color="#9a7fa0"/>
    </linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a3a70"/>
      <stop offset="60%" stop-color="#141c45"/>
      <stop offset="100%" stop-color="#070b22"/>
    </linearGradient>
    <linearGradient id="sail" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fdf3dc"/>
      <stop offset="60%" stop-color="#e8cfa4"/>
      <stop offset="100%" stop-color="#c9a87c"/>
    </linearGradient>
    <linearGradient id="sail2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f6e4c8"/>
      <stop offset="100%" stop-color="#b8906a"/>
    </linearGradient>
    <linearGradient id="hull" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8a5a33"/>
      <stop offset="55%" stop-color="#5a3620"/>
      <stop offset="100%" stop-color="#2b1810"/>
    </linearGradient>
    <radialGradient id="moonGlow">
      <stop offset="0%" stop-color="#fff6d8" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#fff6d8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="lamp">
      <stop offset="0%" stop-color="#fff3b0"/>
      <stop offset="40%" stop-color="#ffc94d" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ffb300" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="312" cy="78" r="62" fill="url(#moonGlow)"/>
  <circle cx="312" cy="78" r="26" fill="#fdf6d9"/>
  <circle cx="320" cy="72" r="5" fill="#eadfbd" opacity="0.7"/>
  <circle cx="305" cy="88" r="7" fill="#eadfbd" opacity="0.5"/>

  <g fill="#fff8e0">
    <circle cx="40" cy="40" r="1.6"/><circle cx="88" cy="22" r="1.1"/>
    <circle cx="130" cy="58" r="1.5"/><circle cx="196" cy="28" r="1.2"/>
    <circle cx="250" cy="52" r="1"/><circle cx="60" cy="110" r="1.3"/>
    <circle cx="22" cy="166" r="1.1"/><circle cx="370" cy="140" r="1.4"/>
    <circle cx="352" cy="36" r="1"/><circle cx="160" cy="100" r="1"/>
    <circle cx="290" cy="170" r="1.2"/><circle cx="112" cy="150" r="1"/>
  </g>

  <path d="M0 300 Q60 288 120 298 Q180 308 240 296 Q310 284 400 298 L400 400 L0 400 Z" fill="url(#sea)"/>

  <g opacity="0.5" stroke="#d9c6e8" fill="none" stroke-linecap="round">
    <path d="M250 320 q18 -6 36 0" stroke-width="2"/>
    <path d="M296 338 q22 -7 44 0" stroke-width="2"/>
    <path d="M40 330 q20 -7 40 0" stroke-width="1.8"/>
    <path d="M90 356 q26 -8 52 0" stroke-width="2"/>
    <path d="M220 370 q30 -9 60 0" stroke-width="2.2"/>
    <path d="M18 382 q24 -8 48 0" stroke-width="1.6"/>
  </g>

  <ellipse cx="200" cy="306" rx="118" ry="12" fill="#0b1030" opacity="0.45"/>

  <g>
    <!-- mástiles -->
    <path d="M152 258 L150 118" stroke="#6b4426" stroke-width="5" stroke-linecap="round"/>
    <path d="M208 262 L206 72" stroke="#7a4d2b" stroke-width="6" stroke-linecap="round"/>
    <path d="M262 256 L266 130" stroke="#6b4426" stroke-width="5" stroke-linecap="round"/>
    <!-- vergas -->
    <g stroke="#53331d" stroke-width="3" stroke-linecap="round">
      <path d="M126 140 L188 136"/><path d="M180 96 L238 92"/>
      <path d="M176 170 L244 166"/><path d="M240 148 L296 146"/>
    </g>

    <!-- velas -->
    <path d="M150 136 C196 152 198 196 176 232 L150 232 Z" fill="url(#sail)" stroke="#a9825a" stroke-width="1"/>
    <path d="M150 136 C112 150 110 198 128 232 L150 232 Z" fill="url(#sail2)" opacity="0.92" stroke="#a9825a" stroke-width="1"/>
    <path d="M206 92 C264 116 268 184 240 236 L206 236 Z" fill="url(#sail)" stroke="#a9825a" stroke-width="1"/>
    <path d="M206 92 C156 114 152 188 176 236 L206 236 Z" fill="url(#sail2)" opacity="0.92" stroke="#a9825a" stroke-width="1"/>
    <path d="M266 146 C306 162 306 206 288 234 L266 234 Z" fill="url(#sail)" stroke="#a9825a" stroke-width="1"/>
    <path d="M266 146 C232 164 232 206 246 234 L266 234 Z" fill="url(#sail2)" opacity="0.9" stroke="#a9825a" stroke-width="1"/>
    <g stroke="#b08d64" stroke-width="0.8" opacity="0.6" fill="none">
      <path d="M160 160 C196 176 194 200 182 218"/>
      <path d="M216 120 C254 142 254 190 236 220"/>
      <path d="M196 120 C168 144 166 196 180 222"/>
    </g>

    <!-- jarcias -->
    <g stroke="#e6dcc5" stroke-width="0.7" opacity="0.55" fill="none">
      <path d="M206 78 L112 250"/><path d="M206 78 L300 248"/>
      <path d="M150 120 L104 252"/><path d="M266 132 L306 244"/>
      <path d="M206 78 L330 212"/>
    </g>

    <!-- banderas -->
    <path d="M206 70 L250 80 L206 90 Z" fill="#e0476b"/>
    <path d="M150 116 L182 124 L150 132 Z" fill="#4fc0c0"/>
    <path d="M266 128 L294 135 L266 142 Z" fill="#f0a93b"/>

    <!-- casco -->
    <path d="M86 252 Q200 350 318 252 Q200 300 86 252 Z" fill="url(#hull)"/>
    <path d="M86 252 Q200 300 318 252 L322 240 Q200 290 82 240 Z" fill="#9a6a3c"/>
    <path d="M82 240 Q200 290 322 240" fill="none" stroke="#e9c892" stroke-width="2.5"/>
    <path d="M92 262 Q200 320 312 262" fill="none" stroke="#c89a62" stroke-width="1.6" opacity="0.7"/>

    <!-- proa curvada -->
    <path d="M318 252 C336 236 344 212 334 196 C330 188 320 188 318 196 C316 206 326 210 330 204"
          fill="none" stroke="#9a6a3c" stroke-width="7" stroke-linecap="round"/>
    <!-- popa curvada -->
    <path d="M86 252 C70 240 64 220 74 208 C80 200 90 204 88 212"
          fill="none" stroke="#9a6a3c" stroke-width="7" stroke-linecap="round"/>

    <!-- ojos de buey -->
    <g>
      <circle cx="150" cy="256" r="4.5" fill="#ffd47a"/>
      <circle cx="182" cy="262" r="4.5" fill="#ffd47a"/>
      <circle cx="214" cy="264" r="4.5" fill="#ffd47a"/>
      <circle cx="246" cy="261" r="4.5" fill="#ffd47a"/>
      <circle cx="276" cy="255" r="4.5" fill="#ffd47a"/>
    </g>

    <!-- farol -->
    <circle cx="206" cy="66" r="14" fill="url(#lamp)"/>
    <circle cx="206" cy="66" r="4" fill="#fff6c2"/>
    <circle cx="94" cy="236" r="12" fill="url(#lamp)"/>
    <circle cx="94" cy="236" r="3.4" fill="#fff6c2"/>
  </g>

  <g opacity="0.65" stroke="#dfd0ef" fill="none" stroke-linecap="round">
    <path d="M70 282 q22 -8 44 -1" stroke-width="2.4"/>
    <path d="M286 280 q24 -9 48 -1" stroke-width="2.4"/>
    <path d="M150 292 q30 -9 60 -1" stroke-width="2"/>
  </g>
</svg>
```