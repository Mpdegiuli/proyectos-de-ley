<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-opacity="0.3" stroke-width="1"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="10" markerHeight="10" orient="auto-start-reverse">
      <path d="M 0 1 L 10 6 L 0 11 z" fill="#38bdf8" />
    </marker>
    <g id="b6">
      <line x1="0" y1="0" x2="0" y2="-20" stroke="#f8fafc" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="0" cy="-20" r="3" fill="#ffffff" stroke="#bae6fd" stroke-width="1"/>
    </g>
    <g id="b5">
      <line x1="0" y1="0" x2="0" y2="-30" stroke="#e0f2fe" stroke-width="2.5" stroke-linecap="round"/>
      <use href="#b6" x="0" y="-30" transform="rotate(-25)"/>
      <use href="#b6" x="0" y="-30" transform="rotate(25)"/>
    </g>
    <g id="b4">
      <line x1="0" y1="0" x2="0" y2="-45" stroke="#bae6fd" stroke-width="3.5" stroke-linecap="round"/>
      <use href="#b5" x="0" y="-45" transform="rotate(-25)"/>
      <use href="#b5" x="0" y="-45" transform="rotate(25)"/>
    </g>
    <g id="b3">
      <line x1="0" y1="0" x2="0" y2="-60" stroke="#7dd3fc" stroke-width="5" stroke-linecap="round"/>
      <use href="#b4" x="0" y="-60" transform="rotate(-25)"/>
      <use href="#b4" x="0" y="-60" transform="rotate(25)"/>
    </g>
    <g id="b2">
      <line x1="0" y1="0" x2="0" y2="-80" stroke="#38bdf8" stroke-width="7" stroke-linecap="round"/>
      <use href="#b3" x="0" y="-80" transform="rotate(-25)"/>
      <use href="#b3" x="0" y="-80" transform="rotate(25)"/>
    </g>
    <g id="b1">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#0ea5e9" stroke-width="9" stroke-linecap="round"/>
      <use href="#b2" x="0" y="-100" transform="rotate(-25)"/>
      <use href="#b2" x="0" y="-100" transform="rotate(25)"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="#020617"/>
  <rect x="15" y="15" width="370" height="370" rx="20" fill="#0f172a" stroke="#1e293b" stroke-width="4"/>
  <rect x="15" y="15" width="370" height="370" rx="20" fill="url(#grid)" />

  <circle cx="35" cy="35" r="4" fill="#ef4444"/>
  <circle cx="50" cy="35" r="4" fill="#eab308"/>
  <circle cx="65" cy="35" r="4" fill="#22c55e"/>

  <path d="M 240.1 50.3 A 155 155 0 0 1 240.1 349.7" stroke="#0284c7" stroke-width="14" stroke-opacity="0.3" fill="none" stroke-linecap="round"/>
  <path d="M 159.9 349.7 A 155 155 0 0 1 159.9 50.3" stroke="#0284c7" stroke-width="14" stroke-opacity="0.3" fill="none" stroke-linecap="round"/>

  <path d="M 240.1 50.3 A 155 155 0 0 1 240.1 349.7" stroke="#38bdf8" stroke-width="6" fill="none" marker-end="url(#arrow)" stroke-linecap="round"/>
  <path d="M 159.9 349.7 A 155 155 0 0 1 159.9 50.3" stroke="#38bdf8" stroke-width="6" fill="none" marker-end="url(#arrow)" stroke-linecap="round"/>

  <use href="#b1" transform="translate(200, 335) scale(0.85)"/>

  <g transform="translate(200, 335)">
    <polygon points="0,-14 14,0 0,14 -14,0" fill="#0f172a" stroke="#0ea5e9" stroke-width="3"/>
    <polygon points="0,-6 6,0 0,6 -6,0" fill="#38bdf8"/>
  </g>
</svg>