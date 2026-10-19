```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#2a1b4a"/>
      <stop offset="100%" stop-color="#0a0516"/>
    </radialGradient>
    <radialGradient id="body" cx="40%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#ff9ad1"/>
      <stop offset="60%" stop-color="#8a3cc9"/>
      <stop offset="100%" stop-color="#2b0a4a"/>
    </radialGradient>
    <linearGradient id="wing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7af0ff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#ff6ec7" stop-opacity="0.5"/>
    </linearGradient>
    <radialGradient id="eye" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fffde0"/>
      <stop offset="60%" stop-color="#ffd84a"/>
      <stop offset="100%" stop-color="#8a4b00"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- estrellitas -->
  <g fill="#fff">
    <circle cx="40" cy="60" r="1.2"/>
    <circle cx="360" cy="80" r="1.5"/>
    <circle cx="320" cy="30" r="1"/>
    <circle cx="80" cy="340" r="1.3"/>
    <circle cx="370" cy="300" r="1.1"/>
    <circle cx="20" cy="200" r="0.9"/>
    <circle cx="200" cy="20" r="1.4"/>
  </g>

  <!-- alas de mariposa -->
  <g>
    <path d="M200,200 Q90,120 60,200 Q90,260 200,230 Z" fill="url(#wing)" stroke="#4a1b6a" stroke-width="2"/>
    <path d="M200,200 Q310,120 340,200 Q310,260 200,230 Z" fill="url(#wing)" stroke="#4a1b6a" stroke-width="2"/>
    <circle cx="110" cy="190" r="10" fill="#ff2d8a" opacity="0.7"/>
    <circle cx="290" cy="190" r="10" fill="#ff2d8a" opacity="0.7"/>
  </g>

  <!-- cuerpo tipo pez con escamas -->
  <ellipse cx="200" cy="220" rx="55" ry="40" fill="url(#body)" stroke="#2b0a4a" stroke-width="2"/>
  <g fill="none" stroke="#ffb3e6" stroke-width="1" opacity="0.7">
    <path d="M170,210 q10,-8 20,0"/>
    <path d="M190,210 q10,-8 20,0"/>
    <path d="M210,210 q10,-8 20,0"/>
    <path d="M160,225 q10,-8 20,0"/>
    <path d="M180,225 q10,-8 20,0"/>
    <path d="M200,225 q10,-8 20,0"/>
    <path d="M220,225 q10,-8 20,0"/>
    <path d="M170,240 q10,-8 20,0"/>
    <path d="M190,240 q10,-8 20,0"/>
    <path d="M210,240 q10,-8 20,0"/>
  </g>

  <!-- cola de pavorreal -->
  <g transform="translate(255,220)">
    <ellipse cx="25" cy="-20" rx="30" ry="10" fill="#1b7a5a" transform="rotate(-30)"/>
    <ellipse cx="35" cy="0" rx="35" ry="10" fill="#2a9a7a"/>
    <ellipse cx="25" cy="20" rx="30" ry="10" fill="#1b7a5a" transform="rotate(30)"/>
    <circle cx="52" cy="-13" r="6" fill="#003355"/>
    <circle cx="52" cy="-13" r="3" fill="#ffcc33"/>
    <circle cx="68" cy="0" r="6" fill="#003355"/>
    <circle cx="68" cy="0" r="3" fill="#ffcc33"/>
    <circle cx="52" cy="13" r="6" fill="#003355"/>
    <circle cx="52" cy="13" r="3" fill="#ffcc33"/>
  </g>

  <!-- cabeza de gato -->
  <circle cx="160" cy="170" r="38" fill="url(#body)" stroke="#2b0a4a" stroke-width="2"/>
  <!-- orejas -->
  <polygon points="130,145 140,110 155,140" fill="#8a3cc9" stroke="#2b0a4a" stroke-width="2"/>
  <polygon points="190,145 180,110 165,140" fill="#8a3cc9" stroke="#2b0a4a" stroke-width="2"/>
  <polygon points="135,138 142,120 150,138" fill="#ff9ad1"/>
  <polygon points="185,138 178,120 170,138" fill="#ff9ad1"/>

  <!-- cuerno de unicornio -->
  <polygon points="160,110 152,70 168,70" fill="#ffd84a" stroke="#8a4b00" stroke-width="1.5"/>
  <line x1="156" y1="100" x2="164" y2="98" stroke="#8a4b00"/>
  <line x1="154" y1="90" x2="166" y2="88" stroke="#8a4b00"/>
  <line x1="153" y1="80" x2="167" y2="78" stroke="#8a4b00"/>

  <!-- ojos -->
  <circle cx="146" cy="170" r="8" fill="url(#eye)"/>
  <ellipse cx="146" cy="170" rx="2" ry="7" fill="#000"/>
  <circle cx="174" cy="170" r="8" fill="url(#eye)"/>
  <ellipse cx="174" cy="170" rx="2" ry="7" fill="#000"/>

  <!-- nariz -->
  <polygon points="156,183 164,183 160,189" fill="#ff2d8a"/>
  <!-- boca con colmillos -->
  <path d="M160,189 Q155,196 148,194 M160,189 Q165,196 172,194" fill="none" stroke="#2b0a4a" stroke-width="1.5"/>
  <polygon points="155,194 157,201 159,194" fill="#fff"/>
  <polygon points="161,194 163,201 165,194" fill="#fff"/>
  <!-- bigotes -->
  <g stroke="#fff" stroke-width="0.8" opacity="0.8">
    <line x1="130" y1="185" x2="105" y2="180"/>
    <line x1="130" y1="190" x2="105" y2="192"/>
    <line x1="190" y1="185" x2="215" y2="180"/>
    <line x1="190" y1="190" x2="215" y2="192"/>
  </g>

  <!-- patas de pulpo -->
  <g fill="url(#body)" stroke="#2b0a4a" stroke-width="1.5">
    <path d="M170,255 Q160,290 180,310 Q190,320 175,335 Q165,345 180,355"/>
    <path d="M190,260 Q185,300 200,325 Q210,340 195,355"/>
    <path d="M210,260 Q215,300 200,325 Q190,340 205,355"/>
    <path d="M225,255 Q240,290 220,310 Q210,320 225,335 Q235,345 220,355"/>
    <path d="M200,260 Q200,310 200,360"/>
  </g>
  <g fill="#ff9ad1">
    <circle cx="178" cy="320" r="2"/>
    <circle cx="183" cy="340" r="2"/>
    <circle cx="196" cy="330" r="2"/>
    <circle cx="203" cy="345" r="2"/>
    <circle cx="222" cy="320" r="2"/>
    <circle cx="217" cy="340" r="2"/>
    <circle cx="200" cy="300" r="2"/>
    <circle cx="200" cy="340" r="2"/>
  </g>

  <!-- antenas -->
  <path d="M145,115 Q130,90 115,95" fill="none" stroke="#2b0a4a" stroke-width="1.5"/>
  <path d="M175,115 Q190,90 205,95" fill="none" stroke="#2b0a4a" stroke-width="1.5"/>
  <circle cx="115" cy="95" r="3" fill="#7af0ff"/>
  <circle cx="205" cy="95" r="3" fill="#7af0ff"/>
</svg>
```