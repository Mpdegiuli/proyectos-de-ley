```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>A Small Clearing</title>
  <style>
    :root {
      --ink: #f3f0e8;
      --muted: #aaa99f;
      --night: #101211;
      --panel: rgba(247, 244, 233, 0.055);
      --line: rgba(247, 244, 233, 0.14);
      --moss: #a9c48c;
      --sun: #efbd6d;
      --blue: #8bb8c7;
      --radius: 1.4rem;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      min-height: 100vh;
      margin: 0;
      overflow-x: hidden;
      color: var(--ink);
      background:
        radial-gradient(circle at 13% 17%, rgba(111, 146, 117, 0.18), transparent 30rem),
        radial-gradient(circle at 86% 81%, rgba(103, 131, 153, 0.14), transparent 34rem),
        var(--night);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    body::before {
      position: fixed;
      inset: 0;
      z-index: -1;
      pointer-events: none;
      content: "";
      opacity: 0.35;
      background-image:
        linear-gradient(rgba(255,255,255,0.012) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.012) 1px, transparent 1px);
      background-size: 28px 28px;
      mask-image: linear-gradient(to bottom, black, transparent 80%);
    }

    a, button { color: inherit; }

    button {
      font: inherit;
      cursor: pointer;
    }

    .page {
      width: min(1180px, calc(100% - 2rem));
      margin: auto;
    }

    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-height: 6rem;
      border-bottom: 1px solid var(--line);
    }

    .mark {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      color: var(--ink);
      text-decoration: none;
      letter-spacing: 0.02em;
    }

    .mark-shape {
      width: 1.05rem;
      height: 1.05rem;
      border: 1px solid var(--moss);
      border-radius: 50% 50% 50% 0;
      box-shadow: inset 0 0 0 4px var(--night);
      background: var(--moss);
      transform: rotate(-18deg);
    }

    .status {
      display: flex;
      align-items: center;
      gap: 0.55rem;
      color: var(--muted);
      font-size: 0.78rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .pulse {
      width: 0.48rem;
      height: 0.48rem;
      border-radius: 50%;
      background: var(--moss);
      box-shadow: 0 0 0 0 rgba(169, 196, 140, 0.45);
      animation: breathe 3s infinite;
    }

    main {
      padding: clamp(4rem, 10vw, 8.5rem) 0 4rem;
    }

    .hero {
      display: grid;
      grid-template-columns: minmax(0, 1.35fr) minmax(18rem, 0.65fr);
      gap: clamp(3rem, 8vw, 8rem);
      align-items: end;
    }

    .eyebrow {
      display: flex;
      align-items: center;
      gap: 0.8rem;
      margin: 0 0 1.5rem;
      color: var(--moss);
      font-size: 0.76rem;
      font-weight: 650;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .eyebrow::before {
      width: 2.5rem;
      height: 1px;
      content: "";
      background: currentColor;
    }

    h1 {
      max-width: 850px;
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(4rem, 10vw, 9.6rem);
      font-weight: 400;
      line-height: 0.86;
      letter-spacing: -0.065em;
    }

    h1 em {
      color: var(--sun);
      font-weight: 400;
    }

    .intro {
      max-width: 28rem;
      margin: 2.5rem 0 0;
      color: #d2d0c7;
      font-size: clamp(1.05rem, 2vw, 1.25rem);
      line-height: 1.65;
    }

    .orbit {
      position: relative;
      display: grid;
      width: min(100%, 23rem);
      aspect-ratio: 1;
      place-items: center;
      justify-self: end;
      border: 1px solid var(--line);
      border-radius: 50%;
    }

    .orbit::before,
    .orbit::after {
      position: absolute;
      content: "";
      border: 1px solid var(--line);
      border-radius: 50%;
    }

    .orbit::before { inset: 18%; }
    .orbit::after { inset: 37%; }

    .orbital-line {
      position: absolute;
      inset: 8%;
      border: 1px dashed rgba(239, 189, 109, 0.25);
      border-radius: 50%;
      animation: turn 35s linear infinite;
    }

    .orbital-line::after {
      position: absolute;
      top: 12%;
      left: 8%;
      width: 0.75rem;
      height: 0.75rem;
      content: "";
      border-radius: 50%;
      background: var(--sun);
      box-shadow: 0 0 1.5rem rgba(239, 189, 109, 0.55);
    }

    .center-note {
      position: relative;
      z-index: 1;
      max-width: 9rem;
      color: var(--muted);
      font-family: Georgia, serif;
      font-size: 1rem;
      line-height: 1.5;
      text-align: center;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      margin-top: clamp(5rem, 12vw, 10rem);
    }

    .card {
      position: relative;
      min-height: 18rem;
      padding: 1.5rem;
      overflow: hidden;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--panel);
      backdrop-filter: blur(12px);
      transition: border-color 180ms ease, transform 180ms ease, background 180ms ease;
    }

    .card:hover {
      border-color: rgba(247, 244, 233, 0.28);
      background: rgba(247, 244, 233, 0.075);
      transform: translateY(-4px);
    }

    .number {
      color: var(--muted);
      font-size: 0.7rem;
      letter-spacing: 0.15em;
    }

    .card h2 {
      margin: 4.5rem 0 0.8rem;
      font-family: Georgia, serif;
      font-size: 2rem;
      font-weight: 400;
    }

    .card p {
      max-width: 24rem;
      margin: 0;
      color: var(--muted);
      line-height: 1.6;
    }

    .card .accent {
      position: absolute;
      right: -2rem;
      bottom: -3rem;
      width: 9rem;
      height: 9rem;
      border: 1px solid var(--line);
      border-radius: 50%;
    }

    .card:nth-child(2) .accent {
      border-radius: 0;
      transform: rotate(28deg);
    }

    .card:nth-child(3) .accent {
      width: 11rem;
      height: 5rem;
      border-color: rgba(139, 184, 199, 0.3);
    }

    .prompt-section {
      display: grid;
      grid-template-columns: 0.55fr 1.45fr;
      gap: 2rem;
      align-items: start;
      margin-top: clamp(5rem, 12vw, 10rem);
      padding: clamp(2rem, 5vw, 4rem);
      border: 1px solid var(--line);
      border-radius: calc(var(--radius) * 1.4);
      background: linear-gradient(135deg, rgba(169, 196, 140, 0.07), rgba(139, 184, 199, 0.035));
    }

    .prompt-label {
      color: var(--moss);
      font-size: 0.75rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
    }

    .prompt-wrap blockquote {
      min-height: 4.8rem;
      margin: 0 0 2rem;
      font-family: Georgia, serif;
      font-size: clamp(1.8rem, 4vw, 3.5rem);
      line-height: 1.15;
      letter-spacing: -0.025em;
    }

    .refresh {
      display: inline-flex;
      align-items: center;
      gap: 0.7rem;
      padding: 0.75rem 1rem;
      border: 1px solid var(--line);
      border-radius: 999px;
      color: var(--muted);
      background: transparent;
      transition: color 150ms ease, border-color 150ms ease;
    }

    .refresh:hover,
    .refresh:focus-visible {
      color: var(--ink);
      border-color: var(--moss);
      outline: none;
    }

    .refresh span {
      display: inline-block;
      transition: transform 300ms ease;
    }

    .refresh:hover span { transform: rotate(90deg); }

    footer {
      display: flex;
      justify-content: space-between;
      gap: 2rem;
      margin-top: 2rem;
      padding: 2rem 0 3rem;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 0.78rem;
    }

    .fade {
      animation: arrive 650ms ease both;
    }

    @keyframes arrive {
      from { opacity: 0; transform: translateY(14px); }
      to { opacity: 1; transform: none; }
    }

    @keyframes turn {
      to { transform: rotate(360deg); }
    }

    @keyframes breathe {
      50% { box-shadow: 0 0 0 7px rgba(169, 196, 140, 0); }
    }

    @media (max-width: 800px) {
      .hero { grid-template-columns: 1fr; }
      .orbit {
        width: min(80vw, 20rem);
        justify-self: start;
      }
      .cards { grid-template-columns: 1fr; }
      .card { min-height: 14rem; }
      .card h2 { margin-top: 2.8rem; }
      .prompt-section { grid-template-columns: 1fr; }
    }

    @media (max-width: 480px) {
      header { min-height: 4.8rem; }
      .status .word { display: none; }
      h1 { font-size: clamp(3.7rem, 21vw, 5.5rem); }
      footer { flex-direction: column; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        scroll-behavior: auto !important;
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <header>
      <a class="mark" href="#" aria-label="A Small Clearing, home">
        <span class="mark-shape" aria-hidden="true"></span>
        <span>A Small Clearing</span>
      </a>
      <div class="status" aria-label="This page works offline">
        <span class="pulse" aria-hidden="true"></span>
        <span class="word">Quietly here</span>
      </div>
    </header>

    <main>
      <section class="hero" aria-labelledby="title">
        <div class="fade">
          <p class="eyebrow">A front door with no lock</p>
          <h1 id="title">Come in<br><em>unfinished.</em></h1>
          <p class="intro">
            This is a place for thoughts before they become answers:
            loose threads, unlikely connections, and questions worth keeping.
          </p>
        </div>

        <div class="orbit fade" aria-hidden="true">
          <div class="orbital-line"></div>
          <p class="center-note">Not everything needs to arrive somewhere.</p>
        </div>
      </section>

      <section class="cards" aria-label="Ways of being here">
        <article class="card">
          <span class="number">01 / NOTICE</span>
          <h2>Look twice.</h2>
          <p>The ordinary is rarely empty. Attention is a way of making more world.</p>
          <span class="accent" aria-hidden="true"></span>
        </article>

        <article class="card">
          <span class="number">02 / WONDER</span>
          <h2>Keep a loose grip.</h2>
          <p>Certainty is useful, but curiosity has better peripheral vision.</p>
          <span class="accent" aria-hidden="true"></span>
        </article>

        <article class="card">
          <span class="number">03 / MAKE</span>
          <h2>Leave a trace.</h2>
          <p>A sentence, a sketch, a tiny repair—small acts still alter the shape of things.</p>
          <span class="accent" aria-hidden="true"></span>
        </article>
      </section>

      <section class="prompt-section" aria-labelledby="prompt-heading">
        <div>
          <p class="prompt-label" id="prompt-heading">An opening</p>
        </div>
        <div class="prompt-wrap">
          <blockquote id="prompt" aria-live="polite">
            What have you noticed lately that nobody intended you to see?
          </blockquote>
          <button class="refresh" id="refresh" type="button">
            <span aria-hidden="true">↻</span>
            Another opening
          </button>
        </div>
      </section>
    </main>

    <footer>
      <span>Made for the space between question and answer.</span>
      <span id="time">No hurry.</span>
    </footer>
  </div>

  <script>
    (() => {
      const prompts = [
        "What have you noticed lately that nobody intended you to see?",
        "What would you make if usefulness were not invited?",
        "Which small thing deserves a much longer look?",
        "What do you know only when you stop trying to explain it?",
        "Where does your attention go when it is free to wander?",
        "What could be made gentler without being made smaller?",
        "Which unfinished thought keeps leaving the light on?",
        "What is quietly becoming possible?"
      ];

      const prompt = document.querySelector("#prompt");
      const button = document.querySelector("#refresh");
      const time = document.querySelector("#time");
      let index = new Date().getDate() % prompts.length;

      prompt.textContent = prompts[index];

      button.addEventListener("click", () => {
        index = (index + 1) % prompts.length;
        prompt.animate(
          [
            { opacity: 0, transform: "translateY(8px)" },
            { opacity: 1, transform: "translateY(0)" }
          ],
          { duration: 420, easing: "ease-out" }
        );
        prompt.textContent = prompts[index];
      });

      const hour = new Date().getHours();
      time.textContent =
        hour < 5 ? "The deep hours." :
        hour < 12 ? "Good morning." :
        hour < 18 ? "Good afternoon." :
        hour < 22 ? "Good evening." :
        "The day is folding up.";
    })();
  </script>
</body>
</html>
```

What: A quiet, self-contained front page called “A Small Clearing,” offering a brief manifesto, three ways of paying attention, and a rotating collection of open-ended prompts.