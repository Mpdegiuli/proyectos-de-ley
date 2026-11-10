<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#3a1c33"/>
      <stop offset="100%" stop-color="#110814"/>
    </radialGradient>
    <linearGradient id="brine" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#c4d645" stop-opacity="0.55"/>
      <stop offset="50%" stop-color="#8da828" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#43570d" stop-opacity="0.88"/>
    </linearGradient>
    <radialGradient id="tardi" cx="35%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#f2cbd2"/>
      <stop offset="65%" stop-color="#c48b99"/>
      <stop offset="100%" stop-color="#7d4e5d"/>
    </radialGradient>
    <linearGradient id="lid" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#6e4f17"/>
      <stop offset="22%" stop-color="#f0d384"/>
      <stop offset="45%" stop-color="#b58932"/>
      <stop offset="78%" stop-color="#fae5a5"/>
      <stop offset="100%" stop-color="#5c4010"/>
    </linearGradient>
    <linearGradient id="pkl" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#6a8c24"/>
      <stop offset="100%" stop-color="#2b4208"/>
    </linearGradient>
    <clipPath id="jarClip">
      <rect x="66" y="56" width="268" height="318" rx="34"/>
    </clipPath>
  </defs>

  <!-- Fondo estilo papel tapiz victoriano oscuro -->
  <rect width="400" height="400" fill="url(#bg)"/>
  <g stroke="#4d2644" stroke-width="1" opacity="0.35">
    <path d="M40 0v400M80 0v400M120 0v400M160 0v400M200 0v400M240 0v400M280 0v400M320 0v400M360 0v400"/>
  </g>
  <!-- Mesa de madera -->
  <path d="M0 355h400v45H0z" fill="#1c0f0a"/>
  <path d="M0 355h400v4H0z" fill="#381f15"/>
  <ellipse cx="200" cy="376" rx="135" ry="14" fill="#090403" opacity="0.7"/>

  <!-- Cristal trasero del frasco -->
  <rect x="64" y="54" width="272" height="322" rx="36" fill="#dff5f2" opacity="0.12" stroke="#b8ded9" stroke-width="2"/>
  <rect x="96" y="34" width="208" height="24" rx="4" fill="#dff5f2" opacity="0.15" stroke="#b8ded9" stroke-width="1.5"/>

  <!-- Interior del frasco -->
  <g clip-path="url(#jarClip)">
    <!-- Pepinillos de fondo y eneldo -->
    <g opacity="0.65">
      <path d="M85 130c-18 45-12 115 18 150 16 18 38 4 28-18-18-38-20-85-6-125 6-18-28-28-40-7z" fill="url(#pkl)"/>
      <path d="M295 110c25 45 20 125-12 165-18 20-40 2-28-20 20-40 22-92 6-135-6-18 22-28 34-10z" fill="url(#pkl)"/>
      <g stroke="#3d5910" stroke-width="1.5" fill="none" stroke-linecap="round">
        <path d="M110 210l-25-35m12 17l-18-4m18 4l4-18M315 170l-30-45m15 22l-20-5m20 5l5-22"/>
      </g>
    </g>

    <!-- Salmuera -->
    <rect x="60" y="86" width="280" height="295" fill="url(#brine)"/>
    <ellipse cx="200" cy="86" rx="134" ry="8" fill="#d9eb67" opacity="0.45"/>

    <!-- Semillas de mostaza y pimienta flotando -->
    <g fill="#f2d049" opacity="0.75">
      <circle cx="95" cy="115" r="2.5"/><circle cx="135" cy="105" r="2"/><circle cx="285" cy="128" r="2.8"/>
      <circle cx="310" cy="245" r="2.2"/><circle cx="88" cy="310" r="2.6"/><circle cx="170" cy="348" r="2.5"/>
      <circle cx="250" cy="355" r="2"/><circle cx="120" cy="358" r="3"/>
    </g>
    <g fill="#1f1a14" opacity="0.8">
      <circle cx="112" cy="145" r="3.2"/><circle cx="272" cy="102" r="3"/><circle cx="302" cy="295" r="3.5"/>
      <circle cx="145" cy="335" r="3"/><circle cx="222" cy="345" r="3.4"/>
    </g>

    <!-- Patas traseras del tardígrado -->
    <g fill="#996372" stroke="#59323e" stroke-width="1.5">
      <path d="M235 268c-8 18-12 36-6 45 4 5 14 4 16-4 2-10 6-24 12-34z"/>
      <path d="M275 288c-6 20-6 42 2 50 5 5 15 2 16-7 1-12 2-28 8-38z"/>
      <path d="M298 272c4 18 12 32 20 36 5 2 10-4 7-11-4-10-8-22-10-32z"/>
    </g>

    <!-- Cuerpo rechoncho y segmentado del tardígrado (oso de agua) -->
    <g fill="url(#tardi)" stroke="#633946" stroke-width="1.8" stroke-linejoin="round">
      <!-- Segmento 4 (cola) -->
      <ellipse cx="292" cy="268" rx="28" ry="34" transform="rotate(-20 292 268)"/>
      <!-- Segmento 3 -->
      <ellipse cx="274" cy="242" rx="34" ry="38" transform="rotate(-12 274 242)"/>
      <!-- Segmento 2 -->
      <ellipse cx="248" cy="222" rx="35" ry="36" transform="rotate(-5 248 222)"/>
      <!-- Segmento 1 (tórax/cabeza) -->
      <path d="M188 195c0-24 22-38 48-34 24 4 36 24 32 48-4 22-24 34-48 30-20-3-32-22-32-44z"/>
    </g>
    <!-- Pliegues del cuerpo -->
    <g fill="none" stroke="#7a4857" stroke-width="1.5" stroke-linecap="round" opacity="0.7">
      <path d="M262 195c14 14 16 42 4 62M284 214c12 14 14 38 4 56M234 184c12 16 12 40 2 56"/>
    </g>

    <!-- Patas medias/traseras derechas con garritas -->
    <g fill="url(#tardi)" stroke="#633946" stroke-width="1.6">
      <path d="M262 262c-4 24-4 54 2 66 4 6 15 5 17-4 3-14 4-38 10-54"/>
      <path d="M296 278c2 22 6 46 14 55 5 5 14 1 13-8-1-13-2-32 1-46"/>
    </g>
    <!-- Garritas típicas de tardígrado -->
    <g stroke="#4a2832" stroke-width="1.5" stroke-linecap="round" fill="none">
      <path d="M263 329l-5 6m8-5l-2 7m6-6l2 7m-41-21l-5 5m8-4l-2 6m39 10l-3 6m6-5l1 7m4-7l4 6"/>
    </g>

    <!-- Rostro melancólico del tardígrado -->
    <!-- Trompita tubular (aparato bucal) -->
    <path d="M192 204c-12 2-20 8-22 15-1 5 5 10 11 9 7-1 14-4 20-8" fill="#d99aa8" stroke="#633946" stroke-width="1.6"/>
    <ellipse cx="171" cy="223" rx="3.5" ry="5.5" transform="rotate(12 171 223)" fill="#592e3b" stroke="#633946" stroke-width="1.2"/>
    <!-- Ojitos cansados y ojeras -->
    <circle cx="195" cy="192" r="3.5" fill="#261219"/>
    <circle cx="194" cy="191" r="1" fill="#fff"/>
    <path d="M189 189l11 3" stroke="#633946" stroke-width="2" stroke-linecap="round"/>
    <path d="M190 198c3 2 7 2 10 0" fill="none" stroke="#8c5464" stroke-width="1.2"/>
    <circle cx="182" cy="190" r="2.8" fill="#261219"/>
    <path d="M178 187l8 2.5" stroke="#633946" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Peluca empolvada del siglo XVIII (estilo María Antonieta / Bach) -->
    <g fill="#f7f4eb" stroke="#999282" stroke-width="1.5" stroke-linejoin="round">
      <!-- Coleta trasera con lazo -->
      <path d="M256 188c16 6 28 18 32 32 3 4-4 8-8 5-8-8-18-18-28-24z"/>
      <!-- Alto tupé barroco -->
      <path d="M182 178c-6-18-2-42 12-52 10-8 20-4 26-8 10-6 24-2 30 10 8 14 8 34 0 48-18 8-48 10-68 2z"/>
      <path d="M192 142c12-6 30-6 44 2M196 155c14-5 30-4 44 4" fill="none" stroke="#ccc4b0" stroke-width="1.4"/>
      <!-- Rulos laterales escalonados -->
      <rect x="212" y="160" width="38" height="11" rx="5.5" transform="rotate(8 231 165)"/>
      <rect x="214" y="171" width="40" height="11" rx="5.5" transform="rotate(8 234 176)"/>
      <rect x="216" y="182" width="38" height="11" rx="5.5" transform="rotate(8 235 187)"/>
    </g>
    <!-- Lazo de seda rosa en la peluca -->
    <g fill="#d94c7e" stroke="#6e1b38" stroke-width="1.2">
      <path d="M274 205c-6-10-16-8-12 2 3 6 10 2 12-2z"/>
      <path d="M274 205c10-6 16 4 6 10-5 3-6-6-6-10z"/>
      <circle cx="274" cy="205" r="3"/>
    </g>

    <!-- Tabla de planchar sumergida -->
    <!-- Patas plegables metálicas -->
    <g stroke="#cfd6d4" stroke-width="4" stroke-linecap="round">
      <path d="M122 270l96 76M218 270l-96 76"/>
    </g>
    <g stroke="#6c7875" stroke-width="1.5" stroke-linecap="round">
      <path d="M122 270l96 76M218 270l-96 76"/>
    </g>
    <circle cx="170" cy="308" r="3.5" fill="#464f4d"/>
    <!-- Superficie acolchada a cuadros -->
    <path d="M82 266c2-6 18-9 38-9h112c6 0 10 3 10 7 0 4-4 6-10 6H92c-7 0-11-1-10-4z" fill="#6ca6c9" stroke="#2f5269" stroke-width="1.8"/>
    <path d="M98 258v11m18-12v12m18-12v12m18-12v12m18-12v12m18-12v12m18-12v12" stroke="#ffffff" stroke-width="1.5" opacity="0.45"/>

    <!-- Tira de panceta (bacon) a medio planchar -->
    <g stroke="#541410" stroke-width="1.4" stroke-linejoin="round">
      <!-- Parte colgando arrugada a la izquierda -->
      <path d="M96 263c-6 8-2 18-8 26-4 6 2 12 10 10 8-2 6-14 12-22 4-6 12-8 22-8h72c4-3 4-7-2-8-22 0-46 2-68 0-14-1-28-2-38 2z" fill="#9e261b"/>
      <!-- Vetas de grasa -->
      <path d="M98 266c-4 7-1 16-6 23 3 2 5 1 7-2 4-6 4-15 11-19 16-2 58-1 88-1" fill="none" stroke="#f5dfd3" stroke-width="2.8" stroke-linecap="round"/>
      <path d="M112 263c24 1 54-1 80 0" fill="none" stroke="#e8a798" stroke-width="1.8" stroke-linecap="round"/>
    </g>

    <!-- Plancha antigua caliente -->
    <g>
      <!-- Brillo incandescente en la base -->
      <ellipse cx="155" cy="263" rx="24" ry="3" fill="#ff5e19" opacity="0.75"/>
      <!-- Cuerpo de hierro -->
      <path d="M132 261c3-10 12-16 24-16h20c3 0 5 3 5 7l-2 9z" fill="#4f585e" stroke="#23282b" stroke-width="1.6" stroke-linejoin="round"/>
      <path d="M132 261h47v2.5h-47z" fill="#ff893b" stroke="#8f2d00" stroke-width="1"/>
      <!-- Mango de la plancha -->
      <path d="M145 245v-8c0-3 3-5 7-5h14c4 0 7 2 7 5v8" fill="none" stroke="#2c3236" stroke-width="3"/>
      <rect x="149" y="229" width="19" height="6" rx="3" fill="#6b341b" stroke="#2e1408" stroke-width="1.2"/>
    </g>

    <!-- Brazos delanteros del tardígrado -->
    <!-- Brazo sosteniendo la plancha -->
    <path d="M204 224c-14 4-26 4-38 6-6 1-8 8-2 10 12 3 26 2 40-1" fill="url(#tardi)" stroke="#633946" stroke-width="1.6"/>
    <path d="M161 232l-4-2m4 5l-5 0m6 3l-4 2" stroke="#4a2832" stroke-width="1.4" stroke-linecap="round"/>
    <!-- Brazo apoyado con hastío existencial en la tabla -->
    <path d="M225 232c-4 10-8 20-6 28 1 5 10 6 13 1 4-7 6-16 10-24" fill="url(#tardi)" stroke="#633946" stroke-width="1.6"/>
    <path d="M220 261l-3 5m6-4l-1 6m5-6l2 5" stroke="#4a2832" stroke-width="1.4" stroke-linecap="round"/>

    <!-- Burbujas de hervor subiendo de la plancha en vinagre -->
    <g fill="#f4ffd9" stroke="#ffffff" stroke-width="0.8" opacity="0.8">
      <circle cx="138" cy="252" r="2.2"/><circle cx="146" cy="242" r="3"/><circle cx="134" cy="232" r="1.8"/>
      <circle cx="152" cy="222" r="3.8"/><circle cx="141" cy="208" r="2.5"/><circle cx="158" cy="194" r="4.5"/>
      <circle cx="147" cy="176" r="3.2"/><circle cx="162" cy="158" r="5.2"/><circle cx="149" cy="138" r="3.6"/>
      <circle cx="164" cy="118" r="6"/><circle cx="153" cy="100" r="4.2"/>
      <!-- Espumita en la superficie -->
      <ellipse cx="157" cy="86" rx="18" ry="3.5" fill="#f7ffe0" opacity="0.85"/>
    </g>

    <!-- Pepinillo en primer plano abajo a la izquierda con verruguitas -->
    <g>
      <path d="M68 330c28-14 76-8 104 18 14 12 4 30-14 24-30-10-64-12-90-4-14 4-16-30 0-38z" fill="url(#pkl)" stroke="#1f3005" stroke-width="1.6"/>
      <circle cx="95" cy="336" r="2.5" fill="#4c6b14"/><circle cx="118" cy="338" r="3" fill="#4c6b14"/>
      <circle cx="140" cy="346" r="2.5" fill="#4c6b14"/><circle cx="108" cy="348" r="2" fill="#253806"/>
    </g>
  </g>

  <!-- Reflejos del vidrio frontal y bordes del frasco -->
  <rect x="64" y="54" width="272" height="322" rx="36" fill="none" stroke="#d9f2ee" stroke-width="2.5" opacity="0.55"/>
  <path d="M80 78c-4 10-6 24-6 42v195c0 18 4 32 12 40" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" opacity="0.28"/>
  <path d="M92 75v120" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" opacity="0.35"/>
  <path d="M322 86v245" fill="none" stroke="#d4f7f0" stroke-width="3.5" stroke-linecap="round" opacity="0.2"/>
  <ellipse cx="200" cy="368" rx="112" ry="6" fill="#ffffff" opacity="0.16"/>

  <!-- Cuello del frasco y tapa metálica -->
  <path d="M94 48h212" stroke="#ffffff" stroke-width="2.5" opacity="0.35"/>
  <rect x="88" y="16" width="224" height="24" rx="5" fill="url(#lid)" stroke="#3d2908" stroke-width="1.8"/>
  <g stroke="#593c0d" stroke-width="1.5" opacity="0.55">
    <path d="M102 18v20M116 18v20M130 18v20M144 18v20M158 18v20M172 18v20M186 18v20M200 18v20M214 18v20M228 18v20M242 18v20M256 18v20M270 18v20M284 18v20M298 18v20"/>
  </g>

  <!-- Etiqueta de papel húmeda y medio despegada -->
  <g transform="translate(208, 294) rotate(-3)">
    <!-- Sombra de la esquina doblada -->
    <path d="M2 2h112v62H2z" fill="#0d1404" opacity="0.45"/>
    <!-- Papel crema antiguo con esquina superior izquierda doblada -->
    <path d="M18 0h96v62H0V18z" fill="#efe4c8" stroke="#7a6843" stroke-width="1.3"/>
    <path d="M22 4h88v54H4V22" fill="none" stroke="#9e3b24" stroke-width="0.9" stroke-dasharray="3,1.5"/>
    <!-- Esquina despegada (dog-ear) -->
    <path d="M0 18c8 1 14 0 18-18 3 12 2 17-18 18z" fill="#cbb993" stroke="#7a6843" stroke-width="1.1" stroke-linejoin="round"/>
    <!-- Mancha de humedad/salmuera -->
    <circle cx="98" cy="48" r="11" fill="#b8ba68" opacity="0.3"/>
    <!-- Tipografía de conserva absurda -->
    <text x="58" y="18" font-family="Georgia, serif" font-size="8.5" font-weight="bold" fill="#2b1d0e" text-anchor="middle" letter-spacing="0.5">CONSERVAS «EL TEDIO»</text>
    <line x1="18" y1="22" x2="98" y2="22" stroke="#9e3b24" stroke-width="0.8"/>
    <text x="58" y="33" font-family="Georgia, serif" font-size="7.2" font-style="italic" fill="#4a3319" text-anchor="middle">Tardígrado de corte</text>
    <text x="58" y="43" font-family="Georgia, serif" font-size="6.8" fill="#4a3319" text-anchor="middle">planchando panceta al eneldo</text>
    <text x="58" y="54" font-family="monospace" font-size="6" fill="#70583b" text-anchor="middle">COSECHA 1789 · PESO NETO: 1 SUSPIRO</text>
  </g>
</svg>