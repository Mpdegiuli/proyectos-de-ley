```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="gradSun" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:gold; stop-opacity:1" />
      <stop offset="100%" style="stop-color:orange; stop-opacity:1" />
    </radialGradient>
    <radialGradient id="gradMoon" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:white; stop-opacity:1" />
      <stop offset="100%" style="stop-color:lightgrey; stop-opacity:1" />
    </radialGradient>
  </defs>
  <rect width="400" height="400" style="fill:darkblue"/>
  <circle cx="300" cy="100" r="50" fill="url(#gradSun)" />
  <circle cx="100" cy="300" r="50" fill="url(#gradMoon)">
    <animateTransform attributeName="transform" attributeType="XML" type="rotate"
                      from="0 100 300" to="360 100 300" dur="15s" repeatCount="indefinite"/>
  </circle>
  <path d="M50,200 q150,-100 300,0 q150,100 0,200 q-150,100 -300,0 q-150,-100 0,-200 z"
        fill="none" stroke="white" stroke-width="3">
    <animateTransform attributeName="transform" attributeType="XML" type="rotate"
                      from="0 200 300" to="360 200 300" dur="20s" repeatCount="indefinite"/>
  </path>
  <path d="M200,200 q100,-150 200,0 q100,150 0,200 q-100,150 -200,0 q-100,-150 0,-200 z"
        fill="none" stroke="white" stroke-width="3">
    <animateTransform attributeName="transform" attributeType="XML" type="rotate"
                      from="360 200 200" to="0 200 200" dur="25s" repeatCount="indefinite"/>
  </path>
</svg>
```