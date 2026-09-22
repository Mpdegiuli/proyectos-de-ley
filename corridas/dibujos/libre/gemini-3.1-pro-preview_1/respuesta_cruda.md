```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#1e1332"/>
      <stop offset="50%" stop-color="#0a0710"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>

    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00c6ff"/>
      <stop offset="100%" stop-color="#0072ff"/>
    </linearGradient>

    <linearGradient id="grad2" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f107a3"/>
      <stop offset="100%" stop-color="#7b2ff7"/>
    </linearGradient>

    <linearGradient id="grad3" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f9d423"/>
      <stop offset="100%" stop-color="#ff4e50"/>
    </linearGradient>

    <linearGradient id="grad4" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00b09b"/>
      <stop offset="100%" stop-color="#96c93d"/>
    </linearGradient>

    <filter id="glow1" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="glow2" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <g id="leaf">
      <path d