```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <!-- Sky background -->
  <defs>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#87CEEB"/>
      <stop offset="100%" stop-color="#E0F4FF"/>
    </linearGradient>
    <linearGradient id="grassGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5DBB63"/>
      <stop offset="100%" stop-color="#3A8C40"/>
    </linearGradient>
    <linearGradient id="wallGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F5DEB3"/>
      <stop offset="100%" stop-color="#DEB887"/>
    </linearGradient>
    <linearGradient id="roofGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#C0392B"/>
      <stop offset="100%" stop-color="#922B21"/>
    </linearGradient>
    <linearGradient id="doorGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8B4513"/>
      <stop offset="100%" stop-color="#5C2E00"/>
    </linearGradient>
    <linearGradient id="sunGrad" cx="50%" cy="50%" r="50%" fx="50%" fy="50%" id="sunGrad" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#FFF176"/>
      <stop offset="100%" stop-color="#FFD600"/>
    </linearGradient>
    <radialGradient id="sunRad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFDE7"/>
      <stop offset="100%" stop-color="#FFD600"/>
    </radialGradient>
  </defs>

  <!-- Sky -->
  <rect x="0" y="0" width="400" height="400" fill="url(#skyGrad)"/>

  <!-- Sun -->
  <circle cx="340" cy="60" r="35" fill="url(#sunRad)" opacity="0.95"/>
  <!-- Sun rays -->
  <g stroke="#FFD600" stroke-width="2.5" opacity="0.7">
    <line x1="340" y1="15" x2="340" y2="5"/>
    <line x1="340" y1="105" x2="340" y2="115"/>
    <line x1="295" y1="60" x2="285" y2="60"/>
    <line x1="385" y1="60" x2="395" y2="60"/>
    <line x1="308" y1="28" x2="301" y2="21"/>
    <line x1="372" y1="92" x2="379" y2="99"/>
    <line x1="372" y1="28" x2="379" y2="21"/>
    <line x1="308" y1="92" x2="301" y2="99"/>
  </g>

  <!-- Clouds -->
  <g opacity="0.9">
    <ellipse cx="80" cy="70" rx="40" ry="22" fill="white"/>
    <ellipse cx="110" cy="58" rx="30" ry="20" fill="white"/>
    <ellipse cx="50" cy="75" rx="28" ry="16" fill="white"/>
  </g>
  <g opacity="0.85">
    <ellipse cx="220" cy="50" rx="35" ry="18" fill="white"/>
    <ellipse cx="248" cy="40" rx="25" ry="17" fill="white"/>
    <ellipse cx="195" cy="55" rx="22" ry="13" fill="white"/>
  </g>

  <!-- Grass -->
  <rect x="0" y="290" width="400" height="110" fill="url(#grassGrad)"/>

  <!-- Path to door -->
  <polygon points="175,290 225,290 210,370 190,370" fill="#C8A86B" opacity="0.8"/>

  <!-- House main wall -->
  <rect x="80" y="190" width="240" height="100" fill="url(#wallGrad)" stroke="#C4A265" stroke-width="1.5"/>

  <!-- Roof -->
  <polygon points="60,195 200,90 340,195" fill="url(#roofGrad)" stroke="#7B241C" stroke-width="2"/>
  <!-- Roof overhang detail -->
  <polygon points="60,195 340,195 340,205 60,205" fill="#922B21"/>

  <!-- Chimney -->
  <rect x="260" y="105" width="30" height="70" fill="#B0B0B0" stroke="#808080" stroke-width="1.5"/>
  <rect x="255" y="100" width="40" height="12" fill="#909090" stroke="#707070" stroke-width="1"/>
  <!-- Smoke -->
  <path d="M270,100 Q265,85 272,75 Q279,65 273,55" fill="none" stroke="#CCCCCC" stroke-width="4" stroke-linecap="round" opacity="0.6"/>
  <path d="M280,98 Q285,83 278,72 Q271,61 277,50" fill="none" stroke="#DDDDDD" stroke-width="3" stroke-linecap="round" opacity="0.5"/>

  <!-- Door -->
  <rect x="170" y="230" width="60" height="60" rx="4" fill="url(#doorGrad)" stroke="#4A1C00" stroke-width="2"/>
  <!-- Door arch top -->
  <path d="M170,245 Q200,220 230,245" fill="#7A3B10" stroke="#4A1C00" stroke-width="2"/>
  <!-- Door knob -->
  <circle cx="222" cy="263" r="4" fill="#DAA520" stroke="#B8860B" stroke-width="1"/>
  <!-- Door panel detail -->
  <rect x="178" y="248" width="19" height="16" rx="2" fill="none" stroke="#5C2E00" stroke-width="1" opacity="0.6"/>
  <rect x="203" y="248" width="19" height="16" rx="2" fill="none" stroke="#5C2E00" stroke-width="1" opacity="0.6"/>

  <!-- Left window -->
  <rect x="100" y="210" width="55" height="45" rx="3" fill="#AED6F1" stroke="#C4A265" stroke-width="2"/>
  <!-- Window frame cross -->
  <line x1="127" y1="210" x2="127" y2="255" stroke="#C4A265" stroke-width="2"/>
  <line x1="100" y1="232" x2="155" y2="232" stroke="#C4A265" stroke-width="2"/>
  <!-- Window shine -->
  <rect x="103" y="213" width="20" height="17" rx="1" fill="white" opacity="0.3"/>

  <!-- Right window -->
  <rect x="245" y="210" width="55" height="45" rx="3" fill="#AED6F1" stroke="#C4A265" stroke-width="2"/>
  <!-- Window frame cross -->
  <line x1="272" y1="210" x2="272" y2="255" stroke="#C4A265" stroke-width="2"/>
  <line x1="245" y1="232" x2="300" y2="232" stroke="#C4A265" stroke-width="2"/>
  <!-- Window shine -->
  <rect x="248" y="213" width="20" height="17" rx="1" fill="white" opacity="0.3"/>

  <!-- Curtains left window -->
  <rect x="100" y="210" width="12" height="45" rx="2" fill="#FF8A65" opacity="0.7"/>
  <rect x="143" y="210" width="12" height="45" rx="2" fill="#FF8A65" opacity="0.7"/>

  <!-- Curtains right window -->
  <rect x="245" y="210" width="12" height="45" rx="2" fill="#FF8A65" opacity="0.7"/>
  <rect x="288" y="210" width="12" height="45" rx="2" fill="#FF8A65" opacity="0.7"/>

  <!-- Trees -->
  <!-- Left tree -->
  <rect x="30" y="250" width="12" height="45" fill="#7D5A2F"/>
  <ellipse cx="36" cy="230" rx="28" ry="35" fill="#2E7D32"/>
  <ellipse cx="25" cy="245" rx="18" ry="22" fill="#388E3C"/>
  <ellipse cx="47" cy="248" rx="16" ry="20" fill="#1B5E20"/>

  <!-- Right tree -->
  <rect x="360" y="255" width="12" height="40" fill="#7D5A2F"/>
  <ellipse cx="366" cy="235" rx="26" ry="32" fill="#2E7D32"/>
  <ellipse cx="354" cy="250" rx="17" ry="20" fill="#388E3C"/>
  <ellipse cx="378" cy="252" rx="15" ry="18" fill="#1B5E20"/>

  <!-- Flower bushes -->
  <g>
    <ellipse cx="95" cy="292" rx="18" ry="10" fill="#388E3C"/>
    <circle cx="85" cy="287" r="5" fill="#FF69B4"/>
    <circle cx="95" cy="285" r="5" fill="#FFD700"/>
    <circle cx="105" cy="287" r="5" fill="#FF69B4"/>
  </g>
  <g>
    <ellipse cx="305" cy="292" rx="18" ry="10" fill="#388E3C"/>
    <circle cx="295" cy="287" r="5" fill="#FF69B4"/>
    <circle cx="305" cy="285" r="5" fill="#FFD700"/>
    <circle cx="315" cy="287" r="5" fill="#EE82EE"/>
  </g>

  <!-- Birds in sky -->
  <g stroke="#333" stroke-width="1.5" fill="none">
    <path d="M150,80 Q155,75 160,80"/>
    <path d="M163,77 Q168,72 173,77"/>
  </g>
  <g stroke="#333" stroke-width="1.5" fill="none">
    <path d="M170,95 Q174,91 178,95"/>
  </g>

  <!-- Ground details - small flowers -->
  <circle cx="145" cy="300" r="3" fill="#FFD700"/>
  <circle cx="255" cy="305" r="3" fill="#FF69B4"/>
  <circle cx="130" cy="315" r="2.5" fill="#FF69B4"/>
  <circle cx="270" cy="310" r="2.5" fill="#FFD700"/>
  <circle cx="340" cy="300" r="3" fill="#EE82EE"/>
  <circle cx="60" cy="308" r="3" fill="#FFD700"/>
</svg>
```