<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
    <defs>
        <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="6" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="glow-strong" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="12" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        
        <marker id="arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#FF00AA"/>
        </marker>

        <!-- Syntax blocks to signify "code/logic" -->
        <g id="code-lines">
            <rect x="40" y="-125" width="80" height="12" rx="6" fill="#00FFCC" opacity="0.3"/>
            <rect x="40" y="-105" width="50" height="12" rx="6" fill="#00FFCC" opacity="0.3"/>
            <rect x="-125" y="105" width="90" height="12" rx="6" fill="#00FFCC" opacity="0.3"/>
            <rect x="-125" y="125" width="60" height="12" rx="6" fill="#00FFCC" opacity="0.3"/>
        </g>

        <!-- Base Case (Termination) -->
        <g id="base-case">
            <circle cx="0" cy="0" r="50" fill="#FF00AA" filter="url(#glow-strong)"/>
            <circle cx="0" cy="0" r="25" fill="#FFFFFF"/>
            <path d="M -10 5 L -2 12 L 15 -5" fill="none" stroke="#FF00AA" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
        </g>

        <!-- Recursive Frame Component -->
        <g id="frame-content">
            <rect x="-150" y