<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<radialGradient id="sky" cx="50%" cy="42%" r="78%">
<stop offset="0" stop-color="#173650"/><stop offset=".55" stop-color="#0d1b2e"/><stop offset="1" stop-color="#04070d"/>
</radialGradient>
<radialGradient id="sea" cx="36%" cy="30%" r="78%">
<stop offset="0" stop-color="#3a91bb"/><stop offset=".6" stop-color="#1b5077"/><stop offset="1" stop-color="#0c2a44"/>
</radialGradient>
<radialGradient id="shade" cx="34%" cy="28%" r="82%">
<stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".6"/>
</radialGradient>
<linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#7fdca4"/><stop offset="1" stop-color="#2c8a68"/>
</linearGradient>
<linearGradient id="warm" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#fff0b8"/><stop offset=".5" stop-color="#ffb457"/><stop offset="1" stop-color="#ff6f6f"/>
</linearGradient>
<linearGradient id="grd" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#12283a"/><stop offset="1" stop-color="#04080e"/>
</linearGradient>
<filter id="glow" x="-70%" y="-70%" width="240%" height="240%">
<feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="soft" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="9"/></filter>
<clipPath id="gc"><circle cx="200" cy="195" r="110"/></clipPath>
</defs>

<rect width="400" height="400" fill="url(#sky)"/>

<g fill="#cfe9ff">
<circle cx="34" cy="46" r="1.1" opacity=".7"/><circle cx="78" cy="24" r=".8" opacity=".5"/>
<circle cx="122" cy="60" r="1" opacity=".6"/><circle cx="300" cy="38" r="1.2" opacity=".7"/>
<circle cx="356" cy="72" r=".9" opacity=".5"/><circle cx="372" cy="26" r="1" opacity=".6"/>
<circle cx="22" cy="140" r=".9" opacity=".45"/><circle cx="52" cy="212" r="1.1" opacity=".5"/>
<circle cx="368" cy="196" r="1" opacity=".5"/><circle cx="344" cy="262" r=".8" opacity=".4"/>
<circle cx="26" cy="286" r="1" opacity=".45"/><circle cx="160" cy="30" r=".7" opacity=".4"/>
<circle cx="248" cy="22" r=".8" opacity=".45"/><circle cx="386" cy="130" r=".7" opacity=".4"/>
</g>
<g fill="#7fd4ff" opacity=".25">
<circle cx="60" cy="96" r="1.6"/><circle cx="330" cy="112" r="1.6"/><circle cx="46" cy="248" r="1.6"/>
<circle cx="352" cy="228" r="1.6"/><circle cx="96" cy="42" r="1.6"/><circle cx="286" cy="60" r="1.6"/>
</g>

<ellipse cx="200" cy="195" rx="152" ry="54" transform="rotate(-22 200 195)" fill="none" stroke="#7fd4ff" stroke-opacity=".3" stroke-width="1" stroke-dasharray="4 7"/>
<circle cx="200" cy="195" r="126" fill="#4aa3c7" opacity=".2" filter="url(#soft)"/>

<circle cx="200" cy="195" r="110" fill="url(#sea)"/>
<g clip-path="url(#gc)">
<g fill="url(#land)" opacity=".9">
<path d="M140,110C155,105 166,120 158,132C150,145 160,150 155,165C150,180 160,190 155,205C150,225 145,246 135,256C128,263 121,250 126,238C130,222 122,210 128,196C133,182 125,170 130,155C134,140 128,120 140,110Z"/>
<path d="M205,120C225,112 246,118 250,130C255,142 240,150 238,162C236,176 246,185 240,200C235,218 226,236 215,241C205,245 199,230 205,218C210,205 199,195 205,182C210,168 197,155 200,140C201,130 198,124 205,120Z"/>
<path d="M254,108C276,102 297,114 299,128C301,141 285,147 274,143C264,139 254,146 249,136C245,126 247,112 254,108Z"/>
<path d="M274,214C285,209 297,216 295,227C293,237 280,239 273,232C268,227 268,217 274,214Z"/>
<path d="M168,262C178,258 190,264 188,272C186,280 172,281 167,275C163,270 163,264 168,262Z"/>
</g>
<g fill="none" stroke="#bfe9ff" stroke-opacity=".18" stroke-width=".9">
<ellipse cx="200" cy="195" rx="36" ry="110"/><ellipse cx="200" cy="195" rx="76" ry="110"/>
<ellipse cx="200" cy="195" rx="110" ry="13"/>
<ellipse cx="200" cy="145" rx="98" ry="11"/><ellipse cx="200" cy="245" rx="98" ry="11"/>
<ellipse cx="200" cy="110" rx="66" ry="8"/><ellipse cx="200" cy="280" rx="66" ry="8"/>
</g>
<g fill="none" stroke="#ffd9a0" stroke-opacity=".75" stroke-width="1.1" filter="url(#glow)">
<path d="M140,130Q195,90 250,126"/>
<path d="M140,130Q140,190 160,205"/>
<path d="M160,205Q205,240 240,192"/>
<path d="M240,192Q272,150 276,126"/>
<path d="M160,205Q140,245 132,252"/>
<path d="M240,192Q268,214 280,224"/>
<path d="M215,240Q170,268 132,252"/>
<path d="M250,126Q225,150 210,140"/>
<path d="M210,140Q170,120 140,130"/>
<path d="M280,224Q250,255 215,240"/>
</g>
<g fill="#fff3d0" filter="url(#glow)">
<circle cx="140" cy="130" r="2.6"/><circle cx="160" cy="205" r="2.6"/><circle cx="210" cy="140" r="2.2"/>
<circle cx="240" cy="192" r="2.8"/><circle cx="250" cy="126" r="2.2"/><circle cx="276" cy="126" r="2"/>
<circle cx="280" cy="224" r="2.2"/><circle cx="132" cy="252" r="2.2"/><circle cx="215" cy="240" r="2.4"/>
</g>
<path d="M199,84L207,120L191,150L209,186L195,216L211,251L200,306" fill="none" stroke="url(#warm)" stroke-width="2.4" stroke-linejoin="round" filter="url(#glow)" opacity=".95"/>
<path d="M209,186L232,196M191,150L168,158M211,251L232,262" fill="none" stroke="url(#warm)" stroke-width="1.3" opacity=".7" filter="url(#glow)"/>
<circle cx="200" cy="195" r="110" fill="url(#shade)"/>
</g>
<circle cx="200" cy="195" r="110" fill="none" stroke="#9fe8ff" stroke-opacity=".35"/>

<g filter="url(#glow)">
<rect x="335" y="135" width="7" height="7" rx="1.5" fill="#ffd9a0" transform="rotate(-22 338.5 138.5)"/>
<path d="M330,138h-9M352,138h-9" stroke="#7fd4ff" stroke-width="2" opacity=".8"/>
</g>

<g stroke="#7fdca4" fill="url(#land)">
<path d="M200,88C199,72 202,62 206,52" fill="none" stroke-width="2.6" stroke-linecap="round"/>
<path d="M206,64C215,55 228,57 231,66C222,75 210,73 206,64Z" stroke="none"/>
<path d="M203,76C193,69 181,72 179,81C188,89 199,85 203,76Z" stroke="none"/>
</g>
<circle cx="206" cy="50" r="2.4" fill="#fff3d0" filter="url(#glow)"/>

<ellipse cx="200" cy="352" rx="92" ry="15" fill="#ffb457" opacity=".2" filter="url(#soft)"/>
<path d="M0,400L0,372C90,338 310,338 400,372L400,400Z" fill="url(#grd)"/>
<path d="M0,372C90,338 310,338 400,372" fill="none" stroke="#ffb457" stroke-opacity=".35"/>

<g fill="none" stroke="#ffd9a0" stroke-opacity=".45" stroke-width="1" stroke-dasharray="3 5">
<path d="M124,327C108,292 118,250 145,232"/>
<path d="M276,327C292,292 282,250 255,232"/>
</g>

<g stroke="#ffd9a0" stroke-width="2" stroke-linecap="round" fill="#ffd9a0" filter="url(#glow)">
<circle cx="131" cy="326" r="3.4" stroke="none"/>
<path d="M131,330v10M131,340l-4,9M131,340l4,9M131,333l-7,-6M131,333l7,-6" fill="none"/>
<circle cx="269" cy="326" r="3.4" stroke="none"/>
<path d="M269,330v10M269,340l-4,9M269,340l4,9M269,333l-7,-6M269,333l7,-6" fill="none"/>
</g>
<g fill="#7fdca4" opacity=".65">
<path d="M60,364c0,-8 4,-13 4,-13s4,5 4,13z"/><path d="M336,366c0,-7 3,-11 3,-11s3,4 3,11z"/>
<path d="M92,372c0,-6 3,-9 3,-9s3,3 3,9z"/><path d="M306,372c0,-6 3,-9 3,-9s3,3 3,9z"/>
</g>
<g fill="#ffb457" opacity=".5">
<circle cx="176" cy="316" r="1.3"/><circle cx="224" cy="322" r="1.1"/><circle cx="200" cy="332" r="1.4"/>
<circle cx="152" cy="300" r="1"/><circle cx="248" cy="304" r="1"/>
</g>
</svg>