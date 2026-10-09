```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <clipPath id="clipTopLeft">
      <rect x="158" y="186" width="34" height="28"/>
    </clipPath>
    <clipPath id="clipMidLeft">
      <rect x="151" y="226" width="34" height="28"/>
    </clipPath>
    <clipPath id="clipMidRight">
      <rect x="215" y="226" width="34" height="28"/>
    </clipPath>
    <clipPath id="clipBotRight">
      <rect x="223" y="266" width="34" height="28"/>
    </clipPath>
  </defs>

  <!-- fondo -->
  <rect width="400" height="400" fill="#fdfdfb"/>
  <line x1="60" y1="340" x2="340" y2="340" stroke="#d8d8d2" stroke-width="2"/>
  <line x1="60" y1="336" x2="340" y2="336" stroke="#d8d8d2" stroke-width="1"/>

  <!-- las dos piernas de la A -->
  <path d="M150,340 L200,60 L250,340" fill="none" stroke="#222222"
        stroke-width="20" stroke-linejoin="round" stroke-linecap="butt"/>

  <!-- el marco (travesaño superior e inferior) -->
  <rect x="150" y="200" width="100" height="80" fill="none"
        stroke="#b03a2e" stroke-width="14" stroke-linejoin="miter"/>

  <!-- travesaño central -->
  <line x1="150" y1="240" x2="250" y2="240" stroke="#b03a2e" stroke-width="14"/>

  <!-- tejido imposible:
       arriba, la pierna izquierda pasa POR DELANTE del marco;
       en el medio, esa misma pierna pasa POR DELANTE del travesaño,
       pero el travesaño pasa POR DELANTE de la pierna derecha;
       abajo, el marco vuelve a estar POR DELANTE de la pierna izquierda
       y POR DETRÁS de la derecha.
       Ningún objeto rígido puede tejerse así. -->

  <!-- pierna izquierda por delante del borde superior -->
  <path d="M150,340 L200,60" fill="none" stroke="#222222" stroke-width="20"
        clip-path="url(#clipTopLeft)"/>

  <!-- pierna izquierda por delante del travesaño central -->
  <path d="M150,340 L200,60" fill="none" stroke="#222222" stroke-width="20"
        clip-path="url(#clipMidLeft)"/>

  <!-- travesaño central por delante de la pierna derecha -->
  <line x1="150" y1="240" x2="250" y2="240" stroke="#b03a2e" stroke-width="14"
        clip-path="url(#clipMidRight)"/>

  <!-- pierna derecha por delante del borde inferior -->
  <path d="M200,60 L250,340" fill="none" stroke="#222222" stroke-width="20"
        clip-path="url(#clipBotRight)"/>

  <!-- vértices Penrose en las esquinas del marco -->
  <g stroke="#b03a2e" stroke-width="14" fill="none">
    <path d="M150,207 L150,240"/>
    <path d="M250,207 L250,240"/>
    <path d="M150,240 L150,273"/>
    <path d="M250,240 L250,273"/>
  </g>

  <text x="200" y="378" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif"
        font-size="15" font-style="italic" fill="#8a8a84">una A imposible: el travesaño pasa a la vez por delante y por detrás</text>
</svg>
```