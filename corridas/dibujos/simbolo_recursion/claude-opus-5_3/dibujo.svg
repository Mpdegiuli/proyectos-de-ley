<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#1b2234"/>
      <stop offset="100%" stop-color="#0b0e16"/>
    </radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="url(#bg)"/>

  <!-- outer loop arrow: the call returning into itself -->
  <g filter="url(#glow)">
    <path d="M 200 14 A 186 186 0 1 1 14 200"
          fill="none" stroke="#36e0b0" stroke-width="7" stroke-linecap="round"/>
    <polygon points="14,168 32,202 -4,202" fill="#36e0b0"/>
  </g>

  <!-- nested self-similar frames: each level contains a smaller copy -->
  <g fill="none" stroke-linejoin="round" filter="url(#glow)">
    <rect x="75" y="75" width="250" height="250" rx="14" stroke="#4fd1e8" stroke-width="5.5" transform="rotate(0 200 200)"/>
    <rect x="115" y="115" width="170" height="170" rx="11" stroke="#6ec3f0" stroke-width="5" transform="rotate(18 200 200)"/>
    <rect x="142.2" y="142.2" width="115.6" height="115.6" rx="9" stroke="#8cb4f3" stroke-width="4.3" transform="rotate(36 200 200)"/>
    <rect x="160.7" y="160.7" width="78.6" height="78.6" rx="7" stroke="#a9a4f4" stroke-width="3.6" transform="rotate(54 200 200)"/>
    <rect x="173.3" y="173.3" width="53.4" height="53.4" rx="5" stroke="#c295ef" stroke-width="3" transform="rotate(72 200 200)"/>
    <rect x="181.8" y="181.8" width="36.4" height="36.4" rx="4" stroke="#d887e3" stroke-width="2.4" transform="rotate(90 200 200)"/>
    <rect x="187.6" y="187.6" width="24.8" height="24.8" rx="3" stroke="#ec7ad2" stroke-width="2" transform="rotate(108 200 200)"/>
  </g>

  <!-- base case at the heart of the nesting -->
  <circle cx="200" cy="200" r="7" fill="#ffd166" filter="url(#glow)"/>

  <!-- chevrons: descent toward the base case -->
  <g fill="none" stroke="#ffd166" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.95">
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(200,56) rotate(90)"/>
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(200,80) rotate(90)"/>
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(344,200) rotate(180)"/>
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(320,200) rotate(180)"/>
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(200,344) rotate(270)"/>
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(200,320) rotate(270)"/>
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(56,200) rotate(0)"/>
    <path d="M -9 -11 L 2 0 L -9 11" transform="translate(80,200) rotate(0)"/>
  </g>
</svg>