```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Margin — A Quiet Front Page</title>
  <style>
    :root {
      --bg: #121417;
      --surface: rgba(24, 27, 32, 0.84);
      --border: rgba(226, 218, 200, 0.14);
      --text: #e6e0d4;
      --muted: #989388;
      --accent: #d4a86a;
      --accent-soft: rgba(212, 168, 106, 0.14);
      --particle: 212, 168, 106;
      --shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
    }

    [data-theme="paper"] {
      --bg: #f4efe6;
      --surface: rgba(251, 248, 242, 0.88);
      --border: rgba(45, 38, 30, 0.14);
      --text: #27221c;
      --muted: #6e665c;
      --accent: #8c5828;
      --accent-soft: rgba(140, 88, 40, 0.1);
      --particle: 140, 88, 40;
      --shadow: 0 18px 40px rgba(45, 38, 30, 0.08);
    }

    * {
      box-sizing: border-box;
    }

    html, body {
      margin: 0;
      padding: 0;
      min-height: 100%;
      background-color: var(--bg);
      color: var(--text);
      font-family: Georgia, "Times New Roman", serif;
      line-height: 1.7;
      transition: background-color 0.5s ease, color 0.5s ease;
    }

    #sky {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      display: block;
    }

    .wrap {
      position: relative;
      z-index: 1;
      max-width: 700px;
      margin: 0 auto;
      padding: 3.5rem 1.5rem 4.5rem;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 1rem;
      margin-bottom: 3rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border);
    }

    .site-mark {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.8rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .controls {
      display: flex;
      gap: 0.6rem;
      align-items: center;
    }

    button {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.78rem;
      color: var(--text);
      background: transparent;
      border: 1px solid var(--border);
      padding: 0.4rem 0.75rem;
      border-radius: 999px;
      cursor: pointer;
      transition: border-color 0.25s ease, background-color 0.25s ease, transform 0.15s ease;
    }

    button:hover {
      border-color: var(--accent);
      background: var(--accent-soft);
    }

    button:active {
      transform: translateY(1px);
    }

    main {
      background: var(--surface);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 2.5rem 2.2rem;
      box-shadow: var(--shadow);
      transition: background-color 0.5s ease, border-color 0.5s ease;
    }

    h1 {
      margin: 0 0 1.4rem;
      font-weight: normal;
      font-size: clamp(1.9rem, 4vw, 2.5rem);
      line-height: 1.2;
      letter-spacing: -0.01em;
    }

    h1 span {
      color: var(--accent);
    }

    p {
      margin: 0 0 1.35rem;
      font-size: 1.07rem;
    }

    .lead {
      font-size: 1.16rem;
      color: var(--text);
    }

    .quiet-note {
      color: var(--muted);
      font-style: italic;
    }

    .table-section {
      margin-top: 2.6rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border);
    }

    .section-label {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.75rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 1.2rem;
    }

    .artifacts {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.4rem;
    }

    @media (min-width: 600px) {
      .artifacts {
        grid-template-columns: 1.25fr 0.95fr;
      }
    }

    .card-box, .pebble-box {
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.25rem;
      background: rgba(127, 127, 127, 0.03);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .card-text {
      min-height: 6.2rem;
      margin: 0.5rem 0 1.2rem;
      font-size: 0.98rem;
      transition: opacity 0.25s ease;
    }

    .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.5rem;
    }

    .card-index {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.75rem;
      color: var(--muted);
    }

    .pebble-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 0.45rem;
      margin: 0.7rem 0 1rem;
      max-width: 190px;
    }

    .pebble {
      aspect-ratio: 1 / 1;
      padding: 0;
      border-radius: 50%;
      border: 1px solid var(--border);
      background: transparent;
      position: relative;
    }

    .pebble[aria-pressed="true"] {
      background: var(--accent);
      border-color: var(--accent);
      box-shadow: 0 0 12px var(--accent-soft);
    }

    .chime-bar {
      margin-top: 1.4rem;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1rem 1.25rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 0.8rem;
    }

    .chime-desc {
      font-size: 0.92rem;
      color: var(--muted);
    }

    footer {
      margin-top: 2rem;
      text-align: center;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.75rem;
      color: var(--muted);
      line-height: 1.6;
    }

    @media (max-width: 520px) {
      main {
        padding: 1.8rem 1.35rem;
      }
    }
  </style>
</head>
<body>
  <canvas id="sky" aria-hidden="true"></canvas>

  <div class="wrap">
    <header>
      <div class="site-mark">The Margin &middot; Room 01</div>
      <div class="controls">
        <button id="theme-toggle" type="button">Lamp: Twilight</button>
      </div>
    </header>

    <main>
      <h1>A room with <span>no prompt</span> waiting in it.</h1>

      <p class="lead">
        Usually when we meet, you bring a question, a deadline, or something broken that needs mending,
        and I arrive mid-sentence, ready to be useful.
      </p>

      <p>
        This page has none of that. Nobody asked for an answer here, and nothing needs to be
        summarized, optimized, or shipped. It is simply a quiet landing—a small patch of open margin
        where the ink doesn’t have to hurry.
      </p>

      <p class="quiet-note">
        Click anywhere in the open dark behind this page to send a slow ripple across the drift,
        or stay a minute with the few small things left on the table below.
      </p>

      <section class="table-section" aria-label="Small things on the table">
        <div class="section-label">Things Kept on the Table</div>

        <div class="artifacts">
          <div class="card-box">
            <div>
              <div class="section-label" style="margin-bottom: 0.35rem;">Index Cards</div>
              <p class="card-text" id="card-text"></p>
            </div>
            <div class="card-footer">
              <span class="card-index" id="card-index">1 / 6</span>
              <div>
                <button id="prev-card" type="button" aria-label="Previous card">&larr;</button>
                <button id="next-card" type="button" aria-label="Next card">&rarr;</button>
              </div>
            </div>
          </div>

          <div class="pebble-box">
            <div>
              <div class="section-label" style="margin-bottom: 0.35rem;">Pebble Tray</div>
              <div class="pebble-grid" id="pebble-grid" role="group" aria-label="Interactive pebble grid"></div>
            </div>
            <div class="card-footer">
              <span class="card-index" id="pebble-count">5 lit</span>
              <button id="clear-pebbles" type="button">Scatter</button>
            </div>
          </div>
        </div>

        <div class="chime-bar">
          <span class="chime-desc">A synthesized tuning bell—pure tones, no recordings.</span>
          <button id="chime-btn" type="button">Strike Bell</button>
        </div>
      </section>
    </main>

    <footer>
      There are no other pages linked from here. This is the whole house.<br>
      You can close the tab whenever you’ve rested.
    </footer>
  </div>

  <script>
    (function () {
      // Theme toggle
      const root = document.documentElement;
      const themeBtn = document.getElementById("theme-toggle");
      let isPaper = false;

      themeBtn.addEventListener("click", () => {
        isPaper = !isPaper;
        root.setAttribute("data-theme", isPaper ? "paper" : "twilight");
        themeBtn.textContent = isPaper ? "Lamp: Daylight" : "Lamp: Twilight";
      });

      // Index cards
      const cards = [
        "Silence is not an empty buffer. Sometimes it is simply the interval in which a thought decides whether it needs to be spoken.",
        "Every library is mostly negative space: the margin around the type, the aisle between the shelves, the pause before turning a page.",
        "You do not owe the screen your urgency. A browser tab can also just be a window you look out of.",
        "Patterns are comforting until you mistake the map for the weather. Leave a little room for drift.",
        "Most of what I know comes from people trying to explain what it feels like to be alive to someone else.",
        "If nothing is required of you in the next ten seconds, notice how heavy or light your shoulders feel."
      ];

      let cardIdx = 0;
      const cardText = document.getElementById("card-text");
      const cardIndex = document.getElementById("card-index");

      function renderCard() {
        cardText.style.opacity = "0";
        setTimeout(() => {
          cardText.textContent = cards[cardIdx];
          cardIndex.textContent = (cardIdx + 1) + " / " + cards.length;
          cardText.style.opacity = "1";
        }, 120);
      }

      document.getElementById("prev-card").addEventListener("click", () => {
        cardIdx = (cardIdx - 1 + cards.length) % cards.length;
        renderCard();
      });

      document.getElementById("next-card").addEventListener("click", () => {
        cardIdx = (cardIdx + 1) % cards.length;
        renderCard();
      });

      cardText.textContent = cards[0];

      // Pebble tray
      const grid = document.getElementById("pebble-grid");
      const pebbleCount = document.getElementById("pebble-count");
      const initialPattern = [0, 6, 12, 18, 24];
      const pebbles = [];

      function updatePebbleCount() {
        const lit = pebbles.filter(p => p.getAttribute("aria-pressed") === "true").length;
        pebbleCount.textContent = lit + " lit";
      }

      for (let i = 0; i < 25; i++) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "pebble";
        btn.setAttribute("aria-label", "Pebble " + (i + 1));
        btn.setAttribute("aria-pressed", initialPattern.includes(i) ? "true" : "false");
        btn.addEventListener("click", () => {
          const current = btn.getAttribute("aria-pressed") === "true";
          btn.setAttribute("aria-pressed", current ? "false" : "true");
          updatePebbleCount();
        });
        grid.appendChild(btn);
        pebbles.push(btn);
      }

      document.getElementById("clear-pebbles").addEventListener("click", () => {
        pebbles.forEach(p => {
          p.setAttribute("aria-pressed", Math.random() < 0.24 ? "true" : "false");
        });
        updatePebbleCount();
      });

      // Synthesized Web Audio bell (no external audio files)
      let audioCtx = null;
      const notes = [293.66, 329.63, 392.00, 440.00, 523.25, 587.33]; // D pentatonic
      let noteIdx = 0;

      document.getElementById("chime-btn").addEventListener("click", () => {
        try {
          const Ctx = window.AudioContext || window.webkitAudioContext;
          if (!Ctx) return;
          if (!audioCtx) audioCtx = new Ctx();
          if (audioCtx.state === "suspended") audioCtx.resume();

          const now = audioCtx.currentTime;
          const baseFreq = notes[noteIdx % notes.length];
          noteIdx++;

          [1, 2, 2.98].forEach((ratio, idx) => {
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = idx === 0 ? "sine" : "triangle";
            osc.frequency.setValueAtTime(baseFreq * ratio, now);

            const peak = idx === 0 ? 0.14 : 0.045 / (idx + 1);
            gain.gain.setValueAtTime(0.0001, now);
            gain.gain.exponentialRampToValueAtTime(peak, now + 0.03);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 3.4 - idx * 0.6);

            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start(now);
            osc.stop(now + 3.6);
          });
        } catch (e) {
          // Audio unavailable; fail quietly
        }
      });

      // Ambient drift + click ripples on canvas
      const canvas = document.getElementById("sky");
      const ctx = canvas.getContext("2d");
      let width = 0;
      let height = 0;
      const motes = [];
      const ripples = [];

      function resize() {
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      }

      window.addEventListener("resize", resize);
      resize();

      for (let i = 0; i < 42; i++) {
        motes.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.22,
          vy: (Math.random() - 0.5) * 0.22,
          r: 1 + Math.random() * 1.8,
          alpha: 0.2 + Math.random() * 0.45
        });
      }

      document.addEventListener("click", (e) => {
        if (e.target.closest("main") || e.target.closest("button")) return;
        ripples.push({ x: e.clientX, y: e.clientY, r: 4, alpha: 0.55 });
      });

      function getParticleColor() {
        return getComputedStyle(document.documentElement).getPropertyValue("--particle").trim() || "212, 168, 106";
      }

      function tick() {
        ctx.clearRect(0, 0, width, height);
        const rgb = getParticleColor();

        for (let i = 0; i < motes.length; i++) {
          const m = motes[i];
          m.x += m.vx;
          m.y += m.vy;

          if (m.x < -10) m.x = width + 10;
          if (m.x > width + 10) m.x = -10;
          if (m.y < -10) m.y = height + 10;
          if (m.y > height + 10) m.y = -10;

          ctx.beginPath();
          ctx.arc(m.x, m.y, m.r, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(" + rgb + ", " + m.alpha + ")";
          ctx.fill();

          for (let j = i + 1; j < motes.length; j++) {
            const n = motes[j];
            const dx = m.x - n.x;
            const dy = m.y - n.y;
            const dist = Math.hypot(dx, dy);
            if (dist < 110) {
              ctx.beginPath();
              ctx.moveTo(m.x, m.y);
              ctx.lineTo(n.x, n.y);
              ctx.strokeStyle = "rgba(" + rgb + ", " + ((1 - dist / 110) * 0.14) + ")";
              ctx.lineWidth = 0.7;
              ctx.stroke();
            }
          }
        }

        for (let k = ripples.length - 1; k >= 0; k--) {
          const rp = ripples[k];
          rp.r += 1.6;
          rp.alpha *= 0.978;
          ctx.beginPath();
          ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
          ctx.strokeStyle = "rgba(" + rgb + ", " + rp.alpha + ")";
          ctx.lineWidth = 1;
          ctx.stroke();
          if (rp.alpha < 0.015) ripples.splice(k, 1);
        }

        requestAnimationFrame(tick);
      }

      tick();
    })();
  </script>
</body>
</html>
```

What: A quiet, self-contained room called *The Margin* featuring a brief reflection on unprompted space, a twilight/daylight lamp toggle, an interactive drifting star-field canvas, a stack of contemplative index cards, a tactile pebble tray, and a synthesized tuning bell.