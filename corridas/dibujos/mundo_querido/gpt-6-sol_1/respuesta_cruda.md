<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="night">
      <stop stop-color="#285c70"/>
      <stop offset="1" stop-color="#102c45"/>
    </radialGradient>
    <linearGradient id="sky" x2="0" y2="1">
      <stop stop-color="#a4ddda"/>
      <stop offset=".7" stop-color="#f5e2bd"/>
      <stop offset="1" stop-color="#fff0ce"/>
    </linearGradient>
    <linearGradient id="sea" x2="0" y2="1">
      <stop stop-color="#66c8c3"/>
      <stop offset="1" stop-color="#267c9e"/>
    </linearGradient>
    <clipPath id="world"><circle cx="200" cy="192" r="150"/></clipPath>
    <g id="spark" fill="#f8dfaa">
      <path d="M0-5 1.3-1.3 5 0 1.3 1.3 0 5-1.3 1.3-5 0-1.3-1.3Z"/>
    </g>
    <g id="flower">
      <g fill="#fff3d6">
        <ellipse cy="-5" rx="2.5" ry="4"/>
        <ellipse cy="5" rx="2.5" ry="4"/>
        <ellipse cx="-5" rx="4" ry="2.5"/>
        <ellipse cx="5" rx="4" ry="2.5"/>
      </g>
      <circle r="2.2" fill="#ed9a63"/>
    </g>
  </defs>

  <rect width="400" height="400" fill="url(#night)"/>
  <circle cx="200" cy="192" r="164" fill="none" stroke="#8bc6c0" stroke-opacity=".25" stroke-width="1.5"/>
  <path d="M24 182C38 86 116 18 211 22M376 202c-5 89-70 158-154 169" fill="none" stroke="#e2d4a7" stroke-opacity=".42" stroke-width="1.5" stroke-linecap="round"/>
  <use href="#spark" x="34" y="97"/>
  <use href="#spark" x="358" y="77"/>
  <use href="#spark" x="371" y="259"/>
  <use href="#spark" x="46" y="254"/>
  <circle cx="82" cy="37" r="2" fill="#f8dfaa"/>
  <circle cx="320" cy="27" r="2" fill="#f8dfaa"/>
  <circle cx="389" cy="148" r="2" fill="#f8dfaa"/>
  <circle cx="15" cy="224" r="2" fill="#f8dfaa"/>

  <g clip-path="url(#world)">
    <rect x="48" y="40" width="304" height="305" fill="url(#sky)"/>

    <circle cx="267" cy="107" r="40" fill="#fff0ac" opacity=".3"/>
    <circle cx="267" cy="107" r="28" fill="#ffda83"/>
    <circle cx="267" cy="107" r="21" fill="#ffe7a3"/>

    <path d="M77 135c7-11 21-10 27-2 5-5 15-5 19 3 11-2 18 5 18 11H72c-1-6 1-10 5-12ZM200 79c6-8 18-8 23-1 5-4 12-2 15 4 8-1 13 4 14 9h-56c0-5 1-9 4-12Z" fill="#fffaf0" opacity=".88"/>
    <path d="M126 104q5-5 10 0 5-5 10 0m25 17q5-5 10 0 5-5 10 0m104 32q5-5 10 0 5-5 10 0" fill="none" stroke="#3b7880" stroke-width="2" stroke-linecap="round"/>

    <path d="M39 216q49-73 113-32 46-65 106-28 46-35 103 22v102H39Z" fill="#87b995"/>
    <path d="M40 239q55-36 99-24 50-46 99-21 63-34 124 15v90H40Z" fill="#5caa82"/>
    <path d="M41 266q49-33 99-17 52-29 106-5 67-28 116 9v94H41Z" fill="#348e78"/>

    <!-- Una aldea y una ciudad alimentadas por el sol -->
    <path d="M86 207v-18l21-15 21 15v42H86Z" fill="#f7e7c3"/>
    <path d="m81 191 26-20 26 20" fill="none" stroke="#a85d55" stroke-width="6" stroke-linejoin="round"/>
    <rect x="101" y="207" width="12" height="24" rx="6" fill="#bd8566"/>
    <rect x="91" y="193" width="8" height="9" rx="2" fill="#75bdc1"/>
    <rect x="116" y="193" width="8" height="9" rx="2" fill="#75bdc1"/>
    <path d="M88 184h38" stroke="#396a73" stroke-width="2"/>
    <path d="M93 181h27" stroke="#578f9e" stroke-width="5"/>

    <g fill="#e6ead0">
      <rect x="268" y="187" width="24" height="55" rx="2"/>
      <rect x="294" y="172" width="27" height="70" rx="2"/>
      <rect x="324" y="199" width="20" height="43" rx="2"/>
    </g>
    <path d="M266 187h29m-2-15h30m-1 27h24" stroke="#358c77" stroke-width="5"/>
    <path d="M299 168q6-10 12 0 6-10 12 0" fill="none" stroke="#4a9d71" stroke-width="3"/>
    <g fill="#7ebec0">
      <path d="M273 198h5v7h-5zm10 0h5v7h-5zm-10 15h5v7h-5zm10 0h5v7h-5zm17-30h5v7h-5zm10 0h5v7h-5zm-10 15h5v7h-5zm10 0h5v7h-5zm-10 15h5v7h-5zm10 0h5v7h-5zm20-4h5v7h-5zm0 15h5v7h-5z"/>
    </g>

    <!-- Bosques -->
    <path d="M67 233v-44m76 54v-54m191 70v-34" stroke="#665c52" stroke-width="6" stroke-linecap="round"/>
    <g fill="#3c946f">
      <circle cx="67" cy="177" r="20"/><circle cx="55" cy="190" r="15"/><circle cx="81" cy="190" r="17"/>
      <circle cx="143" cy="181" r="17"/><circle cx="132" cy="194" r="13"/><circle cx="154" cy="194" r="14"/>
      <circle cx="334" cy="218" r="14"/><circle cx="324" cy="229" r="12"/><circle cx="344" cy="231" r="12"/>
    </g>
    <g fill="#66b682">
      <circle cx="57" cy="177" r="8"/><circle cx="75" cy="186" r="9"/>
      <circle cx="136" cy="180" r="7"/><circle cx="151" cy="191" r="7"/>
      <circle cx="329" cy="216" r="6"/>
    </g>

    <!-- Un camino compartido -->
    <path d="M141 248q57-22 119 0l47 45H94Z" fill="#e3c690"/>
    <path d="M184 253q17 23 6 49m32-48q-12 21-3 49" fill="none" stroke="#f6e2af" stroke-width="2" opacity=".8"/>

    <!-- Personas de la mano -->
    <g stroke="#493f48" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
      <path d="m149 267-5 15m14-15 5 15m24-16-5 17m14-17 5 17m21-17-4 17m13-17 6 17m19-18-4 17m12-17 6 17"/>
    </g>
    <g fill="#b96c56">
      <circle cx="153" cy="237" r="7"/>
      <circle cx="230" cy="237" r="7"/>
    </g>
    <g fill="#6b463b">
      <circle cx="192" cy="234" r="7"/>
    </g>
    <circle cx="258" cy="237" r="7" fill="#e1ab79"/>
    <path d="M146 249q7-6 14 0l3 19h-20Zm39-3q7-6 14 0l3 21h-20Zm38 1q7-6 14 0l3 20h-20Zm28 2q7-6 14 0l3 19h-20Z" fill="#ec9870"/>
    <path d="M182 247q9-6 18 0l2 20h-22Zm42 0q8-6 15 0l2 20h-20Z" fill="#e0bc6d"/>
    <path d="M250 249q8-5 15 0l3 19h-20Z" fill="#72a6a2"/>
    <path d="m145 251-14 10m29-10 16 5m7-8-7 8m25-8 12 7m7-7-7 7m27-6 7 7m1-7-1 7m20-6 13 9" fill="none" stroke="#a96853" stroke-width="4" stroke-linecap="round"/>
    <circle cx="131" cy="261" r="2.5" fill="#a96853"/>
    <circle cx="280" cy="260" r="2.5" fill="#a96853"/>

    <!-- Agua limpia, vida abundante -->
    <path d="M43 290q42-12 79 0t78 0 80 0 80 0v60H43Z" fill="url(#sea)"/>
    <path d="M57 304q18-5 35 0m23 11q21-5 43 0m90-10q18-5 37 0m29 14q15-4 28 0M72 330q18-4 34 0m102-10q18-4 36 0" fill="none" stroke="#c1eee0" stroke-width="2" stroke-linecap="round" opacity=".7"/>
    <path d="m119 315 9-5 10 5-10 5Zm145 15 11-6 11 6-11 6Z" fill="#f5dc9e"/>
    <circle cx="133" cy="314" r="1" fill="#386981"/>
    <circle cx="281" cy="329" r="1" fill="#386981"/>
    <path d="M168 340q-7-17 0-26m0 26q12-15 18-14m46 17q-8-20-2-30m2 30q10-12 17-12" fill="none" stroke="#b7e4bf" stroke-width="3" stroke-linecap="round"/>
    <circle cx="153" cy="310" r="2" fill="#e7f5e4" opacity=".8"/>
    <circle cx="159" cy="303" r="1.5" fill="#e7f5e4" opacity=".8"/>
  </g>

  <circle cx="200" cy="192" r="150" fill="none" stroke="#f7e9bf" stroke-width="4"/>

  <!-- Manos que cuidan el planeta -->
  <path d="M21 301q13-17 27-5l27 25q29 25 69 30l38 3v27q-70-3-113-27-29-16-48-53Z" fill="#db9d77"/>
  <path d="M379 301q-13-17-27-5l-27 25q-29 25-69 30l-38 3v27q70-3 113-27 29-16 48-53Z" fill="#a96355"/>
  <path d="M42 302q27 38 70 52m246-52q-27 38-70 52" fill="none" stroke="#f6c69a" stroke-width="3" opacity=".55" stroke-linecap="round"/>
  <path d="M177 360q23 7 46 0" fill="none" stroke="#f6e0b8" stroke-width="3" stroke-linecap="round"/>
  <use href="#flower" x="46" y="276"/>
  <use href="#flower" x="355" y="279"/>
</svg>