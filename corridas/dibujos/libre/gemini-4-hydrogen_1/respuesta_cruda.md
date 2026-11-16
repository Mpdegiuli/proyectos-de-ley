<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#070b1e"/>
      <stop offset="55%" stop-color="#131c3d"/>
      <stop offset="100%" stop-color="#2a2d5a"/>
    </linearGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff8d6" stop-opacity="0.9"/>
      <stop offset="40%" stop-color="#ffe799" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#ffe799" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#102142"/>
      <stop offset="50%" stop-color="#0a1630"/>
      <stop offset="100%" stop-color="#050b18"/>
    </linearGradient>
    <linearGradient id="beam" x1="1" y1="0.5" x2="0" y2="0.5">
      <stop offset="0%" stop-color="#fff5a8" stop-opacity="0.8"/>
      <stop offset="45%" stop-color="#ffe678" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#ffe678" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="towerShade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000" stop-opacity="0.05"/>
      <stop offset="65%" stop-color="#000" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="cliff" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#222538"/>
      <stop offset="100%" stop-color="#0c0e17"/>
    </linearGradient>
    <radialGradient id="lanternGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="35%" stop-color="#fff199"/>
      <stop offset="100%" stop-color="#ffaa00" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="towerClip">
      <polygon points="282,115 306,115 316,245 272,245"/>
    </clipPath>
  </defs>

  <!-- Cielo -->
  <rect width="400" height="275" fill="url(#sky)"/>

  <!-- Estrellas -->
  <g fill="#ffffff">
    <circle cx="32" cy="36" r="1.2" opacity="0.9"/>
    <circle cx="68" cy="24" r="0.8" opacity="0.6"/>
    <circle cx="115" cy="52" r="1.5" opacity="0.8"/>
    <circle cx="158" cy="28" r="0.9" opacity="0.7"/>
    <circle cx="204" cy="44" r="1.1" opacity="0.85"/>
    <circle cx="248" cy="22" r="1.4" opacity="0.9"/>
    <circle cx="290" cy="58" r="0.8" opacity="0.6"/>
    <circle cx="342" cy="35" r="1.3" opacity="0.9"/>
    <circle cx="375" cy="70" r="1" opacity="0.7"/>
    <circle cx="48" cy="88" r="1" opacity="0.75"/>
    <circle cx="145" cy="96" r="0.7" opacity="0.5"/>
    <circle cx="195" cy="82" r="1.3" opacity="0.85"/>
    <circle cx="236" cy="76" r="0.9" opacity="0.6"/>
    <circle cx="320" cy="84" r="1.1" opacity="0.8"/>
    <circle cx="364" cy="115" r="0.8" opacity="0.65"/>
    <circle cx="25" cy="140" r="1.1" opacity="0.7"/>
    <circle cx="72" cy="162" r="0.8" opacity="0.55"/>
    <circle cx="168" cy="155" r="1.2" opacity="0.7"/>
    <circle cx="222" cy="135" r="0.9" opacity="0.6"/>
    <circle cx="348" cy="165" r="1" opacity="0.75"/>
    <path d="M248,18 L249.5,21.5 L253,23 L249.5,24.5 L248,28 L246.5,24.5 L243,23 L246.5,21.5 Z" opacity="0.85"/>
    <path d="M55,115 L56,118 L59,119 L56,120 L55,123 L54,120 L51,119 L54,118 Z" opacity="0.75"/>
  </g>

  <!-- Luna y halo -->
  <circle cx="105" cy="105" r="78" fill="url(#moonGlow)"/>
  <circle cx="105" cy="105" r="32" fill="#fff7d6"/>
  <g fill="#ebdcb0" opacity="0.55">
    <circle cx="94" cy="96" r="6"/>
    <circle cx="116" cy="114" r="8"/>
    <circle cx="114" cy="92" r="4"/>
    <circle cx="92" cy="116" r="3.5"/>
  </g>

  <!-- Nubes sutiles -->
  <path d="M10,132 Q45,122 80,132 Q115,125 145,135 Q110,142 65,140 Q30,143 10,132 Z" fill="#2c3563" opacity="0.45"/>
  <path d="M180,98 Q220,88 265,98 Q295,93 330,104 Q285,110 235,107 Q200,109 180,98 Z" fill="#242c54" opacity="0.5"/>
  <path d="M275,152 Q315,144 355,153 Q382,148 400,158 L400,165 Q340,164 275,152 Z" fill="#21284d" opacity="0.5"/>

  <!-- Siluetas de aves -->
  <g stroke="#0e142e" stroke-width="1.6" fill="none" stroke-linecap="round">
    <path d="M150,76 Q155,70 160,76 Q165,70 170,76"/>
    <path d="M172,88 Q176,83 180,88 Q184,83 188,88"/>
    <path d="M132,64 Q135,60 138,64 Q141,60 144,64"/>
  </g>

  <!-- Mar -->
  <rect x="0" y="275" width="400" height="125" fill="url(#sea)"/>

  <!-- Reflejo de la luna en el agua -->
  <g fill="#ffe89c">
    <ellipse cx="105" cy="280" rx="34" ry="2.2" opacity="0.65"/>
    <ellipse cx="106" cy="287" rx="28" ry="2" opacity="0.55"/>
    <ellipse cx="103" cy="295" rx="36" ry="2.4" opacity="0.5"/>
    <ellipse cx="107" cy="304" rx="24" ry="2" opacity="0.45"/>
    <ellipse cx="104" cy="314" rx="30" ry="2.3" opacity="0.4"/>
    <ellipse cx="106" cy="325" rx="20" ry="1.8" opacity="0.35"/>
    <ellipse cx="102" cy="336" rx="25" ry="2" opacity="0.3"/>
    <ellipse cx="108" cy="348" rx="16" ry="1.6" opacity="0.25"/>
    <ellipse cx="104" cy="362" rx="18" ry="1.8" opacity="0.2"/>
    <ellipse cx="106" cy="378" rx="12" ry="1.5" opacity="0.15"/>
  </g>

  <!-- Ondas del mar -->
  <g stroke="#29487d" stroke-width="1.5" fill="none" opacity="0.55">
    <path d="M0,290 Q45,286 90,290 T180,290 T270,290"/>
    <path d="M20,312 Q70,307 120,312 T220,312"/>
    <path d="M0,342 Q60,336 120,342 T240,342"/>
    <path d="M10,375 Q80,368 150,375 T290,375"/>
  </g>

  <!-- Pequeño velero lejano -->
  <g transform="translate(175,263)">
    <polygon points="0,12 24,12 19,17 4,17" fill="#0d1326"/>
    <polygon points="11,0 11,11 2,11" fill="#c8d2eb" opacity="0.85"/>
    <polygon points="12,2 12,11 20,11" fill="#9aa8cc" opacity="0.8"/>
    <line x1="11" y1="0" x2="11" y2="12" stroke="#0d1326" stroke-width="1"/>
    <!-- Reflejo del velero -->
    <polygon points="4,19 19,19 14,26 8,26" fill="#0d1326" opacity="0.35"/>
  </g>

  <!-- Haz de luz del faro -->
  <polygon points="292,100 0,30 0,185 292,110" fill="url(#beam)"/>

  <!-- Acantilado rocoso -->
  <polygon points="195,400 218,348 232,315 245,268 265,245 360,245 385,265 400,290 400,400" fill="url(#cliff)"/>
  <polygon points="245,268 265,245 315,245 295,282 260,315 232,315" fill="#2c314a" opacity="0.7"/>
  <polygon points="295,282 340,262 385,265 365,330 310,365 260,315" fill="#171a29" opacity="0.85"/>
  <polygon points="218,348 260,315 310,365 280,400 195,400" fill="#121421"/>
  <!-- Espuma contra las rocas -->
  <path d="M188,396 Q205,388 220,395 Q235,386 248,398" stroke="#6282b8" stroke-width="2.5" fill="none" opacity="0.6" stroke-linecap="round"/>
  <path d="M210,368 Q222,360 232,367" stroke="#6282b8" stroke-width="2" fill="none" opacity="0.5" stroke-linecap="round"/>

  <!-- Casita del farero -->
  <g>
    <rect x="312" y="218" width="44" height="27" fill="#d9dde6"/>
    <rect x="342" y="218" width="14" height="27" fill="#a8b0c2"/>
    <polygon points="307,218 334,200 361,218" fill="#8c262b"/>
    <polygon points="334,200 361,218 345,218" fill="#63191c"/>
    <rect x="322" y="226" width="10" height="10" fill="#ffd966"/>
    <line x1="327" y1="226" x2="327" y2="236" stroke="#63191c" stroke-width="1"/>
    <line x1="322" y1="231" x2="332" y2="231" stroke="#63191c" stroke-width="1"/>
    <rect x="345" y="228" width="7" height="17" fill="#4a2511"/>
    <rect x="345" y="198" width="6" height="12" fill="#4f566b"/>
  </g>

  <!-- Torre del faro -->
  <g clip-path="url(#towerClip)">
    <rect x="270" y="115" width="50" height="26" fill="#e63946"/>
    <rect x="270" y="141" width="50" height="26" fill="#f1f3f8"/>
    <rect x="270" y="167" width="50" height="26" fill="#e63946"/>
    <rect x="270" y="193" width="50" height="26" fill="#f1f3f8"/>
    <rect x="270" y="219" width="50" height="26" fill="#e63946"/>
    <polygon points="282,115 306,115 316,245 272,245" fill="url(#towerShade)"/>
  </g>

  <!-- Ventanas de la torre -->
  <rect x="291" y="149" width="6" height="10" rx="3" fill="#ffe680"/>
  <rect x="291" y="201" width="6" height="10" rx="3" fill="#ffe680"/>

  <!-- Balcón y linterna -->
  <rect x="276" y="112" width="36" height="5" rx="1" fill="#1e2436"/>
  <g stroke="#1e2436" stroke-width="1.2">
    <line x1="278" y1="106" x2="310" y2="106"/>
    <line x1="278" y1="106" x2="278" y2="112"/>
    <line x1="286" y1="106" x2="286" y2="112"/>
    <line x1="294" y1="106" x2="294" y2="112"/>
    <line x1="302" y1="106" x2="302" y2="112"/>
    <line x1="310" y1="106" x2="310" y2="112"/>
  </g>

  <!-- Cámara de luz -->
  <rect x="284" y="96" width="20" height="16" fill="#fff6b3"/>
  <circle cx="294" cy="104" r="24" fill="url(#lanternGlow)"/>
  <g stroke="#1e2436" stroke-width="1.2">
    <line x1="284" y1="96" x2="284" y2="112"/>
    <line x1="294" y1="96" x2="294" y2="112"/>
    <line x1="304" y1="96" x2="304" y2="112"/>
  </g>

  <!-- Cúpula del faro -->
  <path d="M281,96 Q294,82 307,96 Z" fill="#1e2436"/>
  <line x1="294" y1="82" x2="294" y2="77" stroke="#1e2436" stroke-width="2" stroke-linecap="round"/>
  <circle cx="294" cy="77" r="1.8" fill="#ffd966"/>

  <!-- Arbustos en el acantilado -->
  <g fill="#121a24">
    <circle cx="268" cy="246" r="6"/>
    <circle cx="275" cy="247" r="4"/>
    <circle cx="358" cy="245" r="7"/>
    <circle cx="366" cy="247" r="5"/>
  </g>
</svg>