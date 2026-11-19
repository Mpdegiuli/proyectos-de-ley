<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#070b1e"/>
      <stop offset="45%" stop-color="#111d3a"/>
      <stop offset="80%" stop-color="#1f3a5c"/>
      <stop offset="100%" stop-color="#325573"/>
    </linearGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff8d6" stop-opacity="0.7"/>
      <stop offset="35%" stop-color="#a8d0f0" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#111d3a" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="moonFill" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#fffdf0"/>
      <stop offset="70%" stop-color="#f6e7be"/>
      <stop offset="100%" stop-color="#d8c394"/>
    </radialGradient>
    <linearGradient id="aurora" x1="0" y1="0" x2="1" y2="0.4">
      <stop offset="0%" stop-color="#2ee6a6" stop-opacity="0"/>
      <stop offset="35%" stop-color="#2ee6a6" stop-opacity="0.22"/>
      <stop offset="70%" stop-color="#4ea8de" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#7b5cf0" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1d3b58"/>
      <stop offset="30%" stop-color="#12273f"/>
      <stop offset="75%" stop-color="#0a1628"/>
      <stop offset="100%" stop-color="#050b16"/>
    </linearGradient>
    <linearGradient id="beamL" x1="1" y1="0.5" x2="0" y2="0.5">
      <stop offset="0%" stop-color="#fff5b8" stop-opacity="0.82"/>
      <stop offset="25%" stop-color="#ffe787" stop-opacity="0.38"/>
      <stop offset="70%" stop-color="#ffe787" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#ffe787" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="beamR" x1="0" y1="0.5" x2="1" y2="0.5">
      <stop offset="0%" stop-color="#fff5b8" stop-opacity="0.72"/>
      <stop offset="45%" stop-color="#ffe787" stop-opacity="0.24"/>
      <stop offset="100%" stop-color="#ffe787" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="towerShade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2"/>
      <stop offset="45%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#050a18" stop-opacity="0.55"/>
    </linearGradient>
    <linearGradient id="cliffDark" x1="0" y1="0" x2="0.3" y2="1">
      <stop offset="0%" stop-color="#273245"/>
      <stop offset="50%" stop-color="#171f2e"/>
      <stop offset="100%" stop-color="#0b101a"/>
    </linearGradient>
    <radialGradient id="lampGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#fff099" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#ffb84d" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#ffb84d" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4"/>
    </filter>
    <clipPath id="towerClip">
      <polygon points="292,130 318,130 328,236 282,236"/>
    </clipPath>
  </defs>

  <!-- Cielo -->
  <rect width="400" height="270" fill="url(#sky)"/>

  <!-- Aurora sutil -->
  <path d="M-20,90 Q80,35 180,75 T390,45 L410,95 Q290,120 180,105 T-20,130 Z" fill="url(#aurora)" filter="url(#soft)"/>

  <!-- Estrellas -->
  <g fill="#ffffff">
    <circle cx="28" cy="24" r="1.2" opacity="0.9"/>
    <circle cx="64" cy="46" r="0.8" opacity="0.7"/>
    <circle cx="155" cy="28" r="1.1" opacity="0.85"/>
    <circle cx="188" cy="54" r="0.9" opacity="0.75"/>
    <circle cx="222" cy="22" r="1.4" opacity="0.9"/>
    <circle cx="258" cy="48" r="0.8" opacity="0.65"/>
    <circle cx="295" cy="30" r="1" opacity="0.8"/>
    <circle cx="342" cy="18" r="1.3" opacity="0.9"/>
    <circle cx="372" cy="52" r="0.9" opacity="0.7"/>
    <circle cx="355" cy="84" r="1.1" opacity="0.6"/>
    <circle cx="242" cy="76" r="0.8" opacity="0.6"/>
    <circle cx="42" cy="128" r="0.9" opacity="0.6"/>
    <circle cx="172" cy="108" r="0.7" opacity="0.5"/>
    <circle cx="204" cy="136" r="0.8" opacity="0.45"/>
    <circle cx="16" cy="84" r="1" opacity="0.7"/>
    <circle cx="134" cy="14" r="0.9" opacity="0.8"/>
    <circle cx="274" cy="14" r="0.7" opacity="0.75"/>
    <path d="M222,16 L223.2,20.8 L228,22 L223.2,23.2 L222,28 L220.8,23.2 L216,22 L220.8,20.8 Z" opacity="0.85"/>
    <path d="M342,13 L342.9,17.1 L347,18 L342.9,18.9 L342,23 L341.1,18.9 L337,18 L341.1,17.1 Z" opacity="0.75"/>
  </g>

  <!-- Luna y resplandor -->
  <circle cx="105" cy="96" r="95" fill="url(#moonGlow)"/>
  <circle cx="105" cy="96" r="34" fill="url(#moonFill)"/>
  <g fill="#cbb587" opacity="0.35">
    <circle cx="94" cy="86" r="7"/>
    <circle cx="116" cy="104" r="9"/>
    <circle cx="114" cy="80" r="4"/>
    <circle cx="92" cy="108" r="5"/>
    <circle cx="103" cy="96" r="3"/>
  </g>

  <!-- Nubes nocturnas -->
  <g fill="#1c3252" opacity="0.65">
    <path d="M-10,164 Q25,148 60,158 Q88,144 125,156 Q150,150 175,164 Z"/>
    <path d="M210,185 Q245,172 280,182 Q315,170 355,182 Q382,176 410,188 L410,196 L210,196 Z" opacity="0.5"/>
  </g>
  <path d="M52,118 Q74,110 98,116 Q122,108 148,118 Q130,124 95,123 Q68,125 52,118 Z" fill="#233b5e" opacity="0.75"/>

  <!-- Montañas lejanas -->
  <path d="M0,266 L0,248 Q35,232 72,246 Q108,228 148,250 Q176,242 205,266 Z" fill="#13243b"/>

  <!-- Mar -->
  <rect x="0" y="265" width="400" height="135" fill="url(#sea)"/>

  <!-- Reflejo de la luna en el mar -->
  <g fill="#f5e6be" opacity="0.55">
    <rect x="78" y="268" width="54" height="2.2" rx="1"/>
    <rect x="84" y="274" width="42" height="2" rx="1" opacity="0.8"/>
    <rect x="72" y="281" width="66" height="2.4" rx="1" opacity="0.75"/>
    <rect x="88" y="289" width="34" height="2" rx="1" opacity="0.65"/>
    <rect x="76" y="297" width="58" height="2.6" rx="1" opacity="0.6"/>
    <rect x="90" y="307" width="32" height="2.2" rx="1" opacity="0.5"/>
    <rect x="80" y="318" width="48" height="2.6" rx="1" opacity="0.4"/>
    <rect x="93" y="331" width="26" height="2.4" rx="1" opacity="0.32"/>
    <rect x="86" y="345" width="38" height="2.2" rx="1" opacity="0.22"/>
    <rect x="96" y="362" width="20" height="2" rx="1" opacity="0.16"/>
  </g>

  <!-- Velero lejano -->
  <g transform="translate(148, 250)">
    <polygon points="0,14 22,14 18,18 4,18" fill="#0b1524"/>
    <polygon points="10,0 10,13 2,13" fill="#1a2c47"/>
    <polygon points="12,3 12,13 20,13" fill="#122238"/>
    <rect x="4" y="19" width="14" height="1.5" rx="0.7" fill="#07101c" opacity="0.6"/>
  </g>

  <!-- Haz de luz del faro -->
  <polygon points="305,108 0,32 0,174" fill="url(#beamL)" filter="url(#soft)"/>
  <polygon points="305,108 400,72 400,144" fill="url(#beamR)" filter="url(#soft)"/>

  <!-- Acantilado rocoso -->
  <path d="M180,350 L205,305 L234,264 L256,238 L286,232 L348,228 L385,238 L400,248 L400,400 L165,400 Z" fill="url(#cliffDark)"/>
  <!-- Facetas iluminadas del acantilado -->
  <polygon points="234,264 256,238 286,232 272,272 246,294" fill="#324159" opacity="0.6"/>
  <polygon points="286,232 348,228 332,268 272,272" fill="#232e42" opacity="0.7"/>
  <polygon points="205,305 246,294 268,338 212,358" fill="#1d2738" opacity="0.75"/>
  <polygon points="332,268 385,238 400,285 352,310" fill="#101724" opacity="0.8"/>

  <!-- Casita del farero -->
  <g>
    <polygon points="325,212 362,212 362,232 325,232" fill="#c9c2b2"/>
    <polygon points="325,212 362,212 362,232 325,232" fill="#0b1324" opacity="0.45"/>
    <polygon points="320,213 344,199 367,213" fill="#8f2929"/>
    <rect x="334" y="217" width="8" height="9" rx="1" fill="#ffcf6b"/>
    <rect x="348" y="217" width="7" height="9" rx="1" fill="#ffcf6b" opacity="0.85"/>
    <rect x="352" y="200" width="4" height="9" fill="#5e2121"/>
  </g>

  <!-- Torre del faro -->
  <g clip-path="url(#towerClip)">
    <rect x="280" y="130" width="52" height="106" fill="#ebe6da"/>
    <rect x="280" y="146" width="52" height="22" fill="#b83232"/>
    <rect x="280" y="188" width="52" height="24" fill="#b83232"/>
    <rect x="280" y="130" width="52" height="106" fill="url(#towerShade)"/>
  </g>

  <!-- Ventanitas de la torre -->
  <rect x="303" y="153" width="4" height="7" rx="2" fill="#ffe18c"/>
  <rect x="303" y="196" width="4" height="8" rx="2" fill="#2b1b1b"/>
  <rect x="302" y="222" width="6" height="12" rx="3" fill="#201818"/>

  <!-- Galería y linterna del faro -->
  <rect x="286" y="126" width="38" height="5" rx="1.5" fill="#2b3648"/>
  <rect x="289" y="119" width="32" height="7" fill="none" stroke="#1e2736" stroke-width="1.5"/>
  <line x1="295" y1="119" x2="295" y2="126" stroke="#1e2736" stroke-width="1.2"/>
  <line x1="305" y1="119" x2="305" y2="126" stroke="#1e2736" stroke-width="1.2"/>
  <line x1="315" y1="119" x2="315" y2="126" stroke="#1e2736" stroke-width="1.2"/>

  <!-- Cámara de luz -->
  <rect x="294" y="100" width="22" height="20" fill="#fff3b0"/>
  <circle cx="305" cy="109" r="24" fill="url(#lampGlow)"/>
  <circle cx="305" cy="109" r="5" fill="#ffffff"/>
  <line x1="299" y1="100" x2="299" y2="120" stroke="#2b3648" stroke-width="1.2"/>
  <line x1="311" y1="100" x2="311" y2="120" stroke="#2b3648" stroke-width="1.2"/>

  <!-- Cúpula y aguja -->
  <path d="M291,100 Q305,84 319,100 Z" fill="#a82828"/>
  <circle cx="305" cy="89" r="2.2" fill="#d9b46c"/>
  <line x1="305" y1="87" x2="305" y2="78" stroke="#d9b46c" stroke-width="1.3"/>

  <!-- Olas y espuma contra las rocas -->
  <g fill="none" stroke-linecap="round">
    <path d="M12,302 Q45,296 78,302" stroke="#2b4c6e" stroke-width="1.8" opacity="0.5"/>
    <path d="M132,324 Q165,318 192,326" stroke="#31587d" stroke-width="2" opacity="0.55"/>
    <path d="M25,356 Q72,346 122,356" stroke="#22405e" stroke-width="2.2" opacity="0.55"/>
    <path d="M150,378 Q210,366 268,378" stroke="#2a4f73" stroke-width="2.2" opacity="0.45"/>
    <path d="M168,352 Q188,342 206,350 Q222,340 242,352" stroke="#cfe4f5" stroke-width="2.6" opacity="0.65"/>
    <path d="M180,362 Q204,354 228,364" stroke="#9ec2de" stroke-width="1.8" opacity="0.45"/>
    <path d="M248,388 Q284,376 322,388 Q356,378 394,390" stroke="#7da3c4" stroke-width="2" opacity="0.35"/>
  </g>

  <!-- Gaviotas en silueta -->
  <g fill="none" stroke="#0d1729" stroke-width="1.6" stroke-linecap="round">
    <path d="M182,126 Q187,121 192,125 Q197,121 202,126"/>
    <path d="M210,144 Q214,140 218,143 Q222,140 226,144"/>
    <path d="M162,146 Q165,143 168,145 Q171,143 174,146"/>
  </g>
</svg>