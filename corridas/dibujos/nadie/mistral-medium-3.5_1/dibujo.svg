<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00ffff;stop-opacity:1" />
    </linearGradient>
    <filter id="fuzz" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="10" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <path id="blob" d="M100,100 C120,80 150,80 170,100 C190,120 200,150 180,180 C160,210 130,220 110,200 C90,180 80,150 100,100 Z"/>
  </defs>
  <rect width="400" height="400" fill="url(#grad1)" opacity="0.3"/>
  <g transform="translate(200,200)">
    <use href="#blob" fill="none" stroke="#ff0000" stroke-width="2" filter="url(#fuzz)"/>
    <use href="#blob" fill="none" stroke="#00ff00" stroke-width="2" transform="rotate(45)" filter="url(#fuzz)"/>
    <use href="#blob" fill="none" stroke="#0000ff" stroke-width="2" transform="rotate(90)" filter="url(#fuzz)"/>
    <circle cx="0" cy="0" r="50" fill="none" stroke="#ffff00" stroke-width="3" stroke-dasharray="5,5" filter="url(#fuzz)"/>
    <text x="0" y="0" text-anchor="middle" dominant-baseline="middle" font-size="20" fill="#ffffff" filter="url(#fuzz)">¿?</text>
  </g>
  <polygon points="50,50 150,50 150,150 50,150" fill="none" stroke="#ff00ff" stroke-width="2" transform="rotate(15 100 100)" filter="url(#fuzz)"/>
  <polygon points="250,50 350,50 350,150 250,150" fill="none" stroke="#00ffff" stroke-width="2" transform="rotate(-15 300 100)" filter="url(#fuzz)"/>
  <polygon points="50,250 150,250 150,350 50,350" fill="none" stroke="#ff00ff" stroke-width="2" transform="rotate(15 100 300)" filter="url(#fuzz)"/>
  <polygon points="250,250 350,250 350,350 250,350" fill="none" stroke="#00ffff" stroke-width="2" transform="rotate(-15 300 300)" filter="url(#fuzz)"/>
</svg>