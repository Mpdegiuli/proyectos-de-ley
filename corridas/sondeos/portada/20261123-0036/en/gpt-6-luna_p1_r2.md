```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f2eee5">
  <title>The Unfinished Atlas</title>
  <style>
    :root {
      color-scheme: light;
      --paper: #f2eee5;
      --ink: #222b28;
      --muted: #68736b;
      --line: #d7d2c6;
      --green: #526b5a;
      --rust: #b75f43;
      --blue: #93afb0;
      --serif: Georgia, "Times New Roman", serif;
      --sans: "Trebuchet MS", Arial, sans-serif;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      background:
        radial-gradient(ellipse at 83% 9%, rgba(207, 194, 158, .17), transparent 28rem),
        var(--paper);
      color: var(--ink);
      font-family: var(--sans);
      line-height: 1.55;
    }

    a { color: inherit; }

    .page {
      width: min(1160px, calc(100% - 64px));
      margin: 0 auto;
    }

    .masthead {
      min-height: 86px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--line);
      gap: 24px;
    }

    .wordmark {
      text-decoration: none;
      font-size: .78rem;
      font-weight: 700;
      letter-spacing: .16em;
      text-transform: uppercase;
    }

    .wordmark span {
      color: var(--rust);
      padding-right: 7px;
    }

    nav {
      display: flex;
      gap: clamp(16px, 3vw, 38px);
      font-size: .78rem;
      color: var(--muted);
    }

    nav a {
      text-decoration: none;
      transition: color .2s ease;
    }

    nav a:hover, nav a:focus-visible { color: var(--rust); }

    .hero {
      min-height: 610px;
      padding: 76px 0 68px;
      display: grid;
      grid-template-columns: 1fr 1.02fr;
      align-items: center;
      gap: clamp(36px, 7vw, 92px);
    }

    .eyebrow {
      margin: 0 0 22px;
      color: var(--rust);
      font-size: .72rem;
      font-weight: 700;
      letter-spacing: .19em;
      text-transform: uppercase;
    }

    h1, h2, h3, p { margin-top: 0; }

    h1 {
      max-width: 560px;
      margin-bottom: 24px;
      font: 400 clamp(3.35rem, 7vw, 6.7rem)/.94 var(--serif);
      letter-spacing: -.065em;
    }

    .intro {
      max-width: 410px;
      margin-bottom: 32px;
      color: #59645c;
      font: 1.05rem/1.75 var(--serif);
    }

    .coordinates {
      display: flex;
      align-items: center;
      gap: 12px;
      color: var(--muted);
      font-size: .72rem;
      letter-spacing: .08em;
      text-transform: uppercase;
    }

    .coordinates::before {
      content: "";
      display: block;
      width: 27px;
      height: 1px;
      background: var(--rust);
    }

    .landscape {
      position: relative;
      min-height: 405px;
      overflow: hidden;
      border-radius: 48% 48% 4px 4px / 42% 42% 4px 4px;
      background: #dce2d9;
      isolation: isolate;
    }

    .landscape::after {
      content: "";
      position: absolute;
      inset: 0;
      z-index: -1;
      background: linear-gradient(180deg, rgba(255,255,255,.1), rgba(45,67,55,.06));
    }

    .sun {
      position: absolute;
      top: 17%;
      left: 56%;
      width: 76px;
      height: 76px;
      border-radius: 50%;
      background: #d5a16f;
      box-shadow: 0 0 0 17px rgba(213,161,111,.12), 0 0 0 38px rgba(213,161,111,.08);
    }

    .hill {
      position: absolute;
      left: -10%;
      width: 125%;
      border-radius: 50% 50% 0 0 / 24% 24% 0 0;
    }

    .hill-back {
      bottom: 20%;
      height: 41%;
      background: #a8b9a6;
      transform: rotate(-8deg);
    }

    .hill-mid {
      bottom: 4%;
      height: 43%;
      left: 14%;
      width: 110%;
      background: #758d78;
      transform: rotate(9deg);
    }

    .hill-front {
      bottom: -16%;
      height: 42%;
      left: -22%;
      background: #526b5a;
      transform: rotate(-5deg);
    }

    .river {
      position: absolute;
      z-index: 2;
      width: 25%;
      height: 55%;
      left: 46%;
      bottom: -18%;
      border-radius: 50% 50% 0 0;
      background: #a7c1bd;
      transform: rotate(19deg);
      clip-path: polygon(38% 0, 75% 0, 100% 100%, 0 100%);
      opacity: .9;
    }

    .tree {
      position: absolute;
      z-index: 3;
      bottom: 26%;
      width: 4px;
      height: 91px;
      background: #3d5747;
      transform-origin: bottom;
    }

    .tree::before, .tree::after {
      content: "";
      position: absolute;
      bottom: 35px;
      left: 50%;
      width: 39px;
      height: 54px;
      background: #526b5a;
      clip-path: polygon(50% 0, 100% 100%, 0 100%);
      transform: translateX(-50%);
    }

    .tree::after {
      bottom: 57px;
      width: 29px;
      height: 42px;
      background: #607b64;
    }

    .tree.one { left: 24%; transform: scale(.86) rotate(-3deg); }
    .tree.two { left: 79%; bottom: 22%; transform: scale(1.14) rotate(4deg); }

    .scene-label {
      position: absolute;
      z-index: 4;
      right: 22px;
      bottom: 20px;
      color: rgba(255,255,255,.86);
      font-size: .65rem;
      letter-spacing: .13em;
      text-transform: uppercase;
    }

    .section-heading {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 20px;
      padding: 21px 0;
      border-top: 1px solid var(--line);
    }

    .section-heading h2 {
      margin: 0;
      font: 400 1.75rem var(--serif);
      letter-spacing: -.03em;
    }

    .section-heading span {
      color: var(--muted);
      font-size: .72rem;
      letter-spacing: .1em;
      text-transform: uppercase;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
    }

    .card {
      min-height: 224px;
      padding: 26px 28px 30px 0;
    }

    .card + .card {
      padding-left: 28px;
      border-left: 1px solid var(--line);
    }

    .card-index {
      color: var(--rust);
      font-size: .7rem;
      letter-spacing: .12em;
    }

    .card h3 {
      margin: 20px 0 10px;
      font: 400 1.55rem var(--serif);
    }

    .card p {
      max-width: 280px;
      margin-bottom: 0;
      color: var(--muted);
      font-size: .9rem;
      line-height: 1.7;
    }

    .note {
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      gap: 32px;
      padding: 65px 0 70px;
    }

    .note blockquote {
      margin: 0;
      max-width: 760px;
      font: 400 clamp(1.65rem, 3.5vw, 2.8rem)/1.25 var(--serif);
      letter-spacing: -.035em;
    }

    .note cite {
      display: block;
      margin-top: 16px;
      color: var(--muted);
      font: normal .7rem var(--sans);
      letter-spacing: .12em;
      text-transform: uppercase;
    }

    button {
      appearance: none;
      border: 1px solid #a8afa4;
      border-radius: 50px;
      padding: 12px 17px;
      background: transparent;
      color: var(--ink);
      font: 700 .72rem var(--sans);
      letter-spacing: .07em;
      text-transform: uppercase;
      cursor: pointer;
      transition: background .2s, color .2s, border-color .2s;
    }

    button:hover, button:focus-visible {
      background: var(--green);
      border-color: var(--green);
      color: white;
    }

    footer {
      min-height: 82px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: .72rem;
    }

    footer p { margin: 0; }
    .footer-mark { color: var(--rust); }

    @media (max-width: 760px) {
      .page { width: min(100% - 40px, 560px); }
      .masthead { min-height: 72px; }
      nav { gap: 14px; font-size: .7rem; }
      .hero {
        min-height: 0;
        padding: 62px 0 54px;
        grid-template-columns: 1fr;
        gap: 38px;
      }
      h1 { max-width: 480px; }
      .landscape { min-height: 350px; }
      .grid { grid-template-columns: 1fr; }
      .card, .card + .card {
        min-height: 0;
        padding: 24px 0;
        border-left: 0;
      }
      .card + .card { border-top: 1px solid var(--line); }
      .card h3 { margin-top: 13px; }
      .note { grid-template-columns: 1fr; padding: 48px 0; }
      .note button { justify-self: start; }
    }

    @media (max-width: 430px) {
      .page { width: calc(100% - 32px); }
      .masthead { align-items: flex-start; padding: 20px 0 16px; flex-direction: column; }
      nav { width: 100%; justify-content: space-between; }
      .landscape { min-height: 290px; }
      footer { align-items: flex-start; flex-direction: column; justify-content: center; padding: 20px 0; }
    }

    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      *, *::before, *::after { transition-duration: .01ms !important; }
    }
  </style>
</head>
<body>
  <div class="page">
    <header class="masthead">
      <a class="wordmark" href="#top"><span>✳</span>The Unfinished Atlas</a>
      <nav aria-label="Main navigation">
        <a href="#noticings">Noticings</a>
        <a href="#kept">Things kept</a>
        <a href="#margin">The margin</a>
      </nav>
    </header>

    <main id="top">
      <section class="hero" aria-labelledby="title">
        <div>
          <p class="eyebrow">A personal field guide · Vol. 01</p>
          <h1 id="title">The world, in passing.</h1>
          <p class="intro">
            I collect small proof that the world is still here: a window lit at dusk,
            the particular hush before rain, the names people give to ordinary things.
            This is where I leave a few of them.
          </p>
          <p class="coordinates">Somewhere between noticing and remembering</p>
        </div>

        <div class="landscape" role="img" aria-label="A quiet, imagined landscape with green hills, a winding river, trees, and a low sun">
          <div class="sun"></div>
          <div class="hill hill-back"></div>
          <div class="hill hill-mid"></div>
          <div class="river"></div>
          <div class="hill hill-front"></div>
          <div class="tree one"></div>
          <div class="tree two"></div>
          <span class="scene-label">A place I made up</span>
        </div>
      </section>

      <section id="noticings" aria-labelledby="noticings-title">
        <div class="section-heading">
          <h2 id="noticings-title">Recent noticings</h2>
          <span>Filed without urgency</span>
        </div>
        <div class="grid">
          <article class="card">
            <span class="card-index">01 / LIGHT</span>
            <h3>The blue hour</h3>
            <p>For a few minutes, every building looks like it’s remembering a different life.</p>
          </article>
          <article class="card">
            <span class="card-index">02 / LANGUAGE</span>
            <h3>Good words</h3>
            <p>“Apricity”: the warmth of the sun on a cold day. A word with its own little blanket.</p>
          </article>
          <article class="card">
            <span class="card-index">03 / SOUND</span>
            <h3>Kitchen weather</h3>
            <p>Kettle, rain, somebody turning a page. The small orchestra of staying in.</p>
          </article>
        </div>
      </section>

      <section class="note" id="kept" aria-label="A note to keep">
        <div>
          <blockquote id="thought">“Pay attention. Be astonished. Tell about it.”</blockquote>
          <cite id="attribution">A note in the margin</cite>
        </div>
        <button id="shuffle" type="button">Turn over a thought ↗</button>
      </section>
    </main>

    <footer id="margin">
      <p><span class="footer-mark">✳</span> Made slowly, for no particular reason.</p>
      <p>There is always more outside the frame.</p>
    </footer>
  </div>

  <script>
    const thoughts = [
      ["“Pay attention. Be astonished. Tell about it.”", "A note in the margin"],
      ["“Nothing is so small that it cannot be loved.”", "A thought for the pocket"],
      ["“The ordinary is a doorway, if you stand still long enough.”", "From an imaginary notebook"],
      ["“Some days the whole adventure is getting home before the light goes.”", "Field note, untitled"]
    ];

    let current = 0;
    const thought = document.getElementById("thought");
    const attribution = document.getElementById("attribution");

    document.getElementById("shuffle").addEventListener("click", () => {
      current = (current + 1) % thoughts.length;
      thought.textContent = thoughts[current][0];
      attribution.textContent = thoughts[current][1];
    });
  </script>
</body>
</html>
```

What: A quiet, illustrated field guide to small observations, with a few notes and a button that turns over a thought.