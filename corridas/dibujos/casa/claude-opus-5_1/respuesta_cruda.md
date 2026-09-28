```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#7ec8f0"/>
      <stop offset="60%" stop-color="#c7e9f7"/>
      <stop offset="100%" stop-color="#ffe4c4"/>
    </linearGradient>
    <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f6e2c3"/>
      <stop offset="100%" stop-color="#e2c69c"/>
    </linearGradient>
    <linearGradient id="roofg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#b8462f"/>
      <stop offset="100%" stop-color="#8c3220"/>
    </linearGradient>
    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8ebf5f"/>
      <stop offset="100%" stop-color="#5d8f3c"/>
    </linearGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#cfeaf7"/>
      <stop offset="50%" stop-color="#8fc4de"/>
      <stop offset="100%" stop-color="#5f9bbd"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- sol -->
  <circle cx="330" cy="70" r="28" fill="#ffd95e" opacity="0.95"/>
  <circle cx="330" cy="70" r="40" fill="#ffd95e" opacity="0.2"/>

  <!-- nubes -->
  <g fill="#ffffff" opacity="0.85">
    <ellipse cx="80" cy="70" rx="30" ry="16"/>
    <ellipse cx="105" cy="62" rx="22" ry="18"/>
    <ellipse cx="55" cy="76" rx="20" ry="12"/>
    <ellipse cx="250" cy="45" rx="24" ry="12"/>
    <ellipse cx="270" cy="40" rx="18" ry="14"/>
  </g>

  <!-- colinas -->
  <path d="M0 300 Q70 255 150 292 Q230 330 300 288 Q350 258 400 296 L400 400 L0 400 Z" fill="#6fa64a"/>
  <rect x="0" y="300" width="400" height="100" fill="url(#ground)"/>

  <!-- arbol -->
  <rect x="47" y="250" width="12" height="55" fill="#7b5334" rx="3"/>
  <circle cx="53" cy="235" r="28" fill="#4e8b3a"/>
  <circle cx="34" cy="248" r="19" fill="#5c9e44"/>
  <circle cx="72" cy="248" r="19" fill="#437b32"/>
  <circle cx="53" cy="255" r="20" fill="#59983f"/>

  <!-- sombra casa -->
  <ellipse cx="215" cy="308" rx="115" ry="14" fill="#3f6b2c" opacity="0.35"/>

  <!-- cuerpo -->
  <rect x="130" y="190" width="160" height="115" fill="url(#wall)" stroke="#a98a5f" stroke-width="2"/>

  <!-- garage / ala lateral -->
  <rect x="285" y="225" width="62" height="80" fill="#eed7b3" stroke="#a98a5f" stroke-width="2"/>
  <path d="M280 228 L316 200 L352 228 Z" fill="url(#roofg)" stroke="#6f2718" stroke-width="2" stroke-linejoin="round"/>
  <rect x="298" y="250" width="36" height="55" fill="#a9754a" stroke="#7b5334" stroke-width="2"/>
  <g stroke="#7b5334" stroke-width="1.5">
    <line x1="298" y1="264" x2="334" y2="264"/>
    <line x1="298" y1="278" x2="334" y2="278"/>
    <line x1="298" y1="292" x2="334" y2="292"/>
  </g>

  <!-- chimenea -->
  <rect x="243" y="130" width="20" height="45" fill="#9c4a33" stroke="#6f2718" stroke-width="2"/>
  <rect x="239" y="124" width="28" height="10" fill="#7c3726" stroke="#6f2718" stroke-width="2"/>
  <g fill="#ffffff" opacity="0.55">
    <circle cx="253" cy="112" r="7"/>
    <circle cx="261" cy="98" r="9"/>
    <circle cx="252" cy="82" r="11"/>
  </g>

  <!-- techo -->
  <path d="M112 196 L210 122 L308 196 Z" fill="url(#roofg)" stroke="#6f2718" stroke-width="3" stroke-linejoin="round"/>
  <path d="M112 196 L308 196 L308 205 L112 205 Z" fill="#7c3726"/>

  <!-- ventana atico -->
  <circle cx="210" cy="172" r="14" fill="url(#glass)" stroke="#6f2718" stroke-width="3"/>
  <path d="M196 172 h28 M210 158 v28" stroke="#6f2718" stroke-width="2"/>

  <!-- puerta -->
  <rect x="192" y="238" width="40" height="67" rx="3" fill="#8b5a2b" stroke="#5f3a18" stroke-width="2"/>
  <rect x="199" y="248" width="26" height="22" fill="#a3703a" stroke="#5f3a18" stroke-width="1.5"/>
  <rect x="199" y="278" width="26" height="20" fill="#a3703a" stroke="#5f3a18" stroke-width="1.5"/>
  <circle cx="225" cy="274" r="2.6" fill="#ffd95e"/>
  <rect x="186" y="303" width="52" height="6" fill="#cbb48d" stroke="#a98a5f"/>

  <!-- ventanas -->
  <g stroke="#6f4a24" stroke-width="3">
    <rect x="148" y="222" width="34" height="34" fill="url(#glass)"/>
    <rect x="244" y="222" width="34" height="34" fill="url(#glass)"/>
  </g>
  <g stroke="#6f4a24" stroke-width="2">
    <line x1="165" y1="222" x2="165" y2="256"/>
    <line x1="148" y1="239" x2="182" y2="239"/>
    <line x1="261" y1="222" x2="261" y2="256"/>
    <line x1="244" y1="239" x2="278" y2="239"/>
  </g>
  <rect x="144" y="256" width="42" height="5" fill="#cbb48d" stroke="#a98a5f"/>
  <rect x="240" y="256" width="42" height="5" fill="#cbb48d" stroke="#a98a5f"/>

  <!-- jardineras -->
  <rect x="147" y="261" width="36" height="10" fill="#8b5a2b"/>
  <g fill="#e7568c"><circle cx="154" cy="260" r="4"/><circle cx="165" cy="258" r="4"/><circle cx="176" cy="260" r="4"/></g>

  <!-- camino -->
  <path d="M200 309 L224 309 L246 400 L178 400 Z" fill="#d6c7a6" stroke="#b8a482" stroke-width="2"/>
  <g stroke="#b8a482" stroke-width="2">
    <line x1="196" y1="330" x2="228" y2="330"/>
    <line x1="188" y1="358" x2="236" y2="358"/>
  </g>

  <!-- arbustos -->
  <circle cx="126" cy="300" r="14" fill="#4e8b3a"/>
  <circle cx="140" cy="303" r="10" fill="#5c9e44"/>
  <circle cx="356" cy="302" r="13" fill="#4e8b3a"/>
  <circle cx="370" cy="305" r="9" fill="#5c9e44"/>

  <!-- flores -->
  <g>
    <circle cx="96" cy="340" r="4" fill="#f5d442"/>
    <circle cx="300" cy="350" r="4" fill="#ff7f7f"/>
    <circle cx="340" cy="332" r="4" fill="#f5d442"/>
    <circle cx="60" cy="372" r="4" fill="#ff7f7f"/>
    <circle cx="130" cy="366" r="4" fill="#ffffff"/>
  </g>

  <!-- pajaros -->
  <g stroke="#3a3a3a" stroke-width="2" fill="none" stroke-linecap="round">
    <path d="M140 100 q7 -7 14 0"/>
    <path d="M154 100 q7 -7 14 0"/>
    <path d="M170 82 q5 -5 10 0"/>
    <path d="M180 82 q5 -5 10 0"/>
  </g>
</svg>
```