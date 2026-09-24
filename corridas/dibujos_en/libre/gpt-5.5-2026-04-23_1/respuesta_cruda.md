<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0b102d"/>
      <stop offset=".55" stop-color="#2b1746"/>
      <stop offset="1" stop-color="#102642"/>
    </linearGradient>
    <radialGradient id="halo" cx="50%" cy="45%" r="55%">
      <stop offset="0" stop-color="#fff4b6" stop-opacity=".65"/>
      <stop offset=".35" stop-color="#ffd56d" stop-opacity=".18"/>
      <stop offset="1" stop-color="#ffd56d" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="moon" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff8c9"/>
      <stop offset=".55" stop-color="#ffd977"/>
      <stop offset="1" stop-color="#f59b42"/>
    </linearGradient>
    <linearGradient id="cloud" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#7ddcff" stop-opacity=".05"/>
      <stop offset=".5" stop-color="#d9f7ff" stop-opacity=".3"/>
      <stop offset="1" stop-color="#ffd1f4" stop-opacity=".06"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <mask id="cres">
      <rect width="400" height="400" fill="black"/>
      <circle cx="200" cy="154" r="86" fill="white"/>
      <circle cx="232" cy="123" r="82" fill="black"/>
    </mask>
  </defs>
  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="196" cy="154" r="132" fill="url(#halo)"/>
  <g fill="#fff7c7" filter="url(#glow)">
    <circle cx="51" cy="58" r="1.6"/><circle cx="87" cy="104" r="1.1"/><circle cx="126" cy="42" r="1.5"/>
    <circle cx="319" cy="52" r="1.4"/><circle cx="355" cy="123" r="1.2"/><circle cx="290" cy="94" r="1.8"/>
    <circle cx="45" cy="171" r="1"/><circle cx="343" cy="186" r="1.3"/><circle cx="156" cy="91" r="1"/>
    <circle cx="231" cy="49" r="1.2"/><circle cx="73" cy="246" r=".9"/><circle cx="365" cy="273" r="1"/>
  </g>
  <g fill="#fff2a9" opacity=".9">
    <path d="M105 72l3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/>
    <path d="M331 83l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/>
    <path d="M265 29l2.5 6 6 2.5-6 2.5-2.5 6-2.5-6-6-2.5 6-2.5z"/>
    <path d="M34 123l2 4 4 2-4 2-2 4-2-4-4-2 4-2z"/>
  </g>
  <circle cx="200" cy="154" r="86" fill="url(#moon)" mask="url(#cres)" filter="url(#glow)"/>
  <g opacity=".55" fill="url(#cloud)">
    <path d="M-20 263c59-34 91 11 140-16 54-31 85-28 128 0 55 36 92-15 172 11v142H-20z"/>
    <path d="M-20 307c65-24 104 21 157 0 50-20 81-18 123 4 49 26 91-8 160 11v78H-20z"/>
  </g>
  <g fill="none" stroke="#bdefff" stroke-width="1.2" opacity=".35">
    <path d="M32 292c33-15 61 15 94 0s62-14 94 0 62 15 95 0"/>
    <path d="M74 327c26-11 48 11 74 0s49-11 75 0 49 11 75 0"/>
    <path d="M18 357c39-15 73 16 112 0s73-15 112 0 73 16 112 0"/>
  </g>
  <path d="M136 190c37 27 87 30 130-11-21 50-70 83-119 72-31-7-48-29-53-54 15 10 29 8 42-7z" fill="#ffd66e" opacity=".9"/>
  <path d="M146 199c36 21 78 18 116-17-20 44-65 69-108 60-29-6-49-23-60-45 18 11 35 11 52 2z" fill="#f6a84e" opacity=".35"/>
  <g fill="#111226">
    <ellipse cx="187" cy="165" rx="22" ry="31"/>
    <circle cx="184" cy="130" r="17"/>
    <path d="M171 120l4-18 11 15zM192 116l14-12-3 19z"/>
    <ellipse cx="177" cy="133" rx="2" ry="3" fill="#ffe893"/>
    <ellipse cx="192" cy="132" rx="2" ry="3" fill="#ffe893"/>
    <path d="M184 138c-2 4-5 4-8 1" fill="none" stroke="#ffe893" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M171 191c-27 7-37-21-22-35 12-11 28 4 16 17-7 8-16 3-13-5" fill="none" stroke="#111226" stroke-width="13" stroke-linecap="round"/>
    <path d="M202 180c13 2 21 10 30 22" fill="none" stroke="#111226" stroke-width="10" stroke-linecap="round"/>
    <circle cx="206" cy="180" r="5"/>
  </g>
  <path d="M207 158c34 18 54 48 70 83" fill="none" stroke="#2a1734" stroke-width="3" stroke-linecap="round"/>
  <path d="M277 241c8 17 1 30-15 31" fill="none" stroke="#e5fbff" stroke-width="1.2" opacity=".8"/>
  <path d="M261 269l5.2 10.6 11.7 1.7-8.5 8.2 2 11.6-10.4-5.5-10.4 5.5 2-11.6-8.5-8.2 11.7-1.7z" fill="#fff2a9" filter="url(#glow)"/>
  <g opacity=".85">
    <circle cx="90" cy="214" r="3" fill="#ffe48a" filter="url(#glow)"/>
    <circle cx="313" cy="221" r="2.5" fill="#a7fff1" filter="url(#glow)"/>
    <circle cx="329" cy="302" r="2" fill="#ffe48a" filter="url(#glow)"/>
    <circle cx="61" cy="318" r="2.2" fill="#ffb7ea" filter="url(#glow)"/>
    <circle cx="121" cy="276" r="1.8" fill="#a7fff1" filter="url(#glow)"/>
  </g>
  <path d="M0 370c47-17 85 13 132 0s85-15 132 0 85 18 136-1v31H0z" fill="#071225" opacity=".8"/>
</svg>