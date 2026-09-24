<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bgGrad" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0a1024"/>
      <stop offset="100%" stop-color="#010308"/>
    </radialGradient>
    <radialGradient id="coreBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="15%" stop-color="#ffb700"/>
      <stop offset="45%" stop-color="#ff0055"/>
      <stop offset="100%" stop-color="#04000a"/>
    </radialGradient>
    <linearGradient id="metalDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#121a30"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>
    <linearGradient id="metalLight" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1c2745"/>
      <stop offset="100%" stop-color="#2a3b63"/>
    </linearGradient>
    <linearGradient id="cyanMag" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff"/>
      <stop offset="100%" stop-color="#ff0055"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur1"/>
      <feGaussianBlur stdDeviation="8" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#00f0ff" opacity="0.2"/>
      <circle cx="12" cy="12" r="0.5" fill="#ff0055" opacity="0.2"/>
    </pattern>

    <g id="lh">
      <g stroke="#00f0ff" stroke-width="1.5" stroke-dasharray="4 6 2 8" opacity="0.15">
        <line x1="20" y1="0" x2="20" y2="400"/>
        <line x1="45" y1="0" x2="45" y2="400"/>
        <line x1="70" y1="0" x2="70" y2="400"/>
        <line x1="95" y1="0" x2="95" y2="400"/>
      </g>
      
      <path d="M 120 180 C 80 150, 40 100, 10 110" fill="none" stroke="#00f0ff" stroke-width="1" opacity="0.3"/>
      <path d="M 140 220 C 90 230, 50 280, 20 270" fill="none" stroke="#ff0055" stroke-width="1" opacity="0.3"/>
      <path d="M 160 120 C 130 70, 80 40, 30 50" fill="none" stroke="#00f0ff" stroke-width="1.5" stroke-dasharray="2 4" opacity="0.4"/>
      <path d="M 170 300 C 140 330, 90 350, 40 340" fill="none" stroke="#00f0ff" stroke-width="1" opacity="0.3"/>
      <path d="M 110 250 C 70 260, 40 310, 10 330" fill="none" stroke="#ff0055" stroke-width="1.5" stroke-dasharray="1 4" opacity="0.4"/>
      
      <path d="M 201 10 C 130 10, 60 50, 40 140 C 30 220, 60 310, 110 360 C 140 380, 180 395, 201 400 Z" fill="url(#metalDark)" stroke="#004466" stroke-width="1"/>
      
      <path d="M 201 25 L 160 40 L 155 15 L 201 5 Z" fill="#070b19" stroke="#ff0055" stroke-width="1"/>
      <path d="M 201 45 L 175 55 L 170 35 L 201 25 Z" fill="url(#metalLight)"/>
      <path d="M 201 370 L 165 350 L 165 380 L 201 400 Z" fill="#070b19" stroke="#00f0ff" stroke-width="1"/>
      <path d="M 201 350 L 180 340 L 180 370 L 201 385 Z" fill="url(#metalLight)"/>
      
      <path d="M 201 135 L 155 150 L 130 200 L 155 250 L 201 265 Z" fill="#03050a" stroke="#ff0055" stroke-width="1.5"/>
      <path d="M 201 345 L 145 320 L 120 260 L 135 195 L 165 210 L 180 265 L 201 275 Z" fill="url(#metalLight)"/>
      <path d="M 201 30 L 140 45 L 80 110 L 50 200 L 70 290 L 130 350 L 201 370 L 201 350 L 140 330 L 90 270 L 70 200 L 100 120 L 150 60 L 201 50 Z" fill="url(#metalDark)" stroke="#1a2b4c" stroke-width="1"/>
      <path d="M 201 45 L 155 60 L 135 125 L 170 145 L 201 135 Z" fill="url(#metalLight)"/>
      
      <g stroke="#00f0ff" stroke-width="1.5" opacity="0.4">
        <line x1="125" y1="200" x2="165" y2="220"/>
        <line x1="120" y1="210" x2="170" y2="235"/>
        <line x1="115" y1="220" x2="172" y2="250"/>
        <line x1="115" y1="230" x2="168" y2="265"/>
        <line x1="115" y1="240" x2="160" y2="280"/>
        <line x1="115" y1="250" x2="152" y2="295"/>
      </g>
      
      <path d="M 180 35 L 160 55 L 160 100 L 145 115" fill="none" stroke="#ff0055" stroke-width="1.5" opacity="0.8"/>
      <circle cx="145" cy="115" r="2.5" fill="#ff0055" filter="url(#glow)"/>
      <path d="M 201 315 L 170 315 L 150 295 L 150 270" fill="none" stroke="#00f0ff" stroke-width="1.5" opacity="0.8"/>
      <circle cx="150" cy="270" r="2.5" fill="#00f0ff" filter="url(#glow)"/>
      
      <g transform="rotate(-15 170 100)">
        <rect x="160" y="90" width="2" height="15" fill="#ff0055" opacity="0.9"/>
        <rect x="164" y="90" width="1" height="15" fill="#ff0055" opacity="0.9"/>
        <rect x="167" y="90" width="3" height="15" fill="#ff0055" opacity="0.9"/>
        <rect x="172" y="90" width="1" height="15" fill="#ff0055" opacity="0.9"/>
        <rect x="175" y="90" width="4" height="15" fill="#ff0055" opacity="0.9"/>
      </g>
      
      <path d="M 201 80 C 160 80, 140 50, 120 20" fill="none" stroke="#00f0ff" stroke-width="2" opacity="0.7" filter="url(#glow)"/>
      <circle cx="120" cy="20" r="3" fill="#ffffff" filter="url(#glow)"/>
      
      <path d="M 175 220 C 130 240, 80 270, 40 280" fill="none" stroke="url(#cyanMag)" stroke-width="3" filter="url(#glow)" opacity="0.8"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#bgGrad)"/>
  <rect width="400" height="400" fill="url(#dots)"/>

  <use href="#lh"/>
  <use href="#lh" transform="translate(400, 0) scale(-1, 1)"/>

  <g id="center-core">
    <circle cx="200" cy="200" r="65" fill="#00f0ff" opacity="0.1" filter="url(#glow)"/>
    
    <g stroke="#00f0ff" stroke-width="1.5" opacity="0.4">
      <line x1="140" y1="200" x2="260" y2="200"/>
      <line x1="170" y1="148" x2="230" y2="252"/>
      <line x1="170" y1="252" x2="230" y2="148"/>
    </g>
    
    <g fill="none" stroke="#ff0055" stroke-width="2" opacity="0.6">
      <polygon points="200,145 247.6,172.5 247.6,227.5 200,255 152.4,227.5 152.4,172.5"/>
    </g>

    <g fill="none" stroke-width="1.5" stroke="#00f0ff" opacity="0.7">
      <circle cx="200" cy="200" r="100" stroke-dasharray="4 8"/>
      <circle cx="200" cy="200" r="115" stroke-dasharray="30 15 5 15"/>
      <circle cx="200" cy="200" r="130" stroke="#ff0055" stroke-width="1" stroke-dasharray="2 12"/>
    </g>
    
    <g fill="#00f0ff" opacity="0.9">
      <rect x="199" y="60" width="2" height="15"/>
      <rect x="199" y="325" width="2" height="15"/>
      <rect x="60" y="199" width="15" height="2"/>
      <rect x="325" y="199" width="15" height="2"/>
    </g>

    <circle cx="200" cy="200" r="48" fill="url(#coreBg)"/>
    
    <circle cx="200" cy="200" r="42" stroke="#ffffff" stroke-width="1" stroke-dasharray="2 5" fill="none" opacity="0.8"/>
    <circle cx="200" cy="200" r="32" fill="none" stroke="#ffb700" stroke-width="2.5" stroke-dasharray="12 6"/>
    <circle cx="200" cy="200" r="22" fill="none" stroke="#ffffff" stroke-width="1.5" opacity="0.5"/>
    
    <path d="M 200 172 L 212 188 L 228 188 L 216 204 L 222 220 L 200 214 L 178 220 L 184 204 L 172 188 L 188 188 Z" fill="none" stroke="#00f0ff" stroke-width="2" filter="url(#glow)"/>
    
    <circle cx="200" cy="200" r="9" fill="#00f0ff" filter="url(#glow)"/>
    <circle cx="200" cy="200" r="4" fill="#ffffff"/>
    
    <polygon points="200,120 215,140 185,140" fill="none" stroke="#00f0ff" stroke-width="1.5" opacity="0.8" filter="url(#glow)"/>
    <polygon points="200,280 215,260 185,260" fill="none" stroke="#00f0ff" stroke-width="1.5" opacity="0.8" filter="url(#glow)"/>
  </g>
</svg>