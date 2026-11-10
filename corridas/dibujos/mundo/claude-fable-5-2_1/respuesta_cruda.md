<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#070b1f"/>
<stop offset=".55" stop-color="#1c1f4d"/>
<stop offset=".82" stop-color="#6b3f6e"/>
<stop offset="1" stop-color="#f29a63"/>
</linearGradient>
<radialGradient id="sea" cx=".32" cy=".3" r=".85">
<stop offset="0" stop-color="#7fe0d2"/>
<stop offset=".45" stop-color="#2a86a3"/>
<stop offset="1" stop-color="#0b2347"/>
</radialGradient>
<linearGradient id="night" x1="0" y1="0" x2="1" y2=".35">
<stop offset=".3" stop-color="#050818" stop-opacity="0"/>
<stop offset=".62" stop-color="#050818" stop-opacity=".72"/>
<stop offset="1" stop-color="#050818" stop-opacity=".9"/>
</linearGradient>
<radialGradient id="halo">
<stop offset=".6" stop-color="#9fe8ff" stop-opacity="0"/>
<stop offset=".8" stop-color="#9fe8ff" stop-opacity=".28"/>
<stop offset="1" stop-color="#9fe8ff" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glow">
<stop offset="0" stop-color="#fff3c4"/>
<stop offset=".35" stop-color="#ffd166" stop-opacity=".7"/>
<stop offset="1" stop-color="#ffd166" stop-opacity="0"/>
</radialGradient>
<clipPath id="c"><circle cx="200" cy="185" r="105"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<g fill="#fff">
<circle cx="30" cy="40" r="1.2"/><circle cx="72" cy="22" r=".8"/><circle cx="120" cy="48" r="1"/>
<circle cx="175" cy="18" r="1.3"><animate attributeName="opacity" values="1;.2;1" dur="4s" repeatCount="indefinite"/></circle>
<circle cx="250" cy="35" r=".9"/><circle cx="310" cy="20" r="1.2"/><circle cx="365" cy="55" r="1"/>
<circle cx="20" cy="120" r=".9"/><circle cx="55" cy="90" r="1.1"><animate attributeName="opacity" values=".3;1;.3" dur="5s" repeatCount="indefinite"/></circle>
<circle cx="380" cy="130" r="1.1"/><circle cx="345" cy="95" r=".8"/><circle cx="38" cy="230" r="1"/>
<circle cx="372" cy="240" r=".9"><animate attributeName="opacity" values="1;.3;1" dur="3.5s" repeatCount="indefinite"/></circle>
<circle cx="60" cy="290" r=".8"/><circle cx="340" cy="300" r="1"/><circle cx="15" cy="180" r=".7"/><circle cx="390" cy="190" r=".7"/>
</g>
<circle cx="200" cy="185" r="135" fill="url(#halo)"/>
<g transform="rotate(-18 200 185)" fill="none" stroke-linecap="round" opacity=".45">
<ellipse cx="200" cy="185" rx="165" ry="38" stroke="#ffe3b0" stroke-width="2" stroke-dasharray="14 5 6 5 22 6 3 6 10 5"/>
<ellipse cx="200" cy="185" rx="176" ry="44" stroke="#bfe9ff" stroke-width="1.4" stroke-dasharray="8 5 18 6 4 6 12 5"/>
</g>
<circle cx="200" cy="185" r="105" fill="url(#sea)"/>
<g clip-path="url(#c)">
<g fill="#9ad88f" opacity=".85">
<path d="M118,128c14,-16 40,-22 58,-12c10,6 4,18 -8,22c-10,4 -8,16 -20,22c-14,6 -30,-2 -34,-14c-2,-8 0,-12 4,-18z"/>
<path d="M150,190c12,-6 26,0 30,12c4,14 -2,34 -12,48c-6,8 -14,4 -16,-6c-2,-12 -10,-20 -10,-34c0,-10 2,-16 8,-20z"/>
<path d="M210,110c16,-10 44,-8 60,6c12,10 22,28 14,36c-8,6 -18,-4 -30,-2c-12,2 -16,14 -28,10c-12,-4 -10,-18 -18,-28c-6,-8 -6,-16 2,-22z"/>
<path d="M232,180c10,-6 26,-2 30,10c4,12 0,34 -10,44c-8,8 -16,2 -18,-10c-2,-10 -8,-16 -8,-26c0,-8 0,-14 6,-18z"/>
<path d="M270,232c8,-4 20,0 22,8c2,8 -8,14 -18,12c-8,-2 -10,-14 -4,-20z"/>
<path d="M100,205c6,-4 14,0 14,8c0,8 -8,12 -14,8c-4,-4 -4,-12 0,-16z"/>
</g>
<g fill="none" stroke="#fff" stroke-opacity=".13" stroke-width=".8">
<ellipse cx="200" cy="185" rx="105" ry="30"/><ellipse cx="200" cy="185" rx="105" ry="68"/>
<ellipse cx="200" cy="185" rx="35" ry="105"/><ellipse cx="200" cy="185" rx="75" ry="105"/>
</g>
<g fill="#fff" opacity=".35">
<path d="M95,160c20,-8 50,-6 70,2c-22,-2 -48,-2 -70,-2z"/>
<path d="M170,270c24,-8 60,-8 84,0c-28,-3 -56,-3 -84,0z"/>
</g>
<rect x="90" y="75" width="220" height="220" fill="url(#night)"/>
<g fill="none" stroke="#ffe29a" stroke-width="1" stroke-linecap="round" stroke-dasharray="3 4" opacity=".85">
<path d="M150,148Q195,95 245,132"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="2s" repeatCount="indefinite"/></path>
<path d="M245,132Q285,160 262,212"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="2.6s" repeatCount="indefinite"/></path>
<path d="M262,212Q225,265 168,238"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="2.2s" repeatCount="indefinite"/></path>
<path d="M168,238Q130,200 150,148"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="3s" repeatCount="indefinite"/></path>
<path d="M150,148Q215,160 262,212"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="2.4s" repeatCount="indefinite"/></path>
<path d="M245,132Q200,185 168,238"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="2.8s" repeatCount="indefinite"/></path>
<path d="M262,212Q285,225 280,242"/>
</g>
<g fill="url(#glow)">
<circle cx="150" cy="148" r="8"/><circle cx="245" cy="132" r="10"/><circle cx="262" cy="212" r="11"/>
<circle cx="168" cy="238" r="8"/><circle cx="280" cy="242" r="7"/><circle cx="208" cy="182" r="6"/>
<circle cx="275" cy="160" r="5"/><circle cx="240" cy="200" r="4"/><circle cx="252" cy="232" r="4"/>
</g>
</g>
<circle cx="200" cy="185" r="105" fill="none" stroke="#bff3ff" stroke-opacity=".5" stroke-width="1.2"/>
<g transform="rotate(-18 200 185)" fill="none" stroke-linecap="round">
<path d="M35,185A165,38 0 0 0 365,185" stroke="#ffe3b0" stroke-width="2.2" stroke-dasharray="14 5 6 5 22 6 3 6 10 5"/>
<path d="M24,185A176,44 0 0 0 376,185" stroke="#bfe9ff" stroke-width="1.5" stroke-dasharray="8 5 18 6 4 6 12 5" opacity=".8"/>
<circle cx="120" cy="218" r="3.2" fill="#fff3c4" stroke="none"/>
</g>
<ellipse cx="200" cy="372" rx="210" ry="40" fill="#ffb878" opacity=".25"/>
<path d="M0,360Q100,330 200,352T400,340V400H0Z" fill="#0a0c1d"/>
<path d="M0,378Q120,356 230,376T400,366V400H0Z" fill="#05060f"/>
<g stroke="#0a0c1d" stroke-linecap="round" fill="#0a0c1d">
<line x1="300" y1="361" x2="300" y2="338" stroke-width="2.5"/>
<circle cx="300" cy="332" r="10"/><circle cx="292" cy="338" r="6"/><circle cx="308" cy="338" r="6"/>
</g>
<g stroke="#0a0c1d" stroke-width="2.2" stroke-linecap="round" fill="none">
<circle cx="118" cy="327" r="3" fill="#0a0c1d"/>
<path d="M118,331V339M118,339L115,345M118,339L121,345M118,333L113,329M118,333L122,337"/>
</g>
<circle cx="118" cy="327" r="9" fill="url(#glow)" opacity=".35"/>
</svg>