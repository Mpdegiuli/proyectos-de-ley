<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#87CEEB"/>
      <stop offset="100%" stop-color="#1E90FF"/>
    </linearGradient>
    <linearGradient id="bridge" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#A0A0A0"/>
      <stop offset="100%" stop-color="#696969"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="5" dy="5" stdDeviation="3" flood-color="rgba(0,0,0,0.5)"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#sky)"/>
  <path d="M0,300 Q100,250 200,280 T400,300 L400,400 L0,400 Z" fill="#228B22"/>
  <path d="M50,280 Q100,200 150,250 Q200,180 250,250 Q300,200 350,280" stroke="url(#bridge)" stroke-width="10" fill="none" filter="url(#shadow)"/>
  <path d="M50,280 L50,200 M150,250 L150,170 M250,250 L250,170 M350,280 L350,200" stroke="url(#bridge)" stroke-width="5"/>
  <circle cx="100" cy="200" r="15" fill="url(#bridge)"/>
  <circle cx="200" cy="180" r="15" fill="url(#bridge)"/>
  <circle cx="300" cy="200" r="15" fill="url(#bridge)"/>
  <path d="M50,200 L350,200" stroke="#D3D3D3" stroke-width="2" stroke-dasharray="5,5"/>
  <rect x="180" y="150" width="40" height="60" fill="url(#bridge)" opacity="0.7"/>
  <path d="M180,150 L200,130 L220,150" fill="url(#bridge)" opacity="0.7"/>
  <circle cx="200" cy="120" r="10" fill="#FFD700"/>
</svg>