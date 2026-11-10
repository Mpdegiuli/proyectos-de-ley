```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#0d1b2a"/>
  <!-- nested rectangles: same shape, smaller each time -->
  <g fill="none" stroke-linejoin="round">
    <rect x="40" y="40" width="320" height="320" rx="24" stroke="#4cc9f0" stroke-width="7"/>
    <rect x="72" y="72" width="256" height="256" rx="20" stroke="#4895ef" stroke-width="6"/>
    <rect x="100" y="100" width="200" height="200" rx="16" stroke="#4361ee" stroke-width="5"/>
    <rect x="124" y="124" width="152" height="152" rx="13" stroke="#5f7adb" stroke-width="4"/>
    <rect x="146" y="146" width="108" height="108" rx="10" stroke="#7b6fd6" stroke-width="4"/>
    <rect x="164" y="164" width="72" height="72" rx="8" stroke="#9d63c7" stroke-width="3"/>
    <rect x="180" y="180" width="40" height="40" rx="6" stroke="#c163bc" stroke-width="3"/>
    <circle cx="200" cy="200" r="7" fill="#f72585"/>
  </g>
  <!-- spiral arrow: reducing into itself -->
  <path d="M 55 200
           C 55 90, 90 55, 200 55
           C 310 55, 345 90, 345 200
           C 345 310, 310 345, 200 345
           C 110 345, 80 315, 80 240
           C 80 165, 115 135, 185 135
           C 250 135, 280 165, 280 220
           C 280 275, 250 300, 200 300
           C 160 300, 140 280, 140 245
           C 140 210, 162 192, 192 192"
        fill="none" stroke="#ffd166" stroke-width="5"
        stroke-linecap="round"/>
  <!-- arrowhead at the spiral core -->
  <path d="M 192 192 L 214 186 L 206 208 Z" fill="#ffd166"/>
  <!-- two small mirrored arrows: base case stops the descent -->
  <g stroke="#06d6a0" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M 30 358 L 66 358"/>
    <path d="M 42 346 L 30 358 L 42 370"/>
    <path d="M 370 358 L 334 358"/>
    <path d="M 358 346 L 370 358 L 358 370"/>
  </g>
</svg>
```