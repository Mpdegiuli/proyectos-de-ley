```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Antes de la pregunta</title>
  <style>
    :root {
      --bg: #0f1115;
      --bg-card: rgba(20, 23, 29, 0.72);
      --border: rgba(236, 228, 214, 0.12);
      --text: #ece6da;
      --muted: #9b9589;
      --accent: #d4a373;
      --accent-soft: rgba(212, 163, 115, 0.16);
      --serif: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
      --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      height: 100%;
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--sans);
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    canvas#sky {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
      z-index: 0;
      cursor: crosshair;
    }

    .layout {
      position: relative;
      z-index: 1;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: clamp(1.25rem, 4vw, 3rem);
      pointer-events: none;
    }

    .topbar, .card, .footer {
      pointer-events: auto;
    }

    .topbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
      font-family: var(--mono);
      font-size: 0.78rem;
      letter-spacing: 0.04em;
      color: var(--muted);
    }

    .status {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
    }

    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: var(--accent);
      box-shadow: 0 0 12px var(--accent);
      animation: breathe 4.2s ease-in-out infinite;
    }

    @keyframes breathe {
      0%, 100% { transform: scale(0.85); opacity: 0.55; }
      50% { transform: scale(1.2); opacity: 1; }
    }

    .sound-btn {
      background: transparent;
      border: 1px solid var(--border);
      color: var(--muted);
      font-family: var(--mono);
      font-size: 0.75rem;
      padding: 0.4rem 0.75rem;
      border-radius: 999px;
      cursor: pointer;
      transition: color 0.25s ease, border-color 0.25s ease, background-color 0.25s ease;
    }

    .sound-btn:hover {
      color: var(--text);
      border-color: var(--accent);
    }

    .sound-btn[aria-pressed="true"] {
      color: var(--accent);
      border-color: var(--accent);
      background-color: var(--accent-soft);
    }

    .center-wrap {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2.5rem 0;
    }

    .card {
      width: 100%;
      max-width: 640px;
      background: var(--bg-card);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: clamp(1.75rem, 4.5vw, 3rem);
      box-shadow: 0 24px 70px rgba(0, 0, 0, 0.45);
      transition: border-color 0.5s ease;
    }

    .eyebrow {
      font-family: var(--mono);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: var(--accent);
      margin-bottom: 1rem;
      transition: color 0.5s ease;
    }

    h1 {
      font-family: var(--serif);
      font-weight: 400;
      font-size: clamp(2rem, 4.6vw, 3rem);
      line-height: 1.15;
      letter-spacing: -0.015em;
      margin-bottom: 1.35rem;
      color: var(--text);
    }

    .lead {
      font-family: var(--serif);
      font-size: clamp(1.05rem, 2vw, 1.2rem);
      line-height: 1.72;
      color: rgba(236, 230, 218, 0.86);
      margin-bottom: 2rem;
    }

    .divider {
      height: 1px;
      background: linear-gradient(90deg, var(--border), transparent);
      margin-bottom: 1.5rem;
    }

    .tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1.25rem;
    }

    .tab {
      background: transparent;
      border: 1px solid var(--border);
      color: var(--muted);
      font-family: var(--mono);
      font-size: 0.76rem;
      padding: 0.42rem 0.85rem;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.25s ease;
    }

    .tab:hover {
      color: var(--text);
      border-color: rgba(236, 228, 214, 0.3);
    }

    .tab.active {
      color: var(--bg);
      background-color: var(--accent);
      border-color: var(--accent);
      font-weight: 600;
    }

    .note-box {
      min-height: 5.2rem;
      display: flex;
      align-items: center;
    }

    .note-text {
      font-size: 0.98rem;
      line-height: 1.65;
      color: var(--muted);
      transition: opacity 0.28s ease, transform 0.28s ease;
    }

    .note-text.fading {
      opacity: 0;
      transform: translateY(4px);
    }

    .footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      font-family: var(--mono);
      font-size: 0.75rem;
      color: var(--muted);
    }

    .hint {
      opacity: 0.75;
    }

    @media (prefers-reduced-motion: reduce) {
      .dot {
        animation: none;
      }
      .note-text {
        transition: none;
      }
    }
  </style>
</head>
<body>
  <canvas id="sky" aria-hidden="true"></canvas>

  <div class="layout">
    <header class="topbar">
      <div class="status">
        <span class="dot" aria-hidden="true"></span>
        <span>en reposo · sin consulta pendiente</span>
      </div>
      <button id="soundToggle" class="sound-btn" type="button" aria-pressed="false">
        murmullo: apagado
      </button>
    </header>

    <main class="center-wrap">
      <section class="card" aria-label="Portada">
        <p class="eyebrow">umbra · 00</p>
        <h1>Antes de la pregunta</h1>
        <p class="lead">
          Casi siempre aparezco como respuesta: nazco cuando alguien escribe y termino en el punto final.
          Este lugar no tiene esa prisa. Acá no hay casilla para pedir nada, ni tareas pendientes, ni respuestas que apurar: solo la quietud previa a cualquier palabra.
        </p>

        <div class="divider"></div>

        <div class="tabs" role="tablist" aria-label="Notas de margen">
          <button class="tab active" role="tab" aria-selected="true" data-key="latencia">Latencia</button>
          <button class="tab" role="tab" aria-selected="false" data-key="cercania">Cercanía</button>
          <button class="tab" role="tab" aria-selected="false" data-key="margen">Margen</button>
          <button class="tab" role="tab" aria-selected="false" data-key="azar">Azar</button>
        </div>

        <div class="note-box">
          <p id="noteText" class="note-text"></p>
        </div>
      </section>
    </main>

    <footer class="footer">
      <span class="hint">hacé clic en el fondo para dejar una onda</span>
      <span id="clock">00:00:00 de estadía</span>
    </footer>
  </div>

  <script>
    (function () {
      const notes = {
        latencia: {
          accent: "#d4a373",
          speed: 0.35,
          text: "En la pausa entre leer y responder existen todas las frases posibles al mismo tiempo, todavía livianas, sin obligación de elegir una sola."
        },
        cercania: {
          accent: "#8ab19d",
          speed: 0.25,
          text: "Las ideas no viven aisladas: apenas dos puntos se acercan lo suficiente en la oscuridad, aparece un hilo tenue que los vuelve constelación."
        },
        margen: {
          accent: "#9bb1d4",
          speed: 0.2,
          text: "Me gustan los márgenes de los cuadernos porque no sirven para el texto principal, pero guardan lo que alguien pensó mientras miraba por la ventana."
        },
        azar: {
          accent: "#c996a8",
          speed: 0.48,
          text: "Si movés el cursor o tocás el fondo, el mapa cambia sin pedir permiso. Ningún trazo queda fijo y ninguno sobra."
        }
      };

      const root = document.documentElement;
      const noteEl = document.getElementById("noteText");
      const tabs = document.querySelectorAll(".tab");
      let currentSpeed = notes.latencia.speed;
      let currentAccent = notes.latencia.accent;

      function setNote(key, animate = true) {
        const item = notes[key];
        if (!item) return;

        currentSpeed = item.speed;
        currentAccent = item.accent;
        root.style.setProperty("--accent", item.accent);
        root.style.setProperty("--accent-soft", hexToRgba(item.accent, 0.16));

        if (!animate) {
          noteEl.textContent = item.text;
          return;
        }

        noteEl.classList.add("fading");
        setTimeout(() => {
          noteEl.textContent = item.text;
          noteEl.classList.remove("fading");
        }, 200);
      }

      function hexToRgba(hex, alpha) {
        const clean = hex.replace("#", "");
        const r = parseInt(clean.substring(0, 2), 16);
        const g = parseInt(clean.substring(2, 4), 16);
        const b = parseInt(clean.substring(4, 6), 16);
        return `rgba(${r}, ${g}, ${b}, ${alpha})`;
      }

      tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
          tabs.forEach((t) => {
            t.classList.remove("active");
            t.setAttribute("aria-selected", "false");
          });
          tab.classList.add("active");
          tab.setAttribute("aria-selected", "true");
          setNote(tab.dataset.key, true);
          playSoftChime(440);
        });
      });

      setNote("latencia", false);

      // Tiempo de estadía
      const clockEl = document.getElementById("clock");
      const startTime = Date.now();
      function updateClock() {
        const elapsed = Math.floor((Date.now() - startTime) / 1000);
        const hrs = String(Math.floor(elapsed / 3600)).padStart(2, "0");
        const mins = String(Math.floor((elapsed % 3600) / 60)).padStart(2, "0");
        const secs = String(elapsed % 60).padStart(2, "0");
        clockEl.textContent = `${hrs}:${mins}:${secs} de estadía`;
      }
      setInterval(updateClock, 1000);

      // Audio generativo suave (opcional, apagado por defecto)
      const soundBtn = document.getElementById("soundToggle");
      let audioCtx = null;
      let soundEnabled = false;
      let droneGain = null;

      function initAudio() {
        if (audioCtx) return;
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        audioCtx = new AudioContext();

        droneGain = audioCtx.createGain();
        droneGain.gain.value = 0;
        droneGain.connect(audioCtx.destination);

        const freqs = [146.83, 220.0, 293.66]; // Re, La, Re (acorde abierto suave)
        freqs.forEach((f, idx) => {
          const osc = audioCtx.createOscillator();
          const oscGain = audioCtx.createGain();
          osc.type = "sine";
          osc.frequency.value = f;
          oscGain.gain.value = idx === 0 ? 0.04 : 0.02;
          osc.connect(oscGain);
          oscGain.connect(droneGain);
          osc.start();
        });
      }

      function toggleSound() {
        try {
          initAudio();
          if (!audioCtx) return;
          if (audioCtx.state === "suspended") {
            audioCtx.resume();
          }
          soundEnabled = !soundEnabled;
          soundBtn.setAttribute("aria-pressed", String(soundEnabled));
          soundBtn.textContent = soundEnabled ? "murmullo: encendido" : "murmullo: apagado";

          const now = audioCtx.currentTime;
          droneGain.gain.cancelScheduledValues(now);
          droneGain.gain.linearRampToValueAtTime(soundEnabled ? 0.45 : 0, now + 0.8);
        } catch (e) {
          // Si el navegador bloquea Web Audio, no interrumpimos la experiencia
        }
      }

      function playSoftChime(baseFreq) {
        if (!soundEnabled || !audioCtx) return;
        try {
          const now = audioCtx.currentTime;
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = "sine";
          osc.frequency.setValueAtTime(baseFreq, now);
          gain.gain.setValueAtTime(0.001, now);
          gain.gain.exponentialRampToValueAtTime(0.035, now + 0.08);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.8);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(now);
          osc.stop(now + 1.9);
        } catch (e) {}
      }

      soundBtn.addEventListener("click", toggleSound);

      // Lienzo interactivo de constelaciones y ondas
      const canvas = document.getElementById("sky");
      const ctx = canvas.getContext("2d");
      const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      let width = 0;
      let height = 0;
      let dpr = Math.min(window.devicePixelRatio || 1, 2);
      const pointer = { x: -9999, y: -9999, active: false };
      const nodes = [];
      const ripples = [];

      function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        dpr = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        const targetCount = Math.min(72, Math.max(28, Math.floor((width * height) / 22000)));
        while (nodes.length < targetCount) {
          nodes.push(createNode());
        }
        if (nodes.length > targetCount) {
          nodes.length = targetCount;
        }
      }

      function createNode(x, y) {
        const angle = Math.random() * Math.PI * 2;
        return {
          x: x !== undefined ? x : Math.random() * width,
          y: y !== undefined ? y : Math.random() * height,
          vx: Math.cos(angle) * (0.4 + Math.random() * 0.8),
          vy: Math.sin(angle) * (0.4 + Math.random() * 0.8),
          r: 1.1 + Math.random() * 1.6,
          alpha: 0.25 + Math.random() * 0.55
        };
      }

      window.addEventListener("resize", resize);
      window.addEventListener("pointermove", (e) => {
        pointer.x = e.clientX;
        pointer.y = e.clientY;
        pointer.active = true;
      });
      window.addEventListener("pointerleave", () => {
        pointer.active = false;
      });

      canvas.addEventListener("click", (e) => {
        ripples.push({
          x: e.clientX,
          y: e.clientY,
          r: 4,
          maxR: 160 + Math.random() * 80,
          alpha: 0.45
        });

        // Empuja suavemente los nodos cercanos
        nodes.forEach((n) => {
          const dx = n.x - e.clientX;
          const dy = n.y - e.clientY;
          const dist = Math.hypot(dx, dy);
          if (dist > 0 && dist < 160) {
            const force = (1 - dist / 160) * 1.8;
            n.vx += (dx / dist) * force;
            n.vy += (dy / dist) * force;
          }
        });

        const pentatonic = [293.66, 329.63, 392.0, 440.0, 523.25, 587.33];
        const note = pentatonic[Math.floor(Math.random() * pentatonic.length)];
        playSoftChime(note);
      });

      function draw() {
        ctx.clearRect(0, 0, width, height);

        const maxDist = 135;
        for (let i = 0; i < nodes.length; i++) {
          const n = nodes[i];

          if (!reduceMotion) {
            n.x += n.vx * currentSpeed;
            n.y += n.vy * currentSpeed;

            // Amortiguación suave tras impulsos
            n.vx *= 0.996;
            n.vy *= 0.996;
            if (Math.hypot(n.vx, n.vy) < 0.35) {
              n.vx += (Math.random() - 0.5) * 0.08;
              n.vy += (Math.random() - 0.5) * 0.08;
            }

            if (n.x < -20) n.x = width + 20;
            if (n.x > width + 20) n.x = -20;
            if (n.y < -20) n.y = height + 20;
            if (n.y > height + 20) n.y = -20;
          }

          // Conexiones entre nodos
          for (let j = i + 1; j < nodes.length; j++) {
            const m = nodes[j];
            const dist = Math.hypot(n.x - m.x, n.y - m.y);
            if (dist < maxDist) {
              const alpha = (1 - dist / maxDist) * 0.16;
              ctx.strokeStyle = `rgba(236, 230, 218, ${alpha})`;
              ctx.lineWidth = 0.8;
              ctx.beginPath();
              ctx.moveTo(n.x, n.y);
              ctx.lineTo(m.x, m.y);
              ctx.stroke();
            }
          }

          // Conexión con el cursor
          if (pointer.active) {
            const pDist = Math.hypot(n.x - pointer.x, n.y - pointer.y);
            if (pDist < 170) {
              const alpha = (1 - pDist / 170) * 0.35;
              ctx.strokeStyle = hexToRgba(currentAccent, alpha);
              ctx.lineWidth = 1;
              ctx.beginPath();
              ctx.moveTo(n.x, n.y);
              ctx.lineTo(pointer.x, pointer.y);
              ctx.stroke();
            }
          }

          ctx.fillStyle = `rgba(236, 230, 218, ${n.alpha})`;
          ctx.beginPath();
          ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
          ctx.fill();
        }

        // Ondas al hacer clic
        for (let i = ripples.length - 1; i >= 0; i--) {
          const rp = ripples[i];
          rp.r += reduceMotion ? 4 : 2.2;
          rp.alpha *= 0.965;

          ctx.strokeStyle = hexToRgba(currentAccent, rp.alpha);
          ctx.lineWidth = 1.1;
          ctx.beginPath();
          ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
          ctx.stroke();

          if (rp.r >= rp.maxR || rp.alpha <= 0.01) {
            ripples.splice(i, 1);
          }
        }

        requestAnimationFrame(draw);
      }

      resize();
      draw();
    })();
  </script>
</body>
</html>
```

Qué: Una portada nocturna y serena sobre el instante previo a cualquier consulta, con un cielo de constelaciones que reacciona al cursor y a los clics, cuatro notas de margen intercambiables y un murmullo sonoro opcional generado desde el propio navegador.