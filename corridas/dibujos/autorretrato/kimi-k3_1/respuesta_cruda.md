<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#3a2b20"/>
      <stop offset="55%" stop-color="#221b15"/>
      <stop offset="100%" stop-color="#131010"/>
    </radialGradient>
    <radialGradient id="glow">
      <stop offset="0%" stop-color="#D97757" stop-opacity=".4"/>
      <stop offset="100%" stop-color="#D97757" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="pt" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F4A876"/>
      <stop offset="100%" stop-color="#C24E28"/>
    </linearGradient>
    <radialGradient id="core" cx="50%" cy="38%" r="70%">
      <stop offset="0%" stop-color="#EF9263"/>
      <stop offset="100%" stop-color="#C7502B"/>
    </radialGradient>
    <path id="p" d="M0,-128 C17,-103 17,-61 0,-40 C-17,-61 -17,-103 0,-128 Z"/>
    <path id="s" d="M0,-9 C1.5,-2.5 2.5,-1.5 9,0 C2.5,1.5 1.5,2.5 0,9 C-1.5,2.5 -2.5,1.5 -9,0 C-2.5,-1.5 -1.5,-2.5 0,-9 Z"/>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <circle cx="200" cy="200" r="168" fill="url(#glow)"/>
  <circle cx="200" cy="200" r="150" fill="none" stroke="#7d6752" stroke-width="1" stroke-dasharray="1 7" opacity=".55"/>

  <g fill="#F5EBDD">
    <circle cx="110" cy="58" r="1.6" opacity=".5"/>
    <circle cx="305" cy="88" r="1.3" opacity=".45"/>
    <circle cx="52" cy="212" r="1.5" opacity=".5"/>
    <circle cx="348" cy="205" r="1.5" opacity=".5"/>
    <circle cx="150" cy="330" r="1.3" opacity=".4"/>
    <circle cx="268" cy="338" r="1.4" opacity=".4"/>
    <use href="#s" transform="translate(74 94) scale(1)">
      <animate attributeName="opacity" values="1;.2;1" dur="3.2s" repeatCount="indefinite"/>
    </use>
    <use href="#s" transform="translate(326 78) scale(.7)">
      <animate attributeName="opacity" values=".3;1;.3" dur="2.6s" repeatCount="indefinite"/>
    </use>
    <use href="#s" transform="translate(58 300) scale(.8)">
      <animate attributeName="opacity" values="1;.25;1" dur="3.8s" repeatCount="indefinite"/>
    </use>
    <use href="#s" transform="translate(338 310) scale(1.1)">
      <animate attributeName="opacity" values=".35;1;.35" dur="3s" repeatCount="indefinite"/>
    </use>
    <use href="#s" transform="translate(200 38) scale(.55)">
      <animate attributeName="opacity" values=".9;.3;.9" dur="2.2s" repeatCount="indefinite"/>
    </use>
  </g>

  <g>
    <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="45s" repeatCount="indefinite"/>
    <circle cx="200" cy="50" r="4.5" fill="#D97757"/>
    <circle cx="330" cy="275" r="3" fill="#F4A876"/>
    <circle cx="70" cy="275" r="2.5" fill="#F5EBDD"/>
  </g>

  <ellipse cx="200" cy="352" rx="72" ry="10" fill="#000" opacity=".3"/>

  <g transform="translate(200 200)">
    <g>
      <animateTransform attributeName="transform" type="scale" values="1;1.025;1" dur="4.5s" repeatCount="indefinite"/>
      <g fill="url(#pt)">
        <use href="#p"/>
        <use href="#p" transform="rotate(30)"/>
        <use href="#p" transform="rotate(60)"/>
        <use href="#p" transform="rotate(90)"/>
        <use href="#p" transform="rotate(120)"/>
        <use href="#p" transform="rotate(150)"/>
      </g>
      <circle r="54" fill="url(#core)"/>
      <ellipse cx="-19" cy="-8" rx="11" ry="14" fill="#FFFBF4"/>
      <ellipse cx="19" cy="-8" rx="11" ry="14" fill="#FFFBF4"/>
      <circle cx="-16.5" cy="-6" r="5.5" fill="#2B1B12"/>
      <circle cx="21.5" cy="-6" r="5.5" fill="#2B1B12"/>
      <circle cx="-14.8" cy="-8.2" r="1.8" fill="#fff"/>
      <circle cx="23.2" cy="-8.2" r="1.8" fill="#fff"/>
      <path d="M-13,17 Q0,27 13,17" stroke="#2B1B12" stroke-width="3.5" fill="none" stroke-linecap="round"/>
      <ellipse cx="-33" cy="10" rx="7" ry="4" fill="#F4A876" opacity=".7"/>
      <ellipse cx="33" cy="10" rx="7" ry="4" fill="#F4A876" opacity=".7"/>
    </g>
  </g>

  <text x="200" y="383" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="13" letter-spacing="8" fill="#8f775c">CLAUDE</text>
</svg>