```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="lightblue"/>
    <circle cx="200" cy="200" r="100" fill="yellow" stroke="orange" stroke-width="5"/>
    <rect x="150" y="150" width="100" height="100" fill="red" opacity="0.6"/>
    <polygon points="200,40 250,150 150,150" fill="purple"/>

    <line x1="50" y1="350" x2="350" y2="50" stroke="black" stroke-width="3" stroke-dasharray="5,5"/>
    <line x1="50" y1="50" x2="350" y2="350" stroke="black" stroke-width="3" stroke-dasharray="5,5"/>

    <text x="200" y="380" font-family="Verdana" font-size="20" text-anchor="middle" fill="darkblue">SVG Artwork</text>
    
    <defs>
        <radialGradient id="grad1" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
            <stop offset="0%" style="stop-color:rgb(255,255,255);stop-opacity:0" />
            <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
        </radialGradient>
    </defs>
    
    <ellipse cx="200" cy="300" rx="80" ry="40" fill="url(#grad1)" />
    
    <g transform="translate(320, 100) rotate(45)">
        <rect x="0" y="0" width="40" height="40" fill="green"/>
        <circle cx="20" cy="60" r="15" fill="pink"/>
    </g>

    <path d="M 100 250 Q 150 200 200 250 T 300 250" stroke="brown" fill="transparent" stroke-width="3"/>
    <path d="M 100 270 Q 150 220 200 270 T 300 270" stroke="brown" fill="transparent" stroke-width="3"/>
    
    <g fill="black">
        <circle cx="160" cy="180" r="5"/>
        <circle cx="240" cy="180" r="5"/>
    </g>
    
    <path d="M 140 210 C 170 240, 230 240, 260 210" stroke="black" fill="none" stroke-width="2"/>
    
</svg>
```