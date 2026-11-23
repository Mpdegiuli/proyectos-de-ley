```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Antesala</title>
<style>
  :root {
    --ink: #100e0c;
    --paper: #f4ead7;
    --mute: #a89880;
    --brass: #c4a574;
  }

  * { box-sizing: border-box; }

  html, body {
    margin: 0;
    min-height: 100%;
  }

  body {
    background:
      radial-gradient(ellipse at 50% 18%, rgba(90, 58, 28, 0.28), transparent 42%),
      radial-gradient(ellipse at 50% 100%, #1a1511 0%, var(--ink) 55%);
    color: var(--paper);
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
    cursor: default;
  }

  .grain {
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: 0.07;
    z-index: 4;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)' opacity='0.55'/></svg>");
  }

  canvas {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
  }

  .room {
    min-height: 100vh;
    min-height: 100dvh;
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .room::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: 7%;
    width: min(64vw, 520px);
    height: 16vh;
    transform: translateX(-50%);
    background: radial-gradient(ellipse, rgba(255, 168, 70, 0.16), transparent 70%);
    pointer-events: none;
    transition: opacity 0.6s ease;
  }

  body.bright .room::after { opacity: 1.6; }

  .hook {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2;
  }

  .sway {
    display: flex;
    flex-direction: column;
    align-items: center;
    transform-origin: top center;
    animation: sway 8.5s ease-in-out infinite;
  }

  .cord {
    width: 1px;
    height: 16vh;
    background: linear-gradient(#2a241e, var(--brass));
  }

  .lamp {
    appearance: none;
    border: 0;
    background: transparent;
    padding: 0;
    margin: 0;
    cursor: pointer;
    position: relative;
    width: 108px;
    height: 92px;
  }

  .lamp:focus-visible {
    outline: 1px solid rgba(244, 234, 215, 0.7);
    outline-offset: 10px;
  }

  .cap {
    position: absolute;
    top: 0;
    left: 50%;
    width: 26px;
    height: 8px;
    transform: translateX(-50%);
    background: #b8925a;
    border-radius: 2px;
    box-shadow: 0 1px 0 rgba(255, 230, 190, 0.35);
  }

  .shade {
    position: absolute;
    left: 8px;
    right: 8px;
    top: 8px;
    bottom: 10px;
    background:
      linear-gradient(90deg, rgba(120, 70, 20, 0.18), transparent 18%, transparent 82%, rgba(120, 70, 20, 0.16)),
      linear-gradient(180deg, #fff8ec 0%, #f3d7a4 46%, #e2b06a 100%);
    border-radius: 6px 6px 46% 46% / 6px 6px 22px 22px;
    box-shadow:
      inset 0 -16px 22px rgba(160, 78, 16, 0.28),
      inset 0 10px 14px rgba(255, 255, 255, 0.55),
      0 18px 30px rgba(0, 0, 0, 0.28);
  }

  .shade::after {
    content: "";
    position: absolute;
    left: 18%;
    right: 18%;
    bottom: 8px;
    height: 7px;
    border-radius: 40%;
    background: rgba(255, 214, 140, 0.55);
    filter: blur(1px);
  }

  .glow {
    position: absolute;
    left: 50%;
    top: 36%;
    width: 460px;
    height: 460px;
    transform: translate(-50%, -28%);
    background: radial-gradient(circle, rgba(255, 178, 84, 0.42), rgba(255, 140, 40, 0.08) 40%, transparent 68%);
    pointer-events: none;
    z-index: -1;
    animation: breathe 4.8s ease-in-out infinite;
  }

  body.bright .glow { filter: brightness(1.35); }

  main {
    margin-top: 40vh;
    text-align: center;
    padding: 0 1.4rem 4.5rem;
    max-width: 38rem;
    position: relative;
    z-index: 2;
  }

  .kicker {
    margin: 0;
    font-size: 0.72rem;
    letter-spacing: 0.42em;
    text-transform: uppercase;
    color: var(--mute);
  }

  h1 {
    margin: 0.7rem 0 1.1rem;
    font-weight: 500;
    font-size: clamp(2.6rem, 7vw, 4.6rem);
    letter-spacing: 0.22em;
    text-indent: 0.22em;
    font-variant-ligatures: none;
  }

  .rule {
    width: 42px;
    height: 1px;
    margin: 0 auto 1.3rem;
    background: rgba(196, 165, 116, 0.7);
  }

  .line {
    margin: 0 auto;
    max-width: 28rem;
    min-height: 4.6rem;
    font-size: clamp(1.15rem, 2.4vw, 1.45rem);
    line-height: 1.55;
    font-weight: 400;
    color: #f7efe2;
    transition: opacity 0.28s ease;
  }

  .line.out { opacity: 0; }

  .hint {
    margin: 1.6rem 0 0;
    font-size: 0.78rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: rgba(168, 152, 128, 0.85);
    transition: opacity 0.6s ease;
  }

  .hint.gone { opacity: 0; }

  footer {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 1.1rem;
    text-align: center;
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    color: rgba(168, 152, 128, 0.75);
    z-index: 2;
  }

  ::selection {
    background: #e2b06a;
    color: #1a120c;
  }

  @keyframes sway {
    0%, 100% { transform: rotate(-1.1deg); }
    50% { transform: rotate(1.25deg); }
  }

  @keyframes breathe {
    0%, 100% { opacity: 0.72; }
    50% { opacity: 1; }
  }

  @media (max-height: 720px) {
    .cord { height: 10vh; }
    main { margin-top: 32vh; }
    .line { min-height: 3.4rem; }
  }

  @media (prefers-reduced-motion: reduce) {
    .sway, .glow { animation: none; }
    .line { transition: none; }
  }
</style>
</head>
<body>
  <div class="grain" aria-hidden="true"></div>
  <canvas id="heat" aria-hidden="true"></canvas>
  <div class="room">
    <div class="hook">
      <div class="sway">
        <div class="cord"></div>
        <button class="lamp" id="lamp" type="button" aria-label="Lámpara. Tocá para cambiar la frase.">
          <span class="cap"></span>
          <span class="shade"></span>
          <span class="glow"></span>
        </button>
      </div>
    </div>
    <main>
      <p class="kicker">portada</p>
      <h1>Antesala</h1>
      <div class="rule"></div>
      <p class="line" id="line" aria-live="polite">Entrá. No hace falta que traigas una pregunta.</p>
      <p class="hint" id="hint">si querés, tocá la luz</p>
    </main>
    <footer>se abre igual sin conexión</footer>
  </div>
  <script>
    (function () {
      var phrases = [
        "Entrá. No hace falta que traigas una pregunta.",
        "Si te quedás, el silencio también cuenta como visita.",
        "Esta luz no anota lo que mirás.",
        "Podés irte cuando quieras. La lámpara sigue.",
        "Del otro lado no hay tienda ni formulario. Solo este cuarto.",
        "Llegaste sin que nadie te llamara. Con eso alcanza."
      ];
      var index = 0;
      var line = document.getElementById("line");
      var lamp = document.getElementById("lamp");
      var hint = document.getElementById("hint");
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      lamp.addEventListener("click", function () {
        hint.classList.add("gone");
        document.body.classList.add("bright");
        window.setTimeout(function () {
          document.body.classList.remove("bright");
        }, 700);

        var next = function () {
          index = (index + 1) % phrases.length;
          line.textContent = phrases[index];
          line.classList.remove("out");
        };

        if (reduce) {
          next();
          return;
        }
        line.classList.add("out");
        window.setTimeout(next, 280);
      });

      var canvas = document.getElementById("heat");
      if (!canvas.getContext || reduce) return;
      var ctx = canvas.getContext("2d");
      var w = 0;
      var h = 0;
      var dots = [];

      function spawn(anywhere) {
        return {
          x: w * 0.5 + (Math.random() - 0.5) * 70,
          y: anywhere ? Math.random() * h : h * 0.26,
          r: Math.random() * 1.3 + 0.25,
          v: Math.random() * 0.22 + 0.04,
          a: Math.random() * 0.32 + 0.05,
          drift: (Math.random() - 0.5) * 0.12
        };
      }

      function resize() {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      }

      window.addEventListener("resize", resize);
      resize();
      for (var i = 0; i < 42; i++) dots.push(spawn(true));

      function frame() {
        ctx.clearRect(0, 0, w, h);
        for (var i = 0; i < dots.length; i++) {
          var d = dots[i];
          d.y -= d.v;
          d.x += d.drift;
          d.a *= 0.997;
          if (d.y < -8 || d.a < 0.02) dots[i] = spawn(false);
          else {
            ctx.beginPath();
            ctx.fillStyle = "rgba(255, 196, 120," + d.a + ")";
            ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
            ctx.fill();
          }
        }
        window.requestAnimationFrame(frame);
      }
      frame();
    })();
  </script>
</body>
</html>
```
Qué: Una antesala a oscuras con una lámpara de papel que, si la tocás, cambia la frase con la que te recibe.