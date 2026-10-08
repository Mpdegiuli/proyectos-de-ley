```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8ED1F5"/>
      <stop offset="1" stop-color="#DFF3FB"/>
    </linearGradient>
    <radialGradient id="sol" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#FFF6C9"/>
      <stop offset="0.6" stop-color="#FFD86B"/>
      <stop offset="1" stop-color="#FFC53D"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <circle cx="330" cy="66" r="34" fill="url(#sol)"/>
  <g stroke="#FFD86B" stroke-width="3" stroke-linecap="round" opacity="0.85">
    <line x1="330" y1="16" x2="330" y2="4"/>
    <line x1="330" y1="116" x2="330" y2="128"/>
    <line x1="280" y1="66" x2="268" y2="66"/>
    <line x1="380" y1="66" x2="392" y2="66"/>
    <line x1="295" y1="31" x2="287" y2="23"/>
    <line x1="365" y1="31" x2="373" y2="23"/>
    <line x1="295" y1="101" x2="287" y2="109"/>
    <line x1="365" y1="101" x2="373" y2="109"/>
  </g>

  <!-- arcoíris -->
  <g fill="none" stroke-width="7" opacity="0.55">
    <path d="M60 300 A140 140 0 0 1 340 300" stroke="#E5397E"/>
    <path d="M72 300 A128 128 0 0 1 328 300" stroke="#F2811D"/>
    <path d="M84 300 A116 116 0 0 1 316 300" stroke="#F7C325"/>
    <path d="M96 300 A104 104 0 0 1 304 300" stroke="#59B84E"/>
    <path d="M108 300 A92 92 0 0 1 292 300" stroke="#3E8ED0"/>
    <path d="M120 300 A80 80 0 0 1 280 300" stroke="#7A4FBF"/>
  </g>

  <!-- nubes -->
  <g fill="#FFFFFF" opacity="0.9">
    <ellipse cx="80" cy="60" rx="30" ry="13"/>
    <ellipse cx="105" cy="52" rx="22" ry="12"/>
    <ellipse cx="60" cy="52" rx="18" ry="10"/>
    <ellipse cx="200" cy="42" rx="26" ry="11"/>
    <ellipse cx="222" cy="35" rx="18" ry="9"/>
  </g>

  <!-- pájaros -->
  <g stroke="#4A5A6A" stroke-width="2.5" fill="none" stroke-linecap="round">
    <path d="M150 90 q7 -7 14 0 q7 -7 14 0"/>
    <path d="M195 72 q6 -6 12 0 q6 -6 12 0"/>
    <path d="M118 120 q5 -5 10 0 q5 -5 10 0"/>
  </g>

  <!-- colinas -->
  <path d="M0 400 L0 310 Q50 265 110 300 Q160 250 220 295 Q285 252 340 298 Q375 282 400 300 L400 400 Z" fill="#7CC26B"/>
  <path d="M0 400 L0 345 Q70 310 140 345 Q220 308 300 348 Q355 322 400 345 L400 400 Z" fill="#5FAE52"/>
  <ellipse cx="200" cy="398" rx="260" ry="48" fill="#4E9B44"/>

  <!-- paloma de la paz -->
  <g transform="translate(200 168)">
    <path d="M0 0 Q-14 -16 6 -22 Q2 -10 8 -8 Q20 -20 34 -14 Q26 -12 24 -6 Q34 -2 38 6 Q24 4 18 10 Q6 20 -8 14 Q-2 8 0 0 Z" fill="#FFFFFF" stroke="#C9D6DF" stroke-width="1"/>
    <circle cx="14" cy="-12" r="2" fill="#333"/>
    <path d="M10 -15 L18 -18 L11 -9 Z" fill="#F2A33C"/>
    <path d="M-4 -20 L-8 -28 L0 -24 Z" fill="#C9D6DF"/>
    <path d="M-6 15 q-8 4 -6 14 M4 16 q-4 6 -14 8" stroke="#4A5A6A" stroke-width="1.6" fill="none"/>
    <path d="M22 -10 L46 -26" stroke="#7CC26B" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M34 -12 L36 -6" stroke="#7CC26B" stroke-width="1.8" stroke-linecap="round" transform="rotate(20 34 -12)"/>
  </g>

  <!-- árboles -->
  <g>
    <g transform="translate(52 292)">
      <rect x="-3" y="0" width="6" height="22" fill="#7A5230" rx="2"/>
      <circle cx="0" cy="-10" r="17" fill="#3E8E41"/>
      <circle cx="-11" cy="-2" r="12" fill="#48A34B"/>
      <circle cx="11" cy="-2" r="12" fill="#48A34B"/>
    </g>
    <g transform="translate(352 300)">
      <rect x="-3" y="0" width="6" height="22" fill="#7A5230" rx="2"/>
      <circle cx="0" cy="-10" r="17" fill="#3E8E41"/>
      <circle cx="-11" cy="-2" r="12" fill="#48A34B"/>
      <circle cx="11" cy="-2" r="12" fill="#48A34B"/>
    </g>
    <g transform="translate(310 330)">
      <rect x="-2.5" y="0" width="5" height="16" fill="#7A5230" rx="2"/>
      <circle cx="0" cy="-7" r="12" fill="#3E8E41"/>
    </g>
  </g>

  <!-- flores -->
  <g>
    <g transform="translate(90 372)">
      <line x1="0" y1="0" x2="0" y2="-10" stroke="#4E9B44" stroke-width="1.6"/>
      <circle cx="0" cy="-12" r="3.2" fill="#F26D7D"/><circle cx="0" cy="-9" r="3.2" fill="#F26D7D"/>
      <circle cx="-3" cy="-10.5" r="3.2" fill="#F26D7D"/><circle cx="3" cy="-10.5" r="3.2" fill="#F26D7D"/>
      <circle cx="0" cy="-10.5" r="1.7" fill="#FFE066"/>
    </g>
    <g transform="translate(292 384)">
      <line x1="0" y1="0" x2="0" y2="-10" stroke="#4E9B44" stroke-width="1.6"/>
      <circle cx="0" cy="-12" r="3.2" fill="#7FB2F0"/><circle cx="0" cy="-9" r="3.2" fill="#7FB2F0"/>
      <circle cx="-3" cy="-10.5" r="3.2" fill="#7FB2F0"/><circle cx="3" cy="-10.5" r="3.2" fill="#7FB2F0"/>
      <circle cx="0" cy="-10.5" r="1.7" fill="#FFE066"/>
    </g>
    <g transform="translate(60 390)">
      <line x1="0" y1="0" x2="0" y2="-8" stroke="#4E9B44" stroke-width="1.6"/>
      <circle cx="0" cy="-10" r="2.8" fill="#C79BF2"/><circle cx="0" cy="-7.4" r="2.8" fill="#C79BF2"/>
      <circle cx="-2.6" cy="-8.8" r="2.8" fill="#C79BF2"/><circle cx="2.6" cy="-8.8" r="2.8" fill="#C79BF2"/>
      <circle cx="0" cy="-8.8" r="1.5" fill="#FFE066"/>
    </g>
  </g>

  <!-- personas tomadas de la mano (diversas) -->
  <g stroke-linecap="round">
    <!-- persona 1 -->
    <g transform="translate(128 340)">
      <circle cx="0" cy="-26" r="8" fill="#8D5524"/>
      <path d="M-7 -20 Q0 -25 7 -20 L7 -19 -7 -19 Z" fill="#2B2B2B"/>
      <line x1="0" y1="-18" x2="0" y2="-4" stroke="#E63946" stroke-width="7"/>
      <line x1="-4" y1="-15" x2="10" y2="-9" stroke="#E63946" stroke-width="4"/>
      <line x1="0" y1="-4" x2="-4" y2="6" stroke="#39425B" stroke-width="4"/>
      <line x1="0" y1="-4" x2="5" y2="6" stroke="#39425B" stroke-width="4"/>
    </g>
    <!-- persona 2 -->
    <g transform="translate(152 342)">
      <circle cx="0" cy="-28" r="8" fill="#F1C27D"/>
      <path d="M-8 -22 Q0 -27 8 -22 L8 -21 -8 -21 Z" fill="#6B3F1D"/>
      <line x1="0" y1="-20" x2="0" y2="-4" stroke="#2A9D8F" stroke-width="7"/>
      <line x1="-4" y1="-16" x2="-10" y2="-10" stroke="#2A9D8F" stroke-width="4"/>
      <line x1="4" y1="-16" x2="10" y2="-10" stroke="#2A9D8F" stroke-width="4"/>
      <line x1="0" y1="-4" x2="-4" y2="6" stroke="#264653" stroke-width="4"/>
      <line x1="0" y1="-4" x2="5" y2="6" stroke="#264653" stroke-width="4"/>
    </g>
    <!-- persona 3 (silla de ruedas) -->
    <g transform="translate(176 344)">
      <circle cx="0" cy="-26" r="8" fill="#C68642"/>
      <line x1="0" y1="-18" x2="0" y2="-8" stroke="#E9C46A" stroke-width="7"/>
      <line x1="-4" y1="-15" x2="-10" y2="-11" stroke="#E9C46A" stroke-width="4"/>
      <line x1="4" y1="-15" x2="10" y2="-11" stroke="#E9C46A" stroke-width="4"/>
      <circle cx="0" cy="0" r="9" fill="none" stroke="#556" stroke-width="2.5"/>
      <line x1="-8" y1="-3" x2="8" y2="-3" stroke="#556" stroke-width="2.5"/>
      <line x1="0" y1="-8" x2="0" y2="0" stroke="#556" stroke-width="2"/>
    </g>
    <!-- persona 4 -->
    <g transform="translate(200 340)">
      <circle cx="0" cy="-26" r="8" fill="#FFDBAC"/>
      <path d="M-8 -19 Q-9 -32 0 -32 Q9 -32 8 -19 Q0 -23 -8 -19 Z" fill="#4A2C12"/>
      <line x1="0" y1="-18" x2="0" y2="-4" stroke="#9B5DE5" stroke-width="7"/>
      <line x1="-4" y1="-15" x2="-10" y2="-9" stroke="#9B5DE5" stroke-width="4"/>
      <line x1="4" y1="-15" x2="10" y2="-9" stroke="#9B5DE5" stroke-width="4"/>
      <line x1="0" y1="-4" x2="-4" y2="6" stroke="#33334D" stroke-width="4"/>
      <line x1="0" y1="-4" x2="5" y2="6" stroke="#33334D" stroke-width="4"/>
    </g>
    <!-- persona 5 -->
    <g transform="translate(224 342)">
      <circle cx="0" cy="-26" r="8" fill="#8D5524"/>
      <path d="M-7 -22 Q-8 -32 0 -32 Q8 -32 7 -22 Q0 -25 -7 -22 Z" fill="#111"/>
      <line x1="0" y1="-18" x2="0" y2="-4" stroke="#F4A261" stroke-width="7"/>
      <line x1="-4" y1="-15" x2="-10" y2="-9" stroke="#F4A261" stroke-width="4"/>
      <line x1="4" y1="-15" x2="10" y2="-9" stroke="#F4A261" stroke-width="4"/>
      <line x1="0" y1="-4" x2="-4" y2="6" stroke="#2F4858" stroke-width="4"/>
      <line x1="0" y1="-4" x2="5" y2="6" stroke="#2F4858" stroke-width="4"/>
    </g>
    <!-- persona 6 -->
    <g transform="translate(248 340)">
      <circle cx="0" cy="-26" r="8" fill="#F1C27D"/>
      <line x1="0" y1="-18" x2="0" y2="-4" stroke="#457B9D" stroke-width="7"/>
      <line x1="-4" y1="-15" x2="-10" y2="-9" stroke="#457B9D" stroke-width="4"/>
      <line x1="4" y1="-15" x2="10" y2="-9" stroke="#457B9D" stroke-width="4"/>
      <line x1="0" y1="-4" x2="-4" y2="6" stroke="#1D3557" stroke-width="4"/>
      <line x1="0" y1="-4" x2="5" y2="6" stroke="#1D3557" stroke-width="4"/>
    </g>
    <!-- persona 7 -->
    <g transform="translate(272 342)">
      <circle cx="0" cy="-26" r="8" fill="#C68642"/>
      <line x1="0" y1="-18" x2="0" y2="-4" stroke="#E76F51" stroke-width="7"/>
      <line x1="-4" y1="-15" x2="-10" y2="-10" stroke="#E76F51" stroke-width="4"/>
      <line x1="4" y1="-15" x2="10" y2="-10" stroke="#E76F51" stroke-width="4"/>
      <line x1="0" y1="-4" x2="-4" y2="6" stroke="#3A3335" stroke-width="4"/>
      <line x1="0" y1="-4" x2="5" y2="6" stroke="#3A3335" stroke-width="4"/>
    </g>
    <!-- manos unidas -->
    <g fill="#333" stroke="none">
      <circle cx="141" cy="-348" r="0"/>
    </g>
    <g stroke="#333" stroke-width="2.6" stroke-linecap="round">
      <line x1="138" y1="331" x2="146" y2="331"/>
      <line x1="162" y1="331" x2="168" y2="333"/>
      <line x1="186" y1="333" x2="194" y2="331"/>
      <line x1="210" y1="331" x2="218" y2="333"/>
      <line x1="234" y1="333" x2="242" y2="331"/>
      <line x1="258" y1="331" x2="266" y2="332"/>
    </g>
  </g>

  <!-- texto -->
  <text x="200" y="38" text-anchor="middle" font-family="Georgia, serif" font-size="17" font-style="italic" fill="#2B4A6B">Un mundo en paz</text>
</svg>
```