```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>Inventario de lo casi invisible</title>
  <style>
    :root {
      --papel: #f3f0e5;
      --tinta: #213a32;
      --suave: #5c6a5e;
      --linea: #b9c1ad;
      --verde: #dce6cb;
      --naranja: #df754e;
      --claro: #fffdf4;
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

    a:focus-visible, button:focus-visible {
      outline: 3px solid var(--naranja);
      outline-offset: 5px;
    }

    .contenedor {
      width: min(100% - 3rem, 1200px);
      margin-inline: auto;
    }

    .cabecera {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      padding-block: 1.4rem;
      border-bottom: 1px solid var(--linea);
      font: 700 .72rem/1.3 Arial, sans-serif;
      letter-spacing: .1em;
      text-transform: uppercase;
    }

    .marca {
      display: flex;
      align-items: center;
      gap: .6rem;
      text-decoration: none;
    }

    .marca::before {
      content: "";
      width: .75rem;
      height: .75rem;
      background: var(--naranja);
      border-radius: 50%;
    }

    .cabecera nav {
      display: flex;
      gap: 1.5rem;
    }

    .cabecera nav a {
      text-decoration: none;
    }

    .cabecera nav a:hover { text-decoration: underline; }

    .portada {
      display: grid;
      grid-template-columns: 1.12fr .88fr;
      gap: 4rem;
      align-items: center;
      padding-block: clamp(4rem, 9vw, 8rem);
    }

    .etiqueta {
      margin: 0 0 1.4rem;
      font: 700 .7rem/1.4 Arial, sans-serif;
      letter-spacing: .16em;
      text-transform: uppercase;
    }

    h1 {
      max-width: 10ch;
      margin: 0;
      font-size: clamp(3.8rem, 7.5vw, 7.4rem);
      font-weight: 400;
      line-height: .94;
      letter-spacing: -.055em;
    }

    h1 em {
      color: #b65436;
      font-weight: 400;
    }

    .intro {
      max-width: 35rem;
      margin: 2rem 0;
      color: var(--suave);
      font-size: clamp(1.1rem, 1.5vw, 1.3rem);
      line-height: 1.6;
    }

    .enlace {
      display: inline-block;
      padding-bottom: .45rem;
      border-bottom: 1px solid currentColor;
      font: 700 .78rem/1.2 Arial, sans-serif;
      letter-spacing: .06em;
      text-decoration: none;
      text-transform: uppercase;
    }

    .enlace:hover { color: #b65436; }

    .ilustracion {
      position: relative;
      display: grid;
      place-items: center;
      min-height: 31rem;
      overflow: hidden;
      background: var(--verde);
    }

    .ilustracion::before,
    .ilustracion::after {
      content: "";
      position: absolute;
      border: 1px solid rgba(33, 58, 50, .25);
      border-radius: 50%;
    }

    .ilustracion::before {
      width: 77%;
      aspect-ratio: 1;
    }

    .ilustracion::after {
      width: 95%;
      aspect-ratio: 1;
    }

    .ventana {
      position: relative;
      z-index: 1;
      width: 43%;
      aspect-ratio: .72;
      overflow: hidden;
      border: .65rem solid var(--tinta);
      border-radius: 50% 50% 0 0;
      background: #f9f1d7;
      box-shadow: .8rem .8rem 0 rgba(33, 58, 50, .12);
    }

    .ventana::before {
      content: "";
      position: absolute;
      width: 42%;
      aspect-ratio: 1;
      top: 24%;
      left: 29%;
      border-radius: 50%;
      background: var(--naranja);
    }

    .ventana::after {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(90deg, transparent 48.5%, var(--tinta) 48.5%, var(--tinta) 51.5%, transparent 51.5%),
        linear-gradient(0deg, transparent 48.5%, var(--tinta) 48.5%, var(--tinta) 51.5%, transparent 51.5%);
    }

    .nota-imagen {
      position: absolute;
      right: 1.2rem;
      bottom: 1rem;
      z-index: 2;
      margin: 0;
      font: .65rem/1.3 Arial, sans-serif;
      letter-spacing: .12em;
      text-transform: uppercase;
    }

    .seccion {
      padding-block: 4rem 5rem;
      border-top: 1px solid var(--linea);
    }

    .titulo-seccion {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 1rem;
      margin-bottom: 2rem;
    }

    .titulo-seccion h2 {
      margin: 0;
      font-size: clamp(2.1rem, 4vw, 3.5rem);
      font-weight: 400;
      letter-spacing: -.04em;
    }

    .titulo-seccion p {
      margin: 0;
      color: var(--suave);
      font: .7rem/1.4 Arial, sans-serif;
      letter-spacing: .1em;
      text-transform: uppercase;
    }

    .coleccion {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--linea);
    }

    .pieza {
      min-height: 15rem;
      padding: 1.5rem 1.5rem 0 0;
    }

    .pieza + .pieza {
      padding-left: 1.5rem;
      border-left: 1px solid var(--linea);
    }

    .numero {
      color: #a75134;
      font: 700 .7rem/1 Arial, sans-serif;
      letter-spacing: .1em;
    }

    .pieza h3 {
      max-width: 15ch;
      margin: 2.5rem 0 1rem;
      font-size: 1.75rem;
      font-weight: 400;
      line-height: 1.1;
      letter-spacing: -.03em;
    }

    .pieza p {
      max-width: 27rem;
      margin: 0;
      color: var(--suave);
      line-height: 1.55;
    }

    .ficha {
      display: grid;
      grid-template-columns: .8fr 1.2fr;
      gap: 3rem;
      padding: clamp(2rem, 5vw, 4rem);
      background: var(--tinta);
      color: var(--claro);
    }

    .ficha h2 {
      margin: 0 0 1rem;
      font-size: clamp(2.4rem, 5vw, 4rem);
      font-weight: 400;
      line-height: 1;
      letter-spacing: -.04em;
    }

    .ficha-intro {
      max-width: 23rem;
      color: #c9d6c5;
      line-height: 1.6;
    }

    .tarjeta {
      display: flex;
      min-height: 17rem;
      flex-direction: column;
      justify-content: space-between;
      padding: 2rem;
      background: var(--claro);
      color: var(--tinta);
    }

    .tarjeta .etiqueta { color: #a75134; }

    .tarjeta blockquote {
      margin: 1rem 0 2rem;
      font-size: clamp(1.6rem, 3vw, 2.4rem);
      line-height: 1.2;
      letter-spacing: -.025em;
    }

    button {
      align-self: flex-start;
      padding: .8rem 1rem;
      border: 1px solid var(--tinta);
      background: transparent;
      color: var(--tinta);
      cursor: pointer;
      font: 700 .7rem/1 Arial, sans-serif;
      letter-spacing: .08em;
      text-transform: uppercase;
    }

    button:hover {
      background: var(--tinta);
      color: var(--claro);
    }

    .pie {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      padding-block: 2rem;
      color: var(--suave);
      font: .75rem/1.5 Arial, sans-serif;
    }

    .pie p { margin: 0; }

    @media (max-width: 700px) {
      .contenedor { width: min(100% - 2rem, 1200px); }
      .cabecera { align-items: flex-start; }
      .cabecera nav { gap: .8rem; }
      .portada { grid-template-columns: 1fr; gap: 3rem; }
      .ilustracion { min-height: 24rem; }
      .coleccion { grid-template-columns: 1fr; }
      .pieza { min-height: 0; padding: 1.5rem 0 2rem; }
      .pieza + .pieza {
        padding-left: 0;
        border-left: 0;
        border-top: 1px solid var(--linea);
      }
      .pieza h3 { margin-top: 1.5rem; }
      .ficha { grid-template-columns: 1fr; gap: 1.5rem; }
      .pie { flex-direction: column; }
    }

    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
    }
  </style>
</head>
<body>
  <header class="cabecera contenedor">
    <a class="marca" href="#inicio">Inventario<br>de lo casi invisible</a>
    <nav aria-label="Navegación principal">
      <a href="#coleccion">Colección</a>
      <a href="#ficha">Una ficha</a>
    </nav>
  </header>

  <main id="inicio" class="contenedor">
    <section class="portada" aria-labelledby="titulo">
      <div>
        <p class="etiqueta">Un pequeño museo sin paredes</p>
        <h1 id="titulo">Lo que casi pasa <em>desapercibido.</em></h1>
        <p class="intro">
          Hay cosas demasiado pequeñas para guardarlas y demasiado buenas
          para dejarlas pasar. Este es un lugar para prestarles atención.
        </p>
        <a class="enlace" href="#coleccion">Entrar al inventario ↓</a>
      </div>

      <div class="ilustracion" aria-hidden="true">
        <div class="ventana"></div>
        <p class="nota-imagen">Fig. 01 · Un rato de luz</p>
      </div>
    </section>

    <section class="seccion" id="coleccion" aria-labelledby="titulo-coleccion">
      <div class="titulo-seccion">
        <h2 id="titulo-coleccion">Tres cosas para empezar</h2>
        <p>Colección abierta · 001—003</p>
      </div>

      <div class="coleccion">
        <article class="pieza">
          <span class="numero">001 / LUZ</span>
          <h3>El sol que se muda de pared</h3>
          <p>Entra por la ventana y, sin pedir permiso, va cambiando de lugar durante la tarde.</p>
        </article>
        <article class="pieza">
          <span class="numero">002 / SONIDO</span>
          <h3>El instante antes de reconocer una canción</h3>
          <p>Unas pocas notas flotan en el aire. Algo ya las conoce, aunque todavía no sabés qué.</p>
        </article>
        <article class="pieza">
          <span class="numero">003 / ENCUENTRO</span>
          <h3>La risa que llega de otra habitación</h3>
          <p>No escuchaste el chiste. Igual, por un momento, la casa parece estar de buen humor.</p>
        </article>
      </div>
    </section>

    <section class="ficha" id="ficha" aria-labelledby="titulo-ficha">
      <div>
        <p class="etiqueta">Una invitación</p>
        <h2 id="titulo-ficha">Abrí una ficha.</h2>
        <p class="ficha-intro">
          No hay que completar nada. Elegí una pequeña búsqueda y llevátela
          a tu próximo rato libre.
        </p>
      </div>

      <div class="tarjeta">
        <div aria-live="polite" aria-atomic="true">
          <p class="etiqueta">Para observar hoy</p>
          <blockquote id="consigna">Buscá una sombra que tenga una forma inesperada.</blockquote>
        </div>
        <button type="button" id="otra">Mostrar otra ficha ↗</button>
      </div>
    </section>
  </main>

  <footer class="pie contenedor">
    <p>Inventario de lo casi invisible</p>
    <p>Sin prisa. Sin entrada. Sin fecha de cierre.</p>
  </footer>

  <script>
    const consignas = [
      "Buscá una sombra que tenga una forma inesperada.",
      "Escuchá el sonido más lejano que puedas distinguir.",
      "Encontrá algo que alguien haya reparado en vez de tirar.",
      "Mirá cómo cambia un color cuando le da la luz.",
      "Prestá atención a una palabra que te guste decir en voz alta.",
      "Buscá una señal de que alguien pasó por ahí antes que vos."
    ];
    let indice = 0;
    const texto = document.getElementById("consigna");

    document.getElementById("otra").addEventListener("click", () => {
      indice = (indice + 1) % consignas.length;
      texto.textContent = consignas[indice];
    });
  </script>
</body>
</html>
```

Qué: Un pequeño museo de cosas cotidianas que suelen pasar desapercibidas, con fichas para explorar.