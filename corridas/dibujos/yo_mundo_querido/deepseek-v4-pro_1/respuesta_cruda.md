<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4fc3f7"/>
      <stop offset="100%" stop-color="#e1f5fe"/>
    </linearGradient>
    <linearGradient id="hill1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8bc34a"/>
      <stop offset="100%" stop-color="#558b2f"/>
    </linearGradient>
    <linearGradient id="hill2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#aed581"/>
      <stop offset="100%" stop-color="#689f38"/>
    </linearGradient>
    <linearGradient id="sunGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fff176"/>
      <stop offset="100%" stop-color="#ffb300"/>
    </linearGradient>
    <radialGradient id="sunGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff9c4" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#fff9c4" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="riverGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#81d4fa"/>
      <stop offset="100%" stop-color="#0277bd"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <circle cx="70" cy="70" r="40" fill="url(#sunGlow)" opacity="0.7"/>
  <circle cx="70" cy="70" r="25" fill="url(#sunGrad)"/>
  <g stroke="#ffca28" stroke-width="3" stroke-linecap="round">
    <line x1="70" y1="30" x2="70" y2="15"/>
    <line x1="70" y1="110" x2="70" y2="125"/>
    <line x1="30" y1="70" x2="15" y2="70"/>
    <line x1="110" y1="70" x2="125" y2="70"/>
    <line x1="42" y1="42" x2="32" y2="32"/>
    <line x1="98" y1="42" x2="108" y2="32"/>
    <line x1="42" y1="98" x2="32" y2="108"/>
    <line x1="98" y1="98" x2="108" y2="108"/>
  </g>

  <g transform="translate(330,90)" opacity="0.7">
    <path d="M-50,0 A50,50 0 0,1 50,0" fill="none" stroke="#e53935" stroke-width="6"/>
    <path d="M-44,0 A44,44 0 0,1 44,0" fill="none" stroke="#fb8c00" stroke-width="6"/>
    <path d="M-38,0 A38,38 0 0,1 38,0" fill="none" stroke="#fdd835" stroke-width="6"/>
    <path d="M-32,0 A32,32 0 0,1 32,0" fill="none" stroke="#43a047" stroke-width="6"/>
    <path d="M-26,0 A26,26 0 0,1 26,0" fill="none" stroke="#1e88e5" stroke-width="6"/>
    <path d="M-20,0 A20,20 0 0,1 20,0" fill="none" stroke="#8e24aa" stroke-width="6"/>
    <path d="M-14,0 A14,14 0 0,1 14,0" fill="none" stroke="#ec407a" stroke-width="6"/>
  </g>

  <g fill="white" opacity="0.9">
    <circle cx="150" cy="60" r="20"/>
    <circle cx="170" cy="50" r="25"/>
    <circle cx="190" cy="60" r="20"/>
    <circle cx="170" cy="65" r="22"/>
  </g>
  <g fill="white" opacity="0.8">
    <circle cx="280" cy="40" r="15"/>
    <circle cx="295" cy="32" r="20"/>
    <circle cx="310" cy="40" r="15"/>
    <circle cx="295" cy="45" r="18"/>
  </g>

  <polygon points="0,200 80,120 160,200" fill="#6d4c41" opacity="0.6"/>
  <polygon points="100,200 190,100 280,200" fill="#795548" opacity="0.7"/>
  <polygon points="240,200 320,130 400,200" fill="#5d4037" opacity="0.6"/>
  <polygon points="190,100 175,125 183,118 190,130 197,118 205,125" fill="white" opacity="0.9"/>
  <polygon points="320,130 308,148 315,143 320,152 325,143 332,148" fill="white" opacity="0.9"/>

  <path d="M0,250 Q100,200 200,240 T400,240 L400,400 L0,400 Z" fill="url(#hill2)"/>
  <path d="M0,280 Q120,230 240,270 T400,260 L400,400 L0,400 Z" fill="url(#hill1)"/>

  <path d="M200,240 C180,270 220,290 200,320 C180,350 240,370 220,400" fill="none" stroke="url(#riverGrad)" stroke-width="20" stroke-linecap="round"/>
  <path d="M200,240 C180,270 220,290 200,320 C180,350 240,370 220,400" fill="none" stroke="#b3e5fc" stroke-width="6" stroke-linecap="round" opacity="0.5"/>

  <rect x="80" y="240" width="8" height="40" fill="#795548" rx="2"/>
  <circle cx="84" cy="225" r="30" fill="#66bb6a"/>
  <circle cx="70" cy="215" r="8" fill="#66bb6a"/>
  <circle cx="98" cy="215" r="8" fill="#66bb6a"/>
  <circle cx="84" cy="205" r="10" fill="#66bb6a"/>
  <circle cx="72" cy="225" r="5" fill="#e53935"/>
  <circle cx="92" cy="220" r="5" fill="#e53935"/>
  <circle cx="84" cy="210" r="5" fill="#e53935"/>

  <rect x="280" y="240" width="8" height="40" fill="#795548" rx="2"/>
  <circle cx="284" cy="225" r="28" fill="#81c784"/>
  <circle cx="270" cy="215" r="7" fill="#81c784"/>
  <circle cx="298" cy="215" r="7" fill="#81c784"/>
  <circle cx="284" cy="205" r="9" fill="#81c784"/>
  <circle cx="275" cy="225" r="5" fill="#ffb300"/>
  <circle cx="290" cy="220" r="5" fill="#ffb300"/>

  <polygon points="340,220 320,260 360,260" fill="#2e7d32"/>
  <polygon points="340,200 325,235 355,235" fill="#388e3c"/>
  <rect x="336" y="260" width="8" height="20" fill="#5d4037"/>

  <rect x="120" y="220" width="12" height="40" fill="#f5f5f5" rx="2"/>
  <polygon points="126,220 112,230 126,240 140,230" fill="#e0e0e0"/>
  <g transform="translate(126,225)">
    <rect x="-3" y="-35" width="6" height="35" fill="#bdbdbd" rx="2"/>
    <rect x="-3" y="0" width="6" height="35" fill="#bdbdbd" rx="2"/>
    <rect x="-35" y="-3" width="35" height="6" fill="#bdbdbd" rx="2"/>
    <rect x="0" y="-3" width="35" height="6" fill="#bdbdbd" rx="2"/>
    <circle cx="0" cy="0" r="5" fill="#757575"/>
  </g>

  <g>
    <circle cx="50" cy="320" r="4" fill="#f06292"/>
    <circle cx="50" cy="320" r="2" fill="#f8bbd0"/>
    <circle cx="60" cy="330" r="4" fill="#ba68c8"/>
    <circle cx="60" cy="330" r="2" fill="#e1bee7"/>
    <circle cx="40" cy="335" r="4" fill="#f06292"/>
    <circle cx="40" cy="335" r="2" fill="#f8bbd0"/>
    <circle cx="70" cy="310" r="5" fill="#ff7043"/>
    <circle cx="70" cy="310" r="2" fill="#ffe0b2"/>
    <circle cx="30" cy="345" r="4" fill="#4fc3f7"/>
    <circle cx="30" cy="345" r="2" fill="#b3e5fc"/>
    <circle cx="90" cy="340" r="5" fill="#fff176"/>
    <circle cx="90" cy="340" r="2" fill="#fff9c4"/>
  </g>

  <path d="M150,130 q-10,-10 -20,0 q10,-5 20,0" fill="none" stroke="#37474f" stroke-width="2"/>
  <path d="M170,120 q-8,-8 -16,0 q8,-4 16,0" fill="none" stroke="#37474f" stroke-width="2"/>
  <path d="M190,135 q-10,-10 -20,0 q10,-5 20,0" fill="none" stroke="#37474f" stroke-width="2"/>

  <g transform="translate(160,320)">
    <circle cx="-30" cy="-20" r="6" fill="#8d6e63"/>
    <rect x="-34" y="-12" width="8" height="20" fill="#e57373" rx="2"/>
    <line x1="-30" y1="8" x2="-30" y2="25" stroke="#5d4037" stroke-width="2"/>
    <line x1="-30" y1="25" x2="-36" y2="35" stroke="#5d4037" stroke-width="2"/>
    <line x1="-30" y1="25" x2="-24" y2="35" stroke="#5d4037" stroke-width="2"/>
    <line x1="-34" y1="-8" x2="-38" y2="0" stroke="#5d4037" stroke-width="2"/>
    <line x1="-26" y1="-8" x2="-22" y2="0" stroke="#5d4037" stroke-width="2"/>

    <circle cx="0" cy="-22" r="6" fill="#ffcc80"/>
    <rect x="-4" y="-14" width="8" height="20" fill="#64b5f6" rx="2"/>
    <line x1="0" y1="6" x2="0" y2="23" stroke="#5d4037" stroke-width="2"/>
    <line x1="0" y1="23" x2="-6" y2="33" stroke="#5d4037" stroke-width="2"/>
    <line x1="0" y1="23" x2="6" y2="33" stroke="#5d4037" stroke-width="2"/>
    <line x1="-4" y1="-10" x2="-8" y2="-2" stroke="#5d4037" stroke-width="2"/>
    <line x1="4" y1="-10" x2="8" y2="-2" stroke="#5d4037" stroke-width="2"/>

    <circle cx="30" cy="-20" r="6" fill="#a1887f"/>
    <rect x="26" y="-12" width="8" height="20" fill="#81c784" rx="2"/>
    <line x1="30" y1="8" x2="30" y2="25" stroke="#5d4037" stroke-width="2"/>
    <line x1="30" y1="25" x2="24" y2="35" stroke="#5d4037" stroke-width="2"/>
    <line x1="30" y1="25" x2="36" y2="35" stroke="#5d4037" stroke-width="2"/>
    <line x1="26" y1="-8" x2="22" y2="0" stroke="#5d4037" stroke-width="2"/>
    <line x1="34" y1="-8" x2="38" y2="0" stroke="#5d4037" stroke-width="2"/>

    <line x1="-22" y1="0" x2="-8" y2="-2" stroke="#5d4037" stroke-width="2"/>
    <line x1="8" y1="-2" x2="22" y2="0" stroke="#5d4037" stroke-width="2"/>
  </g>

  <g transform="translate(240,270)">
    <circle cx="0" cy="-15" r="10" fill="#ffe0b2"/>
    <rect x="-12" y="-5" width="24" height="30" fill="#e53935" rx="3"/>
    <line x1="-12" y1="5" x2="-35" y2="-10" stroke="#ffe0b2" stroke-width="4" stroke-linecap="round"/>
    <line x1="12" y1="5" x2="35" y2="-10" stroke="#ffe0b2" stroke-width="4" stroke-linecap="round"/>
    <circle cx="-35" cy="-10" r="3" fill="#ffe0b2"/>
    <circle cx="35" cy="-10" r="3" fill="#ffe0b2"/>
    <line x1="-6" y1="25" x2="-10" y2="40" stroke="#424242" stroke-width="4" stroke-linecap="round"/>
    <line x1="6" y1="25" x2="10" y2="40" stroke="#424242" stroke-width="4" stroke-linecap="round"/>
    <ellipse cx="-12" cy="42" rx="5" ry="3" fill="#37474f"/>
    <ellipse cx="12" cy="42" rx="5" ry="3" fill="#37474f"/>
    <circle cx="-3" cy="-17" r="1.5" fill="#333"/>
    <circle cx="3" cy="-17" r="1.5" fill="#333"/>
    <path d="M-4,-12 Q0,-9 4,-12" fill="none" stroke="#333" stroke-width="1.5"/>
    <path d="M0,-3 C-3,-6 -8,-2 0,5 C8,-2 3,-6 0,-3" fill="white" opacity="0.9"/>
  </g>

  <g transform="translate(220,180)">
    <path d="M0,15 C-15,-5 -30,10 0,30 C30,10 15,-5 0,15" fill="#e91e63" opacity="0.9"/>
    <line x1="0" y1="15" x2="0" y2="-10" stroke="#2e7d32" stroke-width="3" stroke-linecap="round"/>
    <path d="M0,-5 Q-10,-10 -15,-5" fill="none" stroke="#2e7d32" stroke-width="3" stroke-linecap="round"/>
    <path d="M0,-10 Q10,-15 15,-10" fill="none" stroke="#2e7d32" stroke-width="3" stroke-linecap="round"/>
    <circle cx="0" cy="-15" r="6" fill="#4caf50"/>
    <circle cx="-15" cy="-5" r="5" fill="#66bb6a"/>
    <circle cx="15" cy="-10" r="5" fill="#66bb6a"/>
  </g>

  <g transform="translate(120,200)">
    <ellipse cx="-5" cy="0" rx="5" ry="3" fill="#f48fb1" transform="rotate(-30)"/>
    <ellipse cx="5" cy="0" rx="5" ry="3" fill="#f48fb1" transform="rotate(30)"/>
    <circle cx="0" cy="0" r="1.5" fill="#333"/>
  </g>
  <g transform="translate(280,160)">
    <ellipse cx="-4" cy="0" rx="4" ry="2.5" fill="#ce93d8" transform="rotate(-30)"/>
    <ellipse cx="4" cy="0" rx="4" ry="2.5" fill="#ce93d8" transform="rotate(30)"/>
    <circle cx="0" cy="0" r="1.5" fill="#333"/>
  </g>
</svg>