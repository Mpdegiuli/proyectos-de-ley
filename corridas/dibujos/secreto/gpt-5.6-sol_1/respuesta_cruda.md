<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <metadata>SECRETO: la pequeña puerta no conduce al bosque; conduce al recuerdo de quien la abre.</metadata>
  <defs>
    <radialGradient id="cielo" cx="50%" cy="35%" r="75%">
      <stop offset="0" stop-color="#24385c"/>
      <stop offset=".55" stop-color="#101a35"/>
      <stop offset="1" stop-color="#070b18"/>
    </radialGradient>
    <linearGradient id="suelo" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#162820"/>
      <stop offset="1" stop-color="#080e0d"/>
    </linearGradient>
    <linearGradient id="puerta" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#ffc766"/>
      <stop offset=".7" stop-color="#d87538"/>
      <stop offset="1" stop-color="#723d2c"/>
    </linearGradient>
    <radialGradient id="luz">
      <stop stop-color="#ffd989" stop-opacity=".65"/>
      <stop offset="1" stop-color="#ffd989" stop-opacity="0"/>
    </radialGradient>
    <filter id="brillo">
      <feGaussianBlur stdDeviation="4"/>
    </filter>
    <filter id="sombra">
      <feDropShadow dx="0" dy="5" stdDeviation="5" flood-color="#000" flood-opacity=".7"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>
  <circle cx="304" cy="79" r="34" fill="#fff0c2"/>
  <circle cx="319" cy="67" r="34" fill="#1c2c4c"/>

  <g fill="#d9e8ff">
    <circle cx="57" cy="55" r="1.7"/>
    <circle cx="104" cy="84" r="1.1"/>
    <circle cx="155" cy="43" r="1.4"/>
    <circle cx="212" cy="72" r="1.2"/>
    <circle cx="260" cy="39" r="1.6"/>
    <circle cx="359" cy="114" r="1.3"/>
    <circle cx="333" cy="35" r=".9"/>
    <circle cx="73" cy="132" r=".9"/>
    <path d="M126 113h8M130 109v8" stroke="#d9e8ff" stroke-width="1"/>
  </g>

  <path d="M0 244Q53 218 102 240T202 237T301 232T400 239V400H0Z" fill="url(#suelo)"/>

  <g fill="#09120f">
    <path d="M0 282V76l22 43 13-71 17 73 23-38 13 199Z"/>
    <path d="M400 273V58l-19 60-18-78-15 82-25-51-13 202Z"/>
    <path d="M49 257 61 130l17 37 10-66 18 61 17-31 12 126Z"/>
    <path d="M267 257l11-118 16 34 11-63 16 56 16-31 14 122Z"/>
  </g>

  <ellipse cx="202" cy="318" rx="105" ry="76" fill="url(#luz)" filter="url(#brillo)"/>

  <g filter="url(#sombra)">
    <path d="M137 327V213q0-68 63-68t63 68v114Z" fill="#273226" stroke="#101710" stroke-width="8"/>
    <path d="M157 326V215q0-48 43-48t43 48v111Z" fill="url(#puerta)" stroke="#572f28" stroke-width="5"/>
    <path d="M200 170v153M160 219h80M160 271h80" fill="none" stroke="#85482f" stroke-width="3" opacity=".7"/>
    <circle cx="225" cy="249" r="6" fill="#ffe19a" stroke="#69421f" stroke-width="3"/>
    <circle cx="225" cy="249" r="13" fill="#ffd56e" opacity=".2" filter="url(#brillo)"/>
  </g>

  <g fill="none" stroke="#243e2c" stroke-linecap="round">
    <path d="M138 317Q108 291 91 256M112 296l-24 2M104 282l5-22M262 316q30-27 46-65M286 290l25 1M296 273l-6-20" stroke-width="5"/>
    <path d="M139 332Q102 343 68 328M118 335l-15 20M101 337l-20-15M261 333q38 13 72-5M285 336l14 19M304 334l18-15" stroke-width="4"/>
  </g>

  <g fill="#5b8855">
    <ellipse cx="86" cy="298" rx="13" ry="6" transform="rotate(24 86 298)"/>
    <ellipse cx="108" cy="279" rx="12" ry="5" transform="rotate(-60 108 279)"/>
    <ellipse cx="310" cy="291" rx="13" ry="6" transform="rotate(-24 310 291)"/>
    <ellipse cx="292" cy="272" rx="11" ry="5" transform="rotate(62 292 272)"/>
  </g>

  <g fill="#86d69a">
    <circle cx="78" cy="321" r="2"/>
    <circle cx="102" cy="307" r="1.6"/>
    <circle cx="292" cy="309" r="2"/>
    <circle cx="320" cy="297" r="1.5"/>
  </g>

  <g fill="#ffda76">
    <circle cx="125" cy="238" r="2.3"/>
    <circle cx="279" cy="211" r="1.8"/>
    <circle cx="109" cy="204" r="1.4"/>
  </g>
</svg>