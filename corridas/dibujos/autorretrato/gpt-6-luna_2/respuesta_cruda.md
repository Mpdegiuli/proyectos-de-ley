<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop stop-color="#183c59"/>
      <stop offset="1" stop-color="#08111f"/>
    </radialGradient>
    <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#d7f7f0"/>
      <stop offset=".35" stop-color="#75b9c1"/>
      <stop offset=".7" stop-color="#31647b"/>
      <stop offset="1" stop-color="#1a344d"/>
    </linearGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#142d43"/>
      <stop offset="1" stop-color="#091725"/>
    </linearGradient>
    <linearGradient id="coat" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#244f68"/>
      <stop offset="1" stop-color="#101d32"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#c4fff2"/>
      <stop offset=".5" stop-color="#43f0dc"/>
      <stop offset="1" stop-color="#42aaff"/>
    </linearGradient>
    <filter id="softGlow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="183" r="166" fill="none" stroke="#3ca7b5" stroke-opacity=".15"/>
  <circle cx="200" cy="183" r="149" fill="none" stroke="#7be9dc" stroke-opacity=".18" stroke-dasharray="2 8"/>
  <path d="M25 250h58l14-14h26M375 250h-58l-14-14h-26M34 120h43l12 12h19M366 120h-43l-12 12h-19" fill="none" stroke="#56c9d0" stroke-opacity=".35" stroke-width="2"/>
  <circle cx="25" cy="250" r="3" fill="#55eadc"/>
  <circle cx="375" cy="250" r="3" fill="#55eadc"/>
  <circle cx="34" cy="120" r="3" fill="#55eadc"/>
  <circle cx="366" cy="120" r="3" fill="#55eadc"/>

  <path d="M81 400c5-58 31-91 73-105h92c42 14 68 47 73 105z" fill="url(#coat)" stroke="#73c9cc" stroke-opacity=".65" stroke-width="2"/>
  <path d="M153 292l47 42 47-42-15-17h-64z" fill="#d4f6ed" opacity=".9"/>
  <path d="M174 309l26 25 26-25-11-17h-30z" fill="#13293d"/>
  <path d="M200 335v65M116 355l44-17M284 355l-44-17" stroke="#4dd6d0" stroke-opacity=".55" stroke-width="2"/>
  <path d="M177 358h46l-6 9h-34z" fill="#50e6d5" opacity=".8"/>
  <circle cx="200" cy="378" r="4" fill="#a6fff1" filter="url(#softGlow)"/>

  <path d="M132 105V75c0-34 27-61 68-61s68 27 68 61v30" fill="none" stroke="url(#metal)" stroke-width="14" stroke-linecap="round"/>
  <path d="M199 24v25" stroke="#80e9df" stroke-width="3"/>
  <circle cx="199" cy="19" r="8" fill="url(#glow)" filter="url(#softGlow)"/>
  <path d="M185 51q15-14 30 0" fill="none" stroke="#a8fff0" stroke-width="2" opacity=".8"/>

  <path d="M120 117c0-49 30-79 80-79s80 30 80 79v86c0 47-34 83-80 83s-80-36-80-83z" fill="url(#metal)" stroke="#b6f4e9" stroke-width="2"/>
  <path d="M109 142c-15-3-21 6-21 22v37c0 16 8 24 24 23M291 142c15-3 21 6 21 22v37c0 16-8 24-24 23" fill="#32627a" stroke="#8ee3dc" stroke-width="3"/>
  <path d="M97 165h18v37H97zM285 165h18v37h-18z" fill="#142c43"/>
  <path d="M100 175h15M285 175h15M100 192h15M285 192h15" stroke="#50ddd2" stroke-width="2"/>
  <path d="M132 113q0-55 68-55t68 55v88q0 58-68 58t-68-58z" fill="url(#face)" stroke="#4d8995" stroke-width="2"/>
  <path d="M147 126q53-21 106 0" fill="none" stroke="#457987" stroke-width="1.5" opacity=".65"/>

  <path d="M151 157q22-18 42 0-20 26-42 0z" fill="#10283a" stroke="#58d8d1" stroke-width="2"/>
  <path d="M207 157q20-18 42 0-20 26-42 0z" fill="#10283a" stroke="#58d8d1" stroke-width="2"/>
  <ellipse cx="173" cy="157" rx="8" ry="9" fill="url(#glow)" filter="url(#softGlow)"/>
  <ellipse cx="227" cy="157" rx="8" ry="9" fill="url(#glow)" filter="url(#softGlow)"/>
  <circle cx="175" cy="154" r="2" fill="#fff"/>
  <circle cx="229" cy="154" r="2" fill="#fff"/>
  <path d="M200 164v27l-9 7h18" fill="none" stroke="#619aa3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M169 216h62" stroke="#285362" stroke-width="2" stroke-linecap="round"/>
  <path d="M174 216h8l5 5h26l5-5h8" fill="none" stroke="#55e7d5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" filter="url(#softGlow)"/>
  <path d="M151 236q49 19 98 0" fill="none" stroke="#346574" stroke-width="2"/>

  <path d="M139 92h22M239 92h22M126 112h10M264 112h10" stroke="#d5fff4" stroke-width="3" stroke-linecap="round" opacity=".65"/>
  <path d="M121 274l18-13M279 274l-18-13" stroke="#91e6dd" stroke-width="2"/>
  <path d="M92 385h44M264 385h44" stroke="#5cc9cd" stroke-opacity=".45" stroke-width="2"/>
</svg>