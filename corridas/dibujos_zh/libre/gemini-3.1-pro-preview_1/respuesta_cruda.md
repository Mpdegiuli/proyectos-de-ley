<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b001a"/>
      <stop offset="45%" stop-color="#2a0845"/>
      <stop offset="100%" stop-color="#64155f"/>
    </linearGradient>
    
    <linearGradient id="sunGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="40%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#db2777"/>
    </linearGradient>
    
    <radialGradient id="sunGlow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#f97316" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#db2777" stop-opacity="0"/>
    </radialGradient>
    
    <linearGradient id="sunReflect" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="100%" stop-color="#db2777"/>
    </linearGradient>

    <linearGradient id="groundFade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#040010" stop-opacity="1"/>
      <stop offset="30%" stop-color="#040010" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#040010" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="starTrail" x1="1" y1="0" x2="0" y2="1">
       <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
       <stop offset="100%" stop-color="#00f3ff" stop-opacity="0"/>
    </linearGradient>

    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <mask id="sunMask">
      <circle cx="200" cy="220" r="110" fill="#fff"/>
      <rect x="80" y="208" width="240" height="6" fill="#000"/>
      <rect x="80" y="196" width="240" height="5" fill="#000"/>
      <rect x="80" y="186" width="240" height="4" fill="#000"/>
      <rect x="80" y="178" width="240" height="3" fill="#000"/>
      <rect x="80" y="172" width="240" height="2" fill="#000"/>
      <rect x="80" y="167" width="240" height="1" fill="#000"/>
    </mask>

    <clipPath id="skyClip">
      <rect x="0" y="0" width="400" height="220"/>
    </clipPath>

    <path id="frond" d="M0,0 Q25,-30 60,10 Q40,-10 30,5 Q25,-5 20,5 Q15,-5 10,5 Q5,-5 0,0 Z" fill="#030008"/>
    
    <g id="palm">
      <path d="M-5,300 Q15,150 0,0 Q10,150 5,300 Z" fill="#030008"/>
      <use href="#frond" transform="rotate(-20) scale(1.1)"/>
      <use href="#frond" transform="rotate(20) scale(1)"/>
      <use href="#frond" transform="rotate(60) scale(0.9)"/>
      <use href="#frond" transform="rotate(100) scale(0.7)"/>
      <use href="#frond" transform="rotate(140) scale(0.8)"/>
      <use href="#frond" transform="rotate(180) scale(1)"/>
      <use href="#frond" transform="rotate(220) scale(0.9)"/>
      <use href="#frond" transform="rotate(260) scale(0.7)"/>
      <use href="#frond" transform="rotate(300) scale(0.8)"/>
      <use href="#frond" transform="rotate(340) scale(1)"/>
    </g>
  </defs>

  <!-- Sky -->
  <rect x="0" y="0" width="400" height="220" fill="url(#skyGrad)"/>

  <!-- Sun Glow -->
  <circle cx="200" cy="220" r="160" fill="url(#sunGlow)" clip-path="url(#skyClip)"/>

  <!-- Stars -->
  <g fill="#fff" opacity="0.85">
    <path d="M50,40 Q50,45 55,45 Q50,45 50,50 Q50,45 45,45 Q50,45 50,40" filter="url(#glow)"/>
    <path d="M280,30 Q280,35 285,35 Q280,35 280,40 Q280,35 275,35 Q280,35 280,30" transform="translate(10, 20) scale(0.8)" filter="url(#glow)"/>
    <path d="M120,80 Q120,83 123,83 Q120,83 120,86 Q120,83 117,83 Q120,83 120,80" filter="url(#glow)"/>
    <path d="M350,60 Q350,64 354,64 Q350,64 350,68 Q350,64 346,64 Q350,64 350,60" filter="url(#glow)"/>
    
    <circle cx="30" cy="90" r="1.2"/>
    <circle cx="80" cy="20" r="1.5"/>
    <circle cx="150" cy="50" r="0.8"/>
    <circle cx="220" cy="30" r="1.2"/>
    <circle cx="310" cy="110" r="1"/>
    <circle cx="380" cy="40" r="1.5"/>
    <circle cx="260" cy="80" r="0.8"/>
    <circle cx="180" cy="110" r="1"/>
    <circle cx="90" cy="140" r="1.2" opacity="0.5"/>
    <circle cx="320" cy="160" r="1" opacity="0.4"/>
  </g>

  <!-- Shooting Star -->
  <line x1="330" y1="30" x2="260" y2="80" stroke="url(#starTrail)" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>
  <line x1="330" y1="30" x2="260" y2="80" stroke="#fff" stroke-width="0.8" stroke-linecap="round"/>

  <!-- Sun -->
  <g clip-path="url(#skyClip)">
    <circle cx="200" cy="220" r="110" fill="url(#sunGrad)" mask="url(#sunMask)"/>
  </g>

  <!-- Back Mountains -->
  <path d="M-10,220 L50,150 L110,180 L160,130 L220,220 Z" fill="#04000a" stroke="#db2777" stroke-width="1.5" opacity="0.5"/>
  <path d="M410,220 L350,140 L300,160 L240,110 L180,220 Z" fill="#04000a" stroke="#db2777" stroke-width="1.5" opacity="0.5"/>

  <!-- Front Mountains -->
  <g stroke="#db2777" filter="url(#glow)">
    <path d="M-20,220 L30,120 L70,160 L120,90 L180,220 Z" fill="#0b0118" stroke-width="2"/>
    <path d="M30,120 L10,220 M30,120 L50,220
             M70,160 L55,220 M70,160 L85,220
             M120,90 L95,220 M120,90 L145,220" stroke-width="0.8" opacity="0.6"/>
             
    <path d="M420,220 L380,130 L340,160 L290,100 L210,220 Z" fill="#0b0118" stroke-width="2"/>
    <path d="M380,130 L360,220 M380,130 L400,220
             M340,160 L325,220 M340,160 L355,220
             M290,100 L265,220 M290,100 L315,220" stroke-width="0.8" opacity="0.6"/>
  </g>

  <!-- Ground -->
  <rect x="0" y="220" width="400" height="180" fill="#040010"/>

  <!-- Grid -->
  <path d="M200,220 L-400,400
           M200,220 L-250,400
           M200,220 L-100,400
           M200,220 L50,400
           M200,220 L200,400
           M200,220 L350,400
           M200,220 L500,400
           M200,220 L650,400
           M200,220 L800,400
           M0,223 L400,223
           M0,227 L400,227
           M0,233 L400,233
           M0,242 L400,242
           M0,255 L400,255
           M0,274 L400,274
           M0,300 L400,300
           M0,335 L400,335
           M0,380 L400,380"
        stroke="#00f3ff" stroke-width="1.2" fill="none" opacity="0.85" filter="url(#glow)"/>

  <!-- Grid Depth Fade -->
  <rect x="0" y="220" width="400" height="180" fill="url(#groundFade)"/>

  <!-- Sun Reflection on Water/Grid -->
  <polygon points="50,400 350,400 310,220 90,220" fill="url(#sunReflect)" opacity="0.1"/>
  <polygon points="130,400 270,400 250,220 150,220" fill="url(#sunReflect)" opacity="0.2"/>
  <polygon points="180,400 220,400 210,220 190,220" fill="url(#sunReflect)" opacity="0.35"/>

  <!-- Horizon Line -->
  <line x1="0" y1="220" x2="400" y2="220" stroke="#00f3ff" stroke-width="2.5" filter="url(#glow)"/>
  <line x1="0" y1="220" x2="400" y2="220" stroke="#fff" stroke-width="0.8"/>

  <!-- Foreground Silhouettes -->
  <use href="#palm" transform="translate(15, 110) scale(1.15)"/>
  <use href="#palm" transform="translate(385, 95) scale(-1.25, 1.25)"/>
</svg>