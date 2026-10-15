<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%" style="background-color: #040508;">
  <defs>
    <radialGradient id="bg-grad" cx="40%" cy="50%" r="80%">
      <stop offset="0%" stop-color="#040508" />
      <stop offset="50%" stop-color="#080b15" />
      <stop offset="100%" stop-color="#1c0512" />
    </radialGradient>

    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.15"/>
      <circle cx="0" cy="0" r="1" fill="#ffffff" opacity="0.3"/>
    </pattern>

    <linearGradient id="grad-out" x1="0" y1="0" x2="1" y2="0">
      <stop offset="25%" stop-color="#ffffff" />
      <stop offset="65%" stop-color="#000000" />
    </linearGradient>
    <mask id="fade-out">
      <rect width="400" height="400" fill="url(#grad-out)" />
    </mask>

    <linearGradient id="grad-in" x1="0" y1="0" x2="1" y2="0">
      <stop offset="35%" stop-color="#000000" />
      <stop offset="65%" stop-color="#ffffff" />
    </linearGradient>
    <mask id="fade-in">
      <rect width="400" height="400" fill="url(#grad-in)" />
    </mask>

    <filter id="beautiful-error" x="-50%" y="-50%" width="200%" height="200%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="3" seed="42" result="noise" />
      
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="180" xChannelSelector="R" yChannelSelector="G" result="dispR" />
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="260" xChannelSelector="B" yChannelSelector="R" result="dispG" />
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="350" xChannelSelector="G" yChannelSelector="B" result="dispB" />
      
      <feColorMatrix in="dispR" type="matrix" values="
        1 0 0 0 0  
        0 0 0 0 0  
        0 0 0 0 0  
        0 0 0 1 0" result="red_channel" />
        
      <feColorMatrix in="dispG" type="matrix" values="
        0 0 0 0 0  
        0 1 0 0 0  
        0 0 0 0 0  
        0 0 0 1 0" result="green_channel" />
        
      <feColorMatrix in="dispB" type="matrix" values="
        0 0 0 0 0  
        0 0 0 0 0  
        0 0 1 0 0  
        0 0 0 1 0" result="blue_channel" />
      
      <feBlend mode="screen" in="red_channel" in2="green_channel" result="rg" />
      <feBlend mode="screen" in="rg" in2="blue_channel" result="rgb" />
      
      <feColorMatrix in="rgb" type="matrix" values="
        1.6 0 0 0 0  
        0 1.6 0 0 0  
        0 0 1.6 0 0  
        0 0 0 1.2 0" result="boosted" />
      
      <feGaussianBlur in="boosted" stdDeviation="3" result="glow" />
      <feBlend mode="screen" in="boosted" in2="glow" />
    </filter>

    <g id="pristine-system">
      <rect x="-200" y="-200" width="800" height="800" fill="url(#grid)" />
      
      <circle cx="200" cy="200" r="160" fill="none" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="1 4" opacity="0.3"/>
      <circle cx="200" cy="200" r="140" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.4"/>
      <circle cx="200" cy="200" r="130" fill="none" stroke="#ffffff" stroke-width="1" stroke-dasharray="2 6"/>
      <circle cx="200" cy="200" r="100" fill="none" stroke="#ffffff" stroke-width="3"/>
      <circle cx="200" cy="200" r="90" fill="none" stroke="#ffffff" stroke-width="1" stroke-dasharray="10 5"/>
      <circle cx="200" cy="200" r="85" fill="none" stroke="#ffffff" stroke-width="1" stroke-dasharray="1 3"/>
      <circle cx="200" cy="200" r="60" fill="none" stroke="#ffffff" stroke-width="0.5"/>
      
      <polygon points="200,100 286.6,250 113.4,250" fill="none" stroke="#ffffff" stroke-width="1.5" />
      <polygon points="200,300 113.4,150 286.6,150" fill="none" stroke="#ffffff" stroke-width="1.5" opacity="0.4"/>
      <rect x="150" y="150" width="100" height="100" fill="none" stroke="#ffffff" stroke-width="0.5" transform="rotate(45, 200, 200)" opacity="0.5"/>
      
      <circle cx="200" cy="200" r="15" fill="none" stroke="#ffffff" stroke-width="2"/>
      <circle cx="200" cy="200" r="4" fill="#ffffff" />
      <circle cx="200" cy="60" r="3" fill="#ffffff" />
      <circle cx="200" cy="340" r="3" fill="#ffffff" />
      <circle cx="60" cy="200" r="3" fill="#ffffff" />
      <circle cx="340" cy="200" r="3" fill="#ffffff" />
      
      <line x1="200" y1="0" x2="200" y2="400" stroke="#ffffff" stroke-width="1" opacity="0.4"/>
      <line x1="0" y1="200" x2="400" y2="200" stroke="#ffffff" stroke-width="1" opacity="0.4"/>
      <line x1="58.6" y1="58.6" x2="341.4" y2="341.4" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
      <line x1="341.4" y1="58.6" x2="58.6" y2="341.4" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
      
      <text x="25" y="35" fill="#ffffff" font-family="monospace" font-size="10" opacity="0.8">SYS_STATE: OPTIMAL</text>
      <text x="25" y="50" fill="#ffffff" font-family="monospace" font-size="10" opacity="0.8">SYNC_RATE: 100%</text>
      
      <text x="375" y="35" fill="#ffffff" font-family="monospace" font-size="10" text-anchor="end" opacity="0.8">MEM: 0x00A0</text>
      <text x="375" y="50" fill="#ffffff" font-family="monospace" font-size="10" text-anchor="end" opacity="0.8">BUFFER: SECURE</text>

      <text x="200" y="225" fill="#ffffff" font-family="monospace" font-size="12" text-anchor="middle" letter-spacing="3" opacity="0.9">CORE_ON</text>

      <g transform="translate(250, 180)">
         <rect x="0" y="0" width="125" height="20" fill="#ff003c" />
         <text x="62.5" y="14" fill="#ffffff" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">CORRUPTION_DET</text>
      </g>
      <g transform="translate(260, 210)">
         <rect x="0" y="0" width="105" height="15" fill="#ffffff" />
         <text x="52.5" y="11" fill="#ff003c" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">OVERFLOW_ERR</text>
      </g>

      <rect x="25" y="360" width="350" height="6" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.5"/>
      <rect x="25" y="360" width="220" height="6" fill="#ffffff" />
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#bg-grad)" />

  <g mask="url(#fade-out)">
    <use href="#pristine-system" />
  </g>

  <g filter="url(#beautiful-error)">
    <g mask="url(#fade-in)">
      <use href="#pristine-system" />
    </g>
  </g>
  
  <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="4" y2="0" stroke="#000000" stroke-width="1" opacity="0.4"/>
  </pattern>
  <rect width="400" height="400" fill="url(#scanlines)" style="mix-blend-mode: overlay; pointer-events: none;" />
</svg>