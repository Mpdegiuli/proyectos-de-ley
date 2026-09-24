<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg">
      <stop stop-color="#203d62"/>
      <stop offset="1" stop-color="#0b122b"/>
    </radialGradient>
    <linearGradient id="metal" x2="1" y2="1">
      <stop stop-color="#b9f5ee"/>
      <stop offset=".48" stop-color="#69b9d1"/>
      <stop offset="1" stop-color="#5964a9"/>
    </linearGradient>
    <linearGradient id="face" x2="0" y2="1">
      <stop stop-color="#162b53"/>
      <stop offset="1" stop-color="#101934"/>
    </linearGradient>
    <linearGradient id="coat" x2="1" y2="1">
      <stop stop-color="#5779bb"/>
      <stop offset="1" stop-color="#252b63"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="176" r="145" fill="none" stroke="#81e6df" stroke-opacity=".13" stroke-width="2"/>
  <circle cx="200" cy="176" r="123" fill="none" stroke="#81e6df" stroke-opacity=".16" stroke-dasharray="3 9"/>
  <circle cx="200" cy="176" r="105" fill="#58d6d1" opacity=".08" filter="url(#glow)"/>

  <g fill="#bafbf0">
    <circle cx="44" cy="85" r="2"/><circle cx="348" cy="137" r="1.5"/>
    <circle cx="62" cy="231" r="1.5"/><circle cx="331" cy="261" r="2"/>
    <circle cx="90" cy="45" r="1"/><circle cx="290" cy="39" r="1.5"/>
  </g>
  <g stroke="#83e8df" stroke-opacity=".55" stroke-linecap="round">
    <path d="M51 117v12m-6-6h12M342 206v12m-6-6h12M315 60v8m-4-4h8"/>
  </g>

  <!-- Shoulders and collar -->
  <path d="M48 400c3-55 24-91 71-108l41-17h80l41 17c47 17 68 53 71 108Z" fill="url(#coat)" stroke="#91dce3" stroke-width="3"/>
  <path d="M112 296l49-21 39 53 39-53 49 21-35 104H147Z" fill="#202b58" opacity=".65"/>
  <path d="M155 275h90l-8 28-37 27-37-27Z" fill="#86bbd0"/>
  <path d="M177 280v-24h46v24l-23 24Z" fill="#3c7197"/>
  <path d="M131 302l35 29-19 69M269 302l-35 29 19 69" fill="none" stroke="#9dece5" stroke-opacity=".35" stroke-width="3"/>

  <!-- Antenna and ears -->
  <path d="M200 104V68" stroke="#8edfe1" stroke-width="7" stroke-linecap="round"/>
  <circle cx="200" cy="62" r="11" fill="#90f4e6" opacity=".45" filter="url(#glow)"/>
  <circle cx="200" cy="62" r="7" fill="#a8fff0"/>
  <rect x="80" y="151" width="29" height="56" rx="12" fill="#558aaa" stroke="#9ce9e3" stroke-width="3"/>
  <rect x="291" y="151" width="29" height="56" rx="12" fill="#558aaa" stroke="#9ce9e3" stroke-width="3"/>
  <path d="M89 169v21m222-21v21" stroke="#b5fff0" stroke-width="3" stroke-linecap="round"/>

  <!-- Head -->
  <rect x="99" y="91" width="202" height="181" rx="57" fill="url(#metal)" stroke="#c2fff0" stroke-width="3"/>
  <rect x="110" y="103" width="180" height="153" rx="45" fill="url(#face)" stroke="#78d9db" stroke-width="2"/>
  <path d="M133 120c31-21 103-21 134 0" fill="none" stroke="#b5fff0" stroke-opacity=".22" stroke-width="5" stroke-linecap="round"/>

  <!-- Glowing expression -->
  <g fill="#74fbe0" opacity=".55" filter="url(#glow)">
    <ellipse cx="158" cy="174" rx="15" ry="22"/>
    <ellipse cx="242" cy="174" rx="15" ry="22"/>
  </g>
  <ellipse cx="158" cy="174" rx="10" ry="17" fill="#a8ffed"/>
  <ellipse cx="242" cy="174" rx="10" ry="17" fill="#a8ffed"/>
  <circle cx="162" cy="168" r="3" fill="#fff"/>
  <circle cx="246" cy="168" r="3" fill="#fff"/>
  <path d="M167 215q33 28 66 0" fill="none" stroke="#91ffdf" stroke-width="5" stroke-linecap="round"/>
  <path d="M125 211h13m124 0h13" stroke="#f39fc7" stroke-width="5" stroke-linecap="round" opacity=".75"/>
  <circle cx="127" cy="135" r="2" fill="#83e9e0"/>
  <circle cx="273" cy="135" r="2" fill="#83e9e0"/>

  <!-- A little conversation at the heart -->
  <rect x="169" y="344" width="62" height="39" rx="14" fill="#93f5e4" opacity=".15" filter="url(#glow)"/>
  <path d="M181 345h38a12 12 0 0 1 12 12v12a12 12 0 0 1-12 12h-18l-11 9v-9h-9a12 12 0 0 1-12-12v-12a12 12 0 0 1 12-12Z" fill="#122e50" stroke="#9bf8e7" stroke-width="2"/>
  <g fill="#a9ffed"><circle cx="187" cy="363" r="3"/><circle cx="200" cy="363" r="3"/><circle cx="213" cy="363" r="3"/></g>
</svg>