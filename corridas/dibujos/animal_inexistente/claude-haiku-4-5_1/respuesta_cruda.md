```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6b4ce6;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#a78bfa;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="eyeGrad" cx="35%" cy="35%">
      <stop offset="0%" style="stop-color:#ffd700;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff8c00;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <!-- Main body - blob-like -->
  <ellipse cx="200" cy="220" rx="90" ry="100" fill="url(#bodyGrad)"/>
  
  <!-- Neck -->
  <rect x="185" y="140" width="30" height="40" fill="url(#bodyGrad)" rx="15"/>
  
  <!-- Head - rounded square -->
  <rect x="160" y="80" width="80" height="80" fill="url(#bodyGrad)" rx="30"/>
  
  <!-- Ears - triangular with curves -->
  <path d="M 170 70 Q 160 40 180 50 Q 175 70 170 70" fill="#a78bfa"/>
  <path d="M 230 70 Q 240 40 220 50 Q 225 70 230 70" fill="#a78bfa"/>
  
  <!-- Eyes - large and alien-like -->
  <circle cx="185" cy="100" r="12" fill="url(#eyeGrad)"/>
  <circle cx="215" cy="100" r="12" fill="url(#eyeGrad)"/>
  <circle cx="187" cy="98" r="6" fill="#000"/>
  <circle cx="217" cy="98" r="6" fill="#000"/>
  
  <!-- Snout - beaked -->
  <ellipse cx="200" cy="120" rx="15" ry="20" fill="#9d7dd1"/>
  <path d="M 200 135 L 205 145 L 195 145 Z" fill="#ff69b4"/>
  
  <!-- Tentacle-like appendages on sides -->
  <path d="M 160 200 Q 140 210 135 240 Q 140 250 150 245" stroke="#a78bfa" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M 240 200 Q 260 210 265 240 Q 260 250 250 245" stroke="#a78bfa" stroke-width="12" fill="none" stroke-linecap="round"/>
  
  <!-- Back spikes/quills -->
  <path d="M 180 150 Q 170 130 175 110" stroke="#ff69b4" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M 200 145 Q 200 115 205 95" stroke="#ff69b4" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M 220 150 Q 230 130 225 110" stroke="#ff69b4" stroke-width="8" fill="none" stroke-linecap="round"/>
  
  <!-- Legs - four thick ones -->
  <ellipse cx="170" cy="310" rx="20" ry="45" fill="#9d7dd1"/>
  <ellipse cx="230" cy="310" rx="20" ry="45" fill="#9d7dd1"/>
  <ellipse cx="150" cy="315" rx="18" ry="40" fill="#9d7dd1"/>
  <ellipse cx="250" cy="315" rx="18" ry="40" fill="#9d7dd1"/>
  
  <!-- Feet -->
  <ellipse cx="170" cy="355" rx="22" ry="15" fill="#ff69b4"/>
  <ellipse cx="230" cy="355" rx="22" ry="15" fill="#ff69b4"/>
  <ellipse cx="150" cy="355" rx="20" ry="14" fill="#ff69b4"/>
  <ellipse cx="250" cy="355" rx="20" ry="14" fill="#ff69b4"/>
  
  <!-- Tail - curly and luminous -->
  <path d="M 280 250 Q 310 240 320 200 Q 330 160 310 140" stroke="#ffd700" stroke-width="14" fill="none" stroke-linecap="round"/>
  
  <!-- Tail glow particles -->
  <circle cx="300" cy="180" r="4" fill="#ffd700" opacity="0.8"/>
  <circle cx="315" cy="150" r="3" fill="#ff69b4" opacity="0.6"/>
  <circle cx="320" cy="200" r="3" fill="#ffd700" opacity="0.7"/>
  
  <!-- Spots on body -->
  <circle cx="190" cy="240" r="8" fill="#ff69b4" opacity="0.6"/>
  <circle cx="220" cy="260" r="7" fill="#ff69b4" opacity="0.6"/>
  <circle cx="200" cy="280" r="6" fill="#ffd700" opacity="0.5"/>
</svg>
```