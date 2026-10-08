<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
    <defs>
        <!-- Space & Aura -->
        <radialGradient id="space" cx="50%" cy="50%" r="75%">
            <stop offset="0%" stop-color="#140b2e"/>
            <stop offset="100%" stop-color="#050117"/>
        </radialGradient>
        <radialGradient id="aura" cx="50%" cy="50%" r="50%">
            <stop offset="45%" stop-color="#00f2fe" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#00f2fe" stop-opacity="0"/>
        </radialGradient>
        
        <!-- Planet Elements -->
        <linearGradient id="ocean" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#00f2fe"/>
            <stop offset="100%" stop-color="#0250c5"/>
        </linearGradient>
        <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#43e97b"/>
            <stop offset="100%" stop-color="#f9d423"/>
        </linearGradient>
        
        <!-- Lotus & Cosmos -->
        <linearGradient id="lotusGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ff9a9e"/>
            <stop offset="100%" stop-color="#fecfef"/>
        </linearGradient>
        <linearGradient id="starGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
            <stop offset="100%" stop-color="#ffffff" stop-opacity="1"/>
        </linearGradient>
        
        <!-- Filters -->
        <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="3" result="blur"/>
            <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <filter id="glowBig" x="-30%" y="-30%" width="160%" height="160%">