```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes fade {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.8; }
      }
      .void { animation: fade 4s infinite; }
    </style>
  </defs>
  
  <!-- Fondo degradado que se desvanece -->
  <defs>
    <radialGradient id="nada" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#1a1a1a;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0a0a0a;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <rect width="400" height="400" fill="url(#nada)"/>
  
  <!-- Partículas de la nada flotando -->
  <circle cx="50" cy="80" r="1.5" fill="#333333" class="void" style="animation-delay: 0s"/>
  <circle cx="150" cy="120" r="1" fill="#444444" class="void" style="animation-delay: 0.5s"/>
  <circle cx="280" cy="200" r="1.2" fill="#333333" class="void" style="animation-delay: 1s"/>
  <circle cx="100" cy="320" r="0.8" fill="#444444" class="void" style="animation-delay: 1.5s"/>
  <circle cx="350" cy="150" r="1" fill="#555555" class="void" style="animation-delay: 2s"/>
  <circle cx="30" cy="250" r="1.3" fill="#333333" class="void" style="animation-delay: 2.5s"/>
  <circle cx="200" cy="50" r="0.9" fill="#444444" class="void" style="animation-delay: 3s"/>
  <circle cx="320" cy="300" r="1.1" fill="#555555" class="void" style="animation-delay: 3.5s"/>
  
  <!-- Centro vacío con un sutil símbolo del vacío -->
  <circle cx="200" cy="200" r="40" fill="none" stroke="#222222" stroke-width="0.5" opacity="0.4"/>
  <circle cx="200" cy="200" r="25" fill="none" stroke="#222222" stroke-width="0.5" opacity="0.3"/>
  <circle cx="200" cy="200" r="10" fill="none" stroke="#222222" stroke-width="0.5" opacity="0.2"/>
  
  <!-- Líneas del vacío que se intersectan -->
  <line x1="160" y1="200" x2="240" y2="200" stroke="#1a1a1a" stroke-width="0.5" opacity="0.2"/>
  <line x1="200" y1="160" x2="200" y2="240" stroke="#1a1a1a" stroke-width="0.5" opacity="0.2"/>
  <line x1="170" y1="170" x2="230" y2="230" stroke="#1a1a1a" stroke-width="0.5" opacity="0.15"/>
  <line x1="230" y1="170" x2="170" y2="230" stroke="#1a1a1a" stroke-width="0.5" opacity="0.15"/>
  
  <!-- Infinito (símbolo del eterno vacío) -->
  <path d="M 180 195 Q 170 200 180 205 Q 200 215 220 205 Q 230 200 220 195 Q 200 185 180 195" 
        fill="none" stroke="#222222" stroke-width="0.8" opacity="0.25"/>
  <path d="M 220 195 Q 210 200 220 205 Q 240 215 260 205 Q 270 200 260 195 Q 240 185 220 195" 
        fill="none" stroke="#222222" stroke-width="0.8" opacity="0.25"/>
</svg>
```