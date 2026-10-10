<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="0.5" cy="0.42" r="0.8">
      <stop offset="0" stop-color="#f9f5ec"/>
      <stop offset="1" stop-color="#ece6d6"/>
    </radialGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4c4661"/>
      <stop offset="0.55" stop-color="#332f44"/>
      <stop offset="1" stop-color="#232030"/>
    </linearGradient>
    <linearGradient id="lobeF" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#342f45"/>
      <stop offset="1" stop-color="#1f1c2a"/>
    </linearGradient>
    <linearGradient id="lobeB" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#d0c5aa"/>
      <stop offset="1" stop-color="#f2ebd9"/>
    </linearGradient>
    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0.5 0.5 0 0"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <rect x="14" y="14" width="372" height="372" fill="none" stroke="#dcd2bb"/>
  <path d="M48 60H352" stroke="#d9d0ba" fill="none"/>
  <path d="M48 317H352" stroke="#c8bea2" stroke-width="1.2" fill="none"/>
  <text x="200" y="38" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-style="italic" font-size="15" letter-spacing="1" fill="#7a7260">una letra que no puede existir</text>
  <text x="200" y="187" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-style="italic" font-size="13" fill="#8d8471">adentro</text>
  <text x="200" y="368" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-style="italic" font-size="13" fill="#8d8471">afuera</text>
  <path d="M200 205V338" stroke="#a89e88" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="0.1 8" fill="none"/>
  <path d="M192.5 335L207.5 335L200 349Z" fill="#a89e88"/>
  <path d="M173 317.2A130 130 0 1 1 227 317.2L214.6 258.5A70 70 0 1 0 185.4 258.5Z" fill="url(#ink)"/>
  <path d="M101.5 172.6A100 100 0 0 1 276.6 125.7" fill="none" stroke="#ffffff" stroke-width="18" stroke-linecap="round" opacity="0.12"/>
  <path d="M296.6 215.9A100 100 0 0 1 242.3 280.6" fill="none" stroke="#000000" stroke-width="18" stroke-linecap="round" opacity="0.12"/>
  <path d="M215.4 262.4A74 74 0 1 0 184.6 262.4" fill="none" stroke="#000000" stroke-width="8" opacity="0.18"/>
  <path d="M173 317.2Q180 308 200 290Q192 272 185.4 258.5Z" fill="url(#lobeF)"/>
  <path d="M200 290Q208 272 214.6 258.5L227 317.2Q220 308 200 290Z" fill="url(#lobeB)"/>
  <path d="M173 317.2A130 130 0 1 1 227 317.2Q220 308 200 290Q208 272 214.6 258.5A70 70 0 1 0 185.4 258.5Q192 272 200 290Q180 308 173 317.2Z" fill="none" stroke="#c2452d" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <rect width="400" height="400" filter="url(#grain)" opacity="0.05"/>
</svg>