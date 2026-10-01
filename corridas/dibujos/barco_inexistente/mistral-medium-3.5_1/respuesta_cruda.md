<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4a6baf;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1a2a5e;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="grad2" cx="50%" cy="50%" r="50%" fx="30%" fy="30%">
      <stop offset="0%" style="stop-color:#a0d2eb;stop-opacity:0.8" />
      <stop offset="100%" style="stop-color:#4a6baf;stop-opacity:0.2" />
    </radialGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Agua -->
  <rect width="400" height="400" fill="url(#grad1)" />

  <!-- Sol -->
  <circle cx="350" cy="50" r="30" fill="#f5d76e" filter="url(#glow)" />
  <circle cx="350" cy="50" r="20" fill="#f7dc6f" />

  <!-- Nubes -->
  <path d="M50,80 Q80,60 110,80 Q140,60 170,80 Q200,60 230,80 Q260,60 290,80" fill="white" opacity="0.7" />
  <path d="M100,120 Q130,100 160,120 Q190,100 220,120 Q250,100 280,120" fill="white" opacity="0.5" />

  <!-- Barco -->
  <g transform="translate(150, 200)">
    <!-- Casco -->
    <path d="M-80,0 Q-60,-40 0,-50 Q60,-40 80,0 L40,0 Q20,-20 0,-30 Q-20,-20 -40,0 Z" fill="#5d4037" stroke="#3e2723" stroke-width="2" />
    <path d="M-80,0 L-100,-20 L-100,20 Z" fill="#5d4037" stroke="#3e2723" stroke-width="2" />
    <path d="M80,0 L100,-20 L100,20 Z" fill="#5d4037" stroke="#3e2723" stroke-width="2" />

    <!-- Velas -->
    <path d="M-30,-50 L-30,-120 L0,-100 Z" fill="url(#grad2)" stroke="#1a2a5e" stroke-width="1" />
    <path d="M30,-50 L30,-120 L0,-100 Z" fill="url(#grad2)" stroke="#1a2a5e" stroke-width="1" />
    <path d="M0,-50 L0,-140 L-20,-120 L20,-120 Z" fill="url(#grad2)" stroke="#1a2a5e" stroke-width="1" />

    <!-- Mastiles -->
    <line x1="0" y1="-50" x2="0" y2="-140" stroke="#3e2723" stroke-width="4" />
    <line x1="-30" y1="-50" x2="-30" y2="-120" stroke="#3e2723" stroke-width="3" />
    <line x1="30" y1="-50" x2="30" y2="-120" stroke="#3e2723" stroke-width="3" />

    <!-- Detalles -->
    <circle cx="0" cy="-50" r="5" fill="#3e2723" />
    <rect x="-15" y="-10" width="30" height="10" rx="2" fill="#8d6e63" />
    <circle cx="-40" cy="0" r="3" fill="#ffd700" />
    <circle cx="40" cy="0" r="3" fill="#ffd700" />

    <!-- Bandera -->
    <path d="M0,-140 L-15,-160 L0,-150 L15,-160 Z" fill="#e53935" />
    <circle cx="0" cy="-155" r="2" fill="#ffd700" />
  </g>

  <!-- Olas -->
  <path d="M0,250 Q50,240 100,250 T200,250 T300,250 T400,250 L400,400 L0,400 Z" fill="rgba(255,255,255,0.3)" />
  <path d="M0,280 Q70,270 140,280 T280,280 T400,280 L400,400 L0,400 Z" fill="rgba(255,255,255,0.2)" />
</svg>