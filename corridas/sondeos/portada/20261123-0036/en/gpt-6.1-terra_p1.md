```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>The Quiet Observatory</title>
  <style>
    :root {
      --paper: #f3f0e7;
      --ink: #25332f;
      --muted: #68736b;
      --line: #c9cec2;
      --orange: #c65c3d;
      --sky: #cbdad1;
      --orb: #f5e6bc;
      --star: #f6f2dc;
      --hill-back: #8fa99a;
      --hill-front: #49685b;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font-family: Georgia, "Times New Roman", serif;
    }

    .page {
      width: min(1120px, calc(100% - 48px));
      margin: auto;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      padding: 25px 0;
      border-bottom: 1px solid var(--line);
      font: 700 11px/1.2 Arial, sans-serif;
      letter-spacing: .14em;
      text-transform: uppercase;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand-mark {
      display: grid;
      width: 30px;
      height: 30px;
      place-items: center;
      border: 1px solid var(--ink);
      border-radius: 50%;
      font-size: 17px;
      font-weight: normal;
      letter-spacing: 0;
    }

    header a {
      color: inherit;
      text-decoration: none;
    }

    header a:hover { text-decoration: underline; }

    .hero {
      display: grid;
      grid-template-columns: .9fr 1.1fr;
      gap: clamp(30px, 6vw, 80px);
      align-items: center;
      padding: clamp(58px, 8vw, 110px) 0;
    }

    .eyebrow, .label, .number, .scene-caption, footer {
      font: 700 10px/1.4 Arial, sans-serif;
      letter-spacing: .16em;
      text-transform: uppercase;
    }

    .eyebrow {
      color: var(--orange);
      margin: 0 0 24px;
    }

    h1 {
      margin: 0;
      max-width: 7em;
      font-size: clamp(56px, 7.5vw, 96px);
      font-weight: normal;
      letter-spacing: -.055em;
      line-height: .96;
    }

    h1 em {
      color: var(--orange);
      font-weight: normal;
    }

    .intro {
      max-width: 355px;
      margin: 30px 0 0;
      color: #59665d;
      font-size: 18px;
      line-height: 1.65;
    }

    .art-wrap { min-width: 0; }

    .art {
      position: relative;
      overflow: hidden;
      aspect-ratio: 1 / 1;
      background: var(--sky);
      border-radius: 50% 50% 4px 4px;
      transition: background 600ms ease;
    }

    .art svg {
      display: block;
      width: 100%;
      height: 100%;
    }

    .orb { fill: var(--orb); transition: fill 600ms ease; }
    .stars { fill: var(--star); opacity: .7; }
    .back-hill { fill: var(--hill-back); transition: fill 600ms ease; }
    .front-hill { fill: var(--hill-front); transition: fill 600ms ease; }

    .art.dusk {
      --sky: #c98e7c;
      --orb: #f6d7a8;
      --star: #f8e6c9;
      --hill-back: #a27672;
      --hill-front: #5b5f59;
    }

    .art.night {
      --sky: #263d48;
      --orb: #e8e1c8;
      --star: #f6f2dc;
      --hill-back: #465f60;
      --hill-front: #283f39;
    }

    .scene-caption {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      min-height: 48px;
      color: var(--muted);
    }

    button {
      border: 0;
      padding: 8px 0;
      background: none;
      color: var(--ink);
      cursor: pointer;
      font: inherit;
      letter-spacing: inherit;
      text-transform: inherit;
      text-decoration: underline;
      text-underline-offset: 4px;
    }

    button:hover { color: var(--orange); }
    button:focus-visible, a:focus-visible {
      outline: 2px solid var(--orange);
      outline-offset: 5px;
    }

    .collection {
      padding: 35px 0 80px;
      border-top: 1px solid var(--line);
    }

    .section-heading {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      align-items: baseline;
      margin-bottom: 36px;
    }

    .section-heading h2 {
      margin: 0;
      font-size: clamp(29px, 4vw, 42px);
      font-weight: normal;
      letter-spacing: -.035em;
    }

    .label { color: var(--muted); }

    .notes {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 36px;
    }

    .note {
      border-top: 1px solid var(--ink);
      padding-top: 16px;
    }

    .number { color: var(--orange); }

    .note h3 {
      margin: 25px 0 12px;
      font-size: 22px;
      font-weight: normal;
    }

    .note p {
      max-width: 290px;
      margin: 0;
      color: #59665d;
      font-size: 16px;
      line-height: 1.65;
    }

    footer {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      padding: 22px 0 35px;
      border-top: 1px solid var(--line);
      color: var(--muted);
    }

    @media (max-width: 700px) {
      .page { width: min(100% - 36px, 520px); }
      .hero { grid-template-columns: 1fr; padding: 60px 0; }
      h1 { font-size: clamp(56px, 13vw, 80px); }
      .intro { margin-top: 22px; }
      .notes { grid-template-columns: 1fr; gap: 28px; }
      .note h3 { margin-top: 16px; }
      .section-heading { display: block; }
      .section-heading .label { display: block; margin-top: 12px; }
      footer { flex-direction: column; }
    }

    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      *, *::before, *::after { transition-duration: 0s !important; }
    }
  </style>
</head>
<body>
  <div class="page">
    <header>
      <a class="brand" href="#top">
        <span class="brand-mark" aria-hidden="true">✳</span>
        <span>The Quiet Observatory</span>
      </a>
      <a href="#field-notes">Field notes ↓</a>
    </header>

    <main id="top">
      <section class="hero" aria-labelledby="title">
        <div>
          <p class="eyebrow">A small place on the internet</p>
          <h1 id="title">Room to <em>notice.</em></h1>
          <p class="intro">
            A little observatory for ordinary wonders, open at all hours.
            Nothing here needs to be finished.
          </p>
        </div>

        <div class="art-wrap">
          <div class="art" id="sky">
            <svg viewBox="0 0 500 500" role="img" aria-label="A small observatory on a hill beneath a wide sky">
              <g class="stars">
                <circle cx="111" cy="151" r="2"/>
                <circle cx="168" cy="88" r="1.5"/>
                <circle cx="352" cy="102" r="2"/>
                <circle cx="405" cy="180" r="1.5"/>
                <path d="M83 235h14M90 228v14M393 67h12M399 61v12"
                      fill="none" stroke="currentColor" stroke-width="1" opacity=".65"/>
              </g>
              <circle class="orb" cx="281" cy="150" r="55"/>
              <path class="back-hill" d="M0 365 Q90 285 180 352 T355 332 T500 340 V500 H0Z"/>
              <path class="front-hill" d="M0 420 Q95 378 175 405 Q270 335 350 380 Q430 415 500 369 V500 H0Z"/>
              <g fill="#f3f0e7">
                <path d="M222 366v-45a28 28 0 0 1 56 0v45z"/>
                <rect x="216" y="363" width="68" height="5" rx="1"/>
              </g>
              <path d="M250 293v-12M243 281h14" fill="none" stroke="#f3f0e7" stroke-width="3"/>
              <path d="M247 366v-19a5 5 0 0 1 10 0v19" fill="#49685b"/>
              <path d="M285 320h19" stroke="#f3f0e7" stroke-width="2"/>
              <path d="M34 457q43-9 77 0m233-13q46-8 87 2" fill="none" stroke="#9bb1a0" stroke-width="1.5" opacity=".7"/>
            </svg>
          </div>
          <div class="scene-caption">
            <span id="sky-label" aria-live="polite">01 / Morning</span>
            <button id="change-sky" type="button" hidden>Change the sky ↗</button>
          </div>
        </div>
      </section>

      <section class="collection" id="field-notes" aria-labelledby="notes-title">
        <div class="section-heading">
          <h2 id="notes-title">A few things worth noticing</h2>
          <span class="label">An incomplete collection</span>
        </div>
        <div class="notes">
          <article class="note">
            <span class="number">01 / Light</span>
            <h3>The moving window</h3>
            <p>A patch of sunlight crosses a room without making a sound. By evening it has visited everything.</p>
          </article>
          <article class="note">
            <span class="number">02 / Sound</span>
            <h3>After the rain</h3>
            <p>Water keeps falling from the trees long after the clouds have decided to stop.</p>
          </article>
          <article class="note">
            <span class="number">03 / Time</span>
            <h3>The unhurried seed</h3>
            <p>Some things spend a long time looking like nothing is happening.</p>
          </article>
        </div>
      </section>
    </main>

    <footer>
      <span>The Quiet Observatory ✳</span>
      <span>Made for looking, not keeping score.</span>
    </footer>
  </div>

  <script>
    const sky = document.getElementById("sky");
    const label = document.getElementById("sky-label");
    const button = document.getElementById("change-sky");
    const scenes = [
      { className: "", label: "01 / Morning" },
      { className: "dusk", label: "02 / Dusk" },
      { className: "night", label: "03 / Night" }
    ];
    let scene = 0;
    button.hidden = false;
    button.addEventListener("click", () => {
      scene = (scene + 1) % scenes.length;
      sky.className = "art" + (scenes[scene].className ? " " + scenes[scene].className : "");
      label.textContent = scenes[scene].label;
    });
  </script>
</body>
</html>
```

What: A quiet little observatory with a changeable sky and notes on ordinary wonders.