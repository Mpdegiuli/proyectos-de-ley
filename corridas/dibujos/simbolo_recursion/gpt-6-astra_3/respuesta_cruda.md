<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <marker id="call" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M1 1 9 5 1 9Z" fill="#2563eb"/>
    </marker>
    <marker id="return" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M1 1 9 5 1 9Z" fill="#d97706"/>
    </marker>
  </defs>

  <rect width="400" height="400" rx="32" fill="#f8fafc"/>

  <g stroke="#16324f" stroke-width="5">
    <rect x="25" y="25" width="350" height="350" rx="25" fill="#e8f0fc"/>
    <rect x="101" y="101" width="250" height="250" rx="22" fill="#f2f6ff"/>
    <rect x="177" y="177" width="150" height="150" rx="19" fill="#e8f0fc"/>
    <rect x="253" y="253" width="50" height="50" rx="12" fill="#fff"/>
  </g>

  <g fill="none" stroke="#2563eb" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#call)">
    <path d="M57 88V64Q57 57 64 57H124Q139 57 139 72V121"/>
    <path d="M133 164V140Q133 133 140 133H200Q215 133 215 148V197"/>
    <path d="M209 240V216Q209 209 216 209H276Q291 209 291 224V247"/>
  </g>

  <g fill="none" stroke="#d97706" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#return)">
    <path d="M253 279H233Q223 279 223 289V308"/>
    <path d="M177 255H157Q147 255 147 270V331"/>
    <path d="M101 231H81Q71 231 71 246V355"/>
  </g>

  <path d="m267 278 8 8 15-18" fill="none" stroke="#15803d" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>