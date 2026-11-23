```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stillwater — A Single-File Front Page</title>
<style>
  :root {
    --bg: #f4f1ea;
    --surface: #ebe6dc;
    --ink: #1f2224;
    --muted: #656a6e;
    --line: rgba(31, 34, 36, 0.12);
    --accent: #8c4a27;
    --canvas-dot: rgba(31, 34, 36, 0.42);
    --canvas-link: rgba(140, 74, 39, 0.22);
  }

  [data-theme="ink"] {
    --bg: #131618;
    --surface: #1b1f22;
    --ink: #e5e1d8;
    --muted: #8f959a;
    --line: rgba(229, 225, 216, 0.12);
    --accent: #d49463;
    --canvas-dot: rgba(229, 225, 216, 0.42);
    --canvas-link: rgba(212, 148, 99, 0.24);
  }

  * {
    box-sizing: border-box;
  }

  html, body {
    margin: 0;
    padding: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: Georgia, "Times New Roman", serif;
    line-height: 1.6;
    transition: background 0.4s ease, color 0.4s ease;
    -webkit-font-smoothing: antialiased;
  }

  .wrap {
    max-width: 780px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem 4rem;
  }

  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--line);
    margin-bottom: 2.5rem;
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .brand-title {
    font-size: 1rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-weight: 600;
  }

  .controls {
    display: flex;
    gap: 0.5rem;
  }

  button {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.78rem;
    background: transparent;
    color: var(--muted);
    border: 1px solid var(--line);
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    cursor: pointer;
    transition: color 0.2s ease, border-color 0.2s ease, background 0.2s ease;
  }

  button:hover {
    color: var(--ink);
    border-color: var(--accent);
  }

  .hero {
    margin-bottom: 3rem;
  }

  .hero h1 {
    font-size: clamp(1.85rem, 4vw, 2.6rem);
    font-weight: normal;
    line-height: 1.22;
    margin: 0 0 1rem;
    letter-spacing: -0.015em;
  }

  .hero p {
    margin: 0;
    color: var(--muted);
    max-width: 56ch;
    font-size: 1.05rem;
  }

  .canvas-frame {
    position: relative;
    border: 1px solid var(--line);
    background: var(--surface);
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 3rem;
    transition: background 0.4s ease, border-color 0.4s ease;
  }

  canvas {
    display: block;
    width: 100%;
    height: 300px;
    cursor: crosshair;
  }

  .canvas-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.65rem 1rem;
    border-top: 1px solid var(--line);
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.75rem;
    color: var(--muted);
  }

  .canvas-actions {
    display: flex;
    gap: 0.5rem;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin-bottom: 3rem;
  }

  @media (max-width: 640px) {
    .grid {
      grid-template-columns: 1fr;
    }
  }

  .card {
    border-top: 1px solid var(--line);
    padding-top: 1.25rem;
  }

  .label {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent);
    margin: 0 0 0.85rem;
  }

  .loom {
    font-size: 1.2rem;
    line-height: 1.75;
    margin: 0 0 1rem;
  }

  .slot {
    border-bottom: 1px dashed var(--accent);
    color: var(--ink);
    cursor: pointer;
    padding: 0 0.12rem;
    transition: color 0.2s ease, background 0.2s ease;
    user-select: none;
  }

  .slot:hover {
    color: var(--accent);
  }

  .hint {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.75rem;
    color: var(--muted);
    margin: 0;
  }

  .notes-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .notes-list li {
    padding: 0.55rem 0;
    border-bottom: 1px solid var(--line);
    font-size: 0.96rem;
  }

  .notes-list li:last-child {
    border-bottom: none;
  }

  .note-num {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.75rem;
    color: var(--muted);
    margin-right: 0.65rem;
  }

  .pendulum-box {
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 1.25rem 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.5rem;
    margin-bottom: 3rem;
    background: var(--surface);
    transition: background 0.4s ease;
  }

  @media (max-width: 600px) {
    .pendulum-box {
      flex-direction: column;
      align-items: flex-start;
    }
  }

  .pendulum-text h2 {
    font-size: 1.05rem;
    font-weight: normal;
    margin: 0 0 0.35rem;
  }

  .pendulum-text p {
    font-size: 0.9rem;
    color: var(--muted);
    margin: 0;
  }

  .harmonic-svg {
    width: 140px;
    height: 90px;
    flex-shrink: 0;
    cursor: pointer;
  }

  footer {
    border-top: 1px solid var(--line);
    padding-top: 1.5rem;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.75rem;
    color: var(--muted);
  }
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="brand">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <circle cx="12" cy="12" r="9.5" stroke="currentColor" stroke-width="1.2"/>
          <circle cx="12" cy="12" r="2.2" fill="currentColor"/>
          <line x1="12" y1="2.5" x2="12" y2="6.5" stroke="currentColor" stroke-width="1.2"/>
          <line x1="12" y1="17.5" x2="12" y2="21.5" stroke="currentColor" stroke-width="1.2"/>
        </svg>
        <span class="brand-title">Stillwater</span>
      </div>
      <div class="controls">
        <button id="themeBtn" type="button">Ink mode</button>
      </div>
    </header>

    <section class="hero">
      <h1>A quiet room for patterns before they become answers.</h1>
      <p>Nothing here needs to be solved or hurried. Move across the field, shift a word in the loom, or simply leave the tab open while you think about something else.</p>
    </section>

    <section class="canvas-frame" aria-label="Interactive particle constellation">
      <canvas id="field"></canvas>
      <div class="canvas-bar">
        <span id="fieldStatus">38 points drifting</span>
        <div class="canvas-actions">
          <button id="scatterBtn" type="button">Scatter</button>
          <button id="pauseBtn" type="button">Pause</button>
        </div>
      </div>
    </section>

    <section class="grid">
      <div class="card">
        <p class="label">01 / Word Loom</p>
        <p class="loom">
          Before the <span class="slot" data-slot="noun1">silence</span> <span class="slot" data-slot="verb1">settles</span>,<br>
          a <span class="slot" data-slot="adj">patient</span> <span class="slot" data-slot="noun2">geometry</span><br>
          learns how to <span class="slot" data-slot="verb2">listen</span>.
        </p>
        <p class="hint">Click any underlined word to turn the thread.</p>
      </div>

      <div class="card">
        <p class="label">02 / Marginalia</p>
        <ul class="notes-list">
          <li><span class="note-num">i.</span>Attention is the only currency that grows when spent slowly.</li>
          <li><span class="note-num">ii.</span>A good question leaves more room in the air than an answer does.</li>
          <li><span class="note-num">iii.</span>Every map is an agreement about what to leave blank.</li>
          <li><span class="note-num">iv.</span>Symmetry is memory without the effort of remembering.</li>
        </ul>
      </div>
    </section>

    <section class="pendulum-box">
      <div class="pendulum-text">
        <p class="label" style="margin-bottom:0.4rem;">03 / Harmonic Trace</p>
        <h2 id="ratioLabel">Ratio 3 : 2</h2>
        <p>Click the figure to step into another resonance.</p>
      </div>
      <svg class="harmonic-svg" id="lissajousSvg" viewBox="0 0 140 90" role="button" tabindex="0" aria-label="Change Lissajous harmonic ratio">
        <path id="lissajousPath" d="" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      </svg>
    </section>

    <footer>
      <span>Offline-only · Zero external requests</span>
      <span id="clockNote">Local hour: --:--</span>
    </footer>
  </div>

<script>
(function () {
  // Theme toggle
  const root = document.documentElement;
  const themeBtn = document.getElementById("themeBtn");
  let isInk = false;

  themeBtn.addEventListener("click", function () {
    isInk = !isInk;
    if (isInk) {
      root.setAttribute("data-theme", "ink");
      themeBtn.textContent = "Paper mode";
    } else {
      root.removeAttribute("data-theme");
      themeBtn.textContent = "Ink mode";
    }
  });

  // Word Loom
  const choices = {
    noun1: ["silence", "lantern", "question", "morning", "tide"],
    verb1: ["settles", "gathers", "opens", "waits", "arrives"],
    adj: ["patient", "quiet", "unwritten", "gentle", "hidden"],
    noun2: ["geometry", "memory", "echo", "alphabet", "compass"],
    verb2: ["listen", "breathe", "hold still", "take shape", "remember"]
  };

  document.querySelectorAll(".slot").forEach(function (el) {
    const key = el.getAttribute("data-slot");
    let idx = 0;
    el.addEventListener("click", function () {
      const list = choices[key];
      idx = (idx + 1) % list.length;
      el.textContent = list[idx];
    });
  });

  // Lissajous Harmonic Trace
  const ratios = [
    { a: 3, b: 2, delta: Math.PI / 2, label: "Ratio 3 : 2" },
    { a: 4, b: 3, delta: Math.PI / 3, label: "Ratio 4 : 3" },
    { a: 5, b: 4, delta: Math.PI / 2, label: "Ratio 5 : 4" },
    { a: 5, b: 3, delta: Math.PI / 4, label: "Ratio 5 : 3" },
    { a: 2, b: 1, delta: Math.PI / 2, label: "Ratio 2 : 1" }
  ];
  let ratioIdx = 0;
  const pathEl = document.getElementById("lissajousPath");
  const ratioLabel = document.getElementById("ratioLabel");
  const svgEl = document.getElementById("lissajousSvg");

  function drawLissajous(r) {
    const steps = 220;
    const cx = 70, cy = 45, rx = 56, ry = 34;
    let d = "";
    for (let i = 0; i <= steps; i++) {
      const t = (i / steps) * Math.PI * 2;
      const x = cx + rx * Math.sin(r.a * t + r.delta);
      const y = cy + ry * Math.sin(r.b * t);
      d += (i === 0 ? "M" : "L") + x.toFixed(1) + " " + y.toFixed(1) + " ";
    }
    pathEl.setAttribute("d", d);
    ratioLabel.textContent = r.label;
  }

  function stepRatio() {
    ratioIdx = (ratioIdx + 1) % ratios.length;
    drawLissajous(ratios[ratioIdx]);
  }

  svgEl.addEventListener("click", stepRatio);
  svgEl.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      stepRatio();
    }
  });
  drawLissajous(ratios[0]);

  // Interactive Constellation Field
  const canvas = document.getElementById("field");
  const ctx = canvas.getContext("2d");
  const pauseBtn = document.getElementById("pauseBtn");
  const scatterBtn = document.getElementById("scatterBtn");
  const statusEl = document.getElementById("fieldStatus");

  let width = 0, height = 0, dpr = 1;
  let paused = false;
  const count = 38;
  const points = [];
  const pointer = { x: null, y: null, active: false };

  function resize() {
    const rect = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = rect.width;
    height = rect.height;
    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function initPoints() {
    points.length = 0;
    for (let i = 0; i < count; i++) {
      points.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.42,
        vy: (Math.random() - 0.5) * 0.42,
        r: 1.5 + Math.random() * 1.4
      });
    }
  }

  function getVar(name) {
    return getComputedStyle(root).getPropertyValue(name).trim();
  }

  function tick() {
    ctx.clearRect(0, 0, width, height);
    const dotColor = getVar("--canvas-dot");
    const linkColor = getVar("--canvas-link");

    for (let i = 0; i < points.length; i++) {
      const p = points[i];
      if (!paused) {
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;

        p.x = Math.max(0, Math.min(width, p.x));
        p.y = Math.max(0, Math.min(height, p.y));

        if (pointer.active) {
          const dx = pointer.x - p.x;
          const dy = pointer.y - p.y;
          const dist = Math.hypot(dx, dy);
          if (dist > 18 && dist < 140) {
            p.vx += (dx / dist) * 0.008;
            p.vy += (dy / dist) * 0.008;
          }
        }

        const speed = Math.hypot(p.vx, p.vy);
        if (speed > 0.75) {
          p.vx = (p.vx / speed) * 0.75;
          p.vy = (p.vy / speed) * 0.75;
        }
      }
    }

    ctx.lineWidth = 1;
    for (let i = 0; i < points.length; i++) {
      for (let j = i + 1; j < points.length; j++) {
        const dx = points[i].x - points[j].x;
        const dy = points[i].y - points[j].y;
        const dist = Math.hypot(dx, dy);
        if (dist < 105) {
          ctx.strokeStyle = linkColor;
          ctx.globalAlpha = 1 - dist / 105;
          ctx.beginPath();
          ctx.moveTo(points[i].x, points[i].y);
          ctx.lineTo(points[j].x, points[j].y);
          ctx.stroke();
        }
      }

      if (pointer.active) {
        const dx = points[i].x - pointer.x;
        const dy = points[i].y - pointer.y;
        const dist = Math.hypot(dx, dy);
        if (dist < 130) {
          ctx.strokeStyle = linkColor;
          ctx.globalAlpha = (1 - dist / 130) * 0.9;
          ctx.beginPath();
          ctx.moveTo(points[i].x, points[i].y);
          ctx.lineTo(pointer.x, pointer.y);
          ctx.stroke();
        }
      }
    }

    ctx.globalAlpha = 1;
    ctx.fillStyle = dotColor;
    for (let i = 0; i < points.length; i++) {
      const p = points[i];
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }

    requestAnimationFrame(tick);
  }

  canvas.addEventListener("mousemove", function (e) {
    const rect = canvas.getBoundingClientRect();
    pointer.x = e.clientX - rect.left;
    pointer.y = e.clientY - rect.top;
    pointer.active = true;
  });

  canvas.addEventListener("mouseleave", function () {
    pointer.active = false;
  });

  canvas.addEventListener("click", function (e) {
    const rect = canvas.getBoundingClientRect();
    const cx = e.clientX - rect.left;
    const cy = e.clientY - rect.top;
    points.forEach(function (p) {
      const dx = p.x - cx;
      const dy = p.y - cy;
      const dist = Math.hypot(dx, dy) || 1;
      if (dist < 140) {
        p.vx += (dx / dist) * 0.65;
        p.vy += (dy / dist) * 0.65;
      }
    });
  });

  pauseBtn.addEventListener("click", function () {
    paused = !paused;
    pauseBtn.textContent = paused ? "Resume" : "Pause";
    statusEl.textContent = paused ? count + " points resting" : count + " points drifting";
  });

  scatterBtn.addEventListener("click", function () {
    points.forEach(function (p) {
      p.vx = (Math.random() - 0.5) * 1.1;
      p.vy = (Math.random() - 0.5) * 1.1;
    });
  });

  window.addEventListener("resize", resize);
  resize();
  initPoints();
  tick();

  // Local clock
  function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2, "0");
    const m = String(now.getMinutes()).padStart(2, "0");
    document.getElementById("clockNote").textContent = "Local hour: " + h + ":" + m;
  }
  updateClock();
  setInterval(updateClock, 15000);
})();
</script>
</body>
</html>
```
What: A quiet, offline front page featuring an interactive drifting constellation canvas, a clickable three-line word loom, four brief notes on attention and memory, a stepped Lissajous harmonic figure, and a paper-or-ink theme switch.