```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bodyGradient" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:rgb(173,216,230);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,105,148);stop-opacity:1" />
    </radialGradient>
  </defs>
  <rect width="400" height="400" fill="lightblue"/>
  <g stroke-width="2">
    <ellipse cx="200" cy="220" rx="100" ry="160" fill="url(#bodyGradient)" stroke="black"/>
    <ellipse cx="200" cy="100" rx="65" ry="65" fill="lightcoral" stroke="black"/>
    <circle cx="175" cy="85" r="10" fill="white" stroke="black"/>
    <circle cx="225" cy="85" r="10" fill="white" stroke="black"/>
    <circle cx="175" cy="85" r="5" fill="black"/>
    <circle cx="225" cy="85" r="5" fill="black"/>
    <path d="M165,115 C200,140 220,140 235,115" fill="transparent" stroke="black"/>
    <path d="M110,220 Q50,180 60,230 Q50,280 110,240" fill="none" stroke="black"/>
    <path d="M290,220 Q350,180 340,230 Q350,280 290,240" fill="none" stroke="black"/>
    <ellipse cx="130" cy="300" rx="20" ry="40" fill="lightcoral" stroke="black" transform="rotate(-20 130 300)"/>
    <ellipse cx="270" cy="300" rx="20" ry="40" fill="lightcoral" stroke="black" transform="rotate(20 270 300)"/>
    <path d="M150,400 Q200,360 250,400" fill="none" stroke="black"/>
  </g>
</svg>
```