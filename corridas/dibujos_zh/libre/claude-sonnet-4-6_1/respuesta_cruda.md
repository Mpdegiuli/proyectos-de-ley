```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="sky" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#1a1a4e"/>
      <stop offset="100%" stop-color="#0d0d2b"/>
    </radialGradient>
    <radialGradient id="moon" cx="40%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#fffde7"/>
      <stop offset="100%" stop-color="#f9a825"/>
    </radialGradient>
    <radialGradient id="water" cx="50%" cy="0%" r="100%">
      <stop offset="0%" stop-color="#1a237e"/>
      <stop offset="100%" stop-color="#0d0d2b"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Sky background -->
  <rect width="400" height="400" fill="url(#sky)"/>

  <!-- Stars -->
  <g fill="white" filter="url(#glow)">
    <circle cx="30" cy="20" r="1.2" opacity="0.9"/>
    <circle cx="80" cy="45" r="0.8" opacity="0.7"/>
    <circle cx="120" cy="15" r="1" opacity="0.85"/>
    <circle cx="160" cy="35" r="0.6" opacity="0.6"/>
    <circle cx="200" cy="10" r="1.1" opacity="0.9"/>
    <circle cx="250" cy="30" r="0.9" opacity="0.75"/>
    <circle cx="300" cy="18" r="1.3" opacity="0.95"/>
    <circle cx="340" cy="50" r="0.7" opacity="0.65"/>
    <circle cx="370" cy="25" r="1" opacity="0.8"/>
    <circle cx="55" cy="70" r="0.8" opacity="0.7"/>
    <circle cx="100" cy="85" r="1.1" opacity="0.85"/>
    <circle cx="145" cy="60" r="0.6" opacity="0.6"/>
    <circle cx="220" cy="55" r="0.9" opacity="0.75"/>
    <circle cx="270" cy="75" r="1.2" opacity="0.9"/>
    <circle cx="320" cy="65" r="0.7" opacity="0.65"/>
    <circle cx="360" cy="80" r="1" opacity="0.8"/>
    <circle cx="15" cy="100" r="0.9" opacity="0.7"/>
    <circle cx="65" cy="110" r="0.7" opacity="0.6"/>
    <circle cx="185" cy="90" r="1" opacity="0.8"/>
    <circle cx="390" cy="40" r="0.8" opacity="0.7"/>
    <circle cx="10" cy="55" r="0.6" opacity="0.55"/>
    <circle cx="135" cy="100" r="0.8" opacity="0.7"/>
    <circle cx="310" cy="95" r="0.9" opacity="0.75"/>
    <circle cx="385" cy="105" r="0.7" opacity="0.65"/>
  </g>

  <!-- Moon -->
  <circle cx="310" cy="80" r="45" fill="#fffde7" opacity="0.15" filter="url(#softglow)"/>
  <circle cx="310" cy="80" r="35" fill="url(#moon)" filter="url(#softglow)"/>
  <!-- Moon craters -->
  <circle cx="300" cy="70" r="5" fill="#f0c040" opacity="0.4"/>
  <circle cx="320" cy="85" r="3.5" fill="#f0c040" opacity="0.35"/>
  <circle cx="305" cy="92" r="2.5" fill="#f0c040" opacity="0.3"/>

  <!-- Moon reflection path on water -->
  <ellipse cx="310" cy="310" rx="18" ry="80" fill="#f9a825" opacity="0.12"/>

  <!-- Mountains background -->
  <polygon points="0,280 60,180 120,250 180,160 240,230 300,170 360,220 400,180 400,280" fill="#0f1b5e" opacity="0.8"/>
  <polygon points="0,280 60,180 120,250 180,160 240,230 300,170 360,220 400,180 400,280" fill="#16205a"/>

  <!-- Mountains foreground -->
  <polygon points="-10,290 50,210 110,270 170,195 230,265 290,200 350,255 410,210 410,290" fill="#0a1240"/>

  <!-- Water / Lake -->
  <rect x="0" y="270" width="400" height="130" fill="url(#water)"/>

  <!-- Water ripples / reflections -->
  <g stroke="#3949ab" stroke-width="1" fill="none" opacity="0.4">
    <ellipse cx="200" cy="285" rx="80" ry="4"/>
    <ellipse cx="200" cy="295" rx="100" ry="4"/>
    <ellipse cx="200" cy="310" rx="120" ry="5"/>
    <ellipse cx="200" cy="325" rx="140" ry="5"/>
    <ellipse cx="200" cy="342" rx="160" ry="5"/>
    <ellipse cx="200" cy="360" rx="180" ry="5"/>
  </g>

  <!-- Mountain reflection in water -->
  <polygon points="0,290 60,340 120,310 180,355 240,315 300,350 360,320 400,345 400,290" fill="#0d1740" opacity="0.7"/>

  <!-- Pine trees left -->
  <g fill="#0a1530">
    <polygon points="40,275 50,230 60,275"/>
    <polygon points="38,270 50,220 62,270"/>
    <polygon points="20,278 32,240 44,278"/>
    <polygon points="18,273 32,228 46,273"/>
    <polygon points="60,278 70,248 80,278"/>
    <polygon points="58,272 70,238 82,272"/>
  </g>

  <!-- Pine trees right -->
  <g fill="#0a1530">
    <polygon points="320,278 332,238 344,278"/>
    <polygon points="318,272 332,226 346,272"/>
    <polygon points="340,276 352,242 364,276"/>
    <polygon points="338,270 352,230 366,270"/>
    <polygon points="360,279 372,245 384,279"/>
    <polygon points="358,273 372,233 386,273"/>
  </g>

  <!-- Shooting star -->
  <line x1="50" y1="40" x2="100" y2="60" stroke="white" stroke-width="1.5" opacity="0.8" stroke-linecap="round"/>
  <circle cx="50" cy="40" r="1.5" fill="white" opacity="0.9"/>

  <!-- Foreground dark ground -->
  <ellipse cx="200" cy="272" rx="220" ry="12" fill="#060e2a"/>

  <!-- Foreground bushes/reeds -->
  <g stroke="#0d1f3a" stroke-width="2" fill="none">
    <line x1="85" y1="275" x2="82" y2="255"/>
    <line x1="90" y1="275" x2="93" y2="252"/>
    <line x1="95" y1="275" x2="91" y2="248"/>
    <line x1="300" y1="275" x2="297" y2="255"/>
    <line x1="305" y1="275" x2="308" y2="252"/>
    <line x1="310" y1="275" x2="306" y2="248"/>
  </g>

  <!-- Subtle aurora borealis -->
  <g opacity="0.12">
    <path d="M0,120 Q100,90 200,110 Q300,130 400,100" stroke="#00e676" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M0,135 Q100,105 200,125 Q300,145 400,115" stroke="#40c4ff" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path d="M0,148 Q100,118 200,138 Q300,158 400,128" stroke="#00e676" stroke-width="4" fill="none" stroke-linecap="round"/>
  </g>
</svg>
```