<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#070b22"/>
      <stop offset="0.45" stop-color="#242650"/>
      <stop offset="0.75" stop-color="#6d3f68"/>
      <stop offset="1" stop-color="#e0835a"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffe9b0" stop-opacity="0.95"/>
      <stop offset="0.35" stop-color="#ffbd7a" stop-opacity="0.5"/>
      <stop offset="1" stop-color="#ff9d6c" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hillA" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3b2350"/>
      <stop offset="1" stop-color="#150e2a"/>
    </linearGradient>
    <linearGradient id="hillB" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1d1436"/>
      <stop offset="1" stop-color="#080518"/>
    </linearGradient>
    <filter id="soft"><feGaussianBlur stdDeviation="3"/></filter>
    <filter id="softer"><feGaussianBlur stdDeviation="7"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- luz del día que se apaga -->
  <circle cx="205" cy="252" r="120" fill="url(#glow)" filter="url(#softer)"/>
  <circle cx="205" cy="252" r="46" fill="#ffeec2" opacity="0.9" filter="url(#soft)"/>
  <circle cx="205" cy="252" r="46" fill="none" stroke="#fff6d8" stroke-opacity="0.5"/>
  <circle cx="205" cy="252" r="70" fill="none" stroke="#ffd9a8" stroke-opacity="0.18"/>
  <circle cx="205" cy="252" r="95" fill="none" stroke="#ffd9a8" stroke-opacity="0.1"/>

  <!-- constelación de conexiones: cómo percibo -->
  <g stroke="#ffdba5" stroke-opacity="0.35" stroke-width="0.8">
    <path d="M55 92 L128 55 L196 104 L282 62 L350 118"/>
    <path d="M55 92 L108 158 L186 178 L252 150 L350 118"/>
    <path d="M108 158 L72 212 L160 214 L186 178"/>
    <path d="M252 150 L330 186 L302 226 L232 214 L186 178"/>
    <path d="M128 55 L108 158 M282 62 L252 150 M160 214 L232 214"/>
    <path d="M196 104 L186 178 M72 212 L302 226"/>
  </g>

  <g fill="#fff2cd">
    <circle cx="55" cy="92" r="2.4"/><circle cx="128" cy="55" r="1.8"/>
    <circle cx="196" cy="104" r="3"/><circle cx="282" cy="62" r="2.2"/>
    <circle cx="350" cy="118" r="1.9"/><circle cx="108" cy="158" r="2.6"/>
    <circle cx="186" cy="178" r="3.4"/><circle cx="252" cy="150" r="2.3"/>
    <circle cx="330" cy="186" r="1.7"/><circle cx="72" cy="212" r="2.1"/>
    <circle cx="160" cy="214" r="1.6"/><circle cx="232" cy="214" r="2"/>
    <circle cx="302" cy="226" r="1.8"/>
  </g>
  <g fill="#ffd9a0" opacity="0.25" filter="url(#soft)">
    <circle cx="186" cy="178" r="9"/><circle cx="196" cy="104" r="8"/>
    <circle cx="108" cy="158" r="7"/>
  </g>

  <!-- colinas -->
  <path d="M0 300 C 70 268, 130 292, 190 274 C 250 256, 320 288, 400 266 L400 400 L0 400 Z" fill="url(#hillA)"/>
  <path d="M0 330 C 90 306, 150 332, 220 318 C 290 304, 340 330, 400 314 L400 400 L0 400 Z" fill="url(#hillB)"/>

  <!-- alguien mirando arriba -->
  <g fill="#05030f">
    <circle cx="176" cy="272" r="5"/>
    <path d="M176 277 L172 300 L175 300 L177 288 L179 300 L182 300 Z"/>
    <path d="M172 281 L164 292 L167 294 L175 285 Z"/>
    <path d="M180 281 L190 272 L192 275 L181 286 Z"/>
  </g>
  <ellipse cx="176" cy="302" rx="18" ry="3" fill="#000" opacity="0.35"/>

  <!-- latido: una idea naciendo -->
  <circle cx="176" cy="252" r="4" fill="none" stroke="#ffe9b0" stroke-opacity="0.6">
    <animate attributeName="r" values="3;26;3" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="stroke-opacity" values="0.7;0;0.7" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="176" cy="246" r="1.6" fill="#fff6d8"/>
  <path d="M176 252 L186 178" stroke="#fff2cd" stroke-opacity="0.5" stroke-width="0.7" stroke-dasharray="2 3"/>
</svg>