<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="sky">
      <stop stop-color="#26345e"/>
      <stop offset=".65" stop-color="#111b3b"/>
      <stop offset="1" stop-color="#080e23"/>
    </radialGradient>
    <linearGradient id="crown" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#235a72"/>
      <stop offset=".5" stop-color="#394778"/>
      <stop offset="1" stop-color="#173d5c"/>
    </linearGradient>
    <linearGradient id="wood">
      <stop stop-color="#163850"/>
      <stop offset=".45" stop-color="#3c7281"/>
      <stop offset="1" stop-color="#142d49"/>
    </linearGradient>
    <linearGradient id="island" x1="0" y1="0" x2=".3" y2="1">
      <stop stop-color="#5c8491"/>
      <stop offset=".3" stop-color="#29465e"/>
      <stop offset="1" stop-color="#121c36"/>
    </linearGradient>
    <radialGradient id="fruit">
      <stop stop-color="#fff7bf"/>
      <stop offset=".35" stop-color="#ffd18b"/>
      <stop offset="1" stop-color="#da7193"/>
    </radialGradient>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
    <clipPath id="canopy">
      <path d="M200 52C180 32 151 39 139 57c-26-10-52 1-57 25-31 2-45 28-32 51-16 21-8 49 16 58-3 28 20 47 46 41 13 25 44 30 64 15 17 17 46 16 63-1 29 13 56-1 59-27 28 2 45-18 40-43 19-16 17-44-3-57 6-29-15-48-42-45-12-24-37-32-59-21-10-11-22-14-34-1Z"/>
    </clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="197" cy="170" r="151" fill="#367c91" opacity=".08" filter="url(#glow)"/>
  <g fill="#b6dce1" opacity=".7">
    <circle cx="28" cy="47" r="1.3"/><circle cx="66" cy="31" r=".8"/>
    <circle cx="328" cy="29" r="1.2"/><circle cx="365" cy="69" r=".9"/>
    <circle cx="25" cy="193" r="1"/><circle cx="374" cy="220" r="1.4"/>
    <circle cx="42" cy="283" r=".8"/><circle cx="345" cy="292" r="1"/>
    <circle cx="91" cy="270" r=".8"/><circle cx="310" cy="264" r=".8"/>
    <circle cx="52" cy="341" r="1"/><circle cx="353" cy="353" r=".8"/>
  </g>
  <g fill="none" stroke="#84c9d3" stroke-width=".8" opacity=".4">
    <path d="M23 81h12m-6-6v12M363 138h14m-7-7v14M48 249h9m-4.5-4.5v9M334 322h10m-5-5v10"/>
    <circle cx="34" cy="142" r="2"/><circle cx="372" cy="270" r="2"/>
  </g>

  <!-- A small island hangs above the empty sky. -->
  <ellipse cx="200" cy="350" rx="116" ry="14" fill="#54a5a9" opacity=".12" filter="url(#glow)"/>
  <path d="M77 334c28-15 75-19 123-18 55-1 97 5 124 18-13 8-53 13-124 13-70 0-110-5-123-13Z" fill="#70a5a7"/>
  <path d="M77 334c21 10 70 15 123 15 55 0 101-5 124-15l-48 34-49 7-27 15-28-16-46-8Z" fill="url(#island)" stroke="#75aeb1" stroke-width="1.5"/>
  <path d="m126 345 27 18 19 11m50-25 5 26m48-32-26 24m-49-18v39" fill="none" stroke="#83bfbc" stroke-width="1.3" opacity=".6"/>

  <!-- The crown is a little ocean of its own. -->
  <path d="M200 52C180 32 151 39 139 57c-26-10-52 1-57 25-31 2-45 28-32 51-16 21-8 49 16 58-3 28 20 47 46 41 13 25 44 30 64 15 17 17 46 16 63-1 29 13 56-1 59-27 28 2 45-18 40-43 19-16 17-44-3-57 6-29-15-48-42-45-12-24-37-32-59-21-10-11-22-14-34-1Z"
        fill="url(#crown)" stroke="#79c9ca" stroke-width="2.5"/>

  <g clip-path="url(#canopy)">
    <circle cx="199" cy="143" r="87" fill="none" stroke="#8dd4d0" stroke-width="1" opacity=".34"/>
    <circle cx="199" cy="143" r="108" fill="none" stroke="#c4afcf" stroke-width="1" opacity=".25"/>
    <path d="M43 168c64-35 108 24 162-4s95-54 159-7M43 189c64-35 109 24 163-4s95-54 159-7"
          fill="none" stroke="#98d9d4" opacity=".16" stroke-width="2"/>
    <g fill="#d5e9d9" opacity=".73">
      <circle cx="110" cy="108" r="1.4"/><circle cx="146" cy="83" r="1"/>
      <circle cx="254" cy="90" r="1.5"/><circle cx="306" cy="132" r="1"/>
      <circle cx="101" cy="184" r="1"/><circle cx="280" cy="194" r="1.3"/>
      <circle cx="180" cy="72" r="1"/><circle cx="227" cy="209" r="1"/>
    </g>
    <!-- A moon swims among the branches. -->
    <circle cx="224" cy="116" r="26" fill="#f3d8b4" opacity=".14" filter="url(#glow)"/>
    <circle cx="224" cy="116" r="18" fill="#f7dfbc"/>
    <circle cx="232" cy="109" r="18" fill="#344a70"/>
    <path d="M115 145c10-12 23-11 32-3 7-5 11-4 17 0-6 2-9 6-11 10-10-1-19-3-26-1l-12 6 3-9Z"
          fill="#bedbd5" opacity=".8"/>
    <circle cx="140" cy="144" r="1" fill="#25435b"/>
    <path d="M265 159c7-9 17-8 23-2l10-4-3 8 3 7-10-3c-7 5-16 4-23-2Z"
          fill="#c9b8d4" opacity=".7"/>
    <circle cx="278" cy="159" r=".9" fill="#253752"/>
  </g>

  <!-- Branches grow into the enclosed sky. -->
  <g fill="none" stroke="#102c47" stroke-linecap="round" stroke-linejoin="round">
    <path d="M198 327c-9-52-1-97-4-139-2-25-17-48-45-70" stroke-width="26"/>
    <path d="M193 225c20-45 44-73 76-98" stroke-width="17"/>
    <path d="M189 186c-5-47 0-75 14-108" stroke-width="13"/>
    <path d="M172 145c-25-18-50-23-77-22M219 169c27-18 51-19 81-17M197 112c-14-21-33-30-51-35M248 144c7-27 23-43 40-53"
          stroke-width="8"/>
  </g>
  <g fill="none" stroke="url(#wood)" stroke-linecap="round" stroke-linejoin="round">
    <path d="M198 327c-9-52-1-97-4-139-2-25-17-48-45-70" stroke-width="18"/>
    <path d="M193 225c20-45 44-73 76-98" stroke-width="11"/>
    <path d="M189 186c-5-47 0-75 14-108" stroke-width="8"/>
    <path d="M172 145c-25-18-50-23-77-22M219 169c27-18 51-19 81-17M197 112c-14-21-33-30-51-35M248 144c7-27 23-43 40-53"
          stroke-width="4"/>
  </g>
  <path d="M185 220c-4 36-1 69 6 98m12-115c-9 41-6 76-1 108m-32-174-25-18m77 49 33-28"
        fill="none" stroke="#a0d8d0" stroke-width="1.5" opacity=".55"/>

  <!-- Leaves resemble tiny folded sails. -->
  <g fill="#8ad7c7" stroke="#b9e9d6" stroke-width="1">
    <path d="M94 122Q76 103 81 85q22 4 29 26-3 10-16 11Z"/>
    <path d="M147 77q-4-27 15-37 14 20-2 38Z"/>
    <path d="M202 79q-5-29 14-41 15 20 0 40Z"/>
    <path d="M288 92q-1-25 18-34 14 22-3 36Z"/>
    <path d="M300 152q21-18 40-10-3 24-30 26Z"/>
    <path d="M269 127q11-24 34-23 2 25-23 33Z"/>
    <path d="M146 121q-22-2-32-22 24-10 39 12Z"/>
    <path d="M111 188q-23 1-33-18 22-12 39 8Z"/>
  </g>
  <g fill="#b7a9d7" stroke="#e1c8e6" stroke-width="1">
    <path d="M149 145q-29 0-36-21 26-9 39 11Z"/>
    <path d="M220 169q-2-26 17-37 14 21-4 37Z"/>
    <path d="M289 195q19-18 38-9-6 22-29 23Z"/>
    <path d="M173 204q-23-8-26-29 26-3 32 21Z"/>
  </g>

  <!-- Luminous fruit hangs on threads of light. -->
  <g stroke="#a8d4cf" fill="none" stroke-width="1.2">
    <path d="M114 119v34m150-24v55m-86-66v46m119-11v29"/>
  </g>
  <g fill="#ffcb92" opacity=".65" filter="url(#glow)">
    <circle cx="114" cy="160" r="11"/><circle cx="264" cy="192" r="13"/>
    <circle cx="178" cy="171" r="9"/><circle cx="297" cy="190" r="8"/>
  </g>
  <g fill="url(#fruit)" stroke="#ffe2ba" stroke-width="1.2">
    <path d="M114 151c-12 12-10 20 0 22 10-2 12-10 0-22Z"/>
    <path d="M264 182c-14 15-12 25 0 27 12-2 14-12 0-27Z"/>
    <path d="M178 163c-10 11-9 18 0 20 9-2 10-9 0-20Z"/>
    <path d="M297 183c-9 9-8 16 0 18 8-2 9-9 0-18Z"/>
  </g>

  <!-- A door for whoever tends this impossible tree. -->
  <path d="M184 321v-28a14 14 0 0 1 28 0v28Z" fill="#10273c" stroke="#a0d1c7" stroke-width="2"/>
  <path d="M189 320v-26a9 9 0 0 1 18 0v26Z" fill="#f6bb84" opacity=".7" filter="url(#glow)"/>
  <path d="M189 321v-27a9 9 0 0 1 18 0v27Z" fill="#e5a875"/>
  <circle cx="203" cy="307" r="1.3" fill="#fff2cf"/>
  <path d="M175 322c-18 4-35 8-48 16m85-16c24 3 42 7 59 15" fill="none" stroke="#afd8bf" stroke-width="2" opacity=".7"/>
  <g fill="#ffd7a1">
    <circle cx="111" cy="330" r="2"/><circle cx="278" cy="331" r="2"/>
    <circle cx="150" cy="326" r="1.5"/><circle cx="244" cy="326" r="1.5"/>
  </g>
</svg>