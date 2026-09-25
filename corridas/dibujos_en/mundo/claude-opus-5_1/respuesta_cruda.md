<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<radialGradient id="sky" cx="50%" cy="45%" r="75%">
<stop offset="0%" stop-color="#16243c"/>
<stop offset="60%" stop-color="#0c1322"/>
<stop offset="100%" stop-color="#05070d"/>
</radialGradient>
<linearGradient id="globe" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#3fa9d8"/>
<stop offset="45%" stop-color="#1d6fa5"/>
<stop offset="100%" stop-color="#0a2c4a"/>
</linearGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="#7fd4ff" stop-opacity="0.45"/>
<stop offset="60%" stop-color="#2b7fb8" stop-opacity="0.12"/>
<stop offset="100%" stop-color="#000000" stop-opacity="0"/>
</radialGradient>
<linearGradient id="warm" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#ffd98a" stop-opacity="0.85"/>
<stop offset="100%" stop-color="#ff9c5b" stop-opacity="0"/>
</linearGradient>
<clipPath id="ball"><circle cx="200" cy="200" r="110"/></clipPath>
<filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
</defs>

<rect width="400" height="400" fill="url(#sky)"/>

<g fill="#ffffff">
<circle cx="32" cy="46" r="1.4" opacity=".8"/><circle cx="78" cy="22" r="1" opacity=".5"/>
<circle cx="140" cy="38" r="1.2" opacity=".6"/><circle cx="342" cy="30" r="1.5" opacity=".75"/>
<circle cx="378" cy="96" r="1" opacity=".5"/><circle cx="24" cy="188" r="1.1" opacity=".6"/>
<circle cx="366" cy="212" r="1.3" opacity=".7"/><circle cx="46" cy="330" r="1" opacity=".5"/>
<circle cx="120" cy="376" r="1.2" opacity=".6"/><circle cx="300" cy="366" r="1.4" opacity=".7"/>
<circle cx="256" cy="26" r="1" opacity=".45"/><circle cx="14" cy="112" r="1" opacity=".45"/>
<circle cx="388" cy="300" r="1.1" opacity=".55"/><circle cx="200" cy="392" r="1" opacity=".4"/>
</g>

<circle cx="200" cy="200" r="175" fill="url(#glow)"/>

<circle cx="200" cy="200" r="110" fill="url(#globe)"/>

<g clip-path="url(#ball)">
  <g fill="#7ee0a8" opacity=".85">
    <path d="M110 128c18-14 46-16 62-6s34 6 44 18-4 26-20 28-30 14-46 8-30-10-38-22-14-18-2-26z"/>
    <path d="M150 210c14-6 22 6 34 8s22 14 18 28-6 30-16 40-20 22-30 12-6-26-10-38-14-18-10-30 2-16 14-20z"/>
    <path d="M232 126c14-8 34-4 44 6s16 4 24 12-2 16-12 18-16 10-26 6-22-6-30-16-14-20 0-26z"/>
    <path d="M250 200c16-4 34 2 42 14s6 28-4 38-26 14-34 4 0-22 0-32-18-20-4-24z"/>
    <path d="M96 262c10-8 24 0 28 10s-4 22-14 22-20-8-20-18 0-10 6-14z"/>
  </g>
  <g stroke="#cfefff" fill="none" opacity=".3" stroke-width="1">
    <ellipse cx="200" cy="200" rx="110" ry="110"/>
    <ellipse cx="200" cy="200" rx="80" ry="110"/>
    <ellipse cx="200" cy="200" rx="45" ry="110"/>
    <ellipse cx="200" cy="200" rx="8" ry="110"/>
    <line x1="90" y1="200" x2="310" y2="200"/>
    <ellipse cx="200" cy="200" rx="110" ry="80" transform="translate(0,-45)"/>
    <ellipse cx="200" cy="200" rx="110" ry="80" transform="translate(0,45)"/>
    <ellipse cx="200" cy="200" rx="110" ry="45" transform="translate(0,-75)"/>
    <ellipse cx="200" cy="200" rx="110" ry="45" transform="translate(0,75)"/>
  </g>
  <path d="M200 90a110 110 0 0 1 0 220a70 110 0 0 0 0-220z" fill="#04080f" opacity=".62"/>
  <path d="M90 200a110 110 0 0 1 110-110 130 110 0 0 0 -70 190z" fill="url(#warm)" opacity=".35"/>
  <g stroke="#ffd27a" stroke-width="1.2" opacity=".55">
    <circle cx="246" cy="150" r="1.6" fill="#ffd27a" stroke="none"/>
    <circle cx="268" cy="196" r="1.8" fill="#ffd27a" stroke="none"/>
    <circle cx="252" cy="244" r="1.4" fill="#ffd27a" stroke="none"/>
    <circle cx="284" cy="168" r="1.3" fill="#ffd27a" stroke="none"/>
    <circle cx="230" cy="280" r="1.5" fill="#ffd27a" stroke="none"/>
  </g>
</g>

<circle cx="200" cy="200" r="110" fill="none" stroke="#9fe4ff" stroke-width="1.2" opacity=".6"/>

<g stroke="#8fd6ff" fill="none" opacity=".5" stroke-width="1">
<ellipse cx="200" cy="200" rx="150" ry="42" transform="rotate(-24 200 200)"/>
<ellipse cx="200" cy="200" rx="168" ry="60" transform="rotate(18 200 200)" opacity=".35"/>
</g>

<g stroke="#a8e8ff" stroke-width="0.8" opacity=".55">
<path d="M62 84 150 108 246 92 330 140" fill="none"/>
<path d="M330 140 352 232 300 300 220 330" fill="none"/>
<path d="M220 330 130 320 74 248 62 84" fill="none"/>
<path d="M150 108 200 200 300 300" fill="none"/>
<path d="M246 92 200 200 130 320" fill="none"/>
<path d="M74 248 200 200 352 232" fill="none"/>
<path d="M62 84 30 200 74 248" fill="none"/>
<path d="M330 140 372 210 352 232" fill="none"/>
</g>

<g fill="#eafaff">
<circle cx="62" cy="84" r="4"/><circle cx="150" cy="108" r="3"/><circle cx="246" cy="92" r="3.4"/>
<circle cx="330" cy="140" r="4"/><circle cx="352" cy="232" r="3"/><circle cx="300" cy="300" r="3.6"/>
<circle cx="220" cy="330" r="3"/><circle cx="130" cy="320" r="3.4"/><circle cx="74" cy="248" r="3"/>
<circle cx="30" cy="200" r="2.6"/><circle cx="372" cy="210" r="2.6"/>
</g>
<g fill="none" stroke="#eafaff" opacity=".3">
<circle cx="62" cy="84" r="9"/><circle cx="330" cy="140" r="9"/><circle cx="300" cy="300" r="8"/>
</g>

<circle cx="330" cy="140" r="16" fill="#9fe4ff" opacity=".18" filter="url(#soft)"/>
<circle cx="62" cy="84" r="16" fill="#ffd27a" opacity=".18" filter="url(#soft)"/>

<g opacity=".85">
<circle cx="316" cy="96" r="2" fill="#fff3c4"/>
<circle cx="96" cy="316" r="2" fill="#fff3c4"/>
<circle cx="352" cy="278" r="1.6" fill="#fff3c4"/>
</g>
</svg>