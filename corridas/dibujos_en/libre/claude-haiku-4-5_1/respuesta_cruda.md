```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background gradient -->
  <defs>
    <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#E0F6FF;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="sunGradient">
      <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FFA500;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <!-- Sky background -->
  <rect width="400" height="400" fill="url(#skyGradient)"/>
  
  <!-- Sun -->
  <circle cx="320" cy="80" r="35" fill="url(#sunGradient)"/>
  <circle cx="320" cy="80" r="32" fill="#FFD700" opacity="0.8"/>
  
  <!-- Clouds -->
  <g opacity="0.85">
    <ellipse cx="60" cy="60" rx="25" ry="18" fill="white"/>
    <ellipse cx="85" cy="65" rx="30" ry="20" fill="white"/>
    <ellipse cx="40" cy="75" rx="20" ry="15" fill="white"/>
  </g>
  
  <g opacity="0.8">
    <ellipse cx="280" cy="120" rx="28" ry="19" fill="white"/>
    <ellipse cx="310" cy="125" rx="32" ry="22" fill="white"/>
    <ellipse cx="255" cy="135" rx="22" ry="16" fill="white"/>
  </g>
  
  <!-- Mountains -->
  <polygon points="0,250 100,120 200,250" fill="#8B7355"/>
  <polygon points="150,250 250,100 350,250" fill="#A0826D"/>
  <polygon points="300,250 380,140 400,250" fill="#9B8B7E"/>
  
  <!-- Snow caps on mountains -->
  <polygon points="100,120 80,150 120,150" fill="white"/>
  <polygon points="250,100 225,145 275,145" fill="white"/>
  <polygon points="380,140 365,160 395,160" fill="white"/>
  
  <!-- Forest -->
  <g fill="#2D5016">
    <!-- Pine trees -->
    <polygon points="50,250 40,280 60,280"/>
    <polygon points="50,265 35,295 65,295"/>
    <polygon points="50,280 30,310 70,310"/>
    
    <polygon points="150,250 135,285 165,285"/>
    <polygon points="150,270 130,305 170,305"/>
    <polygon points="150,290 125,320 175,320"/>
    
    <polygon points="320,250 305,285 335,285"/>
    <polygon points="320,270 300,305 340,305"/>
    <polygon points="320,290 295,320 345,320"/>
  </g>
  
  <!-- River -->
  <path d="M 200 320 Q 220 330 210 345 T 200 370" stroke="#4DA6D6" stroke-width="25" fill="none" stroke-linecap="round"/>
  <path d="M 200 320 Q 180 335 190 350 T 200 370" stroke="#5BB3E3" stroke-width="12" fill="none" stroke-linecap="round"/>
  
  <!-- Grass field -->
  <rect x="0" y="330" width="400" height="70" fill="#6BA84F"/>
  
  <!-- Grass details -->
  <g stroke="#5A9640" stroke-width="1.5" opacity="0.6">
    <line x1="20" y1="350" x2="18" y2="365"/>
    <line x1="45" y1="355" x2="43" y2="370"/>
    <line x1="75" y1="352" x2="73" y2="367"/>
    <line x1="110" y1="348" x2="108" y2="363"/>
    <line x1="140" y1="351" x2="138" y2="366"/>
    <line x1="170" y1="349" x2="168" y2="364"/>
    <line x1="205" y1="350" x2="203" y2="365"/>
    <line x1="235" y1="352" x2="233" y2="367"/>
    <line x1="265" y1="350" x2="263" y2="365"/>
    <line x1="295" y1="351" x2="293" y2="366"/>
    <line x1="325" y1="349" x2="323" y2="364"/>
    <line x1="360" y1="352" x2="358" y2="367"/>
  </g>
  
  <!-- Birds in sky -->
  <g stroke="#333" stroke-width="1.5" fill="none" stroke-linecap="round">
    <path d="M 100 140 Q 105 135 110 140"/>
    <path d="M 115 140 Q 120 135 125 140"/>
    
    <path d="M 280 160 Q 285 155 290 160"/>
    <path d="M 295 160 Q 300 155 305 160"/>
  </g>
  
  <!-- Cabin -->
  <rect x="130" y="240" width="70" height="50" fill="#8B4513"/>
  <polygon points="130,240 165,210 200,240" fill="#A0522D"/>
  
  <!-- Cabin door -->
  <rect x="158" y="265" width="14" height="25" fill="#654321"/>
  <circle cx="171" cy="277" r="2" fill="#FFD700"/>
  
  <!-- Cabin windows -->
  <rect x="138" y="250" width="10" height="10" fill="#87CEEB"/>
  <line x1="143" y1="250" x2="143" y2="260"/>
  <line x1="138" y1="255" x2="148" y2="255"/>
  
  <rect x="188" y="250" width="10" height="10" fill="#87CEEB"/>
  <line x1="193" y1="250" x2="193" y2="260"/>
  <line x1="188" y1="255" x2="198" y2="255"/>
  
  <!-- Chimney smoke -->
  <circle cx="155" cy="205" r="4" fill="#C0C0C0" opacity="0.7"/>
  <circle cx="158" cy="195" r="5" fill="#D3D3D3" opacity="0.6"/>
  <circle cx="160" cy="185" r="6" fill="#E8E8E8" opacity="0.5"/>
  <circle cx="161" cy="175" r="6" fill="#F5F5F5" opacity="0.4"/>
</svg>
```