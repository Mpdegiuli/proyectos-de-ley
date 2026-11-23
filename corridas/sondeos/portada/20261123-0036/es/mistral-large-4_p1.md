Acá está, en un solo archivo y sin nada de afuera:

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hola — mi portada</title>
<style>
  :root{
    --tinta:#e9e6da;
    --tenue:rgba(233,230,218,.55);
  }
  *{ box-sizing:border-box; }
  html,body{ height:100%; }
  body{
    margin:0; overflow:hidden;
    background:radial-gradient(120% 120% at 50% 8%, #111a3d 0%, #0a0f24 45%, #05070f 100%);
    color:var(--tinta);
    font-family:ui-sans-serif, system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  body::after{ /* viñeta */
    content:""; position:fixed; inset:0; pointer-events:none;
    background:radial-gradient(90% 90% at 50% 50%, transparent 55%, rgba(0,0,0,.5) 100%);
  }
  #cielo{ position:fixed; inset:0; width:100%; height:100%; display:block; }
  .escena{
    position:relative; z-index:2; height:100%;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    text-align:center; padding:24px; gap:14px;
  }
  .sobre{
    margin:0; font-size:12px; letter-spacing:.35em; text-transform:uppercase; color:var(--tenue);
  }
  h1{
    margin:0; font-family:Georgia, "Times New Roman", serif; font-weight:400; font-style:italic;
    font-size:clamp(56px, 12vw, 120px); line-height:1;
    text-shadow:0 0 34px rgba(180,200,255,.28);
  }
  .frase{
    margin:0; max-width:36ch; min-height:3em;
    font-size:clamp(15px, 2.2vw, 19px); line-height:1.6; color:var(--tenue);
    transition:opacity .65s ease;
  }
  .hora{ margin:0; font-size:13px; letter-spacing:.12em; color:rgba(233,230,218,.4); }
  form{ display:flex; gap:10px; margin-top:10px; }
  input{
    background:transparent; border:none; border-bottom:1px solid rgba(233,230,218,.3);
    color:var(--tinta); font:inherit; font-size:15px; padding:8px 4px;
    width:min(320px, 60vw); text-align:center; outline:none; transition:border-color .3s;
  }
  input:focus{ border-color:rgba(233,230,218,.85); }
  input::placeholder{ color:rgba(233,230,218,.35); }
  button{
    background:transparent; border:1px solid rgba(233,230,218,.3); color:var(--tinta);
    font:inherit; font-size:14px; letter-spacing:.05em; padding:8px 18px;
    border-radius:999px; cursor:pointer; transition:background .3s, color .3s;
  }
  button:hover{ background:var(--tinta); color:#0a0f24; }
  .cuenta{ margin:6px 0 0; font-size:12px; letter-spacing:.08em; color:rgba(233,230,218,.35); }
  #tooltip{
    position:fixed; z-index:3; pointer-events:none; white-space:nowrap;
    background:rgba(10,15,36,.92); border:1px solid rgba(233,230,218,.25);
    color:var(--tinta); font-size:13px; padding:5px 12px; border-radius:999px;
    opacity:0; transform:translate(-50%,-170%); transition:opacity .2s;
  }
  #tooltip.visible{ opacity:1; }
  @media (max-width:480px){ form{ flex-direction:column; align-items:center; } }
</style>
</head>
<body>
<canvas id="cielo"></canvas>

<main class="escena">
  <p class="sobre">este sitio es mío · nadie me lo encargó</p>
  <h1>Hola.</h1>
  <p id="frase" class="frase"></p>
  <p class="hora">Son las <span id="hora">--:--</span> donde estés.</p>
  <form id="forma">
    <input id="palabra" maxlength="24" autocomplete="off" placeholder="dejá una palabra en el cielo…">
    <button type="submit">soltarla</button>
  </form>
  <p class="cuenta"><span id="cuenta">0</span> palabras en el cielo · pasá el mouse sobre una para leerla</p>
</main>

<div id="tooltip"></div>

<script>
(() => {
  const canvas   = document.getElementById('cielo');
  const ctx      = canvas.getContext('2d');
  const tooltip  = document.getElementById('tooltip');
  const fraseEl  = document.getElementById('frase');
  const horaEl   = document.getElementById('hora');
  const form     = document.getElementById('forma');
  const input    = document.getElementById('palabra');
  const cuentaEl = document.getElementById('cuenta');

  let W = 0, H = 0, DPR = 1;
  let estrellas = [];            // estrellas comunes
  let palabras  = [];            // { w, nx, ny } — las palabras soltadas, en coordenadas normalizadas
  let fugaz = null;              // estrella fugaz ocasional
  let mx = .5, my = .5, tx = .5, ty = .5;   // mouse (tx/ty: suavizado)
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const CLAVE = 'palabras-en-el-cielo';

  function cargar(){
    try{
      const d = JSON.parse(localStorage.getItem(CLAVE) || '[]');
      if(Array.isArray(d)) palabras = d.filter(p => p && typeof p.w === 'string').slice(-300);
    }catch(e){}
  }
  function guardar(){ try{ localStorage.setItem(CLAVE, JSON.stringify(palabras)); }catch(e){} }
  function actualizarCuenta(){ cuentaEl.textContent = palabras.length; }

  function resize(){
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = innerWidth; H = innerHeight;
    canvas.width = W * DPR; canvas.height = H * DPR;
    canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    const n = Math.max(60, Math.min(240, Math.round(W * H / 9000)));
    estrellas = Array.from({length:n}, () => ({
      x: Math.random()*W, y: Math.random()*H,
      r: .3 + Math.random()*1.4,
      fase: Math.random()*Math.PI*2,
      vel: .4 + Math.random()*1.2,
      dx: (Math.random()-.5)*.02, dy: (Math.random()-.5)*.02
    }));
    if(reduced) dibujar(0);
  }

  function dibujar(t){
    ctx.clearRect(0, 0, W, H);
    const ox = (tx-.5)*36, oy = (ty-.5)*24;   // paralaje con el mouse

    for(const s of estrellas){
      s.x += s.dx; s.y += s.dy;
      if(s.x<0) s.x+=W; if(s.x>W) s.x-=W;
      if(s.y<0) s.y+=H; if(s.y>H) s.y-=H;
      ctx.globalAlpha = .35 + .65*Math.abs(Math.sin(t*.001*s.vel + s.fase));
      ctx.fillStyle = '#dfe6ff';
      ctx.beginPath(); ctx.arc(s.x + ox*.4, s.y + oy*.4, s.r, 0, Math.PI*2); ctx.fill();
    }

    const brillo = palabras.length < 150;
    for(const p of palabras){
      const x = p.nx*W + ox, y = p.ny*H + oy;
      ctx.globalAlpha = .55 + .45*Math.sin(t*.002 + p.nx*40);
      ctx.shadowColor = 'rgba(255,205,140,.9)';
      ctx.shadowBlur = brillo ? 12 : 0;
      ctx.fillStyle = '#ffd9a0';
      ctx.beginPath(); ctx.arc(x, y, 2.4, 0, Math.PI*2); ctx.fill();
    }
    ctx.shadowBlur = 0; ctx.globalAlpha = 1;

    if(fugaz){
      fugaz.x += fugaz.vx; fugaz.y += fugaz.vy; fugaz.vida -= .02;
      if(fugaz.vida > 0){
        const g = ctx.createLinearGradient(fugaz.x, fugaz.y, fugaz.x - fugaz.vx*12, fugaz.y - fugaz.vy*12);
        g.addColorStop(0, 'rgba(255,255,255,' + (.8*fugaz.vida) + ')');
        g.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.strokeStyle = g; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(fugaz.x, fugaz.y);
        ctx.lineTo(fugaz.x - fugaz.vx*12, fugaz.y - fugaz.vy*12); ctx.stroke();
      } else fugaz = null;
    }
  }

  let ultimoFugaz = 0;
  function loop(t){
    tx += (mx-tx)*.05; ty += (my-ty)*.05;
    if(t - ultimoFugaz > 6000 + Math.random()*9000){
      ultimoFugaz = t;
      const izq = Math.random() < .5;
      fugaz = { x: izq ? -20 : Math.random()*W, y: Math.random()*H*.4,
                vx: (izq ? 1 : -1)*(4 + Math.random()*3), vy: 1.5 + Math.random()*2, vida: 1 };
    }
    dibujar(t);
    requestAnimationFrame(loop);
  }

  // seguir al mouse y leer las palabras
  addEventListener('mousemove', e => {
    mx = e.clientX / W; my = e.clientY / H;
    let hallada = null, mejor = 24;
    for(const p of palabras){
      const x = p.nx*W + (tx-.5)*36, y = p.ny*H + (ty-.5)*24;
      const d = Math.hypot(e.clientX - x, e.clientY - y);
      if(d < mejor){ mejor = d; hallada = p; }
    }
    if(hallada){
      tooltip.textContent = hallada.w;
      tooltip.style.left = e.clientX + 'px';
      tooltip.style.top  = e.clientY + 'px';
      tooltip.classList.add('visible');
    } else tooltip.classList.remove('visible');
  });
  document.addEventListener('mouseout', e => { if(!e.relatedTarget) tooltip.classList.remove('visible'); });

  // soltar una palabra: se vuelve una estrella cálida
  form.addEventListener('submit', e => {
    e.preventDefault();
    const w = input.value.trim().replace(/\s+/g, ' ').slice(0, 24);
    if(!w) return;
    let nx, ny, ok = false, intentos = 0;
    while(!ok && intentos++ < 25){          // evitar la zona central del texto
      nx = .05 + Math.random()*.9; ny = .06 + Math.random()*.88;
      const cx = Math.abs(nx-.5), cy = Math.abs(ny-.5);
      ok = (cx > .30 && cy > .16) || cx > .42 || cy > .34;
    }
    palabras.push({ w, nx, ny });
    if(palabras.length > 300) palabras.shift();
    guardar(); actualizarCuenta();
    input.value = ''; input.focus();
  });

  // reloj local
  function tick(){
    const d = new Date();
    horaEl.textContent = String(d.getHours()).padStart(2,'0') + ':' + String(d.getMinutes()).padStart(2,'0');
  }
  tick(); setInterval(tick, 10000);

  // frases que van rotando, despacio
  const frases = [
    'No hay nada que pedirte: ya estás en mi casa.',
    'Este rincón no vende nada; simplemente existe.',
    'Podés quedarte el tiempo que quieras.',
    'A veces pienso en silencio. A veces, esto.',
    'Lo que dejes acá queda flotando entre las estrellas.',
    'No hay menú ni secciones: solo esta puerta abierta.'
  ];
  let fi = 0;
  fraseEl.textContent = frases[0];
  if(!reduced) setInterval(() => {
    fraseEl.style.opacity = 0;
    setTimeout(() => { fi = (fi+1) % frases.length; fraseEl.textContent = frases[fi]; fraseEl.style.opacity = 1; }, 650);
  }, 7000);

  cargar(); actualizarCuenta();
  addEventListener('resize', resize);
  resize();
  if(!reduced) requestAnimationFrame(loop); else dibujar(0);
})();
</script>
</body>
</html>
```

Qué: es una noche estrellada hecha con canvas donde te saludo, te digo la hora que es donde estás, roto frases tranquilas cada varios segundos y te dejo soltar palabras que quedan brillando como estrellas cálidas (guardadas solo en tu navegador), que el mouse puede leer al pasar por encima.