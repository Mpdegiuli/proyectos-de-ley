```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>a quiet place</title>
<style>
  html, body {
    margin: 0;
    height: 100%;
    background: #0e0e14;
    color: #d8d4cc;
    font-family: Georgia, 'Times New Roman', serif;
    overflow: hidden;
  }
  #stage {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    padding: 1rem;
    box-sizing: border-box;
  }
  canvas {
    position: fixed;
    inset: 0;
    z-index: 0;
  }
  .words {
    position: relative;
    z-index: 1;
    max-width: 30rem;
  }
  h1 {
    font-weight: normal;
    font-size: clamp(1.8rem, 6vw, 3rem);
    letter-spacing: 0.04em;
    margin: 0 0 1.2rem;
  }
  p {
    font-size: clamp(0.95rem, 2.5vw, 1.1rem);
    line-height: 1.7;
    color: #9a968e;
    font-style: italic;
    margin: 0;
  }
  .hint {
    margin-top: 2.5rem;
    font-size: 0.8rem;
    font-style: normal;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #55525c;
  }
</style>
</head>
<body>
<canvas id="sky"></canvas>
<div id="stage">
  <div class="words">
    <h1>Still here.</h1>
    <p>No feed, no clock, no reason.<br>Just a window with some light behind it.</p>
    <div class="hint">move the cursor</div>
  </div>
</div>
<script>
  const c = document.getElementById('sky');
  const ctx = c.getContext('2d');
  let w, h, stars = [];
  let mx = 0.5, my = 0.5;

  function resize() {
    w = c.width = innerWidth;
    h = c.height = innerHeight;
    stars = [];
    const n = Math.floor((w * h) / 6000);
    for (let i = 0; i < n; i++) {
      stars.push({
        x: Math.random() * w,
        y: Math.random() * h,
        r: Math.random() * 1.4 + 0.3,
        d: Math.random() * 2 + 0.5,
        t: Math.random() * Math.PI * 2,
        s: Math.random() * 0.02 + 0.005
      });
    }
  }

  addEventListener('resize', resize);
  addEventListener('mousemove', e => { mx = e.clientX / w; my = e.clientY / h; });
  addEventListener('touchmove', e => {
    if (e.touches[0]) { mx = e.touches[0].clientX / w; my = e.touches[0].clientY / h; }
  });

  function draw() {
    ctx.clearRect(0, 0, w, h);
    for (const s of stars) {
      s.t += s.s;
      const tw = (Math.sin(s.t) + 1) / 2;
      const px = s.x + (mx - 0.5) * s.d * 20;
      const py = s.y + (my - 0.5) * s.d * 20;
      ctx.beginPath();
      ctx.arc(px, py, s.r * (0.6 + tw * 0.6), 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(220,216,208,' + (0.2 + tw * 0.6) + ')';
      ctx.fill();
    }
    requestAnimationFrame(draw);
  }

  resize();
  draw();
</script>
</body>
</html>
```

What: A dark, quiet landing page with a gentle parallax starfield that drifts and twinkles as you move the cursor, beside a short calm note saying the page exists for no reason at all.