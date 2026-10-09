```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,165,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
    <radialGradient id="grad2" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </radialGradient>
  </defs>
  <rect width="400" height="400" fill="url(#grad2)" />
  <path d="M200,50 C150,100 150,300 200,350 C250,300 250,100 200,50 Z" fill="url(#grad1)" stroke="black" stroke-width="10" />
  <circle cx="200" cy="200" r="50" fill="white" />
  <ellipse cx="200" cy="200" rx="15" ry="50" fill="black" />
  <line x1="150" y1="150" x2="250" y2="250" stroke="black" stroke-width="10" />
  <line x1="250" y1="150" x2="150" y2="250" stroke="black" stroke-width="10" />
  <text x="173" y="390" font-family="Arial" font-size="24" fill="black">LNX</text>
  <line x1="100" y1="100" x2="300" y2="300" stroke="orange" stroke-width="5" stroke-dasharray="10,10" />
  <line x1="300" y1="100" x2="100" y2="300" stroke="orange" stroke-width="5" stroke-dasharray="10,10" />
</svg>
```