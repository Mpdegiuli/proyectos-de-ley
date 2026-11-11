```xml
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#FFFFFF" stroke-opacity="0.04" stroke-width="1"/>
    </pattern>
    <g id="r">
      <rect x="0" y="0" width="360" height="360" rx="20" fill="#090A0F" stroke="currentColor" stroke-width="8"/>
      <line x1="180" y1="-16" x2="180" y2="10" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>
      <polygon points="180,18 172,4 180,8 188,4" fill="currentColor"/>
      
      <polygon points="180,25 215,55 180,85 145,55" fill="none" stroke="currentColor" stroke-width="6"/>
      
      <polyline points="145,55 60,55 60,240" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/>
      <polygon points="60,248 52,234 60,238 68,234" fill="currentColor"/>
      <circle cx="60" cy="268" r="16" fill="#090A0F" stroke="currentColor" stroke-width="6"/>
      <circle cx="60" cy="268" r="6" fill="currentColor"/>
      
      <polyline points="215,55 300,55 300,65" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/>
      <rect x="270" y="65" width="60" height="40" fill="#090A0F" stroke="currentColor" stroke-width="6"/>
      <line x1="282" y1="65" x2="282" y2="105" stroke="currentColor" stroke-width="3"/>
      <line x1="318" y1="65" x2="318" y2="105" stroke="currentColor" stroke-width="3"/>
      
      <polyline points="300,105 300,135 180,135 180,152" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/>
    </g>
  </defs>
  
  <rect width="400" height="400" fill="#090A0F"/>
  <rect width="400" height="400" fill="url(#grid)"/>
  
  <g transform="translate(20, 20)" color="#FF0055">
    <use href="#r"/>
    
    <g transform="translate(90, 160) scale(0.5)" color="#BF00FF">
      <use href="#r"/>
      
      <g transform="translate(90, 160) scale(0.5)" color="#0080FF">
        <use href="#r"/>
        
        <g transform="translate(90, 160) scale(0.5)" color="#00FFCC">
          <use href="#r"/>
          
          <g transform="translate(90, 160) scale(0.5)" color="#00FF00">
            <use href="#r"/>
            
            <g transform="translate(90, 160) scale(0.5)" color="#FFFF00">
              <rect x="0" y="0" width="360" height="360" rx="20" fill="#090A0F" stroke="currentColor" stroke-width="8"/>
              <line x1="180" y1="-16" x2="180" y2="10" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>
              <polygon points="180,18 172,4 180,8 188,4" fill="currentColor"/>
              <circle cx="180" cy="180" r="40" fill="currentColor"/>
              <circle cx="180" cy="180" r="60" fill="none" stroke="currentColor" stroke-width="8"/>
            </g>
          </g>
        </g>
      </g>
    </g>
  </g>
</svg>
```