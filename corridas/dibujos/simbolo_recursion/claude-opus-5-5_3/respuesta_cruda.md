```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="h" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M0 0L10 5L0 10z" fill="#e8553d"/>
    </marker>
    <g id="lvl">
      <rect x="20" y="20" width="360" height="360" rx="30" fill="none" stroke="#2b4c7e" stroke-width="10"/>
      <path d="M60 340 C35 240 45 150 115 195" fill="none" stroke="#e8553d" stroke-width="10" stroke-linecap="round" marker-end="url(#h)"/>
    </g>
  </defs>
  <rect width="400" height="400" fill="#f7f4ec"/>
  <use href="#lvl"/>
  <use href="#lvl" transform="translate(117 117) scale(0.55)" opacity="0.92"/>
  <use href="#lvl" transform="translate(181.35 181.35) scale(0.3025)" opacity="0.84"/>
  <use href="#lvl" transform="translate(216.74 216.74) scale(0.1664)" opacity="0.76"/>
  <use href="#lvl" transform="translate(236.21 236.21) scale(0.0915)" opacity="0.68"/>
  <circle cx="257" cy="257" r="5" fill="#2b4c7e"/>
</svg>
```