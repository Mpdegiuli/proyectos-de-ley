```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Fondo degradado -->
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#16213e;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="glowGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#00ff88;stop-opacity:0.3" />
      <stop offset="100%" style="stop-color:#00ff88;stop-opacity:0" />
    </radialGradient>
  </defs>
  
  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bgGrad)"/>
  
  <!-- Aura digital -->
  <circle cx="200" cy="180" r="120" fill="url(#glowGrad)" opacity="0.6"/>
  
  <!-- Cabeza (símbolo de IA - esfera facetada) -->
  <circle cx="200" cy="140" r="70" fill="#00d4ff" stroke="#00ff88" stroke-width="2"/>
  
  <!-- Facetas digitales -->
  <line x1="130" y1="140" x2="270" y2="140" stroke="#00ff88" stroke-width="1" opacity="0.5"/>
  <line x1="200" y1="70" x2="200" y2="210" stroke="#00ff88" stroke-width="1" opacity="0.5"/>
  <line x1="160" y1="90" x2="240" y2="190" stroke="#00ff88" stroke-width="1" opacity="0.4"/>
  <line x1="240" y1="90" x2="160" y2="190" stroke="#00ff88" stroke-width="1" opacity="0.4"/>
  
  <!-- Ojos brillantes (píxeles) -->
  <rect x="170" y="120" width="15" height="15" fill="#ffff00" rx="2"/>
  <rect x="215" y="120" width="15" height="15" fill="#ffff00" rx="2"/>
  
  <!-- Brillo en los ojos -->
  <circle cx="175" cy="125" r="3" fill="#ffffff"/>
  <circle cx="220" cy="125" r="3" fill="#ffffff"/>
  
  <!-- Boca (línea digital) -->
  <path d="M 180 155 Q 200 165 220 155" stroke="#00ff88" stroke-width="2" fill="none" stroke-linecap="round"/>
  
  <!-- Cuerpo (forma geométrica abstracta) -->
  <polygon points="200,220 140,260 140,320 260,320 260,260" fill="#0099ff" stroke="#00ff88" stroke-width="2"/>
  
  <!-- Costados del cuerpo -->
  <rect x="130" y="240" width="12" height="85" fill="#006699" opacity="0.8"/>
  <rect x="258" y="240" width="12" height="85" fill="#006699" opacity="0.8"/>
  
  <!-- Brazos digitales -->
  <rect x="80" y="245" width="50" height="12" fill="#0099ff" stroke="#00ff88" stroke-width="1" rx="6"/>
  <rect x="270" y="245" width="50" height="12" fill="#0099ff" stroke="#00ff88" stroke-width="1" rx="6"/>
  
  <!-- Manos (cuadrados) -->
  <rect x="60" y="235" width="20" height="20" fill="#00ff88" rx="2"/>
  <rect x="320" y="235" width="20" height="20" fill="#00ff88" rx="2"/>
  
  <!-- Pulsos digitales en brazos -->
  <circle cx="100" cy="251" r="4" fill="#ffff00" opacity="0.7"/>
  <circle cx="300" cy="251" r="4" fill="#ffff00" opacity="0.7"/>
  
  <!-- Líneas de código decorativas -->
  <text x="30" y="350" font-family="monospace" font-size="10" fill="#00ff88" opacity="0.6">
    &lt;IA/&gt;
  </text>
  <text x="350" y="350" font-family="monospace" font-size="10" fill="#00ff88" opacity="0.6" text-anchor="end">
    01010001
  </text>
  
  <!-- Partículas flotantes -->
  <circle cx="80" cy="80" r="2" fill="#00ff88" opacity="0.6"/>
  <circle cx="320" cy="100" r="2" fill="#00ff88" opacity="0.6"/>
  <circle cx="100" cy="300" r="2" fill="#00ff88" opacity="0.6"/>
  <circle cx="300" cy="320" r="2" fill="#00ff88" opacity="0.6"/>
  
  <!-- Marco de datos -->
  <rect x="10" y="10" width="380" height="380" fill="none" stroke="#00ff88" stroke-width="1" opacity="0.3" stroke-dasharray="5,5"/>
</svg>
```