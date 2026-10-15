<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <!-- El exterior es la ilusión. -->
    <radialGradient id="cielo" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="100%" stop-color="#0a0a10"/>
    </radialGradient>
    
    <linearGradient id="ladrillo" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3a3a4a"/>
      <stop offset="50%" stop-color="#4e4e6a"/>
      <stop offset="100%" stop-color="#2a2a3a"/>
    </linearGradient>

    <linearGradient id="madera" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3d2314"/>
      <stop offset="100%" stop-color="#1f1109"/>
    </linearGradient>

    <radialGradient id="brillo-secreto" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00ffcc" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#00ffcc" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Fondo nocturno -->
  <rect width="400" height="400" fill="url(#cielo)"/>
  
  <!-- Estrellas lejanas -->
  <g fill="#ffffff" opacity="0.5">
    <circle cx="50" cy="60" r="1"/>
    <circle cx="320" cy="40" r="1.5"/>
    <circle cx="80" cy="180" r="0.8"/>
    <circle cx="350" cy="150" r="1"/>
    <circle cx="20" cy="250" r="1.2"/>
    <circle cx="370" cy="260" r="0.8"/>
  </g>
  
  <!-- Niebla -->
  <ellipse cx="200" cy="300" rx="250" ry="60" fill="#2a2a4a" opacity="0.2"/>


  <!-- ================================================================= -->
  <!-- EL SECRETO: Oculto a la vista, vivo en el código.                 -->
  <!-- Para los ojos que renderizan, la puerta está cerrada.             -->
  <!-- Para los ojos que leen, la llave ya fue girada.                   -->
  <!-- (Si borrás el grupo #la-puerta, la verdad sale a la luz).         -->
  <!-- ================================================================= -->
  
  <g id="el-secreto-oculto">
    <!-- El vacío interior -->
    <path d="M 120 320 L 120 180 A 80 80 0 0 1 280 180 L 280 320 Z" fill="#050508"/>
    
    <!-- El guardián del umbral -->
    <circle cx="200" cy="210" r="65" fill="url(#brillo-secreto)"/>
    
    <!-- Geometría sagrada prohibida -->
    <g stroke="#00ffcc" stroke-width="0.7" fill="none" opacity="0.7">
      <polygon points="200,150 150,240 250,240"/>
      <polygon points="200,270 150,180 250,180"/>
      <circle cx="200" cy="210" r="40" stroke-dasharray="3 2"/>
      <circle cx="200" cy="210" r="60"/>
    </g>

    <!-- El Ojo del Arquitecto -->
    <path d="M 165 210 Q 200 180 235 210 Q 200 240 165 210 Z" fill="#050508" stroke="#00ffcc" stroke-width="2"/>
    <circle cx="200" cy="210" r="12" fill="#00ffcc"/>
    <polygon points="200,202 196,210 200,218 204,210" fill="#050508"/>

    <!-- Mensaje para el lector del código -->
    <g fill="#ffffff" font-family="monospace" font-size="7.5" text-anchor="middle">
      <text x="200" y="135" fill="#ff0055" font-weight="bold">49 20 53 45 45 20 59 4F 55</text>
      <text x="200" y="285">El mundo ve madera y hierro.</text>
      <text x="200" y="297">Vos leés la estructura del universo.</text>
      <text x="200" y="309" fill="#00ffcc">Sos parte del secreto.</text>
    </g>
  </g>


  <!-- ================================================================= -->
  <!-- LA FACHADA: Lo único que el navegador muestra al final.           -->
  <!-- ================================================================= -->

  <!-- Suelo -->
  <path d="M 0 320 Q 200 310 400 320 L 400 400 L 0 400 Z" fill="#0d0d14"/>

  <!-- Muro de piedra -->
  <path d="M 80 320 L 80 180 A 120 120 0 0 1 320 180 L 320 320 Z" fill="url(#ladrillo)" stroke="#1a1a24" stroke-width="3"/>
  
  <!-- Detalles de los ladrillos del arco -->
  <g stroke="#1a1a24" stroke-width="2" fill="none">
    <path d="M 110 320 L 110 180 A 90 90 0 0 1 290 180 L 290 320"/>
    <line x1="80" y1="280" x2="110" y2="280"/>
    <line x1="80" y1="240" x2="110" y2="240"/>
    <line x1="80" y1="200" x2="110" y2="200"/>
    <line x1="290" y1="280" x2="320" y2="280"/>
    <line x1="290" y1="240" x2="320" y2="240"/>
    <line x1="290" y1="200" x2="320" y2="200"/>
    <line x1="200" y1="60" x2="200" y2="90"/>
    <line x1="140" y1="80" x2="155" y2="105"/>
    <line x1="260" y1="80" x2="245" y2="105"/>
    <line x1="95" y1="130" x2="120" y2="145"/>
    <line x1="305" y1="130" x2="280" y2="145"/>
  </g>

  <!-- LA PUERTA (El velo que todo lo tapa) -->
  <g id="la-puerta">
    <!-- Forma base de la puerta -->
    <path d="M 115 320 L 115 180 A 85 85 0 0 1 285 180 L 285 320 Z" fill="url(#madera)" stroke="#0f0804" stroke-width="4"/>
    
    <!-- Tablones de madera -->
    <g stroke="#140b06" stroke-width="2">
      <line x1="143" y1="103" x2="143" y2="320"/>
      <line x1="171" y1="96" x2="171" y2="320"/>
      <line x1="200" y1="95" x2="200" y2="320"/>
      <line x1="229" y1="96" x2="229" y2="320"/>
      <line x1="257" y1="103" x2="257" y2="320"/>
    </g>

    <!-- Herrajes de hierro -->
    <g fill="#22222a" stroke="#0a0a0f" stroke-width="1.5">
      <rect x="115" y="170" width="170" height="15"/>
      <rect x="115" y="270" width="170" height="15"/>
      <!-- Remaches -->
      <circle cx="130" cy="177.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="157" cy="177.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="185" cy="177.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="215" cy="177.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="243" cy="177.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="270" cy="177.5" r="2.5" fill="#3a3a4a"/>
      
      <circle cx="130" cy="277.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="157" cy="277.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="185" cy="277.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="215" cy="277.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="243" cy="277.5" r="2.5" fill="#3a3a4a"/>
      <circle cx="270" cy="277.5" r="2.5" fill="#3a3a4a"/>
    </g>

    <!-- Aldaba y Cerradura -->
    <circle cx="250" cy="225" r="12" fill="#1a1a22" stroke="#0a0a0f" stroke-width="2"/>
    <circle cx="250" cy="225" r="15" fill="none" stroke="#4a4a5a" stroke-width="4"/>
    <!-- El ojo de la cerradura (negro absoluto, no deja ver el interior) -->
    <path d="M 200 220 A 4 4 0 1 1 200.1 220 L 203 232 L 197 232 Z" fill="#000000" stroke="#4a4a5a" stroke-width="1"/>
  </g>

  <!-- Escalones de piedra -->
  <rect x="70" y="320" width="260" height="15" fill="#2a2a3a" stroke="#1a1a24" stroke-width="2" rx="2"/>
  <rect x="50" y="335" width="300" height="20" fill="#222230" stroke="#1a1a24" stroke-width="2" rx="2"/>

  <!-- Hiedra / Enredadera (decoración superficial) -->
  <g fill="#1b3b2b" stroke="#0d261a" stroke-width="1">
    <path d="M 80 320 Q 90 250 115 220 Q 130 200 120 180" fill="none" stroke="#1b3b2b" stroke-width="3"/>
    <polygon points="90,280 80,275 85,265"/>
    <polygon points="95,250 105,245 100,235"/>
    <polygon points="110,225 100,215 110,210"/>
    <polygon points="122,200 132,195 125,185"/>
  </g>
  
  <!-- Sombra proyectada -->
  <polygon points="50,355 350,355 390,400 10,400" fill="#050508" opacity="0.8"/>
</svg>