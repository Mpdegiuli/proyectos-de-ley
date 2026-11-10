<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0" stop-color="#17345b"/>
      <stop offset="1" stop-color="#07111f"/>
    </radialGradient>
    <linearGradient id="inward" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#66f6ff"/>
      <stop offset="1" stop-color="#5a7dff"/>
    </linearGradient>
    <linearGradient id="return" x1="1" y1="1" x2="0" y2="0">
      <stop stop-color="#ff4fc3"/>
      <stop offset="1" stop-color="#ffad4d"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <marker id="cyanArrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto">
      <path d="M1 1l10 5-10 5z" fill="#66f6ff"/>
    </marker>
    <marker id="pinkArrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto">
      <path d="M1 1l10 5-10 5z" fill="#ff63c9"/>
    </marker>
  </defs>

  <rect width="400" height="400" rx="42" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="169" fill="none" stroke="#7deeff" stroke-opacity=".12" stroke-width="2"/>
  <circle cx="200" cy="200" r="157" fill="none" stroke="#ff67cc" stroke-opacity=".1" stroke-width="2" stroke-dasharray="4 10"/>

  <g fill="#09182a" stroke="url(#inward)" filter="url(#glow)">
    <rect x="64" y="64" width="272" height="272" rx="35" stroke-width="7"/>
    <rect x="110" y="110" width="180" height="180" rx="28" stroke-width="6"/>
    <rect x="147" y="147" width="106" height="106" rx="21" stroke-width="5"/>
    <rect x="174" y="174" width="52" height="52" rx="14" stroke-width="4"/>
  </g>

  <g fill="none" stroke="url(#inward)" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)">
    <path d="M92 201V107q0-15 15-15h186q15 0 15 15v186q0 15-15 15h-64" stroke-width="8" marker-end="url(#cyanArrow)"/>
    <path d="M130 200v-54q0-16 16-16h108q16 0 16 16v108q0 16-16 16h-28" stroke-width="7" marker-end="url(#cyanArrow)"/>
    <path d="M162 199v-21q0-16 16-16h44q16 0 16 16v44q0 16-16 16h-8" stroke-width="6" marker-end="url(#cyanArrow)"/>
  </g>

  <g fill="none" stroke="url(#return)" stroke-linecap="round" filter="url(#glow)">
    <path d="M200 218c-11 0-18-7-18-18s7-18 18-18 18 7 18 18" stroke-width="5" marker-end="url(#pinkArrow)"/>
    <path d="M186 246c-29-6-47-22-47-46 0-34 27-61 61-61" stroke-width="6" marker-end="url(#pinkArrow)"/>
    <path d="M173 286c-47-11-77-40-77-86 0-57 47-104 104-104" stroke-width="7" marker-end="url(#pinkArrow)"/>
    <path d="M146 337C83 316 45 268 45 200 45 114 114 45 200 45c70 0 129 46 149 109" stroke-width="8" marker-end="url(#pinkArrow)"/>
  </g>

  <g filter="url(#glow)">
    <path d="M200 185l15 15-15 15-15-15z" fill="#fff4b0" stroke="#ffad4d" stroke-width="4"/>
    <circle cx="92" cy="201" r="8" fill="#66f6ff"/>
    <circle cx="130" cy="200" r="7" fill="#66f6ff"/>
    <circle cx="162" cy="199" r="6" fill="#66f6ff"/>
  </g>
</svg>