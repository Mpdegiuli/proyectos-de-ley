<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd9a8"/>
      <stop offset="1" stop-color="#f6a5a0"/>
    </linearGradient>
    <linearGradient id="shirt" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#2f7f9e"/>
      <stop offset="1" stop-color="#1d5670"/>
    </linearGradient>
    <radialGradient id="skin" cx="0.4" cy="0.35" r="0.8">
      <stop offset="0" stop-color="#f6c7a0"/>
      <stop offset="1" stop-color="#dc9f78"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="320" cy="80" r="35" fill="#fff2c9" opacity="0.9"/>
  <path d="M0 310 Q100 270 200 300 T400 290 V400 H0Z" fill="#c97b84" opacity="0.5"/>

  <!-- torso -->
  <path d="M95 400 Q100 305 160 290 L240 290 Q300 305 305 400Z" fill="url(#shirt)"/>
  <!-- cuello -->
  <path d="M175 255 H225 V295 Q200 315 175 295Z" fill="#d49470"/>
  <!-- cuello camisa -->
  <path d="M160 290 L200 325 L240 290 L228 284 L200 308 L172 284Z" fill="#e8f3f7"/>

  <!-- orejas -->
  <ellipse cx="137" cy="205" rx="10" ry="16" fill="#dc9f78"/>
  <ellipse cx="263" cy="205" rx="10" ry="16" fill="#dc9f78"/>

  <!-- pelo atrás -->
  <path d="M132 200 Q120 100 200 90 Q285 100 268 200 Q270 140 200 130 Q135 140 132 200Z" fill="#3a2418"/>

  <!-- cara -->
  <ellipse cx="200" cy="200" rx="65" ry="78" fill="url(#skin)"/>

  <!-- flequillo -->
  <path d="M135 190 Q130 105 205 100 Q275 105 265 190 Q255 145 225 135 Q185 150 150 140 Q138 160 135 190Z" fill="#4a2e1e"/>
  <path d="M160 125 Q200 105 245 125" stroke="#6a4630" stroke-width="3" fill="none" opacity="0.6"/>

  <!-- cejas -->
  <path d="M164 178 Q177 170 190 177" stroke="#3a2418" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M210 177 Q223 170 236 178" stroke="#3a2418" stroke-width="4" fill="none" stroke-linecap="round"/>

  <!-- ojos -->
  <ellipse cx="177" cy="198" rx="10" ry="7" fill="#fff"/>
  <ellipse cx="223" cy="198" rx="10" ry="7" fill="#fff"/>
  <circle cx="179" cy="198" r="5" fill="#4b2e1a"/>
  <circle cx="225" cy="198" r="5" fill="#4b2e1a"/>
  <circle cx="180.5" cy="196" r="1.6" fill="#fff"/>
  <circle cx="226.5" cy="196" r="1.6" fill="#fff"/>

  <!-- nariz -->
  <path d="M200 200 Q193 222 200 228 Q207 229 209 224" stroke="#b97a58" stroke-width="3" fill="none" stroke-linecap="round"/>

  <!-- mejillas -->
  <circle cx="163" cy="228" r="11" fill="#f19a8f" opacity="0.4"/>
  <circle cx="237" cy="228" r="11" fill="#f19a8f" opacity="0.4"/>

  <!-- boca -->
  <path d="M176 245 Q200 268 224 245 Q200 254 176 245Z" fill="#a8434a" stroke="#8a2f38" stroke-width="2" stroke-linejoin="round"/>

  <!-- anteojos -->
  <g fill="none" stroke="#222" stroke-width="3">
    <rect x="158" y="184" width="40" height="30" rx="12"/>
    <rect x="202" y="184" width="40" height="30" rx="12"/>
    <path d="M198 196 Q200 192 202 196"/>
    <path d="M158 194 L140 190"/>
    <path d="M242 194 L260 190"/>
  </g>
</svg>