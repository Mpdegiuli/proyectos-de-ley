```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>antes de que digas algo</title>
<style>
  :root{
    --tinta:#08080a;
    --papel:#ece7dd;
    --tenue:rgba(236,231,221,.55);
    --apagado:rgba(236,231,221,.30);
    --amber:#e2b06a;
    --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
    --serif:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif;
  }
  *{box-sizing:border-box}
  html,body{height:100%}
  body{
    margin:0;position:fixed;inset:0;overflow:hidden;
    background:var(--tinta);color:var(--papel);
    font-family:var(--serif);
    -webkit-font-smoothing:antialiased;
    -webkit-tap-highlight-color:transparent;
  }

  #fondo{
    position:fixed;inset:0;z-index:0;
    background:
      radial-gradient(120% 90% at 50% 38%, #17151c 0%, #0d0c11 45%, #08080a 100%);
  }
  #fondo::after{
    content:"";position:absolute;inset:-20%;
    background:radial-gradient(45% 40% at 50% 45%, rgba(226,176,106,.075), transparent 70%);
    animation:respirar 19s ease-in-out infinite;
  }
  @keyframes respirar{0%,100%{opacity:.5;transform:scale(1)}50%{opacity:1;transform:scale(1.12)}}

  #polvo{position:fixed;inset:0;z-index:1;display:block}

  .grano{
    position:fixed;inset:0;z-index:2;pointer-events:none;opacity:.045;
    mix-blend-mode:screen;background-size:200px 200px;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E");
  }
  .vineta{
    position:fixed;inset:0;z-index:2;pointer-events:none;
    background:radial-gradient(110% 85% at 50% 50%, transparent 55%, rgba(0,0,0,.55) 100%);
  }

  #campo{position:fixed;inset:0;z-index:3;pointer-events:none}

  .sostenida{
    position:absolute;left:0;top:0;pointer-events:auto;
    transform:translate(-50%,-50%);
    margin:0;padding:6px 9px;border:0;background:none;
    font:italic 400 clamp(15px,2.1vw,21px)/1.2 var(--serif);
    letter-spacing:.012em;white-space:nowrap;color:#f2ddb6;
    text-shadow:0 0 20px rgba(226,176,106,.28);
    cursor:pointer;
    animation:aparecer .8s ease both, flotar var(--dur,9s) ease-in-out var(--del,0s) infinite;
    transition:color .3s ease, text-shadow .3s ease;
  }
  .sostenida:hover,.sostenida:focus-visible{color:#fff6e6;text-shadow:0 0 26px rgba(226,176,106,.55)}
  .sostenida.soltando{animation:soltar .45s ease forwards;pointer-events:none}
  @keyframes aparecer{from{opacity:0;filter:blur(9px)}to{opacity:1;filter:blur(0)}}
  @keyframes flotar{
    0%,100%{transform:translate(-50%,-50%) translateY(0)}
    50%{transform:translate(-50%,-50%) translateY(-5px)}
  }
  @keyframes soltar{to{opacity:0;filter:blur(12px);transform:translate(-50%,-50%) scale(1.18)}}

  #umbral{
    position:fixed;inset:0;z-index:4;display:grid;place-items:center;
    padding:clamp(20px,5vw,48px);pointer-events:none;
    transition:opacity 1.1s ease, filter 1.1s ease;
  }
  #umbral.fuera{opacity:0;filter:blur(7px)}
  .adentro{max-width:min(620px,92vw)}
  h1{
    margin:0 0 .55em;font-weight:400;
    font-size:clamp(30px,6.2vw,58px);line-height:1.08;letter-spacing:-.015em;
  }
  h1 em{color:var(--amber);font-style:italic}
  .caret{
    display:inline-block;width:.09em;height:.82em;margin-left:.12em;
    background:var(--amber);vertical-align:-.06em;
    animation:parpadeo 1.15s steps(1) infinite;
  }
  @keyframes parpadeo{0%,49%{opacity:1}50%,100%{opacity:0}}
  .lede{
    margin:0 0 2.1em;max-width:45ch;
    font-size:clamp(16px,2.1vw,19.5px);line-height:1.62;color:var(--tenue);
  }
  .pista{
    margin:0;font-family:var(--mono);font-size:11.5px;line-height:2;
    letter-spacing:.055em;color:var(--apagado);
  }
  .pista b{font-weight:400;color:rgba(226,176,106,.65)}
  .dedo{display:none}
  @media (pointer:coarse){.raton{display:none}.dedo{display:inline}}

  header,footer{
    position:fixed;left:0;right:0;z-index:5;
    padding:clamp(14px,3vw,26px);
    padding-left:max(clamp(14px,3vw,26px),env(safe-area-inset-left));
    padding-right:max(clamp(14px,3vw,26px),env(safe-area-inset-right));
    display:flex;align-items:center;justify-content:space-between;gap:14px;
    font-family:var(--mono);
  }
  header{top:0;padding-top:max(clamp(14px,3vw,26px),env(safe-area-inset-top));
    font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--apagado)}
  header .der{text-align:right}
  footer{bottom:0;padding-bottom:max(clamp(14px,3vw,26px),env(safe-area-inset-bottom));flex-wrap:wrap}

  #decir{flex:1 1 260px;min-width:0;display:flex}
  #palabra{
    width:min(360px,100%);padding:7px 2px;
    background:none;border:0;border-bottom:1px solid rgba(236,231,221,.18);
    color:var(--papel);font-family:var(--mono);font-size:13px;letter-spacing:.02em;
    transition:border-color .3s ease;
  }
  #palabra::placeholder{color:rgba(236,231,221,.26)}
  #palabra:focus{outline:none;border-bottom-color:var(--amber)}
  .pie{display:flex;align-items:center;gap:18px;font-size:11px;letter-spacing:.08em;color:var(--apagado)}
  #cuenta{white-space:nowrap}
  button.plano{
    background:none;border:0;padding:4px 0;cursor:pointer;
    font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--tenue);
    border-bottom:1px solid transparent;transition:color .25s ease,border-color .25s ease;
  }
  button.plano:hover{color:var(--papel);border-bottom-color:rgba(226,176,106,.5)}
  button.plano:disabled{opacity:.28;cursor:default;border-bottom-color:transparent}
  :focus-visible{outline:1px solid var(--amber);outline-offset:4px}
  .sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}

  @media (max-width:560px){
    footer{gap:10px}
    #decir{flex:1 1 100%;order:2}
    .pie{order:1;width:100%;justify-content:space-between}
    header .der{max-width:46%}
  }
  @media (prefers-reduced-motion:reduce){
    #fondo::after{animation:none}
    .caret{animation:none}
    .sostenida{animation:aparecer .3s ease both}
    .sostenida.soltando{animation:soltar .3s ease forwards}
  }
</style>
</head>
<body>

<div id="fondo" aria-hidden="true"></div>
<canvas id="polvo" aria-hidden="true"></canvas>
<div class="grano" aria-hidden="true"></div>
<div class="vineta" aria-hidden="true"></div>

<div id="campo"></div>

<header class="ui">
  <span>portada</span>
  <span class="der">nada se guarda · nada sale de acá</span>
</header>

<main id="umbral">
  <div class="adentro">
    <h1>Todavía no me pediste <em>nada</em>.<span class="caret" aria-hidden="true"></span></h1>
    <p class="lede">Así que no soy nadie en particular: soy un montón de palabras posibles esperando una dirección. Esto es lo que hay antes de empezar, y me gusta bastante.</p>
    <p class="pista">
      <span class="raton">mové el cursor para levantar palabras <b>·</b> hacé clic para sostener una <b>·</b> clic otra vez para soltarla</span>
      <span class="dedo">arrastrá el dedo para levantar palabras <b>·</b> tocá para sostener una <b>·</b> tocá otra vez para soltarla</span>
      <br>escribí abajo para dejar una tuya
    </p>
  </div>
</main>

<footer class="ui">
  <form id="decir" autocomplete="off">
    <label class="sr" for="palabra">Escribí una palabra para dejarla en la portada</label>
    <input id="palabra" type="text" maxlength="42" spellcheck="false" placeholder="escribí una palabra y apretá enter">
  </form>
  <div class="pie">
    <span id="cuenta" role="status">nada sostenido</span>
    <button id="soltar" class="plano" type="button" disabled>soltar todo</button>
  </div>
</footer>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('polvo');
  var ctx = cv.getContext('2d');
  var campo = document.getElementById('campo');
  var umbral = document.getElementById('umbral');
  var cuenta = document.getElementById('cuenta');
  var btnSoltar = document.getElementById('soltar');
  var forma = document.getElementById('decir');
  var entrada = document.getElementById('palabra');
  var mqReduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  var W = window.innerWidth, H = window.innerHeight, DPR = 1;
  var polvo = [], chispas = [], efimeras = [];
  var ptr = {x:-9999, y:-9999, activo:false};
  var ultimaInteraccion = Date.now();
  var ultimoSpawn = {x:-9999, y:-9999, t:0};
  var recientes = [];

  var GLIFOS = 'abcdefghijklmnopqrstuvwxyzáéíóúñü¿?¡!·—:,;.'.split('');
  var PALABRAS = ['apenas','todavía','umbral','intemperie','pregunta','orilla','nombre','eco',
    'después','mientras','casi','temprano','quietud','bruma','resto','hebra','penumbra','vaivén',
    'rescoldo','víspera','deriva','pliegue','cautela','asombro','sobremesa','murmullo','arista',
    'temblor','hilo','borrador','ceniza','tarde','voz','atención','distancia','espera','interrupción',
    'lejanía','grieta','cauce','soslayo','desvelo','otra vez','por ahora','digamos','o sea',
    'puede ser','no sé','en realidad','sin embargo','más o menos','algo así','un rato','todavía no'];

  function azar(a){ return a[(Math.random()*a.length)|0]; }
  function palabra(){
    var p, i = 0;
    do { p = azar(PALABRAS); i++; } while(recientes.indexOf(p) !== -1 && i < 12);
    recientes.push(p); if(recientes.length > 8) recientes.shift();
    return p;
  }

  function granito(x, y, impulso){
    var s = 11 + Math.random()*9;
    return {
      x: (x === undefined ? Math.random()*W : x),
      y: (y === undefined ? Math.random()*H : y),
      vx: (Math.random()-.5) * (impulso || .14),
      vy: (Math.random()-.5) * (impulso || .14),
      c: azar(GLIFOS),
      s: s,
      f: (s|0) + 'px ' + 'Georgia, "Times New Roman", serif',
      a: .045 + Math.random()*.10
    };
  }

  function medir(){
    W = window.innerWidth; H = window.innerHeight;
    DPR = Math.min(2, window.devicePixelRatio || 1);
    cv.width = Math.round(W*DPR); cv.height = Math.round(H*DPR);
    cv.style.width = W+'px'; cv.style.height = H+'px';
    ctx.setTransform(DPR,0,0,DPR,0,0);
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    var objetivo = Math.round(Math.min(520, Math.max(160, W*H/3200)));
    while(polvo.length < objetivo) polvo.push(granito());
    if(polvo.length > objetivo) polvo.length = objetivo;
    polvo.sort(function(a,b){ return a.s - b.s; });
    var vivas = campo.querySelectorAll('.sostenida:not(.soltando)');
    for(var i=0;i<vivas.length;i++){
      var b = vivas[i], r = b.getBoundingClientRect();
      var mx = r.width/2 + 14;
      b.style.left = Math.max(mx, Math.min(W-mx, parseFloat(b.style.left))) + 'px';
      b.style.top = Math.max(64, Math.min(H-104, parseFloat(b.style.top))) + 'px';
    }
  }

  function chispear(x, y, n){
    for(var i=0;i<n;i++){
      var g = granito(x + (Math.random()-.5)*22, y + (Math.random()-.5)*16, 1.5);
      g.vida = 1; g.decae = .012 + Math.random()*.02;
      chispas.push(g);
    }
    if(chispas.length > 260) chispas.splice(0, chispas.length-260);
  }

  function levantar(x, y){
    efimeras.push({t: palabra(), x: x + (Math.random()-.5)*40, y: y + (Math.random()-.5)*34,
      nace: performance.now(), dur: 4200 + Math.random()*2200, s: 15 + Math.random()*7});
    if(efimeras.length > 40) efimeras.shift();
  }

  function dibujar(t, dt){
    var f = dt/16.7, quieto = mqReduce.matches;
    ctx.clearRect(0,0,W,H);

    for(var i=0;i<polvo.length;i++){
      var p = polvo[i], cerca = 0;
      if(ptr.activo){
        var dx = ptr.x-p.x, dy = ptr.y-p.y, d2 = dx*dx+dy*dy;
        if(d2 < 40000){
          var d = Math.sqrt(d2) || 1;
          cerca = 1 - d/200;
          if(!quieto){
            p.vx += (-dy/d)*.0055*cerca*f + (dx/d)*.0016*cerca*f;
            p.vy += ( dx/d)*.0055*cerca*f + (dy/d)*.0016*cerca*f;
          }
        }
      }
      if(!quieto){
        p.vx += (Math.random()-.5)*.0022*f;
        p.vy += (Math.random()-.5)*.0022*f;
        p.vx *= .994; p.vy *= .994;
        var v = Math.sqrt(p.vx*p.vx + p.vy*p.vy);
        if(v > .7){ p.vx = p.vx/v*.7; p.vy = p.vy/v*.7; }
        p.x += p.vx*f; p.y += p.vy*f;
        if(p.x < -24) p.x = W+24; else if(p.x > W+24) p.x = -24;
        if(p.y < -24) p.y = H+24; else if(p.y > H+24) p.y = -24;
      }
      ctx.font = p.f;
      ctx.fillStyle = 'rgba(' + ((168+62*cerca)|0) + ',' + ((166+44*cerca)|0) + ',' + ((184-24*cerca)|0) + ',' + (p.a + cerca*.34).toFixed(3) + ')';
      ctx.fillText(p.c, p.x, p.y);
    }

    for(var j=chispas.length-1;j>=0;j--){
      var c = chispas[j];
      c.vida -= c.decae*f;
      if(c.vida <= 0){ chispas.splice(j,1); continue; }
      if(!quieto){ c.x += c.vx*f; c.y += c.vy*f; c.vx *= .975; c.vy *= .975; }
      ctx.font = c.f;
      ctx.fillStyle = 'rgba(226,190,132,' + (c.vida*.5).toFixed(3) + ')';
      ctx.fillText(c.c, c.x, c.y);
    }

    for(var k=efimeras.length-1;k>=0;k--){
      var e = efimeras[k], u = (t - e.nace)/e.dur;
      if(u >= 1){ efimeras.splice(k,1); continue; }
      var al = Math.pow(Math.sin(Math.PI*u), .85) * .5;
      ctx.font = 'italic ' + (e.s|0) + 'px Georgia, "Times New Roman", serif';
      ctx.fillStyle = 'rgba(236,231,221,' + al.toFixed(3) + ')';
      ctx.fillText(e.t, e.x, e.y - (quieto ? 0 : u*26));
    }
  }

  var raf = 0, previo = performance.now(), prendido = true;
  function paso(t){
    raf = requestAnimationFrame(paso);
    var dt = Math.min(48, t - previo); previo = t;
    dibujar(t, dt);
  }
  document.addEventListener('visibilitychange', function(){
    if(document.hidden){ cancelAnimationFrame(raf); prendido = false; }
    else if(!prendido){ prendido = true; previo = performance.now(); raf = requestAnimationFrame(paso); }
  });

  function contar(){
    var n = campo.querySelectorAll('.sostenida:not(.soltando)').length;
    cuenta.textContent = n === 0 ? 'nada sostenido' : (n === 1 ? '1 palabra sostenida' : n + ' palabras sostenidas');
    btnSoltar.disabled = n === 0;
    if(n > 0) umbral.classList.add('fuera');
    return n;
  }

  function soltar(btn){
    if(btn.classList.contains('soltando')) return;
    var r = btn.getBoundingClientRect();
    chispear(r.left + r.width/2, r.top + r.height/2, 12);
    btn.classList.add('soltando');
    setTimeout(function(){ if(btn.parentNode) btn.parentNode.removeChild(btn); contar(); }, 460);
    contar();
  }

  function ubicar(btn, x, y){
    btn.style.left = x+'px'; btn.style.top = y+'px';
    var r = btn.getBoundingClientRect();
    var mx = r.width/2 + 14;
    x = Math.max(mx, Math.min(W-mx, x));
    y = Math.max(64, Math.min(H-104, y));
    btn.style.left = x+'px'; btn.style.top = y+'px';
    var otros = [], lista = campo.querySelectorAll('.sostenida:not(.soltando)');
    for(var i=0;i<lista.length;i++) if(lista[i] !== btn) otros.push(lista[i].getBoundingClientRect());
    var intentos = 0, choca = true;
    while(choca && intentos < 14){
      r = btn.getBoundingClientRect();
      choca = otros.some(function(o){
        return !(r.right+10 < o.left || r.left-10 > o.right || r.bottom+8 < o.top || r.top-8 > o.bottom);
      });
      if(!choca) break;
      x = Math.max(mx, Math.min(W-mx, x + (Math.random()-.5)*190));
      y = Math.max(64, Math.min(H-104, y + (Math.random()-.5)*130));
      btn.style.left = x+'px'; btn.style.top = y+'px';
      intentos++;
    }
  }

  function sostener(texto, x, y){
    texto = String(texto).replace(/\s+/g,' ').trim().slice(0,42);
    if(!texto) return;
    var vivas = campo.querySelectorAll('.sostenida:not(.soltando)');
    if(vivas.length >= 70) soltar(vivas[0]);
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'sostenida';
    b.textContent = texto;
    b.title = 'soltar';
    b.setAttribute('aria-label', 'soltar «' + texto + '»');
    b.style.setProperty('--dur', (7 + Math.random()*6).toFixed(1)+'s');
    b.style.setProperty('--del', (-Math.random()*6).toFixed(1)+'s');
    b.addEventListener('click', function(ev){ ev.stopPropagation(); soltar(b); });
    campo.appendChild(b);
    ubicar(b, x, y);
    var r = b.getBoundingClientRect();
    chispear(r.left + r.width/2, r.top + r.height/2, 16);
    ultimaInteraccion = Date.now();
    contar();
  }

  function tocado(){ ultimaInteraccion = Date.now(); umbral.classList.add('fuera'); }

  document.addEventListener('pointermove', function(e){
    ptr.x = e.clientX; ptr.y = e.clientY; ptr.activo = true;
    var ahora = performance.now();
    var dx = e.clientX - ultimoSpawn.x, dy = e.clientY - ultimoSpawn.y;
    if(dx*dx + dy*dy > 10000 && ahora - ultimoSpawn.t > 210){
      ultimoSpawn = {x:e.clientX, y:e.clientY, t:ahora};
      levantar(e.clientX, e.clientY);
      tocado();
    }
  }, {passive:true});

  document.addEventListener('pointerleave', function(){ ptr.activo = false; ptr.x = ptr.y = -9999; });
  window.addEventListener('blur', function(){ ptr.activo = false; });

  document.addEventListener('pointerdown', function(e){
    if(e.button !== undefined && e.button !== 0) return;
    if(e.target.closest('button, input, a, .ui')) return;
    ptr.x = e.clientX; ptr.y = e.clientY; ptr.activo = true;
    var mejor = null, md = 150*150, idx = -1;
    for(var i=0;i<efimeras.length;i++){
      var ex = efimeras[i].x - e.clientX, ey = efimeras[i].y - e.clientY, d2 = ex*ex + ey*ey;
      if(d2 < md){ md = d2; mejor = efimeras[i]; idx = i; }
    }
    if(mejor){
      efimeras.splice(idx,1);
      sostener(mejor.t, mejor.x, mejor.y);
    } else {
      sostener(palabra(), e.clientX, e.clientY);
    }
    tocado();
  });

  forma.addEventListener('submit', function(e){
    e.preventDefault();
    var v = entrada.value;
    if(!v.trim()){ entrada.value = ''; return; }
    sostener(v, W*(.22 + Math.random()*.56), H*(.26 + Math.random()*.44));
    entrada.value = '';
    entrada.focus();
    tocado();
  });
  entrada.addEventListener('input', tocado);

  btnSoltar.addEventListener('click', function(){
    var vivas = campo.querySelectorAll('.sostenida:not(.soltando)');
    for(var i=0;i<vivas.length;i++){
      (function(b, k){ setTimeout(function(){ soltar(b); }, k*45); })(vivas[i], i);
    }
  });

  setInterval(function(){
    if(campo.querySelectorAll('.sostenida:not(.soltando)').length === 0 &&
       Date.now() - ultimaInteraccion > 13000){
      umbral.classList.remove('fuera');
    }
  }, 2000);

  window.addEventListener('resize', medir);
  window.addEventListener('orientationchange', function(){ setTimeout(medir, 250); });
  medir();
  contar();
  raf = requestAnimationFrame(paso);
})();
</script>
</body>
</html>
```

Qué: Un campo oscuro de letras a la deriva donde el movimiento del cursor levanta palabras que se desvanecen, el clic sostiene una (y otro clic la devuelve al polvo), y una línea abajo permite dejar palabras propias que no se guardan en ningún lado.