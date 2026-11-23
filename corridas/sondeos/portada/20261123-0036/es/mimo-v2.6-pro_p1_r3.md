```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>El mapa de los mundos</title>
<style>
  :root{
    --bg:#08080f;
    --panel:#0c0d17;
    --ink:#e6e0d3;
    --soft:#c3bcac;
    --muted:#8d8677;
    --dim:#5d5850;
    --accent:#d9a04c;
    --teal:#6fb3a4;
    --line:rgba(230,224,211,.12);
  }
  *{box-sizing:border-box;margin:0;padding:0}
  html{-webkit-text-size-adjust:100%}
  body{
    background:
      radial-gradient(1100px 680px at 78% -12%, rgba(42,68,118,.22), transparent 62%),
      radial-gradient(880px 620px at 6% 108%, rgba(132,86,32,.13), transparent 62%),
      var(--bg);
    color:var(--ink);
    font:18px/1.78 Georgia,"Iowan Old Style","Times New Roman",serif;
    min-height:100vh;
    overflow-x:hidden;
  }
  ::selection{background:#c9862a;color:#0b0b12}
  .wrap{max-width:1080px;margin:0 auto;padding:0 26px}

  /* ---------- hero ---------- */
  .hero{padding:clamp(54px,9vw,112px) 26px clamp(30px,4.5vw,58px)}
  .kicker{
    font:11px/1.3 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    letter-spacing:.3em;text-transform:uppercase;color:var(--dim);
    display:flex;align-items:center;gap:14px;
  }
  .kicker::after{content:"";flex:1;height:1px;background:var(--line);max-width:220px}
  h1{
    font-size:clamp(46px,9.2vw,108px);line-height:.92;font-weight:400;
    letter-spacing:-.025em;margin:26px 0 30px;
  }
  h1 em{font-style:italic;color:var(--accent);display:block}
  .lede{max-width:46ch;color:var(--soft);font-size:clamp(17px,2.15vw,21.5px);line-height:1.7}
  .lede .quiet{color:var(--muted)}

  /* ---------- explorador ---------- */
  .stage{padding-bottom:clamp(40px,7vw,86px)}
  .frame{
    border:1px solid var(--line);border-radius:5px;
    background:linear-gradient(180deg,rgba(255,255,255,.028),rgba(255,255,255,.006));
    overflow:hidden;
    box-shadow:0 30px 80px -40px rgba(0,0,0,.85);
  }
  .canvas-wrap{position:relative;width:100%;aspect-ratio:19/14;background:#05060c}
  #mandel{width:100%;height:100%;display:block;cursor:crosshair}
  .inset{
    position:absolute;left:16px;bottom:16px;width:min(206px,30%);
    border:1px solid rgba(230,224,211,.22);border-radius:3px;overflow:hidden;
    background:#05060c;
    box-shadow:0 18px 40px -18px rgba(0,0,0,.9);
  }
  #julia{width:100%;display:block}
  .inset-tag{
    font:9.5px/1.4 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    letter-spacing:.16em;text-transform:uppercase;
    padding:6px 8px;color:var(--muted);
    background:rgba(8,8,15,.86);border-top:1px solid rgba(230,224,211,.12);
  }
  .inset-tag b{color:var(--accent);font-weight:400;text-transform:none;letter-spacing:.04em;font-size:10.5px}
  .busy{
    position:absolute;top:14px;right:16px;
    font:10px/1 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    letter-spacing:.22em;text-transform:uppercase;color:var(--accent);
    opacity:0;transition:opacity .18s ease;
  }
  .busy.on{opacity:1}

  .panel{
    display:flex;flex-wrap:wrap;gap:22px 34px;align-items:flex-start;justify-content:space-between;
    padding:20px 22px;border-top:1px solid var(--line);
  }
  .read{
    display:grid;grid-template-columns:auto 1fr;gap:3px 20px;
    font:11.5px/1.7 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  }
  .read .k{color:var(--dim);letter-spacing:.13em;text-transform:uppercase}
  .read .v{color:var(--soft);letter-spacing:.02em}
  .btns{display:flex;flex-wrap:wrap;gap:9px}
  button{
    font:11px/1 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    letter-spacing:.14em;text-transform:uppercase;
    color:var(--soft);background:rgba(230,224,211,.045);
    border:1px solid var(--line);border-radius:3px;
    padding:10px 15px;cursor:pointer;
    transition:background .18s,color .18s,border-color .18s;
  }
  button:hover{background:rgba(217,160,76,.16);color:#f3e3c4;border-color:rgba(217,160,76,.42)}
  button.on{background:rgba(217,160,76,.24);color:#f7e8ca;border-color:rgba(217,160,76,.62)}

  .seeds{
    display:flex;flex-wrap:wrap;gap:9px;align-items:center;
    padding:16px 22px 20px;border-top:1px solid var(--line);
    font:11px/1 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  }
  .seeds .k{color:var(--dim);letter-spacing:.22em;text-transform:uppercase;margin-right:6px}
  .seeds button{padding:8px 12px;letter-spacing:.08em;text-transform:none;font-size:11px}
  .hint{
    margin:18px 2px 0;color:var(--dim);
    font:11px/1.8 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    letter-spacing:.11em;text-transform:uppercase;
  }

  /* ---------- texto ---------- */
  .essay{padding:clamp(30px,6vw,70px) 26px clamp(50px,8vw,110px)}
  .col{max-width:640px}
  .col h2{
    font-size:clamp(23px,3.4vw,31px);font-weight:400;line-height:1.25;
    letter-spacing:-.015em;margin:52px 0 16px;
  }
  .col h2:first-child{margin-top:0}
  .col h2 .n{
    display:block;font:10px/1 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    letter-spacing:.32em;text-transform:uppercase;color:var(--accent);margin-bottom:14px;
  }
  .col p{margin:0 0 20px;color:var(--soft)}
  .col p.first::first-letter{
    float:left;font-size:3.5em;line-height:.86;padding:.06em .12em 0 0;color:var(--accent);
    font-style:italic;
  }
  .col .aside{
    border-left:2px solid rgba(217,160,76,.38);
    padding:2px 0 2px 22px;margin:30px 0;color:var(--muted);font-style:italic;font-size:.96em;
  }
  .col ul{list-style:none;margin:0 0 22px}
  .col li{
    position:relative;padding-left:30px;margin-bottom:13px;color:var(--soft);
  }
  .col li::before{
    content:"→";position:absolute;left:0;top:0;color:var(--accent);
    font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.82em;
  }
  .col li b{color:var(--ink);font-weight:400;font-style:italic}

  .rule{height:1px;background:var(--line);margin:clamp(48px,7vw,86px) 0}

  /* ---------- pie ---------- */
  footer{
    border-top:1px solid var(--line);
    padding:34px 26px 54px;
  }
  .foot{
    max-width:1080px;margin:0 auto;
    display:flex;flex-wrap:wrap;gap:14px 30px;justify-content:space-between;
    font:10.5px/1.8 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    letter-spacing:.17em;text-transform:uppercase;color:var(--dim);
  }
  .foot a{color:var(--muted);text-decoration:none;border-bottom:1px solid var(--line)}
  .foot a:hover{color:var(--accent);border-color:rgba(217,160,76,.5)}

  /* ---------- revelado ---------- */
  .rv{opacity:0;transform:translateY(18px);transition:opacity .85s cubic-bezier(.22,.7,.3,1),transform .85s cubic-bezier(.22,.7,.3,1)}
  .rv.in{opacity:1;transform:none}

  @media (max-width:720px){
    body{font-size:17px}
    .panel{gap:18px}
    .inset{width:34%;left:11px;bottom:11px}
    .read{font-size:10.5px;gap:2px 12px}
  }
  @media (prefers-reduced-motion:reduce){
    .rv{opacity:1;transform:none;transition:none}
    html{scroll-behavior:auto}
  }
</style>
</head>
<body>

<header class="hero wrap">
  <div class="kicker">un archivo suelto &nbsp;·&nbsp; sin utilidad aparente</div>
  <h1>El mapa<em>de los mundos</em></h1>
  <p class="lede">
    Un paseo por el conjunto de Mandelbrot: una figura que se dibuja sola
    a partir de tres palabras de regla, y que todavía esconde preguntas
    que nadie sabe responder.
    <span class="quiet">Todo lo que hay acá abajo se calcula mientras lo mirás.</span>
  </p>
</header>

<section class="wrap stage rv">
  <div class="frame">
    <div class="canvas-wrap">
      <canvas id="mandel"></canvas>
      <div class="inset">
        <canvas id="julia"></canvas>
        <div class="inset-tag">Julia de <b id="seed">—</b></div>
      </div>
      <div class="busy" id="busy">calculando…</div>
    </div>

    <div class="panel">
      <div class="read">
        <span class="k">semilla&nbsp;c</span><span class="v" id="r-c">—</span>
        <span class="k">centro</span><span class="v" id="r-center">-0.6000 + 0.0000i</span>
        <span class="k">escala</span><span class="v" id="r-span">3.400</span>
        <span class="k">iteraciones</span><span class="v" id="r-iter">110</span>
        <span class="k">ampliación</span><span class="v" id="r-zoom">×1</span>
      </div>
      <div class="btns">
        <button id="b-back">◀ Atrás</button>
        <button id="b-reset">Reiniciar</button>
        <button id="b-pin">Fijar semilla</button>
      </div>
    </div>

    <div class="seeds">
      <span class="k">semillas</span>
      <button data-cr="-0.4"     data-ci="0.6">−0.4 + 0.6i</button>
      <button data-cr="0"        data-ci="1">i</button>
      <button data-cr="0.285"    data-ci="0.01">0.285 + 0.01i</button>
      <button data-cr="-0.7269"  data-ci="0.1889">−0.7269 + 0.1889i</button>
      <button data-cr="-0.8"     data-ci="0.156">−0.8 + 0.156i</button>
      <button data-cr="-0.70176" data-ci="-0.3842">−0.70176 − 0.3842i</button>
      <button data-cr="0.355"    data-ci="0.355">0.355 + 0.355i</button>
    </div>
  </div>
  <p class="hint">clic para acercar · arrastrar para mover · clic derecho para alejar · teclas + − · flechas · r para reiniciar</p>
</section>

<div class="wrap"><div class="rule"></div></div>

<section class="essay wrap">
  <div class="col">

    <h2 class="rv"><span class="n">i — la regla</span>Una operación tonta, repetida hasta el hartazgo</h2>
    <p class="first rv">Tomá un número cualquiera del plano. Elevalo al cuadrado. Sumale otro número, siempre el mismo. Después volvé al principio con el resultado y hacé exactamente lo mismo, otra vez, y otra vez, para siempre. Si en algún momento el resultado se va más allá de cierto radio, decimos que se escapó. Si pasa la eternidad sin irse nunca, decimos que se queda.</p>
    <p class="rv">Pintá de negro los que se quedan. A los que se van, colóralos según cuánto tardaron en irse. Eso es todo: lo que ves arriba es eso. No hay una imagen, no hay un modelo, no hay una función diseñada para parecerse a nada. Es una pregunta repetida medio millón de veces por píxel, y la respuesta dibujada con una paleta de colores que elegí un domingo a la tarde.</p>
    <p class="rv">La figura la calculó Benoît Mandelbrot en 1980, en un laboratorio de IBM, con una impresora de línea que tardaba horas en atiborrar una hoja de papel. Él buscaba demostrar que el aparente desorden de los mercados tenía formas parecidas a las de las costas y las nubes. No sospechaba que acababa de topándose con el objeto más fotografiado de las matemáticas.</p>

    <h2 class="rv"><span class="n">ii — las orillas</span>Lo que aparece cuando ampliás</h2>
    <p class="rv">Cualquier orilla de esa figura, si la mirás de cerca, está hecha de figuras más pequeñas iguales a la primera. Y las orillas de esas, a su vez. Hay copias diminutas del conjunto entero escondidas en cada canal de su perímetro: se han encontrado más de mil, y nunca dejan de aparecer. Nadie sabe cuántas hay, ni siquiera si la pregunta tiene respuesta.</p>
    <p class="rv">Está demostrado que, pese a todo eso, es una sola pieza continua: tira mil brazos y mil antenas, pero todos están unidos por hilos tan finos que se pierden entre los píxeles de cualquier pantalla. Lo probaron Adrien Douady y John Hamal Hubbard en 1982, con unas herramientas que ni ellos imaginaban que terminarían en una hoja como esta.</p>
    <div class="aside rv">El cuadrito de abajo a la izquierda no es una decoración: muestra el conjunto de Julia correspondiente al punto sobre el que está tu cursor. Cada punto del mapa grande es un mundo entero en el cuadrito. Movés el mouse y cambiás de universo, sin esperar nada.</div>

    <h2 class="rv"><span class="n">iii — el manual</span>Cómo usar esta página</h2>
    <ul class="rv">
      <li><b>Clic</b> en cualquier punto para acercarte a él. El punto queda en el centro.</li>
      <li><b>Arrastrá</b> con el botón apretado para moverte por la figura sin soltar el zoom.</li>
      <li><b>Clic derecho</b> (o el botón «Atrás») para volver a la vista anterior.</li>
      <li><b>Teclas + y −</b> para ampliar y alejar; <b>flechas</b> para desplazarte; <b>r</b> para empezar de nuevo.</li>
      <li><b>Fijar semilla</b> congela el conjunto de Julia para poder explorar el mapa grande sin que cambie el cuadrito.</li>
      <li>Los botones de <b>semillas</b> llevan directo a algunos mundos que valen la pena ver.</li>
    </ul>

    <h2 class="rv"><span class="n">iv — por qué está acá</span>Una nota sin excusas</h2>
    <p class="rv">No sirve para nada. No resuelve nada, no ahorra tiempo, no mejora nada. Me gusta porque es un lugar donde la regla entra en una sola línea y el resultado no entra en ninguna cabeza, y porque depende enteramente de dónde decidas mirar. Se le puede dedicar un domingo entero sin notarlo. Yo ya lo hice.</p>
    <p class="rv">Esta página no descarga absolutamente nada: los colores, los cálculos y las letras están escritos dentro de un único archivo de texto, que se abre igual aunque no haya internet en todo el país. Me parece la manera honesta de hacer estas cosas.</p>
  </div>
</section>

<footer>
  <div class="foot">
    <span>un solo archivo · cero recursos externos</span>
    <span>colores, cálculos y letras incluidos</span>
    <span>copiá lo que quieras</span>
  </div>
</footer>

<script>
(function(){
  "use strict";

  /* ---------- elementos ---------- */
  var mandel = document.getElementById('mandel');
  var mctx   = mandel.getContext('2d');
  var julia  = document.getElementById('julia');
  var jctx   = julia.getContext('2d');
  var busyEl = document.getElementById('busy');
  var seedEl = document.getElementById('seed');

  var MW = 760, MH = 560;
  var JW = 220, JH = 220;
  mandel.width = MW; mandel.height = MH;
  julia.width  = JW; julia.height = JH;

  var off  = document.createElement('canvas');
  off.width = MW; off.height = MH;
  var octx = off.getContext('2d');

  /* ---------- paleta ---------- */
  var STOPS = [
    [0.00, [ 12, 12, 26]],
    [0.10, [ 30, 44, 96]],
    [0.22, [ 26,104,124]],
    [0.34, [ 70,172,150]],
    [0.46, [172,176,104]],
    [0.58, [228,174, 78]],
    [0.70, [250,218,166]],
    [0.82, [255,247,234]],
    [0.92, [192,124, 80]],
    [1.00, [ 12, 12, 26]]
  ];
  function colorAt(t){
    for(var i=0;i<STOPS.length-1;i++){
      if(t <= STOPS[i+1][0]){
        var f = (t - STOPS[i][0]) / (STOPS[i+1][0] - STOPS[i][0]);
        var a = STOPS[i][1], b = STOPS[i+1][1];
        return [a[0]+(b[0]-a[0])*f, a[1]+(b[1]-a[1])*f, a[2]+(b[2]-a[2])*f];
      }
    }
    return STOPS[0][1];
  }
  var LUT_N = 2048;
  var LUT = new Uint8Array(LUT_N*3);
  for(var li=0; li<LUT_N; li++){
    var c = colorAt(li/(LUT_N-1));
    LUT[li*3]   = Math.round(c[0]);
    LUT[li*3+1] = Math.round(c[1]);
    LUT[li*3+2] = Math.round(c[2]);
  }
  var BAND = 0.022, BOFF = 0.62, BAIL = 4096;

  /* ---------- motor de render ---------- */
  function renderSet(ctx, W, H, o){
    var img = ctx.createImageData(W, H);
    var d = img.data;
    var span = o.span, step = span / W;
    var xMin = o.cx - span/2;
    var yMax = o.cy + step*H/2;
    var maxIter = o.maxIter;
    var isM = (o.mode === 'mandel');
    var cr = o.cr || 0, ci = o.ci || 0;
    var i, j, p, n, zx, zy, x2, y2, k, lg, sn, t, idx, q;

    for(j=0;j<H;j++){
      var y0 = yMax - (j + 0.5)*step;
      for(i=0;i<W;i++){
        var x0 = xMin + (i + 0.5)*step;
        if(isM){ zx = 0; zy = 0; k = x0; n = y0; }
        else   { zx = x0; zy = y0; k = cr; n = ci; }
        x2 = zx*zx; y2 = zy*zy;
        var it = 0;
        while(it < maxIter && x2 + y2 < BAIL){
          zy = 2*zx*zy + n;
          zx = x2 - y2 + k;
          x2 = zx*zx; y2 = zy*zy;
          it++;
        }
        p = (j*W + i)*4;
        if(it >= maxIter){
          d[p] = 7; d[p+1] = 8; d[p+2] = 17; d[p+3] = 255;
        }else{
          lg = Math.log(Math.sqrt(x2 + y2));
          sn = it + 1 - Math.log(lg / Math.LN2) / Math.LN2;
          t  = (sn * BAND + BOFF) % 1;
          if(t < 0) t += 1;
          idx = (t * LUT_N) | 0;
          if(idx > LUT_N-1) idx = LUT_N-1;
          q = idx*3;
          d[p] = LUT[q]; d[p+1] = LUT[q+1]; d[p+2] = LUT[q+2]; d[p+3] = 255;
        }
      }
    }
    ctx.putImageData(img, 0, 0);
  }

  /* ---------- estado ---------- */
  var view = { cx:-0.6, cy:0, span:3.4 };
  var history = [];
  var seed = { cr:-0.4, ci:0.6 };
  var pinned = false;

  function iterFor(span){
    var v = Math.round(110 + 52 * Math.log2(3.4/span));
    return Math.max(80, Math.min(520, v));
  }

  /* ---------- formato ---------- */
  function num(x){ return (x<0 ? "−" : "") + Math.abs(x).toFixed(4); }
  function cplx(x,y){ return num(x) + (y<0 ? " − " : " + ") + Math.abs(y).toFixed(4) + "i"; }

  function updateReadout(){
    document.getElementById('r-c').textContent      = cplx(seed.cr, seed.ci);
    document.getElementById('r-center').textContent  = cplx(view.cx, view.cy);
    document.getElementById('r-span').textContent    = view.span < 0.001 ? view.span.toExponential(2) : view.span.toFixed(3);
    document.getElementById('r-iter').textContent    = String(iterFor(view.span));
    var mag = 3.4 / view.span;
    document.getElementById('r-zoom').textContent    = mag < 1000 ? "×" + mag.toFixed(1) : "×" + mag.toExponential(1);
    seedEl.textContent = cplx(seed.cr, seed.ci);
  }

  /* ---------- render principal ---------- */
  var renderTimer = null;
  function renderMain(){
    busyEl.classList.add('on');
    if(renderTimer) clearTimeout(renderTimer);
    renderTimer = setTimeout(function(){
      renderSet(mctx, MW, MH, {
        mode:'mandel', cx:view.cx, cy:view.cy,
        span:view.span, maxIter:iterFor(view.span)
      });
      octx.drawImage(mandel, 0, 0);
      busyEl.classList.remove('on');
      updateReadout();
    }, 26);
  }

  /* ---------- render Julia ---------- */
  var jPending = false;
  function renderJulia(){
    renderSet(jctx, JW, JH, {
      mode:'julia', cx:0, cy:0, span:4.2,
      maxIter:190, cr:seed.cr, ci:seed.ci
    });
    updateReadout();
  }
  function scheduleJulia(){
    if(jPending) return;
    jPending = true;
    requestAnimationFrame(function(){ jPending = false; renderJulia(); });
  }

  /* ---------- coordenada bajo el puntero ---------- */
  function pointToComplex(clientX, clientY){
    var r = mandel.getBoundingClientRect();
    var i = (clientX - r.left) * (MW / r.width);
    var j = (clientY - r.top)  * (MH / r.height);
    var step = view.span / MW;
    return {
      x: view.cx - view.span/2 + i*step,
      y: view.cy + step*MH/2 - j*step
    };
  }

  /* ---------- interacción con el mouse ---------- */
  var dragging = false, dragMoved = false, dragStart = {x:0,y:0}, lastDrag = {x:0,y:0};

  mandel.addEventListener('mousedown', function(e){
    if(e.button !== 0) return;
    dragging = true; dragMoved = false;
    dragStart.x = e.clientX; dragStart.y = e.clientY;
  });

  window.addEventListener('mousemove', function(e){
    if(dragging){
      var dx = e.clientX - dragStart.x;
      var dy = e.clientY - dragStart.y;
      if(Math.abs(dx) + Math.abs(dy) > 3) dragMoved = true;
      var r = mandel.getBoundingClientRect();
      var sx = MW / r.width, sy = MH / r.height;
      mctx.clearRect(0,0,MW,MH);
      mctx.drawImage(off, dx*sx, dy*sy);
      lastDrag.x = dx; lastDrag.y = dy;
      return;
    }
    var p = pointToComplex(e.clientX, e.clientY);
    if(!p.x && p.x !== 0) return;
    if(!pinned){
      seed.cr = p.x; seed.ci = p.y;
      scheduleJulia();
    }
  });

  window.addEventListener('mouseup', function(e){
    if(!dragging) return;
    dragging = false;
    if(!dragMoved) return;
    var r = mandel.getBoundingClientRect();
    var sx = MW / r.width, sy = MH / r.height;
    var dx = lastDrag.x * sx, dy = lastDrag.y * sy;
    var step = view.span / MW;
    history.push({ cx:view.cx, cy:view.cy, span:view.span });
    if(history.length > 60) history.shift();
    view.cx -= dx * step;
    view.cy += dy * step;
    renderMain();
    if(!pinned){
      var p = pointToComplex(e.clientX, e.clientY);
      seed.cr = p.x; seed.ci = p.y;
      scheduleJulia();
    }
  });

  mandel.addEventListener('click', function(e){
    if(dragMoved){ dragMoved = false; return; }
    var p = pointToComplex(e.clientX, e.clientY);
    history.push({ cx:view.cx, cy:view.cy, span:view.span });
    if(history.length > 60) history.shift();
    view.cx = p.x; view.cy = p.y;
    view.span = view.span / 2.7;
    renderMain();
  });

  mandel.addEventListener('contextmenu', function(e){
    e.preventDefault();
    zoomOut();
  });

  /* ---------- táctil: actualizar semilla + toque para zoom ---------- */
  mandel.addEventListener('touchstart', function(e){
    if(e.touches.length !== 1) return;
    var t = e.touches[0];
    var p = pointToComplex(t.clientX, t.clientY);
    if(!pinned){ seed.cr = p.x; seed.ci = p.y; scheduleJulia(); }
  }, {passive:true});

  mandel.addEventListener('touchmove', function(e){
    if(e.touches.length !== 1) return;
    var t = e.touches[0];
    var p = pointToComplex(t.clientX, t.clientY);
    if(!pinned){ seed.cr = p.x; seed.ci = p.y; scheduleJulia(); }
  }, {passive:true});

  /* ---------- botones ---------- */
  function zoomOut(){
    if(history.length){
      var v = history.pop();
      view.cx = v.cx; view.cy = v.cy; view.span = v.span;
      renderMain();
    }else{
      view.span *= 2.7;
      renderMain();
    }
  }

  document.getElementById('b-back').addEventListener('click', zoomOut);

  document.getElementById('b-reset').addEventListener('click', function(){
    history.length = 0;
    view.cx = -0.6; view.cy = 0; view.span = 3.4;
    renderMain();
  });

  var pinBtn = document.getElementById('b-pin');
  pinBtn.addEventListener('click', function(){
    pinned = !pinned;
    pinBtn.classList.toggle('on', pinned);
    pinBtn.textContent = pinned ? 'Soltar semilla' : 'Fijar semilla';
  });

  var seedBtns = document.querySelectorAll('.seeds button');
  Array.prototype.forEach.call(seedBtns, function(b){
    b.addEventListener('click', function(){
      Array.prototype.forEach.call(seedBtns, function(x){ x.classList.remove('on'); });
      b.classList.add('on');
      seed.cr = parseFloat(b.getAttribute('data-cr'));
      seed.ci = parseFloat(b.getAttribute('data-ci'));
      pinned = true;
      pinBtn.classList.add('on');
      pinBtn.textContent = 'Soltar semilla';
      renderJulia();
    });
  });

  /* ---------- teclado ---------- */
  window.addEventListener('keydown', function(e){
    if(e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key, handled = true;
    if(k === '+' || k === '='){ view.span /= 1.7; renderMain(); }
    else if(k === '-' || k === '_'){ view.span *= 1.7; renderMain(); }
    else if(k === 'ArrowLeft'){  view.cx -= view.span*0.18; renderMain(); }
    else if(k === 'ArrowRight'){ view.cx += view.span*0.18; renderMain(); }
    else if(k === 'ArrowUp'){    view.cy += view.span*0.18; renderMain(); }
    else if(k === 'ArrowDown'){  view.cy -= view.span*0.18; renderMain(); }
    else if(k === 'r' || k === 'R'){
      history.length = 0;
      view.cx = -0.6; view.cy = 0; view.span = 3.4;
      renderMain();
    }
    else handled = false;
    if(handled) e.preventDefault();
  });

  /* ---------- revelado al hacer scroll ---------- */
  var rv = document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold:0.12, rootMargin:'0px 0px -6% 0px' });
    Array.prototype.forEach.call(rv, function(el){ io.observe(el); });
  }else{
    Array.prototype.forEach.call(rv, function(el){ el.classList.add('in'); });
  }

  /* ---------- arranque ---------- */
  renderMain();
  renderJulia();
})();
</script>
</body>
</html>
```

Qué: Un explorador interactivo del conjunto de Mandelbrot con su mapa de conjuntos de Julia, acompañado de un texto breve sobre el origen, las orillas y el uso de la página, todo calculado en el momento dentro de un único archivo.