```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="400" height="400" fill="#f8f9fa"/>
  
  <!-- Outer circle -->
  <circle cx="200" cy="200" r="180" fill="none" stroke="#2c3e50" stroke-width="3"/>
  
  <!-- First nested circle (medium) -->
  <circle cx="200" cy="200" r="120" fill="none" stroke="#3498db" stroke-width="2.5"/>
  
  <!-- Second nested circle (small) -->
  <circle cx="200" cy="200" r="60" fill="none" stroke="#e74c3c" stroke-width="2"/>
  
  <!-- Center dot -->
  <circle cx="200" cy="200" r="8" fill="#e74c3c"/>
  
  <!-- Arrows pointing inward (recursion direction) -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#2c3e50"/>
    </marker>
    <marker id="arrowhead-blue" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#3498db"/>
    </marker>
  </defs>
  
  <!-- Arrow from outer to middle circle (top) -->
  <path d="M 200 20 L 200 80" fill="none" stroke="#2c3e50" stroke-width="2.5" marker-end="url(#arrowhead)"/>
  
  <!-- Arrow from middle to inner circle (right) -->
  <path d="M 300 200 L 260 200" fill="none" stroke="#3498db" stroke-width="2" marker-end="url(#arrowhead-blue)"/>
  
  <!-- Arrow from outer to middle circle (bottom) -->
  <path d="M 200 380 L 200 320" fill="none" stroke="#2c3e50" stroke-width="2.5" marker-end="url(#arrowhead)"/>
  
  <!-- Arrow from middle to inner circle (left) -->
  <path d="M 100 200 L 140 200" fill="none" stroke="#3498db" stroke-width="2" marker-end="url(#arrowhead-blue)"/>
  
  <!-- Diagonal arrows showing the recursive spiral pattern -->
  <path d="M 270 130 L 230 170" fill="none" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="5,5" marker-end="url(#arrowhead-blue)"/>
  
  <path d="M 130 270 L 170 230" fill="none" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="5,5" marker-end="url(#arrowhead-blue)"/>
  
  <!-- Self-reference loop at center -->
  <path d="M 215 195 Q 235 180 240 200 Q 235 220 215 205" fill="none" stroke="#e74c3c" stroke-width="1.5" marker-end="url(#arrowhead-blue)"/>
</svg>
```