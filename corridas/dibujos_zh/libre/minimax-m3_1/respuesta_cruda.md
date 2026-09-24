<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2d1b4e"/>
      <stop offset="25%" stop-color="#7a2c5f"/>
      <stop offset="55%" stop-color="#ff5e5b"/>
      <stop offset="80%" stop-color="#ffb84d"/>
      <stop offset="100%" stop-color="#ffd98a"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ff5e5b"/>
      <stop offset="35%" stop-color="#7a3b4f"/>
      <stop offset="100%" stop-color="#0a0515"/>
    </linearGradient>
    <radialGradient id="sunGlow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#fff5d6"/>
      <stop offset="35%" stop-color="#ffd700" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ff5e5b" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="moonGlow">
      <stop offset="0%" stop-color="#fff5d6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#fff5d6" stop-opacity="0"/>
    </radialGradient>
  </defs>
  
  <rect width="400" height="225" fill="url(#sky)"/>
  
  <circle cx="200" cy="175" r="95" fill="url(#sunGlow)"/>
  <circle cx="200" cy="175" r="38" fill="#fff5d6"/>
  
  <circle cx="340" cy="55" r="22" fill="url(#moonGlow)"/>
  <circle cx="340" cy="55" r="14" fill="#f5e6c8"/>
  
  <g fill="#fff5d6">
    <circle cx="50" cy="40" r="1.2"/>
    <circle cx="90" cy="25" r="1"/>
    <circle cx="140" cy="60" r="1.5"/>
    <circle cx="180" cy="30" r="1"/>
    <circle cx="250" cy="45" r="1.3"/>
    <circle cx="280" cy="80" r="1"/>
    <circle cx="370" cy="30" r="1.2"/>
    <circle cx="380" cy="100" r="1"/>
    <circle cx="20" cy="120" r="0.8"/>
    <circle cx="60" cy="150" r="0.8"/>
  </g>
  
  <polygon points="0,225 50,150 100,210 160,120 215,200 270,135 330,205 400,150 400,225" fill="#5a3d5c" opacity="0.6"/>
  
  <polygon points="0,225 35,180 90,220 145,160 200,225 255,170 310,225 365,190 400,210 400,225" fill="#3d2548"/>
  
  <rect y="225" width="400" height="175" fill="url(#water)"/>
  
  <ellipse cx="200" cy="255" rx="45" ry="3" fill="#fff5d6" opacity="0.8"/>
  <ellipse cx="200" cy="275" rx="38" ry="3" fill="#fff5d6" opacity="0.6"/>
  <ellipse cx="200" cy="295" rx="32" ry="3" fill="#fff5d6" opacity="0.45"/>
  <ellipse cx="200" cy="315" rx="25" ry="3" fill="#fff5d6" opacity="0.3"/>
  <ellipse cx="200" cy="335" rx="18" ry="3" fill="#fff5d6" opacity="0.2"/>
  
  <g stroke="#fff5d6" stroke-width="0.8" fill="none" opacity="0.4">
    <line x1="30" y1="265" x2="100" y2="265"/>
    <line x1="290" y1="280" x2="370" y2="280"/>
    <line x1="20" y1="310" x2="90" y2="310"/>
    <line x1="310" y1="330" x2="380" y2="330"/>
    <line x1="50" y1="355" x2="130" y2="355"/>
    <line x1="260" y1="370" x2="340" y2="370"/>
  </g>
  
  <g fill="#fff5d6" opacity="0.7">
    <path d="M 150,250 L 160,255 L 150,260 Z"/>
    <polygon points="160,253 175,250 175,253 168,257 175,261 175,264 160,261"/>
  </g>
  
  <g stroke="#1a0a2e" stroke-width="2" fill="none">
    <path d="M 65,85 Q 70,80 75,85 Q 80,80 85,85"/>
    <path d="M 115,65 Q 120,60 125,65 Q 130,60 135,65"/>
    <path d="M 285,55 Q 290,50 295,55 Q 300,50 305,55"/>
    <path d="M 80,110 Q 84,106 88,110 Q 92,106 96,110"/>
  </g>
  
  <ellipse cx="280" cy="340" rx="3" ry="1" fill="#fff5d6" opacity="0.5"/>
  <ellipse cx="320" cy="355" rx="2" ry="0.8" fill="#fff5d6" opacity="0.4"/>
  <ellipse cx="60" cy="345" rx="2.5" ry="1" fill="#fff5d6" opacity="0.4"/>
  
  <g fill="#0a0515">
    <rect x="25" y="280" width="5" height="45"/>
    <polygon points="27.5,245 13,285 42,285"/>
    <polygon points="27.5,260 17,285 38,285"/>
    
    <rect x="55" y="295" width="4" height="30"/>
    <polygon points="57,268 45,300 69,300"/>
    
    <rect x="350" y="285" width="5" height="40"/>
    <polygon points="352.5,250 338,290 367,290"/>
    <polygon points="352.5,265 342,290 363,290"/>
    
    <rect x="375" y="295" width="4" height="30"/>
    <polygon points="377,270 365,300 389,300"/>
  </g>
</svg>