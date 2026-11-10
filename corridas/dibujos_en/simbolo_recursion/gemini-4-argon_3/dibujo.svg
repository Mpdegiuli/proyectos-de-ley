<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <!-- Self-calling Loop Arrowhead (Cyan) -->
    <marker id="loop-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">
      <path d="M0,1 L9,5 L0,9 L2.5,5 z" fill="#38bdf8" />
    </marker>

    <!-- Return Path Arrowhead (Green) -->
    <marker id="ret-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,1 L9,5 L0,9 L2.5,5 z" fill="#4ade80" />
    </marker>

    <!-- Call Stack Frame (Recursive Step) -->
    <g id="frame">
      <!-- Box represents function scope -->
      <rect x="-46" y="-22" width="92" height="44" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2.5" />
      <!-- Top bar represents function signature/header -->
      <path d="M -46 -14 C -46 -18.5 -42.5 -22 -38 -22 L 38 -22 C 42.5 -22 46 -18.5 46 -14 L 46 -8 L -46 -8 Z" fill="#334155" />
      <!-- Dots represent parameters/local state -->
      <circle cx="-32" cy="-15" r="2.5" fill="#38bdf8" />
      <circle cx="-22" cy="-15" r="2.5" fill="#818cf8" />
      <!-- Inner socket represents the point of self-invocation -->
      <rect x="-32" y="-1" width="64" height="16" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1.5" />
      <circle cx="0" cy="7" r="4" fill="#38bdf8" />
    </g>

    <!-- Base Case Frame (Termination Condition) -->
    <g id="base-frame">
      <rect x="-46" y="-22" width="92" height="44" rx="8" fill="#052e16" stroke="#22c55e" stroke-width="2.5" />
      <path d="M -46 -14 C -46 -18.5 -42.5 -22 -38 -22 L 38 -22 C 42.5 -22 46 -18.5 46 -14 L 46 -8 L -46 -8 Z" fill="#14532d" />
      <!-- Concrete value / Stop condition -->
      <circle cx="-32" cy="-15" r="2.5" fill="#4ade80" />
      <rect x="-12" y="-3" width="24" height="20" rx="3" fill="#4ade80" />
    </g>

    <!-- Fractal Tree Branch (Visualizes exponential state space / divide & conquer) -->
    <g id="tree-branch">
      <line x1="0" y1="0" x2="-35" y2="40" stroke="#334155" stroke-width="3" stroke-linecap="round" />
      <line x1="0" y1="0" x2="35" y2="40" stroke="#334155" stroke-width="3" stroke-linecap="round" />
      <circle cx="0" cy="0" r="4.5" fill="#475569" />
    </g>
    <g id="tree-level-2">
      <use href="#tree-branch" />
      <use href="#tree-branch" transform="translate(-35, 40) scale(0.65)" />
      <use href="#tree-branch" transform="translate(35, 40) scale(0.65)" />
    </g>
    <g id="tree-level-3">
      <use href="#tree-level-2" />
      <use href="#tree-level-2" transform="translate(-35, 40) scale(0.65)" />
      <use href="#tree-level-2" transform="translate(35, 40) scale(0.65)" />
    </g>
    <g id="full-tree">
      <use href="#tree-level-3" />
      <use href="#tree-level-3" transform="translate(-35, 40) scale(0.65)" />
      <use href="#tree-level-3" transform="translate(35, 40) scale(0.65)" />
    </g>
  </defs>

  <!-- Background -->
  <rect width="400" height="400" fill="#090d16" />

  <!-- Subtle Grid / Structure -->
  <g stroke="#1e293b" stroke-width="1" opacity="0.4">
    <line x1="0" y1="70" x2="400" y2="70" stroke-dasharray="4 4" />
    <line x1="0" y1="160" x2="400" y2="160" stroke-dasharray="4 4" />
    <line x1="0" y1="250" x2="400" y2="250" stroke-dasharray="4 4" />
    <line x1="0" y1="340" x2="400" y2="340" stroke-dasharray="4 4" />
  </g>

  <!-- 1. BACKGROUND: Self-Similar Recursive Tree + Sierpinski Motif -->
  <g opacity="0.25" transform="translate(200, 30) scale(2.2)">
    <use href="#full-tree" />
  </g>

  <!-- 2. LEFT SIDE: Problem Decomposition (Divide / Shrink Input) -->
  <g transform="translate(35, 0)" opacity="0.85">
    <!-- Input size N -->
    <rect x="-12" y="52" width="24" height="36" rx="3" fill="#38bdf8" />
    <path d="M 0 96 L 0 124" stroke="#475569" stroke-width="2" stroke-dasharray="3 3" />
    <!-- Input size N-1 -->
    <rect x="-9" y="146" width="18" height="28" rx="2.5" fill="#38bdf8" opacity="0.8" />
    <path d="M 0 182 L 0 218" stroke="#475569" stroke-width="2" stroke-dasharray="3 3" />
    <!-- Input size N-2 -->
    <rect x="-6" y="240" width="12" height="20" rx="2" fill="#38bdf8" opacity="0.6" />
    <path d="M 0 268 L 0 312" stroke="#475569" stroke-width="2" stroke-dasharray="3 3" />
    <!-- Base Input (Atomic) -->
    <rect x="-4" y="334" width="8" height="12" rx="1.5" fill="#4ade80" />
  </g>

  <!-- 3. CENTER: The Call Stack (Nested Execution) -->
  <!-- Frame 1 (Initial Call, Scale 1.0) -->
  <use href="#frame" transform="translate(150, 70) scale(1.15)" />
  <!-- Frame 2 (Recursive Call 1, Scale 0.95) -->
  <use href="#frame" transform="translate(185, 160) scale(0.95)" />
  <!-- Frame 3 (Recursive Call 2, Scale 0.75) -->
  <use href="#frame" transform="translate(220, 250) scale(0.75)" />
  <!-- Frame 4 (Base Case, Scale 0.60) -->
  <use href="#base-frame" transform="translate(255, 340) scale(0.60)" />

  <!-- 4. FOREGROUND LEFT: Self-Calling Loops (Winding the Stack) -->
  <!-- Loop 1 to 2 -->
  <path d="M 150 78 C 60 78, 65 142, 130 142" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-linecap="round" marker-end="url(#loop-arrow)" />
  <!-- Loop 2 to 3 -->
  <path d="M 185 167 C 110 167, 115 235, 174 235" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" marker-end="url(#loop-arrow)" />
  <!-- Loop 3 to 4 -->
  <path d="M 220 255 C 160 255, 165 328, 218 328" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round" marker-end="url(#loop-arrow)" />

  <!-- 5. FOREGROUND RIGHT: Return & Combine (Unwinding the Stack) -->
  <!-- Return 4 to 3 -->
  <path d="M 283 340 C 325 340, 325 250, 265 250" fill="none" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="5 5" stroke-linecap="round" marker-end="url(#ret-arrow)" />
  <!-- Return 3 to 2 -->
  <path d="M 255 250 C 310 250, 310 160, 240 160" fill="none" stroke="#4ade80" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round" marker-end="url(#ret-arrow)" />
  <!-- Return 2 to 1 -->
  <path d="M 230 160 C 295 160, 295 70, 215 70" fill="none" stroke="#4ade80" stroke-width="3.5" stroke-dasharray="7 7" stroke-linecap="round" marker-end="url(#ret-arrow)" />
  
  <!-- Final Output Arrow -->
  <path d="M 150 40 L 150 18" fill="none" stroke="#4ade80" stroke-width="4" stroke-linecap="round" marker-end="url(#ret-arrow)" />

  <!-- 6. TOP RIGHT EMBLEM: Pure Concept of Self-Reference / Droste Effect -->
  <g transform="translate(335, 65)">
    <circle cx="0" cy="0" r="38" fill="#0f172a" stroke="#334155" stroke-width="2" />
    <!-- Outer Ouroboros-like self-loop -->
    <path d="M 24 -14 A 28 28 0 1 1 -14 -24" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" marker-end="url(#loop-arrow)" />
    <!-- Nested self-loop -->
    <path d="M 13 -8 A 15 15 0 1 1 -8 -13" fill="none" stroke="#818cf8" stroke-width="2.2" stroke-linecap="round" marker-end="url(#loop-arrow)" />
    <!-- Core / Base -->
    <circle cx="0" cy="0" r="4" fill="#4ade80" />
  </g>
</svg>