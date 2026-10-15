<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="bg" cx="50%" cy="42%" r="72%">
<stop offset="0%" stop-color="#2a1848"/>
<stop offset="100%" stop-color="#0b0714"/>
</radialGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#fff4c8"/>
<stop offset="38%" stop-color="#ffd056"/>
<stop offset="100%" stop-color="#b86a12"/>
</linearGradient>
<filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
<feGaussianBlur in="SourceGraphic" stdDeviation="4" result="b"/>
<feColorMatrix in="b" type="matrix" values="1 0 0 0 0  0 .75 0 0 0  0 0 .15 0 0  0 0 0 .65 0" result="c"/>
<feMerge>
<feMergeNode in="c"/>
<feMergeNode in="SourceGraphic"/>
</feMerge>
</filter>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<g transform="translate(200 200)" filter="url(#glow)">
<g fill="url(#gold)">
<rect x="-14" y="-152" width="28" height="304" rx="14"/>
<rect x="-14" y="-152" width="28" height="304" rx="14" transform="rotate(60)"/>
<rect x="-14" y="-152" width="28" height="304" rx="14" transform="rotate(120)"/>
</g>
<circle r="20" fill="#fff1b8"/>
</g>
</svg>