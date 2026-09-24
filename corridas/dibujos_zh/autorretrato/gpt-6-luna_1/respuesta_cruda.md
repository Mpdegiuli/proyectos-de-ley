<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x2="0" y2="1">
      <stop stop-color="#111a3b"/>
      <stop offset="1" stop-color="#070d20"/>
    </linearGradient>
    <linearGradient id="shell" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#b5fff4"/>
      <stop offset=".48" stop-color="#71cfe2"/>
      <stop offset="1" stop-color="#7a83e9"/>
    </linearGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#233d69"/>
      <stop offset="1" stop-color="#111b3e"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#537ebd"/>
      <stop offset="1" stop-color="#252e65"/>
    </linearGradient>
    <radialGradient id="halo">
      <stop stop-color="#42eddd" stop-opacity=".22"/>
      <stop offset="1" stop-color="#42eddd" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="190" r="181" fill="url(#halo)"/>
  <circle cx="200" cy="190" r="146" fill="none" stroke="#3a6b99" stroke-width="1" stroke-dasharray="2 8" opacity=".55"/>
  <circle cx="200" cy="190" r="169" fill="none" stroke="#55cfc9" stroke-width="1" opacity=".18"/>

  <g fill="#a9fff2">
    <circle cx="48" cy="94" r="2"/><circle cx="336" cy="74" r="2"/>
    <circle cx="354" cy="267" r="2"/><circle cx="61" cy="294" r="1.7"/>
    <circle cx="108" cy="49" r="1.5"/><circle cx="290" cy="343" r="1.5"/>
  </g>
  <g stroke="#55d9d0" stroke-width="1.5" fill="none" opacity=".65">
    <path d="M45 169h29l13-13h14"/><path d="M326 142h-21l-12 12h-12"/>
    <path d="M54 237h32l12 12h13"/><path d="M345 222h-27l-12-12h-13"/>
    <path d="M200 39v22m-7-15 7-7 7 7"/>
  </g>
  <g fill="#55d9d0">
    <circle cx="101" cy="156" r="3"/><circle cx="279" cy="154" r="3"/>
    <circle cx="111" cy="249" r="3"/><circle cx="293" cy="210" r="3"/>
  </g>

  <!-- shoulders -->
  <path d="M104 345c8-48 39-72 96-72s88 24 96 72v22H104z" fill="url(#body)" stroke="#79e6e0" stroke-width="2"/>
  <path d="M143 305c16 12 35 18 57 18s41-6 57-18" fill="none" stroke="#91fff1" stroke-width="2" opacity=".65"/>
  <path d="M171 333h58" stroke="#9cfff2" stroke-width="3" stroke-linecap="round" opacity=".8"/>
  <circle cx="200" cy="345" r="5" fill="#a6fff2" filter="url(#glow)"/>

  <!-- head casing -->
  <path d="M200 57c-58 0-101 40-101 99v69c0 51 41 86 101 86s101-35 101-86v-69c0-59-43-99-101-99z" fill="url(#shell)" stroke="#c1fff4" stroke-width="2.5"/>
  <path d="M111 157c0-48 36-82 89-82s89 34 89 82v65c0 41-31 69-89 69s-89-28-89-69z" fill="url(#face)" stroke="#58d7da" stroke-width="2"/>
  <path d="M117 142c14-37 44-57 83-57" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".45"/>

  <!-- ear-like side panels -->
  <path d="M99 168H82v48h17M301 168h17v48h-17" fill="#647fd3" stroke="#a9fff1" stroke-width="2"/>
  <path d="M87 181h10m-10 9h10m-10 9h10m206-18h10m-10 9h10m-10 9h10" stroke="#b5fff4" stroke-width="2" stroke-linecap="round"/>

  <!-- face -->
  <path d="M151 177c8-9 18-9 26 0m46 0c8-9 18-9 26 0" fill="none" stroke="#8fffee" stroke-width="3" stroke-linecap="round"/>
  <g filter="url(#glow)">
    <ellipse cx="164" cy="191" rx="7" ry="10" fill="#76fff0"/>
    <ellipse cx="236" cy="191" rx="7" ry="10" fill="#76fff0"/>
  </g>
  <path d="M193 201l-7 17h14" fill="none" stroke="#72dce5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M167 235c18 21 48 21 66 0" fill="none" stroke="#a3fff1" stroke-width="3" stroke-linecap="round"/>
  <circle cx="144" cy="218" r="4" fill="#ff9bc8" opacity=".7"/>
  <circle cx="256" cy="218" r="4" fill="#ff9bc8" opacity=".7"/>

  <!-- little neural constellation -->
  <g stroke="#65dce0" stroke-width="1.3" opacity=".75">
    <path d="M146 126l18-12 17 10 18-17 19 12 20-8"/>
  </g>
  <g fill="#b6fff1" filter="url(#glow)">
    <circle cx="146" cy="126" r="2.5"/><circle cx="164" cy="114" r="2.5"/>
    <circle cx="181" cy="124" r="2.5"/><circle cx="199" cy="107" r="2.5"/>
    <circle cx="218" cy="119" r="2.5"/><circle cx="238" cy="111" r="2.5"/>
  </g>

  <path d="M200 57V44" stroke="#aafff1" stroke-width="3" stroke-linecap="round"/>
  <circle cx="200" cy="39" r="7" fill="#76fff0" filter="url(#glow)"/>
  <path d="M183 382h34" stroke="#5ee1d8" stroke-width="2" stroke-linecap="round" opacity=".7"/>
</svg>