<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <path id="stroke" d="M200 40 355.885 310H293.531L200 148 137.646 256H75.292Z"/>
    <mask id="first" maskUnits="userSpaceOnUse" x="0" y="0" width="400" height="400">
      <rect width="400" height="400" fill="white"/>
      <use href="#stroke" transform="rotate(240 200 220)" fill="black"/>
    </mask>
    <mask id="second" maskUnits="userSpaceOnUse" x="0" y="0" width="400" height="400">
      <rect width="400" height="400" fill="white"/>
      <use href="#stroke" fill="black"/>
    </mask>
    <mask id="third" maskUnits="userSpaceOnUse" x="0" y="0" width="400" height="400">
      <rect width="400" height="400" fill="white"/>
      <use href="#stroke" transform="rotate(120 200 220)" fill="black"/>
    </mask>
    <linearGradient id="ink" x1="180" y1="40" x2="300" y2="310" gradientUnits="userSpaceOnUse">
      <stop stop-color="#173a3c"/>
      <stop offset="1" stop-color="#10272a"/>
    </linearGradient>
    <linearGradient id="edge" x1="50" y1="280" x2="350" y2="300" gradientUnits="userSpaceOnUse">
      <stop stop-color="#54756f"/>
      <stop offset="1" stop-color="#8aa095"/>
    </linearGradient>
    <linearGradient id="turn" x1="95" y1="290" x2="200" y2="50" gradientUnits="userSpaceOnUse">
      <stop stop-color="#b4c0ab"/>
      <stop offset="1" stop-color="#79968a"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f3f0e7"/>
  <g transform="translate(20 1) scale(.9)">
    <path d="M75.292 256H120V343Q120 359 141 359H149V371H49V359H58Q75.292 359 75.292 343Z" fill="#173a3c"/>
    <path d="M120 300V343Q120 359 141 359H149V371H130Q101 363 101 343V300Z" fill="#10272a"/>
    <use href="#stroke" fill="url(#ink)" mask="url(#first)"/>
    <use href="#stroke" transform="rotate(120 200 220)" fill="url(#edge)" mask="url(#second)"/>
    <use href="#stroke" transform="rotate(240 200 220)" fill="url(#turn)" mask="url(#third)"/>
  </g>
</svg>