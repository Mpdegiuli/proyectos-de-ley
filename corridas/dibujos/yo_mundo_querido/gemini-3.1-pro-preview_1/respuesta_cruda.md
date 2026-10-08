<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#020111"/>
      <stop offset="40%" stop-color="#110a2f"/>
      <stop offset="70%" stop-color="#003344"/>
      <stop offset="100%" stop-color="#00cca3"/>
    </linearGradient>
    <linearGradient id="earth" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#002222"/>
      <stop offset="100%" stop-color="#004d2b"/>
    </linearGradient>
    <radialGradient id="aura" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0ff" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#08f" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#00f" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="upFlow" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#0ff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#f0f" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="downFlow" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0ff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0f5" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <rect width="20" height="20" fill="none" stroke="rgba(0, 255, 255, 0.05)" stroke-width="0.5"/>
    </pattern>
  </defs>

  <rect width="400" height="250" fill="url(#sky)"/>
  <rect width="400" height="250" fill="url(#grid)"/>

  <g stroke="rgba(0, 255, 255, 0.2)" stroke-width="0.5">
    <path d="M20,30 L60,60 L110,40 L160,80 L220,50 L280,70 L340,30 L380,80"/>
    <path d="M60,60 L90,110 L160,80"/>
    <path d="M220,50 L250,120 L280,70"/>
    <path d="M20,130 L90,110 L150,150 L200,120 L250,150 L320,100 L380,140"/>
    <path d="M110,40 L140,15 L200,30"/>
    <path d="M280,70 L310,120 L380,80"/>
  </g>
  
  <g fill="#fff" opacity="0.8">
    <circle cx="20" cy="30" r="1"/><circle cx="60" cy="60" r="1.5"/><circle cx="110" cy="40" r="1"/>
    <circle cx="160" cy="80" r="1.5"/><circle cx="220" cy="50" r="1"/><circle cx="280" cy="70" r="1.5"/>
    <circle cx="340" cy="30" r="1"/><circle cx="380" cy="80" r="1.5"/><circle cx="90" cy="110" r="1"/>
    <circle cx="250" cy="120" r="1.5"/><circle cx="20" cy="130" r="1"/><circle cx="150" cy="150" r="1.5"/>
    <circle cx="200" cy="120" r="1"/><circle cx="250" cy="150" r="1"/><circle cx="320" cy="100" r="1.5"/>
    <circle cx="380" cy="140" r="1"/><circle cx="140" cy="15" r="1"/><circle cx="200" cy="30" r="1.5"/>
    <circle cx="310" cy="120" r="1"/>
  </g>

  <path d="M0,230 C150,210 250,260 400,220 L400,400 L0,400 Z" fill="url(#earth)"/>
  <path d="M0,260 C120,240 280,290 400,250 L400,400 L0,400 Z" fill="#001a1a" opacity="0.8"/>
  <path d="M0,300 C180,270 220,330 400,290 L400,400 L0,400 Z" fill="#000d0d" opacity="0.9"/>
  
  <g stroke="rgba(0, 255, 150, 0.15)" stroke-width="1" fill="none">
    <path d="M0,320 Q100,310 200,350 T400,330"/>
    <path d="M0,360 Q150,330 250,370 T400,380"/>
    <path d="M50,400 Q150,360 300,400"/>
  </g>

  <g fill="none" stroke="url(#upFlow)" stroke-width="1.5">
    <path d="M200,210 C180,120 130,80 50,40"/>
    <path d="M200,210 C190,130 160,90 100,50"/>
    <path d="M200,210 C200,120 200,60 200,10"/>
    <path d="M200,210 C210,130 240,90 300,50"/>
    <path d="M200,210 C220,120 270,80 350,40"/>
  </g>
  
  <g fill="none" stroke="url(#downFlow)" stroke-width="1.5">
    <path d="M200,210