<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#121236"/>
<stop offset=".45" stop-color="#46336e"/>
<stop offset=".8" stop-color="#c8607a"/>
<stop offset="1" stop-color="#f6a66b"/>
</linearGradient>
<linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#c06478"/>
<stop offset=".3" stop-color="#4a356f"/>
<stop offset="1" stop-color="#0f0f2c"/>
</linearGradient>
<radialGradient id="glow">
<stop offset="0" stop-color="#fff3c9" stop-opacity=".85"/>
<stop offset="1" stop-color="#fff3c9" stop-opacity="0"/>
</radialGradient>
<radialGradient id="lamp">
<stop offset="0" stop-color="#ffb347" stop-opacity=".9"/>
<stop offset="1" stop-color="#ffb347" stop-opacity="0"/>
</radialGradient>
<g id="m">
<path d="M0 250V200L40 170 80 195 130 150 175 200 220 175 270 205 320 160 365 195 400 175V250Z" fill="#6a4780"/>
<path d="M0 250V225L50 200 95 228 150 190 200 232 250 210 300 235 350 205 400 230V250Z" fill="#35275a"/>
</g>
<path id="p" d="M0-60L-8-40H-4L-12-20H-6L-16 0H-2V8H2V0H16L6-20H12L4-40H8Z"/>
</defs>
<rect width="400" height="250" fill="url(#sky)"/>
<g fill="#fff">
<circle cx="30" cy="30" r="1.2"/>
<circle cx="75" cy="62" r=".9" opacity=".8"/>
<circle cx="110" cy="22" r="1.4">
<animate attributeName="opacity" values="1;.2;1" dur="3s" repeatCount="indefinite"/>
</circle>
<circle cx="150" cy="80" r=".8" opacity=".7"/>
<circle cx="185" cy="38" r="1.1"/>
<circle cx="45" cy="105" r="1">
<animate attributeName="opacity" values=".3;1;.3" dur="4s" repeatCount="indefinite"/>
</circle>
<circle cx="225" cy="18" r=".9" opacity=".8"/>
<circle cx="345" cy="35" r="1.3">
<animate attributeName="opacity" values="1;.3;1" dur="5s" repeatCount="indefinite"/>
</circle>
<circle cx="375" cy="85" r=".9" opacity=".7"/>
<circle cx="310" cy="20" r=".8"/>
<circle cx="130" cy="125" r=".8" opacity=".6"/>
<circle cx="18" cy="150" r=".8" opacity=".5"/>
<circle cx="200" cy="105" r=".7" opacity=".6"/>
<circle cx="380" cy="140" r=".7" opacity=".5"/>
</g>
<circle cx="270" cy="110" r="75" fill="url(#glow)"/>
<circle cx="270" cy="110" r="30" fill="#fff6d8"/>
<g fill="#eadfb8" opacity=".6">
<circle cx="260" cy="100" r="6"/>
<circle cx="281" cy="118" r="4"/>
<circle cx="266" cy="124" r="2.5"/>
<circle cx="283" cy="98" r="2"/>
</g>
<use href="#m"/>
<rect y="250" width="400" height="150" fill="url(#water)"/>
<use href="#m" transform="matrix(1 0 0 -1 0 500)" opacity=".3"/>
<g fill="#fff3c9">
<rect x="245" y="256" width="50" height="3" rx="1.5" opacity=".8"/>
<rect x="250" y="264" width="40" height="3" rx="1.5" opacity=".7"/>
<rect x="242" y="273" width="56" height="3" rx="1.5" opacity=".6"/>
<rect x="253" y="284" width="34" height="3" rx="1.5" opacity=".5"/>
<rect x="248" y="296" width="44" height="3" rx="1.5" opacity=".4"/>
<rect x="258" y="310" width="24" height="3" rx="1.5" opacity=".3"/>
<rect x="255" y="326" width="30" height="3" rx="1.5" opacity=".2"/>
</g>
<g stroke="#fff" stroke-width=".8" opacity=".15" stroke-linecap="round">
<path d="M20 270H70M320 268H380M90 290H120M200 320H240M30 310H60M330 295H360M180 350H230M190 275H215"/>
</g>
<circle cx="133" cy="290" r="14" fill="url(#lamp)"/>
<g fill="#0a0920">
<path d="M122 299Q152 310 184 299L178 307Q152 313 129 307Z"/>
<path d="M150 302L152 287Q156 282 160 287L162 302Z"/>
<circle cx="156" cy="280" r="3.6"/>
<path d="M151 277H161L156 272Z"/>
</g>
<path d="M133 301V291M159 290L192 270" stroke="#0a0920" stroke-width="1.2" stroke-linecap="round"/>
<path d="M192 270V304" stroke="#fff" stroke-width=".4" opacity=".6"/>
<circle cx="133" cy="290" r="2.2" fill="#ffd27a"/>
<g fill="#ffb347">
<rect x="128" y="314" width="10" height="2" rx="1" opacity=".6"/>
<rect x="130" y="320" width="7" height="2" rx="1" opacity=".4"/>
<rect x="129" y="327" width="5" height="2" rx="1" opacity=".25"/>
</g>
<ellipse cx="192" cy="304" rx="4" ry="1" fill="none" stroke="#fff" stroke-width=".5" opacity=".5">
<animate attributeName="rx" values="2;8" dur="3s" repeatCount="indefinite"/>
<animate attributeName="opacity" values=".6;0" dur="3s" repeatCount="indefinite"/>
</ellipse>
<g fill="#080716">
<path d="M0 400V330Q40 320 80 345Q110 365 140 400Z"/>
<path d="M400 400V310Q360 305 330 335Q300 365 270 400Z"/>
<use href="#p" transform="translate(20 334) scale(1.6)"/>
<use href="#p" transform="translate(55 340) scale(1.2)"/>
<use href="#p" transform="translate(90 358) scale(.9)"/>
<use href="#p" transform="translate(385 314) scale(1.8)"/>
<use href="#p" transform="translate(350 324) scale(1.3)"/>
<use href="#p" transform="translate(318 350) scale(1)"/>
</g>
<g fill="#ffe98a">
<circle cx="110" cy="345" r="1.3">
<animate attributeName="opacity" values="0;1;0" dur="2.5s" repeatCount="indefinite"/>
</circle>
<circle cx="70" cy="320" r="1.1">
<animate attributeName="opacity" values="1;0;1" dur="3.5s" repeatCount="indefinite"/>
</circle>
<circle cx="295" cy="350" r="1.3">
<animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite"/>
</circle>
<circle cx="330" cy="318" r="1">
<animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
</circle>
<circle cx="125" cy="375" r="1.2">
<animate attributeName="opacity" values="0;1;0" dur="3.2s" repeatCount="indefinite"/>
</circle>
</g>
</svg>