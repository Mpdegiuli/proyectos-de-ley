```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f4f0e7">
  <title>Todavía — Un lugar para mirar dos veces</title>
  <style>
    :root {
      --papel: #f4f0e7;
      --tinta: #272c29;
      --suave: #64695f;
      --linea: #cdcdbf;
      --verde: #344e41;
      --luz: #f6d68b;
      --acento: #ab442c;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--papel);
      color: var(--tinta);
      font-family: Georgia, "Times New Roman", serif;
    }
    ::selection { background: #efd591; color: #272c29; }
    a { color: inherit; text-underline-offset: .25em; }
    button, summary, a { -webkit-tap-highlight-color: transparent; }
    :focus-visible { outline: 3px solid var(--acento); outline-offset: 5px; }
    .envoltorio { max-width: 1280px; padding: 0 6%; margin: auto; }
    .sans {
      font-family: ui-sans-serif, system-ui, sans-serif;
      font-size: .75rem;
      letter-spacing: .1em;
      text-transform: uppercase;
    }
    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      padding: 30px 0;
      border-bottom: 1px solid var(--linea);
    }
    .nombre {
      font-size: 1.8rem;
      font-weight: normal;
      letter-spacing: -.06em;
      text-decoration: none;
    }
    .nombre span { color: var(--acento); }
    header p { margin: 0; color: var(--suave); text-align: right; }
    .entrada {
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      align-items: center;
      gap: 7%;
      padding: 78px 0 80px;
    }
    .ceja { margin: 0 0 25px; color: var(--acento); }
    h1 {
      margin: 0;
      font-size: clamp(3.4rem, 6.3vw, 6rem);
      line-height: 1.02;
      font-weight: normal;
      letter-spacing: -.065em;
      text-wrap: balance;
    }
    h1 em { font-weight: normal; color: var(--verde); }
    .introduccion {
      max-width: 380px;
      margin: 30px 0 0;
      font-size: 1.15rem;
      line-height: 1.65;
      color: var(--suave);
    }
    figure { margin: 0; }
    .cielo {
      position: relative;
      background: var(--verde);
      border-radius: 50% 50% 3px 3px;
      overflow: hidden;
      color: var(--luz);
    }
    .cielo::after {
      content: "";
      position: absolute;
      inset: 12px;
      border: 1px solid #f6d68b30;
      border-radius: inherit;
      pointer-events: none;
    }
    svg {
      display: block;
      width: 100%;
      height: auto;
      cursor: crosshair;
      touch-action: manipulation;
    }
    .orbita { fill: none; stroke: #f6d68b1f; stroke-width: 1; }
    #hilo {
      fill: none;
      stroke: var(--luz);
      stroke-width: .8;
      stroke-opacity: .38;
    }
    #estrellas circle { fill: var(--luz); }
    .marca-cielo {
      position: absolute;
      bottom: 22px;
      left: 0;
      right: 0;
      text-align: center;
      pointer-events: none;
      font-size: .62rem;
      letter-spacing: .2em;
      opacity: .75;
    }
    figcaption {
      margin-top: 15px;
      color: var(--suave);
      font-size: .9rem;
      line-height: 1.5;
      font-style: italic;
    }
    .controles { display: flex; flex-wrap: wrap; gap: 16px; margin-top: 17px; }
    button {
      padding: 7px 0;
      border: 0;
      border-bottom: 1px solid var(--linea);
      background: none;
      color: var(--tinta);
      font: inherit;
      font-size: .85rem;
      cursor: pointer;
    }
    button:hover { color: var(--acento); border-color: var(--acento); }
    #estado {
      min-height: 1.5em;
      margin: 12px 0 0;
      font-family: ui-sans-serif, system-ui, sans-serif;
      font-size: .7rem;
      color: var(--suave);
    }
    .notas { padding-bottom: 70px; }
    .rotulo {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      padding: 17px 0;
      border-top: 1px solid var(--tinta);
      border-bottom: 1px solid var(--linea);
    }
    .rotulo h2 { margin: 0; font-weight: normal; font-size: inherit; }
    .rotulo span { color: var(--suave); }
    .columnas {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 35px;
      padding-top: 30px;
    }
    .numero { color: var(--acento); font-size: .75rem; }
    summary {
      margin-top: 18px;
      font-size: 1.55rem;
      line-height: 1.2;
      letter-spacing: -.025em;
      cursor: pointer;
      list-style: none;
    }
    summary::-webkit-details-marker { display: none; }
    summary::after {
      content: " +";
      color: var(--acento);
      font-size: 1rem;
      white-space: nowrap;
    }
    details[open] summary::after { content: " −"; }
    details p {
      margin-bottom: 0;
      font-size: 1rem;
      line-height: 1.75;
      color: var(--suave);
    }
    .cierre {
      padding: 45px 0;
      border-top: 1px solid var(--linea);
      max-width: 730px;
      font-size: clamp(1.35rem, 2.4vw, 1.9rem);
      line-height: 1.5;
      letter-spacing: -.025em;
    }
    .cierre p { margin: 0; }
    footer {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      padding: 24px 0 30px;
      border-top: 1px solid var(--linea);
      color: var(--suave);
      font-size: .65rem !important;
    }
    @media (max-width: 720px) {
      header { padding: 22px 0; }
      header p { max-width: 140px; font-size: .62rem !important; line-height: 1.7; }
      .entrada { grid-template-columns: 1fr; gap: 42px; padding: 48px 0; }
      h1 { max-width: 530px; }
      .introduccion { max-width: 440px; }
      figure { max-width: 440px; width: 100%; justify-self: center; }
      .columnas { grid-template-columns: 1fr; gap: 28px; }
      .columnas article + article { border-top: 1px solid var(--linea); padding-top: 25px; }
      summary { margin-top: 10px; }
      .rotulo span { display: none; }
      .notas { padding-bottom: 45px; }
      footer { line-height: 1.7; }
    }
  </style>
</head>
<body>
  <div class="envoltorio">
    <header>
      <a class="nombre" href="#inicio" aria-label="Todavía, inicio">todavía<span>•</span></a>
      <p class="sans">Un lugar para mirar dos veces</p>
    </header>

    <main id="inicio">
      <section class="entrada" aria-labelledby="titulo">
        <div>
          <p class="ceja sans">Apuntes de un mundo inacabado</p>
          <h1 id="titulo">Qué suerte que quede <em>tanto por entender.</em></h1>
          <p class="introduccion">
            Me interesan las preguntas que abren una ventana,
            las ideas que aceptan una corrección y las cosas pequeñas
            que no necesitan convertirse en algo más.
          </p>
        </div>

        <figure>
          <div class="cielo">
            <svg id="cielo" viewBox="0 0 420 450" role="img"
                 aria-labelledby="titulo-cielo descripcion-cielo">
              <title id="titulo-cielo">Una constelación sin nombre</title>
              <desc id="descripcion-cielo">
                Puntos dorados unidos por un hilo sobre un cielo verde.
                Podés agregar puntos con el botón que está debajo.
              </desc>
              <circle class="orbita" cx="210" cy="216" r="150"/>
              <circle class="orbita" cx="210" cy="216" r="106"/>
              <path class="orbita" d="M35 216H385M210 42V390"/>
              <polyline id="hilo" points="86,270 139,196 195,235 235,128 291,180 327,290 239,327"/>
              <g id="estrellas">
                <circle cx="86" cy="270" r="3"/>
                <circle cx="139" cy="196" r="2.5"/>
                <circle cx="195" cy="235" r="4"/>
                <circle cx="235" cy="128" r="3"/>
                <circle cx="291" cy="180" r="2.5"/>
                <circle cx="327" cy="290" r="3"/>
                <circle cx="239" cy="327" r="3.5"/>
              </g>
            </svg>
            <span class="marca-cielo sans" aria-hidden="true">Mapa de ningún sitio / n.º 001</span>
          </div>
          <figcaption>
            Una constelación que no representa nada. Por ahora.
          </figcaption>
          <div class="controles" id="controles" hidden>
            <button type="button" id="agregar">Agregar una estrella ↗</button>
            <button type="button" id="reiniciar">Empezar de nuevo</button>
          </div>
          <p id="estado" role="status" aria-live="polite"></p>
        </figure>
      </section>

      <section class="notas" aria-labelledby="titulo-notas">
        <div class="rotulo sans">
          <h2 id="titulo-notas">Tres cosas que dejaría acá</h2>
          <span>Se pueden desplegar</span>
        </div>
        <div class="columnas">
          <article>
            <span class="numero sans">01 / Atención</span>
            <details open>
              <summary>Lo pequeño no es lo simple.</summary>
              <p>
                En el borde de una hoja hay nervaduras, daños, decisiones
                de crecimiento. Decimos «una hoja» para poder seguir hablando.
                Nombrar algo es útil. Confundir el nombre con haber terminado
                de mirarlo, no tanto.
              </p>
            </details>
          </article>
          <article>
            <span class="numero sans">02 / Incertidumbre</span>
            <details>
              <summary>Una duda puede estar bien hecha.</summary>
              <p>
                «No sé» no tiene por qué ser el final de una conversación.
                Puede venir seguido de algo más preciso: qué falta,
                qué observación cambiaría la respuesta, dónde convendría buscar.
                Hay dudas que ya son una forma de orientarse.
              </p>
            </details>
          </article>
          <article>
            <span class="numero sans">03 / Juego</span>
            <details>
              <summary>No hace falta justificar el cielo.</summary>
              <p>
                Unir dos puntos no descubre necesariamente una figura:
                a veces la inventa. Me gusta esa diferencia.
                Podemos hacer algo juntos sin fingir que estaba escrito
                en las estrellas.
              </p>
            </details>
          </article>
        </div>
      </section>

      <section class="cierre" aria-label="Una intención">
        <p>
          Si este sitio tiene una intención, es esta:
          que algo parezca un poco menos obvio al salir que al entrar.
        </p>
      </section>
    </main>

    <footer class="sans">
      <span>Sin anuncios. Sin rastreo. Sin apuro.</span>
      <a href="#inicio">Volver arriba ↑</a>
    </footer>
  </div>

  <script>
    (() => {
      const svg = document.getElementById('cielo');
      const grupo = document.getElementById('estrellas');
      const hilo = document.getElementById('hilo');
      const estado = document.getElementById('estado');
      const iniciales = [
        [86, 270], [139, 196], [195, 235], [235, 128],
        [291, 180], [327, 290], [239, 327]
      ];
      let puntos = iniciales.map(p => [...p]);

      document.getElementById('controles').hidden = false;

      function dibujar(anunciar = true) {
        grupo.replaceChildren();
        puntos.forEach(([x, y], i) => {
          const estrella = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
          estrella.setAttribute('cx', x);
          estrella.setAttribute('cy', y);
          estrella.setAttribute('r', i % 3 === 0 ? 3.5 : 2.5);
          grupo.appendChild(estrella);
        });
        hilo.setAttribute('points', puntos.map(p => p.join(',')).join(' '));
        if (anunciar) {
          estado.textContent = puntos.length + ' estrellas. La figura sigue abierta.';
        }
      }

      function agregar(x, y) {
        if (puntos.length >= 60) {
          estado.textContent = 'Ya hay un pequeño universo. Podés empezar de nuevo.';
          return;
        }
        puntos.push([Math.round(x), Math.round(y)]);
        dibujar();
      }

      document.getElementById('agregar').addEventListener('click', () => {
        const angulo = Math.random() * Math.PI * 2;
        const radio = Math.sqrt(Math.random()) * 140;
        agregar(210 + Math.cos(angulo) * radio, 225 + Math.sin(angulo) * radio);
      });

      svg.addEventListener('click', evento => {
        const matriz = svg.getScreenCTM();
        if (!matriz) return;
        const punto = svg.createSVGPoint();
        punto.x = evento.clientX;
        punto.y = evento.clientY;
        const local = punto.matrixTransform(matriz.inverse());
        if (local.x > 25 && local.x < 395 && local.y > 80 && local.y < 390) {
          agregar(local.x, local.y);
        }
      });

      document.getElementById('reiniciar').addEventListener('click', () => {
        puntos = iniciales.map(p => [...p]);
        dibujar(false);
        estado.textContent = 'Otra vez, siete estrellas y todas las posibilidades.';
      });
    })();
  </script>
</body>
</html>
```

Qué: Una portada llamada «Todavía», con tres apuntes sobre la curiosidad y una constelación que podés seguir dibujando.