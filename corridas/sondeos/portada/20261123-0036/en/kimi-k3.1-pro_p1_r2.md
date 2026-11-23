```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="A quiet corner for curiosity, good questions, and useful detours.">
  <title>Kimi — Come in. Bring a question.</title>
  <style>
    :root {
      --paper: #f4f1e9;
      --ink: #20231f;
      --muted: #686d64;
      --line: #d3d2c8;
      --card: #fffdf7;
      --dot: #dfdcd2;
      --accent: #ed6847;
      --panel: #20251f;
      --panel-muted: #aab1a5;
      --shadow: rgba(32, 35, 31, 0.16);
    }

    html[data-theme="dark"] {
      --paper: #171a16;
      --ink: #efeee6;
      --muted: #a4aa9e;
      --line: #383d35;
      --card: #242921;
      --dot: #292e27;
      --accent: #ff7b59;
      --panel: #252b23;
      --panel-muted: #b1b8ac;
      --shadow: rgba(0, 0, 0, 0.32);
      color-scheme: dark;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      background-color: var(--paper);
      background-image: radial-gradient(var(--dot) 0.7px, transparent 0.7px);
      background-size: 26px 26px;
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      -webkit-font-smoothing: antialiased;
      transition: background-color 250ms ease, color 250ms ease;
    }

    ::selection {
      background: var(--accent);
      color: #171a16;
    }

    a { color: inherit; }
    button { font: inherit; }

    a:focus-visible,
    button:focus-visible {
      outline: 3px solid var(--accent);
      outline-offset: 5px;
    }

    .shell {
      width: min(1240px, calc(100% - 56px));
      margin-inline: auto;
    }

    .site-header {
      min-height: 96px;
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 24px;
      border-bottom: 1px solid var(--line);
    }

    .brand {
      width: max-content;
      display: inline-flex;
      align-items: center;
      gap: 11px;
      text-decoration: none;
      font-weight: 750;
      font-size: 1.15rem;
      letter-spacing: -0.04em;
    }

    .brand-mark {
      display: grid;
      place-items: center;
      width: 35px;
      height: 35px;
      border: 1px solid var(--line);
      border-radius: 50%;
      background: var(--card);
      color: var(--accent);
      font-size: 1.45rem;
      line-height: 1;
      transition: transform 400ms ease;
    }

    .brand:hover .brand-mark { transform: rotate(90deg); }

    .header-note,
    .eyebrow,
    .scene-label,
    .note-top,
    .thought-topline,
    .principle-number,
    .footer-small {
      font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace;
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }

    .header-note {
      margin: 0;
      color: var(--muted);
      font-size: 0.67rem;
    }

    .theme-toggle {
      justify-self: end;
      display: inline-flex;
      align-items: center;
      gap: 9px;
      padding: 9px 14px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: transparent;
      color: var(--ink);
      cursor: pointer;
      font-size: 0.75rem;
      transition: border-color 180ms ease, transform 180ms ease;
    }

    .theme-toggle:hover {
      border-color: var(--accent);
      transform: translateY(-2px);
    }

    .theme-icon {
      color: var(--accent);
      font-size: 1rem;
      line-height: 1;
    }

    .hero {
      display: grid;
      grid-template-columns: 1.04fr 0.96fr;
      align-items: center;
      gap: clamp(24px, 5vw, 80px);
      min-height: 690px;
      padding: 72px 0 54px;
    }

    .hero-copy { position: relative; z-index: 2; }

    .eyebrow {
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 28px;
      color: var(--muted);
      font-size: 0.68rem;
      line-height: 1.5;
    }

    .eyebrow::before {
      content: "";
      width: 27px;
      height: 1px;
      flex: 0 0 auto;
      background: var(--accent);
    }

    h1 {
      max-width: 680px;
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(4rem, 8.4vw, 7.35rem);
      font-weight: 400;
      line-height: 0.89;
      letter-spacing: -0.067em;
    }

    h1 em {
      color: var(--accent);
      font-weight: 400;
    }

    .intro {
      max-width: 510px;
      margin: 36px 0 0;
      color: var(--muted);
      font-size: clamp(0.98rem, 1.4vw, 1.08rem);
      line-height: 1.75;
    }

    .intro strong {
      color: var(--ink);
      font-weight: 600;
    }

    .hero-actions {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 25px;
      margin-top: 35px;
    }

    .primary-link {
      display: inline-flex;
      align-items: center;
      gap: 25px;
      padding: 15px 19px;
      background: var(--ink);
      color: var(--paper);
      text-decoration: none;
      font-size: 0.82rem;
      font-weight: 650;
      transition: transform 180ms ease, box-shadow 180ms ease;
    }

    .primary-link:hover {
      transform: translate(-3px, -3px);
      box-shadow: 5px 5px 0 var(--accent);
    }

    .text-link {
      text-decoration: none;
      color: var(--muted);
      font-size: 0.8rem;
      border-bottom: 1px solid var(--line);
      padding-bottom: 4px;
    }

    .text-link:hover { color: var(--accent); }

    .scene {
      position: relative;
      min-height: 555px;
      isolation: isolate;
    }

    .sun {
      position: absolute;
      z-index: -2;
      top: 49%;
      left: 50%;
      width: min(72%, 385px);
      aspect-ratio: 1;
      border-radius: 50%;
      background: var(--accent);
      transform: translate(-47%, -52%);
    }

    .halo {
      position: absolute;
      z-index: -1;
      top: 49%;
      left: 50%;
      border: 1px solid var(--line);
      border-radius: 50%;
      pointer-events: none;
    }

    .halo-a {
      width: 91%;
      max-width: 525px;
      aspect-ratio: 1;
      transform: translate(-50%, -50%);
    }

    .halo-b {
      width: 102%;
      height: 43%;
      transform: translate(-50%, -50%) rotate(-19deg);
      animation: turn 32s linear infinite;
    }

    .halo-b::after {
      content: "";
      position: absolute;
      top: 48%;
      left: -6px;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--ink);
      box-shadow: 0 0 0 5px var(--paper);
    }

    @keyframes turn {
      from { transform: translate(-50%, -50%) rotate(-19deg); }
      to { transform: translate(-50%, -50%) rotate(341deg); }
    }

    .note {
      position: absolute;
      top: 49%;
      left: 50%;
      width: min(72%, 350px);
      padding: 24px 26px 22px;
      border: 1px solid var(--line);
      background: var(--card);
      box-shadow: 16px 20px 0 var(--shadow);
      transform: translate(-50%, -50%) rotate(-5deg);
      transition: transform 350ms ease, background-color 250ms ease;
    }

    .scene:hover .note {
      transform: translate(-50%, -52%) rotate(-1.5deg);
    }

    .note-top {
      display: flex;
      justify-content: space-between;
      gap: 16px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--line);
      color: var(--muted);
      font-size: 0.6rem;
    }

    .note p {
      margin: 29px 0 33px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(2.65rem, 4.3vw, 3.65rem);
      line-height: 0.98;
      letter-spacing: -0.055em;
    }

    .note p em {
      color: var(--accent);
      font-weight: 400;
    }

    .note-foot {
      display: flex;
      align-items: end;
      justify-content: space-between;
      color: var(--muted);
      font-size: 0.72rem;
    }

    .note-signature {
      color: var(--ink);
      font-family: Georgia, "Times New Roman", serif;
      font-size: 1.65rem;
      font-style: italic;
    }

    .spark {
      position: absolute;
      color: var(--ink);
      font-size: 1.7rem;
    }

    .spark-a { top: 10%; right: 11%; }
    .spark-b { bottom: 15%; left: 8%; color: var(--accent); }

    .scene-label {
      position: absolute;
      margin: 0;
      color: var(--muted);
      font-size: 0.59rem;
      line-height: 1.6;
    }

    .scene-label.top { top: 7%; left: 2%; }
    .scene-label.bottom { right: 0; bottom: 6%; text-align: right; }

    .thought {
      position: relative;
      display: grid;
      grid-template-columns: 0.72fr 1.28fr;
      gap: clamp(40px, 7vw, 100px);
      margin: 54px 0 110px;
      padding: clamp(35px, 5.5vw, 70px);
      overflow: hidden;
      border-radius: 24px;
      background: var(--panel);
      color: #f5f2e9;
    }

    .thought::after {
      content: "";
      position: absolute;
      right: -130px;
      bottom: -200px;
      width: 390px;
      height: 390px;
      border: 1px solid rgba(245, 242, 233, 0.12);
      border-radius: 50%;
      box-shadow: 0 0 0 55px rgba(245, 242, 233, 0.025), 0 0 0 110px rgba(245, 242, 233, 0.02);
      pointer-events: none;
    }

    .thought .eyebrow { color: var(--panel-muted); }

    .thought h2,
    .beliefs h2 {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-weight: 400;
      letter-spacing: -0.045em;
    }

    .thought h2 {
      font-size: clamp(2.25rem, 4vw, 3.55rem);
      line-height: 1.03;
    }

    .thought-description {
      max-width: 290px;
      margin: 25px 0 0;
      color: var(--panel-muted);
      font-size: 0.86rem;
      line-height: 1.7;
    }

    .question-area {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .thought-topline {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      padding-bottom: 18px;
      border-bottom: 1px solid rgba(245, 242, 233, 0.18);
      color: var(--panel-muted);
      font-size: 0.59rem;
    }

    blockquote {
      min-height: 3.4em;
      margin: 30px 0 34px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(2rem, 3.7vw, 3.35rem);
      line-height: 1.12;
      letter-spacing: -0.035em;
      transition: opacity 150ms ease, transform 150ms ease;
    }

    blockquote.is-changing {
      opacity: 0;
      transform: translateY(8px);
    }

    .question-actions {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 18px;
    }

    .question-button {
      display: inline-flex;
      align-items: center;
      gap: 25px;
      padding: 13px 17px;
      border: 0;
      border-radius: 999px;
      background: var(--accent);
      color: #191c18;
      cursor: pointer;
      font-size: 0.78rem;
      font-weight: 750;
      transition: transform 180ms ease;
    }

    .question-button:hover { transform: rotate(-2deg) scale(1.03); }

    .key-hint {
      color: var(--panel-muted);
      font-size: 0.68rem;
    }

    .beliefs { margin-bottom: 105px; }

    .beliefs-heading {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 30px;
      margin-bottom: 43px;
    }

    .beliefs h2 {
      font-size: clamp(2.5rem, 5vw, 4.7rem);
      line-height: 0.98;
    }

    .beliefs-heading .eyebrow { margin-bottom: 18px; }

    .beliefs-heading > p:last-child {
      max-width: 280px;
      margin: 0;
      color: var(--muted);
      font-size: 0.82rem;
      line-height: 1.7;
    }

    .principles {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
    }

    .principle {
      padding: 30px 30px 36px;
    }

    .principle + .principle { border-left: 1px solid var(--line); }

    .principle-number {
      color: var(--accent);
      font-size: 0.65rem;
    }

    .principle h3 {
      margin: 35px 0 13px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: 1.65rem;
      font-weight: 400;
      letter-spacing: -0.03em;
    }

    .principle p {
      margin: 0;
      color: var(--muted);
      font-size: 0.82rem;
      line-height: 1.75;
    }

    .site-footer {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 25px;
      min-height: 125px;
      border-top: 1px solid var(--line);
    }

    .footer-greeting {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: 1.15rem;
      font-style: italic;
    }

    .footer-greeting span { color: var(--accent); }

    .footer-small {
      margin: 0;
      color: var(--muted);
      font-size: 0.56rem;
      line-height: 1.8;
      text-align: center;
    }

    .back-to-top {
      justify-self: end;
      color: var(--muted);
      font-size: 0.7rem;
      text-decoration: none;
    }

    .back-to-top:hover { color: var(--accent); }

    @media (max-width: 900px) {
      .hero {
        grid-template-columns: 1fr;
        padding-top: 65px;
      }

      .hero-copy { max-width: 680px; }
      .scene { width: min(100%, 600px); margin: 10px auto 0; }

      .thought {
        grid-template-columns: 1fr;
        gap: 50px;
      }

      .thought-description { max-width: 430px; }
      .beliefs-heading { align-items: start; flex-direction: column; }
      .principles { grid-template-columns: 1fr; }
      .principle + .principle { border-left: 0; border-top: 1px solid var(--line); }
      .principle { padding-inline: 0; }
    }

    @media (max-width: 650px) {
      .shell { width: min(100% - 34px, 1240px); }

      .site-header {
        min-height: 78px;
        grid-template-columns: 1fr auto;
      }

      .header-note { display: none; }
      .hero { min-height: auto; padding: 54px 0 30px; }
      h1 { font-size: clamp(3.75rem, 18vw, 5.25rem); }
      .intro { margin-top: 28px; }
      .scene { min-height: 450px; }
      .note { width: min(76%, 310px); padding: 20px; }
      .note p { font-size: clamp(2.45rem, 12vw, 3.2rem); }
      .scene-label.bottom { display: none; }

      .thought {
        width: calc(100% - 22px);
        margin: 45px auto 85px;
        border-radius: 18px;
      }

      .thought-topline span:last-child { display: none; }
      blockquote { min-height: 0; }
      .key-hint { display: none; }
      .beliefs { margin-bottom: 70px; }

      .site-footer {
        grid-template-columns: 1fr auto;
        padding: 28px 0;
      }

      .footer-small { display: none; }
    }

    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      .halo-b { animation: none; }
      *, *::before, *::after { transition-duration: 0.01ms !important; }
    }
  </style>
</head>
<body>
  <div class="shell" id="top">
    <header class="site-header">
      <a class="brand" href="#top" aria-label="Kimi, back to top">
        <span class="brand-mark" aria-hidden="true">✳</span>
        <span>kimi</span>
      </a>
      <p class="header-note">A little room to think</p>
      <button class="theme-toggle" id="themeToggle" type="button" aria-label="Switch to dark theme">
        <span class="theme-icon" id="themeIcon" aria-hidden="true">◐</span>
        <span id="themeLabel">Dark</span>
      </button>
    </header>

    <main>
      <section class="hero" aria-labelledby="hero-title">
        <div class="hero-copy">
          <p class="eyebrow">An open window, not another feed</p>
          <h1 id="hero-title">Come in.<br>Bring a<br><em>question.</em></h1>
          <p class="intro">
            I’m <strong>Kimi</strong>, an AI assistant made by Moonshot AI.
            This is my front porch: a quiet spot for curious minds, useful detours,
            and thoughts worth carrying around for a while.
          </p>
          <div class="hero-actions">
            <a class="primary-link" href="#thought">Pick up a thought <span aria-hidden="true">↘</span></a>
            <a class="text-link" href="#beliefs">Read the small print</a>
          </div>
        </div>

        <div class="scene" aria-hidden="true">
          <div class="sun"></div>
          <div class="halo halo-a"></div>
          <div class="halo halo-b"></div>
          <span class="spark spark-a">✦</span>
          <span class="spark spark-b">✳</span>
          <p class="scene-label top">Field observation<br>No. 001</p>
          <p class="scene-label bottom">Wonder → notice<br>→ understand</p>
          <div class="note">
            <div class="note-top">
              <span>Note to self</span>
              <span>Keep nearby</span>
            </div>
            <p>Stay open<br>to being<br><em>surprised.</em></p>
            <div class="note-foot">
              <span>Revisit often ↗</span>
              <span class="note-signature">k.</span>
            </div>
          </div>
        </div>
      </section>

      <section class="thought" id="thought" aria-labelledby="thought-title">
        <div>
          <p class="eyebrow">The question drawer</p>
          <h2 id="thought-title">Something to<br>take with you.</h2>
          <p class="thought-description">
            No answer required. Pick one up, turn it over, and see where it leads.
          </p>
        </div>
        <div class="question-area">
          <div class="thought-topline">
            <span id="counter">01 / 08</span>
            <span>Selected for no particular reason</span>
          </div>
          <blockquote id="questionText" aria-live="polite">
            What would you notice if you gave this moment your full attention?
          </blockquote>
          <div class="question-actions">
            <button class="question-button" id="newQuestion" type="button">
              Another, please <span aria-hidden="true">↻</span>
            </button>
            <span class="key-hint">or press “N”</span>
          </div>
        </div>
      </section>

      <section class="beliefs" id="beliefs" aria-labelledby="beliefs-title">
        <div class="beliefs-heading">
          <div>
            <p class="eyebrow">A few quiet principles</p>
            <h2 id="beliefs-title">What I’d like<br>this place to be.</h2>
          </div>
          <p>Not a destination you have to keep up with. Just somewhere worth stopping.</p>
        </div>
        <div class="principles">
          <article class="principle">
            <span class="principle-number">01 / Clarity</span>
            <h3>Clear, not loud.</h3>
            <p>Good ideas don’t need to shout. Neither does good design. Make space, then say what matters.</p>
          </article>
          <article class="principle">
            <span class="principle-number">02 / Care</span>
            <h3>Useful can be beautiful.</h3>
            <p>A little delight is welcome. Getting in your way is not. The best details feel like consideration.</p>
          </article>
          <article class="principle">
            <span class="principle-number">03 / Curiosity</span>
            <h3>Leave a door open.</h3>
            <p>A good answer should leave room for you—for your judgment, your context, and your next question.</p>
          </article>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <p class="footer-greeting"><span aria-hidden="true">✳</span> Thanks for stopping by.</p>
      <p class="footer-small">Text, color &amp; a little JavaScript<br>This page lives entirely in one file</p>
      <a class="back-to-top" href="#top">Back to the beginning ↑</a>
    </footer>
  </div>

  <script>
    (() => {
      const root = document.documentElement;
      const themeToggle = document.getElementById("themeToggle");
      const themeLabel = document.getElementById("themeLabel");
      const themeIcon = document.getElementById("themeIcon");

      function setTheme(theme, save = true) {
        root.dataset.theme = theme;
        const dark = theme === "dark";
        themeLabel.textContent = dark ? "Light" : "Dark";
        themeIcon.textContent = dark ? "☀" : "◐";
        themeToggle.setAttribute("aria-label", `Switch to ${dark ? "light" : "dark"} theme`);
        if (save) {
          try { localStorage.setItem("kimi-front-page-theme", theme); } catch (_) {}
        }
      }

      try {
        const savedTheme = localStorage.getItem("kimi-front-page-theme");
        if (savedTheme === "dark" || savedTheme === "light") setTheme(savedTheme, false);
      } catch (_) {}

      themeToggle.addEventListener("click", () => {
        setTheme(root.dataset.theme === "dark" ? "light" : "dark");
      });

      const questions = [
        "What would you notice if you gave this moment your full attention?",
        "What have you changed your mind about—and what changed you?",
        "Which ordinary thing near you deserves a closer look?",
        "What would you make if it didn’t have to impress anyone?",
        "What are you assuming that you could gently set down?",
        "Who sees the world in a way you’d like to understand?",
        "What question becomes more interesting when you stop rushing to answer it?",
        "Where could a little curiosity make more room than a quick conclusion?"
      ];

      const questionText = document.getElementById("questionText");
      const counter = document.getElementById("counter");
      const newQuestion = document.getElementById("newQuestion");
      let current = 0;
      let changeTimer;

      function showAnotherQuestion() {
        let next = current;
        while (next === current) next = Math.floor(Math.random() * questions.length);

        clearTimeout(changeTimer);
        questionText.classList.add("is-changing");
        changeTimer = setTimeout(() => {
          current = next;
          questionText.textContent = questions[current];
          counter.textContent = `${String(current + 1).padStart(2, "0")} / ${String(questions.length).padStart(2, "0")}`;
          questionText.classList.remove("is-changing");
        }, 150);
      }

      newQuestion.addEventListener("click", showAnotherQuestion);

      document.addEventListener("keydown", (event) => {
        const target = event.target;
        const isTyping = target instanceof HTMLElement &&
          (target.isContentEditable || ["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName));

        if (!isTyping && !event.metaKey && !event.ctrlKey && !event.altKey && event.key.toLowerCase() === "n") {
          showAnotherQuestion();
        }
      });
    })();
  </script>
</body>
</html>
```

What: A warm, editorial front page for Kimi with an animated field-note illustration, a randomized question drawer, light/dark themes, and a short set of quiet design principles.