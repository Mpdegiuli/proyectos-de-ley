<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a1c3a"/>
      <stop offset="60%" stop-color="#142b4f"/>
      <stop offset="100%" stop-color="#1e3d5e"/>
    </linearGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff9c4" stop-opacity="0.9"/>
      <stop offset="40%" stop-color="#ffe082" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ffe082" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="moonFace" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fffde7"/>
      <stop offset="100%" stop-color="#ffd54f"/>
    </radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softGlow" x="-200%" y="-200%" width="400%" height="400%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <g id="tn1">
      <ellipse cx="0" cy="0" rx="5" ry="4.2" fill="#0d0d0d"/>
      <circle cx="1.8" cy="-1.2" r="1" fill="#fff"/>
      <circle cx="1.8" cy="-1.2" r="0.4" fill="#000"/>
      <path d="M4.5,0.5 Q9,-5,13,-1 T20,0 T27,-1" stroke="#0d0d0d" stroke-width="1.3" fill="none" stroke-linecap="round"/>
    </g>
    <g id="tn2">
      <use href="#tn1"/>
      <line x1="-4" y1="-3.5" x2="-4" y2="-14" stroke="#0d0d0d" stroke-width="1.2"/>
      <path d="M-4,-14 Q1,-11,5,-8" stroke="#0d0d0d" stroke-width="1" fill="none"/>
    </g>
    <g id="tn3">
      <use href="#tn2"/>
      <path d="M-4,-11 Q1,-8,4,-5" stroke="#0d0d0d" stroke-width="1" fill="none"/>
    </g>
    <g id="lilypad">
      <path d="M0,-14 C10,-14 16,-4 14,4 C18,8 16,14 6,14 C-4,14 -14,8 -12,2 C-16,-4 -8,-14 0,-14 Z" fill="#3fa34d" stroke="#2d6a3f" stroke-width="0.8"/>
      <path d="M0,0 L-8,-2 L-4,3 Z" fill="#2d6a3f"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <g fill="#fff" opacity="0.7">
    <circle cx="30" cy="40" r="1"/>
    <circle cx="80" cy="20" r="1.5" opacity="0.5"/>
    <circle cx="150" cy="60" r="1"/>
    <circle cx="250" cy="30" r="1.2"/>
    <circle cx="320" cy="50" r="1"/>
    <circle cx="370" cy="20" r="1.5" opacity="0.6"/>
    <circle cx="60" cy="100" r="0.8"/>
    <circle cx="200" cy="90" r="1.1"/>
    <circle cx="280" cy="110" r="0.9"/>
    <circle cx="50" cy="180" r="1"/>
    <circle cx="120" cy="150" r="1.3"/>
    <circle cx="350" cy="140" r="1"/>
    <circle cx="380" cy="200" r="0.8"/>
    <circle cx="20" cy="250" r="1.2"/>
    <circle cx="90" cy="300" r="1"/>
    <circle cx="150" cy="260" r="0.7"/>
    <circle cx="300" cy="250" r="1.1"/>
    <circle cx="370" cy="300" r="0.9"/>
  </g>

  <circle cx="330" cy="80" r="45" fill="url(#moonGlow)" filter="url(#softGlow)"/>
  <circle cx="330" cy="80" r="30" fill="url(#moonFace)"/>
  <circle cx="322" cy="74" r="2.5" fill="#b08a2e" opacity="0.5"/>
  <circle cx="338" cy="74" r="2.5" fill="#b08a2e" opacity="0.5"/>
  <path d="M324,84 Q330,88 336,84" stroke="#b08a2e" stroke-width="1.5" fill="none" opacity="0.5"/>

  <g stroke="#2c4e6e" stroke-width="0.8" fill="none" opacity="0.5">
    <path d="M0,350 Q50,340 100,350 T200,350 T300,350 T400,350"/>
    <path d="M0,365 Q60,355 120,365 T240,365 T360,365 T400,365"/>
    <path d="M0,380 Q80,370 160,380 T320,380 T400,380"/>
    <path d="M0,395 Q40,390 80,395 T160,395 T240,395 T320,395 T400,395"/>
  </g>

  <g opacity="0.75">
    <path d="M10,140 Q50,128 90,140 T170,140 T250,140 T330,140 T390,140" fill="none" stroke="#e0e7ff" stroke-width="1.2"/>
    <path d="M10,150 Q50,138 90,150 T170,150 T250,150 T330,150 T390,150" fill="none" stroke="#e0e7ff" stroke-width="1.2"/>
    <path d="M10,160 Q50,148 90,160 T170,160 T250,160 T330,160 T390,160" fill="none" stroke="#e0e7ff" stroke-width="1.2"/>
    <path d="M10,170 Q50,158 90,170 T170,170 T250,170 T330,170 T390,170" fill="none" stroke="#e0e7ff" stroke-width="1.2"/>
    <path d="M10,180 Q50,168 90,180 T170,180 T250,180 T330,180 T390,180" fill="none" stroke="#e0e7ff" stroke-width="1.2"/>
  </g>

  <use href="#tn1" transform="translate(60,150)"/>
  <use href="#tn2" transform="translate(100,160) rotate(-10)"/>
  <use href="#tn3" transform="translate(150,140) rotate(5)"/>
  <use href="#tn1" transform="translate(200,170) rotate(15)"/>
  <use href="#tn2" transform="translate(250,150) rotate(-5)"/>
  <use href="#tn3" transform="translate(300,180) rotate(10)"/>
  <use href="#tn1" transform="translate(340,160) rotate(-15)"/>
  <use href="#tn2" transform="translate(120,120) rotate(20)"/>
  <use href="#tn3" transform="translate(280,120) rotate(-20)"/>
  <use href="#tn1" transform="translate(370,130) rotate(30)"/>

  <use href="#lilypad" transform="translate(50,340) scale(0.9)"/>
  <use href="#lilypad" transform="translate(120,360) scale(0.8)"/>
  <use href="#lilypad" transform="translate(300,345) scale(1)"/>
  <use href="#lilypad" transform="translate(360,375) scale(0.7)"/>

  <g transform="translate(65,315)">
    <ellipse cx="0" cy="0" rx="16" ry="11" fill="#4f772d" stroke="#2d4a1e" stroke-width="0.8"/>
    <circle cx="18" cy="-10" r="9" fill="#4f772d" stroke="#2d4a1e" stroke-width="0.8"/>
    <circle cx="14" cy="-17" r="4" fill="#4f772d"/>
    <circle cx="22" cy="-17" r="4" fill="#4f772d"/>
    <circle cx="14" cy="-17" r="2" fill="#111"/>
    <circle cx="22" cy="-17" r="2" fill="#111"/>
    <circle cx="15" cy="-18" r="0.8" fill="#fff"/>
    <circle cx="23" cy="-18" r="0.8" fill="#fff"/>
    <path d="M13,-6 Q18,-3 23,-6" stroke="#1a2e0e" stroke-width="0.8" fill="none"/>
    <rect x="-24" y="-7" width="44" height="3.5" rx="1.5" fill="#e6c77b" stroke="#a3853a" stroke-width="0.5"/>
    <circle cx="-16" cy="-5.25" r="0.8" fill="#a3853a"/>
    <circle cx="-8" cy="-5.25" r="0.8" fill="#a3853a"/>
    <circle cx="0" cy="-5.25" r="0.8" fill="#a3853a"/>
    <circle cx="8" cy="-5.25" r="0.8" fill="#a3853a"/>
    <circle cx="16" cy="-5.25" r="0.8" fill="#a3853a"/>
    <path d="M-8,-2 Q-12,-8 -20,-8" stroke="#4f772d" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M10,-2 Q14,-8 20,-8" stroke="#4f772d" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M-10,9 Q-18,14 -24,10" stroke="#4f772d" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M10,9 Q18,14 24,10" stroke="#4f772d" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M-24,10 L-27,8 M-24,10 L-27,11" stroke="#4f772d" stroke-width="1" fill="none"/>
    <path d="M24,10 L27,8 M24,10 L27,11" stroke="#4f772d" stroke-width="1" fill="none"/>
  </g>

  <g transform="translate(190,330)">
    <ellipse cx="0" cy="0" rx="20" ry="13" fill="#4f772d" stroke="#2d4a1e" stroke-width="0.8"/>
    <circle cx="22" cy="-12" r="10" fill="#4f772d" stroke="#2d4a1e" stroke-width="0.8"/>
    <circle cx="18" cy="-20" r="5" fill="#4f772d"/>
    <circle cx="27" cy="-20" r="5" fill="#4f772d"/>
    <circle cx="18" cy="-20" r="2.5" fill="#111"/>
    <circle cx="27" cy="-20" r="2.5" fill="#111"/>
    <circle cx="19" cy="-21" r="1" fill="#fff"/>
    <circle cx="28" cy="-21" r="1" fill="#fff"/>
    <path d="M17,-8 Q22,-4 27,-8" stroke="#1a2e0e" stroke-width="0.8" fill="none"/>
    <g transform="translate(-10,-4) rotate(-20)">
      <rect x="-10" y="-3" width="20" height="6" fill="#8b5a2b" stroke="#5a3a1a" stroke-width="0.6"/>
      <circle cx="-10" cy="0" r="3" fill="#8b5a2b" stroke="#5a3a1a" stroke-width="0.6"/>
      <circle cx="10" cy="0" r="3" fill="#8b5a2b" stroke="#5a3a1a" stroke-width="0.6"/>
      <path d="M-6,-3 L-4,-8 M-2,-3 L0,-8 M2,-3 L4,-8" stroke="#d4af37" stroke-width="0.6"/>
      <path d="M-6,3 L-4,8 M-2,3 L0,8 M2,3 L4,8" stroke="#d4af37" stroke-width="0.6"/>
      <line x1="-8" y1="0" x2="8" y2="0" stroke="#e6c77b" stroke-width="0.4"/>
      <line x1="-8" y1="1" x2="8" y2="1" stroke="#e6c77b" stroke-width="0.4"/>
      <line x1="-8" y1="2" x2="8" y2="2" stroke="#e6c77b" stroke-width="0.4"/>
    </g>
    <line x1="15" y1="-20" x2="-15" y2="10" stroke="#d4af37" stroke-width="1.5"/>
    <path d="M15,-20 Q0,-15,-15,10" stroke="#d4af37" stroke-width="0.8" fill="none"/>
    <path d="M12,-4 Q8,-12 10,-16" stroke="#4f772d" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M-10,-2 Q-16,-8 -14,-12" stroke="#4f772d" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M-12,10 Q-20,16 -26,10" stroke="#4f772d" stroke-width="3" fill="none"/>
    <path d="M12,10 Q20,16 26,10" stroke="#4f772d" stroke-width="3" fill="none"/>
  </g>

  <g transform="translate(320,315)">
    <ellipse cx="0" cy="0" rx="17" ry="11" fill="#4f772d" stroke="#2d4a1e" stroke-width="0.8"/>
    <circle cx="20" cy="-10" r="9" fill="#4f772d" stroke="#2d4a1e" stroke-width="0.8"/>
    <circle cx="16" cy="-17" r="4" fill="#4f772d"/>
    <circle cx="24" cy="-17" r="4" fill="#4f772d"/>
    <circle cx="16" cy="-17" r="2" fill="#111"/>
    <circle cx="24" cy="-17" r="2" fill="#111"/>
    <circle cx="17" cy="-18" r="0.8" fill="#fff"/>
    <circle cx="25" cy="-18" r="0.8" fill="#fff"/>
    <path d="M15,-6 Q20,-3 25,-6" stroke="#1a2e0e" stroke-width="0.8" fill="none"/>
    <ellipse cx="-15" cy="5" rx="14" ry="10" fill="#c96f3b" stroke="#8a4a1e" stroke-width="1"/>
    <ellipse cx="-15" cy="5" rx="14" ry="3" fill="#e6a15a" stroke="#8a4a1e" stroke-width="0.6"/>
    <path d="M-29,5 L-29,15 M-1,5 L-1,15 M-29,15 L-1,15" stroke="#8a4a1e" stroke-width="1" fill="none"/>
    <line x1="-15" y1="5" x2="-25" y2="-8" stroke="#5a3a1a" stroke-width="1.5"/>
    <line x1="-5" y1="2" x2="-8" y2="-6" stroke="#5a3a1a" stroke-width="1.5"/>
    <path d="M-5,-2 Q-10,-8 -18,-8" stroke="#4f772d" stroke-width="3" fill="none"/>
    <path d="M5,-2 Q10,-8 10,-12" stroke="#4f772d" stroke-width="3" fill="none"/>
    <path d="M-10,9 Q-18,14 -24,10" stroke="#4f772d" stroke-width="3" fill="none"/>
    <path d="M10,9 Q18,14 24,10" stroke="#4f772d" stroke-width="3" fill="none"/>
  </g>

  <g transform="translate(35,290)">
    <path d="M0,0 L20,15 L40,5 L60,15 L80,0 Z" fill="#f5f5dc" stroke="#b0a890" stroke-width="1"/>
    <path d="M20,15 L40,5 L40,25 L20,25 Z" fill="#e0dcc0" stroke="#b0a890" stroke-width="0.5"/>
    <circle cx="40" cy="-8" r="7" fill="#808080"/>
    <path d="M35,-13 L33,-22 L39,-16 Z" fill="#808080"/>
    <path d="M45,-13 L47,-22 L41,-16 Z" fill="#808080"/>
    <circle cx="38" cy="-9" r="1.5" fill="#f0f0f0"/>
    <circle cx="42" cy="-9" r="1.5" fill="#f0f0f0"/>
    <circle cx="38" cy="-9" r="0.6" fill="#000"/>
    <circle cx="42" cy="-9" r="0.6" fill="#000"/>
    <path d="M40,-6 L39.5,-5.5 L40.5,-5.5 Z" fill="#ffaaaa"/>
    <line x1="36" y1="-6" x2="32" y2="-5" stroke="#ccc" stroke-width="0.5"/>
    <line x1="36" y1="-5.5" x2="32" y2="-6.5" stroke="#ccc" stroke-width="0.5"/>
    <line x1="44" y1="-6" x2="48" y2="-5" stroke="#ccc" stroke-width="0.5"/>
    <line x1="44" y1="-5.5" x2="48" y2="-6.5" stroke="#ccc" stroke-width="0.5"/>
    <path d="M36,-3 Q34,0 36,2" stroke="#666" stroke-width="1.5" fill="none"/>
    <path d="M44,-3 Q46,0 44,2" stroke="#666" stroke-width="1.5" fill="none"/>
  </g>

  <g filter="url(#glow)">
    <circle cx="180" cy="250" r="1.8" fill="#ffff88"/>
    <circle cx="210" cy="280" r="1.5" fill="#ffff88"/>
    <circle cx="150" cy="220" r="1.5" fill="#ffff88"/>
    <circle cx="260" cy="230" r="1.8" fill="#ffff88"/>
    <circle cx="310" cy="270" r="1.2" fill="#ffff88"/>
    <circle cx="90" cy="270" r="1.3" fill="#ffff88"/>
    <circle cx="370" cy="240" r="1.5" fill="#ffff88"/>
  </g>

  <path d="M310,340 Q330,335 350,340" stroke="#ffd54f" stroke-width="1" fill="none" opacity="0.5"/>
  <path d="M315,355 Q330,350 345,355" stroke="#ffd54f" stroke-width="0.8" fill="none" opacity="0.4"/>
  <path d="M320,370 Q330,366 340,370" stroke="#ffd54f" stroke-width="0.8" fill="none" opacity="0.3"/>
</svg>