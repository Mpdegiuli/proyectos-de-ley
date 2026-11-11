<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#121626"/>
      <stop offset="100%" stop-color="#040508"/>
    </radialGradient>

    <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="#00FF88" />
    </marker>

    <g id="leaf">
      <circle cx="0" cy="0" r="10" fill="#FF0055" />
      <circle cx="0" cy="0" r="3" fill="#FFFFFF" />
    </g>

    <g id="d1">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#FF0055" stroke-width="8" stroke-linecap="round"/>
      <use href="#leaf" transform="translate(0, -100)"/>
    </g>

    <g id="d2">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#FF00AA" stroke-width="9" stroke-linecap="round"/>
      <circle cx="0" cy="-100" r="3" fill="#FFFFFF"/>
      <use href="#d1" transform="translate(0, -100) rotate(-40) scale(0.75)"/>
      <use href="#d1" transform="translate(0, -100) rotate(40) scale(0.75)"/>
    </g>

    <g id="d3">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#D400FF" stroke-width="10" stroke-linecap="round"/>
      <circle cx="0" cy="-100" r="3.5" fill="#FFFFFF"/>
      <use href="#d2" transform="translate(0, -100) rotate(-35) scale(0.75)"/>
      <use href="#d2" transform="translate(0, -100) rotate(35) scale(0.75)"/>
    </g>

    <g id="d4">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#8800FF" stroke-width="11" stroke-linecap="round"/>
      <circle cx="0" cy="-100" r="4" fill="#FFFFFF"/>
      <use href="#d3" transform="translate(0, -100) rotate(-30) scale(0.75)"/>
      <use href="#d3" transform="translate(0, -100) rotate(30) scale(0.75)"/>
    </g>

    <g id="d5">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#0055FF" stroke-width="12" stroke-linecap="round"/>
      <circle cx="0" cy="-100" r="4.5" fill="#FFFFFF"/>
      <use href="#d4" transform="translate(0, -100) rotate(-25) scale(0.75)"/>
      <use href="#d4" transform="translate(0, -100) rotate(25) scale(0.75)"/>
    </g>

    <g id="d6">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#00CCFF" stroke-width="13" stroke-linecap="round"/>
      <circle cx="0" cy="-100" r="5" fill="#FFFFFF"/>
      <use href="#d5" transform="translate(0, -100) rotate(-20) scale(0.75)"/>
      <use href="#d5" transform="translate(0, -100) rotate(20) scale(0.75)"/>
    </g>
    
    <g id="d7">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#00FFCC" stroke-width="14" stroke-linecap="round"/>
      <circle cx="0" cy="-100" r="5.5" fill="#FFFFFF"/>
      <use href="#d6" transform="translate(0, -100) rotate(-15) scale(0.75)"/>
      <use href="#d6" transform="translate(0, -100) rotate(15) scale(0.75)"/>
    </g>

    <g id="d8">
      <line x1="0" y1="0" x2="0" y2="-100" stroke="#00FF88" stroke-width="15" stroke-linecap="round"/>
      <circle cx="0" cy="-100" r="6" fill="#FFFFFF"/>
      <use href="#d7" transform="translate(0, -100) rotate(-10) scale(0.75)"/>
      <use href="#d7" transform="translate(0, -100) rotate(10) scale(0.75)"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <g fill="none" stroke-width="1.5" opacity="0.3" stroke-dasharray="6 6">
    <rect x="15" y="15" width="370" height="370" rx="20" stroke="#00FF88"/>
    <rect x="45" y="45" width="310" height="310" rx="18" stroke="#00FFCC"/>
    <rect x="75" y="75" width="250" height="250" rx="15" stroke="#00CCFF"/>
    <rect x="105" y="105" width="190" height="190" rx="12" stroke="#0055FF"/>
    <rect x="135" y="135" width="130" height="130" rx="10" stroke="#8800FF"/>
    <rect x="165" y="165" width="70" height="70" rx="8" stroke="#D400FF"/>
    <rect x="185" y="185" width="30" height="30" rx="5" stroke="#FF0055"/>
  </g>

  <use href="#d8" transform="translate(200, 350) scale(0.85)"/>

  <circle cx="200" cy="350" r="14" fill="#00FF88" />
  <circle cx="200" cy="350" r="5" fill="#040508" />
  <path d="M 213 355 C 270 410, 130 410, 187 355" fill="none" stroke="#00FF88" stroke-width="7" stroke-linecap="round" marker-end="url(#arrow)"/>

</svg>