<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0d0b2e"/>
      <stop offset="0.5" stop-color="#3b1f5e"/>
      <stop offset="1" stop-color="#8a4f9e"/>
    </linearGradient>
    <radialGradient id="luna" cx="0.4" cy="0.4" r="0.8">
      <stop offset="0" stop-color="#fffbe8"/>
      <stop offset="0.7" stop-color="#ffe9a8"/>
      <stop offset="1" stop-color="#f5c96b"/>
    </radialGradient>
    <linearGradient id="roca" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5a4a7a"/>
      <stop offset="1" stop-color="#2a1f45"/>
    </linearGradient>
    <linearGradient id="tabla" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#d98c4a"/>
      <stop offset="0.5" stop-color="#f2b56b"/>
      <stop offset="1" stop-color="#d98c4a"/>
    </linearGradient>
    <linearGradient id="agua" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#9fdcf0" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#9fdcf0" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="farol" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fff6c8"/>
      <stop offset="0.4" stop-color="#ffd76b" stop-opacity="0.8"/>
      <stop offset="1" stop-color="#ffd76b" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <g fill="#fff">
    <circle cx="40" cy="50" r="1.5"/>
    <circle cx="90" cy="30" r="1"/>
    <circle cx="150" cy="60" r="1.3"/>
    <circle cx="210" cy="25" r="1"/>
    <circle cx="350" cy="45" r="1.5"/>
    <circle cx="380" cy="90" r="1"/>
    <circle cx="20" cy="120" r="1"/>
    <circle cx="310" cy="20" r="1.2"/>
    <circle cx="250" cy="70" r="0.8"/>
    <circle cx="60" cy="200" r="0.8"/>
    <circle cx="370" cy="180" r="1"/>
    <circle cx="120" cy="110" r="0.9"/>
  </g>

  <circle cx="320" cy="70" r="34" fill="url(#luna)"/>
  <circle cx="310" cy="62" r="5" fill="#e8c06a" opacity="0.6"/>
  <circle cx="330" cy="80" r="7" fill="#e8c06a" opacity="0.5"/>
  <circle cx="320" cy="70" r="44" fill="none" stroke="#ffe9a8" stroke-opacity="0.25" stroke-width="6"/>

  <!-- isla izquierda -->
  <g>
    <path d="M10 230 L110 230 L100 280 Q80 330 60 300 Q45 340 35 295 Q20 320 18 275 Z" fill="url(#roca)"/>
    <path d="M10 230 L110 230 L105 245 Q60 255 12 242 Z" fill="#6b8f5a"/>
    <path d="M10 230 Q60 218 110 230 L110 234 Q60 224 10 234 Z" fill="#8fb972"/>
    <path d="M55 300 q-4 40 2 70 q5 -35 2 -70 Z" fill="url(#agua)"/>
    <path d="M80 290 q-3 30 1 55 q4 -28 2 -55 Z" fill="url(#agua)"/>
  </g>

  <!-- isla derecha -->
  <g>
    <path d="M290 260 L392 260 L388 300 Q372 350 352 315 Q340 355 328 310 Q312 335 305 295 Z" fill="url(#roca)"/>
    <path d="M290 260 L392 260 L388 275 Q340 285 293 272 Z" fill="#6b8f5a"/>
    <path d="M290 260 Q340 248 392 260 L392 264 Q340 254 290 264 Z" fill="#8fb972"/>
    <path d="M338 315 q-3 35 2 60 q4 -30 1 -60 Z" fill="url(#agua)"/>
  </g>

  <!-- bucle imposible del puente -->
  <g fill="none" stroke-linecap="round">
    <!-- cuerdas -->
    <path d="M65 218 C120 150 160 90 210 95 C270 100 265 175 210 178 C165 180 150 130 200 118 C260 105 300 190 345 248"
          stroke="#c97a3d" stroke-width="5"/>
    <path d="M65 230 C122 165 162 104 210 109 C258 113 253 163 210 165 C177 167 166 138 203 130 C252 120 292 200 345 260"
          stroke="#c97a3d" stroke-width="5"/>
    <!-- tablones -->
    <g stroke="url(#tabla)" stroke-width="4">
      <path d="M70 216 L71 229"/>
      <path d="M84 200 L86 213"/>
      <path d="M98 184 L101 197"/>
      <path d="M113 168 L117 181"/>
      <path d="M129 152 L134 165"/>
      <path d="M146 137 L152 150"/>
      <path d="M165 122 L172 135"/>
      <path d="M186 106 L193 121"/>
      <path d="M210 95 L210 109"/>
      <path d="M234 100 L230 114"/>
      <path d="M252 115 L244 126"/>
      <path d="M262 140 L251 145"/>
      <path d="M258 165 L247 158"/>
      <path d="M232 177 L228 164"/>
      <path d="M195 175 L199 163"/>
      <path d="M172 158 L182 149"/>
      <path d="M182 128 L190 139"/>
      <path d="M212 117 L211 130"/>
      <path d="M240 113 L236 125"/>
      <path d="M266 135 L256 143"/>
      <path d="M285 160 L274 168"/>
      <path d="M302 185 L291 193"/>
      <path d="M318 210 L307 218"/>
      <path d="M332 233 L321 241"/>
      <path d="M344 250 L336 258"/>
    </g>
    <!-- barandas superiores flotantes -->
    <path d="M65 200 C120 132 162 74 212 79" stroke="#e8a55e" stroke-width="2" stroke-dasharray="6 5"/>
    <path d="M212 145 C260 137 300 175 345 232" stroke="#e8a55e" stroke-width="2" stroke-dasharray="6 5"/>
  </g>

  <!-- faroles -->
  <g>
    <circle cx="120" cy="160" r="16" fill="url(#farol)"/>
    <circle cx="120" cy="160" r="4" fill="#fff2b0"/>
    <line x1="120" y1="164" x2="121" y2="174" stroke="#8a5a2a" stroke-width="1.5"/>
    <circle cx="210" cy="86" r="18" fill="url(#farol)"/>
    <circle cx="210" cy="86" r="4.5" fill="#fff2b0"/>
    <circle cx="300" cy="195" r="16" fill="url(#farol)"/>
    <circle cx="300" cy="195" r="4" fill="#fff2b0"/>
    <line x1="300" y1="199" x2="301" y2="209" stroke="#8a5a2a" stroke-width="1.5"/>
  </g>

  <!-- peces voladores -->
  <g fill="#9fdcf0" opacity="0.85">
    <path d="M140 300 q14 -6 24 0 q-10 7 -24 0 Z"/>
    <path d="M164 300 l9 -6 l-1 6 l1 6 Z"/>
    <circle cx="146" cy="299" r="1.3" fill="#0d0b2e"/>
    <path d="M230 330 q12 -5 20 0 q-8 6 -20 0 Z"/>
    <path d="M250 330 l8 -5 l-1 5 l1 5 Z"/>
    <circle cx="235" cy="329" r="1.1" fill="#0d0b2e"/>
  </g>

  <!-- nubes bajas -->
  <g fill="#c9a8d8" opacity="0.5">
    <ellipse cx="70" cy="370" rx="55" ry="12"/>
    <ellipse cx="200" cy="385" rx="70" ry="13"/>
    <ellipse cx="340" cy="372" rx="50" ry="11"/>
  </g>

  <!-- arbolito en isla izquierda -->
  <g>
    <rect x="38" y="212" width="4" height="18" fill="#6b4a2a"/>
    <circle cx="40" cy="206" r="11" fill="#7fae5f"/>
    <circle cx="33" cy="212" r="7" fill="#6b9e4f"/>
    <circle cx="48" cy="211" r="7" fill="#6b9e4f"/>
  </g>
  <!-- farolito en isla derecha -->
  <g>
    <rect x="368" y="234" width="3" height="26" fill="#3a2a1a"/>
    <circle cx="369.5" cy="230" r="10" fill="url(#farol)"/>
    <circle cx="369.5" cy="230" r="3.5" fill="#fff2b0"/>
  </g>
</svg>