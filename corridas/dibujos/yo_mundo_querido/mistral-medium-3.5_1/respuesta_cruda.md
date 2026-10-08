<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#87CEEB" />
      <stop offset="100%" stop-color="#1E90FF" />
    </linearGradient>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" stop-color="#FFD700" />
      <stop offset="100%" stop-color="#FFA500" />
    </radialGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#sky)" />
  <circle cx="350" cy="80" r="40" fill="url(#sun)" filter="url(#glow)" />
  <path d="M0,300 Q100,250 200,300 T400,300 L400,400 L0,400 Z" fill="#228B22" />
  <path d="M50,300 Q150,200 250,300 Q350,250 400,300" stroke="#32CD32" stroke-width="3" fill="none" />
  <circle cx="200" cy="200" r="30" fill="#FF6347" />
  <path d="M200,170 Q230,180 200,200 Q170,180 200,170" fill="#FF6347" />
  <circle cx="185" cy="190" r="3" fill="#000" />
  <circle cx="215" cy="190" r="3" fill="#000" />
  <path d="M190,210 Q200,220 210,210" stroke="#000" stroke-width="2" fill="none" />
  <rect x="180" y="230" width="40" height="80" rx="10" fill="#4169E1" />
  <rect x="170" y="240" width="20" height="60" rx="5" fill="#4169E1" />
  <rect x="210" y="240" width="20" height="60" rx="5" fill="#4169E1" />
  <circle cx="150" cy="100" r="20" fill="#FF69B4" />
  <circle cx="250" cy="100" r="20" fill="#FF69B4" />
  <path d="M150,80 Q170,60 200,80 Q230,60 250,80" stroke="#FF69B4" stroke-width="3" fill="none" />
  <circle cx="100" cy="350" r="15" fill="#FFD700" />
  <circle cx="300" cy="350" r="15" fill="#FFD700" />
</svg>