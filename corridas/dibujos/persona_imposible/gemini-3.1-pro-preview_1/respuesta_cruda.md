<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
    <linearGradient id="front" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#cbd5e1"/>
    </linearGradient>
    <linearGradient id="top" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- Esoteric Schematic Lines -->
  <g stroke="#ffffff" stroke-width="1" opacity="0.1" fill="none">
    <line x1="200" y1="0" x2="200" y2="400"/>
    <line x1="0" y1="200" x2="400" y2="200"/>
    <circle cx="200" cy="200" r="160"/>
    <circle cx="200" cy="140" r="80"/>
    <polygon points="200,40 338,280 62,280"/>
  </g>

  <!-- Ground Shadows -->
  <polygon points="70,320 170,320 190,305 90,305" fill="rgba(0,0,0,0.5)" stroke="none"/>
  <polygon points="230,320 330,320 350,305 250,305" fill="rgba(0,0,0,0.5)" stroke="none"/>

  <!-- IMPOSSIBLE PERSON -->
  <g stroke="#0f172a" stroke-width="3" stroke-linejoin="round">
    
    <!-- ================= BACK LAYER (Head) ================= -->
    <!-- 1. Head Front -->
    <path d="M 170,80 L 170,240 L 230,240 L 230,80 Z" fill="url(#front)"/>
    <!-- 2. Head Top -->
    <path d="M 170,80 L 190,65 L 250,65 L 230,80 Z" fill="url(#top)"/>
    <!-- 3. Head Right Depth -->
    <path d="M 230,80 L 250,65 L 250,225 L 230,240 Z" fill="#475569"/>

    <!-- ================= MIDDLE LAYER (Right Side) ================= -->
    <!-- 4. Right Arm & Leg Front -->
    <path d="M 230,240 L 230,320 L 330,320 L 330,140 L 270,140 L 270,240 C 270,265 230,265 230,240 Z" fill="url(#front)"/>
    <!-- 5. Right Arm Top -->
    <path d="M 270,140 L 290,125 L 350,125 L 330,140 Z" fill="url(#top)"/>
    <!-- 6. Right Arm & Leg Right Depth -->
    <path d="M 330,140 L 350,125 L 350,305 L 330,320 Z" fill="#475569"/>
    <!-- 7. U-Curve 2 Depth (Inner Gap) -->
    <path d="M 230,240 C 230,265 270,265 270,240 L 290,225 C 290,250 250,250 250,225 L 230,240 Z" fill="url(#top)"/>

    <!-- ================= FRONT LAYER (Left Side - Forces Impossibility) ================= -->
    <!-- 8. Left Arm & Leg Front -->
    <path d="M 70,140 L 70,320 L 170,320 L 170,240 C 170,265 130,265 130,240 L 130,140 Z" fill="url(#front)"/>
    <!-- 9. Left Arm