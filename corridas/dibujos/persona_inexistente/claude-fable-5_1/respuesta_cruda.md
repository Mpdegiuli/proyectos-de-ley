<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2b3a55"/>
      <stop offset="1" stop-color="#4d5f82"/>
    </linearGradient>
    <linearGradient id="piel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e8b68f"/>
      <stop offset="1" stop-color="#d29a72"/>
    </linearGradient>
    <linearGradient id="pelo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3a2a22"/>
      <stop offset="1" stop-color="#241811"/>
    </linearGradient>
    <linearGradient id="ropa" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#7a4f8f"/>
      <stop offset="1" stop-color="#5a3a6e"/>
    </linearGradient>
  </defs>

  <!-- fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="320" cy="80" r="46" fill="#6e80a6" opacity="0.5"/>
  <circle cx="70" cy="300" r="60" fill="#3a4a6b" opacity="0.6"/>

  <!-- hombros y torso -->
  <path d="M110 400 Q112 330 150 310 Q175 297 200 296 Q225 297 250 310 Q288 330 290 400 Z" fill="url(#ropa)"/>
  <path d="M150 312 Q175 300 200 299 Q225 300 250 312 L250 340 Q200 325 150 340 Z" fill="#4a2f5c"/>

  <!-- cuello -->
  <path d="M182 260 L182 305 Q200 318 218 305 L218 260 Z" fill="url(#piel)"/>
  <path d="M182 260 Q200 282 218 260 L218 278 Q200 292 182 278 Z" fill="#c08c62"/>

  <!-- orejas -->
  <ellipse cx="139" cy="200" rx="12" ry="18" fill="url(#piel)"/>
  <ellipse cx="261" cy="200" rx="12" ry="18" fill="url(#piel)"/>
  <path d="M137 194 q6 4 4 12" stroke="#b9835c" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M263 194 q-6 4 -4 12" stroke="#b9835c" stroke-width="2" fill="none" stroke-linecap="round"/>
  <circle cx="261" cy="216" r="3" fill="#e8c860"/>

  <!-- cara -->
  <path d="M145 170 Q145 110 200 108 Q255 110 255 170 Q255 215 240 240 Q222 268 200 268 Q178 268 160 240 Q145 215 145 170 Z" fill="url(#piel)"/>

  <!-- pelo -->
  <path d="M138 195 Q128 120 170 95 Q200 78 232 92 Q272 110 264 195 Q262 170 252 158 Q254 138 240 128 Q244 145 236 152 Q230 122 200 120 Q170 122 164 152 Q156 145 160 128 Q146 138 148 158 Q140 170 138 195 Z" fill="url(#pelo)"/>
  <path d="M160 128 Q158 112 176 102 Q168 116 170 126 Z" fill="#4a382c" opacity="0.7"/>
  <path d="M240 128 Q242 112 224 102 Q232 116 230 126 Z" fill="#4a382c" opacity="0.7"/>

  <!-- cejas -->
  <path d="M158 172 Q172 163 188 170" stroke="#2e2018" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M212 170 Q228 163 242 172" stroke="#2e2018" stroke-width="5" fill="none" stroke-linecap="round"/>

  <!-- ojos -->
  <g>
    <ellipse cx="173" cy="190" rx="14" ry="9" fill="#fff"/>
    <circle cx="175" cy="191" r="6" fill="#5b4028"/>
    <circle cx="175" cy="191" r="2.6" fill="#1b120b"/>
    <circle cx="177.5" cy="188.5" r="1.6" fill="#fff"/>
    <path d="M159 189 Q173 179 187 189" stroke="#8a5f3e" stroke-width="2" fill="none"/>
  </g>
  <g>
    <ellipse cx="227" cy="190" rx="14" ry="9" fill="#fff"/>
    <circle cx="225" cy="191" r="6" fill="#5b4028"/>
    <circle cx="225" cy="191" r="2.6" fill="#1b120b"/>
    <circle cx="227.5" cy="188.5" r="1.6" fill="#fff"/>
    <path d="M213 189 Q227 179 241 189" stroke="#8a5f3e" stroke-width="2" fill="none"/>
  </g>

  <!-- nariz -->
  <path d="M198 196 Q195 216 190 222 Q196 228 204 224" stroke="#b9835c" stroke-width="3" fill="none" stroke-linecap="round"/>

  <!-- boca -->
  <path d="M178 240 Q200 254 222 240 Q210 246 200 246 Q190 246 178 240 Z" fill="#a95050"/>
  <path d="M178 240 Q200 250 222 240" stroke="#7c3a3a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M186 236 Q200 242 214 236" stroke="#c96a6a" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.7"/>

  <!-- rubor y detalles -->
  <ellipse cx="163" cy="218" rx="11" ry="6" fill="#d97e5e" opacity="0.35"/>
  <ellipse cx="237" cy="218" rx="11" ry="6" fill="#d97e5e" opacity="0.35"/>
  <circle cx="232" cy="228" r="1.8" fill="#7a4a2e"/>

  <!-- collar -->
  <path d="M170 322 Q200 342 230 322" stroke="#e8c860" stroke-width="3" fill="none"/>
  <circle cx="200" cy="338" r="5" fill="#e8c860"/>
</svg>