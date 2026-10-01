```xml
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#050514"/>
            <stop offset="50%" stop-color="#0f172a"/>
            <stop offset="100%" stop-color="#1e1b4b"/>
        </linearGradient>
        <radialGradient id="moonGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#FFF59D"/>
            <stop offset="50%" stop-color="#FFB74D"/>
            <stop offset="100%" stop-color="#F4511E"/>
        </radialGradient>
        <linearGradient id="foxBody" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#FF9800"/>
            <stop offset="40%" stop-color="#FF5722"/>
            <stop offset="100%" stop-color="#BF360C"/>
        </linearGradient>
        <linearGradient id="foxWhite" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#FFFFFF"/>
            <stop offset="100%" stop-color="#B0BEC5"/>
        </linearGradient>
        <linearGradient id="foxDark" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#E65100"/>
            <stop offset="100%" stop-color="#3E2723"/>
        </linearGradient>
    </defs>

    <rect width="400" height="400" fill="url(#skyGrad)"/>

    <path d="M 30 50 h 2 v 2 h -2 Z M 120 30 h 1.5 v 1.5 h -1.5 Z M 250 60 h 2 v 2 h -2 Z M 350 110 h 1 v 1 h -1 Z M 80 150 h 2 v 2 h -2 Z M 160 80 h 1 v 1 h -1 Z M 300 40 h 1.5 v 1.5 h -1.5 Z M 40 200 h 1 v 1 h -1 Z M 380 180 h 2 v 2 h -2 Z M 200 20 h 1 v 1 h -1 Z M 100 110 h 1 v 1 h -1 Z M 280 140 h 1 v 1 h -1 Z M 10 130 h 2 v 2 h -2 Z M 330 200 h 1 v 1 h -1 Z M 180 130 h 2 v 2 h -2 Z" fill="#FFFFFF" opacity="0.6"/>

    <circle cx="200" cy="180" r="140" fill="#FFB74D" opacity="0.1"/>
    <circle cx="200" cy="180" r="100" fill="#FFB74D" opacity="0.2"/>
    <circle cx="200" cy="180" r="80" fill="url(#moonGrad)"/>

    <line x1="360" y1="30" x2="280" y2="110" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" opacity="0.8"/>
    <line x1="360" y1="30" x2="330" y2="60" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.4"/>
    <line x1="80" y1="20" x2="40" y2="60" stroke="#FFFFFF" stroke-width="1" stroke-linecap="round" opacity="0.6"/>

    <rect x="80" y="160" width="100" height="5" rx="2.5" fill="#FFFFFF" opacity="0.15"/>
    <rect x="120" y="180" width="140" height="7" rx="3.5" fill="#FFFFFF" opacity="0.2"/>
    <rect x="220" y="140" width="80" height="4" rx="2" fill="#FFFFFF" opacity="0.15"/>
    <rect x="180" y="210" width="110" height="6" rx="3" fill="#FFFFFF" opacity="0.1"/>
    <rect x="40" y="130" width="60" height="4" rx="2" fill="#FFFFFF" opacity="0.15"/>
    <rect x="280" y="170" width="90" height="5" rx="2.5" fill="#FFFFFF" opacity="0.2"/>

    <g fill="#0B0D17">
        <path d="M 20 180 L 50 250 L 35 250 L 70 330 L -30 330 L 5 250 L -10 250 Z"/>
        <path d="M 90 200 L 115 260 L 100 260 L 135 340 L 45 340 L 80 260 L 65 260 Z"/>
        <path d="M 380 170 L 410 240 L 395 240 L 430 320 L 330 320 L 365 240 L 350 240 Z"/>
        <path d="M 320 190 L 345 250 L 330 250 L 365 330 L 275 330 L 310 250 L 295 250 Z"/>
    </g>

    <g fill="#05060A">
        <path d="M -10 230 L 20 300 L 5 300 L 40 380 L -50 380 L -15 300 L -30 300 Z"/>
        <path d="M 410 210 L 440 280 L 425 280 L 460 360 L 370 360 L 405 280 L 390 280 Z"/>
    </g>

    <path d="M 0 340 Q 100 320 200 340 T 400 340 L 400 400 L 0 400 Z" fill="#05060A"/>

    <circle cx="100" cy="270" r="4" fill="#FFD54F" opacity="0.3"/>
    <circle cx="100" cy="270" r="1.5" fill="#FFFFFF"/>
    <circle cx="310" cy="330" r="3" fill="#FFD54F" opacity="0.3"/>
    <circle cx="310" cy="330" r="1" fill="#FFFFFF"/>
    <circle cx="160" cy="380" r="5" fill="#FFD54F" opacity="0.2"/>
    <circle cx="160" cy="380" r="2" fill="#FFFFFF"/>
    <circle cx="260" cy="390" r="4" fill="#FFD54F" opacity="0.3"/>
    <circle cx="260" cy="390" r="1.5" fill="#FFFFFF"/>

    <path d="M 100 200 C 100 400 300 400 300 200 Z" fill="url(#foxBody)"/>

    <path d="M 300 280 C 380 300 370 380 280 390 C 180 400 60 380 50 320 C 40 260 80 250 100 280 C 70 290 80 360 200 370 C 280 380 340 330 300 280 Z" fill="url(#foxBody)"/>
    <path d="M 50 320 C 40 260 80 250 100 280 C 90 290 80 300 95 310 C 80 315 75 320 85 330 C 70 330 60 325 50 320 Z" fill="url(#foxWhite)"/>

    <g id="foxHead">
        <path d="M 200 360 C 280 360 340 320 340 220 C 340 180 360 100 360 100 C 360 100 320 120 300 140 C 270 110 240 100 200 100 C 160 100 130 110 100 140 C 80 120 40 100 40 100 C 40 100 60 180 60 220 C 60 320 120 360 200 360 Z" fill="url(#foxBody)"/>
        
        <path d="M 100 140 C 110 170 90 190 80 210 C 70 180 60 140 45 105 C 70 120 90 130 100 140 Z" fill="#212121"/>
        <path d="M 300 140 C 290 170 310 190 320 210 C 330 180 340 140 355 105 C 330 120 310 130 300 140 Z" fill="#212121"/>
        <path d="M 55 125 C 65 150 75 160 85 165 C 75 140 65 130 55 125 Z" fill="#FF5722"/>
        <path d="M 345 125 C 335 150 325 160 315 165 C 325 140 335 130 345 125 Z" fill="#FF5722"/>

        <path d="M 200 355 C 260 355 330 300 330 230 C 330 200 300 220 260 230 C 240 235 220 230 200 250 C 180 230 160 235 140 230 C 100 220 70 200 70 230 C 70 300 140 355 200 355 Z" fill="url(#foxWhite)"/>

        <path d="M 200 100 C 230 100 250 120 260 140 C 240 150 220 160 200 180 C 180 160 160 150 140 140 C 150 120 170 100 200 100 Z" fill="url(#foxDark)"/>
        
        <path d="M 200 120 C 220 150 220 200 210 245 C 200 250 200 250 190 245 C 180 200 180 150 200 120 Z" fill="#FFB74D"/>

        <path d="M 185 260 C 195 255 205 255 215 260 C 215 270 205 275 200 275 C 195 275 185 270 185 260 Z" fill="#1A1A1A"/>
        <circle cx="195" cy="262" r="1.5" fill="#FFFFFF" opacity="0.8"/>

        <path d="M 180 220 C 170 200 150 195 140 200 C 150 210 165 215 180 220 Z" fill="#1A1A1A"/>
        <path d="M 220 220 C 230 200 250 195 260 200 C 250 210 235 215 220 220 Z" fill="#1A1A1A"/>

        <circle cx="160" cy="208" r="3.5" fill="#00E5FF"/>
        <circle cx="160" cy="208" r="1.5" fill="#FFFFFF"/>
        <circle cx="240" cy="208" r="3.5" fill="#00E5FF"/>
        <circle cx="240" cy="208" r="1.5" fill="#FFFFFF"/>

        <path d="M 130 260 Q 90 250 60 260" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
        <path d="M 130 270 Q 90 270 50 280" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
        <path d="M 270 260 Q 310 250 340 260" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
        <path d="M 270 270 Q 310 270 350 280" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
    </g>
</svg>
```