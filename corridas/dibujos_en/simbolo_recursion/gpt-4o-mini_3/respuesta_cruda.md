```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            .circle { fill: none; stroke: #007bff; stroke-width: 8; }
            .arrow { fill: #007bff; }
            .spiral { fill: none; stroke: #007bff; stroke-width: 3; }
        </style>
    </defs>
    <rect width="100%" height="100%" fill="#f0f0f0"/>
    <circle cx="200" cy="200" r="120" class="circle"/>
    <path d="M200,80 L200,40 M200,80 L230,60 M200,40 L170,60" class="arrow"/>
    <path d="M200,320 L200,360 M200,320 L230,340 M200,360 L170,340" class="arrow"/>
    <path class="spiral" d="M200,200 C220,170, 280,170, 300,200 C320,230, 270,290, 200,290 C130,290, 80,230, 100,200 C120,170, 160,170, 200,200 Z" />
</svg>
```