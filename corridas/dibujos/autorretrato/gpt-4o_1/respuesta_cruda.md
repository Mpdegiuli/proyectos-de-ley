```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="faceGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" style="stop-color:#f9d1a4;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#deaa87;stop-opacity:1" />
    </radialGradient>
    <radialGradient id="eyeGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" style="stop-color:#ffffff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#c8c8c8;stop-opacity:1" />
    </radialGradient>
    <radialGradient id="lipGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" style="stop-color:#e58c77;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#bc5f51;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <!-- Background -->
  <rect width="400" height="400" fill="#e0f7fa" />

  <!-- Face -->
  <ellipse cx="200" cy="200" rx="100" ry="130" fill="url(#faceGradient)" />

  <!-- Eyes -->
  <ellipse cx="160" cy="170" rx="15" ry="10" fill="url(#eyeGradient)" />
  <ellipse cx="240" cy="170" rx="15" ry="10" fill="url(#eyeGradient)" />
  
  <!-- Pupils -->
  <circle cx="160" cy="170" r="5" fill="#000" />
  <circle cx="240" cy="170" r="5" fill="#000" />

  <!-- Eyebrows -->
  <path d="M145,155 Q160,145 175,155" fill="none" stroke="#5c3d2e" stroke-width="3" />
  <path d="M225,155 Q240,145 255,155" fill="none" stroke="#5c3d2e" stroke-width="3" />

  <!-- Nose -->
  <path d="M200,180 Q190,210 200,230" fill="none" stroke="#8d6e63" stroke-width="2" />

  <!-- Mouth -->
  <path d="M180,250 Q200,270 220,250" fill="none" stroke="url(#lipGradient)" stroke-width="3" />

  <!-- Hair -->
  <path d="M130,90 Q200,40 270,90 T200,140 Z" fill="#5c3d2e" />

  <!-- Neck -->
  <rect x="180" y="280" width="40" height="40" fill="url(#faceGradient)" />

  <!-- Shoulders -->
  <path d="M100,320 C160,290 240,290 300,320 Q200,370 100,320 Z" fill="#8e9eab" />
</svg>
```