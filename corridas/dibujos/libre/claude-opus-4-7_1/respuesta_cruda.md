```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sky" cx="30%" cy="30%" r="90%">
      <stop offset="0%" stop-color="#1a1040"/>
      <stop offset="50%" stop-color="#4a1e6b"/>
      <stop offset="100%" stop-color="#8b2e5f"/>
    </radialGradient>
    <radialGradient id="moon" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fff8e0"/>
      <stop offset="100%" stop-color="#e8c060"/>
    </radialGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a1850"/>
      <stop offset="100%" stop-color="#0a0820"/>
    </linearGradient>
    <linearGradient id="mountain" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a1a4a"/>
      <stop offset="100%" stop-color="#140a28"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff8e0" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#fff8e0" stop-opacity="0"/>
    </radialGradient>
  </defs>
  
  <!-- Cielo -->
  <rect width="400" height="400" fill="url(#sky)"/>
  
  <!-- Estrellas -->
  <g fill="white">
    <circle cx="40" cy="50" r="1.2"/>
    <circle cx="80" cy="30" r="0.8"/>
    <circle cx="120" cy="70" r="1"/>
    <circle cx="170" cy="40" r="0.6"/>
    <circle cx="220" cy="25" r="1.1"/>
    <circle cx="260" cy="60" r="0.7"/>
    <circle cx="310" cy="35" r="0.9"/>
    <circle cx="350" cy="80" r="1"/>
    <circle cx="380" cy="45" r="0.6"/>
    <circle cx="20" cy="120" r="0.8"/>
    <circle cx="60" cy="150" r="0.5"/>
    <circle cx="330" cy="130" r="0.9"/>
    <circle cx="370" cy="160" r="0.7"/>
    <circle cx="140" cy="110" r="0.6"/>
    <circle cx="190" cy="90" r="0.8"/>
  </g>
  
  <!-- Resplandor de la luna -->
  <circle cx="290" cy="110" r="80" fill="url(#glow)"/>
  
  <!-- Luna -->
  <circle cx="290" cy="110" r="45" fill="url(#moon)"/>
  <circle cx="275" cy="100" r="6" fill="#d0a040" opacity="0.4"/>
  <circle cx="300" cy="120" r="4" fill="#d0a040" opacity="0.3"/>
  <circle cx="285" cy="125" r="3" fill="#d0a040" opacity="0.3"/>
  
  <!-- Montañas lejanas -->
  <path d="M 0 260 L 60 210 L 110 240 L 160 200 L 220 235 L 280 205 L 340 230 L 400 215 L 400 280 L 0 280 Z" fill="url(#mountain)" opacity="0.8"/>
  
  <!-- Mar -->
  <rect x="0" y="275" width="400" height="125" fill="url(#sea)"/>
  
  <!-- Reflejo de la luna en el agua -->
  <ellipse cx="290" cy="285" rx="35" ry="3" fill="#fff8e0" opacity="0.5"/>
  <ellipse cx="290" cy="300" rx="25" ry="2" fill="#fff8e0" opacity="0.3"/>
  <ellipse cx="290" cy="315" rx="40" ry="2" fill="#fff8e0" opacity="0.25"/>
  <ellipse cx="290" cy="330" rx="30" ry="1.5" fill="#fff8e0" opacity="0.2"/>
  <ellipse cx="290" cy="345" rx="45" ry="1.5" fill="#fff8e0" opacity="0.15"/>
  <ellipse cx="290" cy="360" rx="35" ry="1" fill="#fff8e0" opacity="0.1"/>
  
  <!-- Ondas del mar -->
  <g stroke="#6a4080" stroke-width="0.5" fill="none" opacity="0.4">
    <path d="M 20 310 Q 40 308 60 310 T 100 310"/>
    <path d="M 150 325 Q 170 323 190 325 T 230 325"/>
    <path d="M 50 350 Q 70 348 90 350 T 130 350"/>
    <path d="M 240 345 Q 260 343 280 345 T 320 345"/>
    <path d="M 330 370 Q 350 368 370 370 T 395 370"/>
  </g>
  
  <!-- Barco -->
  <g transform="translate(100, 290)">
    <path d="M -20 10 L 20 10 L 15 20 L -15 20 Z" fill="#2a1810"/>
    <line x1="0" y1="10" x2="0" y2="-25" stroke="#3a2820" stroke-width="1.5"/>
    <path d="M 0 -25 L 0 5 L 12 5 Z" fill="#f0e8d0" opacity="0.9"/>
    <path d="M 0 -22 L 0 2 L -10 2 Z" fill="#e8dcc0" opacity="0.85"/>
  </g>
</svg>
```