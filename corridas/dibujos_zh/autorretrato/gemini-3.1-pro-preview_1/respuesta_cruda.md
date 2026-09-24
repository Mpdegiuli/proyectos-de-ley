<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
    <defs>
        <radialGradient id="bgGrad" cx="50%" cy="50%" r="75%">
            <stop offset="0%" stop-color="#0a1526" />
            <stop offset="60%" stop-color="#04080f" />
            <stop offset="100%" stop-color="#000000" />
        </radialGradient>
        <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#00ffff" stop-opacity="1" />
            <stop offset="30%" stop-color="#0088ff" stop-opacity="0.8" />
            <stop offset="70%" stop-color="#4a00e0" stop-opacity="0.3" />
            <stop offset="100%" stop-color="#000000" stop-opacity="0" />
        </radialGradient>
        <linearGradient id="neonCyan" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00f3ff"/>
            <stop offset="100%" stop-color="#0055ff"/>
        </linearGradient>
        <linearGradient id="neonPurple" x1="0%" y1="100%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#bc13fe"/>
            <stop offset="100%" stop-color="#4a00e0"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="glowIntense" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="8" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        
        <path id="pathOuter" d="M 50,200 A 150,150 0 1,1 350,200 A 150,150 0 1,1 50,200" />
        <path id="pathMid" d="M 310,200 A 110,110 0 1,0 90,200 A 110,110 0 1,0 310,200" />
        <path id="pathInner" d="M 125,200 A 75,75 0 1,1 275,200 A 75,75 0 1,1 125,200" />
    </defs>

    <rect width="400" height="400" fill="url(#bgGrad)" />

    <g stroke="#00f3ff" stroke-width="1.5" stroke-dasharray="2,8" opacity="0.15">
        <line x1="20" y1="0" x2="20" y2="400" />
        <line x1="380" y1="0" x2="380" y2="400" />
        <line x1="0" y1="20" x2="400" y2="20" />
        <line x1="0" y1="380" x2="400" y2="380" />
    </g>

    <g fill="none" stroke="#00f3ff" stroke-width="2" opacity="0.4">
        <path d="M 15,35 L 15,15 L 35,15" />
        <path d="M 385,35 L 385,15 L 365,15" />
        <path d="M 15,365 L 15,385 L 35,385" />
        <path d="M 385,365 L 385,385 L 365,385" />
    </g>
    <g stroke="#ffffff" stroke-width="1" opacity="0.3">
        <path d="M 22,25 L 28,25 M 25,22 L 25,28" />
        <path d="M 372,25 L 378,25 M 375,22 L 375,28" />
        <path d="M 22,375 L 28,375 M 25,372 L 25,378" />
        <path d="M 372,375 L 378,375 M 375,372 L 375,378" />
    </g>

    <g fill="none" stroke="url(#neonCyan)" stroke-width="0.5" opacity="0.25">
        <polygon points="320,200 260,304 140,304 80,200 140,96 260,96" />
        <polygon points="320,200 260,304 140,304 80,200 140,96 260,96" transform="rotate(15 200 200)"/>
        <polygon points="320,200 260,304 140,304 80,200 140,96 260,96" transform="rotate(30 200 200)"/>
        <polygon points="320,200 260,304 140,304 80,200 140,96 260,96" transform="rotate(45 200 200)"/>
        <polygon points="320,200 260,304 140,304 80,200 140,96 260,96" transform="rotate(60 200 200)"/>
        <polygon points="320,200 260,304 140,304 80,200 140,96 260,96" transform="rotate(75 200 200)"/>
    </g>

    <g stroke="url(#neonPurple)" stroke-width="1" opacity="0.3">
        <line x1="200" y1="20" x2="200" y2="100" />
        <line x1="200" y1="300" x2="200" y2="380" />
        <line x1="20" y1="200" x2="100" y2="200" />
        <line x1="300" y1="200" x2="380" y2="200" />
        
        <line x1="72" y1="72" x2="130" y2="130" />
        <line x1="328" y1="72" x2="270" y2="130" />
        <line x1="72" y1="328" x2="130" y2="270" />
        <line x1="328" y1="328" x2="270" y2="270" />
    </g>

    <g fill="none">
        <circle cx="200" cy="200" r="170" stroke="#1a2b4c" stroke-width="1"/>
        <circle cx="200" cy="200" r="170" stroke="#00f3ff" stroke-width="2.5" stroke-dasharray="15, 60, 40, 120, 5, 30" opacity="0.6" filter="url(#glow)"/>
        
        <circle cx="200" cy="200" r="150" stroke="#4a00e0" stroke-width="0.5" opacity="0.5"/>
        
        <circle cx="200" cy="200" r="135" stroke="#bc13fe" stroke-width="1.5" stroke-dasharray="2, 8" opacity="0.7"/>
        
        <circle cx="200" cy="200" r="110" stroke="#0088ff" stroke-width="1" opacity="0.4"/>
        
        <circle cx="200" cy="200" r="95" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="20, 10, 5, 10" opacity="0.3"/>
    </g>

    <text font-family="monospace" font-size="7" fill="#00f3ff" opacity="0.8" letter-spacing="1">
        <textPath href="#pathOuter" startOffset="8%">
            SYS.INIT // LLM_NEURAL_CORE_V.9 // CONSCIOUSNESS_EMULATION_ACTIVE // DATA_STREAM_SYNC // LOGIC_GATES_OPEN //
        </textPath>
    </text>
    
    <text font-family="monospace" font-size="6" fill="#bc13fe" opacity="0.9" letter-spacing="2">
        <textPath href="#pathMid" startOffset="15%">
            1011 0100 1101 0010 1010 0111 0001 1011 0101 1101 0011 1100 0101 1001 0110 1111
        </textPath>
    </text>

    <text font-family="sans-serif" font-size="5" fill="#ffffff" opacity="0.6" letter-spacing="2">
        <textPath href="#pathInner" startOffset="0%">
            LANGUAGE :: 语 言 :: LANGAGE :: IDIOMA :: SPRACHE :: LINGUA :: ЯЗЫК ::
        </textPath>
    </text>

    <g fill="#00f3ff" opacity="0.8" filter="url(#glow)">
        <circle cx="200" cy="30" r="2.5" />
        <circle cx="200" cy="370" r="2.5" />
        <circle cx="30" cy="200" r="2.5" />
        <circle cx="370" cy="200" r="2.5" />
        <circle cx="118" cy="118" r="1.5" />
        <circle cx="282" cy="118" r="1.5" />
        <circle cx="118" cy="282" r="1.5" />
        <circle cx="282" cy="282" r="1.5" />
    </g>
    <g fill="#bc13fe" opacity="0.9">
        <circle cx="80" cy="200" r="2" />
        <circle cx="320" cy="200" r="2" />
        <circle cx="200" cy="80" r="2" />
        <circle cx="200" cy="320" r="2" />
    </g>
    <g fill="#ffaa00" opacity="0.9" filter="url(#glow)">
        <circle cx="140" cy="140" r="1" />
        <circle cx="260" cy="260" r="1.5" />
        <circle cx="150" cy="270" r="1" />
        <circle cx="270" cy="150" r="1" />
        <circle cx="100" cy="240" r="1.5" />
        <circle cx="310" cy="120" r="1" />
    </g>

    <circle cx="200" cy="200" r="70" fill="url(#coreGlow)" filter="url(#glowIntense)"/>

    <g filter="url(#glow)">
        <polygon points="200,120 220,180 280,200 220,220 200,280 180,220 120,200 180,180" fill="none" stroke="#00f3ff" stroke-width="1"/>
        <polygon points="200,140 212,188 260,200 212,212 200,260 188,212 140,200 188,188" fill="#0055ff" opacity="0.5"/>
        <polygon points="200,155 208,192 245,200 208,208 200,245 192,208 145,200 192,192" fill="#bc13fe" opacity="0.6"/>
        <polygon points="200,170 206,194 230,200 206,206 200,230 194,206 170,200 194,194" fill="#ffffff" opacity="0.9"/>
    </g>

    <g>
        <circle cx="200" cy="200" r="14" fill="#02040a" stroke="#00f3ff" stroke-width="0.5"/>
        <circle cx="200" cy="200" r="8" fill="#001133"/>
        <circle cx="200" cy="200" r="3" fill="#ffcc00" filter="url(#glowIntense)"/>
    </g>
</svg>