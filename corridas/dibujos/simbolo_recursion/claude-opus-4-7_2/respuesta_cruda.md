```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#1a2a4a"/>
      <stop offset="100%" stop-color="#05060f"/>
    </radialGradient>
    <linearGradient id="arrow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffcc33"/>
      <stop offset="100%" stop-color="#ff6633"/>
    </linearGradient>
  </defs>
  
  <rect width="400" height="400" fill="url(#bg)"/>
  
  <!-- Nested self-similar squares with rotation, suggesting recursion -->
  <g transform="translate(200 200)">
    <g stroke="url(#arrow)" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <rect x="-170" y="-170" width="340" height="340" stroke-width="4" rx="8" transform="rotate(0)" opacity="0.95"/>
      <rect x="-130" y="-130" width="260" height="260" stroke-width="3.5" rx="7" transform="rotate(15)" opacity="0.85"/>
      <rect x="-95" y="-95" width="190" height="190" stroke-width="3" rx="6" transform="rotate(30)" opacity="0.75"/>
      <rect x="-68" y="-68" width="136" height="136" stroke-width="2.5" rx="5" transform="rotate(45)" opacity="0.65"/>
      <rect x="-48" y="-48" width="96" height="96" stroke-width="2.2" rx="4" transform="rotate(60)" opacity="0.6"/>
      <rect x="-32" y="-32" width="64" height="64" stroke-width="2" rx="3" transform="rotate(75)" opacity="0.55"/>
      <rect x="-20" y="-20" width="40" height="40" stroke-width="1.8" rx="2" transform="rotate(90)" opacity="0.5"/>
      <rect x="-12" y="-12" width="24" height="24" stroke-width="1.5" rx="2" transform="rotate(105)" opacity="0.45"/>
    </g>
    
    <!-- Core point -->
    <circle r="5" fill="#ffcc33"/>
    
    <!-- Recursive arrow: curved arrow pointing inward, suggesting self-call -->
    <g fill="none" stroke="url(#arrow)" stroke-width="5" stroke-linecap="round">
      <path d="M 0,-185 A 185,185 0 0 1 175,-60" marker-end="url(#ah)"/>
    </g>
  </g>
  
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#ff6633"/>
    </marker>
  </defs>
  
  <!-- Ouroboros-style small arrows inside, each pointing further inward -->
  <g transform="translate(200 200)" fill="#ffcc33" opacity="0.9">
    <polygon points="0,-140 -8,-125 8,-125"/>
    <polygon points="99,-99 85,-91 91,-85" transform="rotate(-45)"/>
  </g>
</svg>
```