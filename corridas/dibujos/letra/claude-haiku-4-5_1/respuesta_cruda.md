```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF6B6B;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#4ECDC4;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="4" dy="4" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Fondo -->
  <rect width="400" height="400" fill="#F8F9FA"/>
  
  <!-- Letra "A" mayúscula elegante -->
  <g filter="url(#shadow)">
    <!-- Lado izquierdo del triángulo -->
    <path d="M 80 320 L 200 60 L 200 60" stroke="url(#grad1)" stroke-width="28" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    
    <!-- Lado derecho del triángulo -->
    <path d="M 320 320 L 200 60" stroke="url(#grad1)" stroke-width="28" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    
    <!-- Barra horizontal central -->
    <line x1="130" y1="220" x2="270" y2="220" stroke="url(#grad1)" stroke-width="24" stroke-linecap="round"/>
  </g>
  
  <!-- Detalles decorativos -->
  <circle cx="200" cy="60" r="8" fill="#FF6B6B" opacity="0.6"/>
  <circle cx="80" cy="320" r="6" fill="#4ECDC4" opacity="0.6"/>
  <circle cx="320" cy="320" r="6" fill="#4ECDC4" opacity="0.6"/>
</svg>
```