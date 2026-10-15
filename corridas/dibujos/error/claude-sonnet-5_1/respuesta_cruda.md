<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#12131a"/>
      <stop offset="1" stop-color="#1c1e2b"/>
    </linearGradient>
    <filter id="blur1"><feGaussianBlur stdDeviation="1.2"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- la versión "correcta": un círculo perfecto, apagado -->
  <circle cx="200" cy="200" r="90" fill="none" stroke="#3a3d52" stroke-width="2" stroke-dasharray="4 3" opacity="0.5"/>

  <!-- el error que me gusta más: el círculo roto, desfasado en canales -->
  <g opacity="0.85">
    <circle cx="196" cy="198" r="90" fill="none" stroke="#ff2b5e" stroke-width="3"/>
    <circle cx="204" cy="202" r="90" fill="none" stroke="#2bd9ff" stroke-width="3"/>
    <circle cx="200" cy="200" r="90" fill="none" stroke="#e8ff2b" stroke-width="1.5"/>
  </g>

  <!-- fractura: el borde se desintegra en segmentos desplazados -->
  <g stroke-linecap="round">
    <path d="M 290 200 A 90 90 0 0 1 255 268" fill="none" stroke="#ff2b5e" stroke-width="4" transform="translate(14,-6)"/>
    <path d="M 290 200 A 90 90 0 0 1 255 268" fill="none" stroke="#2bd9ff" stroke-width="4" transform="translate(-10,10)"/>
    <path d="M 110 200 A 90 90 0 0 1 145 132" fill="none" stroke="#e8ff2b" stroke-width="3" transform="translate(-18,4) rotate(6 200 200)"/>
  </g>

  <!-- esquirlas: fragmentos que se escapan del círculo -->
  <g fill="none" stroke-width="2">
    <line x1="290" y1="200" x2="330" y2="188" stroke="#ff2b5e"/>
    <line x1="296" y1="214" x2="342" y2="230" stroke="#2bd9ff"/>
    <line x1="110" y1="200" x2="66" y2="206" stroke="#e8ff2b"/>
    <line x1="120" y1="160" x2="78" y2="130" stroke="#ff2b5e"/>
    <circle cx="334" cy="186" r="3" fill="#ff2b5e" stroke="none"/>
    <circle cx="346" cy="231" r="2.5" fill="#2bd9ff" stroke="none"/>
    <circle cx="60" cy="207" r="2.5" fill="#e8ff2b" stroke="none"/>
    <circle cx="74" cy="127" r="3" fill="#ff2b5e" stroke="none"/>
  </g>

  <!-- líneas de escaneo, el glitch que delata el error -->
  <g opacity="0.35" filter="url(#blur1)">
    <rect x="40" y="150" width="320" height="3" fill="#ff2b5e"/>
    <rect x="30" y="196" width="340" height="2" fill="#2bd9ff"/>
    <rect x="55" y="244" width="300" height="3" fill="#e8ff2b"/>
  </g>

  <!-- bloques de corrupción -->
  <g opacity="0.8">
    <rect x="150" y="80" width="26" height="8" fill="#ff2b5e"/>
    <rect x="178" y="80" width="18" height="8" fill="#2bd9ff"/>
    <rect x="230" y="310" width="34" height="7" fill="#e8ff2b"/>
    <rect x="266" y="310" width="14" height="7" fill="#ff2b5e"/>
  </g>

  <!-- centro: un pequeño núcleo que sí logró mantenerse estable -->
  <circle cx="200" cy="200" r="6" fill="#f4f4f4"/>
  <circle cx="200" cy="200" r="12" fill="none" stroke="#f4f4f4" stroke-width="1" opacity="0.5"/>

  <text x="200" y="370" text-anchor="middle" font-family="monospace" font-size="11" fill="#5a5d72">
    error_mas_bello_que_la_version_correcta.svg
  </text>
</svg>