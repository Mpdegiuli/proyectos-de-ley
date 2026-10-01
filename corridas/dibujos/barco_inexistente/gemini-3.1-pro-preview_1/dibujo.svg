<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
    <defs>
        <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#030108"/>
            <stop offset="40%" stop-color="#0a0520"/>
            <stop offset="100%" stop-color="#001226"/>
        </linearGradient>

        <linearGradient id="planetGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#ff007f"/>
            <stop offset="40%" stop-color="#3a0ca3"/>
            <stop offset="100%" stop-color="#000000"/>
        </linearGradient>

        <linearGradient id="hullBase" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#0f0c29"/>
            <stop offset="50%" stop-color="#302b63"/>
            <stop offset="100%" stop-color="#141424"/>
        </linearGradient>
        
        <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#f6d365"/>
            <stop offset="100%" stop-color="#ffb199"/>
        </linearGradient>

        <linearGradient id="cyanGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#00f2fe"/>
            <stop offset="100%" stop-color="#4facfe"/>
        </linearGradient>
        
        <linearGradient id="magentaGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#ff0844"/>
            <stop offset="100%" stop-color="#ffb199"/>
        </linearGradient>

        <linearGradient id="yellowGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#f6d365"/>
            <stop offset="100%" stop-color="#fda085"/>
        </linearGradient>

        <linearGradient id="shoot" x1="1" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
            <stop offset="100%" stop-color="#00f2fe" stop-opacity="0"/>
        </linearGradient>

        <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="3" result="blur"/>
            <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>

        <filter id="nebula" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="25"/>
        </filter>
    </defs>

    <rect width="400" height="400" fill="url(#bg)"/>

    <circle cx="80" cy="100" r="90" fill="#9d00ff" filter="url(#nebula)" opacity="0.25"/>
    <circle cx="320" cy="180" r="110" fill="#00e5ff" filter="url(#nebula)" opacity="0.2"/>
    <circle cx="200" cy="280" r="100" fill="#ff007f" filter="url(#nebula)" opacity="0.15"/>

    <path d="M20,40h1.5v1.5h-1.5z M80,90h1v1h-1z M150,30h2v2h-2z M220,110h1.5v1.5h-1.5z M310,50h2v2h-2z M370,120h1v1h-1z M40,180h1v1h-1z M110,210h2v2h-2z M280,40h1v1h-1z M350,190h1.5v1.5h-1.5z M10,140h1.5v1.5h-1.5z M190,160h1v1h-1z" fill="#ffffff" opacity="0.7"/>

    <path d="M 350,20 L 230,80" stroke="url(#shoot)" stroke-width="2" filter="url(#glow)"/>
    <path d="M 380,50 L 290,95" stroke="url(#shoot)" stroke-width="1" filter="url(#glow)" opacity="0.6"/>

    <circle cx="350" cy="100" r="120" fill="url(#planetGrad)" opacity="0.6"/>
    <ellipse cx="350" cy="100" rx="190" ry="35" fill="none" stroke="#00f2fe" stroke-width="1.5" opacity="0.4" transform="rotate(-15 350 100)"/>
    <ellipse cx="350" cy="100" rx="170" ry="25" fill="none" stroke="#ff007f" stroke-width="0.8" opacity="0.3" transform="rotate(-15 350 100)"/>

    <rect x="0" y="285" width="400" height="115" fill="#04020a" opacity="0.85"/>
    <ellipse cx="200" cy="285" rx="200" ry="12" fill="#00f2fe" filter="url(#nebula)" opacity="0.7"/>

    <path d="M 200,285 L -50,400 M 200,285 L 30,400 M 200,285 L 110,400 M 200,285 L 190,400 M 200,285 L 270,400 M 200,285 L 350,400 M 200,285 L 450,400" stroke="#00e5ff" stroke-width="0.5" opacity="0.3"/>
    
    <path d="M -50,305 Q 200,290 450,305" stroke="url(#cyanGrad)" stroke-width="1.5" fill="none" opacity="0.7" filter="url(#glow)"/>
    <path d="M -50,325 Q 200,310 450,325" stroke="url(#magentaGrad)" stroke-width="2" fill="none" opacity="0.5"/>
    <path d="M -50,355 Q 200,335 450,355" stroke="url(#cyanGrad)" stroke-width="3" fill="none" opacity="0.4" filter="url(#glow)"/>
    <path d="M -50,395 Q 200,365 450,395" stroke="url(#magentaGrad)" stroke-width="4" fill="none" opacity="0.3"/>

    <g transform="translate(0, 570) scale(1, -1)" opacity="0.25" filter="url(#glow)">
        <path d="M 50,240 Q 100,290 220,290 T 380,250 Q 250,270 150,240 Q 100,220 50,240 Z" fill="url(#cyanGrad)"/>
        <path d="M 162,50 C 280,80 340,160 270,275 Z" fill="url(#magentaGrad)"/>
    </g>

    <path d="M 50,240 Q 100,290 220,290 T 380,250 Q 250,270 150,240 Q 100,220 50,240 Z" fill="url(#hullBase)"/>
    <path d="M 60,243 Q 105,285 220,285 T 365,250 Q 250,265 150,243 Q 100,225 60,243 Z" fill="url(#gold)"/>
    
    <path d="M 120,265 L 125,270 L 135,265 L 140,270" stroke="#00f2fe" fill="none" stroke-width="1.2" filter="url(#glow)"/>
    <path d="M 170,272 L 175,277 L 185,272" stroke="#ff0844" fill="none" stroke-width="1.2" filter="url(#glow)"/>
    <path d="M 380,250 Q 395,245 405,240" stroke="#00f2fe" stroke-width="2" fill="none" filter="url(#glow)"/>
    <path d="M 380,250 Q 390,255 405,258" stroke="#ff0844" stroke-width="1.5" fill="none" filter="url(#glow)"/>

    <circle cx="50" cy="240" r="8" fill="#00f2fe" filter="url(#glow)"/>
    <circle cx="50" cy="240" r="3" fill="#ffffff"/>
    <path d="M 42,240 L 10,235 M 45,245 L 15,250" stroke="#00f2fe" stroke-width="1.5" filter="url(#glow)"/>
    
    <circle cx="120" cy="293" r="4" fill="#ff0844" filter="url(#glow)"/>
    <circle cx="200" cy="305" r="5" fill="#00f2fe" filter="url(#glow)"/>
    <circle cx="280" cy="293" r="3" fill="#ff0844" filter="url(#glow)"/>

    <circle cx="160" cy="240" r="18" fill="none" stroke="url(#gold)" stroke-width="1.5"/>
    <circle cx="160" cy="240" r="12" fill="none" stroke="#00f2fe" stroke-width="1" transform="rotate(60 160 240) scale(1, 0.4)"/>
    <circle cx="160" cy="240" r="12" fill="none" stroke="#ff0844" stroke-width="1" transform="rotate(-60 160 240) scale(1, 0.4)"/>
    <circle cx="160" cy="240" r="3" fill="#ffffff" filter="url(#glow)"/>

    <path d="M 158,260 L 158,40 L 162,40 L 162,260 Z" fill="url(#gold)"/>

    <path d="M 162,50 C 280,80 340,160 270,275 C 230,200 200,120 162,50 Z" fill="url(#cyanGrad)" filter="url(#glow)" opacity="0.6"/>
    <path d="M 162,50 Q 230,130 270,275" stroke="#ffffff" fill="none" stroke-width="1" opacity="0.6"/>
    <path d="M 162,50 Q 260,150 270,275" stroke="#ffffff" fill="none" stroke-width="0.75" opacity="0.4"/>
    <path d="M 162,50 Q 285,170 270,275" stroke="#ffffff" fill="none" stroke-width="0.5" opacity="0.3"/>

    <path d="M 162,120 C 300,140 370,190 330,260 C 280,225 220,180 162,120 Z" fill="url(#yellowGrad)" filter="url(#glow)" opacity="0.5"/>
    <path d="M 162,120 Q 260,170 330,260" stroke="#ffffff" fill="none" stroke-width="0.8" opacity="0.5"/>

    <path d="M 158,80 C 80,100 30,160 70,245 C 100,200 130,140 158,80 Z" fill="url(#magentaGrad)" filter="url(#glow)" opacity="0.65"/>
    <path d="M 158,80 Q 110,160 70,245" stroke="#ffffff" fill="none" stroke-width="1" opacity="0.5"/>
    <path d="M 158,80 Q 85,170 70,245" stroke="#ffffff" fill="none" stroke-width="0.5" opacity="0.3"/>

    <polygon points="160,15 165,30 180,35 165,40 160,55 155,40 140,35 155,30" fill="url(#cyanGrad)" filter="url(#glow)"/>
    <polygon points="160,22 162,32 170,35 162,38 160,48 158,38 150,35 158,32" fill="#ffffff"/>

    <g fill="#ffffff" filter="url(#glow)">
        <circle cx="280" cy="150" r="1.5"/>
        <circle cx="320" cy="200" r="2"/>
        <circle cx="250" cy="110" r="1"/>
        <circle cx="350" cy="230" r="1.5"/>
        <circle cx="90" cy="140" r="2"/>
        <circle cx="60" cy="190" r="1.5"/>
        <circle cx="120" cy="100" r="1.2"/>
        <circle cx="200" cy="60" r="2"/>
        <circle cx="230" cy="40" r="1"/>
    </g>

    <path d="M 140,248 L 140,238 A 2 2 0 1 1 144,238 L 144,248 Z" fill="#ffffff" opacity="0.9"/>
    <circle cx="142" cy="235" r="2" fill="#00f2fe" filter="url(#glow)"/>
</svg>