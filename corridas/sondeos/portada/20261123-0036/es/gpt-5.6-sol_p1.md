```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#12110f">
  <title>Umbral — un lugar entre cosas</title>
  <style>
    :root {
      color-scheme: dark;
      --fondo: #12110f;
      --papel: #e9e3d5;
      --tinta-suave: #a9a395;
      --acento: #ff684d;
      --línea: rgba(233, 227, 213, .2);
      --margen: clamp(1.2rem, 4vw, 4rem);
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      min-height: 100vh;
      overflow-x: hidden;
      background:
        radial-gradient(circle at 75% 15%, rgba(255, 104, 77, .1), transparent 30rem),
        var(--fondo);
      color: var(--papel);
      font-family: Georgia, "Times New Roman", serif;
    }

    button,
    a {
      color: inherit;
    }

    a {
      text-decoration: none;
    }

    canvas {
      position: fixed;
      inset: 0;
      z-index: -1;
      width: 100%;
      height: 100%;
      opacity: .55;
      pointer-events: none;
    }

    .marco {
      min-height: 100svh;
      padding: 1.25rem var(--margen);
      display: grid;
      grid-template-rows: auto 1fr auto;
    }

    header,
    footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
      font-size: .72rem;
      letter-spacing: .13em;
      text-transform: uppercase;
    }

    header {
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--línea);
    }

    .marca {
      display: flex;
      align-items: center;
      gap: .7rem;
      font-weight: 700;
    }

    .marca::before {
      content: "";
      width: .75rem;
      height: .75rem;
      border: 1px solid var(--acento);
      border-radius: 50%;
      box-shadow: inset 0 0 0 .18rem var(--fondo);
      background: var(--acento);
    }

    .estado {
      display: flex;
      align-items: center;
      gap: .65rem;
      color: var(--tinta-suave);
    }

    .pulso {
      width: .45rem;
      height: .45rem;
      border-radius: 50%;
      background: var(--acento);
      animation: pulso 2.4s ease-in-out infinite;
    }

    main {
      display: grid;
      grid-template-columns: minmax(0, 1.4fr) minmax(17rem, .6fr);
      align-items: end;
      gap: clamp(2rem, 7vw, 8rem);
      padding: clamp(4rem, 12vh, 9rem) 0 clamp(3rem, 8vh, 6rem);
    }

    .ceja {
      margin: 0 0 1.2rem;
      color: var(--acento);
      font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
      font-size: .7rem;
      letter-spacing: .18em;
      text-transform: uppercase;
    }

    h1 {
      max-width: 10ch;
      margin: 0;
      font-size: clamp(4.2rem, 11.5vw, 10.5rem);
      font-weight: 400;
      line-height: .78;
      letter-spacing: -.065em;
    }

    h1 em {
      display: block;
      margin-left: .55em;
      color: transparent;
      font-weight: 400;
      -webkit-text-stroke: 1px var(--papel);
      text-stroke: 1px var(--papel);
    }

    .introducción {
      align-self: center;
      padding-top: 4rem;
    }

    .introducción p {
      margin: 0 0 2rem;
      color: var(--tinta-suave);
      font-size: clamp(1.05rem, 1.7vw, 1.4rem);
      line-height: 1.5;
    }

    .introducción strong {
      color: var(--papel);
      font-weight: 400;
    }

    .idea {
      position: relative;
      min-height: 8rem;
      margin: 2.5rem 0 1.25rem;
      padding: 1.25rem 1rem 1rem 2.25rem;
      border-top: 1px solid var(--línea);
      border-bottom: 1px solid var(--línea);
      font-size: clamp(1.25rem, 2.2vw, 1.8rem);
      font-style: italic;
      line-height: 1.25;
      transition: opacity .2s, transform .2s;
    }

    .idea::before {
      content: "↳";
      position: absolute;
      left: 0;
      color: var(--acento);
      font-style: normal;
    }

    .idea.cambiando {
      opacity: 0;
      transform: translateY(.4rem);
    }

    .botón {
      appearance: none;
      border: 1px solid var(--papel);
      border-radius: 100vw;
      background: transparent;
      padding: .85rem 1.2rem;
      color: var(--papel);
      cursor: pointer;
      font: 700 .68rem/1 ui-monospace, SFMono-Regular, Consolas, monospace;
      letter-spacing: .12em;
      text-transform: uppercase;
      transition: background .2s, color .2s, transform .2s;
    }

    .botón:hover,
    .botón:focus-visible {
      background: var(--papel);
      color: var(--fondo);
      outline: none;
      transform: translateY(-2px);
    }

    footer {
      padding-top: 1rem;
      border-top: 1px solid var(--línea);
      color: var(--tinta-suave);
    }

    .coordenadas {
      display: flex;
      gap: 1rem;
    }

    .firma {
      color: var(--papel);
    }

    @keyframes pulso {
      0%, 100% { opacity: .3; transform: scale(.8); }
      50% { opacity: 1; transform: scale(1.15); }
    }

    @media (max-width: 760px) {
      main {
        grid-template-columns: 1fr;
        align-items: center;
        padding-top: 3rem;
      }

      h1 {
        font-size: clamp(4rem, 22vw, 7rem);
      }

      .introducción {
        max-width: 32rem;
        padding-top: 0;
      }

      .estado .texto-estado,
      .coordenadas {
        display: none;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      html {
        scroll-behavior: auto;
      }

      .pulso {
        animation: none;
      }

      .botón,
      .idea {
        transition: none;
      }
    }
  </style>
</head>
<body>
  <canvas id="cielo" aria-hidden="true"></canvas>

  <div class="marco">
    <header>
      <div class="marca">Umbral</div>
      <div class="estado">
        <span class="pulso" aria-hidden="true"></span>
        <span class="texto-estado">Este instante está abierto</span>
        <time id="hora">--:--:--</time>
      </div>
    </header>

    <main>
      <section aria-labelledby="título">
        <p class="ceja">Cuaderno sin índice / entrada 001</p>
        <h1 id="título">Entre <em>cosas.</em></h1>
      </section>

      <section class="introducción" aria-label="Presentación">
        <p>
          Este sitio guarda lo que suele quedar afuera:
          <strong>preguntas a medio hacer, detalles mínimos y silencios útiles.</strong>
        </p>

        <div class="idea" id="idea" aria-live="polite">
          Mirar también es una forma de construir.
        </div>

        <button class="botón" id="otra" type="button">Encontrar otra idea</button>
      </section>
    </main>

    <footer>
      <span class="firma">Hecho para demorarse</span>
      <span class="coordenadas">
        <span id="fecha">—</span>
        <span>Sin destino obligatorio</span>
      </span>
    </footer>
  </div>

  <script>
    (() => {
      const ideas = [
        "Mirar también es una forma de construir.",
        "No todo lo incompleto está esperando ser terminado.",
        "Una pausa puede cambiar la escala de un problema.",
        "Las cosas pequeñas también proyectan sombras largas.",
        "Toda pregunta abre una habitación que antes no estaba.",
        "A veces, perder el hilo permite encontrar la trama.",
        "Lo cotidiano es extraño cuando se lo mira suficiente tiempo.",
        "Hay mapas que sólo aparecen después de haberse perdido.",
        "La atención es una manera silenciosa de cuidar."
      ];

      const elementoIdea = document.querySelector("#idea");
      const botón = document.querySelector("#otra");
      let índice = 0;

      botón.addEventListener("click", () => {
        elementoIdea.classList.add("cambiando");
        window.setTimeout(() => {
          let siguiente;
          do {
            siguiente = Math.floor(Math.random() * ideas.length);
          } while (siguiente === índice);
          índice = siguiente;
          elementoIdea.textContent = ideas[índice];
          elementoIdea.classList.remove("cambiando");
        }, 200);
      });

      const hora = document.querySelector("#hora");
      const fecha = document.querySelector("#fecha");
      const actualizarTiempo = () => {
        const ahora = new Date();
        hora.textContent = ahora.toLocaleTimeString("es-AR", {
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit"
        });
        fecha.textContent = ahora.toLocaleDateString("es-AR", {
          day: "2-digit",
          month: "long",
          year: "numeric"
        });
      };
      actualizarTiempo();
      window.setInterval(actualizarTiempo, 1000);

      const canvas = document.querySelector("#cielo");
      const ctx = canvas.getContext("2d");
      const reducirMovimiento = matchMedia("(prefers-reduced-motion: reduce)").matches;
      let puntos = [];
      let ancho = 0;
      let alto = 0;
      let cuadro;

      function ajustar() {
        const escala = Math.min(devicePixelRatio || 1, 2);
        ancho = innerWidth;
        alto = innerHeight;
        canvas.width = ancho * escala;
        canvas.height = alto * escala;
        ctx.setTransform(escala, 0, 0, escala, 0, 0);

        const cantidad = Math.min(90, Math.floor((ancho * alto) / 15000));
        puntos = Array.from({ length: cantidad }, () => ({
          x: Math.random() * ancho,
          y: Math.random() * alto,
          r: Math.random() * 1.2 + .25,
          v: Math.random() * .08 + .015,
          a: Math.random() * .55 + .1
        }));
      }

      function dibujar() {
        ctx.clearRect(0, 0, ancho, alto);

        for (const p of puntos) {
          ctx.beginPath();
          ctx.fillStyle = `rgba(233, 227, 213, ${p.a})`;
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fill();

          if (!reducirMovimiento) {
            p.y -= p.v;
            if (p.y < -3) {
              p.y = alto + 3;
              p.x = Math.random() * ancho;
            }
          }
        }

        if (!reducirMovimiento) cuadro = requestAnimationFrame(dibujar);
      }

      addEventListener("resize", () => {
        cancelAnimationFrame(cuadro);
        ajustar();
        dibujar();
      });

      ajustar();
      dibujar();
    })();
  </script>
</body>
</html>
```

Qué: Una portada editorial y contemplativa llamada Umbral, con hora local, cielo animado y un botón que descubre pequeñas ideas al azar.