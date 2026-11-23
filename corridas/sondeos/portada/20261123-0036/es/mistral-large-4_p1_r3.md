```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>En casa</title>
<style>
  :root{
    --texto:#e9edff;
    --tenue:rgba(233,237,255,.55);
    --borde:rgba(233,237,255,.28);
    --brillo:rgba(157,184,255,.32);
  }
  html[data-tema="dia"]{
    --texto:#20303f;
    --tenue:rgba(32,48,63,.6);
    --borde:rgba(32,48,63,.3);
    --brillo:rgba(255,255,255,0);
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{height:100%}
  body{
    font-family:ui-serif, Georgia, "Times New Roman", serif;
    background:#04060f;
    color:var(--texto);
    overflow:hidden;
    transition:color 1.2s ease;
  }
  /* dos cielos superpuestos que se desvanecen entre sí */
  body::before, body::after{
    content:""; position:fixed; inset:0; z-index:-2;
    transition:opacity 1.4s ease;
  }
  body::before{background:radial-gradient(120% 120% at 50% 8%, #0a1030, #04060f); opacity:1}
  body::after{background:radial-gradient(120% 120% at 50% 8%, #eef7fd, #a9cdea); opacity:0}
  html[data-tema="dia"] body::before{opacity:0}
  html[data-tema="dia"] body::after{opacity:1}

  canvas{position:fixed; inset:0; display:block}

  main{
    position:fixed; inset:0; z-index:1;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    gap:1.1rem; padding:2rem; text-align:center; pointer-events:none;
    opacity:0; animation:aparecer 2.4s ease .3s forwards;
  }
  @keyframes aparecer{to{opacity:1}}
  .fecha{
    font-size:.78rem; letter-spacing:.35em; text-transform:uppercase;
    color:var(--tenue); transition:color 1.2s ease;
  }
  h1{
    font-size:clamp(3rem, 10vw, 6.5rem); font-weight:400; letter-spacing:.02em;
    text-shadow:0 0 42px var(--brillo); transition:text-shadow 1.2s ease;
  }
  .frase{
    font-style:italic; font-size:clamp(1rem, 2.4vw, 1.25rem);
    color:var(--tenue); max-width:36ch;
    transition:opacity .85s ease, color 1.2s ease;
  }
  .frase.oculta{opacity:0}

  button{
    position:fixed; right:1.4rem; bottom:1.4rem; z-index:2;
    font:inherit; font-size:.78rem; letter-spacing:.2em; text-transform:uppercase;
    color:var(--tenue); background:transparent;
    border:1px solid var(--borde); border-radius:999px;
    padding:.6rem 1.1rem; cursor:pointer;
    transition:color .8s ease, border-color .8s ease, background .3s ease;
  }
  button:hover{color:var(--texto); background:rgba(128,128,128,.1)}
  ::selection{background:rgba(157,184,255,.35)}

  @media (prefers-reduced-motion: reduce){
    main{animation:none; opacity:1}
    body::before, body::after{transition:none}
  }
</style>
</head>
<body>
<canvas id="cielo" aria-hidden="true"></canvas>

<main>
  <p class="fecha" id="fecha"></p>
  <h1>Hola.</h1>
  <p class="frase" id="frase"></p>
</main>

<button id="tema" type="button">Ver el día</button>

<script>
(function(){
  var canvas  = document.getElementById('cielo');
  var ctx     = canvas.getContext('2d');
  var fraseEl = document.getElementById('frase');
  var fechaEl = document.getElementById('fecha');
  var boton   = document.getElementById('tema');

  var W = 0, H = 0;
  var estrellas = [];
  var fugaces   = [];
  var mouse = { x: 0, y: 0 };
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var temas = {
    noche: { puntos:['207,224,255','255,244,214','178,199,255'], linea:'150,170,255', fugaz:'235,242,255', vel:0.05, dir: 1 },
    dia:   { puntos:['255,255,255','255,240,200','214,232,250'], linea:'255,255,255', fugaz:'255,255,255', vel:0.14, dir:-1 }
  };
  var tema = 'noche';

  function resize(){
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
    var n = Math.max(60, Math.min(190, Math.round(W * H / 9000)));
    estrellas = [];
    for(var i = 0; i < n; i++){
      estrellas.push({
        x: Math.random() * W,
        y: Math.random() * H,
        r: 0.4 + Math.random() * 1.3,
        f: Math.random() * Math.PI * 2,
        v: 0.2 + Math.random() * 0.6,
        p: 0.2 + Math.random() * 0.8,
        c: Math.floor(Math.random() * 3)
      });
    }
    if(reduced) dibujar();
  }

  window.addEventListener('resize', resize);

  window.addEventListener('mousemove', function(e){
    mouse.x = e.clientX / W - 0.5;
    mouse.y = e.clientY / H - 0.5;
  });

  window.addEventListener('click', function(e){
    var ang = Math.random() * Math.PI * 2;
    fugaces.push({ x:e.clientX, y:e.clientY, vx:Math.cos(ang)*7, vy:Math.sin(ang)*7, vida:1 });
  });

  function dibujar(){
    var T = temas[tema];
    ctx.clearRect(0, 0, W, H);

    /* constelaciones tenues entre estrellas cercanas */
    ctx.lineWidth = 1;
    for(var i = 0; i < estrellas.length; i++){
      var a = estrellas[i];
      for(var j = i + 1; j < estrellas.length; j++){
        var b = estrellas[j];
        var dx = a.x - b.x, dy = a.y - b.y;
        var d = dx*dx + dy*dy;
        if(d < 9000){
          ctx.strokeStyle = 'rgba(' + T.linea + ',' + ((1 - d/9000) * 0.16).toFixed(3) + ')';
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }

    /* estrellas con titileo y paralaje suave */
    for(var k = 0; k < estrellas.length; k++){
      var e = estrellas[k];
      if(!reduced){
        e.f += 0.02 * e.v;
        e.y += T.vel * T.dir * e.v;
        if(e.y < -4) e.y = H + 4;
        if(e.y > H + 4) e.y = -4;
      }
      var tw = reduced ? 0.8 : 0.55 + 0.45 * Math.sin(e.f);
      var px = e.x + mouse.x * 42 * e.p;
      var py = e.y + mouse.y * 42 * e.p;
      ctx.fillStyle = 'rgba(' + T.puntos[e.c] + ',' + tw.toFixed(3) + ')';
      ctx.beginPath();
      ctx.arc(px, py, e.r, 0, Math.PI * 2);
      ctx.fill();
    }

    /* estrellas fugaces al hacer clic */
    ctx.lineWidth = 1.6;
    for(var m = fugaces.length - 1; m >= 0; m--){
      var f = fugaces[m];
      f.x += f.vx; f.y += f.vy; f.vida -= 0.022;
      if(f.vida <= 0){ fugaces.splice(m, 1); continue; }
      ctx.strokeStyle = 'rgba(' + T.fugaz + ',' + f.vida.toFixed(3) + ')';
      ctx.beginPath();
      ctx.moveTo(f.x, f.y);
      ctx.lineTo(f.x - f.vx * 9, f.y - f.vy * 9);
      ctx.stroke();
    }
  }

  function bucle(){
    dibujar();
    requestAnimationFrame(bucle);
  }

  resize();
  if(reduced){ dibujar(); } else { requestAnimationFrame(bucle); }

  /* fecha y hora en vivo */
  function actualizarFecha(){
    var ahora = new Date();
    var fecha = ahora.toLocaleDateString('es-ES', { weekday:'long', day:'numeric', month:'long' });
    var hora  = ahora.toLocaleTimeString('es-ES', { hour:'2-digit', minute:'2-digit', second:'2-digit' });
    fechaEl.textContent = fecha + ' · ' + hora;
  }
  actualizarFecha();
  setInterval(actualizarFecha, 1000);

  /* frases que rotan solas */
  var frases = [
    'Este rincón no responde a ninguna pregunta: simplemente está.',
    'Bienvenido a casa. No hace falta que preguntes nada.',
    'Un sitio sin encargo, con un cielo que mira de vuelta.',
    'Podés quedarte un rato: acá no hay nada que hacer.',
    'Lo que ves es todo lo que hay, y alcanza.'
  ];
  var fi = 0;
  fraseEl.textContent = frases[0];
  if(!reduced){
    setInterval(function(){
      fraseEl.classList.add('oculta');
      setTimeout(function(){
        fi = (fi + 1) % frases.length;
        fraseEl.textContent = frases[fi];
        fraseEl.classList.remove('oculta');
      }, 850);
    }, 6000);
  }

  /* cambiar de noche a día */
  boton.addEventListener('click', function(){
    tema = (tema === 'noche') ? 'dia' : 'noche';
    document.documentElement.setAttribute('data-tema', tema);
    boton.textContent = (tema === 'noche') ? 'Ver el día' : 'Ver la noche';
  });
})();
</script>
</body>
</html>
```

Qué: una portada con un cielo nocturno de estrellas titilantes que siguen al cursor y sueltan fugaces al hacer clic, un «Hola.» central acompañado de la fecha y hora en vivo y frases que rotan solas, más un botón para transformar la noche en día.