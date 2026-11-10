```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <rect width="400" height="400" fill="#0d1117"/>
  
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#58a6ff"/>
      <stop offset="100%" stop-color="#bc8cff"/>
    </linearGradient>
  </defs>

  <!-- Nested self-similar squares spiraling inward: recursion visual -->
  <g stroke="url(#g1)" fill="none" stroke-linejoin="round">
    <rect x="30" y="30" width="340" height="340" stroke-width="6" transform="rotate(0 200 200)"/>
    <rect x="65" y="65" width="270" height="270" stroke-width="5.5" transform="rotate(10 200 200)"/>
    <rect x="95" y="95" width="210" height="210" stroke-width="5" transform="rotate(20 200 200)"/>
    <rect x="120" y="120" width="160" height="160" stroke-width="4.5" transform="rotate(30 200 200)"/>
    <rect x="140" y="140" width="120" height="120" stroke-width="4" transform="rotate(40 200 200)"/>
    <rect x="157" y="157" width="86" height="86" stroke-width="3.5" transform="rotate(50 200 200)"/>
    <rect x="170" y="170" width="60" height="60" stroke-width="3" transform="rotate(60 200 200)"/>
    <rect x="181" y="181" width="38" height="38" stroke-width="2.5" transform="rotate(70 200 200)"/>
    <rect x="190" y="190" width="20" height="20" stroke-width="2" transform="rotate(80 200 200)"/>
  </g>

  <!-- curved arrow looping from outer frame into itself, showing self-call -->
  <path d="M 200 30 
           A 170 170 0 1 1 55 110" 
        stroke="#f0883e" stroke-width="5" fill="none" stroke-linecap="round"/>
  <polygon points="55,110 75,100 70,122" fill="#f0883e"/>

  <!-- small core dot: the base case -->
  <circle cx="200" cy="200" r="6" fill="#ffffff"/>
</svg>
```