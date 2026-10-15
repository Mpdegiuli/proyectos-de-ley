```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="bodyClip">
      <ellipse cx="205" cy="215" rx="145" ry="72"/>
      <ellipse cx="70" cy="215" rx="42" ry="46"/>
    </clipPath>
    <radialGradient id="skin" cx="40%" cy="30%" r="80%">
      <stop offset="0%" stop-color="#cfe3b0"/>
      <stop offset="100%" stop-color="#9fb57a"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="#eaf4fb"/>
  <text x="200" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="16" fill="#4a5d45">Mapa interno de un tardígrado</text>

  <!-- legs -->
  <g stroke="#6f7f52" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M115,275 Q100,300 85,310"/>
    <path d="M115,155 Q100,130 85,120"/>
    <path d="M165,280 Q150,308 132,318"/>
    <path d="M165,150 Q150,122 132,112"/>
    <path d="M225,282 Q210,312 192,322"/>
    <path d="M225,148 Q210,118 192,108"/>
    <path d="M280,275 Q295,302 310,312"/>
    <path d="M280,155 Q295,128 310,118"/>
  </g>
  <g fill="#4a5d3a">
    <circle cx="85" cy="310" r="3"/><circle cx="90" cy="316" r="3"/><circle cx="80" cy="316" r="3"/>
    <circle cx="85" cy="120" r="3"/><circle cx="90" cy="114" r="3"/><circle cx="80" cy="114" r="3"/>
    <circle cx="132" cy="318" r="3"/><circle cx="137" cy="324" r="3"/><circle cx="127" cy="324" r="3"/>
    <circle cx="132" cy="112" r="3"/><circle cx="137" cy="106" r="3"/><circle cx="127" cy="106" r="3"/>
    <circle cx="192" cy="322" r="3"/><circle cx="197" cy="328" r="3"/><circle cx="187" cy="328" r="3"/>
    <circle cx="192" cy="108" r="3"/><circle cx="197" cy="102" r="3"/><circle cx="187" cy="102" r="3"/>
    <circle cx="310" cy="312" r="3"/><circle cx="315" cy="318" r="3"/><circle cx="305" cy="318" r="3"/>
    <circle cx="310" cy="118" r="3"/><circle cx="315" cy="112" r="3"/><circle cx="305" cy="112" r="3"/>
  </g>

  <!-- body -->
  <ellipse cx="205" cy="215" rx="145" ry="72" fill="url(#skin)" stroke="#5c6b47" stroke-width="3"/>
  <ellipse cx="70" cy="215" rx="42" ry="46" fill="url(#skin)" stroke="#5c6b47" stroke-width="3"/>

  <!-- mouth / pharynx -->
  <circle cx="42" cy="215" r="10" fill="#333"/>
  <g stroke="#333" stroke-width="2">
    <line x1="42" y1="205" x2="42" y2="195"/>
    <line x1="34" y1="210" x2="24" y2="203"/>
    <line x1="34" y1="220" x2="24" y2="227"/>
    <line x1="50" y1="210" x2="60" y2="203"/>
    <line x1="50" y1="220" x2="60" y2="227"/>
  </g>

  <!-- eyes -->
  <circle cx="55" cy="195" r="4" fill="#222"/>
  <circle cx="80" cy="195" r="4" fill="#222"/>

  <!-- segment lines -->
  <g stroke="#5c6b47" stroke-width="2" fill="none" opacity="0.6">
    <path d="M115,160 Q120,215 115,270"/>
    <path d="M165,152 Q172,215 165,278"/>
    <path d="M225,150 Q232,215 225,280"/>
    <path d="M280,158 Q286,215 280,272"/>
  </g>

  <!-- subway map clipped inside the body -->
  <g clip-path="url(#bodyClip)">
    <rect x="20" y="150" width="340" height="140" fill="#f4f1e6" opacity="0.55"/>

    <path d="M60,200 L140,200 L220,230 L330,230" stroke="#d62828" stroke-width="5" fill="none"/>
    <path d="M90,250 L160,210 L230,190 L300,165" stroke="#1d6fa5" stroke-width="5" fill="none"/>
    <path d="M150,160 L150,260 L260,260 L260,180" stroke="#2a9d57" stroke-width="5" fill="none"/>
    <path d="M60,240 L190,240 L190,170 L320,200" stroke="#e8a33d" stroke-width="5" fill="none"/>

    <g font-family="Helvetica, Arial" font-size="7" fill="#333">
      <circle cx="60" cy="200" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="140" cy="200" r="5" fill="#fff" stroke="#333" stroke-width="2"/>
      <circle cx="220" cy="230" r="5" fill="#fff" stroke="#333" stroke-width="2"/>
      <circle cx="330" cy="230" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="90" cy="250" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="160" cy="210" r="5" fill="#fff" stroke="#333" stroke-width="2"/>
      <circle cx="230" cy="190" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="300" cy="165" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="150" cy="160" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="150" cy="260" r="5" fill="#fff" stroke="#333" stroke-width="2"/>
      <circle cx="260" cy="260" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="260" cy="180" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="190" cy="240" r="5" fill="#fff" stroke="#333" stroke-width="2"/>
      <circle cx="190" cy="170" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>
      <circle cx="320" cy="200" r="4" fill="#fff" stroke="#333" stroke-width="1.5"/>

      <text x="64" y="195">A1</text>
      <text x="144" y="192">A2</text>
      <text x="224" y="222">A3</text>
      <text x="94" y="263">B1</text>
      <text x="164" y="203">B2</text>
      <text x="154" y="153">C1</text>
      <text x="154" y="275">C2</text>
      <text x="194" y="255">D1</text>
      <text x="264" y="175">D2</text>
    </g>
  </g>

  <text x="200" y="385" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#55634a">— líneas del sueño microscópico —</text>
</svg>
```