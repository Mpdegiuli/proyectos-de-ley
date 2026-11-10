<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <rect width="400" height="400" fill="#1E1E2E"/>
  <defs>
    <!-- Base Case / Leaf Node -->
    <g id="leaf">
      <rect x="-14" y="-14" width="28" height="28" rx="6" fill="#F38BA8" fill-opacity="0.15" stroke="#F38BA8" stroke-width="2" stroke-dasharray="3 3"/>
      <circle cx="0" cy="0" r="10" fill="none" stroke="#F38BA8" stroke-width="2"/>
      <circle cx="0" cy="0" r="4" fill="#F38BA8"/>
    </g>

    <!-- Arrow Markers -->
    <marker id="arrowY" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
      <path d="M 0,0 L 5,3 L 0,6 z" fill="#F9E2AF"/>
    </marker>
    <marker id="arrowG" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
      <path d="M 0,0 L 5,3 L 0,6 z" fill="#A6E3A1"/>
    </marker>
    <marker id="arrowB" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
      <path d="M 0,0 L 5,3 L 0,6 z" fill="#89B4FA"/>
    </marker>
    <marker id="arrowLoop" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
      <path d="M 0,0 L 5,3 L 0,6 z" fill="#CBA6F7"/>
    </marker>

    <!-- Loop Back Icon Template (Self-call symbol) -->
    <g id="selfCall">
      <path d="M 9,-4 C 28,-12 28,-38 5,-17" fill="none" stroke="#CBA6F7" stroke-width="2.5" marker-end="url(#arrowLoop)"/>
    </g>

    <!-- Level 1 Branch -->
    <g id="l1">
      <rect x="-42" y="-20" width="84" height="102" rx="8" fill="#F9E2AF" fill-