<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="v" cx="50%" cy="50%" r="85%">
      <stop offset="0%" stop-color="#030303"/>
      <stop offset="60%" stop-color="#000"/>
      <stop offset="100%" stop-color="#010101"/>
    </radialGradient>
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7"/>
      <feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.05 0"/>
    </filter>
    <filter id="soft">
      <feGaussianBlur stdDeviation="0.4"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="#000"/>
  <rect width="400" height="400" fill="url(#v)"/>
  <rect width="400" height="400" filter="url(#grain)"/>
  <g fill="none" stroke="#ffffff" filter="url(#soft)">
    <circle cx="200" cy="200" r="199" stroke-width="0.25" opacity="0.06"/>
    <circle cx="200" cy="200" r="150" stroke-width="0.2" opacity="0.05"/>
    <circle cx="200" cy="200" r="100" stroke-width="0.2" opacity="0.04"/>
    <circle cx="200" cy="200" r="55" stroke-width="0.15" opacity="0.03"/>
    <circle cx="200" cy="200" r="20" stroke-width="0.15" opacity="0.03"/>
  </g>
  <circle cx="200" cy="200" r="0.6" fill="#ffffff" opacity="0.35"/>
</svg>