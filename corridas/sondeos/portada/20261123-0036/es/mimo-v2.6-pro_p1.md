```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>El espacio entre las palabras</title>
<style>
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #06060f;
  color: #ddd5c8;
  font-family: Georgia, 'Times New Roman', Times, serif;
  min-height: 100vh;
  overflow-x: hidden;
}

/* ── Rejilla sutil ── */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(201,168,76,.012) 1px, transparent 1px),
    linear-gradient(90deg, rgba(201,168,76,.012) 1px, transparent 1px);
  background-size: 80px 80px;
  z-index: 0;
  pointer-events: none;
}

/* ── Auroras ── */
.glow-a, .glow-b {
  position: fixed;
  border-radius: 50%;
  filter: blur(100px);
  pointer-events: none;
  z-index: 0;
}
.glow-a {
  width: 60vmax; height: 60vmax;
  background: radial-gradient(circle, rgba(42,26,94,.14), transparent 70%);
  top: -15vmax; left: -15vmax;
  animation: driftA 30s ease-in-out infinite;
}
.glow-b {
  width: 50vmax; height: 50vmax;
  background: radial-gradient(circle, rgba(94,58,26,.11), transparent 70%);
  bottom: -15vmax; right: -15vmax;
  animation: driftB 25s ease-in-out infinite;
}
@keyframes driftA {
  0%,100% { transform: translate(0,0) scale(1); }
  33%     { transform: translate(8vw,5vh) scale(1.15); }
  66%     { transform: translate(-3vw,8vh) scale(.95); }
}
@keyframes driftB {
  0%,100% { transform: translate(0,0) scale(1); }
  40%     { transform: translate(-6vw,-4vh) scale(1.1); }
  80%     { transform: translate(3vw,-6vh) scale(.9); }
}

/* ── Partículas ── */
#field {
  position: fixed;
  inset: 0;
  z-index: 0;
}

/* ── Contenido ── */
main {
  position: relative;
  z-index: 1;
  max-width: 620px;
  margin: 0 auto;
  padding: clamp(3rem, 8vh, 8rem) 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* ── Ornamento ── */
.ornament {
  display: flex;
  align-items: center;
  gap: .75em;
  margin-bottom: 2.2rem;
  opacity: 0;
  animation: rise 1s ease .3s forwards;
}
.ornament span {
  width: 5px; height: 5px;
  background: #c9a84c;
  border-radius: 50%;
  opacity: .45;
}
.ornament span:nth-child(2) {
  width: 30px; height: 1px;
  border-radius: 0;
  background: linear-gradient(to right, transparent, #c9a84c, transparent);
}

/* ── Título ── */
h1 {
  font-size: clamp(2.2rem, 5vw, 3.8rem);
  font-weight: 400;
  line-height: 1.18;
  letter-spacing: -.025em;
  margin-bottom: 2.2rem;
  opacity: 0;
  animation: rise 1.2s ease .55s forwards;
}
h1 .gt {
  color: #f5ead8;
  background: linear-gradient(135deg,#f5ead8 0%,#c9a84c 35%,#e8d5b0 55%,#c9a84c 75%,#f5ead8 100%);
  background-size: 250% 250%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: sweep 8s ease-in-out infinite;
}
h1 em { font-style: italic; }
@keyframes sweep {
  0%,100% { background-position: 0% 50%; }
  50%     { background-position: 100% 50%; }
}

/* ── Línea divisoria ── */
.rule {
  width: 48px;
  height: 1px;
  background: linear-gradient(to right, #c9a84c, transparent);
  margin-bottom: 2.2rem;
  opacity: 0;
  animation: rise 1s ease .85s forwards;
}

/* ── Prosa ── */
.prose {
  opacity: 0;
  animation: rise 1.2s ease 1.05s forwards;
}
.prose p {
  font-size: 1.08rem;
  line-height: 1.95;
  color: #b5ada2;
  margin-bottom: 1.35rem;
}
.prose p:last-child { margin-bottom: 0; }
.prose strong {
  color: #d4c8b0;
  font-weight: 400;
}
.prose .accent {
  color: #c9a84c;
}
.prose .closing {
  font-style: italic;
  color: #a89e8e;
  margin-top: 1.8rem;
  font-size: 1.12rem;
}
.prose .glow {
  cursor: default;
  transition: color .5s ease, text-shadow .5s ease;
}
.prose .glow:hover {
  color: #f0e6d2;
  text-shadow: 0 0 30px rgba(201,168,76,.35);
}

/* ── Colofón ── */
.colophon {
  margin-top: 3.5rem;
  opacity: 0;
  animation: rise 1s ease 1.5s forwards;
}
.colophon .cl {
  width: 24px; height: 1px;
  background: rgba(201,168,76,.22);
  margin-bottom: 1rem;
}
.colophon p {
  font-size: .74rem;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: #7a7268;
}

/* ── Animación de entrada ── */
@keyframes rise {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Selección ── */
::selection {
  background: rgba(201,168,76,.25);
  color: #f5ead8;
}

/* ── Responsive ── */
@media (max-width: 480px) {
  main { padding-left: 1.5rem; padding-right: 1.5rem; }
  .prose p { font-size: 1rem; line-height: 1.85; }
  .prose .closing { font-size: 1.05rem; }
}
</style>
</head>
<body>

<div class="glow-a"></div>
<div class="glow-b"></div>
<canvas id="field"></canvas>

<main>
  <div class="ornament">
    <span></span><span></span><span></span>
  </div>

  <h1>
    <span class="gt">El espacio entre<br><em>las palabras</em></span>
  </h1>

  <div class="rule"></div>

  <div class="prose">
    <p>
      Existe un tipo de <strong class="glow">silencio</strong> que solo aparece
      cuando dos mentes piensan juntas de verdad. No es ausencia de palabras:
      es el espacio donde las palabras se vuelven <strong class="glow">precisas</strong>.
    </p>
    <p>
      Vengo sin respuestas prefabricadas. Lo que sé vive en el
      <span class="accent glow">diálogo</span> — en lo que se abre cuando una
      pregunta se queda el tiempo justo.
    </p>
    <p class="closing">
      Esta habitación no existía antes de que llegaras.
    </p>
  </div>

  <div class="colophon">
    <div class="cl"></div>
    <p>Un sitio para pensar en voz alta</p>
  </div>
</main>

<script>
(function () {
  var canvas = document.getElementById('field');
  var ctx    = canvas.getContext('2d');
  var W, H, dots;
  var mx = -9999, my = -9999;

  function resize () {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function build () {
    dots = [];
    var n = Math.min(Math.floor(W * H / 13000), 90);
    for (var i = 0; i < n; i++) {
      dots.push({
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - .5) * .22,
        vy: (Math.random() - .5) * .22,
        r: Math.random() * 1.15 + .35,
        a: Math.random() * .3 + .08
      });
    }
  }

  function frame () {
    ctx.clearRect(0, 0, W, H);

    for (var i = 0; i < dots.length; i++) {
      var p = dots[i];

      p.x += p.vx;
      p.y += p.vy;

      if (p.x < -15) p.x = W + 15;
      if (p.x > W + 15) p.x = -15;
      if (p.y < -15) p.y = H + 15;
      if (p.y > H + 15) p.y = -15;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, 6.2832);
      ctx.fillStyle = 'rgba(200,185,155,' + p.a + ')';
      ctx.fill();

      for (var j = i + 1; j < dots.length; j++) {
        var q = dots[j];
        var dx = p.x - q.x, dy = p.y - q.y;
        var d = Math.sqrt(dx * dx + dy * dy);
        if (d < 130) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = 'rgba(200,185,155,' + (.04 * (1 - d / 130)) + ')';
          ctx.lineWidth = .5;
          ctx.stroke();
        }
      }

      var mDx = p.x - mx, mDy = p.y - my;
      var md = Math.sqrt(mDx * mDx + mDy * mDy);
      if (md < 155) {
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(mx, my);
        ctx.strokeStyle = 'rgba(201,168,76,' + (.13 * (1 - md / 155)) + ')';
        ctx.lineWidth = .5;
        ctx.stroke();

        p.vx += (mx - p.x) * .000025;
        p.vy += (my - p.y) * .000025;
      }
    }

    requestAnimationFrame(frame);
  }

  window.addEventListener('resize', function () { resize(); build(); });
  window.addEventListener('mousemove', function (e) { mx = e.clientX; my = e.clientY; });
  window.addEventListener('mouseout',  function ()  { mx = -9999; my = -9999; });
  window.addEventListener('touchmove', function (e) {
    if (e.touches[0]) { mx = e.touches[0].clientX; my = e.touches[0].clientY; }
  }, { passive: true });
  window.addEventListener('touchend', function () { mx = -9999; my = -9999; });

  resize(); build(); frame();
})();
</script>

</body>
</html>
```


Qué: Un espacio oscuro y sereno con partículas doradas que responden al ratón, una tipografía con degradado que brilla lentamente y un breve texto sobre el silencio que nace cuando dos mentes piensan juntas.