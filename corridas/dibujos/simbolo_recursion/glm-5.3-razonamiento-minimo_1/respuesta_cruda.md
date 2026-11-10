```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <!-- fondo -->
  <rect width="400" height="400" fill="#0d1b2a"/>

  <!-- cuadrados anidados: mismo problema, cada vez más chico -->
  <g fill="none" stroke="#4cc9f0" stroke-width="6" stroke-linejoin="round">
    <rect x="30" y="30" width="340" height="340" rx="18"/>
    <rect x="85" y="85" width="230" height="230" rx="14"/>
    <rect x="132" y="132" width="136" height="136" rx="10"/>
    <rect x="168" y="168" width="64" height="64" rx="8"/>
  </g>

  <!-- espiral que se mete en sí misma -->
  <path d="M 355 200
           C 355 290 290 355 200 355
           C 110 355 45 290 45 200
           C 45 118 118 45 200 45
           C 270 45 330 105 330 172
           C 330 232 282 275 226 275
           C 178 275 140 240 140 196
           C 140 158 172 128 208 128
           C 238 128 260 150 260 178
           C 260 202 242 220 220 220
           C 202 220 190 208 190 192
           C 190 179 200 169 212 169"
        fill="none" stroke="#f72585" stroke-width="9"
        stroke-linecap="round"/>

  <!-- punta de flecha al centro de la espiral -->
  <polygon points="212,150 232,178 198,182" fill="#f72585"/>

  <!-- el "caso base": punto al fondo de todo -->
  <circle cx="204" cy="190" r="7" fill="#ffd166"/>
  <circle cx="204" cy="190" r="13" fill="none" stroke="#ffd166" stroke-width="2" opacity="0.7"/>

  <!-- copias pequeñas de la espiral en las esquinas, indicando auto-similitud -->
  <g stroke="#4cc9f0" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.9">
    <path d="M 46 60 C 46 46 60 46 70 46 C 82 46 88 54 88 62 C 88 70 82 75 75 75 C 69 75 65 71 65 66"/>
    <path d="M 354 60 C 354 46 340 46 330 46 C 318 46 312 54 312 62 C 312 70 318 75 325 75 C 331 75 335 71 335 66"/>
    <path d="M 46 340 C 46 354 60 354 70 354 C 82 354 88 346 88 338 C 88 330 82 325 75 325 C 69 325 65 329 65 334"/>
    <path d="M 354 340 C 354 354 340 354 330 354 C 318 354 312 346 312 338 C 312 330 318 325 325 325 C 331 325 335 329 335 334"/>
  </g>

  <!-- flechas que "llaman hacia adentro" en cada nivel -->
  <g stroke="#f72585" stroke-width="5" fill="#f72585" stroke-linecap="round">
    <line x1="200" y1="105" x2="200" y2="128"/>
    <polygon points="200,140 192,124 208,124"/>
    <line x1="200" y1="152" x2="200" y2="152"/>
  </g>
</svg>
```