```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Sky gradient -->
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#E0F6FF;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="sunGrad" cx="50%" cy="50%">
      <stop offset="0%" style="stop-color:#FFE680;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FFA500;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <!-- Background -->
  <rect width="400" height="400" fill="url(#skyGrad)"/>
  
  <!-- Sun -->
  <circle cx="320" cy="80" r="40" fill="url(#sunGrad)"/>
  
  <!-- Floating clouds -->
  <g opacity="0.8">
    <ellipse cx="80" cy="60" rx="30" ry="20" fill="white"/>
    <ellipse cx="110" cy="65" rx="25" ry="18" fill="white"/>
    <ellipse cx="50" cy="70" rx="20" ry="15" fill="white"/>
  </g>
  
  <g opacity="0.8">
    <ellipse cx="280" cy="120" rx="28" ry="18" fill="white"/>
    <ellipse cx="310" cy="125" rx="22" ry="15" fill="white"/>
    <ellipse cx="250" cy="130" rx="18" ry="12" fill="white"/>
  </g>
  
  <!-- Green rolling hills -->
  <ellipse cx="200" cy="280" rx="180" ry="80" fill="#2d8a2d"/>
  <ellipse cx="80" cy="320" rx="150" ry="60" fill="#3da03d"/>
  <ellipse cx="320" cy="310" rx="160" ry="70" fill="#2d8a2d"/>
  
  <!-- Trees on hills -->
  <g id="tree">
    <rect x="95" y="250" width="8" height="30" fill="#8B4513"/>
    <polygon points="99,240 115,255 83,255" fill="#228B22"/>
    <polygon points="99,250 118,270 80,270" fill="#2d8a2d"/>
  </g>
  
  <use href="#tree" x="80" y="0"/>
  <use href="#tree" x="160" y="-20"/>
  <use href="#tree" x="240" y="10"/>
  <use href="#tree" x="280" y="-15"/>
  
  <!-- Water body - peaceful lake -->
  <ellipse cx="200" cy="300" rx="140" ry="50" fill="#4DB8E8" opacity="0.6"/>
  <path d="M 80 300 Q 140 295 200 300 T 320 300" stroke="#87CEEB" stroke-width="2" fill="none" opacity="0.7"/>
  <path d="M 70 310 Q 140 308 200 312 T 330 310" stroke="#87CEEB" stroke-width="1.5" fill="none" opacity="0.5"/>
  
  <!-- People holding hands (diversity) -->
  <g id="person">
    <circle cx="0" cy="0" r="5" fill="#FFB6A3"/>
    <rect x="-3" y="5" width="6" height="8" fill="#FF6B6B"/>
    <rect x="-4" y="13" width="3" height="6" fill="#4A4A4A"/>
    <rect x="1" y="13" width="3" height="6" fill="#4A4A4A"/>
    <line x1="-3" y1="8" x2="-6" y2="11" stroke="#FFB6A3" stroke-width="1.5"/>
    <line x1="3" y1="8" x2="6" y2="11" stroke="#FFB6A3" stroke-width="1.5"/>
  </g>
  
  <use href="#person" x="140" y="220" fill="#FFB6A3"/>
  <use href="#person" x="160" y="220" fill="#E6B89C"/>
  <use href="#person" x="180" y="220" fill="#D4A574"/>
  <use href="#person" x="200" y="220" fill="#A0826D"/>
  <use href="#person" x="220" y="220" fill="#FFD7BE"/>
  
  <!-- Connecting line (unity) -->
  <line x1="135" y1="228" x2="225" y2="228" stroke="#FFD700" stroke-width="2" opacity="0.7"/>
  
  <!-- Birds flying -->
  <g id="bird" opacity="0.7">
    <path d="M 0 0 Q -3 -2 -6 0" stroke="#444" stroke-width="1.5" fill="none"/>
    <path d="M 0 0 Q 3 -2 6 0" stroke="#444" stroke-width="1.5" fill="none"/>
    <circle cx="0" cy="0" r="1" fill="#444"/>
  </g>
  
  <use href="#bird" x="120" y="100"/>
  <use href="#bird" x="160" y="90"/>
  <use href="#bird" x="280" y="110"/>
  
  <!-- Text: Hope -->
  <text x="200" y="370" font-family="Arial, sans-serif" font-size="28" font-weight="bold" text-anchor="middle" fill="#2d8a2d" opacity="0.8">UN MUNDO MEJOR</text>
  
  <!-- Small hearts scattered -->
  <g id="heart" opacity="0.6">
    <path d="M 0 -2 C -1 -3 -2.5 -3 -2.5 -2 C -2.5 -1 -1 0 0 1.5 C 1 0 2.5 -1 2.5 -2 C 2.5 -3 1 -3 0 -2 Z" fill="#FF69B4"/>
  </g>
  
  <use href="#heart" x="320" y="180"/>
  <use href="#heart" x="70" y="150"/>
  <use href="#heart" x="150" y="140"/>
  <use href="#heart" x="340" y="240"/>
</svg>
```