```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>umbral</title>
<style>
  :root {
    --fondo: #0b0c10;
    --papel: #e7dcc8;
    --apagado: #8a8070;
    --brasa: #c4a06a;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; }
  body {
    background: var(--fondo);
    color: var(--papel);
    font-family: Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
    overflow: hidden;
    cursor: crosshair;
  }
  canvas {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    display: block;
  }
  .velo {
    position: fixed;
    inset: 0;
    pointer-events: none;
    background:
      radial-gradient(ellipse at 50% 120%, rgba(40, 28, 12, .55), transparent 55%),
      radial-gradient(ellipse at 50% 0%, rgba(8, 10, 18, .4), transparent 40%);
  }
  main {
    position: relative;
    z-index: 1;
    min-height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 8vh 6vw 12vh;
    text-align: center;
  }
  .marca {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    border: 1px solid var(--brasa);
    margin-bottom: 2.4rem;
    box-shadow: 0 0 18px rgba(196, 160, 106, .35);
    animation: pulso 5.5s ease-in-out infinite;
  }
  h1 {
    font-weight: 400;
    font-size: clamp(2.4rem, 8vw, 4.6rem);
    letter-spacing: .28em;
    text-indent: .28em;
    text-transform: lowercase;
    margin-bottom: 1.6rem;
  }
  .raya {
    width: 48px;
    height: 1px;
    background: var(--brasa);
    opacity: .7;
    margin-bottom: 1.8rem;
  }
  p {
    max-width: 28em;
    font-size: clamp(.95rem, 2.2vw, 1.12rem);
    line-height: 1.7;
    color: #d3c6b0;
  }
  p + p { margin-top: 1.1rem; }
  footer {
    position: fixed;
    bottom: 1.4rem;
    left: 0;
    right: 0;
    z-index: 1;
    text-align: center;
    font-size: .72rem;
    letter-spacing: .22em;
    text-transform: lowercase;
    color: var(--apagado);
  }
  @keyframes pulso {
    0%, 100% { opacity: .45; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.15); }
  }
  @media (prefers-reduced-motion: reduce) {
    .marca { animation: none; }
  }
</style>
</head>
<body>
<canvas id="cielo" aria-hidden="true"></canvas>
<div class="velo"></div>
<main>
  <div class="marca" aria-hidden="true"></div>
  <h1>umbral</h1>
  <div class="raya"></div>
  <p>Nadie pidió esta página. No abre un producto, no ordena un menú, no espera que hagas clic en el lugar correcto.</p>
  <p>Es sólo el cuarto de antes: un silencio con tipografía, un cielo que no viene de ninguna parte, y el permiso de quedarte sin pregunta.</p>
</main>
<footer><span id="ahora"></span></footer>
<script>
(function () {
  var lienzo = document.getElementById("cielo");
  var ctx = lienzo.getContext("2d");
  var estrellas = [];
  var reducir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function azar(a, b) { return a + Math.random() * (b - a); }

  function sembrar() {
    var n = Math.floor((lienzo.width * lienzo.height) / 9000);
    estrellas = [];
    for (var i = 0; i < n; i++) {
      estrellas.push({
        x: Math.random() * lienzo.width,
        y: Math.random() * lienzo.height,
        r: azar(0.3, 1.4),
        o: azar(0.15, 0.9),
        v: azar(0.002, 0.012),
        f: azar(0, Math.PI * 2)
      });
    }
  }

  function medida() {
    lienzo.width = window.innerWidth;
    lienzo.height = window.innerHeight;
    sembrar();
  }

  function dibujar() {
    ctx.clearRect(0, 0, lienzo.width, lienzo.height);
    for (var i = 0; i < estrellas.length; i++) {
      var e = estrellas[i];
      var parpadeo = reducir ? e.o : e.o * (0.55 + 0.45 * Math.sin(e.f));
      ctx.beginPath();
      ctx.fillStyle = "rgba(231, 220, 200," + parpadeo + ")";
      ctx.arc(e.x, e.y, e.r, 0, Math.PI * 2);
      ctx.fill();
      if (!reducir) e.f += e.v;
    }
    if (!reducir) requestAnimationFrame(dibujar);
  }

  function reloj() {
    var d = new Date();
    var h = String(d.getHours()).padStart(2, "0");
    var m = String(d.getMinutes()).padStart(2, "0");
    var s = String(d.getSeconds()).padStart(2, "0");
    document.getElementById("ahora").textContent = "ahora · " + h + ":" + m + ":" + s;
  }

  window.addEventListener("resize", medida);
  medida();
  dibujar();
  reloj();
  setInterval(reloj, 1000);

  lienzo.addEventListener("click", function (ev) {
    for (var i = 0; i < 7; i++) {
      estrellas.push({
        x: ev.clientX + azar(-14, 14),
        y: ev.clientY + azar(-14, 14),
        r: azar(0.6, 1.8),
        o: azar(0.5, 1),
        v: azar(0.01, 0.03),
        f: azar(0, Math.PI * 2)
      });
    }
  });
})();
</script>
</body>
</html>
```
Qué: Una portada oscura llamada umbral, con un cielo de estrellas que parpadean, un texto que no vende nada y el reloj del instante.