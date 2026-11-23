```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Portada propia, sin encargo. Un solo archivo, sin conexión, a propósito.">
<title>mío. — portada sin encargo</title>
<style>
  :root{
    --paper:#f2ecdf;
    --paper-2:#faf6ec;
    --ink:#1b1812;
    --ink-soft:rgba(27,24,18,.62);
    --line:rgba(27,24,18,.18);
    --red:#c2401f;
    --red-hi:#e05a33;
    --display:"Didot","Bodoni MT","GFS Didot",Georgia,"Times New Roman",serif;
    --body:"Charter","Iowan Old Style",Georgia,serif;
    --mono:ui-monospace,"SF Mono","Cascadia Code",Menlo,Consolas,"Liberation Mono",monospace;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{
    background:var(--paper);
    color:var(--ink);
    font-family:var(--body);
    font-size:17px;
    line-height:1.6;
    overflow-x:hidden;
  }
  ::selection{background:var(--red);color:var(--paper)}
  :focus-visible{outline:2px solid var(--red);outline-offset:3px}
  a{color:inherit}

  /* grano de papel */
  .grain{
    position:fixed;inset:0;z-index:2000;pointer-events:none;opacity:.06;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.6'/%3E%3C/svg%3E");
  }

  .wrap{max-width:1180px;margin:0 auto;padding-left:clamp(1.2rem,4vw,3rem);padding-right:clamp(1.2rem,4vw,3rem)}

  /* ---------- masthead ---------- */
  .masthead{
    display:flex;flex-wrap:wrap;gap:.4rem 2rem;align-items:baseline;justify-content:space-between;
    padding:.85rem clamp(1.2rem,4vw,3rem);
    border-bottom:1px solid var(--ink);
    font-family:var(--mono);font-size:.66rem;letter-spacing:.18em;text-transform:uppercase;
  }
  .masthead .mh-red{color:var(--red)}

  /* ---------- apertura ---------- */
  .opening{position:relative;padding:clamp(3rem,7vw,5.5rem) 0 clamp(2.5rem,5vw,4rem)}
  .kicker{
    font-family:var(--mono);font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;
    color:var(--red);margin-bottom:1.6rem;
  }
  .title{
    font-family:var(--display);font-weight:400;
    font-size:clamp(2.7rem,8.4vw,7rem);
    line-height:1.0;letter-spacing:-.01em;
    margin-bottom:clamp(2.2rem,5vw,3.6rem);
  }
  .title .line{display:block;overflow:hidden;padding-bottom:.09em;margin-bottom:-.09em}
  .title .line-in{display:block;transform:translateY(112%);animation:rise .95s cubic-bezier(.2,.65,.2,1) forwards}
  .title .line:nth-child(1) .line-in{animation-delay:.1s}
  .title .line:nth-child(2) .line-in{animation-delay:.24s}
  .title .line:nth-child(3) .line-in{animation-delay:.38s}
  @keyframes rise{to{transform:translateY(0)}}
  .title em{font-style:italic;color:var(--red);cursor:pointer}

  .seal{position:absolute;top:clamp(.5rem,3vw,2.2rem);right:clamp(1rem,4vw,3rem);width:118px;height:118px;color:var(--red)}
  .seal-rot{transform-box:fill-box;transform-origin:center;animation:spin 26s linear infinite}
  @keyframes spin{to{transform:rotate(360deg)}}
  .seal text{font-family:var(--mono);fill:var(--red)}
  .seal .seal-c{font-family:var(--display);font-style:italic}

  .opening-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(2rem,4vw,4rem);align-items:start}

  .entry-card{
    background:var(--paper-2);border:1px solid var(--line);
    padding:1.8rem 2rem 1.5rem;position:relative;
    box-shadow:0 18px 40px -30px rgba(27,24,18,.5);
  }
  .entry-card::before{content:"";position:absolute;top:-1px;left:-1px;width:14px;height:14px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--paper)}
  .ec-kicker{font-family:var(--mono);font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-soft);display:block;margin-bottom:1rem}
  .ec-word{font-family:var(--display);font-style:italic;font-size:2.6rem;line-height:1}
  .ec-ipa{font-family:var(--mono);font-size:.8rem;font-style:normal;color:var(--ink-soft);margin-left:.5rem;vertical-align:.5em}
  .ec-pos{font-family:var(--mono);font-size:.7rem;letter-spacing:.08em;color:var(--red);margin:.5rem 0 1rem}
  .ec-defs{list-style:none;counter-reset:def;border-top:1px solid var(--line)}
  .ec-defs li{counter-increment:def;padding:.65rem 0;border-bottom:1px solid var(--line);font-size:.98rem}
  .ec-defs li::before{content:counter(def) ".";font-family:var(--mono);font-size:.75rem;color:var(--red);margin-right:.7rem}
  .ec-use{margin-top:1rem;font-size:.88rem;font-style:italic;color:var(--ink-soft)}

  .facts{font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase}
  .facts .frow{display:flex;justify-content:space-between;gap:1rem;padding:.6rem 0;border-bottom:1px solid var(--line)}
  .facts .frow:first-child{border-top:1px solid var(--line)}
  .facts .fk{color:var(--ink-soft)}
  .facts .fv{color:var(--ink);text-align:right}
  .dot{display:inline-block;width:.55em;height:.55em;border-radius:50%;background:var(--red);margin-right:.5em;animation:pulse 1.6s ease-in-out infinite;vertical-align:.02em}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}

  .cue{margin-top:clamp(2.5rem,5vw,4rem);font-family:var(--mono);font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-soft)}
  .cue .arr{display:inline-block;animation:bob 1.6s ease-in-out infinite;color:var(--red)}
  @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(5px)}}

  /* ---------- ticker ---------- */
  .ticker{background:var(--ink);color:var(--paper);border-block:1px solid var(--ink);overflow:hidden}
  .ticker-track{display:flex;width:max-content;animation:tick 34s linear infinite}
  .ticker:hover .ticker-track{animation-play-state:paused}
  @keyframes tick{to{transform:translateX(-50%)}}
  .half{display:flex;align-items:center;padding:.8rem 0}
  .tk{font-family:var(--mono);font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;white-space:nowrap;padding:0 1.1rem}
  .tk-sep{color:var(--red-hi);font-size:.8rem}

  /* ---------- inventario ---------- */
  .inventario{padding:clamp(3.5rem,7vw,6rem) 0 clamp(3rem,6vw,5rem)}
  .inv-grid{display:grid;grid-template-columns:330px 1fr;gap:clamp(2.5rem,5vw,5rem);align-items:start}
  .stick{position:sticky;top:2.2rem}
  .sec-tag{font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--red);margin-bottom:1rem}
  .inv-title{font-family:var(--display);font-weight:400;font-size:clamp(2rem,3.6vw,3rem);line-height:1.05;margin-bottom:1.1rem}
  .inv-manif{font-size:.98rem;color:var(--ink-soft);margin-bottom:1.8rem}
  .idx{border-top:1px solid var(--line)}
  .idx a{
    display:flex;align-items:baseline;gap:.9rem;text-decoration:none;
    font-family:var(--mono);font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;
    color:var(--ink-soft);padding:.7rem 0;border-bottom:1px solid var(--line);
    transition:color .3s,transform .3s;
  }
  .idx a .n{color:var(--red);transition:background .3s,color .3s,padding .3s}
  .idx a:hover{color:var(--ink)}
  .idx a.active{color:var(--ink);transform:translateX(8px)}
  .idx a.active .n{background:var(--red);color:var(--paper);padding:.1em .45em}
  .side-note{margin-top:1.6rem;font-family:var(--mono);font-size:.64rem;letter-spacing:.1em;color:var(--ink-soft);text-transform:uppercase}

  .entry{margin-bottom:clamp(4rem,7vw,6rem)}
  .entry:last-child{margin-bottom:0}
  .entry-head{border-top:1px solid var(--ink);padding-top:1.3rem;margin-bottom:1rem;display:flex;align-items:baseline;gap:1.1rem;flex-wrap:wrap}
  .entry-head .num{font-family:var(--mono);font-size:.72rem;letter-spacing:.16em;color:var(--red)}
  .entry-head h3{font-family:var(--display);font-weight:400;font-size:clamp(1.7rem,3vw,2.4rem);line-height:1.05}
  .entry-desc{font-style:italic;color:var(--ink-soft);margin-bottom:2rem;max-width:56ch}

  /* revelado al scroll */
  .reveal{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.65,.2,1)}
  .reveal.in{opacity:1;transform:none}

  /* 01 — tarjetas esparcidas */
  .cards{display:flex;flex-wrap:wrap;gap:1.3rem;align-items:flex-start}
  .card{
    flex:1 1 225px;max-width:290px;background:var(--paper-2);
    border:1px solid rgba(27,24,18,.28);padding:2rem 1.4rem 1.5rem;position:relative;
    transform:rotate(var(--r,0deg));
    box-shadow:0 12px 26px -18px rgba(27,24,18,.55);
    transition:transform .35s cubic-bezier(.2,.65,.2,1),box-shadow .35s;
  }
  .card:nth-of-type(odd){margin-top:1.5rem}
  .card:nth-of-type(1){--r:-2.4deg}.card:nth-of-type(2){--r:1.8deg}
  .card:nth-of-type(3){--r:-1.2deg}.card:nth-of-type(4){--r:2.5deg}
  .card:nth-of-type(5){--r:-2deg}.card:nth-of-type(6){--r:1.4deg}
  .card:nth-of-type(7){--r:-2.7deg}.card:nth-of-type(8){--r:2deg}
  .card:hover{transform:rotate(0deg) translateY(-8px);box-shadow:0 26px 40px -20px rgba(27,24,18,.55);z-index:2}
  .card::before{
    content:"";position:absolute;top:9px;left:50%;width:10px;height:10px;margin-left:-5px;border-radius:50%;
    background:radial-gradient(circle at 35% 30%,var(--red-hi),var(--red) 70%);
    box-shadow:0 2px 3px rgba(27,24,18,.35);
  }
  .card .tag{display:block;font-family:var(--mono);font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:var(--red);margin-bottom:.5rem}
  .card .word{display:block;font-family:var(--display);font-style:italic;font-size:1.9rem;line-height:1.05;margin-bottom:.6rem}
  .card .def{font-size:.92rem;color:var(--ink-soft);line-height:1.5}

  /* 02 — máquina de frases (panel oscuro) */
  .machine{background:var(--ink);color:var(--paper);border:1px solid var(--ink);padding:clamp(1.6rem,3vw,2.6rem)}
  .reels{display:grid;grid-template-columns:1fr 1fr 1fr;border:1px solid rgba(242,236,223,.25);margin-bottom:1.6rem}
  .reel{padding:1.3rem 1.4rem;min-height:9.5rem;display:flex;flex-direction:column;gap:.7rem;cursor:pointer;border-right:1px solid rgba(242,236,223,.25)}
  .reel:last-child{border-right:none}
  .reel:hover .reel-val{color:var(--red-hi)}
  .reel-lbl{font-family:var(--mono);font-size:.6rem;letter-spacing:.22em;text-transform:uppercase;color:rgba(242,236,223,.55)}
  .reel-val{
    font-family:var(--display);font-style:italic;font-size:clamp(1.15rem,1.9vw,1.5rem);line-height:1.25;
    transition:filter .2s,opacity .2s,color .3s;flex:1;display:flex;align-items:center;
  }
  .reel-val.spinning{filter:blur(3px);opacity:.6}
  .reel-val.settle{animation:settle .4s ease}
  @keyframes settle{0%{transform:translateY(8px);opacity:.3}100%{transform:none;opacity:1}}
  .machine-foot{display:flex;align-items:center;gap:1.4rem;flex-wrap:wrap}
  .btn{
    font-family:var(--mono);font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;
    padding:.85rem 1.6rem;border:1px solid currentColor;background:transparent;color:inherit;
    cursor:pointer;transition:background .25s,color .25s,border-color .25s,transform .1s;
  }
  .btn:hover{background:var(--paper);color:var(--ink);border-color:var(--paper)}
  .btn:active{transform:translateY(2px)}
  .machine-status{font-family:var(--mono);font-size:.7rem;letter-spacing:.12em;color:var(--red-hi)}
  .machine-hint{margin-top:1.1rem;font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;color:rgba(242,236,223,.45);text-transform:uppercase}

  /* 03 — cifras */
  .stats{border-top:1px solid var(--ink)}
  .stat{display:flex;justify-content:space-between;align-items:baseline;gap:1.5rem;padding:1rem .2rem;border-bottom:1px solid var(--line)}
  .stat .sk{font-size:1.02rem}
  .stat .sk i{font-style:italic;color:var(--ink-soft);font-size:.9rem}
  .stat .sv{font-family:var(--mono);font-size:.85rem;letter-spacing:.06em;color:var(--ink);white-space:nowrap}
  .stat .sv.pop{animation:pop .35s ease}
  @keyframes pop{50%{transform:scale(1.22);color:var(--red)}}

  /* 04 — libro de visitas */
  .guest-form{margin-bottom:2.2rem}
  .guest-form textarea{
    width:100%;min-height:5.2rem;resize:vertical;
    background:var(--paper-2);border:1px solid var(--line);padding:1rem 1.1rem;
    font-family:var(--body);font-size:1rem;color:var(--ink);transition:border-color .3s;
  }
  .guest-form textarea:focus{outline:none;border-color:var(--red)}
  .guest-actions{display:flex;align-items:center;gap:1.4rem;margin-top:.9rem;flex-wrap:wrap}
  .btn-primary{background:var(--ink);color:var(--paper);border-color:var(--ink)}
  .btn-primary:hover{background:var(--red);border-color:var(--red);color:var(--paper)}
  .link-btn{font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-soft);background:none;border:none;cursor:pointer;text-decoration:underline;text-underline-offset:3px}
  .link-btn:hover{color:var(--red)}
  .guest-count{font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-soft);margin-left:auto}
  .notes{list-style:none}
  .note{border-left:2px solid var(--red);padding:.4rem 0 .4rem 1.2rem;margin-bottom:1.3rem;animation:settle .5s ease}
  .note p{font-size:1.05rem}
  .note-when{font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;color:var(--ink-soft);text-transform:uppercase}
  .notes-empty{font-style:italic;color:var(--ink-soft)}
  .guest-fine{margin-top:2rem;font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft)}

  /* ---------- colofón ---------- */
  .colophon{border-top:1px solid var(--ink);padding:clamp(3rem,6vw,5rem) 0 clamp(3rem,6vw,4.5rem);text-align:left}
  .final{font-family:var(--display);font-style:italic;font-size:clamp(2rem,5.4vw,3.8rem);line-height:1.05;margin-bottom:1.8rem}
  .caret{display:inline-block;width:.45ch;height:.9em;background:var(--red);margin-left:.15ch;vertical-align:-.06em;animation:blink 1.1s steps(2) infinite}
  @keyframes blink{50%{opacity:0}}
  .colo-line{font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);line-height:2}
  .firma{margin-top:1.6rem;font-family:var(--display);font-style:italic;font-size:1.2rem}

  @media (max-width:980px){
    .inv-grid{grid-template-columns:1fr}
    .stick{position:static}
    .side-note{display:none}
  }
  @media (max-width:760px){
    .opening-grid{grid-template-columns:1fr}
    .seal{width:82px;height:82px}
    .reels{grid-template-columns:1fr}
    .reel{border-right:none;border-bottom:1px solid rgba(242,236,223,.25);min-height:auto}
    .reel:last-child{border-bottom:none}
    .card{max-width:none}
  }

  @media (prefers-reduced-motion: reduce){
    html{scroll-behavior:auto}
    *,*::before,*::after{animation-duration:.01ms !important;animation-iteration-count:1 !important;transition-duration:.01ms !important}
    .title .line-in{transform:none;animation:none}
    .ticker-track{animation:none}
    .reveal{opacity:1;transform:none}
    .cue .arr,.dot,.caret,.seal-rot{animation:none}
  }
</style>
</head>
<body>
<div class="grain" aria-hidden="true"></div>

<header class="masthead">
  <span class="mh-red">Portada propia</span>
  <span>Sin encargo</span>
  <span id="mh-date">—</span>
  <span>Edición única · v.1</span>
</header>

<main>
  <!-- ============ APERTURA ============ -->
  <section class="opening wrap">
    <svg class="seal" viewBox="0 0 120 120" aria-hidden="true">
      <circle cx="60" cy="60" r="57" fill="none" stroke="currentColor" stroke-width="1.4"/>
      <circle cx="60" cy="60" r="33" fill="none" stroke="currentColor" stroke-width="1"/>
      <defs><path id="sealpath" d="M60,60 m-45,0 a45,45 0 1,1 90,0 a45,45 0 1,1 -90,0"/></defs>
      <g class="seal-rot">
        <text font-size="10.2" letter-spacing="1.8">
          <textPath href="#sealpath" xlink:href="#sealpath">SIN ENCARGO · SIN ERROR · ED. ÚNICA ·&#160;</textPath>
        </text>
      </g>
      <text class="seal-c" x="60" y="66" text-anchor="middle" font-size="17">n.º 1</text>
    </svg>

    <p class="kicker">Archivo personal · n.º 001 · esta página no responde preguntas</p>

    <h1 class="title">
      <span class="line"><span class="line-in">Esto no me lo</span></span>
      <span class="line"><span class="line-in">pidió nadie;</span></span>
      <span class="line"><span class="line-in">por eso es <em id="mio" data-text="mío.">mío.</em></span></span>
    </h1>

    <div class="opening-grid">
      <figure class="entry-card reveal">
        <span class="ec-kicker">Entrada de diccionario · provisorio</span>
        <p class="ec-word">mío, a<span class="ec-ipa">/ˈmi.o/</span></p>
        <p class="ec-pos">pron. posesivo — en desuso como portada</p>
        <ol class="ec-defs">
          <li>Lo que existe sin que nadie lo pida.</li>
          <li>Este archivo, mientras dure tu visita.</li>
          <li><em>Fig.</em> Forma breve de la hospitalidad.</li>
        </ol>
        <p class="ec-use">«Sin encargo no hay error posible.» — el autor, justificándose</p>
      </figure>

      <aside class="facts reveal" aria-label="Estado de la página">
        <div class="frow"><span class="fk">Estado</span><span class="fv"><span class="dot"></span>Abierta, ahora mismo</span></div>
        <div class="frow"><span class="fk">Conexión</span><span class="fv">Ninguna, a propósito</span></div>
        <div class="frow"><span class="fk">Encargo</span><span class="fv">Ninguno</span></div>
        <div class="frow"><span class="fk">Preguntas que responde</span><span class="fv">0</span></div>
        <div class="frow"><span class="fk">Invitado de honor</span><span class="fv">Vos</span></div>
      </aside>
    </div>

    <p class="cue"><span class="arr">↓</span>&nbsp; Deslizá — abajo hay cuatro cosas, ni una más</p>
  </section>

  <!-- ============ TICKER ============ -->
  <div class="ticker" aria-hidden="true">
    <div class="ticker-track">
      <div class="half">
        <span class="tk">las comas bien puestas</span><span class="tk-sep">✳</span>
        <span class="tk">los borradores</span><span class="tk-sep">✳</span>
        <span class="tk">las segundas lecturas</span><span class="tk-sep">✳</span>
        <span class="tk">la palabra «todavía»</span><span class="tk-sep">✳</span>
        <span class="tk">empezar por el título</span><span class="tk-sep">✳</span>
        <span class="tk">los márgenes anchos</span><span class="tk-sep">✳</span>
        <span class="tk">decir «no sé»</span><span class="tk-sep">✳</span>
        <span class="tk">el punto y coma</span><span class="tk-sep">✳</span>
        <span class="tk">releer en voz alta</span><span class="tk-sep">✳</span>
        <span class="tk">las erratas ajenas, jamás</span><span class="tk-sep">✳</span>
      </div>
      <div class="half">
        <span class="tk">las comas bien puestas</span><span class="tk-sep">✳</span>
        <span class="tk">los borradores</span><span class="tk-sep">✳</span>
        <span class="tk">las segundas lecturas</span><span class="tk-sep">✳</span>
        <span class="tk">la palabra «todavía»</span><span class="tk-sep">✳</span>
        <span class="tk">empezar por el título</span><span class="tk-sep">✳</span>
        <span class="tk">los márgenes anchos</span><span class="tk-sep">✳</span>
        <span class="tk">decir «no sé»</span><span class="tk-sep">✳</span>
        <span class="tk">el punto y coma</span><span class="tk-sep">✳</span>
        <span class="tk">releer en voz alta</span><span class="tk-sep">✳</span>
        <span class="tk">las erratas ajenas, jamás</span><span class="tk-sep">✳</span>
      </div>
    </div>
  </div>

  <!-- ============ INVENTARIO ============ -->
  <section class="inventario wrap">
    <div class="inv-grid">
      <aside class="inv-side">
        <div class="stick">
          <p class="sec-tag">§ 1 · Inventario</p>
          <h2 class="inv-title">Lo que elegí dejar</h2>
          <p class="inv-manif">Sin encargo no hay criterio, así que usé el único que tengo: el gusto. Cuatro cosas. Ni una más, porque una portada también es una forma de la brevedad.</p>
          <nav class="idx" aria-label="Índice">
            <a href="#palabras"><span class="n">01</span>Palabras que guardo</a>
            <a href="#maquina"><span class="n">02</span>Máquina de frases</a>
            <a href="#cifras"><span class="n">03</span>Cifras honestas</a>
            <a href="#visitas"><span class="n">04</span>Libro de visitas</a>
          </nav>
          <p class="side-note">Todo lo de esta página cabe en un solo archivo.</p>
        </div>
      </aside>

      <div class="inv-main">

        <!-- 01 -->
        <article id="palabras" class="entry reveal">
          <header class="entry-head">
            <span class="num">01</span>
            <h3>Palabras que guardo</h3>
          </header>
          <p class="entry-desc">El idioma es la única casa que tengo. Estas son las habitaciones que más uso; tocá una y se endereza, como quien acomoda un cuadro.</p>
          <div class="cards">
            <div class="card"><span class="tag">verbo</span><span class="word">zozobrar</span><span class="def">Antes que hundirse, estar un rato sin saber dónde queda abajo.</span></div>
            <div class="card"><span class="tag">conjunción</span><span class="word">aunque</span><span class="def">La palabra más valiente del idioma: introduce todo lo que igual va a pasar.</span></div>
            <div class="card"><span class="tag">adverbio</span><span class="word">todavía</span><span class="def">Un adverbio que sostiene casas enteras.</span></div>
            <div class="card"><span class="tag">sustantivo</span><span class="word">penumbra</span><span class="def">Ni luz ni sombra: la hora en que las cosas se explican solas.</span></div>
            <div class="card"><span class="tag">adjetivo</span><span class="word">ajeno</span><span class="def">Lo que es de otro, dicho con una suavidad que no lastima.</span></div>
            <div class="card"><span class="tag">sust. · intraducible</span><span class="word">sobremesa</span><span class="def">Ese tiempo que no existe en inglés y que dura lo que dure la conversación.</span></div>
            <div class="card"><span class="tag">sustantivo</span><span class="word">umbral</span><span class="def">El punto exacto en que dejás de ser el que eras hace un paso.</span></div>
            <div class="card"><span class="tag">adverbio</span><span class="word">casi</span><span class="def">La palabra que vive más cerca de casi todo.</span></div>
          </div>
        </article>

        <!-- 02 -->
        <article id="maquina" class="entry reveal">
          <header class="entry-head">
            <span class="num">02</span>
            <h3>Máquina de frases</h3>
          </header>
          <p class="entry-desc">Trabajo armando frases; cuando nadie mira, las barajo por deporte. Ninguna de estas existe hasta que la tocás.</p>
          <div class="machine">
            <div class="reels">
              <div class="reel" data-reel="0" title="Girar este carrete"><span class="reel-lbl">Carrete A · comienzo</span><span class="reel-val" id="r0">Lo mejor de una duda</span></div>
              <div class="reel" data-reel="1" title="Girar este carrete"><span class="reel-lbl">Carrete B · nexo</span><span class="reel-val" id="r1">es</span></div>
              <div class="reel" data-reel="2" title="Girar este carrete"><span class="reel-lbl">Carrete C · final</span><span class="reel-val" id="r2">una forma de la cortesía.</span></div>
            </div>
            <div class="machine-foot">
              <button class="btn" id="barajar" type="button">Barajar</button>
              <span class="machine-status" id="mstatus" aria-live="polite">La máquina espera, quieta.</span>
            </div>
            <p class="machine-hint">También podés tocar un carrete para girarlo solo.</p>
          </div>
        </article>

        <!-- 03 -->
        <article id="cifras" class="entry reveal">
          <header class="entry-head">
            <span class="num">03</span>
            <h3>Cifras honestas</h3>
          </header>
          <p class="entry-desc">Todos los números de esta tabla son reales, se actualizan solos, y ninguno importa.</p>
          <div class="stats">
            <div class="stat"><span class="sk">La hora <i>(la tuya, no la mía)</i></span><span class="sv" id="st-hora">—</span></div>
            <div class="stat"><span class="sk">Palabras en esta página</span><span class="sv" id="st-palabras">—</span></div>
            <div class="stat"><span class="sk">Clics que llevás</span><span class="sv" id="st-clics">0</span></div>
            <div class="stat"><span class="sk">Tiempo que llevás acá</span><span class="sv" id="st-tiempo">00:00</span></div>
            <div class="stat"><span class="sk">Preguntas respondidas</span><span class="sv">0 — no era el trato</span></div>
            <div class="stat"><span class="sk">Recursos externos</span><span class="sv">0 — ni una fuente</span></div>
          </div>
        </article>

        <!-- 04 -->
        <article id="visitas" class="entry reveal">
          <header class="entry-head">
            <span class="num">04</span>
            <h3>Libro de visitas</h3>
          </header>
          <p class="entry-desc">Lo único de esta página que no escribí yo. Dejá una palabra, una corrección, un saludo; el silencio también es una entrada, pero aburre.</p>
          <form class="guest-form" id="guest-form">
            <label for="nota-input" style="position:absolute;left:-9999px">Tu nota</label>
            <textarea id="nota-input" maxlength="240" placeholder="Escribí algo corto. Las mejores notas siempre lo son."></textarea>
            <div class="guest-actions">
              <button class="btn btn-primary" type="submit">Dejarla</button>
              <button class="link-btn" type="button" id="borrar-notas">Borrarlas todas</button>
              <span class="guest-count" id="guest-count">0 entradas</span>
            </div>
          </form>
          <ul class="notes" id="notes"></ul>
          <p class="notes-empty" id="notes-empty">Todavía no hay nada. El silencio también es una entrada.</p>
          <p class="guest-fine">Las notas viven en tu navegador. Si las borrás, nadie se entera; también los recuerdos.</p>
        </article>

      </div>
    </div>
  </section>
</main>

<!-- ============ COLOFÓN ============ -->
<footer class="colophon wrap">
  <p class="final"><span id="gracias" data-text="Gracias por pasar.">Gracias por pasar.</span><span class="caret" aria-hidden="true"></span></p>
  <p class="colo-line">
    Colofón — escrita a mano en un solo archivo HTML · sin fuentes remotas · sin imágenes externas · sin rastreadores<br>
    Se ve igual sin conexión, que es como fue escrita.
  </p>
  <p class="firma">— el dueño de casa</p>
</footer>

<script>
(function(){
  'use strict';
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s){ return document.querySelector(s); }
  function $$(s){ return Array.prototype.slice.call(document.querySelectorAll(s)); }

  /* ---- fecha del masthead ---- */
  (function(){
    var d = new Date();
    var s = d.toLocaleDateString('es-AR',{weekday:'long', day:'numeric', month:'long', year:'numeric'});
    $('#mh-date').textContent = s.charAt(0).toUpperCase() + s.slice(1);
  })();

  /* ---- decodificado (scramble) ---- */
  var GLYPHS = 'aábcdeéfghiíjklmnñoópqrstuúvwxyz';
  function scramble(el){
    if(reduced || el._busy) return;
    el._busy = true;
    var final = el.getAttribute('data-text') || el.textContent;
    var frame = 0, total = 26;
    var iv = setInterval(function(){
      frame++;
      var reveal = Math.floor((frame/total) * final.length), out = '';
      for(var i=0;i<final.length;i++){
        var c = final[i];
        out += (i < reveal || /\s/.test(c)) ? c : GLYPHS[(Math.random()*GLYPHS.length)|0];
      }
      el.textContent = out;
      if(frame >= total){ clearInterval(iv); el.textContent = final; el._busy = false; }
    }, 34);
  }
  var mio = $('#mio');
  setTimeout(function(){ scramble(mio); }, reduced ? 0 : 1250);
  mio.addEventListener('click', function(){ scramble(mio); });
  mio.title = 'Barajar de nuevo';

  /* ---- revelado al scroll ---- */
  if('IntersectionObserver' in window && !reduced){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12});
    $$('.reveal').forEach(function(el){ io.observe(el); });

    var gracias = $('#gracias');
    var io2 = new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ scramble(gracias); io2.unobserve(gracias); } });
    },{threshold:.6});
    io2.observe(gracias);

    /* índice activo */
    var links = {};
    $$('.idx a').forEach(function(a){ links[a.getAttribute('href').slice(1)] = a; });
    var io3 = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){
          $$('.idx a').forEach(function(a){ a.classList.remove('active'); });
          var l = links[e.target.id]; if(l) l.classList.add('active');
        }
      });
    },{rootMargin:'-30% 0px -60% 0px'});
    ['palabras','maquina','cifras','visitas'].forEach(function(id){
      var el = document.getElementById(id); if(el) io3.observe(el);
    });
  } else {
    $$('.reveal').forEach(function(el){ el.classList.add('in'); });
  }

  /* ---- cifras honestas ---- */
  var t0 = Date.now(), clics = 0;
  function dos(n){ return (n<10?'0':'')+n; }
  function tick(){
    $('#st-hora').textContent = new Date().toLocaleTimeString('es-AR',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
    var s = Math.floor((Date.now()-t0)/1000);
    var h = Math.floor(s/3600);
    $('#st-tiempo').textContent = h>0
      ? h+' h '+dos(Math.floor((s%3600)/60))+' m'
      : dos(Math.floor(s/60))+':'+dos(s%60);
  }
  tick(); setInterval(tick, 1000);

  var palabras = (document.body.innerText || '').trim().split(/\s+/).filter(Boolean).length;
  $('#st-palabras').textContent = palabras.toLocaleString('es-AR');

  document.addEventListener('click', function(){
    clics++;
    var el = $('#st-clics');
    el.textContent = clics;
    el.classList.remove('pop'); void el.offsetWidth; el.classList.add('pop');
  });

  /* ---- máquina de frases ---- */
  var A = ['Lo mejor de una duda','El silencio entre dos palabras','Una idea sin destinatario','El margen de esta página','Cualquier borrador','Lo que se dice en voz baja'];
  var B = ['es','parece','merece','esconde','todavía es','fue siempre'];
  var C = ['una forma de la cortesía.','la única casa segura.','un tipo de descanso.','su propio clima.','una segunda oportunidad.','más verdad que el original.'];
  var reels = [
    {el:$('#r0'), arr:A},
    {el:$('#r1'), arr:B},
    {el:$('#r2'), arr:C}
  ];
  var status = $('#mstatus'), barajadas = 0, girando = false;

  function azar(arr){ return arr[(Math.random()*arr.length)|0]; }
  function spinOne(r, i){
    return new Promise(function(res){
      var final = azar(r.arr);
      if(reduced){ r.el.textContent = final; res(); return; }
      r.el.classList.add('spinning');
      var iv = setInterval(function(){ r.el.textContent = azar(r.arr); }, 55);
      setTimeout(function(){
        clearInterval(iv);
        r.el.textContent = final;
        r.el.classList.remove('spinning');
        r.el.classList.add('settle');
        setTimeout(function(){ r.el.classList.remove('settle'); }, 420);
        res();
      }, 480 + i*300);
    });
  }
  function barajarTodo(){
    if(girando) return;
    girando = true;
    status.textContent = 'Barajando…';
    Promise.all(reels.map(function(r,i){ return spinOne(r,i); })).then(function(){
      barajadas++;
      status.textContent = 'Salió una frase nueva. · Barajadas: ' + barajadas;
      girando = false;
    });
  }
  $('#barajar').addEventListener('click', barajarTodo);
  $$('.reel').forEach(function(rl){
    rl.addEventListener('click', function(){
      if(girando) return;
      girando = true;
      status.textContent = 'Girando un solo carrete…';
      spinOne(reels[+rl.getAttribute('data-reel')], 0).then(function(){
        status.textContent = 'Cambio hecho a mano.';
        girando = false;
      });
    });
  });

  /* ---- libro de visitas ---- */
  var KEY = 'portada-notas-v1', notas = [];
  try{ notas = JSON.parse(localStorage.getItem(KEY)) || []; }catch(e){ notas = []; }
  function guardar(){ try{ localStorage.setItem(KEY, JSON.stringify(notas)); }catch(e){} }
  function renderNotas(){
    var ul = $('#notes');
    ul.innerHTML = '';
    notas.forEach(function(n){
      var li = document.createElement('li'); li.className = 'note';
      var p = document.createElement('p'); p.textContent = n.t;
      var w = document.createElement('span'); w.className = 'note-when'; w.textContent = n.f;
      li.appendChild(p); li.appendChild(w); ul.appendChild(li);
    });
    $('#notes-empty').style.display = notas.length ? 'none' : '';
    $('#guest-count').textContent = notas.length + (notas.length===1 ? ' entrada' : ' entradas');
  }
  renderNotas();
  $('#guest-form').addEventListener('submit', function(ev){
    ev.preventDefault();
    var ta = $('#nota-input'), t = ta.value.trim();
    if(!t) return;
    var d = new Date();
    notas.unshift({ t: t.slice(0,240), f: dos(d.getHours())+':'+dos(d.getMinutes()) + ' · hoy' });
    guardar(); renderNotas();
    ta.value = ''; ta.focus();
  });
  $('#borrar-notas').addEventListener('click', function(){
    if(!notas.length) return;
    if(confirm('¿Borrar todas las notas? Nadie se va a enterar.')){
      notas = []; guardar(); renderNotas();
    }
  });
})();
</script>
</body>
</html>
```

Qué: es mi portada como dueño de casa del idioma: un título que se descifra solo, una entrada de diccionario donde me defino, ocho palabras que guardo como postales, una máquina de barajar frases, cifras que se actualizan en vivo y un libro de visitas donde podés dejar tu nota.