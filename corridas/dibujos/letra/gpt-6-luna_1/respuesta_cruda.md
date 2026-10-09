<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="43%" r="72%">
      <stop stop-color="#253044"/>
      <stop offset="1" stop-color="#0c111d"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#ffe4a8"/>
      <stop offset=".48" stop-color="#f5a36c"/>
      <stop offset="1" stop-color="#e65c55"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#fff0c7" stop-opacity=".45"/>
      <stop offset="1" stop-color="#fff0c7" stop-opacity="0"/>
    </linearGradient>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r=".8" fill="#d2c6ad" opacity=".17"/>
    </pattern>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="10"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#dots)" opacity=".45"/>
  <circle cx="200" cy="194" r="151" fill="none" stroke="#f1c58a" stroke-opacity=".12"/>
  <circle cx="200" cy="194" r="137" fill="none" stroke="#f1c58a" stroke-opacity=".08" stroke-dasharray="2 7"/>
  <path d="M46 320V80h2v240M352 80v240h2V80" fill="#d9b786" opacity=".22"/>
  <path d="M46 80h22M332 80h22M46 320h22M332 320h22" stroke="#d9b786" stroke-opacity=".45" stroke-width="1"/>

  <path d="M58 326h86l22-63h68l22 63h86L225 59c-6-14-14-21-25-21s-19 7-25 21L58 326Z"
        fill="#f08b61" opacity=".34" filter="url(#glow)"/>
  <path fill="url(#gold)" fill-rule="evenodd" stroke="#ffe0a5" stroke-opacity=".7" stroke-width="1.5" stroke-linejoin="round"
        d="M58 326h86l22-63h68l22 63h86L225 59c-6-14-14-21-25-21s-19 7-25 21L58 326Z
           M170 240l30-93 30 93Z"/>
  <path d="M170 240l30-93 30 93Z" fill="#192235"/>
  <path d="M155 219h90l8 24h-106Z" fill="url(#gold)" stroke="#ffe0a5" stroke-opacity=".48" stroke-width="1"/>
  <path d="M200 49c8 0 13 5 18 16l104 241h-9L214 68c-4-9-8-13-14-13Z" fill="url(#shine)" opacity=".65"/>

  <circle cx="200" cy="24" r="3" fill="#f6c983"/>
  <path d="M200 12v7m0 10v7m-12-12h7m10 0h7" stroke="#f6c983" stroke-opacity=".65"/>
  <circle cx="71" cy="200" r="2" fill="#e7b979"/>
  <circle cx="329" cy="200" r="2" fill="#e7b979"/>
  <path d="M70 190v20m-6-10h12M330 190v20m-6-10h12" stroke="#e7b979" stroke-opacity=".45"/>
</svg>