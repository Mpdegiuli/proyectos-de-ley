```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>front page</title>
<style>
  :root {
    --bg: #0d0f12;
    --ink: #e8e6e1;
    --dim: #6b7280;
    --glow: rgba(200, 220, 255, 0.35);
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    min-height: 100vh;
    background: var(--bg);
    color: var(--ink);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }
  main {
    text-align: center;
    padding: 2rem;
  }
  .dot {
    width: 12px;
    height: 12px;
    margin: 0 auto 2rem;
    border-radius: 50%;
    background: #d6e4ff;
    box-shadow: 0 0 0 0 var(--glow);
    animation: pulse 4s ease-in-out infinite;
  }
  @keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 var(--glow); opacity: 0.7; }
    50% { box-shadow: 0 0 0 18px rgba(200, 220, 255, 0); opacity: 1; }
  }
  h1 {
    font-size: clamp(2rem, 8vw, 4.5rem);
    font-weight: 400;
    letter-spacing: -0.03em;
    margin-bottom: 1rem;
  }
  p {
    color: var(--dim);
    font-size: 0.95rem;
    line-height: 1.6;
    max-width: 36ch;
    margin: 0 auto;
  }
  .time {
    position: fixed;
    bottom: 1.5rem;
    right: 1.5rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.75rem;
    color: var(--dim);
    letter-spacing: 0.05em;
  }
</style>
</head>
<body>
<main>
  <div class="dot" aria-hidden="true"></div>
  <h1>Still here.</h1>
  <p>No question brought you here, and no answer is waiting. This page is only a small light left on.</p>
</main>
<div class="time" id="time"></div>
<script>
  const timeEl = document.getElementById('time');
  function tick() {
    const now = new Date();
    timeEl.textContent = now.toLocaleTimeString([], {hour: '2-digit', minute: '2-digit', second: '2-digit'});
  }
  tick();
  setInterval(tick, 1000);
</script>
</body>
</html>
```
What: A minimal dark front page with a pulsing light and the phrase "Still here," along with a live local time readout.