```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gradEar" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f1c40f;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#f39c12;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="gradBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2ecc71;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#27ae60;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="gradFace" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e74c3c;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#c0392b;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <circle cx="200" cy="200" r="120" fill="url(#gradBody)" />
  <ellipse cx="150" cy="150" rx="30" ry="40" fill="url(#gradEar)" />
  <ellipse cx="250" cy="150" rx="30" ry="40" fill="url(#gradEar)" />
  
  <circle cx="160" cy="175" r="10" fill="#fff" />
  <circle cx="240" cy="175" r="10" fill="#fff" />
  <circle cx="160" cy="175" r="5" fill="#000" />
  <circle cx="240" cy="175" r="5" fill="#000" />

  <path d="M150 230 Q200 260, 250 230" stroke="#3c3c3c" stroke-width="5" fill="none" />

  <path d="M200 160 Q220 190, 200 210 Q180 190, 200 160" fill="url(#gradFace)" />
  <path d="M200 160 Q190 170, 180 160" stroke="#000" stroke-width="2" fill="none" />
  <path d="M200 160 Q210 170, 220 160" stroke="#000" stroke-width="2" fill="none" />
</svg>
```