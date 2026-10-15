<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f8f2e5"/>
      <stop offset="1" stop-color="#eadfc9"/>
    </linearGradient>
    <linearGradient id="ink2" gradientUnits="userSpaceOnUse" x1="178" y1="250" x2="258" y2="78">
      <stop offset="0" stop-color="#2f3d57"/>
      <stop offset="0.3" stop-color="#7a3a68"/>
      <stop offset="0.6" stop-color="#c2365f"/>
      <stop offset="0.85" stop-color="#ef6f3d"/>
      <stop offset="1" stop-color="#f2b544"/>
    </linearGradient>
    <radialGradient id="bloom">
      <stop offset="0" stop-color="#e0457b" stop-opacity="0.30"/>
      <stop offset="0.55" stop-color="#ef6f3d" stop-opacity="0.14"/>
      <stop offset="1" stop-color="#ef6f3d" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="vig">
      <stop offset="0.6" stop-color="#000" stop-opacity="0"/>
      <stop offset="1" stop-color="#5b4a2e" stop-opacity="0.18"/>
    </radialGradient>
    <pattern id="dots" width="50" height="50" patternUnits="userSpaceOnUse">
      <circle cx="25" cy="25" r="8.5" fill="none" stroke="#3b4a63" stroke-width="2.3" opacity="0.8"/>
    </pattern>
    <filter id="wob" x="-30%" y="-30%" width="160%" height="160%">
      <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="11" result="t"/>
      <feDisplacementMap in="SourceGraphic" in2="t" scale="5" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
      <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="4" result="t"/>
      <feDisplacementMap in="SourceGraphic" in2="t" scale="26" xChannelSelector="R" yChannelSelector="G"/>
      <feGaussianBlur stdDeviation="6"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#paper)"/>

  <g stroke="#3b4a63" stroke-width="0.6" opacity="0.13">
    <path d="M50 50H350M50 100H350M50 150H350M50 200H350M50 250H350M50 300H350M50 350H350"/>
    <path d="M50 50V350M100 50V350M150 50V350M200 50V350M250 50V350M300 50V350M350 50V350"/>
  </g>

  <rect x="50" y="50" width="300" height="300" fill="url(#dots)"/>

  <ellipse cx="172" cy="206" rx="150" ry="140" fill="url(#bloom)" filter="url(#soft)"/>

  <rect x="152" y="202" width="46" height="46" fill="url(#paper)" opacity="0.95"/>

  <g filter="url(#wob)" fill="none" stroke="url(#ink2)" stroke-linecap="round">
    <path d="M175,225 C168,220 166,210 174,205 C183,200 194,207 195,217" stroke-width="2.4"/>
    <path d="M195,217 C197,234 183,248 165,249 C141,250 124,231 125,207" stroke-width="4"/>
    <path d="M125,207 C126,173 156,146 191,147 C237,148 272,187 269,233" stroke-width="6.5"/>
    <path d="M269,233 C265,285 220,324 168,321 C101,317 53,260 57,193" stroke-width="9.5"/>
    <path d="M57,193 C61,132 106,84 166,72 C196,66 226,73 251,89" stroke-width="13"/>
    <path d="M251,89 C268,100 282,116 290,135" stroke-width="7"/>
    <path d="M290,135 C295,147 297,157 296,166" stroke-width="3"/>
  </g>

  <g filter="url(#wob)">
    <circle cx="305" cy="118" r="4.6" fill="#ef6f3d"/>
    <circle cx="318" cy="101" r="2.6" fill="#c2365f"/>
    <circle cx="296" cy="96" r="3.4" fill="#f2b544"/>
    <circle cx="330" cy="130" r="1.8" fill="#ef6f3d"/>
    <circle cx="283" cy="79" r="2.1" fill="#c2365f"/>
    <circle cx="258" cy="63" r="3" fill="#ef6f3d" opacity="0.85"/>
    <circle cx="40" cy="245" r="3.6" fill="#8a3a66"/>
    <circle cx="31" cy="214" r="2.2" fill="#c2365f"/>
    <circle cx="112" cy="346" r="2.8" fill="#7a3a68"/>
    <circle cx="146" cy="352" r="1.7" fill="#2f3d57"/>
    <circle cx="214" cy="332" r="2.3" fill="#9c3763"/>
    <circle cx="187" cy="243" r="1.6" fill="#2f3d57"/>
    <circle cx="206" cy="258" r="2" fill="#3b4a63"/>
  </g>

  <g fill="none" stroke="#c2365f" stroke-width="1" opacity="0.5" filter="url(#wob)">
    <path d="M275,250 C262,286 230,310 196,313"/>
    <path d="M70,170 C78,126 115,95 159,88"/>
  </g>

  <rect width="400" height="400" fill="url(#vig)"/>

  <text x="352" y="378" font-family="Georgia,serif" font-size="11.5" font-style="italic" fill="#3b4a63" opacity="0.55" text-anchor="end">el error</text>
</svg>