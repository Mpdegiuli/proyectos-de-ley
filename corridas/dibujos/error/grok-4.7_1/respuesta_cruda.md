<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <path id="petal" d="M0,22 C-30,12 -38,-32 -10,-70 C-3,-84 3,-84 10,-70 C38,-32 30,12 0,22 Z"/>
    <clipPath id="inv">
      <path d="M0,22 C-30,12 -38,-32 -10,-70 C-3,-84 3,-84 10,-70 C38,-32 30,12 0,22 Z" transform="translate(200,198) rotate(50) scale(1.05)"/>
    </clipPath>
    <linearGradient id="paper" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f6f0e5"/>
      <stop offset="1" stop-color="#efe3d2"/>
    </linearGradient>
    <radialGradient id="vig" cx="50%" cy="42%" r="68%">
      <stop offset="0.55" stop-color="#5c4a32" stop-opacity="0"/>
      <stop offset="1" stop-color="#5c4a32" stop-opacity="0.16"/>
    </radialGradient>
    <radialGradient id="blush" cx="200" cy="198" r="96" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#f4cfc6" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#f4cfc6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="sky" cx="250" cy="152" r="62" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#b7c4ee"/>
      <stop offset="0.22" stop-color="#6d82c4"/>
      <stop offset="0.55" stop-color="#2a386e"/>
      <stop offset="1" stop-color="#101426"/>
    </radialGradient>
    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch" result="n"/>
      <feColorMatrix in="n" type="luminanceToAlpha" result="a"/>
      <feComponentTransfer in="a" result="a2">
        <feFuncA type="linear" slope="0.09"/>
      </feComponentTransfer>
      <feFlood flood-color="#7a6548" result="c"/>
      <feComposite in="c" in2="a2" operator="in"/>
    </filter>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#paper)"/>
  <rect width="400" height="400" filter="url(#grain)" opacity="0.55"/>
  <rect width="400" height="400" fill="url(#vig)"/>
  <rect x="22" y="22" width="356" height="356" fill="none" stroke="#cbbfae" stroke-width="0.8"/>
  <rect x="27" y="27" width="346" height="346" fill="none" stroke="#cbbfae" stroke-width="0.35"/>
  <text x="200" y="50" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="11" letter-spacing="3.4" fill="#8d7f6a">L&#193;MINA IV</text>
  <text x="200" y="68" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="13.5" font-style="italic" fill="#6f6254">p&#233;talo en errata</text>
  <line x1="164" y1="78" x2="236" y2="78" stroke="#d5c9b6" stroke-width="0.6"/>
  <circle cx="200" cy="198" r="96" fill="url(#blush)"/>
  <ellipse cx="206" cy="332" rx="58" ry="8" fill="#6b5340" opacity="0.13" filter="url(#soft)"/>
  <path d="M200,248 C197,278 208,308 201,342" fill="none" stroke="#6d8f5c" stroke-width="2.3" stroke-linecap="round"/>
  <path d="M198,256 C196,284 204,312 198,334" fill="none" stroke="#b7d09a" stroke-width="0.55" stroke-linecap="round" opacity="0.8"/>
  <path d="M198,314 C158,306 126,280 112,246 C140,264 154,258 166,272 C156,290 174,306 198,314 Z" fill="#7c9a68"/>
  <path d="M190,310 C158,290 136,268 120,250" fill="none" stroke="#567246" stroke-width="0.55"/>
  <path d="M206,298 C242,288 266,268 280,242 C258,256 248,252 236,264 C246,276 228,290 206,298 Z" fill="#8aa674"/>
  <path d="M214,294 C240,278 258,262 272,248" fill="none" stroke="#5e7c4c" stroke-width="0.5"/>
  <path d="M166,304 C152,292 148,276 160,268" fill="none" stroke="#6d8f5c" stroke-width="1.15" stroke-linecap="round"/>
  <ellipse cx="184" cy="216" rx="11" ry="6" fill="#6f8f5e" transform="rotate(-28 184 216)"/>
  <ellipse cx="218" cy="218" rx="10" ry="5.5" fill="#7d9a66" transform="rotate(24 218 218)"/>
  <g transform="translate(208,206) rotate(47)">
    <use href="#petal" fill="#f3e0da"/>
    <path d="M0,14 C-1,-16 0,-48 0,-72" fill="none" stroke="#e4bfb6" stroke-width="0.4"/>
  </g>
  <g transform="translate(200,198) rotate(300)">
    <use href="#petal" fill="#e7d2cc"/>
    <path d="M0,14 C-1,-18 -1,-48 0,-72" fill="none" stroke="#d7aaa4" stroke-width="0.45"/>
  </g>
  <g transform="translate(200,198) rotate(0)">
    <use href="#petal" fill="#edd8d2"/>
    <path d="M0,14 C-1,-18 -1,-48 0,-72" fill="none" stroke="#d7aaa4" stroke-width="0.45"/>
    <path d="M-1,6 C-14,-16 -16,-42 -7,-62" fill="none" stroke="#d7aaa4" stroke-width="0.28" opacity="0.7"/>
    <path d="M1,6 C14,-16 16,-42 7,-62" fill="none" stroke="#d7aaa4" stroke-width="0.28" opacity="0.7"/>
  </g>
  <g transform="translate(200,198) rotate(240)">
    <use href="#petal" fill="#f1e1db"/>
    <path d="M0,14 C-1,-18 0,-48 0,-72" fill="none" stroke="#d7aaa4" stroke-width="0.45"/>
  </g>
  <g transform="translate(200,198) rotate(120)">
    <use href="#petal" fill="#ead9d3"/>
    <path d="M0,14 C1,-18 0,-48 0,-72" fill="none" stroke="#d7aaa4" stroke-width="0.45"/>
    <path d="M-8,-8 C-18,-30 -14,-54 -5,-68" fill="none" stroke="#fff" stroke-width="1" opacity="0.22"/>
  </g>
  <g transform="translate(200,198) rotate(200)">
    <use href="#petal" fill="#f6e7e2"/>
    <path d="M0,14 C-1,-18 0,-48 0,-72" fill="none" stroke="#d9ada6" stroke-width="0.45"/>
    <path d="M-1,6 C-14,-16 -15,-40 -6,-60" fill="none" stroke="#d9ada6" stroke-width="0.3" opacity="0.75"/>
    <path d="M1,6 C13,-16 15,-40 6,-60" fill="none" stroke="#d9ada6" stroke-width="0.3" opacity="0.75"/>
    <path d="M-8,-6 C-18,-28 -13,-52 -4,-66" fill="none" stroke="#fff" stroke-width="1.1" opacity="0.28"/>
  </g>
  <g transform="translate(200,198) rotate(160)">
    <use href="#petal" fill="#f3e0da"/>
    <path d="M0,14 C-1,-18 1,-48 0,-72" fill="none" stroke="#d9ada6" stroke-width="0.45"/>
    <path d="M-1,6 C-13,-16 -14,-40 -6,-60" fill="none" stroke="#d9ada6" stroke-width="0.3" opacity="0.75"/>
    <path d="M1,5 C12,-16 14,-38 6,-58" fill="none" stroke="#d9ada6" stroke-width="0.3" opacity="0.75"/>
  </g>
  <use href="#petal" transform="translate(205,203) rotate(50) scale(1.05)" fill="#243058" opacity="0.1"/>
  <g clip-path="url(#inv)">
    <rect x="150" y="100" width="150" height="150" fill="url(#sky)"/>
    <circle cx="252" cy="148" r="18" fill="#c5d0f4" opacity="0.28"/>
    <path d="M212,186 L227,170 L243,156" fill="none" stroke="#ead9a4" stroke-width="0.4" opacity="0.75"/>
    <path d="M227,170 L235,182" fill="none" stroke="#ead9a4" stroke-width="0.3" opacity="0.6"/>
    <path d="M243,156 L256,146" fill="none" stroke="#ead9a4" stroke-width="0.28" opacity="0.5"/>
    <circle cx="212" cy="186" r="0.7" fill="#fff6dd"/>
    <circle cx="227" cy="170" r="0.85" fill="#fff"/>
    <circle cx="243" cy="156" r="0.7" fill="#fff4d2"/>
    <circle cx="235" cy="182" r="0.6" fill="#f0e2b0"/>
    <circle cx="256" cy="146" r="0.55" fill="#fff"/>
    <circle cx="248" cy="168" r="0.45" fill="#fff8e8"/>
    <circle cx="220" cy="174" r="0.4" fill="#ffe9a8"/>
    <circle cx="238" cy="148" r="0.4" fill="#fff"/>
    <polygon points="234,152 235.2,156.2 239.6,156.8 235.2,157.6 234,161.6 232.8,157.6 228.4,156.8 232.8,156.2" fill="#fff6d4"/>
    <polygon points="258,140 258.7,142.4 261.2,142.8 258.7,143.3 258,145.6 257.3,143.3 254.8,142.8 257.3,142.4" fill="#fff1c2"/>
    <path d="M249,136 a5.2,5.2 0 0 0 8.2,6.4" fill="none" stroke="#f6e7b8" stroke-width="1.25" stroke-linecap="round"/>
    <circle cx="230" cy="173" r="1.05" fill="#f0c84a"/>
  </g>
  <g transform="translate(200,198) rotate(50) scale(1.05)" fill="none">
    <use href="#petal" stroke="#f6e7e1" stroke-width="2.5"/>
    <use href="#petal" stroke="#e3c15e" stroke-width="0.75"/>
    <path d="M0,12 C1,-20 1,-48 0,-70" stroke="#e8d59a" stroke-width="0.35" opacity="0.8"/>
    <path d="M-1,4 C-12,-18 -10,-42 -5,-58" stroke="#e8d59a" stroke-width="0.25" opacity="0.5"/>
    <path d="M2,2 C11,-16 12,-36 6,-54" stroke="#e8d59a" stroke-width="0.25" opacity="0.5"/>
  </g>
  <circle cx="214" cy="228" r="1.35" fill="#e8c96a"/>
  <circle cx="208" cy="232" r="0.45" fill="#f0dc8a"/>
  <circle cx="196" cy="118" r="0.7" fill="#8ea0d4" opacity="0.75"/>
  <circle cx="206" cy="112" r="0.5" fill="#9aa8dc" opacity="0.6"/>
  <circle cx="188" cy="126" r="0.4" fill="#7f94cc" opacity="0.55"/>
  <g transform="translate(200,198)">
    <g stroke="#c4892a" stroke-width="0.7" fill="none" stroke-linecap="round">
      <path d="M0,1 L1,-16"/>
      <path d="M1,1 L11,-12"/>
      <path d="M1,1 L16,-2"/>
      <path d="M0,2 L12,8"/>
      <path d="M0,2 L2,14"/>
      <path d="M0,1 L-10,10"/>
      <path d="M0,1 L-15,1"/>
      <path d="M0,1 L-11,-10"/>
      <path d="M0,1 L-4,-15"/>
    </g>
    <g fill="#e8b423">
      <circle cx="1" cy="-16" r="1.5"/>
      <circle cx="11" cy="-12" r="1.4"/>
      <circle cx="16" cy="-2" r="1.5"/>
      <circle cx="12" cy="8" r="1.3"/>
      <circle cx="2" cy="14" r="1.5"/>
      <circle cx="-10" cy="10" r="1.4"/>
      <circle cx="-15" cy="1" r="1.5"/>
      <circle cx="-11" cy="-10" r="1.3"/>
      <circle cx="-4" cy="-15" r="1.5"/>
    </g>
    <circle r="7.2" fill="#d7a21a"/>
    <circle r="3" fill="#f2d36e"/>
    <circle r="1.3" fill="#a56b16"/>
  </g>
  <path d="M286,132 C298,126 308,124 316,127" fill="none" stroke="#cfc3b0" stroke-width="0.55"/>
  <text x="320" y="126" font-family="Georgia, 'Times New Roman', serif" font-size="9" font-style="italic" fill="#a89880">sic</text>
  <text x="200" y="366" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="10.5" font-style="italic" fill="#8d7f6a">la versi&#243;n que prefiero</text>
</svg>