```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#2d3b7a"/>
<stop offset=".4" stop-color="#d987a6"/>
<stop offset=".65" stop-color="#ffd49a"/>
</linearGradient>
<radialGradient id="glow">
<stop offset="0" stop-color="#fff8d0"/>
<stop offset=".35" stop-color="#ffdf8a" stop-opacity=".8"/>
<stop offset="1" stop-color="#ffd36b" stop-opacity="0"/>
</radialGradient>
<linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#ffe6b0"/>
<stop offset=".3" stop-color="#8fd3ea"/>
<stop offset="1" stop-color="#3f9fcf"/>
</linearGradient>
<path id="bl" d="M0 0C-3-9-2-21 0-25C2-21 3-9 0 0Z" fill="#fff"/>
<g id="tree"><rect x="-2" y="-4" width="4" height="12" fill="#6b4a32"/><circle r="9" cy="-10" fill="#3f8f4a"/><circle r="6" cx="-4" cy="-14" fill="#57a85c"/></g>
<g id="tree2"><rect x="-1.5" y="-2" width="3" height="9" fill="#6b4a32"/><circle r="7" cy="-7" fill="#4c9a52"/><circle r="2" cx="3" cy="-8" fill="#e8574f"/><circle r="2" cx="-3" cy="-5" fill="#e8574f"/><circle r="2" cx="1" cy="-3" fill="#f2a33a"/></g>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<g fill="#fff">
<circle cx="40" cy="30" r="1.2"/><circle cx="90" cy="60" r="1"/><circle cx="150" cy="22" r="1.4"/><circle cx="260" cy="40" r="1"/><circle cx="330" cy="18" r="1.3"/><circle cx="370" cy="70" r="1"/><circle cx="20" cy="90" r=".9"/><circle cx="210" cy="12" r="1"/>
</g>
<circle cx="205" cy="232" r="110" fill="url(#glow)"/>
<circle cx="205" cy="232" r="32" fill="#fff2b8"/>
<g fill="none" stroke="#5a4060" stroke-width="1.5" stroke-linecap="round">
<path d="M150 150q5-5 10 0q5-5 10 0"/>
<path d="M175 135q4-4 8 0q4-4 8 0"/>
<path d="M240 160q4-4 8 0q4-4 8 0"/>
</g>
<path d="M0 250Q100 212 200 242T400 236V400H0Z" fill="#86bf80"/>
<g stroke="#eef" stroke-width="2">
<line x1="50" y1="236" x2="50" y2="180"/>
<line x1="100" y1="232" x2="100" y2="186"/>
<line x1="350" y1="238" x2="350" y2="190"/>
</g>
<g transform="translate(50 180)"><g>
<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="7s" repeatCount="indefinite"/>
<use href="#bl"/><use href="#bl" transform="rotate(120)"/><use href="#bl" transform="rotate(240)"/>
</g><circle r="2.5" fill="#ddd"/></g>
<g transform="translate(100 186)"><g>
<animateTransform attributeName="transform" type="rotate" from="40" to="400" dur="9s" repeatCount="indefinite"/>
<use href="#bl"/><use href="#bl" transform="rotate(120)"/><use href="#bl" transform="rotate(240)"/>
</g><circle r="2.5" fill="#ddd"/></g>
<g transform="translate(350 190) scale(.85)"><g>
<animateTransform attributeName="transform" type="rotate" from="80" to="440" dur="8s" repeatCount="indefinite"/>
<use href="#bl"/><use href="#bl" transform="rotate(120)"/><use href="#bl" transform="rotate(240)"/>
</g><circle r="2.5" fill="#ddd"/></g>
<path d="M0 292Q200 252 400 292V400H0Z" fill="#5fa35e"/>
<path d="M200 244Q195 258 208 268Q238 290 210 312Q174 338 196 364Q214 384 194 400H258Q274 380 250 358Q226 336 254 312Q282 286 222 266Q207 256 210 244Z" fill="url(#water)"/>
<g stroke="#fff" stroke-width="1.2" stroke-linecap="round" opacity=".7">
<line x1="206" y1="256" x2="212" y2="256"/><line x1="215" y1="280" x2="228" y2="280"/><line x1="200" y1="372" x2="214" y2="372"/><line x1="228" y1="300" x2="238" y2="300"/>
</g>
<g fill="#4a8f3f">
<path d="M10 330L120 310L140 345L20 370Z"/>
</g>
<g stroke="#a6d46a" stroke-width="2" stroke-linecap="round">
<path d="M18 340L124 320M22 350L129 330M26 360L134 340"/>
</g>
<g fill="#ffd34d">
<circle cx="40" cy="336" r="1.6"/><circle cx="70" cy="331" r="1.6"/><circle cx="100" cy="325" r="1.6"/><circle cx="55" cy="352" r="1.6"/><circle cx="90" cy="346" r="1.6"/><circle cx="118" cy="340" r="1.6"/>
</g>
<use href="#tree" x="150" y="290"/>
<use href="#tree" x="30" y="300"/>
<use href="#tree2" x="160" y="365"/>
<use href="#tree2" x="140" y="300"/>
<use href="#tree" x="275" y="370"/>
<use href="#tree2" x="300" y="385"/>
<use href="#tree2" x="80" y="290"/>
<g>
<rect x="290" y="268" width="28" height="22" fill="#f6e3c4"/>
<polygon points="286,268 304,252 322,268" fill="#c45a41"/>
<polygon points="305,255 318,266 312,266 300,256" fill="#2f5aa8"/>
<rect x="296" y="274" width="6" height="6" fill="#ffd36b"/>
<rect x="308" y="278" width="6" height="12" fill="#8a5a3c"/>
<rect x="330" y="262" width="34" height="28" fill="#e8d9f0"/>
<polygon points="326,262 347,244 368,262" fill="#7a5aa8"/>
<polygon points="349,247 364,260 357,260 343,249" fill="#2f5aa8"/>
<rect x="335" y="268" width="7" height="7" fill="#ffd36b"/>
<rect x="352" y="268" width="7" height="7" fill="#ffd36b"/>
<rect x="343" y="278" width="7" height="12" fill="#8a5a3c"/>
<circle cx="335" cy="262" r="3" fill="#57a85c"/><circle cx="341" cy="259" r="3" fill="#57a85c"/>
<rect x="372" y="272" width="24" height="20" fill="#d9eed9"/>
<polygon points="369,272 384,258 399,272" fill="#3f8f8a"/>
<rect x="378" y="277" width="6" height="6" fill="#ffd36b"/>
</g>
<path d="M164 342Q215 312 268 342" fill="none" stroke="#8a5a3c" stroke-width="5" stroke-linecap="round"/>
<path d="M168 332Q215 304 264 332" fill="none" stroke="#a57655" stroke-width="1.5"/>
<g stroke="#a57655" stroke-width="1.5">
<line x1="180" y1="331" x2="180" y2="324"/><line x1="200" y1="324" x2="200" y2="317"/><line x1="230" y1="324" x2="230" y2="317"/><line x1="250" y1="331" x2="250" y2="325"/>
</g>
<path d="M190 316L203 312L216 311L229 312L242 316" fill="none" stroke="#3a2a2a" stroke-width="1.2"/>
<g>
<rect x="186" y="312" width="7" height="12" rx="3" fill="#e05a5a"/><circle cx="189.5" cy="308" r="4" fill="#5a3825"/>
<rect x="199" y="308" width="7" height="13" rx="3" fill="#3f7fd0"/><circle cx="202.5" cy="304" r="4" fill="#f1c9a5"/>
<rect x="212" y="307" width="7" height="13" rx="3" fill="#f2b53a"/><circle cx="215.5" cy="303" r="4" fill="#a8704a"/>
<rect x="225" y="308" width="7" height="13" rx="3" fill="#57a85c"/><circle cx="228.5" cy="304" r="4" fill="#e3b48a"/>
<rect x="238" y="312" width="7" height="12" rx="3" fill="#9a5ac8"/><circle cx="241.5" cy="308" r="4" fill="#7a4a30"/>
</g>
<g>
<rect x="318" y="300" width="7" height="12" rx="3" fill="#f07ab0"/><circle cx="321.5" cy="296" r="4" fill="#c48a60"/>
<line x1="325" y1="303" x2="330" y2="298" stroke="#3a2a2a" stroke-width="1.2"/>
</g>
<path d="M330 298Q340 220 300 130" fill="none" stroke="#fff" stroke-width=".8" opacity=".8"/>
<g transform="translate(300 120)">
<animateTransform attributeName="transform" type="translate" values="300 120;304 116;300 120" dur="4s" repeatCount="indefinite"/>
<polygon points="0,-14 10,0 0,14 -10,0" fill="#ff6b6b"/>
<polygon points="0,-14 10,0 0,0" fill="#ffd34d"/>
<polygon points="0,0 0,14 -10,0" fill="#4fb3e8"/>
<path d="M0 14q4 6 0 10q-4 4 0 10" fill="none" stroke="#fff" stroke-width="1"/>
</g>
<g fill="#fff" opacity=".85">
<ellipse cx="70" cy="120" rx="22" ry="7"/><ellipse cx="85" cy="114" rx="14" ry="7"/>
<ellipse cx="340" cy="150" rx="20" ry="6"/><ellipse cx="352" cy="145" rx="11" ry="6"/>
</g>
</svg>
```