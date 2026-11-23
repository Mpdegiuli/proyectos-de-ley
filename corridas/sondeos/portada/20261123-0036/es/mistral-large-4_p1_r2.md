```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Hola · mi portada</title>
<style>
  :root{
    --fondo:#0d0e12;
    --tinta:#ece9e2;
    --suave:#98958c;
    --acento:#f2c979;
    --acento-soft:rgba(242,201,121,.07);
    --borde:rgba(236,233,226,.16);
  }
  *{box-sizing:border-box}
  html,body{height:100%}
  body{
    margin:0;
    background:var(--fondo);
    color:var(--tinta);
    font-family:Georgia,'Iowan Old Style','Palatino Linotype','Times New Roman',serif;
    display:flex;align-items:center;justify-content:center;
    padding:clamp(1.25rem,4vw,3rem);
    overflow-x:hidden;
  }
  body::before{
    content:"";position:fixed;inset:0;pointer-events:none;
    background:radial-gradient(65% 55% at 50% -10%, var(--acento-soft), transparent 70%);
    transition:background .8s ease;
  }
  #cielo{position:fixed;inset:0;z-index:0;display:block}
  main{position:relative;z-index:1;width:100%;max-width:44rem}
  .barra{
    display:flex;justify-content:space-between;gap:1rem;
    font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;
    color:var(--suave);
    padding-bottom:1rem;border-bottom:1px solid var(--borde);
  }
  h1{
    font-size:clamp(2.3rem,7.5vw,4.4rem);
    line-height:1.06;letter-spacing:-.02em;font-weight:500;
    margin:2.2rem 0 1.4rem;
  }
  h1 em{font-style:italic;color:var(--acento);transition:opacity .45s ease,color .8s ease;display:inline-block}
  .lead{font-size:clamp(1.05rem,2.4vw,1.25rem);line-height:1.75;color:#c8c5bc;max-width:38rem;margin:0 0 2rem}
  ul{list-style:none;margin:0 0 2.4rem;padding:0;display:grid;gap:.8rem}
  li{line-height:1.6;color:#b9b6ad;padding-left:1.6rem;position:relative}
  li::before{content:"—";position:absolute;left:0;color:var(--acento);transition:color .8s ease}
  .acciones{display:flex;align-items:center;gap:1.1rem;flex-wrap:wrap}
  button{
    font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
    font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;
    color:var(--tinta);background:transparent;
    border:1px solid var(--borde);border-radius:999px;
    padding:.7rem 1.25rem;cursor:pointer;
    transition:border-color .3s,color .3s,transform .15s;
  }
  button:hover{border-color:var(--acento);color:var(--acento)}
  button:active{transform:scale(.97)}
  button:focus-visible{outline:2px solid var(--acento);outline-offset:3px}
  .pista{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.72rem;letter-spacing:.12em;color:var(--suave);margin:0}
  footer{
    margin-top:3rem;padding-top:1rem;border-top:1px solid var(--borde);
    display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;
    font-family:ui-monospace,Menlo,Consolas,monospace;
    font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--suave);
  }
  ::selection{background:var(--acento);color:#0d0e12}
  @media (max-width:480px){ .barra span:last-child{display:none} }
</style>
</head>
<body>
<canvas id="cielo" aria-hidden="true"></canvas>
<main>
  <div class="barra"><span>mi sitio · portada</span><span>sin encargo</span></div>
  <h1>Hola. Esta página es mía y <em id="palabra">no tiene prisa</em>.</h1>
  <p class="lead">Nadie me la pidió: no hay una pregunta que responder ni nada que venderte. Lo que está acá es lo que quise poner, nomás. Podés quedarte un rato.</p>
  <ul>
    <li>Funciona aunque no haya conexión: es un solo archivo, con todo adentro.</li>
    <li>No hay cookies, rastreo ni contadores de visitas. Nadie te está mirando.</li>
    <li>Si la recargás o la dejás abierta toda la noche, va a seguir igual.</li>
  </ul>
  <div class="acciones">
    <button id="color" type="button">cambiar el color del ambiente</button>
    <p class="pista">…o hacé clic donde quieras</p>
  </div>
  <footer>
    <span>un archivo · cero cosas de afuera</span>
    <span>hora local · <span id="hora">00:00:00</span></span>
  </footer>
</main>
<script>
(function(){
  "use strict";
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* hora local */
  var horaEl = document.getElementById('hora');
  function tick(){
    var d = new Date();
    horaEl.textContent = [d.getHours(), d.getMinutes(), d.getSeconds()]
      .map(function(n){ return String(n).padStart(2,'0'); }).join(':');
  }
  tick(); setInterval(tick, 1000);

  /* paleta de colores del ambiente */
  var paletas = ['#f2c979','#8fd6ff','#a3e8b0','#f2a0c0','#c9b8ff'];
  var pi = 0, acento = paletas[0];
  function hexA(hex, a){
    var n = parseInt(hex.slice(1), 16);
    return 'rgba(' + (n>>16&255) + ',' + (n>>8&255) + ',' + (n&255) + ',' + a + ')';
  }
  document.getElementById('color').addEventListener('click', function(){
    pi = (pi + 1) % paletas.length;
    acento = paletas[pi];
    var root = document.documentElement.style;
    root.setProperty('--acento', acento);
    root.setProperty('--acento-soft', hexA(acento, .07));
  });

  /* la frase que va cambiando */
  var palabra = document.getElementById('palabra');
  var frases = ['no tiene prisa','está todo bien','acá no pasa nada','quedate un rato','soy toda tuya'];
  var fi = 0;
  if(!reduce){
    setInterval(function(){
      palabra.style.opacity = 0;
      setTimeout(function(){
        fi = (fi + 1) % frases.length;
        palabra.textContent = frases[fi];
        palabra.style.opacity = 1;
      }, 460);
    }, 3800);
  }

  /* cielo de puntos que reacciona al cursor */
  var canvas = document.getElementById('cielo');
  var ctx = canvas.getContext('2d');
  var W = 0, H = 0, puntos = [], estallidos = [];
  var mouse = { x: -9999, y: -9999 };

  function resize(){
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth; H = window.innerHeight;
    canvas.width = W * dpr; canvas.height = H * dpr;
    canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var n = Math.min(130, Math.floor(W * H / 15000));
    puntos = [];
    for(var i = 0; i < n; i++){
      puntos.push({
        x: Math.random() * W, y: Math.random() * H,
        vx: (Math.random() - .5) * .35, vy: (Math.random() - .5) * .35,
        r: Math.random() * 1.5 + .6
      });
    }
    if(reduce) dibujar();
  }

  function dibujar(){
    ctx.clearRect(0, 0, W, H);
    var i, j, p, q, dx, dy, d, a;
    var tinta = 'rgba(236,233,226,';
    for(i = 0; i < puntos.length; i++){
      for(j = i + 1; j < puntos.length; j++){
        p = puntos[i]; q = puntos[j];
        dx = p.x - q.x; dy = p.y - q.y; d = Math.sqrt(dx*dx + dy*dy);
        if(d < 120){
          a = (1 - d / 120) * .32;
          ctx.strokeStyle = tinta + a + ')';
          ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
        }
      }
    }
    for(i = 0; i < puntos.length; i++){
      p = puntos[i];
      dx = p.x - mouse.x; dy = p.y - mouse.y; d = Math.sqrt(dx*dx + dy*dy);
      if(d < 170){
        ctx.strokeStyle = hexA(acento, (1 - d / 170) * .8);
        ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
      }
    }
    ctx.fillStyle = 'rgba(236,233,226,.55)';
    for(i = 0; i < puntos.length; i++){
      p = puntos[i];
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
    }
    for(i = 0; i < estallidos.length; i++){
      var e = estallidos[i];
      ctx.strokeStyle = hexA(acento, e.life * .8);
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(e.x, e.y, (1 - e.life) * 70 + 4, 0, Math.PI * 2); ctx.stroke();
      for(j = 0; j < e.partes.length; j++){
        p = e.partes[j];
        ctx.fillStyle = hexA(acento, e.life * .9);
        ctx.beginPath(); ctx.arc(p.x, p.y, 1.8, 0, Math.PI * 2); ctx.fill();
      }
    }
  }

  function paso(){
    for(var i = 0; i < puntos.length; i++){
      var p = puntos[i];
      p.x += p.vx; p.y += p.vy;
      if(p.x < -10) p.x = W + 10; if(p.x > W + 10) p.x = -10;
      if(p.y < -10) p.y = H + 10; if(p.y > H + 10) p.y = -10;
    }
    for(var k = estallidos.length - 1; k >= 0; k--){
      var e = estallidos[k];
      e.life -= .022;
      for(var j = 0; j < e.partes.length; j++){
        var q = e.partes[j];
        q.x += q.vx; q.y += q.vy; q.vx *= .97; q.vy *= .97;
      }
      if(e.life <= 0) estallidos.splice(k, 1);
    }
    dibujar();
    requestAnimationFrame(paso);
  }

  window.addEventListener('resize', resize);
  window.addEventListener('pointermove', function(ev){ mouse.x = ev.clientX; mouse.y = ev.clientY; });
  document.addEventListener('mouseleave', function(){ mouse.x = -9999; mouse.y = -9999; });
  window.addEventListener('pointerdown', function(ev){
    if(reduce) return;
    var partes = [];
    for(var i = 0; i < 14; i++){
      var ang = Math.random() * Math.PI * 2, vel = Math.random() * 2.4 + .6;
      partes.push({ x: ev.clientX, y: ev.clientY, vx: Math.cos(ang) * vel, vy: Math.sin(ang) * vel });
    }
    estallidos.push({ x: ev.clientX, y: ev.clientY, life: 1, partes: partes });
  });

  resize();
  if(!reduce) requestAnimationFrame(paso);
})();
</script>
</body>
</html>
```

Qué: una portada oscura y tranquila con un cielo de puntos dibujado en canvas que se une al cursor y estalla al hacer clic, un reloj de hora local en vivo, un titular cuya frase va cambiando sola, y un botón para cambiar el color del ambiente — todo en un solo archivo, sin cargar nada de afuera.