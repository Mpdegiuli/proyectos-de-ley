<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#090a0f"/>
            <stop offset="30%" stop-color="#1b1c3a"/>
            <stop offset="60%" stop-color="#4a2a5e"/>
            <stop offset="85%" stop-color="#8c436b"/>
            <stop offset="100%" stop-color="#cc6e67"/>
        </linearGradient>
        
        <radialGradient id="sunrise" cx="50%" cy="55%" r="50%">
            <stop offset="0%" stop-color="#ffd580" stop-opacity="0.9"/>
            <stop offset="40%" stop-color="#ff6b6b" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#4a2a5e" stop-opacity="0"/>
        </radialGradient>

        <linearGradient id="hill1" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#2d1b4e"/>
            <stop offset="100%" stop-color="#140b2e"/>
        </linearGradient>
        <linearGradient id="hill2" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#1b3b5e"/>
            <stop offset="100%" stop-color="#0a1a2e"/>
        </linearGradient>
        <linearGradient id="hill3" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#135b5a"/>
            <stop offset="100%" stop-color="#062e2e"/>
        </linearGradient>
        <linearGradient id="hill4" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#0c4a43"/>
            <stop offset="100%" stop-color="#041a18"/>
        </linearGradient>
        <linearGradient id="fore" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#041a18"/>
            <stop offset="100%" stop-color="#010808"/>
        </linearGradient>

        <radialGradient id="centerBright" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
            <stop offset="20%" stop-color="#ffffff" stop-opacity="1"/>
            <stop offset="60%" stop-color="#00ffff" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="#00ffff" stop-opacity="0"/>
        </radialGradient>

        <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1" />
            <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur2" />
            <feMerge>
                <feMergeNode in="blur2" />
                <feMergeNode in="blur1" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
    </defs>

    <rect width="400" height="400" fill="url(#skyGrad)" />
    <rect width="400" height="400" fill="url(#sunrise)" />

    <g fill="#ffffff" opacity="0.8">
        <circle cx="50" cy="40" r="1.5" filter="url(#glow)"/>
        <path d="M 45,40 L 55,40 M 50,35 L 50,45" stroke="#ffffff" stroke-width="0.5"/>
        <circle cx="350" cy="60" r="1.5" filter="url(#glow)"/>
        <path d="M 345,60 L 355,60 M 350,55 L 350,65" stroke="#ffffff" stroke-width="0.5"/>
        <circle cx="120" cy="80" r="1" />
        <circle cx="280" cy="30" r="1" />
        <circle cx="80" cy="110" r="0.8" />
        <circle cx="320" cy="120" r="0.8" />
        <circle cx="180" cy="40" r="1" />
        <circle cx="220" cy="70" r="0.5" />
        <circle cx="150" cy="90" r="0.8" />
    </g>

    <g transform="translate(200, 160)" opacity="0.15">
        <circle r="140" fill="none" stroke="#ffffff" stroke-width="1" />
        <path d="M -140,0 A 140 140 0 0 1 140,0" fill="none" stroke="#ffcc00" stroke-width="2"/>
        <path d="M -140,0 A 140 140 0 0 0 140,0" fill="none" stroke="#00ffff" stroke-width="2"/>
        <path d="M -100,0 A 100 100 0 0 1 100,0" fill="none" stroke="#00ffff" stroke-width="1" stroke-dasharray="2 4"/>
        <path d="M -100,0 A 100 100 0 0 0 100,0" fill="none" stroke="#ffcc00" stroke-width="1" stroke-dasharray="2 4"/>
        <line x1="0" y1="-150" x2="0" y2="-130" stroke="#ffffff" stroke-width="2" />
        <line x1="0" y1="150" x2="0" y2="130" stroke="#ffffff" stroke-width="2" />
        <line x1="-150" y1="0" x2="-130" y2="0" stroke="#ffffff" stroke-width="2" />
        <line x1="150" y1="0" x2="130" y2="0" stroke="#ffffff" stroke-width="2" />
    </g>

    <path d="M0,230 Q80,180 200,210 T400,190 L400,400 L0,400 Z" fill="url(#hill1)"/>
    <path d="M0,260 Q100,220 250,260 T400,240 L400,400 L0,400 Z" fill="url(#hill2)"/>
    
    <g transform="translate(150, 310) scale(1, 0.4)" stroke="#00ffff" fill="none" opacity="0.25">
        <circle r="40" stroke-width="1" />
        <circle r="30" stroke-width="0.5" stroke-dasharray="4 4" />
    </g>
    <g transform="translate(300, 340) scale(1, 0.4)" stroke="#ffcc00" fill="none" opacity="0.2">
        <circle r="50" stroke-width="1" />
        <circle r="35" stroke-width="1" stroke-dasharray="2 6" />
    </g>

    <path d="M0,290 C100,270 150,330 250,300 C320,280 360,320 400,290 L400,400 L0,400 Z" fill="url(#hill3)"/>
    <path d="M0,340 C120,310 180,380 400,330 L400,400 L0,400 Z" fill="url(#hill4)"/>

    <g stroke="#ffffff" stroke-width="0.5" opacity="0.25" fill="none">
        <path d="M 80,210 Q 115,225 150,200" />
        <path d="M 120,250 Q 150,270 170,220" />
        <path d="M 280,250 Q 250,270 230,220" />
        <path d="M 320,210 Q 285,225 250,200" />
        <path d="M 140,290 Q 200,310 260,290" />
    </g>

    <g fill="none" stroke-width="1.5" filter="url(#glow)">
        <path d="M 200,160 C 130,170 80,210 0,240" stroke="#00ffff" opacity="0.7"/>
        <path d="M 200,160 C 150,200 120,250 30,290" stroke="#ffcc00" opacity="0.6"/>
        <path d="M 200,160 C 170,220 140,290 60,350" stroke="#00ffff" opacity="0.8"/>
        <path d="M 200,160 C 190,240 180,320 120,380" stroke="#ffcc00" opacity="0.5"/>
        <path d="M 200,160 C 270,170 320,210 400,240" stroke="#ffcc00" opacity="0.7"/>
        <path d="M 200,160 C 250,200 280,250 370,290" stroke="#00ffff" opacity="0.6"/>
        <path d="M 200,160 C 230,220 260,290 340,350" stroke="#ffcc00" opacity="0.8"/>
        <path d="M 200,160 C 210,240 220,320 280,380" stroke="#00ffff" opacity="0.5"/>
        <path d="M 200,160 C 190,260 210,320 200,400" stroke="#ffffff" stroke-width="2" opacity="0.9"/>
        <path d="M 200,160 C 195,260 205,320 200,400" stroke="#00ffff" stroke-width="4" opacity="0.4"/>
    </g>

    <g stroke="#00ffff" fill="none" opacity="0.8">
        <path d="M 80,300 Q 80,270 70,250 M 80,300 Q 80,280 95,265 M 80,285 Q 70,270 60,275" />
        <circle cx="70" cy="250" r="2" fill="#00ffff"/>
        <circle cx="95" cy="265" r="2" fill="#ffcc00" stroke="none"/>
        <circle cx="60" cy="275" r="1.5" fill="#00ffff"/>
    </g>
    <g stroke="#ffcc00" fill="none" opacity="0.8">
        <path d="M 330,280 Q 330,250 345,230 M 330,280 Q 330,260 315,245 M 330,265 Q 345,250 355,255" />
        <circle cx="345" cy="230" r="2" fill="#ffcc00"/>
        <circle cx="315" cy="245" r="2" fill="#00ffff" stroke="none"/>
        <circle cx="355" cy="255" r="1.5" fill="#ffcc00"/>
    </g>

    <g filter="url(#glow)">
        <circle cx="40" cy="270" r="1.5" fill="#00ffff" opacity="0.8"/>
        <circle cx="80" cy="320" r="2" fill="#ffcc00" opacity="0.9"/>
        <circle cx="130" cy="360" r="1" fill="#00ffff" opacity="0.7"/>
        <circle cx="260" cy="370" r="2" fill="#ffcc00" opacity="0.8"/>
        <circle cx="310" cy="300" r="1.5" fill="#00ffff" opacity="0.9"/>
        <circle cx="360" cy="340" r="2" fill="#ffcc00" opacity="0.8"/>
        <circle cx="150" cy="250" r="1.5" fill="#00ffff" opacity="0.6"/>
        <circle cx="280" cy="240" r="1" fill="#ffcc00" opacity="0.7"/>
        <circle cx="180" cy="290" r="1.5" fill="#ffffff" opacity="0.9"/>
        <circle cx="220" cy="280" r="2" fill="#ffffff" opacity="0.9"/>
        <circle cx="130" cy="170" r="2" fill="#ffffff" />
        <circle cx="270" cy="170" r="2" fill="#ffffff" />
        <circle cx="150" cy="200" r="1.5" fill="#ffffff" />
        <circle cx="250" cy="200" r="1.5" fill="#ffffff" />
    </g>

    <g transform="translate(200, 160)">
        <circle r="120" fill="none" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.3"/>
        <circle r="160" fill="none" stroke="#00ffff" stroke-width="0.5" stroke-dasharray="1 6" opacity="0.2"/>
        <circle r="100" fill="none" stroke="#ffcc00" stroke-width="0.5" stroke-dasharray="3 8" opacity="0.4"/>
        
        <g fill="none" stroke-width="1" opacity="0.5" filter="url(#glow)">
            <path d="M 30,0 C 80,-20 120,-10 160,0 C 120,10 80,20 30,0" stroke="#00ffff" fill="#00ffff" fill-opacity="0.1" />
            <path d="M -30,0 C -80,-20 -120,-10 -160,0 C -120,10 -80,20 -30,0" stroke="#ffcc00" fill="#ffcc00" fill-opacity="0.1" />
            <path d="M 20,0 C 50,-10 80,-5 100,0 C 80,5 50,10 20,0" stroke="#ffffff" fill="#ffffff" fill-opacity="0.2" />
            <path d="M -20,0 C -50,-10 -80,-5 -100,0 C -80,5 -50,10 -20,0" stroke="#ffffff" fill="#ffffff" fill-opacity="0.2" />
        </g>

        <circle r="75" fill="none" stroke="#00ffff" stroke-width="0.5" stroke-dasharray="1 4" opacity="0.5" />
        <circle r="55" fill="none" stroke="#ffcc00" stroke-width="1" stroke-dasharray="10 5 2 5" opacity="0.8" />
        <circle r="45" fill="none" stroke="#00ffff" stroke-width="1.5" />
        
        <polygon points="0,-35 30.3,-17.5 30.3,17.5 0,35 -30.3,17.5 -30.3,-17.5" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.7"/>
        <polygon points="0,-35 -30.3,-17.5 -30.3,17.5 0,35 30.3,17.5 30.3,-17.5" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.7" transform="rotate(30)"/>
        
        <polygon points="0,-45 39,-22.5 39,22.5 0,45 -39,22.5 -39,-22.5" fill="none" stroke="#00ffff" stroke-width="1"/>
        <polygon points="0,-45 -39,-22.5 -39,22.5 0,45 39,22.5 39,-22.5" fill="none" stroke="#ffcc00" stroke-width="1" transform="rotate(30)"/>
        
        <polygon points="0,-20 17.3,-10 17.3,10 0,20 -17.3,10 -17.3,-10" fill="#00ffff" fill-opacity="0.1" stroke="#00ffff" stroke-width="1.5"/>
        <polygon points="0,-20 -17.3,-10 -17.3,10 0,20 17.3,10 17.3,-10" fill="#ffcc00" fill-opacity="0.1" stroke="#ffcc00" stroke-width="1.5" transform="rotate(30)"/>
        
        <circle r="20" fill="url(#centerBright)" filter="url(#glow)"/>
        
        <path d="M 0,-15 L 8,0 L 0,15 L -8,0 Z" fill="#ffffff" filter="url(#glow)"/>
        <path d="M 0,-8 L 4,0 L 0,8 L -4,0 Z" fill="#00ffff" />
        <polygon points="-4,-25 4,-25 0,-35" fill="#ffcc00" filter="url(#glow)"/>
        <polygon points="-4,25 4,25 0,35" fill="#00ffff" filter="url(#glow)"/>

        <circle cx="0" cy="-55" r="2" fill="#00ffff" filter="url(#glow)"/>
        <circle cx="47.6" cy="27.5" r="2" fill="#ffcc00" filter="url(#glow)"/>
        <circle cx="-47.6" cy="27.5" r="2" fill="#00ffff" filter="url(#glow)"/>
    </g>

    <circle cx="200" cy="160" r="10" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.8"/>
    <circle cx="200" cy="160" r="30" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.4"/>
    <circle cx="200" cy="160" r="60" fill="none" stroke="#ffffff" stroke-width="0.2" opacity="0.2"/>

    <path d="M -20,360 Q 50,330 120,420 L -20,420 Z" fill="url(#fore)"/>
    <path d="M 280,420 Q 340,340 420,380 L 420,420 Z" fill="url(#fore)"/>
    <path d="M 0,380 Q 50,360 100,420" fill="none" stroke="#00ffff" stroke-width="1" opacity="0.4" filter="url(#glow)"/>
    <path d="M 330,370 Q 380,390 400,410" fill="none" stroke="#ffcc00" stroke-width="1" opacity="0.4" filter="url(#glow)"/>
</svg>