<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#07152f"/>
      <stop offset=".55" stop-color="#233765"/>
      <stop offset="1" stop-color="#e27d75"/>
    </linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#294b68"/>
      <stop offset="1" stop-color="#071b2c"/>
    </linearGradient>
    <radialGradient id="moon">
      <stop offset=".7" stop-color="#fffbd5"/>
      <stop offset="1" stop-color="#ffd99a"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="7"/>
    </filter>
    <clipPath id="frame">
      <rect width="400" height="400" rx="24"/>
    </clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="400" height="400" fill="url(#sky)"/>
    <circle cx="298" cy="82" r="43" fill="#ffe6aa" opacity=".22" filter="url(#glow)"/>
    <circle cx="298" cy="82" r="30" fill="url(#moon)"/>
    <circle cx="288" cy="73" r="5" fill="#e8ce99" opacity=".45"/>
    <circle cx="307" cy="94" r="7" fill="#e8ce99" opacity=".35"/>
    <circle cx="313" cy="68" r="3" fill="#e8ce99" opacity=".4"/>

    <g fill="#fff8d6">
      <circle cx="47" cy="52" r="1.7"/>
      <circle cx="84" cy="89" r="1.1"/>
      <circle cx="124" cy="38" r="1.5"/>
      <circle cx="168" cy="72" r="1"/>
      <circle cx="211" cy="34" r="1.8"/>
      <circle cx="249" cy="109" r="1.2"/>
      <circle cx="355" cy="42" r="1.4"/>
      <circle cx="373" cy="124" r="1"/>
      <path d="M70 125h10M75 120v10" stroke="#fff8d6" stroke-width="1.2"/>
      <path d="M187 112h8M191 108v8" stroke="#fff8d6"/>
    </g>

    <path d="M0 231 43 192 74 215 121 158 170 217 218 171 276 222 319 177 400 235V278H0Z" fill="#192b49"/>
    <path d="m92 190 29-32 18 28-17-8-10 13-8-9zM196 190l22-19 25 26-24-10-10 11zM297 198l22-21 28 27-28-11-13 12z" fill="#bbc1ce" opacity=".8"/>
    <path d="M0 251c52-16 91-11 139 2 53 14 93 6 131-7 52-18 88-13 130 0v48H0Z" fill="#101f31"/>
    <path d="M0 268c69-20 111 6 173 2 70-4 132-31 227-3v133H0Z" fill="url(#water)"/>

    <path d="M271 267c18 8 37 9 55 1M255 282c27 10 62 10 91-1M271 299c19 5 39 5 59-1M281 317c14 3 31 3 45-1" fill="none" stroke="#ffd898" stroke-linecap="round" opacity=".45"/>
    <g fill="none" stroke="#7ba0ad" stroke-linecap="round" opacity=".5">
      <path d="M20 290h75M42 307h91M8 337h112M148 294h55M168 321h70M107 362h98M261 345h112M238 374h94"/>
    </g>

    <g fill="#071521">
      <path d="M48 330h21l-8-13h6l-11-18h6l-14-27-14 27h6l-11 18h7l-9 13h21v40h10z"/>
      <path d="M102 347h25l-9-15h7l-13-20h7l-17-32-17 32h7l-13 20h8l-10 15h25v38h10z"/>
      <path d="M344 335h25l-10-15h8l-13-21h7l-17-34-18 34h8l-14 21h8l-9 15h25v43h10z"/>
      <path d="M297 358h19l-7-12h6l-11-17h6l-13-25-13 25h6l-11 17h6l-7 12h19v30h9z"/>
    </g>

    <path d="M0 378c54-16 105-4 155 5 72 13 149-17 245-2v19H0Z" fill="#050e17"/>
    <path d="M184 266c8-8 16-8 24 0 8-8 16-8 24 0" fill="none" stroke="#08131e" stroke-width="3" stroke-linecap="round"/>
    <path d="M79 236c5-5 10-5 15 0 5-5 10-5 15 0" fill="none" stroke="#101b2a" stroke-width="2.5" stroke-linecap="round"/>
  </g>
</svg>