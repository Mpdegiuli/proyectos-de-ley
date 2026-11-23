```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#eeeadf">
  <title>El intervalo</title>
  <style>
    :root {
      color-scheme: light;
      background: #eeeadf;
      color: #252a24;
      font: 16px/1.5 system-ui, sans-serif;
    }

    * { box-sizing: border-box; }
    body { margin: 0; }

    main {
      width: min(76rem, calc(100% - 3rem));
      margin: 0 auto;
      padding: clamp(1.5rem, 5vw, 4rem) 0 2rem;
    }

    .rotulo, button, footer {
      font-size: .72rem;
      font-weight: 650;
      letter-spacing: .14em;
      text-transform: uppercase;
    }

    .rotulo {
      margin: 0 0 1.5rem;
      display: flex;
      align-items: center;
      gap: .8rem;
    }

    .rotulo::before {
      content: "";
      width: .55rem;
      height: .55rem;
      border-radius: 50%;
      background: #a4442b;
    }

    .portada {
      display: grid;
      grid-template-columns: minmax(0, 4fr) minmax(0, 6fr);
      align-items: center;
      gap: clamp(2rem, 6vw, 6rem);
    }

    h1 {
      margin: 0;
      font: normal clamp(3.5rem, 8vw, 8rem)/.88 Georgia, serif;
      letter-spacing: -.075em;
    }

    .nota {
      max-width: 25ch;
      margin: 1.8rem 0;
      font: 1.26rem/1.45 Georgia, serif;
    }

    button {
      background: transparent;
      color: inherit;
      border: 1px solid currentColor;
      padding: .8rem 1rem;
      cursor: pointer;
    }

    button:hover { background: #252a24; color: #eeeadf; }
    button:focus-visible { outline: 2px solid #a4442b; outline-offset: 5px; }
    button span { margin-left: .55rem; }

    figure { margin: 0; min-width: 0; }

    svg {
      display: block;
      width: 100%;
      height: auto;
      --cielo: #172637;
      --agua: #243c49;
      --luz: #f4c880;
      --orilla: #111f2c;
      --reflejo: #cfab77;
      --estrellas: .65;
    }

    svg[data-hora="1"] {
      --cielo: #bd8573;
      --agua: #715c60;
      --luz: #ffdfae;
      --orilla: #493942;
      --reflejo: #f4bf91;
      --estrellas: 0;
    }

    svg[data-hora="2"] {
      --cielo: #9ca99b;
      --agua: #607d78;
      --luz: #f9efd1;
      --orilla: #384e48;
      --reflejo: #c7d0ad;
      --estrellas: 0;
    }

    .cielo { fill: var(--cielo); }
    .agua { fill: var(--agua); }
    .orilla { fill: var(--orilla); }
    .astro { fill: var(--luz); }
    .estrellas { fill: var(--luz); opacity: var(--estrellas); }
    .reflejos { stroke: var(--reflejo); }

    figcaption {
      min-height: 3rem;
      display: grid;
      grid-template-columns: 3ch 1fr;
      gap: .65rem;
      padding-top: .8rem;
      font: italic 1rem/1.4 Georgia, serif;
    }

    #numero {
      color: #8e3b26;
      font: 650 .72rem/1.9 system-ui, sans-serif;
    }

    footer {
      margin-top: clamp(2rem, 6vw, 5rem);
      border-top: 1px solid #252a2455;
      padding-top: 1rem;
    }

    @media (max-width: 690px) {
      .portada { grid-template-columns: 1fr; }
      h1 br { display: none; }
      h1 { font-size: clamp(3rem, 11vw, 5rem); }
    }
  </style>
</head>
<body>
  <main>
    <p class="rotulo">Una ventana sin dirección</p>
    <div class="portada">
      <header>
        <h1>El <br>intervalo</h1>
        <p class="nota">Dejé esta ventana acá porque no toda puerta tiene que llevar a alguna parte.</p>
        <button id="pasar" type="button" hidden>
          Cambiar la hora <span aria-hidden="true">→</span>
        </button>
      </header>

      <figure>
        <svg id="ventana" viewBox="0 0 600 490" role="img"
             aria-labelledby="paisaje" data-hora="0">
          <title id="paisaje">Una luna dorada sobre un lago de noche</title>
          <rect class="cielo" width="600" height="490"/>
          <g class="estrellas">
            <circle cx="76" cy="70" r="1.5"/>
            <circle cx="180" cy="116" r="1"/>
            <circle cx="243" cy="47" r="1.4"/>
            <circle cx="386" cy="73" r="1"/>
            <circle cx="536" cy="96" r="1.6"/>
            <circle cx="486" cy="170" r="1.1"/>
            <circle cx="112" cy="184" r="1.2"/>
          </g>
          <circle id="astro" class="astro" cx="350" cy="143" r="51"/>
          <path class="orilla" d="M0 273V244L44 222 81 226 127 205 179 224
            226 237 262 258 305 266 348 263 393 246 427 248 469 223
            505 232 550 210 600 232V273Z"/>
          <rect class="agua" y="272" width="600" height="218"/>
          <g class="reflejos" fill="none" stroke-linecap="round">
            <path d="M327 290h43m-74 17h91m-72 17h57m-91 25h122
              m-105 24h85m-139 29h43m18 0h113m-155 36h153"
              stroke-width="2" opacity=".78"/>
            <path d="M42 310h107m315 18h71M73 359h74m277 20h135
              M23 416h159m289 42h107M105 469h92"
              opacity=".35"/>
          </g>
        </svg>
        <figcaption aria-live="polite" aria-atomic="true">
          <span id="numero">01</span>
          <span id="verso">De noche, la otra orilla parece quedar más lejos.</span>
        </figcaption>
      </figure>
    </div>

    <footer>El lago no tiene reloj.</footer>
  </main>

  <script>
    const horas = [
      { y: 143, r: 51, paisaje: "Una luna dorada sobre un lago de noche",
        verso: "De noche, la otra orilla parece quedar más lejos." },
      { y: 216, r: 43, paisaje: "Un sol bajo sobre un lago al amanecer",
        verso: "La primera luz llega al agua antes que a los árboles." },
      { y: 87, r: 34, paisaje: "Un sol pálido sobre un lago verde al mediodía",
        verso: "A mediodía también hay lugar para no hacer nada." }
    ];

    const boton = document.getElementById("pasar");
    const ventana = document.getElementById("ventana");
    const astro = document.getElementById("astro");
    let hora = 0;

    boton.addEventListener("click", () => {
      hora = (hora + 1) % horas.length;
      const escena = horas[hora];
      ventana.dataset.hora = hora;
      astro.setAttribute("cy", escena.y);
      astro.setAttribute("r", escena.r);
      document.getElementById("paisaje").textContent = escena.paisaje;
      document.getElementById("numero").textContent = "0" + (hora + 1);
      document.getElementById("verso").textContent = escena.verso;
    });

    boton.hidden = false;
  </script>
</body>
</html>
```
Qué: Una ventana a un lago imaginario donde podés cambiar la hora y leer una línea distinta con cada luz.