<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#1a1a2e"/>
  
  <!-- Nested spiraling squares to suggest self-similarity/recursion -->
  <g fill="none" stroke-linecap="round">
    <rect x="40" y="40" width="320" height="320" rx="20" stroke="#4ecca3" stroke-width="6"/>
    <rect x="80" y="80" width="240" height="240" rx="18" stroke="#52d6a8" stroke-width="5"/>
    <rect x="115" y="115" width="170" height="170" rx="16" stroke="#6fe0b4" stroke-width="4.5"/>
    <rect x="145" y="145" width="110" height="110" rx="14" stroke="#8ae8c2" stroke-width="4"/>
    <rect x="170" y="170" width="60" height="60" rx="10" stroke="#a8f0d2" stroke-width="3.5"/>
    <rect x="188" y="188" width="24" height="24" rx="6" stroke="#cffae8" stroke-width="3"/>
  </g>

  <!-- Arrow spiraling inward (pointing back into itself) -->
  <g fill="none" stroke="#e94560" stroke-width="7" stroke-linecap="round">
    <path d="M 200 330 
             A 130 130 0 0 1 70 200
             A 130 130 0 0 1 200 70
             A 130 130 0 0 1 300 265"/>
  </g>
  <!-- Arrowhead pointing inward -->
  <polygon points="300,265 278,245 320,240" fill="#e94560"/>

  <!-- Center dot: the base case -->
  <circle cx="200" cy="200" r="7" fill="#ffd369"/>
</svg>