<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="bg" cx="50%" cy="45%" r="70%">
<stop offset="0" stop-color="#fbf6e9"/>
<stop offset="1" stop-color="#e6d8b9"/>
</radialGradient>
<path id="sc" d="M0 0a7 7 0 0 0 14 0M-7 7a7 7 0 0 0 14 0M7 7a7 7 0 0 0 14 0M-7 -7a7 7 0 0 0 14 0M7 -7a7 7 0 0 0 14 0" fill="none" stroke="#0d2b1e" stroke-opacity=".3" stroke-width="1.2"/>
<pattern id="pa" width="14" height="14" patternUnits="userSpaceOnUse"><use href="#sc"/></pattern>
<pattern id="pb" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(-120)"><use href="#sc"/></pattern>
<pattern id="pc" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(120)"><use href="#sc"/></pattern>
<polygon id="A" points="81,330 319,330 336,300.6 132,300.6 200,182.8 183,153.3"/>
<polygon id="B" points="336,300.6 217,94.4 183,94.4 285,271.1 149,271.1 132,300.6"/>
<polygon id="C" points="183,94.4 64,300.6 81,330 183,153.3 251,271.1 285,271.1"/>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<ellipse cx="190" cy="362" rx="150" ry="9" fill="#3b2f1a" opacity=".16"/>
<g transform="translate(-18 22)" stroke="#173326" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">
<!-- cuerpo: una vuelta que no cierra en ningún espacio real -->
<use href="#A" fill="#5aa557"/>
<use href="#A" fill="url(#pa)" stroke="none"/>
<use href="#B" fill="#a8d672"/>
<use href="#B" fill="url(#pb)" stroke="none"/>
<use href="#C" fill="#2f6f52"/>
<use href="#C" fill="url(#pc)" stroke="none"/>
<!-- cola -->
<path d="M330 300.6H336C354 300.6 368 297 377 286C382 280 384 274 386 266C389 284 381 304 367 316C353 327 337 330 319 330H310" fill="#5aa557"/>
<path d="M346 306c8 0 16-2 22-6M340 318c10 0 20-3 28-9" fill="none" stroke="#0d2b1e" stroke-opacity=".3" stroke-width="1.2"/>
<!-- cabeza -->
<g transform="translate(200 94.4) rotate(-120)">
<path d="M74 0H90l7 -5M90 0l7 5" fill="none" stroke="#d43d6b" stroke-width="2.2"/>
<path d="M-14 14.7L18 14.7C30 15 34 23 46 22C60 21 74 10 76 0C74 -10 60 -21 46 -22C34 -23 30 -15 18 -14.7L3 -14.7" fill="#a8d672"/>
<path d="M20 0C28 -7 38 -6 44 0C38 6 28 7 20 0Z" fill="#5aa557" stroke="none" opacity=".7"/>
<path d="M2 0C6 -4 11 -4 15 0C11 4 6 4 2 0Z" fill="#5aa557" stroke="none" opacity=".7"/>
<ellipse cx="51" cy="-12" rx="5.2" ry="4.4" fill="#ffe066" stroke-width="1.5"/>
<ellipse cx="51" cy="12" rx="5.2" ry="4.4" fill="#ffe066" stroke-width="1.5"/>
<ellipse cx="51.5" cy="-12" rx="3.6" ry="1.3" fill="#173326" stroke="none"/>
<ellipse cx="51.5" cy="12" rx="3.6" ry="1.3" fill="#173326" stroke="none"/>
<circle cx="69" cy="-3.5" r="1" fill="#173326" stroke="none"/>
<circle cx="69" cy="3.5" r="1" fill="#173326" stroke="none"/>
</g>
</g>
</svg>