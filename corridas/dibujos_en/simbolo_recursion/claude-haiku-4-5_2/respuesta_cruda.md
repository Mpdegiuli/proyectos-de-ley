```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="400" height="400" fill="#f0f0f0"/>
  
  <!-- Title concept: Nested/recursive boxes getting smaller -->
  <!-- Outer box -->
  <rect x="50" y="50" width="300" height="300" fill="none" stroke="#2c3e50" stroke-width="8" rx="10"/>
  
  <!-- Second level box (smaller, centered) -->
  <rect x="100" y="100" width="200" height="200" fill="none" stroke="#3498db" stroke-width="6" rx="8"/>
  
  <!-- Third level box (even smaller) -->
  <rect x="140" y="140" width="120" height="120" fill="none" stroke="#e74c3c" stroke-width="4" rx="6"/>
  
  <!-- Fourth level box (innermost) -->
  <rect x="170" y="170" width="60" height="60" fill="none" stroke="#f39c12" stroke-width="2" rx="4"/>
  
  <!-- Arrow pointing inward to show recursion direction -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#9b59b6"/>
    </marker>
  </defs>
  
  <!-- Curved arrows showing recursive flow -->
  <path d="M 80 70 Q 70 50 90 40" fill="none" stroke="#9b59b6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <path d="M 320 80 Q 340 70 350 50" fill="none" stroke="#9b59b6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <path d="M 320 320 Q 340 330 350 350" fill="none" stroke="#9b59b6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <path d="M 80 320 Q 70 330 60 350" fill="none" stroke="#9b59b6" stroke-width="3" marker-end="url(#arrowhead)"/>
  
  <!-- Center dot to show the base case -->
  <circle cx="200" cy="200" r="4" fill="#2c3e50"/>
</svg>
```