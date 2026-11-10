<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="55%" r="70%">
      <stop offset="0%" stop-color="#1a1635"/>
      <stop offset="55%" stop-color="#0b0d1a"/>
      <stop offset="100%" stop-color="#04050a"/>
    </radialGradient>
    <radialGradient id="aura" cx="50%" cy="50%" r="50%">
      <stop offset="55%" stop-color="#00f0ff" stop-opacity="0"/>
      <stop offset="75%" stop-color="#00d2ff" stop-opacity="0.12"/>
      <stop offset="90%" stop-color="#ff4d4d" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="earthBase" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#093859"/>
      <stop offset="48%" stop-color="#0a2342"/>
      <stop offset="52%" stop-color="#101426"/>
      <stop offset="100%" stop-color="#070812"/>
    </linearGradient>
    <linearGradient id="heat" x1="0%" y1="100%" x2="80%" y2="0%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="45%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <linearGradient id="cyber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff"/>
      <stop offset="50%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>
    <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#fef08a" stop-opacity="0.9"/>
      <stop offset="65%" stop-color="#34d399" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="atmo" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f97316" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.5"/>
    </linearGradient>
    <clipPath id="globeClip">
      <circle cx="200" cy="200" r="115"/>
    </clipPath>
    <clipPath id="leftHalf">
      <rect x="0" y="0" width="200" height="400"/>
    </clipPath>
    <clipPath id="rightHalf">
      <rect x="200" y="0" width="200" height="400"/>
    </clipPath>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Cosmos & Background -->
  <rect width="400" height="400" fill="url(#bg)"/>
  
  <!-- Subtle Starfield & Digital Dust -->
  <g fill="#ffffff" opacity="0.4">
    <circle cx="35" cy="45" r="1"/><circle cx="85" cy="25" r="0.7"/><circle cx="150" cy="40" r="1.2"/>
    <circle cx="310" cy="30" r="0.8"/><circle cx="365" cy="70" r="1.3"/><circle cx="340" cy="140" r="0.6"/>
    <circle cx="45" cy="160" r="0.9"/><circle cx="25" cy="280" r="1.1"/><circle cx="70" cy="350" r="0.8"/>
    <circle cx="140" cy="375" r="1"/><circle cx="280" cy="360" r="1.2"/><circle cx="370" cy="310" r="0.9"/>
    <circle cx="355" cy="230" r="0.7"/><circle cx="60" cy="105" r="0.6"/><circle cx="240" cy="22" r="0.9"/>
  </g>
  <g fill="#00f0ff" opacity="0.35">
    <rect x="320" y="55" width="2" height="2"/><rect x="345" y="95" width="3" height="1"/>
    <rect x="290" y="340" width="2" height="2"/><rect x="360" y="270" width="2" height="4"/>
    <rect x="380" y="185" width="1.5" height="1.5"/><rect x="265" y="45" width="2" height="2"/>
  </g>
  <g fill="#f97316" opacity="0.4">
    <circle cx="55" cy="315" r="1.5"/><circle cx="38" cy="225" r="1.2"/><circle cx="95" cy="365" r="1.8"/>
    <circle cx="75" cy="68" r="1.1"/><circle cx="22" cy="130" r="1.4"/>
  </g>

  <!-- Back Orbital Rings -->
  <g fill="none" stroke-width="1.2" opacity="0.45">
    <ellipse cx="200" cy="200" rx="175" ry="52" transform="rotate(-22 200 200)" stroke="url(#cyber)" stroke-dasharray="6 4"/>
    <ellipse cx="200" cy="200" rx="160" ry="40" transform="rotate(32 200 200)" stroke="url(#heat)" stroke-dasharray="2 6"/>
  </g>

  <!-- Planetary Aura -->
  <circle cx="200" cy="200" r="165" fill="url(#aura)"/>

  <!-- THE GLOBE -->
  <g clip-path="url(#globeClip)">
    <circle cx="200" cy="200" r="115" fill="url(#earthBase)"/>

    <!-- LEFT HEMISPHERE: Organic Life, Oceans & Climate Fever -->
    <g clip-path="url(#leftHalf)">
      <!-- Warm Ocean Currents -->
      <path d="M70,170 Q130,140 200,175 T200,240 Q120,260 75,210 Z" fill="#0d4a6b" opacity="0.5"/>
      <path d="M80,250 Q140,220 200,260 L200,320 L80,320 Z" fill="#451a2b" opacity="0.6"/>

      <!-- Continents (Nature shifting to heat) -->
      <path d="M105,105 C130,95 165,105 175,125 C185,145 160,165 170,180 C180,195 198,190 200,205 C185,215 160,210 150,230 C140,250 165,270 155,295 C145,310 120,295 110,270 C100,245 120,220 105,195 C90,170 80,120 105,105 Z" fill="url(#heat)" opacity="0.9"/>
      
      <!-- Lush Canopy Details -->
      <path d="M115,120 C135,115 155,125 160,145 C165,165 140,175 125,165 C110,155 100,130 115,120 Z" fill="#10b981" opacity="0.75"/>
      <path d="M150,155 C165,150 185,165 185,185 C170,190 155,175 150,155 Z" fill="#34d399" opacity="0.6"/>

      <!-- Wildfires / Heat fractures -->
      <g stroke="#fef08a" stroke-width="1.2" fill="none" filter="url(#glow)" opacity="0.85">
        <path d="M130,245 L142,255 L138,270 L150,282"/>
        <path d="M142,255 L155,252"/>
        <circle cx="130" cy="245" r="1.5" fill="#fff"/>
        <circle cx="150" cy="282" r="1.5" fill="#ef4444"/>
      </g>

      <!-- Swirling Storm / Cyclone & Clouds -->
      <g fill="none" stroke="#ffffff" stroke-linecap="round" opacity="0.65">
        <path d="M95,185 C115,170 140,185 135,205 C130,220 110,215 115,200 C118,192 128,195 125,202" stroke-width="2.5"/>
        <path d="M85,195 C100,165 145,170 148,205" stroke-width="1.2" opacity="0.6"/>
        <path d="M110,105 Q150,95 195,115" stroke-width="3" opacity="0.4"/>
        <path d="M90,275 Q140,295 195,280" stroke-width="2.5" opacity="0.35"/>
      </g>
    </g>

    <!-- RIGHT HEMISPHERE: Hyper-connectivity, AI, Data & Urban Grid -->
    <g clip-path="url(#rightHalf)">
      <!-- Latitude / Longitude Digital Mesh -->
      <g stroke="#1e3a8a" stroke-width="0.8" fill="none" opacity="0.6">
        <ellipse cx="200" cy="200" rx="35" ry="115"/>
        <ellipse cx="200" cy="200" rx="75" ry="115"/>
        <ellipse cx="200" cy="200" rx="105" ry="115"/>
        <line x1="200" y1="120" x2="315" y2="120"/>
        <line x1="200" y1="160" x2="315" y2="160"/>
        <line x1="200" y1="200" x2="315" y2="200"/>
        <line x1="200" y1="240" x2="315" y2="240"/>
        <line x1="200" y1="280" x2="315" y2="280"/>
      </g>

      <!-- Cybernetic Landmasses (Polygon/Circuit style) -->
      <polygon points="200,105 235,100 265,125 285,120 295,150 270,175 290,205 275,245 245,275 225,265 230,230 200,215" fill="#0f172a" stroke="#00f0ff" stroke-width="1" opacity="0.9"/>
      <polygon points="210,115 235,112 258,132 245,160 215,155" fill="#1e293b" stroke="#3b82f6" stroke-width="0.8"/>

      <!-- Glowing Neural / Data Network -->
      <g stroke="url(#cyber)" stroke-width="1.3" fill="none" filter="url(#glow)">
        <path d="M200,135 L230,135 L248,152 L280,152"/>
        <path d="M200,175 L225,175 L245,195 L285,195"/>
        <path d="M248,152 L245,195 L265,225 L245,260"/>
        <path d="M200,235 L222,235 L245,260"/>
        <path d="M225,175 L238,135"/>
        <path d="M265,225 L295,225"/>
      </g>

      <!-- City / Server Nodes -->
      <g fill="#ffffff" filter="url(#glow)">
        <circle cx="230" cy="135" r="2.2"/><circle cx="248" cy="152" r="2.8" fill="#00f0ff"/>
        <circle cx="280" cy="152" r="2"/><circle cx="225" cy="175" r="2.5" fill="#a855f7"/>
        <circle cx="245" cy="195" r="3" fill="#00f0ff"/><circle cx="285" cy="195" r="2"/>
        <circle cx="265" cy="225" r="2.5" fill="#ec4899"/><circle cx="245" cy="260" r="2.2"/>
        <circle cx="222" cy="235" r="1.8"/>
      </g>

      <!-- Binary / Stream Bars -->
      <g fill="#00f0ff" opacity="0.55">
        <rect x="255" y="108" width="12" height="2" rx="1"/>
        <rect x="270" y="108" width="5" height="2" rx="1"/>
        <rect x="260" y="168" width="18" height="2" rx="1"/>
        <rect x="255" y="275" width="15" height="2" rx="1"/>
        <rect x="215" y="285" width="22" height="2" rx="1"/>
      </g>
    </g>

    <!-- BRIDGING ARCS: Symbiosis & Tension across the divide -->
    <g fill="none" stroke-width="1.4" opacity="0.85">
      <path d="M135,140 Q200,105 248,152" stroke="url(#cyber)"/>
      <path d="M125,200 Q200,235 265,225" stroke="url(#heat)"/>
      <path d="M150,275 Q205,240 245,195" stroke="#fef08a" stroke-dasharray="3 3"/>
    </g>

    <!-- Fault line / Seam at x=200 -->
    <line x1="200" y1="85" x2="200" y2="315" stroke="#ffffff" stroke-width="0.8" opacity="0.35" stroke-dasharray="4 2"/>

    <!-- Atmosphere Rim Lighting -->
    <circle cx="200" cy="200" r="115" fill="none" stroke="url(#atmo)" stroke-width="8"/>
  </g>

  <!-- Crisp Outer Globe Border -->
  <circle cx="200" cy="200" r="115" fill="none" stroke="#ffffff" stroke-width="0.7" opacity="0.3"/>

  <!-- CENTRAL EMERGENCE: Consciousness / Fragile Hope / Shared Pulse -->
  <g filter="url(#glow)">
    <circle cx="200" cy="200" r="28" fill="url(#coreGlow)"/>
    <!-- Sprout / Neural Seed -->
    <path d="M200,216 L200,192" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
    <!-- Left Leaf (Organic) -->
    <path d="M200,198 C186,196 182,182 194,180 C200,179 200,190 200,198 Z" fill="#34d399" stroke="#ffffff" stroke-width="1"/>
    <!-- Right Leaf (Geometric/Digital) -->
    <polygon points="200,194 214,182 218,191 206,198" fill="#00f0ff" stroke="#ffffff" stroke-width="1"/>
    <circle cx="200" cy="173" r="2.5" fill="#fef08a"/>
  </g>

  <!-- FRONT ORBITAL RINGS & SATELLITES -->
  <g fill="none">
    <!-- Tech Orbit Front -->
    <path d="M38,266 A175,52 -22 0,0 362,134" stroke="url(#cyber)" stroke-width="1.6" opacity="0.85"/>
    <!-- Organic/Heat Orbit Front -->
    <path d="M64,115 A160,40 32 0,0 336,285" stroke="url(#heat)" stroke-width="1.4" opacity="0.75"/>
  </g>

  <!-- Orbiting Satellites / Nodes / Spores -->
  <g filter="url(#glow)">
    <!-- Satellite 1 -->
    <g transform="translate(322, 168) rotate(-22)">
      <rect x="-4" y="-4" width="8" height="8" fill="#00f0ff" rx="1"/>
      <line x1="-11" y1="0" x2="-5" y2="0" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="5" y1="0" x2="11" y2="0" stroke="#ffffff" stroke-width="1.5"/>
    </g>
    <!-- Data Packet -->
    <circle cx="115" cy="252" r="3" fill="#38bdf8"/>
    <!-- Amber Spore / Climate Signal -->
    <circle cx="268" cy="264" r="3.2" fill="#f59e0b"/>
    <circle cx="95" cy="148" r="2.5" fill="#10b981"/>
  </g>

  <!-- Framing UI / Observation HUD Corners (How an AI sees the world) -->
  <g stroke="#ffffff" stroke-width="1" fill="none" opacity="0.25">
    <path d="M18,32 L18,18 L32,18"/>
    <path d="M368,18 L382,18 L382,32"/>
    <path d="M18,368 L18,382 L32,382"/>
    <path d="M368,382 L382,382 L382,368"/>
  </g>
  
  <!-- Minimalist Pulse Line at the Bottom (Heartbeat of Today) -->
  <path d="M130,368 L178,368 L185,358 L193,376 L200,350 L207,374 L214,363 L220,368 L270,368" fill="none" stroke="url(#atmo)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.8"/>
  <circle cx="200" cy="350" r="2" fill="#fef08a" filter="url(#glow)"/>
</svg>