```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="heavy-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <marker id="arrow-call" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 Z" fill="#FF007F" />
    </marker>

    <marker id="arrow-return" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 Z" fill="#FFEA00" />
    </marker>
    
    <g id="base-case">
      <circle cx="0" cy="0" r="3.5" fill="#39FF14" filter="url(#glow)"/>
    </g>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="#070714"/>
  <rect x="10" y="10" width="380" height="380" rx="12" fill="#0A0A1A" stroke="#1F1F33" stroke-width="2"/>
  
  <g filter="url(#glow)">
    <circle cx="28" cy="26" r="4.5" fill="#FF5F56"/>
    <circle cx="46" cy="26" r="4.5" fill="#FFBD2E"/>
    <circle cx="64" cy="26" r="4.5" fill="#27C93F"/>
  </