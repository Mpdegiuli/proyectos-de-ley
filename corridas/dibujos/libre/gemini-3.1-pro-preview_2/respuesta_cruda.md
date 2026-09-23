<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#050014"/>
      <stop offset="35%" stop-color="#14022e"/>
      <stop offset="70%" stop-color="#4a044e"/>
      <stop offset="100%" stop-color="#8a0054"/>
    </linearGradient>

    <linearGradient id="sun" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff566"/>
      <stop offset="35%" stop-color="#ff9900"/>
      <stop offset="75%" stop-color="#ff0055"/>
      <stop offset="100%" stop-color="#6600cc"/>
    </linearGradient>

    <linearGradient id="mnt" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1b0033"/>
      <stop offset="100%" stop-color="#02000a"/>
    </linearGradient>

    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#02000a"/>
      <stop offset="100%" stop-color="#0a0026"/>
    </linearGradient>

    <linearGradient id="comet" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur1"/>
      <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="glow-cyan" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1"/>
      <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="sun-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="15" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <mask id="sun-mask">
      <rect x="0" y="0" width="400" height="400" fill="#ffffff"/>
      <rect x="0" y="200" width="400" height="2" fill="#000000"/>
      <rect x="0" y="207" width="400" height="3" fill="#000000"/>
      <rect x="0" y="215" width="400" height="4" fill="#000000"/>
      <rect x="0" y="224" width="400" height="5" fill="#000000"/>
      <rect x="0" y="234" width="400" height="6" fill="#000000"/>
      <rect x="0" y="245" width="400" height="7" fill="#000000"/>
      <rect x="0" y="257" width="400" height="9" fill="#000000"/>
    </mask>
  </defs>

  <rect width="400" height="260" fill="url(#sky)"/>

  <g fill="#ffffff">
    <circle cx="30" cy="40" r="1" opacity="0.6"/>
    <circle cx="80" cy="20" r="1.5" opacity="0.9"/>
    <circle cx="150" cy="60" r="0.8" opacity="0.5"/>
    <circle cx="220" cy="30" r="1.2" opacity="0.8"/>
    <circle cx="290" cy="70" r="1" opacity="0.4"/>
    <circle cx="360" cy="40" r="1.5" opacity="1"/>
    <circle cx="380" cy="110" r="0.8" opacity="0.7"/>
    <circle cx="50" cy="120" r="1.2" opacity="0.5"/>
    <circle cx="120" cy="90" r="0.5" opacity="0.6"/>
    <circle cx="320" cy="140" r="1" opacity="0.8"/>
    
    <path d="M80,15 v10 M75,20 h10" stroke="#ffffff" stroke-width="0.5" opacity="0.9"/>
    <path d="M360,35 v10 M355,40 h10" stroke="#ffffff" stroke-width="0.5" opacity="1"/>
    <path d="M220,26 v8 M216,30 h8" stroke="#ffffff" stroke-width="0.5" opacity="0.8"/>
  </g>

  <line x1="320" y1="30" x2="220" y2="80" stroke="url(#comet)" stroke-width="1.5" filter="url(#glow-cyan)"/>
  <circle cx="320" cy="30" r="1.5" fill="#ffffff" filter="url(#glow-cyan)"/>

  <circle cx="200" cy="160" r="95" fill="#ff0077" filter="url(#sun-glow)" opacity="0.6"/>
  <circle cx="200" cy="160" r="90" fill="url(#sun)" mask="url(#sun-mask)"/>

  <path d="M100,260 V220 H115 V195 H125 V210 H135 V180 H155 V215 H165 V170 H180 V205 H195 V185 H210 V220 H225 V190 H240 V230 H255 V200 H265 V215 H275 V180 H290 V260 Z" fill="#02000a"/>
  <path d="M100,260 V220 H115 V195 H125 V210 H135 V180 H155 V215 H165 V170 H180 V205 H195 V185 H210 V220 H225 V190 H240 V230 H255 V200 H265 V215 H275 V180 H290 V260" fill="none" stroke="#ff0055" stroke-width="1.5" filter="url(#glow)"/>

  <path d="M-20,260 L60,170 L140,260 Z" fill="url(#mnt)"/>
  <path d="M-20,260 L60,170 L140,260" fill="none" stroke="#ff0055" stroke-width="1.5" filter="url(#glow)"/>
  
  <path d="M250,260 L330,150 L420,260 Z" fill="url(#mnt)"/>
  <path d="M250,260 L330,150 L420,260" fill="none" stroke="#ff0055" stroke-width="1.5" filter="url(#glow)"/>

  <path d="M-40,260 L40,190 L120,260 Z" fill="#02000a"/>
  <path d="M-40,260 L40,190 L120,260" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#glow-cyan)"/>
  
  <path d="M50,260 L120,210 L190,260 Z" fill="#02000a"/>
  <path d="M50,260 L120,210 L190,260" fill="none" stroke="#00e5ff" stroke-width="1.5" filter="url(#glow-cyan)"/>
  
  <path d="M280,260 L360,170 L440,260 Z" fill="#02000a"/>
  <path d="M280,260 L360,170 L440,260" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#glow-cyan)"/>

  <rect x="0" y="260" width="400" height="140" fill="url(#ground)"/>

  <g stroke="#ff00aa" filter="url(#glow)" opacity="0.8">
    <line x1="200" y1="260" x2="200" y2="400" stroke-width="2"/>
    <line x1="200" y1="260" x2="160" y2="400" stroke-width="1.8"/>
    <line x1="200" y1="260" x2="240" y2="400" stroke-width="1.8"/>
    <line x1="200" y1="260" x2="110" y2="400" stroke-width="1.6"/>
    <line x1="200" y1="260" x2="290" y2="400" stroke-width="1.6"/>
    <line x1="200" y1="260" x2="50" y2="400" stroke-width="1.4"/>
    <line x1="200" y1="260" x2="350" y2="400" stroke-width="1.4"/>
    <line x1="200" y1="260" x2="-30" y2="400" stroke-width="1.2"/>
    <line x1="200" y1="260" x2="430" y2="400" stroke-width="1.2"/>
    <line x1="200" y1="260" x2="-140" y2="400" stroke-width="1"/>
    <line x1="200" y1="260" x2="540" y2="400" stroke-width="1"/>
    <line x1="200" y1="260" x2="-290" y2="400" stroke-width="0.8"/>
    <line x1="200" y1="260" x2="690" y2="400" stroke-width="0.8"/>
    <line x1="200" y1="260" x2="-490" y2="400" stroke-width="0.6"/>
    <line x1="200" y1="260" x2="890" y2="400" stroke-width="0.6"/>

    <line x1="0" y1="264" x2="400" y2="264" stroke-width="0.6"/>
    <line x1="0" y1="269" x2="400" y2="269" stroke-width="0.8"/>
    <line x1="0" y1="276" x2="400" y2="276" stroke-width="1"/>
    <line x1="0" y1="285" x2="400" y2="285" stroke-width="1.3"/>
    <line x1="0" y1="297" x2="400" y2="297" stroke-width="1.6"/>
    <line x1="0" y1="313" x2="400" y2="313" stroke-width="2"/>
    <line x1="0" y1="335" x2="400" y2="335" stroke-width="2.5"/>
    <line x1="0" y1="365" x2="400" y2="365" stroke-width="3"/>
    <line x1="0" y1="400" x2="400" y2="400" stroke-width="3.5"/>
  </g>

  <line x1="0" y1="260" x2="400" y2="260" stroke="#00e5ff" stroke-width="3" filter="url(#glow-cyan)"/>
  <line x1="120" y1="260" x2="280" y2="260" stroke="#ffffff" stroke-width="1.5" filter="url(#glow-cyan)"/>
</svg>