<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b0b2a"/>
      <stop offset="30%" stop-color="#2c1e4a"/>
      <stop offset="55%" stop-color="#7b3b5e"/>
      <stop offset="80%" stop-color="#d06c4a"/>
      <stop offset="100%" stop-color="#f4b26a"/>
    </linearGradient>
    <radialGradient id="sunGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff8d6"/>
      <stop offset="25%" stop-color="#ffd166"/>
      <stop offset="60%" stop-color="#ff9f4a"/>
      <stop offset="100%" stop-color="#ff6f3c" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="haloGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd166" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ffd166" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="lakeGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2c1e4a"/>
      <stop offset="30%" stop-color="#1b1236"/>
      <stop offset="100%" stop-color="#0b0b2a"/>
    </linearGradient>
    <linearGradient id="reflGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffd166" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ffd166" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#ffd166" stop-opacity="0"/>
    </linearGradient>
  </defs>
  
  <rect width="400" height="400" fill="url(#skyGrad)"/>
  
  <g fill="white">
    <circle cx="30" cy="40" r="1.5" opacity="0.8"/>
    <circle cx="80" cy="25" r="1" opacity="0.6"/>
    <circle cx="150" cy="55" r="1.2" opacity="0.7"/>
    <circle cx="250" cy="30" r="1" opacity="0.5"/>
    <circle cx="320" cy="60" r="1.5" opacity="0.8"/>
    <circle cx="370" cy="35" r="1" opacity="0.6"/>
    <circle cx="50" cy="90" r="1" opacity="0.4"/>
    <circle cx="200" cy="70" r="1.2" opacity="0.5"/>
    <circle cx="290" cy="95" r="1" opacity="0.4"/>
    <circle cx="360" cy="80" r="1.3" opacity="0.7"/>
    <circle cx="120" cy="110" r="0.8" opacity="0.5"/>
    <circle cx="380" cy="120" r="1" opacity="0.6"/>
  </g>
  
  <path d="M40,160 q10,-10 20,0 q10,-15 20,0 q10,-10 20,0" stroke="#d06c4a" fill="none" stroke-width="2" opacity="0.3"/>
  <path d="M300,140 q8,-8 16,0 q8,-12 16,0 q8,-8 16,0" stroke="#d06c4a" fill="none" stroke-width="1.5" opacity="0.25"/>
  
  <circle cx="200" cy="200" r="100" fill="url(#haloGrad)"/>
  <circle cx="200" cy="200" r="55" fill="url(#sunGrad)"/>
  
  <path d="M0,280 L80,180 L140,240 L220,160 L300,230 L360,190 L400,260 L400,300 L0,300 Z" fill="#5b3a6b" opacity="0.85"/>
  <path d="M0,290 L60,210 L120,250 L200,190 L280,250 L340,210 L400,270 L400,320 L0,320 Z" fill="#432758" opacity="0.9"/>
  <path d="M0,310 L70,240 L140,280 L210,220 L280,270 L350,240 L400,290 L400,340 L0,340 Z" fill="#2e1c42"/>
  
  <rect x="0" y="290" width="400" height="110" fill="url(#lakeGrad)"/>
  
  <path d="M0,290 Q50,288 100,292 Q150,295 200,291 Q250,287 300,293 Q350,296 400,290 L400,300 Q350,296 300,299 Q250,302 200,297 Q150,293 100,298 Q50,301 0,300 Z" fill="#1b1236"/>
  
  <g fill="none" stroke-linecap="round">
    <path d="M140,320 Q160,315 180,320 Q200,325 220,320 Q240,315 260,320 Q280,325 300,320" stroke="url(#reflGrad)" stroke-width="4" opacity="0.8"/>
    <path d="M130,335 Q150,330 170,335 Q190,340 210,335 Q230,330 250,335 Q270,340 290,335" stroke="url(#reflGrad)" stroke-width="3" opacity="0.5"/>
    <path d="M120,350 Q140,345 160,350 Q180,355 200,350 Q220,345 240,350 Q260,355 280,350" stroke="url(#reflGrad)" stroke-width="2" opacity="0.3"/>
    <path d="M110,365 Q130,360 150,365 Q170,370 190,365 Q210,360 230,365 Q250,370 270,365" stroke="url(#reflGrad)" stroke-width="1.5" opacity="0.2"/>
  </g>
  
  <g stroke="#1a1a3a" fill="none" stroke-linecap="round">
    <path d="M60,130 q5,-5 10,0 q5,-5 10,0" stroke-width="1.5"/>
    <path d="M90,115 q4,-4 8,0 q4,-4 8,0" stroke-width="1.2"/>
    <path d="M75,100 q3,-3 6,0 q3,-3 6,0" stroke-width="1"/>
    <path d="M110,125 q3,-3 6,0 q3,-3 6,0" stroke-width="1"/>
  </g>
  
  <g fill="#0f0a1e">
    <rect x="28" y="275" width="4" height="15"/>
    <path d="M18,280 L30,260 L42,280 Z"/>
    <path d="M20,272 L30,254 L40,272 Z"/>
    <rect x="368" y="272" width="4" height="15"/>
    <path d="M358,277 L370,257 L382,277 Z"/>
    <path d="M360,270 L370,252 L380,270 Z"/>
  </g>
</svg>