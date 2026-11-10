<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="arw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#1a4d8f"/>
    </marker>
    <marker id="arw2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#2e7d32"/>
    </marker>
    <marker id="arw3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#c62828"/>
    </marker>
    <marker id="arw4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="3.5" markerHeight="3.5" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#6a1b9a"/>
    </marker>
  </defs>

  <rect width="400" height="400" fill="#fafafa"/>
  <rect x="1" y="1" width="398" height="398" fill="none" stroke="#cccccc" stroke-width="2" rx="12"/>

  <!-- Level 1: outer box with self-loop arrow -->
  <g>
    <rect x="70" y="70" width="180" height="120" rx="14" fill="#ffffff" stroke="#1a4d8f" stroke-width="7"/>
    <!-- output arrow from box -->
    <path d="M 250 130 L 315 130" fill="none" stroke="#1a4d8f" stroke-width="7" marker-end="url(#arw)"/>
    <!-- loop back arrow -->
    <path d="M 315 130 C 355 130, 355 215, 315 215 C 285 215, 220 215, 160 205"
          fill="none" stroke="#1a4d8f" stroke-width="7" stroke-linecap="round" marker-end="url(#arw)"/>
    <!-- base-case arrow downward (terminal) -->
    <path d="M 160 190 L 160 235" fill="none" stroke="#7a7a7a" stroke-width="6" stroke-linecap="round" marker-end="url(#arw)"/>
    <rect x="135" y="238" width="50" height="26" rx="6" fill="#eeeeee" stroke="#7a7a7a" stroke-width="5"/>
  </g>

  <!-- Level 2: smaller copy, offset lower-left, connected by incoming arrow -->
  <g transform="translate(30,140) scale(0.62)">
    <rect x="70" y="70" width="180" height="120" rx="14" fill="#ffffff" stroke="#2e7d32" stroke-width="8"/>
    <path d="M 250 130 L 315 130" fill="none" stroke="#2e7d32" stroke-width="8" marker-end="url(#arw2)"/>
    <path d="M 315 130 C 355 130, 355 215, 315 215 C 285 215, 220 215, 160 205"
          fill="none" stroke="#2e7d32" stroke-width="8" stroke-linecap="round" marker-end="url(#arw2)"/>
    <path d="M 160 190 L 160 235" fill="none" stroke="#7a7a7a" stroke-width="7" stroke-linecap="round" marker-end="url(#arw2)"/>
    <rect x="135" y="238" width="50" height="26" rx="6" fill="#eeeeee" stroke="#7a7a7a" stroke-width="6"/>
  </g>

  <!-- Level 3: even smaller copy -->
  <g transform="translate(30,235) scale(0.42)">
    <rect x="70" y="70" width="180" height="120" rx="14" fill="#ffffff" stroke="#c62828" stroke-width="10"/>
    <path d="M 250 130 L 315 130" fill="none" stroke="#c62828" stroke-width="10" marker-end="url(#arw3)"/>
    <path d="M 315 130 C 355 130, 355 215, 315 215 C 285 215, 220 215, 160 205"
          fill="none" stroke="#c62828" stroke-width="10" stroke-linecap="round" marker-end="url(#arw3)"/>
    <path d="M 160 190 L 160 235" fill="none" stroke="#7a7a7a" stroke-width="9" stroke-linecap="round" marker-end="url(#arw3)"/>
    <rect x="135" y="238" width="50" height="26" rx="6" fill="#eeeeee" stroke="#7a7a7a" stroke-width="8"/>
  </g>

  <!-- Level 4: smallest copy, hint of infinite descent -->
  <g transform="translate(18,300) scale(0.28)">
    <rect x="70" y="70" width="180" height="120" rx="14" fill="#ffffff" stroke="#6a1b9a" stroke-width="12"/>
    <path d="M 250 130 L 315 130" fill="none" stroke="#6a1b9a" stroke-width="12" marker-end="url(#arw4)"/>
    <path d="M 315 130 C 355 130, 355 215, 315 215 C 285 215, 220 215, 160 205"
          fill="none" stroke="#6a1b9a" stroke-width="12" stroke-linecap="round" marker-end="url(#arw4)"/>
    <path d="M 160 190 L 160 235" fill="none" stroke="#7a7a7a" stroke-width="11" stroke-linecap="round" marker-end="url(#arw4)"/>
    <rect x="135" y="238" width="50" height="26" rx="6" fill="#eeeeee" stroke="#7a7a7a" stroke-width="10"/>
  </g>

  <!-- dotted descent line linking levels, suggesting depth -->
  <path d="M 95 300 C 85 320, 85 330, 80 345" fill="none" stroke="#999999" stroke-width="3" stroke-dasharray="2,7" stroke-linecap="round"/>

  <!-- small dots continuing into the corner: the recursion continues -->
  <circle cx="78" cy="362" r="4" fill="#6a1b9a"/>
  <circle cx="72" cy="378" r="3" fill="#6a1b9a"/>
  <circle cx="68" cy="390" r="2" fill="#6a1b9a"/>

  <!-- top-right accent: nested shrinking circles, another self-similarity cue -->
  <circle cx="345" cy="45" r="16" fill="none" stroke="#1a4d8f" stroke-width="4"/>
  <circle cx="345" cy="45" r="10" fill="none" stroke="#2e7d32" stroke-width="4"/>
  <circle cx="345" cy="45" r="5" fill="#c62828"/>
</svg>