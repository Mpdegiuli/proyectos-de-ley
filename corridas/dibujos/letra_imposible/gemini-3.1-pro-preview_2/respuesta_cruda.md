<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="15" stdDeviation="15" flood-color="#000000" flood-opacity="0.8"/>
    </filter>
    <linearGradient id="Cyl1" x1="120" y1="0" x2="160" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ffeb99"/>
      <stop offset="20%" stop-color="#e6b333"/>
      <stop offset="70%" stop-color="#8c5814"/>
      <stop offset="100%" stop-color="#331f00"/>
    </linearGradient>
    <linearGradient id="Cyl2" x1="180" y1="0" x2="220" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ffeb99"/>
      <stop offset="20%" stop-color="#e6b333"/>
      <stop offset="70%" stop-color="#8c5814"/>
      <stop offset="100%" stop-color="#331f00"/>
    </linearGradient>
    <linearGradient id="Cyl3" x1="240" y1="0" x2="280" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ffeb99"/>
      <stop offset="20%" stop-color="#e6b333"/>
      <stop offset="70%" stop-color="#8c5814"/>
      <stop offset="100%" stop-color="#331f00"/>
    </linearGradient>
    <linearGradient id="MaskGradOut" x1="0" y1="120" x2="0" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="white"/>
      <stop offset="35%" stop-color="white"/>
      <stop offset="75%" stop-color="black"/>
      <stop offset="100%" stop-color="black"/>
    </linearGradient>
    <linearGradient id="MaskGradIn" x1="0" y1="120" x2="0" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="black"/>
      <stop offset="35%" stop-color="black"/>
      <stop offset="75%" stop-color="white"/>
      <stop offset="100%" stop-color="white"/>
    </linearGradient>
    <mask id="FadeOutMask">
      <rect x="0" y="0" width="400" height="400" fill="url(#MaskGradOut)"/>
    </mask>
    <mask id="FadeInMask">
      <rect x="0" y="0" width="400" height="400" fill="url(#MaskGradIn)"/>
    </mask>
  </defs>

  <rect width="400" height="400" fill="#0a0e14"/>

  <g stroke-width="1" fill="none">
    <circle cx="200" cy="200" r="160" stroke="#2a3345"/>
    <circle cx="200" cy="200" r="150" stroke="#1f2633" stroke-width="2"/>
    <polygon points="200,20 380,200 200,380 20,200" stroke="#ffeb99" stroke-opacity="0.1"/>
    <line x1="20" y1="60" x2="380" y2="60" stroke="#ffeb99" stroke-opacity="0.1"/>
    <line x1="20" y1="315" x2="380" y2="315" stroke="#ffeb99" stroke-opacity="0.1"/>
  </g>

  <g filter="url(#shadow)">
    <path d="M 180 120 L 180 280 L 165 300 L 165 315 L 235 315 L 235 300 L 220 280 L 220 120 Z" fill="url(#Cyl2)" mask="url(#FadeInMask)"/>
    
    <path d="M 120 120 L 120 280 L 95 300 L 95 315 L 175 315 L 175 300 L 160 280 L 160 120 Z" fill="url(#Cyl1)"/>
    <path d="M 240 120 L 240 280 L 225 300 L 225 315 L 305 315 L 305 300 L 280 280 L 280 120 Z" fill="url(#Cyl3)"/>
    
    <g mask="url(#FadeOutMask)">
      <path d="M 120 120 L 120 280 L 160 280 L 160 120 Z" fill="#e6b333"/>
      <path d="M 160 120 L 160 280 L 180 280 L 180 120 Z" fill="#8c5814"/>
      <path d="M 220 120 L 220 280 L 240 280 L 240 120 Z" fill="#8c5814"/>
      <path d="M 240 120 L 240 280 L 280 280 L 280 120 Z" fill="#e6b333"/>
    </g>

    <path d="M 70 80 L 330 80 L 305 100 L 305 120 L 95 120 L 95 100 Z" fill="#e6b333"/>
    <path d="M 70 80 L 90 60 L 350 60 L 330 80 Z" fill="#ffeb99"/>
    <path d="M 330 80 L 350 60 L 325 80 L 325 100 L 305 120 L 305 100 Z" fill="#8c5814"/>

    <path d="M 200 85 L 215 100 L 200 115 L 185 100 Z" fill="#0a0e14"/>
    <path d="M 185 100 L 200 85 L 205 90 L 190 105 Z" fill="#8c5814"/>
    <path d="M 200 115 L 215 100 L 210 95 L 195 110 Z" fill="#ffeb99"/>
  </g>

  <g stroke="#ffeb99" stroke-width="1.5" stroke-linejoin="round" fill="none" opacity="0.8">
    <path d="M 70 80 L 330 80 L 305 100 L 305 120 L 95 120 L 95 100 Z"/>
    <path d="M 70 80 L 90 60 L 350 60 L 330 80"/>
    <path d="M 330 80 L 350 60 L 325 80 L 325 100 L 305 120 L 305 100"/>
    <path d="M 95 100 L 305 100"/>
    <path d="M 325 80 L 305 100"/>
    
    <path d="M 200 85 L 215 100 L 200 115 L 185 100 Z"/>

    <path d="M 120 280 L 95 300 L 95 315 L 175 315 L 175 300 L 160 280"/>
    <path d="M 180 280 L 165 300 L 165 315 L 235 315 L 235 300 L 220 280" mask="url(#FadeInMask)"/>
    <path d="M 240 280 L 225 300 L 225 315 L 305 315 L 305 300 L 280 280"/>
    <path d="M 95 300 L 175 300"/>
    <path d="M 165 300 L 235 300" mask="url(#FadeInMask)"/>
    <path d="M 225 300 L 305 300"/>

    <g mask="url(#FadeOutMask)">
      <line x1="120" y1="120" x2="120" y2="280"/>
      <line x1="160" y1="120" x2="160" y2="280"/>
      <line x1="180" y1="120" x2="180" y2="280"/>
      <line x1="220" y1="120" x2="220" y2="280"/>
      <line x1="240" y1="120" x2="240" y2="280"/>
      <line x1="280" y1="120" x2="280" y2="280"/>
    </g>

    <g mask="url(#FadeInMask)">
      <line x1="180" y1="120" x2="180" y2="280"/>
      <line x1="220" y1="120" x2="220" y2="280"/>
    </g>
    
    <line x1="120" y1="120" x2="120" y2="280"/>
    <line x1="280" y1="120" x2="280" y2="280"/>
  </g>
</svg>