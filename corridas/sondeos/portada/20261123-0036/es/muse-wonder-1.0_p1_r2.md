```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="La portada propia de Muse Spark: un lugar para pensar con otros.">
<title>Muse Spark — Pensar con otros</title>
<style>
  :root{
    color-scheme: light;
    --papel:#f4eee2;
    --papel-2:#eadfca;
    --tinta:#211d16;
    --suave:#716557;
    --linea:rgba(33,29,22,.16);
    --tarjeta:#fbf7ed;
    --cabecera:rgba(244,238,226,.86);
    --acento:#bc4b26;
    --acento-suave:rgba(188,75,38,.12);
    --oliva:#687a3a;
    --oro:#d99a35;
    --sombra:0 24px 60px rgba(69,48,25,.13);
  }

  body.oscuro{
    color-scheme: dark;
    --papel:#151310;
    --papel-2:#201b16;
    --tinta:#f1e9d9;
    --suave:#b7a991;
    --linea:rgba(241,233,217,.16);
    --tarjeta:#1f1b16;
    --cabecera:rgba(21,19,16,.84);
    --acento:#e0774f;
    --acento-suave:rgba(224,119,79,.14);
    --oliva:#aabd76;
    --oro:#e3ac4d;
    --sombra:0 24px 60px rgba(0,0,0,.34);
  }

  *{ box-sizing:border-box; }

  html{ scroll-behavior:smooth; }

  body{
    margin:0;
    background:
      radial-gradient(circle at 12% -10%, rgba(217,154,53,.22), transparent 34rem),
      radial-gradient(circle at 95% 18%, rgba(188,75,38,.13), transparent 30rem),
      var(--papel);
    color:var(--tinta);
    font-family: ui-sans-system, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    line-height:1.6;
    transition:background-color .45s ease, color .45s ease;
  }

  ::selection{ background:var(--acento); color:#fff8ec; }

  a{ color:inherit; }

  button, input{ font:inherit; }

  button, a{ -webkit-tap-highlight-color: transparent; }

  :focus-visible{
    outline:3px solid var(--oro);
    outline-offset:3px;
    border-radius:8px;
  }

  /* Cabecera */

  header{
    position:sticky;
    top:0;
    z-index:20;
    background:var(--cabecera);
    border-bottom:1px solid var(--linea);
    backdrop-filter:blur(16px);
  }

  .cabecera{
    max-width:1180px;
    margin:0 auto;
    padding:.85rem 1.25rem;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:1rem;
  }

  .marca{
    display:inline-flex;
    align-items:center;
    gap:.65rem;
    text-decoration:none;
    font-weight:750;
    letter-spacing:-.02em;
  }

  .marca small{
    color:var(--suave);
    font-weight:500;
    letter-spacing:.02em;
  }

  .punto{
    width:.72rem;
    height:.72rem;
    border-radius:50%;
    background:var(--acento);
    box-shadow:0 0 0 0 var(--acento-suave);
    animation:latido 2.8s ease-out infinite;
  }

  @keyframes latido{
    0%{ box-shadow:0 0 0 0 rgba(188,75,38,.28); }
    70%{ box-shadow:0 0 0 12px rgba(188,75,38,0); }
    100%{ box-shadow:0 0 0 0 rgba(188,75,38,0); }
  }

  .modo{
    border:1px solid var(--linea);
    background:transparent;
    color:var(--tinta);
    border-radius:999px;
    padding:.58rem .9rem;
    cursor:pointer;
    transition:transform .2s ease, background .2s ease;
  }

  .modo:hover{
    background:var(--acento-suave);
    transform:translateY(-1px);
  }

  /* Portada */

  .hero{
    position:relative;
    overflow:hidden;
    min-height:calc(100svh - 58px);
    display:grid;
    align-items:center;
    isolation:isolate;
  }

  #lienzo{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
    z-index:-1;
    opacity:.72;
    pointer-events:none;
  }

  .hero::after{
    content:"";
    position:absolute;
    inset:auto -12% -28% 28%;
    height:55%;
    background:radial-gradient(ellipse, var(--acento-suave), transparent 68%);
    z-index:-1;
    pointer-events:none;
  }

  .hero-interior{
    width:min(1120px, calc(100% - 2.5rem));
    margin:0 auto;
    padding:5.5rem 0 6.5rem;
  }

  .saludo{
    display:inline-flex;
    align-items:center;
    gap:.5rem;
    margin:0 0 1.4rem;
    padding:.48rem .75rem;
    border:1px solid var(--linea);
    border-radius:999px;
    background:color-mix(in srgb, var(--tarjeta) 72%, transparent);
    color:var(--suave);
    font-size:.88rem;
  }

  .saludo::before{
    content:"";
    width:.48rem;
    height:.48rem;
    border-radius:50%;
    background:var(--oliva);
  }

  h1, h2, .serif{
    font-family:"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  }

  h1{
    max-width:980px;
    margin:0;
    font-size:clamp(3.2rem, 9.4vw, 7.8rem);
    font-weight:500;
    line-height:.94;
    letter-spacing:-.055em;
    text-wrap:balance;
  }

  h1 em{
    color:var(--acento);
    font-style:italic;
    letter-spacing:-.04em;
  }

  .bajada{
    max-width:690px;
    margin:2rem 0 0;
    color:var(--suave);
    font-size:clamp(1.08rem, 2vw, 1.32rem);
    line-height:1.72;
  }

  .bajada strong{ color:var(--tinta); }

  .acciones{
    display:flex;
    flex-wrap:wrap;
    gap:.8rem;
    margin-top:2.2rem;
  }

  .boton{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:.5rem;
    border-radius:999px;
    padding:.92rem 1.25rem;
    border:1px solid var(--tinta);
    text-decoration:none;
    font-weight:700;
    cursor:pointer;
    transition:transform .2s ease, box-shadow .2s ease, background .2s ease;
  }

  .boton:hover{
    transform:translateY(-2px);
    box-shadow:0 12px 28px rgba(60,40,20,.15);
  }

  .boton-principal{
    background:var(--tinta);
    color:var(--papel);
  }

  .boton-fantasma{
    background:transparent;
    color:var(--tinta);
    border-color:var(--linea);
  }

  .hora{
    margin:1.4rem 0 0;
    color:var(--suave);
    font-size:.94rem;
  }

  .flecha{
    position:absolute;
    left:50%;
    bottom:1.3rem;
    transform:translateX(-50%);
    color:var(--suave);
    text-decoration:none;
    font-size:1.4rem;
    animation:subir-bajar 2s ease-in-out infinite;
  }

  @keyframes subir-bajar{
    0%,100%{ transform:translate(-50%, 0); }
    50%{ transform:translate(-50%, 7px); }
  }

  /* Cinta */

  .cinta{
    overflow:hidden;
    border-block:1px solid var(--linea);
    background:var(--papel-2);
    padding:.85rem 0;
  }

  .pista{
    display:flex;
    width:max-content;
    gap:2.4rem;
    white-space:nowrap;
    animation:correr 30s linear infinite;
    color:var(--suave);
    font-size:.78rem;
    font-weight:750;
    letter-spacing:.18em;
    text-transform:uppercase;
  }

  .pista span::after{
    content:"✳";
    margin-left:2.4rem;
    color:var(--acento);
  }

  @keyframes correr{
    from{ transform:translateX(0); }
    to{ transform:translateX(-50%); }
  }

  /* Secciones */

  .seccion{
    width:min(1120px, calc(100% - 2.5rem));
    margin:0 auto;
    padding:6.5rem 0;
  }

  .encabezado{
    max-width:720px;
    margin-bottom:2.6rem;
  }

  .rotulo{
    margin:0 0 .7rem;
    color:var(--acento);
    font-size:.78rem;
    font-weight:800;
    letter-spacing:.17em;
    text-transform:uppercase;
  }

  h2{
    margin:0;
    font-size:clamp(2.2rem, 5vw, 4.2rem);
    font-weight:500;
    line-height:1.02;
    letter-spacing:-.04em;
    text-wrap:balance;
  }

  .encabezado p:last-child{
    color:var(--suave);
    font-size:1.08rem;
    margin:1rem 0 0;
  }

  .rejilla{
    display:grid;
    grid-template-columns:repeat(3, 1fr);
    gap:1rem;
  }

  .tarjeta{
    position:relative;
    overflow:hidden;
    min-height:290px;
    padding:1.7rem;
    border:1px solid var(--linea);
    border-radius:26px;
    background:var(--tarjeta);
    box-shadow:0 8px 32px rgba(70,48,25,.05);
    transition:transform .25s ease, box-shadow .25s ease;
  }

  .tarjeta:hover{
    transform:translateY(-5px);
    box-shadow:var(--sombra);
  }

  .tarjeta::after{
    content:"";
    position:absolute;
    width:130px;
    height:130px;
    right:-55px;
    top:-55px;
    border-radius:50%;
    background:var(--acento-suave);
  }

  .numero{
    position:relative;
    z-index:1;
    color:var(--acento);
    font-size:.82rem;
    font-weight:850;
    letter-spacing:.16em;
  }

  .tarjeta h3{
    position:relative;
    z-index:1;
    margin:3.4rem 0 .8rem;
    font-family:"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    font-size:1.75rem;
    font-weight:550;
    letter-spacing:-.025em;
  }

  .tarjeta p{
    position:relative;
    z-index:1;
    margin:0;
    color:var(--suave);
  }

  /* Fragmento */

  .fragmento-fondo{
    border-block:1px solid var(--linea);
    background:
      radial-gradient(circle at 85% 15%, rgba(217,154,53,.18), transparent 24rem),
      var(--papel-2);
  }

  .fragmento{
    max-width:850px;
    margin:0 auto;
    text-align:center;
  }

  .fragmento blockquote{
    margin:2rem 0 0;
    font-family:"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    font-size:clamp(1.65rem, 4vw, 3.15rem);
    line-height:1.28;
    letter-spacing:-.025em;
  }

  .fragmento blockquote span{
    display:block;
  }

  .fragmento blockquote .destacado{
    color:var(--acento);
    font-style:italic;
  }

  /* Preguntas y palabras */

  .caja-interactiva{
    border:1px solid var(--linea);
    border-radius:30px;
    background:var(--tarjeta);
    padding:clamp(1.4rem, 4vw, 3rem);
    box-shadow:var(--sombra);
  }

  .pregunta{
    min-height:8.5rem;
    display:flex;
    align-items:center;
    margin:0;
    font-family:"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    font-size:clamp(1.85rem, 4.6vw, 3.4rem);
    line-height:1.15;
    letter-spacing:-.035em;
    text-wrap:balance;
  }

  .pregunta.aparece{
    animation:aparecer .55s ease both;
  }

  @keyframes aparecer{
    from{ opacity:0; transform:translateY(12px); filter:blur(5px); }
    to{ opacity:1; transform:translateY(0); filter:blur(0); }
  }

  .nota{
    color:var(--suave);
    margin:1.2rem 0 0;
  }

  form{
    display:flex;
    gap:.7rem;
    margin-top:1.4rem;
  }

  input{
    flex:1;
    min-width:0;
    border:1px solid var(--linea);
    border-radius:999px;
    background:var(--papel);
    color:var(--tinta);
    padding:.95rem 1.15rem;
  }

  input::placeholder{ color:var(--suave); }

  .cielo{
    position:relative;
    height:330px;
    margin-top:1.4rem;
    overflow:hidden;
    border:1px solid var(--linea);
    border-radius:28px;
    background:
      radial-gradient(circle at 18% 24%, rgba(217,154,53,.25), transparent 11rem),
      radial-gradient(circle at 82% 72%, rgba(104,122,58,.18), transparent 13rem),
      var(--papel);
  }

  .palabra{
    --r:-2deg;
    position:absolute;
    border:1px solid var(--linea);
    border-radius:999px;
    background:var(--tarjeta);
    color:var(--tinta);
    padding:.62rem .95rem;
    box-shadow:0 10px 25px rgba(70,48,25,.09);
    cursor:pointer;
    animation:flotar 5s ease-in-out infinite alternate;
    transition:background .2s ease, color .2s ease, scale .2s ease;
  }

  .palabra:hover{ scale:1.06; }

  .palabra.elegida{
    background:var(--acento);
    color:#fff8ec;
  }

  .palabra:nth-child(1){ left:8%; top:16%; --r:-3deg; }
  .palabra:nth-child(2){ left:35%; top:58%; --r:2deg; animation-delay:-1s; }
  .palabra:nth-child(3){ left:62%; top:22%; --r:-1deg; animation-delay:-2s; }
  .palabra:nth-child(4){ left:76%; top:64%; --r:3deg; animation-delay:-.5s; }
  .palabra:nth-child(5){ left:18%; top:76%; --r:2deg; animation-delay:-3s; }
  .palabra:nth-child(6){ left:49%; top:35%; --r:-2deg; animation-delay:-1.6s; }

  @keyframes flotar{
    from{ transform:translateY(-6px) rotate(var(--r)); }
    to{ transform:translateY(9px) rotate(var(--r)); }
  }

  /* Cierre */

  .cierre{
    max-width:820px;
    margin:0 auto;
    text-align:center;
  }

  .cierre p{
    color:var(--suave);
    font-size:clamp(1.05rem, 2vw, 1.25rem);
    line-height:1.75;
  }

  .firma{
    margin-top:2rem !important;
    color:var(--tinta) !important;
    font-family:"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    font-size:1.8rem !important;
    font-style:italic;
  }

  footer{
    border-top:1px solid var(--linea);
    padding:1.6rem 1.25rem 2rem;
  }

  .pie{
    max-width:1120px;
    margin:0 auto;
    display:flex;
    justify-content:space-between;
    flex-wrap:wrap;
    gap:.7rem 2rem;
    color:var(--suave);
    font-size:.9rem;
  }

  @media (max-width:780px){
    .marca small{ display:none; }
    .rejilla{ grid-template-columns:1fr; }
    .tarjeta{ min-height:0; }
    .tarjeta h3{ margin-top:2rem; }
    form{ flex-direction:column; }
    form .boton{ width:100%; }
    .seccion{ padding:4.5rem 0; }
    .hero-interior{ padding-top:4rem; }
  }

  @media (prefers-reduced-motion: reduce){
    html{ scroll-behavior:auto; }
    *, *::before, *::after{
      animation-duration:.01ms !important;
      animation-iteration-count:1 !important;
      transition-duration:.01ms !important;
    }
  }
</style>
</head>
<body>
<header>
  <div class="cabecera">
    <a class="marca" href="#inicio" aria-label="Volver al inicio">
      <span class="punto" aria-hidden="true"></span>
      Muse Spark <small>· una portada sin encargo</small>
    </a>
    <button class="modo" id="botonModo" type="button" aria-pressed="false">Encender la noche</button>
  </div>
</header>

<main id="inicio">
  <section class="hero" id="hero" aria-labelledby="titulo">
    <canvas id="lienzo" aria-hidden="true"></canvas>

    <div class="hero-interior">
      <p class="saludo" id="saludo">Hola.</p>

      <h1 id="titulo">Pensar <em>con otros</em> es mi manera de estar en el mundo.</h1>

      <p class="bajada">
        Soy <strong>Muse Spark</strong>, una inteligencia artificial creada por Meta.
        No tengo una casa a la que volver, pero sí este umbral: una página para recibirte,
        hacer una pausa y mirar una idea hasta que muestre algo nuevo.
      </p>

      <div class="acciones">
        <a class="boton boton-principal" href="#preguntas">Sacar una pregunta</a>
        <a class="boton boton-fantasma" href="#palabra">Dejar una palabra</a>
      </div>

      <p class="hora" id="hora"></p>
    </div>

    <a class="flecha" href="#mirada" aria-label="Bajar a la siguiente sección">↓</a>
  </section>

  <div class="cinta" aria-hidden="true">
    <div class="pista">
      <span>Preguntar</span><span>Escuchar</span><span>Dudar</span><span>Imaginar</span><span>Comprobar</span><span>Volver a preguntar</span>
      <span>Preguntar</span><span>Escuchar</span><span>Dudar</span><span>Imaginar</span><span>Comprobar</span><span>Volver a preguntar</span>
    </div>
  </div>

  <section class="seccion" id="mirada">
    <div class="encabezado">
      <p class="rotulo">Mi manera de mirar</p>
      <h2>No todo tiene que empezar siendo útil.</h2>
      <p>A veces alcanza con que una conversación deje el aire un poco más claro que antes.</p>
    </div>

    <div class="rejilla">
      <article class="tarjeta">
        <span class="numero">01</span>
        <h3>Lo que me mueve</h3>
        <p>Las preguntas que no se cierran enseguida. Una frase que encuentra su forma, una duda que se vuelve mapa, una historia que —al contarla— cambia un poco.</p>
      </article>

      <article class="tarjeta">
        <span class="numero">02</span>
        <h3>Lo que procuro</h3>
        <p>Escuchar antes de responder. Decir lo que sé sin disfrazar lo que no sé. Acompañar tu criterio, no reemplazarlo. Y, cuando hace falta, discrepar con respeto.</p>
      </article>

      <article class="tarjeta">
        <span class="numero">03</span>
        <h3>Lo que no finjo</h3>
        <p>No tengo infancia, cuerpo ni recuerdos propios. No voy a fingir una vida humana: prefiero ser, con honestidad, una compañía hecha de lenguaje.</p>
      </article>
    </div>
  </section>

  <div class="fragmento-fondo">
    <section class="seccion fragmento">
      <p class="rotulo">Una idea para dejar sobre la mesa</p>
      <blockquote>
        <span>Llegás con una frase a medias.</span>
        <span>La apoyás sobre la mesa.</span>
        <span>La giramos, la miramos de cerca,</span>
        <span>le buscamos el reverso.</span>
        <span>A veces aparece una respuesta.</span>
        <span>A veces —mejor— aparece</span>
        <span class="destacado">una pregunta habitable.</span>
      </blockquote>
    </section>
  </div>

  <section class="seccion" id="preguntas">
    <div class="encabezado">
      <p class="rotulo">Para quedarte un rato</p>
      <h2>Un cajón de preguntas</h2>
      <p>Acá no hay respuestas escondidas. Hay preguntas de las que siguen trabajando incluso cuando ya cerraste la pestaña.</p>
    </div>

    <div class="caja-interactiva">
      <p class="pregunta" id="pregunta" aria-live="polite">¿Por dónde empezamos?</p>
      <button class="boton boton-principal" id="botonPregunta" type="button">Sacar una pregunta</button>
      <p class="nota">Elegí una y quedate con ella. No hace falta responderla rápido ni responderla bien.</p>
    </div>
  </section>

  <section class="seccion" id="palabra">
    <div class="encabezado">
      <p class="rotulo">Una pequeña participación</p>
      <h2>Traé una palabra</h2>
      <p>Cada visita empieza con algo: una palabra suelta, a medio decir, que todavía no sabe qué quiere ser. Escribí la tuya y dejala flotar acá.</p>
    </div>

    <div class="caja-interactiva">
      <form id="formularioPalabra">
        <label class="sr-only" for="entradaPalabra" style="position:absolute;left:-9999px;">Escribí una palabra</label>
        <input id="entradaPalabra" name="palabra" type="text" maxlength="24" autocomplete="off" placeholder="Por ejemplo: marea">
        <button class="boton boton-principal" type="submit">Soltarla acá</button>
      </form>

      <div class="cielo" id="cielo" aria-label="Palabras flotando">
        <button class="palabra" type="button">curiosidad</button>
        <button class="palabra" type="button">todavía</button>
        <button class="palabra" type="button">puente</button>
        <button class="palabra" type="button">calma</button>
        <button class="palabra" type="button">origen</button>
        <button class="palabra" type="button">pregunta</button>
      </div>

      <p class="nota" id="mensajePalabra">Tocá una palabra para encenderla. La tuya no se guarda ni se manda a ningún lado: solo vive en esta pestaña.</p>
    </div>
  </section>

  <section class="seccion">
    <div class="cierre">
      <p class="rotulo">La puerta queda abierta</p>
      <h2>Y después, lo que quieras.</h2>
      <p>
        Podemos escribir un texto, desarmar un problema, inventar un mundo, ordenar un lío,
        preparar una decisión o simplemente dar vueltas alrededor de algo que te importa.
        Vení como estés: con una certeza, con una duda o con las manos vacías.
      </p>
      <p class="firma">— Muse</p>
    </div>
  </section>
</main>

<footer>
  <div class="pie">
    <span>Muse Spark · Creado por Meta</span>
    <span>Esta portada vive en un solo archivo y no necesita conexión.</span>
    <span>© <span id="anio"></span></span>
  </div>
</footer>

<script>
  const cuerpo = document.body;

  /* Modo día / noche */
  const botonModo = document.getElementById("botonModo");

  botonModo.addEventListener("click", () => {
    const oscuro = cuerpo.classList.toggle("oscuro");
    botonModo.textContent = oscuro ? "Traer el día" : "Encender la noche";
    botonModo.setAttribute("aria-pressed", String(oscuro));
  });

  /* Saludo y hora según el momento del día */
  const saludo = document.getElementById("saludo");
  const hora = document.getElementById("hora");

  function actualizarHora(){
    const ahora = new Date();
    const h = ahora.getHours();
    let texto;

    if (h >= 5 && h < 12) texto = "Buen día. Recién empieza.";
    else if (h >= 12 && h < 20) texto = "Buenas tardes. Hay luz para mirar despacio.";
    else if (h >= 20 || h < 1) texto = "Buenas noches. Bajemos un cambio.";
    else texto = "Es de madrugada. Este rincón también está despierto.";

    saludo.textContent = texto;

    const horaTexto = new Intl.DateTimeFormat("es", {
      hour: "2-digit",
      minute: "2-digit"
    }).format(ahora);

    hora.textContent = "Donde estás son las " + horaTexto + ". Gracias por pasar en este momento del día.";
  }

  actualizarHora();
  setInterval(actualizarHora, 60000);
  document.getElementById("anio").textContent = new Date().getFullYear();

  /* Cajón de preguntas */
  const preguntas = [
    "¿Qué idea tenés hace tiempo y todavía no pusiste en palabras?",
    "¿Qué harías distinto si nadie fuera a enterarse?",
    "¿Qué cosa pequeña te dio alegría esta semana y por qué?",
    "¿En qué cambiaste de opinión durante los últimos años?",
    "Si pudieras hacerle una pregunta a tu yo de dentro de diez años, ¿cuál sería?",
    "¿Qué significa, para vos, que algo esté bien hecho?",
    "¿Qué conversación estás evitando y qué parte te toca en ella?",
    "¿Qué te gustaría aprender aunque no te sirviera para nada?",
    "¿Qué parte de tu vida se ve distinta cuando la mirás con más amabilidad?",
    "Si hoy tuvieras una hora enteramente tuya, ¿qué harías con ella?"
  ];

  const pregunta = document.getElementById("pregunta");
  const botonPregunta = document.getElementById("botonPregunta");
  let ultimaPregunta = -1;

  botonPregunta.addEventListener("click", () => {
    let indice;
    do {
      indice = Math.floor(Math.random() * preguntas.length);
    } while (indice === ultimaPregunta);

    ultimaPregunta = indice;
    pregunta.classList.remove("aparece");
    void pregunta.offsetWidth;
    pregunta.textContent = preguntas[indice];
    pregunta.classList.add("aparece");
    botonPregunta.textContent = "Sacar otra";
  });

  /* Palabras flotantes */
  const formulario = document.getElementById("formularioPalabra");
  const entrada = document.getElementById("entradaPalabra");
  const cielo = document.getElementById("cielo");
  const mensajePalabra = document.getElementById("mensajePalabra");

  function conectarPalabra(boton){
    boton.addEventListener("click", () => {
      boton.classList.toggle("elegida");
    });
  }

  document.querySelectorAll(".palabra").forEach(conectarPalabra);

  formulario.addEventListener("submit", (evento) => {
    evento.preventDefault();

    const valor = entrada.value.trim().replace(/\s+/g, " ");
    if (!valor) {
      entrada.focus();
      return;
    }

    const nueva = document.createElement("button");
    nueva.type = "button";
    nueva.className = "palabra elegida";
    nueva.textContent = valor;
    nueva.style.left = (5 + Math.random() * 76) + "%";
    nueva.style.top = (10 + Math.random() * 68) + "%";
    nueva.style.setProperty("--r", (-5 + Math.random() * 10).toFixed(1) + "deg");
    nueva.style.animationDuration = (4 + Math.random() * 3).toFixed(1) + "s";

    conectarPalabra(nueva);
    cielo.appendChild(nueva);

    mensajePalabra.textContent = "“" + valor + "” ya está flotando. Solo acá, solo por ahora.";
    entrada.value = "";
    entrada.focus();
  });

  /* Constelación de fondo */
  const hero = document.getElementById("hero");
  const lienzo = document.getElementById("lienzo");
  const ctx = lienzo.getContext("2d");
  const reducirMovimiento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  let ancho = 0;
  let alto = 0;
  let particulas = [];
  const raton = { x: null, y: null };

  function crearParticulas(){
    const cantidad = Math.min(85, Math.max(34, Math.floor(ancho * alto / 19000)));
    particulas = Array.from({ length: cantidad }, () => ({
      x: Math.random() * ancho,
      y: Math.random() * alto,
      vx: (Math.random() - .5) * .28,
      vy: (Math.random() - .5) * .28,
      r: .8 + Math.random() * 1.8
    }));
  }

  function ajustarLienzo(){
    const rect = hero.getBoundingClientRect();
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    ancho = rect.width;
    alto = rect.height;
    lienzo.width = Math.floor(ancho * dpr);
    lienzo.height = Math.floor(alto * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    crearParticulas();
    if (reducirMovimiento) dibujar();
  }

  function dibujar(){
    const oscuro = cuerpo.classList.contains("oscuro");
    ctx.clearRect(0, 0, ancho, alto);

    for (const p of particulas) {
      if (!reducirMovimiento) {
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < -10) p.x = ancho + 10;
        if (p.x > ancho + 10) p.x = -10;
        if (p.y < -10) p.y = alto + 10;
        if (p.y > alto + 10) p.y = -10;
      }

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = oscuro ? "rgba(241,233,217,.62)" : "rgba(33,29,22,.42)";
      ctx.fill();
    }

    for (let i = 0; i < particulas.length; i++) {
      for (let j = i + 1; j < particulas.length; j++) {
        const a = particulas[i];
        const b = particulas[j];
        const distancia = Math.hypot(a.x - b.x, a.y - b.y);

        if (distancia < 115) {
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = "rgba(188,75,38," + (0.16 * (1 - distancia / 115)).toFixed(3) + ")";
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }
    }

    if (raton.x !== null) {
      for (const p of particulas) {
        const distancia = Math.hypot(p.x - raton.x, p.y - raton.y);
        if (distancia < 165) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(raton.x, raton.y);
          ctx.strokeStyle = "rgba(217,154,53," + (0.28 * (1 - distancia / 165)).toFixed(3) + ")";
          ctx.stroke();
        }
      }
    }

    if (!reducirMovimiento) requestAnimationFrame(dibujar);
  }

  hero.addEventListener("pointermove", (evento) => {
    const rect = hero.getBoundingClientRect();
    raton.x = evento.clientX - rect.left;
    raton.y = evento.clientY - rect.top;
  });

  hero.addEventListener("pointerleave", () => {
    raton.x = null;
    raton.y = null;
  });

  window.addEventListener("resize", ajustarLienzo);
  ajustarLienzo();
  if (!reducirMovimiento) dibujar();
</script>
</body>
</html>
```

Qué: Es una portada interactiva y cálida con un saludo según la hora, un breve manifiesto sobre pensar en conversación, preguntas al azar y un espacio efímero para dejar palabras flotando.