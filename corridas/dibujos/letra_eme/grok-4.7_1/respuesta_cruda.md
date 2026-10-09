<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#2b2342"/>
      <stop offset="100%" stop-color="#100d16"/>
    </radialGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff8e8"/>
      <stop offset="52%" stop-color="#f0d7a4"/>
      <stop offset="100%" stop-color="#c9a36a"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffb199"/>
      <stop offset="100%" stop-color="#d4533c"/>
    </linearGradient>
    <filter id="soft" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4.5" result="b"/>
      <feOffset dy="3" result="o"/>
      <feFlood flood-color="#000" flood-opacity="0.42" result="c"/>
      <feComposite in="c" in2="o" operator="in" result="s"/>
      <feMerge>
        <feMergeNode in="s"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="200" r="174" fill="none" stroke="#3d3158" stroke-width="1.25"/>
  <circle cx="200" cy="200" r="163" fill="none" stroke="#2a2340" stroke-width="0.75"/>
  <g filter="url(#soft)">
    <path fill="url(#ink)" d="M100 286 L100 160 C100 108 132 88 158 100 C182 112 178 148 176 170 L176 286 L154 286 L154 170 C154 146 150 124 138 120 C122 116 122 144 122 164 L122 286 Z"/>
    <path fill="url(#ink)" d="M300 286 L300 160 C300 108 268 88 242 100 C218 112 222 148 224 170 L224 286 L246 286 L246 170 C246 146 250 124 262 120 C278 116 278 144 278 164 L278 286 Z"/>
    <rect x="192" y="198" width="16" height="90" rx="8" fill="url(#ink)"/>
    <rect x="84" y="272" width="232" height="30" rx="15" fill="url(#ink)"/>
    <circle cx="200" cy="72" r="11" fill="url(#ink)"/>
    <line x1="118" y1="287" x2="282" y2="287" stroke="#6a4e2c" stroke-width="2.25" stroke-linecap="round" opacity="0.55"/>
  </g>
  <path d="M172 54 Q200 22 228 54" fill="none" stroke="url(#accent)" stroke-width="6" stroke-linecap="round"/>
  <g fill="#6a5a88">
    <circle cx="200" cy="22" r="2.2"/>
    <circle cx="200" cy="378" r="2.2"/>
    <circle cx="22" cy="200" r="2.2"/>
    <circle cx="378" cy="200" r="2.2"/>
  </g>
</svg>