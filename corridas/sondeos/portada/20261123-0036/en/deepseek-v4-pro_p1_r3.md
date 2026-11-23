```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A Quiet Page</title>
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  html,
  body {
    height: 100%;
  }
  body {
    background: #0b0e14;
    color: #eae6dd;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    user-select: none;
  }
  canvas {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
  }
  main {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 2rem;
    opacity: 0;
    animation: fadeIn 5s ease forwards;
    transition: transform 0.2s ease-out;
    will-change: transform;
  }
  h1 {
    font-size: clamp(2.5rem, 8vw, 6rem);
    font-weight: 300;
    letter-spacing: 0.03em;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 30px rgba(255, 244, 214, 0.3);
  }
  p {
    font-size: clamp(1rem, 2.5vw, 1.5rem);
    font-weight: 300;
    opacity: 0.75;
    letter-spacing: 0.02em;
  }
  footer {
    position: fixed;
    bottom: 1.5rem;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 1;
    font-size: 0.8rem;
    opacity: 0.5;
    letter-spacing: 0.08em;
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
</style>
</head>
<body>
<canvas id="space"></canvas>
<main>
  <h1>You are here.</h1>
  <p>There is nothing required of you on this page.</p>
</main>
<footer>a front page, left open</footer>
<script>
  const canvas = document.getElementById('space');
  const ctx = canvas.getContext('2d');
  let stars = [];
  const STAR_COUNT = 180;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function makeStars() {
    stars = [];
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 1.2 + 0.2,
        baseOpacity: Math.random() * 0.6 + 0.2,
        speed: Math.random() * 0.0004 + 0.0002,
        phase: Math.random() * Math.PI * 2,
        drift: Math.random() * 0.1 + 0.02
      });
    }
  }

  function draw(timestamp) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const time = timestamp * 0.001;
    for (const star of stars) {
      const opacity = star.baseOpacity * (0.6 + 0.4 * Math.sin(time * 2 + star.phase));
      const x = star.x + Math.sin(time * 0.2 + star.phase) * 5;
      const y = star.y + Math.cos(time * 0.15 + star.phase) * 5;
      ctx.beginPath();
      ctx.arc(x, y, star.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 244, 214, ${opacity})`;
      ctx.fill();
    }
    requestAnimationFrame(draw);
  }

  resize();
  makeStars();
  requestAnimationFrame(draw);

  window.addEventListener('resize', () => {
    resize();
    makeStars();
  });

  window.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth - 0.5) * 10;
    const y = (e.clientY / window.innerHeight - 0.5) * 10;
    document.querySelector('main').style.transform = `translate(${x}px, ${y}px)`;
  });
</script>
</body>
</html>
```
What: A quiet, offline front page with a slow starfield and the message “You are here.”