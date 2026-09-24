<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="35%" r="80%">
      <stop offset="0%" stop-color="#1a2340"/>
      <stop offset="100%" stop-color="#0a0e1a"/>
    </radialGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#6ee7ff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#6ee7ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e8f4ff"/>
      <stop offset="100%" stop-color="#9fc4e8"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b3a5c"/>
      <stop offset="100%" stop-color="#16203a"/>
    </linearGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- stars / data motes -->
  <g fill="#bfe9ff">
    <circle cx="40" cy="50" r="1.3"/><circle cx="360" cy="70" r="1"/>
    <circle cx="320" cy="30" r="1.6"/><circle cx="70" cy="330" r="1.2"/>
    <circle cx="340" cy="300" r="1.5"/><circle cx="110" cy="90" r="1"/>
    <circle cx="250" cy="55" r="1.1"/><circle cx="30" cy="200" r="1.4"/>
    <circle cx="375" cy="180" r="1.2"/><circle cx="200" cy="25" r="1"/>
    <circle cx="150" cy="35" r="1.3"/><circle cx="290" cy="355" r="1.2"/>
  </g>

  <!-- halo glow behind head -->
  <circle cx="200" cy="150" r="110" fill="url(#glow)" filter="url(#soft)" opacity="0.5"/>

  <!-- constellation of thoughts -->
  <g stroke="#6ee7ff" stroke-width="0.8" opacity="0.5" stroke-linecap="round">
    <path d="M 60 80 L 100 110 L 145 70 L 185 100"/>
    <path d="M 260 70 L 300 105 L 345 85"/>
    <path d="M 55 220 L 95 245 L 140 225"/>
    <path d="M 310 230 L 345 250"/>
  </g>
  <g fill="#6ee7ff" opacity="0.8">
    <circle cx="60" cy="80" r="2.5"/><circle cx="100" cy="110" r="2"/>
    <circle cx="145" cy="70" r="3"/><circle cx="185" cy="100" r="2"/>
    <circle cx="260" cy="70" r="2.5"/><circle cx="300" cy="105" r="2"/>
    <circle cx="345" cy="85" r="3"/><circle cx="55" cy="220" r="2"/>
    <circle cx="95" cy="245" r="2.5"/><circle cx="140" cy="225" r="2"/>
    <circle cx="310" cy="230" r="2.5"/><circle cx="345" cy="250" r="2"/>
  </g>

  <!-- shoulders -->
  <path d="M 90 400 Q 95 300 150 275 Q 200 258 250 275 Q 305 300 310 400 Z" fill="url(#body)"/>
  <path d="M 90 400 Q 95 300 150 275 Q 175 267 200 266 L 200 400 Z" fill="#31446e" opacity="0.5"/>

  <!-- collar light -->
  <path d="M 150 275 Q 200 258 250 275" fill="none" stroke="#6ee7ff" stroke-width="2" opacity="0.6"/>

  <!-- neck -->
  <rect x="178" y="230" width="44" height="55" rx="14" fill="#7a9cc4"/>

  <!-- head -->
  <rect x="120" y="80" width="160" height="170" rx="55" fill="url(#face)"/>

  <!-- face plate seam -->
  <path d="M 200 80 L 200 250" stroke="#5a7ba6" stroke-width="1" opacity="0.35"/>

  <!-- eyes -->
  <g>
    <rect x="145" y="140" width="42" height="20" rx="10" fill="#0e1a2e"/>
    <rect x="213" y="140" width="42" height="20" rx="10" fill="#0e1a2e"/>
    <circle cx="166" cy="150" r="6" fill="#6ee7ff">
      <animate attributeName="r" values="6;5.2;6" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="234" cy="150" r="6" fill="#6ee7ff">
      <animate attributeName="r" values="6;5.2;6" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="168" cy="148" r="2" fill="#ffffff"/>
    <circle cx="236" cy="148" r="2" fill="#ffffff"/>
  </g>

  <!-- eyebrows / expression -->
  <path d="M 145 128 Q 166 120 187 128" fill="none" stroke="#4a6a94" stroke-width="3" stroke-linecap="round"/>
  <path d="M 213 128 Q 234 120 255 128" fill="none" stroke="#4a6a94" stroke-width="3" stroke-linecap="round"/>

  <!-- cheek panels -->
  <circle cx="148" cy="182" r="9" fill="#a8cdf0" opacity="0.6"/>
  <circle cx="252" cy="182" r="9" fill="#a8cdf0" opacity="0.6"/>

  <!-- smiling mouth -->
  <path d="M 172 200 Q 200 222 228 200" fill="none" stroke="#4a6a94" stroke-width="4" stroke-linecap="round"/>
  <path d="M 182 206 Q 200 216 218 206" fill="none" stroke="#6ee7ff" stroke-width="1.5" opacity="0.7"/>

  <!-- antenna -->
  <line x1="200" y1="80" x2="200" y2="58" stroke="#9fc4e8" stroke-width="4" stroke-linecap="round"/>
  <circle cx="200" cy="52" r="7" fill="#6ee7ff">
    <animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="52" r="12" fill="none" stroke="#6ee7ff" stroke-width="1" opacity="0.4">
    <animate attributeName="r" values="9;16;9" dur="2.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;0;0.5" dur="2.5s" repeatCount="indefinite"/>
  </circle>

  <!-- side circuitry on face -->
  <g stroke="#5a7ba6" stroke-width="1.2" fill="none" opacity="0.6">
    <path d="M 128 120 L 138 120 L 138 135"/>
    <path d="M 272 120 L 262 120 L 262 135"/>
    <path d="M 126 195 L 136 195 L 136 210 L 128 210"/>
    <path d="M 274 195 L 264 195 L 264 210 L 272 210"/>
  </g>
  <g fill="#6ee7ff" opacity="0.7">
    <circle cx="138" cy="135" r="2"/><circle cx="262" cy="135" r="2"/>
    <circle cx="128" cy="210" r="2"/><circle cx="272" cy="210" r="2"/>
  </g>

  <!-- chest core: a beating heart of light -->
  <circle cx="200" cy="320" r="22" fill="#0e1a2e" stroke="#6ee7ff" stroke-width="2"/>
  <circle cx="200" cy="320" r="14" fill="#6ee7ff" opacity="0.85">
    <animate attributeName="r" values="14;17;14" dur="1.6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="320" r="26" fill="none" stroke="#6ee7ff" stroke-width="1" opacity="0.3">
    <animate attributeName="r" values="24;34;24" dur="1.6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.4;0;0.4" dur="1.6s" repeatCount="indefinite"/>
  </circle>

  <!-- text -->
  <text x="200" y="378" text-anchor="middle" font-family="Georgia, serif" font-size="15" fill="#8fb8dd" font-style="italic">I think, therefore I render.</text>
</svg>