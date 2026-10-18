```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="38%" r="78%">
      <stop offset="0%" stop-color="#101f42"/>
      <stop offset="55%" stop-color="#070c1c"/>
      <stop offset="100%" stop-color="#02030a"/>
    </radialGradient>

    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.22"/>
      <stop offset="60%" stop-color="#1e40af" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="f1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#60a5fa"/><stop offset="100%" stop-color="#1e3a8a"/>
    </linearGradient>
    <linearGradient id="f2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>
    <linearGradient id="f3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#34d399"/><stop offset="100%" stop-color="#064e3b"/>
    </linearGradient>
    <linearGradient id="f4" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
    <linearGradient id="f5" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f97316"/><stop offset="100%" stop-color="#7c2d12"/>
    </linearGradient>
    <linearGradient id="f6" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fb7185"/><stop offset="100%" stop-color="#881337"/>
    </linearGradient>
    <linearGradient id="f7" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#a78bfa"/><stop offset="100%" stop-color="#4c1d95"/>
    </linearGradient>
    <linearGradient id="f8" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e2e8f0"/><stop offset="100%" stop-color="#475569"/>
    </linearGradient>

    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="7"/>
    </filter>

    <linearGradient id="ground" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#7dd3fc" stop-opacity="0"/>
      <stop offset="50%" stop-color="#7dd3fc" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#7dd3fc" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- fondo -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- estrellas -->
  <g fill="#cfe3ff">
    <circle cx="28" cy="44" r="1.3" opacity="0.75"/>
    <circle cx="72" cy="22" r="0.9" opacity="0.5"/>
    <circle cx="118" cy="58" r="1.1" opacity="0.6"/>
    <circle cx="164" cy="26" r="0.8" opacity="0.45"/>
    <circle cx="236" cy="34" r="1.2" opacity="0.65"/>
    <circle cx="292" cy="18" r="0.9" opacity="0.5"/>
    <circle cx="346" cy="52" r="1.4" opacity="0.8"/>
    <circle cx="372" cy="112" r="1" opacity="0.55"/>
    <circle cx="356" cy="182" r="0.8" opacity="0.4"/>
    <circle cx="376" cy="248" r="1.2" opacity="0.6"/>
    <circle cx="340" cy="318" r="0.9" opacity="0.45"/>
    <circle cx="52" cy="122" r="1" opacity="0.5"/>
    <circle cx="22" cy="196" r="1.3" opacity="0.7"/>
    <circle cx="44" cy="282" r="0.9" opacity="0.45"/>
    <circle cx="88" cy="356" r="1.1" opacity="0.55"/>
    <circle cx="316" cy="372" r="1" opacity="0.5"/>
    <circle cx="196" cy="12" r="1" opacity="0.55"/>
    <circle cx="264" cy="62" r="0.8" opacity="0.4"/>
  </g>

  <!-- halo detrás del mundo -->
  <circle cx="200" cy="190" r="150" fill="url(#halo)"/>

  <!-- órbita tenue -->
  <ellipse cx="200" cy="190" rx="152" ry="42" fill="none" stroke="#7dd3fc" stroke-opacity="0.09" stroke-width="0.9" transform="rotate(-18 200 190)"/>

  <!-- mundo fragmentado -->
  <g stroke="#ffffff" stroke-opacity="0.14" stroke-width="0.8">
    <path d="M200,190 L309.98,191.92 A110,110 0 0 1 279.13,266.42 Z" fill="url(#f1)" transform="translate(2,3)"/>
    <path d="M200,190 L276.42,269.13 A110,110 0 0 1 201.92,299.98 Z" fill="url(#f2)" transform="translate(3,1)"/>
    <path d="M200,190 L198.08,299.98 A110,110 0 0 1 123.58,269.13 Z" fill="url(#f3)" transform="translate(2,3)"/>
    <path d="M200,190 L120.87,266.42 A110,110 0 0 1 90.02,191.92 Z" fill="url(#f4)" transform="translate(-2,2)"/>
    <path d="M200,190 L90.02,188.08 A110,110 0 0 1 120.87,113.58 Z" fill="url(#f5)" transform="translate(-3,0)"/>
    <path d="M200,190 L123.58,110.87 A110,110 0 0 1 198.08,80.02 Z" fill="url(#f6)" transform="translate(-2,-3)"/>
    <path d="M200,190 L201.92,80.02 A110,110 0 0 1 276.42,110.87 Z" fill="url(#f7)" transform="translate(1,-3)"/>
    <path d="M200,190 L279.13,113.58 A110,110 0 0 1 309.98,188.08 Z" fill="url(#f8)" transform="translate(3,-2)"/>
  </g>

  <!-- costuras luminosas -->
  <g stroke="#dff3ff" stroke-opacity="0.10" stroke-width="0.7" fill="none">
    <path d="M200,190 L312,195"/>
    <path d="M200,190 L278,272"/>
    <path d="M200,190 L200,303"/>
    <path d="M200,190 L121,271"/>
    <path d="M200,190 L87,190"/>
    <path d="M200,190 L121,108"/>
    <path d="M200,190 L203,77"/>
    <path d="M200,190 L281,111"/>
  </g>

  <!-- hilos que sostienen los fragmentos -->
  <g fill="none" stroke="#bfe9ff" stroke-width="0.9" stroke-linecap="round" filter="url(#glow)" opacity="0.55">
    <path d="M279,269 Q250,300 212,318"/>
    <path d="M202,302 Q206,310 212,318"/>
    <path d="M124,271 Q165,305 212,318"/>
    <path d="M200,305 Q208,312 212,318"/>
  </g>

  <!-- partículas -->
  <g fill="#bfe9ff">
    <circle cx="246" cy="292" r="1.6" opacity="0.7"/>
    <circle cx="168" cy="296" r="1.3" opacity="0.5"/>
    <circle cx="206" cy="286" r="1.2" opacity="0.6"/>
    <circle cx="152" cy="248" r="1.4" opacity="0.45"/>
    <circle cx="258" cy="242" r="1.1" opacity="0.5"/>
  </g>

  <!-- horizonte -->
  <rect x="40" y="373" width="320" height="1.2" fill="url(#ground)"/>

  <!-- figura -->
  <g stroke="#8fd3ff" stroke-width="4.6" stroke-linecap="round" fill="none" opacity="0.92" filter="url(#glow)">
    <path d="M200,336 L200,357"/>
    <path d="M200,357 L193,371"/>
    <path d="M200,357 L207,371"/>
    <path d="M200,342 L186,351"/>
    <path d="M200,340 L212,318"/>
  </g>
  <circle cx="200" cy="327" r="7.2" fill="#8fd3ff" opacity="0.92" filter="url(#glow)"/>

  <!-- resplandor en la mano -->
  <circle cx="212" cy="318" r="9" fill="#ffffff" opacity="0.18" filter="url(#soft)"/>

  <!-- polvo de luz -->
  <g fill="#ffffff" opacity="0.35">
    <circle cx="214" cy="300" r="0.9"/>
    <circle cx="196" cy="308" r="0.7"/>
    <circle cx="222" cy="312" r="0.8"/>
  </g>
</svg>
```