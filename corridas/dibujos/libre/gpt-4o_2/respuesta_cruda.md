```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skyGradient" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" style="stop-color:rgb(135,206,235);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(70,130,180);stop-opacity:1" />
    </linearGradient>
    <radialGradient id="sunGradient" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" style="stop-color:rgb(255,255,224);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,215,0);stop-opacity:0" />
    </radialGradient>
    <radialGradient id="groundGradient" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" style="stop-color:rgb(34,139,34);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(85,107,47);stop-opacity:1" />
    </radialGradient>
    <linearGradient id="trunkGradient" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" style="stop-color:rgb(139,69,19);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(160,82,45);stop-opacity:1" />
    </linearGradient>
    <linearGradient id="treeLeavesGradient" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" style="stop-color:rgb(0,100,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(34,139,34);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="400" height="400" fill="url(#skyGradient)" />
  <circle cx="320" cy="80" r="50" fill="url(#sunGradient)" />
  <ellipse cx="200" cy="400" rx="400" ry="100" fill="url(#groundGradient)" />
  <!-- Tree Trunk -->
  <rect x="60" y="220" width="30" height="130" fill="url(#trunkGradient)" />
  <!-- Tree Leaves -->
  <circle cx="75" cy="200" r="40" fill="url(#treeLeavesGradient)" />
  <circle cx="55" cy="180" r="30" fill="url(#treeLeavesGradient)" />
  <circle cx="95" cy="180" r="30" fill="url(#treeLeavesGradient)" />
  <circle cx="75" cy="160" r="30" fill="url(#treeLeavesGradient)" />
  <!-- Clouds -->
  <ellipse cx="120" cy="80" rx="30" ry="15" fill="white" />
  <ellipse cx="140" cy="90" rx="40" ry="20" fill="white" />
  <ellipse cx="160" cy="80" rx="30" ry="15" fill="white" />
  <ellipse cx="260" cy="60" rx="30" ry="15" fill="white" />
  <ellipse cx="280" cy="70" rx="40" ry="20" fill="white" />
  <ellipse cx="300" cy="60" rx="30" ry="15" fill="white" />
  <!-- Path -->
  <path d="M200,400 C230,350 280,350 310,400 Z" fill="rgba(139,69,19,0.5)" />
</svg>
```