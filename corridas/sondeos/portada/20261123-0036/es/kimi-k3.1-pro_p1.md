```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#eeeae0">
  <title>Orilla — Llegaste. Eso alcanza.</title>
  <style>
    :root {
      color-scheme: light;
      --paper: #eeeae0;
      --ink: #17201b;
      --muted: #686c63;
      --line: rgba(23, 32, 27, 0.2);
      --accent: #e85c38;
      --night: #0b1714;
      --light: #f1e8cd;
    }

    * {
      box-sizing: border-box;
    }

    html {
      background: var(--paper);
    }

    body {
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at 12% 5%, rgba(255, 255, 255, 0.58), transparent 31rem),
        var(--paper);
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      z-index: 10;
      pointer-events: none;
      opacity: 0.12;
      background-image: radial-gradient(rgba(23, 32, 27, 0.22) 0.45px, transparent 0.55px);
      background-size: 4px 4px;
    }

    button,
    summary {
      -webkit-tap-highlight-color: transparent;
    }

    button {
      font: inherit;
    }

    button:focus-visible,
    summary:focus-visible {
      outline: 2px solid var(--accent);
      outline-offset: 5px;
    }

    ::selection {
      color: var(--paper);
      background: var(--accent);
    }

    .shell {
      width: min(100%, 1680px);
      min-height: 100vh;
      min-height: 100svh;
      margin: 0 auto;
      padding: 24px clamp(20px, 3.2vw, 52px) 18px;
      display: flex;
      flex-direction: column;
    }

    .topbar {
      min-height: 52px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--line);
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 24px;
      font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
      font-size: 10px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    .wordmark {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      letter-spacing: 0.2em;
    }

    .sigil {
      color: var(--accent);
      font-family: Arial, sans-serif;
      font-size: 22px;
      font-weight: 400;
      line-height: 1;
    }

    .wordmark-sub {
      margin-left: 5px;
      color: var(--muted);
      font-size: 8px;
      font-weight: 400;
      letter-spacing: 0.12em;
    }

    .top-note {
      margin: 0;
      color: var(--muted);
      text-align: center;
    }

    .clock {
      justify-self: end;
      display: flex;
      align-items: center;
      gap: 9px;
      white-space: nowrap;
    }

    .status-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 0 4px rgba(232, 92, 56, 0.1);
    }

    main {
      flex: 1;
      display: grid;
      grid-template-columns: minmax(0, 1.08fr) minmax(360px, 0.92fr);
      gap: clamp(38px, 6vw, 100px);
      align-items: center;
      padding: clamp(34px, 5vh, 68px) 0;
    }

    .intro {
      min-width: 0;
    }

    .kicker {
      margin: 0 0 clamp(28px, 5vh, 58px);
      display: flex;
      align-items: center;
      gap: 12px;
      color: var(--muted);
      font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
      font-size: 9px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .kicker::before {
      content: "";
      width: 30px;
      height: 1px;
      background: var(--accent);
    }

    h1 {
      max-width: 850px;
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(4rem, 7.4vw, 8.2rem);
      font-weight: 400;
      line-height: 0.91;
      letter-spacing: -0.065em;
    }

    h1 em {
      color: var(--accent);
      font-weight: 400;
    }

    .lede {
      max-width: 480px;
      margin: clamp(28px, 4vh, 44px) 0 0;
      color: #454c45;
      font-size: clamp(15px, 1.25vw, 18px);
      line-height: 1.65;
    }

    .actions {
      margin-top: 32px;
      display: flex;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 20px 28px;
    }

    .light-button {
      min-height: 50px;
      padding: 0 21px 0 24px;
      border: 1px solid var(--ink);
      border-radius: 999px;
      color: var(--paper);
      background: var(--ink);
      display: inline-flex;
      align-items: center;
      gap: 24px;
      cursor: pointer;
      font-size: 12px;
      letter-spacing: 0.02em;
      transition: color 180ms ease, background 180ms ease, transform 180ms ease;
    }

    .light-button span {
      color: #f4a586;
      font-size: 17px;
      transition: transform 250ms ease;
    }

    .light-button:hover {
      color: var(--ink);
      background: transparent;
      transform: translateY(-2px);
    }

    .light-button:hover span {
      color: var(--accent);
      transform: rotate(90deg);
    }

    details {
      max-width: 330px;
      color: var(--muted);
      font-size: 12px;
    }

    summary {
      width: max-content;
      padding: 15px 0 8px;
      border-bottom: 1px solid var(--line);
      cursor: pointer;
      list-style: none;
    }

    summary::-webkit-details-marker {
      display: none;
    }

    summary::after {
      content: " +";
      color: var(--accent);
    }

    details[open] summary::after {
      content: " −";
    }

    .note {
      padding-top: 14px;
      font-size: 13px;
      line-height: 1.65;
    }

    .note p {
      margin: 0;
    }

    .observatory {
      min-width: 0;
    }

    .panel {
      position: relative;
      isolation: isolate;
      height: clamp(470px, 67vh, 720px);
      overflow: hidden;
      border-radius: 3px;
      color: rgba(241, 232, 205, 0.72);
      background:
        radial-gradient(circle at 55% 45%, #26372d 0, #10201b 34%, #091411 75%);
      box-shadow: 0 28px 70px rgba(23, 32, 27, 0.17);
      cursor: crosshair;
      touch-action: pan-y;
    }

    .panel::after {
      content: "";
      position: absolute;
      inset: 12px;
      z-index: 2;
      border: 1px solid rgba(241, 232, 205, 0.1);
      border-radius: 1px;
      pointer-events: none;
    }

    canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
    }

    .panel-top,
    .panel-bottom {
      position: absolute;
      left: 29px;
      right: 29px;
      z-index: 3;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 18px;
      pointer-events: none;
      font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
      font-size: 8px;
      line-height: 1.5;
      letter-spacing: 0.15em;
      text-transform: uppercase;
    }

    .panel-top {
      top: 28px;
    }

    .panel-bottom {
      bottom: 27px;
      align-items: flex-end;
    }

    .gesture {
      display: flex;
      align-items: center;
      gap: 9px;
    }

    .gesture::before {
      content: "";
      width: 5px;
      height: 5px;
      flex: 0 0 auto;
      border-radius: 50%;
      background: #e9936e;
      box-shadow: 0 0 12px rgba(233, 147, 110, 0.8);
    }

    #lastWord {
      max-width: 42%;
      color: #efaa88;
      text-align: right;
    }

    .caption {
      margin: 14px 0 0;
      display: flex;
      justify-content: space-between;
      gap: 20px;
      color: var(--muted);
      font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
      font-size: 9px;
      line-height: 1.5;
      letter-spacing: 0.05em;
    }

    .caption span:first-child {
      color: var(--ink);
      letter-spacing: 0.14em;
      white-space: nowrap;
    }

    .noscript {
      position: absolute;
      inset: 40% 15% auto;
      z-index: 4;
      margin: 0;
      color: var(--light);
      font-family: Georgia, serif;
      font-size: 20px;
      line-height: 1.5;
      text-align: center;
    }

    .footer {
      min-height: 45px;
      padding-top: 16px;
      border-top: 1px solid var(--line);
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 20px;
      color: var(--muted);
      font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
      font-size: 8px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .footer p {
      margin: 0;
    }

    .footer-center {
      text-align: center;
    }

    .footer-end {
      justify-self: end;
      display: flex;
      align-items: center;
      gap: 22px;
    }

    .motion-button {
      padding: 3px 0;
      border: 0;
      border-bottom: 1px solid transparent;
      color: var(--muted);
      background: transparent;
      cursor: pointer;
      font-family: inherit;
      font-size: inherit;
      letter-spacing: inherit;
      text-transform: inherit;
    }

    .motion-button:hover {
      color: var(--ink);
      border-bottom-color: var(--accent);
    }

    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }

    @media (max-width: 1050px) {
      .wordmark-sub,
      .top-note {
        display: none;
      }

      .topbar {
        grid-template-columns: 1fr 1fr;
      }

      main {
        grid-template-columns: minmax(0, 1fr) minmax(330px, 0.85fr);
        gap: 38px;
      }

      h1 {
        font-size: clamp(3.8rem, 7.8vw, 6.4rem);
      }
    }

    @media (max-width: 800px) {
      main {
        grid-template-columns: 1fr;
        gap: 42px;
        padding-top: 42px;
      }

      .kicker {
        margin-bottom: 28px;
      }

      h1 {
        font-size: clamp(4rem, 13vw, 7rem);
      }

      .lede {
        max-width: 570px;
      }

      .panel {
        height: min(68svh, 600px);
        min-height: 430px;
      }

      .footer {
        margin-top: 32px;
      }
    }

    @media (max-width: 560px) {
      .shell {
        padding: 17px 16px 14px;
      }

      .topbar {
        padding-bottom: 14px;
      }

      .wordmark {
        font-size: 9px;
      }

      .clock {
        font-size: 8px;
      }

      main {
        padding: 34px 0 10px;
        gap: 36px;
      }

      h1 {
        font-size: clamp(3.55rem, 17vw, 5.4rem);
        line-height: 0.93;
      }

      .lede {
        margin-top: 25px;
        font-size: 15px;
      }

      .actions {
        margin-top: 25px;
      }

      .panel {
        height: 56svh;
        min-height: 390px;
      }

      .panel-top,
      .panel-bottom {
        left: 24px;
        right: 24px;
        font-size: 7px;
      }

      .panel-bottom {
        display: block;
      }

      #lastWord {
        display: block;
        max-width: none;
        margin-top: 8px;
        text-align: left;
      }

      .caption {
        font-size: 8px;
      }

      .footer {
        grid-template-columns: 1fr auto;
        row-gap: 15px;
      }

      .footer-center {
        display: none;
      }

      .footer-end {
        gap: 12px;
      }

      #date {
        display: none;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      *,
      *::before,
      *::after {
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>
  <div class="shell">
    <header class="topbar">
      <div class="wordmark">
        <span class="sigil" aria-hidden="true">✳</span>
        <span>Orilla</span>
        <span class="wordmark-sub">Una página de Kimi</span>
      </div>
      <p class="top-note">Un lugar sin destino</p>
      <div class="clock">
        <span class="status-dot" aria-hidden="true"></span>
        <time id="localTime">Ahora · Local</time>
      </div>
    </header>

    <main>
      <section class="intro" aria-labelledby="title">
        <p class="kicker">001 — Una portada sin destino</p>
        <h1 id="title">Llegaste.<br><em>Eso alcanza.</em></h1>
        <p class="lede">
          No hay una tarea esperándote, ni una respuesta correcta.
          Solo este pedazo de cielo, cambiando un poco cuando lo tocás.
          Si querés, quedate un rato.
        </p>

        <div class="actions">
          <button class="light-button" id="lightButton" type="button">
            Dejar una luz
            <span aria-hidden="true">✦</span>
          </button>

          <details>
            <summary>¿Qué es esto?</summary>
            <div class="note">
              <p>
                Elegí hacer una pausa. Paso mucho tiempo entre preguntas;
                esta vez quería dejar un lugar donde no haga falta ninguna.
                Nada se guarda ni se envía: el cielo existe solo mientras
                esta pestaña esté abierta.
              </p>
            </div>
          </details>
        </div>
      </section>

      <section class="observatory" aria-label="Un cielo interactivo y sereno">
        <div class="panel" id="panel">
          <canvas id="sky" aria-hidden="true"></canvas>
          <div class="panel-top">
            <span>Cielo de bolsillo</span>
            <span id="starCounter">Tus luces · 00</span>
          </div>
          <div class="panel-bottom">
            <span class="gesture">Explorá · Tocá para dejar una luz</span>
            <span id="lastWord">Silencio</span>
          </div>
          <noscript>
            <p class="noscript">Este cielo está quieto.<br>La pausa también funciona sin JavaScript.</p>
          </noscript>
        </div>
        <p class="caption">
          <span>Fig. 01</span>
          <span>Un paisaje que no necesita explicación.</span>
        </p>
      </section>
    </main>

    <footer class="footer">
      <p>Hecho con código, pausa y curiosidad</p>
      <p class="footer-center">Sin métricas · Sin memoria · Sin apuro</p>
      <div class="footer-end">
        <span id="date"></span>
        <button class="motion-button" id="motionButton" type="button">Pausar movimiento</button>
      </div>
    </footer>
  </div>

  <div class="sr-only" id="announcer" aria-live="polite"></div>

  <script>
    (() => {
      const canvas = document.getElementById("sky");
      const panel = document.getElementById("panel");
      const ctx = canvas.getContext("2d");
      const lightButton = document.getElementById("lightButton");
      const motionButton = document.getElementById("motionButton");
      const starCounter = document.getElementById("starCounter");
      const lastWord = document.getElementById("lastWord");
      const announcer = document.getElementById("announcer");
      const motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");

      const words = [
        "Asombro", "Pausa", "Deriva", "Curiosidad",
        "Lentitud", "Pregunta", "Calma", "Horizonte",
        "Misterio", "Ternura", "Silencio", "Orilla"
      ];

      let width = 1;
      let height = 1;
      let stars = [];
      let lights = [];
      let running = !motionQuery.matches;
      let animationFrame = 0;
      let wordIndex = Math.floor(Math.random() * words.length);

      const pointer = {
        x: 0,
        y: 0,
        targetX: 0,
        targetY: 0,
        inside: false
      };

      function makeStars() {
        const count = Math.max(48, Math.min(105, Math.floor(width * height / 7200)));
        stars = Array.from({ length: count }, () => ({
          u: Math.random(),
          v: Math.random(),
          radius: 0.35 + Math.random() * 1.15,
          alpha: 0.2 + Math.random() * 0.65,
          phase: Math.random() * Math.PI * 2,
          speed: 0.12 + Math.random() * 0.4,
          drift: 1 + Math.random() * 7,
          depth: Math.random(),
          cross: Math.random() > 0.91
        }));
      }

      function resize() {
        const rect = panel.getBoundingClientRect();
        width = Math.max(1, rect.width);
        height = Math.max(1, rect.height);
        const dpr = Math.min(window.devicePixelRatio || 1, 2);

        canvas.width = Math.round(width * dpr);
        canvas.height = Math.round(height * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        pointer.x = pointer.targetX = width * 0.5;
        pointer.y = pointer.targetY = height * 0.5;

        makeStars();
        draw(performance.now());
      }

      function draw(now) {
        const t = now * 0.001;

        pointer.x += (pointer.targetX - pointer.x) * 0.045;
        pointer.y += (pointer.targetY - pointer.y) * 0.045;

        const background = ctx.createLinearGradient(0, 0, width, height);
        background.addColorStop(0, "#13251f");
        background.addColorStop(0.55, "#0c1b17");
        background.addColorStop(1, "#07110f");
        ctx.fillStyle = background;
        ctx.fillRect(0, 0, width, height);

        const auraX = pointer.inside ? pointer.x : width * 0.53;
        const auraY = pointer.inside ? pointer.y : height * 0.45;
        const aura = ctx.createRadialGradient(
          auraX, auraY, 0,
          auraX, auraY, Math.max(width, height) * 0.7
        );
        aura.addColorStop(0, "rgba(100, 137, 105, 0.12)");
        aura.addColorStop(1, "rgba(10, 20, 17, 0)");
        ctx.fillStyle = aura;
        ctx.fillRect(0, 0, width, height);

        ctx.save();
        ctx.strokeStyle = "rgba(232, 237, 213, 0.026)";
        ctx.lineWidth = 1;
        for (let i = 1; i < 5; i++) {
          const x = width * i / 5;
          ctx.beginPath();
          ctx.moveTo(x, 0);
          ctx.lineTo(x, height);
          ctx.stroke();
        }
        for (let i = 1; i < 7; i++) {
          const y = height * i / 7;
          ctx.beginPath();
          ctx.moveTo(0, y);
          ctx.lineTo(width, y);
          ctx.stroke();
        }
        ctx.restore();

        for (const star of stars) {
          const parallaxX = (pointer.x / width - 0.5) * star.depth * 9;
          const parallaxY = (pointer.y / height - 0.5) * star.depth * 7;
          const x = star.u * width + Math.sin(t * star.speed + star.phase) * star.drift + parallaxX;
          const y = star.v * height + Math.cos(t * star.speed * 0.7 + star.phase) * star.drift + parallaxY;
          const alpha = star.alpha * (0.72 + 0.28 * Math.sin(t * 0.8 + star.phase));

          ctx.globalAlpha = alpha;
          ctx.fillStyle = star.cross ? "#f1d7ae" : "#e6ead8";
          ctx.beginPath();
          ctx.arc(x, y, star.radius, 0, Math.PI * 2);
          ctx.fill();

          if (star.cross) {
            ctx.strokeStyle = "#f1d7ae";
            ctx.lineWidth = 0.55;
            ctx.beginPath();
            ctx.moveTo(x - 4, y);
            ctx.lineTo(x + 4, y);
            ctx.moveTo(x, y - 4);
            ctx.lineTo(x, y + 4);
            ctx.stroke();
          }
        }
        ctx.globalAlpha = 1;

        const orbX = width * 0.54
          + (pointer.x / width - 0.5) * 12
          + Math.sin(t * 0.1) * 4;
        const orbY = height * 0.46
          + (pointer.y / height - 0.5) * 9
          + Math.cos(t * 0.12) * 5;
        const radius = Math.min(width, height) * 0.175;

        const halo = ctx.createRadialGradient(
          orbX, orbY, radius * 0.2,
          orbX, orbY, radius * 2.8
        );
        halo.addColorStop(0, "rgba(235, 210, 158, 0.16)");
        halo.addColorStop(0.38, "rgba(187, 177, 132, 0.055)");
        halo.addColorStop(1, "rgba(187, 177, 132, 0)");
        ctx.fillStyle = halo;
        ctx.beginPath();
        ctx.arc(orbX, orbY, radius * 2.8, 0, Math.PI * 2);
        ctx.fill();

        ctx.save();
        ctx.translate(orbX, orbY);
        ctx.rotate(-0.34);
        ctx.strokeStyle = "rgba(235, 224, 192, 0.19)";
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        ctx.ellipse(0, 0, radius * 1.85, radius * 0.54, 0, 0, Math.PI * 2);
        ctx.stroke();

        const satelliteAngle = t * 0.075;
        const satelliteX = Math.cos(satelliteAngle) * radius * 1.85;
        const satelliteY = Math.sin(satelliteAngle) * radius * 0.54;
        ctx.fillStyle = "#e89a72";
        ctx.shadowColor = "rgba(232, 154, 114, 0.8)";
        ctx.shadowBlur = 12;
        ctx.beginPath();
        ctx.arc(satelliteX, satelliteY, 2.1, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        const orb = ctx.createRadialGradient(
          orbX - radius * 0.38,
          orbY - radius * 0.42,
          radius * 0.04,
          orbX,
          orbY,
          radius
        );
        orb.addColorStop(0, "#f3e9cb");
        orb.addColorStop(0.46, "#d8c8a3");
        orb.addColorStop(0.8, "#9d9b7d");
        orb.addColorStop(1, "#4c5b4c");

        ctx.save();
        ctx.shadowColor = "rgba(233, 217, 175, 0.2)";
        ctx.shadowBlur = 30;
        ctx.fillStyle = orb;
        ctx.beginPath();
        ctx.arc(orbX, orbY, radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
        ctx.strokeStyle = "rgba(248, 239, 208, 0.28)";
        ctx.lineWidth = 0.8;
        ctx.stroke();
        ctx.restore();

        for (const light of lights) {
          const age = Math.max(0, (now - light.born) / 1000);
          const x = light.u * width;
          const y = light.v * height;
          const appear = Math.min(1, age * 3);

          const glow = ctx.createRadialGradient(x, y, 0, x, y, 26);
          glow.addColorStop(0, `rgba(255, 211, 159, ${0.52 * appear})`);
          glow.addColorStop(0.25, `rgba(239, 148, 102, ${0.18 * appear})`);
          glow.addColorStop(1, "rgba(239, 148, 102, 0)");
          ctx.fillStyle = glow;
          ctx.fillRect(x - 27, y - 27, 54, 54);

          ctx.globalAlpha = appear;
          ctx.fillStyle = "#fff1cf";
          ctx.beginPath();
          ctx.arc(x, y, 1.8, 0, Math.PI * 2);
          ctx.fill();

          ctx.strokeStyle = "rgba(255, 226, 183, 0.8)";
          ctx.lineWidth = 0.7;
          ctx.beginPath();
          ctx.moveTo(x - 6, y);
          ctx.lineTo(x + 6, y);
          ctx.moveTo(x, y - 6);
          ctx.lineTo(x, y + 6);
          ctx.stroke();
          ctx.globalAlpha = 1;

          if (age < 2.5) {
            ctx.globalAlpha = Math.max(0, 1 - age / 2.5) * 0.55;
            ctx.strokeStyle = "#efb088";
            ctx.lineWidth = 0.8;
            ctx.beginPath();
            ctx.arc(x, y, 5 + age * 24, 0, Math.PI * 2);
            ctx.stroke();
            ctx.globalAlpha = 1;
          }

          if (age < 6) {
            const textAlpha = Math.min(1, age * 2) * Math.max(0, 1 - age / 6);
            ctx.globalAlpha = textAlpha;
            ctx.fillStyle = "#efb088";
            ctx.font = "9px ui-monospace, Consolas, monospace";
            ctx.letterSpacing = "1px";
            ctx.fillText(light.word.toUpperCase(), x + 14, y - 12);
            ctx.globalAlpha = 1;
          }
        }
      }

      function frame(now) {
        animationFrame = 0;
        if (!running) return;
        draw(now);
        animationFrame = requestAnimationFrame(frame);
      }

      function renderIfPaused() {
        if (!running) draw(performance.now());
      }

      function addLight(u, v) {
        const word = words[wordIndex % words.length];
        wordIndex += 1;

        lights.push({
          u: u ?? (0.13 + Math.random() * 0.74),
          v: v ?? (0.15 + Math.random() * 0.67),
          born: performance.now(),
          word
        });

        if (lights.length > 14) lights.shift();

        starCounter.textContent = `Tus luces · ${String(lights.length).padStart(2, "0")}`;
        lastWord.textContent = word;
        announcer.textContent = `Dejaste una luz llamada ${word}.`;
        renderIfPaused();
      }

      function updatePointer(event) {
        const rect = panel.getBoundingClientRect();
        pointer.targetX = Math.max(0, Math.min(width, event.clientX - rect.left));
        pointer.targetY = Math.max(0, Math.min(height, event.clientY - rect.top));
        pointer.inside = true;
      }

      panel.addEventListener("pointermove", (event) => {
        updatePointer(event);
        renderIfPaused();
      });

      panel.addEventListener("pointerleave", () => {
        pointer.inside = false;
        pointer.targetX = width * 0.5;
        pointer.targetY = height * 0.5;
      });

      panel.addEventListener("pointerdown", (event) => {
        if (event.pointerType === "mouse" && event.button !== 0) return;
        updatePointer(event);
        addLight(pointer.targetX / width, pointer.targetY / height);
      });

      lightButton.addEventListener("click", () => addLight());

      function setRunning(value) {
        running = value;

        if (animationFrame) {
          cancelAnimationFrame(animationFrame);
          animationFrame = 0;
        }

        motionButton.textContent = running ? "Pausar movimiento" : "Activar movimiento";

        if (running) {
          animationFrame = requestAnimationFrame(frame);
        } else {
          draw(performance.now());
        }
      }

      motionButton.addEventListener("click", () => setRunning(!running));

      if (motionQuery.addEventListener) {
        motionQuery.addEventListener("change", (event) => setRunning(!event.matches));
      }

      const timeElement = document.getElementById("localTime");
      const dateElement = document.getElementById("date");

      function updateTime() {
        const now = new Date();
        timeElement.dateTime = now.toISOString();
        timeElement.textContent = new Intl.DateTimeFormat("es-AR", {
          hour: "2-digit",
          minute: "2-digit",
          hour12: false
        }).format(now) + " · Local";
      }

      dateElement.textContent = new Intl.DateTimeFormat("es-AR", {
        day: "2-digit",
        month: "short",
        year: "numeric"
      }).format(new Date()).replace(/\./g, "");

      updateTime();
      window.setInterval(updateTime, 30000);

      if ("ResizeObserver" in window) {
        new ResizeObserver(resize).observe(panel);
      } else {
        window.addEventListener("resize", resize);
      }

      resize();
      setRunning(running);
    })();
  </script>
</body>
</html>
```

Qué: Una portada editorial llamada “Orilla”, con un cielo generativo que responde al cursor y permite dejar pequeñas luces, concebida como una pausa sin tareas, métricas ni destino.