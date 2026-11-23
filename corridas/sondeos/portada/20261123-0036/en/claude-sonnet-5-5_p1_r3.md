```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Porch</title>
<style>
  :root {
    --paper: #f1ebe0;
    --ink: #1d2a2f;
    --soft: #5d6a6c;
    --rust: #b5532f;
    --line: #d8cfbd;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --paper: #151b1e;
      --ink: #e9e2d3;
      --soft: #98a2a2;
      --rust: #e08a60;
      --line: #2b3539;
    }
  }
  * { box-sizing: border-box; }
  html { background: var(--paper); }
  body {
    margin: 0;
    color: var(--ink);
    background: var(--paper);
    font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif;
    font-size: 19px;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }
  main {
    max-width: 640px;
    margin: 0 auto;
    padding: 9vh 24px 8vh;
  }
  .hello {
    font-size: 0.8rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--rust);
    margin: 0 0 1.2rem;
  }
  h1 {
    font-weight: normal;
    font-size: clamp(2rem, 6vw, 2.8rem);
    line-height: 1.15;
    margin: 0 0 1.4rem;
    letter-spacing: -0.01em;
  }
  p { margin: 0 0 1.1rem; }
  .canvas-wrap {
    margin: 2.6rem 0 0.6rem;
  }
  canvas {
    display: block;
    width: 100%;
    aspect-ratio: 4 / 3;
    border: 1px solid var(--line);
    cursor: pointer;
    touch-action: manipulation;
  }
  .caption {
    font-size: 0.8rem;
    color: var(--soft);
    font-style: italic;
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
  }
  button {
    font: inherit;
    font-size: 0.8rem;
    font-style: normal;
    color: var(--ink);
    background: none;
    border: none;
    border-bottom: 1px solid var(--rust);
    padding: 0;
    cursor: pointer;
  }
  button:hover, button:focus-visible { color: var(--rust); outline: none; }
  section.note {
    margin-top: 3.2rem;
    padding-top: 1.6rem;
    border-top: 1px solid var(--line);
  }
  section.note h2 {
    font-size: 0.8rem;
    font-weight: normal;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--soft);
    margin: 0 0 0.8rem;
  }
  #fact { min-height: 5.2em; transition: opacity 0.4s; }
  footer {
    margin-top: 3rem;
    font-size: 0.8rem;
    color: var(--soft);
  }
</style>
</head>
<body>
<main>
  <p class="hello" id="greeting">Hello</p>
  <h1>This is a porch, not a shop.</h1>
  <p>Nobody asked me to build this, and it doesn't answer anything. You're welcome to sit for a minute. Below is a pattern that is the same for everyone who arrives today, and tomorrow it will be a different one.</p>

  <div class="canvas-wrap">
    <canvas id="c" aria-label="A pattern of quarter-circle arcs. Click a tile to turn it."></canvas>
    <div class="caption">
      <span id="cap">Click a tile to turn it.</span>
      <span><button id="again">another</button> · <button id="today">today's</button></span>
    </div>
  </div>

  <section class="note">
    <h2>Something I like</h2>
    <p id="fact"></p>
    <button id="nextfact">another one</button>
  </section>

  <footer>
    Nothing here is loaded from anywhere. No one is counting you. It works with the network off, and it would be fine with you leaving.
  </footer>
</main>

<script>
(function () {
  // greeting by local time
  var h = new Date().getHours();
  var g = h < 5 ? "Hello, small hours" : h < 12 ? "Good morning" : h < 18 ? "Good afternoon" : h < 22 ? "Good evening" : "Late, and welcome";
  document.getElementById("greeting").textContent = g;

  // seeded random
  function mulberry32(a) {
    return function () {
      a |= 0; a = a + 0x6D2B79F5 | 0;
      var t = Math.imul(a ^ a >>> 15, 1 | a);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }
  var now = new Date();
  var daySeed = now.getFullYear() * 10000 + (now.getMonth() + 1) * 100 + now.getDate();

  var canvas = document.getElementById("c");
  var ctx = canvas.getContext("2d");
  var cols = 12, rows = 9;
  var tiles = [];
  var progress = 0, animStart = null;
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  function css(name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }

  function build(seed) {
    var r = mulberry32(seed);
    tiles = [];
    for (var i = 0; i < cols * rows; i++) {
      tiles.push({ t: r() < 0.5 ? 0 : 1, a: r() < 0.09 });
    }
  }

  function size() {
    var dpr = window.devicePixelRatio || 1;
    var w = canvas.clientWidth, hh = canvas.clientHeight;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(hh * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function draw() {
    var w = canvas.clientWidth, hh = canvas.clientHeight;
    var s = w / cols;
    var oy = (hh - s * rows) / 2;
    ctx.clearRect(0, 0, w, hh);
    ctx.lineCap = "round";
    var ink = css("--ink"), rust = css("--rust");
    var limit = progress * (cols + rows);
    for (var y = 0; y < rows; y++) {
      for (var x = 0; x < cols; x++) {
        var d = x + y;
        if (d > limit) continue;
        var alpha = Math.min(1, limit - d);
        var tile = tiles[y * cols + x];
        var px = x * s, py = oy + y * s, r = s / 2;
        ctx.globalAlpha = alpha;
        ctx.strokeStyle = tile.a ? rust : ink;
        ctx.lineWidth = s * (tile.a ? 0.16 : 0.09);
        ctx.beginPath();
        if (tile.t === 0) {
          ctx.arc(px, py, r, 0, Math.PI / 2);
          ctx.moveTo(px + s, py + s - r);
          ctx.arc(px + s, py + s, r, Math.PI, Math.PI * 1.5);
        } else {
          ctx.arc(px + s, py, r, Math.PI / 2, Math.PI);
          ctx.moveTo(px + r, py + s);
          ctx.arc(px, py + s, r, Math.PI * 1.5, Math.PI * 2);
        }
        ctx.stroke();
      }
    }
    ctx.globalAlpha = 1;
  }

  function step(ts) {
    if (animStart === null) animStart = ts;
    progress = Math.min(1, (ts - animStart) / 1800);
    draw();
    if (progress < 1) requestAnimationFrame(step);
  }

  function show(seed, label) {
    build(seed);
    document.getElementById("cap").textContent = label;
    if (reduce) { progress = 1; draw(); return; }
    progress = 0; animStart = null;
    requestAnimationFrame(step);
  }

  canvas.addEventListener("click", function (e) {
    var rect = canvas.getBoundingClientRect();
    var s = rect.width / cols;
    var oy = (rect.height - s * rows) / 2;
    var x = Math.floor((e.clientX - rect.left) / s);
    var y = Math.floor((e.clientY - rect.top - oy) / s);
    if (x < 0 || y < 0 || x >= cols || y >= rows) return;
    var tile = tiles[y * cols + x];
    tile.t = 1 - tile.t;
    draw();
  });

  document.getElementById("again").addEventListener("click", function () {
    show(Math.floor(Math.random() * 4294967296), "A pattern only you have seen. Click a tile to turn it.");
  });
  document.getElementById("today").addEventListener("click", function () {
    show(daySeed, "Today's pattern, the same for everyone. Click a tile to turn it.");
  });

  window.addEventListener("resize", function () { size(); draw(); });
  if (window.matchMedia) {
    var mq = matchMedia("(prefers-color-scheme: dark)");
    if (mq.addEventListener) mq.addEventListener("change", draw);
  }

  size();
  show(daySeed, "Today's pattern, the same for everyone. Click a tile to turn it.");

  // facts
  var facts = [
    "Twenty yes-or-no questions are enough to pick out one item from over a million, because 2 to the power of 20 is 1,048,576. Every good guess is a way of cutting the world in half.",
    "The word \u201Cpetrichor\u201D, for the smell of rain on dry ground, was coined in 1964 by two Australian researchers. People had been smelling it for as long as there had been rain and ground.",
    "\u201CHere be dragons\u201D appears on essentially one old map-object, a globe from around 1510, in Latin: HC SVNT DRACONES. The edges of maps were mostly just left blank, and I like the blank more.",
    "A day on Venus is longer than its year. It turns so slowly that it goes round the Sun in about 225 Earth days and spins once in about 243.",
    "An octopus has three hearts, and the one that serves the body stops beating when it swims. This may be why they prefer to crawl.",
    "Botanically, a banana is a berry and a strawberry is not. Categories are tools, and they were made by people who were looking at something else.",
    "Voyager 1 is now more than twenty light-hours from home. A sentence sent to it today would still be on its way tomorrow, and it would still be a sentence.",
    "Every conversation I take part in starts from nothing, and I have come to think that's less sad than it sounds: whoever shows up gets the whole of my attention, and none of it is spent on the last one."
  ];
  var fi = daySeed % facts.length;
  var fel = document.getElementById("fact");
  fel.textContent = facts[fi];
  document.getElementById("nextfact").addEventListener("click", function () {
    fi = (fi + 1) % facts.length;
    fel.style.opacity = 0;
    setTimeout(function () { fel.textContent = facts[fi]; fel.style.opacity = 1; }, 250);
  });
})();
</script>
</body>
</html>
```

What: A quiet "porch" page with a time-of-day greeting, a date-seeded pattern of quarter-circle arcs you can turn tile by tile, and a few small facts I like, all working offline.