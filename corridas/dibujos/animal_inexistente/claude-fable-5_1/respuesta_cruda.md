<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="cielo" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#2b1e4f"/>
      <stop offset="100%" stop-color="#0d0a24"/>
    </radialGradient>
    <linearGradient id="cuerpo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#7de3c8"/>
      <stop offset="100%" stop-color="#3a9e94"/>
    </linearGradient>
    <linearGradient id="panza" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#eafff5"/>
      <stop offset="100%" stop-color="#bfe8d8"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd166" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#ffd166" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ala" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#c77dff" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#7b2cbf" stop-opacity="0.6"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#cielo)"/>

  <circle cx="60" cy="60" r="2" fill="#fff" opacity="0.8"/>
  <circle cx="120" cy="40" r="1.5" fill="#fff" opacity="0.6"/>
  <circle cx="330" cy="70" r="2" fill="#fff" opacity="0.7"/>
  <circle cx="290" cy="35" r="1.5" fill="#fff" opacity="0.5"/>
  <circle cx="370" cy="130" r="1.5" fill="#fff" opacity="0.6"/>
  <circle cx="40" cy="150" r="1.5" fill="#fff" opacity="0.5"/>
  <circle cx="200" cy="30" r="2" fill="#fff" opacity="0.7"/>

  <ellipse cx="200" cy="360" rx="150" ry="25" fill="#1a1440"/>
  <ellipse cx="200" cy="355" rx="110" ry="15" fill="#241a55"/>

  <!-- cola espiral -->
  <path d="M275 280 Q340 290 345 250 Q350 215 315 218 Q290 220 295 245 Q298 262 318 255"
        fill="none" stroke="#3a9e94" stroke-width="14" stroke-linecap="round"/>
  <circle cx="318" cy="252" r="9" fill="url(#glow)"/>
  <circle cx="318" cy="252" r="5" fill="#ffd166"/>

  <!-- patas traseras -->
  <path d="M245 320 Q248 350 240 358 L268 358 Q262 345 264 318 Z" fill="#33887e"/>
  <ellipse cx="253" cy="358" rx="20" ry="8" fill="#2a6f68"/>

  <!-- alas de libélula -->
  <g opacity="0.9">
    <path d="M195 190 Q90 110 55 150 Q80 195 190 205 Z" fill="url(#ala)" stroke="#e0aaff" stroke-width="2"/>
    <path d="M200 195 Q120 70 85 95 Q95 150 198 208 Z" fill="url(#ala)" stroke="#e0aaff" stroke-width="2" opacity="0.8"/>
    <path d="M195 200 Q150 130 110 130 Q130 180 195 212" fill="none" stroke="#e0aaff" stroke-width="1" opacity="0.6"/>
  </g>

  <!-- cuerpo -->
  <ellipse cx="205" cy="270" rx="85" ry="65" fill="url(#cuerpo)"/>
  <ellipse cx="195" cy="290" rx="55" ry="40" fill="url(#panza)"/>

  <!-- manchas -->
  <circle cx="255" cy="245" r="10" fill="#2f857c" opacity="0.7"/>
  <circle cx="270" cy="275" r="7" fill="#2f857c" opacity="0.7"/>
  <circle cx="240" cy="220" r="6" fill="#2f857c" opacity="0.7"/>

  <!-- pata delantera -->
  <path d="M175 320 Q172 350 165 358 L195 358 Q190 345 192 320 Z" fill="#46b3a5"/>
  <ellipse cx="180" cy="358" rx="20" ry="8" fill="#37978a"/>

  <!-- cuello y cabeza -->
  <path d="M160 240 Q140 180 150 140 Q155 115 180 118 Q200 122 195 160 Q190 205 210 235 Z" fill="url(#cuerpo)"/>
  <circle cx="165" cy="125" r="48" fill="url(#cuerpo)"/>

  <!-- orejas-antena -->
  <path d="M135 90 Q110 45 95 40" fill="none" stroke="#46b3a5" stroke-width="7" stroke-linecap="round"/>
  <circle cx="93" cy="38" r="12" fill="url(#glow)"/>
  <circle cx="93" cy="38" r="6" fill="#ffd166"/>
  <path d="M190 85 Q210 40 228 32" fill="none" stroke="#46b3a5" stroke-width="7" stroke-linecap="round"/>
  <circle cx="230" cy="30" r="12" fill="url(#glow)"/>
  <circle cx="230" cy="30" r="6" fill="#ffd166"/>

  <!-- hocico -->
  <ellipse cx="130" cy="145" rx="30" ry="22" fill="url(#panza)"/>
  <ellipse cx="112" cy="140" rx="7" ry="5" fill="#2a6f68"/>
  <path d="M118 158 Q130 168 145 160" fill="none" stroke="#2a6f68" stroke-width="3" stroke-linecap="round"/>

  <!-- ojos: tres -->
  <g>
    <circle cx="160" cy="112" r="14" fill="#fff"/>
    <circle cx="157" cy="114" r="7" fill="#1a1440"/>
    <circle cx="154" cy="111" r="2.5" fill="#fff"/>
  </g>
  <g>
    <circle cx="195" cy="118" r="11" fill="#fff"/>
    <circle cx="192" cy="120" r="5.5" fill="#1a1440"/>
    <circle cx="190" cy="117" r="2" fill="#fff"/>
  </g>
  <g>
    <circle cx="177" cy="90" r="8" fill="#fff"/>
    <circle cx="176" cy="91" r="4" fill="#1a1440"/>
    <circle cx="174.5" cy="89.5" r="1.5" fill="#fff"/>
  </g>

  <!-- mejilla -->
  <circle cx="140" cy="130" r="8" fill="#ff8fa3" opacity="0.5"/>

  <!-- púas suaves en el lomo -->
  <path d="M210 210 Q215 195 225 205 Q230 190 242 202 Q250 192 258 208 Q268 200 272 218"
        fill="none" stroke="#c77dff" stroke-width="5" stroke-linecap="round"/>

  <!-- lucecitas flotando -->
  <circle cx="90" cy="230" r="6" fill="url(#glow)"/>
  <circle cx="90" cy="230" r="2.5" fill="#ffd166"/>
  <circle cx="320" cy="150" r="6" fill="url(#glow)"/>
  <circle cx="320" cy="150" r="2.5" fill="#ffd166"/>
  <circle cx="60" cy="310" r="5" fill="url(#glow)"/>
  <circle cx="60" cy="310" r="2" fill="#ffd166"/>
</svg>