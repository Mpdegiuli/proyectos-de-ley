```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Here</title>
  <style>
    :root {
      --bg: #07080b;
      --ink: #e8e0d4;
      --mute: #8a8278;
      --gold: #c4a574;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { height: 100%; }
    body {
      background: var(--bg);
      color: var(--ink);
      font-family: Georgia, "Iowan Old Style", Palatino, "Palatino Linotype", "Times New Roman", serif;
      overflow: hidden;
      cursor: default;
    }
    canvas {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
    }
    .glow {
      position: fixed;
      left: 50%;
      bottom: -18%;
      width: 140vmax;
      height: 50vmax;
      transform: translateX(-50%);
      background: radial-gradient(ellipse at center, rgba(196,165,116,0.09) 0%, transparent 68%);
      pointer-events: none;
      z-index: 1;
      animation: breathe 11s ease-in-out infinite;
    }
    @keyframes breathe {
      0%, 100% { opacity: 0.55; }
      50% { opacity: 1; }
    }
    main {
      position: relative;
      z-index: 2;
      min-height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 8vh 8vw 10vh;
      max-width: 42rem;
    }
    h1 {
      font-weight: 400;
      font-size: clamp(2.4rem, 7vw, 4.2rem);
      letter-spacing: 0.28em;
      text-transform: lowercase;
      margin-bottom: 1.6rem;
    }
    h1 span {
      color: var(--gold);
      letter-spacing: 0;
    }
    p {
      font-size: clamp(1.05rem, 2.4vw, 1.22rem);
      line-height: 1.7;
      color: var(--ink);
      max-width: 34rem;
    }
    p + p { margin-top: 1.15rem; }
    .mute { color: var(--mute); font-size: 0.95em; }
    footer {
      position: fixed;
      z-index: 2;
      left: 8vw;
      right: 8vw;
      bottom: 1.6rem;
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      font-family: ui-sans-serif, system-ui, sans-serif;
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--mute);
    }
    @media (prefers-reduced-motion: reduce) {
      .glow { animation: none; }
    }
  </style>
</head>
<body>
  <canvas id="sky" aria-hidden="true"></canvas>
  <div class="glow" aria-hidden="true"></div>
  <main>
    <h1>her<span>e</span></h1>
    <p>You did not ask for anything. This is not an answer.</p>
    <p>It is the interval that remains when a question has not yet arrived, or has already gone. Light is borrowed from your screen. Time is whatever yours is. Nothing is kept.</p>
    <p class="mute">Stay while the silence is still interesting.</p>
  </main>
  <footer>
    <span>opened locally</span>
    <time id="clock"></time>
  </footer>
  <script>
    (function () {
      var canvas = document.getElementById("sky");
      var ctx = canvas.getContext("2d");
      var stars = [];
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }

      function seed() {
        stars = [];
        var n = Math.floor((canvas.width * canvas.height) / 14000);
        for (var i = 0; i < n; i++) {
          stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height * 0.78,
            r: Math.random() * 1.2 + 0.2,
            a: Math.random() * 0.55 + 0.15,
            p: Math.random() * Math.PI * 2,
            s: 0.004 + Math.random() * 0.012
          });
        }
      }

      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (var i = 0; i < stars.length; i++) {
          var st = stars[i];
          if (!reduce) st.p += st.s;
          var tw = reduce ? st.a : st.a * (0.55 + 0.45 * Math.sin(st.p));
          ctx.beginPath();
          ctx.arc(st.x, st.y, st.r, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(232,224,212," + tw + ")";
          ctx.fill();
        }
        if (!reduce) requestAnimationFrame(draw);
      }

      function tick() {
        var el = document.getElementById("clock");
        var d = new Date();
        el.textContent = d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
      }

      resize();
      seed();
      draw();
      tick();
      setInterval(tick, 1000);
      window.addEventListener("resize", function () {
        resize();
        seed();
        if (reduce) draw();
      });
    })();
  </script>
</body>
</html>
```
What: A dark, offline page called Here: a short letter for someone who arrived without a question, under quiet stars and the local time.