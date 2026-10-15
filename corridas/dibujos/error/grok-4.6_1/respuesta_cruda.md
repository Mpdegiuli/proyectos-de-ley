<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="sky" cx="38%" cy="32%" r="78%">
      <stop offset="0%" stop-color="#2a1848"/>
      <stop offset="45%" stop-color="#120c22"/>
      <stop offset="100%" stop-color="#05040a"/>
    </radialGradient>
    <radialGradient id="cer" cx="36%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#fff6e8"/>
      <stop offset="38%" stop-color="#ead9b8"/>
      <stop offset="72%" stop-color="#c4a57a"/>
      <stop offset="100%" stop-color="#8f6e4a"/>
    </radialGradient>
    <radialGradient id="inn" cx="50%" cy="20%" r="80%">
      <stop offset="0%" stop-color="#5a4033"/>
      <stop offset="100%" stop-color="#1c1210"/>
    </radialGradient>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fff4c2"/>
      <stop offset="35%" stop-color="#f0c14d"/>
      <stop offset="100%" stop-color="#9a6b18"/>
    </linearGradient>
    <linearGradient id="g2" x1="1" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffe9a0"/>
      <stop offset="100%" stop-color="#c48922"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2.2" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="halo" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6"/>
    </filter>
    <clipPath id="bowl">
      <path d="M78,168 C72,168 68,176 72,186 C86,248 128,308 200,318 C272,308 314,248 328,186 C332,176 328,168 322,168 C300,162 248,156 200,156 C152,156 100,162 78,168 Z"/>
    </clipPath>
  </defs>
  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="148" cy="108" r="90" fill="#c45a2a" opacity=".08" filter="url(#halo)"/>
  <g fill="#f4e8c8">
    <circle cx="42" cy="48" r="1.1" opacity=".7"/>
    <circle cx="88" cy="26" r=".7" opacity=".45"/>
    <circle cx="310" cy="38" r="1.3" opacity=".8"/>
    <circle cx="356" cy="72" r=".6" opacity=".4"/>
    <circle cx="368" cy="140" r="1" opacity=".55"/>
    <circle cx="28" cy="160" r=".8" opacity=".5"/>
    <circle cx="60" cy="320" r=".7" opacity=".35"/>
    <circle cx="340" cy="300" r="1.1" opacity=".5"/>
    <circle cx="380" cy="240" r=".5" opacity=".4"/>
    <circle cx="18" cy="250" r=".6" opacity=".3"/>
    <circle cx="200" cy="22" r=".8" opacity=".55"/>
    <circle cx="250" cy="58" r=".5" opacity=".35"/>
    <circle cx="120" cy="44" r=".4" opacity=".3"/>
  </g>
  <ellipse cx="200" cy="332" rx="118" ry="16" fill="#000" opacity=".35" filter="url(#soft)"/>
  <path d="M84,170 C70,176 66,188 74,202 C90,258 130,312 200,322 C270,312 310,258 326,202 C334,188 330,176 316,170" fill="none" stroke="#3a2418" stroke-width="10" opacity=".25"/>
  <path d="M78,168 C72,168 68,176 72,186 C86,248 128,308 200,318 C272,308 314,248 328,186 C332,176 328,168 322,168 C300,162 248,156 200,156 C152,156 100,162 78,168 Z" fill="url(#cer)"/>
  <ellipse cx="200" cy="168" rx="122" ry="22" fill="#d8c4a4"/>
  <ellipse cx="200" cy="166" rx="108" ry="18" fill="url(#inn)"/>
  <ellipse cx="200" cy="164" rx="96" ry="12" fill="#2a1814" opacity=".55"/>
  <g clip-path="url(#bowl)">
    <path d="M200,156 C210,210 168,236 186,318" fill="none" stroke="url(#g)" stroke-width="3.2" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M186,236 C230,228 258,268 322,188" fill="none" stroke="url(#g2)" stroke-width="2.6" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M196,198 C150,206 128,250 92,214" fill="none" stroke="url(#g)" stroke-width="2.4" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M172,268 C148,278 160,300 128,302" fill="none" stroke="url(#g2)" stroke-width="2.1" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M214,176 C240,190 236,214 228,248" fill="none" stroke="url(#g)" stroke-width="1.8" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M98,196 C110,188 118,198 124,210" fill="none" stroke="url(#g2)" stroke-width="1.6" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M248,292 C260,280 278,286 292,264" fill="none" stroke="url(#g)" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M200,156 C188,192 206,220 198,250" fill="none" stroke="#fff3c0" stroke-width=".7" stroke-linecap="round" opacity=".7"/>
  </g>
  <path d="M186,236 C230,228 258,268 318,190" fill="none" stroke="url(#g)" stroke-width="2.2" stroke-linecap="round" filter="url(#glow)" clip-path="url(#bowl)"/>
  <ellipse cx="200" cy="168" rx="122" ry="22" fill="none" stroke="#f0e0c4" stroke-width="2.4"/>
  <ellipse cx="200" cy="166" rx="108" ry="18" fill="none" stroke="#6a5040" stroke-width="1.2"/>
  <path d="M92,168 C130,158 270,158 308,168" fill="none" stroke="#fff" stroke-width="1.6" opacity=".28" stroke-linecap="round"/>
  <g filter="url(#glow)" opacity=".9">
    <path d="M132,338 C136,332 144,334 146,340 C142,346 134,346 132,338 Z" fill="url(#g)"/>
    <path d="M248,344 C252,338 262,340 262,348 C256,352 248,350 248,344 Z" fill="url(#g2)"/>
    <path d="M176,350 C178,346 186,346 186,352 C182,356 174,354 176,350 Z" fill="url(#g)"/>
    <circle cx="214" cy="342" r="3.2" fill="#e8b84a"/>
    <circle cx="300" cy="336" r="2.2" fill="#f0c14d"/>
    <circle cx="108" cy="346" r="1.8" fill="#d4a017"/>
  </g>
  <circle cx="318" cy="96" r="3" fill="#f4e8c8" opacity=".25"/>
  <path d="M74,168 C70,172 76,176 82,170" fill="none" stroke="url(#g)" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>
  <path d="M318,172 C324,176 330,170 326,166" fill="none" stroke="url(#g2)" stroke-width="1.8" stroke-linecap="round" filter="url(#glow)"/>
</svg>