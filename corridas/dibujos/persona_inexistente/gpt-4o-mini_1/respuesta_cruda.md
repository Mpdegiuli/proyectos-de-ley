```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="skinGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f6d7c1;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#e2b19b;stop-opacity:1" />
        </linearGradient>
        <radialGradient id="hairGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
            <stop offset="0%" style="stop-color:#42210f;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#311309;stop-opacity:1" />
        </radialGradient>
        <radialGradient id="shirtGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
            <stop offset="0%" style="stop-color:#4a90e2;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#356ab4;stop-opacity:1" />
        </radialGradient>
    </defs>
    <circle cx="200" cy="100" r="50" fill="url(#skinGradient)" />
    <ellipse cx="200" cy="130" rx="80" ry="50" fill="url(#shirtGradient)" />
    <rect x="160" y="180" width="80" height="150" fill="url(#shirtGradient)" />
    <line x1="160" y1="180" x2="100" y2="280" stroke="#f6d7c1" stroke-width="20" />
    <line x1="240" y1="180" x2="300" y2="280" stroke="#f6d7c1" stroke-width="20" />
    <line x1="160" y1="330" x2="100" y2="400" stroke="#000" stroke-width="15" />
    <line x1="240" y1="330" x2="300" y2="400" stroke="#000" stroke-width="15" />
    <circle cx="180" cy="90" r="5" fill="#000" />
    <circle cx="220" cy="90" r="5" fill="#000" />
    <path d="M 180 110 Q 200 120 220 110" stroke="#000" stroke-width="3" fill="none" />
    <path d="M 150 130 Q 200 150 250 130" fill="#fff" />
    <ellipse cx="200" cy="200" rx="20" ry="10" fill="url(#hairGradient)" />
    <ellipse cx="180" cy="85" rx="60" ry="30" fill="url(#hairGradient)" />
</svg>
```