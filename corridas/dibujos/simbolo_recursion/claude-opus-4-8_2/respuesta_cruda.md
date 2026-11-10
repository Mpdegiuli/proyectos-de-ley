<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#0d1117"/>
  
  <!-- Nested boxes representing recursion into itself -->
  <g fill="none" stroke-linecap="round">
    <rect x="40" y="40" width="320" height="320" rx="20" stroke="#4fc3f7" stroke-width="4"/>
    <rect x="90" y="90" width="220" height="220" rx="16" stroke="#4fc3f7" stroke-width="3.2" opacity="0.85"/>
    <rect x="130" y="130" width="140" height="140" rx="12" stroke="#4fc3f7" stroke-width="2.6" opacity="0.7"/>
    <rect x="160" y="160" width="80" height="80" rx="8" stroke="#4fc3f7" stroke-width="2" opacity="0.55"/>
    <rect x="180" y="180" width="40" height="40" rx="5" stroke="#4fc3f7" stroke-width="1.6" opacity="0.4"/>
  </g>

  <!-- Recursive arrow: function calling itself (circular loop with self-pointing arrow) -->
  <g stroke="#ffb74d" stroke-width="6" fill="none" stroke-linecap="round">
    <path d="M 200 210
             m -60 0
             a 60 60 0 1 1 90 48" />
  </g>
  <!-- arrowhead -->
  <polygon points="230,258 246,250 236,276" fill="#ffb74d"/>

  <!-- small node dot in center -->
  <circle cx="200" cy="200" r="7" fill="#81c784"/>
</svg>