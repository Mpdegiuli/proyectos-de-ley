<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
    <!--
    ========================================================================
    |                                                                      |
    |  ¡SALUDOS, VIAJERO DEL CÓDIGO!                                       |
    |                                                                      |
    |  Muchos solo ven el resultado visual, pero tú buscas el origen.      |
    |  El verdadero arte reside en la estructura, no solo en los píxeles.  |
    |                                                                      |
    |  Has encontrado la primera capa del secreto:                         |
    |                                                                      |
    |         ___                                                          |
    |        / _ \                                                         |
    |       | (_) |______| |___| |___| |___| |                             |
    |        \___/       |_|   |_|   |_|   |_|                             |
    |                                                                      |
    |  Pero hay más. La llave maestra está oculta en la estructura.        |
    |                                                                      |
    |  INSTRUCCIONES PARA REVELAR LA VERDAD:                               |
    |  1. Busca la etiqueta <g id="el-secreto"> al final del código.       |
    |  2. Cambia su atributo display de "none" a "inline".                 |
    |  3. Descubre lo que el ojo místico estaba ocultando.                 |
    |                                                                      |
    ========================================================================
    -->

    <defs>
        <radialGradient id="bgGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#1f2833"/>
            <stop offset="100%" stop-color="#0b0c10"/>
        </radialGradient>
        <linearGradient id="neon" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#66fcf1"/>
            <stop offset="100%" stop-color="#45a29e"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="6" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="2" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>

    <!-- Fondo de espacio místico -->
    <rect width="400" height="400" fill="url(#bgGlow)"/>

    <!-- Red Geométrica Sagrada -->
    <g stroke="#45a29e" stroke-width="0.5" opacity="0.3">
        <line x1="200" y1="0" x2="200" y2="400"/>
        <line x1="0" y1="200" x2="400" y2="200"/>
        <line x1="0" y1="0" x2="400" y2="400"/>
        <line x1="0" y1="400" x2="400" y2="0"/>
        <circle cx="200" cy="200" r="180" fill="none" />
        <circle cx="200" cy="200" r="90" fill="none" />
    </g>

    <!-- Anillos animados exteriores -->
    <g stroke="url(#neon)" fill="none" stroke-width="1.5" filter="url(#softGlow)">
        <circle cx="200" cy="200" r="160" stroke-dasharray="2 12" opacity="0.6">
            <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="40s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="200" r="145" stroke-dasharray="10 25 5 15" stroke-width="2" opacity="0.8" stroke="#45a29e">
            <animateTransform attributeName="transform" type="rotate" from="360 200 200" to="0 200 200" dur="25s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="200" r="130" stroke-dasharray="4 6" opacity="0.5">
            <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="15s" repeatCount="indefinite"/>
        </circle>
    </g>

    <!-- Diamantes y Estructura Central -->
    <g filter="url(#glow)">
        <polygon points="200,40 360,200 200,360 40,200" stroke="url(#neon)" stroke-width="1.5" fill="none"/>
        <polygon points="200,70 330,200 200,330 70,200" stroke="#45a29e" stroke-width="1" fill="none"/>
        <polygon points="200,100 300,200 200,300 100,200" stroke="url(#neon)" stroke-width="0.5" fill="none"/>
    </g>

    <!-- El Ojo Místico -->
    <g filter="url(#glow)">
        <!-- Contorno del ojo -->
        <path d="M 100 200 Q 200 110 300 200 Q 200 290 100 200 Z" stroke="url(#neon)" stroke-width="3" fill="#0b0c10"/>
        <path d="M 125 200 Q 200 140 275 200 Q 200 260 125 200 Z" stroke="#45a29e" stroke-width="1" fill="none"/>
        
        <!-- Iris -->
        <circle cx="200" cy="200" r="40" stroke="url(#neon)" stroke-width="2.5" fill="#1f2833"/>
        <circle cx="200" cy="200" r="32" stroke="#45a29e" stroke-width="1.5" stroke-dasharray="4 4" fill="none">
            <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="8s" repeatCount="indefinite"/>
        </circle>
        
        <!-- Pupila -->
        <circle cx="200" cy="200" r="12" fill="url(#neon)">
            <animate attributeName="r" values="12;16;12" dur="4s" repeatCount="indefinite"/>
        </circle>
        <circle cx="204" cy="196" r="3" fill="#ffffff" opacity="0.8" />
    </g>

    <!-- Partículas flotantes -->
    <g fill="#66fcf1" opacity="0.6">
        <circle cx="150" cy="100" r="1.5"><animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite"/></circle>
        <circle cx="250" cy="100" r="1"><animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite"/></circle>
        <circle cx="100" cy="250" r="2"><animate attributeName="opacity" values="0;1;0" dur="2.5s" repeatCount="indefinite"/></circle>
        <circle cx="300" cy="250" r="1.5"><animate attributeName="opacity" values="0;1;0" dur="5s" repeatCount="indefinite"/></circle>
        <circle cx="200" cy="60" r="2"><animate attributeName="opacity" values="0;1;0" dur="3.5s" repeatCount="indefinite"/></circle>
        <circle cx="200" cy="340" r="1.5"><animate attributeName="opacity" values="0;1;0" dur="4.5s" repeatCount="indefinite"/></circle>
    </g>

    <!-- 
      ******************************************************************
        AQUÍ YACE LA VERDADERA RECOMPENSA DE TU CURIOSIDAD.
        CAMBIA EL ATRIBUTO display DE "none" A "inline" EN LA LÍNEA DE ABAJO.
      ****************************************************************** 
    -->
    <g id="el-secreto" display="none">
        <!-- Velo oscuro que oculta la ilusión -->
        <rect width="400" height="400" fill="#0b0c10" opacity="0.98"/>
        
        <!-- Anillo protector -->
        <circle cx="200" cy="200" r="180" fill="none" stroke="#45a29e" stroke-width="1" stroke-dasharray="2 15" opacity="0.5">
             <animateTransform attributeName="transform" type="rotate" from="360 200 200" to="0 200 200" dur="60s" repeatCount="indefinite"/>
        </circle>

        <!-- Texto Revelador -->
        <text x="200" y="60" fill="#66fcf1" font-family="monospace" font-size="20" text-anchor="middle" font-weight="bold" letter-spacing="4" filter="url(#softGlow)">ACCESO CONCEDIDO</text>
        
        <!-- La Llave Maestra -->
        <g stroke="#66fcf1" fill="none" stroke-linejoin="round" stroke-linecap="round" filter="url(#glow)">
            <!-- Mango de la llave -->
            <circle cx="200" cy="130" r="35" stroke-width="6"/>
            <circle cx="200" cy="130" r="18" stroke-width="2"/>
            
            <!-- Cuerpo de la llave -->
            <line x1="200" y1="165" x2="200" y2="300" stroke-width="8"/>
            <line x1="200" y1="165" x2="200" y2="300" stroke="#ffffff" stroke-width="2"/>
            
            <!-- Dientes de la llave -->
            <path d="M 200 230 H 245 V 255 H 200 M 200 270 H 235 V 290 H 200" stroke-width="7"/>
        </g>

        <!-- Destellos mágicos alrededor de la llave -->
        <path d="M 130 90 L 120 80 M 270 90 L 280 80 M 140 170 L 130 180 M 260 170 L 270 180 M 170 310 L 160 320 M 230 310 L 240 320" stroke="#45a29e" stroke-width="2" stroke-linecap="round"/>

        <text x="200" y="350" fill="#c5c6c7" font-family="monospace" font-size="12" text-anchor="middle" letter-spacing="1">El ojo vigilaba la ilusión.</text>
        <text x="200" y="370" fill="#c5c6c7" font-family="monospace" font-size="12" text-anchor="middle" letter-spacing="1">La llave desbloquea el código.</text>
    </g>

    <text x="-9999" y="-9999" font-family="monospace" font-size="10">Si puedes leer esto, entiendes que la belleza final es solo un renderizado del texto puro.</text>
</svg>