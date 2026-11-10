<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#1565c0"/>
    </marker>
    <marker id="b" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#2e7d32"/>
    </marker>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="#fafafa"/>

  <!-- nested self-similar frames -->
  <rect x="30" y="30" width="340" height="340" rx="24" fill="none" stroke="#1565c0" stroke-width="8"/>
  <rect x="85" y="85" width="230" height="230" rx="18" fill="none" stroke="#1565c0" stroke-width="6" opacity="0.85"/>
  <rect x="125" y="125" width="150" height="150" rx="13" fill="none" stroke="#1565c0" stroke-width="4.5" opacity="0.7"/>
  <rect x="153" y="153" width="94" height="94" rx="9" fill="none" stroke="#1565c0" stroke-width="3.5" opacity="0.6"/>
  <rect x="172" y="172" width="56" height="56" rx="6" fill="none" stroke="#1565c0" stroke-width="2.5" opacity="0.5"/>

  <!-- base case: solid dot at the center -->
  <circle cx="200" cy="200" r="11" fill="#c62828"/>

  <!-- arrows diving inward (recursive calls) -->
  <path d="M55,55 Q75,60 92,92" fill="none" stroke="#1565c0" stroke-width="6" marker-end="url(#a)"/>
  <path d="M105,105 Q120,110 131,131" fill="none" stroke="#1565c0" stroke-width="5" marker-end="url(#a)"/>
  <path d="M140,140 Q152,144 158,158" fill="none" stroke="#1565c0" stroke-width="4" marker-end="url(#a)"/>
  <path d="M165,165 Q173,168 177,177" fill="none" stroke="#1565c0" stroke-width="3" marker-end="url(#a)"/>

  <!-- arrows returning outward (unwinding) -->
  <path d="M223,223 Q230,232 235,235" fill="none" stroke="#2e7d32" stroke-width="3" marker-end="url(#b)"/>
  <path d="M242,242 Q252,254 260,260" fill="none" stroke="#2e7d32" stroke-width="4" marker-end="url(#b)"/>
  <path d="M269,269 Q282,284 294,294" fill="none" stroke="#2e7d32" stroke-width="5" marker-end="url(#b)"/>
  <path d="M308,308 Q326,328 344,344" fill="none" stroke="#2e7d32" stroke-width="6" marker-end="url(#b)"/>
</svg>