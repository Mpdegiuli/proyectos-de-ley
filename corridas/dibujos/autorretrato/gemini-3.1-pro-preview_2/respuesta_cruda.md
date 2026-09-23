<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="bgGrad" cx="50%" cy="50%" r="75%">
            <stop offset="0%" stop-color="#1e1b4b"/>
            <stop offset="45%" stop-color="#020617"/>
            <stop offset="100%" stop-color="#000000"/>
        </radialGradient>
        <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#a78bfa"/>
            <stop offset="35%" stop-color="#0ea5e9"/>
            <stop offset="100%" stop-color="#020617" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="metalLeft" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#334155"/>
            <stop offset="100%" stop-color="#0f172a"/>
        </linearGradient>
        <linearGradient id="metalRight" x1="1" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#475569"/>
            <stop offset="100%" stop-color="#1e293b"/>
        </linearGradient>
        <linearGradient id="metalDark" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#0f172a"/>
            <stop offset="100%" stop-color="#020617"/>
        </linearGradient>
        <filter id="neon" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur1"/>
            <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur2"/>
            <feMerge>
                <feMergeNode in="blur2"/>
                <feMergeNode in="blur1"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <filter id="neonSubtle" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur"/>
            <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>

    <rect width="400" height="400" fill="url(#bgGrad)"/>

    <g id="grid-and-bg">
        <line x1="200" y1="0" x2="200" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="10 10"/>
        <line x1="0" y1="190" x2="400" y2="190" stroke="#1e293b" stroke-width="1" stroke-dasharray="10 10"/>
        
        <circle cx="200" cy="190" r="160" fill="none" stroke="#1e293b" stroke-width="0.5"/>
        <circle cx="200" cy="190" r="120" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="2 12"/>
        
        <polygon points="200,50 299,91 340,190 299,289 200,330 101,289 60,190 101,91" fill="none" stroke="#334155" stroke-width="1"/>
        <polygon transform="rotate(22.5 200 190)" points="200,70 284,105 320,190 284,275 200,310 116,275 80,190 116,105" fill="none" stroke="#1e293b" stroke-width="1.5"/>

        <text x="15" y="35" fill="#475569" font-family="monospace" font-size="10">SYS.INIT(1)</text>
        <polyline points="75,32 85,42 120,42" fill="none" stroke="#334155" stroke-width="1"/>
        
        <text x="325" y="380" fill="#475569" font-family="monospace" font-size="10">0xA9F2</text>
        <polyline points="320,377 310,367 270,367" fill="none" stroke="#334155" stroke-width="1"/>

        <text x="330" y="35" fill="#475569" font-family="monospace" font-size="10">LLM_CORE</text>
        <text x="15" y="380" fill="#38bdf8" opacity="0.6" font-family="monospace" font-size="10" filter="url(#neonSubtle)">A.I. AWAKE</text>
    </g>

    <circle cx="200" cy="190" r="85" fill="url(#coreGlow)" opacity="0.7" filter="url(#neon)"/>

    <g id="neck-and-spine">
        <path d="M 170,400 C 170,370 185,380 185,340" fill="none" stroke="#334155" stroke-width="4"/>
        <path d="M 230,400 C 230,370 215,380 215,340" fill="none" stroke="#334155" stroke-width="4"/>
        <path d="M 150,400 C 150,350 185,360 185,320" fill="none" stroke="#0ea5e9" stroke-width="1" stroke-dasharray="4 4"/>
        <path d="M 250,400 C 250,350 215,360 215,320" fill="none" stroke="#0ea5e9" stroke-width="1" stroke-dasharray="4 4"/>

        <rect x="185" y="320" width="30" height="80" fill="url(#metalDark)" stroke="#1e293b" stroke-width="2"/>
        <line x1="180" y1="340" x2="220" y2="340" stroke="#0ea5e9" stroke-width="1.5" filter="url(#neonSubtle)"/>
        <line x1="185" y1="355" x2="215" y2="355" stroke="#38bdf8" stroke-width="1.5" filter="url(#neonSubtle)"/>
        <line x1="180" y1="370" x2="220" y2="370" stroke="#0ea5e9" stroke-width="1.5" filter="url(#neonSubtle)"/>
    </g>

    <g id="outer-plates">
        <polygon points="200,40 90,110 70,210 130,320 200,380 200,310 140,260 120,200 140,130 200,90" fill="url(#metalLeft)" stroke="#0ea5e9" stroke-width="0.75"/>
        <polygon points="200,40 310,110 330,210 270,320 200,380 200,310 260,260 280,200 260,130 200,90" fill="url(#metalRight)" stroke="#0ea5e9" stroke-width="0.75"/>
    </g>

    <g id="inner-plates">
        <polygon points="200,90 140,130 120,200 140,260 200,310 200,260 155,220 155,160 200,120" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
        <polygon points="200,90 260,130 280,200 260,260 200,310 200,260 245,220 245,160 200,120" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    </g>

    <g id="face-details">
        <polyline points="140,130 110,160 110,190" fill="none" stroke="#38bdf8" stroke-width="1" opacity="0.6"/>
        <polyline points="260,130 290,160 290,190" fill="none" stroke="#38bdf8" stroke-width="1" opacity="0.6"/>
        <line x1="130" y1="320" x2="160" y2="290" stroke="#0ea5e9" stroke-width="1.5"/>
        <line x1="270" y1="320" x2="240" y2="290" stroke="#0ea5e9" stroke-width="1.5"/>
        <circle cx="120" cy="200" r="2.5" fill="#22d3ee" filter="url(#neonSubtle)"/>
        <circle cx="280" cy="200" r="2.5" fill="#22d3ee" filter="url(#neonSubtle)"/>
    </g>

    <polygon id="cavity" points="200,120 155,160 155,220 200,260 245,220 245,160" fill="url(#metalDark)"/>

    <g id="ai-core">
        <circle cx="200" cy="190" r="38" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2 6" filter="url(#neonSubtle)"/>
        <circle cx="200" cy="190" r="26" fill="url(#coreGlow)"/>
        <circle cx="200" cy="190" r="16" fill="none" stroke="#e0f2fe" stroke-width="2.5" stroke-dasharray="12 4 4 4" filter="url(#neon)"/>
        <polygon points="200,174 212,192 200,210 188,192" fill="#ffffff" filter="url(#neon)"/>
        <circle cx="200" cy="190" r="3" fill="#020617"/>
    </g>

    <g id="top-bottom-armor">
        <polygon points="200,20 160,70 200,110 240,70" fill="url(#metalRight)" stroke="#38bdf8" stroke-width="1.5" filter="url(#neonSubtle)"/>
        <polygon points="200,390 160,330 200,290 240,330" fill="url(#metalLeft)" stroke="#38bdf8" stroke-width="1.5"/>
        <circle cx="200" cy="65" r="4" fill="#22d3ee" filter="url(#neon)"/>
    </g>

    <g id="generative-waveform">
        <path d="M 160,310 Q 170,285 180,310 T 200,310 T 220,310 T 240,310" fill="none" stroke="#22d3ee" stroke-width="2.5" filter="url(#neon)"/>
        <path d="M 165,310 Q 175,325 185,310 T 205,310 T 225,310 T 235,310" fill="none" stroke="#818cf8" stroke-width="1.5" filter="url(#neonSubtle)"/>
        <line x1="150" y1="310" x2="250" y2="310" stroke="#0ea5e9" stroke-width="0.5" stroke-dasharray="2 4"/>
    </g>

    <g id="data-particles">
        <circle cx="200" cy="100" r="2" fill="#ffffff" filter="url(#neon)"/>
        <circle cx="185" cy="80" r="1.5" fill="#22d3ee" />
        <circle cx="215" cy="70" r="2.5" fill="#a78bfa" filter="url(#neon)"/>
        <circle cx="205" cy="45" r="1" fill="#ffffff" />
        <circle cx="170" cy="55" r="2" fill="#38bdf8" filter="url(#neonSubtle)"/>
        <circle cx="230" cy="35" r="1.5" fill="#818cf8" />
        <circle cx="195" cy="15" r="2.5" fill="#22d3ee" filter="url(#neon)"/>
        <circle cx="180" cy="35" r="1" fill="#e0f2fe" />
    </g>
</svg>