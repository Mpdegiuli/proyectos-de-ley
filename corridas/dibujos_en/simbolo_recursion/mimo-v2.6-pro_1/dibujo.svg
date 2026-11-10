<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="75%">
      <stop offset="0" stop-color="#17293f"/>
      <stop offset="0.6" stop-color="#0c1a2a"/>
      <stop offset="1" stop-color="#060e18"/>
    </radialGradient>
    <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="55" y1="25" x2="355" y2="380">
      <stop offset="0" stop-color="#7ef0e0"/>
      <stop offset="0.33" stop-color="#35c2f0"/>
      <stop offset="0.68" stop-color="#8b8df6"/>
      <stop offset="1" stop-color="#f472b6"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="9"/>
    </filter>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="url(#bg)"/>

  <!-- soft aura -->
  <circle cx="200" cy="200" r="150" fill="#2ee6c8" opacity="0.07" filter="url(#soft)"/>

  <!-- nested self-similar frames -->
  <g fill="none" stroke="url(#g)" stroke-linejoin="round" filter="url(#glow)">
    <rect x="82" y="82" width="236" height="236" rx="26" stroke-width="8" opacity="0.95"/>
    <rect x="117.4" y="117.4" width="165.2" height="165.2" rx="18" stroke-width="6.6" opacity="0.92"/>
    <rect x="142.2" y="142.2" width="115.6" height="115.6" rx="13" stroke-width="5.5" opacity="0.9"/>
    <rect x="159.5" y="159.5" width="81" height="81" rx="9" stroke-width="4.5" opacity="0.88"/>
    <rect x="171.7" y="171.7" width="56.6" height="56.6" rx="6.4" stroke-width="3.8" opacity="0.86"/>
    <rect x="180.2" y="180.2" width="39.6" height="39.6" rx="4.5" stroke-width="3.1" opacity="0.84"/>
    <rect x="186.1" y="186.1" width="27.8" height="27.8" rx="3.2" stroke-width="2.6" opacity="0.82"/>
    <rect x="190.3" y="190.3" width="19.4" height="19.4" rx="2.2" stroke-width="2.1" opacity="0.8"/>
  </g>

  <!-- recursive call arcs entering each smaller copy -->
  <g fill="none" stroke="url(#g)" stroke-linecap="round" filter="url(#glow)">
    <path d="M259 82 C259 26.5 141 26.5 141 82" stroke-width="6.9"/>
    <path d="M241.3 117.4 C241.3 78.6 158.7 78.6 158.7 117.4" stroke-width="5.1"/>
    <path d="M228.9 142.2 C228.9 115 171.1 115 171.1 142.2" stroke-width="3.9"/>
    <path d="M220.2 159.5 C220.2 140.5 179.8 140.5 179.8 159.5" stroke-width="3"/>
    <path d="M214.2 171.7 C214.2 158.4 185.8 158.4 185.8 171.7" stroke-width="2.4"/>
    <path d="M209.9 180.2 C209.9 170.9 190.1 170.9 190.1 180.2" stroke-width="2"/>
  </g>

  <!-- arrow heads -->
  <g fill="url(#g)" filter="url(#glow)">
    <polygon points="141,82 124.5,52.3 157.5,52.3"/>
    <polygon points="158.7,117.4 147.1,96.6 170.3,96.6"/>
    <polygon points="171.1,142.2 163,127.6 179.2,127.6"/>
    <polygon points="179.8,159.5 174.1,149.3 185.5,149.3"/>
    <polygon points="185.8,171.7 181.8,164.6 189.8,164.6"/>
    <polygon points="190.1,180.2 187.3,175.2 192.9,175.2"/>
  </g>

  <!-- base case -->
  <circle cx="200" cy="200" r="17" fill="#fbbf24" opacity="0.16" filter="url(#soft)"/>
  <g filter="url(#glow)">
    <rect x="192" y="192" width="16" height="16" rx="2.5" transform="rotate(45 200 200)" fill="#fcd34d"/>
    <rect x="196.4" y="196.4" width="7.2" height="7.2" rx="1.2" transform="rotate(45 200 200)" fill="#fff6d8"/>
  </g>

  <!-- self-reference loop -->
  <g fill="none" stroke="url(#g)" stroke-linecap="round" opacity="0.85" filter="url(#glow)">
    <path d="M312 116 A172 172 0 1 0 118 40" stroke-width="4.5" stroke-dasharray="26 16"/>
  </g>
  <polygon points="118,40 132,20 92,26" fill="url(#g)" opacity="0.9" filter="url(#glow)"/>
</svg>