<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg-glow" cx="50%" cy="48%" r="60%">
      <stop offset="0%" stop-color="#181d2b"/>
      <stop offset="65%" stop-color="#0f121b"/>
      <stop offset="100%" stop-color="#090b10"/>
    </radialGradient>

    <linearGradient id="grad-light" gradientUnits="userSpaceOnUse" x1="-110" y1="-120" x2="55" y2="50">
      <stop offset="0%" stop-color="#fcf8f0"/>
      <stop offset="55%" stop-color="#ece3d3"/>
      <stop offset="100%" stop-color="#d2c4ae"/>
    </linearGradient>

    <linearGradient id="grad-med" gradientUnits="userSpaceOnUse" x1="-60" y1="-100" x2="165" y2="148">
      <stop offset="0%" stop-color="#70b1b5"/>
      <stop offset="50%" stop-color="#4c888e"/>
      <stop offset="100%" stop-color="#325f66"/>
    </linearGradient>

    <linearGradient id="grad-dark" gradientUnits="userSpaceOnUse" x1="-120" y1="48" x2="140" y2="148">
      <stop offset="0%" stop-color="#3a4e70"/>
      <stop offset="55%" stop-color="#2a3954"/>
      <stop offset="100%" stop-color="#1b263b"/>
    </linearGradient>

    <linearGradient id="grad-leg-light" gradientUnits="userSpaceOnUse" x1="-110" y1="72" x2="-155" y2="148">
      <stop offset="0%" stop-color="#bfb29c"/>
      <stop offset="35%" stop-color="#dfd4c2"/>
      <stop offset="100%" stop-color="#f2eadc"/>
    </linearGradient>

    <linearGradient id="grad-leg-med" gradientUnits="userSpaceOnUse" x1="-80" y1="72" x2="-130" y2="148">
      <stop offset="0%" stop-color="#2d575d"/>
      <stop offset="40%" stop-color="#447c82"/>
      <stop offset="100%" stop-color="#5e9ca1"/>
    </linearGradient>

    <linearGradient id="under-bar-shadow" gradientUnits="userSpaceOnUse" x1="0" y1="72" x2="0" y2="96">
      <stop offset="0%" stop-color="#07090e" stop-opacity="0.72"/>
      <stop offset="100%" stop-color="#07090e" stop-opacity="0"/>
    </linearGradient>

    <radialGradient id="foot-shadow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#040508" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#040508" stop-opacity="0"/>
    </radialGradient>

    <filter id="soft-glow" x="-15%" y="-15%" width="130%" height="130%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg-glow)"/>

  <g stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.75" fill="none">
    <line x1="20" y1="66" x2="380" y2="66"/>
    <line x1="20" y1="210" x2="380" y2="210"/>
    <line x1="20" y1="258" x2="380" y2="258"/>
    <line x1="20" y1="334" x2="380" y2="334"/>
    <line x1="200" y1="20" x2="200" y2="380" stroke-dasharray="3 5"/>
    <line x1="209.2" y1="20" x2="4.9" y2="374"/>
    <line x1="190.8" y1="20" x2="395.1" y2="374"/>
    <circle cx="200" cy="200" r="168" stroke-opacity="0.045" stroke-dasharray="2 6"/>
  </g>

  <g stroke="#d2c4ae" stroke-opacity="0.22" stroke-width="0.8">
    <path d="M28,66 h8 M32,62 v8"/>
    <path d="M364,66 h8 M368,62 v8"/>
    <path d="M28,334 h8 M32,330 v8"/>
    <path d="M364,334 h8 M368,330 v8"/>
  </g>

  <g transform="translate(200, 186)">
    <ellipse cx="-140.9" cy="151" rx="34" ry="6" fill="url(#foot-shadow)"/>
    <ellipse cx="140.9" cy="151" rx="34" ry="6" fill="url(#foot-shadow)"/>

    <g stroke="#0c0f17" stroke-width="0.6" stroke-linejoin="round">
      <polygon points="-124.71,72 -97.00,72 -140.87,148 -168.59,148" fill="url(#grad-leg-light)"/>
      <polygon points="-97.00,72 -69.28,72 -113.16,148 -140.87,148" fill="url(#grad-leg-med)"/>

      <polygon points="-124.71,72 -69.28,72 -83.14,96 -138.56,96" fill="url(#under-bar-shadow)" stroke="none"/>

      <polygon points="-13.86,-120 13.86,-120 -69.28,24 41.57,24 55.43,48 -110.85,48" fill="url(#grad-light)"/>

      <polygon points="-69.28,24 13.86,-120 168.59,148 140.87,148 13.86,-72 -41.57,24" fill="url(#grad-med)"/>

      <polygon points="-110.85,48 55.43,48 0,-48 13.86,-72 140.87,148 113.16,148 69.28,72 -124.71,72" fill="url(#grad-dark)"/>
    </g>

    <g fill="none" stroke-linecap="round">
      <polyline points="-13.86,-120 13.86,-120 -69.28,24" stroke="#ffffff" stroke-opacity="0.45" stroke-width="0.9"/>
      <line x1="-110.85" y1="48" x2="55.43" y2="48" stroke="#ffffff" stroke-opacity="0.28" stroke-width="0.8"/>
      <line x1="13.86" y1="-72" x2="140.87" y2="148" stroke="#9be3e7" stroke-opacity="0.32" stroke-width="0.8"/>
      <line x1="-97.00" y1="72" x2="-140.87" y2="148" stroke="#ffffff" stroke-opacity="0.28" stroke-width="0.8"/>
      <line x1="-124.71" y1="72" x2="69.28" y2="72" stroke="#080a0f" stroke-opacity="0.65" stroke-width="1"/>
    </g>
  </g>
</svg>