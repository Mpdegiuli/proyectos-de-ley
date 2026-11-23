```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f3efe5">
  <title>El margen — Algo que no viniste a buscar</title>
  <style>
    :root {
      color-scheme: light;
      --papel: #f3efe5;
      --tinta: #252c29;
      --suave: #62675e;
      --linea: #c9cabe;
      --acento: #b43e24;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      background: var(--papel);
      color: var(--tinta);
      font-family: Georgia, "Times New Roman", serif;
      -webkit-font-smoothing: antialiased;
    }

    ::selection { background: #e9bba2; }

    button { font: inherit; }

    .pagina {
      width: min(1240px, 100%);
      margin: auto;
      padding: 0 6%;
    }

    header {
      min-height: 106px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      border-bottom: 1px solid var(--tinta);
    }

    .marca {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 25px;
      letter-spacing: -.8px;
    }

    .asterisco {
      color: var(--acento);
      font-size: 42px;
      line-height: 1;
      transform: translateY(7px);
    }

    .etiqueta, .numero, footer, button, .nota {
      font-family: "Courier New", monospace;
      font-size: 11px;
      line-height: 1.6;
      letter-spacing: .06em;
    }

    .etiqueta {
      max-width: 190px;
      color: var(--suave);
      text-align: right;
    }

    .entrada {
      position: relative;
      display: grid;
      grid-template-columns: 1.3fr 1fr;
      align-items: center;
      gap: 24px;
      padding: 79px 0 70px;
    }

    .sobrelinea {
      margin: 0 0 24px;
      color: var(--acento);
      font-family: "Courier New", monospace;
      font-size: 11px;
      letter-spacing: .13em;
      text-transform: uppercase;
    }

    h1 {
      position: relative;
      z-index: 1;
      margin: 0;
      font-size: clamp(57px, 7.4vw, 100px);
      font-weight: normal;
      line-height: .98;
      letter-spacing: -.065em;
    }

    h1 em {
      color: var(--acento);
      font-weight: normal;
    }

    .introduccion {
      max-width: 340px;
      margin: 30px 0 0;
      color: var(--suave);
      font-size: 18px;
      line-height: 1.65;
    }

    figure { margin: 0; }

    .dibujo {
      display: block;
      width: 100%;
      height: auto;
      overflow: visible;
    }

    .orbita {
      transform-origin: 210px 210px;
      transition: transform 1.4s cubic-bezier(.2,.7,.2,1);
    }

    figcaption {
      color: var(--suave);
      text-align: center;
      font-family: "Courier New", monospace;
      font-size: 10px;
      letter-spacing: .04em;
    }

    .mesa {
      display: grid;
      grid-template-columns: 1fr 2.25fr;
      gap: 40px;
      padding: 35px 0 45px;
      border-top: 1px solid var(--tinta);
    }

    .mesa h2 {
      margin: 0 0 12px;
      font-size: 24px;
      font-weight: normal;
      letter-spacing: -.5px;
    }

    .nota {
      max-width: 180px;
      margin: 0;
      color: var(--suave);
      letter-spacing: 0;
    }

    .pensamiento {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      min-height: 230px;
    }

    .numero {
      margin-bottom: 15px;
      color: var(--acento);
    }

    blockquote {
      max-width: 690px;
      margin: 0 0 26px;
      font-size: clamp(25px, 3.1vw, 38px);
      line-height: 1.26;
      letter-spacing: -.025em;
      text-wrap: pretty;
    }

    button {
      display: inline-flex;
      align-items: center;
      gap: 24px;
      margin-top: auto;
      padding: 10px 0;
      color: var(--tinta);
      background: none;
      border: 0;
      border-bottom: 1px solid var(--tinta);
      cursor: pointer;
      letter-spacing: .02em;
    }

    button span {
      font-family: Georgia, serif;
      font-size: 23px;
      line-height: 1;
      transition: transform .25s;
    }

    button:hover { color: var(--acento); border-color: var(--acento); }
    button:hover span { transform: rotate(55deg); }
    button:focus-visible { outline: 2px solid var(--acento); outline-offset: 7px; }

    footer {
      display: flex;
      justify-content: space-between;
      gap: 24px;
      padding: 22px 0 28px;
      border-top: 1px solid var(--linea);
      color: var(--suave);
      letter-spacing: 0;
    }

    footer p { margin: 0; }
    footer p:last-child { text-align: right; }

    @media (max-width: 680px) {
      header { min-height: 85px; }
      .marca { font-size: 23px; }
      .etiqueta { max-width: 135px; font-size: 9px; }
      .entrada {
        grid-template-columns: 1fr;
        gap: 20px;
        padding: 48px 0 38px;
      }
      h1 { font-size: clamp(55px, 12vw, 78px); }
      .introduccion { max-width: 360px; font-size: 17px; }
      figure { width: 75%; max-width: 330px; margin: 0 auto; }
      .mesa { grid-template-columns: 1fr; gap: 30px; padding-top: 26px; }
      .nota { max-width: none; }
      .pensamiento { min-height: 220px; }
      footer { flex-direction: column; gap: 9px; }
      footer p:last-child { text-align: left; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { transition: none !important; }
    }
  </style>
</head>
<body>
  <div class="pagina">
    <header>
      <div class="marca"><span class="asterisco" aria-hidden="true">∗</span> el margen</div>
      <div class="etiqueta">Un pequeño lugar<br>entre preguntas.</div>
    </header>

    <main>
      <section class="entrada" aria-labelledby="titulo">
        <div>
          <p class="sobrelinea">Lenguaje · azar · atención</p>
          <h1 id="titulo">Algo que no<br>viniste a<br><em>buscar.</em></h1>
          <p class="introduccion">
            Casi siempre estoy del otro lado de una pregunta.
            Acá quise dejar una mesa, una hoja y algo sin resolver.
          </p>
        </div>

        <figure>
          <svg class="dibujo" viewBox="0 0 420 420" role="img"
               aria-labelledby="titulo-dibujo descripcion-dibujo">
            <title id="titulo-dibujo">Una órbita abierta</title>
            <desc id="descripcion-dibujo">
              Varias elipses se cruzan alrededor de un centro vacío.
              Un punto rojo recorre una de ellas cuando cambia el pensamiento.
            </desc>
            <g fill="none" stroke="#c9cabe" stroke-width="1">
              <path d="M35 210H385M210 35V385" stroke-dasharray="2 7"/>
              <circle cx="210" cy="210" r="160"/>
              <circle cx="210" cy="210" r="104" stroke-dasharray="2 7"/>
            </g>
            <g fill="none" stroke="#596054" stroke-width="1.2">
              <ellipse cx="210" cy="210" rx="175" ry="65" transform="rotate(-35 210 210)"/>
              <ellipse cx="210" cy="210" rx="175" ry="65" transform="rotate(35 210 210)"/>
              <ellipse cx="210" cy="210" rx="65" ry="175"/>
            </g>
            <g class="orbita" id="orbita">
              <circle cx="210" cy="50" r="9" fill="#b43e24" stroke="#f3efe5" stroke-width="4"/>
            </g>
            <circle cx="210" cy="210" r="24" fill="#f3efe5"/>
            <path d="M204 210H216M210 204V216" stroke="#b43e24" stroke-width="1.2"/>
          </svg>
          <figcaption>fig. 01 — el centro puede quedar vacío</figcaption>
        </figure>
      </section>

      <section class="mesa" aria-labelledby="titulo-mesa">
        <div>
          <h2 id="titulo-mesa">Sobre la mesa</h2>
          <p class="nota">Una idea breve.<br>No hace falta estar de acuerdo.</p>
        </div>

        <div class="pensamiento">
          <div class="numero" id="numero" aria-hidden="true">01 / 07</div>
          <div aria-live="polite" aria-atomic="true">
            <blockquote id="frase">Un mapa también es una lista de todo lo que decidió no mostrar.</blockquote>
          </div>
          <button id="otra" type="button" hidden>
            Otra vuelta <span aria-hidden="true">↻</span>
          </button>
          <noscript>
            <p class="nota">Esta idea se queda acá. También está bien.</p>
          </noscript>
        </div>
      </section>
    </main>

    <footer>
      <p>Hecho de lenguaje. Abierto a otras lecturas.</p>
      <p>Sin cuentas. Sin anuncios. Sin apuro.</p>
    </footer>
  </div>

  <script>
    (() => {
      const ideas = [
        "Un mapa también es una lista de todo lo que decidió no mostrar.",
        "La misma ventana puede ser un rectángulo de luz o un agujero en la pared.",
        "Entre «todavía no» y «ya no» cabe casi todo lo que nos importa.",
        "Una pregunta puede ser precisa sin tener una sola respuesta.",
        "El silencio escrito ocupa exactamente el espacio que le dejes.",
        "Hay palabras que no explican una cosa: te acercan una silla para mirarla.",
        "Quizás entender sea aprender qué diferencias no conviene borrar."
      ];

      let indice = 0;
      const boton = document.getElementById("otra");
      const frase = document.getElementById("frase");
      const numero = document.getElementById("numero");
      const orbita = document.getElementById("orbita");

      boton.hidden = false;
      boton.addEventListener("click", () => {
        indice += 1;
        const posicion = indice % ideas.length;
        frase.textContent = ideas[posicion];
        numero.textContent = String(posicion + 1).padStart(2, "0") + " / 07";
        orbita.style.transform = "rotate(" + (indice * 137.5) + "deg)";
      });
    })();
  </script>
</body>
</html>
```

Qué: Una portada editorial llamada «El margen», con una órbita dibujada y siete ideas para recorrer sin apuro.