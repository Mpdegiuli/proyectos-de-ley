<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="body" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#ffd86b"/>
      <stop offset="60%" stop-color="#ff9a3c"/>
      <stop offset="100%" stop-color="#e14e6d"/>
    </radialGradient>
    <linearGradient id="wing" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#7be0ff"/>
      <stop offset="100%" stop-color="#5a6bff"/>
    </linearGradient>
    <radialGradient id="eye" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fff"/>
      <stop offset="70%" stop-color="#9ef"/>
      <stop offset="100%" stop-color="#36a"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="#10243b"/>
  <circle cx="320" cy="70" r="40" fill="#1c3a5e" opacity="0.6"/>
  <circle cx="70" cy="330" r="55" fill="#1c3a5e" opacity="0.5"/>

  <!-- tail -->
  <path d="M120 250 Q40 280 60 340 Q90 300 130 300 Z" fill="url(#wing)" opacity="0.9"/>
  <path d="M130 260 Q60 300 90 350 Q110 310 145 305 Z" fill="#ff7bbd" opacity="0.8"/>

  <!-- wings -->
  <path d="M200 180 Q90 120 70 210 Q140 200 190 240 Z" fill="url(#wing)" stroke="#2a3a8f" stroke-width="3"/>
  <path d="M200 180 Q310 120 330 210 Q260 200 210 240 Z" fill="url(#wing)" stroke="#2a3a8f" stroke-width="3"/>
  <path d="M190 200 Q120 170 110 215" fill="none" stroke="#2a3a8f" stroke-width="2"/>
  <path d="M210 200 Q280 170 290 215" fill="none" stroke="#2a3a8f" stroke-width="2"/>

  <!-- body -->
  <ellipse cx="200" cy="250" rx="70" ry="90" fill="url(#body)"/>
  <ellipse cx="200" cy="250" rx="70" ry="90" fill="none" stroke="#c23e5a" stroke-width="2"/>

  <!-- spots -->
  <circle cx="180" cy="260" r="10" fill="#fff6c9" opacity="0.7"/>
  <circle cx="220" cy="290" r="8" fill="#fff6c9" opacity="0.7"/>
  <circle cx="205" cy="230" r="6" fill="#fff6c9" opacity="0.7"/>

  <!-- head -->
  <circle cx="200" cy="150" r="55" fill="url(#body)" stroke="#c23e5a" stroke-width="2"/>

  <!-- horns/antennae -->
  <path d="M165 110 Q150 60 180 70" fill="none" stroke="#5a6bff" stroke-width="6" stroke-linecap="round"/>
  <path d="M235 110 Q250 60 220 70" fill="none" stroke="#5a6bff" stroke-width="6" stroke-linecap="round"/>
  <circle cx="177" cy="68" r="7" fill="#7be0ff"/>
  <circle cx="223" cy="68" r="7" fill="#7be0ff"/>

  <!-- eyes -->
  <circle cx="178" cy="145" r="18" fill="url(#eye)"/>
  <circle cx="222" cy="145" r="18" fill="url(#eye)"/>
  <circle cx="182" cy="148" r="8" fill="#10243b"/>
  <circle cx="226" cy="148" r="8" fill="#10243b"/>
  <circle cx="185" cy="144" r="3" fill="#fff"/>
  <circle cx="229" cy="144" r="3" fill="#fff"/>

  <!-- snout -->
  <ellipse cx="200" cy="178" rx="22" ry="16" fill="#ffe6a0"/>
  <ellipse cx="192" cy="176" rx="4" ry="5" fill="#8a4a2a"/>
  <ellipse cx="208" cy="176" rx="4" ry="5" fill="#8a4a2a"/>
  <path d="M185 188 Q200 198 215 188" fill="none" stroke="#8a4a2a" stroke-width="3" stroke-linecap="round"/>

  <!-- legs -->
  <path d="M170 335 Q165 370 180 375" fill="none" stroke="#e14e6d" stroke-width="12" stroke-linecap="round"/>
  <path d="M230 335 Q235 370 220 375" fill="none" stroke="#e14e6d" stroke-width="12" stroke-linecap="round"/>
  <ellipse cx="182" cy="378" rx="14" ry="7" fill="#5a6bff"/>
  <ellipse cx="218" cy="378" rx="14" ry="7" fill="#5a6bff"/>
</svg>