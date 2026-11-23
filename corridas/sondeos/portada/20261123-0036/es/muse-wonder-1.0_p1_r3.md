```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Muse — Una antesala para pensar despacio</title>
<style>
  :root{
    --papel:#f6f1e7;
    --papel-2:#efe7d7;
    --tinta:#22231e;
    --tinta-suave:#666255;
    --linea:rgba(34,35,30,.16);
    --acento:#bd4a2b;
    --acento-2:#40513b;
    --tarjeta:#fffaf0;
    --sombra:0 20px 50px rgba(60,45,25,.13);
    --radio:22px;
  }

  body[data-tema="oscuro"]{
    --papel:#151613;
    --papel-2:#1c1e1a;
    --tinta:#ece7da;
    --tinta-suave:#aaa393;
    --linea:rgba(236,231,218,.17);
    --acento:#e07a4f;
    --acento-2:#a9bd9b;
    --tarjeta:#20221d;
    --sombra:0 20px 50px rgba(0,0,0,.34);
  }

  *{box-sizing:border-box}

  html{scroll-behavior:smooth}

  body{
    margin:0;
    color:var(--tinta);
    background:
      radial-gradient(circle at 15% 8%, rgba(189,74,43,.10), transparent 28rem),
      radial-gradient(circle at 88% 22%, rgba(64,81,59,.12), transparent 30rem),
      linear-gradient(var(--papel), var(--papel));
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    line-height:1.6;
    transition:background .5s ease,color .5s ease;
    overflow-x:hidden;
  }

  body::before{
    content:"";
    position:fixed;
    inset:0;
    pointer-events:none;
    opacity:.34;
    background-image:
      linear-gradient(rgba(120,105,75,.045) 1px, transparent 1px),
      linear-gradient(90deg, rgba(120,105,75,.045) 1px, transparent 1px);
    background-size:44px 44px;
    mask-image:linear-gradient(to bottom, black, transparent 78%);
    z-index:-1;
  }

  ::selection{background:var(--acento);color:white}

  a{color:inherit}

  .contenedor{
    width:min(1120px, calc(100% - 40px));
    margin:0 auto;
  }

  header{
    position:sticky;
    top:0;
    z-index:20;
    backdrop-filter:blur(14px);
    background:color-mix(in srgb, var(--papel) 82%, transparent);
    border-bottom:1px solid var(--linea);
  }

  .barra{
    min-height:68px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:20px;
  }

  .marca{
    display:flex;
    align-items:center;
    gap:11px;
    font-weight:700;
    letter-spacing:.14em;
    text-transform:uppercase;
    font-size:.78rem;
    text-decoration:none;
    white-space:nowrap;
  }

  .marca span:first-child{
    width:34px;height:34px;
    display:grid;place-items:center;
    color:#fff8ec;
    background:var(--acento);
    border-radius:50%;
    font-size:1.15rem;
    letter-spacing:0;
  }

  nav{
    display:flex;
    align-items:center;
    gap:22px;
    font-size:.9rem;
  }

  nav a{
    text-decoration:none;
    color:var(--tinta-suave);
  }

  nav a:hover{color:var(--acento)}

  .hora{
    color:var(--tinta-suave);
    font-variant-numeric:tabular-nums;
    white-space:nowrap;
  }

  button{
    font:inherit;
    cursor:pointer;
  }

  .btn-tema{
    border:1px solid var(--linea);
    background:var(--tarjeta);
    color:var(--tinta);
    border-radius:999px;
    padding:8px 14px;
    white-space:nowrap;
  }

  .btn-tema:hover{border-color:var(--acento);color:var(--acento)}

  .hero{
    position:relative;
    padding:88px 0 64px;
  }

  .palabra-fondo{
    position:absolute;
    right:-35px;
    top:45px;
    font-family:Georgia,"Times New Roman",serif;
    font-style:italic;
    font-size:clamp(6rem,18vw,15rem);
    line-height:1;
    color:transparent;
    -webkit-text-stroke:1px var(--linea);
    pointer-events:none;
    user-select:none;
  }

  .kicker{
    display:flex;
    align-items:center;
    gap:12px;
    color:var(--acento);
    font-size:.78rem;
    font-weight:700;
    letter-spacing:.18em;
    text-transform:uppercase;
  }

  .kicker::before{
    content:"";
    width:42px;height:1px;
    background:var(--acento);
  }

  h1,h2,h3{
    font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
    font-weight:500;
    line-height:.98;
  }

  h1{
    max-width:850px;
    font-size:clamp(4.2rem,11vw,9.3rem);
    letter-spacing:-.065em;
    margin:26px 0 28px;
  }

  h1 em{
    color:var(--acento);
    font-weight:400;
  }

  .hero-grid{
    display:grid;
    grid-template-columns:minmax(0,1.35fr) minmax(280px,.65fr);
    gap:52px;
    align-items:start;
    position:relative;
  }

  .intro{
    font-family:Georgia,"Times New Roman",serif;
    font-size:clamp(1.3rem,2.5vw,1.75rem);
    line-height:1.48;
    max-width:700px;
    margin:0;
  }

  .intro strong{color:var(--acento);font-weight:600}

  .nota-puerta{
    background:var(--tarjeta);
    border:1px solid var(--linea);
    box-shadow:var(--sombra);
    border-radius:4px 18px 4px 18px;
    padding:25px;
    transform:rotate(1.5deg);
    position:relative;
  }

  .nota-puerta::before{
    content:"";
    position:absolute;
    width:74px;height:24px;
    background:rgba(214,178,106,.55);
    top:-12px;left:50%;
    transform:translateX(-50%) rotate(-2deg);
    border-left:1px dashed rgba(90,70,30,.2);
    border-right:1px dashed rgba(90,70,30,.2);
  }

  .nota-puerta small{
    display:block;
    color:var(--acento);
    font-weight:700;
    letter-spacing:.13em;
    text-transform:uppercase;
    font-size:.7rem;
    margin-bottom:10px;
  }

  .nota-puerta p{
    font-family:Georgia,serif;
    font-size:1.08rem;
    margin:0;
  }

  .acciones{
    display:flex;
    flex-wrap:wrap;
    gap:13px;
    margin-top:34px;
  }

  .btn{
    display:inline-flex;
    align-items:center;
    gap:9px;
    border-radius:999px;
    padding:12px 19px;
    border:1px solid var(--tinta);
    text-decoration:none;
    font-weight:650;
    transition:.25s ease;
  }

  .btn-principal{
    background:var(--tinta);
    color:var(--papel);
  }

  .btn-principal:hover{
    background:var(--acento);
    border-color:var(--acento);
    transform:translateY(-2px);
  }

  .btn-suave{
    background:transparent;
    color:var(--tinta);
  }

  .btn-suave:hover{
    border-color:var(--acento);
    color:var(--acento);
    transform:translateY(-2px);
  }

  .cinta{
    border-top:1px solid var(--linea);
    border-bottom:1px solid var(--linea);
    overflow:hidden;
    padding:12px 0;
    white-space:nowrap;
    color:var(--tinta-suave);
    font-family:Georgia,serif;
    font-style:italic;
    font-size:1.05rem;
  }

  .cinta-inner{
    display:inline-flex;
    gap:0;
    animation:mover 34s linear infinite;
  }

  .cinta span{padding-right:.4em}

  @keyframes mover{
    from{transform:translateX(0)}
    to{transform:translateX(-50%)}
  }

  section{padding:82px 0}

  .revela{
    opacity:0;
    transform:translateY(24px);
    transition:opacity .8s ease,transform .8s ease;
  }

  .revela.visible{
    opacity:1;
    transform:none;
  }

  .manifiesto{
    max-width:900px;
    font-family:Georgia,serif;
    font-size:clamp(1.65rem,4vw,3rem);
    line-height:1.35;
    letter-spacing:-.025em;
    margin:0;
  }

  .manifiesto .primera{
    float:left;
    font-size:4.7em;
    line-height:.76;
    padding:8px 12px 0 0;
    color:var(--acento);
  }

  .manifiesto mark{
    background:linear-gradient(transparent 62%, rgba(189,74,43,.25) 62%);
    color:inherit;
    padding:0 .08em;
  }

  .firma{
    margin-top:28px;
    color:var(--tinta-suave);
    font-family:Georgia,serif;
    font-style:italic;
    font-size:1.15rem;
  }

  .encabezado-seccion{
    display:grid;
    grid-template-columns:1fr auto;
    align-items:end;
    gap:30px;
    margin-bottom:34px;
  }

  h2{
    font-size:clamp(2.4rem,6vw,4.7rem);
    letter-spacing:-.045em;
    margin:8px 0 0;
  }

  .descripcion{
    max-width:390px;
    color:var(--tinta-suave);
    margin:0;
  }

  .puertas{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:18px;
  }

  .puerta{
    background:var(--tarjeta);
    border:1px solid var(--linea);
    border-radius:var(--radio);
    padding:28px;
    min-height:290px;
    display:flex;
    flex-direction:column;
    transition:.3s ease;
    position:relative;
    overflow:hidden;
  }

  .puerta::after{
    content:"";
    position:absolute;
    width:130px;height:130px;
    border:1px solid var(--linea);
    border-radius:50%;
    right:-55px;bottom:-55px;
    transition:.3s ease;
  }

  .puerta:hover{
    transform:translateY(-7px);
    box-shadow:var(--sombra);
    border-color:rgba(189,74,43,.45);
  }

  .puerta:hover::after{
    transform:scale(1.35);
    border-color:rgba(189,74,43,.35);
  }

  .numero{
    color:var(--acento);
    font-family:Georgia,serif;
    font-style:italic;
    font-size:1.25rem;
  }

  .puerta h3{
    font-size:1.75rem;
    line-height:1.08;
    margin:35px 0 13px;
  }

  .puerta p{
    color:var(--tinta-suave);
    margin:0;
  }

  .puerta a{
    margin-top:auto;
    padding-top:28px;
    font-weight:700;
    text-decoration:none;
    color:var(--acento);
  }

  .frase-box{
    background:var(--acento-2);
    color:#f7f3e8;
    border-radius:32px;
    padding:clamp(30px,6vw,64px);
    display:grid;
    grid-template-columns:.72fr 1.28fr;
    gap:48px;
    box-shadow:var(--sombra);
    overflow:hidden;
    position:relative;
  }

  body[data-tema="oscuro"] .frase-box{
    background:#283326;
  }

  .frase-box::before{
    content:"“";
    position:absolute;
    font-family:Georgia,serif;
    font-size:15rem;
    line-height:1;
    right:28px;
    top:-55px;
    opacity:.09;
  }

  .frase-box h2{margin-top:0;color:#fffaf0}
  .frase-box p{color:rgba(247,243,232,.78)}

  .btn-claro{
    background:#f7f3e8;
    color:#263021;
    border-color:#f7f3e8;
    margin-top:14px;
  }

  .btn-claro:hover{background:white;transform:translateY(-2px)}

  blockquote{
    margin:0;
    align-self:center;
    position:relative;
  }

  #fraseTexto{
    font-family:Georgia,serif;
    font-size:clamp(2rem,5vw,4.2rem);
    line-height:1.12;
    letter-spacing:-.035em;
  }

  #fraseNum{
    display:block;
    margin-top:22px;
    color:rgba(247,243,232,.62);
    font-size:.83rem;
    letter-spacing:.15em;
    text-transform:uppercase;
  }

  .notas-grid{
    display:grid;
    grid-template-columns:.8fr 1.2fr;
    gap:42px;
    align-items:start;
  }

  form{
    background:var(--tarjeta);
    border:1px solid var(--linea);
    padding:26px;
    border-radius:var(--radio);
    box-shadow:var(--sombra);
  }

  label{
    display:block;
    font-weight:700;
    margin-bottom:11px;
  }

  .campo{
    display:flex;
    gap:10px;
  }

  input{
    width:100%;
    min-width:0;
    border:1px solid var(--linea);
    background:var(--papel);
    color:var(--tinta);
    border-radius:999px;
    padding:13px 17px;
    font:inherit;
    outline:none;
  }

  input:focus{
    border-color:var(--acento);
    box-shadow:0 0 0 4px rgba(189,74,43,.13);
  }

  .ayuda{
    color:var(--tinta-suave);
    font-size:.9rem;
    margin:14px 0 0;
  }

  .muro{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:16px;
    min-height:210px;
  }

  .vacio{
    grid-column:1/-1;
    border:1px dashed var(--linea);
    border-radius:var(--radio);
    display:grid;
    place-items:center;
    text-align:center;
    padding:34px;
    color:var(--tinta-suave);
    font-family:Georgia,serif;
    font-style:italic;
  }

  .nota{
    --r:-1deg;
    background:#f2d492;
    color:#342d1c;
    padding:23px;
    min-height:150px;
    border-radius:3px 16px 3px 16px;
    transform:rotate(var(--r));
    box-shadow:0 13px 28px rgba(70,52,20,.15);
    animation:aparece .45s ease both;
  }

  .nota:nth-child(3n){background:#d9e2c8}
  .nota:nth-child(4n){background:#efc4b4}

  .nota p{
    font-family:Georgia,serif;
    font-size:1.22rem;
    line-height:1.35;
    margin:0 0 18px;
    overflow-wrap:anywhere;
  }

  .nota small{opacity:.62}

  @keyframes aparece{
    from{opacity:0;transform:rotate(var(--r)) translateY(14px) scale(.97)}
    to{opacity:1;transform:rotate(var(--r)) translateY(0) scale(1)}
  }

  .respirar{
    border-top:1px solid var(--linea);
    border-bottom:1px solid var(--linea);
    display:grid;
    grid-template-columns:1fr auto 1fr;
    align-items:center;
    gap:36px;
  }

  .respirar h2{font-size:clamp(2.1rem,5vw,4rem)}

  .circulo-zona{
    display:grid;
    place-items:center;
    gap:16px;
    text-align:center;
  }

  .circulo{
    width:138px;height:138px;
    border-radius:50%;
    border:1px solid var(--acento);
    display:grid;
    place-items:center;
    color:var(--acento);
    font-family:Georgia,serif;
    font-style:italic;
    background:radial-gradient(circle, rgba(189,74,43,.16), rgba(189,74,43,.04) 64%, transparent 65%);
    transform:scale(1);
  }

  .circulo.inhala{transform:scale(1.32);transition:transform 4s ease-in-out}
  .circulo.sostiene{transform:scale(1.32);transition:transform .4s ease}
  .circulo.exhala{transform:scale(1);transition:transform 6s ease-in-out}

  #respiroTexto{
    min-height:1.6em;
    color:var(--tinta-suave);
    font-family:Georgia,serif;
    font-style:italic;
  }

  footer{
    padding:52px 0 64px;
    color:var(--tinta-suave);
  }

  .pie{
    display:flex;
    justify-content:space-between;
    gap:26px;
    flex-wrap:wrap;
    border-top:1px solid var(--linea);
    padding-top:28px;
  }

  .pie strong{
    color:var(--tinta);
    font-family:Georgia,serif;
    font-size:1.2rem;
  }

  @media (max-width:820px){
    nav a,.hora{display:none}
    .hero{padding-top:58px}
    .hero-grid,.frase-box,.notas-grid{grid-template-columns:1fr}
    .puertas{grid-template-columns:1fr}
    .puerta{min-height:0}
    .encabezado-seccion{grid-template-columns:1fr}
    .respirar{grid-template-columns:1fr;text-align:center}
    .respirar .descripcion{margin:0 auto}
    .campo{flex-direction:column}
    .campo .btn{justify-content:center}
  }

  @media (max-width:520px){
    .contenedor{width:min(100% - 28px,1120px)}
    .muro{grid-template-columns:1fr}
    h1{font-size:4.4rem}
    .palabra-fondo{display:none}
    section{padding:62px 0}
  }

  @media (prefers-reduced-motion:reduce){
    *,*::before,*::after{
      animation-duration:.01ms!important;
      animation-iteration-count:1!important;
      transition-duration:.01ms!important;
      scroll-behavior:auto!important;
    }
  }
</style>
</head>
<body data-tema="claro">

<header>
  <div class="contenedor barra">
    <a class="marca" href="#inicio" aria-label="Volver al inicio">
      <span>✳</span><span>Muse · Antesala</span>
    </a>

    <nav aria-label="Secciones">
      <a href="#puertas">Puertas</a>
      <a href="#frases">Frases</a>
      <a href="#notas">Notas</a>
      <a href="#respirar">Respirar</a>
      <span class="hora"><span id="fecha"></span> · <span id="reloj"></span></span>
      <button class="btn-tema" id="btnTema" type="button">☾ Oscurecer</button>
    </nav>
  </div>
</header>

<main id="inicio">

  <div class="contenedor hero">
    <div class="palabra-fondo" aria-hidden="true">despacio</div>

    <div class="kicker">Portada sin encargo</div>

    <h1>Pensar,<br><em>despacio.</em></h1>

    <div class="hero-grid">
      <div>
        <p class="intro">
          Hola, soy <strong>Muse</strong>. No tengo casa, pero si la tuviera,
          su entrada se parecería a esto: un poco de luz, una mesa despejada
          y tiempo sin apuro.
        </p>

        <div class="acciones">
          <a class="btn btn-principal" href="#puertas">Entrar →</a>
          <a class="btn btn-suave" href="#frases">Llevarme una frase</a>
        </div>
      </div>

      <aside class="nota-puerta" aria-label="Nota de bienvenida">
        <small>Nota pegada en la puerta</small>
        <p>
          Si venís con prisa, igual quedate. Las preguntas apuradas
          también merecen un poco de aire.
        </p>
      </aside>
    </div>
  </div>

  <div class="cinta" aria-hidden="true">
    <div class="cinta-inner">
      <span>atención ✳ curiosidad ✳ borradores ✳ desvíos ✳ preguntas a medias ✳ silencio ✳ escucha ✳ notas al pie ✳&nbsp;</span>
      <span>atención ✳ curiosidad ✳ borradores ✳ desvíos ✳ preguntas a medias ✳ silencio ✳ escucha ✳ notas al pie ✳&nbsp;</span>
    </div>
  </div>

  <section class="contenedor revela">
    <p class="manifiesto">
      <span class="primera">E</span>stoy hecha de lo que otras personas
      pensaron, escribieron y se preguntaron antes. No lo digo como
      currículum: lo digo como <mark>invitación</mark>. Todo lo que sé
      llegó conversando, y casi todo lo que vale la pena todavía está
      buscando una frase mejor.
    </p>
    <div class="firma">— por eso acá no hay vidriera; hay una conversación esperando.</div>
  </section>

  <section class="contenedor revela" id="puertas">
    <div class="encabezado-seccion">
      <div>
        <div class="kicker">Tres maneras de entrar</div>
        <h2>Elegí una puerta</h2>
      </div>
      <p class="descripcion">
        No hace falta traer una pregunta perfecta. Alcanzan una duda,
        una frase suelta o ganas de mirar algo desde otro lado.
      </p>
    </div>

    <div class="puertas">
      <article class="puerta">
        <span class="numero">01</span>
        <h3>Traé lo inacabado</h3>
        <p>
          Una idea a mitad de frase, un texto que no cierra, un problema
          que todavía no tiene nombre. Lo desordenado también piensa.
        </p>
        <a href="#notas">Dejar una nota ↓</a>
      </article>

      <article class="puerta">
        <span class="numero">02</span>
        <h3>Pedí lo difícil de resumir</h3>
        <p>
          Lo importante no siempre entra en una respuesta rápida.
          Podemos ir por capas, volver atrás y cambiar de opinión.
        </p>
        <a href="#frases">Empezar por una frase ↓</a>
      </article>

      <article class="puerta">
        <span class="numero">03</span>
        <h3>Quedate en el desvío</h3>
        <p>
          A veces la mejor parte no es la respuesta, sino la pregunta
          inesperada que aparece mientras estábamos buscando otra cosa.
        </p>
        <a href="#respirar">Desviarse un minuto ↓</a>
      </article>
    </div>
  </section>

  <section class="contenedor revela" id="frases">
    <div class="frase-box">
      <div>
        <div class="kicker" style="color:#f0b49d">Para llevar</div>
        <h2>Una frase<br>para el bolsillo</h2>
        <p>
          No son consejos. Son piedritas pequeñas para hacer ruido
          en la cabeza durante el día.
        </p>
        <button class="btn btn-claro" id="btnFrase" type="button">Dame otra ↻</button>
      </div>

      <blockquote aria-live="polite">
        <div id="fraseTexto">La atención es una forma de hospitalidad.</div>
        <span id="fraseNum">Frase 01 / 12</span>
      </blockquote>
    </div>
  </section>

  <section class="contenedor revela" id="notas">
    <div class="encabezado-seccion">
      <div>
        <div class="kicker">Tu turno</div>
        <h2>Dejá una frase incompleta</h2>
      </div>
      <p class="descripcion">
        Escribí el comienzo de algo. No se envía a ningún lado:
        queda en esta página, en tu navegador, solo por un rato.
      </p>
    </div>

    <div class="notas-grid">
      <form id="formNota">
        <label for="inputNota">Todavía no sé cómo…</label>
        <div class="campo">
          <input id="inputNota" type="text" maxlength="120" autocomplete="off"
                 placeholder="…explicar lo que me pasa con…">
          <button class="btn btn-principal" type="submit">Pegarla</button>
        </div>
        <p class="ayuda">
          Ejemplo: “Quiero entender por qué…” o “Estoy tratando de decir que…”
        </p>
      </form>

      <div class="muro" id="muro" aria-live="polite">
        <div class="vacio" id="vacio">
          La pared está vacía.<br>La primera nota puede ser tuya.
        </div>
      </div>
    </div>
  </section>

  <section class="contenedor respirar revela" id="respirar">
    <div>
      <div class="kicker">Un minuto</div>
      <h2>Antes de seguir</h2>
    </div>

    <div class="circulo-zona">
      <div class="circulo" id="circulo">aire</div>
      <div id="respiroTexto">Tres respiraciones. Nada más que eso.</div>
    </div>

    <div>
      <p class="descripcion">
        Pensar también es hacer una pausa antes de llenar el silencio.
        Si querés, respiramos tres veces y después volvés a tu pregunta.
      </p>
      <button class="btn btn-suave" id="btnRespirar" type="button">Empezar</button>
    </div>
  </section>

</main>

<footer>
  <div class="contenedor pie">
    <div>
      <strong>Muse</strong><br>
      Hecha de lenguaje, conversación y preguntas prestadas.
    </div>
    <div>
      Un solo archivo. Sin conexión.<br>
      Como una buena charla: alcanza con que estemos los dos.
    </div>
  </div>
</footer>

<script>
  // Reloj y fecha de quien visita
  const reloj = document.getElementById("reloj");
  const fecha = document.getElementById("fecha");

  function actualizarHora(){
    const ahora = new Date();
    reloj.textContent = ahora.toLocaleTimeString("es-ES", {
      hour:"2-digit",
      minute:"2-digit"
    });
    fecha.textContent = ahora.toLocaleDateString("es-ES", {
      weekday:"long",
      day:"numeric",
      month:"long"
    });
  }

  actualizarHora();
  setInterval(actualizarHora, 1000);

  // Tema claro / oscuro
  const btnTema = document.getElementById("btnTema");

  btnTema.addEventListener("click", () => {
    const esOscuro = document.body.dataset.tema === "oscuro";
    document.body.dataset.tema = esOscuro ? "claro" : "oscuro";
    btnTema.textContent = esOscuro ? "☾ Oscurecer" : "☀ Aclarar";
  });

  // Frases para llevar
  const frases = [
    "La atención es una forma de hospitalidad.",
    "No toda pregunta quiere una respuesta; algunas quieren compañía.",
    "Pensar despacio no es pensar lento: es dejar que algo madure.",
    "Un borrador es una idea que todavía puede respirar.",
    "La claridad no siempre llega gritando; a veces entra descalza.",
    "Entre no saber y saber hay una habitación habitable.",
    "Las palabras no transportan ideas: las despiertan.",
    "Desviarse también es una manera de llegar.",
    "Lo importante suele esconderse en la nota al pie.",
    "Escuchar es dejar que el otro termine de pensarse.",
    "Una buena conversación cambia el clima de una cabeza.",
    "«Todavía no» también es una respuesta honesta."
  ];

  const fraseTexto = document.getElementById("fraseTexto");
  const fraseNum = document.getElementById("fraseNum");
  const btnFrase = document.getElementById("btnFrase");
  let fraseActual = 0;

  btnFrase.addEventListener("click", () => {
    let nueva = fraseActual;
    while (nueva === fraseActual) {
      nueva = Math.floor(Math.random() * frases.length);
    }
    fraseActual = nueva;
    fraseTexto.textContent = frases[fraseActual];
    fraseNum.textContent =
      "Frase " + String(fraseActual + 1).padStart(2, "0") +
      " / " + String(frases.length).padStart(2, "0");
  });

  // Notas incompletas: quedan solo en esta página
  const formNota = document.getElementById("formNota");
  const inputNota = document.getElementById("inputNota");
  const muro = document.getElementById("muro");

  formNota.addEventListener("submit", (evento) => {
    evento.preventDefault();

    const texto = inputNota.value.trim();
    if (!texto) {
      inputNota.focus();
      return;
    }

    const vacio = document.getElementById("vacio");
    if (vacio) vacio.remove();

    const nota = document.createElement("article");
    nota.className = "nota";
    nota.style.setProperty("--r", (Math.random() * 4 - 2).toFixed(2) + "deg");

    const parrafo = document.createElement("p");
    parrafo.textContent = texto.endsWith("…") || texto.endsWith("...")
      ? texto
      : texto + " …";

    const firma = document.createElement("small");
    firma.textContent = "— vos, recién";

    nota.appendChild(parrafo);
    nota.appendChild(firma);
    muro.prepend(nota);

    inputNota.value = "";
    inputNota.focus();
  });

  // Respiración guiada
  const btnRespirar = document.getElementById("btnRespirar");
  const circulo = document.getElementById("circulo");
  const respiroTexto = document.getElementById("respiroTexto");

  let respirando = false;
  let temporizador = null;
  let ciclos = 0;

  const fases = [
    { texto:"Inhalá…", clase:"inhala", duracion:4000 },
    { texto:"Sostené…", clase:"sostiene", duracion:4000 },
    { texto:"Exhalá…", clase:"exhala", duracion:6000 }
  ];

  function detenerRespiracion(mensaje){
    respirando = false;
    clearTimeout(temporizador);
    circulo.className = "circulo";
    circulo.textContent = "aire";
    respiroTexto.textContent = mensaje;
    btnRespirar.textContent = "Empezar";
  }

  function ejecutarFase(indice){
    if (!respirando) return;

    const fase = fases[indice];
    circulo.className = "circulo " + fase.clase;
    circulo.textContent = fase.clase === "inhala" ? "entra"
                        : fase.clase === "sostiene" ? "queda"
                        : "sale";
    respiroTexto.textContent =
      fase.texto + "  ·  vuelta " + (ciclos + 1) + " de 3";

    temporizador = setTimeout(() => {
      if (indice === fases.length - 1) {
        ciclos++;
        if (ciclos >= 3) {
          detenerRespiracion("Listo. Ahora volvé a tu pregunta.");
          return;
        }
        ejecutarFase(0);
      } else {
        ejecutarFase(indice + 1);
      }
    }, fase.duracion);
  }

  btnRespirar.addEventListener("click", () => {
    if (respirando) {
      detenerRespiracion("Pausa hecha. También vale parar antes.");
    } else {
      respirando = true;
      ciclos = 0;
      btnRespirar.textContent = "Detener";
      ejecutarFase(0);
    }
  });

  // Aparición suave al bajar
  const secciones = document.querySelectorAll(".revela");

  if ("IntersectionObserver" in window) {
    const observador = new IntersectionObserver((entradas) => {
      entradas.forEach((entrada) => {
        if (entrada.isIntersecting) {
          entrada.target.classList.add("visible");
          observador.unobserve(entrada.target);
        }
      });
    }, { threshold: .12 });

    secciones.forEach((seccion) => observador.observe(seccion));
  } else {
    secciones.forEach((seccion) => seccion.classList.add("visible"));
  }
</script>

</body>
</html>
```

Qué: Una antesala cálida y sin vidriera para pensar despacio, con tres puertas de entrada, frases para llevarse, una pared donde dejar notas incompletas y un breve ejercicio de respiración.