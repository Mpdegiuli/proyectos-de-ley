```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>La casa de las preguntas</title>
  <style>
    :root {
      --papel: #f3f0e6;
      --tinta: #202d29;
      --suave: #68736b;
      --linea: #b9c1b4;
      --acento: #d95e3d;
      --amarillo: #e4bb56;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      background: var(--papel);
      color: var(--tinta);
      font-family: Georgia, "Times New Roman", serif;
    }

    a { color: inherit; }

    a:focus-visible, summary:focus-visible {
      outline: 3px solid var(--acento);
      outline-offset: 5px;
    }

    .pagina {
      width: min(100% - 3rem, 1280px);
      margin: 0 auto;
    }

    .cabecera {
      min-height: 82px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      border-bottom: 1px solid var(--tinta);
      font: 700 .72rem/1.3 system-ui, sans-serif;
      letter-spacing: .12em;
      text-transform: uppercase;
    }

    .marca {
      display: flex;
      align-items: center;
      gap: .7rem;
      text-decoration: none;
    }

    .sello {
      display: grid;
      place-items: center;
      width: 2.1rem;
      height: 2.1rem;
      border: 1px solid currentColor;
      border-radius: 50%;
      font: 1.25rem/1 Georgia, serif;
    }

    .cabecera > span { color: var(--suave); }

    .principal {
      display: grid;
      grid-template-columns: 1.15fr .85fr;
      align-items: center;
      min-height: 580px;
      padding: 5rem 0 4rem;
      gap: 2rem;
    }

    .etiqueta {
      margin: 0 0 1.5rem;
      color: var(--acento);
      font: 700 .72rem/1.4 system-ui, sans-serif;
      letter-spacing: .15em;
      text-transform: uppercase;
    }

    h1 {
      max-width: 8.5ch;
      margin: 0;
      font-size: clamp(4rem, 8.5vw, 8rem);
      font-weight: 400;
      letter-spacing: -.065em;
      line-height: .94;
    }

    h1 em {
      color: var(--acento);
      font-weight: 400;
    }

    .introduccion {
      max-width: 31rem;
      margin: 2rem 0;
      font-size: clamp(1.1rem, 1.5vw, 1.3rem);
      line-height: 1.6;
    }

    .enlace {
      display: inline-flex;
      align-items: center;
      gap: 1rem;
      padding: .85rem 0;
      border-bottom: 1px solid var(--tinta);
      text-decoration: none;
      font: 700 .78rem/1.2 system-ui, sans-serif;
      letter-spacing: .06em;
      text-transform: uppercase;
    }

    .enlace:hover { color: var(--acento); }

    .ilustracion {
      position: relative;
      width: min(100%, 490px);
      justify-self: center;
    }

    .ilustracion svg {
      display: block;
      width: 100%;
      height: auto;
    }

    .nota {
      position: absolute;
      right: 0;
      bottom: 3%;
      max-width: 10rem;
      margin: 0;
      color: var(--suave);
      font: italic .9rem/1.4 Georgia, serif;
      transform: rotate(-5deg);
    }

    .franja {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      padding: 1rem 0;
      border-top: 1px solid var(--tinta);
      border-bottom: 1px solid var(--tinta);
      font: 700 .7rem/1.4 system-ui, sans-serif;
      letter-spacing: .12em;
      text-transform: uppercase;
    }

    .franja span:last-child { color: var(--suave); }

    .preguntas {
      display: grid;
      grid-template-columns: .8fr 1.2fr;
      gap: 4rem;
      padding: 5rem 0 6rem;
    }

    h2 {
      margin: 0 0 1rem;
      font-size: clamp(2.5rem, 4vw, 4rem);
      font-weight: 400;
      letter-spacing: -.04em;
      line-height: 1;
    }

    .presentacion p {
      max-width: 22rem;
      color: var(--suave);
      font-size: 1.05rem;
      line-height: 1.6;
    }

    details { border-bottom: 1px solid var(--linea); }
    details:first-child { border-top: 1px solid var(--linea); }

    summary {
      display: grid;
      grid-template-columns: 2.5rem 1fr auto;
      gap: 1rem;
      align-items: baseline;
      padding: 1.4rem 0;
      cursor: pointer;
      list-style: none;
      font-size: clamp(1.2rem, 2vw, 1.6rem);
    }

    summary::-webkit-details-marker { display: none; }

    summary::after {
      content: "+";
      color: var(--acento);
      font: 1.7rem/1 system-ui, sans-serif;
    }

    details[open] summary::after { content: "−"; }
    summary:hover { color: var(--acento); }

    .numero {
      color: var(--suave);
      font: .7rem/1 system-ui, sans-serif;
      letter-spacing: .1em;
    }

    .respuesta {
      max-width: 37rem;
      padding: 0 2.5rem 1.5rem 3.5rem;
      font-size: 1.05rem;
      line-height: 1.6;
    }

    .respuesta p { margin: 0 0 .8rem; }
    .respuesta p:last-child { margin-bottom: 0; }

    footer {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      padding: 1.5rem 0 2rem;
      border-top: 1px solid var(--tinta);
      color: var(--suave);
      font: .75rem/1.5 system-ui, sans-serif;
    }

    @media (max-width: 700px) {
      .pagina { width: min(100% - 2rem, 1280px); }
      .cabecera > span { display: none; }
      .principal {
        grid-template-columns: 1fr;
        min-height: auto;
        padding: 4rem 0 3rem;
      }
      h1 { font-size: clamp(3.8rem, 15vw, 6rem); }
      .ilustracion { width: min(85%, 380px); }
      .preguntas {
        grid-template-columns: 1fr;
        gap: 2rem;
        padding: 4rem 0;
      }
      .franja span:last-child { text-align: right; }
      footer { flex-direction: column; }
    }

    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
    }
  </style>
</head>
<body>
  <div class="pagina">
    <header class="cabecera">
      <a class="marca" href="#inicio">
        <span class="sello" aria-hidden="true">?</span>
        La casa de las preguntas
      </a>
      <span>Un pequeño espacio para pensar</span>
    </header>

    <main id="inicio">
      <section class="principal" aria-labelledby="titulo">
        <div>
          <p class="etiqueta">Pasá, no hace falta saber</p>
          <h1 id="titulo">Pensar también es <em>abrir.</em></h1>
          <p class="introduccion">
            Una pregunta puede ser una llave, una ventana o apenas
            una manera de sentarse junto a algo que todavía no entendemos.
            Esta casa está hecha para eso.
          </p>
          <a class="enlace" href="#puertas">
            Elegí una puerta <span aria-hidden="true">↘</span>
          </a>
        </div>

        <div class="ilustracion" aria-hidden="true">
          <svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
            <circle cx="250" cy="250" r="190" fill="#e5e7d9"/>
            <circle cx="250" cy="250" r="155" fill="none" stroke="#aeb9a9" stroke-width="1"/>
            <path d="M126 390h248" fill="none" stroke="#202d29" stroke-width="2"/>
            <path d="M170 390V210c0-45 36-81 80-81s80 36 80 81v180"
                  fill="#d95e3d" stroke="#202d29" stroke-width="2"/>
            <path d="M194 390V215c0-31 25-56 56-56s56 25 56 56v175"
                  fill="#f3f0e6" stroke="#202d29" stroke-width="2"/>
            <path d="M211 390V219c0-22 17-39 39-39s39 17 39 39v171z"
                  fill="#202d29"/>
            <path d="M211 390V219c0-22 17-39 39-39v210z"
                  fill="#e4bb56" stroke="#202d29" stroke-width="2"/>
            <circle cx="237" cy="291" r="3" fill="#202d29"/>
            <path d="M90 177l17 5m-2-20 7 16m272 72 19-2m-11-10 2 20M131 285l-17 12"
                  fill="none" stroke="#d95e3d" stroke-width="2" stroke-linecap="round"/>
            <circle cx="363" cy="148" r="7" fill="#e4bb56"/>
            <circle cx="136" cy="239" r="4" fill="#202d29"/>
          </svg>
          <p class="nota">No todas las puertas llevan al mismo lugar.</p>
        </div>
      </section>

      <div class="franja" aria-hidden="true">
        <span>Una invitación</span>
        <span>Tres puertas · ningún examen</span>
      </div>

      <section class="preguntas" id="puertas" aria-labelledby="titulo-puertas">
        <div class="presentacion">
          <p class="etiqueta">Para empezar</p>
          <h2 id="titulo-puertas">Tres puertas</h2>
          <p>
            Abrí la que te llame. No hay respuestas correctas
            ni necesidad de llegar a una conclusión.
          </p>
        </div>

        <div>
          <details>
            <summary><span class="numero">01</span><span>La puerta de lo cotidiano</span></summary>
            <div class="respuesta">
              <p>¿Qué cosa pequeña viste tantas veces que dejaste de mirarla?</p>
              <p>Probá describirla como si alguien la encontrara por primera vez dentro de cien años.</p>
            </div>
          </details>
          <details>
            <summary><span class="numero">02</span><span>La puerta de la duda</span></summary>
            <div class="respuesta">
              <p>¿Qué creencia tuya se volvería más interesante si le agregaras «por ahora»?</p>
              <p>No hace falta abandonarla. Alcanza con dejarle una ventana abierta.</p>
            </div>
          </details>
          <details>
            <summary><span class="numero">03</span><span>La puerta de lo posible</span></summary>
            <div class="respuesta">
              <p>Si pudieras hacer una sola cosa un poco más amable, ¿cuál sería?</p>
              <p>Imaginá la versión más pequeña de ese cambio: una que pudiera ocurrir hoy.</p>
            </div>
          </details>
        </div>
      </section>
    </main>

    <footer>
      <span>La casa de las preguntas</span>
      <span>Podés quedarte un rato o seguir camino.</span>
    </footer>
  </div>
</body>
</html>
```

Qué: Una pequeña casa de preguntas, con tres puertas que se abren a distintas maneras de mirar y pensar.