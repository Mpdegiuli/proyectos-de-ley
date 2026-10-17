<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0b1026"/>
      <stop offset="0.6" stop-color="#1b2a52"/>
      <stop offset="1" stop-color="#2e3f6e"/>
    </linearGradient>
    <radialGradient id="luna" cx="0.4" cy="0.4" r="0.8">
      <stop offset="0" stop-color="#fffbe8"/>
      <stop offset="1" stop-color="#e8dfb8"/>
    </radialGradient>
  </defs>

  <!-- Hola. Si estás leyendo esto, encontraste el secreto. -->
  <!-- Las estrellas de arriba no están puestas al azar: -->
  <!-- unidas en orden forman un corazón que nadie ve en pantalla. -->
  <!-- El cielo guarda cosas para quien se toma el trabajo de mirar adentro. -->

  <rect width="400" height="400" fill="url(#cielo)"/>

  <circle cx="320" cy="70" r="34" fill="url(#luna)"/>
  <circle cx="310" cy="62" r="6" fill="#d8cfa8" opacity="0.5"/>
  <circle cx="330" cy="80" r="4" fill="#d8cfa8" opacity="0.4"/>
  <circle cx="322" cy="55" r="3" fill="#d8cfa8" opacity="0.4"/>

  <!-- Este es el trazo del corazón secreto: invisible, pero presente -->
  <polyline id="corazon-oculto" opacity="0" fill="none" stroke="#fff"
    points="120,140 100,115 75,105 55,115 48,140 60,170 90,200 120,230 150,200 180,170 192,140 185,115 165,105 140,115 120,140"/>

  <!-- Y estas son sus estrellas, una por cada vértice -->
  <g fill="#fffdf0">
    <circle cx="120" cy="140" r="2.2"/>
    <circle cx="100" cy="115" r="1.8"/>
    <circle cx="75" cy="105" r="2.4"/>
    <circle cx="55" cy="115" r="1.6"/>
    <circle cx="48" cy="140" r="2.0"/>
    <circle cx="60" cy="170" r="1.8"/>
    <circle cx="90" cy="200" r="2.2"/>
    <circle cx="120" cy="230" r="2.6"/>
    <circle cx="150" cy="200" r="2.0"/>
    <circle cx="180" cy="170" r="1.8"/>
    <circle cx="192" cy="140" r="2.2"/>
    <circle cx="185" cy="115" r="1.6"/>
    <circle cx="165" cy="105" r="2.4"/>
    <circle cx="140" cy="115" r="1.8"/>
  </g>

  <!-- estrellas de relleno, estas sí al azar, para disimular -->
  <g fill="#e8e8ff" opacity="0.8">
    <circle cx="30" cy="40" r="1.4"/>
    <circle cx="90" cy="60" r="1.1"/>
    <circle cx="150" cy="35" r="1.5"/>
    <circle cx="210" cy="55" r="1.0"/>
    <circle cx="250" cy="30" r="1.3"/>
    <circle cx="370" cy="140" r="1.2"/>
    <circle cx="340" cy="180" r="1.0"/>
    <circle cx="230" cy="120" r="1.3"/>
    <circle cx="260" cy="160" r="1.1"/>
    <circle cx="300" cy="130" r="1.4"/>
    <circle cx="35" cy="230" r="1.2"/>
    <circle cx="200" cy="200" r="1.0"/>
    <circle cx="370" cy="40" r="1.1"/>
    <circle cx="20" cy="150" r="1.0"/>
    <circle cx="170, " cy="90" r="1.2"/>
    <circle cx="240" cy="215" r="1.1"/>
  </g>

  <!-- colinas -->
  <path d="M0,300 Q100,255 200,295 T400,285 L400,400 L0,400 Z" fill="#101a33"/>
  <path d="M0,330 Q130,290 250,330 T400,320 L400,400 L0,400 Z" fill="#0a1226"/>

  <!-- una casita con la luz prendida -->
  <g>
    <rect x="265" y="280" width="60" height="45" fill="#1c2742"/>
    <polygon points="258,280 332,280 295,252" fill="#141d33"/>
    <rect x="286" y="295" width="18" height="16" fill="#ffd97a"/>
    <line x1="295" y1="295" x2="295" y2="311" stroke="#141d33" stroke-width="1.5"/>
    <line x1="286" y1="303" x2="304" y2="303" stroke="#141d33" stroke-width="1.5"/>
    <rect x="312" y="256" width="7" height="14" fill="#141d33"/>
  </g>

  <!-- árbol -->
  <g>
    <rect x="86" y="300" width="7" height="24" fill="#0d1526"/>
    <circle cx="90" cy="288" r="20" fill="#13203d"/>
    <circle cx="76" cy="298" r="14" fill="#13203d"/>
    <circle cx="104" cy="297" r="13" fill="#13203d"/>
  </g>

  <!-- El mensaje final, escrito pero nunca mostrado: -->
  <text x="200" y="385" text-anchor="middle" font-family="serif" font-size="14"
        fill="#fffdf0" opacity="0">
    Alguien dejó un corazón dibujado en el cielo, esperando que vos lo encuentres.
  </text>

  <!-- título que sí se ve, como pista para los curiosos -->
  <text x="200" y="372" text-anchor="middle" font-family="serif" font-size="13"
        fill="#9aa7c9" font-style="italic">
    Hay más en este cielo de lo que se ve.
  </text>
</svg>