```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Sky -->
  <rect width="400" height="400" fill="lightblue"/>

  <!-- Sun -->
  <circle cx="320" cy="80" r="40" fill="gold"/>
  <!-- Sun Rays -->
  <g stroke="gold" stroke-width="4">
    <line x1="320" y1="0" x2="320" y2="40"/>
    <line x1="320" y1="120" x2="320" y2="160"/>
    <line x1="280" y1="80" x2="240" y2="80"/>
    <line x1="360" y1="80" x2="400" y2="80"/>
    <line x1="285" y1="45" x2="245" y2="5"/>
    <line x1="355" y1="45" x2="395" y2="5"/>
    <line x1="285" y1="115" x2="245" y2="155"/>
    <line x1="355" y1="115" x2="395" y2="155"/>
  </g>

  <!-- Trees -->
  <g>
    <rect x="50" y="300" width="20" height="50" fill="saddlebrown"/>
    <circle cx="60" cy="290" r="30" fill="forestgreen"/>
    <rect x="330" y="300" width="20" height="50" fill="saddlebrown"/>
    <circle cx="340" cy="290" r="30" fill="forestgreen"/>
  </g>

  <!-- Grass -->
  <rect y="350" width="400" height="50" fill="greenyellow"/>

  <!-- Me -->
  <g>
    <!-- Body -->
    <rect x="185" y="240" width="30" height="70" fill="blue"/>
    <!-- Arms -->
    <rect x="160" y="260" width="30" height="10" fill="blue"/>
    <rect x="215" y="260" width="30" height="10" fill="blue"/>
    <!-- Legs -->
    <rect x="185" y="310" width="10" height="40" fill="blue"/>
    <rect x="205" y="310" width="10" height="40" fill="blue"/>
    <!-- Head -->
    <circle cx="200" cy="220" r="20" fill="peachpuff"/>
    <!-- Smile -->
    <path d="M190 220 Q200 230 210 220" stroke="black" stroke-width="2" fill="none"/>
    <!-- Eyes -->
    <circle cx="193" cy="215" r="2" fill="black"/>
    <circle cx="207" cy="215" r="2" fill="black"/>
  </g>

  <!-- Clouds -->
  <g fill="white">
    <circle cx="100" cy="100" r="20"/>
    <circle cx="120" cy="90" r="20"/>
    <circle cx="140" cy="100" r="20"/>
    <circle cx="280" cy="50" r="15"/>
    <circle cx="300" cy="40" r="15"/>
    <circle cx="320" cy="50" r="15"/>
  </g>

  <!-- Rainbow -->
  <g fill="none" stroke-width="10">
    <path d="M50 350 Q200 200 350 350" stroke="red"/>
    <path d="M70 350 Q200 220 330 350" stroke="orange"/>
    <path d="M90 350 Q200 240 310 350" stroke="yellow"/>
    <path d="M110 350 Q200 260 290 350" stroke="green"/>
    <path d="M130 350 Q200 280 270 350" stroke="blue"/>
    <path d="M150 350 Q200 300 250 350" stroke="indigo"/>
    <path d="M170 350 Q200 320 230 350" stroke="violet"/>
  </g>
</svg>
```