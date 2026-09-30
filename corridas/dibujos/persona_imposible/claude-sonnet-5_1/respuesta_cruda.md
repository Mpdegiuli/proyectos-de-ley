```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="skin" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f4c9a0"/>
      <stop offset="100%" stop-color="#e0a876"/>
    </linearGradient>
    <linearGradient id="cloth" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#5b7fae"/>
      <stop offset="100%" stop-color="#33507a"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="#eef2f7"/>

  <!-- Impossible torso: a Penrose-like triangular body -->
  <path d="M200 120
           L260 200
           L200 280
           L140 200
           Z"
        fill="url(#cloth)" stroke="#22314a" stroke-width="3"/>
  <path d="M200 120 L260 200 L230 210 L200 150 Z" fill="#7291bd"/>
  <path d="M200 280 L140 200 L170 190 L200 250 Z" fill="#7291bd"/>

  <!-- Neck connecting to two heads (impossible duplication) -->
  <rect x="185" y="90" width="30" height="40" fill="url(#skin)"/>

  <!-- Left head -->
  <circle cx="160" cy="70" r="30" fill="url(#skin)"/>
  <circle cx="150" cy="65" r="4" fill="#2b2b2b"/>
  <circle cx="170" cy="65" r="4" fill="#2b2b2b"/>
  <path d="M150 80 Q160 88 170 80" stroke="#7a4b30" stroke-width="2" fill="none"/>
  <path d="M140 50 Q160 30 180 50" stroke="#3a2a1a" stroke-width="6" fill="none"/>

  <!-- Right head, upside down -->
  <g transform="translate(240,70) rotate(180)">
    <circle cx="0" cy="0" r="30" fill="url(#skin)"/>
    <circle cx="-10" cy="-5" r="4" fill="#2b2b2b"/>
    <circle cx="10" cy="-5" r="4" fill="#2b2b2b"/>
    <path d="M-10 10 Q0 18 10 10" stroke="#7a4b30" stroke-width="2" fill="none"/>
    <path d="M-20 -20 Q0 -40 20 -20" stroke="#3a2a1a" stroke-width="6" fill="none"/>
  </g>

  <!-- Three arms, impossible connections -->
  <path d="M140 160 Q80 150 60 200" stroke="url(#skin)" stroke-width="18" fill="none" stroke-linecap="round"/>
  <path d="M260 160 Q320 150 340 200" stroke="url(#skin)" stroke-width="18" fill="none" stroke-linecap="round"/>
  <path d="M200 200 Q200 260 260 260" stroke="url(#skin)" stroke-width="16" fill="none" stroke-linecap="round"/>

  <!-- Hands -->
  <circle cx="58" cy="205" r="10" fill="url(#skin)"/>
  <circle cx="342" cy="205" r="10" fill="url(#skin)"/>
  <circle cx="262" cy="262" r="9" fill="url(#skin)"/>

  <!-- Impossible legs: they merge and swap, like an Escher staircase -->
  <path d="M180 280 
           C 160 320, 220 320, 200 360
           C 180 400, 260 400, 240 360
           C 220 320, 180 320, 200 280 Z"
        fill="url(#skin)" stroke="#c68a5a" stroke-width="2"/>

  <!-- Feet -->
  <ellipse cx="195" cy="368" rx="18" ry="8" fill="#3a2a1a"/>
  <ellipse cx="235" cy="368" rx="18" ry="8" fill="#3a2a1a"/>

  <!-- Extra subtle impossible shading lines to enhance paradox -->
  <path d="M200 120 L200 280" stroke="#1c2740" stroke-width="1" stroke-dasharray="4 3" opacity="0.4"/>
  <path d="M140 200 L260 200" stroke="#1c2740" stroke-width="1" stroke-dasharray="4 3" opacity="0.4"/>
</svg>
```