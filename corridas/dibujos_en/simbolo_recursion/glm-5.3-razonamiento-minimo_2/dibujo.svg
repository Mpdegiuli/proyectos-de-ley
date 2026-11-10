<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#1a237e"/>
    </marker>
    <marker id="arrowSmall" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#1a237e"/>
    </marker>
  </defs>

  <rect width="400" height="400" fill="#fdfdfd"/>
  <circle cx="200" cy="200" r="188" fill="#e8eaf6"/>

  <!-- Recursive tree: function calling itself on smaller subproblems -->
  <!-- Root -->
  <line x1="200" y1="330" x2="200" y2="270" stroke="#1a237e" stroke-width="7" stroke-linecap="round"/>
  <line x1="200" y1="270" x2="150" y2="220" stroke="#1a237e" stroke-width="6" stroke-linecap="round"/>
  <line x1="200" y1="270" x2="250" y2="220" stroke="#1a237e" stroke-width="6" stroke-linecap="round"/>
  <circle cx="200" cy="335" r="14" fill="#1a237e"/>
  <circle cx="150" cy="215" r="10" fill="#3949ab"/>
  <circle cx="250" cy="215" r="10" fill="#3949ab"/>

  <line x1="150" y1="215" x2="118" y2="172" stroke="#3949ab" stroke-width="5" stroke-linecap="round"/>
  <line x1="150" y1="215" x2="164" y2="168" stroke="#3949ab" stroke-width="5" stroke-linecap="round"/>
  <line x1="250" y1="215" x2="236" y2="168" stroke="#3949ab" stroke-width="5" stroke-linecap="round"/>
  <line x1="250" y1="215" x2="282" y2="172" stroke="#3949ab" stroke-width="5" stroke-linecap="round"/>
  <circle cx="115" cy="166" r="7" fill="#5c6bc0"/>
  <circle cx="166" cy="162" r="7" fill="#5c6bc0"/>
  <circle cx="234" cy="162" r="7" fill="#5c6bc0"/>
  <circle cx="285" cy="166" r="7" fill="#5c6bc0"/>

  <line x1="115" y1="166" x2="96" y2="132" stroke="#5c6bc0" stroke-width="4" stroke-linecap="round"/>
  <circle cx="93" cy="127" r="5" fill="#9fa8da"/>
  <line x1="166" y1="162" x2="155" y2="128" stroke="#5c6bc0" stroke-width="4" stroke-linecap="round"/>
  <circle cx="153" cy="123" r="5" fill="#9fa8da"/>
  <line x1="234" y1="162" x2="245" y2="128" stroke="#5c6bc0" stroke-width="4" stroke-linecap="round"/>
  <circle cx="247" cy="123" r="5" fill="#9fa8da"/>
  <line x1="285" y1="166" x2="304" y2="132" stroke="#5c6bc0" stroke-width="4" stroke-linecap="round"/>
  <circle cx="307" cy="127" r="5" fill="#9fa8da"/>

  <!-- Self-call loop arrow from right branch back up into the tree -->
  <path d="M 285 166 C 340 130, 340 300, 262 300 C 232 300, 222 292, 210 288"
        fill="none" stroke="#1a237e" stroke-width="6" stroke-linecap="round"
        marker-end="url(#arrow)" stroke-dasharray="14 9"/>

  <!-- Base case: checkmark in a small box (the termination condition) -->
  <rect x="62" y="228" width="52" height="52" rx="10" fill="#ffffff" stroke="#2e7d32" stroke-width="5"/>
  <path d="M 74 255 L 84 267 L 103 242" fill="none" stroke="#2e7d32" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Arrow from tree to base case -->
  <path d="M 132 240 L 120 240" fill="none" stroke="#2e7d32" stroke-width="5" stroke-linecap="round" marker-end="url(#arrowSmall)" opacity="0.001"/>
  <path d="M 140 226 C 128 232, 120 240, 114 252" fill="none" stroke="#2e7d32" stroke-width="5" stroke-linecap="round" marker-end="url(#arrowSmall)"/>

  <!-- Nested self-similar frames (top-left): problem inside itself, shrinking -->
  <g fill="none" stroke="#1a237e" stroke-linejoin="round">
    <rect x="48" y="48" width="96" height="96" rx="8" stroke-width="5"/>
    <rect x="66" y="66" width="60" height="60" rx="6" stroke-width="4"/>
    <rect x="82" y="82" width="28" height="28" rx="5" stroke-width="3.5"/>
    <rect x="94" y="94" width="4" height="4" fill="#1a237e" stroke="none"/>
  </g>
  <!-- spiral dot at the heart of nesting -->
  <circle cx="96" cy="96" r="2.6" fill="#1a237e"/>

  <!-- Spiral (top-right): converging recursion -->
  <path d="M 340 70
           a 8 8 0 0 1 -8 8
           a 16 16 0 0 1 -16 -16
           a 30 30 0 0 1 30 -30
           a 48 48 0 0 1 48 48
           a 70 70 0 0 1 -70 70
           a 92 92 0 0 1 -92 -92
           a 116 116 0 0 1 116 -116"
        fill="none" stroke="#3949ab" stroke-width="6" stroke-linecap="round"/>
  <circle cx="332" cy="78" r="5" fill="#3949ab"/>

  <!-- Bottom-right: mirrored shrinking triangles, same shape at each scale -->
  <g fill="none" stroke="#1a237e" stroke-linejoin="round">
    <path d="M 300 345 L 360 345 L 330 288 Z" stroke-width="6"/>
    <path d="M 315 342 L 345 342 L 330 315 Z" stroke-width="4.5" fill="#c5cae9"/>
    <path d="M 323 340 L 337 340 L 330 326 Z" stroke-width="3.5" fill="#3949ab"/>
  </g>

  <!-- Bottom-left: brackets calling themselves, nested -->
  <g fill="none" stroke="#1a237e" stroke-width="5" stroke-linecap="round">
    <path d="M 55 300 L 72 300 L 72 348 L 55 348"/>
    <path d="M 345 300 L 328 300 L 328 348 L 345 348" transform="translate(0,0)"/>
    <path d="M 345 300 L 328 300 L 328 348 L 345 348"/>
    <path d="M 86 312 L 97 312 L 97 336 L 86 336" stroke-width="4"/>
    <path d="M 314 312 L 303 312 L 303 336 L 314 336" stroke-width="4"/>
  </g>
</svg>