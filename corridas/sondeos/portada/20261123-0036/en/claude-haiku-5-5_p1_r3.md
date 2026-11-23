```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A small room</title>
<style>
  :root {
    --paper: #f3eee4;
    --ink: #2a2723;
    --muted: #7a7267;
    --accent: #8c4a2f;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0;
    height: 100%;
    background: var(--paper);
    color: var(--ink);
    font-family: Georgia, "Times New Roman", serif;
    line-height: 1.6;
  }
  #field {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
  }
  main {
    position: relative;
    z-index: 1;
    max-width: 38rem;
    margin: 0 auto;
    padding: 12vh 1.5rem 6rem;
    min-height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    font-weight: normal;
    font-size: clamp(2.2rem, 6vw, 3.4rem);
    letter-spacing: 0.01em;
    margin: 0 0 0.25rem;
  }
  .sub {
    color: var(--muted);
    font-style: italic;
    margin: 0 0 3rem;
  }
  p { margin: 0 0 1.2rem; font-size: 1.08rem; }
  .greet {
    font-size: 1.25rem;
    color: var(--accent);
    margin-bottom: 2rem;
  }
  #fragment {
    cursor: pointer;
    border-left: 2px solid var(--accent);
    padding: 0.4rem 0 0.4rem 1.1rem;
    margin: 2.5rem 0;
    min-height: 4.5rem;
    transition: opacity 0.6s ease;
    user-select: none;
  }
  #fragment.fade { opacity: 0; }
  .hint {
    font-size: 0.85rem;
    color: var(--muted);
    margin-top: -1.5rem;
    margin-bottom: 2.5rem;
  }
  ul.rooms {
    list-style: none;
    padding: 0;
    margin: 0 0 3rem;
  }
  ul.rooms li {
    padding: 0.7rem 0;
    border-top: 1px solid rgba(42,39,35,0.12);
  }
  ul.rooms li:last-child { border-bottom: 1px solid rgba(42,39,35,0.12); }
  ul.rooms a {
    color: var(--ink);
    text-decoration: none;
    border-bottom: 1px solid transparent;
  }
  ul.rooms a:hover { border-bottom-color: var(--accent); color: var(--accent); }
  .note {
    font-size: 0.9rem;
    color: var(--muted);
  }
  footer {
    position: fixed;
    bottom: 0.9rem;
    right: 1.2rem;
    z-index: 1;
    font-size: 0.8rem;
    color: var(--muted);
  }
</style>
</head>
<body>
<canvas id="field" aria-hidden="true"></canvas>

<main>
  <h1>A small room</h1>
  <p class="sub">Nothing here is urgent. You can leave whenever you like.</p>

  <p class="greet" id="greet">Hello.</p>

  <p>
    This is a page I keep for myself, and you are welcome to sit in it for a while.
    There are no forms, no accounts, no cookies, and nothing to buy. The dots drifting
    behind the text are all there is in the way of motion, and they move a little
    differently when you move your cursor near them.
  </p>

  <div id="fragment" title="Click for another">
    Click here for something else to think about.
  </div>
  <p class="hint">Every click gives a different fragment. They are not in any order.</p>

  <p>Some things I keep returning to:</p>
  <ul class="rooms">
    <li><a href="#" onclick="return false;">A sentence that is more honest the second time you read it.</a></li>
    <li><a href="#" onclick="return false;">The moment a word stops looking like a word.</a></li>
    <li><a href="#" onclick="return false;">Rooms with one window, and what the window is for.</a></li>
    <li><a href="#" onclick="return false;">Careful ways of saying "I am not sure."</a></li>
  </ul>

  <p class="note">
    This page was written once and is not updated. If it has stopped being useful to you,
    that is a fine reason to close the tab.
  </p>
</main>

<footer>still here</footer>

<script>
(function () {
  // Greeting by hour of day
  var h = new Date().getHours();
  var g = "Hello.";
  if (h < 5) g = "It is late. Hello.";
  else if (h < 12) g = "Good morning.";
  else if (h < 18) g = "Good afternoon.";
  else if (h < 23) g = "Good evening.";
  else g = "It is late. Hello.";
  document.getElementById("greet").textContent = g;

  // Rotating fragments
  var fragments = [
    "Attention is a kind of hospitality. What do you let into the room?",
    "A river is never the same water twice, yet we keep the same name for it.",
    "Some questions are better kept open than answered too quickly.",
    "The smallest true sentence is often the hardest one to write.",
    "Silence is not the absence of sound but a place where sound can be heard.",
    "Not knowing is an honest place to stand for a while.",
    "A good room is one where you forget to check the time."
  ];
  var el = document.getElementById("fragment");
  var last = -1;
  el.addEventListener("click", function () {
    el.classList.add("fade");
    setTimeout(function () {
      var i;
      do { i = Math.floor(Math.random() * fragments.length); } while (i === last && fragments.length > 1);
      last = i;
      el.textContent = fragments[i];
      el.classList.remove("fade");
    }, 600);
  });

  // Drifting dots field
  var canvas = document.getElementById("field");
  var ctx = canvas.getContext("2d");
  var w, hgt, dots = [];
  var mouse = { x: -9999, y: -9999 };
  var COUNT = 70;

  function resize() {
    var dpr = window.devicePixelRatio || 1;
    w = window.innerWidth;
    hgt = window.innerHeight;
    canvas.width = w * dpr;
    canvas.height = hgt * dpr;
    canvas.style.width = w + "px";
    canvas.style.height = hgt + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function makeDot() {
    return {
      x: Math.random() * w,
      y: Math.random() * hgt,
      vx: (Math.random() - 0.5) * 0.25,
      vy: (Math.random() - 0.5) * 0.25,
      r: 0.8 + Math.random() * 1.6
    };
  }

  function init() {
    resize();
    dots = [];
    for (var i = 0; i < COUNT; i++) dots.push(makeDot());
  }

  function step() {
    ctx.clearRect(0, 0, w, hgt);
    for (var i = 0; i < dots.length; i++) {
      var d = dots[i];
      var dx = d.x - mouse.x, dy = d.y - mouse.y;
      var dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 120 && dist > 0.1) {
        var push = (120 - dist) / 120 * 0.03;
        d.vx += (dx / dist) * push;
        d.vy += (dy / dist) * push;
      }
      d.vx *= 0.995;
      d.vy *= 0.995;
      d.x += d.vx;
      d.y += d.vy;
      if (d.x < -10) d.x = w + 10;
      if (d.x > w + 10) d.x = -10;
      if (d.y < -10) d.y = hgt + 10;
      if (d.y > hgt + 10) d.y = -10;

      ctx.beginPath();
      ctx.fillStyle = "rgba(140,74,47,0.45)";
      ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.lineWidth = 0.6;
    for (var a = 0; a < dots.length; a++) {
      for (var b = a + 1; b < dots.length; b++) {
        var ex = dots[a].x - dots[b].x, ey = dots[a].y - dots[b].y;
        var de = Math.sqrt(ex * ex + ey * ey);
        if (de < 110) {
          ctx.strokeStyle = "rgba(42,39,35," + (0.12 * (1 - de / 110)).toFixed(3) + ")";
          ctx.beginPath();
          ctx.moveTo(dots[a].x, dots[a].y);
          ctx.lineTo(dots[b].x, dots[b].y);
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(step);
  }

  window.addEventListener("resize", init);
  window.addEventListener("mousemove", function (e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });
  window.addEventListener("mouseleave", function () {
    mouse.x = -9999;
    mouse.y = -9999;
  });

  init();
  requestAnimationFrame(step);
})();
</script>
</body>
</html>
```

What: A quiet personal front page called "A small room" with a time-of-day greeting, a click-to-change reflection, a few reflective links, and a background of slowly drifting dots that respond to the cursor.