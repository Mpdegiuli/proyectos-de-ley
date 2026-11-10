<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .arrow { fill: none; stroke-linecap: round; stroke-linejoin: round; }
    </style>
  </defs>
  
  <!-- Background -->
  <rect width="400" height="400" fill="#1a1a2e"/>
  
  <!-- Recursive spiral made of nested self-similar triangles -->
  <!-- Outer triangle -->
  <polygon points="200,30 370,340 30,340" fill="none" stroke="#4fc3f7" stroke-width="3"/>
  
  <!-- Mid triangle - rotated/scaled inward -->
  <polygon points="200,95 315,300 85,300" fill="none" stroke="#29b6f6" stroke-width="2.5"/>
  
  <!-- Smaller triangle -->
  <polygon points="200,148 268,265 132,265" fill="none" stroke="#0288d1" stroke-width="2"/>
  
  <!-- Even smaller -->
  <polygon points="200,190 232,240 168,240" fill="none" stroke="#0277bd" stroke-width="1.8"/>
  
  <!-- Tiny -->
  <polygon points="200,218 218,248 182,248" fill="none" stroke="#01579b" stroke-width="1.5"/>
  
  <!-- Tiniest visible -->
  <polygon points="200,232 210,250 190,250" fill="none" stroke="#014f8a" stroke-width="1.2"/>
  
  <!-- Circular arrow at the top indicating "call itself" -->
  <!-- This is a looping arrow suggesting recursion -->
  <path d="M 200,30 
            C 240,10 280,30 275,70 
            C 270,100 245,110 220,100" 
        fill="none" stroke="#ff7043" stroke-width="3" stroke-linecap="round"/>
  <!-- Arrowhead pointing back toward triangle apex -->
  <polygon points="220,100 205,88 215,112" fill="#ff7043"/>
  
  <!-- Stack frames visualization on the left side -->
  <!-- Representing call stack -->
  <rect x="20" y="160" width="40" height="18" rx="3" fill="none" stroke="#4fc3f7" stroke-width="1.5"/>
  <rect x="24" y="143" width="34" height="18" rx="3" fill="none" stroke="#29b6f6" stroke-width="1.5"/>
  <rect x="28" y="128" width="28" height="16" rx="3" fill="none" stroke="#0288d1" stroke-width="1.5"/>
  <rect x="31" y="115" width="23" height="14" rx="3" fill="none" stroke="#0277bd" stroke-width="1.5"/>
  <rect x="34" y="104" width="17" height="12" rx="3" fill="none" stroke="#01579b" stroke-width="1.5"/>
  
  <!-- Arrow pointing down on stack (unwinding) -->
  <line x1="40" y1="183" x2="40" y2="205" stroke="#ff7043" stroke-width="2" stroke-linecap="round"/>
  <polygon points="40,210 35,200 45,200" fill="#ff7043"/>
  
  <!-- Fractal tree on the right to reinforce recursion -->
  <g transform="translate(340, 340)">
    <!-- Trunk -->
    <line x1="0" y1="0" x2="0" y2="-50" stroke="#66bb6a" stroke-width="3" stroke-linecap="round"/>
    <!-- Branch level 1 left -->
    <line x1="0" y1="-50" x2="-22" y2="-82" stroke="#66bb6a" stroke-width="2.2" stroke-linecap="round"/>
    <!-- Branch level 1 right -->
    <line x1="0" y1="-50" x2="22" y2="-82" stroke="#66bb6a" stroke-width="2.2" stroke-linecap="round"/>
    <!-- Branch level 2 -->
    <line x1="-22" y1="-82" x2="-33" y2="-102" stroke="#81c784" stroke-width="1.6" stroke-linecap="round"/>
    <line x1="-22" y1="-82" x2="-10" y2="-102" stroke="#81c784" stroke-width="1.6" stroke-linecap="round"/>
    <line x1="22" y1="-82" x2="10" y2="-102" stroke="#81c784" stroke-width="1.6" stroke-linecap="round"/>
    <line x1="22" y1="-82" x2="33" y2="-102" stroke="#81c784" stroke-width="1.6" stroke-linecap="round"/>
    <!-- Branch level 3 -->
    <line x1="-33" y1="-102" x2="-39" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="-33" y1="-102" x2="-26" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="-10" y1="-102" x2="-16" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="-10" y1="-102" x2="-4" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="10" y1="-102" x2="4" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="10" y1="-102" x2="16" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="33" y1="-102" x2="26" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="33" y1="-102" x2="39" y2="-116" stroke="#a5d6a7" stroke-width="1.1" stroke-linecap="round"/>
  </g>
  
  <!-- Central dot at the base case - glowing dot at the center bottom of triangles -->
  <circle cx="200" cy="242" r="6" fill="#ff7043" opacity="0.9"/>
  <circle cx="200" cy="242" r="10" fill="none" stroke="#ff7043" stroke-width="1.5" opacity="0.5"/>
  <circle cx="200" cy="242" r="14" fill="none" stroke="#ff7043" stroke-width="1" opacity="0.3"/>
  
</svg>