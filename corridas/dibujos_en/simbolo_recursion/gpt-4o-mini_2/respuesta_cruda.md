```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ff6f61;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#6a5acd;stop-opacity:1" />
    </linearGradient>
    <filter id="f1" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="5" />
      <feOffset dx="0" dy="0" result="blur" />
      <feMerge>
        <feMergeNode />
        <feMergeNode in="blur" />
      </feMerge>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" />
  <circle cx="200" cy="200" r="150" fill="url(#grad1)" filter="url(#f1)" />
  <path d="M200,145 L210,135 C220,125 230,145 240,135 C250,125 260,145 260,145 C270,155 260,165 250,160 C240,155 225,145 200,145 Z" 
        fill="#ffffff" />
  <path d="M200,255 L190,265 C180,275 170,255 160,265 C150,275 140,255 140,255 C130,245 140,235 150,240 C160,245 175,255 200,255 Z" 
        fill="#ffffff" />
  <path d="M145,200 L135,190 C125,180 145,170 135,160 C125,150 145,140 145,140 C155,130 165,140 160,150 C155,160 145,175 145,200 Z" 
        fill="#ffffff" />
  <path d="M255,200 L265,190 C275,180 255,170 265,160 C275,150 255,140 255,140 C245,130 235,140 240,150 C245,160 255,175 255,200 Z" 
        fill="#ffffff" />
  <path d="M200,70 C220,80 150,120 200,150 C250,180 180,220 200,230 C220,240 190,240 200,255 C210,270 180,260 200,275 C220,290 210,250 220,230 C230,210 200,270 180,250 C160,230 180,200 200,210 C220,220 210,180 230,195 C250,220 200,250 200,250 C200,250 250,220 200,210 Z"
        fill="none" stroke="#ffffff" stroke-width="5" />
  <circle cx="200" cy="200" r="50" fill="none" stroke="#ffffff" stroke-width="8" />
  <path d="M200,200 Q180,170 150,200 T100,200" fill="none" stroke="#ffffff" stroke-width="5" />
  <path d="M200,200 Q220,170 250,200 T300,200" fill="none" stroke="#ffffff" stroke-width="5" />
  <circle cx="200" cy="200" r="10" fill="#ff6f61" />
</svg>
```