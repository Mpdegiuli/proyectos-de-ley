<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="46%" cy="40%" r="78%">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset="1" stop-color="#D8E2EE"/>
    </radialGradient>
    <filter id="sh" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="7" stdDeviation="9" flood-color="#1B2C4E" flood-opacity="0.20"/>
    </filter>
    <filter id="glow" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- self-similar shrinking copies of the same problem -->
  <g fill="none" stroke-linejoin="round">
    <rect x="40" y="40" width="320" height="320" rx="27" stroke="#1B2C4E" stroke-width="11" filter="url(#sh)"/>
    <rect x="126.4" y="126.4" width="176" height="176" rx="15" stroke="#2B4A7B" stroke-width="8.5"/>
    <rect x="173.9" y="173.9" width="96.8" height="96.8" rx="8.2" stroke="#3B6499" stroke-width="6.4"/>
    <rect x="200" y="200" width="53.2" height="53.2" rx="4.5" stroke="#5480B2" stroke-width="4.8"/>
    <rect x="214.4" y="214.4" width="29.3" height="29.3" rx="2.5" stroke="#7099C6" stroke-width="3.6"/>
    <rect x="222.3" y="222.3" width="16.1" height="16.1" rx="1.4" stroke="#95B9DB" stroke-width="2.5"/>
  </g>

  <!-- the same call, repeated at every scale -->
  <g fill="none" stroke-linecap="round">
    <g transform="translate(40,40) scale(3.2)">
      <path d="M5.5 21.5C5 11 11 5 21.5 5.5C25 5.8 26 10 25.4 18" stroke="#E8552F" stroke-width="3.6"/>
      <polygon points="25.3 25.6 21.2 17.5 29.4 17.5" fill="#E8552F" stroke="none"/>
    </g>
    <g transform="translate(126.4,126.4) scale(1.76)">
      <path d="M5.5 21.5C5 11 11 5 21.5 5.5C25 5.8 26 10 25.4 18" stroke="#E8552F" stroke-width="3.6"/>
      <polygon points="25.3 25.6 21.2 17.5 29.4 17.5" fill="#E8552F" stroke="none"/>
    </g>
    <g transform="translate(173.9,173.9) scale(0.968)">
      <path d="M5.5 21.5C5 11 11 5 21.5 5.5C25 5.8 26 10 25.4 18" stroke="#E8552F" stroke-width="3.6"/>
      <polygon points="25.3 25.6 21.2 17.5 29.4 17.5" fill="#E8552F" stroke="none"/>
    </g>
    <g transform="translate(200,200) scale(0.532)">
      <path d="M5.5 21.5C5 11 11 5 21.5 5.5C25 5.8 26 10 25.4 18" stroke="#E8552F" stroke-width="3.6"/>
      <polygon points="25.3 25.6 21.2 17.5 29.4 17.5" fill="#E8552F" stroke="none"/>
    </g>
  </g>

  <!-- base case -->
  <rect x="226.4" y="226.4" width="9.2" height="9.2" rx="1.2" fill="#E8552F" filter="url(#glow)"/>
</svg>