<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#22306b"/>
<stop offset="0.45" stop-color="#d98aa0"/>
<stop offset="0.75" stop-color="#ffc98a"/>
<stop offset="1" stop-color="#ffe9b8"/>
</linearGradient>
<radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#fffbe6"/>
<stop offset="0.5" stop-color="#ffe08a"/>
<stop offset="1" stop-color="#ffe08a" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#fff3b0" stop-opacity="0.9"/>
<stop offset="1" stop-color="#fff3b0" stop-opacity="0"/>
</radialGradient>
<linearGradient id="h1" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#7d7fb0"/>
<stop offset="1" stop-color="#8fa88f"/>
</linearGradient>
<linearGradient id="h2" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#6fa36a"/>
<stop offset="1" stop-color="#3f7a55"/>
</linearGradient>
<linearGradient id="h3" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#4f9060"/>
<stop offset="1" stop-color="#2c5e45"/>
</linearGradient>
<linearGradient id="river" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#8fd0e8"/>
<stop offset="1" stop-color="#ffd9a0"/>
</linearGradient>
</defs>

<rect width="400" height="400" fill="url(#sky)"/>

<g fill="#fff" opacity="0.8">
<circle cx="40" cy="30" r="1.4"/>
<circle cx="95" cy="55" r="1"/>
<circle cx="150" cy="22" r="1.3"/>
<circle cx="250" cy="35" r="1"/>
<circle cx="320" cy="20" r="1.5"/>
<circle cx="365" cy="62" r="1"/>
<circle cx="205" cy="70" r="0.9"/>
</g>

<circle cx="215" cy="215" r="90" fill="url(#sun)"/>
<circle cx="215" cy="215" r="30" fill="#fff4c4"/>

<g fill="#fff" opacity="0.55">
<ellipse cx="85" cy="120" rx="45" ry="9"/>
<ellipse cx="110" cy="112" rx="28" ry="8"/>
<ellipse cx="310" cy="145" rx="50" ry="8"/>
<ellipse cx="335" cy="137" rx="28" ry="7"/>
</g>

<path d="M0 235 Q60 195 130 225 T260 215 T400 225 V400 H0Z" fill="url(#h1)"/>

<g>
<rect x="120" y="222" width="16" height="12" fill="#f6d9b0"/>
<path d="M117 223 L128 213 L139 223Z" fill="#c4695a"/>
<rect x="150" y="226" width="13" height="10" fill="#f6d9b0"/>
<path d="M148 227 L156.5 219 L165 227Z" fill="#b95f66"/>
<rect x="290" y="218" width="18" height="14" fill="#f6d9b0"/>
<path d="M287 219 L299 208 L311 219Z" fill="#c4695a"/>
<rect x="126" y="226" width="4" height="5" fill="#ffd54a"/>
<rect x="155" y="229" width="3" height="4" fill="#ffd54a"/>
<rect x="297" y="222" width="4" height="6" fill="#ffd54a"/>
</g>

<path d="M0 260 Q80 232 180 255 T400 245 V400 H0Z" fill="url(#h2)"/>

<path d="M190 256 C170 280 230 295 205 320 C185 345 120 350 100 400 L190 400 C200 360 270 345 265 315 C260 285 215 280 232 258Z" fill="url(#river)" opacity="0.9"/>
<path d="M205 275 q10 -3 20 0 M190 320 q10 -3 22 0 M150 355 q10 -3 20 0" stroke="#fff" stroke-width="1.2" fill="none" opacity="0.7"/>

<path d="M0 320 Q90 285 170 310 T330 300 T400 305 V400 H0Z" fill="url(#h3)"/>

<path d="M300 400 C310 360 330 340 330 305" stroke="#e8c98f" stroke-width="7" fill="none" opacity="0.7" stroke-linecap="round"/>

<g>
<path d="M338 330 C335 290 342 265 340 240" stroke="#5b3b2e" stroke-width="9" fill="none" stroke-linecap="round"/>
<path d="M340 270 L362 250 M339 255 L320 238" stroke="#5b3b2e" stroke-width="4" fill="none" stroke-linecap="round"/>
<circle cx="340" cy="222" r="32" fill="#3f8a55"/>
<circle cx="312" cy="238" r="22" fill="#4c9a5f"/>
<circle cx="366" cy="240" r="22" fill="#4c9a5f"/>
<circle cx="345" cy="205" r="20" fill="#5fae6c"/>
<circle cx="325" cy="222" r="5" fill="#ffb3a7"/>
<circle cx="356" cy="230" r="5" fill="#ffb3a7"/>
<circle cx="342" cy="212" r="4" fill="#ffd3c9"/>
<circle cx="370" cy="246" r="4" fill="#ffb3a7"/>
<circle cx="310" cy="244" r="4" fill="#ffd3c9"/>
</g>

<g>
<circle cx="110" cy="318" r="48" fill="url(#glow)"/>
<ellipse cx="110" cy="345" rx="26" ry="5" fill="#1f4a38" opacity="0.5"/>
<path d="M110 270 q-4 -10 0 -16 q6 8 0 16z" fill="#ffd54a"/>
<path d="M110 270 q-2 -5 0 -9 q3 4 0 9z" fill="#fff6c0"/>
<path d="M88 320 C88 288 132 288 132 320 C132 342 120 345 110 345 C100 345 88 342 88 320Z" fill="#ffe7a8"/>
<path d="M88 320 C88 288 132 288 132 320 C132 342 120 345 110 345 C100 345 88 342 88 320Z" fill="none" stroke="#e8a85a" stroke-width="2"/>
<circle cx="101" cy="316" r="3" fill="#4a3326"/>
<circle cx="119" cy="316" r="3" fill="#4a3326"/>
<circle cx="102" cy="315" r="1" fill="#fff"/>
<circle cx="120" cy="315" r="1" fill="#fff"/>
<path d="M103 326 Q110 333 117 326" stroke="#4a3326" stroke-width="2" fill="none" stroke-linecap="round"/>
<circle cx="96" cy="324" r="3.5" fill="#ffb3a7" opacity="0.7"/>
<circle cx="124" cy="324" r="3.5" fill="#ffb3a7" opacity="0.7"/>
<path d="M132 322 q10 2 14 -8" stroke="#e8a85a" stroke-width="3" fill="none" stroke-linecap="round"/>
</g>

<g>
<ellipse cx="170" cy="347" rx="12" ry="3" fill="#1f4a38" opacity="0.5"/>
<path d="M162 345 C160 330 164 322 170 322 C177 322 180 330 178 345Z" fill="#6e86d9"/>
<circle cx="170" cy="314" r="8" fill="#f1c8a0"/>
<path d="M162 313 C162 304 178 304 178 313 C174 309 166 309 162 313Z" fill="#3a2a22"/>
<circle cx="167.5" cy="315" r="1" fill="#3a2a22"/>
<circle cx="172.5" cy="315" r="1" fill="#3a2a22"/>
<path d="M167.5 318.5 Q170 320.5 172.5 318.5" stroke="#3a2a22" stroke-width="1" fill="none"/>
<path d="M160 330 L147 322" stroke="#f1c8a0" stroke-width="3" stroke-linecap="round"/>
</g>

<g>
<ellipse cx="210" cy="352" rx="14" ry="3" fill="#1f4a38" opacity="0.5"/>
<path d="M196 348 C196 334 212 328 224 336 C230 340 234 346 238 344 C236 352 226 352 222 351 L198 351Z" fill="#e8823a"/>
<path d="M196 337 L192 326 L202 332Z" fill="#e8823a"/>
<path d="M203 333 L204 324 L210 331Z" fill="#e8823a"/>
<path d="M233 346 C240 346 244 342 244 337 C240 338 236 340 233 346Z" fill="#fff"/>
<path d="M196 343 q-4 2 -3 6 q4 0 6 -3z" fill="#fff"/>
<circle cx="200" cy="339" r="1" fill="#2c1b12"/>
</g>

<g stroke="#2c5e45" stroke-width="1.5" fill="none">
<path d="M20 372 v-12 M45 380 v-14 M70 368 v-10 M250 372 v-12 M275 380 v-10 M375 372 v-10"/>
</g>
<g>
<circle cx="20" cy="358" r="4" fill="#ff8fa3"/>
<circle cx="45" cy="364" r="4" fill="#ffe27a"/>
<circle cx="70" cy="356" r="4" fill="#fff"/>
<circle cx="250" cy="358" r="4" fill="#ffe27a"/>
<circle cx="275" cy="368" r="4" fill="#ff8fa3"/>
<circle cx="375" cy="360" r="4" fill="#fff"/>
</g>

<g fill="none" stroke="#3b3560" stroke-width="1.8" stroke-linecap="round">
<path d="M60 90 q5 -5 10 0 q5 -5 10 0"/>
<path d="M95 70 q4 -4 8 0 q4 -4 8 0"/>
<path d="M265 95 q5 -5 10 0 q5 -5 10 0"/>
<path d="M285 75 q4 -4 8 0 q4 -4 8 0"/>
</g>

<g>
<path d="M55 150 l14 -18 l14 18 l-14 12z" fill="#ff8fa3"/>
<path d="M69 132 l14 18 l-14 12z" fill="#ffe27a"/>
<path d="M69 162 C66 190 78 200 72 225" stroke="#fff" stroke-width="1" fill="none" opacity="0.8"/>
</g>
</svg>