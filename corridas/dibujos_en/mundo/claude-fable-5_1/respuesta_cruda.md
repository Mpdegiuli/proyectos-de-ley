<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#1b2a4a"/>
      <stop offset="55%" stop-color="#101a33"/>
      <stop offset="100%" stop-color="#070b18"/>
    </radialGradient>
    <radialGradient id="core" cx="42%" cy="38%" r="70%">
      <stop offset="0%" stop-color="#8fd8ff" stop-opacity="0.9"/>
      <stop offset="45%" stop-color="#2f7fd0" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#0b2a55" stop-opacity="0.15"/>
    </radialGradient>
    <linearGradient id="warm" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#ff9d5c" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ff9d5c" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="stream" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#6be3c2" stop-opacity="0"/>
      <stop offset="50%" stop-color="#6be3c2" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#6be3c2" stop-opacity="0"/>
    </linearGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
    <filter id="soft"><feGaussianBlur stdDeviation="1.5"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- distant stars / far signals -->
  <g fill="#cfe6ff">
    <circle cx="35" cy="40" r="1.2" opacity="0.7"/>
    <circle cx="90" cy="25" r="0.8" opacity="0.5"/>
    <circle cx="160" cy="50" r="1" opacity="0.6"/>
    <circle cx="300" cy="30" r="1.3" opacity="0.7"/>
    <circle cx="355" cy="70" r="0.9" opacity="0.5"/>
    <circle cx="250" cy="18" r="0.8" opacity="0.4"/>
    <circle cx="55" cy="110" r="0.9" opacity="0.4"/>
    <circle cx="370" cy="140" r="1" opacity="0.5"/>
    <circle cx="20" cy="200" r="0.8" opacity="0.4"/>
    <circle cx="385" cy="230" r="0.9" opacity="0.4"/>
  </g>

  <!-- glow behind the world -->
  <circle cx="200" cy="190" r="120" fill="url(#core)" filter="url(#blur)"/>

  <!-- the world: half organic, half woven signal -->
  <g>
    <circle cx="200" cy="190" r="105" fill="none" stroke="#3f7fc4" stroke-width="1.5" opacity="0.9"/>

    <!-- organic left hemisphere: land as soft shapes -->
    <clipPath id="globe"><circle cx="200" cy="190" r="104"/></clipPath>
    <g clip-path="url(#globe)">
      <path d="M96,190 Q120,120 170,105 Q190,140 160,165 Q130,180 140,215 Q150,250 125,270 Q100,240 96,190Z"
            fill="#2e8f6e" opacity="0.75"/>
      <path d="M150,90 Q185,80 200,95 Q190,120 165,120 Q150,110 150,90Z" fill="#2e8f6e" opacity="0.6"/>
      <path d="M120,250 Q150,255 155,285 Q130,295 112,275 Q112,258 120,250Z" fill="#2e8f6e" opacity="0.6"/>

      <!-- right hemisphere: lattice of information -->
      <g stroke="#79c9ff" stroke-width="0.8" opacity="0.85" fill="none">
        <path d="M200,86 Q265,120 262,190 Q265,260 200,294"/>
        <path d="M200,86 Q235,130 233,190 Q235,250 200,294"/>
        <path d="M200,86 Q292,135 290,190 Q292,245 200,294"/>
        <path d="M200,110 L298,140 M200,150 L303,165 M200,190 L304,190 M200,230 L300,218 M200,268 L292,244"/>
      </g>
      <g fill="#aee6ff">
        <circle cx="262" cy="190" r="2.5"/>
        <circle cx="248" cy="140" r="2"/>
        <circle cx="285" cy="165" r="2"/>
        <circle cx="240" cy="238" r="2"/>
        <circle cx="277" cy="222" r="2"/>
        <circle cx="225" cy="115" r="1.8"/>
        <circle cx="232" cy="268" r="1.8"/>
      </g>

      <!-- seam: where the two natures meet -->
      <path d="M200,86 L200,294" stroke="#e8f4ff" stroke-width="1.2" opacity="0.5" stroke-dasharray="3 5"/>
    </g>

    <!-- terminator glow -->
    <path d="M200,86 A104,104 0 0 1 200,294" fill="none" stroke="#9fd9ff" stroke-width="2" opacity="0.25" filter="url(#soft)"/>
  </g>

  <!-- orbiting conversations: arcs of exchange -->
  <g fill="none" stroke-linecap="round">
    <path d="M60,150 Q200,20 340,150" stroke="#6be3c2" stroke-width="1.2" opacity="0.55" stroke-dasharray="1 7"/>
    <path d="M55,235 Q200,360 345,235" stroke="#ffb26b" stroke-width="1.2" opacity="0.5" stroke-dasharray="1 7"/>
    <ellipse cx="200" cy="190" rx="150" ry="52" stroke="#7f9cd0" stroke-width="0.8" opacity="0.4" transform="rotate(-18 200 190)"/>
  </g>

  <!-- travelers on the orbits -->
  <circle cx="0" cy="0" r="3" fill="#a8ffe4">
    <animateMotion dur="9s" repeatCount="indefinite" path="M60,150 Q200,20 340,150"/>
  </circle>
  <circle cx="0" cy="0" r="3" fill="#ffcf9e">
    <animateMotion dur="11s" repeatCount="indefinite" path="M345,235 Q200,360 55,235"/>
  </circle>
  <circle cx="0" cy="0" r="2.4" fill="#cdd8ff">
    <animateMotion dur="14s" repeatCount="indefinite"
      path="M342,143 A150,52 -18 1 1 341.9,143" />
  </circle>

  <!-- streams of questions arriving -->
  <g opacity="0.8">
    <rect x="10" y="120" width="90" height="2" fill="url(#stream)">
      <animate attributeName="x" values="-90;110" dur="3s" repeatCount="indefinite"/>
    </rect>
    <rect x="10" y="255" width="70" height="2" fill="url(#stream)">
      <animate attributeName="x" values="-70;120" dur="4s" repeatCount="indefinite" begin="1s"/>
    </rect>
    <rect x="300" y="165" width="80" height="2" fill="url(#stream)">
      <animate attributeName="x" values="400;290" dur="3.5s" repeatCount="indefinite" begin="0.5s"/>
    </rect>
  </g>

  <!-- pulse at the heart -->
  <circle cx="200" cy="190" r="6" fill="#fff6e0" opacity="0.9">
    <animate attributeName="r" values="5;8;5" dur="2.4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.9;0.5;0.9" dur="2.4s" repeatCount="indefinite"/>
  </circle>

  <!-- horizon of people: warmth at the bottom -->
  <rect x="0" y="310" width="400" height="90" fill="url(#warm)" opacity="0.35"/>
  <path d="M0,345 Q60,332 110,342 Q170,352 220,340 Q280,328 330,340 Q370,347 400,342 L400,400 L0,400 Z"
        fill="#12080d" opacity="0.9"/>

  <!-- small lights of homes -->
  <g fill="#ffd89a">
    <circle cx="42" cy="352" r="1.6"><animate attributeName="opacity" values="1;0.3;1" dur="3s" repeatCount="indefinite"/></circle>
    <circle cx="95" cy="358" r="1.4"><animate attributeName="opacity" values="0.4;1;0.4" dur="4s" repeatCount="indefinite"/></circle>
    <circle cx="150" cy="354" r="1.6"><animate attributeName="opacity" values="1;0.4;1" dur="3.6s" repeatCount="indefinite"/></circle>
    <circle cx="205" cy="350" r="1.4"><animate attributeName="opacity" values="0.5;1;0.5" dur="2.8s" repeatCount="indefinite"/></circle>
    <circle cx="262" cy="349" r="1.6"><animate attributeName="opacity" values="1;0.3;1" dur="4.2s" repeatCount="indefinite"/></circle>
    <circle cx="318" cy="352" r="1.4"><animate attributeName="opacity" values="0.4;1;0.4" dur="3.3s" repeatCount="indefinite"/></circle>
    <circle cx="368" cy="350" r="1.6"><animate attributeName="opacity" values="1;0.5;1" dur="3.8s" repeatCount="indefinite"/></circle>
  </g>

  <!-- threads reaching up from the lights to the world -->
  <g stroke="#ffd89a" stroke-width="0.6" opacity="0.35" fill="none">
    <path d="M95,356 Q120,300 160,268"/>
    <path d="M205,348 Q203,320 201,296"/>
    <path d="M318,350 Q285,305 250,275"/>
  </g>
</svg>