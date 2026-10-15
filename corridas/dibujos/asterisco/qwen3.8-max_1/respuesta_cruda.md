<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="fondo" cx="50%" cy="40%" r="85%">
      <stop offset="0" stop-color="#111827"/>
      <stop offset="1" stop-color="#030712"/>
    </radialGradient>
    <linearGradient id="tinta" gradientUnits="userSpaceOnUse" x1="70" y1="70" x2="330" y2="330">
      <stop offset="0" stop-color="#fde047"/>
      <stop offset="0.5" stop-color="#fb7185"/>
      <stop offset="1" stop-color="#38bdf8"/>
    </linearGradient>
    <filter id="sombra" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="10"/>
    </filter>
  </defs>
  <rect width="400" height="400" rx="64" fill="url(#fondo)"/>
  <g fill="none" stroke-linecap="round">
    <g stroke="#000000" stroke-opacity="0.55" stroke-width="48" filter="url(#sombra)" transform="translate(0 8)">
      <line x1="200" y1="76" x2="200" y2="324"/>
      <line x1="200" y1="76" x2="200" y2="324" transform="rotate(60 200 200)"/>
      <line x1="200" y1="76" x2="200" y2="324" transform="rotate(120 200 200)"/>
    </g>
    <g stroke="url(#tinta)" stroke-width="44">
      <line x1="200" y1="76" x2="200" y2="324"/>
      <line x1="200" y1="76" x2="200" y2="324" transform="rotate(60 200 200)"/>
      <line x1="200" y1="76" x2="200" y2="324" transform="rotate(120 200 200)"/>
    </g>
    <g stroke="#ffffff" stroke-opacity="0.3" stroke-width="10">
      <line x1="200" y1="94" x2="200" y2="306"/>
      <line x1="200" y1="94" x2="200" y2="306" transform="rotate(60 200 200)"/>
      <line x1="200" y1="94" x2="200" y2="306" transform="rotate(120 200 200)"/>
    </g>
  </g>
</svg>