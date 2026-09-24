<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#050a25"/>
      <stop offset="55%" stop-color="#16265c"/>
      <stop offset="100%" stop-color="#4a3a72"/>
    </linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a3566"/>
      <stop offset="100%" stop-color="#070b1c"/>
    </linearGradient>
    <radialGradient id="moonGlow">
      <stop offset="0%" stop-color="#fff8d8" stop-opacity="0.75"/>
      <stop offset="45%" stop-color="#ffeeb0" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ffeeb0" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="lampGlow">
      <stop offset="0%" stop-color="#fff6c0" stop-opacity="1"/>
      <stop offset="35%" stop-color="#ffdb66" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#ffcc44" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff3bd" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#fff3bd" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="beam2" x1="1" y1="0" x2="0" y2="0">
      <stop offset="0%" stop-color="#fff3bd" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#fff3bd" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="towerClip">
      <path d="M289 292 L295 186 L315 186 L321 292 Z"/>
    </clipPath>
    <linearGradient id="cliff" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b2d45"/>
      <stop offset="100%" stop-color="#0c0d18"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- stars -->
  <g fill="#ffffff">
    <circle cx="24" cy="30" r="1.5" opacity=".9"/>
    <circle cx="58" cy="17" r="1" opacity=".6"/>
    <circle cx="96" cy="38" r="1.2" opacity=".8"/>
    <circle cx="140" cy="22" r="1.6" opacity=".95"/>
    <circle cx="176" cy="55" r="1" opacity=".5"/>
    <circle cx="205" cy="28" r="1.4" opacity=".85"/>
    <circle cx="238" cy="60" r="1.1" opacity=".7"/>
    <circle cx="268" cy="24" r="1.7" opacity=".9"/>
    <circle cx="310" cy="48" r="1" opacity=".55"/>
    <circle cx="344" cy="26" r="1.3" opacity=".8"/>
    <circle cx="378" cy="60" r="1.5" opacity=".9"/>
    <circle cx="16" cy="88" r="1.2" opacity=".7"/>
    <circle cx="150" cy="96" r="1.1" opacity=".65"/>
    <circle cx="190" cy="120" r="1.3" opacity=".75"/>
    <circle cx="232" cy="98" r="1" opacity=".5"/>
    <circle cx="286" cy="110" r="1.4" opacity=".8"/>
    <circle cx="352" cy="120" r="1.1" opacity=".6"/>
    <circle cx="66" cy="142" r="1.2" opacity=".65"/>
    <circle cx="120" cy="160" r="1" opacity=".45"/>
    <circle cx="255" cy="150" r="1.2" opacity=".6"/>
    <circle cx="384" cy="160" r="1" opacity=".5"/>
    <circle cx="44" cy="190" r="1" opacity=".4"/>
    <circle cx="170" cy="188" r="1.1" opacity=".5"/>
  </g>

  <!-- moon -->
  <circle cx="92" cy="82" r="62" fill="url(#moonGlow)"/>
  <circle cx="92" cy="82" r="26" fill="#fdf6d3"/>
  <circle cx="83" cy="74" r="5" fill="#eadfb4" opacity=".7"/>
  <circle cx="100" cy="92" r="7" fill="#eadfb4" opacity=".55"/>
  <circle cx="103" cy="70" r="3" fill="#eadfb4" opacity=".5"/>

  <!-- light beams -->
  <polygon points="305,172 40,120 30,230" fill="url(#beam2)"/>
  <polygon points="305,172 400,130 400,236" fill="url(#beam)"/>

  <!-- sea -->
  <rect x="0" y="250" width="400" height="150" fill="url(#sea)"/>
  <g fill="#fdf6d3" opacity=".5">
    <rect x="76" y="256" width="32" height="2" rx="1"/>
    <rect x="70" y="266" width="44" height="2.5" rx="1.2"/>
    <rect x="80" y="278" width="26" height="2" rx="1"/>
    <rect x="64" y="290" width="52" height="3" rx="1.5"/>
    <rect x="78" y="304" width="30" height="2" rx="1"/>
    <rect x="58" y="320" width="62" height="3" rx="1.5"/>
    <rect x="74" y="338" width="38" height="2.5" rx="1.2"/>
    <rect x="52" y="358" width="70" height="3" rx="1.5"/>
    <rect x="70" y="378" width="44" height="2.5" rx="1.2"/>
  </g>
  <g stroke="#8fa3d6" stroke-opacity=".35" fill="none" stroke-width="1.4">
    <path d="M0 262 q18 -4 36 0 t36 0 t36 0 t36 0"/>
    <path d="M160 272 q20 -5 40 0 t40 0 t40 0 t40 0"/>
    <path d="M10 296 q22 -6 44 0 t44 0"/>
    <path d="M200 300 q22 -6 44 0 t44 0 t44 0"/>
    <path d="M0 332 q26 -7 52 0 t52 0"/>
    <path d="M230 344 q26 -7 52 0 t52 0"/>
    <path d="M30 372 q28 -8 56 0 t56 0"/>
  </g>

  <!-- distant sailboat -->
  <g opacity=".85">
    <path d="M182 250 L182 228 L196 250 Z" fill="#dfe6ff" opacity=".8"/>
    <path d="M180 250 L180 234 L170 250 Z" fill="#c3cdf0" opacity=".7"/>
    <path d="M166 251 h32 l-5 5 h-22 z" fill="#0d1230"/>
  </g>

  <!-- cliff -->
  <path d="M232 400 L246 330 L262 300 L286 288 L318 286 L352 296 L400 288 L400 400 Z" fill="url(#cliff)"/>
  <path d="M246 330 L262 300 L286 288 L300 292 L276 400 L232 400 Z" fill="#000000" opacity=".22"/>

  <!-- lighthouse -->
  <path d="M289 292 L295 186 L315 186 L321 292 Z" fill="#ece7dc"/>
  <g clip-path="url(#towerClip)">
    <rect x="285" y="196" width="40" height="16" fill="#c9452f"/>
    <rect x="285" y="228" width="40" height="17" fill="#c9452f"/>
    <rect x="285" y="262" width="40" height="18" fill="#c9452f"/>
    <rect x="316" y="180" width="12" height="120" fill="#000" opacity=".16"/>
    <rect x="286" y="180" width="6" height="120" fill="#fff" opacity=".25"/>
  </g>
  <path d="M289 292 L295 186 L315 186 L321 292 Z" fill="none" stroke="#3a3830" stroke-width="1.2"/>

  <!-- gallery -->
  <rect x="286" y="180" width="38" height="7" rx="2" fill="#3f4a5a"/>
  <rect x="288" y="174" width="34" height="6" fill="#55606f" opacity=".8"/>
  <!-- lamp room -->
  <rect x="295" y="158" width="20" height="17" fill="#2c3440"/>
  <circle cx="305" cy="167" r="34" fill="url(#lampGlow)"/>
  <rect x="297" y="160" width="16" height="13" fill="#ffe680"/>
  <rect x="304" y="158" width="2" height="17" fill="#2c3440"/>
  <polygon points="291,158 305,142 319,158" fill="#c9452f"/>
  <rect x="304" y="132" width="2" height="11" fill="#2c3440"/>
  <circle cx="305" cy="131" r="2.5" fill="#2c3440"/>

  <!-- door & window -->
  <path d="M301 292 v-14 a4 4 0 0 1 8 0 v14 z" fill="#38302a"/>
  <rect x="301" y="232" width="7" height="8" rx="1" fill="#ffd977" opacity=".85"/>
  <rect x="301" y="206" width="7" height="8" rx="1" fill="#ffd977" opacity=".6"/>

  <!-- rocks foreground -->
  <path d="M0 400 L0 372 q30 -14 62 -4 q34 10 52 32 z" fill="#0a0c18"/>
  <ellipse cx="150" cy="396" rx="34" ry="10" fill="#0a0c18"/>

  <!-- birds -->
  <g stroke="#dfe6ff" stroke-width="1.6" fill="none" opacity=".65">
    <path d="M56 130 q6 -6 12 0 q6 -6 12 0"/>
    <path d="M148 150 q5 -5 10 0 q5 -5 10 0"/>
    <path d="M110 168 q4 -4 8 0 q4 -4 8 0"/>
  </g>
</svg>