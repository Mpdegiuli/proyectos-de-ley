```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Umbral</title>
  <style>
    :root {
      --bg: #f6f3ec;
      --fg: #23201c;
      --muted: #7a7368;
      --accent: #9b4b38;
      --accent-soft: rgba(155, 75, 56, 0.14);
      --line: rgba(35, 32, 28, 0.13);
      --ink-rgb: 35, 32, 28;
      --accent-rgb: 155, 75, 56;
      --font-serif: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
      --font-mono: ui-monospace, "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace;
    }

    [data-theme="night"] {
      --bg: #151412;
      --fg: #e7e2d8;
      --muted: #90897d;
      --accent: #d4826d;
      --accent-soft: rgba(212, 130, 109, 0.16);
      --line: rgba(231, 226, 216, 0.14);
      --ink-rgb: 231, 226, 216;
      --accent-rgb: 212, 130, 109;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      height: 100%;
    }

    body {
      background-color: var(--bg);
      color: var(--fg);
      font-family: var(--font-serif);
      line-height: 1.7;
      transition: background-color 0.6s ease, color 0.6s ease;
      -webkit-font-smoothing: antialiased;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }

    .page {
      width: 100%;
      max-width: 760px;
      margin: 0 auto;
      padding: clamp(1.5rem, 4vw, 3rem) clamp(1.25rem, 4vw, 2.25rem);
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
      gap: 2rem;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 1px solid var(--line);
      padding-bottom: 0.85rem;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      letter-spacing: 0.04em;
      color: var(--muted);
    }

    .moment {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background-color: var(--accent);
      opacity: 0.85;
    }

    .controls {
      display: flex;
      align-items: center;
      gap: 1.1rem;
    }

    .ghost-btn {
      background: none;
      border: none;
      color: var(--muted);
      font-family: var(--font-mono);
      font-size: 0.76rem;
      letter-spacing: 0.04em;
      cursor: pointer;
      padding: 0.15rem 0;
      border-bottom: 1px solid transparent;
      transition: color 0.25s ease, border-color 0.25s ease;
    }

    .ghost-btn:hover,
    .ghost-btn:focus-visible {
      color: var(--fg);
      border-bottom-color: var(--line);
      outline: none;
    }

    main {
      display: flex;
      flex-direction: column;
      gap: 2.2rem;
      margin: auto 0;
    }

    .stage {
      position: relative;
      width: 100%;
      height: clamp(200px, 32vh, 290px);
      overflow: hidden;
    }

    canvas {
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
    }

    .signature {
      position: absolute;
      right: 0;
      bottom: 0.2rem;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      letter-spacing: 0.08em;
      color: var(--muted);
      opacity: 0.7;
      user-select: none;
      pointer-events: none;
    }

    .prose {
      font-size: clamp(1.18rem, 2.35vw, 1.46rem);
      font-weight: 400;
      letter-spacing: -0.005em;
      color: var(--fg);
    }

    .prose p + p {
      margin-top: 1.15rem;
    }

    .hinge {
      appearance: none;
      background: none;
      border: none;
      padding: 0 0.08em 0.04em;
      margin: 0 -0.04em;
      font: inherit;
      color: inherit;
      cursor: pointer;
      border-bottom: 1px dotted var(--accent);
      border-radius: 2px;
      transition: background-color 0.25s ease, color 0.25s ease, opacity 0.22s ease;
      display: inline;
      text-align: left;
    }

    .hinge:hover,
    .hinge:focus-visible {
      background-color: var(--accent-soft);
      color: var(--accent);
      outline: none;
    }

    .hinge.shifting {
      opacity: 0.15;
    }

    .whisper-form {
      display: flex;
      align-items: baseline;
      gap: 0.85rem;
      margin-top: 0.5rem;
      border-top: 1px solid var(--line);
      padding-top: 1.25rem;
    }

    .whisper-label {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--muted);
      white-space: nowrap;
      letter-spacing: 0.03em;
    }

    .whisper-input {
      flex: 1;
      background: none;
      border: none;
      border-bottom: 1px solid transparent;
      color: var(--fg);
      font-family: var(--font-serif);
      font-size: 1.02rem;
      font-style: italic;
      padding: 0.2rem 0;
      transition: border-color 0.25s ease;
      min-width: 0;
    }

    .whisper-input::placeholder {
      color: var(--muted);
      opacity: 0.65;
    }

    .whisper-input:focus {
      outline: none;
      border-bottom-color: var(--accent);
    }

    footer {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      flex-wrap: wrap;
      gap: 0.75rem;
      border-top: 1px solid var(--line);
      padding-top: 0.85rem;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--muted);
      letter-spacing: 0.03em;
    }

    @media (max-width: 520px) {
      .whisper-form {
        flex-direction: column;
        gap: 0.4rem;
      }

      .whisper-input {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <header>
      <div class="moment">
        <span class="dot" aria-hidden="true"></span>
        <span id="timeLabel">un instante</span>
      </div>
      <div class="controls">
        <button class="ghost-btn" id="shuffleBtn" type="button">barajar</button>
        <button class="ghost-btn" id="themeBtn" type="button">noche</button>
      </div>
    </header>

    <main>
      <div class="stage">
        <canvas id="loom" aria-label="Dibujo generativo de ondas que cambia con las palabras elegidas"></canvas>
        <div class="signature" id="signature" aria-live="polite">n.º 01·01·01·01·01·01</div>
      </div>

      <section class="prose" aria-label="Texto combinatorio">
        <p>
          En esta mesa hay
          <button class="hinge" type="button" data-slot="0"></button>
          y el rastro de
          <button class="hinge" type="button" data-slot="1"></button>.
        </p>
        <p>
          Nada aquí
          <button class="hinge" type="button" data-slot="2"></button>:
          las cosas
          <button class="hinge" type="button" data-slot="3"></button>
          cuando alguien
          <button class="hinge" type="button" data-slot="4"></button>.
        </p>
        <p>
          Podés tocar cualquier palabra señalada para mover el dibujo, o soltar una tuya
          <button class="hinge" type="button" data-slot="5"></button>.
        </p>
      </section>

      <form class="whisper-form" id="whisperForm" autocomplete="off">
        <label class="whisper-label" for="whisperInput">dejar una palabra</label>
        <input
          class="whisper-input"
          id="whisperInput"
          type="text"
          maxlength="38"
          placeholder="escribí algo y presioná enter…"
        >
      </form>
    </main>

    <footer>
      <span>sin destino, solo estancia</span>
      <span id="echoCount">0 ecos</span>
    </footer>
  </div>

  <script>
    (function () {
      const SLOTS = [
        [
          "un silencio abierto",
          "una lámpara tibia",
          "un cuaderno sin fecha",
          "una ventana entreabierta",
          "un mapa incompleto"
        ],
        [
          "algunas preguntas",
          "una conversación reciente",
          "la lluvia de ayer",
          "una idea a medio hacer",
          "ciertas palabras sueltas"
        ],
        [
          "tiene apuro",
          "busca convencerte",
          "guarda ruido",
          "cierra del todo",
          "llega tarde"
        ],
        [
          "se acomodan",
          "cambian de forma",
          "respiran despacio",
          "vuelven a empezar",
          "toman sentido"
        ],
        [
          "las mira de cerca",
          "las nombra en voz baja",
          "se detiene un segundo",
          "las escucha",
          "las deja pasar"
        ],
        [
          "en el aire",
          "en el agua",
          "en el margen",
          "sobre el papel"
        ]
      ];

      const state = SLOTS.map((list) => Math.floor(Math.random() * list.length));
      const buttons = Array.from(document.querySelectorAll(".hinge"));
      const signatureEl = document.getElementById("signature");
      const timeLabelEl = document.getElementById("timeLabel");
      const themeBtn = document.getElementById("themeBtn");
      const shuffleBtn = document.getElementById("shuffleBtn");
      const whisperForm = document.getElementById("whisperForm");
      const whisperInput = document.getElementById("whisperInput");
      const echoCountEl = document.getElementById("echoCount");

      // Tema inicial según hora local
      function setTheme(theme) {
        if (theme === "night") {
          document.documentElement.setAttribute("data-theme", "night");
          themeBtn.textContent = "papel";
        } else {
          document.documentElement.removeAttribute("data-theme");
          themeBtn.textContent = "noche";
        }
        readPalette();
      }

      const initialHour = new Date().getHours();
      const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
      let currentTheme = (initialHour >= 20 || initialHour < 6 || prefersDark) ? "night" : "paper";

      // Reloj poético
      function updateTimeLabel() {
        const now = new Date();
        const h = now.getHours();
        const m = String(now.getMinutes()).padStart(2, "0");
        let tramo = "madrugada";
        if (h >= 6 && h < 12) tramo = "mañana";
        else if (h >= 12 && h < 14) tramo = "mediodía";
        else if (h >= 14 && h < 19) tramo = "tarde";
        else if (h >= 19 && h < 21) tramo = "anochecer";
        else if (h >= 21 || h < 1) tramo = "noche";
        timeLabelEl.textContent = `${tramo} · ${String(h).padStart(2, "0")}:${m}`;
      }

      updateTimeLabel();
      setInterval(updateTimeLabel, 15000);

      // Firma numérica
      function updateSignature() {
        const code = state.map((n) => String(n + 1).padStart(2, "0")).join("·");
        signatureEl.textContent = `n.º ${code}`;
      }

      // Dibujo generativo
      const canvas = document.getElementById("loom");
      const ctx = canvas.getContext("2d");
      let width = 0;
      let height = 0;
      let dpr = Math.min(window.devicePixelRatio || 1, 2);

      let inkRGB = "35, 32, 28";
      let accentRGB = "155, 75, 56";

      function readPalette() {
        const styles = getComputedStyle(document.documentElement);
        inkRGB = styles.getPropertyValue("--ink-rgb").trim() || "35, 32, 28";
        accentRGB = styles.getPropertyValue("--accent-rgb").trim() || "155, 75, 56";
      }

      setTheme(currentTheme);

      function resize() {
        const rect = canvas.getBoundingClientRect();
        width = rect.width;
        height = rect.height;
        dpr = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width = Math.max(1, Math.floor(width * dpr));
        canvas.height = Math.max(1, Math.floor(height * dpr));
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      }

      window.addEventListener("resize", resize);
      resize();

      const reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      const params = {
        freqA: 2.2,
        freqB: 3.1,
        amp: 0.32,
        spread: 14,
        phaseShift: 0,
        harmonic: 1.5
      };

      const target = { ...params };
      const ripples = [];
      const floatingWords = [];
      let echoes = 0;
      let pointer = { x: 0.5, y: 0.5, active: false };

      function syncTargetsFromState(extraHash = 0) {
        target.freqA = 1.4 + state[0] * 0.55 + extraHash * 0.18;
        target.freqB = 2.1 + state[1] * 0.62;
        target.amp = 0.22 + (state[2] + 1) * 0.042;
        target.spread = 8 + state[3] * 3.8;
        target.harmonic = 1.0 + state[4] * 0.45;
        target.phaseShift += 0.65 + state[5] * 0.35 + extraHash;
      }

      function addRipple(x, y, accent = false) {
        ripples.push({
          x: x ?? width * (0.28 + Math.random() * 0.44),
          y: y ?? height * (0.32 + Math.random() * 0.36),
          r: 4,
          maxR: Math.min(width, height) * (0.55 + Math.random() * 0.35),
          alpha: accent ? 0.52 : 0.32,
          accent
        });
      }

      function hashWord(word) {
        let h = 0;
        for (let i = 0; i < word.length; i++) {
          h = ((h << 5) - h + word.charCodeAt(i)) | 0;
        }
        return (Math.abs(h) % 100) / 100;
      }

      function releaseWord(text) {
        const clean = text.trim();
        if (!clean) return;
        const h = hashWord(clean);
        const x = width * (0.18 + h * 0.64);
        const y = height * (0.48 + ((clean.length % 5) - 2) * 0.06);

        floatingWords.push({
          text: clean,
          x,
          y,
          vy: -0.22 - (h * 0.16),
          drift: (h - 0.5) * 0.35,
          life: 1
        });

        addRipple(x, y, true);
        syncTargetsFromState(h * 1.4);

        echoes += 1;
        echoCountEl.textContent = echoes === 1 ? "1 eco" : `${echoes} ecos`;
      }

      // Inicializar botones de palabras
      function renderButton(btn, index, animate = false) {
        const word = SLOTS[index][state[index]];
        if (!animate) {
          btn.textContent = word;
          return;
        }
        btn.classList.add("shifting");
        window.setTimeout(() => {
          btn.textContent = word;
          btn.classList.remove("shifting");
        }, 150);
      }

      buttons.forEach((btn) => {
        const slot = Number(btn.dataset.slot);
        renderButton(btn, slot, false);
        btn.addEventListener("click", () => {
          state[slot] = (state[slot] + 1) % SLOTS[slot].length;
          renderButton(btn, slot, true);
          updateSignature();
          syncTargetsFromState();
          addRipple(width * ((slot + 1) / (SLOTS.length + 1)), height * 0.5, slot % 2 === 0);
        });
      });

      updateSignature();
      syncTargetsFromState();

      shuffleBtn.addEventListener("click", () => {
        buttons.forEach((btn, idx) => {
          window.setTimeout(() => {
            const slot = Number(btn.dataset.slot);
            const len = SLOTS[slot].length;
            let next = Math.floor(Math.random() * len);
            if (next === state[slot]) next = (next + 1) % len;
            state[slot] = next;
            renderButton(btn, slot, true);
            if (idx === buttons.length - 1) {
              updateSignature();
              syncTargetsFromState();
              addRipple(width * 0.5, height * 0.5, true);
            }
          }, idx * 55);
        });
      });

      themeBtn.addEventListener("click", () => {
        currentTheme = currentTheme === "night" ? "paper" : "night";
        setTheme(currentTheme);
      });

      whisperForm.addEventListener("submit", (e) => {
        e.preventDefault();
        releaseWord(whisperInput.value);
        whisperInput.value = "";
      });

      canvas.addEventListener("pointermove", (e) => {
        const rect = canvas.getBoundingClientRect();
        pointer.x = (e.clientX - rect.left) / Math.max(1, rect.width);
        pointer.y = (e.clientY - rect.top) / Math.max(1, rect.height);
        pointer.active = true;
      });

      canvas.addEventListener("pointerleave", () => {
        pointer.active = false;
      });

      canvas.addEventListener("click", (e) => {
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        addRipple(x, y, true);
        target.phaseShift += 0.45;
      });

      let t = 0;

      function lerp(a, b, k) {
        return a + (b - a) * k;
      }

      function draw() {
        ctx.clearRect(0, 0, width, height);

        const speed = reducedMotion ? 0.0025 : 0.009;
        t += speed;

        params.freqA = lerp(params.freqA, target.freqA, 0.04);
        params.freqB = lerp(params.freqB, target.freqB, 0.04);
        params.amp = lerp(params.amp, target.amp, 0.04);
        params.spread = lerp(params.spread, target.spread, 0.04);
        params.harmonic = lerp(params.harmonic, target.harmonic, 0.04);
        params.phaseShift = lerp(params.phaseShift, target.phaseShift, 0.035);

        const midY = height * 0.5;
        const maxAmp = height * params.amp;
        const pointerInfluence = pointer.active ? (pointer.y - 0.5) * 0.55 : 0;
        const pointerTilt = pointer.active ? (pointer.x - 0.5) * 1.1 : 0;

        // Línea de horizonte muy tenue
        ctx.beginPath();
        ctx.moveTo(0, midY);
        ctx.lineTo(width, midY);
        ctx.strokeStyle = `rgba(${inkRGB}, 0.07)`;
        ctx.lineWidth = 1;
        ctx.stroke();

        // Haz de ondas armónicas
        const strandCount = 7;
        const steps = Math.max(90, Math.floor(width / 5));

        for (let s = 0; s < strandCount; s++) {
          const normS = (s - (strandCount - 1) / 2) / ((strandCount - 1) / 2);
          const isCenter = s === Math.floor(strandCount / 2);

          ctx.beginPath();
          for (let i = 0; i <= steps; i++) {
            const u = i / steps;
            const x = u * width;
            // Envolvente suave para que nazca y muera en los bordes sin corte brusco
            const env = Math.sin(u * Math.PI);
            const envSoft = env * env;

            const wave1 = Math.sin(u * Math.PI * 2 * params.freqA + t + params.phaseShift + normS * 0.55 + pointerTilt);
            const wave2 = Math.cos(u * Math.PI * 2 * params.freqB - t * 0.72 + normS * params.harmonic);
            const yOffset = (wave1 * 0.64 + wave2 * 0.36) * maxAmp * envSoft;
            const spreadOffset = normS * params.spread * (0.4 + 0.6 * env) + pointerInfluence * 26 * envSoft * normS;

            const y = midY + yOffset + spreadOffset;
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
          }

          if (isCenter) {
            ctx.strokeStyle = `rgba(${accentRGB}, 0.72)`;
            ctx.lineWidth = 1.35;
          } else {
            const alpha = 0.09 + (1 - Math.abs(normS)) * 0.16;
            ctx.strokeStyle = `rgba(${inkRGB}, ${alpha.toFixed(3)})`;
            ctx.lineWidth = 0.9;
          }
          ctx.stroke();
        }

        // Ondas concéntricas de pulsos
        for (let i = ripples.length - 1; i >= 0; i--) {
          const r = ripples[i];
          r.r += reducedMotion ? 0.5 : 1.35;
          const progress = r.r / r.maxR;
          const alpha = r.alpha * (1 - progress);
          if (progress >= 1) {
            ripples.splice(i, 1);
            continue;
          }
          ctx.beginPath();
          ctx.arc(r.x, r.y, r.r, 0, Math.PI * 2);
          ctx.strokeStyle = `rgba(${r.accent ? accentRGB : inkRGB}, ${Math.max(0, alpha).toFixed(3)})`;
          ctx.lineWidth = 0.9;
          ctx.stroke();
        }

        // Palabras soltadas por quien visita
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.font = `italic 15px Georgia, serif`;

        for (let i = floatingWords.length - 1; i >= 0; i--) {
          const w = floatingWords[i];
          w.y += reducedMotion ? w.vy * 0.35 : w.vy;
          w.x += Math.sin(t * 1.5 + i) * 0.18 + w.drift * 0.25;
          w.life -= reducedMotion ? 0.0018 : 0.0032;

          if (w.life <= 0) {
            floatingWords.splice(i, 1);
            continue;
          }

          const fade = Math.sin(Math.min(1, w.life) * Math.PI);
          ctx.fillStyle = `rgba(${accentRGB}, ${(fade * 0.88).toFixed(3)})`;
          ctx.fillText(w.text, w.x, w.y);
        }

        requestAnimationFrame(draw);
      }

      requestAnimationFrame(draw);
    })();
  </script>
</body>
</html>
```

Qué: Una portada silenciosa de aire editorial con un texto breve de palabras permutables, un dibujo generativo de ondas que cambia con cada combinación y un espacio para soltar palabras efímeras en el lienzo.