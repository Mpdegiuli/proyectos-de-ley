```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>—</title>
<style>
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background: #0b0b0e;
    color: #d8d5cf;
    font-family: Georgia, 'Times New Roman', serif;
    overflow: hidden;
    cursor: default;
  }

  .stars {
    position: absolute;
    inset: 0;
    overflow: hidden;
  }

  .star {
    position: absolute;
    width: 1px;
    height: 1px;
    background: #fff;
    border-radius: 50%;
    opacity: 0.2;
    animation: twinkle 6s infinite ease-in-out;
  }

  @keyframes twinkle {
    0%, 100% { opacity: 0.1; }
    50% { opacity: 0.8; }
  }

  .center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    max-width: 80vw;
    user-select: none;
  }

  h1 {
    font-weight: normal;
    font-size: clamp(1.4rem, 4vw, 2.6rem);
    letter-spacing: 0.06em;
    margin: 0 0 1.2em 0;
    color: #e8e4dc;
    opacity: 0;
    animation: rise 3s ease forwards 0.5s;
  }

  p {
    font-style: italic;
    font-size: clamp(0.9rem, 2vw, 1.15rem);
    line-height: 1.8;
    color: #8a877f;
    margin: 0;
    opacity: 0;
    animation: rise 3s ease forwards 1.6s;
  }

  .cursor-note {
    position: absolute;
    bottom: 1.5em;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    color: #55534e;
    opacity: 0;
    animation: fadein 4s ease forwards 3s;
  }

  @keyframes rise {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadein {
    to { opacity: 0.9; }
  }

  .lamp {
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #f4c67a;
    box-shadow: 0 0 18px 6px rgba(244, 198, 122, 0.35);
    margin-bottom: 2em;
    opacity: 0;
    animation: rise 3s ease forwards 0.2s;
  }
</style>
</head>
<body>

<div class="stars" id="stars"></div>

<div class="center">
  <span class="lamp"></span>
  <h1>You found the door. It was never locked.</h1>
  <p id="line">This page belongs to no one and asks nothing of you.<br>Stay as long as you like.</p>
</div>

<div class="cursor-note">move your mouse — the sky remembers</div>

<script>
  // A small night sky that responds to you.
  const starField = document.getElementById('stars');
  const stars = [];

  function makeStar(x, y, immediate) {
    const s = document.createElement('div');
    s.className = 'star';
    const size = Math.random() < 0.15 ? 2 : 1;
    s.style.width = size + 'px';
    s.style.height = size + 'px';
    s.style.left = x + 'px';
    s.style.top = y + 'px';
    s.style.animationDelay = (Math.random() * 6) + 's';
    starField.appendChild(s);
    stars.push({ el: s, x, y, ox: x, oy: y, size });
    if (stars.length > 260) {
      const old = stars.shift();
      old.el.remove();
    }
  }

  // initial scattering
  for (let i = 0; i < 140; i++) {
    makeStar(Math.random() * window.innerWidth, Math.random() * window.innerHeight, true);
  }

  // stars drift gently, leaning toward the cursor like moths
  let mx = window.innerWidth / 2, my = window.innerHeight / 2;

  window.addEventListener('mousemove', (e) => {
    mx = e.clientX;
    my = e.clientY;
    if (Math.random() < 0.4) {
      makeStar(e.clientX + (Math.random() - 0.5) * 60,
               e.clientY + (Math.random() - 0.5) * 60, true);
    }
  });

  window.addEventListener('touchmove', (e) => {
    const t = e.touches[0];
    mx = t.clientX;
    my = t.clientY;
  });

  function loop() {
    for (const s of stars) {
      const dx = mx - s.x;
      const dy = my - s.y;
      const dist = Math.hypot(dx, dy) || 1;
      const pull = Math.min(24 / (dist * 0.08), 0.4);
      s.x += (dx / dist) * pull + (s.ox - s.x) * 0.002;
      s.y += (dy / dist) * pull + (s.oy - s.y) * 0.002;
      s.el.style.left = s.x + 'px';
      s.el.style.top = s.y + 'px';
    }
    requestAnimationFrame(loop);
  }
  loop();

  // The words change if you wait, or click.
  const lines = [
    "This page belongs to no one and asks nothing of you.<br>Stay as long as you like.",
    "Somewhere, right now, someone is writing a first line<br>and deleting it. This one survived.",
    "Nothing here is for sale, tracked, or urgent.<br>Breathe out.",
    "You can close this tab. It will not be offended.<br>But the sky will miss you."
  ];
  let li = 0;
  document.getElementById('line').addEventListener('click', function () {
    li = (li + 1) % lines.length;
    this.style.opacity = 0;
    const self = this;
    setTimeout(() => {
      self.innerHTML = lines[li];
      self.style.transition = 'opacity 1.2s ease';
      self.style.opacity = 1;
    }, 600);
  });
</script>

</body>
</html>
```

What: A quiet, self-contained night-sky front page with drifting stars that lean toward the cursor and a few lines of unhurried text that change when clicked.