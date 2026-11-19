<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8cb4ce"/>
      <stop offset="48%" stop-color="#cddfe0"/>
      <stop offset="82%" stop-color="#efe0c2"/>
      <stop offset="100%" stop-color="#f3d5aa"/>
    </linearGradient>
    <linearGradient id="sand" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#dda979"/>
      <stop offset="55%" stop-color="#c38457"/>
      <stop offset="100%" stop-color="#9e6240"/>
    </linearGradient>
    <radialGradient id="eclipseGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f9dc8c" stop-opacity="0.95"/>
      <stop offset="48%" stop-color="#f2be5c" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#f2be5c" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bodyGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#366b88"/>
      <stop offset="55%" stop-color="#224a67"/>
      <stop offset="100%" stop-color="#163249"/>
    </linearGradient>
    <linearGradient id="neckGrad" x1="0" y1="0" x2="1" y2="0.8">
      <stop offset="0%" stop-color="#4b859e"/>
      <stop offset="60%" stop-color="#275573"/>
      <stop offset="100%" stop-color="#193851"/>
    </linearGradient>
    <linearGradient id="penLight" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#dfefea"/>
      <stop offset="100%" stop-color="#9ecbc7"/>
    </linearGradient>
    <linearGradient id="penMid" x1="0" y1="0" x2="1" y2="0.4">
      <stop offset="0%" stop-color="#3e7894"/>
      <stop offset="100%" stop-color="#275472"/>
    </linearGradient>
    <linearGradient id="penDark" x1="0" y1="0" x2="0.3" y2="1">
      <stop offset="0%" stop-color="#1c3c57"/>
      <stop offset="100%" stop-color="#102539"/>
    </linearGradient>
    <linearGradient id="waterTail" x1="0" y1="1" x2="0.5" y2="0">
      <stop offset="0%" stop-color="#1c415e"/>
      <stop offset="45%" stop-color="#3a86a3" stop-opacity="0.9"/>
      <stop offset="85%" stop-color="#8fd2d4" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#e8f7f5" stop-opacity="0.65"/>
    </linearGradient>
    <linearGradient id="upperLegFade" gradientUnits="userSpaceOnUse" x1="0" y1="244" x2="0" y2="296">
      <stop offset="0%" stop-color="#204764" stop-opacity="1"/>
      <stop offset="32%" stop-color="#275372" stop-opacity="0.92"/>
      <stop offset="70%" stop-color="#2e607e" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#2e607e" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="lowerLegFade" gradientUnits="userSpaceOnUse" x1="0" y1="252" x2="0" y2="306">
      <stop offset="0%" stop-color="#2e607e" stop-opacity="0"/>
      <stop offset="32%" stop-color="#2b5a78" stop-opacity="0.24"/>
      <stop offset="72%" stop-color="#214966" stop-opacity="0.94"/>
      <stop offset="100%" stop-color="#16334c" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="fadeLineDown" gradientUnits="userSpaceOnUse" x1="0" y1="256" x2="0" y2="298">
      <stop offset="0%" stop-color="#102030" stop-opacity="0"/>
      <stop offset="100%" stop-color="#102030" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="antlerGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#c99c52"/>
      <stop offset="55%" stop-color="#f2d590"/>
      <stop offset="100%" stop-color="#fbf3df"/>
    </linearGradient>
    <clipPath id="cosmosClip">
      <polygon points="190,199.8 218,199.8 204,175.5"/>
    </clipPath>
  </defs>

  <!-- Surreal Daylight Sky -->
  <rect width="400" height="318" fill="url(#sky)"/>

  <!-- Soft Distant Clouds -->
  <g fill="#f7f3e8" opacity="0.62">
    <path d="M18,148 Q38,136 62,144 Q80,132 102,144 Q118,144 124,154 L14,154 Z"/>
    <path d="M250,76 Q268,64 292,70 Q310,58 332,70 Q348,70 354,80 L244,80 Z"/>
    <path d="M312,248 Q330,238 352,244 Q368,236 386,248 L308,248 Z"/>
  </g>

  <!-- Distant Mesas (kept clear of legs) -->
  <path d="M0,318 L0,298 L28,292 L58,302 L86,318 Z" fill="#cfa684" opacity="0.55"/>
  <path d="M312,318 L342,296 L372,294 L400,305 L400,318 Z" fill="#cfa684" opacity="0.55"/>

  <!-- Desert Ground Plane -->
  <rect y="316" width="400" height="84" fill="url(#sand)"/>
  <line x1="0" y1="316" x2="400" y2="316" stroke="#f5dfbc" stroke-width="1.2" opacity="0.7"/>
  <path d="M0,352 Q110,346 215,356 T400,350" fill="none" stroke="#9d6341" stroke-width="0.9" opacity="0.35"/>
  <path d="M0,378 Q150,370 280,382 T400,376" fill="none" stroke="#854e30" stroke-width="1" opacity="0.3"/>

  <!-- Five Grounded Cast Shadows (for 5 hooves!) -->
  <g fill="#262d40" opacity="0.34">
    <ellipse cx="117" cy="345" rx="14" ry="4.2"/>
    <ellipse cx="156" cy="345" rx="15" ry="4.4"/>
    <ellipse cx="200" cy="345" rx="16" ry="4.5"/>
    <ellipse cx="245" cy="345" rx="16" ry="4.5"/>
    <ellipse cx="289" cy="345" rx="14" ry="4.2"/>
  </g>

  <!-- Daylight Black Eclipse Sun (framed by Möbius antlers) -->
  <g>
    <circle cx="95" cy="56" r="30" fill="url(#eclipseGlow)"/>
    <g stroke="#f5cb6c" stroke-width="1" opacity="0.65">
      <line x1="95" y1="22" x2="95" y2="33"/>
      <line x1="95" y1="79" x2="95" y2="90"/>
      <line x1="61" y1="56" x2="72" y2="56"/>
      <line x1="118" y1="56" x2="129" y2="56"/>
      <line x1="71" y1="32" x2="79" y2="40"/>
      <line x1="111" y1="72" x2="119" y2="80"/>
      <line x1="119" y1="32" x2="111" y2="40"/>
      <line x1="79" y1="72" x2="71" y2="80"/>
    </g>
    <circle cx="95" cy="56" r="14.2" fill="#f9dd92"/>
    <circle cx="95" cy="56" r="12.5" fill="#101a2c"/>
  </g>

  <!-- IMPOSSIBLE LEGS: 5 Lower Legs (materialize from sky -> solid hooves) -->
  <g fill="url(#lowerLegFade)">
    <!-- Foot 1 (C0..C1) -->
    <path d="M116,252 Q114,280 111,326 L108,343 L126,343 L127,326 Q130,280 131,252 Z"/>
    <!-- Foot 2 (C2..C3) -->
    <path d="M151,252 Q150,280 148,326 L146,343 L166,343 L168,326 Q170,280 171,252 Z"/>
    <!-- Foot 3 (C4..C5) -->
    <path d="M191.5,252 Q191,280 190,326 L189,343 L211,343 L212,326 Q212,280 212,252 Z"/>
    <!-- Foot 4 (C6..C7) -->
    <path d="M232.5,252 Q233,280 234,326 L234,343 L256,343 L256,326 Q254,280 253,252 Z"/>
    <!-- Foot 5 (C8..C9) -->
    <path d="M274,252 Q276,280 279,326 L280,343 L298,343 L297,326 Q294,280 292,252 Z"/>
  </g>

  <!-- Five Cloven Hooves -->
  <g fill="#0f2030" stroke="#0c1824" stroke-width="1.2">
    <path d="M110,331 L127,331 L126,343 Q121,345 117,341 Q113,345 108,343 Z"/>
    <path d="M147,331 L167,331 L166,343 Q161,345 156,341 Q151,345 146,343 Z"/>
    <path d="M189.5,331 L211.5,331 L211,343 Q205,345 200,341 Q195,345 189,343 Z"/>
    <path d="M234,331 L256,331 L256,343 Q250,345 245,341 Q240,345 234,343 Z"/>
    <path d="M279,331 L297,331 L298,343 Q293,345 289,341 Q285,345 280,343 Z"/>
  </g>
  <!-- Hoof Rim Highlights -->
  <g stroke="#7fb3b8" stroke-width="1" opacity="0.7" fill="none">
    <line x1="111" y1="332" x2="126" y2="332"/>
    <line x1="148" y1="332" x2="166" y2="332"/>
    <line x1="190" y1="332" x2="211" y2="332"/>
    <line x1="235" y1="332" x2="255" y2="332"/>
    <line x1="280" y1="332" x2="296" y2="332"/>
  </g>

  <!-- IMPOSSIBLE LEGS: 4 Upper Legs (solid at torso -> dissolve into sky) -->
  <g fill="url(#upperLegFade)">
    <!-- Upper Leg 1 (C1..C2) -->
    <path d="M132,222 Q131,260 129,298 L149,298 Q151,260 152,224 Z"/>
    <!-- Upper Leg 2 (C3..C4) -->
    <path d="M172,224 Q171,260 169,298 L190.5,298 Q191.5,260 192,224 Z"/>
    <!-- Upper Leg 3 (C5..C6) -->
    <path d="M212,224 Q212,260 212,298 L233.5,298 Q232.5,260 232,224 Z"/>
    <!-- Upper Leg 4 (C7..C8) -->
    <path d="M252,224 Q253.5,260 255,298 L277.5,298 Q274.5,260 272,221 Z"/>
  </g>

  <!-- Continuous Unbroken Leg Contours (C1..C8) + Fading Outer Edges (C0, C9) -->
  <g fill="none" stroke="#102030" stroke-width="1.65" stroke-linecap="round">
    <path d="M115,256 Q114,282 111,326 L108,343" stroke="url(#fadeLineDown)"/>
    <path d="M132,222 Q130,280 127,326 L126,343"/>
    <path d="M152,224 Q150,280 148,326 L146,343"/>
    <path d="M172,224 Q170,280 168,326 L166,343"/>
    <path d="M192,224 Q191,280 190,326 L189,343"/>
    <path d="M212,224 Q212,280 212,326 L211,343"/>
    <path d="M232,224 Q233,280 234,326 L234,343"/>
    <path d="M252,224 Q254,280 256,326 L256,343"/>
    <path d="M272,221 Q276,280 279,326 L280,343"/>
    <path d="M293,256 Q294,282 297,326 L298,343" stroke="url(#fadeLineDown)"/>
  </g>

  <!-- Liquid-Wave Impossible Tail & Gravity-Defying Upward Droplets -->
  <g>
    <path d="M278,176 C312,174 342,158 345,128 C348,104 332,92 318,98 C328,108 326,124 314,132 C328,132 336,122 332,112 C340,126 330,152 282,190 Z" fill="url(#waterTail)" stroke="#1a415b" stroke-width="1.4"/>
    <!-- Translucent Fin Rays & Foam Crest -->
    <path d="M332,100 C346,84 360,92 356,108 C352,118 344,122 338,118" fill="#8fd2d4" fill-opacity="0.5" stroke="#2d6e87" stroke-width="1.2"/>
    <path d="M294,178 C318,170 335,152 338,128" fill="none" stroke="#d5f2f0" stroke-width="1.1" opacity="0.75"/>
    <!-- Upward-Falling Water Droplets (inverted teardrops!) -->
    <g fill="#7dc8cf" stroke="#1e536d" stroke-width="1">
      <path d="M334,82 C334,76 339,72 339,66 C339,72 344,76 344,82 A5,5 0 1,1 334,82 Z"/>
      <path d="M318,66 C318,62 321.5,59 321.5,54 C321.5,59 325,62 325,66 A3.5,3.5 0 1,1 318,66 Z"/>
      <path d="M348,58 C348,54.5 351,52 351,48 C351,52 354,54.5 354,58 A3,3 0 1,1 348,58 Z"/>
      <path d="M333,44 C333,41.5 335.2,39.5 335.2,36 C335.2,39.5 337.4,41.5 337.4,44 A2.2,2.2 0 1,1 333,44 Z"/>
    </g>
    <!-- Tiny Golden Fish Swimming Through Dry Air -->
    <g transform="translate(358,126) rotate(-18)">
      <path d="M-9,0 C-5,-4.5 3,-4.5 8,0 C3,4.5 -5,4.5 -9,0 Z" fill="#f3c667" stroke="#163249" stroke-width="1"/>
      <path d="M-9,0 L-14,-4 L-12.5,0 L-14,4 Z" fill="#e59e48" stroke="#163249" stroke-width="0.9"/>
      <circle cx="4" cy="-0.8" r="0.9" fill="#102030"/>
    </g>
  </g>

  <!-- Sculpted Animal Body (fusing seamlessly around the Penrose Triangle) -->
  <g stroke="#102030" stroke-width="1.7" stroke-linejoin="round">
    <!-- Main Torso, Chest, Haunch & Neck -->
    <path d="M90,112 C104,132 114,158 118,184 C116,204 123,218 132,224 L152,224 C156,222 166,222 172,224 L192,224 C198,222 206,222 212,224 L232,224 C238,222 246,222 252,224 L272,222 C284,210 289,192 284,175 C278,158 262,152 244,154 L211,139.1 L197,139.1 L168,155 C144,156 128,144 108,108 Z" fill="url(#bodyGrad)"/>
    <!-- Lit Neck & Chest Facet -->
    <path d="M90,112 C105,134 114,158 118,184 C117,200 122,212 132,222 L152,222 C142,204 139,180 144,156 C128,150 114,134 102,110 Z" fill="url(#neckGrad)" stroke="none"/>
    <!-- Subtle Golden Mystical Shoulder & Haunch Arcs -->
    <path d="M126,182 Q138,174 148,186" fill="none" stroke="#e9c16d" stroke-width="1.1" opacity="0.8"/>
    <path d="M256,176 Q270,174 275,188" fill="none" stroke="#e9c16d" stroke-width="1.1" opacity="0.8"/>
  </g>

  <!-- EXACT PENROSE IMPOSSIBLE TRIANGLE RIBCAGE (S=8, Zero-Gap Isometric Geometry) -->
  <g stroke="#102030" stroke-width="1.65" stroke-linejoin="round">
    <!-- Face 3: Lit Seafoam-Ivory (Outer-Left + Top-of-Bottom) -->
    <polygon points="197,139.1 155,211.9 225,211.9 218,199.8 176,199.8 211,139.1" fill="url(#penLight)"/>
    <!-- Face 1: Mid Cerulean-Teal (Bottom + Inner-Right) -->
    <polygon points="162,224 246,224 211,163.4 204,175.5 225,211.9 155,211.9" fill="url(#penMid)"/>
    <!-- Face 2: Deep Nocturnal Indigo (Outer-Right + Inner-Left) -->
    <polygon points="253,211.9 211,139.1 176,199.8 190,199.8 211,163.4 246,224" fill="url(#penDark)"/>
  </g>

  <!-- COSMIC NIGHT WINDOW inside the Penrose Heart (Night inside Daylight!) -->
  <g clip-path="url(#cosmosClip)">
    <rect x="188" y="174" width="32" height="28" fill="#081224"/>
    <!-- Twinkling Stars -->
    <circle cx="198" cy="186" r="0.85" fill="#fff7d6"/>
    <circle cx="209" cy="182" r="0.7" fill="#d9eef8"/>
    <circle cx="212" cy="195" r="0.8" fill="#fff7d6"/>
    <circle cx="195" cy="196" r="0.65" fill="#d9eef8"/>
    <circle cx="204" cy="179" r="0.6" fill="#fff7d6"/>
    <!-- Luminous Golden Crescent Moon -->
    <path d="M206.5,187.5 A4.8,4.8 0 1,0 206.5,196.2 A3.7,3.7 0 1,1 206.5,187.5 Z" fill="#f7d278"/>
  </g>
  <polygon points="190,199.8 218,199.8 204,175.5" fill="none" stroke="#102030" stroke-width="1.5" stroke-linejoin="round"/>

  <!-- Continuous Möbius Antlers (looping around the Black Eclipse!) -->
  <g stroke="#102030" stroke-width="1.35" stroke-linejoin="round">
    <!-- Left-to-Top Ribbon Loop -->
    <path d="M88,92 C64,84 54,60 66,40 C77,22 108,22 122,40 C134,56 128,78 102,88 C118,76 122,58 113,44 C103,30 80,30 72,44 C64,58 72,78 92,88 Z" fill="url(#antlerGrad)"/>
    <!-- Delicate Antler Tines Dissolving into Sky -->
    <path d="M68,42 C56,34 50,24 54,18" fill="none" stroke="#e9c87a" stroke-width="2" stroke-linecap="round"/>
    <path d="M121,40 C132,32 138,24 135,17" fill="none" stroke="#f5e6bf" stroke-width="1.8" stroke-linecap="round"/>
    <path d="M124,62 C136,58 144,54 148,48" fill="none" stroke="#f5e6bf" stroke-width="1.5" stroke-linecap="round"/>
  </g>

  <!-- Mythical Head & Uncanny Celestial Eye -->
  <g>
    <!-- Swept Ear -->
    <path d="M98,94 L120,78 L106,104 Z" fill="#2c5f7d" stroke="#102030" stroke-width="1.5" stroke-linejoin="round"/>
    <path d="M102,94 L115,83 L106,99 Z" fill="#9bc7c4"/>
    <!-- Sleek Chimera-Stag-Heron Head -->
    <path d="M104,95 C96,86 82,88 70,96 C58,103 48,108 42,113 C49,117 61,117 72,118 C82,120 92,122 103,115 C110,110 110,101 104,95 Z" fill="url(#neckGrad)" stroke="#102030" stroke-width="1.65" stroke-linejoin="round"/>
    <!-- Beak/Muzzle Highlight -->
    <path d="M44,113 C55,109 66,105 76,102" fill="none" stroke="#b6dcd8" stroke-width="1.1" opacity="0.8"/>
    <!-- Uncanny Golden Eye -->
    <path d="M75,103 Q82,97 89,103 Q82,109 75,103 Z" fill="#f7d278" stroke="#102030" stroke-width="1.2"/>
    <ellipse cx="82" cy="103" rx="1.6" ry="3.8" fill="#0d1b2a"/>
    <circle cx="80.6" cy="101.6" r="1" fill="#ffffff"/>
  </g>

  <!-- Fine Art Vintage Naturalist Plate Border -->
  <rect x="10" y="10" width="380" height="380" fill="none" stroke="#163047" stroke-width="0.9" opacity="0.32"/>
  <g fill="#163047" opacity="0.4">
    <polygon points="10,7 13,10 10,13 7,10"/>
    <polygon points="390,7 393,10 390,13 387,10"/>
    <polygon points="10,387 13,390 10,393 7,390"/>
    <polygon points="390,387 393,390 390,393 387,390"/>
  </g>
</svg>