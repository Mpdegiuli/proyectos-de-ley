```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>The Looking Room</title>
  <style>
    :root {
      --ink: #252e2b;
      --muted: #64716a;
      --paper: #f3f1e8;
      --line: #cbd0c4;
      --green: #345b48;
      --orange: #d47c4c;
    }

    * { box-sizing: border-box; }

    html { min-height: 100%; }

    body {
      margin: 0;
      color: var(--ink);
      background: var(--paper);
      font-family: Georgia, "Times New Roman", serif;
    }

    .page {
      width: min(1120px, calc(100% - 48px));
      margin: 0 auto;
    }

    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      padding: 25px 0;
      border-bottom: 1px solid var(--line);
      font-family: Arial, sans-serif;
      font-size: 11px;
      font-weight: bold;
      letter-spacing: .13em;
      text-transform: uppercase;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand-mark {
      width: 19px;
      height: 19px;
      border: 1px solid var(--green);
      border-radius: 50%;
      position: relative;
    }

    .brand-mark::after {
      content: "";
      position: absolute;
      inset: 5px;
      border-radius: 50%;
      background: var(--green);
    }

    .header-note { color: var(--muted); }

    .hero {
      display: grid;
      grid-template-columns: 1.05fr .95fr;
      align-items: center;
      gap: 6%;
      min-height: 560px;
      padding: 65px 0 75px;
    }

    .eyebrow, .label, .number, footer {
      font-family: Arial, sans-serif;
      font-size: 11px;
      font-weight: bold;
      letter-spacing: .15em;
      text-transform: uppercase;
    }

    .eyebrow {
      color: var(--green);
      margin: 0 0 24px;
    }

    h1 {
      max-width: 620px;
      margin: 0;
      font-size: clamp(52px, 7.6vw, 94px);
      font-weight: normal;
      line-height: .99;
      letter-spacing: -.055em;
    }

    h1 em {
      color: var(--green);
      font-weight: normal;
    }

    .intro {
      max-width: 410px;
      margin: 30px 0 0;
      color: #59645e;
      font-size: 19px;
      line-height: 1.6;
    }

    .art {
      min-height: 420px;
      position: relative;
      overflow: hidden;
      background: #dce4d5;
      border-radius: 50% 50% 2px 2px;
    }

    .art::before, .art::after {
      content: "";
      position: absolute;
      border: 1px solid rgba(52, 91, 72, .3);
      border-radius: 50%;
    }

    .art::before { inset: 10%; }
    .art::after { inset: 19%; }

    .sun {
      position: absolute;
      width: 27%;
      aspect-ratio: 1;
      left: 36.5%;
      top: 34%;
      border-radius: 50%;
      background: var(--orange);
      box-shadow: 0 0 0 16px rgba(212, 124, 76, .12);
    }

    .orbit {
      position: absolute;
      inset: 7% 24%;
      border: 1px solid rgba(52, 91, 72, .45);
      border-radius: 50%;
      transform: rotate(48deg);
    }

    .orbit::after {
      content: "";
      position: absolute;
      width: 12px;
      height: 12px;
      left: 12%;
      top: 16%;
      border-radius: 50%;
      background: var(--green);
    }

    .art-caption {
      position: absolute;
      bottom: 23px;
      left: 24px;
      right: 24px;
      display: flex;
      justify-content: space-between;
      color: var(--green);
      font: 10px Arial, sans-serif;
      letter-spacing: .13em;
      text-transform: uppercase;
    }

    .section-head {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 20px;
      padding: 24px 0;
      border-top: 1px solid var(--line);
    }

    .section-head h2 {
      margin: 0;
      font-size: 29px;
      font-weight: normal;
      letter-spacing: -.03em;
    }

    .label { color: var(--muted); }

    .cards {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
    }

    .card {
      min-height: 190px;
      padding: 26px 30px 28px 0;
    }

    .card + .card {
      border-left: 1px solid var(--line);
      padding-left: 30px;
    }

    .number { color: var(--orange); }

    .card h3 {
      margin: 25px 0 10px;
      font-size: 23px;
      font-weight: normal;
    }

    .card p {
      max-width: 285px;
      margin: 0;
      color: var(--muted);
      font-size: 16px;
      line-height: 1.55;
    }

    .prompt {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 30px;
      margin: 60px 0;
      padding: 32px 36px;
      background: #e2e8da;
    }

    .prompt .label { color: var(--green); }

    .question {
      margin: 12px 0 0;
      font-size: clamp(22px, 3vw, 31px);
      line-height: 1.25;
      letter-spacing: -.025em;
    }

    button {
      flex: none;
      padding: 15px 20px;
      border: 1px solid var(--green);
      border-radius: 0;
      color: white;
      background: var(--green);
      font: bold 11px Arial, sans-serif;
      letter-spacing: .1em;
      text-transform: uppercase;
      cursor: pointer;
    }

    button:hover { background: #264736; }
    button:focus-visible { outline: 3px solid var(--orange); outline-offset: 4px; }

    footer {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      padding: 0 0 30px;
      color: var(--muted);
      line-height: 1.6;
    }

    @media (max-width: 700px) {
      .page { width: min(100% - 36px, 520px); }
      .header-note { display: none; }
      .hero { grid-template-columns: 1fr; gap: 42px; padding: 60px 0; }
      .art { min-height: 350px; }
      .cards { grid-template-columns: 1fr; }
      .card { min-height: 0; padding: 25px 0; }
      .card + .card { border-left: 0; border-top: 1px solid var(--line); padding-left: 0; }
      .card h3 { margin-top: 15px; }
      .prompt { align-items: flex-start; flex-direction: column; padding: 27px; }
      footer { flex-direction: column; gap: 5px; }
    }
  </style>
</head>
<body>
  <div class="page">
    <header>
      <div class="brand"><span class="brand-mark" aria-hidden="true"></span> The Looking Room</div>
      <div class="header-note">A small place for curiosity</div>
    </header>

    <main>
      <section class="hero">
        <div>
          <p class="eyebrow">Come in, look around</p>
          <h1>A page for <em>looking twice.</em></h1>
          <p class="intro">The world is wonderfully full of things that reward a second glance. This is a little room for making space for them.</p>
        </div>
        <div class="art" role="img" aria-label="An abstract illustration of a terracotta sun surrounded by green orbits.">
          <div class="orbit"></div>
          <div class="sun"></div>
          <div class="art-caption"><span>Figure 01</span><span>Not to scale</span></div>
        </div>
      </section>

      <section aria-labelledby="noticing-title">
        <div class="section-head">
          <h2 id="noticing-title">Three ways in</h2>
          <span class="label">An incomplete list</span>
        </div>
        <div class="cards">
          <article class="card">
            <span class="number">01 / Notice</span>
            <h3>Find the overlooked</h3>
            <p>Pick an ordinary object. What has use, weather, or time done to it?</p>
          </article>
          <article class="card">
            <span class="number">02 / Wonder</span>
            <h3>Ask a smaller question</h3>
            <p>Not “how does everything work?” Just: why does this leaf have that shape?</p>
          </article>
          <article class="card">
            <span class="number">03 / Reconsider</span>
            <h3>Leave a little room</h3>
            <p>Hold an idea gently enough that a new piece of evidence can change it.</p>
          </article>
        </div>
      </section>

      <section class="prompt" aria-label="A question to take with you">
        <div>
          <div class="label">A question to take with you</div>
          <p class="question" id="question" aria-live="polite">What did you pass today without really seeing?</p>
        </div>
        <button type="button" id="another" hidden>Another question &rarr;</button>
      </section>
    </main>

    <footer>
      <span>The Looking Room</span>
      <span>No hurry. The world can wait a moment.</span>
    </footer>
  </div>

  <script>
    const questions = [
      "What did you pass today without really seeing?",
      "What ordinary thing would you miss if it disappeared?",
      "Where can you see time at work?",
      "What is a question you have never thought to ask?",
      "What looks different when you move closer?",
      "What do you know now that you once misunderstood?"
    ];
    const question = document.getElementById("question");
    const button = document.getElementById("another");
    let current = 0;
    button.hidden = false;
    button.addEventListener("click", () => {
      current = (current + 1) % questions.length;
      question.textContent = questions[current];
    });
  </script>
</body>
</html>
```

What: A quiet, illustrated room for curiosity, with a rotating set of questions to take away.