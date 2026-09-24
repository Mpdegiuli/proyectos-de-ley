```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b0f2b"/>
      <stop offset="45%" stop-color="#1a2456"/>
      <stop offset="75%" stop-color="#4a3a6b"/>
      <stop offset="100%" stop-color="#8a5a7a"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a2456"/>
      <stop offset="100%" stop-color="#0b0f2b"/>
    </linearGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff9e6" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#fff9e6" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#fff9e6" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="mountainFar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3a3568"/>
      <stop offset="100%" stop-color="#2a2456"/>
    </linearGradient>
    <linearGradient id="mountainNear" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1f1a40"/>
      <stop offset="100%" stop-color="#141030"/>
    </linearGradient>
  </defs>

  <!-- Sky -->
  <rect x="0" y="0" width="400" height="240" fill="url(#sky)"/>

  <!-- Stars -->
  <g fill="#ffffff">
    <circle cx="30" cy="30" r="1.2" opacity="0.9"/>
    <circle cx="70" cy="60" r="0.8" opacity="0.7"/>
    <circle cx="110" cy="25" r="1" opacity="0.8"/>
    <circle cx="150" cy="50" r="0.7" opacity="0.6"/>
    <circle cx="190" cy="15" r="1.3" opacity="0.9"/>
    <circle cx="230" cy="45" r="0.9" opacity="0.7"/>
    <circle cx="260" cy="20" r="1" opacity="0.8"/>
    <circle cx="20" cy="90" r="0.9" opacity="0.6"/>
    <circle cx="60" cy="110" r="1.1" opacity="0.8"/>
    <circle cx="130" cy="90" r="0.7" opacity="0.5"/>
    <circle cx="170" cy="100" r="1" opacity="0.7"/>
    <circle cx="340" cy="40" r="1.2" opacity="0.9"/>
    <circle cx="370" cy="70" r="0.8" opacity="0.6"/>
    <circle cx="310" cy="90" r="1" opacity="0.7"/>
    <circle cx="380" cy="110" r="0.9" opacity="0.6"/>
    <circle cx="290" cy="130" r="0.7" opacity="0.5"/>
    <circle cx="15" cy="150" r="0.8" opacity="0.6"/>
    <circle cx="220" cy="130" r="0.6" opacity="0.5"/>
    <circle cx="250" cy="150" r="0.9" opacity="0.6"/>
    <circle cx="100" cy="140" r="0.6" opacity="0.5"/>
  </g>

  <!-- Moon glow -->
  <circle cx="290" cy="80" r="70" fill="url(#moonGlow)"/>
  <!-- Moon -->
  <circle cx="290" cy="80" r="32" fill="#fdf6e3"/>
  <circle cx="278" cy="68" r="5" fill="#e8dcc0" opacity="0.5"/>
  <circle cx="300" cy="90" r="7" fill="#e8dcc0" opacity="0.4"/>
  <circle cx="295" cy="65" r="3" fill="#e8dcc0" opacity="0.4"/>

  <!-- Far mountains -->
  <path d="M0,180 L40,140 L80,170 L120,120 L160,165 L200,130 L240,170 L280,145 L320,175 L360,150 L400,175 L400,240 L0,240 Z" fill="url(#mountainFar)" opacity="0.85"/>

  <!-- Near mountains -->
  <path d="M0,220 L50,160 L90,200 L140,150 L190,205 L230,170 L280,210 L330,165 L370,200 L400,190 L400,240 L0,240 Z" fill="url(#mountainNear)"/>

  <!-- Water -->
  <rect x="0" y="240" width="400" height="160" fill="url(#water)"/>

  <!-- Moon reflection -->
  <ellipse cx="290" cy="260" rx="18" ry="6" fill="#fdf6e3" opacity="0.5"/>
  <ellipse cx="290" cy="275" rx="24" ry="5" fill="#fdf6e3" opacity="0.35"/>
  <ellipse cx="290" cy="292" rx="14" ry="4" fill="#fdf6e3" opacity="0.25"/>
  <ellipse cx="290" cy="308" rx="30" ry="4" fill="#fdf6e3" opacity="0.15"/>

  <!-- Mountain reflections -->
  <path d="M0,260 L50,320 L90,280 L140,330 L190,275 L230,310 L280,270 L330,315 L370,280 L400,290 L400,240 L0,240 Z" fill="#1a1638" opacity="0.5"/>

  <!-- Water ripples -->
  <g stroke="#5a4a7a" stroke-width="1" opacity="0.3" fill="none">
    <path d="M20,260 q15,4 30,0 q15,-4 30,0"/>
    <path d="M120,270 q15,4 30,0 q15,-4 30,0"/>
    <path d="M60,300 q20,5 40,0 q20,-5 40,0"/>
    <path d="M200,290 q18,4 36,0 q18,-4 36,0"/>
    <path d="M10,340 q22,5 44,0 q22,-5 44,0"/>
    <path d="M150,350 q20,5 40,0 q20,-5 40,0"/>
    <path d="M240,330 q16,4 32,0 q16,-4 32,0"/>
    <path d="M320,300 q15,4 30,0"/>
    <path d="M40,380 q25,5 50,0 q25,-5 50,0"/>
    <path d="M180,370 q22,5 44,0"/>
    <path d="M280,360 q20,4 40,0"/>
  </g>

  <!-- Small boat silhouette -->
  <g transform="translate(90,248)">
    <path d="M-15,3 Q0,10 15,3 L11,7 Q0,11 -11,7 Z" fill="#0a0818"/>
    <line x1="0" y1="3" x2="0" y2="-14" stroke="#0a0818" stroke-width="1"/>
    <path d="M0,-14 L10,-4 L0,-2 Z" fill="#0a0818"/>
  </g>

  <!-- Birds -->
  <g stroke="#0a0818" stroke-width="1.3" fill="none" opacity="0.8">
    <path d="M150,60 q6,-6 12,0 q6,-6 12,0"/>
    <path d="M170,75 q5,-5 10,0 q5,-5 10,0"/>
    <path d="M130,50 q4,-4 8,0 q4,-4 8,0"/>
  </g>
</svg>