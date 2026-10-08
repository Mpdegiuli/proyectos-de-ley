<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400" role="img">
<title>El mundo como me gustaría</title>
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#141736"/>
<stop offset=".45" stop-color="#4a3f77"/>
<stop offset=".72" stop-color="#b25f80"/>
<stop offset=".9" stop-color="#ea8a5e"/>
<stop offset="1" stop-color="#f8b268"/>
</linearGradient>
<radialGradient id="sun">
<stop offset="0" stop-color="#fff7da"/>
<stop offset=".55" stop-color="#ffd27a"/>
<stop offset="1" stop-color="#ff9c4a"/>
</radialGradient>
<radialGradient id="halo">
<stop offset="0" stop-color="#ffe9b0" stop-opacity=".85"/>
<stop offset="1" stop-color="#ffe9b0" stop-opacity="0"/>
</radialGradient>
<radialGradient id="core">
<stop offset="0" stop-color="#fffdf4"/>
<stop offset=".6" stop-color="#ffe08a"/>
<stop offset="1" stop-color="#ffb35c" stop-opacity=".15"/>
</radialGradient>
<linearGradient id="gFar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7c6aa9"/><stop offset="1" stop-color="#5a5192"/></linearGradient>
<linearGradient id="gMid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f8a76"/><stop offset="1" stop-color="#2b5f55"/></linearGradient>
<linearGradient id="gNear" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b5e4f"/><stop offset="1" stop-color="#1c453b"/></linearGradient>
<linearGradient id="gFg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#234e43"/><stop offset="1" stop-color="#152f29"/></linearGradient>
<linearGradient id="gRio" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe6a6"/><stop offset="1" stop-color="#f09c58"/></linearGradient>
<radialGradient id="vig" cx=".5" cy=".42" r=".72">
<stop offset=".62" stop-color="#0b0e24" stop-opacity="0"/>
<stop offset="1" stop-color="#0b0e24" stop-opacity=".42"/>
</radialGradient>
<filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
<feGaussianBlur stdDeviation="2.6" result="b"/>
<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="soft" x="-70%" y="-70%" width="240%" height="240%"><feGaussianBlur stdDeviation="7"/></filter>
<mask id="mMoon"><rect x="40" y="30" width="42" height="42" fill="#fff"/><circle cx="64" cy="44" r="9.5" fill="#000"/></mask>
<path id="arc" d="M52,98 Q200,44 348,98" fill="none"/>
</defs>

<rect width="400" height="400" fill="url(#sky)"/>

<g fill="#fff" opacity=".85">
<circle cx="30" cy="30" r="1.4"><animate attributeName="opacity" values=".25;1;.25" dur="3.4s" repeatCount="indefinite"/></circle>
<circle cx="120" cy="24" r="1.1"/>
<circle cx="168" cy="58" r=".9"/>
<circle cx="210" cy="30" r="1.3"><animate attributeName="opacity" values="1;.2;1" dur="4.6s" begin="-2s" repeatCount="indefinite"/></circle>
<circle cx="258" cy="50" r="1"/>
<circle cx="296" cy="22" r="1.4"><animate attributeName="opacity" values=".3;1;.3" dur="5.2s" begin="-1s" repeatCount="indefinite"/></circle>
<circle cx="372" cy="30" r="1.1"/>
<circle cx="382" cy="72" r="1"/>
<circle cx="26" cy="88" r="1"><animate attributeName="opacity" values=".2;1;.2" dur="4s" begin="-3s" repeatCount="indefinite"/></circle>
<circle cx="60" cy="118" r=".9"/>
<circle cx="342" cy="106" r="1"/>
</g>
<circle cx="58" cy="48" r="11" fill="#f6e7c8" opacity=".9" mask="url(#mMoon)"/>

<g stroke="#3a2b52" stroke-width="2" fill="none" stroke-linecap="round" opacity=".85">
<path d="M96,120 q7,-7 14,0 q7,-7 14,0"/>
<path d="M146,98 q5,-6 11,0 q5,-6 11,0"/>
<animateTransform attributeName="transform" type="translate" values="0,0;7,-4;0,0" dur="10s" repeatCount="indefinite"/>
</g>

<circle cx="200" cy="250" r="80" fill="url(#halo)" filter="url(#soft)" opacity=".55">
<animate attributeName="opacity" values=".4;.7;.4" dur="6s" repeatCount="indefinite"/>
</circle>
<circle cx="200" cy="250" r="42" fill="url(#sun)"/>

<path d="M158,180 l1.4,3.4 3.4,1.4 -3.4,1.4 -1.4,3.4 -1.4,-3.4 -3.4,-1.4 3.4,-1.4 Z" fill="#ffe9b0">
<animate attributeName="opacity" values=".3;.9;.3" dur