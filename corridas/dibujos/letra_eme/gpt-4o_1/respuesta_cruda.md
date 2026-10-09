```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="grad1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:rgb(255,255,255);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:0.1" />
    </radialGradient>
  </defs>
  <rect width="400" height="400" fill="url(#grad1)" />
  <path d="M 100 300 Q 150 50, 200 100 Q 250 50, 300 300" fill="none" stroke="black" stroke-width="20"/>
  <circle cx="200" cy="200" r="30" fill="black"/>
  <path d="M 100 300 L 150 150 Q 200 200, 250 150 L 300 300" fill="none" stroke="black" stroke-width="20"/>
</svg>
```