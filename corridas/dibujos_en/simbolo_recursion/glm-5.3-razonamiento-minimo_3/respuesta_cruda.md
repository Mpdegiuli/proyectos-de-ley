<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#1a237e"/>
    </marker>
  </defs>

  <rect width="400" height="400" fill="#fafafa"/>
  <circle cx="200" cy="200" r="185" fill="#ffffff" stroke="#1a237e" stroke-width="6"/>

  <!-- nested self-similar squares (droste / recursion) -->
  <g stroke="#1a237e" fill="none" stroke-linejoin="round">
    <rect x="100" y="100" width="200" height="200" stroke-width="9" rx="10"/>
    <rect x="130" y="130" width="140" height="140" stroke-width="7" rx="8"/>
    <rect x="155" y="155" width="90"  height="90"  stroke-width="5" rx="6"/>
    <rect x="175" y="175" width="50"  height="50"  stroke-width="4" rx="4"/>
  </g>

  <!-- base case: filled dot at the center -->
  <circle cx="200" cy="200" r="9" fill="#c62828"/>

  <!-- spiral arrow flowing inward: self-call -->
  <path d="M 330 70
           A 120 120 0 0 1 330 330
           A 95 95 0 0 1 330 100
           A 70 70 0 0 1 330 300
           A 48 48 0 0 1 320 130"
        fill="none" stroke="#c62828" stroke-width="7"
        stroke-linecap="round" marker-end="url(#arrow)"/>

  <!-- ouroboros: function calling itself -->
  <g transform="translate(200,200)">
    <circle r="52" fill="none" stroke="#1a237e" stroke-width="5" stroke-dasharray="120 210"/>
    <path d="M -30 -42 q -14 -18 8 -22 l 22 6 -10 14 q -10 -8 -20 2 z" fill="#1a237e"/>
  </g>

  <!-- small arrows on nested boxes pointing to smaller copy (self-similarity) -->
  <g stroke="#c62828" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M 112 140 L 128 148" marker-end="url(#arrow)"/>
    <path d="M 140 158 L 154 165" marker-end="url(#arrow)"/>
    <path d="M 164 176 L 176 182" marker-end="url(#arrow)"/>
  </g>
</svg>