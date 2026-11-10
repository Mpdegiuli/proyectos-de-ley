<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#10182d"/>
      <stop offset="1" stop-color="#08101f"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <marker id="in" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0 0L10 5L0 10Z" fill="#5ee7ff"/>
    </marker>
    <marker id="out" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0 0L10 5L0 10Z" fill="#ffb45e"/>
    </marker>
  </defs>
  <rect width="400" height="400" rx="38" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="174" fill="none" stroke="#263858" stroke-width="3"/>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <rect x="58" y="58" width="284" height="284" rx="38" stroke="#5ee7ff" stroke-width="8"/>
    <rect x="103" y="103" width="194" height="194" rx="31" stroke="#50cce7" stroke-width="7"/>
    <rect x="143" y="143" width="114" height="114" rx="24" stroke="#43b1d0" stroke-width="6"/>
    <rect x="174" y="174" width="52" height="52" rx="15" stroke="#3794b4" stroke-width="5"/>
    <path d="M91 84C116 75 139 81 151 102" stroke="#5ee7ff" stroke-width="7" marker-end="url(#in)" filter="url(#glow)"/>
    <path d="M129 126C148 117 166 122 176 142" stroke="#5ee7ff" stroke-width="6" marker-end="url(#in)"/>
    <path d="M163 161C176 155 187 160 192 174" stroke="#5ee7ff" stroke-width="5" marker-end="url(#in)"/>
    <path d="M208 226C213 240 224 245 237 239" stroke="#ffb45e" stroke-width="5" marker-end="url(#out)"/>
    <path d="M224 258C234 278 252 283 271 274" stroke="#ffb45e" stroke-width="6" marker-end="url(#out)"/>
    <path d="M249 298C261 319 284 325 309 316" stroke="#ffb45e" stroke-width="7" marker-end="url(#out)" filter="url(#glow)"/>
  </g>
  <g transform="translate(200 200)" filter="url(#glow)">
    <path d="M0-15L15 0L0 15L-15 0Z" fill="#ffe27a" stroke="#fff4bd" stroke-width="4"/>
    <circle r="4.5" fill="#10182d"/>
  </g>
  <g fill="#5ee7ff">
    <circle cx="58" cy="200" r="5"/>
    <circle cx="103" cy="200" r="4.5"/>
    <circle cx="143" cy="200" r="4"/>
  </g>
  <g fill="#ffb45e">
    <circle cx="257" cy="200" r="4"/>
    <circle cx="297" cy="200" r="4.5"/>
    <circle cx="342" cy="200" r="5"/>
  </g>
</svg>