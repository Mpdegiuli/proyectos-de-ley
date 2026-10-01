```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<title>El puente que solo existe en el reflejo</title>
<defs>
<linearGradient id="s" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#10123a"/><stop offset=".45" stop-color="#43305f"/><stop offset=".72" stop-color="#a24a60"/><stop offset=".9" stop-color="#e78a4e"/><stop offset="1" stop-color="#f7b558"/>
</linearGradient>
<linearGradient id="w" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#d97a52"/><stop offset=".2" stop-color="#8a3f5c"/><stop offset=".55" stop-color="#2a1b4a"/><stop offset="1" stop-color="#120e2c"/>
</linearGradient>
<radialGradient id="h"><stop offset="0" stop-color="#ffe9bd" stop-opacity=".55"/><stop offset="1" stop-color="#ffe9bd" stop-opacity="0"/></radialGradient>
<radialGradient id="v" cx=".5" cy=".42" r=".8"><stop offset=".65" stop-color="#0b0620" stop-opacity="0"/><stop offset="1" stop-color="#0b0620" stop-opacity=".5"/></radialGradient>
<filter id="g" x="-150%" y="-150%" width="400%" height="400%"><feGaussianBlur stdDeviation="2.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="r" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".013 .2" numOctaves="1" seed="4" result="n"><animate attributeName="baseFrequency" values=".013 .2;.017 .24;.013 .2" dur="10s" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" in2="n" scale="8"/></filter>
<path id="arc" d="M112 206 Q200 158 288 206" fill="none"/>
<g id="isl">
<path d="M10 212 Q58 196 126 208 L120 226 Q100 238 96 280 Q78 248 52 242 Q26 236 10 212Z" fill="#1c1533"/>
<path d="M14 211 Q58 197 124 208" stroke="#e8975a" stroke-width="1" fill="none" opacity=".5"/>
<path d="M46 188l5-2 3 14-6 2z" fill="#221839" stroke="#e8975a" stroke-width=".6" opacity=".9"/>
<path d="M274 208 Q330 194 392 206 L382 228 Q362 240 356 283 Q338 250 306 242 Q282 234 274 208Z" fill="#1c1533"/>
<path d="M278 207 Q330 195 388 206" stroke="#e8975a" stroke-width="1" fill="none" opacity=".5"/>
<path d="M328 174h16v34h-16z M333 208v-9a3 3 0 0 1 6 0v9z" fill="#221839" fill-rule="evenodd" stroke="#e8975a" stroke-width=".6"/>
<circle cx="336" cy="203" r="1.6" fill="#ffd27a"><animate attributeName="opacity" values="1;.4;1" dur="4s" repeatCount="indefinite"/></circle>
</g>
</defs>
<rect width="400" height="290" fill="url(#s)"/>
<g fill="#ffe7c2">
<circle cx="24" cy="30" r="1.1"/><circle cx="62" cy="16" r=".9"/><circle cx="134" cy="22" r=".9"/><circle cx="170" cy="38" r="1.2"/><circle cx="208" cy="14" r="1"/><circle cx="244" cy="30" r=".9"/><circle cx="372" cy="26" r="1.1"/><circle cx="386" cy="66" r=".8"/><circle cx="30" cy="84" r=".9"/><circle cx="56" cy="120" r=".8"/><circle cx="150" cy="70" r=".8"/>
<circle cx="97" cy="44" r="1.3"><animate attributeName="opacity" values="1;.2;1" dur="3.4s" repeatCount="indefinite"/></circle>
<circle cx="212" cy="58" r="1.2"><animate attributeName="opacity" values=".3;1;.3" dur="4.6s" repeatCount="indefinite"/></circle>
</g>
<circle cx="312" cy="84" r="58" fill="url(#h)"><animate attributeName="r" values="58;63;58" dur="9s" repeatCount="indefinite"/></circle>
<circle cx="312" cy="84" r="30" fill="#f7e0ac"/>
<circle cx="303" cy="77" r="5" fill="#e2c48d" opacity=".6"/><circle cx="320" cy="92" r="4" fill="#e2c48d" opacity=".5"/><circle cx="313" cy="70" r="2.6" fill="#e2c48d" opacity=".5"/>
<circle cx="84" cy="56" r="8" fill="#e8c9d8" opacity=".85"/>
<rect x="36" y="238" width="150" height="3" rx="1.5" fill="#f2a05e" opacity=".32"/>
<rect x="180" y="252" width="190" height="3.4" rx="1.7" fill="#e78a4e" opacity=".3"/>
<rect x="70" y="266" width="230" height="4" rx="2" fill="#d96a52" opacity=".26"/>
<g stroke="#1a1230" stroke-width="1.5" fill="none" opacity=".9">
<path d="M0 0q4-4 8 0q4-4 8 0" transform="translate(136,116)"/>
<path d="M0 0q4-4 8 0q4-4 8 0" transform="translate(160,128) scale(.65)"/>
<animateTransform attributeName="transform" type="translate" values="0 0;10 -4;0 0" dur="11s" repeatCount="indefinite"/>
</g>
<use href="#isl"/>
<use href="#arc" stroke="#0e0a20" stroke-width="10" stroke-dasharray="13 7"/>
<use href="#arc" stroke="#f2a95c" stroke-width="3.4" stroke-dasharray="13 7"/>
<ellipse cx="200" cy="186" rx="46" ry="9" fill="#f2a95c" opacity=".1" filter="url(#g)"/>
<g fill="#241a45" stroke="#e8975a" stroke-width=".7">
<g><rect x="203" y="148" width="10" height="4" rx="1" transform="rotate(-9 208 150)"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0" dur="6s" repeatCount="indefinite"/></g>
<g><rect x="220" y="132" width="8" height="3.4" rx="1" transform="rotate(-15 224 134)"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur="7.5s" repeatCount="indefinite"/></g>
<g><rect x="234" y="118" width="6" height="2.8" rx=".9" transform="rotate(8 237 119)"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -8;0 0" dur="9s" repeatCount="indefinite"/></g>
</g>
<g stroke="#3a2c55" stroke-width="1.4">
<line x1="156" y1="183" x2="156" y2="174"/><line x1="200" y1="177" x2="200" y2="168"/><line x1="244" y1="183" x2="244" y2="174"/>
</g>
<g fill="#ffd27a" filter="url(#g)">
<circle cx="156" cy="172.5" r="2.4"><animate attributeName="opacity" values="1;.5;1" dur="3.2s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="166.5" r="2.4"><animate attributeName="opacity" values=".5;1;.5" dur="2.6s" repeatCount="indefinite"/></circle>
<circle cx="244" cy="172.5" r="2.4"><animate attributeName="opacity" values="1;.4;1" dur="3.8s" repeatCount="indefinite"/></circle>
</g>
<rect y="290" width="400" height="110" fill="url(#w)"/>
<rect y="288.5" width="400" height="2.5" fill="#f7b558" opacity=".8" filter="url(#g)"/>
<g transform="translate(0,522) scale(1,-.8)" filter="url(#r)" opacity=".85">
<use href="#isl" opacity=".6"/>
<use href="#arc" stroke="#241a45" stroke-width="10"/>
<use href="#arc" stroke="#f2a95c" stroke-width="3.4" opacity=".9"/>
</g>
<g fill="#ffd27a" opacity=".7" filter="url(#g)">
<circle cx="156" cy="384" r="2"/><circle cx="200" cy="389" r="2.2"/><circle cx="244" cy="384" r="2"/>
</g>
<ellipse cx="312" cy="352" rx="6" ry="40" fill="url(#h)" opacity=".5"/>
<g stroke="#f7c98a" stroke-width="1" opacity=".35">
<line x1="296" y1="306" x2="330" y2="306"/><line x1="302" y1="322" x2="324" y2="322"/><line x1="298" y1="342" x2="328" y2="342"/>
</g>
<path d="M20 316h60M110 336h70M250 356h90M60 368h80M300 380h70" stroke="#7a4a70" stroke-width="1" stroke-linecap="round" opacity=".45" fill="none"/>
<rect width="400" height="400" fill="url(#v)"/>
</svg>
```