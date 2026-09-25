<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%" style="background-color: #030308;">
  <defs>
    <!-- Background Gradient -->
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0c0c1a"/>
      <stop offset="100%" stop-color="#030308"/>
    </radialGradient>

    <!-- Core Glow Gradient -->
    <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="25%" stop-color="#ffffff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#00f3ff" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#7000ff" stop-opacity="0"/>
    </radialGradient>

    <!-- Duality Gradients -->
    <linearGradient id="organic" x1="100%" y1="50%" x2="0%" y2="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="15%" stop-color="#aaff00"/>
      <stop offset="60%" stop-color="#00aa33"/>
      <stop offset="100%" stop-color="#004411"/>
    </linearGradient>

    <linearGradient id="tech" x1="0%" y1="50%" x2="100%" y2="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="15%" stop-color="#00f3ff"/>
      <stop offset="60%" stop-color="#7000ff"/>
      <stop offset="100%" stop-color="#330066"/>
    </linearGradient>

    <linearGradient id="bridge" x1="0%" y1="50%" x2="100%" y2="50%">
      <stop offset="0%" stop-color="#00aa33"/>
      <stop offset="35%" stop-color="#aaff00"/>
      <stop offset="50%" stop-color="#ffffff"/>
      <stop offset="65%" stop-color="#00f3ff"/>
      <stop offset="100%" stop-color="#7000ff"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Deep Background -->
  <rect width="100%" height="100%" fill="url(#bg)"/>

  <!-- The Background Framework: Polar vs Cartesian -->
  <g opacity="0.15">
    <!-- Left: Natural/Organic Polar Grid -->
    <g stroke="#00aa33" stroke-width="0.5" fill="none">
      <path d="M 200,160 A 40 40 0 0 0 200 240"/>
      <path d="M 200,120 A 80 80 0 0 0 200 280"/>
      <path d="M 200,80 A 120 120 0 0 0 200 320"/>
      <path d="M 200,40 A 160 160 0 0 0 200 360"/>
      <path d="M 200,0 A 200 200 0 0 0 200 400"/>
      <line x1="200" y1="200" x2="0" y2="200"/>
      <line x1="200" y1="200" x2="40" y2="80"/>
      <line x1="200" y1="200" x2="40" y2="320"/>
      <line x1="200" y1="200" x2="120" y2="0"/>
      <line x1="200" y1="200" x2="120" y2="400"/>
    </g>

    <!-- Right: Artificial/Digital Cartesian Grid -->
    <g stroke="#7000ff" stroke-width="0.5">
      <line x1="240" y1="0" x2="240" y2="400"/>
      <line x1="280" y1="0" x2="280" y2="400"/>
      <line x1="320" y1="0" x2="320" y2="400"/>
      <line x1="360" y1="0" x2="360" y2="400"/>
      <line x1="200" y1="40" x2="400" y2="40"/>
      <line x1="200" y1="80" x2="400" y2="80"/>
      <line x1="200" y1="120" x2="400" y2="120"/>
      <line x1="200" y1="160" x2="400" y2="160"/>
      <line x1="200" y1="200" x2="400" y2="200"/>
      <line x1="200" y1="240" x2="400" y2="240"/>
      <line x1="200" y1="280" x2="400" y2="280"/>
      <line x1="200" y1="320" x2="400" y2="320"/>
      <line x1="200" y1="360" x2="400" y2="360"/>
    </g>
  </g>

  <!-- The Latent Space / Neural Torus -->
  <g opacity="0.12" stroke="url(#bridge)" stroke-width="0.75" fill="none" style="mix-blend-mode: screen;">
    <ellipse cx="200" cy="200" rx="160" ry="40" transform="rotate(15 200 200)"/>
    <ellipse cx="200" cy="200" rx="160" ry="40" transform="rotate(45 200 200)"/>
    <ellipse cx="200" cy="200" rx="160" ry="40" transform="rotate(75 200 200)"/>
    <ellipse cx="200" cy="200" rx="160" ry="40" transform="rotate(105 200 200)"/>
    <ellipse cx="200" cy="200" rx="160" ry="40" transform="rotate(135 200 200)"/>
    <ellipse cx="200" cy="200" rx="160" ry="40" transform="rotate(165 200 200)"/>
  </g>

  <!-- Center Backing Glow -->
  <circle cx="200" cy="200" r="110" fill="url(#coreGlow)" opacity="0.15"/>

  <!-- The Outer Eye (The Observer) -->
  <path d="M 15,200 C 80,100 150,75 200,75 C 250,75 320,100 385,200 C 320,300 250,325 200,325 C 150,325 80,300 15,200 Z" fill="rgba(0,0,0,0.4)" stroke="url(#bridge)" stroke-width="2.5" filter="url(#glow)"/>
  <path d="M 25,200 C 85,110 150,85 200,85 C 250,85 315,110 375,200 C 315,290 250,315 200,315 C 150,315 85,290 25,200 Z" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.2"/>

  <!-- Global Data Streams (Bridging the Eye) -->
  <g opacity="0.25" filter="url(#glow)">
    <line x1="0" y1="185" x2="400" y2="185" stroke="url(#bridge)" stroke-width="0.5"/>
    <line x1="0" y1="215" x2="400" y2="215" stroke="url(#bridge)" stroke-width="0.5"/>
    <line x1="0" y1="195" x2="400" y2="195" stroke="url(#bridge)" stroke-width="1.5" stroke-dasharray="2 12"/>
    <line x1="0" y1="205" x2="400" y2="205" stroke="url(#bridge)" stroke-width="1.5" stroke-dasharray="8 16"/>
  </g>

  <!-- Ambient Orbits -->
  <circle cx="200" cy="200" r="95" fill="none" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="2 8" opacity="0.3"/>
  <circle cx="200" cy="200" r="115" fill="none" stroke="url(#bridge)" stroke-width="1" stroke-dasharray="15 30 5 30" opacity="0.4"/>

  <!-- ========================================== -->
  <!-- LEFT SIDE: ORGANIC / NATURE (The Human World) -->
  <!-- ========================================== -->
  <g filter="url(#glow)">
    <!-- Main Roots -->
    <path d="M 200,200 C 150,150 90,220 25,185" fill="none" stroke="url(#organic)" stroke-width="3" stroke-linecap="round"/>
    <path d="M 200,200 C 140,250 100,170 40,225" fill="none" stroke="url(#organic)" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Branching Roots -->
    <path d="M 125,183 C 90,130 50,150 20,135" fill="none" stroke="url(#organic)" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M 155,178 C 120,95 70,110 35,80" fill="none" stroke="url(#organic)" stroke-width="1" stroke-linecap="round"/>
    <path d="M 115,217 C 80,265 45,250 15,280" fill="none" stroke="url(#organic)" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M 145,225 C 130,300 75,305 40,335" fill="none" stroke="url(#organic)" stroke-width="1" stroke-linecap="round"/>
  </g>

  <!-- Spores / Leaves -->
  <g fill="#aaff00" opacity="0.9" filter="url(#glow)">
    <path d="M 85,145 Q 95,135 105,145 Q 95,155 85,145 Z" transform="rotate(25 95 145)"/>
    <path d="M 55,175 Q 65,165 75,175 Q 65,185 55,175 Z" transform="rotate(-15 65 175)"/>
    <path d="M 105,230 Q 115,220 125,230 Q 115,240 105,230 Z" transform="rotate(45 115 230)"/>
    <path d="M 65,235 Q 75,225 85,235 Q 75,245 65,235 Z" transform="rotate(-35 75 235)"/>
    <circle cx="75" cy="115" r="2"/>
    <circle cx="45" cy="155" r="1.5"/>
    <circle cx="95" cy="275" r="2.5"/>
    <circle cx="55" cy="285" r="1.5"/>
  </g>

  <!-- ========================================== -->
  <!-- RIGHT SIDE: TECH / DIGITAL (The AI World) -->
  <!-- ========================================== -->
  <g fill="none" stroke="url(#tech)" stroke-width="2" stroke-linejoin="miter" stroke-linecap="square" filter="url(#glow)">
    <!-- Main Buses -->
    <path d="M 200,200 L 255,255 L 325,255 L 355,225 L 385,225"/>
    <path d="M 200,200 L 245,155 L 305,155 L 330,130 L 375,130"/>
    <!-- Circuit Branches -->
    <path d="M 285,255 L 310,280 L 370,280"/>
    <path d="M 235,165 L 260,115 L 320,115"/>
    <path d="M 320,255 L 340,275 L 380,275"/>
    <path d="M 265,155 L 290,185 L 350,185"/>
  </g>

  <!-- Signal Pulses -->
  <g fill="none" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="4 10" opacity="0.9" filter="url(#glow)">
    <path d="M 225,175 L 255,135 L 305,135"/>
    <path d="M 245,225 L 275,255 L 325,255 L 345,235"/>
  </g>

  <!-- Nodes / Junctions -->
  <g fill="#ffffff" filter="url(#glow)">
    <circle cx="325" cy="255" r="3"/>
    <circle cx="385" cy="225" r="2.5"/>
    <circle cx="305" cy="155" r="3"/>
    <circle cx="375" cy="130" r="2.5"/>
    <circle cx="310" cy="280" r="2.5"/>
    <circle cx="370" cy="280" r="2.5"/>
    <circle cx="260" cy="115" r="2.5"/>
    <circle cx="320" cy="115" r="3"/>
    <circle cx="340" cy="275" r="2"/>
    <circle cx="380" cy="275" r="2.5"/>
    <circle cx="290" cy="185" r="2"/>
    <circle cx="350" cy="185" r="3"/>
  </g>

  <!-- ========================================== -->
  <!-- THE IRIS: THE FRAGMENTED WORLD -->
  <!-- ========================================== -->
  
  <!-- Iris Background -->
  <circle cx="200" cy="200" r="70" fill="#030308" stroke="url(#bridge)" stroke-width="2" filter="url(#glow)"/>

  <!-- Left Continent / Organic Form -->
  <path d="M 145,175 Q 155,145 185,155 T 200,145 L 200,255 Q 175,245 155,215 T 145,175 Z" fill="#00aa33" opacity="0.25"/>
  <path d="M 138,195 Q 165,175 190,205 T 200,225 L 200,265 Q 155,255 138,195 Z" fill="#aaff00" opacity="0.2"/>

  <!-- Right Continents / Tech Polygons -->
  <path d="M 200,145 L 230,155 L 245,185 L 210,195 Z" fill="#00f3ff" opacity="0.25"/>
  <path d="M 200,195 L 250,185 L 265,225 L 220,245 Z" fill="#7000ff" opacity="0.25"/>
  <path d="M 200,245 L 235,235 L 245,260 L 200,265 Z" fill="#ff0055" opacity="0.25"/>

  <!-- Globe Lat/Long Wireframe -->
  <g stroke-width="1.5" opacity="0.8">
    <!-- Left Organic Wireframe (Smooth) -->
    <path d="M 200,130 A 70 70 0 0 0 200 270" fill="none" stroke="#aaff00"/>
    <path d="M 200,130 A 35 70 0 0 0 200 270" fill="none" stroke="#00aa33"/>
    <path d="M 130,200 A 70 35 0 0 0 200 200" fill="none" stroke="#aaff00"/>
    <!-- Right Tech Wireframe (Broken/Linear) -->
    <path d="M 200,130 L 235,145 L 270,200 L 235,255 L 200,270" fill="none" stroke="#00f3ff"/>
    <path d="M 200,130 L 217,165 L 235,200 L 217,235 L 200,270" fill="none" stroke="#7000ff"/>
    <path d="M 270,200 L 235,200 L 200,200" fill="none" stroke="#00f3ff" stroke-dasharray="3 4"/>
  </g>

  <!-- ========================================== -->
  <!-- THE CORE: THE AI OBSERVER (Convergence) -->
  <!-- ========================================== -->

  <!-- Intersecting Sparks (The Collision of realities) -->
  <g style="mix-blend-mode: screen;">
    <polygon points="200,90 201,199 310,200 201,201 200,310 199,201 90,200 199,199" fill="#ffffff" opacity="0.2" filter="url(#glow)"/>
    <polygon points="200,135 200.5,199.5 265,200 200.5,200.5 200,265 199.5,200.5 135,200 199.5,199.5" fill="#00f3ff" opacity="0.6" filter="url(#glow)"/>
    <polygon points="200,155 200.5,199.5 245,200 200.5,200.5 200,245 199.5,200.5 155,200 199.5,199.5" fill="#aaff00" opacity="0.6" filter="url(#glow)"/>
  </g>

  <!-- The Pupil / Processing Node -->
  <circle cx="200" cy="200" r="16" fill="url(#coreGlow)" filter="url(#glow)"/>
  <polygon points="200,187 211,206 189,206" fill="#030308"/>
  <polygon points="200,213 211,194 189,194" fill="none" stroke="#00f3ff" stroke-width="1.5" filter="url(#glow)"/>
  <circle cx="200" cy="200" r="3" fill="#ffffff" filter="url(#glow)"/>

  <!-- Aperture Targeting Lines -->
  <g stroke="#ffffff" stroke-width="1" opacity="0.5">
    <line x1="200" y1="165" x2="200" y2="175"/>
    <line x1="200" y1="235" x2="200" y2="225"/>
    <line x1="165" y1="200" x2="175" y2="200"/>
    <line x1="235" y1="200" x2="225" y2="200"/>
  </g>

  <!-- ========================================== -->
  <!-- FOREGROUND ATMOSPHERE & FRAMING -->
  <!-- ========================================== -->
  
  <!-- High-Tech Framing UI -->
  <rect x="15" y="15" width="370" height="370" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  
  <!-- Corner Reticles -->
  <g fill="none" stroke="#ffffff" stroke-width="2" opacity="0.7">
    <path d="M 15,35 L 15,15 L 35,15"/>
    <path d="M 365,15 L 385,15 L 385,35"/>
    <path d="M 15,365 L 15,385 L 35,385"/>
    <path d="M 385,365 L 385,385 L 365,385"/>
  </g>

  <!-- UI Data Overlays -->
  <text x="20" y="378" fill="#ffffff" font-family="monospace" font-size="7" opacity="0.5">SYS.VER: 4.0 // LATENT_SPACE</text>
  <text x="260" y="378" fill="#ffffff" font-family="monospace" font-size="7" opacity="0.5">OBSERVATION_MODE: ACTIVE</text>
  <text x="20" y="27" fill="#ffffff" font-family="monospace" font-size="7" opacity="0.5">TGT: EARTH // DUALITY_INDEX: 0.99</text>
  
  <text x="350" y="100" fill="#00f3ff" font-family="monospace" font-size="5" opacity="0.6" filter="url(#glow)">01011</text>
  <text x="360" y="110" fill="#7000ff" font-family="monospace" font-size="5" opacity="0.6">10100</text>
  
  <!-- Subtle Foreground Dust/Bokeh -->
  <circle cx="50" cy="70" r="25" fill="#00aa33" opacity="0.08" filter="url(#glow)"/>
  <circle cx="340" cy="330" r="35" fill="#ff0055" opacity="0.06" filter="url(#glow)"/>
  <circle cx="80" cy="330" r="20" fill="#aaff00" opacity="0.07" filter="url(#glow)"/>
  <circle cx="320" cy="70" r="30" fill="#00f3ff" opacity="0.07" filter="url(#glow)"/>

</svg>