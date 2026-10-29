<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x2="0" y2="1">
      <stop stop-color="#10152f"/>
      <stop offset=".58" stop-color="#26345a"/>
      <stop offset="1" stop-color="#456273"/>
    </linearGradient>
    <radialGradient id="halo">
      <stop stop-color="#ffe8a3" stop-opacity=".28"/>
      <stop offset="1" stop-color="#ffe8a3" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="moon" x1=".2" y1="0" x2=".8" y2="1">
      <stop stop-color="#fff4c9"/>
      <stop offset="1" stop-color="#eec776"/>
    </linearGradient>
    <linearGradient id="fur" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#f6a54a"/>
      <stop offset=".55" stop-color="#dc683b"/>
      <stop offset="1" stop-color="#a93e37"/>
    </linearGradient>
    <linearGradient id="tail" x1="0" y1="0" x2=".8" y2="1">
      <stop stop-color="#ffbd59"/>
      <stop offset=".6" stop-color="#e7763d"/>
      <stop offset="1" stop-color="#bd4937"/>
    </linearGradient>
    <filter id="glow" x="-200%" y="-200%" width="500%" height="500%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="205" cy="137" r="142" fill="url(#halo)"/>

  <g fill="#fff4cf">
    <circle cx="42" cy="54" r="1.4"/><circle cx="82" cy="91" r="1"/>
    <circle cx="119" cy="39" r="1.6"/><circle cx="164" cy="72" r=".9"/>
    <circle cx="253" cy="38" r="1.2"/><circle cx="300" cy="72" r="1.5"/>
    <circle cx="355" cy="42" r="1"/><circle cx="371" cy="115" r="1.5"/>
    <circle cx="29" cy="144" r=".9"/><circle cx="72" cy="166" r="1.3"/>
    <circle cx="331" cy="169" r=".8"/><circle cx="287" cy="113" r=".8"/>
    <circle cx="102" cy="128" r=".7"/><circle cx="342" cy="102" r=".7"/>
  </g>
  <g stroke="#fff2bd" stroke-linecap="round" filter="url(#glow)">
    <path d="M60 109v10m-5-5h10" stroke-width="1.2"/>
    <path d="M325 48v12m-6-6h12" stroke-width="1.1"/>
    <path d="M362 205v9m-4.5-4.5h9" stroke-width="1"/>
    <path d="M104 202v8m-4-4h8" stroke-width=".9"/>
  </g>

  <circle cx="205" cy="137" r="88" fill="url(#moon)"/>
  <g fill="#cfa85f" opacity=".18">
    <ellipse cx="169" cy="102" rx="19" ry="13" transform="rotate(-24 169 102)"/>
    <circle cx="242" cy="93" r="11"/>
    <ellipse cx="248" cy="162" rx="24" ry="17" transform="rotate(18 248 162)"/>
    <circle cx="177" cy="177" r="14"/>
    <circle cx="205" cy="128" r="7"/>
    <circle cx="149" cy="141" r="6"/>
  </g>
  <path d="M143 85c23-33 70-46 105-25" fill="none" stroke="#fffbe4" stroke-width="3" stroke-linecap="round" opacity=".45"/>

  <g fill="#a9bfd0" opacity=".18">
    <path d="M0 196c22-13 45-10 58 2 19-12 49-7 57 10H0z"/>
    <path d="M286 218c14-16 40-17 55-4 18-8 43-2 59 13v8h-114z"/>
  </g>

  <path d="M0 273 49 218l24 27 45-61 55 72 37-42 49 51 40-69 101 90v54H0z" fill="#344563"/>
  <path d="m49 218 24 27 45-61 22 29-22-10-16 24-12-9-17 27-24 27-20-10z" fill="#718096" opacity=".36"/>
  <path d="m259 196 40-69 45 40-38-16-13 24-11-8-23 29z" fill="#82909c" opacity=".3"/>
  <path d="M0 297c52-31 98-24 140 3 50-38 112-36 156-4 40-23 74-20 104-4v108H0z" fill="#203d4b"/>
  <path d="M0 330c62-30 117-17 159 5 60-35 151-26 241 3v62H0z" fill="#142f39"/>

  <g fill="#102a35">
    <path d="M22 322h6l-2-93h-2z"/>
    <path d="m25 205-23 48h14l-25 38h22l-19 28h62l-20-28h22l-25-38h14z"/>
    <path d="M365 330h6l-2-112h-2z"/>
    <path d="m368 185-25 51h15l-28 42h23l-22 32h74l-23-32h24l-29-42h16z"/>
    <path d="M334 326h4l-1-69h-2z" opacity=".8"/>
    <path d="m336 238-17 35h10l-19 29h16l-14 21h49l-15-21h17l-20-29h11z" opacity=".8"/>
  </g>

  <ellipse cx="211" cy="350" rx="112" ry="18" fill="#0b222b" opacity=".55"/>

  <path d="M143 292c8-38 46-58 88-46 39 10 61 45 47 72-13 26-54 35-91 24-37-10-51-26-44-50z" fill="url(#fur)"/>
  <path d="M191 256c25-10 56 1 69 22-17-9-38-8-52 2-12 8-18 21-17 35-18-19-17-46 0-59z" fill="#f6b55c" opacity=".38"/>

  <path d="M270 280c40-12 73 12 67 42-7 35-63 50-119 40-42-8-75-24-82-43-6-16 5-29 22-28 18 1 26 16 39 25 25 18 76 20 96 5 12-9 5-24-10-24z" fill="url(#tail)"/>
  <path d="M315 300c16 7 25 18 21 32-5 18-29 30-57 32 17-11 27-23 25-35-2-13-12-21-25-25 12-7 25-8 36-4z" fill="#ffe3ae"/>
  <path d="M151 302c7 13 25 25 48 33 36 13 78 12 105-1-26 20-73 23-111 10-35-12-55-28-57-40-1-7 5-12 15-12z" fill="#9f3934" opacity=".35"/>

  <path d="M137 291l-4-46 31 18c15-8 35-6 48 5l25-20-3 45c-2 25-27 42-53 39-25-2-42-18-44-41z" fill="url(#fur)"/>
  <path d="m140 254 20 13-18 12z" fill="#743443"/>
  <path d="m229 257-14 14 15 10z" fill="#743443"/>
  <path d="M145 292c10 4 20 2 28-5 7 11 19 16 34 14-3 18-20 29-38 25-17-3-27-17-24-34z" fill="#ffe0aa"/>
  <path d="M167 288c4 4 10 4 14 0" fill="none" stroke="#532f38" stroke-width="3" stroke-linecap="round"/>
  <path d="M204 286c4 3 9 3 13-1" fill="none" stroke="#532f38" stroke-width="3" stroke-linecap="round"/>
  <path d="m184 302 7-1-3 6z" fill="#4b2b35"/>
  <path d="M188 308c-1 5-6 7-11 5m11-5c2 4 7 5 11 2" fill="none" stroke="#8d553f" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M151 302c-11-1-20 1-27 5m30 1c-10 2-17 6-22 11" fill="none" stroke="#ffe8bd" stroke-width="1.2" stroke-linecap="round" opacity=".75"/>

  <g fill="none" stroke="#56816d" stroke-width="2" stroke-linecap="round">
    <path d="M73 363q-3-19 5-30m-5 19-10-9m12 2 9-11"/>
    <path d="M318 371q3-21-5-34m5 20 11-10m-13 1-8-9"/>
    <path d="M101 375q0-13 7-22m-6 13-8-5"/>
  </g>
  <g fill="#f9d67c" filter="url(#glow)">
    <circle cx="92" cy="286" r="2.2"/><circle cx="308" cy="267" r="1.8"/>
    <circle cx="70" cy="318" r="1.4"/><circle cx="347" cy="287" r="1.5"/>
  </g>
  <g fill="#d9e6c2">
    <circle cx="55" cy="367" r="2"/><circle cx="61" cy="370" r="1.4"/>
    <circle cx="348" cy="365" r="2"/><circle cx="354" cy="369" r="1.3"/>
    <circle cx="112" cy="385" r="1.5"/><circle cx="291" cy="382" r="1.6"/>
  </g>
</svg>