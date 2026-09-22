```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#050a23"/>
      <stop offset="45%" stop-color="#132048"/>
      <stop offset="75%" stop-color="#3b3a6b"/>
      <stop offset="100%" stop-color="#7a5a7a"/>
    </linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a3563"/>
      <stop offset="100%" stop-color="#0a1130"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#fff6c8" stop-opacity="0.95"/>
      <stop offset="40%" stop-color="#ffe17a" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#ffd24a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff4c0" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#fff4c0" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="moonG" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#fdfbe8" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#fdfbe8" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- estrellas -->
  <g fill="#ffffff">
    <circle cx="28" cy="34" r="1.4" opacity=".9"/>
    <circle cx="66" cy="18" r="1" opacity=".7"/>
    <circle cx="103" cy="52" r="1.6" opacity=".95"/>
    <circle cx="142" cy="26" r="1" opacity=".6"/>
    <circle cx="176" cy="62" r="1.3" opacity=".8"/>
    <circle cx="215" cy="30" r="0.9" opacity=".65"/>
    <circle cx="248" cy="70" r="1.5" opacity=".9"/>
    <circle cx="286" cy="20" r="1.1" opacity=".75"/>
    <circle cx="330" cy="58" r="1.3" opacity=".85"/>
    <circle cx="368" cy="32" r="1" opacity=".6"/>
    <circle cx="48" cy="92" r="1.2" opacity=".7"/>
    <circle cx="124" cy="104" r="0.9" opacity=".55"/>
    <circle cx="196" cy="118" r="1.1" opacity=".6"/>
    <circle cx="306" cy="112" r="1" opacity=".5"/>
    <circle cx="358" cy="96" r="1.4" opacity=".8"/>
    <circle cx="14" cy="140" r="0.9" opacity=".45"/>
    <circle cx="86" cy="146" r="1" opacity=".5"/>
  </g>

  <!-- luna -->
  <circle cx="312" cy="80" r="42" fill="url(#moonG)"/>
  <circle cx="312" cy="80" r="20" fill="#fdfbe8"/>
  <circle cx="306" cy="74" r="4" fill="#ece9d0" opacity=".8"/>
  <circle cx="318" cy="88" r="3" fill="#ece9d0" opacity=".7"/>
  <circle cx="317" cy="70" r="2" fill="#ece9d0" opacity=".6"/>

  <!-- nubes -->
  <g fill="#ffffff" opacity=".10">
    <ellipse cx="90" cy="120" rx="60" ry="12"/>
    <ellipse cx="130" cy="112" rx="38" ry="9"/>
    <ellipse cx="300" cy="150" rx="70" ry="11"/>
    <ellipse cx="250" cy="144" rx="40" ry="8"/>
  </g>

  <!-- haz de luz -->
  <g opacity=".85">
    <polygon points="122,196 400,120 400,250" fill="url(#beam)"/>
    <polygon points="122,196 0,150 0,238" fill="url(#beam)" transform="scale(-1,1) translate(-400,0)" opacity="0"/>
    <polygon points="122,196 -20,142 -20,232" fill="url(#beam)" transform="rotate(180 122 196)" opacity=".35"/>
  </g>

  <!-- mar -->
  <rect x="0" y="260" width="400" height="140" fill="url(#sea)"/>
  <!-- reflejo lunar -->
  <g fill="#fdfbe8" opacity=".18">
    <rect x="296" y="266" width="32" height="3" rx="1.5"/>
    <rect x="288" y="278" width="48" height="3" rx="1.5"/>
    <rect x="300" y="290" width="26" height="2.5" rx="1.2"/>
    <rect x="284" y="302" width="54" height="3" rx="1.5"/>
    <rect x="298" y="316" width="30" height="2.5" rx="1.2"/>
  </g>
  <!-- olas -->
  <g stroke="#8fa8d8" fill="none" opacity=".35" stroke-linecap="round">
    <path d="M10 274 q10 -5 20 0 t20 0" stroke-width="1.6"/>
    <path d="M70 288 q12 -6 24 0 t24 0" stroke-width="1.6"/>
    <path d="M150 272 q10 -5 20 0 t20 0" stroke-width="1.4"/>
    <path d="M20 312 q14 -7 28 0 t28 0" stroke-width="1.8"/>
    <path d="M120 330 q16 -8 32 0 t32 0" stroke-width="1.8"/>
    <path d="M250 300 q12 -6 24 0 t24 0" stroke-width="1.5"/>
    <path d="M230 344 q18 -8 36 0 t36 0" stroke-width="2"/>
    <path d="M40 360 q18 -9 36 0 t36 0" stroke-width="2.2"/>
    <path d="M180 378 q20 -9 40 0 t40 0" stroke-width="2.4"/>
    <path d="M300 368 q16 -8 32 0 t32 0" stroke-width="2"/>
  </g>

  <!-- barquito -->
  <g transform="translate(60,296)">
    <path d="M-16 0 L16 0 L11 9 L-11 9 Z" fill="#1b1b2e"/>
    <rect x="-1" y="-22" width="2" height="22" fill="#1b1b2e"/>
    <path d="M1 -21 L13 -3 L1 -3 Z" fill="#2c2c4a"/>
    <path d="M-2 -18 L-11 -3 L-2 -3 Z" fill="#23233c"/>
  </g>

  <!-- roca -->
  <path d="M60 268 Q100 254 150 258 Q200 262 230 272 L240 300 L60 300 Z" fill="#16182c"/>
  <path d="M90 262 Q120 252 155 259 Q185 264 200 272 L100 274 Z" fill="#1e2138" opacity=".8"/>

  <!-- faro -->
  <g>
    <path d="M108 258 L136 258 L131 190 L113 190 Z" fill="#e8e6dd"/>
    <path d="M113 190 L131 190 L132 202 L112 202 Z" fill="#cf4b43"/>
    <path d="M110.5 222 L133.5 222 L134.5 234 L109.5 234 Z" fill="#cf4b43"/>
    <path d="M108.2 254 L135.8 254 L136 258 L108 258 Z" fill="#cf4b43"/>
    <path d="M124 190 L131 190 L136 258 L128 258 Z" fill="#000" opacity=".12"/>
    <!-- galería -->
    <rect x="108" y="184" width="28" height="6" rx="1.5" fill="#3a3f55"/>
    <!-- linterna -->
    <rect x="113" y="168" width="18" height="17" rx="1.5" fill="#2d3247"/>
    <rect x="115" y="170" width="14" height="13" fill="#ffe9a0"/>
    <!-- techo -->
    <path d="M110 168 L134 168 L122 154 Z" fill="#cf4b43"/>
    <circle cx="122" cy="151" r="2.2" fill="#3a3f55"/>
    <!-- resplandor -->
    <circle cx="122" cy="176" r="34" fill="url(#glow)"/>
  </g>

  <!-- casita -->
  <g>
    <path d="M140 258 L140 240 L172 240 L172 258 Z" fill="#dedbd0"/>
    <path d="M136 241 L156 228 L176 241 Z" fill="#8f4a46"/>
    <rect x="148" y="246" width="8" height="12" fill="#4a4a66"/>
    <rect x="161" y="245" width="7" height="6" fill="#ffe9a0"/>
  </g>

  <!-- aves -->
  <g stroke="#0d1226" fill="none" stroke-width="1.8" stroke-linecap="round" opacity=".7">
    <path d="M238 112 q6 -6 12 0"/>
    <path d="M250 112 q6 -6 12 0"/>
    <path d="M262 132 q5 -5 10 0"/>
    <path d="M272 132 q5 -5 10 0"/>
  </g>
</svg>
```