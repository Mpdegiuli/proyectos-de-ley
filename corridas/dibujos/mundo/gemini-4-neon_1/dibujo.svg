<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#070b1e"/>
      <stop offset="38%" stop-color="#172047"/>
      <stop offset="68%" stop-color="#4e345c"/>
      <stop offset="86%" stop-color="#c45c4c"/>
      <stop offset="100%" stop-color="#f5b461"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2c2444"/>
      <stop offset="35%" stop-color="#141c38"/>
      <stop offset="100%" stop-color="#060a17"/>
    </linearGradient>
    <radialGradient id="horizonGlow" cx="50%" cy="72%" r="48%">
      <stop offset="0%" stop-color="#ffd98e" stop-opacity="0.7"/>
      <stop offset="45%" stop-color="#e07253" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#172047" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="atmo" cx="50%" cy="50%" r="50%">
      <stop offset="68%" stop-color="#5ce1e6" stop-opacity="0.45"/>
      <stop offset="84%" stop-color="#5ce1e6" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#5ce1e6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ocean" cx="35%" cy="32%" r="72%">
      <stop offset="0%" stop-color="#2994b2"/>
      <stop offset="55%" stop-color="#154d75"/>
      <stop offset="100%" stop-color="#091f3a"/>
    </radialGradient>
    <linearGradient id="landLush" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#68c77c"/>
      <stop offset="100%" stop-color="#256d5b"/>
    </linearGradient>
    <linearGradient id="landWarm" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e89f54"/>
      <stop offset="100%" stop-color="#b84237"/>
    </linearGradient>
    <radialGradient id="sphereShade" cx="32%" cy="28%" r="72%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.14"/>
      <stop offset="55%" stop-color="#0a1630" stop-opacity="0"/>
      <stop offset="85%" stop-color="#060d21" stop-opacity="0.52"/>
      <stop offset="100%" stop-color="#030714" stop-opacity="0.82"/>
    </radialGradient>
    <linearGradient id="netGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#6fffe9"/>
      <stop offset="100%" stop-color="#ffd166"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2.5" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="globeClip">
      <circle cx="200" cy="162" r="80"/>
    </clipPath>
  </defs>

  <!-- Sky -->
  <rect width="400" height="288" fill="url(#sky)"/>
  <rect width="400" height="288" fill="url(#horizonGlow)"/>

  <!-- Subtle cosmic & digital arcs in background -->
  <g fill="none" stroke="#8ecae6" stroke-opacity="0.12" stroke-width="0.7">
    <circle cx="200" cy="162" r="118" stroke-dasharray="3 5"/>
    <circle cx="200" cy="162" r="152" stroke-dasharray="1 7"/>
    <path d="M20 75 Q200 10 380 85"/>
  </g>

  <!-- Stars -->
  <g fill="#ffffff">
    <circle cx="38" cy="34" r="1.2" opacity="0.9"/>
    <circle cx="72" cy="58" r="0.8" opacity="0.6"/>
    <circle cx="112" cy="26" r="1" opacity="0.8"/>
    <circle cx="155" cy="44" r="0.7" opacity="0.5"/>
    <circle cx="248" cy="30" r="1.1" opacity="0.85"/>
    <circle cx="295" cy="52" r="0.9" opacity="0.7"/>
    <circle cx="342" cy="28" r="1.3" opacity="0.9"/>
    <circle cx="368" cy="70" r="0.8" opacity="0.6"/>
    <circle cx="26" cy="96" r="0.9" opacity="0.55"/>
    <circle cx="88" cy="108" r="0.7" opacity="0.45"/>
    <circle cx="318" cy="94" r="1" opacity="0.65"/>
    <circle cx="378" cy="118" r="0.7" opacity="0.5"/>
    <circle cx="52" cy="140" r="0.8" opacity="0.4"/>
    <circle cx="350" cy="152" r="0.9" opacity="0.45"/>
  </g>

  <!-- Crescent moon -->
  <path d="M56 54 A12 12 0 1 0 70 68 A9.5 9.5 0 1 1 56 54 Z" fill="#fff3cc" opacity="0.85" filter="url(#glow)"/>

  <!-- Back orbit ring -->
  <ellipse cx="200" cy="162" rx="126" ry="34" transform="rotate(-19 200 162)" fill="none" stroke="#5ce1e6" stroke-opacity="0.32" stroke-width="1" stroke-dasharray="4 4"/>
  <ellipse cx="200" cy="162" rx="112" ry="26" transform="rotate(21 200 162)" fill="none" stroke="#ffd166" stroke-opacity="0.28" stroke-width="0.9"/>

  <!-- Earth atmosphere -->
  <circle cx="200" cy="162" r="102" fill="url(#atmo)"/>

  <!-- Earth sphere -->
  <circle cx="200" cy="162" r="80" fill="url(#ocean)"/>

  <!-- Earth interior details -->
  <g clip-path="url(#globeClip)">
    <!-- Lush continents (left/north) -->
    <path d="M128 118 C144 102, 174 96, 186 112 C194 123, 182 138, 173 147 C163 157, 177 167, 168 182 C158 197, 142 204, 134 190 C126 176, 132 158, 122 146 Z" fill="url(#landLush)"/>
    <path d="M168 202 C180 194, 195 204, 192 222 C188 238, 174 246, 164 236 C156 226, 158 209, 168 202 Z" fill="url(#landLush)" opacity="0.9"/>

    <!-- Warming/arid continents (right/east) -->
    <path d="M206 108 C226 96, 260 106, 274 126 C284 142, 276 164, 258 170 C244 175, 232 162, 218 164 C205 166, 200 152, 204 138 C208 126, 198 114, 206 108 Z" fill="url(#landWarm)"/>
    <path d="M222 178 C240 174, 262 184, 266 202 C270 218, 254 234, 238 230 C224 226, 216 212, 218 196 Z" fill="url(#landWarm)" opacity="0.88"/>

    <!-- Subtle meridian/data grid inside globe -->
    <g fill="none" stroke="#90f1ef" stroke-opacity="0.16" stroke-width="0.6">
      <ellipse cx="200" cy="162" rx="42" ry="80"/>
      <ellipse cx="200" cy="162" rx="80" ry="28"/>
      <line x1="120" y1="162" x2="280" y2="162"/>
    </g>

    <!-- Soft clouds -->
    <g fill="#ffffff" opacity="0.22">
      <rect x="132" y="128" width="52" height="7" rx="3.5"/>
      <rect x="158" y="138" width="38" height="5" rx="2.5"/>
      <rect x="210" y="148" width="58" height="6" rx="3"/>
      <rect x="148" y="192" width="46" height="6" rx="3"/>
      <rect x="206" y="210" width="44" height="5" rx="2.5"/>
    </g>

    <!-- Spherical shading -->
    <circle cx="200" cy="162" r="80" fill="url(#sphereShade)"/>

    <!-- Glowing city clusters & embers on night/warm side -->
    <g fill="#ffd166" filter="url(#glow)">
      <circle cx="228" cy="134" r="1.4"/>
      <circle cx="235" cy="138" r="1"/>
      <circle cx="246" cy="148" r="1.6"/>
      <circle cx="254" cy="144" r="0.9"/>
      <circle cx="238" cy="194" r="1.5"/>
      <circle cx="246" cy="202" r="1.1"/>
      <circle cx="226" cy="208" r="1"/>
      <circle cx="164" cy="142" r="1.1" fill="#80ffdb"/>
      <circle cx="152" cy="170" r="1.2" fill="#80ffdb"/>
      <circle cx="182" cy="214" r="1.1" fill="#80ffdb"/>
    </g>

    <!-- Network web connecting hemispheres -->
    <g stroke="url(#netGrad)" stroke-width="0.9" fill="none" opacity="0.72">
      <path d="M164 142 Q196 118 228 134"/>
      <path d="M152 170 Q198 152 246 148"/>
      <path d="M152 170 Q192 192 238 194"/>
      <path d="M182 214 Q212 204 238 194"/>
      <path d="M228 134 Q244 164 238 194"/>
      <path d="M164 142 Q150 156 152 170"/>
    </g>
  </g>

  <!-- Rim highlight on Earth -->
  <path d="M138 112 A80 80 0 0 1 218 84" fill="none" stroke="#b8f7ff" stroke-width="1.6" stroke-linecap="round" opacity="0.65"/>

  <!-- Front orbital arcs & satellites -->
  <path d="M84 202 A126 34 -19 0 0 316 122" fill="none" stroke="#6fffe9" stroke-width="1.2" opacity="0.7"/>
  <circle cx="288" cy="133" r="2.6" fill="#6fffe9" filter="url(#glow)"/>
  <circle cx="102" cy="195" r="2" fill="#ffd166" filter="url(#glow)"/>

  <!-- Floating data-constellation lifting from Earth into sky -->
  <g stroke="#72efdd" stroke-width="0.7" opacity="0.55" fill="none">
    <path d="M246 148 L294 114 L328 130 L306 164"/>
    <path d="M294 114 L318 82"/>
    <path d="M164 142 L108 112 L78 136"/>
  </g>
  <g fill="#a8f9ff" filter="url(#glow)">
    <circle cx="294" cy="114" r="1.8"/>
    <circle cx="328" cy="130" r="1.4"/>
    <circle cx="306" cy="164" r="1.2"/>
    <circle cx="318" cy="82" r="1.5"/>
    <circle cx="108" cy="112" r="1.7"/>
    <circle cx="78" cy="136" r="1.3"/>
  </g>

  <!-- Soft horizon clouds -->
  <path d="M0 264 Q55 248 115 262 T240 258 T400 264 L400 288 L0 288 Z" fill="#5e3455" opacity="0.4"/>

  <!-- Distant horizon: City skyline (left) transitioning to Mountains & Wind Turbines (right) -->
  <g fill="#12162e">
    <!-- Left skyline -->
    <rect x="0" y="252" width="18" height="36"/>
    <rect x="20" y="236" width="16" height="52"/>
    <rect x="27" y="224" width="2" height="12"/>
    <rect x="38" y="248" width="14" height="40"/>
    <rect x="54" y="228" width="18" height="60"/>
    <rect x="74" y="244" width="14" height="44"/>
    <rect x="90" y="258" width="20" height="30"/>
    <rect x="112" y="266" width="16" height="22"/>
    <rect x="130" y="274" width="18" height="14"/>
    <!-- Right mountains & forest -->
    <path d="M238 288 L268 264 L294 276 L332 246 L364 266 L388 252 L400 260 L400 288 Z"/>
  </g>

  <!-- Tiny warm city lights -->
  <g fill="#ffd166" opacity="0.85">
    <rect x="24" y="242" width="2" height="3"/><rect x="30" y="248" width="2" height="3"/>
    <rect x="24" y="256" width="2" height="3"/><rect x="42" y="254" width="2" height="3"/>
    <rect x="58" y="234" width="2" height="3"/><rect x="65" y="234" width="2" height="3"/>
    <rect x="58" y="244" width="2" height="3"/><rect x="65" y="250" width="2" height="3"/>
    <rect x="78" y="252" width="2" height="3"/><rect x="96" y="264" width="2" height="3"/>
  </g>

  <!-- Wind turbines on right ridge -->
  <g stroke="#e0c3a8" stroke-width="1.1" stroke-linecap="round" opacity="0.78">
    <line x1="274" y1="268" x2="274" y2="248"/>
    <path d="M274 248 L266 243 M274 248 L281 244 M274 248 L274 256"/>
    <line x1="302" y1="274" x2="302" y2="256"/>
    <path d="M302 256 L296 251 M302 256 L309 253 M302 256 L302 263"/>
  </g>

  <!-- Water -->
  <rect x="0" y="288" width="400" height="112" fill="url(#water)"/>

  <!-- Water reflections of horizon & Earth -->
  <g opacity="0.45">
    <ellipse cx="200" cy="292" rx="130" ry="6" fill="#f5b461"/>
    <ellipse cx="200" cy="306" rx="88" ry="8" fill="#5ce1e6" opacity="0.5"/>
    <ellipse cx="200" cy="324" rx="68" ry="7" fill="#2994b2" opacity="0.55"/>
    <ellipse cx="200" cy="342" rx="52" ry="6" fill="#e89f54" opacity="0.45"/>
    <ellipse cx="200" cy="360" rx="36" ry="5" fill="#5ce1e6" opacity="0.35"/>
    <ellipse cx="200" cy="376" rx="22" ry="3.5" fill="#ffd166" opacity="0.35"/>
  </g>

  <!-- Shimmering water ripples -->
  <g fill="#ffe8b6" opacity="0.5">
    <rect x="148" y="294" width="104" height="1.5" rx="1"/>
    <rect x="166" y="302" width="68" height="1.5" rx="1"/>
    <rect x="158" y="313" width="84" height="1.4" rx="1" fill="#80ffdb"/>
    <rect x="174" y="325" width="52" height="1.4" rx="1"/>
    <rect x="180" y="338" width="40" height="1.3" rx="1" fill="#80ffdb"/>
    <rect x="186" y="352" width="28" height="1.2" rx="1"/>
    <rect x="52" y="296" width="18" height="1.2" rx="1" fill="#ffd166" opacity="0.6"/>
    <rect x="58" y="305" width="12" height="1.1" rx="1" fill="#ffd166" opacity="0.45"/>
  </g>

  <!-- Foreground left cliff & contemplative human figure -->
  <path d="M0 332 Q52 326 98 342 Q142 356 176 400 L0 400 Z" fill="#060916"/>

  <!-- Human silhouette looking up at the world, releasing light/hope -->
  <g fill="#060916">
    <!-- Body -->
    <circle cx="96" cy="307" r="5"/>
    <path d="M92 314 C90 322, 88 334, 87 346 L93 346 L96 330 L99 347 L105 347 C104 334, 102 322, 100 314 Z"/>
    <!-- Outstretched arm toward globe -->
    <path d="M98 316 L112 308 L114 311 L100 320 Z"/>
  </g>

  <!-- Luminous origami bird & rising sparks from hand toward the Earth's network -->
  <g filter="url(#glow)">
    <path d="M116 303 L125 296 L121 305 L127 308 L118 307 Z" fill="#fff3b0"/>
    <circle cx="129" cy="291" r="1.4" fill="#ffd166"/>
    <circle cx="137" cy="278" r="1.2" fill="#80ffdb"/>
    <circle cx="144" cy="262" r="1.1" fill="#ffd166"/>
    <circle cx="149" cy="244" r="1.3" fill="#80ffdb"/>
    <circle cx="155" cy="226" r="1" fill="#ffffff"/>
  </g>

  <!-- Foreground right bank & growing tree of renewal -->
  <path d="M262 400 Q318 362 356 352 Q382 346 400 350 L400 400 Z" fill="#060916"/>
  <g stroke="#060916" stroke-linecap="round" fill="none">
    <path d="M342 362 Q338 334 345 310" stroke-width="4"/>
    <path d="M342 336 Q326 324 316 314" stroke-width="2.2"/>
    <path d="M343 326 Q358 314 368 304" stroke-width="2"/>
    <path d="M344 316 Q336 302 332 294" stroke-width="1.6"/>
  </g>
  <!-- Glowing leaves on the tree -->
  <g fill="#72efdd" opacity="0.82" filter="url(#glow)">
    <circle cx="315" cy="313" r="3"/>
    <circle cx="323" cy="306" r="2.2" fill="#ffd166"/>
    <circle cx="332" cy="293" r="2.8"/>
    <circle cx="345" cy="304" r="3.2" fill="#80ffdb"/>
    <circle cx="356" cy="298" r="2.4" fill="#ffd166"/>
    <circle cx="368" cy="303" r="2.8"/>
    <circle cx="360" cy="314" r="2" fill="#80ffdb"/>
  </g>

  <!-- Distant flying birds across the twilight -->
  <g fill="none" stroke="#1b1834" stroke-width="1.3" stroke-linecap="round">
    <path d="M294 218 Q298 214 302 218 Q306 214 310 218"/>
    <path d="M316 206 Q319 203 322 206 Q325 203 328 206"/>
    <path d="M74 202 Q77 199 80 202 Q83 199 86 202"/>
  </g>
</svg>