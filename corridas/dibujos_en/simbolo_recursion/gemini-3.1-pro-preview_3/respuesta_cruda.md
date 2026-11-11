<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" stroke-linecap="round" stroke-linejoin="round">
<rect width="400" height="400" fill="#0A0E17"/>
<defs>
    <polygon id="arr" points="-12,-16 12,-16 0,0"/>
    
    <g id="t0">
        <line x1="0" y1="0" x2="0" y2="-80" stroke="rgba(100,200,255,0.15)" stroke-width="8"/>
        <circle cx="0" cy="-80" r="10" fill="rgba(100,200,255,0.3)"/>
    </g>
    <g id="t1"><line x1="0" y1="0" x2="0" y2="-80" stroke="rgba(100,200,255,0.15)" stroke-width="8"/><g transform="translate(0,-80) scale(0.7) rotate(40)"><use href="#t0"/></g><g transform="translate(0,-80) scale(0.7) rotate(-40)"><use href="#t0"/></g></g>
    <g id="t2"><line x1="0" y1="0" x2="0" y2="-80" stroke="rgba(100,200,255,0.15)" stroke-width="8"/><g transform="translate(0,-80) scale(0.7) rotate(40)"><use href="#t1"/></g><g transform="translate(0,-80) scale(0.7) rotate(-40)"><use href="#t1"/></g></g>
    <g id="t3"><line x1="0" y1="0" x2="0" y2="-80" stroke="rgba(100,200,255,0.15)" stroke-width="8"/><g transform="translate(0,-80) scale(0.7) rotate(40)"><use href="#t2"/></g><g transform="translate(0,-80) scale(0.7) rotate(-40)"><use href="#t2"/></g></g>
    <g id="t4"><line x1="0" y1="0" x2="0" y2="-80" stroke="rgba(100,200,255,0.15)" stroke-width="8"/><g transform="translate(0,-80) scale(0.7) rotate(40)"><use href="#t3"/></g><g transform="translate(0,-80) scale(0.7) rotate(-40)"><use href="#t3"/></g></g>
    <g id="t5"><line x1="0" y1="0" x2="0" y2="-80" stroke="rgba(100,200,255,0.15)" stroke-width="8"/><g transform="translate(0,-80) scale(0.7) rotate(40)"><use href="#t4"/></g><g transform="translate(0,-80) scale(0.7) rotate(-40)"><use href="#t4"/></g></g>

    <g id="lvl0">
        <rect x="-200" y="0" width="400" height="400" rx="30" fill="rgba(0,255,204,0.05)" stroke="#00ffcc" stroke-width="8"/>
        <line x1="0" y1="0" x2="0" y2="160" stroke="#fff" stroke-width="8"/>
        <use href="#arr" x="0" y="160" fill="#fff"/>
        <circle cx="0" cy="200" r="40" fill="rgba(255,234,0,0.2)" stroke="#ffea00" stroke-width="8"/>
        <circle cx="0" cy="200" r="15" fill="#ffea00"/>
        <line x1="0" y1="240" x2="0" y2="400" stroke="#fff" stroke-width="8"/>
        <use href="#arr" x="0" y="400" fill="#fff"/>
    </g>

    <g id="paths">
        <rect x="-200" y="0" width="400" height="400" rx="30" fill="rgba(0,255,204,0.05)" stroke="#00ffcc" stroke-width="8"/>
        <line x1="0" y1="0" x2="0" y2="30" stroke="#fff" stroke-width="8"/>
        <use href="#arr" x="0" y="30" fill="#fff"/>
        <polygon points="0,30 40,70 0,110 -40,70" fill="rgba(255,0,127,0.15)" stroke="#ff007f" stroke-width="8"/>
        <path d="M -40 70 L -160 70 L -160 360 L 0 360" fill="none" stroke="#ffea00" stroke-width="8"/>
        <use href="#arr" x="-160" y="215" fill="#ffea00"/>
        <line x1="0" y1="110" x2="0" y2="140" stroke="#fff" stroke-width="8"/>
        <line x1="0" y1="360" x2="0" y2="400" stroke="#fff" stroke-width="8"/>
        <use href="#arr" x="0" y="400" fill="#fff"/>
    </g>

    <g id="lvl1"><use href="#paths"/><g transform="translate(0, 140) scale(0.55)"><use href="#lvl0"/></g></g>
    <g id="lvl2"><use href="#paths"/><g transform="translate(0, 140) scale(0.55)"><use href="#lvl1"/></g></g>
    <g id="lvl3"><use href="#paths"/><g transform="translate(0, 140) scale(0.55)"><use href="#lvl2"/></g></g>
    <g id="lvl4"><use href="#paths"/><g transform="translate(0, 140) scale(0.55)"><use href="#lvl3"/></g></g>
</defs>

<use href="#t5" x="200" y="390"/>

<g transform="translate(200, 20) scale(0.9)">
    <line x1="0" y1="-25" x2="0" y2="0" stroke="#fff" stroke-width="8"/>
    <use href="#lvl4"/>
</g>
</svg>