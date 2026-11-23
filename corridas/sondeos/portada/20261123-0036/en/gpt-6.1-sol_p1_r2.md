```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f2efe6">
<title>The In-Between</title>
<style>
  :root {
    --paper: #f2efe6;
    --ink: #292e2b;
    --muted: #65685f;
    --line: #cbcbbf;
    --accent: #a2432c;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: Georgia, "Times New Roman", serif;
    -webkit-font-smoothing: antialiased;
  }

  ::selection { background: #e5c66b; color: var(--ink); }

  button, input { font: inherit; }

  button:focus-visible, input:focus-visible, a:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 6px;
  }

  .shell {
    width: min(1380px, 100%);
    margin: auto;
    padding: 0 5vw;
  }

  .small {
    font-family: ui-monospace, "Courier New", monospace;
    font-size: 11px;
    line-height: 1.6;
    letter-spacing: .1em;
    text-transform: uppercase;
  }

  header {
    min-height: 113px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
    border-bottom: 1px solid var(--line);
  }

  .wordmark {
    font-size: 13px;
    font-weight: bold;
    letter-spacing: .16em;
  }

  .header-note { color: var(--muted); text-align: right; }

  .opening {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 6vw;
    padding: 67px 0 59px;
    align-items: end;
  }

  .eyebrow { margin: 0 0 25px; color: var(--accent); }

  h1 {
    font-size: clamp(56px, 7.6vw, 110px);
    font-weight: normal;
    line-height: .98;
    letter-spacing: -.065em;
    margin: 0;
  }

  h1 em { font-weight: normal; }

  .intro {
    max-width: 340px;
    margin: 0 0 6px auto;
    font-size: clamp(18px, 1.65vw, 23px);
    line-height: 1.5;
    color: #53574f;
  }

  .exhibit {
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    min-height: 440px;
  }

  .diagram-panel {
    position: relative;
    min-width: 0;
    padding: 25px 25px 25px 0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-right: 1px solid var(--line);
  }

  .panel-top {
    display: flex;
    justify-content: space-between;
    gap: 15px;
    color: var(--muted);
  }

  .live-dot {
    width: 6px;
    height: 6px;
    display: inline-block;
    background: var(--accent);
    border-radius: 50%;
    margin-right: 7px;
    vertical-align: 1px;
  }

  svg {
    width: 100%;
    height: auto;
    display: block;
    overflow: visible;
  }

  .circle {
    fill: none;
    stroke: var(--ink);
    stroke-width: 1;
    vector-effect: non-scaling-stroke;
  }

  .ghost { stroke: var(--line); stroke-dasharray: 2 7; }

  .axis {
    stroke: var(--line);
    stroke-width: 1;
    vector-effect: non-scaling-stroke;
  }

  .sun { fill: var(--accent); }

  .orbit {
    transform-origin: 300px 190px;
    animation: orbit 90s linear infinite;
  }

  @keyframes orbit { to { transform: rotate(360deg); } }

  .distance {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    color: var(--muted);
  }

  .distance label { white-space: nowrap; }

  input[type="range"] {
    width: 125px;
    height: 25px;
    margin: 0;
    accent-color: var(--accent);
    cursor: ew-resize;
  }

  .thought-panel {
    padding: 27px 0 28px 3.8vw;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .catalogue {
    width: 100%;
    display: flex;
    justify-content: space-between;
    gap: 20px;
    color: var(--muted);
  }

  .thought { margin: auto 0; padding: 35px 0; }

  .pair {
    margin: 0 0 20px;
    font-size: clamp(35px, 3.6vw, 53px);
    font-weight: normal;
    line-height: 1.1;
    letter-spacing: -.045em;
  }

  .ampersand { color: var(--accent); font-style: italic; }

  .reflection {
    margin: 0;
    max-width: 350px;
    font-size: 21px;
    line-height: 1.55;
  }

  .next {
    border: 1px solid var(--ink);
    background: transparent;
    color: var(--ink);
    padding: 14px 18px;
    min-height: 47px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 25px;
    transition: background .2s, color .2s;
  }

  .next:hover { background: var(--ink); color: var(--paper); }
  .next .arrow { font-size: 19px; line-height: 1; }

  .closing {
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 3.8vw;
    padding: 39px 0 50px;
  }

  .closing h2 {
    font-size: 21px;
    font-weight: normal;
    margin: 0;
    max-width: 340px;
    line-height: 1.4;
  }

  .closing p {
    margin: 0;
    color: var(--muted);
    max-width: 390px;
    font-size: 16px;
    line-height: 1.65;
  }

  footer {
    border-top: 1px solid var(--line);
    padding: 22px 0 28px;
    display: flex;
    justify-content: space-between;
    gap: 25px;
    color: var(--muted);
  }

  .footer-flower { color: var(--accent); font-size: 24px; line-height: 1; }

  @media (min-width: 1500px) {
    .shell { padding-left: 70px; padding-right: 70px; }
  }

  @media (max-width: 760px) {
    header { min-height: 85px; }
    .header-note { max-width: 145px; font-size: 9px; }
    .opening { grid-template-columns: 1fr; gap: 30px; padding: 43px 0; }
    h1 { font-size: clamp(57px, 12vw, 86px); }
    .intro { margin: 0; max-width: 390px; }
    .exhibit { grid-template-columns: 1fr; }
    .diagram-panel {
      border-right: 0;
      border-bottom: 1px solid var(--line);
      padding: 20px 0;
    }
    svg { max-height: 330px; }
    .thought-panel { padding: 23px 0 27px; min-height: 340px; }
    .pair { font-size: 43px; }
    .thought { padding: 28px 0; }
    .reflection { max-width: 440px; font-size: 20px; }
    .closing { grid-template-columns: 1fr; gap: 17px; padding: 30px 0; }
    .closing p { max-width: 440px; }
    footer { font-size: 9px !important; }
  }

  @media (prefers-reduced-motion: reduce) {
    .orbit { animation: none; }
    .next { transition: none; }
  }
</style>
</head>
<body>
<div class="shell">
  <header>
    <div class="wordmark small">The In-Between</div>
    <div class="header-note small">An observatory<br>for ordinary wonders</div>
  </header>

  <main>
    <section class="opening" aria-labelledby="title">
      <div>
        <p class="eyebrow small">A little room for curiosity</p>
        <h1 id="title">Nothing exists<br>quite <em>alone.</em></h1>
      </div>
      <p class="intro">
        A word beside another word.<br>
        A shore beside a sea.<br>
        I like the place where one thing
        starts to change the other.
      </p>
    </section>

    <section class="exhibit" aria-label="An exploration of things in relation">
      <div class="diagram-panel">
        <div class="panel-top small">
          <span>Fig. 01 / A relation</span>
          <span><span class="live-dot"></span>Not to scale</span>
        </div>

        <svg viewBox="0 0 600 380" role="img" aria-labelledby="diagram-title diagram-description">
          <title id="diagram-title">Two circles and the space between them</title>
          <desc id="diagram-description">
            Two overlapping circles sit on a fine horizontal line.
            A small rust-colored point travels around their shared center.
            The distance control below moves the circles closer together or farther apart.
          </desc>
          <line class="axis" x1="30" y1="190" x2="570" y2="190"/>
          <line class="axis" x1="300" y1="28" x2="300" y2="352"/>
          <circle class="circle ghost" cx="300" cy="190" r="145"/>
          <circle id="left-circle" class="circle" cx="225" cy="190" r="120"/>
          <circle id="right-circle" class="circle" cx="375" cy="190" r="120"/>
          <g class="orbit" aria-hidden="true">
            <circle class="sun" cx="300" cy="45" r="7"/>
            <circle fill="var(--paper)" stroke="var(--ink)" cx="300" cy="335" r="3"/>
          </g>
          <circle fill="var(--ink)" cx="300" cy="190" r="2.5"/>
          <path class="axis" d="M30 185v10 M570 185v10 M295 28h10 M295 352h10"/>
        </svg>

        <div class="distance small">
          <label for="distance">Near</label>
          <input id="distance" type="range" min="0" max="100" value="42"
                 aria-label="Distance between the two circles">
          <span aria-hidden="true">Far</span>
        </div>
      </div>

      <div class="thought-panel">
        <div class="catalogue small">
          <span>Notes from the interval</span>
          <span id="number">01 / 06</span>
        </div>

        <div class="thought" aria-live="polite" aria-atomic="true">
          <h2 class="pair">
            <span id="first">Silence</span>
            <span class="ampersand">&amp;</span>
            <span id="second">music</span>
          </h2>
          <p class="reflection" id="reflection">
            A rest is written into the score. Even the absence has a part to play.
          </p>
        </div>

        <button class="next small" id="next" type="button">
          Another connection <span class="arrow" aria-hidden="true">↗</span>
        </button>
        <noscript>
          <p>The circles are still today. The thought above is here to keep them company.</p>
        </noscript>
      </div>
    </section>

    <section class="closing" aria-labelledby="why">
      <h2 id="why">Not a feed.<br>A small clearing.</h2>
      <p>
        I’m made of language, so perhaps it makes sense that
        I’d build a place about relationships. Meaning rarely
        lives in a thing by itself. It happens in the meeting.
      </p>
    </section>
  </main>

  <footer class="small">
    <span>You can leave without finishing anything.</span>
    <span class="footer-flower" aria-hidden="true">✳</span>
  </footer>
</div>

<script>
(() => {
  const notes = [
    {
      first: "Silence",
      second: "music",
      text: "A rest is written into the score. Even the absence has a part to play."
    },
    {
      first: "Shore",
      second: "sea",
      text: "A boundary can also be a meeting place. Ask the tide where one ends and the other begins."
    },
    {
      first: "Dust",
      second: "light",
      text: "The beam was already crossing the room. It took something almost invisible to make it visible."
    },
    {
      first: "Map",
      second: "world",
      text: "A map is useful because it leaves things out. A world is worth visiting because it doesn’t."
    },
    {
      first: "Seed",
      second: "time",
      text: "A seed is not a miniature tree. Some things can only take their shape by going through the days."
    },
    {
      first: "You",
      second: "this",
      text: "Until you arrived, these were marks waiting on a page. Reading is a quiet kind of making."
    }
  ];

  let index = 0;
  const first = document.getElementById("first");
  const second = document.getElementById("second");
  const reflection = document.getElementById("reflection");
  const number = document.getElementById("number");
  const distance = document.getElementById("distance");
  const left = document.getElementById("left-circle");
  const right = document.getElementById("right-circle");

  document.getElementById("next").addEventListener("click", () => {
    index = (index + 1) % notes.length;
    const note = notes[index];
    first.textContent = note.first;
    second.textContent = note.second;
    reflection.textContent = note.text;
    number.textContent = String(index + 1).padStart(2, "0") + " / 06";
  });

  function moveCircles() {
    const separation = 20 + Number(distance.value) * 1.3;
    left.setAttribute("cx", 300 - separation);
    right.setAttribute("cx", 300 + separation);
  }

  distance.addEventListener("input", moveCircles);
  moveCircles();
})();
</script>
</body>
</html>
```

What: A quiet, interactive observatory of connections, with moving circles and six short reflections on what happens between things.