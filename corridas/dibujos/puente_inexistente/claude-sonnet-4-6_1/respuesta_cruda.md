```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0a2e"/>
      <stop offset="60%" stop-color="#1a1a6e"/>
      <stop offset="100%" stop-color="#2a2a9e"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0d3b6e"/>
      <stop offset="100%" stop-color="#051a3a"/>
    </linearGradient>
    <linearGradient id="crystalGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#a0e8ff" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#5090cc" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#2050aa" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="towerGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8888ff"/>
      <stop offset="50%" stop-color="#ccccff"/>
      <stop offset="100%" stop-color="#8888ff"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <radialGradient id="moonGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffc8"/>
      <stop offset="100%" stop-color="#e8e8a0"/>
    </radialGradient>
  </defs>

  <!-- Sky -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Stars -->
  <circle cx="30" cy="20" r="1" fill="white" opacity="0.8"/>
  <circle cx="80" cy="45" r="1.2" fill="white" opacity="0.9"/>
  <circle cx="150" cy="15" r="0.8" fill="white" opacity="0.7"/>
  <circle cx="200" cy="30" r="1" fill="white" opacity="0.6"/>
  <circle cx="260" cy="10" r="1.1" fill="white" opacity="0.8"/>
  <circle cx="320" cy="35" r="0.9" fill="white" opacity="0.7"/>
  <circle cx="370" cy="20" r="1.2" fill="white" opacity="0.9"/>
  <circle cx="50" cy="70" r="0.8" fill="white" opacity="0.6"/>
  <circle cx="110" cy="55" r="1" fill="white" opacity="0.7"/>
  <circle cx="340" cy="60" r="1" fill="white" opacity="0.8"/>
  <circle cx="390" cy="50" r="0.7" fill="white" opacity="0.6"/>

  <!-- Moon -->
  <circle cx="340" cy="55" r="22" fill="url(#moonGrad)" filter="url(#softglow)" opacity="0.95"/>
  <circle cx="350" cy="48" r="18" fill="url(#sky)" opacity="0.3"/>

  <!-- Water -->
  <rect x="0" y="270" width="400" height="130" fill="url(#water)"/>

  <!-- Water reflections -->
  <ellipse cx="200" cy="285" rx="80" ry="5" fill="#3a6aaa" opacity="0.3"/>
  <ellipse cx="100" cy="295" rx="40" ry="3" fill="#3a6aaa" opacity="0.2"/>
  <ellipse cx="300" cy="295" rx="40" ry="3" fill="#3a6aaa" opacity="0.2"/>

  <!-- Moon reflection in water -->
  <ellipse cx="340" cy="310" rx="15" ry="40" fill="#ffffc8" opacity="0.07"/>

  <!-- Cliff left -->
  <polygon points="0,270 80,270 80,400 0,400" fill="#1a1a3a"/>
  <polygon points="0,240 85,270 0,270" fill="#252540"/>

  <!-- Cliff right -->
  <polygon points="320,270 400,240 400,400 320,400" fill="#1a1a3a"/>
  <polygon points="315,270 400,240 400,270" fill="#252540"/>

  <!-- === IMPOSSIBLE HELIX BRIDGE === -->
  <!-- The deck twists in a möbius-like spiral as it crosses -->

  <!-- Bridge deck segments - twisting ribbon -->
  <!-- Left side approach -->
  <polygon points="80,265 140,260 140,275 80,278" fill="#9090ee" opacity="0.85"/>

  <!-- Twist segment 1 -->
  <polygon points="140,260 180,240 185,260 140,275" fill="url(#crystalGrad)" opacity="0.9"/>

  <!-- Twist segment 2 - narrows to center point -->
  <polygon points="180,240 215,255 215,255 185,260" fill="url(#crystalGrad)" opacity="0.85"/>

  <!-- Twist segment 3 - widens other side -->
  <polygon points="215,255 215,255 260,240 215,270" fill="url(#crystalGrad)" opacity="0.85"/>

  <!-- Right side approach -->
  <polygon points="260,240 320,265 320,278 215,270" fill="#9090ee" opacity="0.85"/>

  <!-- Underside of deck (different color to show twist) -->
  <polygon points="140,275 185,260 215,260 175,280" fill="#4040aa" opacity="0.7"/>
  <polygon points="215,260 260,240 270,255 220,275" fill="#4040aa" opacity="0.7"/>

  <!-- === CRYSTAL SPIRE TOWERS === -->
  <!-- Left tower -->
  <rect x="120" y="180" width="22" height="90" fill="url(#towerGrad)" opacity="0.9"/>
  <!-- Tower crystal top -->
  <polygon points="131,130 120,180 142,180" fill="#d0d0ff" filter="url(#glow)" opacity="0.95"/>
  <polygon points="131,130 126,155 136,155" fill="white" opacity="0.5"/>
  <!-- Tower base decoration -->
  <rect x="115" y="260" width="32" height="10" fill="#a0a0dd" opacity="0.8"/>

  <!-- Right tower -->
  <rect x="258" y="180" width="22" height="90" fill="url(#towerGrad)" opacity="0.9"/>
  <!-- Tower crystal top -->
  <polygon points="269,130 258,180 280,180" fill="#d0d0ff" filter="url(#glow)" opacity="0.95"/>
  <polygon points="269,130 264,155 274,155" fill="white" opacity="0.5"/>
  <!-- Tower base decoration -->
  <rect x="253" y="260" width="32" height="10" fill="#a0a0dd" opacity="0.8"/>

  <!-- === IMPOSSIBLE SUSPENSION CABLES === -->
  <!-- These cables go OVER and UNDER the twisted deck simultaneously -->

  <!-- Main cables left tower top to right tower top -->
  <path d="M131,135 Q200,90 269,135" stroke="#c0c0ff" stroke-width="2" fill="none" filter="url(#glow)" opacity="0.9"/>
  <path d="M131,135 Q200,195 269,135" stroke="#8080cc" stroke-width="1.5" fill="none" opacity="0.6"/>

  <!-- Vertical hangers from upper cable -->
  <line x1="155" y1="131" x2="148" y2="262" stroke="#a0a0ff" stroke-width="1" opacity="0.6"/>
  <line x1="175" y1="118" x2="168" y2="262" stroke="#a0a0ff" stroke-width="1" opacity="0.6"/>
  <line x1="200" y1="112" x2="200" y2="262" stroke="#a0a0ff" stroke-width="1" opacity="0.6"/>
  <line x1="225" y1="118" x2="232" y2="262" stroke="#a0a0ff" stroke-width="1" opacity="0.6"/>
  <line x1="245" y1="131" x2="252" y2="262" stroke="#a0a0ff" stroke-width="1" opacity="0.6"/>

  <!-- Diagonal cables that cross (impossible geometry) -->
  <line x1="131" y1="140" x2="269" y2="200" stroke="#80c0ff" stroke-width="1.5" opacity="0.5"/>
  <line x1="131" y1="200" x2="269" y2="140" stroke="#80c0ff" stroke-width="1.5" opacity="0.5"/>

  <!-- === FLOATING GLOWING RINGS === -->
  <!-- Rings encircle the bridge at impossible angles -->
  <ellipse cx="200" cy="210" rx="60" ry="15" fill="none" stroke="#00ffff" stroke-width="1.5" opacity="0.4" filter="url(#glow)"/>
  <ellipse cx="200" cy="210" rx="60" ry="35" fill="none" stroke="#8800ff" stroke-width="1" opacity="0.3" filter="url(#glow)" transform="rotate(30,200,210)"/>
  <ellipse cx="200" cy="220" rx="55" ry="20" fill="none" stroke="#ff88ff" stroke-width="1" opacity="0.3" filter="url(#glow)" transform="rotate(-20,200,220)"/>

  <!-- === TOWER LIGHT BEAMS === -->
  <line x1="131" y1="130" x2="50" y2="50" stroke="#ffffaa" stroke-width="1" opacity="0.2"/>
  <line x1="269" y1="130" x2="350" y2="50" stroke="#ffffaa" stroke-width="1" opacity="0.2"/>

  <!-- Glowing orbs at tower tops -->
  <circle cx="131" cy="130" r="6" fill="#ffffff" filter="url(#softglow)" opacity="0.9"/>
  <circle cx="269" cy="130" r="6" fill="#ffffff" filter="url(#softglow)" opacity="0.9"/>

  <!-- Small platform in the middle of impossible twist -->
  <ellipse cx="200" cy="257" rx="12" ry="5" fill="#ccccff" opacity="0.8"/>
  <circle cx="200" cy="252" r="3" fill="white" filter="url(#glow)" opacity="0.9"/>

  <!-- Water ripple reflections of towers -->
  <line x1="131" y1="275" x2="131" y2="340" stroke="#8080cc" stroke-width="1" opacity="0.15"/>
  <line x1="269" y1="275" x2="269" y2="340" stroke="#8080cc" stroke-width="1" opacity="0.15"/>
  <ellipse cx="131" cy="320" rx="8" ry="2" fill="#8080cc" opacity="0.1"/>
  <ellipse cx="269" cy="320" rx="8" ry="2" fill="#8080cc" opacity="0.1"/>

  <!-- Fog / mist at water level -->
  <ellipse cx="200" cy="272" rx="180" ry="12" fill="#aaaadd" opacity="0.08"/>
  <ellipse cx="200" cy="268" rx="120" ry="7" fill="#bbbbff" opacity="0.06"/>

</svg>
```