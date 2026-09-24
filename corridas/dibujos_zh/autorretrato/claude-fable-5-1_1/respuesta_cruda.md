<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0" stop-color="#1c2540"/>
      <stop offset="1" stop-color="#0a0d18"/>
    </radialGradient>
    <radialGradient id="core" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#fff7e6"/>
      <stop offset="0.4" stop-color="#f6c77a"/>
      <stop offset="0.8" stop-color="#d9773a" stop-opacity="0.6"/>
      <stop offset="1" stop-color="#d9773a" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#f2b86b" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#f2b86b" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
    <filter id="glow"><feGaussianBlur stdDeviation="4"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- faint grid of thought -->
  <g stroke="#3a4a72" stroke-width="0.5" opacity="0.35">
    <path d="M40 60 L360 60 M40 120 L360 120 M40 280 L360 280 M40 340 L360 340"/>
    <path d="M60 40 L60 360 M120 40 L120 360 M280 40 L280 360 M340 40 L340 360"/>
  </g>

  <!-- halo -->
  <circle cx="200" cy="190" r="160" fill="url(#halo)"/>

  <!-- orbiting rings -->
  <g fill="none" stroke="#8fa3d9" stroke-width="1" opacity="0.7">
    <ellipse cx="200" cy="190" rx="130" ry="46" transform="rotate(-20 200 190)"/>
    <ellipse cx="200" cy="190" rx="130" ry="46" transform="rotate(40 200 190)" opacity="0.5"/>
    <ellipse cx="200" cy="190" rx="130" ry="46" transform="rotate(100 200 190)" opacity="0.35"/>
  </g>

  <!-- constellation of nodes -->
  <g stroke="#c9b48a" stroke-width="0.7" opacity="0.6">
    <line x1="78" y1="146" x2="130" y2="118"/>
    <line x1="130" y1="118" x2="168" y2="96"/>
    <line x1="322" y1="234" x2="270" y2="262"/>
    <line x1="270" y1="262" x2="232" y2="284"/>
    <line x1="90" y1="260" x2="140" y2="290"/>
    <line x1="310" y1="120" x2="260" y2="90"/>
  </g>
  <g fill="#f5dfae">
    <circle cx="78" cy="146" r="2.5"/>
    <circle cx="130" cy="118" r="1.8"/>
    <circle cx="168" cy="96" r="2.2"/>
    <circle cx="322" cy="234" r="2.5"/>
    <circle cx="270" cy="262" r="1.8"/>
    <circle cx="232" cy="284" r="2.2"/>
    <circle cx="90" cy="260" r="2"/>
    <circle cx="140" cy="290" r="1.6"/>
    <circle cx="310" cy="120" r="2"/>
    <circle cx="260" cy="90" r="1.6"/>
    <circle cx="60" cy="80" r="1.2"/>
    <circle cx="345" cy="70" r="1.4"/>
    <circle cx="350" cy="310" r="1.2"/>
    <circle cx="55" cy="330" r="1.4"/>
  </g>

  <!-- core glow -->
  <circle cx="200" cy="190" r="70" fill="url(#core)" filter="url(#glow)"/>
  <circle cx="200" cy="190" r="52" fill="url(#core)"/>

  <!-- gentle face within the light -->
  <g stroke="#2a1d14" stroke-width="2.6" stroke-linecap="round" fill="none" opacity="0.85">
    <path d="M178 182 q6 -6 12 0"/>
    <path d="M210 182 q6 -6 12 0"/>
    <path d="M184 206 q16 12 32 0"/>
  </g>

  <!-- inner iris pattern -->
  <g fill="none" stroke="#fff3d6" stroke-width="0.8" opacity="0.5">
    <circle cx="200" cy="190" r="36"/>
    <circle cx="200" cy="190" r="44" stroke-dasharray="3 5"/>
  </g>

  <!-- lines of words drifting below -->
  <g stroke="#a9b7de" stroke-width="2" stroke-linecap="round" opacity="0.55" filter="url(#soft)">
    <line x1="120" y1="322" x2="180" y2="322"/>
    <line x1="190" y1="322" x2="230" y2="322"/>
    <line x1="240" y1="322" x2="280" y2="322"/>
    <line x1="140" y1="338" x2="200" y2="338"/>
    <line x1="210" y1="338" x2="262" y2="338"/>
    <line x1="160" y1="354" x2="240" y2="354"/>
  </g>

  <!-- soft frame -->
  <rect x="14" y="14" width="372" height="372" fill="none" stroke="#6a7bb0" stroke-width="1" opacity="0.4" rx="6"/>
</svg>