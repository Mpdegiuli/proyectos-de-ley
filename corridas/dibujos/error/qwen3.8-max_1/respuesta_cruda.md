<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 400" font-family="'Courier New',monospace">
<title>Un error que me gusta más: el triángulo imposible</title>
<defs>
<radialGradient id="bg" cx="50%" cy="40%" r="75%">
<stop offset="0" stop-color="#1c3159"/>
<stop offset=".55" stop-color="#0f1d3d"/>
<stop offset="1" stop-color="#070d1e"/>
</radialGradient>
<radialGradient id="vig" cx="50%" cy="46%" r="70%">
<stop offset=".62" stop-color="#020610" stop-opacity="0"/>
<stop offset="1" stop-color="#020610" stop-opacity=".6"/>
</radialGradient>
<linearGradient id="gCA" gradientUnits="userSpaceOnUse" x1="200" y1="54" x2="89.2" y2="246">
<stop offset="0" stop-color="#ffb795"/>
<stop offset=".55" stop-color="#f26b4a"/>
<stop offset="1" stop-color="#c53a2b"/>
</linearGradient>
<linearGradient id="gAB" gradientUnits="userSpaceOnUse" x1="200" y1="54" x2="310.9" y2="246">
<stop offset="0" stop-color="#ffe49a"/>
<stop offset=".55" stop-color="#f7b13e"/>
<stop offset="1" stop-color="#d97c1c"/>
</linearGradient>
<linearGradient id="gBC" gradientUnits="userSpaceOnUse" x1="89.2" y1="246" x2="310.9" y2="246">
<stop offset="0" stop-color="#5fd9c7"/>
<stop offset=".5" stop-color="#2fb3a3"/>
<stop offset="1" stop-color="#147f78"/>
</linearGradient>
<pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
<path d="M20 0H0V20" fill="none" stroke="#7ea0e8" stroke-opacity=".06"/>
</pattern>
<filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
<feGaussianBlur stdDeviation="2.6" result="b"/>
<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<path id="loop" d="M206.5 98.3L275.8 218.3A13 13 0 0 1 269.3 229.5L130.7 229.5A13 13 0 0 1 124.2 218.3L193.5 98.3A13 13 0 0 1 206.5 98.3Z"/>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<rect width="400" height="400" fill="url(#grid)"/>
<rect width="400" height="400" fill="url(#vig)"/>
<circle cx="200" cy="182" r="155" fill="none" stroke="#7f9bd6" stroke-opacity=".16" stroke-dasharray="2 8">
<animateTransform attributeName="transform" type="rotate" from="0 200 182" to="360 200 182" dur="80s" repeatCount="indefinite"/>
</circle>
<path d="M200 170v24M188 182h24" stroke="#8fa8e0" stroke-opacity=".35"/>
<path d="M14 30V14h16M370 14h16v16M386 370v16h-16M30 386H14v-16" fill="none" stroke="#8fa8e0" stroke-opacity=".35" stroke-width="1.2"/>
<g stroke-linecap="round">
<path d="M60 40 84 80H36Z" fill="none" stroke="#8fa3c8" stroke-width="1.3" stroke-dasharray="4 3" opacity=".8"/>
<path d="M44 48 76 76M76 48 44 76" stroke="#ff5468" stroke-width="2" opacity=".85"/>
<text x="60" y="95" font-size="8" fill="#8fa3c8" text-anchor="middle" letter-spacing="1">versión correcta</text>
</g>
<g transform="rotate(7 322 58)" opacity=".85">
<rect x="270" y="40" width="104" height="36" rx="4" fill="none" stroke="#ff5468" stroke-width="2.5"/>
<text x="322" y="57" font-size="12.5" font-weight="bold" fill="#ff5468" text-anchor="middle" letter-spacing="2">RECHAZADO</text>
<text x="322" y="70" font-size="6.5" fill="#ff5468" text-anchor="middle" letter-spacing="1.5">MOTIVO: IMPOSIBLE</text>
</g>
<ellipse cx="200" cy="272" rx="112" ry="13" fill="#04081a" opacity=".55" filter="url(#soft)"/>
<g>
<animateTransform attributeName="transform" type="translate" values="0 0;0 -5;0 0" dur="7s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1"/>
<g>
<animateTransform attributeName="transform" type="rotate" values="-1.4 200 182;1.4 200 182;-1.4 200 182" dur="9s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1"/>
<g id="tribar" stroke="#0c1526" stroke-width="2"