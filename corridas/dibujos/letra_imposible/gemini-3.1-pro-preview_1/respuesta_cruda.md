<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0a0c" />
      <stop offset="100%" stop-color="#1c1d24" />
    </linearGradient>
    
    <linearGradient id="gold1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f9d976" />
      <stop offset="50%" stop-color="#e1b84f" />
      <stop offset="100%" stop-color="#a67c00" />
    </linearGradient>

    <linearGradient id="gold2" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffeba8" />
      <stop offset="40%" stop-color="#d4af37" />
      <stop offset="100%" stop-color="#8a6508" />
    </linearGradient>

    <linearGradient id="gold3" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fdf0b0" />
      <stop offset="60%" stop-color="#c59b27" />
      <stop offset="100%" stop-color="#5c4300" />
    </linearGradient>

    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="5" dy="8" stdDeviation="6" flood-color="#000" flood-opacity="0.8" />
    </filter>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bgGrad)" />

  <g transform="translate(0, 15)">
    <!-- A_top: Top portion of Left Leg -->
    <path