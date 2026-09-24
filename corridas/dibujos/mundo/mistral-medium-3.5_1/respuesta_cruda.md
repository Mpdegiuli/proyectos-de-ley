<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a2a6c"/>
      <stop offset="100%" stop-color="#b21f1f"/>
    </linearGradient>
    <filter id="blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="200" cy="200" r="100" fill="none" stroke="#f5af19" stroke-width="8" stroke-dasharray="15,10" filter="url(#blur)"/>
  <g transform="translate(200,200)">
    <path d="M-50,-30 L-30,-50 L0,-40 L30,-50 L50,-30 L40,0 L50,30 L30,50 L0,40 L-30,50 L-50,30 Z" fill="#3a7d44" opacity="0.7"/>
    <circle cx="0" cy="0" r="20" fill="#e74c3c"/>
    <rect x="-10" y="-5" width="20" height="10" fill="#2c3e50"/>
    <line x1="-40" y1="0" x2="40" y2="0" stroke="#ecf0f1" stroke-width="2"/>
    <line x1="0" y1="-40" x2="0" y2="40" stroke="#ecf0f1" stroke-width="2"/>
  </g>
  <rect x="50" y="300" width="300" height="50" fill="#2c3e50" rx="5"/>
  <rect x="100" y="250" width="50" height="50" fill="#e74c3c" rx="3"/>
  <rect x="200" y="250" width="50" height="50" fill="#3498db" rx="3"/>
  <rect x="300" y="250" width="50" height="50" fill="#2ecc71" rx="3"/>
  <path d="M100,300 Q200,280 300,300" stroke="#ecf0f1" stroke-width="3" fill="none"/>
  <circle cx="150" cy="100" r="15" fill="#f1c40f"/>
  <circle cx="250" cy="100" r="15" fill="#f1c40f"/>
  <path d="M150,100 Q200,80 250,100" stroke="#f39c12" stroke-width="2" fill="none"/>
</svg>