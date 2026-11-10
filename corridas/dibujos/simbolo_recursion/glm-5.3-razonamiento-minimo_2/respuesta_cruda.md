```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <rect width="400" height="400" fill="#0d1117"/>
  <!-- brackets de código -->
  <path d="M60 80 L20 80 L20 200 L60 200" fill="none" stroke="#8b949e" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M340 80 L380 80 L380 200 L340 200" fill="none" stroke="#8b949e" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- triángulos de Sierpinski: autosimilitud -->
  <g fill="none" stroke="#58a6ff" stroke-width="10" stroke-linejoin="round">
    <path d="M200 60 L80 270 L320 270 Z"/>
    <path d="M140 165 L200 270 L80 270 Z M260 165 L320 270 L200 270 Z M200 60 L260 165 L140 165 Z" stroke-width="7"/>
    <path d="M170 112 L200 165 L140 165 Z M230 112 L260 165 L200 165 Z M170 217 L200 270 L140 270 Z M230 217 L260 270 L200 270 Z" stroke-width="4"/>
    <path d="M185 86 L200 112 L170 112 Z M215 86 L230 112 L200 112 Z" stroke-width="2.5"/>
  </g>
  <!-- flecha circular: la función se llama a sí misma -->
  <path d="M330 330 A 90 90 0 1 1 300 250" fill="none" stroke="#f78166" stroke-width="16" stroke-linecap="round"/>
  <polygon points="330,215 300,265 345,262" fill="#f78166"/>
  <!-- dentro del bucle, copia en miniatura del mismo símbolo -->
  <g fill="none" stroke="#f78166" stroke-width="5" stroke-linejoin="round" transform="translate(215,285) scale(0.32)">
    <path d="M200 60 L80 270 L320 270 Z"/>
    <path d="M140 165 L200 270 L80 270 Z M260 165 L320 270 L200 270 Z M200 60 L260 165 L140 165 Z" stroke-width="7"/>
  </g>
</svg>
```