```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="sky" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#2a1a4a"/>
      <stop offset="100%" stop-color="#0a0520"/>
    </radialGradient>
    <radialGradient id="body" cx="40%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#ff8ac4"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#4c1d95"/>
    </radialGradient>
    <radialGradient id="belly" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#fde68a"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </radialGradient>
    <radialGradient id="eye" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="70%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#064e3b"/>
    </radialGradient>
    <radialGradient id="horn" cx="30%" cy="30%" r="80%">
      <stop offset="0%" stop-color="#fff"/>
      <stop offset="100%" stop-color="#60a5fa"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  
  <!-- estrellas -->
  <g fill="#fff">
    <circle cx="40" cy="60" r="1.2"/>
    <circle cx="350" cy="40" r="1.5"/>
    <circle cx="80" cy="120" r="1"/>
    <circle cx="370" cy="150" r="1.3"/>
    <circle cx="30" cy="300" r="1.1"/>
    <circle cx="380" cy="320" r="1"/>
    <circle cx="200" cy="30" r="1.4"/>
    <circle cx="120" cy="25" r="1"/>
  </g>

  <!-- cola espiral -->
  <path d="M 310 260 Q 370 240 360 180 Q 350 130 300 140 Q 270 150 285 180" 
        stroke="url(#body)" stroke-width="18" fill="none" stroke-linecap="round"/>
  <path d="M 310 260 Q 370 240 360 180 Q 350 130 300 140 Q 270 150 285 180" 
        stroke="#ff8ac4" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.5"/>

  <!-- patas traseras -->
  <ellipse cx="150" cy="320" rx="22" ry="35" fill="url(#body)"/>
  <ellipse cx="240" cy="320" rx="22" ry="35" fill="url(#body)"/>
  <ellipse cx="150" cy="350" rx="28" ry="12" fill="#4c1d95"/>
  <ellipse cx="240" cy="350" rx="28" ry="12" fill="#4c1d95"/>
  <!-- garras -->
  <g fill="#fde68a">
    <circle cx="135" cy="355" r="3"/><circle cx="150" cy="358" r="3"/><circle cx="165" cy="355" r="3"/>
    <circle cx="225" cy="355" r="3"/><circle cx="240" cy="358" r="3"/><circle cx="255" cy="355" r="3"/>
  </g>

  <!-- cuerpo -->
  <ellipse cx="195" cy="260" rx="100" ry="75" fill="url(#body)"/>
  <ellipse cx="195" cy="275" rx="60" ry="45" fill="url(#belly)"/>
  
  <!-- manchas luminosas -->
  <g fill="#fde68a" filter="url(#glow)" opacity="0.9">
    <circle cx="130" cy="230" r="4"/>
    <circle cx="260" cy="225" r="5"/>
    <circle cx="150" cy="200" r="3"/>
    <circle cx="245" cy="195" r="3"/>
    <circle cx="110" cy="270" r="4"/>
    <circle cx="275" cy="265" r="4"/>
  </g>

  <!-- cabeza -->
  <ellipse cx="195" cy="155" rx="75" ry="65" fill="url(#body)"/>
  
  <!-- orejas largas puntiagudas -->
  <path d="M 135 110 Q 110 40 95 80 Q 100 120 150 135 Z" fill="url(#body)"/>
  <path d="M 255 110 Q 280 40 295 80 Q 290 120 240 135 Z" fill="url(#body)"/>
  <path d="M 128 105 Q 115 60 108 85 Q 115 110 140 125 Z" fill="#ff8ac4" opacity="0.6"/>
  <path d="M 262 105 Q 275 60 282 85 Q 275 110 250 125 Z" fill="#ff8ac4" opacity="0.6"/>

  <!-- cuerno central brillante -->
  <path d="M 195 90 L 185 30 L 205 30 Z" fill="url(#horn)" filter="url(#glow)"/>
  <circle cx="195" cy="30" r="5" fill="#fff" filter="url(#glow)"/>

  <!-- tres ojos -->
  <ellipse cx="160" cy="155" rx="16" ry="20" fill="#fff"/>
  <ellipse cx="230" cy="155" rx="16" ry="20" fill="#fff"/>
  <ellipse cx="195" cy="125" rx="12" ry="15" fill="#fff"/>
  
  <circle cx="162" cy="158" r="11" fill="url(#eye)"/>
  <circle cx="232" cy="158" r="11" fill="url(#eye)"/>
  <circle cx="195" cy="128" r="8" fill="url(#eye)"/>
  
  <ellipse cx="162" cy="160" rx="4" ry="8" fill="#000"/>
  <ellipse cx="232" cy="160" rx="4" ry="8" fill="#000"/>
  <ellipse cx="195" cy="130" rx="3" ry="6" fill="#000"/>
  
  <circle cx="164" cy="155" r="2" fill="#fff"/>
  <circle cx="234" cy="155" r="2" fill="#fff"/>
  <circle cx="196" cy="127" r="1.5" fill="#fff"/>

  <!-- nariz -->
  <path d="M 185 185 Q 195 195 205 185 Q 200 200 195 200 Q 190 200 185 185 Z" fill="#4c1d95"/>
  
  <!-- boca con colmillitos -->
  <path d="M 170 205 Q 195 220 220 205" stroke="#4c1d95" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M 185 212 L 183 220 L 188 215 Z" fill="#fff"/>
  <path d="M 205 212 L 207 220 L 202 215 Z" fill="#fff"/>

  <!-- bigotes -->
  <g stroke="#fff" stroke-width="1" opacity="0.7">
    <line x1="155" y1="200" x2="120" y2="195"/>
    <line x1="155" y1="205" x2="120" y2="210"/>
    <line x1="235" y1="200" x2="270" y2="195"/>
    <line x1="235" y1="205" x2="270" y2="210"/>
  </g>

  <!-- alitas pequeñas -->
  <path d="M 110 220 Q 60 200 50 240 Q 70 260 115 250 Z" fill="#ff8ac4" opacity="0.8"/>
  <path d="M 280 220 Q 330 200 340 240 Q 320 260 275 250 Z" fill="#ff8ac4" opacity="0.8"/>
  <path d="M 110 220 Q 70 215 60 240" stroke="#a855f7" stroke-width="1.5" fill="none"/>
  <path d="M 280 220 Q 320 215 330 240" stroke="#a855f7" stroke-width="1.5" fill="none"/>

</svg>
```