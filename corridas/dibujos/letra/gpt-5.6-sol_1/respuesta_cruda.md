<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#111827"/>
      <stop offset="1" stop-color="#312e81"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#22d3ee"/>
      <stop offset=".55" stop-color="#a78bfa"/>
      <stop offset="1" stop-color="#f472b6"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="400" height="400" rx="32" fill="url(#bg)"/>
  <circle cx="68" cy="70" r="3" fill="#fff" opacity=".65"/>
  <circle cx="337" cy="91" r="2" fill="#fff" opacity=".5"/>
  <circle cx="317" cy="326" r="3" fill="#fff" opacity=".45"/>
  <circle cx="93" cy="301" r="2" fill="#fff" opacity=".4"/>
  <path d="M78 330 174 73q7-19 26-19t26 19l96 257h-61l-22-65h-80l-21 65zm98-117h47l-23-73z"
        fill="url(#ink)" filter="url(#glow)"/>
  <path d="M78 330 174 73q7-19 26-19t26 19l96 257h-61l-22-65h-80l-21 65zm98-117h47l-23-73z"
        fill="url(#ink)"/>
</svg>