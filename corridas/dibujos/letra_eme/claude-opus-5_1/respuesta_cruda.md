```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="fondo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f7f1e6"/>
      <stop offset="1" stop-color="#ead9c2"/>
    </linearGradient>
    <linearGradient id="tinta" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1d2b36"/>
      <stop offset="1" stop-color="#3c5a6b"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#fondo)"/>
  <rect x="12" y="12" width="376" height="376" fill="none" stroke="#c2ad90" stroke-width="2"/>

  <!-- pauta caligráfica -->
  <g stroke="#cbb79b" stroke-width="1.5" stroke-dasharray="7 7">
    <line x1="30" y1="110" x2="370" y2="110"/>
    <line x1="30" y1="200" x2="370" y2="200"/>
  </g>
  <line x1="30" y1="320" x2="370" y2="320" stroke="#b79a73" stroke-width="2.5"/>

  <!-- signo nasal: el aire que sale por la nariz -->
  <path d="M 112 78 C 130 46 156 46 174 78 C 192 110 218 110 236 78 C 250 55 268 52 282 66"
        fill="none" stroke="url(#tinta)" stroke-width="13" stroke-linecap="round"/>

  <!-- cuerpo de la letra: labios cerrados (lazo) sobre asta vertical -->
  <path d="M 140 112 L 140 320"
        fill="none" stroke="url(#tinta)" stroke-width="22" stroke-linecap="round"/>
  <path d="M 140 196 C 232 176 292 212 292 258 C 292 306 230 340 140 320"
        fill="none" stroke="url(#tinta)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- vibración: dos trazos cortos que cruzan el lazo -->
  <g stroke="#9c4a2f" stroke-width="7" stroke-linecap="round">
    <line x1="196" y1="232" x2="250" y2="232"/>
    <line x1="196" y1="284" x2="250" y2="284"/>
  </g>

  <!-- punto de apoyo en la base -->
  <circle cx="140" cy="348" r="7" fill="#9c4a2f"/>

  <!-- nombre del sonido -->
  <text x="300" y="352" font-family="Georgia, serif" font-size="30" fill="#1d2b36" letter-spacing="2">/m/</text>
  <text x="34" y="372" font-family="Georgia, serif" font-size="15" fill="#7b6games" opacity="0"> </text>
  <text x="34" y="374" font-family="Georgia, serif" font-size="14" fill="#7b6650" letter-spacing="3">nasal · bilabial · sonora</text>
</svg>
```