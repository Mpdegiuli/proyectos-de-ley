<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <rect width="400" height="400" fill="#1e1e1e"/>
  
  <defs>
    <!-- Marker for the self-calling recursive loop -->
    <marker id="loop-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ce9178"/>
    </marker>

    <!-- Base component representing a function/process frame -->
    <g id="frame">
      <!-- Outer Window -->
      <rect x="-150" y="-150" width="300" height="300" rx="16" fill="#252526" stroke="#569cd6" stroke-width="6"/>
      
      <!-- Window Header -->
      <path d="M -150 -110 L 150 -110" stroke="#569cd6" stroke-width="4"/>
      <circle cx="-125" cy="-130" r="7" fill="#f44747"/>
      <circle cx="-100" cy="-130" r="7" fill="#cca700"/>
      <circle cx="-75" cy="-130" r="7" fill="#4ec9b0"/>
      
      <!-- Divide and Conquer / Branching paths -->
      <path d="M 0 -110 C 0 -80, -80 -90, -80 -55" fill="none" stroke="#c586c0" stroke-width="5" stroke-dasharray="6,4"/>
      <path d="M 0 -110 C 0 -80, 80 -90, 80 -55" fill="none" stroke="#c586c0" stroke-width="5" stroke-dasharray="6,4"/>
      
      <!-- Self-Reference Loop (The Recursive Call) -->
      <path d="M 150 40 C 200 40, 200 -60, 100 -60" fill="none" stroke="#ce9178" stroke-width="6" marker-end="url(#loop-arrow)"/>
    </g>

    <!-- Sub-problem (Base Case) -->
    <g id="leaf">
      <rect x="-25" y="-25" width="50" height="50" rx="8" fill="#2d2d30" stroke="#4ec9b0" stroke-width="3"/>
      <circle cx="0" cy="0" r="8" fill="#4ec9b0"/>
    </g>
  </defs>

  <g transform="translate(200, 215)">
    
    <!-- LEVEL 1 (Outer Frame) -->
    <use href="#frame"/>
    <use href="#leaf" transform="translate(-95, -25)"/>
    
    <!-- LEVEL 2 -->
    <g transform="translate(20, 25) scale(0.55)">
      <use href="#frame"/>
      <use href="#leaf" transform="translate(-95, -25)"/>
      
      <!-- LEVEL 3 -->
      <g transform="translate(20, 25) scale(0.55)">
        <use href="#frame"/>
        <use href="#leaf" transform="translate(-95, -25)"/>
        
        <!-- LEVEL 4 -->
        <g transform="translate(20, 25) scale(0.55)">
          <use href="#frame"/>
          <use href="#leaf" transform="translate(-95, -25)"/>
          
          <!-- LEVEL 5 (Base Case Reached) -->
          <g transform="translate(20, 25) scale(0.55)">
            <rect x="-150" y="-150" width="300" height="300" rx="24" fill="#4ec9b0" stroke="#ffffff" stroke-width="12"/>
            <!-- Stop / Return Symbol -->
            <rect x="-60" y="-60" width="120" height="120" rx="16" fill="#1e1e1e"/>
          </g>
          
        </g>
      </g>
    </g>
    
  </g>

  <!-- Unwinding / Return cascade ( Bottom-up resolution ) -->
  <path d="M 244 259 C 210 290, 150 260, 120 200" fill="none" stroke="#4ec9b0" stroke-width="4" stroke-dasharray="4,8" marker-end="url(#loop-arrow)"/>
</svg>