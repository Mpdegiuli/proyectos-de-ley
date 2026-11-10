```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#ffcc33"/>
    </marker>
    <g id="lvl">
      <rect x="40" y="40" width="320" height="320" rx="18" fill="#1d2b4a" stroke="#6fc3ff" stroke-width="8"/>
      <circle cx="80" cy="80" r="12" fill="#6fc3ff"/>
      <path d="M86,96 Q96,170 140,172" fill="none" stroke="#ffcc33" stroke-width="9" stroke-linecap="round" marker-end="url(#ah)"/>
    </g>
  </defs>
  <rect width="400" height="400" fill="#0e1424"/>
  <use href="#lvl"/>
  <g transform="translate(148 148) scale(0.6) translate(-40 -40)">
    <use href="#lvl"/>
    <g transform="translate(148 148) scale(0.6) translate(-40 -40)">
      <use href="#lvl"/>
      <g transform="translate(148 148) scale(0.6) translate(-40 -40)">
        <use href="#lvl"/>
        <g transform="translate(148 148) scale(0.6) translate(-40 -40)">
          <use href="#lvl"/>
          <g transform="translate(148 148) scale(0.6) translate(-40 -40)">
            <rect x="40" y="40" width="320" height="320" rx="18" fill="#1d2b4a" stroke="#6fc3ff" stroke-width="8"/>
            <circle cx="200" cy="200" r="90" fill="#ff5d73"/>
          </g>
        </g>
      </g>
    </g>
  </g>
</svg>
```