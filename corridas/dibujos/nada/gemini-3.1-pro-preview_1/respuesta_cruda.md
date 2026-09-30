<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
    <defs>
        <radialGradient id="wallLight" cx="50%" cy="30%" r="75%">
            <stop offset="0%" stop-color="#2a2a30"/>
            <stop offset="100%" stop-color="#070709"/>
        </radialGradient>
        
        <filter id="dropShadow" x="-20%" y="-20%" width="150%" height="150%">
            <feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#000" flood-opacity="0.85"/>
        </filter>
        
        <filter id="plaqueShadow" x="-30%" y="-30%" width="160%" height="160%">
            <feDropShadow dx="0" dy="5" stdDeviation="4" flood-color="#000" flood-opacity="0.75"/>
        </filter>

        <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#e8c973"/>
            <stop offset="25%" stop-color="#fdf3d6"/>
            <stop offset="50%" stop-color="#d4af37"/>
            <stop offset="75%" stop-color="#a67c1e"/>
            <stop offset="100%" stop-color="#543f0e"/>
        </linearGradient>

        <radialGradient id="voidGrad" cx="50%" cy="50%" r="65%">
            <stop offset="0%" stop-color="#000000"/>
            <stop offset="25%" stop-color="#000000"/>
            <stop offset="65%" stop-color="#030303"/>
            <stop offset="100%" stop-color="#0e0e0e"/>
        </radialGradient>

        <linearGradient id="shadowTop" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#000" stop-opacity="1"/>
            <stop offset="100%" stop-color="#000" stop-opacity="0"/>
        </linearGradient>

        <filter id="voidNoise">
            <feTurbulence type="fractalNoise" baseFrequency="1.5" numOctaves="3" stitchTiles="stitch"/>
            <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0.04 0"/>
        </filter>
    </defs>

    <rect width="400" height="400" fill="url(#wallLight)"/>

    <g filter="url(#dropShadow)">
        <path d="M 60 50 L 340 50 L 320 70 L 80 70 Z" fill="#222222"/>
        <path d="M 60 330 L 340 330 L 320 310 L 80 310 Z" fill="#040404"/>
        <path d="M 60 50 L 80 70 L 80 310 L 60 330 Z" fill="#141414"/>
        <path d="M 340 50 L 320 70 L 320 310 L 340 330 Z" fill="#0a0a0a"/>
        
        <rect x="79" y="69" width="242" height="242" fill="none" stroke="#000" stroke-width="2"/>
        <rect x="60" y="50" width="280" height="280" fill="none" stroke="#111" stroke-width="1"/>

        <path d="M 80 70 L 320 70 L 320 310 L 80 310 Z M 130 120 L 130 260 L 270 260 L 270 120 Z" fill="#f2f2eb" fill-rule="evenodd"/>
        
        <path d="M 130 120 L 270 120 L 265 125 L 135 125 Z" fill="#ffffff"/>
        <path d="M 130 260 L 270 260 L 265 255 L 135 255 Z" fill="#b3b3b3"/>
        <path d="M 130 120 L 135 125 L 135 255 L 130 260 Z" fill="#e0e0e0"/>
        <path d="M 270 120 L 265 125 L 265 255 L 270 260 Z" fill="#cccccc"/>

        <g>
            <rect x="135" y="125" width="130" height="130" fill="url(#voidGrad)"/>
            
            <rect x="135" y="125" width="130" height="130" filter="url(#voidNoise)"/>
            
            <g opacity="0.12" fill="none" stroke="#ffffff">
                <rect x="140" y="130" width="120" height="120" stroke-width="0.5"/>
                <rect x="148" y="138" width="104" height="104" stroke-width="0.4"/>
                <rect x="158" y="148" width="84" height="84" stroke-width="0.3"/>
                <rect x="172" y="162" width="56" height="56" stroke-width="0.2"/>
                <rect x="190" y="180" width="20" height="20" stroke-width="0.1"/>
                <circle cx="200" cy="190" r="0.4" fill="#ffffff" stroke="none" opacity="0.5"/>
            </g>
            
            <rect x="135" y="125" width="130" height="130" fill="url(#voidGrad)" opacity="0.6"/>
            
            <rect x="135" y="125" width="130" height="22" fill="url(#shadowTop)"/>
        </g>
    </g>

    <g filter="url(#plaqueShadow)">
        <rect x="150" y="348" width="100" height="28" fill="#2b2009" rx="3"/>
        <rect x="151" y="349" width="98" height="26" fill="url(#gold)" rx="2"/>
        
        <rect x="153" y="351" width="94" height="22" fill="none" stroke="#7a5c17" stroke-width="0.5" rx="1"/>
        
        <circle cx="157" cy="362" r="1.5" fill="#3a2b0c"/>
        <circle cx="243" cy="362" r="1.5" fill="#3a2b0c"/>
        <circle cx="156.5" cy="361.5" r="0.5" fill="#a67c1e"/>
        <circle cx="242.5" cy="361.5" r="0.5" fill="#a67c1e"/>

        <text x="200" y="361" font-family="Georgia, 'Times New Roman', serif" font-size="7.5" fill="#171104" text-anchor="middle" font-weight="bold" letter-spacing="3.5">LA NADA</text>
        <text x="200" y="369" font-family="Georgia, 'Times New Roman', serif" font-size="4.2" fill="#2e2206" text-anchor="middle" font-style="italic">Anónimo, 2024</text>
    </g>
</svg>