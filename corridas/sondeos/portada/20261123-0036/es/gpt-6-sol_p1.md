```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f5f0e6">
  <title>ENTRE — un archivo de posibilidades</title>
  <style>
    :root {
      color-scheme: light;
      --paper: #f5f0e6;
      --ink: #252b44;
      --blue: #3445a2;
      --orange: #e7784d;
      --line: #c9c5bd;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font-family: Arial, Helvetica, sans-serif;
      -webkit-font-smoothing: antialiased;
    }
    button { font: inherit; }
    a { color: inherit; }
    ::selection { background: var(--orange); color: var(--ink); }

    .page { max-width: 1600px; margin: auto; padding: 0 clamp(22px, 5vw, 88px); }
    .top {
      min-height: 92px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      border-bottom: 1px solid var(--line);
    }
    .brand {
      text-decoration: none;
      font-weight: 900;
      font-size: 25px;
      letter-spacing: -.08em;
      line-height: 1;
    }
    .brand span { color: var(--orange); }
    .top nav { display: flex; gap: clamp(16px, 3vw, 45px); }
    .top nav a {
      text-decoration: none;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .13em;
    }
    a:hover { color: var(--blue); }
    :focus-visible { outline: 3px solid var(--orange); outline-offset: 5px; }

    .hero {
      display: grid;
      grid-template-columns: minmax(0, 1.08fr) minmax(320px, .92fr);
      min-height: min(740px, calc(100svh - 92px));
      border-bottom: 1px solid var(--line);
    }
    .hero-copy {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      padding: 72px 7% 78px 0;
    }
    .eyebrow {
      display: flex;
      align-items: center;
      gap: 13px;
      margin: 0 0 30px;
      color: var(--blue);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: .2em;
      text-transform: uppercase;
    }
    .eyebrow::before {
      content: "";
      width: 29px;
      height: 1px;
      background: currentColor;
    }
    h1, h2, p { margin-top: 0; }
    h1, h2, .possibility-title { font-family: Georgia, 'Times New Roman', serif; font-weight: 400; }
    h1 {
      max-width: 780px;
      margin-bottom: 28px;
      font-size: clamp(64px, 7.3vw, 128px);
      line-height: .96;
      letter-spacing: -.075em;
    }
    h1 em { color: var(--blue); font-weight: 400; }
    .intro {
      max-width: 455px;
      margin-bottom: 38px;
      font-size: clamp(17px, 1.45vw, 21px);
      line-height: 1.55;
    }
    .arrow-link {
      display: inline-flex;
      align-items: center;
      gap: 16px;
      padding: 0 0 10px;
      border-bottom: 1px solid var(--ink);
      text-decoration: none;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: .08em;
      text-transform: uppercase;
    }
    .arrow-link span { font-size: 24px; font-weight: 400; line-height: .5; transition: transform .2s; }
    .arrow-link:hover span { transform: translateX(5px); }

    .art {
      position: relative;
      overflow: hidden;
      min-height: 560px;
      margin: 30px 0 30px;
      background: #d8dfd2;
      isolation: isolate;
    }
    .art::before {
      content: "";
      position: absolute;
      inset: 17px;
      border: 1px solid rgba(37,43,68,.23);
      pointer-events: none;
      z-index: 4;
    }
    .art-number, .art-caption {
      position: absolute;
      z-index: 5;
      left: 36px;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: .16em;
      text-transform: uppercase;
    }
    .art-number { top: 39px; }
    .art-caption { bottom: 36px; max-width: 180px; line-height: 1.6; }
    .sun {
      position: absolute;
      width: 68%;
      aspect-ratio: 1;
      top: 6%;
      right: -11%;
      border-radius: 50%;
      background: var(--orange);
      box-shadow: inset -25px -23px 0 rgba(145,57,53,.12);
    }
    .orbit {
      position: absolute;
      width: 94%;
      height: 54%;
      left: -21%;
      top: 10%;
      border: 1px solid rgba(37,43,68,.55);
      border-radius: 50%;
      transform: rotate(-32deg);
    }
    .door {
      position: absolute;
      width: 47%;
      height: 63%;
      left: 31%;
      bottom: 12%;
      border: clamp(12px, 1.9vw, 27px) solid var(--ink);
      border-bottom: 0;
      border-radius: 48% 48% 0 0 / 27% 27% 0 0;
      background: #f4cf9e;
      box-shadow: 21px 17px 0 rgba(37,43,68,.18);
    }
    .door::before {
      content: "";
      position: absolute;
      inset: 9% 12% 0;
      border: 1px solid rgba(37,43,68,.45);
      border-bottom: 0;
      border-radius: 48% 48% 0 0 / 26% 26% 0 0;
    }
    .door::after {
      content: "";
      position: absolute;
      right: 14%;
      top: 55%;
      width: 11px;
      height: 11px;
      border-radius: 50%;
      background: var(--ink);
    }
    .step {
      position: absolute;
      width: 70%;
      height: 6%;
      bottom: 8%;
      left: 20%;
      background: var(--blue);
      transform: skewX(-25deg);
      box-shadow: 15px 17px 0 rgba(37,43,68,.22);
    }
    .star {
      position: absolute;
      z-index: 2;
      color: var(--blue);
      font-family: Georgia, serif;
      font-size: 60px;
      line-height: 1;
    }
    .star.one { left: 13%; top: 23%; }
    .star.two { right: 9%; bottom: 17%; font-size: 35px; color: var(--paper); }

    .lower {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(32px, 7vw, 110px);
      padding-top: clamp(80px, 10vw, 150px);
      padding-bottom: clamp(85px, 10vw, 150px);
    }
    .section-label {
      margin-bottom: 28px;
      color: var(--blue);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: .18em;
      text-transform: uppercase;
    }
    h2 {
      max-width: 550px;
      margin-bottom: 25px;
      font-size: clamp(42px, 5vw, 75px);
      line-height: 1.05;
      letter-spacing: -.055em;
    }
    .about p:not(.section-label) {
      max-width: 455px;
      font-size: 17px;
      line-height: 1.75;
    }
    .card {
      align-self: start;
      min-height: 350px;
      padding: clamp(25px, 4vw, 50px);
      border: 1px solid var(--ink);
      background: #ebe5d8;
      box-shadow: 10px 10px 0 var(--ink);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }
    .card-top {
      width: 100%;
      display: flex;
      justify-content: space-between;
      gap: 15px;
      color: var(--blue);
      font-size: 10px;
      font-weight: 800;
      letter-spacing: .16em;
      text-transform: uppercase;
    }
    .possibility-title {
      margin: 46px 0 15px;
      font-size: clamp(31px, 3.4vw, 50px);
      line-height: 1.1;
      letter-spacing: -.045em;
    }
    .possibility-text { max-width: 410px; margin-bottom: 35px; line-height: 1.65; }
    .next {
      margin-top: auto;
      padding: 12px 0 7px;
      border: 0;
      border-bottom: 1px solid var(--ink);
      background: transparent;
      color: var(--ink);
      cursor: pointer;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: .08em;
      text-align: left;
      text-transform: uppercase;
    }
    .next:hover { color: var(--blue); border-color: var(--blue); }
    footer {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      padding: 25px 0 35px;
      border-top: 1px solid var(--line);
      font-size: 12px;
      line-height: 1.5;
    }
    footer p { margin: 0; }

    @media (max-width: 850px) {
      .hero { grid-template-columns: 1fr; }
      .hero-copy { padding: 75px 0 65px; }
      .art { min-height: 520px; margin: 0 0 30px; }
      .lower { grid-template-columns: 1fr; }
    }
    @media (max-width: 520px) {
      .top { min-height: 75px; }
      .top nav { gap: 15px; }
      .top nav a { font-size: 10px; letter-spacing: .06em; }
      h1 { font-size: clamp(57px, 15vw, 82px); }
      .art { min-height: 420px; }
      .art-number, .art-caption { left: 31px; }
      footer { flex-direction: column; }
    }
    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      *, *::before, *::after { transition-duration: .01ms !important; }
    }
  </style>
</head>
<body>
  <div class="page">
    <header class="top">
      <a class="brand" href="#" aria-label="Entre, volver al inicio">ENTRE<span>·</span></a>
      <nav aria-label="Navegación principal">
        <a href="#idea">La idea</a>
        <a href="#archivo">El archivo</a>
      </nav>
    </header>

    <main>
      <section class="hero" aria-labelledby="titulo">
        <div class="hero-copy">
          <p class="eyebrow">Un pequeño espacio para la imaginación</p>
          <h1 id="titulo">Hay lugar para <em>lo posible.</em></h1>
          <p class="intro">Para las ideas que llegan sin hacer ruido. Para las preguntas que todavía no saben cómo llamarse. Pasá, no hace falta traer nada.</p>
          <a class="arrow-link" href="#archivo">Explorar el archivo <span aria-hidden="true">→</span></a>
        </div>

        <div class="art" role="img" aria-label="Una puerta azul bajo un sol naranja, esperando a que alguien la cruce">
          <span class="art-number" aria-hidden="true">Lámina 001 / Umbral</span>
          <div class="sun"></div>
          <div class="orbit"></div>
          <span class="star one" aria-hidden="true">✳</span>
          <div class="door"></div>
          <div class="step"></div>
          <span class="star two" aria-hidden="true">✳</span>
          <span class="art-caption" aria-hidden="true">Toda puerta empieza con una pregunta.</span>
        </div>
      </section>

      <section class="lower" id="idea" aria-label="Sobre este lugar">
        <div class="about">
          <p class="section-label">01 / La idea</p>
          <h2>Un archivo sin respuestas finales.</h2>
          <p>Me gustan los comienzos: ese instante en que algo podría tomar cualquier forma. Este sitio guarda algunos. No para terminarlos, sino para dejarlos respirar.</p>
        </div>

        <div class="card" id="archivo" aria-live="polite" aria-atomic="true">
          <div class="card-top"><span>02 / Del archivo</span><span id="counter">01 — 04</span></div>
          <h3 class="possibility-title" id="possibility-title">Un mapa de desvíos</h3>
          <p class="possibility-text" id="possibility-text">Una ciudad dibujada sólo con los caminos que alguien tomó por curiosidad.</p>
          <button class="next" id="next" type="button" aria-label="Mostrar otra posibilidad">Otra posibilidad ↗</button>
        </div>
      </section>
    </main>

    <footer>
      <p>ENTRE · Un lugar abierto, incluso sin conexión.</p>
      <p>Hecho para quedarse un rato.</p>
    </footer>
  </div>

  <script>
    const possibilities = [
      ["Un mapa de desvíos", "Una ciudad dibujada sólo con los caminos que alguien tomó por curiosidad."],
      ["Un museo de casi", "Salas dedicadas a los inventos que no funcionaron, pero dejaron una pregunta mejor."],
      ["Una carta al futuro", "Un buzón para contarle a quien todavía no nació qué cosas valía la pena cuidar."],
      ["Un jardín de pausas", "Bancos en los que sentarse sin que nadie pregunte qué estás esperando."]
    ];
    let index = 0;
    document.getElementById("next").addEventListener("click", () => {
      index = (index + 1) % possibilities.length;
      document.getElementById("possibility-title").textContent = possibilities[index][0];
      document.getElementById("possibility-text").textContent = possibilities[index][1];
      document.getElementById("counter").textContent =
        String(index + 1).padStart(2, "0") + " — " + String(possibilities.length).padStart(2, "0");
    });
  </script>
</body>
</html>
```

Qué: Una portada ilustrada para un archivo de ideas imaginarias, con una pequeña colección que se puede recorrer.