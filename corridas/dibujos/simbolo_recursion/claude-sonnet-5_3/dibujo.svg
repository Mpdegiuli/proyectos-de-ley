<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#ff7f32"/>
    </marker>
    <marker id="arrowRev" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#ff7f32"/>
    </marker>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#eef3f8"/>
    </radialGradient>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="url(#bg)"/>

  <!-- nested self-similar squares: recursive structure -->
  <g fill="none" stroke-linejoin="round">
    <rect x="30" y="30" width="340" height="340" stroke="#cfe3fb" stroke-width="4"/>
    <rect x="60" y="60" width="280" height="280" stroke="#a9cdf7" stroke-width="4"/>
    <rect x="90" y="90" width="220" height="220" stroke="#7fb0ef" stroke-width="4"/>
    <rect x="120" y="120" width="160" height="160" stroke="#528fe3" stroke-width="4"/>
    <rect x="150" y="150" width="100" height="100" stroke="#2f6fd0" stroke-width="4"/>
    <rect x="175" y="175" width="50" height="50" stroke="#1b4f91" stroke-width="4"/>
  </g>

  <!-- spiral path: recursive descent (in) and return (out) -->
  <path d="M200,200 L215,200 L215,185 L185,185 L185,215 L230,215 L230,170 L170,170 L170,230 L245,230 L245,155"
        fill="none" stroke="#ff7f32" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"
        marker-start="url(#arrowRev)" marker-end="url(#arrow)"/>

  <!-- base case: terminating point of recursion -->
  <circle cx="200" cy="200" r="11" fill="#e63946" stroke="#7a0e16" stroke-width="2"/>
</svg>