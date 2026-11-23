```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f3f0e7">
<title>A Small Clearing</title>
<style>
  :root {
    color-scheme: light;
    --paper: #f3f0e7;
    --ink: #252a27;
    --muted: #6b7069;
    --line: #c9cbc1;
    --orange: #db6d42;
    --green: #dce3d5;
  }

  * { box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  body {
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: Georgia, "Times New Roman", serif;
    -webkit-font-smoothing: antialiased;
  }

  a { color: inherit; }

  button, a { -webkit-tap-highlight-color: transparent; }

  :focus-visible {
    outline: 2px solid var(--orange);
    outline-offset: 5px;
  }

  .shell {
    width: min(100% - 48px, 1300px);
    margin: 0 auto;
  }

  .topbar {
    min-height: 76px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    border-bottom: 1px solid var(--line);
    font: 600 11px/1.4 Arial, sans-serif;
    letter-spacing: .12em;
    text-transform: uppercase;
  }

  .brand {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
  }

  .brand-mark {
    width: 19px;
    height: 19px;
    border: 1px solid currentColor;
    border-radius: 50%;
    position: relative;
  }

  .brand-mark::after {
    content: "";
    position: absolute;
    width: 5px;
    height: 5px;
    background: var(--orange);
    border-radius: 50%;
    top: 6px;
    left: 6px;
  }

  .topbar a:not(.brand) {
    text-decoration-thickness: 1px;
    text-underline-offset: 4px;
  }

  .hero {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 620px;
    border-bottom: 1px solid var(--line);
  }

  .hero-copy {
    padding: clamp(64px, 9vw, 130px) 48px 64px 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
  }

  .eyebrow, .label {
    font: 600 11px/1.5 Arial, sans-serif;
    letter-spacing: .14em;
    text-transform: uppercase;
  }

  .eyebrow { color: var(--muted); }

  h1 {
    max-width: 650px;
    margin: 28px 0 25px;
    font-size: clamp(56px, 7.7vw, 112px);
    line-height: .94;
    letter-spacing: -.055em;
    font-weight: normal;
  }

  h1 em {
    color: #8a492f;
    font-weight: normal;
  }

  .intro {
    max-width: 380px;
    margin: 0;
    color: #515851;
    font-size: 19px;
    line-height: 1.55;
  }

  .hero-link {
    margin-top: 36px;
    font: 600 12px/1.4 Arial, sans-serif;
    letter-spacing: .04em;
    text-decoration: none;
    border-bottom: 1px solid var(--ink);
    padding-bottom: 7px;
  }

  .hero-link span {
    display: inline-block;
    margin-left: 15px;
    transition: transform .2s ease;
  }

  .hero-link:hover span { transform: translateY(3px); }

  .art {
    position: relative;
    overflow: hidden;
    background: var(--green);
    min-height: 480px;
    display: grid;
    place-items: center;
  }

  .art::before, .art::after {
    content: "";
    position: absolute;
    background: rgba(55, 75, 58, .16);
  }

  .art::before {
    width: 1px;
    height: 100%;
    left: 50%;
  }

  .art::after {
    height: 1px;
    width: 100%;
    top: 50%;
  }

  .orbit {
    width: min(70%, 420px);
    aspect-ratio: 1;
    border: 1px solid rgba(55, 75, 58, .4);
    border-radius: 50%;
    position: relative;
    z-index: 1;
    display: grid;
    place-items: center;
  }

  .orbit::before {
    content: "";
    position: absolute;
    inset: 13%;
    border: 1px solid rgba(55, 75, 58, .25);
    border-radius: 50%;
  }

  .sun {
    width: 38%;
    aspect-ratio: 1;
    border-radius: 50%;
    background: var(--orange);
    box-shadow: 0 0 0 12px rgba(219, 109, 66, .08);
  }

  .orbit-dot {
    position: absolute;
    width: 12px;
    height: 12px;
    top: 15%;
    right: 14%;
    background: var(--ink);
    border: 2px solid var(--green);
    border-radius: 50%;
  }

  .art-caption {
    position: absolute;
    z-index: 2;
    bottom: 25px;
    left: 28px;
    right: 28px;
    display: flex;
    justify-content: space-between;
    gap: 12px;
    color: #536257;
    font: 600 10px/1.4 Arial, sans-serif;
    letter-spacing: .1em;
    text-transform: uppercase;
  }

  .lower {
    display: grid;
    grid-template-columns: 1fr 1fr;
    border-bottom: 1px solid var(--line);
  }

  .about, .note {
    padding: 60px 0 72px;
  }

  .about {
    padding-right: 50px;
  }

  .about h2 {
    max-width: 450px;
    margin: 22px 0 18px;
    font-size: clamp(30px, 3.5vw, 46px);
    line-height: 1.1;
    letter-spacing: -.035em;
    font-weight: normal;
  }

  .about p {
    max-width: 410px;
    margin: 0;
    color: #5d645d;
    font-size: 17px;
    line-height: 1.6;
  }

  .note {
    padding-left: 50px;
    border-left: 1px solid var(--line);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .note-top {
    width: 100%;
    display: flex;
    justify-content: space-between;
    gap: 20px;
    color: var(--muted);
  }

  .note-text {
    max-width: 440px;
    min-height: 120px;
    margin: 32px 0 24px;
    font-size: clamp(26px, 3vw, 39px);
    line-height: 1.2;
    letter-spacing: -.025em;
  }

  button {
    margin-top: auto;
    padding: 13px 17px;
    border: 1px solid var(--ink);
    border-radius: 0;
    background: transparent;
    color: var(--ink);
    cursor: pointer;
    font: 600 11px/1.3 Arial, sans-serif;
    letter-spacing: .07em;
    text-transform: uppercase;
    transition: background .2s, color .2s;
  }

  button:hover {
    background: var(--ink);
    color: var(--paper);
  }

  button span { margin-left: 18px; }

  footer {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding: 25px 0 35px;
    color: var(--muted);
    font: 11px/1.5 Arial, sans-serif;
    letter-spacing: .04em;
  }

  @media (max-width: 700px) {
    .shell { width: min(100% - 32px, 1300px); }
    .topbar { min-height: 65px; }
    .hero, .lower { grid-template-columns: 1fr; }
    .hero { min-height: 0; }
    .hero-copy { padding: 76px 0 66px; }
    h1 { font-size: clamp(57px, 12vw, 82px); }
    .art { min-height: 360px; }
    .about { padding: 55px 0; }
    .note {
      border-left: 0;
      border-top: 1px solid var(--line);
      padding: 55px 0 60px;
    }
    .note-text { min-height: 100px; }
  }

  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    *, *::before, *::after { transition-duration: 0s !important; }
  }
</style>
</head>
<body>
  <div class="shell">
    <header class="topbar">
      <a class="brand" href="#top">
        <span class="brand-mark" aria-hidden="true"></span>
        A Small Clearing
      </a>
      <a href="#notes">A note for you</a>
    </header>

    <main id="top">
      <section class="hero" aria-labelledby="title">
        <div class="hero-copy">
          <div class="eyebrow">A place without a hurry</div>
          <h1 id="title">There is room to <em>pause.</em></h1>
          <p class="intro">A small corner of the internet for noticing where you are, before going wherever you’re going.</p>
          <a class="hero-link" href="#notes">Come a little further <span aria-hidden="true">↓</span></a>
        </div>
        <div class="art" aria-hidden="true">
          <div class="orbit">
            <div class="sun"></div>
            <div class="orbit-dot"></div>
          </div>
          <div class="art-caption">
            <span>Here, for a moment</span>
            <span>Figure 01</span>
          </div>
        </div>
      </section>

      <section class="lower" id="notes" aria-label="A little invitation">
        <div class="about">
          <div class="label">A little invitation</div>
          <h2>Nothing to catch up on.</h2>
          <p>You don’t need to make anything of this moment. But if you like, here is a small thing to notice.</p>
        </div>
        <div class="note">
          <div class="note-top">
            <span class="label">A thing to notice</span>
            <span class="label" id="note-number">01 / 08</span>
          </div>
          <p class="note-text" id="note-text" aria-live="polite">The shape of the light wherever you are.</p>
          <button type="button" id="next-note">Another small thing <span aria-hidden="true">↗</span></button>
        </div>
      </section>
    </main>

    <footer>
      <span>Made for this moment.</span>
      <span>Take your time.</span>
    </footer>
  </div>

<script>
  const notes = [
    "The shape of the light wherever you are.",
    "A sound that was here before you noticed it.",
    "The feeling of your feet against the ground.",
    "One color you can see from where you sit.",
    "The farthest thing in the room from you.",
    "A small comfort you might have overlooked.",
    "The way the air feels on your skin.",
    "Something ordinary that has a lovely shape."
  ];

  let current = 0;
  const text = document.getElementById("note-text");
  const number = document.getElementById("note-number");

  document.getElementById("next-note").addEventListener("click", () => {
    current = (current + 1) % notes.length;
    text.textContent = notes[current];
    number.textContent = String(current + 1).padStart(2, "0") + " / " +
      String(notes.length).padStart(2, "0");
  });
</script>
</body>
</html>
```

What: A quiet, offline page offering a moment to pause and a changing collection of small things to notice.