<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#3fb6f0"/><stop offset=".52" stop-color="#a5e6ff"/><stop offset="1" stop-color="#ffe8b3"/></linearGradient>
<radialGradient id="sea" cx=".34" cy=".28" r=".95">
<stop offset="0" stop-color="#63c2fb"/><stop offset="1" stop-color="#0d4d9e"/></radialGradient>
<radialGradient id="sunG" cx=".5" cy=".5" r=".5">
<stop offset="0" stop-color="#fffbe3"/><stop offset="1" stop-color="#ffd23f"/></radialGradient>
<linearGradient id="grass" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#7ed957"/><stop offset="1" stop-color="#146b34"/></linearGradient>
<clipPath id="gclip"><circle cx="200" cy="220" r="88"/></clipPath>
<g id="body"><path d="M-7,-25 C-11,-21 -11,-8 -9.5,0 L9.5,0 C11,-8 11,-21 7,-25 Z"/><path d="M-7,-23 L-15,-13 M7,-23 L15,-13" fill="none" stroke-width="4.2" stroke-linecap="round"/></g>
<g id="head"><circle cy="-35" r="6.8"/><circle cx="-15" cy="-13" r="2.7"/><circle cx="15" cy="-13" r="2.7"/></g>
<g id="bird" fill="none" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round"><path d="M-15,2 Q-8,-8 0,-1 Q8,-8 15,2"/></g>
</defs>

<rect width="400" height="400" fill="url(#sky)"/>

<g transform="translate(200,76)">
<g stroke="#ffd23f" stroke-width="6" stroke-linecap="round" opacity=".85">
<path d="M0,-30 L0,-44"/><path d="M0,30 L0,44"/><path d="M-30,0 L-44,0"/><path d="M30,0 L44,0"/>
<path d="M-21,-21 L-31,-31"/><path d="M21,-21 L31,-31"/><path d="M-21,21 L-31,31"/><path d="M21,21 L31,31"/>
</g>
<circle r="26" fill="url(#sunG)"/>
</g>

<g fill="none" stroke-width="9" opacity=".78">
<path d="M2,330 A198,198 0 0 1 398,330" stroke="#9775fa"/>
<path d="M12,330 A188,188 0 0 1 388,330" stroke="#4dabf7"/>
<path d="M22,330 A178,178 0 0 1 378,330" stroke="#69db7c"/>
<path d="M32,330 A168,168 0 0 1 368,330" stroke="#ffd43b"/>
<path d="M42,330 A158,158 0 0 1 358,330" stroke="#ff922b"/>
<path d="M52,330 A148,148 0 0 1 348,330" stroke="#ff6b6b"/>
</g>

<use href="#bird" transform="translate(72,132) scale(.9)"/>
<use href="#bird" transform="translate(118,102) scale(.62)"/>
<use href="#bird" transform="translate(322,126) scale(.85)"/>
<use href="#bird" transform="translate(357,172) scale(.58)"/>
<use href="#bird" transform="translate(255,64) scale(.5)"/>

<circle cx="200" cy="220" r="100" fill="#ffffff" opacity=".14"/>
<circle cx="200" cy="220" r="88" fill="url(#sea)"/>
<g clip-path="url(#gclip)">
<path d="M126,178 q28,-16 42,2 q7,13 -11,17 q-21,6 -33,-6 z" fill="#5fd07c"/>
<path d="M212,166 q32,-13 54,5 q11,11 -7,19 q-23,10 -41,1 q-15,-7 -6,-25 z" fill="#57c475"/>
<path d="M190,204 q23,-9 31,11 q7,19 -9,33 q-13,12 -21,-1 q-8,-17 -5,-31 z" fill="#4fbd6e"/>
<path d="M160,224 q15,-7 19,9 q4,19 -9,35 q-11,12 -17,0 q-4,-25 7,-44 z" fill="#5fd07c"/>
<path d="M246,258 q17,-7 19,9 q0,13 -13,13 q-15,0 -12,-22 z" fill="#4fbd6e"/>
<ellipse cx="200" cy="137" rx="55" ry="15" fill="#eaf7ff" opacity=".85"/>
<ellipse cx="200" cy="303" rx="58" ry="16" fill="#eaf7ff" opacity=".6"/>
<ellipse cx="168" cy="178" rx="36" ry="22" fill="#ffffff" opacity=".22" transform="rotate(-32 168 178)"/>
</g>
<circle cx="200" cy="220" r="88" fill="none" stroke="#ffffff" stroke-width="3" opacity=".45"/>

<path d="M0,400 L0,332 Q200,284 400,332 L400,400 Z" fill="url(#grass)"/>
<path d="M0,400 L0,362 Q200,320 400,362 L400,400 Z" fill="#0f5c2c" opacity=".55"/>

<g>
<rect x="57" y="288" width="7" height="36" rx="3" fill="#7a4b26"/>
<circle cx="60" cy="278" r="21" fill="#2f9e44"/><circle cx="43" cy="293" r="15" fill="#37b24d"/><circle cx="78" cy="293" r="15" fill="#37b24d"/>
<rect x="342" y="290" width="7" height="34" rx="3" fill="#7a4b26"/>
<circle cx="345" cy="281" r="19" fill="#2f9e44"/><circle cx="330" cy="295" r="13" fill="#37b24d"/><circle cx="361" cy="295" r="13" fill="#37b24d"/>
</g>

<g>
<use href="#body" transform="translate(110,313)" fill="#ff6b6b"/><use href="#head" transform="translate(110,313)" fill="#8d5a3b"/>
<use href="#body" transform="translate(140,313)" fill="#ffd43b"/><use href="#head" transform="translate(140,313)" fill="#f2c39a"/>
<use href="#body" transform="translate(170,313)" fill="#4dabf7"/><use href="#head" transform="translate(170,313)" fill="#c98b5f"/>
<use href="#body" transform="translate(200,313)" fill="#f783ac"/><use href="#head" transform="translate(200,313)" fill="#6b4226"/>
<use href="#body" transform="translate(230,313)" fill="#69db7c"/><use href="#head" transform="translate(230,313)" fill="#f6c9a0"/>
<use href="#body" transform="translate(260,313)" fill="#b197fc"/><use href="#head" transform="translate(260,313)" fill="#e0a97e"/>
<use href="#body" transform="translate(290,313)" fill="#ffa94d"/><use href="#head" transform="translate(290,313)" fill="#f2b98c"/>
</g>

<g>
<circle cx="24" cy="336" r="3.2" fill="#ff6b6b"/><circle cx="88" cy="331" r="3" fill="#fff"/>
<circle cx="122" cy="336" r="3.2" fill="#b197fc"/><circle cx="196" cy="331" r="3" fill="#ffd43b"/>
<circle cx="268" cy="333" r="3.2" fill="#ff6b6b"/><circle cx="318" cy="338" r="3" fill="#fff"/>
<circle cx="376" cy="334" r="3.2" fill="#b197fc"/>
</g>

<text x="200" y="383" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="15" letter-spacing="2.5" fill="#e9ffe2" opacity=".95">un mundo en común</text>
</svg>