<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1a2a6c"/>
      <stop offset="0.4" stop-color="#b21f1f"/>
      <stop offset="0.7" stop-color="#fdbb2d"/>
      <stop offset="1" stop-color="#ff9966"/>
    </linearGradient>
    <radialGradient id="sunGlow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff7cc" stop-opacity="1"/>
      <stop offset="0.3" stop-color="#ffd700" stop-opacity="0.8"/>
      <stop offset="1" stop-color="#ff8c00" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="lake" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4a3a5c"/>
      <stop offset="1" stop-color="#1a1a3a"/>
    </linearGradient>
    <linearGradient id="mtn1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3d2b4a"/>
      <stop offset="1" stop-color="#1f1530"/>
    </linearGradient>
    <linearGradient id="mtn2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5a4070"/>
      <stop offset="1" stop-color="#2a1f40"/>
    </linearGradient>
  </defs>
  
  <!-- Sky -->
  <rect width="400" height="400" fill="url(#sky)"/>
  
  <!-- Stars -->
  <circle cx="50" cy="40" r="1" fill="#fff" opacity="0.8"/>
  <circle cx="120" cy="25" r="1.2" fill="#fff" opacity="0.9"/>
  <circle cx="200" cy="50" r="0.8" fill="#fff" opacity="0.7"/>
  <circle cx="350" cy="30" r="1" fill="#fff" opacity="0.8"/>
  <circle cx="80" cy="80" r="0.7" fill="#fff" opacity="0.6"/>
  
  <!-- Sun glow -->
  <circle cx="280" cy="180" r="90" fill="url(#sunGlow)"/>
  <circle cx="280" cy="180" r="28" fill="#fff7cc"/>
  
  <!-- Birds -->
  <path d="M 60 150 Q 65 145 70 150 Q 75 145 80 150" stroke="#1a1a3a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M 100 130 Q 104 126 108 130 Q 112 126 116 130" stroke="#1a1a3a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M 150 110 Q 153 107 156 110 Q 159 107 162 110" stroke="#1a1a3a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  
  <!-- Far mountains -->
  <path d="M 0 240 L 40 200 L 80 230 L 130 190 L 180 220 L 230 185 L 290 215 L 340 195 L 400 220 L 400 280 L 0 280 Z" fill="url(#mtn2)" opacity="0.8"/>
  
  <!-- Near mountains -->
  <path d="M 0 280 L 60 220 L 110 250 L 170 200 L 230 245 L 300 210 L 360 250 L 400 230 L 400 320 L 0 320 Z" fill="url(#mtn1)"/>
  
  <!-- Snow caps -->
  <path d="M 170 200 L 180 215 L 160 215 Z" fill="#e8d8f0" opacity="0.7"/>
  <path d="M 300 210 L 312 225 L 288 225 Z" fill="#e8d8f0" opacity="0.7"/>
  <path d="M 60 220 L 70 235 L 50 235 Z" fill="#e8d8f0" opacity="0.6"/>
  
  <!-- Lake -->
  <rect y="280" width="400" height="120" fill="url(#lake)"/>
  
  <!-- Sun reflection on water -->
  <ellipse cx="280" cy="300" rx="25" ry="3" fill="#ffd700" opacity="0.6"/>
  <ellipse cx="280" cy="315" rx="30" ry="2" fill="#ffd700" opacity="0.4"/>
  <ellipse cx="280" cy="330" rx="22" ry="2" fill="#ffd700" opacity="0.3"/>
  <ellipse cx="280" cy="345" rx="18" ry="1.5" fill="#ffd700" opacity="0.2"/>
  
  <!-- Water ripples -->
  <line x1="50" y1="320" x2="80" y2="320" stroke="#6a5a8c" stroke-width="1" opacity="0.5"/>
  <line x1="120" y1="340" x2="150" y2="340" stroke="#6a5a8c" stroke-width="1" opacity="0.4"/>
  <line x1="200" y1="360" x2="240" y2="360" stroke="#6a5a8c" stroke-width="1" opacity="0.4"/>
  <line x1="320" y1="350" x2="350" y2="350" stroke="#6a5a8c" stroke-width="1" opacity="0.5"/>
  
  <!-- Foreground silhouette trees -->
  <g fill="#0a0515">
    <ellipse cx="30" cy="395" rx="20" ry="8"/>
    <rect x="28" y="340" width="4" height="60"/>
    <ellipse cx="30" cy="335" rx="15" ry="30"/>
    
    <ellipse cx="80" cy="395" rx="25" ry="10"/>
    <rect x="78" y="330" width="5" height="70"/>
    <ellipse cx="80" cy="325" rx="18" ry="35"/>
    
    <ellipse cx="350" cy="395" rx="22" ry="9"/>
    <rect x="348" y="345" width="4" height="55"/>
    <ellipse cx="350" cy="340" rx="16" ry="28"/>
    
    <ellipse cx="380" cy="395" rx="18" ry="7"/>
    <rect x="378" y="355" width="4" height="45"/>
    <ellipse cx="380" cy="350" rx="13" ry="22"/>
  </g>
  
  <!-- Reeds/grass at shore -->
  <g stroke="#0a0515" stroke-width="1.5" stroke-linecap="round" fill="none">
    <path d="M 150 395 Q 152 380 150 365"/>
    <path d="M 155 395 Q 157 382 155 368"/>
    <path d="M 160 395 Q 158 380 160 370"/>
    <path d="M 220 395 Q 222 385 220 375"/>
    <path d="M 225 395 Q 223 383 225 372"/>
    <path d="M 280 395 Q 282 385 280 375"/>
    <path d="M 285 395 Q 283 382 285 370"/>
  </g>
</svg>