<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="sky" cx="42%" cy="32%" r="78%">
<stop offset="0%" stop-color="#1c3358"/>
<stop offset="55%" stop-color="#0b1028"/>
<stop offset="100%" stop-color="#03040c"/>
</radialGradient>
<radialGradient id="sea" cx="36%" cy="30%" r="68%">
<stop offset="0%" stop-color="#7ec8e8"/>
<stop offset="28%" stop-color="#2a7aaa"/>
<stop offset="70%" stop-color="#123d5c"/>
<stop offset="100%" stop-color="#071828"/>
</radialGradient>
<radialGradient id="halo" cx="50%" cy="50%" r="50%">
<stop offset="72%" stop-color="#8fd4ee" stop-opacity="0"/>
<stop offset="86%" stop-color="#8fd4ee" stop-opacity=".45"/>
<stop offset="100%" stop-color="#4a7a9a" stop-opacity="0"/>
</radialGradient>
<linearGradient id="dusk" x1="0" y1="0" x2="1" y2=".15">
<stop offset="38%" stop-color="#000" stop-opacity="0"/>
<stop offset="58%" stop-color="#020814" stop-opacity=".35"/>
<stop offset="100%" stop-color="#000814" stop-opacity=".78"/>
</linearGradient>
<linearGradient id="leaf" x1="0" y1="0" x2=".4" y2="1">
<stop offset="0%" stop-color="#8fce7a"/>
<stop offset="55%" stop-color="#3d8a52"/>
<stop offset="100%" stop-color="#1e4a32"/>
</linearGradient>
<linearGradient id="sand" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#e0c58a"/>
<stop offset="100%" stop-color="#c4a05a"/>
</linearGradient>
<radialGradient id="sun" cx="40%" cy="40%" r="50%">
<stop offset="0%" stop-color="#fff6d0"/>
<stop offset="45%" stop-color="#ffcc55"/>
<stop offset="100%" stop-color="#ff8a1a"/>
</radialGradient>
<filter id="blur" x="-80%" y="-80%" width="260%" height="260%">
<feGaussianBlur stdDeviation="10"/>
</filter>
<filter id="soft">
<feGaussianBlur stdDeviation="2.2"/>
</filter>
<filter id="glow">
<feGaussianBlur stdDeviation="1.4"/>
</filter>
<clipPath id="globe">
<circle cx="200" cy="208" r="96"/>
</clipPath>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<g fill="#e8f0ff">
<circle cx="28" cy="46" r=".7" opacity=".9"/>
<circle cx="67" cy="22" r=".5" opacity=".55"/>
<circle cx="94" cy="71" r=".6" opacity=".7"/>
<circle cx="142" cy="18" r=".4" opacity=".4"/>
<circle cx="178" cy="52" r=".5" opacity=".6"/>
<circle cx="231" cy="14" r=".8" opacity=".85"/>
<circle cx="268" cy="43" r=".45" opacity=".5"/>
<circle cx="312" cy="19" r=".6" opacity=".75"/>
<circle cx="351" cy="58" r=".5" opacity=".45"/>
<circle cx="378" cy="31" r=".7" opacity=".8"/>
<circle cx="18" cy="118" r=".5" opacity=".5"/>
<circle cx="52" cy="162" r=".4" opacity=".35"/>
<circle cx="14" cy="214" r=".6" opacity=".65"/>
<circle cx="41" cy="268" r=".45" opacity=".4"/>
<circle cx="22" cy="322" r=".7" opacity=".7"/>
<circle cx="73" cy="348" r=".5" opacity=".5"/>
<circle cx="118" cy="372" r=".6" opacity=".6"/>
<circle cx="176" cy="386" r=".4" opacity=".35"/>
<circle cx="248" cy="378" r=".7" opacity=".75"/>
<circle cx="304" cy="362" r=".5" opacity=".45"/>
<circle cx="356" cy="338" r=".6" opacity=".7"/>
<circle cx="382" cy="286" r=".45" opacity=".4"/>
<circle cx="368" cy="198" r=".5" opacity=".55"/>
<circle cx="388" cy="142" r=".6" opacity=".65"/>
<circle cx="344" cy="96" r=".4" opacity=".35"/>
<circle cx="86" cy="98" r=".35" opacity=".3"/>
<circle cx="318" cy="248" r=".4" opacity=".4"/>
<circle cx="48" cy="88" r=".5" opacity=".5"/>
<circle cx="290" cy="388" r=".35" opacity=".3"/>
<circle cx="198" cy="8" r=".5" opacity=".55"/>
</g>
<circle cx="78" cy="72" r="28" fill="#ffb84a" opacity=".18" filter="url(#blur)"/>
<circle cx="78" cy="72" r="14" fill="#ffd878" opacity=".28" filter="url(#blur)"/>
<circle cx="78" cy="72" r="7.5" fill="url(#sun)"/>
<circle cx="78" cy="72" r="3.2" fill="#fff8e0"/>
<circle cx="200" cy="208" r="128" fill="url(#halo)"/>
<circle cx="200" cy="208" r="104" fill="none" stroke="#9ad4ea" stroke-width=".6" opacity=".28"/>
<circle cx="200" cy="208" r="118" fill="none" stroke="#6aa8c8" stroke-width=".35" opacity=".16" stroke-dasharray="3 9"/>
<ellipse cx="200" cy="208" rx="148" ry="36" fill="none" stroke="#7ec8e0" stroke-width=".4" opacity=".2" transform="rotate(-18 200 208)"/>
<ellipse cx="200" cy="208" rx="142" ry="28" fill="none" stroke="#a0d8c0" stroke-width=".35" opacity=".16" transform="rotate(32 200 208)"/>
<circle cx="200" cy="208" r="96" fill="url(#sea)"/>
<g clip-path="url(#globe)">
<path fill="url(#leaf)" d="M118 168 C128 132 168 118 186 148 C198 166 188 188 176 206 C168 228 152 248 138 258 C122 268 108 248 110 222 C108 198 110 178 118 168Z"/>
<path fill="#2f6b42" d="M142 252 C156 258 168 278 164 302 C158 324 146 338 136 326 C126 308 130 278 138 262 C140 256 142 252 142 252Z"/>
<path fill="#458556" d="M198 158 C214 148 232 156 238 176 C244 198 236 228 226 252 C216 274 202 286 194 268 C186 244 190 208 196 184 C198 170 198 158 198 158Z"/>
<path fill="url(#sand)" d="M208 176 C226 170 238 184 236 204 C234 220 222 226 212 216 C204 204 204 186 208 176Z" opacity=".85"/>
<path fill="#3d7a4a" d="M228 138 C258 124 292 138 302 168 C310 192 292 208 270 202 C248 196 236 178 232 156 C230 146 228 138 228 138Z"/>
<path fill="#5a9a62" d="M198 138 C210 128 228 134 232 148 C228 160 214 164 204 156 C196 148 194 140 198 138Z"/>
<path fill="#4a8a58" d="M278 258 C296 254 310 268 304 282 C296 294 278 292 272 278 C268 266 278 258 278 258Z"/>
<path fill="#d8eef6" d="M168 118 C186 108 214 112 226 128 C210 136 186 134 168 126 C164 122 168 118 168 118Z"/>
<path fill="#eaf6fb" d="M170 292 C190 300 220 298 238 288 C230 304 200 314 176 308 C168 300 170 292 170 292Z" opacity=".7"/>
<ellipse cx="148" cy="198" rx="22" ry="8" fill="#fff" opacity=".12" transform="rotate(-18 148 198)"/>
<ellipse cx="230" cy="168" rx="28" ry="7" fill="#fff" opacity=".1" transform="rotate(12 230 168)"/>
<ellipse cx="210" cy="238" rx="18" ry="6" fill="#fff" opacity=".08" transform="rotate(-8 210 238)"/>
<rect width="400" height="400" fill="url(#dusk)"/>
<g filter="url(#glow)">
<circle cx="248" cy="162" r="1.1" fill="#ffe9a0"/>
<circle cx="262" cy="178" r=".8" fill="#ffd278"/>
<circle cx="276" cy="166" r="1" fill="#fff0c0"/>
<circle cx="254" cy="194" r=".7" fill="#ffcc66"/>
<circle cx="270" cy="204" r="1.2" fill="#ffe08a"/>
<circle cx="286" cy="192" r=".6" fill="#ffeeaa"/>
<circle cx="242" cy="214" r=".9" fill="#ffd890"/>
<circle cx="258" cy="226" r=".7" fill="#ffe8b0"/>
<circle cx="278" cy="218" r="1" fill="#ffcc70"/>
<circle cx="292" cy="208" r=".5" fill="#fff3c8"/>
<circle cx="266" cy="242" r=".8" fill="#ffd080"/>
<circle cx="248" cy="238" r=".6" fill="#ffe4a8"/>
<circle cx="236" cy="188" r=".5" fill="#fff0b8"/>
<circle cx="284" cy="174" r=".7" fill="#ffc868"/>
<circle cx="298" cy="186" r=".9" fill="#ffe08c"/>
<circle cx="274" cy="156" r=".6" fill="#fff6d0"/>
<circle cx="252" cy="252" r=".7" fill="#ffd478"/>
<circle cx="268" cy="264" r=".5" fill="#ffeab0"/>
<circle cx="288" cy="248" r=".8" fill="#ffcc72"/>
<circle cx="240" cy="172" r=".55" fill="#fff2c4"/>
<circle cx="230" cy="228" r=".45" fill="#ffdfa0"/>
<circle cx="300" cy="222" r=".6" fill="#ffd890"/>
</g>
<path d="M120 150 C160 90 250 90 290 160" fill="none" stroke="#6ff0c0" stroke-width="3" opacity=".18" filter="url(#soft)"/>
<path d="M130 140 C180 80 260 95 286 155" fill="none" stroke="#c08cff" stroke-width="2" opacity=".14" filter="url(#soft)"/>
</g>
<circle cx="200" cy="208" r="96.6" fill="none" stroke="#b8e4f4" stroke-width="1.4" opacity=".35"/>
<circle cx="200" cy="208" r="99" fill="none" stroke="#ffffff" stroke-width=".4" opacity=".15"/>
<path d="M108 168 C70 120 90 70 140 92" fill="none" stroke="#8ad4ee" stroke-width=".7" opacity=".28"/>
<path d="M292 160 C340 110 330 60 280 78" fill="none" stroke="#8ad4ee" stroke-width=".7" opacity=".22"/>
<path d="M124 268 C80 310 110 360 168 348" fill="none" stroke="#7ec8c0" stroke-width=".6" opacity=".2"/>
<path d="M286 270 C340 320 300 366 240 352" fill="none" stroke="#7ec8c0" stroke-width=".6" opacity=".18"/>
<g fill="#c8f0ff">
<circle cx="92" cy="126" r="1.6"/>
<circle cx="318" cy="118" r="1.4"/>
<circle cx="86" cy="298" r="1.3"/>
<circle cx="322" cy="292" r="1.5"/>
</g>
<circle cx="92" cy="126" r="4" fill="#9ae0ff" opacity=".2" filter="url(#glow)"/>
<circle cx="318" cy="118" r="3.5" fill="#9ae0ff" opacity=".18" filter="url(#glow)"/>
<circle cx="334" cy="96" r="5.5" fill="#d8e4f0" opacity=".85"/>
<circle cx="332" cy="94" r="4.2" fill="#b8c4d4"/>
<circle cx="331" cy="93" r="1.4" fill="#f0f4f8" opacity=".5"/>
<g fill="none" stroke="#a8d8c8" stroke-width=".45" opacity=".22">
<path d="M40 390 C90 360 140 370 200 356 C270 340 330 358 380 348"/>
<path d="M20 376 C80 350 150 362 210 344 C280 326 340 344 400 336"/>
</g>
<circle cx="200" cy="208" r="96" fill="none" stroke="#ffd27a" stroke-width=".3" opacity=".2"/>
</svg>