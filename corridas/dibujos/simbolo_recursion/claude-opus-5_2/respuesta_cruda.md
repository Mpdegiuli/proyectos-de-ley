```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <rect width="400" height="400" fill="#FAF8F4"/>

  <!-- loop arrow: the call that returns to itself -->
  <g fill="none" stroke="#E8792B" stroke-width="10" stroke-linecap="round">
    <path d="M 170.5 367.4 A 170 170 0 1 1 229.5 367.4"/>
  </g>
  <polygon points="213.7,370.2 231.4,378.2 227.6,356.6" fill="#E8792B"/>

  <!-- self-similar nested frames: each contains a smaller copy of itself -->
  <g fill="none" stroke="#1F3A5F" stroke-linejoin="round">
    <rect x="90"    y="90"    width="220" height="220" rx="20"  stroke-width="7"/>
    <rect x="115"   y="115"   width="170" height="170" rx="15"  stroke-width="6.1"/>
    <rect x="134.5" y="134.5" width="131" height="131" rx="12"  stroke-width="5.3"/>
    <rect x="149.5" y="149.5" width="101" height="101" rx="9"   stroke-width="4.5"/>
    <rect x="161"   y="161"   width="78"  height="78"  rx="7"   stroke-width="3.9"/>
    <rect x="170"   y="170"   width="60"  height="60"  rx="5.5" stroke-width="3.3"/>
    <rect x="177"   y="177"   width="46"  height="46"  rx="4"   stroke-width="2.8"/>
    <rect x="182"   y="182"   width="36"  height="36"  rx="3"   stroke-width="2.3"/>
    <rect x="186.5" y="186.5" width="27"  height="27"  rx="2.5" stroke-width="1.9"/>
    <rect x="189.5" y="189.5" width="21"  height="21"  rx="2"   stroke-width="1.6"/>
  </g>

  <!-- base case at the deepest level -->
  <circle cx="200" cy="200" r="5.5" fill="#E8792B"/>

  <!-- descent into the smaller copies -->
  <g fill="#E8792B">
    <polygon points="-7.8,-7.2 -7.8,7.2 9.1,0" transform="translate(102.5,102.5) rotate(45)"/>
    <polygon points="-6,-5.5 -6,5.5 7,0"       transform="translate(124.8,124.8) rotate(45)"/>
    <polygon points="-4.8,-4.4 -4.8,4.4 5.6,0" transform="translate(142,142) rotate(45)"/>
  </g>
</svg>
```