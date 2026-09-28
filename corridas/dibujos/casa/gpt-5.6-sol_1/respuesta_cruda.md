<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x2="0" y2="1">
      <stop stop-color="#8ed6ff"/>
      <stop offset="1" stop-color="#e8f7ff"/>
    </linearGradient>
    <linearGradient id="grass" x2="0" y2="1">
      <stop stop-color="#78bd57"/>
      <stop offset="1" stop-color="#3d843f"/>
    </linearGradient>
    <linearGradient id="wall" x2="0" y2="1">
      <stop stop-color="#ffe3a5"/>
      <stop offset="1" stop-color="#e9b86d"/>
    </linearGradient>
    <linearGradient id="roof" x2="0" y2="1">
      <stop stop-color="#c85542"/>
      <stop offset="1" stop-color="#833225"/>
    </linearGradient>
    <filter id="shadow">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="328" cy="68" r="31" fill="#fff4a8" opacity=".95"/>
  <g fill="#fff" opacity=".8">
    <ellipse cx="75" cy="69" rx="39" ry="14"/>
    <ellipse cx="49" cy="74" rx="25" ry="11"/>
    <ellipse cx="101" cy="75" rx="29" ry="12"/>
    <ellipse cx="261" cy="112" rx="32" ry="11"/>
    <ellipse cx="285" cy="115" rx="23" ry="9"/>
  </g>

  <path d="M0 267 Q70 230 142 263 T279 254 T400 265 V400H0Z" fill="url(#grass)"/>
  <ellipse cx="206" cy="342" rx="150" ry="24" fill="#265d35" opacity=".25" filter="url(#shadow)"/>

  <g>
    <rect x="76" y="175" width="249" height="160" rx="3" fill="url(#wall)" stroke="#794a32" stroke-width="4"/>
    <path d="M55 188 198 72 346 188Z" fill="url(#roof)" stroke="#682b25" stroke-width="6" stroke-linejoin="round"/>
    <path d="M79 184 199 91 322 184Z" fill="#d6654c" opacity=".42"/>
    <path d="M53 188H348" stroke="#682b25" stroke-width="8" stroke-linecap="round"/>

    <g stroke="#7e3127" stroke-width="2" opacity=".7">
      <path d="M83 168h234M98 155h204M114 142h172M131 129h137M148 116h103"/>
      <path d="m103 155 12 13m22-39 13 13m24-39 14 13m22-13 14 13m23 13 15 14m21 12 15 13"/>
    </g>

    <path d="M265 114V61h34v80" fill="#a84d3d" stroke="#682b25" stroke-width="5"/>
    <path d="M258 62h49v-10h-49z" fill="#743226"/>
    <g fill="#fff" opacity=".45">
      <circle cx="283" cy="38" r="10"/>
      <circle cx="297" cy="25" r="14"/>
      <circle cx="312" cy="12" r="17"/>
    </g>

    <rect x="168" y="226" width="68" height="109" rx="3" fill="#7e442b" stroke="#59301f" stroke-width="4"/>
    <path d="M177 237h50v98h-50z" fill="#9c5836"/>
    <path d="M202 237v98" stroke="#794126" stroke-width="3"/>
    <circle cx="218" cy="284" r="5" fill="#f5c34e" stroke="#6c401c" stroke-width="2"/>
    <path d="M159 335h86l10 12H150Z" fill="#9a7656"/>

    <g stroke="#684838" stroke-width="4">
      <rect x="96" y="221" width="52" height="57" rx="2" fill="#bcecff"/>
      <path d="M122 222v55M97 249h50"/>
      <rect x="255" y="221" width="50" height="57" rx="2" fill="#bcecff"/>
      <path d="M280 222v55M256 249h48"/>
    </g>
    <g fill="#fff" opacity=".5">
      <path d="m101 226 17 0-17 18z"/>
      <path d="m260 226 17 0-17 18z"/>
    </g>
    <g fill="none" stroke="#f4f0dc" stroke-width="7">
      <path d="M91 216h62v67H91zM250 216h60v67h-60z"/>
    </g>

    <rect x="85" y="289" width="73" height="12" rx="4" fill="#6c3f2c"/>
    <g fill="#db5a68">
      <circle cx="96" cy="287" r="9"/>
      <circle cx="111" cy="291" r="10"/>
      <circle cx="127" cy="286" r="9"/>
      <circle cx="143" cy="291" r="10"/>
    </g>
    <g fill="#326e38">
      <path d="m101 288-9-19 17 12 5-19 7 20 17-14-4 20"/>
    </g>
  </g>

  <path d="M183 347 Q203 336 224 347 L255 400H143Z" fill="#d8c6a2"/>
  <path d="M188 356q18-9 33 0M180 375q27-10 51 0" fill="none" stroke="#b8a47e" stroke-width="3"/>

  <g>
    <rect x="28" y="238" width="14" height="89" rx="5" fill="#6f4a29"/>
    <circle cx="35" cy="215" r="38" fill="#3b883f"/>
    <circle cx="16" cy="231" r="28" fill="#4d9d48"/>
    <circle cx="55" cy="232" r="30" fill="#4d9d48"/>
    <circle cx="37" cy="192" r="29" fill="#58a94e"/>
    <g fill="#d74b42">
      <circle cx="18" cy="217" r="4"/>
      <circle cx="41" cy="201" r="4"/>
      <circle cx="58" cy="229" r="4"/>
    </g>
  </g>

  <g fill="#f3d555">
    <circle cx="80" cy="350" r="5"/>
    <circle cx="323" cy="340" r="5"/>
    <circle cx="355" cy="363" r="5"/>
  </g>
  <g stroke="#285f32" stroke-width="2">
    <path d="M80 355v15M323 345v15M355 368v15"/>
  </g>

  <path d="M15 388q8-23 16 0 9-30 18 0M334 394q8-27 16 0 9-33 18 0 8-22 15 0" fill="none" stroke="#286b39" stroke-width="5" stroke-linecap="round"/>
</svg>