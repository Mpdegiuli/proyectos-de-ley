<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5aa9e6"/>
      <stop offset="1" stop-color="#d6efff"/>
    </linearGradient>
    <linearGradient id="roof" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#b5482f"/>
      <stop offset="1" stop-color="#8a3220"/>
    </linearGradient>
    <linearGradient id="grass" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#6cc04a"/>
      <stop offset="1" stop-color="#3f8f2f"/>
    </linearGradient>
    <pattern id="brick" width="24" height="12" patternUnits="userSpaceOnUse">
      <rect width="24" height="12" fill="#f0d9b0"/>
      <path d="M0 0H24M0 6H24M0 12H24M6 0V6M18 6V12" stroke="#d9bc86" stroke-width="1" fill="none"/>
    </pattern>
    <radialGradient id="sun">
      <stop offset="0" stop-color="#fff7b0"/>
      <stop offset="1" stop-color="#ffd93b"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="330" cy="70" r="50" fill="#fff3a0" opacity="0.4"/>
  <circle cx="330" cy="70" r="32" fill="url(#sun)"/>

  <g fill="#fff" opacity="0.95">
    <ellipse cx="80" cy="70" rx="38" ry="14"/>
    <ellipse cx="105" cy="60" rx="28" ry="13"/>
    <ellipse cx="60" cy="62" rx="22" ry="10"/>
    <ellipse cx="240" cy="110" rx="30" ry="10"/>
    <ellipse cx="258" cy="102" rx="20" ry="9"/>
  </g>

  <path d="M0 300 Q90 250 190 290 T400 280 V400 H0Z" fill="#8cc97a"/>
  <rect y="295" width="400" height="105" fill="url(#grass)"/>

  <!-- camino -->
  <path d="M175 400 L190 320 H230 L250 400Z" fill="#d8c39a"/>
  <path d="M182 370H244M186 345H236" stroke="#b9a274" stroke-width="2"/>

  <!-- sombra -->
  <ellipse cx="200" cy="322" rx="140" ry="9" fill="#000" opacity="0.15"/>

  <!-- chimenea -->
  <rect x="265" y="110" width="30" height="70" fill="#a35a3c"/>
  <rect x="261" y="104" width="38" height="10" fill="#7a3f28"/>
  <g fill="#ddd" opacity="0.7">
    <circle cx="280" cy="90" r="8"/>
    <circle cx="288" cy="72" r="11"/>
    <circle cx="300" cy="50" r="14"/>
  </g>

  <!-- paredes -->
  <rect x="80" y="170" width="240" height="150" fill="url(#brick)" stroke="#b89a68" stroke-width="2"/>
  <rect x="80" y="308" width="240" height="12" fill="#9a8f80"/>

  <!-- techo -->
  <path d="M55 178 L200 75 L345 178Z" fill="url(#roof)"/>
  <path d="M55 178 L200 75 L345 178" fill="none" stroke="#5e2114" stroke-width="5" stroke-linejoin="round"/>
  <g stroke="#6e2818" stroke-width="1.5" opacity="0.6">
    <path d="M85 157H315M110 137H290M135 117H265M160 97H240"/>
  </g>
  <rect x="50" y="176" width="300" height="8" fill="#5e2114"/>

  <!-- ventana del ático -->
  <circle cx="200" cy="135" r="16" fill="#f5f0e6" stroke="#5e3a22" stroke-width="4"/>
  <circle cx="200" cy="135" r="12" fill="#9fd4f5"/>
  <path d="M200 123V147M188 135H212" stroke="#5e3a22" stroke-width="2"/>

  <!-- puerta -->
  <rect x="172" y="234" width="56" height="86" rx="3" fill="#f5f0e6"/>
  <path d="M177 320V246Q177 238 200 238T223 246V320Z" fill="#7a4a2b" stroke="#4d2c16" stroke-width="2"/>
  <path d="M200 238V320" stroke="#4d2c16" stroke-width="1.5"/>
  <rect x="183" y="250" width="12" height="24" rx="2" fill="none" stroke="#4d2c16" stroke-width="1.5"/>
  <rect x="205" y="250" width="12" height="24" rx="2" fill="none" stroke="#4d2c16" stroke-width="1.5"/>
  <circle cx="194" cy="284" r="3" fill="#ffd54a"/>
  <rect x="164" y="320" width="72" height="6" fill="#b0a898"/>

  <!-- ventanas -->
  <g>
    <rect x="98" y="220" width="52" height="56" fill="#5e3a22"/>
    <rect x="102" y="224" width="44" height="48" fill="#a9dcf7"/>
    <path d="M102 224 L146 224 L102 262Z" fill="#fff" opacity="0.35"/>
    <path d="M124 224V272M102 248H146" stroke="#f5f0e6" stroke-width="3"/>
    <rect x="94" y="276" width="60" height="7" fill="#f5f0e6" stroke="#b9ae9c"/>

    <rect x="250" y="220" width="52" height="56" fill="#5e3a22"/>
    <rect x="254" y="224" width="44" height="48" fill="#a9dcf7"/>
    <path d="M254 224 L298 224 L254 262Z" fill="#fff" opacity="0.35"/>
    <path d="M276 224V272M254 248H298" stroke="#f5f0e6" stroke-width="3"/>
    <rect x="246" y="276" width="60" height="7" fill="#f5f0e6" stroke="#b9ae9c"/>
  </g>

  <!-- postigos -->
  <g fill="#2f7a5a">
    <rect x="84" y="220" width="12" height="56"/>
    <rect x="152" y="220" width="12" height="56"/>
    <rect x="236" y="220" width="12" height="56"/>
    <rect x="304" y="220" width="12" height="56"/>
  </g>

  <!-- macetas -->
  <g>
    <path d="M96 283H152L148 270H100Z" fill="#8b4a2b"/>
    <circle cx="106" cy="266" r="5" fill="#e63946"/>
    <circle cx="124" cy="264" r="5" fill="#ff8fab"/>
    <circle cx="142" cy="266" r="5" fill="#ffd166"/>
    <path d="M248 283H304L300 270H252Z" fill="#8b4a2b"/>
    <circle cx="258" cy="266" r="5" fill="#ffd166"/>
    <circle cx="276" cy="264" r="5" fill="#e63946"/>
    <circle cx="294" cy="266" r="5" fill="#ff8fab"/>
  </g>

  <!-- arbustos -->
  <g fill="#2f8f3a">
    <circle cx="70" cy="315" r="20"/>
    <circle cx="92" cy="322" r="16"/>
    <circle cx="330" cy="315" r="20"/>
    <circle cx="308" cy="322" r="16"/>
  </g>
  <g fill="#49b04f">
    <circle cx="64" cy="309" r="9"/>
    <circle cx="324" cy="309" r="9"/>
  </g>

  <!-- árbol -->
  <rect x="26" y="230" width="14" height="90" fill="#7a4a2b"/>
  <circle cx="33" cy="215" r="34" fill="#2f8f3a"/>
  <circle cx="15" cy="235" r="22" fill="#3aa347"/>
  <circle cx="52" cy="232" r="22" fill="#3aa347"/>
  <circle cx="30" cy="200" r="16" fill="#52b95a"/>

  <!-- cerca -->
  <g fill="#fff" stroke="#c9c2b5" stroke-width="1">
    <path d="M338 350h8v-30l-4-5-4 5zM354 350h8v-30l-4-5-4 5zM370 350h8v-30l-4-5-4 5zM386 350h8v-30l-4-5-4 5z"/>
  </g>
  <rect x="334" y="328" width="64" height="5" fill="#fff" stroke="#c9c2b5"/>

  <!-- pájaros -->
  <path d="M140 40q8-8 16 0q8-8 16 0M180 25q6-6 12 0q6-6 12 0" fill="none" stroke="#333" stroke-width="2" stroke-linecap="round"/>
</svg>