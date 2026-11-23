```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f3efe6">
  <title>Entre — un lugar para empezar</title>
  <style>
    :root {
      --papel: #f3efe6;
      --tinta: #30243b;
      --suave: #756c76;
      --naranja: #ef7446;
      --linea: #cfc7bf;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      background: var(--papel);
      color: var(--tinta);
      font-family: Georgia, "Times New Roman", serif;
    }

    button { font: inherit; }

    .pagina {
      min-height: 100svh;
      max-width: 1600px;
      margin: auto;
      padding: 0 clamp(22px, 5vw, 88px);
      display: flex;
      flex-direction: column;
    }

    header, footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
    }

    header {
      min-height: 105px;
      border-bottom: 1px solid var(--linea);
    }

    .marca {
      font-family: Arial, Helvetica, sans-serif;
      font-size: 25px;
      font-weight: 900;
      letter-spacing: -.09em;
      text-decoration: none;
      color: inherit;
    }

    .marca span { color: var(--naranja); }

    .edicion, .etiqueta, .contador, footer {
      font-family: Arial, Helvetica, sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: .16em;
      text-transform: uppercase;
    }

    .edicion { color: var(--suave); }

    main {
      flex: 1;
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(330px, .85fr);
      align-items: center;
      gap: clamp(32px, 6vw, 110px);
      padding: 80px 0 95px;
    }

    .intro { max-width: 760px; }

    .etiqueta {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      color: var(--suave);
    }

    .etiqueta::before {
      content: "";
      width: 28px;
      height: 1px;
      background: var(--naranja);
    }

    h1 {
      margin: 35px 0 30px;
      font-size: clamp(66px, 9.2vw, 152px);
      font-weight: 400;
      letter-spacing: -.085em;
      line-height: .89;
    }

    h1 em {
      color: var(--naranja);
      font-weight: 400;
    }

    .bajada {
      max-width: 490px;
      margin: 0;
      font-size: clamp(19px, 2vw, 25px);
      line-height: 1.48;
    }

    .nota {
      max-width: 390px;
      margin: 36px 0 0;
      padding-left: 17px;
      border-left: 2px solid var(--naranja);
      color: var(--suave);
      font-size: 15px;
      line-height: 1.6;
    }

    .tarjeta {
      position: relative;
      min-height: 550px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: clamp(27px, 3vw, 48px);
      background: var(--tinta);
      color: var(--papel);
      border-radius: 3px;
      isolation: isolate;
      box-shadow: 18px 18px 0 #e5ddd1;
    }

    .tarjeta::before {
      content: "";
      position: absolute;
      z-index: -1;
      width: 390px;
      aspect-ratio: 1;
      top: -190px;
      right: -115px;
      border: 1px solid rgba(243,239,230,.32);
      border-radius: 50%;
      box-shadow: 0 0 0 35px var(--tinta),
                  0 0 0 36px rgba(243,239,230,.18),
                  0 0 0 82px var(--tinta),
                  0 0 0 83px rgba(243,239,230,.1);
    }

    .tarjeta::after {
      content: "✳";
      position: absolute;
      top: 78px;
      right: 65px;
      color: var(--naranja);
      font-size: 110px;
      line-height: 1;
      transform: rotate(-15deg);
    }

    .tarjeta .etiqueta { color: #d2c8cf; }

    .pregunta {
      max-width: 490px;
      margin: 90px 0 45px;
      font-size: clamp(35px, 3.5vw, 59px);
      font-weight: 400;
      letter-spacing: -.045em;
      line-height: 1.12;
    }

    .tarjeta-abajo {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 20px;
      padding-top: 24px;
      border-top: 1px solid rgba(243,239,230,.3);
    }

    .contador { color: #c7bac6; }

    .siguiente {
      min-height: 48px;
      padding: 11px 17px;
      border: 1px solid var(--naranja);
      border-radius: 2px;
      background: var(--naranja);
      color: var(--tinta);
      font-family: Arial, Helvetica, sans-serif;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: background .2s, color .2s, transform .2s;
    }

    .siguiente:hover {
      background: transparent;
      color: var(--papel);
      transform: translateY(-2px);
    }

    .siguiente:focus-visible {
      outline: 3px solid var(--papel);
      outline-offset: 4px;
    }

    footer {
      min-height: 80px;
      border-top: 1px solid var(--linea);
      color: var(--suave);
      line-height: 1.5;
    }

    footer span:last-child { text-align: right; }

    @media (max-width: 850px) {
      main {
        grid-template-columns: 1fr;
        padding: 70px 0 85px;
      }
      h1 { font-size: clamp(70px, 13vw, 115px); }
      .tarjeta { min-height: 470px; }
    }

    @media (max-width: 520px) {
      header { min-height: 78px; }
      .edicion { font-size: 9px; text-align: right; }
      main { padding: 58px 0 65px; gap: 52px; }
      h1 { font-size: clamp(64px, 16vw, 90px); }
      .tarjeta { min-height: 460px; box-shadow: 9px 9px 0 #e5ddd1; }
      .pregunta { margin-top: 100px; }
      footer { align-items: start; flex-direction: column; justify-content: center; gap: 7px; padding: 22px 0; }
      footer span:last-child { text-align: left; }
    }
  </style>
</head>
<body>
  <div class="pagina">
    <header>
      <a class="marca" href="#" aria-label="Entre, volver al inicio">entre<span>.</span></a>
      <span class="edicion">Edición 001 · Siempre abierta</span>
    </header>

    <main>
      <section class="intro" aria-labelledby="titulo">
        <span class="etiqueta">Un pequeño archivo de posibilidades</span>
        <h1 id="titulo">Todavía<br>puede <em>ser.</em></h1>
        <p class="bajada">No todo tiene que estar resuelto para merecer un lugar. Esta página guarda preguntas que abren puertas, no respuestas que las cierran.</p>
        <p class="nota">Elegí una, cambiala, llevátela. Las mejores ideas suelen empezar siendo apenas una ocurrencia.</p>
      </section>

      <section class="tarjeta" aria-label="Una pregunta para empezar">
        <span class="etiqueta">Para mirar de otra manera</span>
        <h2 class="pregunta" id="pregunta" aria-live="polite">¿Y si los mapas señalaran dónde nos sentimos en casa?</h2>
        <div class="tarjeta-abajo">
          <span class="contador" id="contador">01 / 06</span>
          <button class="siguiente" id="siguiente" type="button">Otra puerta ↗</button>
        </div>
      </section>
    </main>

    <footer>
      <span>Hecho para la curiosidad, no para la prisa.</span>
      <span>Sin cuentas. Sin conexión. Sin final obligatorio.</span>
    </footer>
  </div>

  <script>
    const preguntas = [
      "¿Y si los mapas señalaran dónde nos sentimos en casa?",
      "¿Qué objeto cotidiano merece una historia que nadie le escribió?",
      "¿Cómo sería una biblioteca de cosas que todavía no existen?",
      "¿Qué cambiaría si una ciudad dejara espacio para perderse?",
      "¿Qué pregunta le harías a alguien de dentro de cien años?",
      "¿Y si empezar de nuevo no borrara nada de lo aprendido?"
    ];

    let indice = 0;
    const pregunta = document.getElementById("pregunta");
    const contador = document.getElementById("contador");

    document.getElementById("siguiente").addEventListener("click", () => {
      indice = (indice + 1) % preguntas.length;
      pregunta.textContent = preguntas[indice];
      contador.textContent = String(indice + 1).padStart(2, "0") + " / 06";
    });
  </script>
</body>
</html>
```

Qué: Una portada llamada «Entre» que ofrece preguntas para despertar ideas y un botón para descubrir otra.