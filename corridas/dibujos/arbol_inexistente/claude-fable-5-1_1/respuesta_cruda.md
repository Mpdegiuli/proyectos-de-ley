<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="sky" cx="50%" cy="35%" r="75%">
<stop offset="0" stop-color="#2d1b4f"/>
<stop offset="0.6" stop-color="#140c2a"/>
<stop offset="1" stop-color="#06040f"/>
</radialGradient>
<linearGradient id="trunk" x1="0" x2="1">
<stop offset="0" stop-color="#2a1a36"/>
<stop offset="0.45" stop-color="#7a5690"/>
<stop offset="0.6" stop-color="#9b78b0"/>
<stop offset="1" stop-color="#221530"/>
</linearGradient>
<radialGradient id="orb">
<stop offset="0" stop-color="#fffbe6"/>
<stop offset="0.3" stop-color="#ffd27a"/>
<stop offset="0.7" stop-color="#ff8a5c" stop-opacity="0.5"/>
<stop offset="1" stop-color="#ff6b6b" stop-opacity="0"/>
</radialGradient>
<radialGradient id="ground" cx="50%" cy="0%" r="80%">
<stop offset="0" stop-color="#23183d"/>
<stop offset="1" stop-color="#090612"/>
</radialGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.2"/></filter>
<symbol id="leaf" viewBox="-8 -8 16 16">
<path d="M0 -7 A7 7 0 1 1 0 7 A4.5 7 0 1 0 0 -7Z" fill="#7fe8d8"/>
</symbol>
<symbol id="orbit" viewBox="-20 -20 40 40">
<circle r="18" fill="url(#orb)"/>
<circle r="5" fill="#fff6d6"/>
</symbol>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<g fill="#fff" opacity="0.7">
<circle cx="40" cy="50" r="1.2"/><circle cx="90" cy="30" r="0.8"/><circle cx="330" cy="40" r="1.3"/><circle cx="370" cy="90" r="0.9"/><circle cx="20" cy="140" r="0.8"/><circle cx="380" cy="160" r="1"/><circle cx="250" cy="20" r="1"/><circle cx="150" cy="15" r="0.7"/><circle cx="60" cy="210" r="0.9"/><circle cx="350" cy="230" r="0.7"/>
</g>
<path d="M0 325 Q120 295 200 305 Q290 315 400 290 V400 H0Z" fill="url(#ground)"/>
<g stroke="#5fd6c4" stroke-width="2" fill="none" opacity="0.55" stroke-linecap="round">
<path d="M185 335 C160 345 140 340 120 365 C105 385 80 380 60 395"/>
<path d="M190 338 C180 360 150 365 140 395"/>
<path d="M215 338 C240 350 260 345 280 370 C295 388 320 385 340 398"/>
<path d="M210 340 C225 360 250 362 260 395"/>
<path d="M200 342 C198 365 205 380 200 400"/>
</g>
<g fill="#5fd6c4" opacity="0.6" filter="url(#soft)">
<circle cx="60" cy="395" r="3"/><circle cx="140" cy="395" r="2.5"/><circle cx="340" cy="398" r="3"/><circle cx="260" cy="395" r="2.5"/><circle cx="120" cy="365" r="2"/><circle cx="280" cy="370" r="2"/>
</g>
<path d="M172 340 C182 300 148 262 184 222 C200 204 188 190 206 168 L218 170 C212 192 224 206 212 228 C190 266 226 300 230 340 Z" fill="url(#trunk)"/>
<path d="M190 330 C193 295 170 268 192 232" stroke="#b690cc" stroke-width="1.2" fill="none" opacity="0.5"/>
<g stroke="#5a3f6e" stroke-linecap="round" fill="none">
<path d="M208 172 C185 150 150 160 118 125 C105 112 100 95 108 80" stroke-width="7"/>
<path d="M212 172 C235 140 268 150 296 115 C306 103 310 90 304 76" stroke-width="7"/>
<path d="M209 176 C180 182 158 160 146 128 C142 118 146 108 154 102" stroke-width="5"/>
<path d="M214 178 C240 185 262 170 274 140 C278 130 274 120 266 114" stroke-width="5"/>
<path d="M210 170 C208 140 200 120 188 95 C184 86 186 76 194 70" stroke-width="5"/>
<path d="M213 170 C222 142 236 122 250 95 C255 86 254 76 246 70" stroke-width="4.5"/>
<path d="M118 125 C100 128 85 140 72 158" stroke-width="4"/>
<path d="M296 115 C315 120 328 134 340 152" stroke-width="4"/>
<path d="M150 158 C130 166 115 180 100 198" stroke-width="3.5"/>
<path d="M270 150 C290 162 305 176 312 198" stroke-width="3.5"/>
</g>
<g stroke="#9b78b0" stroke-width="1.8" fill="none" stroke-linecap="round">
<path d="M108 80 C104 70 96 68 92 76 C89 83 97 88 101 82"/>
<path d="M304 76 C308 66 316 64 320 72 C323 79 315 84 311 78"/>
<path d="M154 102 C158 95 152 88 146 92 C141 96 146 102 150 99"/>
<path d="M266 114 C264 106 270 100 276 104 C280 108 276 114 272 111"/>
<path d="M194 70 C190 60 196 54 202 58 C207 62 202 70 197 67"/>
<path d="M246 70 C250 60 244 54 238 58 C233 62 238 70 243 67"/>
</g>
<g filter="url(#glow)" opacity="0.9">
<use href="#orbit" x="52" y="138" width="40" height="40"/>
<use href="#orbit" x="320" y="132" width="40" height="40"/>
<use href="#orbit" x="80" y="178" width="40" height="40"/>
<use href="#orbit" x="292" y="178" width="40" height="40"/>
<use href="#orbit" x="76" y="56" width="36" height="36"/>
<use href="#orbit" x="288" y="52" width="36" height="36"/>
<use href="#orbit" x="178" y="42" width="40" height="40"/>
<use href="#orbit" x="222" y="42" width="40" height="40"/>
<use href="#orbit" x="130" y="78" width="32" height="32"/>
<use href="#orbit" x="256" y="88" width="32" height="32"/>
</g>
<g opacity="0.95">
<use href="#leaf" x="120" y="100" width="16" height="16" transform="rotate(-30 128 108)"/>
<use href="#leaf" x="140" y="135" width="14" height="14" transform="rotate(20 147 142)"/>
<use href="#leaf" x="165" y="110" width="15" height="15" transform="rotate(-60 172 117)"/>
<use href="#leaf" x="180" y="135" width="13" height="13" transform="rotate(40 186 141)"/>
<use href="#leaf" x="225" y="110" width="15" height="15" transform="rotate(60 232 117)"/>
<use href="#leaf" x="250" y="130" width="14" height="14" transform="rotate(-20 257 137)"/>
<use href="#leaf" x="270" y="95" width="16" height="16" transform="rotate(30 278 103)"/>
<use href="#leaf" x="100" y="150" width="14" height="14" transform="rotate(10 107 157)"/>
<use href="#leaf" x="300" y="150" width="14" height="14" transform="rotate(-10 307 157)"/>
<use href="#leaf" x="200" y="100" width="14" height="14" transform="rotate(90 207 107)"/>
<use href="#leaf" x="150" y="80" width="12" height="12" transform="rotate(-45 156 86)"/>
<use href="#leaf" x="240" y="78" width="12" height="12" transform="rotate(45 246 84)"/>
<use href="#leaf" x="215" y="150" width="12" height="12" transform="rotate(-80 221 156)"/>
<use href="#leaf" x="80" y="120" width="12" height="12" transform="rotate(70 86 126)"/>
<use href="#leaf" x="315" y="112" width="12" height="12" transform="rotate(-70 321 118)"/>
</g>
<g stroke="#ffd27a" stroke-width="0.8" opacity="0.6">
<line x1="135" y1="150" x2="135" y2="178"/><line x1="265" y1="148" x2="265" y2="176"/><line x1="195" y1="140" x2="195" y2="165"/><line x1="235" y1="145" x2="235" y2="170"/><line x1="112" y1="170" x2="112" y2="190"/><line x1="290" y1="168" x2="290" y2="190"/>
</g>
<g fill="#ffe9a8" filter="url(#soft)">
<circle cx="135" cy="180" r="2.2"/><circle cx="265" cy="178" r="2.2"/><circle cx="195" cy="167" r="2"/><circle cx="235" cy="172" r="2"/><circle cx="112" cy="192" r="1.8"/><circle cx="290" cy="192" r="1.8"/>
</g>
<g fill="#7fe8d8" opacity="0.7">
<circle cx="60" cy="260" r="1.5"/><circle cx="345" cy="250" r="1.5"/><circle cx="90" cy="300" r="1.2"/><circle cx="310" cy="285" r="1.2"/><circle cx="40" cy="230" r="1"/><circle cx="365" cy="215" r="1"/>
</g>
<ellipse cx="200" cy="345" rx="60" ry="6" fill="#5fd6c4" opacity="0.12"/>
</svg>