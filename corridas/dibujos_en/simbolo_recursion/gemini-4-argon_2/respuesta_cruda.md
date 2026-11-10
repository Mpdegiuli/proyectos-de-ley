<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <rect width="400" height="400" fill="#1e1e1e"/>
  
  <defs>
    <!-- Marker for the call arrows -->
    <marker id="call-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#4fc1ff"/>
    </marker>
    
    <!-- Marker for the return arrows -->
    <marker id="ret-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ce9178"/>
    </marker>

    <!-- A single stack frame / function representation (Droste effect style) -->
    <g id="frame">
      <rect x="0" y="0" width="120" height="80" rx="6" fill="#252526" stroke="#569cd6" stroke-width="2.5"/>
      <!-- Header bar -->
      <path d="M 0 6 C 0 2.7 2.7 0 6 0 L 114 0 C 117.3 0 120 2.7 120 6 L 120 16 L 0 16 Z" fill="#569cd6"/>
      <!-- Window controls -->
      <circle cx="10" cy="8" r="3" fill="#ff5f56"/>
      <circle cx="20" cy="8" r="3" fill="#ffbd2e"/>
      <circle cx="30" cy="8" r="3" fill="#27c93f"/>
      <!-- Abstract code lines -->
      <line x1="12" y1="30" x2="50" y2="30" stroke="#9cdcfe" stroke-width="4" stroke-linecap="round"/>
      <!-- If condition (base case vs recursive step) -->
      <line x1="20" y1="42" x2="45" y2="42" stroke="#c586c0" stroke-width="4" stroke-linecap="round"/>
      <line x1="28" y1="54" x2="70" y2="54" stroke="#4ec9b0" stroke-width="4" stroke-linecap="round"/>
      <line x1="20" y1="66" x2="60" y2="66" stroke="#ce9178" stroke-width="4" stroke-linecap="round"/>
    </g>

    <!-- Base case frame -->
    <g id="base-frame">
      <rect x="0" y="0" width="120" height="80" rx="6" fill="#252526" stroke="#4ec9b0" stroke-width="3"/>
      <path d="M 0 6 C 0 2.7 2.7 0 6 0 L 114 0 C 117.3 0 120 2.7 120 6 L 120 16 L 0 16 Z" fill="#4ec9b0"/>
      <circle cx="10" cy="8" r="3" fill="#1e1e1e"/>
      <!-- Base case solid block (resolved value) -->
      <rect x="35" y="30" width="50" height="36" rx="4" fill="#4ec9b0" opacity="0.2"/>
      <path d="M 48 48 L 56 56 L 74 38" fill="none" stroke="#4ec9b0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </defs>

  <!-- Background Fractal / Binary Tree to reinforce Divide & Conquer / Recursion -->
  <g stroke="#333333" stroke-width="2" fill="none" opacity="0.6">
    <!-- Root to L1 -->
    <path d="M 200 40 L 100 100 M 200 40 L 300 100"/>
    <!-- L1 to L2 -->
    <path d="M 100 100 L 50 160 M 100 100 L 150 160 M 300 100 L 250 160 M 300 100 L 350 160"/>
    <!-- L2 to L3 -->
    <path d="M 50 160 L 25 220 M 50 160 L 75 220 M 150 160 L 125 220 M 150 160 L 175 220 M 250 160 L 225 220 M 250 160 L 275 220 M 350 160 L 325 220 M 350 160 L 375 220"/>
  </g>

  <!-- THE CALL STACK (Stepping down) -->
  
  <!-- Frame 1 (Top-Left) -->
  <g transform="translate(30, 30)">
    <use href="#frame"/>
    <!-- Mini-frame inside to show self-reference -->
    <use href="#frame" transform="translate(75, 42) scale(0.3)"/>
  </g>

  <!-- Frame 2 -->
  <g transform="translate(105, 115)">
    <use href="#frame"/>
    <use href="#frame" transform="translate(75, 42) scale(0.3)"/>
  </g>

  <!-- Frame 3 -->
  <g transform="translate(180, 200)">
    <use href="#frame"/>
    <use href="#frame" transform="translate(75, 42) scale(0.3)"/>
  </g>

  <!-- Frame 4 (Base Case, Bottom-Right) -->
  <g transform="translate(255, 285)">
    <use href="#base-frame"/>
  </g>


  <!-- RECURSIVE CALL ARROWS (Stepping Down - Blue) -->
  <!-- From inside the 'recursive call line' of one frame to the top of the next -->
  <path d="M 125 84 C 155 84, 150 95, 155 110" fill="none" stroke="#4fc1ff" stroke-width="2.5" marker-end="url(#call-arrow)"/>
  <path d="M 200 169 C 230 169, 225 180, 230 195" fill="none" stroke="#4fc1ff" stroke-width="2.5" marker-end="url(#call-arrow)"/>
  <path d="M 275 254 C 305 254, 300 265, 305 280" fill="none" stroke="#4fc1ff" stroke-width="2.5" marker-end="url(#call-arrow)"/>

  <!-- RETURN ARROWS (Unwinding the stack - Orange, Dashed) -->
  <!-- From the base case back up the chain -->
  <path d="M 255 335 C 210 335, 220 295, 210 284" fill="none" stroke="#ce9178" stroke-width="2.5" stroke-dasharray="5,3" marker-end="url(#ret-arrow)"/>
  <path d="M 180 250 C 135 250, 145 210, 135 199" fill="none" stroke="#ce9178" stroke-width="2.5" stroke-dasharray="5,3" marker-end="url(#ret-arrow)"/>
  <path d="M 105 165 C 60 165, 70 125, 60 114" fill="none" stroke="#ce9178" stroke-width="2.5" stroke-dasharray="5,3" marker-end="url(#ret-arrow)"/>

  <!-- Final Output Arrow (From top frame out) -->
  <path d="M 50 110 L 50 340 L 90 340" fill="none" stroke="#4ec9b0" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#call-arrow)"/>
  <circle cx="115" cy="340" r="16" fill="#4ec9b0"/>
  <path d="M 108 340 L 113 345 L 123 335" fill="none" stroke="#1e1e1e" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Big Self-Loop Icon in the Top-Right Corner (Universal symbol for recursion) -->
  <g transform="translate(310, 75)">
    <!-- Outer function box -->
    <rect x="-45" y="-45" width="90" height="90" rx="16" fill="none" stroke="#c586c0" stroke-width="4"/>
    <!-- Inner box -->
    <rect x="-20" y="-20" width="40" height="40" rx="8" fill="none" stroke="#c586c0" stroke-width="3"/>
    <!-- Innermost box -->
    <rect x="-6" y="-6" width="12" height="12" rx="2" fill="#c586c0"/>
    <!-- Loop arrow -->
    <path d="M 45 0 C 75 0, 75 -70, 0 -70 C -40 -70, -55 -45, -35 -25" fill="none" stroke="#4fc1ff" stroke-width="4" stroke-linecap="round" marker-end="url(#call-arrow)"/>
  </g>

</svg>