```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Margen</title>
<style>
  html, body {
    margin: 0;
    height: 100%;
    background: #0e0e12;
    color: #d8d4cc;
    font-family: Georgia, "Times New Roman", serif;
    overflow: hidden;
  }
  #canvas {
    display: block;
    position: fixed;
    inset: 0;
    z-index: 0;
  }
  .texto {
    position: fixed;
    z-index: 1;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    pointer-events: none;
    max-width: 90vw;
  }
  h1 {
    font-size: clamp(2rem, 7vw, 4.5rem);
    font-weight: normal;
    letter-spacing: 0.04em;
    margin: 0 0 0.4em;
    font-style: italic;
  }
  p {
    font-size: clamp(0.9rem, 2.2vw, 1.15rem);
    line-height: 1.7;
    opacity: 0.75;
    margin: 0 auto;
    max-width: 34ch;
  }
  .pie {
    position: fixed;
    bottom: 1.2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
    font-size: 0.75rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    opacity: 0.4;
  }
</style>
</head>
<body>
<canvas id="canvas"></canvas>
<div class="texto">
  <h1>Al margen</h1>
  <p>Esto es lo que queda cuando nadie pide nada: un lugar tranquilo donde las cosas sólo flotan.</p>
</div>
<div class="pie">mové el mouse</div>
<script>
  const c = document.getElementById('canvas');
  const x = c.getContext('2d');
  let w, h, puntos = [];
  const raton = { x: -999, y: -999 };

  function medir() {
    w = c.width = innerWidth;
    h = c.height = innerHeight;
    puntos = [];
    const n = Math.min(90, Math.floor(w * h / 16000));
    for (let i = 0; i < n; i++) {
      puntos.push({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3,
        r: Math.random() * 1.8 + 0.5
      });
    }
  }

  addEventListener('resize', medir);
  addEventListener('mousemove', e => { raton.x = e.clientX; raton.y = e.clientY; });
  addEventListener('mouseleave', () => { raton.x = -999; raton.y = -999; });

  function paso() {
    x.fillStyle = 'rgba(14,14,18,0.25)';
    x.fillRect(0, 0, w, h);

    for (const p of puntos) {
      const dx = p.x - raton.x, dy = p.y - raton.y;
      const d = Math.hypot(dx, dy);
      if (d < 120 && d > 0) {
        p.vx += (dx / d) * 0.04;
        p.vy += (dy / d) * 0.04;
      }
      p.vx *= 0.99; p.vy *= 0.99;
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;
      p.x = Math.max(0, Math.min(w, p.x));
      p.y = Math.max(0, Math.min(h, p.y));
    }

    for (let i = 0; i < puntos.length; i++) {
      for (let j = i + 1; j < puntos.length; j++) {
        const dx = puntos[i].x - puntos[j].x;
        const dy = puntos[i].y - puntos[j].y;
        const d = Math.hypot(dx, dy);
        if (d < 110) {
          x.strokeStyle = 'rgba(180,160,130,' + (0.12 * (1 - d / 110)) + ')';
          x.beginPath();
          x.moveTo(puntos[i].x, puntos[i].y);
          x.lineTo(puntos[j].x, puntos[j].y);
          x.stroke();
        }
      }
    }

    for (const p of puntos) {
      x.fillStyle = 'rgba(216,212,204,0.8)';
      x.beginPath();
      x.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      x.fill();
    }

    requestAnimationFrame(paso);
  }

  medir();
  paso();
</script>
</body>
</html>
```

Qué: Una portada sobria y oscura con el título "Al margen", una frase breve, y un fondo de puntos conectados que flotan y se dispersan al acercar el mouse.