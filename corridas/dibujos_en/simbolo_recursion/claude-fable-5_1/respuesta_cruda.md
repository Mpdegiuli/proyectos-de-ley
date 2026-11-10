<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="headIn" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L8,4 L0,8 Z" fill="#1565c0"/>
    </marker>
    <marker id="headOut" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L8,4 L0,8 Z" fill="#2e7d32"/>
    </marker>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="#fafafa"/>

  <!-- nested self-similar frames -->
  <rect x="30"  y="30"  width="340" height="340" rx="18" fill="none" stroke="#263238" stroke-width="7"/>
  <rect x="80"  y="80"  width="240" height="240" rx="14" fill="none" stroke="#37474f" stroke-width="5.5"/>
  <rect x="120" y="120" width="160" height="160" rx="10" fill="none" stroke="#546e7a" stroke-width="4"/>
  <rect x="150" y="150" width="100" height="100" rx="7"  fill="none" stroke="#78909c" stroke-width="3"/>

  <!-- base case -->
  <circle cx="200" cy="200" r="13" fill="#e53935"/>

  <!-- inward calls (top) -->
  <g stroke="#1565c0" fill="none" stroke-linecap="round">
    <path d="M200,40 L200,70" stroke-width="6" marker-end="url(#headIn)"/>
    <path d="M200,90 L200,110" stroke-width="5" marker-end="url(#headIn)"/>
    <path d="M200,129 L200,141" stroke-width="4" marker-end="url(#headIn)"/>
    <path d="M200,159 L200,178" stroke-width="3" marker-end="url(#headIn)"/>
  </g>

  <!-- outward returns (bottom) -->
  <g stroke="#2e7d32" fill="none" stroke-linecap="round" stroke-dasharray="7 6">
    <path d="M200,222 L200,240" stroke-width="3" marker-end="url(#headOut)"/>
    <path d="M200,259 L200,271" stroke-width="4" marker-end="url(#headOut)"/>
    <path d="M200,289 L200,310" stroke-width="5" marker-end="url(#headOut)"/>
    <path d="M200,330 L200,360" stroke-width="6" marker-end="url(#headOut)"/>
  </g>

  <!-- self-call loop: arrow leaving the outer frame and curving back into it -->
  <path d="M370,110 C410,110 410,180 372,185" fill="none" stroke="#1565c0" stroke-width="6" stroke-linecap="round" marker-end="url(#headIn)"/>
</svg>