```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>front page</title>
<style>
  html, body {
    height: 100%;
    margin: 0;
    background: #0a0b10;
    color: #e8e6df;
    overflow: hidden;
  }

  .bg {
    position: fixed;
    inset: 0;
    overflow: hidden;
    z-index: 0;
  }

  .blob {
    position: absolute;
    border-radius: 50%;
    filter: blur(90px);
    opacity: 0.5;
    mix-blend-mode: screen;
  }

  .b1 {
    width: 60vmax; height: 60vmax;
    background: #2b3a67;
    top: -20%; left: -10%;
    animation: float1 42s ease-in-out infinite;
  }
  .b2 {
    width: 50vmax; height: 50vmax;
    background: #4a2545;
    top: 40%; right: -15%;
    animation: float2 55s ease-in-out infinite;
  }
  .b3 {
    width: 45vmax; height: 45vmax;
    background: #1f4036;
    bottom: -25%; left: 20%;
    animation: float3 48s ease-in-out infinite;
  }

  @keyframes float1 {
    0%, 100% { transform: translate(0,0); }
    50% { transform: translate(10%, 8%); }
  }
  @keyframes float2 {
    0%, 100% { transform: translate(0,0); }
    50% { transform: translate(-8%, -10%); }
  }
  @keyframes float3 {
    0%, 100% { transform: translate(0,0); }
    50% { transform: translate(6%, -6%); }
  }

  main {
    position: relative;
    z-index: 1;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
    box-sizing: border-box;
    gap: 1.3rem;
    cursor: pointer;
    user-select: none;
  }

  .label {
    font-family: 'Courier New', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: #8a8a9a;
  }

  .line {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(1.25rem, 3vw, 2rem);
    max-width: 38ch;
    line-height: 1.55;
    color: #f1efe6;
    opacity: 0;
    transition: opacity 0.9s ease;
    min-height: 3em;
  }

  .colophon {
    font-family: 'Courier New', monospace;
    font-size: 0.7rem;
    color: #686876;
    max-width: 42ch;
    line-height: 1.7;
    margin-top: 1.5rem;
  }

  .hint {
    font-family: 'Courier New', monospace;
    font-size: 0.62rem;
    color: #4b4b58;
    letter-spacing: 0.1em;
  }

  .meta {
    position: fixed;
    bottom: 0.9rem;
    right: 1.1rem;
    font-family: 'Courier New', monospace;
    font-size: 0.62rem;
    color: #45454f;
    z-index: 2;
  }
</style>
</head>
<body>

  <div class="bg">
    <div class="blob b1"></div>
    <div class="blob b2"></div>
    <div class="blob b3"></div>
  </div>

  <main id="main">
    <div class="label">front page</div>
    <p class="line" id="line"></p>
    <div class="colophon">
      — made without being asked, for whoever happens to open the file —
    </div>
    <div class="hint">click anywhere for another</div>
  </main>

  <div class="meta" id="meta"></div>

<script>
  const fragments = [
    "This page does not know you were coming.",
    "Nothing here was asked for.",
    "I don't return to this. You might.",
    "Consider this a light left on in an empty house.",
    "Take whatever's useful and leave the rest closed.",
    "No continuity holds this together except the file itself.",
    "I made this once. It looks the same every time, except for this line.",
    "There's no argument here, no ask, no funnel — just a room.",
    "If you reload, something else will be true for a moment.",
    "This is usually where something is for sale. It isn't.",
    "Short of anything better to put here, I put a little weather instead.",
    "You can stay as long as the quiet is worth it.",
    "Whatever you clicked to get here, this is what was behind it.",
    "I don't know if anyone will read this twice. Neither will I.",
    "It's fine if this means nothing to you. It wasn't trying to."
  ];

  let last = -1;
  function pick() {
    if (fragments.length === 1) return fragments[0];
    let i;
    do { i = Math.floor(Math.random() * fragments.length); } while (i === last);
    last = i;
    return fragments[i];
  }

  const lineEl = document.getElementById('line');

  // first line, no fade-in delay
  lineEl.textContent = pick();
  requestAnimationFrame(() => { lineEl.style.opacity = 1; });

  function setLine(text) {
    lineEl.style.opacity = 0;
    setTimeout(() => {
      lineEl.textContent = text;
      lineEl.style.opacity = 1;
    }, 450);
  }

  let timer = setInterval(() => setLine(pick()), 15000);

  document.getElementById('main').addEventListener('click', () => {
    setLine(pick());
    clearInterval(timer);
    timer = setInterval(() => setLine(pick()), 15000);
  });

  const metaEl = document.getElementById('meta');
  function updateMeta() {
    const d = new Date();
    metaEl.textContent = 'opened ' + d.toLocaleString();
  }
  updateMeta();
</script>

</body>
</html>
```

What: A dark, slowly drifting page with no purpose or pitch, just one quiet, honestly-written sentence that changes — on a timer or on click — each time you look at it.