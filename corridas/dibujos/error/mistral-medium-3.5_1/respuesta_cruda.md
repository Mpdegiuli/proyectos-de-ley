<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00ffff;stop-opacity:1" />
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="black"/>
  <g transform="translate(200,200)">
    <circle cx="0" cy="0" r="150" fill="none" stroke="url(#grad1)" stroke-width="15" stroke-dasharray="20,10" filter="url(#glow)"/>
    <path d="M-100,-50 Q-50,-150 0,-50 Q50,-150 100,-50 Q50,50 0,100 Q-50,50 -100,-50" fill="none" stroke="#ff00ff" stroke-width="8" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M-80,30 Q-30,80 30,30 Q80,80 120,30" fill="none" stroke="#00ffff" stroke-width="6" stroke-dasharray="10,5" filter="url(#glow)"/>
    <circle cx="-70" cy="-20" r="15" fill="#ff00ff" filter="url(#glow)"/>
    <circle cx="70" cy="-20" r="15" fill="#00ffff" filter="url(#glow)"/>
    <polygon points="-20,100 20,100 0,150" fill="#ff00ff" opacity="0.7" filter="url(#glow)"/>
    <text x="0" y="180" font-family="Arial" font-size="30" fill="white" text-anchor="middle" filter="url(#glow)">ERROR</text>
  </g>
</svg>