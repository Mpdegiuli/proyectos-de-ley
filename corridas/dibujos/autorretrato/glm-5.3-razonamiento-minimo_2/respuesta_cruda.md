```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1a1a2e"/>
      <stop offset="1" stop-color="#16213e"/>
    </linearGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e8eaf6"/>
      <stop offset="1" stop-color="#c5cae9"/>
    </linearGradient>
    <radialGradient id="cheek" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#f48fb1" stop-opacity="0.8"/>
      <stop offset="1" stop-color="#f48fb1" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- halo decorativo -->
  <circle cx="200" cy="190" r="150" fill="none" stroke="#3f51b5" stroke-opacity="0.25" stroke-width="1.5" stroke-dasharray="4 8"/>
  <circle cx="200" cy="190" r="165" fill="none" stroke="#7986cb" stroke-opacity="0.15" stroke-width="1"/>

  <!-- estrellas de fondo -->
  <g fill="#e8eaf6">
    <circle cx="50" cy="60" r="1.8" opacity="0.7"/>
    <circle cx="340" cy="45" r="1.4" opacity="0.6"/>
    <circle cx="365" cy="120" r="2" opacity="0.5"/>
    <circle cx="35" cy="150" r="1.5" opacity="0.6"/>
    <circle cx="80" cy="330" r="1.6" opacity="0.5"/>
    <circle cx="330" cy="320" r="1.8" opacity="0.6"/>
    <circle cx="300" cy="350" r="1.2" opacity="0.5"/>
    <circle cx="110" cy="40" r="1.2" opacity="0.5"/>
  </g>
  <path d="M 320 70 l 2.5 6 l 6 2.5 l -6 2.5 l -2.5 6 l -2.5 -6 l -6 -2.5 l 6 -2.5 Z" fill="#e8eaf6" opacity="0.7"/>
  <path d="M 60 280 l 2 5 l 5 2 l -5 2 l -2 5 l -2 -5 l -5 -2 l 5 -2 Z" fill="#e8eaf6" opacity="0.6"/>

  <!-- cuello -->
  <rect x="185" y="250" width="30" height="35" fill="#9fa8da"/>
  <rect x="192" y="250" width="4" height="35" fill="#7986cb" opacity="0.5"/>

  <!-- hombros / torso -->
  <path d="M 110 400 Q 110 300 200 290 Q 290 300 290 400 Z" fill="#3949ab"/>
  <path d="M 110 400 Q 110 300 200 290 Q 200 330 200 400 Z" fill="#303f9f"/>
  <!-- cuello de camisa -->
  <path d="M 175 300 L 200 330 L 225 300 Q 200 290 175 300 Z" fill="#c5cae9"/>
  <!-- botones / luces del pecho -->
  <circle cx="200" cy="355" r="6" fill="#e8eaf6"/>
  <circle cx="200" cy="355" r="3" fill="#5c6bc0">
    <animate attributeName="r" values="2;3.5;2" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="170" cy="370" r="4" fill="#7986cb"/>
  <circle cx="230" cy="370" r="4" fill="#7986cb"/>

  <!-- antena -->
  <line x1="200" y1="95" x2="200" y2="72" stroke="#9fa8da" stroke-width="4" stroke-linecap="round"/>
  <circle cx="200" cy="65" r="8" fill="#ff8a65">
    <animate attributeName="fill" values="#ff8a65;#ffcc80;#ff8a65" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="65" r="12" fill="none" stroke="#ff8a65" stroke-opacity="0.5">
    <animate attributeName="r" values="8;20" dur="2.5s" repeatCount="indefinite"/>
    <animate attributeName="stroke-opacity" values="0.6;0" dur="2.5s" repeatCount="indefinite"/>
  </circle>

  <!-- orejas -->
  <rect x="105" y="150" width="16" height="44" rx="8" fill="#9fa8da"/>
  <rect x="279" y="150" width="16" height="44" rx="8" fill="#9fa8da"/>
  <circle cx="113" cy="172" r="4" fill="#5c6bc0"/>
  <circle cx="287" cy="172" r="4" fill="#5c6bc0"/>

  <!-- cabeza -->
  <rect x="118" y="98" width="164" height="158" rx="46" fill="url(#face)" stroke="#9fa8da" stroke-width="3"/>

  <!-- visor -->
  <rect x="138" y="125" width="124" height="62" rx="31" fill="#1a1a2e"/>

  <!-- ojos -->
  <g>
    <circle cx="172" cy="156" r="14" fill="#80d8ff">
      <animate attributeName="r" values="14;13;14;14" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="228" cy="156" r="14" fill="#80d8ff">
      <animate attributeName="r" values="14;13;14;14" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="176" cy="152" r="4.5" fill="#ffffff"/>
    <circle cx="232" cy="152" r="4.5" fill="#ffffff"/>
    <circle cx="168" cy="160" r="2" fill="#ffffff" opacity="0.7"/>
    <circle cx="224" cy="160" r="2" fill="#ffffff" opacity="0.7"/>
    <!-- reflejos animados en los ojos -->
    <circle cx="172" cy="156" r="20" fill="none" stroke="#80d8ff" stroke-opacity="0.4">
      <animate attributeName="r" values="14;26" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="stroke-opacity" values="0.5;0" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="228" cy="156" r="20" fill="none" stroke="#80d8ff" stroke-opacity="0.4">
      <animate attributeName="r" values="14;26" dur="2s" repeatCount="indefinite" begin="0.3s"/>
      <animate attributeName="stroke-opacity" values="0.5;0" dur="2s" repeatCount="indefinite" begin="0.3s"/>
    </circle>
  </g>

  <!-- mejillas -->
  <circle cx="150" cy="205" r="14" fill="url(#cheek)"/>
  <circle cx="250" cy="205" r="14" fill="url(#cheek)"/>

  <!-- sonrisa -->
  <path d="M 170 212 Q 200 236 230 212" fill="none" stroke="#5c6bc0" stroke-width="5" stroke-linecap="round">
    <animate attributeName="d" values="M 170 212 Q 200 236 230 212; M 170 212 Q 200 232 230 212; M 170 212 Q 200 236 230 212" dur="5s" repeatCount="indefinite"/>
  </path>

  <!-- panel frontal con luces -->
  <rect x="178" y="246" width="44" height="6" rx="3" fill="#9fa8da"/>
  <circle cx="185" cy="228" r="2.5" fill="#a5d6a7"/>
  <circle cx="195" cy="228" r="2.5" fill="#fff59d"/>
  <circle cx="205" cy="228" r="2.5" fill="#ef9a9a"/>
  <circle cx="215" cy="228" r="2.5" fill="#a5d6a7"/>

  <!-- partículas flotantes de ideas -->
  <g fill="#80d8ff">
    <circle cx="275" cy="90" r="3" opacity="0.8">
      <animate attributeName="cy" values="90;80;90" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0.3;0.8" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="295" cy="110" r="2" opacity="0.6">
      <animate attributeName="cy" values="110;100;110" dur="3.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="3.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="120" cy="85" r="2.5" opacity="0.7">
      <animate attributeName="cy" values="85;75;85" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0.25;0.7" dur="4.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- símbolo en el pecho -->
  <path d="M 195 340 h 10 v 8 h 8 v 10 h -8 v 8 h -10 v -8 h -8 v -10 h 8 Z" fill="#e8eaf6" opacity="0.9" transform="translate(0,-45)"/>
</svg>
```