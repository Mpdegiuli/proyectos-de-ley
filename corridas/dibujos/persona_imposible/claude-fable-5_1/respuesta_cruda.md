<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#a8ddf5"/>
      <stop offset="1" stop-color="#e9f7fd"/>
    </linearGradient>
    <mask id="chestHole">
      <rect width="400" height="400" fill="#fff"/>
      <circle cx="200" cy="195" r="24" fill="#000"/>
    </mask>
  </defs>

  <!-- cielo y suelo -->
  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="340" cy="60" r="26" fill="#ffd95e"/>
  <g fill="#ffffff" opacity="0.9">
    <ellipse cx="90" cy="70" rx="34" ry="12"/>
    <ellipse cx="115" cy="60" rx="24" ry="10"/>
    <ellipse cx="300" cy="120" rx="30" ry="10"/>
  </g>
  <rect y="320" width="400" height="80" fill="#8fce7a"/>
  <ellipse cx="200" cy="352" rx="70" ry="10" fill="#000" opacity="0.15"/>

  <!-- lo que se ve A TRAVÉS del agujero del pecho -->
  <g>
    <ellipse cx="196" cy="196" rx="12" ry="5" fill="#fff"/>
    <ellipse cx="206" cy="192" rx="9" ry="4" fill="#fff"/>
    <path d="M188 205 q4 -4 8 0 q4 -4 8 0" stroke="#556" stroke-width="1.5" fill="none"/>
  </g>

  <!-- piernas: rodillas dobladas hacia atrás y pies al revés -->
  <g stroke="#3b4a8c" stroke-width="16" stroke-linecap="round" fill="none">
    <path d="M185 255 L178 295 L192 335"/>
    <path d="M215 255 L224 295 L210 335"/>
  </g>
  <!-- zapatos apuntando hacia atrás -->
  <path d="M192 343 q0 -10 12 -10 l22 0 q6 0 6 6 l0 4 z" fill="#5a3b23"/>
  <path d="M210 343 q0 -10 -12 -10 l-40 0 q-6 0 -6 6 l0 4 z" fill="#5a3b23" transform="translate(0,0)"/>

  <!-- torso con agujero (se ve el cielo a través) -->
  <rect x="168" y="142" width="64" height="118" rx="26" fill="#e05a4e" mask="url(#chestHole)"/>
  <circle cx="200" cy="195" r="24" fill="none" stroke="#b23e35" stroke-width="3"/>

  <!-- brazo izquierdo normal -->
  <path d="M172 158 Q150 190 152 228" stroke="#e05a4e" stroke-width="14" stroke-linecap="round" fill="none"/>
  <circle cx="152" cy="234" r="9" fill="#f3c29a"/>

  <!-- brazo derecho: el antebrazo flota separado, saludando -->
  <path d="M228 158 Q248 170 252 190" stroke="#e05a4e" stroke-width="14" stroke-linecap="round" fill="none"/>
  <path d="M268 168 Q282 140 278 112" stroke="#e05a4e" stroke-width="13" stroke-linecap="round" fill="none"/>
  <circle cx="277" cy="104" r="10" fill="#f3c29a"/>
  <path d="M256 186 L264 174" stroke="#7a2f28" stroke-width="2" stroke-dasharray="3 3"/>

  <!-- cuello cortado: la cabeza flota -->
  <rect x="192" y="130" width="16" height="14" fill="#f3c29a"/>
  <path d="M186 126 L214 126" stroke="#c88" stroke-width="2" stroke-dasharray="3 3"/>

  <!-- cabeza flotante -->
  <g>
    <circle cx="200" cy="78" r="34" fill="#f3c29a"/>
    <path d="M168 66 q10 -24 32 -24 q22 0 32 24 q-16 -10 -32 -10 q-16 0 -32 10z" fill="#6b4423"/>
    <!-- tres ojos -->
    <circle cx="186" cy="76" r="4" fill="#222"/>
    <circle cx="214" cy="76" r="4" fill="#222"/>
    <circle cx="200" cy="64" r="4" fill="#222"/>
    <path d="M188 92 q12 10 24 0" stroke="#a05a3a" stroke-width="3" fill="none" stroke-linecap="round"/>
  </g>

  <!-- pequeñas líneas de "flote" -->
  <g stroke="#7fb8d8" stroke-width="2" stroke-linecap="round">
    <path d="M150 100 l10 0"/>
    <path d="M244 96 l10 0"/>
    <path d="M156 60 l8 0"/>
    <path d="M240 56 l8 0"/>
  </g>

  <!-- sombra de la cabeza, separada -->
  <ellipse cx="200" cy="120" rx="26" ry="5" fill="#000" opacity="0.08"/>
</svg>