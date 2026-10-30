<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x2="0" y2="1">
      <stop stop-color="#15143d"/>
      <stop offset="1" stop-color="#47275f"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#a8f6da"/>
      <stop offset=".55" stop-color="#55c8c5"/>
      <stop offset="1" stop-color="#4386b5"/>
    </linearGradient>
    <linearGradient id="wing" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#ffd0e8" stop-opacity=".9"/>
      <stop offset="1" stop-color="#a88bea" stop-opacity=".55"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop stop-color="#ffdfac" stop-opacity=".6"/>
      <stop offset="1" stop-color="#ffdfac" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="319" cy="78" r="65" fill="url(#glow)"/>
  <circle cx="319" cy="78" r="24" fill="#ffdfa9"/>
  <circle cx="328" cy="70" r="22" fill="#29204c"/>
  <g fill="#fff0cf">
    <circle cx="51" cy="65" r="2"/><circle cx="103" cy="100" r="1.5"/>
    <circle cx="169" cy="45" r="2"/><circle cx="245" cy="74" r="1.5"/>
    <circle cx="359" cy="151" r="2"/><circle cx="35" cy="236" r="1.5"/>
    <circle cx="69" cy="325" r="2"/><circle cx="332" cy="302" r="1.5"/>
    <path d="M78 142l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>
    <path d="M350 223l1.5 5 5 1.5-5 1.5-1.5 5-1.5-5-5-1.5 5-1.5z"/>
    <path d="M220 28l1 4 4 1-4 1-1 4-1-4-4-1 4-1z"/>
  </g>

  <ellipse cx="202" cy="354" rx="115" ry="13" fill="#171536" opacity=".35"/>
  <g stroke="#252447" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <!-- wings -->
    <path d="M183 195C143 177 119 137 136 104c14-27 44-9 57 25 2-48 39-64 54-40 17 27-5 77-31 108z" fill="url(#wing)"/>
    <path d="M186 188c-17-27-29-52-37-69m46 69c8-35 21-65 38-87" fill="none" stroke="#f9e0f4" stroke-width="2" opacity=".7"/>
    <path d="M151 133l19 9m-12 7 21 8m53-37-19 13m13 4-19 13" fill="none" stroke="#f9e0f4" stroke-width="2" opacity=".7"/>

    <!-- curling tail -->
    <path d="M126 220c-46 5-65-11-59-38 3-14 16-21 27-15 9 5 8 17-1 19-5 1-8-2-9-5" fill="none" stroke="#252447" stroke-width="17"/>
    <path d="M126 220c-46 5-65-11-59-38 3-14 16-21 27-15 9 5 8 17-1 19-5 1-8-2-9-5" fill="none" stroke="#6ddbd0" stroke-width="10"/>

    <!-- tendrils -->
    <path d="M135 254c-5 29 13 32 5 54-3 9-11 12-17 8" fill="none" stroke="#252447" stroke-width="13"/>
    <path d="M135 254c-5 29 13 32 5 54-3 9-11 12-17 8" fill="none" stroke="#73dcd1" stroke-width="7"/>
    <path d="M168 264c-9 25 8 40 1 61-3 9-9 12-15 9" fill="none" stroke="#252447" stroke-width="13"/>
    <path d="M168 264c-9 25 8 40 1 61-3 9-9 12-15 9" fill="none" stroke="#73dcd1" stroke-width="7"/>
    <path d="M212 265c11 25-3 39 8 60 4 7 11 9 16 5" fill="none" stroke="#252447" stroke-width="13"/>
    <path d="M212 265c11 25-3 39 8 60 4 7 11 9 16 5" fill="none" stroke="#73dcd1" stroke-width="7"/>
    <path d="M245 251c13 22 5 37 18 51 6 6 13 5 17 0" fill="none" stroke="#252447" stroke-width="13"/>
    <path d="M245 251c13 22 5 37 18 51 6 6 13 5 17 0" fill="none" stroke="#73dcd1" stroke-width="7"/>

    <!-- body and head -->
    <path d="M104 220c0-41 38-62 85-59 27 2 48 12 61 30 23 30 11 67-23 78-25 8-74 7-98-4-17-8-25-24-25-45z" fill="url(#body)"/>
    <path d="M132 239c17 16 48 22 75 18" fill="none" stroke="#d7fff0" stroke-width="3" opacity=".55"/>
    <path d="M220 182c-2-18 2-37 9-52 11 3 21 13 27 22 9-4 20-5 30-3 9-10 19-16 29-17 5 17 5 35 1 49 9 11 12 25 8 38-6 22-29 35-57 33-30-2-50-16-52-36-1-12 1-23 5-34z" fill="url(#body)"/>
    <path d="M230 145c5 2 11 8 14 13l-15 6zM306 145c-6 3-11 8-14 13l17 5z" fill="#efadd1" stroke="none"/>

    <!-- antlers -->
    <path d="M254 151c-5-14-4-27 2-37m-4 18c-9-3-13-9-14-16m19 10c7-3 11-8 13-15" fill="none" stroke="#f6c995" stroke-width="4"/>
    <circle cx="237" cy="113" r="4" fill="#ffd999" stroke="none"/>
    <circle cx="271" cy="108" r="4" fill="#ffd999" stroke="none"/>

    <!-- face -->
    <ellipse cx="248" cy="192" rx="5" ry="7" fill="#252447" stroke="none"/>
    <ellipse cx="296" cy="192" rx="5" ry="7" fill="#252447" stroke="none"/>
    <circle cx="249" cy="190" r="1.5" fill="#fff" stroke="none"/>
    <circle cx="297" cy="190" r="1.5" fill="#fff" stroke="none"/>
    <ellipse cx="272" cy="176" rx="4" ry="5.5" fill="#252447" stroke="none"/>
    <circle cx="273" cy="174" r="1.3" fill="#fff" stroke="none"/>
    <path d="M267 207l5 4 5-4z" fill="#db83a7" stroke="none"/>
    <path d="M272 211v5m0 0c-3 4-8 4-10 1m10-1c3 4 8 4 10 1" fill="none" stroke-width="2"/>
    <ellipse cx="240" cy="207" rx="9" ry="4" fill="#f29dbb" stroke="none" opacity=".6"/>
    <ellipse cx="304" cy="207" rx="9" ry="4" fill="#f29dbb" stroke="none" opacity=".6"/>
  </g>

  <!-- orbiting little planet -->
  <g transform="translate(112 119) rotate(-22)">
    <ellipse rx="22" ry="6" fill="none" stroke="#ffe1a8" stroke-width="2"/>
    <circle r="10" fill="#f4aebd" stroke="#252447" stroke-width="2"/>
    <path d="M-21 2c8 5 31 5 42 0" fill="none" stroke="#ffe1a8" stroke-width="2"/>
  </g>
  <g fill="#d7fff0" opacity=".8">
    <circle cx="143" cy="202" r="3"/><circle cx="155" cy="190" r="2"/>
    <circle cx="165" cy="207" r="2"/><circle cx="184" cy="185" r="3"/>
  </g>
  <path d="M91 284l2 6 6 2-6 2-2 6-2-6-6-2 6-2z" fill="#ffd99e"/>
  <path d="M301 270l1.5 4 4 1.5-4 1.5-1.5 4-1.5-4-4-1.5 4-1.5z" fill="#ffd99e"/>
</svg>