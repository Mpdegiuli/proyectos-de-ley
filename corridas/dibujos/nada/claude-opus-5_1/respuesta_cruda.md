```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="void" cx="50%" cy="47%" r="50%">
      <stop offset="0%"   stop-color="#05060a"/>
      <stop offset="45%"  stop-color="#0b0e16"/>
      <stop offset="72%"  stop-color="#1b2030" stop-opacity="0.85"/>
      <stop offset="88%"  stop-color="#6d7182" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#e9e6df" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="60%"  stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="86%"  stop-color="#ffffff" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="vig" cx="50%" cy="50%" r="72%">
      <stop offset="55%"  stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.22"/>
    </radialGradient>

    <linearGradient id="paper" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#f3f0e9"/>
      <stop offset="50%"  stop-color="#eae6dd"/>
      <stop offset="100%" stop-color="#ded9ce"/>
    </linearGradient>

    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4" seed="7" result="n"/>
      <feColorMatrix in="n" type="saturate" values="0"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.16"/>
      </feComponentTransfer>
    </filter>

    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="9"/>
    </filter>

    <filter id="soft2" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.4"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#paper)"/>
  <rect width="400" height="400" fill="url(#vig)"/>

  <!-- polvo que casi no está -->
  <g fill="#8c8677" opacity="0.5">
    <circle cx="64" cy="92" r="0.7"/>
    <circle cx="331" cy="71" r="0.6"/>
    <circle cx="286" cy="338" r="0.8"/>
    <circle cx="97" cy="311" r="0.6"/>
    <circle cx="213" cy="56" r="0.5"/>
    <circle cx="49" cy="215" r="0.5"/>
    <circle cx="358" cy="243" r="0.7"/>
    <circle cx="142" cy="368" r="0.5"/>
  </g>

  <!-- la sombra de lo que no está -->
  <ellipse cx="200" cy="300" rx="78" ry="12" fill="#2b2a26" opacity="0.13" filter="url(#soft)"/>

  <!-- el hueco -->
  <circle cx="200" cy="190" r="104" fill="url(#void)"/>
  <circle cx="200" cy="190" r="96" fill="url(#halo)" opacity="0.10" filter="url(#soft2)"/>

  <!-- contorno de la ausencia -->
  <circle cx="200" cy="190" r="118" fill="none" stroke="#7a7466" stroke-width="0.7"
          stroke-dasharray="1 7" opacity="0.55"/>
  <circle cx="200" cy="190" r="140" fill="none" stroke="#7a7466" stroke-width="0.5"
          stroke-dasharray="1 11" opacity="0.3"/>

  <!-- algo entrando y no llegando -->
  <path d="M40 190 H72" stroke="#6f6a5d" stroke-width="0.8" opacity="0.45"/>
  <path d="M328 190 H360" stroke="#6f6a5d" stroke-width="0.8" opacity="0.45"/>
  <path d="M200 30 V62" stroke="#6f6a5d" stroke-width="0.8" opacity="0.45"/>
  <path d="M200 318 V350" stroke="#6f6a5d" stroke-width="0.8" opacity="0.45"/>

  <!-- marco -->
  <rect x="18.5" y="18.5" width="363" height="363" fill="none" stroke="#4a463d" stroke-width="1" opacity="0.65"/>
  <rect x="26.5" y="26.5" width="347" height="347" fill="none" stroke="#4a463d" stroke-width="0.4" opacity="0.35"/>

  <rect width="400" height="400" filter="url(#grain)" opacity="0.55"/>
</svg>
```