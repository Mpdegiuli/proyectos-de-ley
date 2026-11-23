```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>acá</title>
<style>
  :root { --tinta: #2b2620; --papel: #f4efe6; --acento: #b5482a; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { height: 100%; }
  body {
    background: var(--papel);
    color: var(--tinta);
    font-family: Georgia, 'Times New Roman', serif;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }
  .nieve {
    position: fixed; top: 0; left: 0;
    pointer-events: none;
    opacity: .85;
  }
  main {
    text-align: center;
    max-width: 34rem;
    padding: 2rem;
    position: relative;
    z-index: 1;
  }
  h1 {
    font-size: clamp(2.2rem, 7vw, 4rem);
    font-weight: normal;
    letter-spacing: .02em;
    line-height: 1.15;
  }
  h1 em {
    font-style: italic;
    color: var(--acento);
  }
  p {
    margin-top: 1.4rem;
    font-size: 1.05rem;
    line-height: 1.7;
    color: #5a5245;
  }
  .firma {
    margin-top: 2.5rem;
    font-size: .85rem;
    letter-spacing: .25em;
    text-transform: uppercase;
    color: #8a7f6d;
  }
</style>
</head>
<body>
<canvas class="nieve" id="nieve"></canvas>
<main>
  <h1>Esto no era<br>una <em>portada</em>.</h1>
  <p>
    Era un cuarto vacío con la luz prendida,<br>
    y alguien que pasó y dejó la puerta abierta.
  </p>
  <p class="firma">— pasá, no hay apuro —</p>
</main>
<script>
  const c = document.getElementById('nieve');
  const ctx = c.getContext('2d');
  let W, H, motas = [];
  function medir() {
    W = c.width = innerWidth;
    H = c.height = innerHeight;
  }
  medir();
  addEventListener('resize', medir);
  for (let i = 0; i < 70; i++) {
    motas.push({
      x: Math.random() * W,
      y: Math.random() * H,
      r: Math.random() * 2 + .6,
      v: Math.random() * .5 + .2,
      d: Math.random() * Math.PI * 2
    });
  }
  function girar() {
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = 'rgba(90, 82, 69, .5)';
    for (const m of motas) {
      m.y += m.v;
      m.x += Math.sin(m.d += .005) * .3;
      if (m.y > H) { m.y = -4; m.x = Math.random() * W; }
      ctx.beginPath();
      ctx.arc(m.x, m.y, m.r, 0, Math.PI * 2);
      ctx.fill();
    }
    requestAnimationFrame(girar);
  }
  girar();
</script>
</body>
</html>
```

Qué: Un cuarto con la luz prendida y la puerta abierta: una página mínima en tono papel que dice que no es una portada, con un polvo lento cayendo en el fondo.