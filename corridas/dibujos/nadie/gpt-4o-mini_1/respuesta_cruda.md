```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ff7e5f;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#feb47b;stop-opacity:1" />
    </linearGradient>
    <filter id="f1" x="0" y="0">
      <feGaussianBlur in="SourceGraphic" stdDeviation="5" />
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" />
  <g transform="translate(200,200)">
    <g transform="rotate(45)">
      <circle cx="-50" cy="-50" r="40" fill="purple" filter="url(#f1)" />
      <circle cx="50" cy="-50" r="40" fill="orange" filter="url(#f1)" />
      <circle cx="-50" cy="50" r="40" fill="cyan" filter="url(#f1)" />
      <circle cx="50" cy="50" r="40" fill="lime" filter="url(#f1)" />
    </g>
    <g transform="scale(0.6)">
      <path d="M 0 -80 Q 30 -100 60 -80 Q 90 -60 60 -40 Q 30 -20 0 -40 Q -30 -60 -60 -40 Q -90 -20 -60 -80 Q -30 -100 0 -80 Z" fill="rgba(255, 255, 255, 0.5)" />
      <path d="M 0 -80 Q 30 -60 60 -80 Q 90 -100 60 -120 Q 30 -140 0 -120 Q -30 -100 -60 -120 Q -90 -140 -60 -80 Q -30 -60 0 -80 Z" fill="rgba(255, 0, 0, 0.4)" transform="rotate(120)" />
      <path d="M 0 -80 Q 30 -140 60 -120 Q 90 -100 60 -80 Q 30 -60 0 -80 Q -30 -100 -60 -80 Q -90 -60 -60 -120 Q -30 -140 0 -80 Z" fill="rgba(0, 255, 0, 0.3)" transform="rotate(240)" />
    </g>
  </g>
  <text x="200" y="380" font-family="Arial" font-size="24" fill="black" text-anchor="middle">Un mundo de formas y colores</text>
</svg>
```