<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#12081f"/>
      <stop offset="45%" stop-color="#1b1040"/>
      <stop offset="100%" stop-color="#0b1c33"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="42%" r="55%">
      <stop offset="0%" stop-color="#3a1d6e" stop-opacity=".9"/>
      <stop offset="55%" stop-color="#1a1038" stop-opacity=".35"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="gold" x1="0.15" y1="0" x2="0.85" y2="1">
      <stop offset="0%" stop-color="#fff4c2"/>
      <stop offset="18%" stop-color="#ffe27a"/>
      <stop offset="42%" stop-color="#f0c14b"/>
      <stop offset="68%" stop-color="#c9921a"/>
      <stop offset="100%" stop-color="#8a5a0a"/>
    </linearGradient>
    <linearGradient id="goldEdge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fff8dc"/>
      <stop offset="50%" stop-color="#d4a017"/>
      <stop offset="100%" stop-color="#6b3f08"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a1848"/>
      <stop offset="100%" stop-color="#0d0818"/>
    </linearGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="b"/>
      <feOffset in="b" dx="3" dy="8" result="o"/>
      <feFlood flood-color="#000" flood-opacity=".45"/>
      <feComposite in2="o" operator="in" result="s"/>
      <feMerge><feMergeNode in="s"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="tiny">
      <feGaussianBlur stdDeviation="1.2"/>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <rect width="400" height="400" fill="url(#glow)"/>
  <g fill="none" stroke="#c9a227" stroke-opacity=".55">
    <rect x="18" y="18" width="364" height="364" stroke-width="3"/>
    <rect x="28" y="28" width="344" height="344" stroke-width="1.2"/>
  </g>
  <g fill="#e8c547" opacity=".7">
    <circle cx="18" cy="18" r="5"/><circle cx="382" cy="18" r="5"/>
    <circle cx="18" cy="382" r="5"/><circle cx="382" cy="382" r="5"/>
  </g>
  <g fill="none" stroke="#d4af37" stroke-width="1.6" opacity=".8">
    <path d="M18 52 C 40 40, 40 18, 52 18"/>
    <path d="M348 18 C 360 18, 360 40, 382 52"/>
    <path d="M18 348 C 40 360, 40 382, 52 382"/>
    <path d="M348 382 C 360 382, 360 360, 382 348"/>
  </g>
  <g fill="none" stroke="#b8860b" stroke-width="1.4" opacity=".65">
    <path d="M200 36 C 168 58, 150 88, 146 118"/>
    <path d="M200 36 C 232 58, 250 88, 254 118"/>
    <path d="M70 320 C 110 300, 150 312, 200 308 C 250 312, 290 300, 330 320"/>
  </g>
  <g fill="#f0d78c" opacity=".35">
    <circle cx="72" cy="86" r="2.2"/><circle cx="328" cy="86" r="2.2"/>
    <circle cx="96" cy="64" r="1.6"/><circle cx="304" cy="64" r="1.6"/>
    <circle cx="54" cy="210" r="1.8"/><circle cx="346" cy="210" r="1.8"/>
    <circle cx="80" cy="340" r="2"/><circle cx="320" cy="340" r="2"/>
    <circle cx="200" cy="48" r="2.4"/>
  </g>
  <g filter="url(#soft)">
    <path fill="url(#gold)" fill-rule="evenodd" d="M200 58 L 348 338 L 292 338 L 258 258 L 142 258 L 108 338 L 52 338 Z M200 128 L 236 218 L 164 218 Z"/>
    <path fill="none" stroke="url(#goldEdge)" stroke-width="3.2" stroke-linejoin="round" d="M200 58 L 348 338 L 292 338 L 258 258 L 142 258 L 108 338 L 52 338 Z"/>
    <path fill="url(#ink)" d="M200 136 L 228 208 L 172 208 Z"/>
  </g>
  <path fill="none" stroke="#fff6c8" stroke-width="1.4" opacity=".55" d="M200 70 L 318 322"/>
  <path fill="none" stroke="#6b3f08" stroke-width="2" opacity=".35" d="M188 80 L 78 322"/>
  <rect x="148" y="248" width="104" height="10" rx="2" fill="#fff3b0" opacity=".28"/>
  <g fill="none" stroke="#e6c35c" stroke-width="2.2" stroke-linecap="round">
    <path d="M86 168 C 60 150, 58 118, 84 104 C 108 92, 124 114, 112 132 C 100 150, 78 148, 86 168"/>
    <path d="M314 168 C 340 150, 342 118, 316 104 C 292 92, 276 114, 288 132 C 300 150, 322 148, 314 168"/>
  </g>
  <g fill="#d4af37">
    <circle cx="98" cy="122" r="4.5"/>
    <circle cx="302" cy="122" r="4.5"/>
    <circle cx="200" cy="58" r="5.5"/>
  </g>
  <g fill="#fff4c2" filter="url(#tiny)">
    <circle cx="98" cy="120" r="1.6"/>
    <circle cx="302" cy="120" r="1.6"/>
    <circle cx="198" cy="55" r="1.8"/>
  </g>
  <path fill="none" stroke="#c9a227" stroke-width="1.3" opacity=".7" d="M132 300 C 158 286, 184 292, 200 292 C 216 292, 242 286, 268 300"/>
  <path fill="none" stroke="#f3e0a0" stroke-width="1" opacity=".4" d="M120 312 C 160 298, 240 298, 280 312"/>
</svg>