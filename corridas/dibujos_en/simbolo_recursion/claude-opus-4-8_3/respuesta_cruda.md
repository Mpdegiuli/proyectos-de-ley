<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#0d1b2a"/>

  <!-- Nested recursive squares spiraling inward -->
  <g fill="none" stroke-linecap="round">
    <rect x="40" y="40" width="320" height="320" stroke="#e0e1dd" stroke-width="4"/>
    <rect x="80" y="80" width="240" height="240" stroke="#a8dadc" stroke-width="3.5" transform="rotate(10 200 200)"/>
    <rect x="115" y="115" width="170" height="170" stroke="#457b9d" stroke-width="3" transform="rotate(20 200 200)"/>
    <rect x="145" y="145" width="110" height="110" stroke="#a8dadc" stroke-width="2.5" transform="rotate(30 200 200)"/>
    <rect x="170" y="170" width="60" height="60" stroke="#e0e1dd" stroke-width="2" transform="rotate(40 200 200)"/>
    <rect x="188" y="188" width="24" height="24" stroke="#f1faee" stroke-width="1.5" transform="rotate(50 200 200)"/>
  </g>

  <!-- Circular arrow indicating self-reference / loop back -->
  <g fill="none" stroke="#ffb703" stroke-width="6" stroke-linecap="round">
    <path d="M 200 60 A 140 140 0 1 1 60 200"/>
  </g>
  <polygon points="60,200 48,172 82,180" fill="#ffb703"/>

  <!-- Small inner self-pointing arrow -->
  <g fill="none" stroke="#fb8500" stroke-width="4" stroke-linecap="round">
    <path d="M 200 150 A 55 55 0 1 1 150 200"/>
  </g>
  <polygon points="150,200 141,181 164,186" fill="#fb8500"/>

  <!-- Central dot (base case) -->
  <circle cx="200" cy="200" r="7" fill="#f1faee"/>
</svg>