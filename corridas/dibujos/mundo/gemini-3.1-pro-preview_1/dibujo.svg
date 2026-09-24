<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="spaceBg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="50%" stop-color="#060913"/>
      <stop offset="100%" stop-color="#020307"/>
    </radialGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe"/>
      <stop offset="100%" stop-color="#4facfe"/>
    </linearGradient>
    <linearGradient id="magentaGrad" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff0844"/>
      <stop offset="100%" stop-color="#ffb199"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#43e97b"/>
      <stop offset="100%" stop-color="#38f9d7"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="50%" x2="100%" y2="50%">
      <stop offset="0%" stop-color="#f6d365"/>
      <stop offset="100%" stop-color="#fda085"/>
    </linearGradient>

    <filter id="softGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="hyperGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2" result="blur1"/>
      <feGaussianBlur stdDeviation="6" result="blur2"/>
      <feGaussianBlur stdDeviation="12" result="blur3"/>
      <feMerge>
        <feMergeNode in="blur3"/>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#spaceBg)"/>

  <g stroke="#ffffff" opacity="0.03" stroke-width="1">
    <path d="M 0 100 L 400 100 M 0 200 L 400 200 M 0 300 L 400 300" />
    <path d="M 100 0 L 100 400 M 200 0 L 200 400 M 300 0 L 300 400" />
    <circle cx="200" cy="200" r="100" />
    <circle cx="200" cy="200" r="150" />
    <circle cx="200" cy="200" r="200" />
  </g>

  <g stroke="#ffffff" fill="none" opacity="0.15">
    <path d="M 20 200 Q 200 60 380 200 Q 200 340 20 200" stroke-width="2" stroke-dasharray="8 12" filter="url(#softGlow)"/>
    <path d="M 50 200 Q 200 90 350 200 Q 200 310 50 200" stroke-width="0.5"/>
  </g>

  <g fill="#ffffff" opacity="0.4">
    <circle cx="60" cy="120" r="1"/>
    <circle cx="340" cy="80" r="1.5"/>
    <circle cx="370" cy="280" r="1"/>
    <circle cx="40" cy="310" r="2"/>
    <circle cx="120" cy="40" r="1"/>
    <circle cx="280" cy="360" r="1.5"/>
    <circle cx="240" cy="30" r="1"/>
    <circle cx="90" cy="360" r="1"/>
  </g>

  <g fill="none" stroke-width="1" opacity="0.15">
    <path d="M 60 120 L 120 40 L 200 100 L 340 80" stroke="#00f2fe"/>
    <path d="M 40 310 L 90 360 L 200 280 L 370 280" stroke="#ff0844"/>
    <path d="M 120 40 L 150 180 L 200 200 L 280 360" stroke="#43e97b"/>
  </g>

  <g fill="none" filter="url(#softGlow)">
    <circle cx="200" cy="200" r="140" stroke="#4facfe" stroke-width="0.5" stroke-dasharray="2 6" opacity="0.6"/>
    <circle cx="200" cy="200" r="115" stroke="#ffb199" stroke-width="1" stroke-dasharray="1 8 4 8" opacity="0.7"/>
    <circle cx="200" cy="200" r="80" stroke="#38f9d7" stroke-width="1.5" stroke-dasharray="15 10 5 10" opacity="0.8"/>
    <circle cx="200" cy="200" r="55" stroke="#f6d365" stroke-width="0.5" stroke-dasharray="3 3" opacity="0.9"/>
  </g>

  <g transform="rotate(15 200 200)" fill="none" opacity="0.4" filter="url(#softGlow)">
    <path d="M 200 90 L 295 145 L 295 255 L 200 310 L 105 255 L 105 145 Z" stroke="url(#cyanGrad)" stroke-width="1.5"/>
    <path d="M 200 200 L 200 90 M 200 200 L 295 145 M 200 200 L 295 255 M 200 200 L 200 310 M 200 200 L 105 255 M 200 200 L 105 145" stroke="url(#cyanGrad)" stroke-width="0.5"/>
  </g>

  <g fill="none" stroke-width="2" filter="url(#hyperGlow)">
    <ellipse cx="200" cy="200" rx="90" ry="20" stroke="url(#cyanGrad)" transform="rotate(30 200 200)"/>
    <ellipse cx="200" cy="200" rx="90" ry="20" stroke="url(#cyanGrad)" transform="rotate(90 200 200)"/>
    <ellipse cx="200" cy="200" rx="90" ry="20" stroke="url(#magentaGrad)" transform="rotate(150 200 200)"/>
    <ellipse cx="200" cy="200" rx="90" ry="20" stroke="url(#magentaGrad)" transform="rotate(210 200 200)"/>
  </g>

  <path d="M 120 200 C 120 120, 150 80, 200 80 C 260 80, 280 140, 280 200 C 280 260, 240 320, 200 320 C 140 320, 120 280, 120 200" stroke="url(#greenGrad)" stroke-width="2.5" fill="none" filter="url(#softGlow)"/>

  <path d="M 25 180 Q 130 150 180 50 T 340 100" stroke="url(#magentaGrad)" stroke-width="1.5" fill="none" opacity="0.6" filter="url(#softGlow)"/>
  <path d="M 375 220 Q 270 250 220 350 T 60 300" stroke="url(#cyanGrad)" stroke-width="1.5" fill="none" opacity="0.6" filter="url(#softGlow)"/>
  <path d="M 100 80 Q 200 200 300 320" stroke="url(#goldGrad)" stroke-width="1" stroke-dasharray="4 4" fill="none" opacity="0.8" filter="url(#softGlow)"/>

  <g filter="url(#hyperGlow)">
    <circle cx="200" cy="200" r="16" fill="#ffffff"/>
    <circle cx="200" cy="200" r="11" fill="#00f2fe"/>
    <circle cx="200" cy="200" r="5" fill="#ffffff"/>
  </g>

  <g stroke="#ffffff" stroke-width="1" opacity="0.5">
    <line x1="160" y1="130" x2="200" y2="80"/>
    <line x1="260" y1="120" x2="280" y2="200"/>
    <line x1="240" y1="270" x2="200" y2="320"/>
    <line x1="140" y1="280" x2="120" y2="200"/>
    <line x1="200" y1="200" x2="160" y2="130"/>
    <line x1="200" y1="200" x2="240" y2="270"/>
    <line x1="200" y1="200" x2="120" y2="200"/>
    <line x1="200" y1="200" x2="280" y2="200"/>
  </g>

  <g filter="url(#softGlow)">
    <circle cx="160" cy="130" r="3" fill="#ff0844"/>
    <circle cx="240" cy="270" r="3.5" fill="#00f2fe"/>
    <circle cx="120" cy="200" r="2.5" fill="#43e97b"/>
    <circle cx="280" cy="200" r="3" fill="#f6d365"/>
    <circle cx="200" cy="80" r="3" fill="#38f9d7"/>
    <circle cx="200" cy="320" r="4" fill="#ff0844"/>
    <circle cx="260" cy="120" r="2.5" fill="#4facfe"/>
    <circle cx="140" cy="280" r="3" fill="#38f9d7"/>
    <circle cx="180" cy="50" r="2" fill="#ffb199"/>
    <circle cx="220" cy="350" r="2" fill="#00f2fe"/>
  </g>

  <g stroke-width="1.5" stroke="#ffffff" opacity="0.4" fill="none">
    <path d="M 200 10 L 200 25 M 200 390 L 200 375"/>
    <path d="M 10 200 L 25 200 M 390 200 L 375 200"/>
  </g>
</svg>