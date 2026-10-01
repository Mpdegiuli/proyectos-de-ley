<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="sky" cx="50%" cy="38%" r="75%">
      <stop offset="0%" stop-color="#2d1f4a"/>
      <stop offset="55%" stop-color="#17132e"/>
      <stop offset="100%" stop-color="#090a18"/>
    </radialGradient>
    <linearGradient id="bark" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#2a1a2e"/>
      <stop offset="40%" stop-color="#6b4a5c"/>
      <stop offset="70%" stop-color="#3e2a3c"/>
      <stop offset="100%" stop-color="#1b1020"/>
    </linearGradient>
    <radialGradient id="bulb">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="35%" stop-color="#8ff0d8"/>
      <stop offset="75%" stop-color="#2bb49a"/>
      <stop offset="100%" stop-color="#0d5a52" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bulb2">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="35%" stop-color="#ffc8f0"/>
      <stop offset="75%" stop-color="#c050b0"/>
      <stop offset="100%" stop-color="#5a1050" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#58e6c4" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#58e6c4" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="leaf" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#7ef0cf"/>
      <stop offset="50%" stop-color="#3aa6a0"/>
      <stop offset="100%" stop-color="#23506b"/>
    </linearGradient>
    <linearGradient id="leaf2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f3a5e2"/>
      <stop offset="60%" stop-color="#8b4bb0"/>
      <stop offset="100%" stop-color="#2b1b55"/>
    </linearGradient>
    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1d2a38"/>
      <stop offset="100%" stop-color="#070a12"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <g fill="#fff">
    <circle cx="40" cy="48" r="1.1" opacity=".8"/><circle cx="92" cy="26" r=".8" opacity=".6"/>
    <circle cx="150" cy="60" r="1" opacity=".5"/><circle cx="330" cy="40" r="1.2" opacity=".85"/>
    <circle cx="368" cy="96" r=".9" opacity=".6"/><circle cx="286" cy="22" r=".7" opacity=".5"/>
    <circle cx="22" cy="130" r=".9" opacity=".55"/><circle cx="212" cy="18" r=".8" opacity=".7"/>
    <circle cx="360" cy="180" r=".8" opacity=".45"/><circle cx="66" cy="200" r=".7" opacity=".4"/>
  </g>

  <ellipse cx="200" cy="200" rx="165" ry="165" fill="url(#halo)"/>

  <ellipse cx="200" cy="372" rx="190" ry="30" fill="url(#ground)"/>
  <ellipse cx="200" cy="362" rx="96" ry="16" fill="#0b1a1c" opacity=".8"/>

  <!-- raíces -->
  <g stroke="url(#bark)" fill="none" stroke-linecap="round">
    <path d="M200 350 C168 352 142 358 112 368" stroke-width="9"/>
    <path d="M200 350 C232 352 262 358 292 366" stroke-width="8"/>
    <path d="M200 352 C186 362 168 370 150 376" stroke-width="6"/>
    <path d="M200 352 C214 362 236 370 254 374" stroke-width="5"/>
  </g>

  <!-- tronco trenzado -->
  <path d="M176 356 C180 300 160 268 170 226 C178 192 190 176 196 150 L208 150 C206 180 196 196 190 228 C182 270 200 302 198 356 Z" fill="url(#bark)"/>
  <path d="M224 356 C218 302 242 272 232 228 C224 192 210 178 204 150 L194 152 C200 180 212 196 218 230 C226 272 206 300 212 356 Z" fill="url(#bark)" opacity=".92"/>
  <path d="M186 340 C196 300 182 262 192 224" stroke="#d9a7c8" stroke-opacity=".25" stroke-width="2" fill="none"/>
  <path d="M216 338 C206 298 222 260 210 222" stroke="#d9a7c8" stroke-opacity=".2" stroke-width="2" fill="none"/>

  <!-- ramas -->
  <g fill="none" stroke="url(#bark)" stroke-linecap="round">
    <path d="M200 152 C196 120 170 104 140 96" stroke-width="8"/>
    <path d="M200 152 C206 122 232 106 262 100" stroke-width="8"/>
    <path d="M198 160 C178 142 152 140 126 146" stroke-width="6"/>
    <path d="M202 160 C224 144 250 142 274 150" stroke-width="6"/>
    <path d="M200 146 C200 116 198 96 206 72" stroke-width="7"/>
    <path d="M140 96 C122 90 112 76 104 62" stroke-width="4"/>
    <path d="M140 96 C128 100 116 112 110 124" stroke-width="3.5"/>
    <path d="M262 100 C280 94 290 80 298 66" stroke-width="4"/>
    <path d="M262 100 C276 106 288 116 294 130" stroke-width="3.5"/>
    <path d="M206 72 C190 62 182 50 178 38" stroke-width="3.5"/>
    <path d="M206 72 C222 64 232 52 238 40" stroke-width="3.5"/>
    <path d="M126 146 C112 152 104 164 100 176" stroke-width="3"/>
    <path d="M274 150 C288 156 296 166 300 180" stroke-width="3"/>
  </g>

  <!-- hojas cristalinas -->
  <g opacity=".92">
    <g fill="url(#leaf)">
      <path d="M104 62 l-16 -14 l6 22 l-18 2 l20 12 l-6 16 l18 -12 l8 14 l2 -18 l16 2 l-14 -14 Z"/>
      <path d="M298 66 l16 -14 l-6 22 l18 2 l-20 12 l6 16 l-18 -12 l-8 14 l-2 -18 l-16 2 l14 -14 Z"/>
      <path d="M100 176 l-18 -6 l8 16 l-14 10 l18 2 l2 16 l12 -12 l12 10 l-4 -18 l14 -8 l-18 -4 Z"/>
      <path d="M300 180 l18 -6 l-8 16 l14 10 l-18 2 l-2 16 l-12 -12 l-12 10 l4 -18 l-14 -8 l18 -4 Z"/>
    </g>
    <g fill="url(#leaf2)">
      <path d="M178 38 l-14 -16 l2 22 l-18 6 l20 8 l-4 18 l16 -14 l10 12 l0 -18 l16 0 l-16 -12 Z"/>
      <path d="M238 40 l14 -16 l-2 22 l18 6 l-20 8 l4 18 l-16 -14 l-10 12 l0 -18 l-16 0 l16 -12 Z"/>
      <path d="M110 124 l-16 -4 l8 14 l-12 10 l16 2 l2 14 l10 -12 l12 8 l-4 -16 l12 -8 l-16 -2 Z"/>
      <path d="M294 130 l16 -4 l-8 14 l12 10 l-16 2 l-2 14 l-10 -12 l-12 8 l4 -16 l-12 -8 l16 -2 Z"/>
    </g>
  </g>

  <!-- frutos luminosos -->
  <g>
    <circle cx="104" cy="62" r="16" fill="url(#bulb)"/>
    <circle cx="298" cy="66" r="16" fill="url(#bulb)"/>
    <circle cx="178" cy="38" r="15" fill="url(#bulb2)"/>
    <circle cx="238" cy="40" r="13" fill="url(#bulb2)"/>
    <circle cx="110" cy="124" r="12" fill="url(#bulb)"/>
    <circle cx="294" cy="130" r="12" fill="url(#bulb)"/>
    <circle cx="100" cy="176" r="12" fill="url(#bulb2)"/>
    <circle cx="300" cy="180" r="12" fill="url(#bulb2)"/>
    <circle cx="206" cy="72" r="9" fill="url(#bulb)"/>
    <circle cx="140" cy="96" r="8" fill="url(#bulb2)"/>
    <circle cx="262" cy="100" r="8" fill="url(#bulb2)"/>
  </g>

  <!-- esporas flotantes -->
  <g fill="#9ff3dd">
    <circle cx="150" cy="200" r="1.8" opacity=".8"/><circle cx="256" cy="212" r="1.5" opacity=".7"/>
    <circle cx="128" cy="244" r="1.3" opacity=".6"/><circle cx="286" cy="252" r="1.6" opacity=".65"/>
    <circle cx="170" cy="278" r="1.2" opacity=".55"/><circle cx="238" cy="296" r="1.4" opacity=".6"/>
    <circle cx="96" cy="300" r="1.5" opacity=".5"/><circle cx="318" cy="306" r="1.2" opacity=".5"/>
    <circle cx="200" cy="230" r="1.1" opacity=".5"/><circle cx="64" cy="252" r="1.2" opacity=".4"/>
    <circle cx="340" cy="226" r="1.3" opacity=".45"/>
  </g>

  <ellipse cx="200" cy="360" rx="70" ry="10" fill="#4fe0c0" opacity=".12"/>
</svg>