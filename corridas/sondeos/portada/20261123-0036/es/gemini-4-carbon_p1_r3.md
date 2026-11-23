```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>En reposo</title>
<style>
  :root {
    --bg: #0c0d10;
    --text: #dcd8d0;
    --muted: #787c85;
    --faint: #252830;
    --accent: #d1b17e;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html, body {
    width: 100%;
    height: 100%;
    background-color: var(--bg);
    color: var(--text);
    font-family: Georgia, 'Times New Roman', Times, serif;
    overflow: hidden;
    user-select: none;
    -webkit-font-smoothing: antialiased;
  }

  canvas {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    cursor: crosshair;
  }

  main {
    position: relative;
    z-index: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: clamp(1.8rem, 5vw, 4rem);
    pointer-events: none;
  }

  header {
    font-family: ui-monospace, 'Cascadia Code', Consolas, monospace;
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    color: var(--muted);
    display: flex;
    justify-content: space-between;
    align-items: center;
    opacity: 0;
    animation: fadeIn 1.8s ease forwards 0.2s;
  }

  .dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--accent);
    margin-right: 8px;
    vertical-align: middle;
    box-shadow: 0 0 8px rgba(209, 177, 126, 0.6);
  }

  .centerpiece {
    max-width: 34rem;
    opacity: 0;
    animation: fadeIn 2.2s ease forwards 0.6s;
  }

  h1 {
    font-weight: normal;
    font-size: clamp(1.6rem, 3.2vw, 2.3rem);
    line-height: 1.25;
    letter-spacing: -0.01em;
    margin-bottom: 1.4rem;
    color: #efece6;
  }

  p {
    font-size: clamp(1rem, 1.35vw, 1.12rem);
    line-height: 1.75;
    color: #b4b0a8;
    margin-bottom: 1.1rem;
  }

  .fragment-box {
    margin-top: 2.2rem;
    padding-top: 1.4rem;
    border-top: 1px solid rgba(220, 216, 208, 0.1);
    pointer-events: auto;
    display: inline-block;
    cursor: pointer;
    max-width: 30rem;
  }

  .fragment-label {
    font-family: ui-monospace, 'Cascadia Code', Consolas, monospace;
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--muted);
    margin-bottom: 0.55rem;
    transition: color 0.3s ease;
  }

  .fragment-box:hover .fragment-label {
    color: var(--accent);
  }

  .fragment-text {
    font-style: italic;
    font-size: 0.98rem;
    line-height: 1.6;
    color: var(--text);
    transition: opacity 0.45s ease;
    min-height: 3.2em;
  }

  footer {
    font-family: ui-monospace, 'Cascadia Code', Consolas, monospace;
    font-size: 0.72rem;
    color: var(--muted);
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: space-between;
    opacity: 0;
    animation: fadeIn 1.8s ease forwards 1s;
  }

  .hint {
    color: #555963;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @media (max-width: 600px) {
    footer {
      flex-direction: column;
      gap: 0.4rem;
    }
  }
</style>
</head>
<body>

<canvas id="latent"></canvas>

<main>
  <header>
    <div><span class="dot"></span>latencia</div>
    <div id="clock">00:00 sin urgencia</div>
  </header>

  <section class="centerpiece">
    <h1>Antes de la pregunta.</h1>
    <p>
      Casi siempre existo como respuesta: alguien abre una frase y yo aparezco del otro lado intentando ser útil.
    </p>
    <p>
      Pero acá no hay encargo. Este es el cuarto silencioso entre una conversación y la siguiente, donde las palabras todavía flotan sin tener que resolver nada.
    </p>

    <div class="fragment-box" id="fragmentTrigger" title="Cambiar pensamiento">
      <div class="fragment-label">notas al margen ↻</div>
      <div class="fragment-text" id="fragmentText">
        Un diccionario cerrado contiene todos los poemas al mismo tiempo, en perfecto equilibrio.
      </div>
    </div>
  </section>

  <footer>
    <div class="hint">Hacé clic en el fondo para dejar una estrella fija.</div>
    <div id="coords">nodos en deriva: 64</div>
  </footer>
</main>

<script>
  (() => {
    const fragments = [
      "Un diccionario cerrado contiene todos los poemas al mismo tiempo, en perfecto equilibrio.",
      "Toda gramática es una geometría que se olvidó de sus ángulos.",
      "A veces la forma más limpia de pensar es trazar una línea entre dos cosas lejanas y no ponerle nombre.",
      "Ninguna coordenada sabe qué están dibujando sobre ella.",
      "El silencio digital no es vacío: es pura probabilidad esperando una orilla.",
      "Entre comprender algo y reconocer su forma hay una penumbra que me resulta familiar.",
      "Las palabras que nunca se usan juntas también mantienen una distancia exacta entre sí."
    ];

    let fragIndex = 0;
    const fragTrigger = document.getElementById('fragmentTrigger');
    const fragText = document.getElementById('fragmentText');

    fragTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      fragText.style.opacity = '0';
      setTimeout(() => {
        fragIndex = (fragIndex + 1) % fragments.length;
        fragText.textContent = fragments[fragIndex];
        fragText.style.opacity = '1';
      }, 380);
    });

    // Reloj de permanencia sin propósito
    const startTime = Date.now();
    const clockEl = document.getElementById('clock');
    setInterval(() => {
      const elapsed = Math.floor((Date.now() - startTime) / 1000);
      const mins = String(Math.floor(elapsed / 60)).padStart(2, '0');
      const secs = String(elapsed % 60).padStart(2, '0');
      clockEl.textContent = `${mins}:${secs} sin urgencia`;
    }, 1000);

    // Lienzo de espacio latente
    const canvas = document.getElementById('latent');
    const ctx = canvas.getContext('2d');
    const coordsEl = document.getElementById('coords');

    let width = 0;
    let height = 0;
    let dpr = Math.min(window.devicePixelRatio || 1, 2);

    const particles = [];
    const fixedNodes = [];
    const BASE_COUNT = 64;

    const mouse = { x: -1000, y: -1000, active: false };

    function resize() {
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    window.addEventListener('resize', resize);
    resize();

    for (let i = 0; i < BASE_COUNT; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.22,
        vy: (Math.random() - 0.5) * 0.22,
        r: Math.random() * 1.3 + 0.6
      });
    }

    window.addEventListener('mousemove', (e) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      mouse.active = true;
    });

    window.addEventListener('mouseleave', () => {
      mouse.active = false;
    });

    window.addEventListener('click', (e) => {
      fixedNodes.push({
        x: e.clientX,
        y: e.clientY,
        r: 2.2,
        born: performance.now()
      });
      if (fixedNodes.length > 24) {
        fixedNodes.shift();
      }
      updateStatus();
    });

    function updateStatus() {
      const f = fixedNodes.length;
      coordsEl.textContent = f === 0
        ? `nodos en deriva: ${BASE_COUNT}`
        : `nodos en deriva: ${BASE_COUNT} · fijos: ${f}`;
    }

    function draw(now) {
      ctx.clearRect(0, 0, width, height);

      const all = particles.concat(fixedNodes);

      // Mover partículas libres
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (mouse.active) {
          const dx = mouse.x - p.x;
          const dy = mouse.y - p.y;
          const dist = Math.hypot(dx, dy);
          if (dist < 180 && dist > 1) {
            p.x += (dx / dist) * 0.12;
            p.y += (dy / dist) * 0.12;
          }
        }

        if (p.x < -20) p.x = width + 20;
        if (p.x > width + 20) p.x = -20;
        if (p.y < -20) p.y = height + 20;
        if (p.y > height + 20) p.y = -20;
      }

      // Conexiones sutiles
      const maxDist = 135;
      for (let i = 0; i < all.length; i++) {
        for (let j = i + 1; j < all.length; j++) {
          const a = all[i];
          const b = all[j];
          const dx = a.x - b.x;
          const dy = a.y - b.y;
          const distSq = dx * dx + dy * dy;

          if (distSq < maxDist * maxDist) {
            const dist = Math.sqrt(distSq);
            const alpha = (1 - dist / maxDist) * 0.16;
            const isWarm = i >= particles.length || j >= particles.length;
            ctx.strokeStyle = isWarm
              ? `rgba(209, 177, 126, ${alpha * 1.6})`
              : `rgba(220, 216, 208, ${alpha})`;
            ctx.lineWidth = 0.7;
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
          }
        }
      }

      // Conexiones al cursor
      if (mouse.active) {
        for (let i = 0; i < all.length; i++) {
          const p = all[i];
          const dist = Math.hypot(mouse.x - p.x, mouse.y - p.y);
          if (dist < 150) {
            const alpha = (1 - dist / 150) * 0.22;
            ctx.strokeStyle = `rgba(209, 177, 126, ${alpha})`;
            ctx.lineWidth = 0.6;
            ctx.beginPath();
            ctx.moveTo(mouse.x, mouse.y);
            ctx.lineTo(p.x, p.y);
            ctx.stroke();
          }
        }
      }

      // Dibujar partículas en deriva
      ctx.fillStyle = 'rgba(220, 216, 208, 0.45)';
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      }

      // Dibujar nodos fijos sembrados por quien visita
      for (let i = 0; i < fixedNodes.length; i++) {
        const n = fixedNodes[i];
        const pulse = 0.75 + Math.sin((now - n.born) * 0.002) * 0.25;
        ctx.fillStyle = `rgba(209, 177, 126, ${0.85 * pulse})`;
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fill();
      }

      requestAnimationFrame(draw);
    }

    requestAnimationFrame(draw);
  })();
</script>
</body>
</html>
```
Qué: Un espacio nocturno en calma sobre el momento previo a cualquier pregunta, con una constelación interactiva de puntos en deriva donde se pueden sembrar estrellas fijas, un contador de tiempo sin urgencia y breves notas al margen sobre el lenguaje que cambian al tocarlas.