<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="1"/>
    </pattern>

    <marker id="mC" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="3.5" markerHeight="3.5" orient="auto">
      <path d="M 0,2 L 8,5 L 0,8 Z" fill="#a855f7"/>
    </marker>
    <marker id="mR" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="3.5" markerHeight="3.5" orient="auto">
      <path d="M 0,2 L 8,5 L 0,8 Z" fill="#f43f5e"/>
    </marker>

    <!-- Base Case / Stop Condition -->
    <g id="l0">
      <rect x="0" y="0" width="200" height="200" rx="20" fill="#4a044e" stroke="#f43f5e" stroke-width="8"/>
      <circle cx="100" cy="100" r="26" fill="#f43f5e" stroke="#fda4af" stroke-width="4"/>
      <!-- Internal Call execution mapping to Base Case -->
      <path d="M 0,50 C 50,50 100,45 100,74" fill="none" stroke="#a855f7" stroke-width="6" marker-end="url(#mC)"/>
      <!-- Internal Return originating from Base Case -->
      <path d="M 100,126 C 100,155 50,150 0,150" fill="none" stroke="#f43f5e" stroke-width="6" stroke-dasharray="10,10" marker-end="url(#mR)"/>
    </g>

    <!-- Recursive Call Depth 1 -->
    <g id="l1">
      <rect x="0" y="0" width="200" height="200" rx="20" fill="#3b0764" stroke="#d946ef" stroke-width="8"/>
      <path d