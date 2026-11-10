<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="75%">
      <stop offset="0" stop-color="#27457a"/>
      <stop offset="0.6" stop-color="#152a52"/>
      <stop offset="1" stop-color="#0a1530"/>
    </radialGradient>
    <linearGradient id="gold" gradientUnits="userSpaceOnUse" x1="100" y1="80" x2="300" y2="320">
      <stop offset="0" stop-color="#fff3c4"/>
      <stop offset="0.35" stop-color="#f6c95a"/>
      <stop offset="0.7" stop-color="#e09a2b"/>
      <stop offset="1" stop-color="#b86a14"/>
    </linearGradient>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="1.1" fill="#ffffff" opacity="0.08"/>
    </pattern>
    <g id="enie">
      <g stroke="none">
        <rect x="118" y="140" width="36" height="170"/>
        <rect x="246" y="140" width="36" height="170"/>
        <polygon points="118,140 162,140 282,310 238,310"/>
        <rect x="98" y="140" width="64" height="13" rx="3"/>
        <rect x="98" y="297" width="76" height="13" rx="3"/>
        <rect x="226" y="140" width="76" height="13" rx="3"/>
      </g>
      <path d="M152 110 C166 86 186 86 200 99 S236 114 250 90" fill="none" stroke-width="15" stroke-linecap="round"/>
    </g>
    <path id="star" d="M0 -9 L2 -2 L9 0 L2 2 L0 9 L-2 2 L-9 0 L-2 -2 Z"/>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#dots)"/>

  <rect x="22" y="22" width="356" height="356" rx="20" fill="none" stroke="#f6c95a" stroke-width="3"/>
  <rect x="34" y="34" width="332" height="332" rx="12" fill="none" stroke="#f6c95a" stroke-width="1.2" stroke-dasharray="2 7" stroke-linecap="round" opacity="0.8"/>

  <g fill="#f6c95a">
    <use href="#star" x="200" y="22"/>
    <use href="#star" x="200" y="378"/>
    <use href="#star" x="22" y="200"/>
    <use href="#star" x="378" y="200"/>
  </g>

  <g fill="#fff3c4" opacity="0.85">
    <use href="#star" transform="translate(70 80) scale(0.9)"/>
    <use href="#star" transform="translate(330 110) scale(0.6)"/>
    <use href="#star" transform="translate(320 330) scale(1)"/>
    <use href="#star" transform="translate(75 320) scale(0.55)"/>
    <use href="#star" transform="translate(205 345) scale(0.45)"/>
    <use href="#star" transform="translate(300 62) scale(0.4)"/>
    <use href="#star" transform="translate(62 200) scale(0.4)"/>
  </g>

  <ellipse cx="200" cy="336" rx="110" ry="9" fill="#000" opacity="0.25"/>

  <use href="#enie" transform="translate(9 9)" fill="#060d20" stroke="#060d20" opacity="0.6"/>
  <use href="#enie" fill="url(#gold)" stroke="url(#gold)"/>

  <g fill="#ffffff" opacity="0.35">
    <rect x="123" y="158" width="5" height="134" rx="2.5"/>
    <rect x="251" y="158" width="5" height="134" rx="2.5"/>
  </g>
  <path d="M155 104 C167 88 184 88 198 97" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.4"/>
</svg>