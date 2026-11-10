<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#1b2838"/>
      <stop offset="100%" stop-color="#070b12"/>
    </radialGradient>
    <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2.2" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <marker id="in" viewBox="0 0 10 10" markerWidth="8" markerHeight="8" refX="8" refY="5" orient="auto">
      <path d="M0 1.2 L8.5 5 L0 8.8 Z" fill="#f6c15b"/>
    </marker>
    <marker id="out" viewBox="0 0 10 10" markerWidth="8" markerHeight="8" refX="8" refY="5" orient="auto">
      <path d="M0 1.2 L8.5 5 L0 8.8 Z" fill="#9eb0ff"/>
    </marker>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="176" fill="none" stroke="#67e8f9" stroke-width="1.2" opacity="0.16"/>
  <g fill="none" stroke="#7ee7df" stroke-linejoin="round" filter="url(#soft)">
    <rect x="52" y="52" width="296" height="296" rx="40" stroke-width="3"/>
    <rect x="104" y="104" width="192" height="192" rx="30" stroke-width="2.5" opacity="0.9"/>
    <rect x="150" y="150" width="100" height="100" rx="20" stroke-width="2.1" opacity="0.8"/>
  </g>
  <g fill="none" stroke="#f6c15b" stroke-linecap="round" filter="url(#soft)">
    <path d="M214 52 C214 16 368 16 368 142 C368 228 332 202 300 176" stroke-width="3.4" marker-end="url(#in)"/>
    <path d="M214 104 C214 80 320 80 320 150 C320 198 292 184 256 168" stroke-width="2.7" marker-end="url(#in)" opacity="0.92"/>
    <path d="M206 150 C206 136 264 136 264 170 C264 194 236 188 216 184" stroke-width="2.2" marker-end="url(#in)" opacity="0.88"/>
  </g>
  <path d="M188 214 C124 268 78 318 30 346" fill="none" stroke="#9eb0ff" stroke-width="2.4" stroke-linecap="round" marker-end="url(#out)"/>
  <circle cx="200" cy="200" r="20" fill="none" stroke="#f6c15b" stroke-width="2"/>
  <circle cx="200" cy="200" r="9" fill="#f6c15b"/>
</svg>