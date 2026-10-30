<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x2="1" y2="1">
      <stop stop-color="#101e38"/>
      <stop offset="1" stop-color="#273355"/>
    </linearGradient>
    <linearGradient id="shell" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#ecfaf6"/>
      <stop offset=".5" stop-color="#badbd8"/>
      <stop offset="1" stop-color="#78aaa9"/>
    </linearGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#233b53"/>
      <stop offset="1" stop-color="#101d32"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#d2ebe4"/>
      <stop offset="1" stop-color="#729c9e"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop stop-color="#71e4cb" stop-opacity=".3"/>
      <stop offset="1" stop-color="#71e4cb" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="8"/></filter>
    <clipPath id="frame"><rect x="12" y="12" width="376" height="376" rx="38"/></clipPath>
  </defs>

  <rect width="400" height="400" fill="#0c1729"/>
  <g clip-path="url(#frame)">
    <rect x="12" y="12" width="376" height="376" fill="url(#bg)"/>
    <circle cx="200" cy="170" r="164" fill="url(#glow)"/>
    <g fill="none" stroke="#a9e9da" stroke-opacity=".16" stroke-width="1">
      <circle cx="200" cy="177" r="143"/>
      <circle cx="200" cy="177" r="159"/>
      <path d="M23 111h47l20 20h22M377 111h-47l-20 20h-22M22 254h45l23-23h20M378 254h-45l-23-23h-20"/>
    </g>
    <g fill="#8ae4cf" opacity=".55">
      <circle cx="70" cy="111" r="3"/><circle cx="330" cy="111" r="3"/>
      <circle cx="67" cy="254" r="3"/><circle cx="333" cy="254" r="3"/>
      <circle cx="65" cy="164" r="2"/><circle cx="335" cy="164" r="2"/>
      <circle cx="92" cy="72" r="2"/><circle cx="310" cy="73" r="2"/>
    </g>

    <ellipse cx="200" cy="385" rx="145" ry="24" fill="#091528" opacity=".5"/>
    <path d="M73 400v-28c0-43 34-70 88-78h78c54 8 88 35 88 78v28z" fill="url(#body)" stroke="#e4faf2" stroke-opacity=".55" stroke-width="2"/>
    <path d="M160 292v-30h80v30c-5 21-19 32-40 32s-35-11-40-32z" fill="#679697"/>
    <path d="M160 290c8 13 22 19 40 19s32-6 40-19" fill="none" stroke="#d2f1e7" stroke-width="2" opacity=".6"/>
    <path d="M103 400v-24c0-27 10-47 30-61M297 400v-24c0-27-10-47-30-61" fill="none" stroke="#557d84" stroke-width="2" opacity=".55"/>
    <path d="M170 337l30 19 30-19" fill="none" stroke="#5e8e8e" stroke-width="2"/>
    <circle cx="200" cy="365" r="9" fill="#284b58"/>
    <circle cx="200" cy="365" r="4" fill="#a4f4d8"/>

    <path d="M105 158h-8c-12 0-19 9-19 22v28c0 13 7 22 19 22h8M295 158h8c12 0 19 9 19 22v28c0 13-7 22-19 22h-8" fill="#6a9a9b" stroke="#c8eae0" stroke-width="2"/>
    <path d="M89 178v31M311 178v31" stroke="#baf4e1" stroke-width="4" stroke-linecap="round"/>

    <path d="M200 74c-59 0-97 32-97 83v55c0 49 38 79 97 79s97-30 97-79v-55c0-51-38-83-97-83z" fill="url(#shell)" stroke="#e6fff5" stroke-width="2"/>
    <path d="M200 84c-48 0-80 22-87 58" fill="none" stroke="#fff" stroke-opacity=".52" stroke-width="3" stroke-linecap="round"/>
    <path d="M124 158c0-23 18-39 42-42 11-2 23-2 34-2s23 0 34 2c24 3 42 19 42 42v48c0 31-28 52-76 52s-76-21-76-52z" fill="url(#face)" stroke="#678f93" stroke-width="2"/>
    <path d="M139 145c12-14 31-19 61-19s49 5 61 19" fill="none" stroke="#9fe8d5" stroke-opacity=".12" stroke-width="2"/>
    <ellipse cx="163" cy="181" rx="23" ry="20" fill="#75ecd0" opacity=".2" filter="url(#blur)"/>
    <ellipse cx="237" cy="181" rx="23" ry="20" fill="#75ecd0" opacity=".2" filter="url(#blur)"/>
    <path d="M145 182c4-8 10-12 18-12s14 4 18 12" fill="none" stroke="#a9f8df" stroke-width="5" stroke-linecap="round"/>
    <path d="M219 182c4-8 10-12 18-12s14 4 18 12" fill="none" stroke="#a9f8df" stroke-width="5" stroke-linecap="round"/>
    <path d="M184 216c9 7 23 7 32 0" fill="none" stroke="#9be9d5" stroke-width="3" stroke-linecap="round"/>
    <circle cx="145" cy="206" r="3" fill="#e99f9b" opacity=".7"/>
    <circle cx="255" cy="206" r="3" fill="#e99f9b" opacity=".7"/>
    <path d="M184 96h32" stroke="#6caaa5" stroke-width="3" stroke-linecap="round"/>
    <circle cx="200" cy="96" r="5" fill="#d3fff0" stroke="#6caaa5" stroke-width="2"/>

    <g fill="#c8ffea">
      <path d="M64 55l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>
      <path d="M337 285l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/>
      <circle cx="333" cy="53" r="2"/>
      <circle cx="54" cy="299" r="2"/>
    </g>
  </g>
  <rect x="12" y="12" width="376" height="376" rx="38" fill="none" stroke="#b9e9dd" stroke-opacity=".28" stroke-width="2"/>
</svg>