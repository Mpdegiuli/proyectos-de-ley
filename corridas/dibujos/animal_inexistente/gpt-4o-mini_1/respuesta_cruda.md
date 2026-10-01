```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="grad1" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
            <stop offset="0%" style="stop-color:#ffcc00; stop-opacity:1" />
            <stop offset="100%" style="stop-color:#ff9900; stop-opacity:1" />
        </radialGradient>
        <radialGradient id="grad2" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
            <stop offset="0%" style="stop-color:#008080; stop-opacity:1" />
            <stop offset="100%" style="stop-color:#004d4d; stop-opacity:1" />
        </radialGradient>
    </defs>
    <g id="creature">
        <ellipse cx="200" cy="220" rx="80" ry="50" fill="url(#grad1)" />
        <ellipse cx="150" cy="210" rx="40" ry="25" fill="url(#grad2)" />
        <ellipse cx="250" cy="210" rx="40" ry="25" fill="url(#grad2)" />
        <path d="M200,250 Q160,280 130,250 Q160,300 200,290 Q240,300 270,250 Q240,280 200,250" fill="#a0522d" />
        <path d="M170,270 Q150,290 120,260" fill="#a0522d" />
        <path d="M230,270 Q250,290 280,260" fill="#a0522d" />
        <circle cx="160" cy="200" r="15" fill="#fff" />
        <circle cx="240" cy="200" r="15" fill="#fff" />
        <circle cx="160" cy="200" r="7" fill="#000" />
        <circle cx="240" cy="200" r="7" fill="#000" />
        <path d="M 180 220 Q 200 240 220 220" stroke="black" stroke-width="2" fill="none" />
        <path d="M 200 240 Q 180 260 200 260 Q 220 260 200 240" fill="blue" />
        <path d="M120,150 Q100,100 150,150" fill="none" stroke="purple" stroke-width="3" />
        <path d="M280,150 Q300,100 250,150" fill="none" stroke="purple" stroke-width="3" />

        <g id="tails">
            <path d="M 80 250 Q 50 270 100 300" stroke="#a0522d" stroke-width="5" fill="none" />
            <path d="M 320 250 Q 350 270 300 300" stroke="#a0522d" stroke-width="5" fill="none" />
        </g>
    </g>
</svg>
```