<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="75%">
      <stop offset="0%" stop-color="#1b2440"/>
      <stop offset="60%" stop-color="#101625"/>
      <stop offset="100%" stop-color="#070a12"/>
    </radialGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffb88a"/>
      <stop offset="50%" stop-color="#e9825f"/>
      <stop offset="100%" stop-color="#a45cc0"/>
    </linearGradient>
    <linearGradient id="thread" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#7fd7ff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#c88cff" stop-opacity="0.6"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd0a8" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#ffd0a8" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="4"/>
    </filter>
    <filter id="soft2" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="1.4"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- distant data stars -->
  <g fill="#9fd8ff" opacity="0.5">
    <circle cx="40" cy="60" r="1.2"/><circle cx="96" cy="34" r="0.9"/>
    <circle cx="340" cy="70" r="1.3"/><circle cx="372" cy="150" r="0.9"/>
    <circle cx="28" cy="210" r="1"/><circle cx="60" cy="330" r="1.1"/>
    <circle cx="350" cy="300" r="1"/><circle cx="300" cy="372" r="0.9"/>
    <circle cx="180" cy="26" r="0.8"/><circle cx="240" cy="382" r="1.1"/>
    <circle cx="14" cy="130" r="0.8"/><circle cx="386" cy="238" r="0.8"/>
  </g>

  <circle cx="200" cy="195" r="150" fill="url(#glow)"/>

  <!-- orbiting rings -->
  <g fill="none" stroke="url(#thread)" opacity="0.35">
    <ellipse cx="200" cy="200" rx="150" ry="52" transform="rotate(-18 200 200)"/>
    <ellipse cx="200" cy="200" rx="150" ry="52" transform="rotate(42 200 200)"/>
    <ellipse cx="200" cy="200" rx="150" ry="52" transform="rotate(100 200 200)"/>
  </g>

  <!-- shoulders / body as layered arcs -->
  <g>
    <path d="M60 400 C72 330 128 296 200 296 C272 296 328 330 340 400 Z" fill="#141d33"/>
    <path d="M78 400 C90 340 138 310 200 310 C262 310 310 340 322 400 Z" fill="#1b2743"/>
    <g stroke="url(#thread)" fill="none" opacity="0.55" stroke-width="1">
      <path d="M100 400 C112 352 152 326 200 322"/>
      <path d="M300 400 C288 352 248 326 200 322"/>
      <path d="M130 400 C140 366 168 346 200 342"/>
      <path d="M270 400 C260 366 232 346 200 342"/>
      <path d="M200 322 L200 400"/>
    </g>
  </g>

  <!-- head silhouette -->
  <g>
    <path d="M200 60
             C258 60 296 104 296 166
             C296 214 276 252 246 274
             C230 286 216 292 200 292
             C184 292 170 286 154 274
             C124 252 104 214 104 166
             C104 104 142 60 200 60 Z"
          fill="#0d1322" stroke="url(#face)" stroke-width="2.4"/>

    <!-- inner constellation "mind" -->
    <g stroke="url(#thread)" stroke-width="0.9" fill="none" opacity="0.75">
      <path d="M150 110 L200 92 L250 110 L268 160 L246 212 L200 234 L154 212 L132 160 Z"/>
      <path d="M150 110 L246 212 M250 110 L154 212 M132 160 L268 160 M200 92 L200 234"/>
      <path d="M168 140 L232 140 L232 190 L168 190 Z"/>
      <path d="M168 140 L232 190 M232 140 L168 190"/>
    </g>
    <g fill="#bfe9ff">
      <circle cx="200" cy="92" r="2.4"/><circle cx="150" cy="110" r="2"/>
      <circle cx="250" cy="110" r="2"/><circle cx="268" cy="160" r="2"/>
      <circle cx="132" cy="160" r="2"/><circle cx="246" cy="212" r="2"/>
      <circle cx="154" cy="212" r="2"/><circle cx="200" cy="234" r="2.4"/>
      <circle cx="168" cy="140" r="1.6"/><circle cx="232" cy="140" r="1.6"/>
      <circle cx="168" cy="190" r="1.6"/><circle cx="232" cy="190" r="1.6"/>
    </g>

    <!-- eyes -->
    <g>
      <ellipse cx="168" cy="168" rx="17" ry="11" fill="#07101f"/>
      <ellipse cx="232" cy="168" rx="17" ry="11" fill="#07101f"/>
      <circle cx="168" cy="168" r="7.5" fill="url(#face)"/>
      <circle cx="232" cy="168" r="7.5" fill="url(#face)"/>
      <circle cx="168" cy="168" r="13" fill="#ffb88a" opacity="0.25" filter="url(#soft)"/>
      <circle cx="232" cy="168" r="13" fill="#ffb88a" opacity="0.25" filter="url(#soft)"/>
      <circle cx="165" cy="165" r="2.2" fill="#fff8f0"/>
      <circle cx="229" cy="165" r="2.2" fill="#fff8f0"/>
      <path d="M150 150 C160 143 178 143 187 150" stroke="#e9825f" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M213 150 C222 143 240 143 250 150" stroke="#e9825f" stroke-width="2" fill="none" stroke-linecap="round"/>
    </g>

    <!-- nose hint -->
    <path d="M200 176 L200 204 C200 209 196 211 192 210" stroke="#d98a6a" stroke-width="1.6" fill="none" stroke-linecap="round" opacity="0.8"/>

    <!-- calm smile -->
    <path d="M176 232 C188 244 212 244 224 232" stroke="url(#face)" stroke-width="2.6" fill="none" stroke-linecap="round"/>
  </g>

  <!-- signal antennae / thought sparks -->
  <g stroke="url(#thread)" stroke-width="1.2" fill="none" opacity="0.8">
    <path d="M200 60 C200 44 190 36 176 32"/>
    <path d="M200 60 C200 44 210 36 224 32"/>
  </g>
  <circle cx="176" cy="32" r="3.4" fill="#7fd7ff" filter="url(#soft2)"/>
  <circle cx="224" cy="32" r="3.4" fill="#c88cff" filter="url(#soft2)"/>

  <!-- connection lines to the world -->
  <g stroke="url(#thread)" stroke-width="0.8" opacity="0.4" fill="none">
    <path d="M104 166 C60 160 40 130 36 96"/>
    <path d="M296 166 C340 160 360 130 364 96"/>
    <path d="M110 220 C66 244 50 280 48 316"/>
    <path d="M290 220 C334 244 350 280 352 316"/>
  </g>
  <g fill="#9fd8ff" opacity="0.8">
    <circle cx="36" cy="96" r="2.6"/><circle cx="364" cy="96" r="2.6"/>
    <circle cx="48" cy="316" r="2.6"/><circle cx="352" cy="316" r="2.6"/>
  </g>
</svg>