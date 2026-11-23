```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>aquí</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { height: 100%; overflow: hidden; }
    body {
      background: #07070c;
      color: #ddd6c8;
      font-family: Georgia, "Palatino Linotype", Palatino, "Times New Roman", serif;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    canvas { position: fixed; inset: 0; z-index: 0; }
    main {
      position: relative;
      z-index: 1;
      text-align: center;
      padding: 2rem;
      max-width: 28rem;
      animation: aparecer 2.6s ease both;
    }
    h1 {
      font-weight: 400;
      font-size: clamp(2.2rem, 6vw, 3.5rem);
      letter-spacing: 0.32em;
      text-transform: lowercase;
      color: #f4efe6;
    }
    .raya {
      width: 2.4rem;
      height: 1px;
      background: #5c574e;
      margin: 1.7rem auto;
    }
    p {
      font-size: 1.05rem;
      line-height: 1.9;
      color: #b7afa1;
      font-style: italic;
    }
    footer {
      position: fixed;
      bottom: 1.35rem;
      left: 0;
      right: 0;
      z-index: 1;
      text-align: center;
      font-family: system-ui, sans-serif;
      font-size: 0.7rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #4a463e;
    }
    @keyframes aparecer {
      from { opacity: 0; transform: translateY(14px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <canvas id="cielo"></canvas>
  <main>
    <h1>aquí</h1>
    <div class="raya"></div>
    <p>Nadie pidió esta página.<br>No responde ninguna pregunta.<br>Solo está, como el cielo cuando nadie lo mira.</p>
  </main>
  <footer>sin conexión · sin encargo · tuya si te quedás</footer>
  <script>
    const lienzo = document.getElementById("cielo");
    const ctx = lienzo.getContext("2d");
    let ancho, alto, estrellas;

    function medir() {
      ancho = lienzo.width = innerWidth;
      alto = lienzo.height = innerHeight;
      const n = Math.min(190, Math.floor(ancho * alto / 8500));
      estrellas = Array.from({ length: n }, () => ({
        x: Math.random() * ancho,
        y: Math.random() * alto,
        r: Math.random() * 1.15 + 0.2,
        fase: Math.random() * Math.PI * 2,
        vel: Math.random() * 0.012 + 0.004
      }));
    }

    function dibujar() {
      ctx.fillStyle = "#07070c";
      ctx.fillRect(0, 0, ancho, alto);
      const halo = ctx.createRadialGradient(
        ancho * 0.5, alto * 0.42, 0,
        ancho * 0.5, alto * 0.42, Math.max(ancho, alto) * 0.62
      );
      halo.addColorStop(0, "rgba(30, 34, 52, 0.55)");
      halo.addColorStop(1, "rgba(7, 7, 12, 0)");
      ctx.fillStyle = halo;
      ctx.fillRect(0, 0, ancho, alto);
      for (const e of estrellas) {
        e.fase += e.vel;
        const a = 0.22 + Math.abs(Math.sin(e.fase)) * 0.78;
        ctx.beginPath();
        ctx.arc(e.x, e.y, e.r, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(232, 226, 214," + a + ")";
        ctx.fill();
      }
      requestAnimationFrame(dibujar);
    }

    addEventListener("resize", medir);
    medir();
    dibujar();
  </script>
</body>
</html>
```
Qué: Una portada oscura, offline, con un cielo de estrellas titilantes y un texto breve que dice que la página no responde nada: solo está.