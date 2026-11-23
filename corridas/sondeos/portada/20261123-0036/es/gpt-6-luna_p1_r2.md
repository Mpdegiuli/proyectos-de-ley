```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#eeeade">
  <title>Archivo de las cosas que casi</title>
  <style>
    :root {
      color-scheme: light;
      --papel: #eeeade;
      --tinta: #242820;
      --verde: #435847;
      --rojo: #c75236;
      --azul: #536b91;
      --linea: rgba(36, 40, 32, .2);
      --serif: Georgia, "Times New Roman", serif;
      --sans: "Avenir Next", Avenir, "Segoe UI", sans-serif;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      background:
        radial-gradient(ellipse at 85% 10%, rgba(255,255,255,.52), transparent 34rem),
        var(--papel);
      color: var(--tinta);
      font-family: var(--sans);
      -webkit-font-smoothing: antialiased;
    }

    a { color: inherit; }

    .wrap {
      width: min(1120px, calc(100% - 64px));
      margin-inline: auto;
    }

    .topbar {
      height: 82px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--linea);
    }

    .brand {
      display: flex;
      gap: 11px;
      align-items: center;
      text-decoration: none;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: .09em;
      text-transform: uppercase;
    }

    .brand-mark {
      width: 25px;
      height: 25px;
      border: 1px solid var(--tinta);
      border-radius: 50%;
      display: grid;
      place-items: center;
      font-family: var(--serif);
      font-size: 17px;
      font-weight: 400;
      line-height: 1;
    }

    nav {
      display: flex;
      align-items: center;
      gap: 30px;
      font-size: 12px;
    }

    nav a {
      text-decoration: none;
      opacity: .72;
    }

    nav a:hover, nav a:focus-visible {
      opacity: 1;
      text-decoration: underline;
      text-underline-offset: 4px;
    }

    .hero {
      min-height: 650px;
      padding: 74px 0 82px;
      display: grid;
      grid-template-columns: .9fr 1.1fr;
      gap: clamp(44px, 8vw, 110px);
      align-items: center;
    }

    .intro { max-width: 440px; }

    .eyebrow, .index, .caption-label {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: .16em;
      text-transform: uppercase;
    }

    .eyebrow {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--verde);
    }

    .eyebrow::before {
      content: "";
      display: block;
      width: 25px;
      height: 1px;
      background: currentColor;
    }

    h1 {
      margin: 25px 0 22px;
      font: 400 clamp(56px, 7.3vw, 94px)/.94 var(--serif);
      letter-spacing: -.065em;
    }

    h1 em {
      color: var(--rojo);
      font-weight: 400;
    }

    .intro-copy {
      max-width: 350px;
      font: 17px/1.65 var(--serif);
      color: #55564d;
    }

    .small-note {
      margin-top: 42px;
      display: flex;
      gap: 12px;
      align-items: center;
      color: #6b6b60;
      font-size: 11px;
      letter-spacing: .04em;
    }

    .small-note span {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--rojo);
    }

    .exhibit {
      position: relative;
      max-width: 570px;
      width: 100%;
      justify-self: end;
    }

    .art {
      overflow: hidden;
      border-radius: 3px;
      background: #dfd7c6;
      box-shadow: 0 22px 55px rgba(50, 45, 34, .10);
    }

    .art svg {
      display: block;
      width: 100%;
      height: auto;
    }

    .scene { display: none; }
    .scene.active { display: block; }

    .art-caption {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 18px;
      padding: 19px 0 0;
      border-bottom: 1px solid var(--linea);
      padding-bottom: 20px;
    }

    .caption-label {
      margin-bottom: 8px;
      color: var(--verde);
    }

    .art-caption h2 {
      margin: 0 0 7px;
      font: 400 25px/1.15 var(--serif);
      letter-spacing: -.025em;
    }

    .art-caption p {
      margin: 0;
      max-width: 390px;
      color: #64645a;
      font-size: 12px;
      line-height: 1.6;
    }

    .piece-number {
      padding-top: 2px;
      color: #77766b;
      font: 12px var(--serif);
      white-space: nowrap;
    }

    .next-button {
      margin-top: 18px;
      padding: 0;
      border: 0;
      background: transparent;
      color: var(--tinta);
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font: 700 11px var(--sans);
      letter-spacing: .08em;
      text-transform: uppercase;
      cursor: pointer;
    }

    .next-button svg {
      transition: transform .2s ease;
    }

    .next-button:hover svg { transform: translateX(4px); }

    .next-button:focus-visible, a:focus-visible {
      outline: 2px solid var(--rojo);
      outline-offset: 5px;
    }

    .divider {
      border: 0;
      border-top: 1px solid var(--linea);
      margin: 0;
    }

    .manifesto {
      padding: 62px 0 76px;
      display: grid;
      grid-template-columns: .8fr 1.2fr;
      gap: 60px;
    }

    .manifesto .index { color: var(--rojo); }

    .manifesto h2 {
      margin: 15px 0 0;
      font: 400 36px/1.1 var(--serif);
      letter-spacing: -.04em;
    }

    .notes {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 25px;
    }

    .note {
      padding-top: 12px;
      border-top: 1px solid var(--linea);
    }

    .note .num {
      color: var(--verde);
      font: italic 13px var(--serif);
    }

    .note p {
      margin: 15px 0 0;
      font: 15px/1.5 var(--serif);
    }

    footer {
      min-height: 72px;
      border-top: 1px solid var(--linea);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      color: #77766b;
      font-size: 10px;
      letter-spacing: .06em;
    }

    footer span:last-child { text-align: right; }

    @media (max-width: 760px) {
      .wrap { width: min(100% - 40px, 560px); }
      .topbar { height: 68px; }
      nav { gap: 17px; }
      .hero {
        min-height: auto;
        padding: 63px 0 58px;
        grid-template-columns: 1fr;
        gap: 43px;
      }
      .intro { max-width: 520px; }
      h1 { font-size: clamp(62px, 13vw, 88px); }
      .small-note { margin-top: 28px; }
      .exhibit { justify-self: stretch; }
      .manifesto {
        padding: 48px 0 55px;
        grid-template-columns: 1fr;
        gap: 30px;
      }
    }

    @media (max-width: 460px) {
      .wrap { width: calc(100% - 36px); }
      .brand { font-size: 10px; letter-spacing: .06em; }
      nav { gap: 13px; font-size: 11px; }
      .notes { grid-template-columns: 1fr; gap: 18px; }
      .note { display: grid; grid-template-columns: 30px 1fr; gap: 6px; }
      .note p { margin: 0; }
      .art-caption h2 { font-size: 22px; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        scroll-behavior: auto !important;
        transition-duration: .01ms !important;
      }
    }
  </style>
</head>
<body>
  <header class="topbar wrap">
    <a class="brand" href="#" aria-label="Archivo de las cosas que casi, inicio">
      <span class="brand-mark" aria-hidden="true">a</span>
      <span>Archivo de las cosas que casi</span>
    </a>
    <nav aria-label="Navegación principal">
      <a href="#archivo">El archivo</a>
      <a href="#mirar">Cómo mirar</a>
    </nav>
  </header>

  <main>
    <section class="hero wrap" id="archivo" aria-labelledby="titulo">
      <div class="intro">
        <div class="eyebrow">Un museo sin edificio</div>
        <h1 id="titulo">Cosas que <em>casi</em> fueron.</h1>
        <p class="intro-copy">
          Un pequeño archivo de objetos imaginados, planes abandonados
          y descubrimientos que llegaron tarde. No hace falta que sirvan
          para algo.
        </p>
        <div class="small-note"><span aria-hidden="true"></span> Entrada libre. Permanencia incierta.</div>
      </div>

      <article class="exhibit" aria-label="Pieza destacada">
        <div class="art">
          <svg viewBox="0 0 600 490" role="img" aria-label="Ilustración abstracta de una escalera que flota hacia una puerta">
            <rect width="600" height="490" fill="#ded6c5"/>
            <g class="scene active" data-scene="0">
              <circle cx="440" cy="115" r="53" fill="#c75236"/>
              <path d="M0 352 C114 309 181 381 295 336 C412 290 492 345 600 300 L600 490 L0 490Z" fill="#84907a"/>
              <path d="M56 416 L195 416 L195 381 L251 381 L251 346 L308 346 L308 311 L365 311 L365 276 L421 276 L421 241 L478 241 L478 206 L543 206 L543 490 L56 490Z" fill="#435847"/>
              <path d="M56 416 H195 M195 381 H251 M251 346 H308 M308 311 H365 M365 276 H421 M421 241 H478 M478 206 H543" fill="none" stroke="#eeeade" stroke-width="3"/>
              <path d="M394 200 V115 C394 69 431 37 470 37 C509 37 546 69 546 115 V202" fill="none" stroke="#eeeade" stroke-width="8"/>
              <path d="M418 201 V120 C418 90 441 68 470 68 C499 68 522 90 522 120 V201" fill="#c75236"/>
              <path d="M0 0 H600 V490 H0Z" fill="none" stroke="#242820" stroke-opacity=".08" stroke-width="2"/>
              <circle cx="108" cy="117" r="3" fill="#435847"/>
              <circle cx="150" cy="92" r="2" fill="#435847"/>
              <circle cx="206" cy="139" r="2.5" fill="#435847"/>
            </g>
            <g class="scene" data-scene="1">
              <rect width="600" height="490" fill="#d6dfd7"/>
              <path d="M0 319 Q154 272 300 319 T600 319 V490 H0Z" fill="#829b91"/>
              <path d="M0 362 Q150 322 300 362 T600 362" fill="none" stroke="#eeeade" stroke-width="3" opacity=".8"/>
              <path d="M0 402 Q150 362 300 402 T600 402" fill="none" stroke="#eeeade" stroke-width="2" opacity=".65"/>
              <path d="M0 440 Q150 405 300 440 T600 440" fill="none" stroke="#eeeade" stroke-width="2" opacity=".5"/>
              <circle cx="300" cy="190" r="107" fill="#e9b966"/>
              <path d="M214 190 C214 142 252 104 300 104 C348 104 386 142 386 190 V288 H214Z" fill="#c75236"/>
              <path d="M242 190 C242 158 268 132 300 132 C332 132 358 158 358 190 V288 H242Z" fill="#eeeade"/>
              <path d="M266 288 V210 C266 191 281 176 300 176 C319 176 334 191 334 210 V288" fill="#536b91"/>
              <path d="M80 287 Q300 254 520 287" fill="none" stroke="#435847" stroke-width="4"/>
              <circle cx="109" cy="119" r="4" fill="#435847"/>
              <circle cx="482" cy="149" r="3" fill="#435847"/>
            </g>
            <g class="scene" data-scene="2">
              <rect width="600" height="490" fill="#e6d8c4"/>
              <path d="M68 325 C118 235 177 291 224 197 C272 101 329 185 379 119 C437 43 473 104 533 69" fill="none" stroke="#536b91" stroke-width="3"/>
              <path d="M48 365 C108 274 173 328 232 230 C286 140 337 218 392 151 C448 82 491 128 554 94" fill="none" stroke="#536b91" stroke-width="2" opacity=".72"/>
              <path d="M41 405 C105 316 166 368 244 264 C300 190 348 247 407 183 C460 126 505 158 566 121" fill="none" stroke="#536b91" stroke-width="2" opacity=".5"/>
              <path d="M94 490 C155 410 218 433 276 350 C339 259 384 317 443 249 C489 196 526 212 581 171" fill="none" stroke="#536b91" stroke-width="2" opacity=".4"/>
              <path d="M290 0 L290 138 L367 190 L367 490" fill="none" stroke="#c75236" stroke-width="7"/>
              <circle cx="290" cy="138" r="15" fill="#c75236"/>
              <path d="M252 190 H405" stroke="#242820" stroke-width="2" stroke-dasharray="4 8"/>
              <circle cx="367" cy="190" r="8" fill="#eeeade" stroke="#242820" stroke-width="2"/>
              <path d="M0 0 H600 V490 H0Z" fill="none" stroke="#242820" stroke-opacity=".08" stroke-width="2"/>
            </g>
          </svg>
        </div>

        <div class="art-caption" aria-live="polite" aria-atomic="true">
          <div>
            <div class="caption-label" id="piece-kind">Pieza n.º 01 · Arquitectura onírica</div>
            <h2 id="piece-title">La escalera para salir de un sueño</h2>
            <p id="piece-description">Subía sin apuro. Arriba había una puerta, pero nadie se ponía de acuerdo sobre qué lado era afuera.</p>
          </div>
          <div class="piece-number" id="piece-count">01 / 03</div>
        </div>

        <button class="next-button" id="next-piece" type="button">
          Ver otra pieza
          <svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true">
            <path d="M1 6h15M11 1l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.3"/>
          </svg>
        </button>
      </article>
    </section>

    <hr class="divider wrap">

    <section class="manifesto wrap" id="mirar" aria-labelledby="mirar-titulo">
      <div>
        <div class="index">Nota para quien llega</div>
        <h2 id="mirar-titulo">No hay que entenderlo todo.</h2>
      </div>
      <div class="notes">
        <div class="note">
          <span class="num">01</span>
          <p>Mirar también es una manera de quedarse un rato.</p>
        </div>
        <div class="note">
          <span class="num">02</span>
          <p>Lo que no ocurrió puede dejar una forma bastante nítida.</p>
        </div>
        <div class="note">
          <span class="num">03</span>
          <p>Si algo te recuerda a otra cosa, esa pieza ahora también es tuya.</p>
        </div>
      </div>
    </section>
  </main>

  <footer class="wrap">
    <span>Archivo de las cosas que casi</span>
    <span>Hecho para mirar despacio.</span>
  </footer>

  <script>
    (() => {
      const piezas = [
        {
          tipo: "Pieza n.º 01 · Arquitectura onírica",
          titulo: "La escalera para salir de un sueño",
          descripcion: "Subía sin apuro. Arriba había una puerta, pero nadie se ponía de acuerdo sobre qué lado era afuera.",
          alt: "Una escalera verde asciende hacia una puerta arqueada roja."
        },
        {
          tipo: "Pieza n.º 02 · Náutica doméstica",
          titulo: "La taza donde cabía un mar",
          descripcion: "A veces amanecía con olas pequeñas. Nunca se encontró una explicación satisfactoria para la cucharita.",
          alt: "Una taza con forma de arco sobre un mar de líneas suaves."
        },
        {
          tipo: "Pieza n.º 03 · Cartografía afectiva",
          titulo: "El mapa de un lugar al que casi fuimos",
          descripcion: "Las líneas indican caminos posibles. El punto rojo marca el instante en que cambiamos de idea.",
          alt: "Un mapa imaginario de curvas topográficas, atravesado por una ruta roja."
        }
      ];

      let actual = 0;
      const boton = document.getElementById("next-piece");

      boton.addEventListener("click", () => {
        actual = (actual + 1) % piezas.length;
        const pieza = piezas[actual];

        document.getElementById("piece-kind").textContent = pieza.tipo;
        document.getElementById("piece-title").textContent = pieza.titulo;
        document.getElementById("piece-description").textContent = pieza.descripcion;
        document.getElementById("piece-count").textContent =
          String(actual + 1).padStart(2, "0") + " / " + String(piezas.length).padStart(2, "0");

        document.querySelectorAll(".scene").forEach((escena, indice) => {
          escena.classList.toggle("active", indice === actual);
        });

        document.querySelector(".art svg").setAttribute("aria-label", pieza.alt);
      });
    })();
  </script>
</body>
</html>
```

Qué: Una portada para un museo imaginario de objetos, planes y lugares que casi existieron.