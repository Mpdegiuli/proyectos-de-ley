<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- fondo -->
  <rect width="400" height="400" fill="#f6f2e9"/>

  <!-- líneas de pauta tipográfica -->
  <g stroke="#c9bfa8" stroke-width="1" stroke-dasharray="4 5">
    <line x1="20" y1="90" x2="380" y2="90"/>
    <line x1="20" y1="160" x2="380" y2="160"/>
    <line x1="20" y1="310" x2="380" y2="310"/>
    <line x1="20" y1="350" x2="380" y2="350"/>
  </g>
  <g font-family="monospace" font-size="10" fill="#b0a58c">
    <text x="24" y="86">ascendente</text>
    <text x="24" y="156">altura x</text>
    <text x="24" y="306">base</text>
    <text x="24" y="346">descendente</text>
  </g>

  <!-- la letra: "therna" -->
  <g fill="none" stroke="#1d1a16" stroke-linecap="round" stroke-linejoin="round">

    <!-- asta principal, de ascendente a descendente, con comba -->
    <path d="M178 90
             C 172 150, 172 240, 178 310
             C 181 335, 176 350, 162 350"
          stroke-width="26"/>

    <!-- panza cerrada a la derecha, naciendo del asta -->
    <path d="M181 175
             C 240 150, 292 172, 292 225
             C 292 278, 240 300, 186 282"
          stroke-width="24"/>

    <!-- barra interior que cruza la panza -->
    <path d="M188 232 L 266 222" stroke-width="16"/>

    <!-- brazo superior hacia la izquierda, gesto propio -->
    <path d="M178 118
             C 150 108, 122 112, 106 134"
          stroke-width="20"/>

    <!-- gota terminal del brazo -->
    <circle cx="103" cy="140" r="15" fill="#1d1a16" stroke="none"/>

    <!-- cola del descendente con remate -->
    <circle cx="156" cy="349" r="13" fill="#1d1a16" stroke="none"/>
  </g>

  <!-- diacrítico inventado: doble tilde partida -->
  <g stroke="#1d1a16" stroke-width="12" stroke-linecap="round" fill="none">
    <path d="M218 62 C 232 50, 248 50, 258 60"/>
    <path d="M266 60 C 276 50, 292 50, 302 62"/>
  </g>

  <!-- ficha de espécimen -->
  <g font-family="monospace" fill="#1d1a16">
    <text x="330" y="330" font-size="34" text-anchor="middle">ȹ̃</text>
    <text x="200" y="382" font-size="13" text-anchor="middle" fill="#6b614c">U+??? · LETRA MINÚSCULA THERNA CON DOBLE TILDE</text>
  </g>
</svg>