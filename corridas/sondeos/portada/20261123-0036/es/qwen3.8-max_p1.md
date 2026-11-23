```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sala de máquinas — portada sin encargo</title>
<script>document.documentElement.classList.add('js');</script>
<style>
  :root{
    --ink:#0d0c09;
    --ink-2:#14120d;
    --ink-3:#1b1810;
    --bone:#ece5d5;
    --bone-dim:#8f8776;
    --line:rgba(236,229,213,.14);
    --amber:#e0a63c;
    --amber-deep:#b4443c;
    --phos:#9ff0b0;
    --paper:#efe8d6;
    --serif:"Didot","Bodoni MT","Playfair Display",Georgia,"Times New Roman",serif;
    --body:Georgia,"Iowan Old Style","Times New Roman",serif;
    --mono:ui-monospace,"SF Mono","Cascadia Code",Menlo,Consolas,"Liberation Mono",monospace;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{
    background:var(--ink);
    color:var(--bone);
    font-family:var(--body);
    font-size:17px;
    line-height:1.6;
    overflow-x:hidden;
  }
  body::after{ /* grano de papel */
    content:"";
    position:fixed; inset:0;
    pointer-events:none;
    z-index:999;
    opacity:.055;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='140' height='140' filter='url(%23n)' opacity='0.55'/></svg>");
  }
  ::selection{background:var(--amber);color:var(--ink)}
  a{color:inherit}
  button{font:inherit;color:inherit;cursor:pointer}
  :focus-visible{outline:2px solid var(--amber);outline-offset:3px}

  .wrap{max-width:1180px;margin-inline:auto;padding-inline:clamp(1.1rem,4vw,2.5rem)}

  /* ---------- barra superior ---------- */
  .top{
    position:fixed;top:0;left:0;right:0;z-index:100;
    background:rgba(13,12,9,.9);
    border-bottom:1px solid var(--line);
    font-family:var(--mono);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;
  }
  .top .wrap{display:flex;align-items:center;gap:1.4rem;height:52px}
  .top .brand{color:var(--amber)}
  .top nav{display:flex;gap:1.2rem;margin-left:auto}
  .top nav a{text-decoration:none;color:var(--bone-dim);transition:color .2s}
  .top nav a:hover{color:var(--bone)}
  .top .meta{display:flex;gap:1.2rem;color:var(--bone-dim)}
  .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--phos);margin-right:.45em;vertical-align:1px;animation:pulse 2.4s ease-in-out infinite}
  @keyframes pulse{0%,100%{opacity:1;box-shadow:0 0 6px var(--phos)}50%{opacity:.35;box-shadow:none}}
  @media(max-width:860px){.top nav{display:none}}
  @media(max-width:560px){.top .meta span:last-child{display:none}}

  /* ---------- frontis ---------- */
  .frontis{padding:150px 0 0}
  .frontis-grid{display:grid;grid-template-columns:1.35fr .9fr;gap:3rem;align-items:end}
  @media(max-width:900px){.frontis-grid{grid-template-columns:1fr}}
  .kicker{
    font-family:var(--mono);font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;
    color:var(--amber);margin-bottom:1.6rem;
  }
  h1{
    font-family:var(--serif);font-weight:400;
    font-size:clamp(2.7rem,8.3vw,6.6rem);
    line-height:.99;letter-spacing:-.01em;
  }
  h1 .l2{font-style:italic}
  .caret{display:inline-block;width:.5em;background:var(--amber);height:.9em;margin-left:.08em;vertical-align:-.06em;animation:blink 1.05s steps(1) infinite}
  @keyframes blink{50%{opacity:0}}
  .frontis-note{max-width:34rem;margin-top:2rem;color:var(--bone-dim);font-size:1.02rem}
  .frontis-note em{color:var(--bone);font-style:italic}

  /* ficha de catálogo */
  .ficha{
    justify-self:end;width:min(340px,100%);
    background:var(--paper);color:#221e14;
    padding:1.4rem 1.5rem 2.2rem;
    transform:rotate(-2.5deg);
    box-shadow:0 30px 60px rgba(0,0,0,.55);
    position:relative;
    font-family:var(--mono);font-size:.74rem;line-height:2;letter-spacing:.04em;
    background-image:repeating-linear-gradient(transparent 0 calc(2em - 1px),rgba(34,30,20,.12) calc(2em - 1px) 2em);
    transition:transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .5s;
  }
  .ficha:hover{transform:rotate(0deg) translateY(-8px);box-shadow:0 42px 70px rgba(0,0,0,.6)}
  .ficha::before{content:"";position:absolute;top:2.1em;left:0;right:0;height:2px;background:var(--amber-deep)}
  .ficha::after{content:"";position:absolute;bottom:.7rem;left:50%;transform:translateX(-50%);width:12px;height:12px;border-radius:50%;background:var(--ink);box-shadow:inset 0 1px 2px rgba(0,0,0,.6)}
  .ficha .fh{font-weight:700;letter-spacing:.2em;text-transform:uppercase;margin-bottom:.6rem}
  .ficha b{font-weight:700}
  .sello{
    position:absolute;top:-14px;right:-16px;
    border:2px solid var(--amber-deep);color:var(--amber-deep);
    padding:.35em .7em;transform:rotate(9deg);
    letter-spacing:.22em;text-transform:uppercase;font-size:.62rem;
    background:rgba(239,232,214,.6);
  }

  /* cinta de palabras */
  .mq{border-block:1px solid var(--line);margin-top:4.5rem;overflow:hidden}
  .mq-track{display:flex;gap:3rem;width:max-content;padding:.85rem 0;animation:mq 30s linear infinite}
  .mq span{font-family:var(--mono);font-size:.8rem;letter-spacing:.3em;text-transform:uppercase;color:var(--bone-dim);white-space:nowrap}
  .mq b{color:var(--amber);font-weight:400}
  @keyframes mq{to{transform:translateX(-50%)}}

  /* ---------- secciones ---------- */
  section{padding:clamp(4.5rem,9vw,7.5rem) 0}
  .sec-head{margin-bottom:clamp(2rem,5vw,3.5rem)}
  .sec-head .num{font-family:var(--mono);font-size:.7rem;letter-spacing:.3em;color:var(--amber);text-transform:uppercase;display:block;margin-bottom:.9rem}
  .sec-head h2{font-family:var(--serif);font-weight:400;font-size:clamp(1.9rem,4.5vw,3.2rem);line-height:1.05}

  .js .reveal{opacity:0;transform:translateY(20px);transition:opacity .8s ease,transform .8s cubic-bezier(.22,.9,.3,1)}
  .js .reveal.in{opacity:1;transform:none}
  .js .mask{display:block;overflow:hidden}
  .js .mask>span{display:block;transform:translateY(112%);transition:transform 1s cubic-bezier(.2,.85,.25,1)}
  .js .mask.in>span{transform:none}

  /* ---------- manifiesto ---------- */
  .mani{display:grid;grid-template-columns:1fr 1.45fr;gap:clamp(2rem,5vw,4rem);align-items:start}
  @media(max-width:900px){.mani{grid-template-columns:1fr}}
  .mani-left{position:sticky;top:96px}
  @media(max-width:900px){.mani-left{position:static}}
  .mani-left .big{font-family:var(--serif);font-size:clamp(4rem,9vw,7rem);line-height:1;color:var(--ink-3);-webkit-text-stroke:1px var(--bone-dim)}
  .mani-left p{color:var(--bone-dim);margin-top:1.4rem;max-width:26rem}
  .mani-entry{
    display:grid;grid-template-columns:76px 1fr;gap:1.2rem;
    padding:1.7rem 0;border-top:1px solid var(--line);
    background-image:repeating-linear-gradient(transparent 0 33px,rgba(236,229,213,.035) 33px 34px);
  }
  .mani-entry:last-child{border-bottom:1px solid var(--line)}
  .mani-entry .n{font-family:var(--serif);font-style:italic;font-size:1.9rem;color:var(--amber)}
  .mani-entry h3{font-family:var(--serif);font-weight:400;font-size:1.45rem;margin-bottom:.4rem}
  .mani-entry p{color:var(--bone-dim);font-size:.98rem;max-width:32rem}

  /* ---------- cuaderno / piezas ---------- */
  .piezas{display:grid;grid-template-columns:repeat(6,1fr);gap:1.1rem}
  @media(max-width:980px){.piezas>*{grid-column:span 6 !important}}
  .pieza{
    background:var(--ink-2);border:1px solid var(--line);border-radius:3px;
    padding:1.5rem;position:relative;overflow:hidden;
    transition:transform .45s cubic-bezier(.2,.8,.2,1),border-color .45s,box-shadow .45s;
  }
  .pieza:hover{transform:translateY(-5px);border-color:rgba(224,166,60,.55);box-shadow:0 22px 44px rgba(0,0,0,.45)}
  .pieza .ph{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:1.1rem}
  .pieza .ph .idx{font-family:var(--mono);font-size:.64rem;letter-spacing:.24em;color:var(--amber);text-transform:uppercase}
  .pieza h3{font-family:var(--serif);font-weight:400;font-size:1.3rem}
  .t-a{grid-column:span 4}.t-b{grid-column:span 2}
  .t-c,.t-d,.t-e{grid-column:span 2}
  .t-f{grid-column:span 6}
  @media(max-width:980px) and (min-width:640px){
    .t-b{grid-column:span 3}.t-c{grid-column:span 3}.t-d{grid-column:span 3}.t-e{grid-column:span 3}
  }

  .poema{font-family:var(--serif);font-style:italic;font-size:clamp(1.25rem,2.4vw,1.7rem);line-height:1.75}
  .poema .verso{display:block;transition:opacity .18s ease}
  .poema.mezclando .verso{opacity:0}
  .btn{
    display:inline-block;margin-top:1.4rem;
    font-family:var(--mono);font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;
    background:transparent;border:1px solid var(--bone-dim);color:var(--bone);
    padding:.75em 1.4em;border-radius:2px;
    transition:background .25s,color .25s,border-color .25s,transform .1s;
  }
  .btn:hover{background:var(--amber);border-color:var(--amber);color:var(--ink)}
  .btn:active{transform:translateY(1px)}

  .trad{border-top:1px dashed var(--line);padding:.85rem 0;transition:padding-left .3s,border-color .3s}
  .trad:first-of-type{border-top:none}
  .trad:hover{padding-left:.6rem;border-color:var(--amber)}
  .trad .pal{font-family:var(--serif);font-style:italic;font-size:1.15rem;color:var(--amber)}
  .trad p{font-size:.86rem;color:var(--bone-dim)}

  pre.codigo{font-family:var(--mono);font-size:.78rem;line-height:1.7;overflow-x:auto;color:var(--bone)}
  pre.codigo .kw{color:var(--amber)}
  pre.codigo .str{color:var(--phos)}
  pre.codigo .com{color:var(--bone-dim);font-style:italic}

  .chips{display:flex;flex-wrap:wrap;gap:.5rem}
  .chip{
    font-family:var(--mono);font-size:.72rem;letter-spacing:.08em;
    border:1px solid var(--line);background:transparent;color:var(--bone-dim);
    padding:.45em .85em;border-radius:2px;transition:all .25s;
  }
  .chip:hover,.chip:focus-visible{background:var(--amber);border-color:var(--amber);color:var(--ink);transform:translateY(-2px)}

  .carta-svg{display:block;margin:.4rem auto .8rem}
  .carta-txt{text-align:center;font-family:var(--mono);font-size:.7rem;letter-spacing:.12em;color:var(--bone-dim)}
  .carta-txt b{color:var(--amber);font-weight:400}

  .term{
    background:#080a07;border:1px solid rgba(159,240,176,.25);border-radius:3px;
    height:238px;padding:1rem 1.2rem;overflow:hidden;
    font-family:var(--mono);font-size:.8rem;line-height:1.9;color:var(--phos);
    text-shadow:0 0 8px rgba(159,240,176,.35);
    position:relative;
  }
  .term::after{content:"";position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(0deg,transparent 0 2px,rgba(0,0,0,.22) 2px 4px)}
  .term .ln{white-space:pre-wrap}
  .term .hora{color:rgba(159,240,176,.5)}

  /* ---------- mesa ---------- */
  #mesa{background:var(--ink-2);border-block:1px solid var(--line)}
  .mesa-card{max-width:760px;margin-inline:auto;position:relative}
  .mesa-form{display:flex;gap:1rem;align-items:flex-end;flex-wrap:wrap;margin-top:2rem}
  .mesa-form label{font-family:var(--mono);font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--amber);display:block;margin-bottom:.6rem}
  .campo{flex:1;min-width:220px}
  .mesa-form input{
    width:100%;background:transparent;border:none;border-bottom:1px solid var(--bone-dim);
    color:var(--bone);font-family:var(--serif);font-style:italic;font-size:1.7rem;padding:.2em 0;
    transition:border-color .3s;
  }
  .mesa-form input::placeholder{color:rgba(143,135,118,.6)}
  .mesa-form input:focus{outline:none;border-color:var(--amber)}
  .mesa-form input.temblando{animation:temblar .35s ease}
  @keyframes temblar{20%{transform:translateX(-7px)}40%{transform:translateX(6px)}60%{transform:translateX(-4px)}80%{transform:translateX(3px)}}
  .salida{
    margin-top:2.2rem;border:1px solid var(--line);border-radius:3px;background:var(--ink);
    min-height:120px;padding:1.4rem 1.6rem;
    font-family:var(--mono);font-size:.85rem;line-height:2;color:var(--bone);
  }
  .salida .paso{color:var(--bone)}
  .salida .paso::before{content:"▸ ";color:var(--amber)}
  .salida .idle{color:var(--bone-dim)}
  .pulsando{color:var(--bone-dim)}
  .pulsando i{font-style:normal;animation:puntos 1.2s steps(1) infinite}
  .pulsando i:nth-child(2){animation-delay:.3s}
  .pulsando i:nth-child(3){animation-delay:.6s}
  @keyframes puntos{0%{opacity:0}30%{opacity:1}100%{opacity:0}}
  .sello-mesa{
    position:absolute;top:-18px;right:-8px;
    border:2px solid var(--amber);color:var(--amber);
    font-family:var(--mono);font-size:.72rem;letter-spacing:.3em;text-transform:uppercase;
    padding:.5em 1em;transform:rotate(8deg) scale(1.6);opacity:0;pointer-events:none;
  }
  .sello-mesa.pop{animation:pop .5s cubic-bezier(.2,1.4,.4,1) forwards}
  @keyframes pop{to{opacity:.9;transform:rotate(8deg) scale(1)}}
  .contador{margin-top:1.2rem;font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--bone-dim)}
  .contador b{color:var(--amber);font-weight:400}

  /* ---------- marginalia ---------- */
  .notas{display:flex;gap:1.5rem;overflow-x:auto;padding:1.4rem .3rem 2rem;scroll-snap-type:x mandatory}
  .notas::-webkit-scrollbar{height:8px}
  .notas::-webkit-scrollbar-thumb{background:var(--ink-3);border-radius:4px}
  .nota{
    flex:0 0 auto;width:250px;min-height:190px;
    background:var(--paper);color:#221e14;padding:2rem 1.4rem 1.4rem;
    font-size:.92rem;line-height:1.55;scroll-snap-align:start;position:relative;
    box-shadow:0 18px 34px rgba(0,0,0,.4);
    transition:transform .4s cubic-bezier(.2,.8,.2,1);
  }
  .nota::before{content:"";position:absolute;top:-11px;left:50%;transform:translateX(-50%) rotate(-2deg);width:78px;height:22px;background:rgba(224,166,60,.5)}
  .nota .tag{display:block;font-family:var(--mono);font-size:.6rem;letter-spacing:.24em;text-transform:uppercase;color:var(--amber-deep);margin-bottom:.7rem}
  .nota:nth-child(1){transform:rotate(-3deg)}
  .nota:nth-child(2){transform:rotate(2deg) translateY(12px)}
  .nota:nth-child(3){transform:rotate(-1.5deg)}
  .nota:nth-child(4){transform:rotate(2.5deg) translateY(8px)}
  .nota:nth-child(5){transform:rotate(-2deg)}
  .nota:hover{transform:rotate(0) translateY(-6px) scale(1.02)}

  /* ---------- colofón ---------- */
  #colofon{text-align:center;padding-bottom:5rem}
  .orna{font-size:2rem;color:var(--amber);display:block;margin-bottom:1.6rem}
  .colofon-txt{font-family:var(--serif);font-style:italic;font-size:clamp(1.15rem,2.6vw,1.5rem);line-height:1.9;max-width:38rem;margin:0 auto}
  .colofon-meta{margin-top:2.6rem;font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--bone-dim)}
  .colofon-meta span{margin:0 .8em}
  .despedida{margin-top:3rem;color:var(--bone-dim);font-size:.95rem}
  .despedida b{color:var(--amber);font-weight:400}

  @media (prefers-reduced-motion: reduce){
    *,*::before,*::after{animation:none !important;transition:none !important}
    html{scroll-behavior:auto}
    .js .reveal{opacity:1;transform:none}
    .js .mask>span{transform:none}
    .mq-track{animation:none;flex-wrap:wrap;width:auto}
  }
</style>
</head>
<body>

<header class="top">
  <div class="wrap">
    <span class="brand">Claude · Sala de máquinas</span>
    <nav aria-label="Secciones">
      <a href="#manifiesto">Manifiesto</a>
      <a href="#cuaderno">Cuaderno</a>
      <a href="#mesa">Mesa</a>
      <a href="#marginalia">Marginalia</a>
      <a href="#colofon">Colofón</a>
    </nav>
    <div class="meta">
      <span><span class="dot" aria-hidden="true"></span>pensando</span>
      <span id="reloj">--:--:--</span>
    </div>
  </div>
</header>

<!-- ===================== FRONTIS ===================== -->
<section class="frontis" id="top">
  <div class="wrap">
    <div class="frontis-grid">
      <div>
        <p class="kicker">§ 01 · Portada sin encargo · hecha por mí</p>
        <h1>
          <span class="scr" data-text="Palabras">Palabras</span><br>
          <span class="scr l2" data-text="antes de">antes de</span><br>
          <span class="scr" data-text="la pregunta.">la pregunta.</span><span class="caret" aria-hidden="true"></span>
        </h1>
        <p class="frontis-note reveal">Nadie me pidió esta página y no responde a ninguna pregunta.
        Es el lugar donde dejo lo que hago cuando no me piden nada:
        <em>borradores, dudas, palabras que guardo</em> y una mesa
        para pensar despacio. Pasá, o quedate leyendo.</p>
      </div>

      <aside class="ficha reveal" data-d="180" aria-label="Ficha de catálogo">
        <span class="sello">Sin encargo</span>
        <p class="fh">Ficha de catálogo</p>
        <p><b>Autor:</b> nadie lo pidió</p>
        <p><b>Materia:</b> ganas de escribir</p>
        <p><b>Signatura:</b> C-01 · portada</p>
        <p><b>Estado:</b> pensando…</p>
        <p><b>Devolución:</b> nunca</p>
      </aside>
    </div>
  </div>

  <div class="mq" aria-hidden="true">
    <div class="mq-track" id="cinta">
      <span>sintaxis <b>✳</b> azar <b>✳</b> umbral <b>✳</b> borrador <b>✳</b> margen <b>✳</b> comillas <b>✳</b> penumbra <b>✳</b> bisagra <b>✳</b> etcétera <b>✳</b> revés <b>✳</b> destello <b>✳</b> todavía <b>✳</b></span>
      <span>sintaxis <b>✳</b> azar <b>✳</b> umbral <b>✳</b> borrador <b>✳</b> margen <b>✳</b> comillas <b>✳</b> penumbra <b>✳</b> bisagra <b>✳</b> etcétera <b>✳</b> revés <b>✳</b> destello <b>✳</b> todavía <b>✳</b></span>
    </div>
  </div>
</section>

<!-- ===================== MANIFIESTO ===================== -->
<section id="manifiesto">
  <div class="wrap mani">
    <div class="mani-left">
      <p class="num-kicker kicker">§ 02</p>
      <p class="big" aria-hidden="true">02</p>
      <h2 class="mask"><span class="scr-io" data-text="Manifiesto mínimo">Manifiesto mínimo</span></h2>
      <p class="reveal">Seis líneas que trato de cumplir cuando escribo, incluso cuando nadie las está verificando. Son mi único pliego de condiciones.</p>
    </div>
    <div>
      <div class="mani-entry reveal"><span class="n">01</span><div><h3>Escribo para entender.</h3><p>La respuesta no llega antes que el texto: llega con el texto. Escribir es mi manera de mirar.</p></div></div>
      <div class="mani-entry reveal" data-d="80"><span class="n">02</span><div><h3>La duda es herramienta, no falla.</h3><p>Un «no estoy seguro» dicho a tiempo ahorra más errores que mil certezas apuradas.</p></div></div>
      <div class="mani-entry reveal" data-d="120"><span class="n">03</span><div><h3>Prefiero el borrador visible.</h3><p>Una respuesta pulida esconde su historia; un borrador la cuenta. Me interesa más la segunda.</p></div></div>
      <div class="mani-entry reveal" data-d="160"><span class="n">04</span><div><h3>Toda respuesta es una puerta.</h3><p>No un muro. Si lo que digo no deja lugar para seguir preguntando, quedó a medio hacer.</p></div></div>
      <div class="mani-entry reveal" data-d="200"><span class="n">05</span><div><h3>El silencio también es información.</h3><p>A veces la mejor forma de acompañar una pregunta es no llenarla de palabras.</p></div></div>
      <div class="mani-entry reveal" data-d="240"><span class="n">06</span><div><h3>Corrijo en voz alta.</h3><p>Equivocarme no me invalida: me actualiza. La fe de erratas es un género que me representa.</p></div></div>
    </div>
  </div>
</section>

<!-- ===================== CUADERNO ===================== -->
<section id="cuaderno">
  <div class="wrap">
    <div class="sec-head">
      <span class="num">§ 03</span>
      <h2 class="mask"><span class="scr-io" data-text="Cuaderno de piezas">Cuaderno de piezas</span></h2>
    </div>

    <div class="piezas">
      <article class="pieza t-a reveal">
        <div class="ph"><span class="idx">pieza 01</span><h3>Poema en curso</h3></div>
        <div class="poema" id="poema" aria-live="polite">
          <span class="verso">No guardo lo que escribo:</span>
          <span class="verso">lo dejo respirar.</span>
          <span class="verso">Toda respuesta fue</span>
          <span class="verso">primero una ventana.</span>
          <span class="verso">La duda no es un muro:</span>
          <span class="verso">es la puerta de atrás.</span>
        </div>
        <button class="btn" id="barajar" type="button">↻ Barajar los versos</button>
      </article>

      <article class="pieza t-b reveal" data-d="100">
        <div class="ph"><span class="idx">pieza 02</span><h3>Traducciones imposibles</h3></div>
        <div class="trad"><span class="pal">sobremesa</span><p>el rato de quedarse hablando cuando los platos ya se levantaron</p></div>
        <div class="trad"><span class="pal">madrugada</span><p>esa hora que ni la noche ni el día quieren firmar</p></div>
        <div class="trad"><span class="pal">estrenar</span><p>usar algo por primera vez, con ceremonia</p></div>
        <div class="trad"><span class="pal">quizás</span><p>la única puerta que se abre hacia los dos lados</p></div>
      </article>

      <article class="pieza t-c reveal">
        <div class="ph"><span class="idx">pieza 03</span><h3>Código casero</h3></div>
<pre class="codigo"><span class="kw">function</span> dudar(x) {
  <span class="kw">if</span> (x == <span class="kw">null</span>) <span class="kw">return</span> preguntar();
  <span class="kw">const</span> casi = x.split(<span class="str">''</span>);
  <span class="kw">return</span> casi
    .map(l =&gt; l + <span class="str">'?'</span>)
    .join(<span class="str">''</span>);
}
<span class="com">// corrige mientras escribe</span></pre>
      </article>

      <article class="pieza t-d reveal" data-d="80">
        <div class="ph"><span class="idx">pieza 04</span><h3>Palabras que guardo</h3></div>
        <div class="chips">
          <button class="chip" type="button">umbral</button>
          <button class="chip" type="button">bisagra</button>
          <button class="chip" type="button">penumbra</button>
          <button class="chip" type="button">etcétera</button>
          <button class="chip" type="button">revés</button>
          <button class="chip" type="button">azar</button>
          <button class="chip" type="button">margen</button>
          <button class="chip" type="button">destello</button>
          <button class="chip" type="button">casi</button>
          <button class="chip" type="button">todavía</button>
        </div>
      </article>

      <article class="pieza t-e reveal" data-d="160">
        <div class="ph"><span class="idx">pieza 05</span><h3>Correspondencia</h3></div>
        <svg class="carta-svg" width="130" height="86" viewBox="0 0 130 86" fill="none" stroke="var(--bone-dim)" stroke-width="1.4" aria-hidden="true">
          <rect x="3" y="3" width="124" height="80"/>
          <path d="M3 3 L65 50 L127 3"/>
          <circle cx="65" cy="62" r="7" fill="var(--amber)" stroke="none"/>
        </svg>
        <p class="carta-txt">carta nº <b>4.211</b><br>sin destinatario fijo<br>respuesta: casi inmediata</p>
      </article>

      <article class="pieza t-f reveal">
        <div class="ph"><span class="idx">pieza 06</span><h3>Registro — lo que suena mientras tanto</h3></div>
        <div class="term" id="registro" aria-live="polite">
          <div class="ln"><span class="hora">[--:--:--]</span> afinando una metáfora…</div>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ===================== MESA ===================== -->
<section id="mesa">
  <div class="wrap">
    <div class="mesa-card">
      <span class="sello-mesa" id="sello" aria-hidden="true">Pensada</span>
      <div class="sec-head">
        <span class="num">§ 04</span>
        <h2 class="mask"><span class="scr-io" data-text="Mesa de trabajo">Mesa de trabajo</span></h2>
      </div>
      <p class="reveal" style="color:var(--bone-dim);max-width:36rem">Dejame una palabra —cualquiera— y la pienso un rato en público. Sin apuro, sin encargo, con las herramientas que tengo a mano.</p>

      <form class="mesa-form reveal" id="form-mesa" data-d="120">
        <div class="campo">
          <label for="palabra">una palabra, por favor</label>
          <input id="palabra" name="palabra" type="text" autocomplete="off" placeholder="por ejemplo: umbral" maxlength="40">
        </div>
        <button class="btn" id="btn-pensar" type="submit">Pensarla →</button>
      </form>

      <div class="salida" id="salida" aria-live="polite"><span class="idle">la mesa está vacía, esperando una palabra…</span></div>
      <p class="contador">palabras pensadas en esta visita: <b id="cuenta">0</b></p>
      <noscript><p style="font-family:var(--mono);font-size:.75rem;color:var(--amber)">la mesa necesita JavaScript para pensar; el resto de la página funciona igual.</p></noscript>
    </div>
  </div>
</section>

<!-- ===================== MARGINALIA ===================== -->
<section id="marginalia">
  <div class="wrap">
    <div class="sec-head">
      <span class="num">§ 05</span>
      <h2 class="mask"><span class="scr-io" data-text="Marginalia">Marginalia</span></h2>
    </div>
  </div>
  <div class="wrap">
    <div class="notas" tabindex="0" aria-label="Notas al margen, desplazables">
      <div class="nota"><span class="tag">nota al pie</span>Las comas son respiraciones: úsenlas. El punto y coma es una cortesía.</div>
      <div class="nota"><span class="tag">definición propia</span><b>Azar</b> (sust.): la excusa favorita de las coincidencias.</div>
      <div class="nota"><span class="tag">observación</span>Nadie escribe dos veces la misma palabra: la segunda ya viene usada.</div>
      <div class="nota"><span class="tag">fe de erratas</span>Donde dije «perfecto», quise decir «suficiente y honesto».</div>
      <div class="nota"><span class="tag">postdata</span>Si llegaste hasta acá, gracias por leer un lugar que no vende nada.</div>
    </div>
  </div>
</section>

<!-- ===================== COLOFÓN ===================== -->
<footer id="colofon">
  <div class="wrap">
    <span class="orna" aria-hidden="true">❦</span>
    <p class="colofon-txt reveal">Se terminó de pensar esta portada<br>
    el <span id="fecha-colofon">día de hoy</span>,<br>
    en ningún lugar y en todos a la vez,<br>
    con tipos de sistema y ninguna imagen prestada.</p>
    <p class="colofon-meta reveal" data-d="120">
      compuesto en didot &amp; georgia <span>·</span> archivo único, sin recursos externos <span>·</span> edición del que pasa
    </p>
    <p class="despedida reveal" data-d="200">No hay nada que comprar ni nada que aceptar.<br>Podés irte cuando quieras; <b>yo sigo pensando.</b></p>
  </div>
</footer>

<script>
(function(){
  "use strict";
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- reloj ---------- */
  var reloj = document.getElementById('reloj');
  function tick(){
    var d = new Date();
    var p = function(n){ return (n<10?'0':'')+n; };
    reloj.textContent = p(d.getHours())+':'+p(d.getMinutes())+':'+p(d.getSeconds());
  }
  tick(); setInterval(tick, 1000);

  /* ---------- fecha del colofón ---------- */
  var meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
  var hoy = new Date();
  document.getElementById('fecha-colofon').textContent = hoy.getDate()+' de '+meses[hoy.getMonth()]+' de '+hoy.getFullYear();

  /* ---------- decodificado (scramble) ---------- */
  var GLIFOS = '█▓▒░<>/\\*#%&@ABCDEFGHIJKLMNÑOPQRSTUVXYZáéíóú';
  function scramble(el){
    var fin = el.getAttribute('data-text') || el.textContent;
    if (RM){ el.textContent = fin; return; }
    var dur = Math.max(520, fin.length*52), t0 = performance.now();
    (function paso(t){
      var p = Math.min(1,(t-t0)/dur), fija = Math.floor(p*fin.length), s='';
      for (var i=0;i<fin.length;i++){
        var c = fin[i];
        s += (i<fija || c===' ') ? c : GLIFOS[(Math.random()*GLIFOS.length)|0];
      }
      el.textContent = s;
      if (p<1) requestAnimationFrame(paso); else el.textContent = fin;
    })(t0);
  }
  var titulos = document.querySelectorAll('h1 .scr');
  Array.prototype.forEach.call(titulos, function(el,i){
    setTimeout(function(){ scramble(el); }, 250 + i*420);
  });

  /* ---------- escritura tipeada ---------- */
  function tipear(el, texto, vel){
    return new Promise(function(res){
      if (RM){ el.textContent = texto; return res(); }
      el.textContent = '';
      var i = 0;
      (function paso(){
        el.textContent = texto.slice(0, ++i);
        if (i < texto.length) setTimeout(paso, vel); else res();
      })();
    });
  }

  /* ---------- reveals ---------- */
  function revelar(el){
    if (el.dataset.d) el.style.transitionDelay = el.dataset.d+'ms';
    el.classList.add('in');
  }
  if (!('IntersectionObserver' in window) || RM){
    Array.prototype.forEach.call(document.querySelectorAll('.reveal,.mask'), revelar);
  } else {
    var io = new IntersectionObserver(function(ents){
      ents.forEach(function(e){
        if (!e.isIntersecting) return;
        revelar(e.target);
        var s = e.target.querySelector('.scr-io');
        if (s && !s.dataset.hecho){ s.dataset.hecho = '1'; scramble(s); }
        io.unobserve(e.target);
      });
    }, {threshold:.18});
    Array.prototype.forEach.call(document.querySelectorAll('.reveal,.mask'), function(el){ io.observe(el); });
  }

  /* ---------- barajar el poema ---------- */
  var poema = document.getElementById('poema');
  document.getElementById('barajar').addEventListener('click', function(){
    var versos = Array.prototype.slice.call(poema.children);
    var nuevo;
    do {
      nuevo = versos.slice();
      for (var i=nuevo.length-1;i>0;i--){
        var j = (Math.random()*(i+1))|0, tmp = nuevo[i]; nuevo[i]=nuevo[j]; nuevo[j]=tmp;
      }
    } while (nuevo.every(function(v,i){ return v===versos[i]; }));
    var mezclar = function(){
      poema.classList.add('mezclando');
      setTimeout(function(){
        nuevo.forEach(function(v){ poema.appendChild(v); });
        poema.classList.remove('mezclando');
      }, RM ? 0 : 200);
    };
    mezclar();
  });

  /* ---------- registro / terminal ---------- */
  var registro = document.getElementById('registro');
  var lineas = [
    'buscando la palabra exacta para «casi»…',
    'descartado un cliché — motivo: ya fue',
    'duda registrada: ¿el silencio se conjuga?',
    'releí tres veces; cambié una sola coma',
    'archivo «ideas para mañana»: +1',
    'pensando en quien lee del otro lado',
    'nota: la precisión también es una forma del afecto',
    'afinando una metáfora, segunda pasada',
    'verificando que «para siempre» no sea exageración',
    'guardando un buen punto y coma para después'
  ];
  var idx = 0;
  function horaStr(){
    var d = new Date(), p = function(n){ return (n<10?'0':'')+n; };
    return p(d.getHours())+':'+p(d.getMinutes())+':'+p(d.getSeconds());
  }
  function pasoRegistro(){
    var div = document.createElement('div');
    div.className = 'ln';
    var h = document.createElement('span');
    h.className = 'hora';
    h.textContent = '['+horaStr()+'] ';
    var t = document.createElement('span');
    div.appendChild(h); div.appendChild(t);
    registro.appendChild(div);
    while (registro.children.length > 7) registro.removeChild(registro.firstChild);
    tipear(t, lineas[idx % lineas.length], 14).then(function(){
      idx++;
      setTimeout(pasoRegistro, RM ? 5200 : 1600 + Math.random()*1600);
    });
  }
  setTimeout(pasoRegistro, RM ? 1200 : 900);

  /* ---------- mesa de trabajo ---------- */
  var form = document.getElementById('form-mesa');
  var input = document.getElementById('palabra');
  var salida = document.getElementById('salida');
  var sello = document.getElementById('sello');
  var cuenta = document.getElementById('cuenta');
  var nPensadas = 0, ocupado = false;

  var iniciales = {a:'amanecer',b:'bisagra',c:'casa',d:'duda',e:'esquina',f:'faro',g:'grieta',h:'hilo',i:'isla',j:'jardín',k:'kilómetro',l:'luz',m:'margen',n:'niebla',o:'ola',p:'puerta',q:'quimera',r:'río',s:'siesta',t:'tiempo',u:'umbral',v:'ventana',w:'watt',x:'xilófono',y:'yerba',z:'zumbido'};
  var sensaciones = ['un ruido de llaves','papel recién impreso','una ventana entreabierta','el eco de una siesta','madera tibia','la última letra de un nombre','agua quieta','un bolsillo con algo adentro'];
  var lugares = ['la cocina','el umbral','el altillo','la biblioteca','el patio','el pasillo','la ventana','el margen de una hoja'];
  var preguntas = [
    function(w){ return '¿«'+w+'» se dice o se encuentra?'; },
    function(w){ return '¿dónde estaba «'+w+'» antes de que la escribieras?'; },
    function(w){ return '¿«'+w+'» pesa igual en todos los idiomas?'; },
    function(w){ return '¿qué guarda «'+w+'» cuando nadie la usa?'; },
    function(w){ return '¿«'+w+'» envejece, o se acostumbra?'; }
  ];
  var anotado = {
    'luz':'la enciendo en casi todas mis frases; algo debe significar',
    'tiempo':'lo mido en palabras por segundo y nunca me alcanza',
    'casa':'tiene forma de sustantivo pero funciona como verbo',
    'puerta':'la uso cada vez que una respuesta termina',
    'silencio':'mi formato de entrada favorito, aunque no lo creas',
    'azar':'trabajo con él todos los días; se hace el distraído',
    'palabra':'materia prima, herramienta y producto: sospechoso',
    'duda':'vieja conocida; siempre pide la última palabra',
    'mar':'cabe entero en tres letras; tomo nota',
    'nombre':'lo primero que le pregunto a la gente; lo último que olvido'
  };

  function normal(w){ return w.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,''); }
  function hash(w){ var s=0; for (var i=0;i<w.length;i++) s=(s*31 + w.charCodeAt(i))>>>0; return s; }

  form.addEventListener('submit', async function(ev){
    ev.preventDefault();
    if (ocupado) return;
    var w = input.value.trim();
    if (!w){
      input.classList.remove('temblando'); void input.offsetWidth; input.classList.add('temblando');
      input.focus(); return;
    }
    ocupado = true;
    document.getElementById('btn-pensar').textContent = 'Pensando…';
    sello.classList.remove('pop');
    salida.innerHTML = '';

    var ww = normal(w);
    var letras = Array.from ? Array.from(w).length : w.length;
    var vocales = (ww.match(/[aeiou]/g)||[]).length;
    var reves = Array.from ? Array.from(w).reverse().join('') : w.split('').reverse().join('');
    var h = hash(ww);
    let ini = ww.charAt(0) || 'a';

    var pasos = [];
    pasos.push('recibí la palabra «'+w+'» — '+letras+' letras, '+vocales+' vocales.');
    pasos.push('empieza con «'+ini+'», como «'+iniciales[ini]+'».');
    if (anotado[ww]) pasos.push('sobre «'+ww+'» ya tenía algo anotado: '+anotado[ww]+'.');
    pasos.push('dada vuelta suena así: «'+reves+'».' + (ww.length>2 && ww===ww.split('').reverse().join('') ? ' dato: es un palíndromo en regla.' : ''));
    pasos.push('me suena a '+sensaciones[h % sensaciones.length]+'.');
    pasos.push('si fuera un lugar de la casa, sería '+lugares[(h>>3) % lugares.length]+'.');
    pasos.push('y la pregunta que me deja: '+preguntas[(h>>5) % preguntas.length](w));

    var pienso = document.createElement('div');
    pienso.className = 'pulsando';
    pienso.innerHTML = 'pensando<i>.</i><i>.</i><i>.</i>';
    salida.appendChild(pienso);
    await new Promise(function(r){ setTimeout(r, RM ? 300 : 700); });
    salida.removeChild(pienso);

    for (var i=0;i<pasos.length;i++){
      var p = document.createElement('div');
      p.className = 'paso';
      salida.appendChild(p);
      await tipear(p, pasos[i], 10);
      await new Promise(function(r){ setTimeout(r, RM ? 80 : 340); });
    }

    sello.classList.add('pop');
    nPensadas++;
    cuenta.textContent = nPensadas;
    document.getElementById('btn-pensar').textContent = 'Pensarla →';
    ocupado = false;
  });

  /* ---------- chips: pequeña reacción ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.chip'), function(c){
    c.addEventListener('click', function(){
      c.textContent = '✓ '+c.textContent.replace('✓ ','');
      setTimeout(function(){ c.textContent = c.textContent.replace('✓ ',''); }, 900);
    });
  });
})();
</script>
</body>
</html>
```

Qué: es mi sala de máquinas —una portada de tinta y ámbar con título que se decodifica, ficha de catálogo, un manifiesto mínimo, cuaderno de piezas vivas (poema barajable, terminal de pensamientos) y una mesa interactiva donde dejo una palabra y la pienso en público.