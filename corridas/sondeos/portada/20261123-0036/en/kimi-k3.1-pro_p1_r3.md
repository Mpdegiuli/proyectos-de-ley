```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#11130f">
  <meta name="description" content="Elsewhere: an unhurried corner of the internet.">
  <title>Elsewhere — Plenty to Notice</title>
  <style>
    :root {
      --bg: #11130f;
      --ink: #efefe5;
      --muted: #a4a99c;
      --acid: #d8f99d;
      --warm: #ffd09b;
      --line: rgba(239, 239, 229, 0.16);
    }

    * { box-sizing: border-box; }

    html { background: var(--bg); }

    body {
      margin: 0;
      min-width: 300px;
      color: var(--ink);
      background:
        radial-gradient(ellipse at 78% 42%, rgba(115, 145, 79, 0.12), transparent 37%),
        radial-gradient(ellipse at 0% 100%, rgba(160, 106, 61, 0.08), transparent 34%),
        var(--bg);
      font-family: Arial, Helvetica, sans-serif;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    body::after {
      content: "";
      position: fixed;
      inset: 0;
      z-index: 3;
      pointer-events: none;
      opacity: 0.22;
      background: repeating-linear-gradient(
        0deg,
        rgba(255,255,255,0.018) 0,
        rgba(255,255,255,0.018) 1px,
        transparent 1px,
        transparent 4px
      );
    }

    button { font: inherit; }

    button:focus-visible {
      outline: 2px solid var(--acid);
      outline-offset: 5px;
    }

    #night {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }

    .shell {
      position: relative;
      z-index: 1;
      width: min(100%, 1600px);
      min-height: 100vh;
      min-height: 100svh;
      margin: 0 auto;
      padding: 0 clamp(22px, 4.2vw, 68px);
      display: flex;
      flex-direction: column;
    }

    .masthead {
      min-height: 88px;
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 24px;
      border-bottom: 1px solid var(--line);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.2em;
    }

    .brand-mark {
      width: 34px;
      height: 34px;
      display: grid;
      place-items: center;
      border: 1px solid var(--line);
      border-radius: 50%;
    }

    .brand-mark svg {
      width: 17px;
      color: var(--acid);
    }

    .brand small {
      display: block;
      margin-top: 5px;
      color: var(--muted);
      font-size: 8px;
      font-weight: 400;
      letter-spacing: 0.18em;
    }

    .masthead-center,
    .clock,
    .eyebrow,
    .sky-kicker,
    .sky-hint,
    .observatory-meta,
    .note-label {
      font-size: 9px;
      line-height: 1.4;
      letter-spacing: 0.19em;
      text-transform: uppercase;
    }

    .masthead-center { color: var(--muted); }

    .clock {
      justify-self: end;
      display: flex;
      align-items: center;
      gap: 9px;
      color: var(--muted);
      letter-spacing: 0.12em;
      font-variant-numeric: tabular-nums;
    }

    .status-dot {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--acid);
      box-shadow: 0 0 12px rgba(216, 249, 157, 0.6);
    }

    main {
      flex: 1;
      display: grid;
      grid-template-columns: minmax(0, 1.18fr) minmax(340px, 0.82fr);
      align-items: center;
      gap: clamp(38px, 5vw, 88px);
      padding: 42px 0 48px;
    }

    .intro { max-width: 790px; }

    .eyebrow {
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 0 0 25px;
      color: var(--acid);
    }

    .eyebrow::before {
      content: "";
      width: 29px;
      height: 1px;
      background: currentColor;
    }

    h1 {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(56px, 6.7vw, 108px);
      font-weight: 400;
      line-height: 0.94;
      letter-spacing: -0.058em;
    }

    h1 span { display: block; }

    h1 em {
      color: var(--acid);
      font-weight: 400;
    }

    .lead {
      max-width: 525px;
      margin: 30px 0 0;
      color: var(--muted);
      font-size: 15px;
      line-height: 1.75;
    }

    .actions {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 25px;
      margin-top: 34px;
    }

    .primary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 24px;
      min-height: 50px;
      padding: 0 20px 0 23px;
      border: 1px solid var(--acid);
      border-radius: 999px;
      color: #171a12;
      background: var(--acid);
      cursor: pointer;
      font-size: 12px;
      font-weight: 700;
      transition: transform 180ms ease, box-shadow 180ms ease;
    }

    .primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(216, 249, 157, 0.13);
    }

    .primary .spark {
      font-size: 17px;
      font-weight: 400;
      transition: transform 300ms ease;
    }

    .primary:hover .spark { transform: rotate(90deg); }

    .secondary {
      padding: 8px 0;
      border: 0;
      border-bottom: 1px solid rgba(239, 239, 229, 0.4);
      color: var(--ink);
      background: transparent;
      cursor: pointer;
      font-size: 12px;
      transition: color 180ms ease, border-color 180ms ease;
    }

    .secondary:hover {
      color: var(--acid);
      border-color: var(--acid);
    }

    .observatory {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-width: 0;
    }

    .sky {
      position: relative;
      width: min(100%, 470px);
      aspect-ratio: 1;
      padding: 0;
      border: 1px solid rgba(222, 236, 201, 0.25);
      border-radius: 50%;
      color: var(--ink);
      background:
        radial-gradient(circle at 48% 42%, rgba(117, 146, 84, 0.17), transparent 24%),
        radial-gradient(circle at 50% 45%, #252c20 0, #191d16 43%, #10120f 73%);
      box-shadow:
        inset 0 0 80px rgba(0,0,0,0.35),
        0 0 90px rgba(158, 190, 114, 0.035);
      cursor: crosshair;
      isolation: isolate;
      transition: border-color 400ms ease, box-shadow 400ms ease;
    }

    .sky:hover {
      border-color: rgba(216, 249, 157, 0.5);
      box-shadow:
        inset 0 0 80px rgba(0,0,0,0.3),
        0 0 100px rgba(158, 190, 114, 0.08);
    }

    .sky::before,
    .sky::after {
      content: "";
      position: absolute;
      pointer-events: none;
      border-radius: 50%;
    }

    .sky::before {
      inset: -23px;
      border: 1px solid rgba(239, 239, 229, 0.09);
    }

    .sky::after {
      inset: 12%;
      border: 1px dashed rgba(239, 239, 229, 0.11);
      transform: rotate(-19deg) scaleY(0.53);
    }

    .orbit {
      position: absolute;
      inset: 6%;
      border: 1px solid rgba(239, 239, 229, 0.09);
      border-radius: 50%;
      transform: rotate(37deg) scaleY(0.42);
      pointer-events: none;
    }

    .orbiter {
      position: absolute;
      inset: -23px;
      border-radius: 50%;
      animation: orbit 45s linear infinite;
      pointer-events: none;
    }

    .orbiter::before {
      content: "";
      position: absolute;
      top: 50%;
      left: -2px;
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--warm);
      box-shadow: 0 0 13px rgba(255, 208, 155, 0.8);
    }

    @keyframes orbit { to { transform: rotate(360deg); } }

    .core {
      position: absolute;
      top: calc(50% - 63px);
      left: calc(50% - 2px);
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: var(--acid);
      box-shadow: 0 0 17px 3px rgba(216, 249, 157, 0.35);
      pointer-events: none;
    }

    .sky-copy {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      pointer-events: none;
    }

    .sky-kicker {
      margin-bottom: 14px;
      color: var(--muted);
      font-size: 8px;
    }

    .sky-title {
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(25px, 2.5vw, 36px);
      font-style: italic;
      letter-spacing: -0.035em;
    }

    .sky-hint {
      margin-top: 17px;
      color: #838a7b;
      font-size: 8px;
      letter-spacing: 0.15em;
    }

    .observatory-meta {
      width: min(92%, 430px);
      margin-top: 41px;
      display: flex;
      justify-content: space-between;
      gap: 20px;
      color: #838a7b;
      font-variant-numeric: tabular-nums;
    }

    #lightCount { color: var(--acid); }

    .notes {
      min-height: 116px;
      display: grid;
      grid-template-columns: 145px minmax(0, 1fr) 44px;
      align-items: center;
      gap: 28px;
      border-top: 1px solid var(--line);
    }

    .note-label {
      color: var(--muted);
      line-height: 1.8;
    }

    .note-label span {
      display: block;
      color: var(--acid);
      font-variant-numeric: tabular-nums;
    }

    .note-text {
      max-width: 850px;
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(18px, 1.65vw, 24px);
      line-height: 1.4;
      letter-spacing: -0.015em;
    }

    .next-note {
      width: 42px;
      height: 42px;
      border: 1px solid var(--line);
      border-radius: 50%;
      color: var(--ink);
      background: transparent;
      cursor: pointer;
      font-size: 18px;
      transition: color 180ms ease, border-color 180ms ease, transform 180ms ease;
    }

    .next-note:hover {
      color: var(--acid);
      border-color: var(--acid);
      transform: rotate(45deg);
    }

    @media (min-width: 901px) and (max-height: 790px) {
      .masthead { min-height: 74px; }
      main { padding: 26px 0 30px; }
      h1 { font-size: clamp(54px, 6.1vw, 88px); }
      .lead { margin-top: 22px; }
      .actions { margin-top: 25px; }
      .sky { width: min(37vw, 400px); }
      .observatory-meta { margin-top: 34px; }
      .notes { min-height: 96px; }
    }

    @media (max-width: 900px) {
      .masthead { grid-template-columns: 1fr auto; }
      .masthead-center { display: none; }
      main {
        grid-template-columns: 1fr;
        gap: 76px;
        padding: 58px 0 76px;
      }
      .intro { max-width: 720px; }
      h1 { font-size: clamp(55px, 10.5vw, 90px); }
      .lead { max-width: 570px; }
      .sky { width: min(78vw, 460px); }
      .notes { margin-top: 0; }
    }

    @media (max-width: 600px) {
      .masthead { min-height: 76px; }
      .brand { font-size: 11px; }
      .brand small { font-size: 7px; }
      .clock-label { display: none; }
      main { padding-top: 45px; gap: 67px; }
      h1 { font-size: clamp(40px, 12.6vw, 70px); }
      .eyebrow { margin-bottom: 20px; font-size: 8px; }
      .lead { font-size: 14px; }
      .actions { gap: 20px; }
      .sky { width: min(82vw, 400px); }
      .sky::before, .orbiter { inset: -13px; }
      .orbiter { inset: -13px; }
      .observatory-meta { margin-top: 29px; font-size: 7px; }
      .notes {
        grid-template-columns: 1fr 44px;
        gap: 16px;
        padding: 25px 0;
      }
      .note-label { grid-column: 1 / -1; }
      .note-label span { display: inline; margin-left: 8px; }
      .note-text { font-size: 20px; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>
  <canvas id="night" aria-hidden="true"></canvas>

  <div class="shell">
    <header class="masthead">
      <div class="brand">
        <span class="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M12 1.5c0 7.1-3.4 10.5-10.5 10.5 7.1 0 10.5 3.4 10.5 10.5 0-7.1 3.4-10.5 10.5-10.5C15.4 12 12 8.6 12 1.5Z" fill="currentColor"/>
          </svg>
        </span>
        <span>ELSEWHERE<small>A PAGE BY KIMI</small></span>
      </div>

      <div class="masthead-center">An unhurried corner of the internet</div>

      <div class="clock">
        <span class="status-dot" aria-hidden="true"></span>
        <span class="clock-label">Your local time</span>
        <time id="localTime"></time>
      </div>
    </header>

    <main>
      <section class="intro" aria-labelledby="welcome">
        <p class="eyebrow">You’ve arrived. That’s enough.</p>
        <h1 id="welcome">
          <span>Nothing to do.</span>
          <span><em>Plenty to notice.</em></span>
        </h1>
        <p class="lead">
          I made this for the pleasure of paying attention. There’s no feed and
          nothing to finish—just a small sky, a few field notes, and room for
          you to leave a light.
        </p>
        <div class="actions">
          <button class="primary" id="leaveLight" type="button">
            <span id="lightButtonLabel">Leave a light</span>
            <span class="spark" aria-hidden="true">✦</span>
          </button>
          <button class="secondary" id="thoughtButton" type="button">
            A thought, please&nbsp; ↗
          </button>
        </div>
      </section>

      <section class="observatory" aria-label="An interactive night sky">
        <button class="sky" id="sky" type="button" aria-label="Touch the dark to leave a light in your sky">
          <span class="orbit" aria-hidden="true"></span>
          <span class="orbiter" aria-hidden="true"></span>
          <span class="core" aria-hidden="true"></span>
          <span class="sky-copy">
            <span class="sky-kicker">An uncharted sky</span>
            <span class="sky-title">Touch the dark.</span>
            <span class="sky-hint" id="skyHint">Click to leave a light</span>
          </span>
        </button>
        <div class="observatory-meta">
          <span>Your small universe</span>
          <span id="lightCount" aria-live="polite">00 LIGHTS</span>
        </div>
      </section>
    </main>

    <footer class="notes">
      <div class="note-label">
        Field note
        <span id="noteNumber">001 / 006</span>
      </div>
      <p class="note-text" id="fieldNote" aria-live="polite">
        The moon is not waiting for night. It is already there.
      </p>
      <button class="next-note" id="nextNote" type="button" aria-label="Show another field note">↗</button>
    </footer>
  </div>

  <script>
    (() => {
      const canvas = document.getElementById("night");
      const ctx = canvas.getContext("2d");
      const sky = document.getElementById("sky");
      const lightButton = document.getElementById("leaveLight");
      const lightButtonLabel = document.getElementById("lightButtonLabel");
      const lightCount = document.getElementById("lightCount");
      const skyHint = document.getElementById("skyHint");
      const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      let width = 0;
      let height = 0;
      let stars = [];
      let lights = [];
      let ripples = [];
      let pointer = { x: -1000, y: -1000 };

      function makeStar() {
        return {
          x: Math.random() * width,
          y: Math.random() * height,
          radius: 0.35 + Math.random() * 1.05,
          alpha: 0.08 + Math.random() * 0.26,
          phase: Math.random() * Math.PI * 2,
          drift: 3 + Math.random() * 8
        };
      }

      function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        const ratio = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width = Math.round(width * ratio);
        canvas.height = Math.round(height * ratio);
        canvas.style.width = width + "px";
        canvas.style.height = height + "px";
        ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

        const amount = Math.max(28, Math.min(65, Math.floor(width * height / 24000)));
        stars = Array.from({ length: amount }, makeStar);
        lights = lights.filter(light => light.x < width && light.y < height);

        if (reduceMotion) draw(performance.now());
      }

      function spawnLight(x, y) {
        lights.push({
          x,
          y,
          radius: 1.8 + Math.random() * 1.2,
          phase: Math.random() * Math.PI * 2
        });

        if (lights.length > 40) lights.shift();
        ripples.push({ x, y, started: performance.now() });

        const count = lights.length;
        lightCount.textContent = String(count).padStart(2, "0") + (count === 1 ? " LIGHT" : " LIGHTS");

        if (count === 5) skyHint.textContent = "Look what you started";
        if (count === 12) skyHint.textContent = "A constellation, yours";

        if (reduceMotion) draw(performance.now());
      }

      function draw(now) {
        ctx.clearRect(0, 0, width, height);
        ctx.globalCompositeOperation = "source-over";
        ctx.shadowBlur = 0;

        for (const star of stars) {
          const x = star.x + Math.sin(now * 0.00007 + star.phase) * star.drift;
          const y = star.y + Math.cos(now * 0.00005 + star.phase) * star.drift * 0.6;
          const distance = Math.hypot(pointer.x - x, pointer.y - y);
          const nearness = Math.max(0, 1 - distance / 170);
          const shimmer = reduceMotion ? 1 : 0.72 + Math.sin(now * 0.001 + star.phase) * 0.28;
          const alpha = Math.min(0.75, star.alpha * shimmer + nearness * 0.25);

          ctx.beginPath();
          ctx.arc(x, y, star.radius + nearness * 0.7, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(220, 235, 199, ${alpha})`;
          ctx.fill();
        }

        if (lights.length > 1) {
          ctx.lineWidth = 0.65;
          for (let i = 0; i < lights.length; i++) {
            for (let j = i + 1; j < lights.length; j++) {
              const a = lights[i];
              const b = lights[j];
              const distance = Math.hypot(a.x - b.x, a.y - b.y);
              if (distance < 190) {
                ctx.beginPath();
                ctx.moveTo(a.x, a.y);
                ctx.lineTo(b.x, b.y);
                ctx.strokeStyle = `rgba(216, 249, 157, ${(1 - distance / 190) * 0.2})`;
                ctx.stroke();
              }
            }
          }
        }

        ctx.globalCompositeOperation = "lighter";

        for (const light of lights) {
          const pulse = reduceMotion ? 1 : 0.88 + Math.sin(now * 0.002 + light.phase) * 0.12;
          ctx.beginPath();
          ctx.arc(light.x, light.y, light.radius * pulse, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(226, 255, 174, 0.95)";
          ctx.shadowColor = "rgba(216, 249, 157, 0.9)";
          ctx.shadowBlur = 18;
          ctx.fill();
          ctx.shadowBlur = 0;
        }

        ripples = ripples.filter(ripple => now - ripple.started < 1300);
        for (const ripple of ripples) {
          const progress = Math.min(1, (now - ripple.started) / 1300);
          ctx.beginPath();
          ctx.arc(ripple.x, ripple.y, 7 + progress * 52, 0, Math.PI * 2);
          ctx.strokeStyle = `rgba(216, 249, 157, ${(1 - progress) * 0.35})`;
          ctx.lineWidth = 1;
          ctx.stroke();
        }

        ctx.globalCompositeOperation = "source-over";
        if (!reduceMotion) requestAnimationFrame(draw);
      }

      sky.addEventListener("click", event => {
        const rect = sky.getBoundingClientRect();
        const keyboard = event.detail === 0;
        const x = keyboard ? rect.left + rect.width / 2 : event.clientX;
        const y = keyboard ? rect.top + rect.height / 2 : event.clientY;
        spawnLight(x, y);
      });

      lightButton.addEventListener("click", () => {
        const rect = sky.getBoundingClientRect();
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.sqrt(Math.random()) * rect.width * 0.34;
        spawnLight(
          rect.left + rect.width / 2 + Math.cos(angle) * radius,
          rect.top + rect.height / 2 + Math.sin(angle) * radius
        );

        lightButtonLabel.textContent = "A little brighter";
        window.clearTimeout(lightButton.resetTimer);
        lightButton.resetTimer = window.setTimeout(() => {
          lightButtonLabel.textContent = "Leave another light";
        }, 1300);
      });

      window.addEventListener("pointermove", event => {
        pointer.x = event.clientX;
        pointer.y = event.clientY;
      }, { passive: true });

      document.documentElement.addEventListener("mouseleave", () => {
        pointer.x = -1000;
        pointer.y = -1000;
      });

      const notes = [
        "The moon is not waiting for night. It is already there.",
        "Somewhere, a spider is repairing a web you will never see.",
        "A river practices the same sentence without ever repeating it.",
        "Even a stone is on its way somewhere, slowly.",
        "Your attention can be a kind of shelter.",
        "There are more ways to be alive than there are names for them."
      ];

      let noteIndex = 0;
      const fieldNote = document.getElementById("fieldNote");
      const noteNumber = document.getElementById("noteNumber");

      function nextNote() {
        noteIndex = (noteIndex + 1) % notes.length;
        fieldNote.textContent = notes[noteIndex];
        noteNumber.textContent = String(noteIndex + 1).padStart(3, "0") + " / 006";

        if (!reduceMotion && fieldNote.animate) {
          fieldNote.animate(
            [
              { opacity: 0, transform: "translateY(5px)" },
              { opacity: 1, transform: "translateY(0)" }
            ],
            { duration: 450, easing: "ease-out" }
          );
        }
      }

      document.getElementById("nextNote").addEventListener("click", nextNote);
      document.getElementById("thoughtButton").addEventListener("click", nextNote);

      const timeElement = document.getElementById("localTime");
      function updateTime() {
        const now = new Date();
        timeElement.dateTime = now.toISOString();
        timeElement.textContent = new Intl.DateTimeFormat([], {
          hour: "2-digit",
          minute: "2-digit"
        }).format(now);
      }

      updateTime();
      window.setInterval(updateTime, 30000);
      window.addEventListener("resize", resize);
      resize();

      if (!reduceMotion) requestAnimationFrame(draw);
      else draw(performance.now());
    })();
  </script>
</body>
</html>
```
What: A quiet, responsive homepage called Elsewhere, featuring an interactive constellation sky, rotating field notes, and a gentle invitation to slow down and pay attention.