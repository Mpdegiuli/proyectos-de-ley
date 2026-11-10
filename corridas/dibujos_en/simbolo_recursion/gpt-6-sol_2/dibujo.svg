<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M1 1 9 5 1 9" fill="none" stroke="#53d8f5" stroke-width="2"/>
    </marker>
    <marker id="up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M1 1 9 5 1 9" fill="none" stroke="#ffbf69" stroke-width="2"/>
    </marker>
    <g id="fork">
      <path d="M-13 15Q-40 30-68 65M13 15Q40 30 68 65" fill="none" stroke="#53d8f5" stroke-width="3.5" stroke-linecap="round" marker-end="url(#down)"/>
      <path d="M-81 65Q-63 12-22-4M81 65Q63 12 22-4" fill="none" stroke="#ffbf69" stroke-width="2.6" stroke-linecap="round" marker-end="url(#up)"/>
      <circle r="20" fill="#273d69" stroke="#8baeff" stroke-width="3"/>
      <path d="M0-9V2M0 2L-8 10M0 2L8 10" fill="none" stroke="#e9f3ff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <g id="leaf">
      <circle r="16" fill="#143e40" stroke="#74e6b0" stroke-width="3"/>
      <path d="M-7 0H7" stroke="#a6ffd0" stroke-width="3.5" stroke-linecap="round"/>
    </g>
    <g id="level1">
      <use href="#fork"/>
      <use href="#leaf" transform="translate(-72 82) scale(.72)"/>
      <use href="#leaf" transform="translate(72 82) scale(.72)"/>
    </g>
    <g id="level2">
      <use href="#fork"/>
      <use href="#level1" transform="translate(-72 82) scale(.72)"/>
      <use href="#level1" transform="translate(72 82) scale(.72)"/>
    </g>
    <g id="level3">
      <use href="#fork"/>
      <use href="#level2" transform="translate(-72 82) scale(.72)"/>
      <use href="#level2" transform="translate(72 82) scale(.72)"/>
    </g>
  </defs>
  <rect width="400" height="400" rx="26" fill="#101827"/>
  <use href="#level3" transform="translate(200 65)"/>
</svg>